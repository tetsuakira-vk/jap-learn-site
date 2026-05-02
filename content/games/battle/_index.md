---
title: "Kanji Quest — Japanese Battle RPG"
description: "Free browser RPG for learning Japanese — battle monsters by answering hiragana, katakana, kanji, and JLPT N5 vocabulary questions. Wrong answers deal damage."
date: 2025-01-01
showtoc: false
---

<div class="game-wrap">

<!-- ── MENU SCREEN ── -->
<div id="scr-menu" class="game-screen">
  <div class="game-logo">⚔️ <span>KANJI</span> QUEST</div>
  <div class="game-tagline">Answer correctly to attack. Wrong answers hurt you. How far can you get?</div>
  <div class="mode-grid">
    <button class="mode-btn" onclick="GM.start('hiragana')">
      <div class="mode-icon">あ</div>
      <div class="mode-name">Hiragana</div>
      <div class="mode-desc">46 characters</div>
    </button>
    <button class="mode-btn" onclick="GM.start('katakana')">
      <div class="mode-icon">ア</div>
      <div class="mode-name">Katakana</div>
      <div class="mode-desc">46 characters</div>
    </button>
    <button class="mode-btn" onclick="GM.start('kanji')">
      <div class="mode-icon">水</div>
      <div class="mode-name">Kanji N5</div>
      <div class="mode-desc">50 kanji</div>
    </button>
    <button class="mode-btn" onclick="GM.start('vocab')">
      <div class="mode-icon">語</div>
      <div class="mode-name">JLPT N5</div>
      <div class="mode-desc">50 words</div>
    </button>
  </div>
</div>

<!-- ── BATTLE SCREEN ── -->
<div id="scr-battle" class="game-screen" style="display:none">
  <div class="battle-hud">
    <div class="hud-lv">LV <b id="h-lv">1</b></div>
    <div class="hud-mode" id="h-mode">HIRAGANA</div>
    <div class="hud-score">⭐ <b id="h-score">0</b></div>
  </div>

  <div class="enemy-zone">
    <div class="enemy-label" id="e-label">スライム <span class="enemy-lv">Lv.1</span></div>
    <div class="enemy-card" id="e-card">
      <div class="enemy-char" id="e-char">あ</div>
    </div>
    <div class="enemy-hp-track"><div class="enemy-hp-fill" id="e-hp"></div></div>
    <div class="hit-msg" id="hit-msg"></div>
  </div>

  <div class="q-label" id="q-label">How do you read this?</div>

  <div class="answer-grid" id="ans-grid"></div>

  <div class="player-bar">
    <div class="player-hearts" id="p-hearts"></div>
    <div class="streak-tag" id="streak-tag"></div>
  </div>
</div>

<!-- ── LEVEL UP SCREEN ── -->
<div id="scr-lvup" class="game-screen" style="display:none">
  <div class="bscreen-icon">⬆️</div>
  <div class="bscreen-title">LEVEL UP!</div>
  <div class="bscreen-sub" id="lvup-sub"></div>
  <button class="game-btn" onclick="GM.continueGame()">Continue →</button>
  <button class="game-btn game-btn--ghost" onclick="GM.menu()">Quit to Menu</button>
</div>

<!-- ── GAME OVER SCREEN ── -->
<div id="scr-over" class="game-screen" style="display:none">
  <div class="bscreen-icon">💀</div>
  <div class="bscreen-title">GAME OVER</div>
  <div class="bscreen-sub" id="over-sub"></div>
  <button class="game-btn" onclick="GM.restart()">Play Again</button>
  <button class="game-btn game-btn--ghost" onclick="GM.menu()">Change Mode</button>
</div>

</div><!-- .game-wrap -->

