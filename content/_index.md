---
title: "Learn Japanese — Free Interactive Study Site"
description: "Free interactive Japanese learning with quizzes, reference charts, and phrase guides."
---

<div class="section-grid">
  <a class="section-card" href="/videos/">
    <span class="sc-icon">▶️</span>
    <span class="sc-title">Videos</span>
    <span class="sc-desc">Latest from the YouTube channel</span>
  </a>
  <a class="section-card" href="/start/">
    <span class="sc-icon">🚀</span>
    <span class="sc-title">Start Here</span>
    <span class="sc-desc">Complete beginner? Start here.</span>
  </a>
  <a class="section-card" href="/hiragana/">
    <span class="sc-icon">あ</span>
    <span class="sc-title">Hiragana</span>
    <span class="sc-desc">46 characters. The foundation.</span>
  </a>
  <a class="section-card" href="/katakana/">
    <span class="sc-icon">ア</span>
    <span class="sc-title">Katakana</span>
    <span class="sc-desc">Foreign words & emphasis.</span>
  </a>
  <a class="section-card" href="/kanji/">
    <span class="sc-icon">漢</span>
    <span class="sc-title">Kanji</span>
    <span class="sc-desc">50 essential beginner kanji.</span>
  </a>
  <a class="section-card" href="/vocab/">
    <span class="sc-icon">📚</span>
    <span class="sc-title">N5 Vocab</span>
    <span class="sc-desc">100 essential N5 words + quiz.</span>
  </a>
  <a class="section-card" href="/numbers/">
    <span class="sc-icon">🔢</span>
    <span class="sc-title">Numbers</span>
    <span class="sc-desc">Count to 10,000 with audio.</span>
  </a>
  <a class="section-card" href="/phrases/">
    <span class="sc-icon">💬</span>
    <span class="sc-title">Phrases</span>
    <span class="sc-desc">Real sentences. Hear them spoken.</span>
  </a>
  <a class="section-card" href="/sentences/quiz/">
    <span class="sc-icon">🎯</span>
    <span class="sc-title">Sentence Quiz</span>
    <span class="sc-desc">English → Japanese. Can you pick it?</span>
  </a>
</div>

---

## Word of the Day

<div id="wotd-card" style="background:var(--entry);border:1px solid var(--border);border-radius:12px;padding:1.4rem 1.6rem;margin:0.5rem 0 1.5rem;max-width:480px">
  <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.08em;color:var(--secondary);margin-bottom:0.6rem">Word of the Day</div>
  <div id="wotd-jp" style="font-size:2.2rem;font-weight:700;cursor:pointer;line-height:1.1" onclick="wotdSpeak()" title="Click to hear">—</div>
  <div id="wotd-en" style="font-size:1rem;color:var(--secondary);margin-top:0.35rem">Loading...</div>
  <div id="wotd-hint" style="font-size:0.82rem;color:var(--secondary);margin-top:0.25rem;font-style:italic"></div>
  <div style="margin-top:0.8rem">
    <button class="pt-play" onclick="wotdSpeak()">▶ Hear it</button>
  </div>
</div>

<script>
(function() {
  var words = [
    {jp:'おはようございます',en:'Good morning',hint:'Greeting — used in the morning'},
    {jp:'ありがとうございます',en:'Thank you (polite)',hint:'The most useful phrase to know'},
    {jp:'すみません',en:'Excuse me / Sorry',hint:'Works for getting attention or apologising'},
    {jp:'わかりません',en:'I don\'t understand',hint:'You\'ll use this a lot at first!'},
    {jp:'がんばって！',en:'Do your best!',hint:'Great encouragement phrase'},
    {jp:'日本語を勉強しています',en:'I\'m studying Japanese',hint:'Perfect for introducing yourself'},
    {jp:'おいしい！',en:'Delicious!',hint:'React to food like a local'},
    {jp:'どこですか？',en:'Where is it?',hint:'Essential for navigating Japan'},
    {jp:'いくらですか？',en:'How much is it?',hint:'Vital for shopping'},
    {jp:'また明日',en:'See you tomorrow',hint:'Casual farewell'},
    {jp:'よろしくお願いします',en:'Pleased to meet you / I\'m in your care',hint:'Heard constantly in Japan'},
    {jp:'大丈夫ですか？',en:'Are you okay?',hint:'Check in on someone'},
    {jp:'はじめまして',en:'Nice to meet you (first time)',hint:'Always used at a first introduction'},
    {jp:'ゆっくり話してください',en:'Please speak slowly',hint:'Don\'t be shy — native speakers appreciate the effort'},
    {jp:'日本語が好きです',en:'I like Japanese',hint:'True, right?'},
    {jp:'毎日練習します',en:'I practise every day',hint:'The secret to fluency'},
    {jp:'かっこいい！',en:'Cool! / Awesome!',hint:'Useful reaction word'},
    {jp:'なるほど',en:'I see / That makes sense',hint:'Very natural filler in conversation'},
    {jp:'気をつけて',en:'Take care',hint:'Said when someone is leaving'},
    {jp:'お疲れ様です',en:'Good work / Thanks for your efforts',hint:'Said at the end of a work day — very Japanese'},
    {jp:'楽しかった！',en:'That was fun!',hint:'Past tense of 楽しい — use after an activity'},
    {jp:'どうぞ',en:'Please / Go ahead / Here you are',hint:'Very versatile — said when offering something'},
    {jp:'ちょっと待ってください',en:'Please wait a moment',hint:'Polite way to ask someone to hang on'},
    {jp:'本当ですか？',en:'Really? Is that true?',hint:'Show surprise or interest in conversation'},
    {jp:'面白い！',en:'Interesting! / Funny!',hint:'おもしろい — great reaction to news or jokes'},
    {jp:'頑張ります',en:'I\'ll do my best',hint:'Commitment — said before a challenge'},
    {jp:'お腹が空いた',en:'I\'m hungry',hint:'Casual — very commonly heard'},
    {jp:'疲れた',en:'I\'m tired',hint:'Casual — drop です in informal speech'},
    {jp:'行ってきます',en:'I\'m heading out (and I\'ll be back)',hint:'Said when leaving home — deeply Japanese'},
    {jp:'ただいま',en:'I\'m home',hint:'Said when arriving home — the response is おかえり'}
  ];

  var idx = Math.floor(Date.now() / 86400000) % words.length;
  var w = words[idx];
  document.getElementById('wotd-jp').textContent = w.jp;
  document.getElementById('wotd-en').textContent = w.en;
  document.getElementById('wotd-hint').textContent = w.hint;

  window.wotdSpeak = function() {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance(w.jp);
    u.lang = 'ja-JP'; u.rate = 0.82;
    window.speechSynthesis.speak(u);
  };
})();
</script>

---

## How this site works

Each section has a **reference chart** you can click to hear pronunciations, and an **interactive quiz** to test yourself. No sign-up. No ads. Just drill.

**Recommended order:**

1. Read [Start Here](/start/) to understand the writing systems
2. Learn [Hiragana](/hiragana/) — use the chart, then take the quiz daily
3. Move to [Katakana](/katakana/) once hiragana clicks
4. Build [N5 Vocab](/vocab/) and [Kanji](/kanji/) alongside the YouTube lessons
5. Practice real [Phrases](/phrases/) and [Sentences](/sentences/quiz/) as soon as possible

> Click any character or phrase button across the site to hear it pronounced.
