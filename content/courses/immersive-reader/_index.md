---
title: "Immersive Reader — Japanese Unlocked"
description: "Read real Japanese — news, food reviews, culture stories. Hover over kanji to see meanings, then write a summary in English and see how much you understood."
date: 2025-01-01
showtoc: false
---

<div class="ir-wrap">

<p class="ir-intro">Real Japanese paragraphs — news, food, culture, sports. Hover (or tap) any kanji to see its meaning. Then write what the article was about in English and check your understanding.</p>

<div class="ir-cats" id="ir-cats"></div>

<div class="ir-loading" id="ir-loading">Loading articles…</div>

<div class="ir-card" id="ir-card" style="display:none">
  <div class="ir-meta" id="ir-meta"></div>
  <h2 class="ir-title" id="ir-title"></h2>
  <div class="ir-text" id="ir-text"></div>

  <div class="ir-task">
    <div class="ir-task-label">📝 What was this article about? Write a summary in English.</div>
    <textarea class="ir-summary" id="ir-summary" rows="4" placeholder="In this article, …"></textarea>
    <button class="ir-submit" id="ir-submit">Check my summary →</button>
  </div>
</div>

<div class="ir-results" id="ir-results" style="display:none">
  <div class="ir-score-header" id="ir-score-header"></div>
  <div class="ir-keywords" id="ir-keywords"></div>
  <div class="ir-model-answer" id="ir-model-answer"></div>
  <div class="ir-actions">
    <button class="ir-btn-secondary" id="ir-retry">↩ Try Again</button>
    <button class="ir-btn-primary" id="ir-next-btn">Next Article →</button>
  </div>
</div>

<div class="ir-dots" id="ir-dots"></div>

</div>

<div class="ir-tip" id="ir-tip" style="display:none"></div>