<script>
(function () {

/* ── DATA ─────────────────────────────────────────────────── */
var DATA = {
  hiragana: [
    {q:'あ',a:'a'},{q:'い',a:'i'},{q:'う',a:'u'},{q:'え',a:'e'},{q:'お',a:'o'},
    {q:'か',a:'ka'},{q:'き',a:'ki'},{q:'く',a:'ku'},{q:'け',a:'ke'},{q:'こ',a:'ko'},
    {q:'さ',a:'sa'},{q:'し',a:'shi'},{q:'す',a:'su'},{q:'せ',a:'se'},{q:'そ',a:'so'},
    {q:'た',a:'ta'},{q:'ち',a:'chi'},{q:'つ',a:'tsu'},{q:'て',a:'te'},{q:'と',a:'to'},
    {q:'な',a:'na'},{q:'に',a:'ni'},{q:'ぬ',a:'nu'},{q:'ね',a:'ne'},{q:'の',a:'no'},
    {q:'は',a:'ha'},{q:'ひ',a:'hi'},{q:'ふ',a:'fu'},{q:'へ',a:'he'},{q:'ほ',a:'ho'},
    {q:'ま',a:'ma'},{q:'み',a:'mi'},{q:'む',a:'mu'},{q:'め',a:'me'},{q:'も',a:'mo'},
    {q:'や',a:'ya'},{q:'ゆ',a:'yu'},{q:'よ',a:'yo'},
    {q:'ら',a:'ra'},{q:'り',a:'ri'},{q:'る',a:'ru'},{q:'れ',a:'re'},{q:'ろ',a:'ro'},
    {q:'わ',a:'wa'},{q:'を',a:'wo'},{q:'ん',a:'n'},
    {q:'が',a:'ga'},{q:'ぎ',a:'gi'},{q:'ぐ',a:'gu'},{q:'げ',a:'ge'},{q:'ご',a:'go'},
    {q:'ざ',a:'za'},{q:'じ',a:'ji'},{q:'ず',a:'zu'},{q:'ぜ',a:'ze'},{q:'ぞ',a:'zo'},
    {q:'だ',a:'da'},{q:'で',a:'de'},{q:'ど',a:'do'},
    {q:'ば',a:'ba'},{q:'び',a:'bi'},{q:'ぶ',a:'bu'},{q:'べ',a:'be'},{q:'ぼ',a:'bo'},
    {q:'ぱ',a:'pa'},{q:'ぴ',a:'pi'},{q:'ぷ',a:'pu'},{q:'ぺ',a:'pe'},{q:'ぽ',a:'po'}
  ],
  katakana: [
    {q:'ア',a:'a'},{q:'イ',a:'i'},{q:'ウ',a:'u'},{q:'エ',a:'e'},{q:'オ',a:'o'},
    {q:'カ',a:'ka'},{q:'キ',a:'ki'},{q:'ク',a:'ku'},{q:'ケ',a:'ke'},{q:'コ',a:'ko'},
    {q:'サ',a:'sa'},{q:'シ',a:'shi'},{q:'ス',a:'su'},{q:'セ',a:'se'},{q:'ソ',a:'so'},
    {q:'タ',a:'ta'},{q:'チ',a:'chi'},{q:'ツ',a:'tsu'},{q:'テ',a:'te'},{q:'ト',a:'to'},
    {q:'ナ',a:'na'},{q:'ニ',a:'ni'},{q:'ヌ',a:'nu'},{q:'ネ',a:'ne'},{q:'ノ',a:'no'},
    {q:'ハ',a:'ha'},{q:'ヒ',a:'hi'},{q:'フ',a:'fu'},{q:'ヘ',a:'he'},{q:'ホ',a:'ho'},
    {q:'マ',a:'ma'},{q:'ミ',a:'mi'},{q:'ム',a:'mu'},{q:'メ',a:'me'},{q:'モ',a:'mo'},
    {q:'ヤ',a:'ya'},{q:'ユ',a:'yu'},{q:'ヨ',a:'yo'},
    {q:'ラ',a:'ra'},{q:'リ',a:'ri'},{q:'ル',a:'ru'},{q:'レ',a:'re'},{q:'ロ',a:'ro'},
    {q:'ワ',a:'wa'},{q:'ヲ',a:'wo'},{q:'ン',a:'n'},
    {q:'ガ',a:'ga'},{q:'ギ',a:'gi'},{q:'グ',a:'gu'},{q:'ゲ',a:'ge'},{q:'ゴ',a:'go'},
    {q:'ザ',a:'za'},{q:'ジ',a:'ji'},{q:'ズ',a:'zu'},{q:'ゼ',a:'ze'},{q:'ゾ',a:'zo'},
    {q:'ダ',a:'da'},{q:'デ',a:'de'},{q:'ド',a:'do'},
    {q:'バ',a:'ba'},{q:'ビ',a:'bi'},{q:'ブ',a:'bu'},{q:'ベ',a:'be'},{q:'ボ',a:'bo'},
    {q:'パ',a:'pa'},{q:'ピ',a:'pi'},{q:'プ',a:'pu'},{q:'ペ',a:'pe'},{q:'ポ',a:'po'}
  ],
  kanji: [
    {q:'水',a:'water',h:'みず'},{q:'火',a:'fire',h:'ひ'},{q:'山',a:'mountain',h:'やま'},
    {q:'川',a:'river',h:'かわ'},{q:'木',a:'tree',h:'き'},{q:'日',a:'sun / day',h:'ひ'},
    {q:'月',a:'moon / month',h:'つき'},{q:'空',a:'sky',h:'そら'},{q:'海',a:'sea',h:'うみ'},
    {q:'雨',a:'rain',h:'あめ'},{q:'風',a:'wind',h:'かぜ'},{q:'花',a:'flower',h:'はな'},
    {q:'人',a:'person',h:'ひと'},{q:'大',a:'big',h:'おお'},{q:'小',a:'small',h:'ちい'},
    {q:'中',a:'middle / inside',h:'なか'},{q:'上',a:'up / above',h:'うえ'},{q:'下',a:'down / below',h:'した'},
    {q:'左',a:'left',h:'ひだり'},{q:'右',a:'right',h:'みぎ'},{q:'本',a:'book / origin',h:'ほん'},
    {q:'国',a:'country',h:'くに'},{q:'年',a:'year',h:'とし'},{q:'円',a:'yen / circle',h:'えん'},
    {q:'学',a:'study',h:'がく'},{q:'生',a:'life / birth',h:'せい'},{q:'子',a:'child',h:'こ'},
    {q:'女',a:'woman',h:'おんな'},{q:'男',a:'man',h:'おとこ'},{q:'口',a:'mouth',h:'くち'},
    {q:'手',a:'hand',h:'て'},{q:'目',a:'eye',h:'め'},{q:'耳',a:'ear',h:'みみ'},
    {q:'力',a:'strength / power',h:'ちから'},{q:'金',a:'gold / money',h:'かね'},
    {q:'土',a:'earth / soil',h:'つち'},{q:'田',a:'rice field',h:'た'},
    {q:'電',a:'electricity',h:'でん'},{q:'車',a:'car / vehicle',h:'くるま'},
    {q:'駅',a:'station',h:'えき'},{q:'道',a:'road / way',h:'みち'},
    {q:'食',a:'food / eat',h:'しょく'},{q:'飲',a:'drink',h:'の'},
    {q:'見',a:'see / look',h:'み'},{q:'聞',a:'hear / listen',h:'き'},
    {q:'読',a:'read',h:'よ'},{q:'書',a:'write',h:'か'},
    {q:'話',a:'speak / story',h:'はな'},{q:'来',a:'come',h:'く'},
    {q:'行',a:'go',h:'い'},{q:'出',a:'exit / leave',h:'で'},
    {q:'入',a:'enter',h:'はい'},{q:'高',a:'tall / expensive',h:'たか'},
    {q:'安',a:'cheap / safe',h:'やす'},{q:'新',a:'new',h:'あたら'},
    {q:'古',a:'old',h:'ふる'},{q:'白',a:'white',h:'しろ'},
    {q:'黒',a:'black',h:'くろ'},{q:'赤',a:'red',h:'あか'},
    {q:'青',a:'blue / green',h:'あお'},{q:'名',a:'name',h:'な'}
  ],
  vocab: [
    {q:'ありがとう',a:'thank you',h:'arigatou'},{q:'すみません',a:'excuse me / sorry',h:'sumimasen'},
    {q:'はい',a:'yes',h:'hai'},{q:'いいえ',a:'no',h:'iie'},
    {q:'おはよう',a:'good morning',h:'ohayou'},{q:'こんにちは',a:'hello',h:'konnichiwa'},
    {q:'こんばんは',a:'good evening',h:'konbanwa'},{q:'さようなら',a:'goodbye',h:'sayounara'},
    {q:'わたし',a:'I / me',h:'watashi'},{q:'これ',a:'this thing',h:'kore'},
    {q:'それ',a:'that thing',h:'sore'},{q:'どこ',a:'where',h:'doko'},
    {q:'なに',a:'what',h:'nani'},{q:'いつ',a:'when',h:'itsu'},
    {q:'だれ',a:'who',h:'dare'},{q:'いくら',a:'how much',h:'ikura'},
    {q:'おいしい',a:'delicious',h:'oishii'},{q:'かわいい',a:'cute',h:'kawaii'},
    {q:'たのしい',a:'fun / enjoyable',h:'tanoshii'},{q:'むずかしい',a:'difficult',h:'muzukashii'},
    {q:'やさしい',a:'easy / kind',h:'yasashii'},{q:'おおきい',a:'big / large',h:'ookii'},
    {q:'ちいさい',a:'small / tiny',h:'chiisai'},{q:'あたらしい',a:'new',h:'atarashii'},
    {q:'たかい',a:'tall / expensive',h:'takai'},{q:'やすい',a:'cheap',h:'yasui'},
    {q:'いきます',a:'to go',h:'ikimasu'},{q:'きます',a:'to come',h:'kimasu'},
    {q:'たべます',a:'to eat',h:'tabemasu'},{q:'のみます',a:'to drink',h:'nomimasu'},
    {q:'みます',a:'to see / watch',h:'mimasu'},{q:'ききます',a:'to listen',h:'kikimasu'},
    {q:'よみます',a:'to read',h:'yomimasu'},{q:'かきます',a:'to write',h:'kakimasu'},
    {q:'はなします',a:'to speak',h:'hanashimasu'},{q:'ねます',a:'to sleep',h:'nemasu'},
    {q:'おきます',a:'to wake up',h:'okimasu'},{q:'かいます',a:'to buy',h:'kaimasu'},
    {q:'わかります',a:'to understand',h:'wakarimasu'},{q:'います',a:'to exist (living)',h:'imasu'},
    {q:'あります',a:'to exist (object)',h:'arimasu'},
    {q:'がっこう',a:'school',h:'gakkou'},{q:'びょういん',a:'hospital',h:'byouin'},
    {q:'えき',a:'train station',h:'eki'},{q:'としょかん',a:'library',h:'toshokan'},
    {q:'ぎんこう',a:'bank',h:'ginkou'},{q:'ともだち',a:'friend',h:'tomodachi'},
    {q:'せんせい',a:'teacher',h:'sensei'},{q:'がくせい',a:'student',h:'gakusei'},
    {q:'でんしゃ',a:'train',h:'densha'},{q:'くるま',a:'car',h:'kuruma'},
    {q:'おかね',a:'money',h:'okane'},{q:'じかん',a:'time',h:'jikan'}
  ]
};

/* ── ENEMIES ───────────────────────────────────────────────── */
var ENEMIES = [
  {n:'スライム',  e:'Slime',     glow:'#22c55e', hp:2},
  {n:'コウモリ',  e:'Bat',       glow:'#a78bfa', hp:2},
  {n:'ゴースト',  e:'Ghost',     glow:'#7c3aed', hp:3},
  {n:'オーク',    e:'Orc',       glow:'#fb923c', hp:3},
  {n:'スケルトン',e:'Skeleton',  glow:'#94a3b8', hp:3},
  {n:'ウィザード',e:'Wizard',    glow:'#60a5fa', hp:4},
  {n:'ドラゴン',  e:'Dragon',    glow:'#ef4444', hp:4},
  {n:'デーモン',  e:'Demon',     glow:'#dc2626', hp:5},
  {n:'魔王',      e:'Dark Lord', glow:'#fbbf24', hp:6}
];

/* ── STATE ─────────────────────────────────────────────────── */
var S = {
  mode:null, pool:[], qi:0, cur:null,
  pHP:5, pHPmax:5,
  eHP:0, eHPmax:0, ei:0,
  score:0, streak:0, level:1, killed:0
};

/* ── HELPERS ───────────────────────────────────────────────── */
function shuffle(a) { return a.slice().sort(function(){ return Math.random()-0.5; }); }
function el(id)     { return document.getElementById(id); }

function showScreen(id) {
  ['menu','battle','lvup','over'].forEach(function(s){
    el('scr-'+s).style.display = (s===id) ? 'flex' : 'none';
  });
}

function scoreAdd(n) {
  S.score += n;
  el('h-score').textContent = Math.floor(S.score);
}

/* ── ENEMY ─────────────────────────────────────────────────── */
function spawnEnemy() {
  var idx = Math.min(S.ei, ENEMIES.length-1);
  var e = ENEMIES[idx];
  var bonus = Math.floor(S.level / 2);
  S.eHP = e.hp + bonus;
  S.eHPmax = S.eHP;
  el('e-label').innerHTML = e.n + ' <span class="enemy-lv">— ' + e.e + '</span>';
  el('e-card').style.borderColor = e.glow;
  el('e-card').style.boxShadow = '0 0 28px '+e.glow+'55, 0 0 8px '+e.glow+'33';
  // restart idle animation
  var ch = el('e-char');
  ch.style.animation = 'none';
  void ch.offsetWidth;
  ch.style.animation = '';
  refreshEnemyHP();
}

function refreshEnemyHP() {
  var pct = (S.eHP / S.eHPmax) * 100;
  var bar = el('e-hp');
  bar.style.width = pct + '%';
  bar.style.background = pct > 55 ? '#22c55e' : pct > 25 ? '#f59e0b' : '#ef4444';
}

/* ── QUESTIONS ─────────────────────────────────────────────── */
function nextQ() {
  if (S.qi >= S.pool.length) { S.pool = shuffle(DATA[S.mode]); S.qi = 0; }
  S.cur = S.pool[S.qi++];
  el('e-char').textContent = S.cur.q;

  var qText = (S.mode==='hiragana'||S.mode==='katakana') ? 'How do you read this?' : 'What does this mean?';
  el('q-label').textContent = qText;

  // Build 4 options: 1 correct + 3 wrong from pool
  var wrong = shuffle(DATA[S.mode].filter(function(x){ return x.a !== S.cur.a; })).slice(0,3);
  var opts  = shuffle([S.cur].concat(wrong));

  var grid = el('ans-grid');
  grid.innerHTML = '';
  opts.forEach(function(opt) {
    var btn = document.createElement('button');
    btn.className = 'answer-btn';
    btn.textContent = opt.a;
    btn.addEventListener('click', function(){ GM.answer(opt.a); });
    grid.appendChild(btn);
  });

  refreshHearts();
}

/* ── ANSWER ────────────────────────────────────────────────── */
function lockButtons() {
  el('ans-grid').querySelectorAll('.answer-btn').forEach(function(b){ b.disabled = true; });
}
function markButtons(chosen) {
  el('ans-grid').querySelectorAll('.answer-btn').forEach(function(b){
    if (b.textContent === chosen)    b.classList.add(chosen===S.cur.a ? 'answer-btn--ok' : 'answer-btn--bad');
    if (b.textContent === S.cur.a)   b.classList.add('answer-btn--ok');
  });
}

function floatMsg(text, cls) {
  var m = el('hit-msg');
  m.textContent = text;
  m.className = 'hit-msg ' + cls;
  void m.offsetWidth;
  m.classList.add('msg-go');
}

function animate(id, cls, dur) {
  var node = el(id);
  node.classList.add(cls);
  setTimeout(function(){ node.classList.remove(cls); }, dur||520);
}

/* ── PUBLIC API ────────────────────────────────────────────── */
window.GM = {
  start: function(mode) {
    S.mode = mode;
    S.pool = shuffle(DATA[mode]);
    S.qi = 0;
    S.pHP = 5; S.pHPmax = 5;
    S.score = 0; S.streak = 0; S.level = 1; S.killed = 0; S.ei = 0;
    el('h-mode').textContent = {hiragana:'HIRAGANA',katakana:'KATAKANA',kanji:'KANJI N5',vocab:'JLPT N5'}[mode];
    el('h-lv').textContent = 1;
    el('h-score').textContent = 0;
    showScreen('battle');
    spawnEnemy();
    nextQ();
  },

  answer: function(chosen) {
    lockButtons();
    markButtons(chosen);

    if (chosen === S.cur.a) {
      /* ── HIT ── */
      S.streak++;
      var pts = 10 + Math.floor((S.streak-1) * 4);
      scoreAdd(pts);
      S.eHP--;
      floatMsg('+' + pts, 'hit-msg--hit');
      if (S.streak >= 3) {
        var stk = el('streak-tag');
        stk.textContent = '🔥 ' + S.streak + ' streak!';
        stk.style.opacity = '1';
      }
      animate('e-char', 'gm-shake');
      setTimeout(function(){
        refreshEnemyHP();
        if (S.eHP <= 0) {
          /* enemy dead */
          animate('e-card', 'gm-dissolve', 650);
          S.killed++;
          scoreAdd(50);
          S.ei++;
          setTimeout(function(){
            if (S.killed > 0 && S.killed % 5 === 0) {
              /* level up every 5 kills */
              S.level++;
              el('h-lv').textContent = S.level;
              // restore 1 HP on level up (max 5)
              if (S.pHP < S.pHPmax) { S.pHP++; refreshHearts(); }
              el('lvup-sub').innerHTML =
                'Level <b>' + S.level + '</b> — enemies get tougher!<br>' +
                'Score: ' + Math.floor(S.score) + ' &nbsp;|&nbsp; Defeated: ' + S.killed;
              showScreen('lvup');
            } else {
              spawnEnemy();
              nextQ();
            }
          }, 700);
        } else {
          nextQ();
        }
      }, 550);

    } else {
      /* ── MISS ── */
      S.streak = 0;
      el('streak-tag').style.opacity = '0';
      S.pHP--;
      floatMsg('✗ ' + S.cur.a, 'hit-msg--miss');
      animate('p-hearts', 'gm-phit');
      refreshHearts();
      setTimeout(function(){
        if (S.pHP <= 0) {
          el('over-sub').innerHTML =
            'You reached <b>Level ' + S.level + '</b><br>' +
            'Score: ' + Math.floor(S.score) + ' &nbsp;|&nbsp; Enemies defeated: ' + S.killed;
          showScreen('over');
        } else {
          nextQ();
        }
      }, 700);
    }
  },

  continueGame: function() {
    showScreen('battle');
    spawnEnemy();
    nextQ();
  },

  restart: function() { GM.start(S.mode); },
  menu:    function() { showScreen('menu'); }
};

function refreshHearts() {
  var h = el('p-hearts');
  h.innerHTML = '';
  for (var i=0; i<S.pHPmax; i++) {
    h.innerHTML += (i < S.pHP) ? '❤️' : '🖤';
  }
}

})();
</script>
