---
title: "Script Quiz — Hiragana, Katakana & Kanji"
description: "Test your Japanese script knowledge. Flash-card style quiz for hiragana, katakana, and kanji — pick your set and get started, free, no signup."
date: 2025-01-01
showtoc: false
---

<style>
/* Ported from a prototype with its own color-variable names — this maps
   them onto the live site's real theme variables, scoped to this page. */
.quiz-page {
  --serif: Georgia, 'Times New Roman', serif;
}
.quiz-page .btn {
  display: inline-block;
  padding: 10px 20px;
  border: 1.5px solid var(--primary);
  background: none;
  color: var(--primary);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .03em;
  cursor: pointer;
}
.quiz-page .btn.btn-solid {
  background: var(--primary);
  color: var(--theme);
}
.quiz-page .btn:hover { opacity: .85; }

.quiz-page .quiz-shell {
  max-width: 540px;
  margin: 0 auto;
  padding: 0 16px 60px;
}

/* ── Set picker ────────────────────────────────────────────── */
.quiz-page .picker { display: flex; flex-direction: column; gap: 20px; }

.quiz-page .picker-label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--secondary);
  margin-bottom: 4px;
}

.quiz-page .set-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
  border: 1.5px solid var(--primary);
}
@media (max-width: 420px) { .quiz-page .set-grid { grid-template-columns: repeat(2, 1fr); } }

.quiz-page .set-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 20px 10px;
  border: none;
  border-right: 1px solid var(--border);
  background: none;
  color: var(--primary);
  cursor: pointer;
  transition: background .13s;
  position: relative;
}
.quiz-page .set-btn:last-child { border-right: none; }
.quiz-page .set-btn.active { background: var(--primary); color: var(--theme); }
.quiz-page .set-btn:hover:not(.active) { background: var(--tertiary); }
.quiz-page .set-char {
  font-family: var(--serif);
  font-size: 2rem;
  font-weight: 700;
  line-height: 1;
}
.quiz-page .set-name {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
}
@media (max-width: 420px) {
  .quiz-page .set-btn { border-bottom: 1px solid var(--border); }
  .quiz-page .set-btn:nth-child(even) { border-right: none; }
  .quiz-page .set-btn:nth-last-child(-n+2) { border-bottom: none; }
}

.quiz-page .scope-row {
  display: flex;
  gap: 0;
  border: 1.5px solid var(--border);
}
.quiz-page .scope-btn {
  flex: 1;
  padding: 10px 14px;
  background: none;
  border: none;
  border-right: 1px solid var(--border);
  color: var(--secondary);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .05em;
  cursor: pointer;
  transition: background .13s, color .13s;
}
.quiz-page .scope-btn:last-child { border-right: none; }
.quiz-page .scope-btn.active { background: var(--tertiary); color: var(--primary); border-color: var(--border); }
.quiz-page .scope-row.hidden { display: none; }

.quiz-page .picker-start {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 18px;
  border: 1.5px solid var(--primary);
  cursor: pointer;
  background: var(--primary);
  color: var(--theme);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  transition: background .13s;
  user-select: none;
}
.quiz-page .picker-start:hover { background: #c0392b; border-color: #c0392b; }
.quiz-page .ps-count { font-size: 11px; opacity: .7; font-weight: 400; text-transform: none; letter-spacing: 0; }

/* ── Quiz ──────────────────────────────────────────────────── */
.quiz-page .quiz-area { display: none; }

.quiz-page .q-progress-bg {
  height: 3px;
  background: var(--border);
  margin-bottom: 22px;
}
.quiz-page .q-progress-fill {
  height: 100%;
  background: var(--primary);
  transition: width .3s ease;
}

.quiz-page .q-meta {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 16px;
}
.quiz-page .q-counter {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--secondary);
}
.quiz-page .q-set-label {
  font-size: 11px;
  color: var(--secondary);
}

.quiz-page .q-char-wrap {
  border: 1.5px solid var(--primary);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 160px;
  margin-bottom: 6px;
  background: var(--tertiary);
  cursor: pointer;
  user-select: none;
  transition: background .12s;
  position: relative;
  overflow: hidden;
}
.quiz-page .q-char-wrap:hover { background: var(--entry); }
.quiz-page .q-char {
  font-family: var(--serif);
  font-size: clamp(4rem, 15vw, 7rem);
  font-weight: 700;
  line-height: 1;
  transition: transform .08s;
}
.quiz-page .q-char-wrap:active .q-char { transform: scale(.94); }
.quiz-page .q-hint {
  font-size: 10px;
  color: var(--secondary);
  letter-spacing: .06em;
  text-transform: uppercase;
  margin-top: 10px;
}
.quiz-page .q-hint.hidden { opacity: 0; }