<script>
(function(){

/* ── Kanji dictionary ──────────────────────────────────────────── */
var KD = {
'一':'one','二':'two','三':'three','四':'four','五':'five',
'六':'six','七':'seven','八':'eight','九':'nine','十':'ten',
'百':'hundred','千':'thousand','万':'ten thousand','億':'100 million','兆':'trillion',
'円':'yen','度':'degree / time','回':'times / turn','番':'number / turn',
'号':'number / issue','名':'name / famous','点':'point','位':'rank','枚':'flat things (counter)',
'台':'machines (counter)','個':'items (counter)',
'日':'day / sun','月':'month / moon','年':'year','時':'hour / time',
'分':'minute / part','秒':'second','週':'week',
'朝':'morning','昼':'noon / daytime','夕':'evening','夜':'night',
'今':'now / this','昨':'yesterday / previous','明':'bright / next','去':'past / leave',
'毎':'every / each','春':'spring','夏':'summer','秋':'autumn','冬':'winter',
'上':'above / up','下':'below / down','中':'middle / inside','外':'outside',
'内':'inside / within','前':'before / front','後':'after / back',
'左':'left','右':'right','東':'east','西':'west','南':'south','北':'north',
'近':'near / close','遠':'far','間':'interval / between',
'大':'big / large','小':'small','長':'long / leader','短':'short',
'高':'high / expensive','低':'low','安':'cheap / peaceful','多':'many / much',
'少':'few / little','全':'all / whole','半':'half','新':'new','古':'old',
'若':'young','強':'strong','弱':'weak','重':'heavy / important',
'軽':'light / easy','広':'wide / broad','狭':'narrow','深':'deep',
'浅':'shallow','速':'fast','遅':'slow / late','早':'early',
'明':'bright / clear','暗':'dark','良':'good','悪':'bad','正':'correct',
'同':'same','別':'different / special','各':'each / respective',
'山':'mountain','川':'river','海':'sea / ocean','空':'sky / empty',
'天':'sky / heaven','地':'ground / earth','島':'island','野':'field / plain',
'森':'forest','林':'woods','花':'flower','草':'grass','木':'tree',
'石':'stone / rock','水':'water','火':'fire','風':'wind','雨':'rain',
'雪':'snow','雲':'cloud','波':'wave','晴':'clear weather',
'暑':'hot (weather)','寒':'cold','暖':'warm','涼':'cool',
'人':'person / people','男':'man / male','女':'woman / female','子':'child',
'親':'parent','父':'father','母':'mother','兄':'older brother',
'弟':'younger brother','姉':'older sister','妹':'younger sister',
'友':'friend','者':'person (suffix)','民':'people / nation',
'方':'direction / person','生':'life / birth / student',
'国':'country / nation','都':'capital city','道':'road / way',
'府':'urban prefecture','県':'prefecture','市':'city','町':'town',
'村':'village','区':'ward / district','域':'region / area',
'場':'place / occasion','所':'place','家':'house / family','店':'shop',
'校':'school','館':'building / hall','院':'institution','室':'room',
'港':'port / harbour','橋':'bridge','駅':'station','路':'road / path',
'線':'line','列':'row / line',
'行':'go','帰':'return home','出':'exit / leave','入':'enter',
'見':'see / look','聞':'hear / listen','言':'say','話':'talk / story',
'書':'write','読':'read','教':'teach','学':'study / learning','知':'know',
'思':'think','感':'feel / sense','使':'use','作':'make / create',
'食':'eat / food','飲':'drink','買':'buy','売':'sell','取':'take / get',
'受':'receive','持':'hold / have','開':'open','閉':'close',
'起':'rise / occur','始':'begin / start','終':'end / finish',
'続':'continue','決':'decide','考':'think / consider',
'調':'investigate / adjust','働':'work / labour','動':'move',
'走':'run','歩':'walk','乗':'ride / get on','降':'get off / descend',
'飛':'fly','増':'increase','減':'decrease','変':'change',
'発':'emit / depart','集':'gather / collect','合':'fit / meet',
'立':'stand','待':'wait','止':'stop','置':'place / put',
'助':'help / save','守':'protect','支':'support / branch',
'求':'seek / request','願':'wish / request','困':'trouble',
'失':'lose / miss','選':'select / choose','競':'compete',
'勝':'win','負':'lose','優':'superior / gentle',
'体':'body / form','心':'heart / mind','頭':'head','手':'hand',
'足':'foot / leg','目':'eye','耳':'ear','口':'mouth','鼻':'nose',
'顔':'face','血':'blood','骨':'bone','皮':'skin',
'病':'illness / disease','痛':'pain / hurt','熱':'heat / fever',
'薬':'medicine / drug','医':'medicine / doctor','師':'teacher / master',
'看':'look after','護':'protect (nurse)','患':'suffer illness',
'健':'healthy','康':'ease / health','療':'treatment / cure',
'死':'die / death','息':'breath / son',
'仕':'serve / work','事':'matter / thing','業':'work / industry',
'職':'occupation / post','会':'meeting / society','社':'company / shrine',
'商':'commerce / trade','農':'agriculture','工':'craft / industrial',
'産':'produce / birth','品':'item / quality','物':'thing / object',
'料':'fee / material','費':'expense / cost','税':'tax',
'収':'income / harvest','予':'advance / prepare','算':'calculate',
'銀':'silver / bank','保':'protect / maintain','険':'risk',
'証':'proof / certificate','価':'price / value','格':'rank / status',
'経':'manage / pass through','済':'finish / help','輸':'transport',
'貿':'trade (foreign)','株':'stock / stump',
'政':'government / politics','法':'law / method','権':'right / authority',
'律':'rule / law','挙':'raise / hold','投':'throw / vote',
'議':'discuss','条':'article / clause','約':'promise / approx.',
'協':'cooperate','定':'decide / set','交':'exchange / mix',
'軍':'military / army','防':'defend / prevent','危':'danger / risky',
'難':'difficult / disaster','救':'rescue / save','避':'avoid / escape',
'警':'warn / police','報':'report / inform','震':'shake',
'台':'typhoon (台風)','洪':'flood','害':'harm / damage','故':'reason / cause',
'科':'subject / department','研':'research','究':'investigate',
'技':'skill / technique','術':'art / technique','文':'sentence / culture',
'化':'change / culture','芸':'art / performance','音':'sound / music',
'楽':'music / comfortable','映':'reflect / project','画':'picture / film',
'劇':'drama / theatre','演':'perform','語':'language / word','習':'practice',
'情':'feeling / information','通':'pass through / traffic',
'信':'trust / message','電':'electricity','機':'machine / chance',
'自':'self / natural','数':'number / count','量':'amount / volume',
'系':'system / lineage',
'記':'record / write','録':'record / list','史':'history',
'代':'era / generation','初':'first / beginning','最':'most / extreme',
'実':'real / practice','公':'public / official','私':'private / I',
'共':'together / both','相':'mutual / minister','対':'against / facing',
'特':'special','主':'main / master','活':'active / lively',
'現':'current / appear','当':'this / hit','旧':'old / former',
'以':'by means of','及':'reach / and','並':'line up / average',
'他':'other / another','本':'origin / book / real','元':'origin / former',
'先':'ahead / tip / previous','次':'next / following','再':'again / re-',
'末':'end / tip','的':'~ic / ~al (suffix)','率':'rate / ratio',
'便':'convenient / mail','利':'benefit / use','不':'not / un-',
'有':'exist / have','無':'nothing / without','可':'possible',
'必':'necessary','要':'important / need','確':'certain / confirm',
'然':'natural / so','際':'occasion / edge','的':'target / suffix -ic',
'局':'bureau / situation','部':'section / part','課':'section / lesson',
'会':'assembly','長':'chief / leader','員':'member / staff',
'者':'person','的':'suffix (-ic, -al)','性':'nature / sex / -ness',
'力':'power / strength','心':'mind / heart','身':'body / oneself',
'意':'meaning / intention','気':'spirit / air / feeling',
'言':'word / say','語':'language','文':'writing / sentence',
};

/* ── State ────────────────────────────────────────────────────── */
var allArticles  = [];
var filtered     = [];
var currentIdx   = 0;
var currentCat   = 'all';
var visited      = {};
var tipTimeout   = null;

/* ── Utility ──────────────────────────────────────────────────── */
function esc(str) {
  return String(str)
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}

function processJapanese(text) {
  /* Wrap ALL kanji — known ones show meaning, unknown ones link to Jisho */
  var out = '';
  for (var i = 0; i < text.length; i++) {
    var c    = text[i];
    var code = c.charCodeAt(0);
    var isKanji = (code >= 0x4E00 && code <= 0x9FAF) ||
                  (code >= 0x3400 && code <= 0x4DBF);
    if (isKanji) {
      var meaning = KD[c] || '';
      var cls = meaning ? 'ir-kanji' : 'ir-kanji ir-kanji--unknown';
      out += '<span class="' + cls + '" data-m="' + esc(meaning) + '" data-c="' + esc(c) + '">' + esc(c) + '</span>';
    } else if (c === '\n') {
      out += '<br>';
    } else {
      out += esc(c);
    }
  }
  return out;
}

/* ── Tooltip ──────────────────────────────────────────────────── */
var tip = null;
function getTip() { return tip || (tip = document.getElementById('ir-tip')); }

function showTip(meaning, x, y) {
  var t = getTip();
  t.textContent = meaning;
  t.style.display = 'block';
  moveTip(x, y);
}

function moveTip(x, y) {
  var t   = getTip();
  var tx  = x + 14;
  var ty  = y - 38;
  if (tx + 220 > window.innerWidth)  tx = x - 224;
  if (ty < 8)                         ty = y + 18;
  t.style.left = tx + 'px';
  t.style.top  = ty + 'px';
}

function hideTip() {
  var t = getTip();
  if (t) t.style.display = 'none';
}

/* ── Grading ──────────────────────────────────────────────────── */
function gradeKeywords(userText, keywords) {
  var lower   = userText.toLowerCase();
  var matched = [];
  var missed  = [];
  for (var i = 0; i < keywords.length; i++) {
    var kw = keywords[i].toLowerCase();
    // Accept partial match (e.g. "tourist" matches "tourists")
    if (lower.indexOf(kw) >= 0 || kw.indexOf(lower) >= 0) {
      matched.push(keywords[i]);
    } else {
      // Check if any 5+ char substring of kw appears
      var found = false;
      if (kw.length >= 5) {
        for (var j = 0; j <= kw.length - 4; j++) {
          if (lower.indexOf(kw.slice(j, j + 4)) >= 0) { found = true; break; }
        }
      }
      if (found) matched.push(keywords[i]);
      else       missed.push(keywords[i]);
    }
  }
  return { matched: matched, missed: missed, score: Math.round(matched.length / keywords.length * 100) };
}

function verdict(score) {
  if (score >= 80) return '🎉 Excellent! You captured the key details very well.';
  if (score >= 60) return '👍 Good effort — you got the main idea.';
  if (score >= 40) return '💪 You got some key points — check the model answer for what you missed.';
  if (score >= 20) return '📖 A good attempt — re-read the article and compare with the model answer.';
  return '🔁 Have another read — focus on the nouns and numbers.';
}

/* ── Build article card ───────────────────────────────────────── */
function catLabel(cat) {
  var m = {culture:'🎋 Culture',food:'🍜 Food',technology:'💻 Technology',
            sports:'⚽ Sports',entertainment:'🎬 Entertainment',news:'📰 News'};
  return m[cat] || cat;
}

function loadArticle(idx) {
  var art = filtered[idx];
  currentIdx = idx;

  document.getElementById('ir-loading').style.display = 'none';
  document.getElementById('ir-results').style.display = 'none';

  var card = document.getElementById('ir-card');
  card.style.display = 'block';

  document.getElementById('ir-meta').innerHTML =
    '<span class="ir-source">' + esc(art.source) + '</span>' +
    '<span class="ir-date">' + esc(art.date) + '</span>' +
    '<span class="ir-cat-badge">' + catLabel(art.category) + '</span>';

  document.getElementById('ir-title').innerHTML = processJapanese(art.title);
  document.getElementById('ir-text').innerHTML  = processJapanese(art.japanese);

  var ta = document.getElementById('ir-summary');
  ta.value = '';
  ta.disabled = false;
  document.getElementById('ir-submit').disabled = false;
  document.getElementById('ir-submit').textContent = 'Check my summary →';

  hideTip();
  attachKanjiEvents();
  updateDots();
}

function attachKanjiEvents() {
  var spans = document.querySelectorAll('.ir-kanji');
  spans.forEach(function(span) {
    span.addEventListener('mouseover', function(e) {
      var m = this.dataset.m;
      showTip(m || ('🔍 ' + this.dataset.c + ' — tap to look up on Jisho'), e.clientX, e.clientY);
    });
    span.addEventListener('mousemove', function(e) {
      moveTip(e.clientX, e.clientY);
    });
    span.addEventListener('mouseout', function() {
      hideTip();
    });
    // Click unknown kanji → open Jisho in new tab
    span.addEventListener('click', function() {
      if (!this.dataset.m) {
        window.open('https://jisho.org/search/' + encodeURIComponent(this.dataset.c), '_blank');
      }
    });
    // Touch support
    span.addEventListener('touchstart', function(e) {
      e.preventDefault();
      var active = document.querySelector('.ir-kanji--active');
      if (active && active !== this) active.classList.remove('ir-kanji--active');
      if (active === this) { hideTip(); active.classList.remove('ir-kanji--active'); return; }
      this.classList.add('ir-kanji--active');
      var r = this.getBoundingClientRect();
      var m = this.dataset.m;
      showTip(m || ('🔍 ' + this.dataset.c + ' — tap again to look up on Jisho'), r.left + r.width / 2, r.top);
    }, {passive: false});
    // Double-tap unknown kanji on touch → open Jisho
    span.addEventListener('dblclick', function() {
      if (!this.dataset.m) {
        window.open('https://jisho.org/search/' + encodeURIComponent(this.dataset.c), '_blank');
      }
    });
  });
  document.addEventListener('touchstart', function(e) {
    if (!e.target.classList.contains('ir-kanji')) {
      var active = document.querySelector('.ir-kanji--active');
      if (active) { active.classList.remove('ir-kanji--active'); hideTip(); }
    }
  });
}

/* ── Submit ───────────────────────────────────────────────────── */
function submitSummary() {
  var art     = filtered[currentIdx];
  var userTxt = document.getElementById('ir-summary').value.trim();
  if (!userTxt) {
    document.getElementById('ir-summary').placeholder = 'Write something — even a rough guess!';
    document.getElementById('ir-summary').focus();
    return;
  }

  document.getElementById('ir-submit').disabled = true;
  document.getElementById('ir-summary').disabled = true;

  var result  = gradeKeywords(userTxt, art.keywords);
  var isLast  = currentIdx >= filtered.length - 1;

  var scoreHtml =
    '<div class="ir-score-num">' + result.matched.length + '<span>/' + art.keywords.length + '</span></div>' +
    '<div class="ir-score-detail">' +
      '<div class="ir-score-pct">' + result.score + '% of key concepts</div>' +
      '<div class="ir-score-verdict">' + verdict(result.score) + '</div>' +
    '</div>';

  var kwHtml = result.matched.map(function(kw) {
    return '<span class="ir-kw ir-kw--hit">' + esc(kw) + ' ✓</span>';
  }).join('') + result.missed.map(function(kw) {
    return '<span class="ir-kw ir-kw--miss">' + esc(kw) + '</span>';
  }).join('');

  var modelHtml =
    '<div class="ir-model-label">📖 Model answer</div>' +
    '<div class="ir-model-text">' + esc(art.english_model) + '</div>';

  document.getElementById('ir-score-header').innerHTML = scoreHtml;
  document.getElementById('ir-keywords').innerHTML     = kwHtml;
  document.getElementById('ir-model-answer').innerHTML = modelHtml;
  document.getElementById('ir-next-btn').textContent   = isLast ? '🔁 Start Over' : 'Next Article →';
  document.getElementById('ir-results').style.display  = 'block';

  visited[currentIdx] = true;
  updateDots();

  document.getElementById('ir-results').scrollIntoView({behavior:'smooth', block:'nearest'});
}

/* ── Navigation ───────────────────────────────────────────────── */
document.addEventListener('click', function(e) {
  var id = e.target.id;
  if (id === 'ir-submit') { submitSummary(); return; }
  if (id === 'ir-retry') {
    document.getElementById('ir-results').style.display = 'none';
    var ta = document.getElementById('ir-summary');
    ta.value = ''; ta.disabled = false;
    document.getElementById('ir-submit').disabled = false;
    document.getElementById('ir-submit').textContent = 'Check my summary →';
    return;
  }
  if (id === 'ir-next-btn') {
    var next = (currentIdx + 1) % filtered.length;
    loadArticle(next);
    document.getElementById('ir-card').scrollIntoView({behavior:'smooth', block:'start'});
    return;
  }
});

/* ── Category tabs ────────────────────────────────────────────── */
function getCats() {
  var cats = ['all'];
  allArticles.forEach(function(a) {
    if (cats.indexOf(a.category) === -1) cats.push(a.category);
  });
  return cats;
}

function buildCats() {
  var el   = document.getElementById('ir-cats');
  if (!el) return;
  var cats = getCats();
  var labels = {all:'⭐ All', culture:'🎋 Culture', food:'🍜 Food',
                technology:'💻 Technology', sports:'⚽ Sports',
                entertainment:'🎬 Entertainment', news:'📰 News'};
  el.innerHTML = cats.map(function(c) {
    return '<button class="ir-cat-btn' + (c === currentCat ? ' active' : '') +
           '" data-cat="' + c + '">' + (labels[c] || c) + '</button>';
  }).join('');
  el.querySelectorAll('.ir-cat-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      currentCat = this.getAttribute('data-cat');
      visited    = {};
      filtered   = currentCat === 'all' ? allArticles :
                   allArticles.filter(function(a){ return a.category === currentCat; });
      currentIdx = 0;
      buildCats();
      buildDots();
      loadArticle(0);
    });
  });
}

