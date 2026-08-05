"""
Walk Mode — Audio Service (canonical)

TTS provider interface and session stitcher.

Provider selected via WALK_TTS_PROVIDER env var (default: edge_tts).
Clips cached by sha256(ClassName|voice_or_lang|role|text) in audio_cache/walk/.
Switching provider or voice config causes a clean re-synthesise.

Three roles:
  narrator   — EN scene_intro, context lines, cues
  answer     — JP target phrase (what the learner says)
  character  — JP other-person dialogue (stimulus)

Edge-TTS voice defaults (overridable via env):
  WALK_TTS_VOICE_NARRATOR   en-GB-SoniaNeural
  WALK_TTS_VOICE_CHARACTER  ja-JP-NanamiNeural  (other person — always Nanami)
  WALK_TTS_VOICE_ANSWER     ja-JP-KeitaNeural   (correct answer to shadow — always Keita)

Beat stitch order:
  [context EN] → [character JP, if present] → 500ms
  → [EN cue] → [GAP] → [JP answer] → 600ms → [JP answer slow] → [GAP] → 1000ms

GAP = max(2500ms, jp_duration × 1.4).
Slow repeat uses ANSWER_SLOW_RATE (default -20%) via edge-tts rate param.
"""

from __future__ import annotations

import asyncio
import hashlib
import io
import os
import time
from abc import ABC, abstractmethod
from pathlib import Path

from pydub import AudioSegment

# tools/walk/ → tools/ → repo root
BASE_DIR = Path(__file__).parent
CACHE_DIR = BASE_DIR.parent.parent / "audio_cache" / "walk"

PRACTICE_GAP_RATIO  = 1.4
PRACTICE_GAP_MIN_MS = 2500
CHAR_PAUSE_MS       = 500
CONTEXT_PAUSE_MS    = 400
INTER_BEAT_GAP_MS   = 1000
INTRO_PAUSE_MS      = 1000

ANSWER_SLOW_RATE    = "-35%"   # edge-tts rate for the slow repeat
SLOW_REPEAT_GAP_MS  = 600      # pause between normal and slow delivery


def _ensure_dirs() -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# TTS Provider interface
# ---------------------------------------------------------------------------

class TTSProvider(ABC):

    def _cache_key(self, text: str, lang: str, role: str) -> str:
        raw = f"{self.__class__.__name__}|{lang}|{role}|{text}"
        return hashlib.sha256(raw.encode()).hexdigest()

    @abstractmethod
    def synthesise(self, text: str, lang: str, role: str = "answer") -> AudioSegment:
        """Synthesise and return an AudioSegment. role: narrator|answer|character."""

    def get_or_synthesise(self, text: str, lang: str, role: str = "answer") -> AudioSegment:
        _ensure_dirs()
        key = self._cache_key(text, lang, role)
        path = CACHE_DIR / f"{key}.mp3"
        if path.exists():
            return AudioSegment.from_mp3(path)
        audio = self.synthesise(text, lang, role)
        audio.export(str(path), format="mp3")
        return audio

    def prefetch_batch(self, clips: list[tuple[str, str, str]]) -> None:
        """Pre-synthesise clips. Override in async providers for parallel fetch."""


