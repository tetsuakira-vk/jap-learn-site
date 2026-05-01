#!/usr/bin/env python3
"""
Sends the daily Japanese Word of the Day email via Brevo (Sendinblue) API.
Runs on a GitHub Actions cron schedule.

Required secrets (GitHub repo → Settings → Secrets → Actions):
  BREVO_API_KEY      — from Brevo dashboard → Settings → API Keys
  BREVO_SENDER_EMAIL — verified sender address in Brevo
  BREVO_LIST_ID      — contact list ID (Brevo → Contacts → Lists — it's a number like 3)
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

# ── Config ────────────────────────────────────────────────────────────────────

API_KEY      = os.environ.get("BREVO_API_KEY", "")
SENDER_EMAIL = os.environ.get("BREVO_SENDER_EMAIL", "")
LIST_ID      = os.environ.get("BREVO_LIST_ID", "")

if not API_KEY or not SENDER_EMAIL or not LIST_ID:
    print("ERROR: BREVO_API_KEY, BREVO_SENDER_EMAIL and BREVO_LIST_ID must all be set.")
    sys.exit(1)

API_BASE = "https://api.brevo.com/v3"
HEADERS  = {
    "accept":       "application/json",
    "content-type": "application/json",
    "api-key":      API_KEY,
}

# ── Load words ────────────────────────────────────────────────────────────────

repo_root  = Path(__file__).resolve().parents[2]
words_file = repo_root / "data" / "wotd.json"

with open(words_file, encoding="utf-8") as f:
    words = json.load(f)

day_index = datetime.now(timezone.utc).timetuple().tm_yday
word = words[day_index % len(words)]
print(f"Today's word ({day_index % len(words)}): {word['jp']} — {word['en']}")

# ── Build email HTML ──────────────────────────────────────────────────────────

template_path = repo_root / "static" / "email" / "wotd-preview.html"
html = template_path.read_text(encoding="utf-8")

replacements = {
    "{{WORD_JP}}":      word["jp"],
    "{{WORD_READING}}": word["reading"],
    "{{WORD_ROMAJI}}":  word["romaji"],
    "{{WORD_POS}}":     word["pos"],
    "{{WORD_EN}}":      word["en"],
    "{{SENTENCE_JP}}":  word["sentence_jp"],
    "{{SENTENCE_EN}}":  word["sentence_en"],
    "{{TIP}}":          word["tip"],
    # Brevo injects its own unsubscribe link — remove the placeholder
    "{{UNSUBSCRIBE_URL}}": "#",
}
for placeholder, value in replacements.items():
    html = html.replace(placeholder, value)

# ── Create campaign ───────────────────────────────────────────────────────────

subject = f"🇯🇵 Word of the Day: {word['en']} — {word['jp']}"

campaign_payload = {
    "name":    f"WOTD {datetime.now(timezone.utc).strftime('%Y-%m-%d')} — {word['jp']}",
    "subject": subject,
    "sender":  {"name": "Japanese Unlocked", "email": SENDER_EMAIL},
    "type":    "classic",
    "htmlContent": html,
    "recipients":  {"listIds": [int(LIST_ID)]},
}

print(f"Creating campaign: {subject}")
resp = requests.post(f"{API_BASE}/emailCampaigns", headers=HEADERS, json=campaign_payload, timeout=30)
print(f"Create response {resp.status_code}: {resp.text[:500]}")

if not resp.ok:
    print("FAILED to create campaign.")
    sys.exit(1)

campaign_id = resp.json().get("id")
print(f"Campaign created: id={campaign_id}")

# ── Send immediately ──────────────────────────────────────────────────────────

send_resp = requests.post(
    f"{API_BASE}/emailCampaigns/{campaign_id}/sendNow",
    headers=HEADERS,
    timeout=30,
)
print(f"Send response {send_resp.status_code}: {send_resp.text[:500]}")

if send_resp.ok:
    print(f"SUCCESS — email sent to list {LIST_ID}")
else:
    print("Campaign created but FAILED to send.")
    sys.exit(1)
