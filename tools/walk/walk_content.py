"""
Walk Mode — Content Service

Scene-based session selector with SM2-ish SRS scheduler.
Canonical source — used by both local generation and GitHub Actions.
"""

from __future__ import annotations

import json
import random
from datetime import date, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCENARIOS_PATH = BASE_DIR / "data" / "walk_scenarios.json"
SRS_PATH       = BASE_DIR / "data" / "walk_srs.json"

DEFAULT_EASE = 2.5
MIN_EASE     = 1.3
MAX_EASE     = 5.0
EASE_CORRECT   = 0.1
EASE_INCORRECT = 0.2
SPILL_THRESHOLD = 6


def _load_scenes() -> list[dict]:
    with open(SCENARIOS_PATH, encoding="utf-8") as f:
        return json.load(f)


def _load_srs() -> dict:
    if SRS_PATH.exists():
        with open(SRS_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_srs(srs: dict) -> None:
    SRS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SRS_PATH, "w", encoding="utf-8") as f:
        json.dump(srs, f, ensure_ascii=False, indent=2)


def _is_due(entry: dict, today: date) -> bool:
    return date.fromisoformat(entry["due_date"]) <= today


def _scene_score(scene: dict, srs: dict, today: date) -> float:
    beats = scene.get("beats", [])
    if not beats:
        return -1.0
    useful = sum(
        1 for b in beats
        if b["srs_id"] not in srs or _is_due(srs[b["srs_id"]], today)
    )
    return useful / len(beats)


def get_session_scene(max_beats: int = 15, new_ratio: float = 0.3) -> dict:
    """
    Select today's scene with beats in arc order.
    Picks the scene with the most actionable (due or unseen) beats.
    """
    scenes = _load_scenes()
    srs    = _load_srs()
    today  = date.today()

    active = [s for s in scenes if s.get("beats")]
    if not active:
        raise ValueError("No scenes with beats found in walk_scenarios.json")

    scored = sorted(
        active,
        key=lambda s: (_scene_score(s, srs, today), random.random()),
        reverse=True,
    )
    primary = scored[0]
    beats = list(primary["beats"])[:max_beats]

    if len(primary["beats"]) < SPILL_THRESHOLD and len(scored) > 1:
        secondary = scored[1]
        beats += list(secondary["beats"])[: max_beats - len(beats)]

    return {
        "scene_id":        primary["scene_id"],
        "scene_intro":     primary["scene_intro"],
        "other_character": primary.get("other_character", ""),
        "character_gender": primary.get("character_gender", "male"),
        "level":           primary.get("level", "N5"),
        "beats":           beats,
    }


def mark_session_seen(srs_ids: list[str], correct: bool = True) -> None:
    srs   = _load_srs()
    today = date.today()

    for sid in srs_ids:
        entry    = srs.get(sid, {"ease": DEFAULT_EASE, "interval_days": 1})
        ease     = float(entry["ease"])

        if correct:
            ease     = min(ease + EASE_CORRECT, MAX_EASE)
            interval = max(1, round(entry["interval_days"] * ease))
        else:
            ease     = max(ease - EASE_INCORRECT, MIN_EASE)
            interval = 1

        srs[sid] = {
            "last_seen":    today.isoformat(),
            "interval_days": interval,
            "ease":          round(ease, 2),
            "due_date":      (today + timedelta(days=interval)).isoformat(),
        }

    _save_srs(srs)