class EdgeTTSProvider(TTSProvider):
    """
    Microsoft Edge TTS — free, no account needed.
    pip install edge-tts

    Uses asyncio.gather to synthesise all uncached clips in parallel,
    then the stitch loop only does cache reads (no per-clip blocking).
    """

    _VOICE_ENV = {
        "narrator":     ("WALK_TTS_VOICE_NARRATOR",  "en-GB-SoniaNeural"),
        "character":    ("WALK_TTS_VOICE_CHARACTER",  "ja-JP-NanamiNeural"),
        "answer":       ("WALK_TTS_VOICE_ANSWER",     "ja-JP-KeitaNeural"),
        "answer_slow":  ("WALK_TTS_VOICE_ANSWER",     "ja-JP-KeitaNeural"),  # same voice, slow rate
    }

    def _voice_for_role(self, role: str) -> str:
        env_key, default = self._VOICE_ENV.get(role, self._VOICE_ENV["answer"])
        return os.environ.get(env_key, default)

    @staticmethod
    def _rate_for_role(role: str) -> str:
        return ANSWER_SLOW_RATE if role == "answer_slow" else "+0%"

    def _cache_key(self, text: str, lang: str, role: str) -> str:
        voice = self._voice_for_role(role)
        rate  = self._rate_for_role(role)
        raw = f"EdgeTTSProvider|{voice}|{rate}|{text}"
        return hashlib.sha256(raw.encode()).hexdigest()

    @staticmethod
    async def _async_save(text: str, voice: str, path: Path, rate: str = "+0%") -> None:
        import edge_tts
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        await communicate.save(str(path))

    def synthesise(self, text: str, lang: str, role: str = "answer") -> AudioSegment:
        """Single-clip synthesis. prefetch_batch() is faster for many clips."""
        _ensure_dirs()
        voice = self._voice_for_role(role)
        rate  = self._rate_for_role(role)
        key   = self._cache_key(text, lang, role)
        path  = CACHE_DIR / f"{key}.mp3"
        asyncio.run(self._async_save(text, voice, path, rate))
        return AudioSegment.from_mp3(path)

    def prefetch_batch(self, clips: list[tuple[str, str, str]]) -> None:
        """Synthesise all uncached clips concurrently."""
        _ensure_dirs()
        to_fetch: list[tuple[str, str, str, Path]] = []
        for text, lang, role in clips:
            key  = self._cache_key(text, lang, role)
            path = CACHE_DIR / f"{key}.mp3"
            if not path.exists():
                to_fetch.append((text, self._voice_for_role(role), self._rate_for_role(role), path))

        cached = len(clips) - len(to_fetch)
        if not to_fetch:
            print(f"  All {len(clips)} clips already cached.")
            return

        print(f"  Synthesising {len(to_fetch)} clips in parallel ({cached} cached)…")

        async def _run() -> None:
            await asyncio.gather(*[
                self._async_save(text, voice, path, rate)
                for text, voice, rate, path in to_fetch
            ])

        asyncio.run(_run())


class GTTSProvider(TTSProvider):
    """Free Google TTS via gTTS. pip install gtts. Both JP roles use the same voice."""

    def synthesise(self, text: str, lang: str, role: str = "answer") -> AudioSegment:
        from gtts import gTTS
        tts = gTTS(text=text, lang=lang, slow=False)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        time.sleep(0.3)
        return AudioSegment.from_mp3(buf)


class GoogleCloudTTSProvider(TTSProvider):
    """Google Cloud TTS neural voices. Set GOOGLE_APPLICATION_CREDENTIALS."""

    def __init__(self) -> None:
        self.voice_jp_answer = os.environ.get("WALK_TTS_VOICE_ANSWER", "ja-JP-Neural2-B")
        self.voice_jp_char   = os.environ.get("WALK_TTS_VOICE_CHARACTER", "ja-JP-Neural2-C")
        self.voice_en        = os.environ.get("WALK_TTS_VOICE_NARRATOR", "en-US-Neural2-C")

    def synthesise(self, text: str, lang: str, role: str = "answer") -> AudioSegment:
        from google.cloud import texttospeech
        client = texttospeech.TextToSpeechClient()
        if lang == "ja":
            voice_name = self.voice_jp_char if role == "character" else self.voice_jp_answer
            lang_code = "ja-JP"
        else:
            voice_name = self.voice_en
            lang_code = "en-US"
        response = client.synthesize_speech(
            input=texttospeech.SynthesisInput(text=text),
            voice=texttospeech.VoiceSelectionParams(language_code=lang_code, name=voice_name),
            audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3),
        )
        return AudioSegment.from_mp3(io.BytesIO(response.audio_content))


