---
title: "Sentence Forge — Japanese Unlocked"
description: "Build Japanese sentences from scratch. You get a grammar pattern or vocabulary word, vocabulary chips to drag or click in, and a mic for speech input. We grade your attempt and show model answers."
date: 2025-01-01
showtoc: false
---

<div class="sf-wrap">

<p class="sf-intro">You get a grammar point or vocabulary word — make a sentence. Use the chips, type freely, or speak. We grade your attempt and show natural model answers.</p>

<div class="sf-cats" id="sf-cats"></div>

<div class="sf-progress-bar"><div class="sf-progress-fill" id="sf-progress-fill"></div></div>

<div class="sf-card" id="sf-card"></div>

<div class="sf-dots" id="sf-dots"></div>

</div>

<script>
(function(){

/* ── Prompts ─────────────────────────────────────────────────── */
var prompts = [
  /* ── Grammar patterns ── */
  {id:'g01',type:'grammar',level:'N5',
   focus:'〜ています',
   eng:'Describe something happening right now, or an ongoing state.',
   hint:'verb て-form + います',
   example:'雨が降っています。— It is raining.',
   pat:'ています|ていません|ている|でいます',
   chips:[
     {jp:'食べています',en:'eating',rom:'tabeteimasu'},
     {jp:'飲んでいます',en:'drinking',rom:'nondeimasu'},
     {jp:'今',en:'now',rom:'ima'},
     {jp:'毎日',en:'every day',rom:'mainichi'},
     {jp:'住んでいます',en:'living (in)',rom:'sundeimasu'},
     {jp:'働いています',en:'working',rom:'hataraiteimasu'},
   ],
   models:[
     {jp:'今コーヒーを飲んでいます。',en:'I am drinking coffee now.'},
     {jp:'毎日日本語を勉強しています。',en:'I study Japanese every day.'},
     {jp:'東京に住んでいます。',en:'I live in Tokyo.'},
   ]},
  {id:'g02',type:'grammar',level:'N5',
   focus:'〜たいです',
   eng:'Express what you want to do.',
   hint:'verb stem + たいです',
   example:'日本へ行きたいです。— I want to go to Japan.',
   pat:'たいです|たい|たくない',
   chips:[
     {jp:'食べたい',en:'want to eat',rom:'tabetai'},
     {jp:'見たい',en:'want to see',rom:'mitai'},
     {jp:'日本',en:'Japan',rom:'nihon'},
     {jp:'旅行',en:'travel',rom:'ryokou'},
     {jp:'学びたい',en:'want to learn',rom:'manahitai'},
     {jp:'話したい',en:'want to speak',rom:'hanashitai'},
   ],
   models:[
     {jp:'日本に旅行したいです。',en:'I want to travel to Japan.'},
     {jp:'もっと日本語を話したいです。',en:'I want to speak more Japanese.'},
     {jp:'お寿司を食べたいです。',en:'I want to eat sushi.'},
   ]},
  {id:'g03',type:'grammar',level:'N5',
   focus:'〜てください',
   eng:'Make a polite request.',
   hint:'verb て-form + ください',
   example:'ここに名前を書いてください。— Please write your name here.',
   pat:'てください|でください',
   chips:[
     {jp:'待ってください',en:'please wait',rom:'mattekudasai'},
     {jp:'教えてください',en:'please tell me',rom:'oshietekudasai'},
     {jp:'ゆっくり',en:'slowly',rom:'yukkuri'},
     {jp:'話してください',en:'please speak',rom:'hanashitekudasai'},
     {jp:'見てください',en:'please look',rom:'mitekudasai'},
     {jp:'もう一度',en:'one more time',rom:'mouichido'},
   ],
   models:[
     {jp:'ゆっくり話してください。',en:'Please speak slowly.'},
     {jp:'もう一度教えてください。',en:'Please tell me one more time.'},
     {jp:'ここで待ってください。',en:'Please wait here.'},
   ]},
  {id:'g04',type:'grammar',level:'N5',
   focus:'〜ましょう',
   eng:'Suggest doing something together — "let\'s …"',
   hint:'verb ます-stem + ましょう',
   example:'一緒に行きましょう。— Let\'s go together.',
   pat:'ましょう|ましょうか',
   chips:[
     {jp:'行きましょう',en:"let's go",rom:'ikimashou'},
     {jp:'食べましょう',en:"let's eat",rom:'tabemashou'},
     {jp:'一緒に',en:'together',rom:'isshoni'},
     {jp:'始めましょう',en:"let's start",rom:'hajimemashou'},
     {jp:'休みましょう',en:"let's rest",rom:'yasumimashou'},
     {jp:'頑張りましょう',en:"let's do our best",rom:'ganbarimashou'},
   ],
   models:[
     {jp:'一緒に頑張りましょう！',en:"Let's do our best together!"},
     {jp:'お昼を食べましょう。',en:"Let's eat lunch."},
     {jp:'少し休みましょうか。',en:"Shall we rest a bit?"},
   ]},
  {id:'g05',type:'grammar',level:'N4',
   focus:'〜ことができます',
   eng:'Say what you can or are able to do.',
   hint:'verb dictionary form + ことができます',
   example:'私は日本語を話すことができます。— I can speak Japanese.',
   pat:'ことができ|ことができる',
   chips:[
     {jp:'話すことができます',en:'can speak',rom:'hanasukoto'},
     {jp:'泳ぐことができます',en:'can swim',rom:'oyogukoto'},
     {jp:'料理',en:'cooking',rom:'ryouri'},
     {jp:'運転',en:'driving',rom:'unten'},
     {jp:'少し',en:'a little',rom:'sukoshi'},
     {jp:'日本語',en:'Japanese',rom:'nihongo'},
   ],
   models:[
     {jp:'少し日本語を話すことができます。',en:'I can speak a little Japanese.'},
     {jp:'自転車で行くことができます。',en:'I can go by bicycle.'},
     {jp:'料理することができません。',en:"I can't cook."},
   ]},
  {id:'g06',type:'grammar',level:'N4',
   focus:'〜てもいいですか',
   eng:'Ask permission to do something.',
   hint:'verb て-form + もいいですか',
   example:'ここに座ってもいいですか。— May I sit here?',
   pat:'てもいいですか|でもいいですか|ていいですか',
   chips:[
     {jp:'見てもいいですか',en:'may I look?',rom:'mitemoyii'},
     {jp:'聞いてもいいですか',en:'may I ask?',rom:'kiitemoyii'},
     {jp:'写真',en:'photo',rom:'shashin'},
     {jp:'使ってもいいですか',en:'may I use this?',rom:'tsukattemoyii'},
     {jp:'帰ってもいいですか',en:'may I go home?',rom:'kaettemoyii'},
     {jp:'ちょっと',en:'a moment / just',rom:'chotto'},
   ],
   models:[
     {jp:'写真を撮ってもいいですか。',en:'May I take a photo?'},
     {jp:'ちょっと聞いてもいいですか。',en:'May I ask you something?'},
     {jp:'窓を開けてもいいですか。',en:'May I open the window?'},
   ]},
  {id:'g07',type:'grammar',level:'N4',
   focus:'〜なければなりません',
   eng:'Express obligation — something must be done.',
   hint:'verb ない-form + なければなりません',
   example:'明日早く起きなければなりません。— I must wake up early tomorrow.',
   pat:'なければなりません|なければならない|なきゃ|ないといけません',
   chips:[
     {jp:'勉強しなければなりません',en:'must study',rom:'benkyouna'},
     {jp:'明日',en:'tomorrow',rom:'ashita'},
     {jp:'早く',en:'early',rom:'hayaku'},
     {jp:'行かなければなりません',en:'must go',rom:'ikana'},
     {jp:'提出',en:'submission',rom:'teishutsu'},
     {jp:'練習',en:'practice',rom:'renshuu'},
   ],
   models:[
     {jp:'明日早く起きなければなりません。',en:'I must wake up early tomorrow.'},
     {jp:'宿題を出さなければなりません。',en:'I must submit my homework.'},
     {jp:'もっと練習しなければなりません。',en:'I must practice more.'},
   ]},
  {id:'g08',type:'grammar',level:'N4',
   focus:'〜から',
   eng:'Give a reason — "because / since" (reason comes first).',
   hint:'[reason] から、[result]',
   example:'疲れたから、早く寝ます。— Because I\'m tired, I\'ll sleep early.',
   pat:'から[、。！　]|から$|から\n',
   chips:[
     {jp:'疲れた',en:'tired',rom:'tsukareta'},
     {jp:'から',en:'because',rom:'kara'},
     {jp:'寒い',en:'cold',rom:'samui'},
     {jp:'忙しい',en:'busy',rom:'isogashii'},
     {jp:'好きだ',en:'I like it',rom:'sukida'},
     {jp:'時間がない',en:'no time',rom:'jikangana'},
   ],
   models:[
     {jp:'疲れたから、今日は休みます。',en:"Because I'm tired, I'll rest today."},
     {jp:'寒いから、コートを着ます。',en:"Because it's cold, I'll wear a coat."},
     {jp:'日本語が好きだから、毎日勉強しています。',en:"Because I like Japanese, I study every day."},
   ]},
  {id:'g09',type:'grammar',level:'N4',
   focus:'〜ながら',
   eng:'Describe doing two things at the same time.',
   hint:'verb ます-stem + ながら + [main action]',
   example:'音楽を聴きながら勉強します。— I study while listening to music.',
   pat:'ながら',
   chips:[
     {jp:'聴きながら',en:'while listening',rom:'kikinagara'},
     {jp:'食べながら',en:'while eating',rom:'tabenagara'},
     {jp:'歩きながら',en:'while walking',rom:'arukinagara'},
     {jp:'音楽',en:'music',rom:'ongaku'},
     {jp:'電話',en:'phone call',rom:'denwa'},
     {jp:'テレビ',en:'TV',rom:'terebi'},
   ],
   models:[
     {jp:'音楽を聴きながら勉強します。',en:'I study while listening to music.'},
     {jp:'歩きながら電話をします。',en:'I make phone calls while walking.'},
     {jp:'テレビを見ながら食べます。',en:'I eat while watching TV.'},
   ]},
  {id:'g10',type:'grammar',level:'N4',
   focus:'〜てしまいました',
   eng:'Say something was done completely — often with regret.',
   hint:'verb て-form + しまいました',
   example:'財布を忘れてしまいました。— I accidentally forgot my wallet.',
   pat:'てしまいました|でしまいました|てしまった|ちゃった|じゃった',
   chips:[
     {jp:'忘れてしまいました',en:'accidentally forgot',rom:'wasurete'},
     {jp:'食べてしまいました',en:'ended up eating',rom:'tabete'},
     {jp:'財布',en:'wallet',rom:'saifu'},
     {jp:'全部',en:'all / everything',rom:'zenbu'},
     {jp:'遅刻してしまいました',en:'ended up late',rom:'chikoku'},
     {jp:'壊してしまいました',en:'ended up breaking',rom:'kowashite'},
   ],
   models:[
     {jp:'財布を家に忘れてしまいました。',en:'I accidentally left my wallet at home.'},
     {jp:'ケーキを全部食べてしまいました。',en:'I ended up eating all the cake.'},
     {jp:'遅刻してしまいました。',en:'I ended up being late.'},
   ]},

  /* ── Vocabulary / expressions ── */
  {id:'v01',type:'vocab',level:'N5',
   focus:'大丈夫',
   eng:'"Okay / fine / no problem / are you alright?" — one of the most useful words in Japanese.',
   hint:'Works as a question (大丈夫ですか？), reassurance, or polite refusal.',
   example:'大丈夫ですか？— Are you okay?',
   pat:'大丈夫',
   chips:[
     {jp:'大丈夫ですか',en:'are you okay?',rom:'daijoubu desuka'},
     {jp:'大丈夫です',en:"it's fine",rom:'daijoubu desu'},
     {jp:'全然',en:'not at all / totally',rom:'zenzen'},
     {jp:'心配しないで',en:"don't worry",rom:'shinpai shinaide'},
     {jp:'もう',en:'already',rom:'mou'},
     {jp:'ちょっと',en:'a little',rom:'chotto'},
   ],
   models:[
     {jp:'大丈夫ですか？転んだのを見ました。',en:'Are you okay? I saw you fall.'},
     {jp:'全然大丈夫です、心配しないでください。',en:"I'm totally fine, please don't worry."},
     {jp:'ちょっと疲れましたが、大丈夫です。',en:"I'm a bit tired but I'm okay."},
   ]},
  {id:'v02',type:'vocab',level:'N4',
   focus:'やっぱり',
   eng:'"As I expected / after all / just as I thought" — confirms a suspicion or re-states a preference.',
   hint:'Use when reality confirms what you suspected, or when you revert to your original preference.',
   example:'やっぱり日本語は面白いですね。— Japanese is interesting after all.',
   pat:'やっぱり|やはり',
   chips:[
     {jp:'やっぱり',en:'after all / as expected',rom:'yappari'},
     {jp:'思った通り',en:'just as I thought',rom:'omotta toori'},
     {jp:'面白い',en:'interesting',rom:'omoshiroi'},
     {jp:'難しい',en:'difficult',rom:'muzukashii'},
     {jp:'好きです',en:'I like it',rom:'suki desu'},
     {jp:'無理',en:'impossible',rom:'muri'},
   ],
   models:[
     {jp:'やっぱり日本語は難しいですね。',en:"Japanese is difficult after all, isn't it."},
     {jp:'やっぱり彼女が一番好きです。',en:'After all, I like her best.'},
     {jp:'試してみたけど、やっぱり無理でした。',en:'I tried it, but as I thought, it was impossible.'},
   ]},
  {id:'v03',type:'vocab',level:'N4',
   focus:'ちょうど',
   eng:'"Just / exactly / precisely" — the thing is perfectly right or happened at exactly the right moment.',
   hint:'Use for exact times, perfect fits, or things that happened right when you needed them.',
   example:'ちょうど5時です。— It\'s exactly 5 o\'clock.',
   pat:'ちょうど',
   chips:[
     {jp:'ちょうど',en:'exactly / just',rom:'choudo'},
     {jp:'今',en:'just now / now',rom:'ima'},
     {jp:'良かった',en:'how good / glad',rom:'yokatta'},
     {jp:'間に合いました',en:'made it in time',rom:'maniai mashita'},
     {jp:'同じ',en:'same',rom:'onaji'},
     {jp:'考えていました',en:'was thinking',rom:'kangaete imashita'},
   ],
   models:[
     {jp:'ちょうどあなたのことを考えていました！',en:'I was just thinking about you!'},
     {jp:'ちょうど間に合いました。',en:'I made it just in time.'},
     {jp:'ちょうど良い大きさです。',en:"It's just the right size."},
   ]},
  {id:'v04',type:'vocab',level:'N4',
   focus:'おかげで',
   eng:'"Thanks to / because of" — used for positive outcomes.',
   hint:'Attribute a good result to someone or something. Often: [person/thing]のおかげで。',
   example:'あなたのおかげで合格できました。— Thanks to you, I passed.',
   pat:'おかげで|おかげ',
   chips:[
     {jp:'おかげで',en:'thanks to',rom:'okage de'},
     {jp:'あなたの',en:'your',rom:'anata no'},
     {jp:'練習したおかげで',en:'thanks to practising',rom:'renshuu shita okage de'},
     {jp:'うまくできました',en:'was able to do well',rom:'umaku dekimashita'},
     {jp:'先生',en:'teacher',rom:'sensei'},
     {jp:'助かりました',en:'was a great help',rom:'tasukarimashita'},
   ],
   models:[
     {jp:'あなたのおかげで助かりました。',en:'Thanks to you, I was really helped.'},
     {jp:'練習したおかげで上手になりました。',en:'Thanks to practising, I got better.'},
     {jp:'先生のおかげで日本語が好きになりました。',en:"Thanks to my teacher, I've come to like Japanese."},
   ]},
  {id:'v05',type:'vocab',level:'N3',
   focus:'せっかく',
   eng:'"Since you went to the trouble / taking the effort" — used when effort shouldn\'t go to waste.',
   hint:'Often followed by のに (wasted effort) or から (so let\'s make the most of it).',
   example:'せっかく来たから、楽しみましょう。— Since we went to the trouble of coming, let\'s enjoy it.',
   pat:'せっかく',
   chips:[
     {jp:'せっかく',en:"since we're here / went to the trouble",rom:'sekkaku'},
     {jp:'来たから',en:'since (I/we) came',rom:'kita kara'},
     {jp:'楽しみましょう',en:"let's enjoy",rom:'tanoshimi mashou'},
     {jp:'機会',en:'opportunity',rom:'kikai'},
     {jp:'無駄にしたくない',en:"don't want to waste it",rom:'muda ni shitakunai'},
     {jp:'頑張りました',en:'tried hard',rom:'ganbari mashita'},
   ],
   models:[
     {jp:'せっかく来たから、全部見ていきましょう。',en:"Since we came all this way, let's see everything."},
     {jp:'せっかくの機会を無駄にしたくありません。',en:"I don't want to waste this rare opportunity."},
     {jp:'せっかく頑張ったのに、残念でした。',en:'I went to all that effort, so it was a shame.'},
   ]},
  {id:'v06',type:'vocab',level:'N3',
   focus:'我慢する',
   eng:'"To endure / to put up with / to hold back" — a very Japanese concept.',
   hint:'Used for enduring pain, temptation, discomfort, or waiting patiently.',
   example:'もう我慢できません。— I can\'t stand it anymore.',
   pat:'我慢',
   chips:[
     {jp:'我慢する',en:'endure / put up with',rom:'gaman suru'},
     {jp:'もう',en:'anymore / already',rom:'mou'},
     {jp:'できません',en:"can't",rom:'dekimasen'},
     {jp:'辛い',en:'tough / painful',rom:'tsurai'},
     {jp:'痛い',en:'it hurts',rom:'itai'},
     {jp:'もう少し',en:'a little more',rom:'mou sukoshi'},
   ],
   models:[
     {jp:'もう我慢できません！',en:"I can't stand it anymore!"},
     {jp:'痛いけど、我慢します。',en:"It hurts, but I'll endure it."},
     {jp:'もう少し我慢してください。',en:'Please bear with it a little longer.'},
   ]},
  {id:'v07',type:'vocab',level:'N3',
   focus:'懐かしい',
   eng:'"Nostalgic / brings back memories" — a warm feeling for something from the past.',
   hint:'Used for songs, places, food, or people that trigger fond old memories.',
   example:'この歌を聴くと懐かしい気持ちになります。— When I hear this song, I feel nostalgic.',
   pat:'懐かし',
   chips:[
     {jp:'懐かしい',en:'nostalgic',rom:'natsukashii'},
     {jp:'この曲',en:'this song',rom:'kono kyoku'},
     {jp:'昔',en:'old days / the past',rom:'mukashi'},
     {jp:'気持ち',en:'feeling',rom:'kimochi'},
     {jp:'思い出',en:'memories',rom:'omoide'},
     {jp:'よく来ました',en:'used to come (here) often',rom:'yoku kimashita'},
   ],
   models:[
     {jp:'懐かしい！昔よくここに来ました。',en:"So nostalgic! I used to come here often."},
     {jp:'この写真を見ると懐かしい気持ちになります。',en:'When I see this photo, I feel nostalgic.'},
     {jp:'この曲は懐かしくて、泣きそうになりました。',en:'This song was so nostalgic, I almost cried.'},
   ]},
  {id:'v08',type:'vocab',level:'N3',
   focus:'もったいない',
   eng:'"What a waste! / Too good to throw away" — lamenting waste or misuse of something valuable.',
   hint:'Food, opportunities, talent, nice things going unused — all もったいない。',
   example:'食べ物を捨てるのはもったいないです。— It\'s a waste to throw away food.',
   pat:'もったいない',
   chips:[
     {jp:'もったいない',en:"what a waste",rom:'mottainai'},
     {jp:'捨てるのは',en:'throwing away',rom:'suteru no wa'},
     {jp:'食べ物',en:'food',rom:'tabemono'},
     {jp:'この機会',en:'this chance',rom:'kono kikai'},
     {jp:'使わないのは',en:'not using it',rom:'tsukawanai no wa'},
     {jp:'本当に',en:'really / truly',rom:'hontou ni'},
   ],
   models:[
     {jp:'食べ物を捨てるのはもったいないです。',en:"It's a waste to throw away food."},
     {jp:'この機会を逃すのはもったいない！',en:"It would be such a waste to miss this chance!"},
     {jp:'こんなに良い服を捨てるのは本当にもったいないです。',en:"It's really a waste to throw away such nice clothes."},
   ]},
  {id:'v09',type:'vocab',level:'N4',
   focus:'気になる',
   eng:'"To be curious about / to bother you / to be on your mind" — used when you can\'t stop thinking about something.',
   hint:'Can be positive curiosity or a nagging concern. Often: [thing]が気になる。',
   example:'その映画が気になっています。— That movie has been on my mind.',
   pat:'気になる|気になって|気になり|気になっ',
   chips:[
     {jp:'気になる',en:"I'm curious about / on my mind",rom:'ki ni naru'},
     {jp:'ずっと',en:'this whole time / always',rom:'zutto'},
     {jp:'あの人',en:'that person',rom:'ano hito'},
     {jp:'この映画',en:'this film',rom:'kono eiga'},
     {jp:'どうしても',en:'no matter what',rom:'doushitemo'},
     {jp:'試験の結果',en:'exam results',rom:'shiken no kekka'},
   ],
   models:[
     {jp:'ずっとあの人のことが気になっています。',en:'That person has been on my mind the whole time.'},
     {jp:'この映画が気になって、早く見たいです。',en:"This film is on my mind and I want to see it soon."},
     {jp:'試験の結果がどうしても気になります。',en:'The exam results are really weighing on my mind.'},
   ]},
  {id:'v10',type:'vocab',level:'N3',
   focus:'そのまま',
   eng:'"As is / just like that / without changing" — the current state continues unchanged.',
   hint:'Use when something should stay as it is, or when an action is done without stopping.',
   example:'そのままでいいです。— It\'s fine as it is.',
   pat:'そのまま',
   chips:[
     {jp:'そのまま',en:'as is / just like that',rom:'sono mama'},
     {jp:'でいいです',en:'is fine / is okay',rom:'de ii desu'},
     {jp:'待っていてください',en:'please keep waiting',rom:'matte ite kudasai'},
     {jp:'続けてください',en:'please continue',rom:'tsuzukete kudasai'},
     {jp:'使ってください',en:'please use it',rom:'tsukatte kudasai'},
     {jp:'変えないで',en:"don't change it",rom:'kaenaide'},
   ],
   models:[
     {jp:'そのままでいいです、変えないでください。',en:"It's fine as is — please don't change it."},
     {jp:'そのまま待っていてください。',en:'Please stay just like that and wait.'},
     {jp:'このファイルはそのまま使ってください。',en:'Please use this file as is.'},
   ]},
];

/* ── State ─────────────────────────────────────────────────────── */
var filtered   = prompts.slice();
var currentIdx = 0;
var currentCat = 'all';
var visited    = {};
var isRecording = false;
var recognition = null;

/* ── Grading ────────────────────────────────────────────────────── */
function gradeResponse(userText, prompt) {
  var text = userText.trim();
  if (!text || text.length < 2) return {grade:'D',score:0,patternHit:false,chipsUsed:[]};

  var score = 0;

  // 1. Target pattern present? (50pts)
  var patternHit = new RegExp(prompt.pat).test(text);
  if (patternHit) score += 50;

  // 2. Vocabulary chips used (up to 30pts)
  var chipsUsed = prompt.chips.filter(function(c) {
    var stem = c.jp.replace(/ます$|です$|ました$|ません$/, '');
    return text.indexOf(c.jp) >= 0 || (stem.length > 1 && text.indexOf(stem) >= 0);
  });
  score += Math.min(30, chipsUsed.length * 15);

  // 3. Completeness (20pts)
  var cleaned = text.replace(/\s/g, '');
  if (cleaned.length >= 8) score += 12;
  else if (cleaned.length >= 3) score += 6;
  if (/[。！？]/.test(text) || /ます|です|ない|した|ている|いる/.test(text)) score += 8;

  var grade;
  if      (score >= 85) grade = 'S';
  else if (score >= 65) grade = 'A';
  else if (score >= 45) grade = 'B';
  else if (score >= 25) grade = 'C';
  else                  grade = 'D';

  return {grade:grade, score:score, patternHit:patternHit, chipsUsed:chipsUsed};
}

function gradeVerdict(result, prompt) {
  if (!result.patternHit) {
    return 'Try to include <strong>' + esc(prompt.focus) + '</strong> in your sentence.';
  }
  if (result.grade === 'S') return '🎉 Excellent — that sounds natural!';
  if (result.grade === 'A') return '👍 Great — the pattern is there and it makes sense.';
  if (result.grade === 'B') return '💪 Good attempt — check the model answers to refine it.';
  return '📖 You\'ve got the pattern — look at the models to see how to build it out.';
}

/* ── HTML helpers ───────────────────────────────────────────────── */
function esc(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
                  .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}

function typeLabel(prompt) {
  return prompt.type === 'grammar' ? '📐 Grammar' : '📖 Vocabulary';
}

function levelColor(lvl) {
  return {N5:'#44aa66',N4:'#4488cc',N3:'#cc8844',N2:'#aa44cc',N1:'#cc4444'}[lvl] || '#888';
}

/* ── Build card ─────────────────────────────────────────────────── */
function buildCard(prompt) {
  var chipsHtml = prompt.chips.map(function(c) {
    return '<button class="sf-chip" draggable="true" data-jp="' + esc(c.jp) + '" data-rom="' + esc(c.rom) + '">' +
      '<span class="sf-chip-jp">' + esc(c.jp) + '</span>' +
      '<span class="sf-chip-en">' + esc(c.en) + '</span>' +
    '</button>';
  }).join('');

  var micSupport = !!(window.SpeechRecognition || window.webkitSpeechRecognition);

  return '<div class="sf-prompt">' +
    '<div class="sf-type-row">' +
      '<span class="sf-type-label">' + typeLabel(prompt) + '</span>' +
      '<span class="sf-level-badge" style="background:' + levelColor(prompt.level) + '">' + esc(prompt.level) + '</span>' +
    '</div>' +
    '<div class="sf-focus">' + esc(prompt.focus) + '</div>' +
    '<div class="sf-instruction">' + esc(prompt.eng) + '</div>' +
    '<div class="sf-hint-row">' +
      '<span class="sf-pattern-badge">' + esc(prompt.hint) + '</span>' +
      '<button class="sf-example-btn" id="sf-ex-btn">See example ▾</button>' +
    '</div>' +
    '<div class="sf-example" id="sf-example" style="display:none">' + esc(prompt.example) + '</div>' +
  '</div>' +
  '<div class="sf-input-area">' +
    '<div class="sf-textarea-wrap">' +
      '<'+'textarea class="sf-input" id="sf-input" rows="3" placeholder="日本語で文章を書いてください…" autocomplete="off" autocorrect="off" spellcheck="false"><'+'\/textarea>' +
      (micSupport ? '<button class="sf-mic" id="sf-mic" title="Speech input (Japanese)">🎤</button>' : '') +
    '</div>' +
    '<div class="sf-chips-label">Vocabulary help — click or drag into the box:</div>' +
    '<div class="sf-chips" id="sf-chips">' + chipsHtml + '</div>' +
  '</div>' +
  '<div class="sf-grade-wrap" id="sf-grade-wrap"></div>' +
  '<div class="sf-card-actions">' +
    '<button class="sf-submit" id="sf-submit">Check →</button>' +
  '</div>' +
  '<div class="sf-models-wrap" id="sf-models-wrap" style="display:none"></div>' +
  '<div class="sf-nav-row" id="sf-nav-row" style="display:none">' +
    '<button class="sf-btn-secondary" id="sf-retry">↩ Try Again</button>' +
    '<button class="sf-btn-primary" id="sf-next-btn">Next →</button>' +
  '</div>';
}

/* ── Wire card events ───────────────────────────────────────────── */
function wireCard(prompt) {
  var ta = document.getElementById('sf-input');

  // Example toggle
  document.getElementById('sf-ex-btn').addEventListener('click', function() {
    var ex = document.getElementById('sf-example');
    var open = ex.style.display !== 'none';
    ex.style.display = open ? 'none' : 'block';
    this.textContent = open ? 'See example ▾' : 'Hide example ▴';
  });

  // Chips: click to insert
  document.querySelectorAll('.sf-chip').forEach(function(chip) {
    chip.addEventListener('click', function() {
      insertAtCursor(ta, this.dataset.jp);
    });
    // Drag
    chip.addEventListener('dragstart', function(e) {
      e.dataTransfer.setData('application/x-sf-chip', this.dataset.jp);
      e.dataTransfer.effectAllowed = 'copy';
    });
  });

  // Textarea: accept chip drops
  ta.addEventListener('dragover', function(e) {
    if (e.dataTransfer.types.indexOf('application/x-sf-chip') >= 0) {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'copy';
    }
  });
  ta.addEventListener('drop', function(e) {
    var text = e.dataTransfer.getData('application/x-sf-chip');
    if (text) {
      e.preventDefault();
      insertAtCursor(ta, text);
    }
  });

  // Submit
  document.getElementById('sf-submit').addEventListener('click', function() {
    submitAnswer(prompt);
  });

  // Retry
  document.getElementById('sf-retry').addEventListener('click', function() {
    loadPrompt(currentIdx);
  });

  // Next
  document.getElementById('sf-next-btn').addEventListener('click', function() {
    var next = (currentIdx + 1) % filtered.length;
    loadPrompt(next);
    document.getElementById('sf-card').scrollIntoView({behavior:'smooth', block:'start'});
  });

  // Speech input
  setupSpeech(ta);
}

function insertAtCursor(ta, text) {
  var start = ta.selectionStart;
  var end   = ta.selectionEnd;
  ta.value  = ta.value.slice(0, start) + text + ta.value.slice(end);
  ta.selectionStart = ta.selectionEnd = start + text.length;
  ta.focus();
}

/* ── Speech input ───────────────────────────────────────────────── */
function setupSpeech(ta) {
  var SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
  var micBtn    = document.getElementById('sf-mic');
  if (!SpeechRec || !micBtn) return;

  recognition = new SpeechRec();
  recognition.lang = 'ja-JP';
  recognition.continuous = false;
  recognition.interimResults = true;

  micBtn.addEventListener('click', function() {
    if (isRecording) {
      recognition.stop();
      return;
    }
    isRecording = true;
    micBtn.classList.add('sf-mic-active');
    micBtn.textContent = '⏹';
    try { recognition.start(); } catch(e) { resetMic(micBtn); }
  });

  recognition.onresult = function(e) {
    var t = '';
    for (var i = e.resultIndex; i < e.results.length; i++) {
      t += e.results[i][0].transcript;
    }
    ta.value = t;
  };
  recognition.onend   = function() { resetMic(micBtn); };
  recognition.onerror = function(e) {
    resetMic(micBtn);
    if (e.error !== 'aborted' && e.error !== 'no-speech') {
      var el = document.getElementById('sf-grade-wrap');
      if (el) el.innerHTML = '<div class="sf-mic-err">🎤 ' + esc(e.error) + ' — try typing instead.</div>';
    }
  };
}

function resetMic(btn) {
  isRecording = false;
  if (btn) { btn.classList.remove('sf-mic-active'); btn.textContent = '🎤'; }
}

/* ── Submit & grade ─────────────────────────────────────────────── */
function submitAnswer(prompt) {
  var ta   = document.getElementById('sf-input');
  var text = ta ? ta.value.trim() : '';

  if (!text) {
    ta.placeholder = 'Type something — even a short attempt!';
    ta.focus();
    return;
  }

  var result = gradeResponse(text, prompt);

  // Grade badge
  var gradeColors = {S:'#a78bfa',A:'#34d399',B:'#60a5fa',C:'#fb923c',D:'#f87171'};
  var gradeHtml =
    '<div class="sf-grade-result">' +
      '<div class="sf-grade-badge sf-grade-badge--' + result.grade + '">' + result.grade + '</div>' +
      '<div class="sf-grade-detail">' +
        '<div class="sf-grade-score">' + result.score + '/100</div>' +
        '<div class="sf-grade-verdict">' + gradeVerdict(result, prompt) + '</div>' +
        (result.chipsUsed.length ? '<div class="sf-grade-chips-used">Used: ' +
          result.chipsUsed.map(function(c){ return '<span class="sf-cu-tag">' + esc(c.jp) + '</span>'; }).join('') +
        '</div>' : '') +
      '</div>' +
    '</div>';

  document.getElementById('sf-grade-wrap').innerHTML = gradeHtml;

  // Model answers
  var modHtml = '<div class="sf-models-label">📖 Model answers</div>' +
    prompt.models.map(function(m) {
      return '<div class="sf-model-item">' +
        '<div class="sf-model-jp">' + esc(m.jp) + '</div>' +
        '<div class="sf-model-en">' + esc(m.en) + '</div>' +
      '</div>';
    }).join('');

  document.getElementById('sf-models-wrap').innerHTML = modHtml;
  document.getElementById('sf-models-wrap').style.display = 'block';

  var navRow = document.getElementById('sf-nav-row');
  navRow.style.display = 'flex';
  var isLast = currentIdx >= filtered.length - 1;
  document.getElementById('sf-next-btn').textContent = isLast ? '🔁 Start Over' : 'Next →';

  document.getElementById('sf-submit').disabled = true;
  if (ta) ta.disabled = true;

  visited[currentIdx] = result.grade;
  updateDots();
  updateProgress();

  document.getElementById('sf-grade-wrap').scrollIntoView({behavior:'smooth', block:'nearest'});
}

/* ── Load prompt ────────────────────────────────────────────────── */
function loadPrompt(idx) {
  if (recognition && isRecording) { try { recognition.stop(); } catch(e){} }
  recognition = null;
  isRecording = false;

  if (idx >= filtered.length) idx = 0;
  currentIdx = idx;

  var prompt = filtered[idx];
  var card = document.getElementById('sf-card');
  card.innerHTML = buildCard(prompt);
  wireCard(prompt);
  updateDots();
  updateProgress();
}

/* ── Category tabs ──────────────────────────────────────────────── */
function buildCats() {
  var el = document.getElementById('sf-cats');
  if (!el) return;
  var cats = [
    {k:'all',label:'⭐ All'},
    {k:'grammar',label:'📐 Grammar'},
    {k:'vocab',label:'📖 Vocabulary'},
    {k:'N5',label:'N5'},
    {k:'N4',label:'N4'},
    {k:'N3',label:'N3'},
  ];
  el.innerHTML = cats.map(function(c) {
    return '<button class="sf-cat-btn' + (c.k === currentCat ? ' active' : '') +
           '" data-cat="' + c.k + '">' + c.label + '</button>';
  }).join('');
  el.querySelectorAll('.sf-cat-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      currentCat = this.getAttribute('data-cat');
      if (currentCat === 'all') filtered = prompts.slice();
      else if (currentCat === 'grammar' || currentCat === 'vocab') filtered = prompts.filter(function(p){ return p.type === currentCat; });
      else filtered = prompts.filter(function(p){ return p.level === currentCat; });
      if (filtered.length === 0) filtered = prompts.slice();
      currentIdx = 0;
      visited = {};
      buildCats();
      buildDots();
      loadPrompt(0);
    });
  });
}

