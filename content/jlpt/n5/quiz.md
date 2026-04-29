---
title: "N5 Vocab Quiz"
description: "Test your JLPT N5 vocabulary. See the Japanese word — pick the correct English meaning."
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
    <div id="quiz-char" title="Click to hear" onclick="speakCurrent()" style="font-size:2.4rem;line-height:1.3">?</div>
    <div id="quiz-char-hint">Click to hear it</div>
    <div id="quiz-options"></div>
    <div id="quiz-feedback"></div>
  </div>
</div>

<script>
const VOCAB = [
  {jp:'私',read:'watashi',en:'I, me'},{jp:'彼',read:'kare',en:'he / boyfriend'},{jp:'彼女',read:'kanojo',en:'she / girlfriend'},
  {jp:'友達',read:'tomodachi',en:'friend'},{jp:'先生',read:'sensei',en:'teacher'},{jp:'学生',read:'gakusei',en:'student'},
  {jp:'今',read:'ima',en:'now'},{jp:'今日',read:'kyou',en:'today'},{jp:'明日',read:'ashita',en:'tomorrow'},
  {jp:'昨日',read:'kinou',en:'yesterday'},{jp:'朝',read:'asa',en:'morning'},{jp:'昼',read:'hiru',en:'daytime / noon'},
  {jp:'夜',read:'yoru',en:'night'},{jp:'毎日',read:'mainichi',en:'every day'},{jp:'来週',read:'raishuu',en:'next week'},
  {jp:'家',read:'ie',en:'house / home'},{jp:'学校',read:'gakkou',en:'school'},{jp:'病院',read:'byouin',en:'hospital'},
  {jp:'駅',read:'eki',en:'station'},{jp:'店',read:'mise',en:'shop / restaurant'},{jp:'図書館',read:'toshokan',en:'library'},
  {jp:'銀行',read:'ginkou',en:'bank'},{jp:'右',read:'migi',en:'right'},{jp:'左',read:'hidari',en:'left'},
  {jp:'前',read:'mae',en:'in front / before'},{jp:'後ろ',read:'ushiro',en:'behind'},
  {jp:'ご飯',read:'gohan',en:'rice / meal'},{jp:'水',read:'mizu',en:'water'},{jp:'お茶',read:'ocha',en:'tea'},
  {jp:'卵',read:'tamago',en:'egg'},{jp:'肉',read:'niku',en:'meat'},{jp:'魚',read:'sakana',en:'fish'},
  {jp:'野菜',read:'yasai',en:'vegetables'},{jp:'果物',read:'kudamono',en:'fruit'},
  {jp:'大きい',read:'ookii',en:'big'},{jp:'小さい',read:'chiisai',en:'small'},{jp:'新しい',read:'atarashii',en:'new'},
  {jp:'古い',read:'furui',en:'old (things)'},{jp:'高い',read:'takai',en:'expensive / tall'},{jp:'安い',read:'yasui',en:'cheap'},
  {jp:'おいしい',read:'oishii',en:'delicious'},{jp:'暑い',read:'atsui',en:'hot (weather)'},{jp:'寒い',read:'samui',en:'cold (weather)'},
  {jp:'難しい',read:'muzukashii',en:'difficult'},{jp:'楽しい',read:'tanoshii',en:'fun / enjoyable'},{jp:'忙しい',read:'isogashii',en:'busy'},
  {jp:'行きます',read:'ikimasu',en:'to go'},{jp:'来ます',read:'kimasu',en:'to come'},{jp:'帰ります',read:'kaerimasu',en:'to return home'},
  {jp:'食べます',read:'tabemasu',en:'to eat'},{jp:'飲みます',read:'nomimasu',en:'to drink'},{jp:'見ます',read:'mimasu',en:'to see / watch'},
  {jp:'聞きます',read:'kikimasu',en:'to listen / ask'},{jp:'読みます',read:'yomimasu',en:'to read'},{jp:'書きます',read:'kakimasu',en:'to write'},
  {jp:'話します',read:'hanashimasu',en:'to speak / talk'},{jp:'買います',read:'kaimasu',en:'to buy'},
  {jp:'分かります',read:'wakarimasu',en:'to understand'},{jp:'起きます',read:'okimasu',en:'to wake up'},{jp:'寝ます',read:'nemasu',en:'to sleep'},
  {jp:'勉強します',read:'benkyou shimasu',en:'to study'},
  {jp:'本',read:'hon',en:'book'},{jp:'電話',read:'denwa',en:'telephone'},{jp:'車',read:'kuruma',en:'car'},
  {jp:'電車',read:'densha',en:'train'},{jp:'お金',read:'okane',en:'money'},{jp:'時計',read:'tokei',en:'watch / clock'}
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
    '<div id="quiz-char" title="Click to hear" onclick="speakCurrent()" style="font-size:2.4rem;line-height:1.3">?</div>' +
    '<div id="quiz-char-hint">Click to hear it</div>' +
    '<div id="quiz-options"></div><div id="quiz-feedback"></div>';
  document.querySelector('.quiz-mode-btns').style.display = 'flex';
}

function speakCurrent() {
  if (currentItem) speak(currentItem.read);
}

function speak(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'ja-JP'; u.rate = 0.85;
  window.speechSynthesis.speak(u);
}
</script>
