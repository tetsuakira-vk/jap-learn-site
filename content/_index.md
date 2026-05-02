---
title: "Japanese Unlocked — Free Interactive Japanese Learning"
description: "Japanese Unlocked — free interactive Japanese learning for beginners. Study hiragana, katakana, kanji, JLPT vocab, grammar, and phrases with audio quizzes. No sign-up needed."
---

<div id="wotd-card" class="wotd-card">
  <div class="wotd-main">
    <div class="wotd-label">Word of the Day</div>
    <div id="wotd-jp" class="wotd-jp" onclick="wotdSpeak()" title="Click to hear">—</div>
    <div id="wotd-read" class="wotd-read"></div>
    <div id="wotd-en" class="wotd-en">Loading...</div>
    <div id="wotd-hint" class="wotd-hint"></div>
    <button class="pt-play" onclick="wotdSpeak()" style="margin-top:0.9rem">▶ Hear it</button>
  </div>
  <div class="wotd-side">
    <div id="wotd-deco" class="wotd-deco"></div>
    <div id="wotd-tip" class="wotd-tip"></div>
  </div>
</div>

<script>
(function() {
  var words = [
    {jp:'おはようございます',read:'ohayou gozaimasu',en:'Good morning',hint:'Greeting — used in the morning'},
    {jp:'ありがとうございます',read:'arigatou gozaimasu',en:'Thank you (polite)',hint:'The most useful phrase to know'},
    {jp:'すみません',read:'sumimasen',en:'Excuse me / Sorry',hint:'Works for getting attention or apologising'},
    {jp:'わかりません',read:'wakarimasen',en:'I don\'t understand',hint:'You\'ll use this a lot at first!'},
    {jp:'がんばって！',read:'ganbatte!',en:'Do your best!',hint:'Great encouragement phrase'},
    {jp:'日本語を勉強しています',read:'nihongo wo benkyou shite imasu',en:'I\'m studying Japanese',hint:'Perfect for introducing yourself'},
    {jp:'おいしい！',read:'oishii!',en:'Delicious!',hint:'React to food like a local'},
    {jp:'どこですか？',read:'doko desu ka?',en:'Where is it?',hint:'Essential for navigating Japan'},
    {jp:'いくらですか？',read:'ikura desu ka?',en:'How much is it?',hint:'Vital for shopping'},
    {jp:'また明日',read:'mata ashita',en:'See you tomorrow',hint:'Casual farewell'},
    {jp:'よろしくお願いします',read:'yoroshiku onegai shimasu',en:'Pleased to meet you',hint:'Heard constantly in Japan'},
    {jp:'大丈夫ですか？',read:'daijoubu desu ka?',en:'Are you okay?',hint:'Check in on someone'},
    {jp:'はじめまして',read:'hajimemashite',en:'Nice to meet you',hint:'Always used at a first introduction'},
    {jp:'ゆっくり話してください',read:'yukkuri hanashite kudasai',en:'Please speak slowly',hint:'Native speakers appreciate the effort'},
    {jp:'日本語が好きです',read:'nihongo ga suki desu',en:'I like Japanese',hint:'True, right?'},
    {jp:'毎日練習します',read:'mainichi renshuu shimasu',en:'I practise every day',hint:'The secret to fluency'},
    {jp:'かっこいい！',read:'kakkoii!',en:'Cool! / Awesome!',hint:'Useful reaction word'},
    {jp:'なるほど',read:'naruhodo',en:'I see / That makes sense',hint:'Very natural filler in conversation'},
    {jp:'気をつけて',read:'ki wo tsukete',en:'Take care',hint:'Said when someone is leaving'},
    {jp:'お疲れ様です',read:'otsukaresama desu',en:'Good work / Thanks for your efforts',hint:'Said at the end of a work day'},
    {jp:'楽しかった！',read:'tanoshikatta!',en:'That was fun!',hint:'Past tense of 楽しい — use after an activity'},
    {jp:'どうぞ',read:'douzo',en:'Please / Go ahead / Here you are',hint:'Said when offering something'},
    {jp:'ちょっと待ってください',read:'chotto matte kudasai',en:'Please wait a moment',hint:'Polite way to ask someone to hang on'},
    {jp:'本当ですか？',read:'hontou desu ka?',en:'Really? Is that true?',hint:'Show surprise in conversation'},
    {jp:'面白い！',read:'omoshiroi!',en:'Interesting! / Funny!',hint:'Great reaction to news or jokes'},
    {jp:'頑張ります',read:'ganbarimasu',en:'I\'ll do my best',hint:'Said before a challenge'},
    {jp:'お腹が空いた',read:'onaka ga suita',en:'I\'m hungry',hint:'Casual — very commonly heard'},
    {jp:'疲れた',read:'tsukareta',en:'I\'m tired',hint:'Casual — drop です in informal speech'},
    {jp:'行ってきます',read:'itte kimasu',en:'I\'m heading out',hint:'Said when leaving home — deeply Japanese'},
    {jp:'ただいま',read:'tadaima',en:'I\'m home',hint:'Said when arriving home — response is おかえり'}
  ];
  var decoWords = ['勉強','練習','上達','努力','継続','挑戦','学習','成長','忍耐','情熱',
                   '夢','希望','前進','達成','言語','可能','未来','文化','知識','才能'];
  var tips = [
    'Japanese has no spaces between words — you spot boundaries by recognising patterns.',
    'Verbs go at the END in Japanese. "I sushi eat" → 寿司を食べる.',
    'Adding か to any sentence makes it a question. No question mark needed.',
    'Japanese has 3 politeness levels — casual, polite (です/ます), and honorific.',
    'Hiragana was created in the Heian period (794–1185) — originally a women\'s script.',
    'Japan has ~50,000 kanji in total. Daily life only needs around 2,136.',
    'Japanese primary school teaches 1,006 kanji over 6 years — that\'s your first target.',
    '日本 (Nihon) means "origin of the sun" — that\'s where the name Japan comes from.',
    'Japanese borrows from many languages. パン (pan, bread) came from Portuguese!',
    'No grammatical gender in Japanese — there is no "he" or "she" distinction.',
    'The subject is often dropped in Japanese — context does the work.',
    'A single kanji can have multiple readings — on\'yomi (Chinese) and kun\'yomi (Japanese).',
    'です and ます verb forms cover 90% of polite daily conversation. Master those first.',
    'Japanese people rarely say a direct "no" — silence or 難しい often means no.',
    'Writing kanji by hand helps memory — the stroke order has logic once you see it.',
    'The Japanese alphabet (hiragana) can be learned in about one week with daily practice.',
    'Japanese sentences follow Subject–Object–Verb order, unlike English Subject–Verb–Object.',
    'Pitch accent exists in Japanese — the same word can mean different things depending on tone.',
    'Reading manga in Japanese is one of the fastest ways to build vocabulary naturally.',
    'Every hiragana character represents one mora (sound unit) — no silent letters.'
  ];
  var idx = Math.floor(Date.now() / 86400000) % words.length;
  var w = words[idx];
  document.getElementById('wotd-jp').textContent = w.jp;
  document.getElementById('wotd-read').textContent = w.read;
  document.getElementById('wotd-en').textContent = w.en;
  document.getElementById('wotd-hint').textContent = w.hint;
  document.getElementById('wotd-deco').textContent = decoWords[idx % decoWords.length];
  document.getElementById('wotd-tip').textContent = tips[idx % tips.length];
  window.wotdSpeak = function() {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance(w.jp);
    u.lang = 'ja-JP'; u.rate = 0.82;
    window.speechSynthesis.speak(u);
  };
})();
</script>

