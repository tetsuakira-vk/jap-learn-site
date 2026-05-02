---
title: "Rhythm — Japanese Music Game"
description: "Free Japanese rhythm game in your browser. Hit the right lane as hiragana, katakana, kanji, and vocabulary notes fall to the beat. Learn Japanese through music and timing."
date: 2025-01-01
showtoc: false
---

<!-- ── MENU SCREEN ── -->
<div id="rg-menu" class="rg-active">
  <div class="rg-title">リズム — Rhythm</div>
  <div class="rg-subtitle">Notes fall to the beat — hit the correct lane before they pass.</div>

  <div class="rg-mode-grid">
    <button class="rg-mode-btn rg-mode-active" onclick="RG.setMode('hiragana',this)">
      <span class="rg-mode-icon">あ</span>
      <span class="rg-mode-label">Hiragana</span>
    </button>
    <button class="rg-mode-btn" onclick="RG.setMode('katakana',this)">
      <span class="rg-mode-icon">ア</span>
      <span class="rg-mode-label">Katakana</span>
    </button>
    <button class="rg-mode-btn" onclick="RG.setMode('kanji',this)">
      <span class="rg-mode-icon">漢</span>
      <span class="rg-mode-label">Kanji N5</span>
    </button>
    <button class="rg-mode-btn" onclick="RG.setMode('vocab',this)">
      <span class="rg-mode-icon">語</span>
      <span class="rg-mode-label">Vocab N5</span>
    </button>
  </div>

  <div class="rg-howto">
    <span>Press</span>
    <kbd class="rg-kbd rg-kbd--0">D</kbd>
    <kbd class="rg-kbd rg-kbd--1">F</kbd>
    <kbd class="rg-kbd rg-kbd--2">J</kbd>
    <kbd class="rg-kbd rg-kbd--3">K</kbd>
    <span>— or tap a lane — when the note hits the bar.</span>
  </div>

  <div class="rg-diff-heading">Difficulty</div>
  <div class="rg-diff-row">
    <button class="rg-diff-btn rg-diff-active" onclick="RG.setDiff('easy',this)">
      Easy<span class="rg-diff-sub">Slow · 4 chars</span>
    </button>
    <button class="rg-diff-btn" onclick="RG.setDiff('medium',this)">
      Medium<span class="rg-diff-sub">Steady · 6 chars</span>
    </button>
    <button class="rg-diff-btn" onclick="RG.setDiff('hard',this)">
      Hard<span class="rg-diff-sub">Fast · 8 chars</span>
    </button>
  </div>

  <button class="rg-start-btn" onclick="RG.start()">▶ &nbsp;Start</button>
</div>

<!-- ── GAME SCREEN ── -->
<div id="rg-game">
  <div class="rg-game-inner">
    <div class="rg-hud">
      <div class="rg-hud-stat">
        <span class="rg-hud-val" id="rg-score">0</span>
        <span class="rg-hud-label">Score</span>
      </div>
      <div class="rg-hud-stat">
        <span class="rg-hud-val" id="rg-combo">0</span>
        <span class="rg-hud-label">Combo</span>
      </div>
      <div class="rg-hud-stat">
        <span class="rg-hud-val rg-hud-mult" id="rg-mult">×1</span>
        <span class="rg-hud-label">Mult</span>
      </div>
      <div class="rg-hud-stat">
        <span class="rg-hud-val" id="rg-lives" style="color:#ef4444;letter-spacing:0.06em">♥♥♥♥♥</span>
        <span class="rg-hud-label">Lives</span>
      </div>
      <button class="rg-quit-btn" onclick="RG.quit()">Quit</button>
    </div>

    <div class="rg-canvas-wrap">
      <canvas id="rg-canvas"></canvas>
      <div class="rg-hit-layer">
        <div class="rg-hit-cell"><span class="rg-hit-text" id="rg-ht0"></span></div>
        <div class="rg-hit-cell"><span class="rg-hit-text" id="rg-ht1"></span></div>
        <div class="rg-hit-cell"><span class="rg-hit-text" id="rg-ht2"></span></div>
        <div class="rg-hit-cell"><span class="rg-hit-text" id="rg-ht3"></span></div>
      </div>
    </div>

    <div class="rg-lane-row">
      <div class="rg-lane-cell" data-lane="0" onclick="RG.pressLane(0)">
        <span class="rg-lane-key">D</span>
        <span class="rg-lane-romaji" id="rg-l0">—</span>
      </div>
      <div class="rg-lane-cell" data-lane="1" onclick="RG.pressLane(1)">
        <span class="rg-lane-key">F</span>
        <span class="rg-lane-romaji" id="rg-l1">—</span>
      </div>
      <div class="rg-lane-cell" data-lane="2" onclick="RG.pressLane(2)">
        <span class="rg-lane-key">J</span>
        <span class="rg-lane-romaji" id="rg-l2">—</span>
      </div>
      <div class="rg-lane-cell" data-lane="3" onclick="RG.pressLane(3)">
        <span class="rg-lane-key">K</span>
        <span class="rg-lane-romaji" id="rg-l3">—</span>
      </div>
    </div>
  </div>
