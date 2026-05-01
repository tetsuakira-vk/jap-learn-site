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

# STATUS: "draft" = saves to Beehiiv for you to review & send manually
#         "confirmed" = sends immediately to all subscribers
STATUS = "draft"

payload = {
    "title":        f"WOTD: {word['jp']} — {word['en']}",
    "subject":      subject,
    "subtitle":     subtitle,
    "status":       STATUS,
    "content_html": html,
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type":  "application/json",
    "Accept":        "application/json",
}

print(f"Posting to: {API_BASE}/publications/{PUB_ID}/posts")
print(f"Subject: {subject}")
print(f"Status: {STATUS}")

resp = requests.post(
    f"{API_BASE}/publications/{PUB_ID}/posts",
    headers=headers,
    json=payload,
    timeout=30,
)

print(f"Response status: {resp.status_code}")
print(f"Response body: {resp.text[:2000]}")

if resp.ok:
    data = resp.json()
    post_id = data.get("data", {}).get("id", "unknown")
    print(f"SUCCESS — Draft created: {post_id}")
    print(f"Review it at: https://app.beehiiv.com/posts/{post_id}")
else:
    print("FAILED — see response above for details")
    sys.exit(1)
