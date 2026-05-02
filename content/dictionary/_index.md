---
title: "Japanese Dictionary — Search Kanji, Kana & Romaji"
description: "Free Japanese–English dictionary. Search any Japanese word, kanji, hiragana, katakana, or romaji to instantly get readings, meanings, JLPT level, and part of speech."
date: 2025-01-01
showtoc: false
---

Search any Japanese word, kanji, hiragana, or romaji — get readings, meanings, JLPT level, and part of speech instantly. No login needed.

<div class="dict-search-wrap">
  <div class="dict-input-row">
    <input class="dict-input" id="dict-q" type="text" placeholder="e.g. 食べる · taberu · 猫 · neko…" autocomplete="off" />
    <button class="dict-btn" id="dict-go">Search 検索</button>
  </div>
  <div class="dict-hint">Type Japanese or romaji — press Enter or click Search</div>
</div>

<div id="dict-results" class="dict-results"></div>

<script>
(function () {
  var input   = document.getElementById('dict-q');
  var btn     = document.getElementById('dict-go');
  var results = document.getElementById('dict-results');

  function jlptLabel(tags) {
    for (var i = 0; i < tags.length; i++) {
      if (/^jlpt-n/.test(tags[i])) return tags[i].replace('jlpt-', '').toUpperCase();
    }
    return null;
  }

  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  function render(data) {
    if (!data || !data.length) {
      results.innerHTML = '<div class="dict-empty">No results found — try a different spelling or the Japanese characters directly.</div>';
      return;
    }
    var html = '';
    var items = data.slice(0, 8);
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      var jp      = item.japanese && item.japanese[0];
      var word    = jp ? (jp.word || jp.reading) : item.slug;
      var reading = jp && jp.word ? jp.reading : '';

      html += '<div class="dict-card">';

      /* word + reading */
      html += '<div class="dict-card-top">';
      html += '<span class="dict-word">' + esc(word) + '</span>';
      if (reading) html += '<span class="dict-reading">' + esc(reading) + '</span>';
      html += '</div>';

      /* badges */
      var badges = '';
      if (item.is_common) badges += '<span class="dict-badge dict-badge--common">Common</span>';
      var jlpt = jlptLabel(item.jlpt || []);
      if (jlpt) badges += '<span class="dict-badge dict-badge--jlpt">' + esc(jlpt) + '</span>';
      if (badges) html += '<div class="dict-badges">' + badges + '</div>';

      /* senses (up to 4) */
      var senses = (item.senses || []).slice(0, 4);
      for (var j = 0; j < senses.length; j++) {
        var s    = senses[j];
        var pos  = (s.parts_of_speech || []).join(', ');
        var defs = (s.english_definitions || []).join('; ');
        html += '<div class="dict-sense">';
        if (pos) html += '<div class="dict-pos">' + esc(pos) + '</div>';
        html += '<div class="dict-defs">' + (j + 1) + '. ' + esc(defs) + '</div>';
        html += '</div>';
      }

      html += '</div>';
    }
    html += '<div class="dict-attribution">Results powered by <a href="https://jisho.org" target="_blank" rel="noopener">Jisho.org</a></div>';
    results.innerHTML = html;
  }

  function search() {
    var q = input.value.trim();
    if (!q) return;
    results.innerHTML = '<div class="dict-loading">Searching…</div>';
    fetch('https://jisho.org/api/v1/search/words?keyword=' + encodeURIComponent(q))
      .then(function (r) { return r.json(); })
      .then(function (json) { render(json.data || []); })
      .catch(function () {
        results.innerHTML = '<div class="dict-empty">Something went wrong — please try again.</div>';
      });
  }

  btn.addEventListener('click', search);
  input.addEventListener('keydown', function (e) { if (e.key === 'Enter') search(); });

  /* auto-search if query string present: /dictionary/?q=taberu */
  var qs = new URLSearchParams(window.location.search).get('q');
  if (qs) { input.value = qs; search(); }
})();
</script>