/* ── Progress bar ───────────────────────────────────────────────── */
function updateProgress() {
  var done = Object.keys(visited).length;
  var pct  = filtered.length > 0 ? Math.round(done / filtered.length * 100) : 0;
  var el   = document.getElementById('sf-progress-fill');
  if (el) el.style.width = pct + '%';
}

/* ── Dots ───────────────────────────────────────────────────────── */
var gradeColors = {S:'#a78bfa',A:'#34d399',B:'#60a5fa',C:'#fb923c',D:'#f87171'};

function buildDots() {
  var el = document.getElementById('sf-dots');
  if (!el) return;
  el.innerHTML = filtered.map(function(p, i) {
    var g = visited[i];
    var style = g ? 'background:' + (gradeColors[g] || '#556') + ';border-color:' + (gradeColors[g] || '#556') : '';
    var cls = 'sf-dot' + (i === currentIdx ? ' current' : '');
    return '<div class="' + cls + '" data-idx="' + i + '" style="' + style + '" title="' + esc(p.focus) + '"></div>';
  }).join('');
  el.querySelectorAll('.sf-dot').forEach(function(dot) {
    dot.addEventListener('click', function() {
      loadPrompt(parseInt(this.getAttribute('data-idx'), 10));
      document.getElementById('sf-card').scrollIntoView({behavior:'smooth', block:'start'});
    });
  });
}

function updateDots() {
  var el = document.getElementById('sf-dots');
  if (!el) return;
  el.querySelectorAll('.sf-dot').forEach(function(dot, i) {
    var g = visited[i];
    dot.style.background    = g ? (gradeColors[g] || '#556') : '';
    dot.style.borderColor   = g ? (gradeColors[g] || '#556') : '';
    dot.className = 'sf-dot' + (i === currentIdx ? ' current' : '');
  });
}

/* ── Boot ───────────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', function() {
  buildCats();
  buildDots();
  loadPrompt(0);
});

})();
</script>
