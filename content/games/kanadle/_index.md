---
title: "KANADLE — Daily Japanese Kana Wordle"
description: "Guess the 5-kana Japanese word in 6 tries. A new word every day. Free daily Japanese word game — hiragana Wordle, no signup."
date: 2025-01-01
showtoc: false
---

<style>
/* KANADLE was ported from a prototype with its own color-variable names —
   this maps them onto the live site's real theme variables, and defines
   the two font variables (serif/sans) the live site doesn't have at all,
   scoped to this page only. */
.kanadle-page {
  --serif: Georgia, 'Times New Roman', serif;
  --sans: -apple-system, 'Segoe UI', Roboto, sans-serif;
}
.kanadle-page .btn.btn-solid {
  display: inline-block;
  padding: 10px 20px;
  border: 1.5px solid var(--primary);
  background: var(--primary);
  color: var(--theme);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .03em;
  cursor: pointer;
}
.kanadle-page .btn.btn-solid:hover { opacity: .85; }

/* ── Page layout ─────────────────────────────────────────────── */
.kanadle-page .game-layout {
  display: flex;
  align-items: flex-start;
  max-width: 680px;
  margin: 0 auto;
  padding: 0 0 60px;
  border-left: 1.5px solid var(--border);
  border-right: 1.5px solid var(--border);
  min-height: 80vh;
}

/* ── Sidebar ─────────────────────────────────────────────────── */
.kanadle-page .game-sidebar {
  width: 220px;
  flex-shrink: 0;
  border-right: 1.5px solid var(--border);
  position: sticky;
  top: 56px;
  align-self: flex-start;
}
.kanadle-page .sb-section { padding: 16px 14px; }
.kanadle-page .sb-section + .sb-section { border-top: 1px solid var(--border); }
.kanadle-page .sb-heading {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--secondary);
  margin-bottom: 10px;
}

