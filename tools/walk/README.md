# Walk Mode — generation tools

Hands-free Japanese speaking trainer. Each session is a pre-generated MP3 paired with a JSON manifest. The player at `/walk/` is a static page; no server required in production.

---

## Quick start (local)

```bash
# From repo root
pip install edge-tts pydub
brew install ffmpeg          # one-time

python tools/walk/generate_session.py
```

Output lands in `static/walk/audio/` and `static/walk/manifest.json`. Open `static/walk/index.html` in a browser, or run `hugo server` and visit `/walk/`.

### Options

```
--date YYYY-MM-DD   Session date (default: today)
--n N               Max beats from scene (default: 15)
--keep-sessions N   Rolling window size (default: 30)
--force             Regenerate even if date already exists
```

---

## TTS provider

Default is `edge_tts` — free, no account needed.

| Env var | Default | Notes |
|---|---|---|
| `WALK_TTS_PROVIDER` | `edge_tts` | Also: `gtts`, `google_cloud`, `azure` |
| `WALK_TTS_VOICE_NARRATOR` | `en-GB-SoniaNeural` | English narration |
| `WALK_TTS_VOICE_ANSWER` | `ja-JP-NanamiNeural` | JP answer (female) |
| `WALK_TTS_VOICE_CHARACTER` | `ja-JP-KeitaNeural` | JP character (male) |

Clips are cached in `audio_cache/walk/` (gitignored). Changing a voice env var triggers clean re-synthesis on next run.

---

## GitHub Actions — daily auto-generation

The workflow at `.github/workflows/walk_session.yml` runs at 6 AM UTC every day:

1. Installs Python 3.11, ffmpeg, edge-tts, pydub
2. Runs `generate_session.py` (edge-tts, no secrets needed)
3. Commits changed files (`static/walk/`, `tools/walk/data/walk_srs.json`)
4. The push triggers the existing Hugo deploy workflow → site redeploys with new session

Trigger manually from the **Actions** tab → **Generate Walk Session** → **Run workflow**.

### SRS state

`tools/walk/data/walk_srs.json` is committed to the repo. GitHub Actions reads and updates it so spaced-repetition state persists across runs. Do not gitignore it.

---

## Switching audio to Cloudflare R2 (future)

When ready: add a `--upload` flag to `generate_session.py` that uploads each new MP3 to R2 and writes the bucket URL into `audio_url` in the manifest. The player and the rest of the pipeline need no changes — they already read `audio_url` from the manifest.

---

## Scene data

`tools/walk/data/walk_scenarios.json` is the canonical source for all scenes and beats. Edit here; do not edit the copy in `Japp/web_version/data/`.