class AzureTTSProvider(TTSProvider):
    """Azure Cognitive Services TTS. Set AZURE_TTS_KEY and AZURE_TTS_REGION."""

    def __init__(self) -> None:
        self.key             = os.environ["AZURE_TTS_KEY"]
        self.region          = os.environ["AZURE_TTS_REGION"]
        self.voice_jp_answer = os.environ.get("WALK_TTS_VOICE_ANSWER", "ja-JP-NanamiNeural")
        self.voice_jp_char   = os.environ.get("WALK_TTS_VOICE_CHARACTER", "ja-JP-KeitaNeural")
        self.voice_en        = os.environ.get("WALK_TTS_VOICE_NARRATOR", "en-US-JennyNeural")

    def synthesise(self, text: str, lang: str, role: str = "answer") -> AudioSegment:
        import azure.cognitiveservices.speech as speechsdk
        voice = (self.voice_jp_char if role == "character" else self.voice_jp_answer) \
                if lang == "ja" else self.voice_en
        config = speechsdk.SpeechConfig(subscription=self.key, region=self.region)
        config.speech_synthesis_voice_name = voice
        synth = speechsdk.SpeechSynthesizer(speech_config=config, audio_config=None)
        result = synth.speak_text_async(text).get()
        return AudioSegment.from_mp3(io.BytesIO(result.audio_data))


def get_provider() -> TTSProvider:
    name = os.environ.get("WALK_TTS_PROVIDER", "edge_tts").lower()
    if name == "google_cloud":
        return GoogleCloudTTSProvider()
    if name == "azure":
        return AzureTTSProvider()
    if name == "gtts":
        return GTTSProvider()
    return EdgeTTSProvider()


# ---------------------------------------------------------------------------
# Session stitcher
# ---------------------------------------------------------------------------

def _silence(ms: int) -> AudioSegment:
    return AudioSegment.silent(duration=ms)


def _bell(hz: int, duration_ms: int = 600, decay_rate: float = 6.0) -> AudioSegment:
    """
    Bell tone: exponential decay + inharmonic partials + striker click.
    Sounds like a triangle or chime. No external files needed — only numpy.
    """
    import numpy as np
    sr  = 44100
    pad = 400  # tail so the note fades naturally rather than hard-cutting
    n   = int(sr * (duration_ms + pad) / 1000)
    t   = np.linspace(0, (duration_ms + pad) / 1000, n, endpoint=False)
    env = np.exp(-decay_rate * t)

    # Inharmonic partials based on Helmholtz bell acoustics
    sig = (
        1.00 * np.sin(2 * np.pi * hz * 1.000 * t) +
        0.50 * np.sin(2 * np.pi * hz * 2.000 * t) +
        0.28 * np.sin(2 * np.pi * hz * 2.756 * t) +
        0.18 * np.sin(2 * np.pi * hz * 3.000 * t) +
        0.10 * np.sin(2 * np.pi * hz * 4.069 * t)
    ) * env

    # 4 ms noise burst at attack — simulates the striker/mallet click
    rng       = np.random.default_rng(0)
    click_len = min(int(sr * 0.004), n)
    sig[:click_len] += rng.normal(0, 0.12, click_len) * np.exp(-500 * t[:click_len])

    peak = np.max(np.abs(sig))
    if peak > 0:
        sig = sig / peak * 0.42
    samples = (sig * 32767).astype(np.int16)
    seg = AudioSegment(samples.tobytes(), frame_rate=sr, sample_width=2, channels=1)
    return seg[:duration_ms]


def _make_intro_jingle() -> AudioSegment:
    """Ascending two-note bell chime: E5 → A5."""
    return _bell(659, 420, decay_rate=7.0) + _silence(30) + _bell(880, 580, decay_rate=5.5)


def _make_outro_jingle() -> AudioSegment:
    """Descending two-note bell chime: A5 → E5, longer resonance."""
    return _bell(880, 320, decay_rate=8.0) + _silence(20) + _bell(659, 720, decay_rate=4.5)


