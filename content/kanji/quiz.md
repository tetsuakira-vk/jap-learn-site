---
title: "Kanji Quiz"
description: "Test your beginner kanji knowledge. See the kanji — pick the correct English meaning."
date: 2025-01-01
showtoc: false
---

A kanji is shown — pick the correct English meaning.

<div class="quiz-wrapper">
  <div class="quiz-mode-btns">
    <button class="quiz-mode-btn active" id="btn-start" onclick="startQuiz()">Start Quiz ▶</button>
  </div>

  <div id="quiz-box" style="display:none">
    <div id="quiz-progress-bar-bg"><div id="quiz-progress-bar"></div></div>
    <div id="quiz-counter">Question 1 of 10</div>
    <div id="quiz-char" title="Click to hear" onclick="speakCurrent()">?</div>
    <div id="quiz-char-hint">Click the kanji to hear it</div>
    <div id="quiz-options"></div>
    <div id="quiz-feedback"></div>
  </div>
</div>

<script>
const KANJI = [
  {kanji:'日',meaning:'day / sun'},{kanji:'月',meaning:'month / moon'},{kanji:'火',meaning:'fire'},
  {kanji:'水',meaning:'water'},{kanji:'木',meaning:'tree'},{kanji:'金',meaning:'gold / money'},
  {kanji:'土',meaning:'earth / soil'},{kanji:'人',meaning:'person'},{kanji:'女',meaning:'woman'},
  {kanji:'男',meaning:'man'},{kanji:'子',meaning:'child'},{kanji:'学',meaning:'study'},
  {kanji:'先',meaning:'previous / ahead'},{kanji:'生',meaning:'life / birth'},{kanji:'山',meaning:'mountain'},
  {kanji:'川',meaning:'river'},{kanji:'田',meaning:'rice field'},{kanji:'天',meaning:'heaven / sky'},
  {kanji:'空',meaning:'sky / empty'},{kanji:'雨',meaning:'rain'},{kanji:'電',meaning:'electricity'},
  {kanji:'車',meaning:'car / vehicle'},{kanji:'校',meaning:'school'},{kanji:'友',meaning:'friend'},
  {kanji:'本',meaning:'book / origin'},{kanji:'語',meaning:'language / word'},{kanji:'読',meaning:'read'},
  {kanji:'書',meaning:'write'},{kanji:'聞',meaning:'hear / ask'},{kanji:'話',meaning:'talk / story'},
  {kanji:'買',meaning:'buy'},{kanji:'食',meaning:'eat / food'},{kanji:'飲',meaning:'drink'},
  {kanji:'行',meaning:'go'},{kanji:'来',meaning:'come'},{kanji:'見',meaning:'see / look'},
  {kanji:'立',meaning:'stand'},{kanji:'入',meaning:'enter'},{kanji:'出',meaning:'exit / come out'},
  {kanji:'大',meaning:'big / large'},{kanji:'小',meaning:'small'},{kanji:'中',meaning:'middle / inside'},
  {kanji:'長',meaning:'long / leader'},{kanji:'白',meaning:'white'},{kanji:'黒',meaning:'black'},
  {kanji:'赤',meaning:'red'},{kanji:'青',meaning:'blue / green'},{kanji:'名',meaning:'name'},
  {kanji:'年',meaning:'year'},{kanji:'時',meaning:'time / hour'}
];

let questions = [], currentIdx = 0, score = 0, answered = false;

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function startQuiz() {
  questions = shuffle(KANJI).slice(0, 10);
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
  document.getElementById('quiz-char').textContent = q.kanji;
  document.getElementById('quiz-feedback').textContent = '';
  const wrongs = shuffle(KANJI.filter(function(x){ return x.meaning !== q.meaning; })).slice(0, 3);
  const options = shuffle([q].concat(wrongs));
  const grid = document.getElementById('quiz-options');
  grid.innerHTML = '';
  options.forEach(function(opt) {
    const btn = document.createElement('button');
    btn.className = 'q-opt-btn';
    btn.textContent = opt.meaning;
    btn.style.fontSize = '0.88rem';
    btn.onclick = function(){ checkAnswer(btn, opt.meaning, q); };
    grid.appendChild(btn);
  });
}

function checkAnswer(btn, selected, q) {
  if (answered) return;
  answered = true;
  const isCorrect = selected === q.meaning;
  if (isCorrect) { btn.classList.add('correct'); score++; speak(q.kanji); document.getElementById('quiz-feedback').textContent = '✓ Correct!'; }
  else {
    btn.classList.add('wrong');
    document.getElementById('quiz-feedback').textContent = '✗ It was: ' + q.meaning;
    document.querySelectorAll('.q-opt-btn').forEach(function(b){ if (b.textContent === q.meaning) b.classList.add('correct'); });
    speak(q.kanji);
  }
  document.querySelectorAll('.q-opt-btn').forEach(function(b){ b.disabled = true; });
  setTimeout(function(){ currentIdx++; if (currentIdx < 10) { renderQuestion(); } else { showResult(); } }, 1400);
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
    '<div id="quiz-char-hint">Click the kanji to hear it</div>' +
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
