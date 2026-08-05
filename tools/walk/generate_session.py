#!/usr/bin/env python3
"""
Walk Mode — static session generator.

Writes the session MP3 and updates static/walk/manifest.json.
Keeps a rolling window of --keep-sessions sessions; older MP3s are pruned.

Usage (from repo root):
    python tools/walk/generate_session.py
    python tools/walk/generate_session.py --date 2026-07-27
    python tools/walk/generate_session.py --force
    python tools/walk/generate_session.py --keep-sessions 14

Output:
    static/walk/audio/{session_id}.mp3
    static/walk/manifest.json          (updated in place)
    tools/walk/data/walk_srs.json      (updated SRS state)

Set WALK_TTS_PROVIDER=edge_tts (default) and WALK_TTS_VOICE_* if needed.
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

# Allow importing sibling modules regardless of cwd
TOOLS_WALK = Path(__file__).resolve().parent
REPO_ROOT  = TOOLS_WALK.parent.parent
sys.path.insert(0, str(TOOLS_WALK))

from walk_content import get_session_scene, mark_session_seen
from walk_audio   import build_session

STATIC_WALK  = REPO_ROOT / "static" / "walk"
MANIFEST_PATH = STATIC_WALK / "manifest.json"
AUDIO_DIR     = STATIC_WALK / "audio"


def _load_manifest() -> list[dict]:
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, encoding="utf-8") as f:
            return json.load(f)
    return []


def _save_manifest(sessions: list[dict]) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(sessions, f, ensure_ascii=False, indent=2)


def _prune(sessions: list[dict], keep: int) -> list[dict]:
    """Remove entries beyond the rolling window and delete their audio files."""
    to_keep  = sessions[:keep]
    to_prune = sessions[keep:]
    for entry in to_prune:
        audio_file = AUDIO_DIR / Path(entry["audio_url"]).name
        if audio_file.exists():
            audio_file.unlink()
            print(f"  Pruned: {audio_file.name}")
    return to_keep


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a Walk Mode session.")
    parser.add_argument("--date", default=date.today().isoformat(),
                        help="Session date YYYY-MM-DD (default: today)")
    parser.add_argument("--n", type=int, default=15,
                        help="Max beats per scene (default: 15)")
    parser.add_argument("--keep-sessions", type=int, default=30,
                        help="Rolling window size (default: 30)")
    parser.add_argument("--force", action="store_true",
                        help="Regenerate even if session already exists")
    args = parser.parse_args()

    session_id  = args.date
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    mp3_path    = AUDIO_DIR / f"{session_id}.mp3"

    sessions = _load_manifest()

    if any(s["session_id"] == session_id for s in sessions) and not args.force:
        print(f"Session {session_id} already in manifest. Use --force to regenerate.")
        return

    print(f"Generating Walk Mode session: {session_id}")

    scene = get_session_scene(max_beats=args.n)

    print(f"  Scene: {scene['scene_id']}  ({len(scene['beats'])} beats)")
    for b in scene["beats"]:
        print(f"    [{b['srs_id']}] {b['english_cue']}")

    print("\n  Synthesising audio…")
    manifest_entry = build_session(scene, session_id, mp3_path)

    # Update rolling manifest (remove any existing entry for this date first)
    sessions = [s for s in sessions if s["session_id"] != session_id]
    sessions = [manifest_entry] + sessions          # newest first
    sessions = _prune(sessions, args.keep_sessions)
    _save_manifest(sessions)

    mark_session_seen([b["srs_id"] for b in scene["beats"]])

    mins, secs = divmod(manifest_entry["duration_seconds"], 60)
    print(f"\n✓ Done.")
    print(f"  MP3:      {mp3_path}")
    print(f"  Duration: {mins}m {secs}s  |  {manifest_entry['beat_count']} beats")
    print(f"  Manifest: {MANIFEST_PATH}  ({len(sessions)} sessions total)")


if __name__ == "__main__":
    main()
