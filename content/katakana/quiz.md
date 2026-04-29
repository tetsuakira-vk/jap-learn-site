---
title: "Katakana Quiz"
description: "Test your katakana knowledge with this interactive multiple-choice quiz."
date: 2025-01-01
showtoc: false
---

A katakana character is shown — pick the correct romaji reading.

<div class="quiz-wrapper">
  <div class="quiz-mode-btns">
    <button class="quiz-mode-btn active" id="btn-basic" onclick="setMode('basic')">Basic 46</button>
    <button class="quiz-mode-btn" id="btn-all" onclick="setMode('all')">All Characters</button>
    <button class="quiz-mode-btn" id="btn-start" onclick="startQuiz()" style="margin-left:auto">Start Quiz ▶</button>
  </div>

  <div id="quiz-box" style="display:none">
    <div id="quiz-progress-bar-bg"><div id="quiz-progress-bar"></div></div>
    <div id="quiz-counter">Question 1 of 10</div>
    <div id="quiz-char" title="Click to hear" onclick="speakCurrent()">?</div>
    <div id="quiz-char-hint">Click the character to hear it</div>
    <div id="quiz-options"></div>
    <div id="quiz-feedback"></div>
  </div>
</div>

<script>
const BASIC = [
  {kana:'ア',romaji:'a'},{kana:'イ',romaji:'i'},{kana:'ウ',romaji:'u'},{kana:'エ',romaji:'e'},{kana:'オ',romaji:'o'},
  {kana:'カ',romaji:'ka'},{kana:'キ',romaji:'ki'},{kana:'ク',romaji:'ku'},{kana:'ケ',romaji:'ke'},{kana:'コ',romaji:'ko'},
  {kana:'サ',romaji:'sa'},{kana:'シ',romaji:'shi'},{kana:'ス',romaji:'su'},{kana:'セ',romaji:'se'},{kana:'ソ',romaji:'so'},
  {kana:'タ',romaji:'ta'},{kana:'チ',romaji:'chi'},{kana:'ツ',romaji:'tsu'},{kana:'テ',romaji:'te'},{kana:'ト',romaji:'to'},
  {kana:'ナ',romaji:'na'},{kana:'ニ',romaji:'ni'},{kana:'ヌ',romaji:'nu'},{kana:'ネ',romaji:'ne'},{kana:'ノ',romaji:'no'},
  {kana:'ハ',romaji:'ha'},{kana:'ヒ',romaji:'hi'},{kana:'フ',romaji:'fu'},{kana:'ヘ',romaji:'he'},{kana:'ホ',romaji:'ho'},
  {kana:'マ',romaji:'ma'},{kana:'ミ',romaji:'mi'},{kana:'ム',romaji:'mu'},{kana:'メ',romaji:'me'},{kana:'モ',romaji:'mo'},
  {kana:'ヤ',romaji:'ya'},{kana:'ユ',romaji:'yu'},{kana:'ヨ',romaji:'yo'},
  {kana:'ラ',romaji:'ra'},{kana:'リ',romaji:'ri'},{kana:'ル',romaji:'ru'},{kana:'レ',romaji:'re'},{kana:'ロ',romaji:'ro'},
  {kana:'ワ',romaji:'wa'},{kana:'ヲ',romaji:'wo'},{kana:'ン',romaji:'n'}
];

const EXTENDED = [
  {kana:'ガ',romaji:'ga'},{kana:'ギ',romaji:'gi'},{kana:'グ',romaji:'gu'},{kana:'ゲ',romaji:'ge'},{kana:'ゴ',romaji:'go'},
  {kana:'ザ',romaji:'za'},{kana:'ジ',romaji:'ji'},{kana:'ズ',romaji:'zu'},{kana:'ゼ',romaji:'ze'},{kana:'ゾ',romaji:'zo'},
  {kana:'ダ',romaji:'da'},{kana:'デ',romaji:'de'},{kana:'ド',romaji:'do'},
  {kana:'バ',romaji:'ba'},{kana:'ビ',romaji:'bi'},{kana:'ブ',romaji:'bu'},{kana:'ベ',romaji:'be'},{kana:'ボ',romaji:'bo'},
  {kana:'パ',romaji:'pa'},{kana:'ピ',romaji:'pi'},{kana:'プ',romaji:'pu'},{kana:'ペ',romaji:'pe'},{kana:'ポ',romaji:'po'},
  {kana:'キャ',romaji:'kya'},{kana:'キュ',romaji:'kyu'},{kana:'キョ',romaji:'kyo'},
  {kana:'シャ',romaji:'sha'},{kana:'シュ',romaji:'shu'},{kana:'ショ',romaji:'sho'},
  {kana:'チャ',romaji:'cha'},{kana:'チュ',romaji:'chu'},{kana:'チョ',romaji:'cho'},
  {kana:'ニャ',romaji:'nya'},{kana:'ニュ',romaji:'nyu'},{kana:'ニョ',romaji:'nyo'},
  {kana:'ヒャ',romaji:'hya'},{kana:'ヒュ',romaji:'hyu'},{kana:'ヒョ',romaji:'hyo'},
  {kana:'ミャ',romaji:'mya'},{kana:'ミュ',romaji:'myu'},{kana:'ミョ',romaji:'myo'},
  {kana:'リャ',romaji:'rya'},{kana:'リュ',romaji:'ryu'},{kana:'リョ',romaji:'ryo'}
];