</div>

<!-- ── RESULT SCREEN ── -->
<div id="rg-over">
  <div class="rg-result-box">
    <div class="rg-result-grade" id="rg-grade">S</div>
    <div class="rg-result-rank-label">Rank</div>
    <div class="rg-result-score" id="rg-final-score">0</div>
    <div class="rg-result-breakdown" id="rg-breakdown"></div>
    <div class="rg-result-btns">
      <button class="rg-result-btn rg-result-btn--play" onclick="RG.playAgain()">Play Again</button>
      <button class="rg-result-btn rg-result-btn--menu" onclick="RG.menu()">Menu</button>
    </div>
  </div>
</div>

<script>
(function () {
  'use strict';

  /* ── CONSTANTS ── */
  var LANE_COLORS = ['#ef4444', '#f97316', '#3b82f6', '#a855f7'];
  var KEY_MAP = { KeyD: 0, KeyF: 1, KeyJ: 2, KeyK: 3 };

  var DIFF_CFG = {
    easy:   { bpm: 70,  speed: 200, beatsPerNote: 2.0 },
    medium: { bpm: 90,  speed: 270, beatsPerNote: 1.5 },
    hard:   { bpm: 120, speed: 350, beatsPerNote: 1.0 }
  };

  /* ── DATA ── */
  var DATA = {
    hiragana: [
      {jp:'あ',en:'a'},{jp:'い',en:'i'},{jp:'う',en:'u'},{jp:'え',en:'e'},{jp:'お',en:'o'},
      {jp:'か',en:'ka'},{jp:'き',en:'ki'},{jp:'く',en:'ku'},{jp:'け',en:'ke'},{jp:'こ',en:'ko'},
      {jp:'さ',en:'sa'},{jp:'し',en:'shi'},{jp:'す',en:'su'},{jp:'せ',en:'se'},{jp:'そ',en:'so'},
      {jp:'た',en:'ta'},{jp:'ち',en:'chi'},{jp:'つ',en:'tsu'},{jp:'て',en:'te'},{jp:'と',en:'to'},
      {jp:'な',en:'na'},{jp:'に',en:'ni'},{jp:'ぬ',en:'nu'},{jp:'ね',en:'ne'},{jp:'の',en:'no'},
      {jp:'は',en:'ha'},{jp:'ひ',en:'hi'},{jp:'ふ',en:'fu'},{jp:'へ',en:'he'},{jp:'ほ',en:'ho'},
      {jp:'ま',en:'ma'},{jp:'み',en:'mi'},{jp:'む',en:'mu'},{jp:'め',en:'me'},{jp:'も',en:'mo'},
      {jp:'や',en:'ya'},{jp:'ゆ',en:'yu'},{jp:'よ',en:'yo'},
      {jp:'ら',en:'ra'},{jp:'り',en:'ri'},{jp:'る',en:'ru'},{jp:'れ',en:'re'},{jp:'ろ',en:'ro'},
      {jp:'わ',en:'wa'},{jp:'を',en:'wo'},{jp:'ん',en:'n'},
      {jp:'が',en:'ga'},{jp:'ぎ',en:'gi'},{jp:'ぐ',en:'gu'},{jp:'げ',en:'ge'},{jp:'ご',en:'go'},
      {jp:'ざ',en:'za'},{jp:'じ',en:'ji'},{jp:'ず',en:'zu'},{jp:'ぞ',en:'zo'},
      {jp:'だ',en:'da'},{jp:'で',en:'de'},{jp:'ど',en:'do'},
      {jp:'ば',en:'ba'},{jp:'び',en:'bi'},{jp:'ぶ',en:'bu'},{jp:'べ',en:'be'},{jp:'ぼ',en:'bo'},
      {jp:'ぱ',en:'pa'},{jp:'ぴ',en:'pi'},{jp:'ぷ',en:'pu'},{jp:'ぺ',en:'pe'},{jp:'ぽ',en:'po'}
    ],
    katakana: [
      {jp:'ア',en:'a'},{jp:'イ',en:'i'},{jp:'ウ',en:'u'},{jp:'エ',en:'e'},{jp:'オ',en:'o'},
      {jp:'カ',en:'ka'},{jp:'キ',en:'ki'},{jp:'ク',en:'ku'},{jp:'ケ',en:'ke'},{jp:'コ',en:'ko'},
      {jp:'サ',en:'sa'},{jp:'シ',en:'shi'},{jp:'ス',en:'su'},{jp:'セ',en:'se'},{jp:'ソ',en:'so'},
      {jp:'タ',en:'ta'},{jp:'チ',en:'chi'},{jp:'ツ',en:'tsu'},{jp:'テ',en:'te'},{jp:'ト',en:'to'},
      {jp:'ナ',en:'na'},{jp:'ニ',en:'ni'},{jp:'ヌ',en:'nu'},{jp:'ネ',en:'ne'},{jp:'ノ',en:'no'},
      {jp:'ハ',en:'ha'},{jp:'ヒ',en:'hi'},{jp:'フ',en:'fu'},{jp:'ヘ',en:'he'},{jp:'ホ',en:'ho'},
      {jp:'マ',en:'ma'},{jp:'ミ',en:'mi'},{jp:'ム',en:'mu'},{jp:'メ',en:'me'},{jp:'モ',en:'mo'},
      {jp:'ヤ',en:'ya'},{jp:'ユ',en:'yu'},{jp:'ヨ',en:'yo'},
      {jp:'ラ',en:'ra'},{jp:'リ',en:'ri'},{jp:'ル',en:'ru'},{jp:'レ',en:'re'},{jp:'ロ',en:'ro'},
      {jp:'ワ',en:'wa'},{jp:'ヲ',en:'wo'},{jp:'ン',en:'n'},
      {jp:'ガ',en:'ga'},{jp:'ギ',en:'gi'},{jp:'グ',en:'gu'},{jp:'ゲ',en:'ge'},{jp:'ゴ',en:'go'},
      {jp:'ザ',en:'za'},{jp:'ジ',en:'ji'},{jp:'ズ',en:'zu'},{jp:'ゾ',en:'zo'},
      {jp:'ダ',en:'da'},{jp:'デ',en:'de'},{jp:'ド',en:'do'},
      {jp:'バ',en:'ba'},{jp:'ビ',en:'bi'},{jp:'ブ',en:'bu'},{jp:'ベ',en:'be'},{jp:'ボ',en:'bo'},
      {jp:'パ',en:'pa'},{jp:'ピ',en:'pi'},{jp:'プ',en:'pu'},{jp:'ペ',en:'pe'},{jp:'ポ',en:'po'}
    ],
    kanji: [
      {jp:'一',en:'one'},{jp:'二',en:'two'},{jp:'三',en:'three'},{jp:'四',en:'four'},{jp:'五',en:'five'},
      {jp:'六',en:'six'},{jp:'七',en:'seven'},{jp:'八',en:'eight'},{jp:'九',en:'nine'},{jp:'十',en:'ten'},
      {jp:'百',en:'hundred'},{jp:'千',en:'thousand'},{jp:'万',en:'10,000'},
      {jp:'日',en:'day'},{jp:'月',en:'month'},{jp:'火',en:'fire'},{jp:'水',en:'water'},
      {jp:'木',en:'tree'},{jp:'金',en:'gold'},{jp:'土',en:'earth'},
      {jp:'山',en:'mountain'},{jp:'川',en:'river'},{jp:'田',en:'rice field'},{jp:'林',en:'grove'},{jp:'森',en:'forest'},
      {jp:'人',en:'person'},{jp:'女',en:'woman'},{jp:'男',en:'man'},{jp:'子',en:'child'},{jp:'口',en:'mouth'},
      {jp:'手',en:'hand'},{jp:'目',en:'eye'},{jp:'耳',en:'ear'},{jp:'足',en:'foot'},{jp:'力',en:'power'},
      {jp:'大',en:'big'},{jp:'小',en:'small'},{jp:'中',en:'middle'},{jp:'上',en:'above'},{jp:'下',en:'below'},
      {jp:'左',en:'left'},{jp:'右',en:'right'},{jp:'前',en:'front'},{jp:'後',en:'behind'},
      {jp:'本',en:'book'},{jp:'車',en:'car'},{jp:'気',en:'spirit'},{jp:'学',en:'study'},
      {jp:'生',en:'life'},{jp:'年',en:'year'}
    ],
    vocab: [
      {jp:'いぬ',en:'dog'},{jp:'ねこ',en:'cat'},{jp:'さかな',en:'fish'},{jp:'とり',en:'bird'},{jp:'うま',en:'horse'},
      {jp:'みず',en:'water'},{jp:'ごはん',en:'rice'},{jp:'パン',en:'bread'},{jp:'にく',en:'meat'},{jp:'たまご',en:'egg'},
      {jp:'あか',en:'red'},{jp:'あお',en:'blue'},{jp:'しろ',en:'white'},{jp:'くろ',en:'black'},{jp:'きいろ',en:'yellow'},
      {jp:'おおきい',en:'big'},{jp:'ちいさい',en:'small'},{jp:'あたらしい',en:'new'},{jp:'ふるい',en:'old'},{jp:'たかい',en:'tall'},
      {jp:'あさ',en:'morning'},{jp:'ひる',en:'noon'},{jp:'よる',en:'night'},{jp:'きょう',en:'today'},{jp:'あした',en:'tomorrow'},
      {jp:'でんしゃ',en:'train'},{jp:'バス',en:'bus'},{jp:'くるま',en:'car'},{jp:'ひこうき',en:'airplane'},
      {jp:'がっこう',en:'school'},{jp:'びょういん',en:'hospital'},{jp:'えき',en:'station'},{jp:'みせ',en:'shop'},{jp:'うち',en:'home'},
      {jp:'たべる',en:'to eat'},{jp:'のむ',en:'to drink'},{jp:'みる',en:'to see'},{jp:'きく',en:'to listen'},{jp:'はなす',en:'to speak'},
      {jp:'すき',en:'like'},{jp:'きらい',en:'dislike'},{jp:'げんき',en:'healthy'},{jp:'しずか',en:'quiet'},
      {jp:'いくら',en:'how much'},{jp:'どこ',en:'where'},{jp:'だれ',en:'who'},{jp:'なに',en:'what'},{jp:'いつ',en:'when'}
    ]
  };

  /* ── HIT WINDOWS (px from hit zone centre) ── */
  var HIT_PERFECT = 35;
  var HIT_GOOD    = 65;
  var MISS_PAST   = 70;   /* px past hitY before auto-miss */
  var MAX_LIVES   = 5;

  /* ── STATE ── */
  var S = {
    mode: 'hiragana', diff: 'easy',
    notes: [],
    score: 0, combo: 0, maxCombo: 0, mult: 1,
    perfect: 0, good: 0, miss: 0, total: 0,
    lives: MAX_LIVES,
    running: false, animId: null,
    /* audio */
    audioCtx: null, masterGain: null,
    beatCount: 0, nextBeatTime: 0, beatInt: null,
    /* lane */
    laneItems: [], laneActive: [false, false, false, false],
    spawnTimer: 0, bpm: 70, speed: 200, interval: 1.71,
    W: 600, H: 460, dpr: 1
  };

  /* pre-created noise buffers */
  var snareBuffer = null;
  var hihatBuffer = null;

  /* ── HELPERS ── */
  function el(id) { return document.getElementById(id); }

  function show(id) {
    ['rg-menu', 'rg-game', 'rg-over'].forEach(function (s) {
      var e = el(s); if (!e) return;
      e.classList.remove('rg-active'); e.style.display = '';
    });
    var t = el(id);
    if (t) { t.classList.add('rg-active'); t.style.display = 'block'; }
  }

  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
    }
    return a;
  }

  /* ── CANVAS SETUP ── */
  function setupCanvas() {
    var canvas = el('rg-canvas');
    if (!canvas) return;
    var dpr = window.devicePixelRatio || 1;
    var W = canvas.parentElement.clientWidth || 600;
    var H = parseInt(window.getComputedStyle(canvas).height, 10) || 460;
    canvas.width  = Math.round(W * dpr);
    canvas.height = Math.round(H * dpr);
    S.W = W; S.H = H; S.dpr = dpr;
  }

  /* ── LANE SETUP ── */
  function setupLanes() {
    var pool = shuffle(DATA[S.mode]);
    S.laneItems = pool.slice(0, 4);
    for (var i = 0; i < 4; i++) {
      var lbl = el('rg-l' + i);
      if (lbl) lbl.textContent = S.laneItems[i].en;
    }
  }

  /* ═══════════════════════════════════════
     WEB AUDIO BEAT SYNTHESISER
  ═══════════════════════════════════════ */

  function ensureAudio() {
    if (!S.audioCtx) {
      try { S.audioCtx = new (window.AudioContext || window.webkitAudioContext)(); }
      catch (e) { return false; }
    }
    if (S.audioCtx.state === 'suspended') S.audioCtx.resume();
    return true;
  }

  function initBuffers() {
    var ac = S.audioCtx, sr = ac.sampleRate;
    /* snare — 140 ms white noise */
    var sLen = Math.ceil(sr * 0.14);
    snareBuffer = ac.createBuffer(1, sLen, sr);
    var sd = snareBuffer.getChannelData(0);
    for (var i = 0; i < sLen; i++) sd[i] = Math.random() * 2 - 1;
    /* hi-hat — 45 ms white noise */
    var hLen = Math.ceil(sr * 0.045);
    hihatBuffer = ac.createBuffer(1, hLen, sr);
    var hd = hihatBuffer.getChannelData(0);
    for (var j = 0; j < hLen; j++) hd[j] = Math.random() * 2 - 1;
  }

  function playKick(when) {
    var ac = S.audioCtx;
    var osc  = ac.createOscillator();
    var gain = ac.createGain();
    osc.connect(gain);
    gain.connect(S.masterGain);
    osc.frequency.setValueAtTime(100, when);
    osc.frequency.exponentialRampToValueAtTime(0.001, when + 0.38);
    gain.gain.setValueAtTime(1.0, when);
    gain.gain.exponentialRampToValueAtTime(0.001, when + 0.38);
    osc.start(when); osc.stop(when + 0.4);
  }

  function playSnare(when) {
    var ac  = S.audioCtx;
    var src = ac.createBufferSource();
    src.buffer = snareBuffer;
    var flt = ac.createBiquadFilter();
    flt.type = 'highpass'; flt.frequency.value = 1800;
    var gain = ac.createGain();
    gain.gain.setValueAtTime(0.65, when);
    gain.gain.exponentialRampToValueAtTime(0.001, when + 0.14);
    src.connect(flt); flt.connect(gain); gain.connect(S.masterGain);
    src.start(when); src.stop(when + 0.15);
  }

  function playHihat(when, open) {
    var ac  = S.audioCtx;
    var src = ac.createBufferSource();
    src.buffer = hihatBuffer;
    var flt = ac.createBiquadFilter();
    flt.type = 'highpass'; flt.frequency.value = 10000;
    var dur  = open ? 0.045 : 0.022;
    var gain = ac.createGain();
    gain.gain.setValueAtTime(0.28, when);
    gain.gain.exponentialRampToValueAtTime(0.001, when + dur);
    src.connect(flt); flt.connect(gain); gain.connect(S.masterGain);
    src.start(when); src.stop(when + dur + 0.005);
  }

  function playBeat(when, step) {
    switch (step % 4) {
      case 0: playKick(when); playHihat(when, true);             break;
      case 1:                 playHihat(when, false);            break;
      case 2: playKick(when); playSnare(when); playHihat(when, true); break;
      case 3:                 playHihat(when, false);            break;
    }
  }

  function scheduleBeat() {
    if (!S.audioCtx || !S.running) return;
    var lookahead = 0.1;
    var now = S.audioCtx.currentTime;
    while (S.nextBeatTime < now + lookahead) {
      playBeat(S.nextBeatTime, S.beatCount);
      S.nextBeatTime += 60 / S.bpm;
      S.beatCount++;
    }
  }

  function startBeat() {
    if (!ensureAudio()) return;
    if (S.masterGain) { try { S.masterGain.disconnect(); } catch (e) {} }
    S.masterGain = S.audioCtx.createGain();
    S.masterGain.gain.value = 0.45;
    S.masterGain.connect(S.audioCtx.destination);
    initBuffers();
    S.beatCount = 0;
    S.nextBeatTime = S.audioCtx.currentTime + 0.08;
    clearInterval(S.beatInt);
    S.beatInt = setInterval(scheduleBeat, 25);
  }

  function stopBeat() {
    clearInterval(S.beatInt);
    S.beatInt = null;
    if (S.audioCtx) { try { S.audioCtx.suspend(); } catch (e) {} }
  }

  /* ═══════════════════════════════════════
     HIT DETECTION & SCORING
  ═══════════════════════════════════════ */

  function updateHUD() {
    el('rg-score').textContent = S.score.toLocaleString();
    el('rg-combo').textContent = S.combo;
    el('rg-mult').textContent  = '×' + S.mult;
    var hearts = '';
    for (var i = 0; i < MAX_LIVES; i++) hearts += i < S.lives ? '♥' : '♡';
    el('rg-lives').textContent = hearts;
  }

  function showHitText(lane, quality) {
    var htEl = el('rg-ht' + lane);
    if (!htEl) return;
    htEl.className = 'rg-hit-text rg-hit-text--' + quality.toLowerCase() + ' rg-show';
    htEl.textContent = quality;
    clearTimeout(htEl._t);
    htEl._t = setTimeout(function () { htEl.classList.remove('rg-show'); }, 550);
  }

  function registerHit(note, quality) {
    note.hit   = true;
    note.alpha = 0;
    S.combo++;
    if (S.combo > S.maxCombo) S.maxCombo = S.combo;
    S.mult = S.combo >= 40 ? 4 : S.combo >= 20 ? 3 : S.combo >= 10 ? 2 : 1;
    var pts = (quality === 'PERFECT' ? 100 : 50) * S.mult;
    S.score += pts;
    if (quality === 'PERFECT') S.perfect++; else S.good++;
    showHitText(note.lane, quality);
    updateHUD();
  }

  function registerMiss(note) {
    if (note.missed) return;
    note.missed = true;
    S.combo = 0;
    S.mult  = 1;
    S.miss++;
    S.lives = Math.max(0, S.lives - 1);
    showHitText(note.lane, 'MISS');
    updateHUD();
    /* canvas shake */
    var wrap = el('rg-canvas') && el('rg-canvas').parentElement;
    if (wrap) {
      wrap.classList.remove('rg-shake');
      void wrap.offsetWidth; /* reflow to restart animation */
      wrap.classList.add('rg-shake');
      setTimeout(function () { wrap.classList.remove('rg-shake'); }, 300);
    }
    if (S.lives <= 0) {
      setTimeout(function () {
        S.running = false;
        cancelAnimationFrame(S.animId);
        stopBeat();
        showResult();
      }, 600);
    }
  }

  function tryHit(lane) {
    var hitY = S.H - 68;
    var best = null, bestDist = Infinity;
    for (var i = 0; i < S.notes.length; i++) {
      var note = S.notes[i];
      if (note.lane !== lane || note.hit || note.missed) continue;
      var dist = Math.abs(note.y - hitY);
      if (dist < bestDist) { bestDist = dist; best = note; }
    }
    if (!best) return;
    if (bestDist <= HIT_PERFECT)      registerHit(best, 'PERFECT');
    else if (bestDist <= HIT_GOOD)    registerHit(best, 'GOOD');
    /* outside window — press does nothing; miss fires in update() */
  }

  /* ── NOTE SPAWN ── */
  function spawnNote() {
    var lane = Math.floor(Math.random() * 4);
    S.notes.push({ lane: lane, item: S.laneItems[lane], y: -30,
                   hit: false, missed: false, alpha: 1 });
    S.total++;
  }

  /* ── ROUND RECT ── */
  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h - r);
    ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    ctx.lineTo(x + r, y + h);
    ctx.quadraticCurveTo(x, y + h, x, y + h - r);
    ctx.lineTo(x, y + r);
    ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
  }

  /* ── NOTE DRAW ── */
  function drawNote(ctx, note, laneW) {
    if (note.alpha <= 0) return;
    var cx    = (note.lane + 0.5) * laneW;
    var noteW = laneW * 0.70;
    var noteH = 52;
    var x     = cx - noteW / 2;
    var y     = note.y - noteH / 2;
    /* missed notes go gray */
    var color = note.missed ? '#4b5563' : LANE_COLORS[note.lane];
    /* glow brightens as note approaches hit zone */
    var hitY     = S.H - 68;
    var dist     = hitY - note.y;
    var glowMult = (!note.missed && dist > 0 && dist < 120) ? 1 + (1 - dist / 120) * 0.8 : 1;

    ctx.save();
    ctx.globalAlpha = note.alpha;
    ctx.shadowColor = color;
    ctx.shadowBlur  = 14 * glowMult;

    roundRect(ctx, x, y, noteW, noteH, 10);
    ctx.fillStyle = '#0e0e1c'; ctx.fill();

    roundRect(ctx, x, y, noteW, noteH, 10);
    ctx.strokeStyle = color; ctx.lineWidth = 2.5; ctx.stroke();
    ctx.shadowBlur = 0;

    var grad = ctx.createLinearGradient(x, y, x, y + noteH * 0.4);
    grad.addColorStop(0, color + '30'); grad.addColorStop(1, 'transparent');
    roundRect(ctx, x + 1, y + 1, noteW - 2, noteH - 2, 9);
    ctx.fillStyle = grad; ctx.fill();

    var text  = note.item.jp;
    var fsize = text.length <= 1 ? 26 : text.length <= 2 ? 21 : text.length <= 4 ? 16 : 12;
    ctx.fillStyle    = note.missed ? '#9ca3af' : '#ffffff';
    ctx.font         = 'bold ' + fsize + 'px system-ui, "Hiragino Sans", sans-serif';
    ctx.textAlign    = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(text, cx, note.y, noteW - 8);
    ctx.restore();
  }

  /* ── RENDER ── */
  function render() {
    var canvas = el('rg-canvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var W = S.W, H = S.H, dpr = S.dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    var laneW = W / 4;
    var hitY  = H - 68;

    ctx.fillStyle = '#070710'; ctx.fillRect(0, 0, W, H);

    /* lane tints */
    for (var i = 0; i < 4; i++) {
      var lx = i * laneW;
      if (i % 2 === 0) { ctx.fillStyle = 'rgba(255,255,255,0.013)'; ctx.fillRect(lx, 0, laneW, H); }
      var gBot = ctx.createLinearGradient(0, hitY - 110, 0, H);
      gBot.addColorStop(0, 'transparent'); gBot.addColorStop(1, LANE_COLORS[i] + '22');
      ctx.fillStyle = gBot; ctx.fillRect(lx, 0, laneW, H);
    }

    /* beat grid */
    ctx.strokeStyle = 'rgba(255,255,255,0.03)'; ctx.lineWidth = 1;
    for (var gy = 60; gy < H - 80; gy += 60) {
      ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(W, gy); ctx.stroke();
    }

    /* lane dividers */
    ctx.strokeStyle = 'rgba(255,255,255,0.07)'; ctx.lineWidth = 1;
    for (var j = 1; j < 4; j++) {
      ctx.beginPath(); ctx.moveTo(j * laneW, 0); ctx.lineTo(j * laneW, H); ctx.stroke();
    }

    /* notes */
    for (var n = 0; n < S.notes.length; n++) drawNote(ctx, S.notes[n], laneW);

    /* hit zone line */
    ctx.strokeStyle = 'rgba(255,255,255,0.18)'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(0, hitY); ctx.lineTo(W, hitY); ctx.stroke();

    /* hit zone circles */
    for (var k = 0; k < 4; k++) {
      var cx = (k + 0.5) * laneW, active = S.laneActive[k];
      ctx.save();
      ctx.strokeStyle = LANE_COLORS[k];
      ctx.lineWidth   = active ? 3.5 : 2.5;
      ctx.shadowColor = LANE_COLORS[k];
      ctx.shadowBlur  = active ? 24 : 12;
      ctx.beginPath(); ctx.arc(cx, hitY, active ? 23 : 20, 0, Math.PI * 2); ctx.stroke();
      if (active) { ctx.fillStyle = LANE_COLORS[k] + '28'; ctx.fill(); }
      ctx.restore();
    }
  }

  /* ── UPDATE ── */
  function update(dt) {
    S.spawnTimer += dt;
    if (S.spawnTimer >= S.interval) {
      spawnNote();
      S.spawnTimer -= S.interval;
    }

    var hitY  = S.H - 68;
    var missY = S.H + 60;

    for (var i = S.notes.length - 1; i >= 0; i--) {
      var note = S.notes[i];
      note.y += S.speed * dt;

      /* fade missed notes */
      if (note.missed) note.alpha = Math.max(0, note.alpha - dt * 4);

      /* auto-miss: note passed hit zone without being hit */
      if (!note.hit && !note.missed && note.y > hitY + MISS_PAST) registerMiss(note);

      /* remove off-screen or fully-hit notes */
      if (note.alpha <= 0 || note.y > missY) S.notes.splice(i, 1);
    }
  }

  /* ── GAME LOOP ── */
  var lastTime = 0;
  function gameLoop(ts) {
    var dt = Math.min((ts - lastTime) / 1000, 0.1);
    lastTime = ts;
    if (S.running) {
      update(dt);
      render();
      S.animId = requestAnimationFrame(gameLoop);
    }
  }

  /* ── RESULT SCREEN ── */
  function showResult() {
    var total    = S.perfect + S.good + S.miss;
    var accuracy = total > 0 ? Math.round((S.perfect + S.good) / total * 100) : 0;
    var grade    = accuracy >= 95 ? 'S' : accuracy >= 85 ? 'A' : accuracy >= 70 ? 'B' : accuracy >= 50 ? 'C' : 'D';
    var gradeEl  = el('rg-grade');
    gradeEl.textContent = grade;
    gradeEl.className   = 'rg-result-grade rg-result-grade--' + grade;
    el('rg-final-score').textContent = S.score.toLocaleString();
    el('rg-breakdown').innerHTML =
      '✨ Perfect: ' + S.perfect +
      ' &nbsp;|&nbsp; ✔ Good: ' + S.good +
      ' &nbsp;|&nbsp; ✖ Miss: ' + S.miss + '<br>' +
      'Max Combo: ' + S.maxCombo +
      ' &nbsp;|&nbsp; Accuracy: ' + accuracy + '%';
    show('rg-over');
  }

  /* ── PUBLIC API ── */
  window.RG = {
    setMode: function (mode, btn) {
      S.mode = mode;
      document.querySelectorAll('.rg-mode-btn').forEach(function (b) { b.classList.remove('rg-mode-active'); });
      if (btn) btn.classList.add('rg-mode-active');
    },

    setDiff: function (diff, btn) {
      S.diff = diff;
      document.querySelectorAll('.rg-diff-btn').forEach(function (b) { b.classList.remove('rg-diff-active'); });
      if (btn) btn.classList.add('rg-diff-active');
    },

    start: function () {
      cancelAnimationFrame(S.animId);
      stopBeat();
      S.running = false;
      S.notes = [];
      S.score = 0; S.combo = 0; S.maxCombo = 0; S.mult = 1;
      S.perfect = 0; S.good = 0; S.miss = 0; S.total = 0;
      S.lives = MAX_LIVES;
      S.spawnTimer = 0;
      S.laneActive = [false, false, false, false];

      var cfg    = DIFF_CFG[S.diff];
      S.bpm      = cfg.bpm;
      S.speed    = cfg.speed;
      S.interval = (60 / cfg.bpm) * cfg.beatsPerNote;

      show('rg-game');
      setTimeout(function () {
        setupCanvas();
        setupLanes();
        updateHUD();
        startBeat();
        S.running = true;
        lastTime  = performance.now();
        S.animId  = requestAnimationFrame(gameLoop);
      }, 30);
    },

    quit: function () {
      S.running = false;
      cancelAnimationFrame(S.animId);
      stopBeat();
      show('rg-menu');
    },

    playAgain: function () { RG.start(); },

    menu: function () {
      S.running = false;
      cancelAnimationFrame(S.animId);
      stopBeat();
      show('rg-menu');
    },

    pressLane: function (lane) {
      if (!S.running) return;
      S.laneActive[lane] = true;
      var cell = document.querySelector('.rg-lane-cell[data-lane="' + lane + '"]');
      if (cell) {
        cell.classList.add('rg-lane-flash');
        setTimeout(function () {
          cell.classList.remove('rg-lane-flash');
          S.laneActive[lane] = false;
        }, 130);
      }
      tryHit(lane);
    }
  };

  /* ── KEYBOARD ── */
  document.addEventListener('keydown', function (e) {
    if (e.code in KEY_MAP) { e.preventDefault(); RG.pressLane(KEY_MAP[e.code]); }
  });

  /* ── RESIZE ── */
  window.addEventListener('resize', function () {
    if (S.running) setupCanvas();
  });

  show('rg-menu');
})();
</script>
