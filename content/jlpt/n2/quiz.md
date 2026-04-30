---
title: "N2 Vocab Quiz"
description: "Test your JLPT N2 vocabulary. See the Japanese word — pick the correct English meaning."
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
  {jp:'反映する',read:'hanei suru',en:'to reflect / mirror'},{jp:'示す',read:'shimesu',en:'to show / indicate'},
  {jp:'認める',read:'mitomeru',en:'to recognise / admit'},{jp:'求める',read:'motomeru',en:'to demand / seek'},
  {jp:'述べる',read:'noberu',en:'to state / mention'},{jp:'導く',read:'michibiku',en:'to lead / guide'},
  {jp:'判断する',read:'handan suru',en:'to judge / determine'},{jp:'確認する',read:'kakunin suru',en:'to confirm / verify'},
  {jp:'実現する',read:'jitsugen suru',en:'to realise / achieve'},{jp:'解決する',read:'kaiketsu suru',en:'to solve / resolve'},
  {jp:'失う',read:'ushinau',en:'to lose'},{jp:'含む',read:'fukumu',en:'to contain / include'},
  {jp:'主張する',read:'shuchou suru',en:'to insist / claim'},{jp:'提案する',read:'teian suru',en:'to propose / suggest'},
  {jp:'指摘する',read:'shiteki suru',en:'to point out'},{jp:'促す',read:'unagasu',en:'to urge / encourage'},
  {jp:'従う',read:'shitagau',en:'to follow / obey'},{jp:'比較する',read:'hikaku suru',en:'to compare'},
  {jp:'依頼する',read:'irai suru',en:'to request / commission'},{jp:'承認する',read:'shounin suru',en:'to approve / sanction'},
  {jp:'義務',read:'gimu',en:'obligation / duty'},{jp:'権利',read:'kenri',en:'right / entitlement'},
  {jp:'責任',read:'sekinin',en:'responsibility'},{jp:'優先',read:'yuusen',en:'priority'},
  {jp:'条件',read:'jouken',en:'condition / requirement'},{jp:'基準',read:'kijun',en:'standard / criterion'},
  {jp:'範囲',read:'hani',en:'range / scope'},{jp:'限界',read:'genkai',en:'limit / boundary'},
  {jp:'目標',read:'mokuhyou',en:'goal / target'},{jp:'方針',read:'houshin',en:'policy / direction'},
  {jp:'背景',read:'haikei',en:'background / context'},{jp:'状況',read:'joukyou',en:'situation / circumstances'},
  {jp:'内容',read:'naiyou',en:'content / substance'},{jp:'手段',read:'shudan',en:'means / method'},
  {jp:'課題',read:'kadai',en:'task / challenge'},{jp:'傾向',read:'keikou',en:'tendency / trend'},
  {jp:'影響',read:'eikyou',en:'influence / effect'},{jp:'前提',read:'zentei',en:'premise / prerequisite'},
  {jp:'矛盾',read:'mujun',en:'contradiction'},{jp:'概念',read:'gainen',en:'concept / notion'},
  {jp:'妥協',read:'dakyou',en:'compromise'},{jp:'批判',read:'hihan',en:'criticism'},
  {jp:'積極的な',read:'sekkyokuteki na',en:'proactive / positive'},{jp:'消極的な',read:'shoukyokuteki na',en:'passive / negative'},
  {jp:'合理的な',read:'gouriteki na',en:'rational / logical'},{jp:'効率的な',read:'kouritsuteki na',en:'efficient'},
  {jp:'具体的な',read:'gutaiteki na',en:'concrete / specific'},{jp:'抽象的な',read:'chuushouteki na',en:'abstract'},
  {jp:'客観的な',read:'kyakukanteki na',en:'objective'},{jp:'主観的な',read:'shukanteki na',en:'subjective'},
  {jp:'したがって',read:'shitagatte',en:'therefore / consequently'},{jp:'ところが',read:'tokoro ga',en:'however (unexpected)'},
  {jp:'さらに',read:'sara ni',en:'furthermore / moreover'},{jp:'むしろ',read:'mushiro',en:'rather / instead'},
  {jp:'すなわち',read:'sunawachi',en:'namely / that is to say'},{jp:'いわば',read:'iwaba',en:'so to speak'}
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
