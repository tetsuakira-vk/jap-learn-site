---
title: "Sentence Quiz"
description: "Japanese sentence quiz. Read the English — pick the correct Japanese sentence."
date: 2025-01-01
showtoc: false
---

Read the English sentence — pick the correct Japanese from four options. Click any Japanese option to hear it before you choose.

<div class="quiz-wrapper">
  <div class="quiz-mode-btns">
    <button class="quiz-mode-btn active" id="btn-start" onclick="startQuiz()">Start Quiz ▶</button>
  </div>

  <div id="quiz-box" style="display:none">
    <div id="quiz-progress-bar-bg"><div id="quiz-progress-bar"></div></div>
    <div id="quiz-counter">Question 1 of 10</div>
    <div id="quiz-char" style="font-size:1.25rem;line-height:1.5;text-align:center;padding:1rem 0.5rem;min-height:3.5rem">?</div>
    <div id="quiz-char-hint" style="font-size:0.76rem">Pick the Japanese translation below</div>
    <div id="quiz-options" style="display:grid;grid-template-columns:1fr;gap:0.6rem"></div>
    <div id="quiz-feedback"></div>
  </div>
</div>

<script>
const SENTENCES = [
  {en:'Good morning',jp:'おはようございます'},{en:'Hello / Good afternoon',jp:'こんにちは'},
  {en:'Good evening',jp:'こんばんは'},{en:'Goodbye',jp:'さようなら'},
  {en:'Thank you',jp:'ありがとうございます'},{en:"You're welcome",jp:'どういたしまして'},
  {en:'Excuse me / Sorry',jp:'すみません'},{en:"I'm sorry",jp:'ごめんなさい'},
  {en:'I understand',jp:'わかります'},{en:"I don't understand",jp:'わかりません'},
  {en:'One more time, please',jp:'もう一度お願いします'},{en:'Please speak slowly',jp:'ゆっくり話してください'},
  {en:'Where is it?',jp:'どこですか？'},{en:'How much is it?',jp:'いくらですか？'},
  {en:'What is your name?',jp:'名前は何ですか？'},{en:'I am a student',jp:'私は学生です'},
  {en:'I am studying Japanese',jp:'日本語を勉強しています'},{en:"I'm from the UK",jp:'私はイギリスから来ました'},
  {en:'Nice to meet you',jp:'はじめまして'},{en:'Pleased to meet you',jp:'よろしくお願いします'},
  {en:'Where is the station?',jp:'駅はどこですか？'},{en:'Where is the toilet?',jp:'トイレはどこですか？'},
  {en:'I like Japanese',jp:'日本語が好きです'},{en:'Do your best!',jp:'がんばって！'},
  {en:"I'll do my best",jp:'がんばります'},{en:'I practise every day',jp:'毎日練習します'},
  {en:'Delicious!',jp:'おいしい！'},{en:'The bill, please',jp:'お会計をお願いします'},
  {en:"I'll take this",jp:'これをください'},{en:'I want to go to Japan',jp:'日本に行きたいです'},
  {en:'Good night',jp:'おやすみなさい'},{en:"It's okay",jp:'大丈夫です'},
  {en:'Do you speak English?',jp:'英語が話せますか？'},{en:'I speak a little Japanese',jp:'日本語を少し話せます'},
  {en:'Please turn right',jp:'右に曲がってください'},{en:'Please turn left',jp:'左に曲がってください'}
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
  questions = shuffle(SENTENCES).slice(0, 10);
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
  document.getElementById('quiz-char').textContent = q.en;
  document.getElementById('quiz-feedback').textContent = '';
  const wrongs = shuffle(SENTENCES.filter(function(x){ return x.jp !== q.jp; })).slice(0, 3);
  const options = shuffle([q].concat(wrongs));
  const grid = document.getElementById('quiz-options');
  grid.innerHTML = '';
  options.forEach(function(opt) {
    const btn = document.createElement('button');
    btn.className = 'q-opt-btn';
    btn.textContent = opt.jp;
    btn.style.cssText = 'font-size:0.95rem;text-align:left;padding:0.7rem 0.8rem;height:auto;white-space:normal;';
    btn.onclick = function(e){
      if (e.target === btn) checkAnswer(btn, opt.jp, q);
    };
    // sub-label for hearing
    const hear = document.createElement('span');
    hear.textContent = ' ▶';
    hear.style.cssText = 'font-size:0.7rem;opacity:0.6;cursor:pointer;';
    hear.onclick = function(e){ e.stopPropagation(); speak(opt.jp); };
    btn.appendChild(hear);
    grid.appendChild(btn);
  });
}

function checkAnswer(btn, selected, q) {
  if (answered) return;
  answered = true;
  const isCorrect = selected === q.jp;
  if (isCorrect) { btn.classList.add('correct'); score++; speak(q.jp); document.getElementById('quiz-feedback').textContent = '✓ Correct!'; }
  else {
    btn.classList.add('wrong');
    document.getElementById('quiz-feedback').textContent = '✗ Wrong';
    document.querySelectorAll('.q-opt-btn').forEach(function(b){
      if (b.textContent.replace(' ▶','') === q.jp || b.textContent.startsWith(q.jp)) b.classList.add('correct');
    });
    speak(q.jp);
  }
  document.querySelectorAll('.q-opt-btn').forEach(function(b){ b.disabled = true; });
  setTimeout(function(){ currentIdx++; if (currentIdx < 10) { renderQuestion(); } else { showResult(); } }, 1600);
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
    '<div id="quiz-char" style="font-size:1.25rem;line-height:1.5;text-align:center;padding:1rem 0.5rem;min-height:3.5rem">?</div>' +
    '<div id="quiz-char-hint" style="font-size:0.76rem">Pick the Japanese translation below</div>' +
    '<div id="quiz-options" style="display:grid;grid-template-columns:1fr;gap:0.6rem"></div>' +
    '<div id="quiz-feedback"></div>';
  document.querySelector('.quiz-mode-btns').style.display = 'flex';
}

function speak(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'ja-JP'; u.rate = 0.82;
  window.speechSynthesis.speak(u);
}
</script>
