#!/usr/bin/env python3
"""
Sends the daily Japanese Word of the Day email via Beehiiv API.
Runs on a GitHub Actions cron schedule.

Required secrets (set in GitHub repo settings → Secrets → Actions):
  BEEHIIV_API_KEY  — from Beehiiv dashboard → Settings → API
  BEEHIIV_PUB_ID   — from Beehiiv dashboard URL: /publications/pub_XXXXXXXX
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

# ── Config ────────────────────────────────────────────────────────────────────

API_KEY = os.environ.get("BEEHIIV_API_KEY", "")
PUB_ID  = os.environ.get("BEEHIIV_PUB_ID", "")

if not API_KEY or not PUB_ID:
    print("ERROR: BEEHIIV_API_KEY and BEEHIIV_PUB_ID must be set.")
    sys.exit(1)

SITE_URL  = "https://japaneseunlocked.com"
API_BASE  = "https://api.beehiiv.com/v2"

# ── Load words ────────────────────────────────────────────────────────────────

repo_root  = Path(__file__).resolve().parents[2]
words_file = repo_root / "data" / "wotd.json"

with open(words_file, encoding="utf-8") as f:
    words = json.load(f)

# Pick today's word — cycles through the list indefinitely
day_index = datetime.now(timezone.utc).timetuple().tm_yday
word = words[day_index % len(words)]

print(f"Today's word ({day_index % len(words)}): {word['jp']} — {word['en']}")

# ── Build email HTML ──────────────────────────────────────────────────────────

template_path = repo_root / "static" / "email" / "wotd-preview.html"
html = template_path.read_text(encoding="utf-8")

# Replace placeholders
replacements = {
    "{{WORD_JP}}":      word["jp"],
    "{{WORD_READING}}": word["reading"],
    "{{WORD_ROMAJI}}":  word["romaji"],
    "{{WORD_POS}}":     word["pos"],
    "{{WORD_EN}}":      word["en"],
    "{{SENTENCE_JP}}":  word["sentence_jp"],
    "{{SENTENCE_EN}}":  word["sentence_en"],
    "{{TIP}}":          word["tip"],
    "{{UNSUBSCRIBE_URL}}": "{{unsubscribe_url}}",  # Beehiiv injects this at send time
}
for placeholder, value in replacements.items():
    html = html.replace(placeholder, value)

# ── Send via Beehiiv API ──────────────────────────────────────────────────────

subject  = f"🇯🇵 Word of the Day: {word['en']} — {word['jp']}"
subtitle = f"{word['reading']}  ·  {word['sentence_en'][:60]}…"

payload = {
    "subject":       subject,
    "subtitle":      subtitle,
    "status":        "confirmed",        # send immediately; use "draft" to review first
    "audience":      "free",             # send to all free subscribers
    "content_html":  html,
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type":  "application/json",
    "Accept":        "application/json",
}

resp = requests.post(
    f"{API_BASE}/publications/{PUB_ID}/posts",
    headers=headers,
    json=payload,
    timeout=30,
)

if resp.ok:
    data = resp.json()
    print(f"SUCCESS — Post created: {data.get('data', {}).get('id', 'unknown')}")
else:
    print(f"ERROR {resp.status_code}: {resp.text}")
    sys.exit(1)
