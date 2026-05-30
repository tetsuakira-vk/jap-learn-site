#!/usr/bin/env python3
"""
Weekly NHK Web Easy article fetcher for Japanese Unlocked.

Fetches one recent NHK Web Easy article, translates it to English,
extracts keywords, and prepends it to static/data/immersive-articles.json.

Dependencies: Python 3.8+ stdlib only (no pip install needed).

Env vars:
  DEEPL_API_KEY  — DeepL free-tier key (optional; falls back to MyMemory if absent)
"""

import html
import json
import os
import re
import sys
import time
import random
import urllib.request
import urllib.parse
from datetime import datetime, timezone

# ── Config ────────────────────────────────────────────────────────────────────

DATA_FILE    = "static/data/immersive-articles.json"
MAX_ARTICLES = 25
MAX_BODY_CHARS = 800   # keep articles learner-appropriate

NHK_LIST    = "https://www3.nhk.or.jp/news/easy/news-list.json"
NHK_ARTICLE = "https://www3.nhk.or.jp/news/easy/{id}/{id}.html"

UA = "Mozilla/5.0 (compatible; JapaneseUnlockedScraper/1.0; educational)"

STOPWORDS = {
    "the","a","an","and","or","but","in","on","at","to","for","of","with",
    "by","from","is","are","was","were","be","been","have","has","had",
    "do","does","did","will","would","could","should","may","might",
    "this","that","these","those","it","its","they","them","their","there",
    "as","if","when","where","who","which","how","what","about","into","up",
    "out","than","then","also","very","more","most","some","such","not","no",
    "so","much","many","one","two","three","said","says","according","year",
    "years","people","japan","japanese","new","time","since","after","before",
    "during","while","between","through","over","under","around","per",
    "been","being","were","can","its","was","are","has","had","did",
    "just","even","now","still","last","next","first","well","back",
    "only","both","than","too","very","our","your","their","has",
}

# ── HTTP helpers ───────────────────────────────────────────────────────────────

def fetch(url, retries=3):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.read()
        except Exception as exc:
            if attempt == retries - 1:
                raise
            print(f"  Retry {attempt+1}: {exc}")
            time.sleep(2 ** attempt)

# ── HTML processing ────────────────────────────────────────────────────────────

def strip_ruby(text):
    """Remove <rt> (furigana) tags, keep kanji."""
    text = re.sub(r'<rt[^>]*>.*?</rt>', '', text, flags=re.DOTALL)
    text = re.sub(r'</?ruby[^>]*>', '', text)
    return text

def strip_tags(text):
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    return text