<div class="section-grid">
  <a class="section-card" href="start/">
    <span class="sc-icon"><img src="/icons/torii-gate.svg" alt=""></span>
    <span class="sc-title">Start Here</span>
    <span class="sc-desc">Complete beginner? Start here.</span>
  </a>
  <a class="section-card" href="hiragana/">
    <span class="sc-icon">あ</span>
    <span class="sc-title">Hiragana</span>
    <span class="sc-desc">46 characters. The foundation.</span>
  </a>
  <a class="section-card" href="katakana/">
    <span class="sc-icon">ア</span>
    <span class="sc-title">Katakana</span>
    <span class="sc-desc">Foreign words & emphasis.</span>
  </a>
  <a class="section-card" href="kanji/">
    <span class="sc-icon">漢</span>
    <span class="sc-title">Kanji</span>
    <span class="sc-desc">50 essential beginner kanji.</span>
  </a>
  <a class="section-card" href="jlpt/">
    <span class="sc-icon"><img src="/icons/daruma.svg" alt=""></span>
    <span class="sc-title">JLPT Levels</span>
    <span class="sc-desc">N5 → N1 vocab & quizzes.</span>
  </a>
  <a class="section-card" href="numbers/">
    <span class="sc-icon">数</span>
    <span class="sc-title">Numbers</span>
    <span class="sc-desc">Count to 10,000 with audio.</span>
  </a>
  <a class="section-card" href="phrases/">
    <span class="sc-icon">話</span>
    <span class="sc-title">Phrases</span>
    <span class="sc-desc">Real sentences. Hear them spoken.</span>
  </a>
  <a class="section-card" href="grammar/">
    <span class="sc-icon">文</span>
    <span class="sc-title">Grammar</span>
    <span class="sc-desc">Particles, verb forms &amp; sentence patterns.</span>
  </a>
  <a class="section-card" href="videos/">
    <span class="sc-icon">映</span>
    <span class="sc-title">Videos</span>
    <span class="sc-desc">Latest from the YouTube channel.</span>
  </a>
