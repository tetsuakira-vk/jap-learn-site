#!/usr/bin/env python3
"""
Walk Mode — generate audio for every scenario and write static/walk/scenes.json.

Run once to set up the full scene catalogue. Subsequent runs skip scenes whose
MP3 already exists (unless --force).

Usage:
    python tools/walk/generate_all_scenes.py
    python tools/walk/generate_all_scenes.py --force
    python tools/walk/generate_all_scenes.py --scene konbini_visit
"""

import argparse
import json
import sys
from pathlib import Path

BASE_DIR   = Path(__file__).parent          # tools/walk/
REPO_ROOT  = BASE_DIR.parent.parent         # repo root
STATIC_WALK = REPO_ROOT / "static" / "walk"

sys.path.insert(0, str(BASE_DIR))
from walk_audio import build_session


def load_scenarios() -> list[dict]:
    path = BASE_DIR / "data" / "walk_scenarios.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_existing_scenes(scenes_path: Path) -> dict:
    if scenes_path.exists():
        with open(scenes_path, encoding="utf-8") as f:
            return {e["scene_id"]: e for e in json.load(f)}
    return {}


def scene_title(scene_id: str) -> str:
    return scene_id.replace("_", " ").title()


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate all Walk Mode scenes.")
    parser.add_argument("--force", action="store_true", help="Regenerate even if MP3 exists")
    parser.add_argument("--scene", default=None, help="Only regenerate a specific scene_id")
    args = parser.parse_args()

    audio_dir   = STATIC_WALK / "audio"
    scenes_path = STATIC_WALK / "scenes.json"

    audio_dir.mkdir(parents=True, exist_ok=True)

    scenarios     = load_scenarios()
    existing      = load_existing_scenes(scenes_path)
    scene_entries = []

    for scenario in scenarios:
        scene_id = scenario["scene_id"]

        if args.scene and scene_id != args.scene:
            # Keep existing entry if we're only regenerating one scene
            if scene_id in existing:
                scene_entries.append(existing[scene_id])
            continue

        mp3_path = audio_dir / f"{scene_id}.mp3"

        if scene_id in existing and mp3_path.exists() and not args.force:
            # Update metadata from scenarios file without re-synthesising audio
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
            "title":            scene_title(scene_id),
            "level":            scenario.get("level", "N5"),
            "topic":            scenario.get("topic", "general"),
            "scene_intro":      scenario["scene_intro"],
            "other_character":  scenario.get("other_character", ""),
            "beat_count":       session_data["beat_count"],
            "duration_seconds": session_data["duration_seconds"],
            "audio_url":        f"audio/{scene_id}.mp3",
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
