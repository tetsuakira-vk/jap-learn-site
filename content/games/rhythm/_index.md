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

  /* ── STATE ── */
  var S = {
    mode: 'hiragana', diff: 'easy',
    notes: [],
    score: 0, combo: 0, maxCombo: 0, mult: 1,
    perfect: 0, good: 0, miss: 0, total: 0,
    running: false, animId: null,
    audioCtx: null, beatInt: null,
    laneItems: [], laneActive: [false, false, false, false],
    spawnTimer: 0, bpm: 70, speed: 200, interval: 1.71,
    W: 600, H: 460, dpr: 1
  };

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

  /* ── NOTE SPAWN ── */
  function spawnNote() {
    var lane = Math.floor(Math.random() * 4);
    S.notes.push({
      lane: lane,
      item: S.laneItems[lane],
      y: -30,
      hit: false,
      missed: false,
      alpha: 1
    });
    S.total++;
  }

  /* ── ROUND RECT HELPER ── */
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
    var color = LANE_COLORS[note.lane];

    /* brighten glow as note approaches hit zone */
    var hitY       = S.H - 68;
    var dist       = hitY - note.y;
    var glowMult   = dist > 0 && dist < 120 ? 1 + (1 - dist / 120) * 0.8 : 1;

    ctx.save();
    ctx.globalAlpha = note.alpha;

    /* glow */
    ctx.shadowColor = color;
    ctx.shadowBlur  = 14 * glowMult;

    /* dark pill background */
    roundRect(ctx, x, y, noteW, noteH, 10);
    ctx.fillStyle = '#0e0e1c';
    ctx.fill();

    /* colored border */
    roundRect(ctx, x, y, noteW, noteH, 10);
    ctx.strokeStyle = color;
    ctx.lineWidth   = 2.5;
    ctx.stroke();
    ctx.shadowBlur  = 0;

    /* subtle top-color gradient accent */
    var grad = ctx.createLinearGradient(x, y, x, y + noteH * 0.4);
    grad.addColorStop(0, color + '30');
    grad.addColorStop(1, 'transparent');
    roundRect(ctx, x + 1, y + 1, noteW - 2, noteH - 2, 9);
    ctx.fillStyle = grad;
    ctx.fill();

    /* Japanese character */
    var text  = note.item.jp;
    var fsize = text.length <= 1 ? 26 : text.length <= 2 ? 21 : text.length <= 4 ? 16 : 12;
    ctx.fillStyle    = '#ffffff';
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

    /* background */
    ctx.fillStyle = '#070710';
    ctx.fillRect(0, 0, W, H);

    /* lane tints */
    for (var i = 0; i < 4; i++) {
      var lx = i * laneW;
      if (i % 2 === 0) {
        ctx.fillStyle = 'rgba(255,255,255,0.013)';
        ctx.fillRect(lx, 0, laneW, H);
      }
      var gBot = ctx.createLinearGradient(0, hitY - 110, 0, H);
      gBot.addColorStop(0, 'transparent');
      gBot.addColorStop(1, LANE_COLORS[i] + '22');
      ctx.fillStyle = gBot;
      ctx.fillRect(lx, 0, laneW, H);
    }

    /* beat grid */
    ctx.strokeStyle = 'rgba(255,255,255,0.03)';
    ctx.lineWidth = 1;
    for (var gy = 60; gy < H - 80; gy += 60) {
      ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(W, gy); ctx.stroke();
    }

    /* lane dividers */
    ctx.strokeStyle = 'rgba(255,255,255,0.07)';
    ctx.lineWidth = 1;
    for (var j = 1; j < 4; j++) {
      ctx.beginPath();
      ctx.moveTo(j * laneW, 0); ctx.lineTo(j * laneW, H);
      ctx.stroke();
    }

    /* falling notes (below hit zone circles) */
    for (var n = 0; n < S.notes.length; n++) {
      drawNote(ctx, S.notes[n], laneW);
    }

    /* hit zone line */
    ctx.strokeStyle = 'rgba(255,255,255,0.18)';
    ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(0, hitY); ctx.lineTo(W, hitY); ctx.stroke();

    /* hit zone circles — pulse when lane active */
    for (var k = 0; k < 4; k++) {
      var cx     = (k + 0.5) * laneW;
      var active = S.laneActive[k];
      ctx.save();
      ctx.strokeStyle = LANE_COLORS[k];
      ctx.lineWidth   = active ? 3.5 : 2.5;
      ctx.shadowColor = LANE_COLORS[k];
      ctx.shadowBlur  = active ? 24 : 12;
      ctx.beginPath();
      ctx.arc(cx, hitY, active ? 23 : 20, 0, Math.PI * 2);
      ctx.stroke();
      if (active) {
        ctx.fillStyle = LANE_COLORS[k] + '28';
        ctx.fill();
      }
      ctx.restore();
    }
  }

  /* ── UPDATE ── */
  function update(dt) {
    S.spawnTimer += dt;
    if (S.spawnTimer >= S.interval) {
      spawnNote();
      S.spawnTimer -= S.interval; /* keep fractional remainder for tight timing */
    }

    var missY = S.H + 50;
    for (var i = S.notes.length - 1; i >= 0; i--) {
      S.notes[i].y += S.speed * dt;
      if (S.notes[i].y > missY) {
        S.notes.splice(i, 1); /* miss handling added in Task 3 */
      }
    }
  }

  /* ── GAME LOOP ── */
  var lastTime = 0;
  function gameLoop(ts) {
    var dt = Math.min((ts - lastTime) / 1000, 0.1); /* cap at 100 ms */
    lastTime = ts;
    if (S.running) {
      update(dt);
      render();
      S.animId = requestAnimationFrame(gameLoop);
    }
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
      S.running = false;
      S.notes = [];
      S.score = 0; S.combo = 0; S.maxCombo = 0; S.mult = 1;
      S.perfect = 0; S.good = 0; S.miss = 0; S.total = 0;
      S.spawnTimer = 0;
      S.laneActive = [false, false, false, false];

      var cfg   = DIFF_CFG[S.diff];
      S.bpm      = cfg.bpm;
      S.speed    = cfg.speed;
      S.interval = (60 / cfg.bpm) * cfg.beatsPerNote;

      show('rg-game');
      setTimeout(function () {
        setupCanvas();
        setupLanes();
        el('rg-score').textContent = '0';
        el('rg-combo').textContent = '0';
        el('rg-mult').textContent  = '×1';
        S.running = true;
        lastTime  = performance.now();
        S.animId  = requestAnimationFrame(gameLoop);
      }, 30);
    },

    quit: function () {
      S.running = false;
      cancelAnimationFrame(S.animId);
      show('rg-menu');
    },

    playAgain: function () { RG.start(); },

    menu: function () {
      S.running = false;
      cancelAnimationFrame(S.animId);
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
      /* hit detection added in Task 3 */
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