let mode = 'basic';
let pool = [], questions = [], currentIdx = 0, score = 0, answered = false;

function setMode(m) {
  mode = m;
  document.getElementById('btn-basic').classList.toggle('active', m === 'basic');
  document.getElementById('btn-all').classList.toggle('active', m === 'all');
}

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function startQuiz() {
  pool = mode === 'basic' ? BASIC : BASIC.concat(EXTENDED);
  questions = shuffle(pool).slice(0, 10);
  currentIdx = 0; score = 0; answered = false;
  document.getElementById('quiz-box').style.display = 'block';
  document.querySelector('.quiz-mode-btns').style.display = 'none';
  renderQuestion();
}

function renderQuestion() {
  answered = false;
  const q = questions[currentIdx];
  document.getElementById('quiz-progress-bar').style.width = ((currentIdx / 10) * 100) + '%';
  document.getElementById('quiz-counter').textContent = 'Question ' + (currentIdx + 1) + ' of 10';
  document.getElementById('quiz-char').textContent = q.kana;
  document.getElementById('quiz-feedback').textContent = '';
  const wrongs = shuffle(pool.filter(function(x){ return x.romaji !== q.romaji; })).slice(0, 3);
  const options = shuffle([q].concat(wrongs));
  const grid = document.getElementById('quiz-options');
  grid.innerHTML = '';
  options.forEach(function(opt) {
    const btn = document.createElement('button');
    btn.className = 'q-opt-btn';
    btn.textContent = opt.romaji;
    btn.onclick = function(){ checkAnswer(btn, opt.romaji, q); };
    grid.appendChild(btn);
  });
}

function checkAnswer(btn, selected, q) {
  if (answered) return;
  answered = true;
  const isCorrect = selected === q.romaji;
  if (isCorrect) { btn.classList.add('correct'); score++; speak(q.kana); document.getElementById('quiz-feedback').textContent = '✓ Correct!'; }
  else {
    btn.classList.add('wrong');
    document.getElementById('quiz-feedback').textContent = '✗ It was: ' + q.romaji;
    document.querySelectorAll('.q-opt-btn').forEach(function(b){ if (b.textContent === q.romaji) b.classList.add('correct'); });
    speak(q.kana);
  }
  document.querySelectorAll('.q-opt-btn').forEach(function(b){ b.disabled = true; });
  setTimeout(function(){ currentIdx++; if (currentIdx < 10) { renderQuestion(); } else { showResult(); } }, 1300);
}

function showResult() {
  const pct = Math.round((score / 10) * 100);
  const msg = pct === 100 ? '完璧！ Perfect!' : pct >= 80 ? 'すごい！ Excellent!' : pct >= 60 ? 'よくできました！ Good work!' : 'もう一度！ Keep practicing!';
  document.getElementById('quiz-box').innerHTML =
    '<div class="quiz-result"><div class="result-score">' + score + '/10</div><div class="result-label">' + pct + '%</div>' +
    '<div class="result-msg">' + msg + '</div><button class="quiz-restart-btn" onclick="resetQuiz()">Try Again</button></div>';
}

function resetQuiz() {
  document.getElementById('quiz-box').style.display = 'none';
  document.getElementById('quiz-box').innerHTML =
    '<div id="quiz-progress-bar-bg"><div id="quiz-progress-bar"></div></div>' +
    '<div id="quiz-counter">Question 1 of 10</div>' +
    '<div id="quiz-char" title="Click to hear" onclick="speakCurrent()">?</div>' +
    '<div id="quiz-char-hint">Click the character to hear it</div>' +
    '<div id="quiz-options"></div><div id="quiz-feedback"></div>';
  document.querySelector('.quiz-mode-btns').style.display = 'flex';
}

function speakCurrent() {
  const txt = document.getElementById('quiz-char').textContent;
  if (txt && txt !== '?') speak(txt);
}

function speak(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'ja-JP'; u.rate = 0.85;
  window.speechSynthesis.speak(u);
}
</script>
