---
title: "Hiragana Quiz"
description: "Test your hiragana knowledge with this interactive multiple-choice quiz. Choose basic or all characters."
date: 2025-01-01
showtoc: false
---

Choose a character set and get started. The character is shown — pick the correct romaji reading.

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
  {kana:'あ',romaji:'a'},{kana:'い',romaji:'i'},{kana:'う',romaji:'u'},{kana:'え',romaji:'e'},{kana:'お',romaji:'o'},
  {kana:'か',romaji:'ka'},{kana:'き',romaji:'ki'},{kana:'く',romaji:'ku'},{kana:'け',romaji:'ke'},{kana:'こ',romaji:'ko'},
  {kana:'さ',romaji:'sa'},{kana:'し',romaji:'shi'},{kana:'す',romaji:'su'},{kana:'せ',romaji:'se'},{kana:'そ',romaji:'so'},
  {kana:'た',romaji:'ta'},{kana:'ち',romaji:'chi'},{kana:'つ',romaji:'tsu'},{kana:'て',romaji:'te'},{kana:'と',romaji:'to'},
  {kana:'な',romaji:'na'},{kana:'に',romaji:'ni'},{kana:'ぬ',romaji:'nu'},{kana:'ね',romaji:'ne'},{kana:'の',romaji:'no'},
  {kana:'は',romaji:'ha'},{kana:'ひ',romaji:'hi'},{kana:'ふ',romaji:'fu'},{kana:'へ',romaji:'he'},{kana:'ほ',romaji:'ho'},
  {kana:'ま',romaji:'ma'},{kana:'み',romaji:'mi'},{kana:'む',romaji:'mu'},{kana:'め',romaji:'me'},{kana:'も',romaji:'mo'},
  {kana:'や',romaji:'ya'},{kana:'ゆ',romaji:'yu'},{kana:'よ',romaji:'yo'},
  {kana:'ら',romaji:'ra'},{kana:'り',romaji:'ri'},{kana:'る',romaji:'ru'},{kana:'れ',romaji:'re'},{kana:'ろ',romaji:'ro'},
  {kana:'わ',romaji:'wa'},{kana:'を',romaji:'wo'},{kana:'ん',romaji:'n'}
];

const EXTENDED = [
  {kana:'が',romaji:'ga'},{kana:'ぎ',romaji:'gi'},{kana:'ぐ',romaji:'gu'},{kana:'げ',romaji:'ge'},{kana:'ご',romaji:'go'},
  {kana:'ざ',romaji:'za'},{kana:'じ',romaji:'ji'},{kana:'ず',romaji:'zu'},{kana:'ぜ',romaji:'ze'},{kana:'ぞ',romaji:'zo'},
  {kana:'だ',romaji:'da'},{kana:'で',romaji:'de'},{kana:'ど',romaji:'do'},
  {kana:'ば',romaji:'ba'},{kana:'び',romaji:'bi'},{kana:'ぶ',romaji:'bu'},{kana:'べ',romaji:'be'},{kana:'ぼ',romaji:'bo'},
  {kana:'ぱ',romaji:'pa'},{kana:'ぴ',romaji:'pi'},{kana:'ぷ',romaji:'pu'},{kana:'ぺ',romaji:'pe'},{kana:'ぽ',romaji:'po'},
  {kana:'きゃ',romaji:'kya'},{kana:'きゅ',romaji:'kyu'},{kana:'きょ',romaji:'kyo'},
  {kana:'しゃ',romaji:'sha'},{kana:'しゅ',romaji:'shu'},{kana:'しょ',romaji:'sho'},
  {kana:'ちゃ',romaji:'cha'},{kana:'ちゅ',romaji:'chu'},{kana:'ちょ',romaji:'cho'},
  {kana:'にゃ',romaji:'nya'},{kana:'にゅ',romaji:'nyu'},{kana:'にょ',romaji:'nyo'},
  {kana:'ひゃ',romaji:'hya'},{kana:'ひゅ',romaji:'hyu'},{kana:'ひょ',romaji:'hyo'},
  {kana:'みゃ',romaji:'mya'},{kana:'みゅ',romaji:'myu'},{kana:'みょ',romaji:'myo'},
  {kana:'りゃ',romaji:'rya'},{kana:'りゅ',romaji:'ryu'},{kana:'りょ',romaji:'ryo'}
];

let mode = 'basic';
let pool = [];
let questions = [];
let currentIdx = 0;
let score = 0;
let answered = false;

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
  currentIdx = 0;
  score = 0;
  answered = false;
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

  // Build 4 options: 1 correct + 3 wrong
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
  if (isCorrect) {
    btn.classList.add('correct');
    score++;
    speak(q.kana);
    document.getElementById('quiz-feedback').textContent = '✓ Correct!';
  } else {
    btn.classList.add('wrong');
    document.getElementById('quiz-feedback').textContent = '✗ It was: ' + q.romaji;
    document.querySelectorAll('.q-opt-btn').forEach(function(b){
      if (b.textContent === q.romaji) b.classList.add('correct');
    });
    speak(q.kana);
  }
  document.querySelectorAll('.q-opt-btn').forEach(function(b){ b.disabled = true; });
  setTimeout(function(){
    currentIdx++;
    if (currentIdx < 10) { renderQuestion(); } else { showResult(); }
  }, 1300);
}

function showResult() {
  const pct = Math.round((score / 10) * 100);
  const msgs = {
    100: '完璧！ Perfect score!',
    90:  'すごい！ Excellent!',
    80:  'よくできました！ Great work!',
    70:  'いいね！ Good job!',
    60:  'まあまあ！ Not bad — keep going!',
    0:   'もう一度！ Keep practicing!'
  };
  const msg = msgs[pct] || (pct >= 60 ? msgs[60] : msgs[0]);
  document.getElementById('quiz-box').innerHTML =
    '<div class="quiz-result">' +
    '<div class="result-score">' + score + '/10</div>' +
    '<div class="result-label">' + pct + '%</div>' +
    '<div class="result-msg">' + msg + '</div>' +
    '<button class="quiz-restart-btn" onclick="resetQuiz()">Try Again</button>' +
    '</div>';
}

function resetQuiz() {
  document.getElementById('quiz-box').style.display = 'none';
  document.getElementById('quiz-box').innerHTML =
    '<div id="quiz-progress-bar-bg"><div id="quiz-progress-bar"></div></div>' +
    '<div id="quiz-counter">Question 1 of 10</div>' +
    '<div id="quiz-char" title="Click to hear" onclick="speakCurrent()">?</div>' +
    '<div id="quiz-char-hint">Click the character to hear it</div>' +
    '<div id="quiz-options"></div>' +
    '<div id="quiz-feedback"></div>';
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
  u.lang = 'ja-JP';
  u.rate = 0.85;
  window.speechSynthesis.speak(u);
}
</script>
