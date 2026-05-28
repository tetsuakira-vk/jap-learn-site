---
title: "Shadowing Trainer — Japanese Unlocked"
description: "Train your mouth to move at Japanese speed. Listen to native-paced phrases, shadow them out loud, then see a visual rhythm comparison. No recording uploads — everything runs in your browser."
date: 2025-01-01
showtoc: false
---

<div class="sh-wrap">

<p class="sh-intro">Listen to each phrase, then repeat it out loud right after — that's shadowing. The goal isn't perfect pronunciation; it's getting your mouth used to Japanese speed and rhythm.</p>

<div class="sh-cats" id="sh-cats"></div>

<div class="sh-card" id="sh-app">
  <div style="text-align:center;padding:2rem;color:#888">Loading…</div>
</div>

<div class="sh-dots" id="sh-dots"></div>

</div>

<script>
(function(){

var sentences = [
  // Reactions
  {jp:'えっ、本当に？',        en:'What, really?',              cat:'reactions'},
  {jp:'マジで！',              en:'Seriously! / No way!',        cat:'reactions'},
  {jp:'すごいね！',            en:"That's amazing!",             cat:'reactions'},
  {jp:'やばい！',              en:'Wow! / That\'s crazy!',       cat:'reactions'},
  {jp:'なるほどね。',          en:'I see. / That makes sense.',   cat:'reactions'},
  // Texting / casual
  {jp:'ちょっと待って。',      en:'Wait a sec.',                  cat:'texting'},
  {jp:'今どこ？',              en:'Where are you?',               cat:'texting'},
  {jp:'あとで連絡するね。',    en:"I'll text you later.",         cat:'texting'},
  {jp:'了解！',                en:'Got it!',                      cat:'texting'},
  {jp:'また今度ね。',          en:'Maybe next time.',             cat:'texting'},
  // Restaurant
  {jp:'これをください。',      en:"I'll have this, please.",      cat:'restaurant'},
  {jp:'おすすめは何ですか？',  en:'What do you recommend?',       cat:'restaurant'},
  {jp:'おいしい！',            en:'Delicious!',                   cat:'restaurant'},
  {jp:'お会計をお願いします。',en:'The check, please.',           cat:'restaurant'},
  {jp:'一つお願いします。',    en:'One, please.',                 cat:'restaurant'},
  // Polite / daily
  {jp:'よろしくお願いします。',en:'Nice to meet you.',            cat:'polite'},
  {jp:'お疲れ様でした。',      en:'Good work today.',             cat:'polite'},
  {jp:'ありがとうございます。',en:'Thank you very much.',         cat:'polite'},
  {jp:'すみません。',          en:'Excuse me.',                   cat:'polite'},
  {jp:'ちょっと待ってください。',en:'Please wait a moment.',      cat:'polite'},
  // Getting around
  {jp:'駅はどこですか？',      en:'Where is the station?',        cat:'around'},
  {jp:'ここで降ります。',      en:"I'll get off here.",           cat:'around'},
  {jp:'右に曲がってください。',en:'Please turn right.',           cat:'around'},
  {jp:'どのくらいかかりますか？',en:'How long will it take?',     cat:'around'},
  {jp:'次は何駅ですか？',      en:"What's the next station?",     cat:'around'},
];

var catMeta = {
  all:        {label:'⭐ All',            color:'var(--primary)'},
  reactions:  {label:'😮 Reactions',      color:'#cc88ff'},
  texting:    {label:'💬 Texting',        color:'#88ccff'},
  restaurant: {label:'🍜 Restaurant',     color:'#ffaa66'},
  polite:     {label:'🙇 Polite',         color:'#66ccaa'},
  around:     {label:'🗺️ Getting Around', color:'#ff9999'},
};

// ── State ──
var currentIdx    = 0;
var currentCat    = 'all';
var state         = 'idle'; // idle | playing | ready | recording | done
var nativeMs      = 2000;
var nativeEnv     = [];
var userEnv       = [];
var audioCtx      = null;
var analyserNode  = null;
var mediaStream   = null;
var recordIval    = null;
var recordTimer   = null;
var visited       = {};

// ── Helpers ──
function getFiltered() {
  if (currentCat === 'all') return sentences;
  return sentences.filter(function(s){ return s.cat === currentCat; });
}

function countMorae(text) {
  var small = 'ぁぃぅぇぉゃゅょっァィゥェォャュョッ';
  var n = 0;
  for (var i = 0; i < text.length; i++) {
    var code = text.charCodeAt(i);
    var c    = text[i];
    if ((code >= 0x3040 && code <= 0x309F) || (code >= 0x30A0 && code <= 0x30FF)) {
      if (small.indexOf(c) === -1) n++;
    } else if (code >= 0x4E00 && code <= 0x9FAF) {
      n += 2;
    }
  }
  return Math.max(n, 2);
}

function generateNativeEnv(morae, durationMs) {
  var n   = Math.max(Math.ceil(durationMs / 50), 8);
  var env = [];
  for (var i = 0; i < n; i++) {
    var t     = i / (n - 1);
    var base  = Math.pow(Math.sin(Math.PI * t), 0.35) * 0.6;
    var pulse = 0.28 * Math.abs(Math.sin(morae * Math.PI * t + 0.4));
    env.push(Math.max(0.02, base + pulse));
  }
  return env;
}

// ── Canvas ──
function drawCanvas(id, samples, color, label) {
  var canvas = document.getElementById(id);
  if (!canvas) return;
  var ctx = canvas.getContext('2d');

  // Use actual rendered width for sharp canvas
  var dpr = window.devicePixelRatio || 1;
  var rect = canvas.getBoundingClientRect();
  if (rect.width > 0 && (canvas.width !== Math.round(rect.width * dpr))) {
    canvas.width  = Math.round(rect.width  * dpr);
    canvas.height = Math.round(rect.height * dpr);
    ctx.scale(dpr, dpr);
  }

  var W = rect.width  || canvas.width;
  var H = rect.height || canvas.height;

  ctx.clearRect(0, 0, W, H);
  ctx.fillStyle = '#12121e';
  ctx.fillRect(0, 0, W, H);

  // Label
  ctx.fillStyle = '#445566';
  ctx.font = '10px monospace';
  ctx.fillText(label, 8, 14);

  // Midline
  var mid = H / 2;
  ctx.beginPath();
  ctx.strokeStyle = '#222233';
  ctx.lineWidth = 1;
  ctx.moveTo(0, mid);
  ctx.lineTo(W, mid);
  ctx.stroke();

  if (!samples || samples.length < 2) return;

  // Filled waveform
  ctx.beginPath();
  ctx.moveTo(0, mid);
  for (var i = 0; i < samples.length; i++) {
    var x = (i / (samples.length - 1)) * W;
    var y = mid - samples[i] * mid * 0.82;
    ctx.lineTo(x, y);
  }
  for (var i = samples.length - 1; i >= 0; i--) {
    var x = (i / (samples.length - 1)) * W;
    var y = mid + samples[i] * mid * 0.82;
    ctx.lineTo(x, y);
  }
  ctx.closePath();
  ctx.fillStyle = color + '28';
  ctx.fill();

  // Top line
  ctx.beginPath();
  ctx.strokeStyle = color;
  ctx.lineWidth = 1.8;
  for (var i = 0; i < samples.length; i++) {
    var x = (i / (samples.length - 1)) * W;
    var y = mid - samples[i] * mid * 0.82;
    if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
  }
  ctx.stroke();

  // Bottom mirror (softer)
  ctx.beginPath();
  ctx.strokeStyle = color + '55';
  ctx.lineWidth = 1;
  for (var i = 0; i < samples.length; i++) {
    var x = (i / (samples.length - 1)) * W;
    var y = mid + samples[i] * mid * 0.82;
    if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
  }
  ctx.stroke();
}

function clearCanvas(id, label) {
  drawCanvas(id, [], '#aaa', label);
}

// ── Scoring ──
function envelopeMatch(a, b) {
  var BUCKETS = 16;
  function resample(arr) {
    var out = [];
    for (var i = 0; i < BUCKETS; i++) {
      var s = Math.floor(i * arr.length / BUCKETS);
      var e = Math.floor((i + 1) * arr.length / BUCKETS);
      if (e <= s) e = s + 1;
      var sum = 0;
      for (var j = s; j < e && j < arr.length; j++) sum += arr[j];
      out.push(sum / (e - s));
    }
    return out;
  }
  function norm(arr) {
    var mx = 0;
    for (var i = 0; i < arr.length; i++) if (arr[i] > mx) mx = arr[i];
    return mx > 0 ? arr.map(function(v){ return v / mx; }) : arr;
  }
  if (a.length < 2 || b.length < 2) return 50;
  var na = norm(resample(a)), nb = norm(resample(b));
  var diff = 0;
  for (var i = 0; i < BUCKETS; i++) diff += Math.abs(na[i] - nb[i]);
  return Math.max(0, Math.round((1 - diff / BUCKETS) * 100));
}

// ── TTS ──
function getJaVoice() {
  var voices = speechSynthesis.getVoices();
  for (var i = 0; i < voices.length; i++) {
    if (voices[i].lang.startsWith('ja')) return voices[i];
  }
  return null;
}

function doPlay(sentence) {
  if (state === 'recording') { doStopRecord(); return; }
  speechSynthesis.cancel();
  state = 'playing';

  setHint('🔊 Listening…');
  btnSet('sh-play',   '▶ Playing…', true);
  btnSet('sh-record', '⏺ Shadow', true);

  var utter = new SpeechSynthesisUtterance(sentence.jp);
  utter.lang = 'ja-JP';
  utter.rate = 0.85;
  var voice = getJaVoice();
  if (voice) utter.voice = voice;

  var t0;
  utter.onstart = function() { t0 = performance.now(); };
  utter.onend   = function() {
    var elapsed = performance.now() - t0;
    nativeMs = (elapsed > 600) ? elapsed : countMorae(sentence.jp) * 135;

    nativeEnv = generateNativeEnv(countMorae(sentence.jp), nativeMs);
    var col = (catMeta[sentence.cat] || catMeta.all).color;
    drawCanvas('sh-canvas-native', nativeEnv, col, 'Target rhythm (estimated from TTS)');

    state = 'ready';
    setHint('⬆ Shadow now! Say it out loud right after.');
    btnSet('sh-play',   '▶ Listen again', false);
    btnSet('sh-record', '⏺ Shadow', false);
    var rb = document.getElementById('sh-record');
    if (rb) rb.classList.add('sh-ready-flash');
  };

  speechSynthesis.speak(utter);
}

// ── Recording ──
function doRecord(sentence) {
  if (state === 'recording') { doStopRecord(); return; }
  if (state === 'idle') {
    setHint('⚠ Press Listen first to hear the phrase.');
    return;
  }

  state = 'recording';
  setHint('⏺ Recording… speak now!');
  btnSet('sh-play', '▶ Listen', true);
  btnSet('sh-record', '⏹ Stop', false);

  var rb = document.getElementById('sh-record');
  if (rb) { rb.classList.remove('sh-ready-flash'); rb.classList.add('sh-recording'); }

  userEnv = [];

  navigator.mediaDevices.getUserMedia({audio:true, video:false}).then(function(stream) {
    mediaStream = stream;
    audioCtx    = new (window.AudioContext || window.webkitAudioContext)();
    analyserNode = audioCtx.createAnalyser();
    analyserNode.fftSize = 1024;
    var src = audioCtx.createMediaStreamSource(stream);
    src.connect(analyserNode);

    var dataArr = new Uint8Array(analyserNode.fftSize);
    var col = (catMeta[sentence.cat] || catMeta.all).color;

    recordIval = setInterval(function() {
      if (state !== 'recording') { clearInterval(recordIval); return; }
      analyserNode.getByteTimeDomainData(dataArr);
      var sum = 0;
      for (var i = 0; i < dataArr.length; i++) {
        var v = (dataArr[i] - 128) / 128;
        sum += v * v;
      }
      userEnv.push(Math.sqrt(sum / dataArr.length));
      drawCanvas('sh-canvas-user', userEnv, '#ee6644', 'Your voice (recording…)');
    }, 50);

    var maxMs = Math.max(nativeMs * 1.8, 6000);
    recordTimer = setTimeout(doStopRecord, maxMs);

  }).catch(function(err) {
    showPermErr();
    state = 'ready';
    btnSet('sh-play', '▶ Listen again', false);
    btnSet('sh-record', '⏺ Shadow', false);
  });
}

function doStopRecord() {
  clearInterval(recordIval); recordIval = null;
  clearTimeout(recordTimer); recordTimer = null;

  if (mediaStream) { mediaStream.getTracks().forEach(function(t){ t.stop(); }); mediaStream = null; }
  if (audioCtx)    { audioCtx.close(); audioCtx = null; }

  var rb = document.getElementById('sh-record');
  if (rb) rb.classList.remove('sh-recording');

  // Trim trailing silence
  while (userEnv.length > 6 && userEnv[userEnv.length - 1] < 0.025) userEnv.pop();

  drawCanvas('sh-canvas-user', userEnv, '#ee6644', 'Your voice');

  state = 'done';
  showResults();
}

// ── Results ──
function showResults() {
  var userMs   = userEnv.length * 50;
  var ratio    = nativeMs > 0 ? userMs / nativeMs : 1;
  var tScore   = Math.round(Math.max(0, Math.min(100, 100 - Math.abs(ratio - 1) * 95)));
  var rScore   = envelopeMatch(nativeEnv, userEnv);
  var tLabel;
  if      (ratio < 0.60) tLabel = 'Much too fast — slow down a little';
  else if (ratio < 0.82) tLabel = 'A bit fast — give each syllable time';
  else if (ratio <= 1.25) tLabel = 'Good pace ✓';
  else if (ratio <= 1.55) tLabel = 'A bit slow — try to match the speed';
  else                    tLabel = 'Too slow — aim to shadow right after';

  var avg = Math.round((tScore + rScore) / 2);
  var verdict;
  if      (avg >= 80) verdict = '🎉 Excellent! Your timing is very close to natural Japanese.';
  else if (avg >= 60) verdict = '👍 Good effort — keep shadowing to tighten your rhythm.';
  else if (avg >= 40) verdict = '💪 Getting there — listen one more time then jump right in.';
  else                verdict = '🔁 Have another go — shadow immediately after you hear it.';

  var el = document.getElementById('sh-results');
  if (!el) return;
  el.innerHTML =
    '<div class="sh-score-row">' +
      '<div class="sh-score-pill sh-score-timing"><strong>' + tScore + '</strong><span>Timing</span></div>' +
      '<div class="sh-score-pill sh-score-rhythm"><strong>' + rScore + '</strong><span>Rhythm</span></div>' +
    '</div>' +
    '<div class="sh-score-detail">' + tLabel + '</div>' +
    '<div class="sh-score-verdict">' + verdict + '</div>';
  el.style.display = 'block';

  setHint('');
  btnSet('sh-play',   '▶ Listen again', false);
  btnSet('sh-record', '⏺ Shadow', true);

  var acts = document.getElementById('sh-actions');
  if (acts) acts.style.display = 'flex';

  visited[currentIdx] = true;
  updateDots();
}

// ── UI helpers ──
function setHint(txt) {
  var el = document.getElementById('sh-hint');
  if (el) el.textContent = txt;
}
function btnSet(id, txt, dis) {
  var el = document.getElementById(id);
  if (el) { el.textContent = txt; el.disabled = dis; }
}
function showPermErr() {
  setHint('🎤 Microphone blocked — please allow access in browser settings.');
}

// ── Card ──
function buildCard(sentence) {
  var catLabel = (catMeta[sentence.cat] || {label:sentence.cat}).label;
  var filtered  = getFiltered();
  var isLast    = currentIdx >= filtered.length - 1;

  return '<div class="sh-sentence">' +
    '<div class="sh-jp">' + sentence.jp + '</div>' +
    '<div class="sh-en">' + sentence.en + '</div>' +
    '<div class="sh-cat-badge">' + catLabel + '</div>' +
    '</div>' +
    '<div class="sh-controls">' +
      '<button class="sh-btn sh-btn-play" id="sh-play">▶ Listen</button>' +
      '<button class="sh-btn sh-btn-rec"  id="sh-record" disabled>⏺ Shadow</button>' +
    '</div>' +
    '<div class="sh-hint" id="sh-hint">Press Listen, then Shadow right after it ends.</div>' +
    '<div class="sh-waves">' +
      '<div class="sh-canvas-wrap"><canvas id="sh-canvas-native" style="height:80px"></canvas></div>' +
      '<div class="sh-canvas-wrap"><canvas id="sh-canvas-user"   style="height:80px"></canvas></div>' +
    '</div>' +
    '<div class="sh-results" id="sh-results" style="display:none"></div>' +
    '<div class="sh-actions" id="sh-actions" style="display:none">' +
      '<button class="sh-btn-secondary" id="sh-retry">↩ Try Again</button>' +
      '<button class="sh-btn-primary" id="sh-next-btn">' + (isLast ? '🔁 Start Over' : 'Next →') + '</button>' +
    '</div>';
}

function wireCard(sentence) {
  document.getElementById('sh-play').addEventListener('click',   function(){ doPlay(sentence); });
  document.getElementById('sh-record').addEventListener('click', function(){ doRecord(sentence); });
  document.getElementById('sh-retry').addEventListener('click',  function(){ loadSentence(currentIdx); });
  document.getElementById('sh-next-btn').addEventListener('click', function(){
    var filtered = getFiltered();
    var next = (currentIdx + 1) % filtered.length;
    loadSentence(next);
  });

  // Init blank canvases after layout
  setTimeout(function(){
    clearCanvas('sh-canvas-native', 'Target rhythm — press Listen');
    clearCanvas('sh-canvas-user',   'Your voice — press Shadow');
  }, 50);
}

function loadSentence(idx) {
  speechSynthesis.cancel();
  clearInterval(recordIval); recordIval = null;
  clearTimeout(recordTimer);  recordTimer = null;
  if (mediaStream) { mediaStream.getTracks().forEach(function(t){ t.stop(); }); mediaStream = null; }
  if (audioCtx)    { audioCtx.close(); audioCtx = null; }

  state     = 'idle';
  nativeEnv = [];
  userEnv   = [];

  var filtered = getFiltered();
  if (idx >= filtered.length) idx = 0;
  currentIdx = idx;

  var el = document.getElementById('sh-app');
  if (!el) return;
  el.innerHTML = buildCard(filtered[idx]);
  wireCard(filtered[idx]);
  updateDots();
}

// ── Category tabs ──
function buildCats() {
  var cats  = ['all','reactions','texting','restaurant','polite','around'];
  var el    = document.getElementById('sh-cats');
  if (!el) return;
  el.innerHTML = cats.map(function(c){
    var lbl = (catMeta[c] || {label:c}).label;
    return '<button class="sh-cat-btn' + (c === currentCat ? ' active' : '') +
           '" data-cat="' + c + '">' + lbl + '</button>';
  }).join('');
  el.querySelectorAll('.sh-cat-btn').forEach(function(btn){
    btn.addEventListener('click', function(){
      currentCat = this.getAttribute('data-cat');
      currentIdx = 0;
      visited    = {};
      buildCats();
      buildDots();
      loadSentence(0);
    });
  });
}

// ── Progress dots ──
function buildDots() {
  var el = document.getElementById('sh-dots');
  if (!el) return;
  var filtered = getFiltered();
  el.innerHTML = filtered.map(function(s, i){
    var cls = 'sh-dot' +
      (i === currentIdx  ? ' current' : '') +
      (visited[i]        ? ' visited' : '');
    return '<div class="' + cls + '" data-idx="' + i + '" title="' + s.jp + '"></div>';
  }).join('');
  el.querySelectorAll('.sh-dot').forEach(function(dot){
    dot.addEventListener('click', function(){
      loadSentence(parseInt(this.getAttribute('data-idx'), 10));
    });
  });
}

function updateDots() {
  var el = document.getElementById('sh-dots');
  if (!el) return;
  el.querySelectorAll('.sh-dot').forEach(function(dot, i){
    dot.className = 'sh-dot' +
      (i === currentIdx ? ' current' : '') +
      (visited[i]       ? ' visited' : '');
  });
}

// ── Boot ──
document.addEventListener('DOMContentLoaded', function(){
  // Prime voice list (async in some browsers)
  if (speechSynthesis.onvoiceschanged !== undefined) {
    speechSynthesis.onvoiceschanged = function(){ speechSynthesis.getVoices(); };
  }
  speechSynthesis.getVoices();

  buildCats();
  buildDots();
  loadSentence(0);
});

})();
</script>
