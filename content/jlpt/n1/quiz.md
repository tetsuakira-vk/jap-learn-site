---
title: "N1 Vocab Quiz"
description: "Test your JLPT N1 vocabulary. See the Japanese word — pick the correct English meaning."
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
    <div id="quiz-char" title="Click to hear" onclick="speakCurrent()" style="font-size:2rem;line-height:1.3">?</div>
    <div id="quiz-char-hint">Click to hear it</div>
    <div id="quiz-options"></div>
    <div id="quiz-feedback"></div>
  </div>
</div>

<script>
const VOCAB = [
  {jp:'怠る',read:'okotaru',en:'to neglect / be negligent'},{jp:'顧みる',read:'kaerimiru',en:'to reflect on / look back'},
  {jp:'阻む',read:'habamu',en:'to obstruct / prevent'},{jp:'担う',read:'ninau',en:'to take on / bear responsibility'},
  {jp:'覆す',read:'kutsugaesu',en:'to overturn / overthrow'},{jp:'培う',read:'tsuchikau',en:'to cultivate / foster'},
  {jp:'模索する',read:'mosaku suru',en:'to grope for / search out'},{jp:'克服する',read:'kokufuku suru',en:'to overcome'},
  {jp:'是正する',read:'zesei suru',en:'to correct / rectify'},{jp:'懸念する',read:'kenen suru',en:'to be concerned about'},
  {jp:'吟味する',read:'ginmi suru',en:'to scrutinise / examine closely'},{jp:'危惧する',read:'kigu suru',en:'to fear / be apprehensive'},
  {jp:'企てる',read:'kuwadateru',en:'to plan / scheme'},{jp:'抱く',read:'idaku',en:'to hold / harbour feelings'},
  {jp:'損なう',read:'sokonau',en:'to damage / impair'},
  {jp:'葛藤',read:'kattou',en:'conflict / inner struggle'},{jp:'懸念',read:'kenen',en:'concern / apprehension'},
  {jp:'逆説',read:'gyakusetsu',en:'paradox'},{jp:'弊害',read:'heigai',en:'harmful effect / abuse'},
  {jp:'根拠',read:'konkyo',en:'basis / grounds'},{jp:'見解',read:'kenkai',en:'view / opinion'},
  {jp:'動向',read:'doukou',en:'trend / movement'},{jp:'本質',read:'honshitsu',en:'essence / true nature'},
  {jp:'趣旨',read:'shushi',en:'gist / purpose'},{jp:'誤解',read:'gokai',en:'misunderstanding'},
  {jp:'齟齬',read:'sogo',en:'discrepancy / mismatch'},{jp:'忖度',read:'sontaku',en:'reading someone\'s wishes'},
  {jp:'曖昧',read:'aimai',en:'ambiguity / vagueness'},{jp:'概要',read:'gaiyou',en:'outline / summary'},
  {jp:'慣例',read:'kanrei',en:'precedent / convention'},
  {jp:'高尚な',read:'koushou na',en:'noble / refined'},{jp:'卑劣な',read:'hiretsu na',en:'despicable / mean'},
  {jp:'冷淡な',read:'reitan na',en:'cold / indifferent'},{jp:'無謀な',read:'mubou na',en:'reckless / rash'},
  {jp:'狡猾な',read:'koukatsu na',en:'cunning / sly'},{jp:'崇高な',read:'suukou na',en:'sublime / lofty'},
  {jp:'一石二鳥',read:'isseki nichou',en:'killing two birds with one stone'},
  {jp:'試行錯誤',read:'shikou sakugo',en:'trial and error'},
  {jp:'以心伝心',read:'ishin denshin',en:'unspoken understanding'},
  {jp:'自業自得',read:'jigou jitoku',en:'reaping what you sow'},
  {jp:'一期一会',read:'ichi go ichi e',en:'once in a lifetime encounter'},
  {jp:'臨機応変',read:'rinki ouhen',en:'adapting flexibly to circumstances'},
  {jp:'半信半疑',read:'hanshin hangi',en:'half-believing / doubtful'},
  {jp:'喜怒哀楽',read:'ki do ai raku',en:'the full range of human emotions'},
  {jp:'五里霧中',read:'gori muchuu',en:'at a complete loss / in the dark'}
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
    btn.style.fontSize = '0.82rem';
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
    '<div id="quiz-char" title="Click to hear" onclick="speakCurrent()" style="font-size:2rem;line-height:1.3">?</div>' +
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
