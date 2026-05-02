---
title: "Japanese Dictionary — Search Kanji, Kana & Romaji"
description: "Free Japanese–English dictionary. Search any Japanese word, kanji, hiragana, katakana, or romaji to instantly get readings, meanings, and part of speech."
date: 2025-01-01
showtoc: false
---

Search any Japanese word, kanji, hiragana, or romaji — results appear as you type.

<div class="dict-search-wrap">
  <div class="dict-input-row">
    <input class="dict-input" id="dict-q" type="text" placeholder="e.g. 食べる · taberu · 猫 · water…" autocomplete="off" />
    <button class="dict-btn" id="dict-go">Search 検索</button>
  </div>
  <div class="dict-hint" id="dict-hint">Type Japanese, romaji, or English — results appear as you type</div>
</div>

<div id="dict-results" class="dict-results"></div>

<script>
(function () {
  var input   = document.getElementById('dict-q');
  var btn     = document.getElementById('dict-go');
  var hint    = document.getElementById('dict-hint');
  var results = document.getElementById('dict-results');
  var timer   = null;
  var lastQ   = '';

  function posLabel(posArr) {
    if (!posArr || !posArr.length) return '';
    return posArr.map(function (p) {
      var keys = Object.keys(p);
      if (!keys.length) return '';
      var type = keys[0];
      var sub  = p[type];
      if (!sub || sub === 'Normal' || sub === type) return type;
      return type + ' (' + sub + ')';
    }).filter(Boolean).join(', ');
  }

  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  function render(words) {
    if (!words || !words.length) {
      results.innerHTML = '<div class="dict-empty">No results — try different spelling or the Japanese characters directly.</div>';
      hint.textContent = 'Type Japanese, romaji, or English — results appear as you type';
      return;
    }
    var html = '';
    var items = words.slice(0, 8);
    for (var i = 0; i < items.length; i++) {
      var item    = items[i];
      var reading = item.reading || {};
      var word    = reading.kanji || reading.kana || '';
      var kana    = reading.kanji ? reading.kana : '';

      html += '<div class="dict-card">';

      /* word + kana reading */
      html += '<div class="dict-card-top">';
      html += '<span class="dict-word">' + esc(word) + '</span>';
      if (kana) html += '<span class="dict-reading">' + esc(kana) + '</span>';
      html += '</div>';

      /* common badge */
      if (item.common) {
        html += '<div class="dict-badges"><span class="dict-badge dict-badge--common">Common</span></div>';
      }

      /* senses */
      var senses = (item.senses || []).slice(0, 4);
      for (var j = 0; j < senses.length; j++) {
        var s    = senses[j];
        if (s.language && s.language !== 'English') continue;
        var pos  = posLabel(s.pos || []);
        var defs = (s.glosses || []).join('; ');
        if (!defs) continue;
        html += '<div class="dict-sense">';
        if (pos) html += '<div class="dict-pos">' + esc(pos) + '</div>';
        html += '<div class="dict-defs">' + (j + 1) + '. ' + esc(defs) + '</div>';
        html += '</div>';
      }

      html += '</div>';
    }
    html += '<div class="dict-attribution">Results via <a href="https://jotoba.de" target="_blank" rel="noopener">Jotoba</a> (JMdict)</div>';
    results.innerHTML = html;
    hint.textContent = words.length + ' result' + (words.length !== 1 ? 's' : '') + ' found';
  }

  function search(q) {
    if (!q || q === lastQ) return;
    lastQ = q;
    hint.textContent = 'Searching…';
    fetch('https://jotoba.de/api/search/words', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: q, language: 'English', no_english: false })
    })
      .then(function (r) { return r.json(); })
      .then(function (json) { render(json.words || []); })
      .catch(function () {
        hint.textContent = 'Type Japanese, romaji, or English — results appear as you type';
        results.innerHTML = '<div class="dict-empty">Connection error — please try again.</div>';
        lastQ = '';
      });
  }

  /* debounced auto-search as you type */
  input.addEventListener('input', function () {
    clearTimeout(timer);
    var q = input.value.trim();
    if (!q) {
      results.innerHTML = '';
      hint.textContent = 'Type Japanese, romaji, or English — results appear as you type';
      lastQ = '';
      return;
    }
    hint.textContent = 'Searching…';
    timer = setTimeout(function () { search(q); }, 350);
  });

  btn.addEventListener('click', function () {
    lastQ = '';
    search(input.value.trim());
  });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { clearTimeout(timer); lastQ = ''; search(input.value.trim()); }
  });

  /* auto-search from URL query string: /dictionary/?q=taberu */
  var qs = new URLSearchParams(window.location.search).get('q');
  if (qs) { input.value = qs; search(qs); }
})();
</script>