def build_session(scene: dict, session_id: str, mp3_path: Path) -> dict:
    """
    Stitch a scene into a single MP3 at mp3_path.
    Returns the manifest dict for this session.

    Collects all clips → calls provider.prefetch_batch() for parallel
    synthesis → then stitches from cache (no per-clip blocking in loop).
    """
    _ensure_dirs()
    mp3_path.parent.mkdir(parents=True, exist_ok=True)
    provider = get_provider()

    # --- Collect all clips for batch pre-synthesis ---
    all_clips: list[tuple[str, str, str]] = [
        ("Japanese Unlocked", "en", "narrator"),
        (scene["scene_intro"], "en", "narrator"),
    ]
    for beat in scene["beats"]:
        all_clips.append((beat["context_line"], "en", "narrator"))
        char_jp = beat.get("character_japanese", "").strip()
        if char_jp:
            all_clips.append((char_jp, "ja", "character"))
        all_clips.append((beat["english_cue"], "en", "narrator"))
        all_clips.append((beat["japanese_answer"], "ja", "answer"))
        all_clips.append((beat["japanese_answer"], "ja", "answer_slow"))

    provider.prefetch_batch(all_clips)

    # --- Stitch ---
    beat_timings: list[dict] = []

    # Intro jingle + brand name
    brand = provider.get_or_synthesise("Japanese Unlocked", "en", "narrator")
    track = _make_intro_jingle() + _silence(220) + brand + _silence(600)
    track += provider.get_or_synthesise(scene["scene_intro"], "en", "narrator")
    track += _silence(INTRO_PAUSE_MS)

    for i, beat in enumerate(scene["beats"]):
        beat_start_ms = len(track)

        track += provider.get_or_synthesise(beat["context_line"], "en", "narrator")

        char_jp = beat.get("character_japanese", "").strip()
        if char_jp:
            track += provider.get_or_synthesise(char_jp, "ja", "character")
            track += _silence(CHAR_PAUSE_MS)
        else:
            track += _silence(CONTEXT_PAUSE_MS)

        track += provider.get_or_synthesise(beat["english_cue"], "en", "narrator")

        jp_audio = provider.get_or_synthesise(beat["japanese_answer"], "ja", "answer")
        jp_slow  = provider.get_or_synthesise(beat["japanese_answer"], "ja", "answer_slow")
        gap_ms   = max(PRACTICE_GAP_MIN_MS, int(len(jp_audio) * PRACTICE_GAP_RATIO))
        track += _silence(gap_ms)          # gap: learner speaks
        track += jp_audio                  # answer at natural speed
        track += _silence(SLOW_REPEAT_GAP_MS)
        track += jp_slow                   # answer again, slower — shadow this one
        track += _silence(gap_ms)
        track += _silence(INTER_BEAT_GAP_MS)

        beat_timings.append({
            "beat": i + 1,
            "srs_id": beat["srs_id"],
            "start_ms": beat_start_ms,
            "context_line": beat["context_line"],
            "character_japanese": char_jp,
            "english_cue": beat["english_cue"],
            "japanese_answer": beat["japanese_answer"],
            "romaji": beat.get("romaji", ""),
            "grammar_tag": beat.get("grammar_tag", ""),
        })

    # Outro jingle
    track += _silence(400)
    track += _make_outro_jingle()
    track += _silence(300)

    track.export(str(mp3_path), format="mp3", bitrate="128k")

    return {
        "session_id":       session_id,
        "scene_id":         scene["scene_id"],
        "title":            scene["scene_id"].replace("_", " ").title(),
        "scene_intro":      scene["scene_intro"],
        "other_character":  scene.get("other_character", ""),
        "unit_count":       len(scene["beats"]),
        "beat_count":       len(scene["beats"]),
        "duration_seconds": round(len(track) / 1000),
        "audio_url":        f"audio/{session_id}.mp3",
        "beats":            beat_timings,
    }
