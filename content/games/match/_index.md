---
title: "Memory Match — Japanese Flip Card Game"
description: "Free Japanese memory match game. Flip cards to match hiragana, katakana, kanji, or JLPT N5 vocabulary with their readings and meanings. Train your memory while learning Japanese."
date: 2025-01-01
showtoc: false
---

<!-- ── MENU SCREEN ── -->
<div id="fm-menu" class="fm-active">
  <div class="fm-title">記憶マッチ — Memory Match</div>
  <div class="fm-subtitle">Flip cards to match Japanese with their reading or meaning.</div>

  <div class="fm-mode-grid">
    <button class="fm-mode-btn fm-mode-active" data-mode="hiragana" onclick="FM.setMode('hiragana',this)">
      <span class="fm-mode-icon">あ</span>
      <span class="fm-mode-label">Hiragana</span>
    </button>
    <button class="fm-mode-btn" data-mode="katakana" onclick="FM.setMode('katakana',this)">
      <span class="fm-mode-icon">ア</span>
      <span class="fm-mode-label">Katakana</span>
    </button>
    <button class="fm-mode-btn" data-mode="kanji" onclick="FM.setMode('kanji',this)">
      <span class="fm-mode-icon">漢</span>
      <span class="fm-mode-label">Kanji N5</span>
    </button>
    <button class="fm-mode-btn" data-mode="vocab" onclick="FM.setMode('vocab',this)">
      <span class="fm-mode-icon">語</span>
      <span class="fm-mode-label">Vocab N5</span>
    </button>
  </div>

  <div style="text-align:center;color:var(--secondary);font-size:0.82rem;margin-bottom:0.6rem;text-transform:uppercase;letter-spacing:0.07em;">Difficulty</div>
  <div class="fm-diff-row">
    <button class="fm-diff-btn" onclick="FM.startGame('easy')">Easy<br><span style="font-weight:400;font-size:0.75rem;color:var(--secondary)">6 pairs</span></button>
    <button class="fm-diff-btn" onclick="FM.startGame('medium')">Medium<br><span style="font-weight:400;font-size:0.75rem;color:var(--secondary)">8 pairs</span></button>
    <button class="fm-diff-btn" onclick="FM.startGame('hard')">Hard<br><span style="font-weight:400;font-size:0.75rem;color:var(--secondary)">12 pairs</span></button>
  </div>
</div>

<!-- ── GAME SCREEN ── -->
<div id="fm-game">
  <div class="fm-hud">
    <div class="fm-hud-stat">
      <span class="fm-hud-val" id="fm-timer">0:00</span>
      <span class="fm-hud-label">Time</span>
    </div>
    <div class="fm-hud-stat">
      <span class="fm-hud-val" id="fm-pairs">0 / 0</span>
      <span class="fm-hud-label">Pairs</span>
    </div>
    <div class="fm-hud-stat">
      <span class="fm-hud-val" id="fm-flips">0</span>
      <span class="fm-hud-label">Flips</span>
    </div>
    <button class="fm-hud-btn" onclick="FM.menu()">Menu</button>
  </div>
  <div class="fm-progress-wrap"><div class="fm-progress-fill" id="fm-progress" style="width:0%"></div></div>
  <div id="fm-grid" class="fm-grid fm-grid--4col"></div>
</div>

<!-- ── WIN SCREEN ── -->
<div id="fm-win">
  <div class="fm-win-box">
    <div class="fm-win-trophy" id="fm-trophy">🏆</div>
    <div class="fm-win-title">Cleared!</div>
    <div class="fm-win-score" id="fm-score">0</div>
    <div class="fm-win-breakdown" id="fm-breakdown"></div>
    <div class="fm-win-btns">
      <button class="fm-win-btn fm-win-btn--play" onclick="FM.restart()">Play Again</button>
      <button class="fm-win-btn fm-win-btn--menu" onclick="FM.menu()">Menu</button>
    </div>
  </div>
</div>