</div>

---

<div class="home-phrases-wrap">
  <div class="home-phrases-hdr">
    <span class="home-phrases-title">Hear some Japanese</span>
    <span class="home-phrases-sub">Click any card to hear it spoken</span>
  </div>
  <div class="home-phrases-grid">
    <div class="hp-card" onclick="hpSpeak('おはようございます')">
      <div class="hp-play">▶</div>
      <div class="hp-jp">おはようございます</div>
      <div class="hp-read">ohayou gozaimasu</div>
      <div class="hp-en">Good morning</div>
    </div>
    <div class="hp-card" onclick="hpSpeak('ありがとうございます')">
      <div class="hp-play">▶</div>
      <div class="hp-jp">ありがとうございます</div>
      <div class="hp-read">arigatou gozaimasu</div>
      <div class="hp-en">Thank you</div>
    </div>
    <div class="hp-card" onclick="hpSpeak('すみません')">
      <div class="hp-play">▶</div>
      <div class="hp-jp">すみません</div>
      <div class="hp-read">sumimasen</div>
      <div class="hp-en">Excuse me</div>
    </div>
    <div class="hp-card" onclick="hpSpeak('いくらですか')">
      <div class="hp-play">▶</div>
      <div class="hp-jp">いくらですか？</div>
      <div class="hp-read">ikura desu ka?</div>
      <div class="hp-en">How much is it?</div>
    </div>
    <div class="hp-card" onclick="hpSpeak('どこですか')">
      <div class="hp-play">▶</div>
      <div class="hp-jp">どこですか？</div>
      <div class="hp-read">doko desu ka?</div>
      <div class="hp-en">Where is it?</div>
    </div>
    <div class="hp-card" onclick="hpSpeak('よろしくおねがいします')">
      <div class="hp-play">▶</div>
      <div class="hp-jp">よろしくお願いします</div>
      <div class="hp-read">yoroshiku onegai shimasu</div>
      <div class="hp-en">Pleased to meet you</div>
    </div>
  </div>
  <a href="/phrases/" class="hp-more">See all phrases →</a>
</div>

<script>
window.hpSpeak = function(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  var u = new SpeechSynthesisUtterance(text);
  u.lang = 'ja-JP'; u.rate = 0.82;
  window.speechSynthesis.speak(u);
};
</script>

---