/* ── Dots ─────────────────────────────────────────────────────── */
function buildDots() {
  var el = document.getElementById('ir-dots');
  if (!el) return;
  el.innerHTML = filtered.map(function(a, i) {
    var cls = 'ir-dot' +
      (i === currentIdx ? ' current' : '') +
      (visited[i]       ? ' visited' : '');
    return '<div class="' + cls + '" data-idx="' + i + '" title="' + esc(a.title) + '"></div>';
  }).join('');
  el.querySelectorAll('.ir-dot').forEach(function(dot) {
    dot.addEventListener('click', function() {
      loadArticle(parseInt(this.getAttribute('data-idx'), 10));
      document.getElementById('ir-card').scrollIntoView({behavior:'smooth', block:'start'});
    });
  });
}

function updateDots() {
  var el = document.getElementById('ir-dots');
  if (!el) return;
  el.querySelectorAll('.ir-dot').forEach(function(dot, i) {
    dot.className = 'ir-dot' +
      (i === currentIdx ? ' current' : '') +
      (visited[i]       ? ' visited' : '');
  });
}

/* ── Boot ─────────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', function() {
  fetch('/data/immersive-articles.json')
    .then(function(r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function(data) {
      allArticles = data;
      filtered    = data;
      buildCats();
      buildDots();
      loadArticle(0);
    })
    .catch(function() {
      document.getElementById('ir-loading').textContent =
        'Could not load articles — please refresh the page.';
    });
});

})();
</script>
