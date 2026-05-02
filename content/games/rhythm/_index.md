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

  /* ── LANE COLOURS (reused by canvas in later tasks) ── */
  var LANE_COLORS = ['#ef4444', '#f97316', '#3b82f6', '#a855f7'];
  var KEY_MAP = { KeyD: 0, KeyF: 1, KeyJ: 2, KeyK: 3 };

  /* ── STATE ── */
  var S = {
    mode:   'hiragana',
    diff:   'easy',
    /* game fields (populated Task 2+) */
    notes:    [],
    score:    0,
    combo:    0,
    maxCombo: 0,
    mult:     1,
    perfect:  0,
    good:     0,
    miss:     0,
    total:    0,
    running:  false,
    animId:   null,
    /* audio (Task 3) */
    audioCtx: null,
    beatInt:  null,
    /* lane state */
    laneLabels: ['—', '—', '—', '—'],
    laneActive:  [false, false, false, false]
  };

  /* ── HELPERS ── */
  function el(id) { return document.getElementById(id); }

  function show(id) {
    ['rg-menu', 'rg-game', 'rg-over'].forEach(function (s) {
      var e = el(s);
      if (!e) return;
      e.classList.remove('rg-active');
      e.style.display = '';
    });
    var t = el(id);
    if (t) { t.classList.add('rg-active'); t.style.display = 'block'; }
  }

  /* ── STATIC CANVAS DRAW (placeholder until Task 2) ── */
  function drawStatic() {
    var canvas = el('rg-canvas');
    if (!canvas) return;
    var wrap = canvas.parentElement;
    var W = wrap.clientWidth || 600;
    var H = canvas.offsetHeight || 460;
    canvas.width  = W;
    canvas.height = H;
    var ctx = canvas.getContext('2d');

    /* background */
    ctx.fillStyle = '#070710';
    ctx.fillRect(0, 0, W, H);

    var laneW = W / 4;

    /* alternating lane tint + per-lane colour glow */
    for (var i = 0; i < 4; i++) {
      var x = i * laneW;

      if (i % 2 === 0) {
        ctx.fillStyle = 'rgba(255,255,255,0.012)';
        ctx.fillRect(x, 0, laneW, H);
      }

      /* bottom glow */
      var gBot = ctx.createLinearGradient(0, H - 140, 0, H);
      gBot.addColorStop(0, 'transparent');
      gBot.addColorStop(1, LANE_COLORS[i] + '20');
      ctx.fillStyle = gBot;
      ctx.fillRect(x, 0, laneW, H);

      /* top glow */
      var gTop = ctx.createLinearGradient(0, 0, 0, 50);
      gTop.addColorStop(0, LANE_COLORS[i] + '15');
      gTop.addColorStop(1, 'transparent');
      ctx.fillStyle = gTop;
      ctx.fillRect(x, 0, laneW, H);
    }

    /* horizontal beat grid */
    ctx.strokeStyle = 'rgba(255,255,255,0.03)';
    ctx.lineWidth = 1;
    for (var y = 60; y < H - 80; y += 60) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke();
    }

    /* lane dividers */
    ctx.strokeStyle = 'rgba(255,255,255,0.07)';
    ctx.lineWidth = 1;
    for (var j = 1; j < 4; j++) {
      ctx.beginPath(); ctx.moveTo(j * laneW, 0); ctx.lineTo(j * laneW, H); ctx.stroke();
    }

    /* hit zone line */
    var hitY = H - 68;
    ctx.strokeStyle = 'rgba(255,255,255,0.22)';
    ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(0, hitY); ctx.lineTo(W, hitY); ctx.stroke();

    /* hit zone circles */
    for (var k = 0; k < 4; k++) {
      var cx = (k + 0.5) * laneW;
      ctx.save();
      ctx.strokeStyle = LANE_COLORS[k];
      ctx.lineWidth = 2.5;
      ctx.shadowColor = LANE_COLORS[k];
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.arc(cx, hitY, 20, 0, Math.PI * 2);
      ctx.stroke();
      ctx.restore();
    }

    /* centre prompt */
    ctx.fillStyle = 'rgba(255,255,255,0.16)';
    ctx.font = '13px system-ui, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('Select a mode and press ▶ Start', W / 2, H / 2);
  }

  /* ── PUBLIC API ── */
  window.RG = {
    setMode: function (mode, btn) {
      S.mode = mode;
      document.querySelectorAll('.rg-mode-btn').forEach(function (b) {
        b.classList.remove('rg-mode-active');
      });
      if (btn) btn.classList.add('rg-mode-active');
    },

    setDiff: function (diff, btn) {
      S.diff = diff;
      document.querySelectorAll('.rg-diff-btn').forEach(function (b) {
        b.classList.remove('rg-diff-active');
      });
      if (btn) btn.classList.add('rg-diff-active');
    },

    start: function () {
      show('rg-game');
      setTimeout(drawStatic, 30);
    },

    quit: function () {
      S.running = false;
      show('rg-menu');
    },

    playAgain: function () { RG.start(); },

    menu: function () {
      S.running = false;
      show('rg-menu');
    },

    /* stub — wired up in Task 3 */
    pressLane: function (lane) {
      var cell = document.querySelector('.rg-lane-cell[data-lane="' + lane + '"]');
      if (!cell) return;
      cell.classList.add('rg-lane-flash');
      setTimeout(function () { cell.classList.remove('rg-lane-flash'); }, 120);
    }
  };

  /* keyboard listener stub (full logic in Task 3) */
  document.addEventListener('keydown', function (e) {
    if (e.code in KEY_MAP) RG.pressLane(KEY_MAP[e.code]);
  });

  /* redraw static canvas on resize while game screen is showing */
  window.addEventListener('resize', function () {
    if (el('rg-game').classList.contains('rg-active')) drawStatic();
  });

  show('rg-menu');
})();
</script>