<div class="jlpt-strip-wrap">
  <div class="jlpt-strip-hdr">JLPT levels — which are you aiming for?</div>
  <div class="jlpt-strip">
    <a class="jlpt-tile" href="/jlpt/n5/">
      <div class="jt-badge jt-n5">N5</div>
      <div class="jt-name">Beginner</div>
      <div class="jt-words">~800 words</div>
      <div class="jt-detail">Hiragana, katakana, basic grammar</div>
    </a>
    <a class="jlpt-tile" href="/jlpt/n4/">
      <div class="jt-badge jt-n4">N4</div>
      <div class="jt-name">Elementary</div>
      <div class="jt-words">~1,500 words</div>
      <div class="jt-detail">Everyday conversation, 300 kanji</div>
    </a>
    <a class="jlpt-tile" href="/jlpt/n3/">
      <div class="jt-badge jt-n3">N3</div>
      <div class="jt-name">Intermediate</div>
      <div class="jt-words">~3,750 words</div>
      <div class="jt-detail">News, real-world reading</div>
    </a>
    <a class="jlpt-tile" href="/jlpt/n2/">
      <div class="jt-badge jt-n2">N2</div>
      <div class="jt-name">Upper Int.</div>
      <div class="jt-words">~6,000 words</div>
      <div class="jt-detail">Most jobs in Japan require this</div>
    </a>
    <a class="jlpt-tile" href="/jlpt/n1/">
      <div class="jt-badge jt-n1">N1</div>
      <div class="jt-name">Advanced</div>
      <div class="jt-words">~10,000 words</div>
      <div class="jt-detail">Near-native reading & listening</div>
    </a>
  </div>
</div>

---

<div class="writing-systems-wrap">
  <div class="writing-systems-hdr">Three writing systems — all used at once</div>
  <div class="writing-systems-grid">
    <a class="ws-card" href="/hiragana/">
      <div class="ws-char">あ</div>
      <div class="ws-name">Hiragana</div>
      <div class="ws-count">46 characters</div>
      <div class="ws-desc">The core phonetic alphabet. Every Japanese learner starts here. Can be learned in about one week.</div>
      <div class="ws-example">例: たべる — to eat</div>
    </a>
    <a class="ws-card" href="/katakana/">
      <div class="ws-char">ア</div>
      <div class="ws-name">Katakana</div>
      <div class="ws-count">46 characters</div>
      <div class="ws-desc">Same sounds as hiragana, different shapes. Used for foreign loanwords, emphasis, and sound effects.</div>
      <div class="ws-example">例: コーヒー — coffee</div>
    </a>
    <a class="ws-card" href="/kanji/">
      <div class="ws-char">漢</div>
      <div class="ws-name">Kanji</div>
      <div class="ws-count">2,136 daily-use</div>
      <div class="ws-desc">Characters adopted from Chinese. Each carries meaning. 50 essential ones get you surprisingly far.</div>
      <div class="ws-example">例: 山 (yama) — mountain</div>
    </a>
  </div>
</div>

---

## Learning path

Each section has a reference chart you can click to hear, and an interactive quiz to drill. No account. No ads.

<div class="learn-path">
  <div class="lp-step"><span class="lp-num">1</span><div><strong><a href="/hiragana/">Hiragana</a></strong> — the foundation. 46 characters, learnable in a week.</div></div>
  <div class="lp-step"><span class="lp-num">2</span><div><strong><a href="/katakana/">Katakana</a></strong> — same sounds, different shapes. Unlocks foreign loanwords.</div></div>
  <div class="lp-step"><span class="lp-num">3</span><div><strong><a href="/grammar/">Grammar</a></strong> — particles and verb forms. These are what make sentences work.</div></div>
  <div class="lp-step"><span class="lp-num">4</span><div><strong><a href="/jlpt/n5/">JLPT N5 vocab</a></strong> — the 800 most common words. Learn these first.</div></div>
  <div class="lp-step"><span class="lp-num">5</span><div><strong><a href="/phrases/">Phrases</a></strong> — real sentences with audio. Start using Japanese as early as possible.</div></div>
  <div class="lp-step"><span class="lp-num">6</span><div><strong><a href="/kanji/">Kanji</a></strong> — pick these up gradually as you build vocabulary, not all at once.</div></div>
</div>