<script>
(function(){
  // ── DATA ──────────────────────────────────────────
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
      {jp:'ざ',en:'za'},{jp:'じ',en:'ji'},{jp:'ず',en:'zu'},{jp:'ぜ',en:'ze'},{jp:'ぞ',en:'zo'},
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
      {jp:'ザ',en:'za'},{jp:'ジ',en:'ji'},{jp:'ズ',en:'zu'},{jp:'ゼ',en:'ze'},{jp:'ゾ',en:'zo'},
      {jp:'ダ',en:'da'},{jp:'デ',en:'de'},{jp:'ド',en:'do'},
      {jp:'バ',en:'ba'},{jp:'ビ',en:'bi'},{jp:'ブ',en:'bu'},{jp:'ベ',en:'be'},{jp:'ボ',en:'bo'},
      {jp:'パ',en:'pa'},{jp:'ピ',en:'pi'},{jp:'プ',en:'pu'},{jp:'ペ',en:'pe'},{jp:'ポ',en:'po'}
    ],
    kanji: [
      {jp:'一',en:'one'},{jp:'二',en:'two'},{jp:'三',en:'three'},{jp:'四',en:'four'},{jp:'五',en:'five'},
      {jp:'六',en:'six'},{jp:'七',en:'seven'},{jp:'八',en:'eight'},{jp:'九',en:'nine'},{jp:'十',en:'ten'},
      {jp:'百',en:'hundred'},{jp:'千',en:'thousand'},{jp:'万',en:'ten thousand'},
      {jp:'日',en:'day/sun'},{jp:'月',en:'moon/month'},{jp:'火',en:'fire'},{jp:'水',en:'water'},{jp:'木',en:'tree'},{jp:'金',en:'gold'},{jp:'土',en:'earth'},
      {jp:'山',en:'mountain'},{jp:'川',en:'river'},{jp:'田',en:'rice field'},{jp:'林',en:'forest'},{jp:'森',en:'woods'},
      {jp:'人',en:'person'},{jp:'女',en:'woman'},{jp:'男',en:'man'},{jp:'子',en:'child'},{jp:'口',en:'mouth'},
      {jp:'手',en:'hand'},{jp:'目',en:'eye'},{jp:'耳',en:'ear'},{jp:'足',en:'foot/leg'},{jp:'力',en:'power'},
      {jp:'大',en:'big'},{jp:'小',en:'small'},{jp:'中',en:'middle'},{jp:'上',en:'above'},{jp:'下',en:'below'},
      {jp:'左',en:'left'},{jp:'右',en:'right'},{jp:'前',en:'front'},{jp:'後',en:'behind'},
      {jp:'本',en:'book/origin'},{jp:'車',en:'car'},{jp:'電',en:'electricity'},{jp:'気',en:'spirit/air'},{jp:'学',en:'study'},
      {jp:'校',en:'school'},{jp:'先',en:'before/ahead'},{jp:'生',en:'life/birth'},{jp:'年',en:'year'},{jp:'国',en:'country'}
    ],
    vocab: [
      {jp:'いぬ',en:'dog'},{jp:'ねこ',en:'cat'},{jp:'さかな',en:'fish'},{jp:'とり',en:'bird'},{jp:'うま',en:'horse'},
      {jp:'みず',en:'water'},{jp:'ごはん',en:'rice/meal'},{jp:'パン',en:'bread'},{jp:'にく',en:'meat'},{jp:'たまご',en:'egg'},
      {jp:'あか',en:'red'},{jp:'あお',en:'blue'},{jp:'しろ',en:'white'},{jp:'くろ',en:'black'},{jp:'きいろ',en:'yellow'},
      {jp:'おおきい',en:'big'},{jp:'ちいさい',en:'small'},{jp:'あたらしい',en:'new'},{jp:'ふるい',en:'old'},{jp:'たかい',en:'tall/expensive'},
      {jp:'あさ',en:'morning'},{jp:'ひる',en:'noon'},{jp:'よる',en:'night'},{jp:'きょう',en:'today'},{jp:'あした',en:'tomorrow'},
      {jp:'でんしゃ',en:'train'},{jp:'バス',en:'bus'},{jp:'くるま',en:'car'},{jp:'じてんしゃ',en:'bicycle'},{jp:'ひこうき',en:'airplane'},
      {jp:'がっこう',en:'school'},{jp:'びょういん',en:'hospital'},{jp:'えき',en:'station'},{jp:'みせ',en:'shop'},{jp:'うち',en:'home'},
      {jp:'たべる',en:'to eat'},{jp:'のむ',en:'to drink'},{jp:'みる',en:'to see'},{jp:'きく',en:'to listen'},{jp:'はなす',en:'to speak'},
      {jp:'すき',en:'like'},{jp:'きらい',en:'dislike'},{jp:'げんき',en:'healthy/well'},{jp:'しずか',en:'quiet'},{jp:'にぎやか',en:'lively'},
      {jp:'いくら',en:'how much'},{jp:'どこ',en:'where'},{jp:'だれ',en:'who'},{jp:'なに',en:'what'},{jp:'いつ',en:'when'},
      {jp:'ありがとう',en:'thank you'},{jp:'すみません',en:'excuse me'},{jp:'はい',en:'yes'},{jp:'いいえ',en:'no'},{jp:'わかった',en:'understood'}
    ]
  };

  // ── DIFFICULTY CONFIG ───────────────────────────
  var DIFF = {
    easy:   { pairs: 6,  cols: 3 },
    medium: { pairs: 8,  cols: 4 },
    hard:   { pairs: 12, cols: 4 }
  };

  // ── STATE ────────────────────────────────────────
  var S = {
    mode:      'hiragana',
    diff:      'medium',
    cards:     [],       // [{pairId, type:'jp'|'en', item}]
    flipped:   [],       // indices of face-up unmatched cards
    matched:   0,
    totalPairs: 0,
    flips:     0,
    timerSec:  0,
    timerInt:  null,
    timerStarted: false,
    locked:    false
  };

  // ── HELPERS ──────────────────────────────────────
  function el(id) { return document.getElementById(id); }
  function show(id) {
    ['fm-menu','fm-game','fm-win'].forEach(function(s){
      var e = el(s);
      if (e) { e.classList.remove('fm-active'); e.style.display = ''; }
    });
    var t = el(id);
    if (t) { t.classList.add('fm-active'); t.style.display = 'block'; }
  }
  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
    }
    return a;
  }
  function fmtTime(s) {
    return Math.floor(s / 60) + ':' + (s % 60 < 10 ? '0' : '') + (s % 60);
  }

  // ── FONT SIZE FOR JAPANESE TEXT ──────────────────
  function jpFontSize(text) {
    var l = text.length;
    if (l <= 1) return '2.4rem';
    if (l <= 2) return '2.0rem';
    if (l <= 3) return '1.7rem';
    if (l <= 4) return '1.4rem';
    if (l <= 6) return '1.1rem';
    return '0.9rem';
  }
  function enFontSize(text) {
    var l = text.length;
    if (l <= 6) return '1.0rem';
    if (l <= 10) return '0.85rem';
    return '0.72rem';
  }

  // ── BUILD GRID ───────────────────────────────────
  function buildGrid() {
    var pool = shuffle(DATA[S.mode]);
    var picked = pool.slice(0, S.totalPairs);
    var cards = [];
    picked.forEach(function(item, idx) {
      cards.push({ pairId: idx, type: 'jp', item: item });
      cards.push({ pairId: idx, type: 'en', item: item });
    });
    S.cards = shuffle(cards);

    var grid = el('fm-grid');
    grid.innerHTML = '';
    grid.className = 'fm-grid fm-grid--' + DIFF[S.diff].cols + 'col';

    S.cards.forEach(function(card, i) {
      var div = document.createElement('div');
      div.className = 'fm-card fm-card--' + card.type;
      div.setAttribute('data-idx', i);
      div.innerHTML =
        '<div class="fm-card-inner">' +
          '<div class="fm-face fm-face--back">日</div>' +
          '<div class="fm-face fm-face--front">' + buildFaceHTML(card) + '</div>' +
        '</div>';
      div.addEventListener('click', function() { FM.flip(i); });
      grid.appendChild(div);
    });

    el('fm-pairs').textContent = '0 / ' + S.totalPairs;
    el('fm-flips').textContent = '0';
    el('fm-timer').textContent = '0:00';
    el('fm-progress').style.width = '0%';
  }

  function buildFaceHTML(card) {
    if (card.type === 'jp') {
      return '<span class="fm-card-char" style="font-size:' + jpFontSize(card.item.jp) + '">' + card.item.jp + '</span>';
    } else {
      return '<span class="fm-card-char" style="font-size:' + enFontSize(card.item.en) + '">' + card.item.en + '</span>';
    }
  }

  // ── TIMER ─────────────────────────────────────────
  function startTimer() {
    if (S.timerStarted) return;
    S.timerStarted = true;
    S.timerInt = setInterval(function() {
      S.timerSec++;
      el('fm-timer').textContent = fmtTime(S.timerSec);
    }, 1000);
  }
  function stopTimer() {
    clearInterval(S.timerInt);
    S.timerInt = null;
  }

  // ── SCORE CALC ────────────────────────────────────
  function calcScore() {
    var base = S.totalPairs * 100;
    var timeBonus = Math.max(0, 600 - S.timerSec) * 2;
    var accuracy = S.totalPairs / Math.max(S.totalPairs, Math.floor(S.flips / 2));
    var accBonus = Math.round(accuracy * 200);
    return {
      base: base,
      timeBonus: timeBonus,
      accBonus: accBonus,
      total: base + timeBonus + accBonus
    };
  }

  // ── PUBLIC API ────────────────────────────────────
  window.FM = {
    setMode: function(mode, btn) {
      S.mode = mode;
      document.querySelectorAll('.fm-mode-btn').forEach(function(b) { b.classList.remove('fm-mode-active'); });
      if (btn) btn.classList.add('fm-mode-active');
    },

    startGame: function(diff) {
      S.diff        = diff;
      S.totalPairs  = DIFF[diff].pairs;
      S.matched     = 0;
      S.flips       = 0;
      S.flipped     = [];
      S.locked      = false;
      S.timerSec    = 0;
      S.timerStarted = false;
      stopTimer();
      buildGrid();
      show('fm-game');
    },

    flip: function(idx) {
      if (S.locked) return;
      var card = S.cards[idx];
      if (!card) return;
      if (card.matched) return;
      if (S.flipped.indexOf(idx) !== -1) return;

      startTimer();
      S.flips++;
      el('fm-flips').textContent = S.flips;

      var cardEl = document.querySelector('.fm-card[data-idx="' + idx + '"]');
      cardEl.classList.add('fm-flipped');
      S.flipped.push(idx);

      if (S.flipped.length === 2) {
        S.locked = true;
        var i0 = S.flipped[0], i1 = S.flipped[1];
        var c0 = S.cards[i0], c1 = S.cards[i1];

        if (c0.pairId === c1.pairId && c0.type !== c1.type) {
          // MATCH
          c0.matched = true; c1.matched = true;
          setTimeout(function() {
            [i0, i1].forEach(function(i) {
              var e = document.querySelector('.fm-card[data-idx="' + i + '"]');
              e.classList.add('fm-match', 'fm-card--matched');
              setTimeout(function() { e.classList.remove('fm-match'); }, 450);
            });
            S.matched++;
            el('fm-pairs').textContent = S.matched + ' / ' + S.totalPairs;
            el('fm-progress').style.width = (S.matched / S.totalPairs * 100) + '%';
            S.flipped = [];
            S.locked = false;
            if (S.matched === S.totalPairs) {
              stopTimer();
              setTimeout(FM.showWin, 500);
            }
          }, 200);
        } else {
          // NO MATCH
          setTimeout(function() {
            [i0, i1].forEach(function(i) {
              var e = document.querySelector('.fm-card[data-idx="' + i + '"]');
              e.classList.add('fm-nope');
              setTimeout(function() {
                e.classList.remove('fm-nope', 'fm-flipped');
              }, 560);
            });
            S.flipped = [];
            S.locked = false;
          }, 700);
        }
      }
    },

    showWin: function() {
      var sc = calcScore();
      var trophy = sc.total >= 900 ? '🏆' : sc.total >= 600 ? '🥈' : '🥉';
      el('fm-trophy').textContent = trophy;
      el('fm-score').textContent = sc.total.toLocaleString();
      el('fm-breakdown').innerHTML =
        'Pairs × 100 = ' + sc.base + '<br>' +
        'Time bonus = +' + sc.timeBonus + '<br>' +
        'Accuracy bonus = +' + sc.accBonus + '<br>' +
        'Time: ' + fmtTime(S.timerSec) + ' &nbsp;|&nbsp; Flips: ' + S.flips;
      show('fm-win');
    },

    restart: function() {
      FM.startGame(S.diff);
    },

    menu: function() {
      stopTimer();
      show('fm-menu');
    }
  };

  // ── INIT ──────────────────────────────────────────
  show('fm-menu');
})();
</script>