/* Tile guide */
.kanadle-page .sb-tile-row { display: flex; align-items: center; gap: 8px; margin-bottom: 7px; }
.kanadle-page .sb-tile-row:last-child { margin-bottom: 0; }
.kanadle-page .sb-tile {
  width: 28px; height: 28px; flex-shrink: 0;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--serif); font-size: .85rem; font-weight: 700;
  border: 1.5px solid var(--border);
}
.kanadle-page .sb-tile.correct { background: #538d4e; color: #fff; border-color: #538d4e; }
.kanadle-page .sb-tile.present { background: #b59f3b; color: #fff; border-color: #b59f3b; }
.kanadle-page .sb-tile.absent  { background: #3a3a3c; color: #fff; border-color: #3a3a3c; }
[data-theme="light"]  .kanadle-page .sb-tile.absent { background: #787c7e; border-color: #787c7e; }
[data-theme="sakura"] .kanadle-page .sb-tile.absent { background: #8a7f76; border-color: #8a7f76; }
.kanadle-page .sb-tile-desc { font-size: 11px; color: var(--secondary); line-height: 1.4; }

/* Keyboard tips */
.kanadle-page .sb-tip {
  font-size: 11.5px;
  color: var(--secondary);
  line-height: 1.55;
  margin-bottom: 8px;
}
.kanadle-page .sb-tip:last-of-type { margin-bottom: 0; }
.kanadle-page .sb-tip strong { color: var(--primary); font-weight: 700; }
.kanadle-page .sb-key {
  display: inline-block;
  padding: 1px 5px;
  border: 1px solid var(--border);
  font-family: var(--serif);
  font-size: 11px;
  background: var(--tertiary);
  color: var(--primary);
  vertical-align: middle;
}
.kanadle-page .sb-kbd {
  display: inline-block;
  padding: 1px 5px;
  border: 1px solid var(--border);
  background: var(--tertiary);
  font-size: 10px;
  font-family: var(--sans);
  color: var(--primary);
  vertical-align: middle;
}
.kanadle-page .sb-romaji {
  display: inline-block;
  font-family: var(--sans);
  font-size: 10px;
  font-weight: 700;
  color: var(--primary);
  background: var(--entry);
  padding: 1px 4px;
  border: 1px solid var(--border);
  letter-spacing: .02em;
}

/* Hint */
.kanadle-page .hint-btn {
  width: 100%;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  padding: 8px 10px;
  border: 1.5px solid var(--border);
  background: none;
  color: var(--secondary);
  cursor: pointer;
  transition: border-color .12s, color .12s;
  text-align: left;
  margin-top: 4px;
}
.kanadle-page .hint-btn:hover:not(:disabled) { border-color: var(--primary); color: var(--primary); }
.kanadle-page .hint-btn:disabled { opacity: .45; cursor: default; }
.kanadle-page .hint-panel {
  margin-top: 8px;
  padding: 10px 10px;
  border: 1.5px solid var(--border);
  background: var(--tertiary);
  display: none;
}
.kanadle-page .hint-panel.show { display: block; }
.kanadle-page .hint-cat-label { font-size: 9px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: var(--secondary); margin-bottom: 4px; }
.kanadle-page .hint-cat-text  { font-size: 13px; font-weight: 700; color: var(--primary); }

/* ── Main game column ─────────────────────────────────────────── */
.kanadle-page .game-main {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  padding: 16px 12px 48px;
}

/* ── Header ─────────────────────────────────────────────────── */
.kanadle-page .game-header {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1.5px solid var(--primary);
  padding-bottom: 10px;
}
.kanadle-page .game-title {
  font-family: var(--serif);
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: .04em;
  line-height: 1.1;
}
.kanadle-page .game-title-jp {
  font-size: .7rem;
  color: var(--secondary);
  font-weight: 400;
  display: block;
  letter-spacing: .05em;
}
.kanadle-page .game-meta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 3px;
}
.kanadle-page .game-day {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--secondary);
}
.kanadle-page .streak-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 2px 7px;
  border: 1.5px solid var(--border);
  color: var(--secondary);
}
.kanadle-page .streak-badge.on { border-color: var(--primary); color: var(--primary); background: var(--tertiary); }

/* ── Toast ──────────────────────────────────────────────────── */
.kanadle-page .toast {
  position: fixed;
  top: 66px;
  left: 50%;
  transform: translateX(-50%) translateY(-6px);
  background: var(--primary);
  color: var(--theme);
  padding: 9px 18px;
  font-size: 13px;
  font-weight: 700;
  opacity: 0;
  pointer-events: none;
  transition: opacity .18s, transform .18s;
  z-index: 200;
  white-space: nowrap;
}
.kanadle-page .toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

/* ── Tile grid ──────────────────────────────────────────────── */
.kanadle-page .grid { display: flex; flex-direction: column; gap: 5px; }
.kanadle-page .grid-row { display: flex; gap: 5px; }
.kanadle-page .tile {
  width: 54px; height: 54px;
  border: 2px solid var(--border);
  display: flex; align-items: center; justify-content: center;
  font-family: var(--serif); font-size: 1.35rem; font-weight: 700;
  user-select: none;
  transition: border-color .1s;
}
.kanadle-page .tile.filled { border-color: var(--secondary); }
.kanadle-page .tile.correct { background: #538d4e; color: #fff; border-color: #538d4e; }
.kanadle-page .tile.present { background: #b59f3b; color: #fff; border-color: #b59f3b; }
.kanadle-page .tile.absent  { background: #3a3a3c; color: #fff; border-color: #3a3a3c; }
[data-theme="light"]  .kanadle-page .tile.absent { background: #787c7e; border-color: #787c7e; }
[data-theme="sakura"] .kanadle-page .tile.absent { background: #8a7f76; border-color: #8a7f76; }

.kanadle-page .tile.pop   { animation: kd-pop   .12s ease; }
.kanadle-page .tile.shake { animation: kd-shake .4s ease; }
.kanadle-page .tile.flip  { animation: kd-flip  .5s ease forwards; }
@keyframes kd-pop   { 0%,100%{transform:scale(1)} 50%{transform:scale(1.14)} }
@keyframes kd-shake { 0%,100%{transform:translateX(0)} 20%{transform:translateX(-6px)} 40%{transform:translateX(6px)} 60%{transform:translateX(-4px)} 80%{transform:translateX(4px)} }
@keyframes kd-flip  { 0%{transform:scaleY(1)} 45%{transform:scaleY(0)} 55%{transform:scaleY(0)} 100%{transform:scaleY(1)} }

/* ── Result panel ───────────────────────────────────────────── */
.kanadle-page .result-panel { display: none; width: 100%; border: 1.5px solid var(--primary); text-align: center; }
.kanadle-page .result-panel.show { display: block; }
.kanadle-page .rp-top { padding: 22px 18px 14px; border-bottom: 1px solid var(--border); background: var(--tertiary); }
.kanadle-page .rp-outcome { font-size: 10px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--secondary); margin-bottom: 6px; }
.kanadle-page .rp-word    { font-family: var(--serif); font-size: 2rem; font-weight: 700; line-height: 1.1; margin-bottom: 4px; }
.kanadle-page .rp-meaning { font-size: 13px; color: var(--secondary); }
.kanadle-page .rp-stats   { display: grid; grid-template-columns: repeat(3, 1fr); border-bottom: 1px solid var(--border); }
.kanadle-page .rps        { padding: 14px 10px; border-right: 1px solid var(--border); }
.kanadle-page .rps:last-child { border-right: none; }
.kanadle-page .rps-num    { font-family: var(--serif); font-size: 1.5rem; font-weight: 700; line-height: 1; margin-bottom: 2px; }
.kanadle-page .rps-label  { font-size: 10px; text-transform: uppercase; letter-spacing: .1em; color: var(--secondary); }
.kanadle-page .rp-next    { font-size: 11px; color: var(--secondary); padding: 10px 18px 0; }
.kanadle-page .rp-actions { padding: 14px 18px; display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }

/* ── Keyboard ───────────────────────────────────────────────── */
.kanadle-page .kboard { width: 100%; display: flex; flex-direction: column; gap: 3px; }
.kanadle-page .kboard-row { display: flex; gap: 3px; justify-content: center; }
.kanadle-page .kkey {
  height: 36px;
  flex: 1;
  border: 1.5px solid var(--border);
  background: var(--tertiary);
  color: var(--primary);
  font-family: var(--serif);
  font-size: 1rem;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: background .1s, color .1s, border-color .1s;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
  min-width: 0;
}
.kanadle-page .kkey:active { opacity: .65; }
.kanadle-page .kkey.wide { font-size: .65rem; font-family: var(--sans); font-weight: 700; letter-spacing: .02em; flex: 1.6; }
.kanadle-page .kkey.mod  { font-size: .8rem; font-family: var(--sans); color: var(--secondary); flex: 1.2; }
.kanadle-page .kkey.mod.active { background: var(--primary); color: var(--theme); border-color: var(--primary); }
.kanadle-page .kkey.correct { background: #538d4e; color: #fff; border-color: #538d4e; }
.kanadle-page .kkey.present { background: #b59f3b; color: #fff; border-color: #b59f3b; }
.kanadle-page .kkey.absent  { background: var(--border); color: var(--secondary); border-color: var(--border); }

/* ── Mobile ─────────────────────────────────────────────────── */
@media (max-width: 620px) {
  .kanadle-page .game-layout {
    flex-direction: column;
    border: none;
  }
  .kanadle-page .game-sidebar {
    width: 100%;
    position: static;
    border-right: none;
    border-bottom: 1.5px solid var(--border);
    overflow: hidden;
  }
  .kanadle-page .game-sidebar.collapsed .sb-section { display: none; }
  .kanadle-page .sb-toggle {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 14px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .07em;
    text-transform: uppercase;
    color: var(--secondary);
    cursor: pointer;
    border-bottom: 1px solid var(--border);
    user-select: none;
  }
  .kanadle-page .game-sidebar.collapsed .sb-toggle { border-bottom: none; }
  .kanadle-page .sb-toggle-arrow { transition: transform .2s; }
  .kanadle-page .game-sidebar.collapsed .sb-toggle-arrow { transform: rotate(-90deg); }
  .kanadle-page .tile { width: 50px; height: 50px; font-size: 1.2rem; }
  .kanadle-page .kkey { height: 32px; font-size: .9rem; }
  .kanadle-page .kboard { gap: 2px; }
  .kanadle-page .kboard-row { gap: 2px; }
}
@media (min-width: 621px) {
  .kanadle-page .sb-toggle { display: none; }
}
</style>

<div class="kanadle-page">
<div class="toast" id="toast"></div>

<div class="game-layout">

<!-- ── Sidebar ──────────────────────────────────────────────── -->
<aside class="game-sidebar collapsed" id="game-sidebar">

<div class="sb-toggle" id="sb-toggle" onclick="toggleSidebar()">
How to play &amp; hint
<span class="sb-toggle-arrow">▾</span>
</div>

<div class="sb-section">
<div class="sb-heading">How to play</div>
<p style="font-size:12px;color:var(--secondary);line-height:1.55;margin-bottom:10px">Guess the 5-kana Japanese word in 6 tries. After each guess the tiles change colour.</p>
<div class="sb-tile-row">
<div class="sb-tile correct">あ</div>
<div class="sb-tile-desc">Right kana,<br>right place</div>
</div>
<div class="sb-tile-row">
<div class="sb-tile present">い</div>
<div class="sb-tile-desc">Right kana,<br>wrong place</div>
</div>
<div class="sb-tile-row">
<div class="sb-tile absent">う</div>
<div class="sb-tile-desc">Not in<br>the word</div>
</div>
</div>

<div class="sb-section">
<div class="sb-heading">On-screen keyboard</div>
<p class="sb-tip">Tap any kana to add it to your guess.</p>
<p class="sb-tip">Press <span class="sb-key">゛</span> then a key for voiced sounds — <span class="sb-key">か</span>→が, <span class="sb-key">さ</span>→ざ, <span class="sb-key">た</span>→だ, <span class="sb-key">は</span>→ば.</p>
<p class="sb-tip">Press <span class="sb-key">°</span> then a key for the ぱ row — <span class="sb-key">は</span>→ぱ, <span class="sb-key">ひ</span>→ぴ etc.</p>
</div>

<div class="sb-section">
<div class="sb-heading">Type with your keyboard</div>
<p class="sb-tip">Type romaji and it converts to hiragana automatically:</p>
<p class="sb-tip">
<span class="sb-romaji">ka</span>→か &nbsp;
<span class="sb-romaji">shi</span>→し &nbsp;
<span class="sb-romaji">tsu</span>→つ
</p>
<p class="sb-tip">
<span class="sb-romaji">chi</span>→ち &nbsp;
<span class="sb-romaji">fu</span>→ふ &nbsp;
<span class="sb-romaji">ji</span>→じ
</p>
<p class="sb-tip">Double a consonant for っ — <span class="sb-romaji">kka</span>→っか, <span class="sb-romaji">tta</span>→った.</p>
<p class="sb-tip"><span class="sb-kbd">Enter</span> to submit &nbsp; <span class="sb-kbd">⌫</span> to delete</p>
</div>

<div class="sb-section">
<div class="sb-heading">Daily hint</div>
<p class="sb-tip">One hint per game. Reveals the category of today's word — not the meaning.</p>
<button class="hint-btn" id="hint-btn" onclick="revealHint()">💡 Reveal category hint</button>
<div class="hint-panel" id="hint-panel">
<div class="hint-cat-label">Today's word is in...</div>
<div class="hint-cat-text" id="hint-cat-text"></div>
</div>
</div>

</aside>

<!-- ── Main game ─────────────────────────────────────────────── -->
<div class="game-main">

<div class="game-header">
<div>
<div class="game-title">KANADLE <span class="game-title-jp">かなどる</span></div>
</div>
<div class="game-meta">
<div class="game-day" id="game-day">Day —</div>
<div class="streak-badge" id="streak-badge">🔥 0 streak</div>
</div>
</div>

<div class="grid" id="grid"></div>

<div class="result-panel" id="result-panel">
<div class="rp-top">
<div class="rp-outcome" id="rp-outcome"></div>
<div class="rp-word"    id="rp-word"></div>
<div class="rp-meaning" id="rp-meaning"></div>
</div>
<div class="rp-stats">
<div class="rps"><div class="rps-num" id="stat-played">0</div><div class="rps-label">Played</div></div>
<div class="rps"><div class="rps-num" id="stat-streak">0</div><div class="rps-label">Streak</div></div>
<div class="rps"><div class="rps-num" id="stat-best">0</div><div class="rps-label">Best</div></div>
</div>
<div class="rp-next" id="rp-next"></div>
<div class="rp-actions">
<button class="btn btn-solid" onclick="shareResult()">Share result</button>
</div>
</div>

<div class="kboard" id="kboard"></div>

</div>
</div>
</div>

<script>
// ── Word list ─────────────────────────────────────────────────────────────
// Each entry: [kana, meaning, romaji, category]
function kdMakeWords(cat, words) {
  return words.map(([w, m, r]) => [w, m, r, cat]);
}

const KD_WORDS = [
  ...kdMakeWords('Greetings', [
    ['ありがとう','thank you','arigatou'],
    ['さようなら','goodbye','sayounara'],
    ['おめでとう','congratulations','omedetou'],
    ['すみません','excuse me','sumimasen'],
    ['こんにちは','hello','konnichiwa'],
    ['がんばって','do your best','ganbatte'],
    ['きをつけて','take care','ki wo tsukete'],
    ['たのしんで','enjoy yourself','tanoshinde'],
  ]),
  ...kdMakeWords('Family', [
    ['おかあさん','mother','okaasan'],
    ['おとうさん','father','otousan'],
    ['おにいさん','older brother','oniisan'],
    ['おねえさん','older sister','oneesan'],
    ['おじいさん','grandfather','ojiisan'],
    ['おばあさん','grandmother','obaasan'],
  ]),
  ...kdMakeWords('Adjectives', [
    ['むずかしい','difficult','muzukashii'],
    ['おもしろい','interesting','omoshiroi'],
    ['いそがしい','busy','isogashii'],
    ['すばらしい','wonderful','subarashii'],
    ['なつかしい','nostalgic','natsukashii'],
    ['かわいそう','poor thing / pitiful','kawaisou'],
    ['きもちいい','feels good','kimochiii'],
    ['あたらしい','new / fresh','atarashii'],
    ['じょうずな','skilful','jouzuna'],
    ['ていねいな','polite / careful','teineina'],
    ['しんせつな','kind / helpful','shinsetsuna'],
    ['にぎやかな','lively / bustling','nigiyakana'],
    ['たいせつな','precious / important','taisetsuna'],
    ['はなやかな','gorgeous / colourful','hanayakana'],
  ]),
  ...kdMakeWords('Actions & verbs', [
    ['たべている','is eating','tabete iru'],
    ['のんでいる','is drinking','nonde iru'],
    ['あそんでる','is playing','asonderu'],
    ['はしってる','is running','hashitteru'],
    ['みています','is watching','mite imasu'],
    ['ねています','is sleeping','nete imasu'],
    ['わかります','I understand','wakarimasu'],
    ['できません','cannot do it','dekimasen'],
    ['わすれない','won\'t forget','wasurenai'],
    ['おぼえてる','remembering','oboeteru'],
    ['しっている','I know','shitte iru'],
    ['やってみる','give it a try','yatte miru'],
    ['あるいてる','is walking','aruiteru'],
    ['おきました','woke up','okimashita'],
    ['かいました','bought it','kaimashita'],
    ['いきました','went there','ikimashita'],
    ['よみました','read it','yomimashita'],
    ['かきました','wrote it','kakimashita'],
    ['うたいます','will sing','utaimasu'],
    ['みえません','cannot see','miemasen'],
    ['きこえない','cannot hear','kikoenai'],
  ]),
  ...kdMakeWords('Food & drink', [
    ['あさごはん','breakfast','asagohan'],
    ['ひるごはん','lunch','hirugohan'],
    ['ばんごはん','dinner','bangohan'],
    ['おべんとう','bento box','obentou'],
    ['おみそしる','miso soup','omisoshiru'],
    ['たまごやき','tamagoyaki','tamagoyaki'],
    ['にぎりずし','nigiri sushi','nigirizushi'],
    ['まぜごはん','mixed rice','magegohan'],
    ['やきさかな','grilled fish','yakisakana'],
    ['いためもの','stir fry','itamemono'],
    ['かすていら','castella cake','kasutera'],
    ['たぬきそば','tanuki soba','tanukisoba'],
    ['いなりずし','inari sushi','inarizushi'],
    ['まんじゅう','manju sweet','manjuu'],
    ['わらびもち','warabi mochi','warabimochi'],
    ['ところてん','tokoroten jelly','tokoroten'],
    ['ちらしずし','chirashi sushi','chirashizushi'],
    ['うなぎどん','unagi rice bowl','unagidon'],
    ['さんまやき','grilled saury','sanmayaki'],
    ['ほたてがい','scallop','hotategai'],
    ['しじみじる','clam soup','shijimijiru'],
    ['かきふらい','fried oyster','kakifurai'],
    ['ほうじちゃ','hojicha tea','houjicha'],
  ]),
  ...kdMakeWords('Places', [
    ['えいがかん','cinema','eigakan'],
    ['としょかん','library','toshokan'],
    ['びょういん','hospital','byouin'],
    ['ようちえん','kindergarten','youchien'],
    ['こうさてん','intersection','kousaten'],
    ['びようしつ','beauty salon','biyoushitsu'],
    ['しょうてん','shop / store','shouten'],
    ['ゆうえんち','amusement park','yuuenchi'],
    ['たいしかん','embassy','taishikan'],
    ['やきとりや','yakitori restaurant','yakitoriya'],
    ['すしやさん','sushi restaurant','sushiyasan'],
    ['そばやさん','soba restaurant','sobayasan'],
    ['てんぷらや','tempura restaurant','tenpuraya'],
    ['ぱんやさん','bakery','panyasan'],
    ['にくやさん','butcher\'s shop','nikuyasan'],
    ['やおやさん','greengrocer','yaoyasan'],
    ['はなやさん','flower shop','hanayasan'],
    ['ほんやさん','bookshop','honyasan'],
  ]),
  ...kdMakeWords('Transport & travel', [
    ['じてんしゃ','bicycle','jitensha'],
    ['ていきけん','commuter pass','teikiken'],
    ['しゅうでん','last train of the night','shuuden'],
    ['しゅっぱつ','departure','shuppatsu'],
    ['とうちゃく','arrival','touchaku'],
  ]),
  ...kdMakeWords('Nature & seasons', [
    ['なつやすみ','summer holiday','natsuyasumi'],
    ['ふゆやすみ','winter holiday','fuyuyasumi'],
    ['はくちょう','swan','hakuchou'],
    ['みずたまり','puddle','mizutamari'],
    ['ゆきだるま','snowman','yukidaruma'],
    ['もみじがり','autumn leaf viewing','momijigari'],
    ['にほんばれ','crystal clear sky','nihonbare'],
    ['こいのぼり','carp streamer','koinobori'],
    ['ひなまつり','Hinamatsuri festival','hinamatsuri'],
    ['ほたるがり','firefly watching','hotarugari'],
    ['きのこがり','mushroom picking','kinokogari'],
    ['つきみだん','moon-viewing dumplings','tsukimidan'],
    ['おつきさま','the moon','otsukisama'],
    ['ゆきのはな','snowflake','yukinohana'],
    ['なみのおと','sound of waves','naminooto'],
    ['あかとんぼ','red dragonfly','akatombo'],
    ['さくらいろ','cherry blossom colour','sakurairo'],
    ['かざぐるま','pinwheel / windmill','kazaguruma'],
    ['こどものひ','Children\'s Day','kodomono hi'],
    ['はなみかい','flower-viewing party','hanamikai'],
    ['すいかわり','watermelon splitting game','suikawari'],
    ['ふじのはな','wisteria flower','fujino hana'],
  ]),
  ...kdMakeWords('Days of the week', [
    ['にちようび','Sunday','nichiyoubi'],
    ['げつようび','Monday','getsuyoubi'],
    ['すいようび','Wednesday','suiyoubi'],
    ['もくようび','Thursday','mokuyoubi'],
    ['きんようび','Friday','kin\'youbi'],
  ]),
  ...kdMakeWords('Home & daily life', [
    ['おちゃわん','rice bowl','ochawan'],
    ['おてあらい','bathroom / toilet','otearai'],
    ['たたみべや','tatami room','tatamibea'],
    ['おせんたく','laundry','osentaku'],
    ['おちゃかい','tea ceremony gathering','ochakai'],
    ['かぜぐすり','cold medicine','kazegusuri'],
    ['かいぎしつ','meeting room','kaigishitsu'],
  ]),
  ...kdMakeWords('Study & culture', [
    ['べんきょう','studying','benkyou'],
    ['りゅうがく','studying abroad','ryuugaku'],
    ['ものがたり','tale / story','monogatari'],
    ['おしゃべり','chatting / chatterbox','oshaberi'],
    ['ひとりごと','talking to oneself','hitorigoto'],
    ['しょうぼう','firefighting','shoubouu'],
  ]),
  ...kdMakeWords('Expressions', [
    ['たのしみに','looking forward to it','tanoshimini'],
    ['ゆっくりと','slowly / take it easy','yukkurito'],
    ['おたがいに','each other / mutually','otagaini'],
  ]),
  ...kdMakeWords('Weather & seasons', [
    ['あめがふる','it rains / raining','ame ga furu'],
    ['ゆきがふる','it snows / snowing','yuki ga furu'],
    ['はれている','it\'s sunny / clear','harete iru'],
    ['すずしいひ','a cool day','suzushii hi'],
    ['つゆのじき','the rainy season','tsuyu no jiki'],
    ['にじがでた','a rainbow appeared','niji ga deta'],
    ['かみなりが','thunder (subject marker)','kaminari ga'],
    ['たいふうが','a typhoon (subject marker)','taifuu ga'],
  ]),
  ...kdMakeWords('Adjectives — too much (Xすぎる)', [
    ['たかすぎる','too expensive','takasugiru'],
    ['やすすぎる','too cheap','yasusugiru'],
    ['おもすぎる','too heavy','omosugiru'],
    ['かるすぎる','too light','karusugiru'],
    ['ながすぎる','too long','nagasugiru'],
    ['はやすぎる','too fast / early','hayasugiru'],
    ['おそすぎる','too slow / late','ososugiru'],
    ['おおすぎる','too many / much','oosugiru'],
    ['ちかすぎる','too close','chikasugiru'],
    ['とおすぎる','too far','toosugiru'],
    ['せますぎる','too narrow / small','semasugiru'],
    ['ひろすぎる','too wide','hirosugiru'],
    ['あますぎる','too sweet','amasugiru'],
    ['からすぎる','too spicy','karasugiru'],
    ['にがすぎる','too bitter','nigasugiru'],
    ['うすすぎる','too thin / weak','ususugiru'],
    ['こわすぎる','too scary','kowasugiru'],
    ['つよすぎる','too strong','tsuyosugiru'],
    ['よわすぎる','too weak','yowasugiru'],
    ['おいしそう','looks delicious','oishisou'],
    ['たのしそう','looks fun','tanoshisou'],
    ['うれしそう','looks happy','ureshisou'],
    ['さびしそう','looks lonely','sabishisou'],
    ['あぶなそう','looks dangerous','abunasou'],
    ['げんきそう','looks energetic','genkisou'],
    ['しんぱいだ','I\'m worried','shinpai da'],
  ]),
  ...kdMakeWords('Actions & verbs (extra)', [
    ['のみました','drank','nomimashita'],
    ['ききました','listened / heard','kikimashita'],
    ['たちました','stood up','tachimashita'],
    ['とびました','flew / jumped','tobimashita'],
    ['できました','was able to / done','dekimashita'],
    ['かりました','borrowed','karimashita'],
    ['はなします','will speak / tell','hanashimasu'],
    ['おしえます','will teach','oshiemasu'],
    ['おくります','will send','okurimasu'],
    ['つくります','will make','tsukurimasu'],
    ['さがします','will search for','sagashimasu'],
    ['なおします','will fix / repair','naoshimasu'],
    ['けしました','erased / turned off','keshimashita'],
    ['よびました','called out to','yobimashita'],
    ['まけました','lost (a game)','makemashita'],
    ['かちました','won (a game)','kachimashita'],
    ['はじめます','will begin','hajimemasu'],
    ['おわります','will finish','owarimasu'],
    ['つづきます','will continue','tsuzukimasu'],
    ['きめました','decided','kimemashita'],
    ['しらべます','will look into / check','shirabemasu'],
    ['あつめます','will collect','atsumemasu'],
    ['すすみます','will proceed / advance','susumimasu'],
    ['まもります','will protect','mamorimasu'],
    ['こまります','get into trouble','komarimasu'],
    ['おどります','will dance','odorimasu'],
    ['さわります','will touch','sawarimasu'],
    ['ひろいます','will pick up','hiroimasu'],
    ['すてました','threw away','sutemashita'],
    ['はこびます','will carry','hakobimasu'],
    ['よごします','will make dirty','yogoshimasu'],
    ['こわします','will break (something)','kowashimasu'],
    ['なくします','will lose (an item)','nakushimasu'],
    ['みつけます','will find','mitsukemasu'],
    ['さんぽする','take a walk','sanpo suru'],
    ['よやくする','make a reservation','yoyaku suru'],
    ['そうじする','clean / tidy up','souji suru'],
    ['でんわする','make a phone call','denwa suru'],
  ]),
  ...kdMakeWords('Body & health', [
    ['ねつがある','have a fever','netsu ga aru'],
    ['せきがでる','have a cough','seki ga deru'],
    ['げんきです','I\'m well / fine','genki desu'],
    ['つかれたな','I\'m tired (casual)','tsukaretana'],
    ['ねむいです','I\'m sleepy','nemui desu'],
    ['はがいたい','my tooth hurts','ha ga itai'],
  ]),
  ...kdMakeWords('Shopping & money', [
    ['いくらです','how much is it','ikura desu'],
    ['たかいです','it\'s expensive','takai desu'],
    ['やすいです','it\'s cheap','yasui desu'],
    ['げんきんで','by cash','genkin de'],
    ['おつりです','this is your change','otsuri desu'],
  ]),
  ...kdMakeWords('School & work', [
    ['かいぎです','it\'s a meeting','kaigi desu'],
    ['しごとです','it\'s work / a job','shigoto desu'],
    ['やすみます','will take a rest / day off','yasumimasu'],
  ]),
  ...kdMakeWords('Animals & nature (extra)', [
    ['いぬがいる','there\'s a dog','inu ga iru'],
    ['ねこがねる','the cat sleeps','neko ga neru'],
    ['とりがとぶ','the bird flies','tori ga tobu'],
    ['もりのなか','inside the forest','mori no naka'],
    ['はながさく','the flower blooms','hana ga saku'],
    ['きがたかい','the tree is tall','ki ga takai'],
  ]),
  ...kdMakeWords('Food & drink (extra)', [
    ['おいしいね','it\'s delicious, isn\'t it','oishii ne'],
    ['まずいです','it tastes bad','mazui desu'],
    ['みずをのむ','drink water','mizu wo nomu'],
  ]),
  ...kdMakeWords('Places & directions (extra)', [
    ['えきのまえ','in front of the station','eki no mae'],
    ['ひだりがわ','the left side','hidari gawa'],
    ['こうばんへ','to the police box','kouban e'],
  ]),
  ...kdMakeWords('Time & daily routine (extra)', [
    ['こんげつは','this month (topic)','kongetsu wa'],
    ['らいげつは','next month (topic)','raigetsu wa'],
    ['きょねんは','last year (topic)','kyonen wa'],
    ['らいねんは','next year (topic)','rainen wa'],
    ['あさおきる','wake up in the morning','asa okiru'],
    ['よるねます','go to sleep at night','yoru nemasu'],
    ['じかんです','it\'s time','jikan desu'],
    ['おくれます','will be late','okuremasu'],
    ['まにあった','made it in time','maniatta'],
  ]),
  ...kdMakeWords('Home & daily life (extra)', [
    ['ごみをだす','take out the trash','gomi wo dasu'],
    ['やちんです','it\'s the rent','yachin desu'],
  ]),
  ...kdMakeWords('Study & culture (extra)', [
    ['にほんごを','Japanese language (object)','nihongo wo'],
    ['えいごより','more than English','eigo yori'],
  ]),
  ...kdMakeWords('Expressions (extra)', [
    ['ほんとうに','really / truly','hontou ni'],
    ['たぶんです','probably','tabun desu'],
    ['もちろんだ','of course','mochiron da'],
    ['どういたし','don\'t mention it (part)','dou itashi'],
    ['やっぱりね','I knew it / as expected','yappari ne'],
    ['それはいい','that\'s good','sore wa ii'],
    ['それはだめ','that\'s no good','sore wa dame'],
  ]),
  ...kdMakeWords('Places (extra)', [
    ['やっきょく','pharmacy','yakkyoku'],
    ['しょくどう','cafeteria / dining hall','shokudou'],
    ['こうじょう','factory','koujou'],
    ['びよういん','beauty salon','biyouin'],
    ['しやくしょ','city hall','shiyakusho'],
    ['きっさてん','coffee shop / cafe','kissaten'],
    ['ゆうびんや','the post office (casual)','yuubin ya'],
  ]),
  ...kdMakeWords('Family & people (extra)', [
    ['ごしゅじん','(someone\'s) husband','goshujin'],
    ['むすこさん','son (polite)','musuko-san'],
    ['むすめさん','daughter (polite)','musume-san'],
    ['おいごさん','nephew (polite)','oigo-san'],
    ['めいごさん','niece (polite)','meigo-san'],
    ['おさなじみ','childhood friend','osananajimi'],
  ]),
  ...kdMakeWords('Actions & verbs — masu present (2-kana stem + ます)', [
    ['かえります','will go home','kaerimasu'],
    ['はいります','will enter','hairimasu'],
    ['でかけます','will go out','dekakemasu'],
    ['もどります','will return','modorimasu'],
    ['とまります','will stop / stay','tomarimasu'],
    ['はしります','will run','hashirimasu'],
    ['あるきます','will walk','arukimasu'],
    ['わたります','will cross','watarimasu'],
    ['のぼります','will climb','noborimasu'],
    ['わかれます','will part ways','wakaremasu'],
  ]),
  ...kdMakeWords('Actions & verbs — ました past (2-kana stem + ました)', [
    ['いいました','said','iimashita'],
    ['あいました','met','aimashita'],
    ['とりました','took / got','torimashita'],
    ['つきました','arrived','tsukimashita'],
    ['いれました','put in','iremashita'],
    ['だしました','took out / submitted','dashimashita'],
    ['もちました','held / carried','mochimashita'],
    ['おりました','got off','orimashita'],
    ['のりました','got on / rode','norimashita'],
  ]),
  ...kdMakeWords('Actions & verbs — ません negative (stem + ません)', [
    ['いきません','won\'t go','ikimasen'],
    ['たべません','won\'t eat','tabemasen'],
    ['のみません','won\'t drink','nomimasen'],
    ['かいません','won\'t buy','kaimasen'],
    ['よみません','won\'t read','yomimasen'],
    ['かきません','won\'t write','kakimasen'],
  ]),
  ...kdMakeWords('Adjectives — plain 5-kana (extra)', [
    ['やわらかい','soft','yawarakai'],
    ['かたいです','it\'s hard / stiff','katai desu'],
    ['まるいです','it\'s round','marui desu'],
    ['ひくいです','it\'s low / short','hikui desu'],
    ['ふかいです','it\'s deep','fukai desu'],
    ['あさいです','it\'s shallow','asai desu'],
    ['きたないな','it\'s dirty (casual)','kitanai na'],
    ['きれいだね','it\'s pretty, isn\'t it','kirei da ne'],
    ['しずかだね','it\'s quiet, isn\'t it','shizuka da ne'],
    ['にぎやかだ','it\'s lively','nigiyaka da'],
    ['べんりだね','it\'s convenient','benri da ne'],
    ['ふべんだよ','it\'s inconvenient','fuben da yo'],
    ['じょうぶだ','it\'s sturdy','joubu da'],
    ['ゆうめいだ','it\'s famous','yuumei da'],
    ['ひつような','necessary','hitsuyou na'],
    ['じゆうです','it\'s free (unrestricted)','jiyuu desu'],
    ['あんぜんだ','it\'s safe','anzen da'],
    ['きけんです','it\'s dangerous','kiken desu'],
  ]),
  ...kdMakeWords('Numbers, time & counting (extra)', [
    ['さんじかん','three hours','sanjikan'],
    ['よじかんも','as much as four hours','yojikan mo'],
    ['ごふんまえ','five minutes before','gofun mae'],
    ['じっぷんご','ten minutes later','jippun go'],
    ['はんとしも','as much as half a year','hantoshi mo'],
    ['みっかまえ','three days ago','mikka mae'],
    ['さんかげつ','three months','sankagetsu'],
  ]),
  ...kdMakeWords('Sports, hobbies & play', [
    ['やきゅうを','baseball (object)','yakyuu wo'],
    ['すいえいが','swimming (subject)','suiei ga'],
    ['しゃしんを','a photo (object)','shashin wo'],
    ['つりをする','go fishing','tsuri wo suru'],
    ['やまのぼり','mountain climbing','yamanobori'],
  ]),
  ...kdMakeWords('Clothing & appearance', [
    ['ふくをきる','wear clothes','fuku wo kiru'],
    ['くつをはく','put on shoes','kutsu wo haku'],
    ['ぼうしです','it\'s a hat','boushi desu'],
    ['めがねです','it\'s glasses','megane desu'],
    ['かさをさす','put up an umbrella','kasa wo sasu'],
    ['てぶくろを','gloves (object)','tebukuro wo'],
  ]),
  ...kdMakeWords('Expressions — extra (careful count)', [
    ['わたしもだ','me too (casual)','watashi mo da'],
    ['きをつけろ','watch out! (rough)','ki wo tsukero'],
    ['がんばろう','let\'s do our best','ganbarou'],
    ['しんじてる','I believe (in you)','shinjiteru'],
    ['きにいった','I liked it','ki ni itta'],
    ['どうしよう','what should I do','dou shiyou'],
    ['しかたない','it can\'t be helped','shikata nai'],
    ['めんどうだ','it\'s a hassle','mendou da'],
    ['たいへんだ','that\'s tough','taihen da'],
    ['よかったね','that\'s great, isn\'t it','yokatta ne'],
    ['ざんねんだ','that\'s a shame','zannen da'],
  ]),
  ...kdMakeWords('Family & people (round 3)', [
    ['いとこたち','cousins','itoko-tachi'],
    ['おともだち','friend (polite)','o-tomodachi'],
    ['こうはいだ','(is a) junior / underclassman','kouhai da'],
  ]),
  ...kdMakeWords('Seasons & events (round 3)', [
    ['なつまつり','summer festival','natsu matsuri'],
    ['ゆきまつり','snow festival','yuki matsuri'],
    ['おおみそか','New Year\'s Eve','oomisoka'],
    ['しょうがつ','New Year','shougatsu'],
    ['つゆあけた','the rainy season ended','tsuyu aketa'],
  ]),
  ...kdMakeWords('Gifts & shops (round 3)', [
    ['おいわいだ','it\'s a celebration','oiwai da'],
    ['おくりもの','a gift / present','okurimono'],
    ['おみやげや','souvenir shop','omiyage-ya'],
    ['くつやさん','shoe shop','kutsuya-san'],
    ['ふくやさん','clothes shop','fukuya-san'],
    ['おいわいに','for the celebration','oiwai ni'],
  ]),
  ...kdMakeWords('Na-adjectives (round 3)', [
    ['かんぜんだ','it\'s perfect / complete','kanzen da'],
    ['ふくざつだ','it\'s complicated','fukuzatsu da'],
    ['かんたんだ','it\'s simple / easy','kantan da'],
    ['めいわくだ','it\'s a nuisance','meiwaku da'],
    ['しんせんだ','it\'s fresh','shinsen da'],
    ['すなおだね','honest, isn\'t it','sunao da ne'],
    ['りっぱだね','splendid, isn\'t it','rippa da ne'],
  ]),
  ...kdMakeWords('I-adjectives (round 3)', [
    ['めずらしい','rare / unusual','mezurashii'],
    ['おそろしい','frightening / terrible','osoroshii'],
  ]),
  ...kdMakeWords('More verbs — verified stems (round 3)', [
    ['つたえます','will convey / tell','tsutaemasu'],
    ['おぼえます','will memorize','oboemasu'],
    ['わすれます','will forget','wasuremasu'],
    ['きこえます','can be heard','kikoemasu'],
    ['みえますか','can it be seen?','miemasu ka'],
  ]),
  ...kdMakeWords('More nouns, compact (round 3)', [
    ['ひるやすみ','lunch break','hiruyasumi'],
    ['よるおそく','late at night','yoru osoku'],
    ['あさはやく','early in the morning','asa hayaku'],
    ['まんなかに','in the middle','mannaka ni'],
    ['すぐそばに','right next to','sugu soba ni'],
    ['いちばんに','first / number one','ichiban ni'],
    ['さいごまで','until the end','saigo made'],
    ['さいしょに','at the beginning','saisho ni'],
    ['とちゅうで','along the way','tochuu de'],
  ]),
];

// Runtime filter: only exactly-5-char entries become answers
const KD_VALID = KD_WORDS.filter(([w]) => [...w].length === 5);

// ── Daily word ────────────────────────────────────────────────────────────
const KD_EPOCH = new Date('2026-01-01T00:00:00+09:00');
function kdDayNumber() {
  const now = new Date();
  const jst = new Date(now.toLocaleString('en-US', { timeZone: 'Asia/Tokyo' }));
  jst.setHours(0, 0, 0, 0);
  return Math.floor((jst - KD_EPOCH) / 86400000) + 1;
}
const DAY         = kdDayNumber();
const ENTRY       = KD_VALID[(DAY - 1) % KD_VALID.length];
const ANSWER      = [...ENTRY[0]];
const MEANING     = ENTRY[1];
const WORD_ROMAJI = ENTRY[2];
const CATEGORY    = ENTRY[3];

// ── Modifier maps ─────────────────────────────────────────────────────────
const DAKUTEN = {
  'か':'が','き':'ぎ','く':'ぐ','け':'げ','こ':'ご',
  'さ':'ざ','し':'じ','す':'ず','せ':'ぜ','そ':'ぞ',
  'た':'だ','ち':'ぢ','つ':'づ','て':'で','と':'ど',
  'は':'ば','ひ':'び','ふ':'ぶ','へ':'べ','ほ':'ぼ',
};
const HANDAKUTEN = {
  'は':'ぱ','ひ':'ぴ','ふ':'ぷ','へ':'ぺ','ほ':'ぽ',
};
const TO_BASE = {};
Object.entries(DAKUTEN).forEach(([b,v]) => { TO_BASE[v] = b; });
Object.entries(HANDAKUTEN).forEach(([b,v]) => { TO_BASE[v] = b; });

// ── State ─────────────────────────────────────────────────────────────────
const SK = 'kanadle_v2';
let state = loadState();

function loadState() {
  try {
    const s = JSON.parse(localStorage.getItem(SK) || '{}');
    if (s.day === DAY) return s;
    return {
      day: DAY, guesses: [], grades: [], status: 'playing',
      streak: s.status === 'won' ? (s.streak || 0) : 0,
      best:   Math.max(s.best || 0, s.status === 'won' ? (s.streak || 0) : 0),
      played: s.played || 0,
      hintUsed: false,
    };
  } catch(e) {
    return { day: DAY, guesses: [], grades: [], status: 'playing', streak: 0, best: 0, played: 0, hintUsed: false };
  }
}
function save() {
  try { localStorage.setItem(SK, JSON.stringify(state)); } catch(e) {}
}

// ── Modifier state ────────────────────────────────────────────────────────
let modD = false;
let modH = false;

function setMod(d, h) {
  modD = d; modH = h;
  document.getElementById('mod-d')?.classList.toggle('active', d);
  document.getElementById('mod-h')?.classList.toggle('active', h);
}

// ── Key states ────────────────────────────────────────────────────────────
const keyStates = {};
const RANK = { correct: 2, present: 1, absent: 0 };

function updateKeys(guess, result) {
  guess.forEach((k, i) => {
    const base = TO_BASE[k] || k;
    const curr = result[i];
    if (!keyStates[base] || RANK[curr] > RANK[keyStates[base]]) keyStates[base] = curr;
  });
}

// ── Grading ───────────────────────────────────────────────────────────────
function grade(guess) {
  const result = new Array(5).fill('absent');
  const pool   = [...ANSWER];
  for (let i = 0; i < 5; i++) {
    if (guess[i] === ANSWER[i]) { result[i] = 'correct'; pool[i] = null; }
  }
  for (let i = 0; i < 5; i++) {
    if (result[i] === 'correct') continue;
    const j = pool.indexOf(guess[i]);
    if (j !== -1) { result[i] = 'present'; pool[j] = null; }
  }
  return result;
}

// ── Romaji → hiragana converter ────────────────────────────────────────────
const ROMAJI_MAP = {
  'a':'あ','i':'い','u':'う','e':'え','o':'お',
  'nn':'ん',
  'ka':'か','ki':'き','ku':'く','ke':'け','ko':'こ',
  'kya':'きゃ','kyu':'きゅ','kyo':'きょ',
  'sa':'さ','si':'し','su':'す','se':'せ','so':'そ',
  'shi':'し',
  'sha':'しゃ','shu':'しゅ','sho':'しょ',
  'sya':'しゃ','syu':'しゅ','syo':'しょ',
  'ta':'た','ti':'ち','tu':'つ','te':'て','to':'と',
  'chi':'ち','tsu':'つ',
  'cha':'ちゃ','chu':'ちゅ','cho':'ちょ',
  'tya':'ちゃ','tyu':'ちゅ','tyo':'ちょ',
  'na':'な','ni':'に','nu':'ぬ','ne':'ね','no':'の',
  'nya':'にゃ','nyu':'にゅ','nyo':'にょ',
  'ha':'は','hi':'ひ','hu':'ふ','he':'へ','ho':'ほ',
  'fu':'ふ',
  'hya':'ひゃ','hyu':'ひゅ','hyo':'ひょ',
  'ma':'ま','mi':'み','mu':'む','me':'め','mo':'も',
  'mya':'みゃ','myu':'みゅ','myo':'みょ',
  'ya':'や','yu':'ゆ','yo':'よ',
  'ra':'ら','ri':'り','ru':'る','re':'れ','ro':'ろ',
  'rya':'りゃ','ryu':'りゅ','ryo':'りょ',
  'wa':'わ','wi':'ゐ','wu':'う','we':'ゑ','wo':'を',
  'ga':'が','gi':'ぎ','gu':'ぐ','ge':'げ','go':'ご',
  'gya':'ぎゃ','gyu':'ぎゅ','gyo':'ぎょ',
  'za':'ざ','zi':'じ','zu':'ず','ze':'ぜ','zo':'ぞ',
  'ji':'じ',
  'ja':'じゃ','ju':'じゅ','jo':'じょ',
  'jya':'じゃ','jyu':'じゅ','jyo':'じょ',
  'da':'だ','di':'ぢ','du':'づ','de':'で','do':'ど',
  'dya':'ぢゃ','dyu':'ぢゅ','dyo':'ぢょ',
  'ba':'ば','bi':'び','bu':'ぶ','be':'べ','bo':'ぼ',
  'bya':'びゃ','byu':'びゅ','byo':'びょ',
  'pa':'ぱ','pi':'ぴ','pu':'ぷ','pe':'ぺ','po':'ぽ',
  'pya':'ぴゃ','pyu':'ぴゅ','pyo':'ぴょ',
  'ltu':'っ','ltsu':'っ','xtu':'っ','xtsu':'っ',
  'lya':'ゃ','lyu':'ゅ','lyo':'ょ',
  'la':'ぁ','li':'ぃ','lu':'ぅ','le':'ぇ','lo':'ぉ',
};
const ROMAJI_KEYS = Object.keys(ROMAJI_MAP);
let romajiBuffer = '';

function resolveBuffer() {
  const VOWELS = 'aeiou';
  while (romajiBuffer.length > 0) {
    if (ROMAJI_MAP[romajiBuffer]) {
      const kana = ROMAJI_MAP[romajiBuffer];
      for (const k of [...kana]) pushKana(k);
      romajiBuffer = '';
      showPendingRomaji();
      continue;
    }
    if (romajiBuffer.length >= 2) {
      const c0 = romajiBuffer[0], c1 = romajiBuffer[1];
      if (c0 === c1 && c0 !== 'n' && !VOWELS.includes(c0)) {
        pushKana('っ');
        romajiBuffer = romajiBuffer.slice(1);
        continue;
      }
    }
    if (romajiBuffer[0] === 'n' && romajiBuffer.length >= 2) {
      const next = romajiBuffer[1];
      if (next === 'n') { pushKana('ん'); romajiBuffer = romajiBuffer.slice(2); continue; }
      if (!'aiueony'.includes(next)) { pushKana('ん'); romajiBuffer = romajiBuffer.slice(1); continue; }
    }
    if (ROMAJI_KEYS.some(k => k.startsWith(romajiBuffer))) break;
    romajiBuffer = romajiBuffer.slice(1);
  }
  showPendingRomaji();
}

function processRomaji(key) {
  if (state.status !== 'playing') return;
  if (!/^[a-z]$/i.test(key)) return;
  if (cur.length >= 5 && romajiBuffer === '') return;
  romajiBuffer += key.toLowerCase();
  resolveBuffer();
}

function showPendingRomaji() {
  const row = state.guesses.length;
  const col = cur.length;
  if (row >= 6 || col >= 5) return;
  const tile = document.getElementById(`t-${row}-${col}`);
  if (!tile) return;
  if (romajiBuffer) {
    tile.textContent = romajiBuffer;
    tile.style.fontSize = '.6rem';
    tile.style.color = 'var(--secondary)';
    tile.style.letterSpacing = '.03em';
    tile.classList.add('filled');
  } else {
    tile.textContent = '';
    tile.style.fontSize = '';
    tile.style.color = '';
    tile.style.letterSpacing = '';
    tile.classList.remove('filled');
  }
}

// ── Current guess ─────────────────────────────────────────────────────────
let cur = [];

function pushKana(k) {
  if (state.status !== 'playing' || cur.length >= 5) return;
  cur.push(k);
  const row = state.guesses.length, col = cur.length - 1;
  const tile = document.getElementById(`t-${row}-${col}`);
  if (tile) {
    tile.textContent = k;
    tile.style.fontSize = '';
    tile.style.color = '';
    tile.style.letterSpacing = '';
    tile.classList.add('filled');
    void tile.offsetWidth;
    tile.classList.add('pop');
    tile.addEventListener('animationend', () => tile.classList.remove('pop'), { once: true });
  }
}

function addKana(k) {
  let ch = k;
  if (modD) { ch = DAKUTEN[k] || k; setMod(false, false); }
  else if (modH) { ch = HANDAKUTEN[k] || k; setMod(false, false); }
  pushKana(ch);
}

function del() {
  if (state.status !== 'playing') return;
  setMod(false, false);
  if (romajiBuffer.length > 0) {
    romajiBuffer = romajiBuffer.slice(0, -1);
    showPendingRomaji();
    return;
  }
  if (!cur.length) return;
  const row = state.guesses.length, col = cur.length - 1;
  const tile = document.getElementById(`t-${row}-${col}`);
  if (tile) { tile.textContent = ''; tile.classList.remove('filled'); }
  cur.pop();
}

function submit() {
  if (state.status !== 'playing') return;
  if (romajiBuffer === 'n') { pushKana('ん'); romajiBuffer = ''; }
  if (cur.length < 5) { shakeRow(state.guesses.length); showToast('5文字入力してください'); return; }
  const guess  = [...cur];
  const result = grade(guess);
  state.guesses.push(guess);
  state.grades.push(result);
  cur = []; romajiBuffer = '';
  const ri = state.guesses.length - 1;
  revealRow(ri, guess, result, () => {
    updateKeys(guess, result);
    refreshKb();
    const won  = result.every(r => r === 'correct');
    const lost = !won && state.guesses.length >= 6;
    if (won) {
      state.status = 'won';
      state.streak = (state.streak || 0) + 1;
      state.best   = Math.max(state.best || 0, state.streak);
      state.played = (state.played || 0) + 1;
      save();
      const msgs = ['完璧！🎉','すごい！','よくできました！','正解！'];
      showToast(msgs[Math.min(ri, msgs.length - 1)]);
      setTimeout(() => showResult(true), 500);
    } else if (lost) {
      state.status = 'lost';
      state.streak = 0;
      state.played = (state.played || 0) + 1;
      save();
      setTimeout(() => showResult(false), 500);
    } else {
      save();
    }
  });
}

// ── Animation ─────────────────────────────────────────────────────────────
function revealRow(ri, guess, result, cb) {
  const D = 280;
  result.forEach((res, col) => {
    const tile = document.getElementById(`t-${ri}-${col}`);
    if (!tile) return;
    setTimeout(() => {
      tile.classList.add('flip');
      setTimeout(() => { tile.className = `tile ${res}`; tile.textContent = guess[col]; }, 230);
    }, col * D);
  });
  setTimeout(cb, result.length * D + 280);
}

function shakeRow(ri) {
  for (let c = 0; c < 5; c++) {
    const t = document.getElementById(`t-${ri}-${c}`);
    if (!t) continue;
    t.classList.remove('shake'); void t.offsetWidth; t.classList.add('shake');
    t.addEventListener('animationend', () => t.classList.remove('shake'), { once: true });
  }
}

// ── Keyboard ──────────────────────────────────────────────────────────────
const KB = [
  ['あ','い','う','え','お'],
  ['か','き','く','け','こ'],
  ['さ','し','す','せ','そ'],
  ['た','ち','つ','て','と'],
  ['な','に','ぬ','ね','の'],
  ['は','ひ','ふ','へ','ほ'],
  ['ま','み','む','め','も'],
  ['や','ゆ','よ','ゃ','ゅ'],
  ['ら','り','る','れ','ろ'],
  ['わ','を','ん','っ','ょ'],
  ['゛','°','←','ENTER'],
];

function buildKb() {
  const kb = document.getElementById('kboard');
  KB.forEach((row, ri) => {
    const rowEl = document.createElement('div');
    rowEl.className = 'kboard-row';
    const isAction = ri === KB.length - 1;
    row.forEach(k => {
      const btn = document.createElement('button');
      if (isAction) {
        if (k === '゛') {
          btn.className = 'kkey mod'; btn.id = 'mod-d'; btn.textContent = '゛';
          btn.addEventListener('click', () => setMod(!modD, false));
        } else if (k === '°') {
          btn.className = 'kkey mod'; btn.id = 'mod-h'; btn.textContent = '°';
          btn.addEventListener('click', () => setMod(false, !modH));
        } else if (k === '←') {
          btn.className = 'kkey wide'; btn.textContent = '←';
          btn.addEventListener('click', del);
        } else {
          btn.className = 'kkey wide'; btn.textContent = 'ENTER';
          btn.addEventListener('click', submit);
        }
      } else {
        btn.className = 'kkey';
        btn.textContent = k;
        btn.dataset.k = k;
        btn.addEventListener('click', () => addKana(k));
      }
      rowEl.appendChild(btn);
    });
    kb.appendChild(rowEl);
  });
}

function refreshKb() {
  document.querySelectorAll('.kkey[data-k]').forEach(btn => {
    const s = keyStates[btn.dataset.k];
    if (s) btn.className = `kkey ${s}`;
  });
}

// ── Toast ─────────────────────────────────────────────────────────────────
let _tt;
function showToast(msg, ms = 1800) {
  const el = document.getElementById('toast');
  el.textContent = msg; el.classList.add('show');
  clearTimeout(_tt);
  _tt = setTimeout(() => el.classList.remove('show'), ms);
}

// ── Hint ──────────────────────────────────────────────────────────────────
function revealHint() {
  if (state.hintUsed) return;
  state.hintUsed = true;
  save();
  document.getElementById('hint-cat-text').textContent = CATEGORY;
  document.getElementById('hint-panel').classList.add('show');
  const btn = document.getElementById('hint-btn');
  btn.textContent = 'Hint revealed';
  btn.disabled = true;
}

// ── Mobile sidebar toggle ──────────────────────────────────────────────────
function toggleSidebar() {
  document.getElementById('game-sidebar').classList.toggle('collapsed');
}

// ── Result panel ──────────────────────────────────────────────────────────
function showResult(won) {
  document.getElementById('rp-outcome').textContent = won
    ? `Solved in ${state.guesses.length} ${state.guesses.length === 1 ? 'guess' : 'guesses'}`
    : 'Better luck tomorrow';
  document.getElementById('rp-word').textContent    = ANSWER.join('');
  document.getElementById('rp-meaning').textContent = `${MEANING} — ${WORD_ROMAJI}`;
  document.getElementById('stat-played').textContent = state.played;
  document.getElementById('stat-streak').textContent = state.streak;
  document.getElementById('stat-best').textContent   = state.best;
  const jst  = new Date(new Date().toLocaleString('en-US', { timeZone: 'Asia/Tokyo' }));
  const next  = new Date(jst); next.setDate(next.getDate() + 1); next.setHours(0,0,0,0);
  const diff  = next - jst;
  const hh    = String(Math.floor(diff / 3600000)).padStart(2,'0');
  const mm    = String(Math.floor((diff % 3600000) / 60000)).padStart(2,'0');
  document.getElementById('rp-next').textContent = `Next word in ${hh}h ${mm}m`;
  document.getElementById('result-panel').classList.add('show');
}

// ── Share ─────────────────────────────────────────────────────────────────
function shareResult() {
  const em = { correct:'🟩', present:'🟨', absent:'⬜' };
  const grid = state.grades.map(r => r.map(s => em[s]).join('')).join('\n');
  const won  = state.status === 'won';
  const text = `KANADLE — Day ${DAY}\n${won ? state.guesses.length : 'X'}/6\n\n${grid}\n\njapaneseunlocked.com/games/kanadle/`;
  navigator.clipboard.writeText(text)
    .then(()  => showToast('Copied to clipboard!'))
    .catch(() => showToast('Copy failed — try manually'));
}

// ── Grid builder ──────────────────────────────────────────────────────────
function buildGrid() {
  const grid = document.getElementById('grid');
  for (let r = 0; r < 6; r++) {
    const row = document.createElement('div');
    row.className = 'grid-row';
    for (let c = 0; c < 5; c++) {
      const tile = document.createElement('div');
      tile.className = 'tile';
      tile.id = `t-${r}-${c}`;
      row.appendChild(tile);
    }
    grid.appendChild(row);
  }
}

// ── Restore ───────────────────────────────────────────────────────────────
function restore() {
  state.guesses.forEach((guess, ri) => {
    const result = state.grades[ri];
    guess.forEach((k, ci) => {
      const t = document.getElementById(`t-${ri}-${ci}`);
      if (t) { t.textContent = k; t.className = `tile ${result[ci]}`; }
    });
    updateKeys(guess, result);
  });
  refreshKb();
  if (state.hintUsed) {
    document.getElementById('hint-cat-text').textContent = CATEGORY;
    document.getElementById('hint-panel').classList.add('show');
    const btn = document.getElementById('hint-btn');
    btn.textContent = 'Hint revealed';
    btn.disabled = true;
  }
}

// ── Header ────────────────────────────────────────────────────────────────
function updateHeader() {
  document.getElementById('game-day').textContent = `Day ${DAY}`;
  const s = state.streak || 0;
  const badge = document.getElementById('streak-badge');
  badge.textContent = `🔥 ${s} streak`;
  if (s > 0) badge.classList.add('on');
}

// ── Physical keyboard ─────────────────────────────────────────────────────
document.addEventListener('keydown', e => {
  if (e.ctrlKey || e.metaKey || e.altKey) return;
  if (e.key === 'Enter')          submit();
  else if (e.key === 'Backspace') del();
  else                            processRomaji(e.key);
});

// ── On desktop, sidebar starts open ───────────────────────────────────────
if (window.innerWidth >= 621) {
  document.getElementById('game-sidebar').classList.remove('collapsed');
}

// ── Init ──────────────────────────────────────────────────────────────────
buildGrid();
buildKb();
updateHeader();
restore();
if (state.status !== 'playing') setTimeout(() => showResult(state.status === 'won'), 200);
</script>