def clean_text(raw_html):
    text = strip_ruby(raw_html)
    text = strip_tags(text)
    text = html.unescape(text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

# ── Translation ────────────────────────────────────────────────────────────────

def translate_deepl(text, api_key):
    body = urllib.parse.urlencode({
        "auth_key": api_key,
        "text": text[:1200],
        "source_lang": "JA",
        "target_lang": "EN",
    }).encode()
    req = urllib.request.Request(
        "https://api-free.deepl.com/v2/translate",
        data=body,
        headers={"User-Agent": UA},
    )
    data = json.loads(urllib.request.urlopen(req, timeout=20).read())
    return data["translations"][0]["text"]

def translate_mymemory(text):
    """Free fallback: MyMemory (up to 500 chars/request)."""
    url = (
        "https://api.mymemory.translated.net/get"
        "?q={}&langpair=ja|en&de=japaneseunlocked%40gmail.com".format(
            urllib.parse.quote(text[:500])
        )
    )
    data = json.loads(fetch(url))
    return data.get("responseData", {}).get("translatedText", "")

def translate(text):
    api_key = os.environ.get("DEEPL_API_KEY", "").strip()
    if api_key:
        try:
            result = translate_deepl(text, api_key)
            print(f"  DeepL: OK ({len(result)} chars)")
            return result
        except Exception as e:
            print(f"  DeepL failed ({e}), falling back to MyMemory")
    result = translate_mymemory(text)
    print(f"  MyMemory: OK ({len(result)} chars)")
    return result

# ── Keyword extraction ─────────────────────────────────────────────────────────

def extract_keywords(english, n=10):
    words = re.findall(r'\b[a-z]{3,}\b', english.lower())
    freq = {}
    for w in words:
        if w not in STOPWORDS:
            freq[w] = freq.get(w, 0) + 1
    ranked = sorted(freq.items(), key=lambda x: -x[1])
    return [w for w, _ in ranked[:n]]

# ── Category detection ─────────────────────────────────────────────────────────

def detect_category(title, body):
    text = title + body
    if any(k in text for k in ['祭', 'フェス', '伝統', '神社', '文化']):
        return 'culture'
    if any(k in text for k in ['食', '料理', 'レストラン', 'グルメ', 'ラーメン', '味']):
        return 'food'
    if any(k in text for k in ['スポーツ', '選手', '試合', '優勝', 'マラソン', 'オリンピック', '競技']):
        return 'sports'
    if any(k in text for k in ['映画', 'アニメ', '音楽', 'ドラマ', '番組', '芸能', '俳優']):
        return 'entertainment'
    if any(k in text for k in ['技術', 'ロボット', 'AI', 'スマホ', 'アプリ', 'デジタル', 'IT']):
        return 'technology'
    return 'news'

# ── NHK article parsing ────────────────────────────────────────────────────────

def parse_nhk_article(html_bytes):
    text = html_bytes.decode('utf-8', errors='replace')

    # Title: try multiple selectors
    title = ''
    for pattern in [
        r'class="article-main__title"[^>]*>(.*?)</h1>',
        r'class="news-title"[^>]*>(.*?)</h1>',
        r'<h1[^>]*>(.*?)</h1>',
    ]:
        m = re.search(pattern, text, re.DOTALL)
        if m:
            title = clean_text(m.group(1))
            break

    # Body: try multiple selectors
    body = ''
    for pattern in [
        r'id="js-article-body"[^>]*>(.*?)</div>',
        r'class="article-main__body"[^>]*>(.*?)</div>',
        r'class="news-content"[^>]*>(.*?)</section>',
    ]:
        m = re.search(pattern, text, re.DOTALL)
        if m:
            body = clean_text(m.group(1))
            break

    return title, body

# ── Data file helpers ──────────────────────────────────────────────────────────

def load_articles():
    try:
        with open(DATA_FILE, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Warning: could not load {DATA_FILE}: {e}")
        return []

def save_articles(articles):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("=== NHK Web Easy weekly fetch ===")

    print("Fetching article list…")
    list_data = json.loads(fetch(NHK_LIST))

    # Flatten: list is [{date: [articles]}, ...]
    all_articles = []
    for item in list_data:
        for _date, articles in item.items():
            all_articles.extend(articles)

    all_articles.sort(key=lambda x: x.get('news_prearranged_time', ''), reverse=True)
    candidates = all_articles[:8]
    print(f"Found {len(all_articles)} articles, checking top {len(candidates)}")

    existing      = load_articles()
    existing_ids  = {a['id'] for a in existing}

    # Pick first candidate we don't already have
    pick = None
    for c in candidates:
        if c.get('news_id') and c['news_id'] not in existing_ids:
            pick = c
            break

    if not pick:
        pick = random.choice(candidates)
        print("All recent articles already in bank — picking a random one anyway.")

    article_id  = pick['news_id']
    article_url = NHK_ARTICLE.format(id=article_id)
    print(f"Fetching: {article_url}")

    raw_html = fetch(article_url)
    title_jp, body_jp = parse_nhk_article(raw_html)

    if not title_jp:
        title_jp = html.unescape(pick.get('title', 'NHK Web Easy'))
    if not body_jp:
        print("ERROR: Could not parse article body — aborting.")
        sys.exit(1)

    # Trim body to learner-friendly length
    if len(body_jp) > MAX_BODY_CHARS:
        # Try to end at sentence boundary
        cut = body_jp[:MAX_BODY_CHARS]
        last_period = max(cut.rfind('。'), cut.rfind('！'), cut.rfind('？'))
        body_jp = cut[:last_period + 1] if last_period > 200 else cut

    print(f"Title: {title_jp}")
    print(f"Body:  {len(body_jp)} chars")

    print("Translating…")
    english_model = translate(f"{title_jp}\n\n{body_jp}")

    keywords = extract_keywords(english_model, n=10)
    print(f"Keywords: {keywords}")

    category = detect_category(title_jp, body_jp)
    print(f"Category: {category}")

    new_article = {
        "id":            article_id,
        "title":         title_jp,
        "category":      category,
        "date":          datetime.now(timezone.utc).strftime('%Y-%m-%d'),
        "source":        "NHK Web Easy",
        "source_url":    article_url,
        "japanese":      body_jp,
        "english_model": english_model,
        "keywords":      keywords,
    }

    if article_id not in existing_ids:
        existing.insert(0, new_article)
        existing = existing[:MAX_ARTICLES]
        save_articles(existing)
        print(f"✓ Saved: {title_jp}")
    else:
        print(f"Article {article_id} already in bank — file unchanged.")

if __name__ == '__main__':
    main()
