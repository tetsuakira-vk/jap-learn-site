---
title: "N3 Vocab Quiz"
description: "Test your JLPT N3 vocabulary. See the Japanese word — pick the correct English meaning."
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
  {jp:'受ける',read:'ukeru',en:'to receive / take an exam'},{jp:'断る',read:'kotowaru',en:'to refuse / decline'},
  {jp:'比べる',read:'kuraberu',en:'to compare'},{jp:'探す',read:'sagasu',en:'to search for'},
  {jp:'見つける',read:'mitsukeru',en:'to find'},{jp:'選ぶ',read:'erabu',en:'to choose / select'},
  {jp:'消える',read:'kieru',en:'to disappear'},{jp:'増える',read:'fueru',en:'to increase'},
  {jp:'減る',read:'heru',en:'to decrease'},{jp:'壊れる',read:'kowareru',en:'to break (intransitive)'},
  {jp:'壊す',read:'kowasu',en:'to break (transitive)'},{jp:'直す',read:'naosu',en:'to fix / correct'},
  {jp:'倒れる',read:'taoreru',en:'to fall over / collapse'},{jp:'驚く',read:'odoroku',en:'to be surprised'},
  {jp:'喜ぶ',read:'yorokobu',en:'to be pleased / rejoice'},{jp:'悩む',read:'nayamu',en:'to be troubled'},
  {jp:'諦める',read:'akirameru',en:'to give up'},{jp:'頑張る',read:'ganbaru',en:'to do one\'s best'},
  {jp:'慣れる',read:'nareru',en:'to get used to'},{jp:'変える',read:'kaeru',en:'to change (transitive)'},
  {jp:'起こる',read:'okoru',en:'to happen / occur'},{jp:'決まる',read:'kimaru',en:'to be decided'},
  {jp:'細い',read:'hosoi',en:'thin / narrow'},{jp:'太い',read:'futoi',en:'thick / fat'},
  {jp:'深い',read:'fukai',en:'deep'},{jp:'浅い',read:'asai',en:'shallow'},
  {jp:'固い',read:'katai',en:'hard / firm'},{jp:'柔らかい',read:'yawarakai',en:'soft'},
  {jp:'珍しい',read:'mezurashii',en:'rare / unusual'},{jp:'恥ずかしい',read:'hazukashii',en:'embarrassing / shy'},
  {jp:'嬉しい',read:'ureshii',en:'happy / pleased'},{jp:'悲しい',read:'kanashii',en:'sad'},
  {jp:'怖い',read:'kowai',en:'scary / frightening'},{jp:'眠い',read:'nemui',en:'sleepy'},
  {jp:'様々な',read:'samazama na',en:'various / diverse'},{jp:'正確な',read:'seikaku na',en:'accurate / precise'},
  {jp:'適切な',read:'tekisetsu na',en:'appropriate / suitable'},{jp:'豊かな',read:'yutaka na',en:'rich / abundant'},
  {jp:'無駄な',read:'muda na',en:'wasteful / pointless'},{jp:'自由な',read:'jiyuu na',en:'free / unrestricted'},
  {jp:'必要な',read:'hitsuyou na',en:'necessary'},{jp:'不思議な',read:'fushigi na',en:'mysterious / strange'},
  {jp:'性格',read:'seikaku',en:'personality / character'},{jp:'事故',read:'jiko',en:'accident'},
  {jp:'事件',read:'jiken',en:'incident / case'},{jp:'原因',read:'genin',en:'cause / reason'},
  {jp:'関係',read:'kankei',en:'relationship / connection'},{jp:'努力',read:'doryoku',en:'effort'},
  {jp:'注意',read:'chuui',en:'attention / caution'},{jp:'準備',read:'junbi',en:'preparation'},
  {jp:'計画',read:'keikaku',en:'plan / project'},{jp:'自信',read:'jishin',en:'confidence'},
  {jp:'安心',read:'anshin',en:'relief / peace of mind'},{jp:'人口',read:'jinkou',en:'population'},
  {jp:'自然',read:'shizen',en:'nature'},{jp:'科学',read:'kagaku',en:'science'},
  {jp:'習慣',read:'shuukan',en:'habit / custom'},{jp:'目的',read:'mokuteki',en:'purpose / goal'},
  {jp:'やっと',read:'yatto',en:'finally / at last'},{jp:'すっかり',read:'sukkari',en:'completely / entirely'},
  {jp:'だんだん',read:'dandan',en:'gradually'},{jp:'きっと',read:'kitto',en:'surely / certainly'},
  {jp:'まるで',read:'marude',en:'as if / just like'},{jp:'ちゃんと',read:'chanto',en:'properly / correctly'},
  {jp:'どんどん',read:'dondon',en:'rapidly / steadily'}
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