.quiz-page .q-opts {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  border: 1.5px solid var(--border);
  margin-bottom: 12px;
}
.quiz-page .q-opt {
  padding: 16px 12px;
  border: none;
  border-right: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  background: none;
  color: var(--primary);
  font-size: 1rem;
  font-family: var(--serif);
  font-weight: 700;
  cursor: pointer;
  transition: background .1s;
  line-height: 1.2;
}
.quiz-page .q-opt:nth-child(even) { border-right: none; }
.quiz-page .q-opt:nth-child(n+3) { border-bottom: none; }
.quiz-page .q-opt:hover:not(:disabled) { background: var(--tertiary); }
.quiz-page .q-opt.correct  { background: #538d4e; color: #fff; border-color: #538d4e; }
.quiz-page .q-opt.wrong    { background: #c0392b; color: #fff; border-color: #c0392b; }
.quiz-page .q-opt:disabled { cursor: default; }

.quiz-page .q-feedback {
  min-height: 22px;
  font-size: 13px;
  font-weight: 700;
  text-align: center;
  color: var(--secondary);
}

/* ── Result ─────────────────────────────────────────────────── */
.quiz-page .result-area { display: none; text-align: center; }
.quiz-page .result-box {
  border: 1.5px solid var(--primary);
  padding: 36px 28px;
  background: var(--tertiary);
}
.quiz-page .result-score {
  font-family: var(--serif);
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1;
  margin-bottom: 6px;
}
.quiz-page .result-pct {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--secondary);
  margin-bottom: 16px;
}
.quiz-page .result-msg {
  font-family: var(--serif);
  font-size: 1.1rem;
  margin-bottom: 28px;
}
.quiz-page .result-actions {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
}
</style>

<div class="quiz-page">
<div class="quiz-shell">

<div class="picker" id="picker">
<div>
<div class="picker-label">Choose your set</div>
<div class="set-grid">
<button class="set-btn active" data-set="hiragana" onclick="selectSet('hiragana')">
<span class="set-char">あ</span>
<span class="set-name">Hiragana</span>
</button>
<button class="set-btn" data-set="katakana" onclick="selectSet('katakana')">
<span class="set-char">ア</span>
<span class="set-name">Katakana</span>
</button>
<button class="set-btn" data-set="kanji" onclick="selectSet('kanji')">
<span class="set-char">漢</span>
<span class="set-name">Kanji</span>
</button>
<button class="set-btn" data-set="mix" onclick="selectSet('mix')">
<span class="set-char">全</span>
<span class="set-name">Mix all</span>
</button>
</div>
</div>

<div>
<div class="picker-label">Scope</div>
<div class="scope-row" id="scope-row">
<button class="scope-btn active" data-scope="basic" onclick="selectScope('basic')">Basic 46</button>
<button class="scope-btn" data-scope="all" onclick="selectScope('all')">All characters (including voiced &amp; compounds)</button>
</div>
<div class="scope-row hidden" id="scope-row-kanji">
<button class="scope-btn active" data-scope="basic" onclick="selectScope('basic')">Essential 50</button>
<button class="scope-btn" data-scope="all" onclick="selectScope('all')">All 100</button>
</div>
</div>

<div>
<div class="picker-start" id="start-btn" onclick="startQuiz()">
<span>Start quiz</span>
<span class="ps-count" id="pool-count"></span>
</div>
</div>
</div>

<div class="quiz-area" id="quiz-area">
<div class="q-progress-bg"><div class="q-progress-fill" id="q-progress" style="width:0%"></div></div>
<div class="q-meta">
<span class="q-counter" id="q-counter">Question 1 of 10</span>
<span class="q-set-label" id="q-set-label"></span>
</div>
<div class="q-char-wrap" onclick="speakCurrent()" id="q-char-wrap">
<div class="q-char" id="q-char">？</div>
<div class="q-hint" id="q-hint">Tap to hear</div>
</div>
<div class="q-opts" id="q-opts"></div>
<div class="q-feedback" id="q-feedback"></div>
</div>

<div class="result-area" id="result-area">
<div class="result-box">
<div class="result-score" id="result-score">0/10</div>
<div class="result-pct"  id="result-pct">0%</div>
<div class="result-msg"  id="result-msg"></div>
<div class="result-actions">
<button class="btn btn-solid" onclick="startQuiz()">Try again</button>
<button class="btn" onclick="showPicker()">Change set</button>
</div>
</div>
</div>

</div>
</div>

<script>
// ── Data ──────────────────────────────────────────────────────────────────
const HIRA_BASIC = [
  {char:'あ',ans:'a'},{char:'い',ans:'i'},{char:'う',ans:'u'},{char:'え',ans:'e'},{char:'お',ans:'o'},
  {char:'か',ans:'ka'},{char:'き',ans:'ki'},{char:'く',ans:'ku'},{char:'け',ans:'ke'},{char:'こ',ans:'ko'},
  {char:'さ',ans:'sa'},{char:'し',ans:'shi'},{char:'す',ans:'su'},{char:'せ',ans:'se'},{char:'そ',ans:'so'},
  {char:'た',ans:'ta'},{char:'ち',ans:'chi'},{char:'つ',ans:'tsu'},{char:'て',ans:'te'},{char:'と',ans:'to'},
  {char:'な',ans:'na'},{char:'に',ans:'ni'},{char:'ぬ',ans:'nu'},{char:'ね',ans:'ne'},{char:'の',ans:'no'},
  {char:'は',ans:'ha'},{char:'ひ',ans:'hi'},{char:'ふ',ans:'fu'},{char:'へ',ans:'he'},{char:'ほ',ans:'ho'},
  {char:'ま',ans:'ma'},{char:'み',ans:'mi'},{char:'む',ans:'mu'},{char:'め',ans:'me'},{char:'も',ans:'mo'},
  {char:'や',ans:'ya'},{char:'ゆ',ans:'yu'},{char:'よ',ans:'yo'},
  {char:'ら',ans:'ra'},{char:'り',ans:'ri'},{char:'る',ans:'ru'},{char:'れ',ans:'re'},{char:'ろ',ans:'ro'},
  {char:'わ',ans:'wa'},{char:'を',ans:'wo'},{char:'ん',ans:'n'},
];
const HIRA_EXT = [
  {char:'が',ans:'ga'},{char:'ぎ',ans:'gi'},{char:'ぐ',ans:'gu'},{char:'げ',ans:'ge'},{char:'ご',ans:'go'},
  {char:'ざ',ans:'za'},{char:'じ',ans:'ji'},{char:'ず',ans:'zu'},{char:'ぜ',ans:'ze'},{char:'ぞ',ans:'zo'},
  {char:'だ',ans:'da'},{char:'で',ans:'de'},{char:'ど',ans:'do'},
  {char:'ば',ans:'ba'},{char:'び',ans:'bi'},{char:'ぶ',ans:'bu'},{char:'べ',ans:'be'},{char:'ぼ',ans:'bo'},
  {char:'ぱ',ans:'pa'},{char:'ぴ',ans:'pi'},{char:'ぷ',ans:'pu'},{char:'ぺ',ans:'pe'},{char:'ぽ',ans:'po'},
  {char:'きゃ',ans:'kya'},{char:'きゅ',ans:'kyu'},{char:'きょ',ans:'kyo'},
  {char:'しゃ',ans:'sha'},{char:'しゅ',ans:'shu'},{char:'しょ',ans:'sho'},
  {char:'ちゃ',ans:'cha'},{char:'ちゅ',ans:'chu'},{char:'ちょ',ans:'cho'},
  {char:'にゃ',ans:'nya'},{char:'にゅ',ans:'nyu'},{char:'にょ',ans:'nyo'},
  {char:'ひゃ',ans:'hya'},{char:'ひゅ',ans:'hyu'},{char:'ひょ',ans:'hyo'},
  {char:'みゃ',ans:'mya'},{char:'みゅ',ans:'myu'},{char:'みょ',ans:'myo'},
  {char:'りゃ',ans:'rya'},{char:'りゅ',ans:'ryu'},{char:'りょ',ans:'ryo'},
];
const KATA_BASIC = [
  {char:'ア',ans:'a'},{char:'イ',ans:'i'},{char:'ウ',ans:'u'},{char:'エ',ans:'e'},{char:'オ',ans:'o'},
  {char:'カ',ans:'ka'},{char:'キ',ans:'ki'},{char:'ク',ans:'ku'},{char:'ケ',ans:'ke'},{char:'コ',ans:'ko'},
  {char:'サ',ans:'sa'},{char:'シ',ans:'shi'},{char:'ス',ans:'su'},{char:'セ',ans:'se'},{char:'ソ',ans:'so'},
  {char:'タ',ans:'ta'},{char:'チ',ans:'chi'},{char:'ツ',ans:'tsu'},{char:'テ',ans:'te'},{char:'ト',ans:'to'},
  {char:'ナ',ans:'na'},{char:'ニ',ans:'ni'},{char:'ヌ',ans:'nu'},{char:'ネ',ans:'ne'},{char:'ノ',ans:'no'},
  {char:'ハ',ans:'ha'},{char:'ヒ',ans:'hi'},{char:'フ',ans:'fu'},{char:'ヘ',ans:'he'},{char:'ホ',ans:'ho'},
  {char:'マ',ans:'ma'},{char:'ミ',ans:'mi'},{char:'ム',ans:'mu'},{char:'メ',ans:'me'},{char:'モ',ans:'mo'},
  {char:'ヤ',ans:'ya'},{char:'ユ',ans:'yu'},{char:'ヨ',ans:'yo'},
  {char:'ラ',ans:'ra'},{char:'リ',ans:'ri'},{char:'ル',ans:'ru'},{char:'レ',ans:'re'},{char:'ロ',ans:'ro'},
  {char:'ワ',ans:'wa'},{char:'ヲ',ans:'wo'},{char:'ン',ans:'n'},
];
const KATA_EXT = [
  {char:'ガ',ans:'ga'},{char:'ギ',ans:'gi'},{char:'グ',ans:'gu'},{char:'ゲ',ans:'ge'},{char:'ゴ',ans:'go'},
  {char:'ザ',ans:'za'},{char:'ジ',ans:'ji'},{char:'ズ',ans:'zu'},{char:'ゼ',ans:'ze'},{char:'ゾ',ans:'zo'},
  {char:'ダ',ans:'da'},{char:'デ',ans:'de'},{char:'ド',ans:'do'},
  {char:'バ',ans:'ba'},{char:'ビ',ans:'bi'},{char:'ブ',ans:'bu'},{char:'ベ',ans:'be'},{char:'ボ',ans:'bo'},
  {char:'パ',ans:'pa'},{char:'ピ',ans:'pi'},{char:'プ',ans:'pu'},{char:'ペ',ans:'pe'},{char:'ポ',ans:'po'},
  {char:'キャ',ans:'kya'},{char:'キュ',ans:'kyu'},{char:'キョ',ans:'kyo'},
  {char:'シャ',ans:'sha'},{char:'シュ',ans:'shu'},{char:'ショ',ans:'sho'},
  {char:'チャ',ans:'cha'},{char:'チュ',ans:'chu'},{char:'チョ',ans:'cho'},
  {char:'ニャ',ans:'nya'},{char:'ニュ',ans:'nyu'},{char:'ニョ',ans:'nyo'},
  {char:'ヒャ',ans:'hya'},{char:'ヒュ',ans:'hyu'},{char:'ヒョ',ans:'hyo'},
  {char:'ミャ',ans:'mya'},{char:'ミュ',ans:'myu'},{char:'ミョ',ans:'myo'},
  {char:'リャ',ans:'rya'},{char:'リュ',ans:'ryu'},{char:'リョ',ans:'ryo'},
];
const KANJI_BASIC = [
  {char:'日',ans:'day / sun'},{char:'月',ans:'month / moon'},{char:'火',ans:'fire'},
  {char:'水',ans:'water'},{char:'木',ans:'tree / wood'},{char:'金',ans:'gold / money'},
  {char:'土',ans:'earth / soil'},{char:'人',ans:'person'},{char:'女',ans:'woman'},
  {char:'男',ans:'man'},{char:'子',ans:'child'},{char:'学',ans:'study / learn'},
  {char:'先',ans:'previous / ahead'},{char:'生',ans:'life / birth'},{char:'山',ans:'mountain'},
  {char:'川',ans:'river'},{char:'田',ans:'rice field'},{char:'天',ans:'heaven / sky'},
  {char:'空',ans:'sky / empty'},{char:'雨',ans:'rain'},{char:'電',ans:'electricity'},
  {char:'車',ans:'car / vehicle'},{char:'校',ans:'school'},{char:'友',ans:'friend'},
  {char:'本',ans:'book / origin'},{char:'語',ans:'language / word'},{char:'読',ans:'read'},
  {char:'書',ans:'write'},{char:'聞',ans:'listen / ask'},{char:'話',ans:'speak / story'},
  {char:'買',ans:'buy'},{char:'食',ans:'eat / food'},{char:'飲',ans:'drink'},
  {char:'行',ans:'go'},{char:'来',ans:'come'},{char:'見',ans:'see / look'},
  {char:'立',ans:'stand'},{char:'入',ans:'enter'},{char:'出',ans:'exit / emerge'},
  {char:'大',ans:'big / large'},{char:'小',ans:'small'},{char:'中',ans:'middle / inside'},
  {char:'長',ans:'long / leader'},{char:'白',ans:'white'},{char:'黒',ans:'black'},
  {char:'赤',ans:'red'},{char:'青',ans:'blue / green'},{char:'名',ans:'name'},
  {char:'年',ans:'year'},{char:'時',ans:'time / hour'},
];
const KANJI_EXT = [
  {char:'国',ans:'country'},{char:'語',ans:'language'},{char:'文',ans:'writing / sentence'},
  {char:'字',ans:'character / letter'},{char:'気',ans:'spirit / feeling / air'},
  {char:'何',ans:'what / how many'},{char:'今',ans:'now / present'},
  {char:'毎',ans:'every'},{char:'週',ans:'week'},{char:'月',ans:'month / moon'},
  {char:'曜',ans:'day of the week'},{char:'朝',ans:'morning'},{char:'昼',ans:'noon / daytime'},
  {char:'夜',ans:'night'},{char:'夕',ans:'evening'},{char:'花',ans:'flower'},
  {char:'魚',ans:'fish'},{char:'肉',ans:'meat'},{char:'野',ans:'field / wild'},
  {char:'菜',ans:'vegetable'},{char:'茶',ans:'tea'},{char:'米',ans:'rice / America'},
  {char:'店',ans:'shop / store'},{char:'駅',ans:'station'},{char:'道',ans:'road / way'},
  {char:'橋',ans:'bridge'},{char:'海',ans:'sea / ocean'},{char:'池',ans:'pond'},
  {char:'公',ans:'public'},{char:'園',ans:'garden / park'},{char:'図',ans:'diagram / map'},
  {char:'館',ans:'building / hall'},{char:'会',ans:'meeting / society'},
  {char:'社',ans:'company / shrine'},{char:'員',ans:'member'},
  {char:'仕',ans:'serve / work'},{char:'事',ans:'thing / matter / work'},
  {char:'家',ans:'house / home'},{char:'族',ans:'family / tribe'},
  {char:'父',ans:'father'},{char:'母',ans:'mother'},{char:'兄',ans:'older brother'},
  {char:'姉',ans:'older sister'},{char:'弟',ans:'younger brother'},{char:'妹',ans:'younger sister'},
  {char:'友',ans:'friend'},{char:'口',ans:'mouth'},{char:'目',ans:'eye'},
  {char:'耳',ans:'ear'},{char:'手',ans:'hand'},{char:'足',ans:'foot / leg'},
];

// ── State ─────────────────────────────────────────────────────────────────
let currentSet  = 'hiragana';
let currentScope = 'basic';
let pool  = [];
let questions = [];
let qIdx  = 0;
let score = 0;
let answered = false;
let isKanji = false;

// ── Set + scope selection ─────────────────────────────────────────────────
function selectSet(s) {
  currentSet = s;
  document.querySelectorAll('.set-btn').forEach(b => b.classList.toggle('active', b.dataset.set === s));
  const isK = s === 'kanji';
  document.getElementById('scope-row').classList.toggle('hidden', isK);
  document.getElementById('scope-row-kanji').classList.toggle('hidden', !isK);
  updatePoolCount();
}

function selectScope(s) {
  currentScope = s;
  const activeRow = currentSet === 'kanji'
    ? document.querySelectorAll('#scope-row-kanji .scope-btn')
    : document.querySelectorAll('#scope-row .scope-btn');
  activeRow.forEach(b => b.classList.toggle('active', b.dataset.scope === s));
  updatePoolCount();
}

function buildPool() {
  const all = currentScope === 'all';
  switch (currentSet) {
    case 'hiragana': return all ? HIRA_BASIC.concat(HIRA_EXT) : HIRA_BASIC;
    case 'katakana': return all ? KATA_BASIC.concat(KATA_EXT) : KATA_BASIC;
    case 'kanji':    return all ? KANJI_BASIC.concat(KANJI_EXT) : KANJI_BASIC;
    case 'mix':      return (all
      ? HIRA_BASIC.concat(HIRA_EXT, KATA_BASIC, KATA_EXT, KANJI_BASIC, KANJI_EXT)
      : HIRA_BASIC.concat(KATA_BASIC, KANJI_BASIC));
  }
}

function updatePoolCount() {
  const n = buildPool().length;
  document.getElementById('pool-count').textContent = n + ' characters in pool';
}

// ── Quiz flow ─────────────────────────────────────────────────────────────
function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function startQuiz() {
  pool = buildPool();
  questions = shuffle(pool).slice(0, 10);
  qIdx = 0; score = 0; answered = false;
  isKanji = currentSet === 'kanji' || (currentSet === 'mix' && false); // updated per question

  const setLabels = { hiragana:'Hiragana', katakana:'Katakana', kanji:'Kanji', mix:'Mix' };
  document.getElementById('q-set-label').textContent = setLabels[currentSet];

  document.getElementById('picker').style.display      = 'none';
  document.getElementById('result-area').style.display = 'none';
  document.getElementById('quiz-area').style.display   = 'block';
  renderQuestion();
}

function renderQuestion() {
  answered = false;
  const q = questions[qIdx];
  const qIsKanji = KANJI_BASIC.includes(q) || KANJI_EXT.includes(q);
  const qIsKana  = !qIsKanji;

  document.getElementById('q-progress').style.width = ((qIdx / 10) * 100) + '%';
  document.getElementById('q-counter').textContent  = `Question ${qIdx + 1} of 10`;
  document.getElementById('q-char').textContent     = q.char;
  document.getElementById('q-feedback').textContent = '';
  document.getElementById('q-hint').className       = qIsKana ? 'q-hint' : 'q-hint hidden';

  const samePool = qIsKanji
    ? (currentScope === 'all' ? KANJI_BASIC.concat(KANJI_EXT) : KANJI_BASIC)
    : pool;
  const wrongs = shuffle(samePool.filter(x => x.ans !== q.ans)).slice(0, 3);
  const opts   = shuffle([q, ...wrongs]);

  const grid = document.getElementById('q-opts');
  grid.innerHTML = '';
  opts.forEach(opt => {
    const btn = document.createElement('button');
    btn.className = 'q-opt';
    btn.textContent = opt.ans;
    btn.onclick = () => checkAnswer(btn, opt.ans, q, qIsKana);
    grid.appendChild(btn);
  });
}

function checkAnswer(btn, selected, q, isKana) {
  if (answered) return;
  answered = true;
  const correct = selected === q.ans;
  if (correct) {
    btn.classList.add('correct');
    score++;
    document.getElementById('q-feedback').textContent = '✓ Correct!';
  } else {
    btn.classList.add('wrong');
    document.getElementById('q-feedback').textContent = `✗  ${q.ans}`;
    document.querySelectorAll('.q-opt').forEach(b => {
      if (b.textContent === q.ans) b.classList.add('correct');
    });
  }
  if (isKana) speak(q.char);
  document.querySelectorAll('.q-opt').forEach(b => b.disabled = true);
  setTimeout(() => {
    qIdx++;
    if (qIdx < 10) renderQuestion();
    else showResult();
  }, 1400);
}

function showResult() {
  const pct = Math.round((score / 10) * 100);
  const msg = pct === 100 ? '完璧！ Perfect score!'
            : pct >= 90  ? 'すごい！ Excellent!'
            : pct >= 80  ? 'よくできました！ Great work!'
            : pct >= 70  ? 'いいね！ Good job!'
            : pct >= 60  ? 'まあまあ！ Not bad — keep going!'
            :               'もう一度！ Keep practicing!';
  document.getElementById('result-score').textContent = `${score}/10`;
  document.getElementById('result-pct').textContent   = `${pct}%`;
  document.getElementById('result-msg').textContent   = msg;
  document.getElementById('quiz-area').style.display   = 'none';
  document.getElementById('result-area').style.display = 'block';
}

function showPicker() {
  document.getElementById('result-area').style.display = 'none';
  document.getElementById('picker').style.display      = 'flex';
  document.getElementById('picker').style.flexDirection = 'column';
}

// ── Speech ────────────────────────────────────────────────────────────────
function speakCurrent() {
  const txt = document.getElementById('q-char').textContent;
  if (txt) speak(txt);
}
function speak(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'ja-JP'; u.rate = 0.85;
  window.speechSynthesis.speak(u);
}

// ── Init ──────────────────────────────────────────────────────────────────
const urlSet = new URLSearchParams(location.search).get('set');
if (['hiragana','katakana','kanji','mix'].includes(urlSet)) selectSet(urlSet);
updatePoolCount();
</script>
