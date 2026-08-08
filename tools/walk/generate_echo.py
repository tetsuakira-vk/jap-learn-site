#!/usr/bin/env python3
"""
Echo 影 — generate audio for all scenarios and write redesign/echo/scenes.json.

Same pipeline as generate_all_scenes.py but outputs to redesign/echo/ so the
redesign preview server can serve the audio at /echo/audio/.

Usage:
    python tools/walk/generate_echo.py
    python tools/walk/generate_echo.py --force
    python tools/walk/generate_echo.py --scene konbini_visit
"""

import argparse
import json
import sys
from pathlib import Path

BASE_DIR  = Path(__file__).parent        # tools/walk/
REPO_ROOT = BASE_DIR.parent.parent       # repo root
ECHO_DIR  = REPO_ROOT / "redesign" / "echo"

sys.path.insert(0, str(BASE_DIR))
from walk_audio import build_session


def load_scenarios() -> list[dict]:
    path = BASE_DIR / "data" / "walk_scenarios.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_existing(scenes_path: Path) -> dict:
    if scenes_path.exists():
        with open(scenes_path, encoding="utf-8") as f:
            return {e["scene_id"]: e for e in json.load(f)}
    return {}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Echo 影 audio for all scenes.")
    parser.add_argument("--force", action="store_true", help="Regenerate even if MP3 exists")
    parser.add_argument("--scene", default=None, help="Only regenerate a specific scene_id")
    args = parser.parse_args()

    audio_dir   = ECHO_DIR / "audio"
    scenes_path = ECHO_DIR / "scenes.json"

    audio_dir.mkdir(parents=True, exist_ok=True)

    scenarios     = load_scenarios()
    existing      = load_existing(scenes_path)
    scene_entries = []

    for scenario in scenarios:
        scene_id = scenario["scene_id"]

        if args.scene and scene_id != args.scene:
            if scene_id in existing:
                scene_entries.append(existing[scene_id])
            continue

        mp3_path = audio_dir / f"{scene_id}.mp3"

        if scene_id in existing and mp3_path.exists() and not args.force:
            entry = existing[scene_id]
            entry["level"]       = scenario.get("level", entry.get("level", "N5"))
            entry["topic"]       = scenario.get("topic", entry.get("topic", "general"))
            entry["key_phrases"] = scenario.get("key_phrases", [])
            scene_entries.append(entry)
            print(f"  cached  {scene_id}")
            continue

        print(f"  generating  {scene_id} …")
        session_data = build_session(scenario, scene_id, mp3_path)

        entry = {
            "scene_id":         scene_id,
            "title":            scene_id.replace("_", " ").title(),
            "level":            scenario.get("level", "N5"),
            "topic":            scenario.get("topic", "general"),
            "scene_intro":      scenario["scene_intro"],
            "other_character":  scenario.get("other_character", ""),
            "goal":             scenario.get("goal", ""),
            "grammar_focus":    scenario.get("grammar_focus", ""),
            "setting":          scenario.get("setting", ""),
            "beat_count":       session_data["beat_count"],
            "duration_seconds": session_data["duration_seconds"],
            "audio_url":        f"/echo/audio/{scene_id}.mp3",
            "beats":            session_data["beats"],
            "key_phrases":      scenario.get("key_phrases", []),
        }
        scene_entries.append(entry)
        mins, secs = divmod(entry["duration_seconds"], 60)
        print(f"    done  {entry['beat_count']} beats  {mins}m{secs}s")

    with open(scenes_path, "w", encoding="utf-8") as f:
        json.dump(scene_entries, f, ensure_ascii=False, indent=2)

    print(f"\nWrote {len(scene_entries)} scenes to {scenes_path}")


if __name__ == "__main__":
    main()
