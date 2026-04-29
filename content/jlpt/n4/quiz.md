---
title: "N4 Vocab Quiz"
description: "Test your JLPT N4 vocabulary. See the Japanese word — pick the correct English meaning."
date: 2025-01-01
showtoc: false
---

A Japanese word is shown — pick the correct English meaning.

<div class="quiz-wrapper">
  <div class="quiz-mode-btns">
    <button class="quiz-mode-btn active" id="btn-start" onclick="startQuiz()">Start Quiz ▶</button>
  </div>

  <div id="quiz-box" style="display:none">
    <div id="quiz-progress-bar-bg"><div id="quiz-progress-bar"></div></div>
    <div id="quiz-counter">Question 1 of 10</div>
    <div id="quiz-char" title="Click to hear" onclick="speakCurrent()" style="font-size:2.2rem;line-height:1.3">?</div>
    <div id="quiz-char-hint">Click to hear it</div>
    <div id="quiz-options"></div>
    <div id="quiz-feedback"></div>
  </div>
</div>

<script>
const VOCAB = [
  {jp:'覚える',read:'oboeru',en:'to memorise / remember'},{jp:'忘れる',read:'wasureru',en:'to forget'},
  {jp:'教える',read:'oshieru',en:'to teach / tell'},{jp:'習う',read:'narau',en:'to learn (from someone)'},
  {jp:'決める',read:'kimeru',en:'to decide'},{jp:'変わる',read:'kawaru',en:'to change'},
  {jp:'続ける',read:'tsuzukeru',en:'to continue'},{jp:'終わる',read:'owaru',en:'to end / finish'},
  {jp:'始まる',read:'hajimaru',en:'to begin'},{jp:'集まる',read:'atsumaru',en:'to gather / assemble'},
  {jp:'心配する',read:'shinpai suru',en:'to worry'},{jp:'相談する',read:'soudan suru',en:'to consult / discuss'},
  {jp:'連絡する',read:'renraku suru',en:'to contact / get in touch'},{jp:'説明する',read:'setsumei suru',en:'to explain'},
  {jp:'予約する',read:'yoyaku suru',en:'to reserve / book'},
  {jp:'もらう',read:'morau',en:'to receive'},{jp:'あげる',read:'ageru',en:'to give (to someone)'},
  {jp:'送る',read:'okuru',en:'to send'},{jp:'届く',read:'todoku',en:'to arrive / be delivered'},
  {jp:'便利な',read:'benri na',en:'convenient'},{jp:'大切な',read:'taisetsu na',en:'important / precious'},
  {jp:'特別な',read:'tokubetsu na',en:'special'},{jp:'親切な',read:'shinsetsu na',en:'kind'},
  {jp:'有名な',read:'yuumei na',en:'famous'},{jp:'安全な',read:'anzen na',en:'safe'},
  {jp:'危険な',read:'kiken na',en:'dangerous'},{jp:'複雑な',read:'fukuzatsu na',en:'complicated'},
  {jp:'丁寧な',read:'teinei na',en:'polite / careful'},{jp:'真面目な',read:'majime na',en:'serious / hardworking'},
  {jp:'賑やかな',read:'nigiyaka na',en:'lively / bustling'},{jp:'静かな',read:'shizuka na',en:'quiet'},
  {jp:'意味',read:'imi',en:'meaning'},{jp:'理由',read:'riyuu',en:'reason'},
  {jp:'問題',read:'mondai',en:'problem / question'},{jp:'答え',read:'kotae',en:'answer'},
  {jp:'質問',read:'shitsumon',en:'question (to ask)'},{jp:'結果',read:'kekka',en:'result'},
  {jp:'予定',read:'yotei',en:'plan / schedule'},{jp:'気持ち',read:'kimochi',en:'feeling'},
  {jp:'経験',read:'keiken',en:'experience'},{jp:'文化',read:'bunka',en:'culture'},
  {jp:'言葉',read:'kotoba',en:'word / language'},{jp:'場所',read:'basho',en:'place'},
  {jp:'旅行',read:'ryokou',en:'travel / trip'},{jp:'練習',read:'renshuu',en:'practice'},
  {jp:'いつも',read:'itsumo',en:'always'},{jp:'たいてい',read:'taitei',en:'usually'},
  {jp:'ときどき',read:'tokidoki',en:'sometimes'},{jp:'全然',read:'zenzen',en:'not at all'}
];

let questions = [], currentIdx = 0, score = 0, answered = false, currentItem = null;

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function startQuiz() {
  questions = shuffle(VOCAB).slice(0, 10);
  currentIdx = 0; score = 0; answered = false;
  document.getElementById('quiz-box').style.display = 'block';
  document.querySelector('.quiz-mode-btns').style.display = 'none';
  renderQuestion();
}

function renderQuestion() {
  answered = false;
  currentItem = questions[currentIdx];
  document.getElementById('quiz-progress-bar').style.width = ((currentIdx / 10) * 100) + '%';
  document.getElementById('quiz-counter').textContent = 'Question ' + (currentIdx + 1) + ' of 10';
  document.getElementById('quiz-char').textContent = currentItem.jp;
  document.getElementById('quiz-feedback').textContent = '';
  const wrongs = shuffle(VOCAB.filter(function(x){ return x.en !== currentItem.en; })).slice(0, 3);
  const options = shuffle([currentItem].concat(wrongs));
  const grid = document.getElementById('quiz-options');
  grid.innerHTML = '';
  options.forEach(function(opt) {
    const btn = document.createElement('button');
    btn.className = 'q-opt-btn';
    btn.textContent = opt.en;
    btn.style.fontSize = '0.85rem';
    btn.onclick = function(){ checkAnswer(btn, opt.en, currentItem); };
    grid.appendChild(btn);
  });
}

function checkAnswer(btn, selected, q) {
  if (answered) return;
  answered = true;
  const isCorrect = selected === q.en;
  if (isCorrect) { btn.classList.add('correct'); score++; speak(q.read); document.getElementById('quiz-feedback').textContent = '✓ Correct! ' + q.read; }
  else {
    btn.classList.add('wrong');
    document.getElementById('quiz-feedback').textContent = '✗ It was: ' + q.en + ' (' + q.read + ')';
    document.querySelectorAll('.q-opt-btn').forEach(function(b){ if (b.textContent === q.en) b.classList.add('correct'); });
    speak(q.read);
  }
  document.querySelectorAll('.q-opt-btn').forEach(function(b){ b.disabled = true; });
  setTimeout(function(){ currentIdx++; if (currentIdx < 10) { renderQuestion(); } else { showResult(); } }, 1500);
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
    '<div id="quiz-char" title="Click to hear" onclick="speakCurrent()" style="font-size:2.2rem;line-height:1.3">?</div>' +
    '<div id="quiz-char-hint">Click to hear it</div>' +
    '<div id="quiz-options"></div><div id="quiz-feedback"></div>';
  document.querySelector('.quiz-mode-btns').style.display = 'flex';
}

function speakCurrent() { if (currentItem) speak(currentItem.read); }

function speak(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'ja-JP'; u.rate = 0.85;
  window.speechSynthesis.speak(u);
}
</script>
