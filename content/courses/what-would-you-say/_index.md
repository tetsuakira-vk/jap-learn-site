---
title: "What Would You Say? — Real Japanese for Real Situations"
description: "Practice colloquial Japanese in 10 real situations — texting friends, running late, recommending music, venting about stress. Type what you'd say, get model answers, grammar notes, and vocab hints."
date: 2025-01-01
showtoc: false
---

Ten everyday situations. Each one asks you to type what you'd actually say in Japanese — casual, natural, the way people really talk. Vocabulary chips help when you get stuck, autocomplete suggests words as you type, and model answers show three levels of formality when you're ready.

<div class="wws-wrap" id="wws-app">
<div class="wws-progress-wrap">
<div class="wws-progress-bar"><div class="wws-progress-fill" id="wws-prog-fill" style="width:0%"></div></div>
<div class="wws-progress-label" id="wws-prog-label">1 / 10</div>
</div>
<div class="wws-dot-nav" id="wws-dots"></div>
<div id="wws-card-area"></div>
<div class="wws-complete" id="wws-complete">
<div class="wws-complete-icon">🎉</div>
<div class="wws-complete-title">Course Complete!</div>
<div class="wws-complete-sub" id="wws-complete-sub">You made it through all 10 situations.<br>Keep practising — the more natural it feels, the better.</div>
<div class="wws-complete-stats" id="wws-complete-stats"></div>
<div style="display:flex;gap:0.75rem;justify-content:center;flex-wrap:wrap">
<button class="wws-btn wws-btn--restart" onclick="WWS.restart()">↺ Start Again</button>
</div>
</div>
</div>

<script>
(function(){
'use strict';

var SCENARIOS=[
{
  emoji:'📱',
  situation:"Your friend texts: <em>\"Want to hang out tonight?\"</em> You're exhausted after a long day. Decline nicely.",
  chips:[
    {jp:'ごめん',en:'sorry',romaji:'gomen'},
    {jp:'無理',en:'no way / can\'t',romaji:'muri'},
    {jp:'疲れた',en:'I\'m tired',romaji:'tsukareta'},
    {jp:'今日は',en:'today (topic)',romaji:'kyouwa'},
    {jp:'また今度',en:'next time',romaji:'matakondo'},
    {jp:'きつい',en:'rough / tough',romaji:'kitsui'},
    {jp:'ちょっと',en:'a little / kind of',romaji:'chotto'}
  ],
  hints:[
    'ごめん (gomen) is the most natural opener for a casual apology or decline.',
    '無理 literally means "impossible" — in casual Japanese it\'s the standard way to say "I can\'t." Much more natural than 行けない.',
    'Try: ごめん + your reason (疲れた) + a soft close (また今度ね).'
  ],
  answers:[
    {label:'Very casual',jp:'ごめん、今日無理〜 疲れた',romaji:'Gomen, kyou muri~ tsukareta',en:'Sorry, can\'t tonight~ I\'m tired'},
    {label:'Casual',jp:'ごめんね、今日はちょっと疲れてて…',romaji:'Gomen ne, kyou wa chotto tsukarete...',en:'Sorry, I\'m a bit tired today…'},
    {label:'Softer',jp:'ごめんなさい、今日はちょっと都合が悪くて',romaji:'Gomen nasai, kyou wa chotto tsugou ga warukute',en:'I\'m sorry, today is a bit inconvenient for me'}
  ],
  grammar:[
    {term:'無理',note:'"Impossible / no way" — direct and very common in casual speech. More natural for declining than 行けない (can\'t go).'},
    {term:'〜てて',note:'て-form + て signals an ongoing state. 疲れてて = "I\'m tired (and so...)" — trailing off is natural and polite.'},
    {term:'また今度',note:'"Next time / another time." The standard soft way to imply rescheduling without over-committing.'}
  ]
},
{
  emoji:'🏃',
  situation:"You're running 15 minutes late to meet a friend at a café. Send them a quick text.",
  chips:[
    {jp:'ごめん',en:'sorry',romaji:'gomen'},
    {jp:'遅れる',en:'running late',romaji:'okureru'},
    {jp:'あと',en:'more / remaining',romaji:'ato'},
    {jp:'分',en:'minutes',romaji:'fun'},
    {jp:'今向かってる',en:'heading there now',romaji:'imamukatteru'},
    {jp:'もうすぐ',en:'almost there / soon',romaji:'mousugu'},
    {jp:'着く',en:'to arrive',romaji:'tsuku'}
  ],
  hints:[
    'あと + number + 分 = "in X more minutes." あと15分で着く = "I\'ll be there in 15 minutes."',
    '今向かってる (ima mukatteru) = "heading there now" — essential phrase for late texts.',
    'Japanese texts tend to be short. ごめん、あと15分！ on its own is perfectly natural.'
  ],
  answers:[
    {label:'Very casual',jp:'ごめん！あと15分で着く！',romaji:'Gomen! Ato juugo-fun de tsuku!',en:'Sorry! Be there in 15!'},
    {label:'Casual',jp:'ごめんね、今向かってるけどあと15分くらいかかりそう',romaji:'Gomen ne, ima mukatteru kedo ato juugo-fun kurai kakarisou',en:'Sorry, heading there now but might take another ~15 min'},
    {label:'Softer',jp:'すみません、少し遅れそうです。あと15分ほどで着きます',romaji:'Sumimasen, sukoshi okure sou desu. Ato juugo-fun hodo de tsukimasu',en:'I\'m sorry, it looks like I\'ll be a bit late. I\'ll be there in about 15 minutes.'}
  ],
  grammar:[
    {term:'あと〜分で',note:'"In X more minutes." あと = "remaining," 着く = "to arrive." One of the most useful patterns for everyday punctuality.'},
    {term:'〜そう',note:'Looks / seems probable. かかりそう = "seems like it\'ll take." Add to any い-adjective or verb stem.'},
    {term:'今〜てる',note:'Casual contraction of 〜ている (ongoing action). 向かっている → 向かってる — drop the い in casual speech.'}
  ]
},
{
  emoji:'🎵',
  situation:"You've been completely obsessed with a song all week. Text a friend — they <em>have</em> to listen to it.",
  chips:[
    {jp:'ハマる',en:'to be hooked / obsessed',romaji:'hamaru'},
    {jp:'聞いてみて',en:'try listening to it',romaji:'kiitemite'},
    {jp:'絶対',en:'definitely / for sure',romaji:'zettai'},
    {jp:'ヤバい',en:'insane / amazing (slang)',romaji:'yabai'},
    {jp:'めちゃ',en:'super / very (casual)',romaji:'mecha'},
    {jp:'最高',en:'the best',romaji:'saikou'},
    {jp:'好きそう',en:'seems like you\'d like it',romaji:'sukisou'}
  ],
  hints:[
    'ハマる = to be hooked/obsessed. 最近これにハマってる = "I\'ve been really into this lately."',
    '絶対聞いてみて = "definitely give it a listen" — 絶対 (zettai) makes the recommendation feel urgent.',
    'ヤバい originally meant "dangerous" but now means "amazing/insane" in modern casual Japanese. ヤバすぎ = "too good / insane."'
  ],
  answers:[
    {label:'Very casual',jp:'これ絶対聞いて！ヤバすぎ',romaji:'Kore zettai kiite! Yaba sugi',en:'You have to listen to this! It\'s insane'},
    {label:'Casual',jp:'最近これにめちゃハマってるんだけど、絶対好きだと思う',romaji:'Saikin kore ni mecha hamatterun dakedo, zettai suki dato omou',en:'I\'ve been super into this lately — I think you\'ll definitely love it'},
    {label:'Softer',jp:'この曲聞いてみてほしいんだけど、すごくよくて',romaji:'Kono kyoku kiite mite hoshiin dakedo, sugoku yokute',en:'I\'d love for you to give this song a listen — it\'s really good'}
  ],
  grammar:[
    {term:'ヤバい',note:'Originally "dangerous/sketchy," now the go-to slang for "amazing." ヤバすぎ = "too insane/good." Avoid in formal settings.'},
    {term:'〜んだけど',note:'Sets up context and implies something follows. ハマってるんだけど = "I\'ve been into it (and so...)" — very conversational.'},
    {term:'絶対',note:'"Definitely/absolutely." Intensifies whatever comes next. 絶対好き = "you\'ll definitely like it."'}
  ]
},
{
  emoji:'🍜',
  situation:"You want to grab ramen with a friend this weekend. Casually suggest going somewhere.",
  chips:[
    {jp:'ラーメン',en:'ramen',romaji:'raamen'},
    {jp:'食べに行かない？',en:'wanna go eat?',romaji:'tabenikanai'},
    {jp:'一緒に',en:'together',romaji:'isshoni'},
    {jp:'週末',en:'this weekend',romaji:'shuumatsu'},
    {jp:'あそこ',en:'that place over there',romaji:'asoko'},
    {jp:'美味しそう',en:'looks delicious',romaji:'oishisou'},
    {jp:'どう？',en:'how about it?',romaji:'dou'}
  ],
  hints:[
    '〜に行かない？ = "Wanna go to ~?" — the negative question form is the most natural casual invitation.',
    'どう？ on its own = "how about it?" Perfect for casual suggestions.',
    '一緒にラーメン食べに行かない？ = "Wanna go eat ramen together?" — the complete natural sentence.'
  ],
  answers:[
    {label:'Very casual',jp:'週末ラーメン食べに行かない？',romaji:'Shuumatsu raamen tabeni ikanai?',en:'Wanna go eat ramen this weekend?'},
    {label:'Casual',jp:'一緒にラーメン屋行かない？あそこ美味しそうだったんだよね',romaji:'Issho ni raamen-ya ikanai? Asoko oishisou dattan da yo ne',en:'Wanna go to that ramen place together? That spot looked so good'},
    {label:'Softer',jp:'週末もしよかったらラーメン食べに行かない？',romaji:'Shuumatsu moshi yokattara raamen tabeni ikanai?',en:'If you\'re free this weekend, wanna go eat ramen?'}
  ],
  grammar:[
    {term:'〜に行かない？',note:'"Wanna go ~?" Negative question forms are used for invitations in casual Japanese — way more natural than 行きましょう.'},
    {term:'〜屋',note:'"Shop / place." ラーメン屋 = ramen restaurant. Casual and natural — more so than レストラン for most eateries.'},
    {term:'もしよかったら',note:'"If you\'re up for it / if it\'s okay." Softens an invitation without requiring a reason. Very polite without being stiff.'}
  ]
},
{
  emoji:'📅',
  situation:"You haven't seen your friend in ages. Text them to check if they're free this weekend.",
  chips:[
    {jp:'暇？',en:'free? / got time?',romaji:'hima'},
    {jp:'週末',en:'this weekend',romaji:'shuumatsu'},
    {jp:'久しぶり',en:'long time no see',romaji:'hisashiburi'},
    {jp:'遊ぼう',en:'let\'s hang out',romaji:'asobou'},
    {jp:'最近どう？',en:'how have you been?',romaji:'saikindou'},
    {jp:'会いたい',en:'I want to see you',romaji:'aitai'},
    {jp:'時間ある？',en:'got time?',romaji:'jikanaru'}
  ],
  hints:[
    '暇？ alone is the most casual way to ask "are you free?" in Japanese — literally "bored / free time?"',
    '久しぶり = "long time no see" — perfect opener for reconnecting. 久しぶり！元気？ is super natural.',
    '週末暇？遊ぼ！ — two sentences, very short, totally natural.'
  ],
  answers:[
    {label:'Very casual',jp:'久しぶり！週末暇？遊ぼ',romaji:'Hisashiburi! Shuumatsu hima? Asobo',en:'Long time no see! Free this weekend? Let\'s hang'},
    {label:'Casual',jp:'最近どう？週末時間あったら一緒に遊ばない？',romaji:'Saikin dou? Shuumatsu jikan attara issho ni asobanai?',en:'How\'ve you been? If you\'ve got time this weekend, wanna hang?'},
    {label:'Softer',jp:'久しぶりだね。週末もし予定なければ一緒に遊べたら嬉しいな',romaji:'Hisashiburi da ne. Shuumatsu moshi yotei nakereba issho ni asobereba ureshii na',en:'It\'s been a while! If you don\'t have plans this weekend, I\'d love to hang out'}
  ],
  grammar:[
    {term:'暇？',note:'"Free?" Literally "boring/idle." Very casual availability check. Formal equivalent: ご都合はいかがですか — very different register.'},
    {term:'遊ぼ',note:'Super casual volitional. 遊ぼう → 遊ぼ. "Let\'s hang/play." The う drops in very casual spoken/text Japanese.'},
    {term:'〜たら嬉しい',note:'"I\'d be happy if ~." Softens a desire or request without being demanding. More natural than 〜てください.'}
  ]
},
{
  emoji:'😩',
  situation:"Work or school has been completely overwhelming. Text your friend to vent about how rough things have been.",
  chips:[
    {jp:'しんどい',en:'rough / exhausted',romaji:'shindoi'},
    {jp:'きつい',en:'tough / intense',romaji:'kitsui'},
    {jp:'マジ',en:'seriously / really',romaji:'maji'},
    {jp:'最近',en:'lately / recently',romaji:'saikin'},
    {jp:'忙しすぎ',en:'way too busy',romaji:'isogashisugi'},
    {jp:'限界',en:'my limit / breaking point',romaji:'genkai'},
    {jp:'疲れた',en:'I\'m tired',romaji:'tsukareta'},
    {jp:'やばい',en:'crazy / intense',romaji:'yabai'}
  ],
  hints:[
    'しんどい and きつい both mean "rough/tough." しんどい is more about fatigue and emotional exhaustion; きつい is about intensity.',
    'マジ = "seriously/really." Pairs with anything: マジ疲れた = "I\'m seriously exhausted."',
    '限界 = "limit/breaking point." 限界かも = "might be at my limit." Adding かも softens it.'
  ],
  answers:[
    {label:'Very casual',jp:'最近マジしんどい、もう限界かも',romaji:'Saikin maji shindoi, mou genkai kamo',en:'Things have been seriously rough lately, I might be at my limit'},
    {label:'Casual',jp:'最近忙しすぎて死にそう…きつい',romaji:'Saikin isogashisugite shini sou... kitsui',en:'Lately I\'ve been so busy I feel like I\'m dying… rough'},
    {label:'Softer',jp:'最近ちょっとしんどくて、疲れが取れなくて',romaji:'Saikin chotto shindokute, tsukare ga torenakute',en:'Lately it\'s been kind of rough — the tiredness just won\'t go away'}
  ],
  grammar:[
    {term:'しんどい',note:'Kansai-origin word now widely used nationally. Closer to emotional/bodily exhaustion than 疲れた. More relatable in casual venting.'},
    {term:'〜すぎて',note:'"So ~ that…" 忙しすぎて = "so busy that…" — connects cause to (implied) effect.'},
    {term:'かも',note:'"Maybe / might be." 限界かも = "might be at my limit." Softens a strong statement — Japanese speakers use this a lot even when certain.'}
  ]
},
{
  emoji:'📺',
  situation:"You just binge-watched an amazing show. Text your friend to find out if they've seen it.",
  chips:[
    {jp:'もう見た？',en:'have you seen it yet?',romaji:'moumita'},
    {jp:'一気見',en:'binge-watch',romaji:'ikkimi'},
    {jp:'ハマる',en:'to be hooked',romaji:'hamaru'},
    {jp:'絶対見て',en:'you have to watch it',romaji:'zettaimite'},
    {jp:'ヤバい',en:'insane / amazing',romaji:'yabai'},
    {jp:'おすすめ',en:'recommendation',romaji:'osusume'},
    {jp:'感動した',en:'I was moved / blown away',romaji:'kandoushita'}
  ],
  hints:[
    'もう見た？ = "Have you seen it yet?" — the most natural way to ask this. もう = "already," past tense = "have done."',
    '一気見 (ikki-mi) = "binge-watching" — 一気 (all at once) + 見 (watch). Very common modern term.',
    'If they haven\'t: 絶対見て！ = "You have to watch it!" — urgent but friendly.'
  ],
  answers:[
    {label:'Very casual',jp:'○○もう見た？ヤバすぎて一気見した',romaji:'(Show) mou mita? Yabasugite ikki mi shita',en:'Seen (show) yet? It was insane, I binge-watched everything'},
    {label:'Casual',jp:'○○見てる？まじでハマって一気見しちゃった。絶対おすすめ',romaji:'(Show) miteru? Maji de hamatte ikki mi shichatta. Zettai osusume',en:'Watching (show)? I got totally hooked and binged it. Highly recommend'},
    {label:'Softer',jp:'○○って見た？すごくよかったからおすすめしたくて',romaji:'(Show) tte mita? Sugoku yokatta kara osusume shitakute',en:'Have you seen (show)? It was so good, I wanted to recommend it'}
  ],
  grammar:[
    {term:'もう〜た？',note:'"Have you ~ yet?" もう = "already," + past tense. もう食べた？ = "Have you eaten yet?" — endlessly useful pattern.'},
    {term:'一気見',note:'Compound: 一気 (all at once) + 見 (watch). Modern word for binge-watching. You can also say 一気読み (binge-reading) for books.'},
    {term:'しちゃった',note:'しまった (ended up doing, often with slight regret/surprise). 一気見しちゃった = "ended up watching it all." Very natural for things you got carried away with.'}
  ]
},
{
  emoji:'🍽️',
  situation:"It's 3pm and you haven't eaten since breakfast. Dramatically text your friend about how hungry you are.",
  chips:[
    {jp:'お腹すいた',en:'I\'m hungry',romaji:'onakasuita'},
    {jp:'すぎる',en:'way too much',romaji:'sugiru'},
    {jp:'死にそう',en:'I feel like I\'m dying (hyperbole)',romaji:'shinisou'},
    {jp:'マジ',en:'seriously',romaji:'maji'},
    {jp:'腹ペコ',en:'starving (cute/casual)',romaji:'harapeko'},
    {jp:'なにか食べたい',en:'I want to eat something',romaji:'nanikatabetai'},
    {jp:'ご飯',en:'food / rice / meal',romaji:'gohan'}
  ],
  hints:[
    'お腹すいた = "I\'m hungry." The most natural everyday phrase — works alone as a full sentence.',
    '〜すぎる = "way too ~." お腹すきすぎる = "I\'m way too hungry."',
    '死にそう = "I feel like I\'m dying" — standard hyperbole for any intense discomfort. お腹すきすぎて死にそう is a very common thing to say.'
  ],
  answers:[
    {label:'Very casual',jp:'お腹すきすぎて死にそう',romaji:'Onaka sukisugite shini sou',en:'I\'m so hungry I feel like I\'m dying'},
    {label:'Casual',jp:'まじでお腹ペコペコなんだけど、なんか食べに行かない？',romaji:'Maji de onaka pekopeko nan dakedo, nanka tabeni ikanai?',en:'I\'m seriously starving — wanna go eat something?'},
    {label:'Softer',jp:'お腹すきすぎてちょっときついんだけど…',romaji:'Onaka sukisugite chotto kitsuin dakedo...',en:'I\'m way too hungry and it\'s kind of killing me…'}
  ],
  grammar:[
    {term:'死にそう',note:'"Seems like I\'ll die." Used constantly for harmless hyperbole: 寒くて死にそう (dying of cold), 眠くて死にそう (dying of sleepiness). Very natural casual expression.'},
    {term:'ペコペコ',note:'Onomatopoeia for an empty, growling stomach. Very cute/casual. Works as an adjective: お腹ペコペコ = "stomach is growling / starving."'},
    {term:'〜なんだけど',note:'Sets context and implies a request or continuation. "...so (I was wondering if we could eat)." The unstated part is understood by context.'}
  ]
},
{
  emoji:'🙏',
  situation:"Your friend stayed up late to help you with an important problem. Text them a heartfelt thank you.",
  chips:[
    {jp:'助かった',en:'you saved me / that helped so much',romaji:'tasukatta'},
    {jp:'めちゃ',en:'so much / really (casual)',romaji:'mecha'},
    {jp:'ありがとう',en:'thank you',romaji:'arigatou'},
    {jp:'本当に',en:'truly / really',romaji:'hontouni'},
    {jp:'おかげで',en:'thanks to you',romaji:'okagede'},
    {jp:'昨日',en:'yesterday',romaji:'kinou'},
    {jp:'なんとかなった',en:'it worked out / I managed',romaji:'nantokanatta'}
  ],
  hints:[
    '助かった (tasukatta) = "you saved me / that really helped." More heartfelt than just ありがとう.',
    'おかげで = "thanks to you." おかげでなんとかなった = "because of you it worked out."',
    'めちゃ is casual slang for "very / so much." めちゃ助かった = "you really, really saved me."'
  ],
  answers:[
    {label:'Very casual',jp:'昨日はマジ助かった！めちゃありがとう',romaji:'Kinou wa maji tasukatta! Mecha arigatou',en:'You really saved me yesterday! Thanks so much'},
    {label:'Casual',jp:'昨日は本当にありがとう。おかげでなんとかなった',romaji:'Kinou wa hontou ni arigatou. Okage de nantoka natta',en:'Thanks so much for yesterday. Because of you I managed to pull through'},
    {label:'Softer',jp:'昨日は助かりました。本当にありがとうございます',romaji:'Kinou wa tasukarimashita. Hontou ni arigatou gozaimasu',en:'You really helped me out yesterday. Thank you so much.'}
  ],
  grammar:[
    {term:'助かった',note:'Past tense of 助かる "to be saved/helped." Much warmer than ありがとうだけ. Makes the other person feel genuinely useful.'},
    {term:'おかげで',note:'"Thanks to ~." おかげで + result = because of you, this happened. おかげさまで is the more formal version.'},
    {term:'なんとかなった',note:'"Somehow managed / it worked out." なんとか = "somehow," なった = "it became." A humble, natural way to say you pulled through.'}
  ]
},
{
  emoji:'😱',
  situation:"Your friend texts you shocking news — they quit their job, got into a dream school, or something totally unexpected. React!",
  chips:[
    {jp:'うそ！',en:'no way! / you\'re kidding!',romaji:'uso'},
    {jp:'マジで？',en:'seriously?!',romaji:'majide'},
    {jp:'びっくりした',en:'I\'m shocked / surprised',romaji:'bikkurishita'},
    {jp:'すごい',en:'amazing / wow',romaji:'sugoi'},
    {jp:'え',en:'what / huh (reaction)',romaji:'e'},
    {jp:'やばい',en:'insane / wow',romaji:'yabai'},
    {jp:'信じられない',en:'I can\'t believe it',romaji:'shinjirarenai'}
  ],
  hints:[
    'うそ！ = "No way! / You\'re kidding!" — literally "lie," used as an exclamation of disbelief. Very common.',
    'マジで？ = "Seriously?!" — the casual version of 本当に？ Essential for reacting to news.',
    'びっくりした = "I was surprised / I\'m shocked." Works as a standalone sentence.'
  ],
  answers:[
    {label:'Very casual',jp:'え、うそ！？マジで！？やばすぎ',romaji:'E, uso!? Maji de!? Yaba sugi',en:'Wait, no way!? Seriously!? That\'s insane'},
    {label:'Casual',jp:'えっ、マジで！？びっくりした！すごいじゃん！',romaji:'E, maji de!? Bikkuri shita! Sugoi jan!',en:'Wait, seriously!? I\'m shocked! That\'s amazing!'},
    {label:'Softer',jp:'え、本当に！？それはすごいね、びっくりした',romaji:'E, hontou ni!? Sore wa sugoi ne, bikkuri shita',en:'Wait, really!? That\'s amazing, I\'m surprised'}
  ],
  grammar:[
    {term:'うそ',note:'Literally "lie." As an exclamation: "No way! / You\'re kidding!" Don\'t confuse with うそつき (liar) — alone as a reaction it\'s very friendly.'},
    {term:'マジで',note:'Casual 本当に ("really"). マジで？ = "Seriously?" You\'ll hear this constantly in casual Japanese.'},
    {term:'すごいじゃん',note:'じゃん = casual じゃない ("isn\'t it"). すごいじゃん = "That\'s amazing, isn\'t it!" Seeks agreement and shares excitement.'}
  ]
}
];

/* ── State ── */
var progress=[];
for(var i=0;i<SCENARIOS.length;i++)progress.push(null);
var cur=0,hintLevel=0,answered=false,assessed=false,composing=false;
var selStart=0,selEnd=0;

/* ── Helpers ── */
function el(id){return document.getElementById(id);}
function qsa(sel,ctx){return (ctx||document).querySelectorAll(sel);}

/* ─────────────────────────────────────────────────
   GRADING — bigram overlap against all model answers
   ───────────────────────────────────────────────── */
function gradeInput(userText,answers){
  if(!userText||!userText.trim())return{score:0,grade:'D',bestIdx:0,hint:'Type something to get graded!'};
  function norm(s){
    return s.replace(/[\s　！？、。「」…〜・ー～!?○]/g,'');
  }
  function bigramScore(u,a){
    var nu=norm(u),na=norm(a);
    if(na.length===0)return 0;
    if(na.length===1)return nu.indexOf(na)>=0?1:0;
    var matched=0,total=na.length-1;
    for(var i=0;i<total;i++){
      if(nu.indexOf(na.slice(i,i+2))>=0)matched++;
    }
    return matched/total;
  }
  var best=0,bestIdx=0;
  for(var i=0;i<answers.length;i++){
    var s=bigramScore(userText,answers[i].jp);
    if(s>best){best=s;bestIdx=i;}
  }
  var grade,hint;
  if(best>=0.78){grade='S';hint='Excellent — very close to natural Japanese!';}
  else if(best>=0.55){grade='A';hint='Great work — the key elements are there.';}
  else if(best>=0.35){grade='B';hint='Good attempt — check the model answers to refine it.';}
  else if(best>=0.12){grade='C';hint='You\'re trying — compare with the model answers to see what to add.';}
  else{grade='D';hint='Have a look at the vocabulary chips and model answers for ideas.';}
  return{score:Math.round(best*100),grade:grade,bestIdx:bestIdx,hint:hint};
}

function showGrade(result){
  var wrap=el('wws-grade-wrap');
  if(!wrap)return;
  var ta=el('wws-ta');
  var empty=!ta||!ta.value.trim();
  if(empty){wrap.classList.remove('wws-vis');return;}
  var matchLabel=result.score>0?' — closest to: '+SCENARIOS[cur].answers[result.bestIdx].label:'';
  wrap.innerHTML=
    '<div class="wws-grade-badge wws-grade-badge--'+result.grade+'">'+result.grade+'</div>'+
    '<div>'+
    '<div class="wws-grade-score">Match score: '+result.score+'%'+matchLabel+'</div>'+
    '<div class="wws-grade-msg">'+result.hint+'</div>'+
    '</div>';
  wrap.classList.add('wws-vis');
}

function preSetAssessment(grade){
  var map={S:'got-it',A:'got-it',B:'almost',C:'practice',D:'practice'};
  var auto=map[grade]||'almost';
  var btns=qsa('.wws-assess-btn');
  for(var i=0;i<btns.length;i++){
    if(btns[i].getAttribute('data-result')===auto){
      btns[i].classList.add('wws-pre-select');
      btns[i].innerHTML=btns[i].innerHTML+'<span class="wws-pre-label">← suggested</span>';
    }
  }
}

/* ─────────────────────────────────────────────────
   AUTOCOMPLETE — romaji prefix + kana prefix match
   ───────────────────────────────────────────────── */
function getCurrentToken(text,cursorPos){
  var before=text.slice(0,cursorPos);
  var romMatch=before.match(/[a-zA-Z]+$/);
  if(romMatch)return{text:romMatch[0],start:cursorPos-romMatch[0].length,end:cursorPos,type:'romaji'};
  var kanaMatch=before.match(/[぀-ヿ一-龯々]+$/);
  if(kanaMatch)return{text:kanaMatch[0],start:cursorPos-kanaMatch[0].length,end:cursorPos,type:'kana'};
  return null;
}

function getSuggestions(text,cursorPos,chips){
  var token=getCurrentToken(text,cursorPos);
  if(!token||token.text.length<1)return[];
  var t=token.text.toLowerCase();
  var out=[];
  for(var i=0;i<chips.length;i++){
    var c=chips[i];
    if(token.type==='romaji'){
      var r=(c.romaji||'').toLowerCase().replace(/\s/g,'');
      if(r.indexOf(t)===0&&r.length>t.length)out.push(c);
    }else{
      if(c.jp.indexOf(token.text)===0&&c.jp.length>token.text.length)out.push(c);
    }
  }
  return out.slice(0,4);
}

function updateSuggestions(){
  var ta=el('wws-ta');
  var wrap=el('wws-suggest');
  if(!ta||!wrap)return;
  var suggs=getSuggestions(ta.value,ta.selectionStart,SCENARIOS[cur].chips);
  wrap.innerHTML='';
  for(var i=0;i<suggs.length;i++){
    (function(chip){
      var btn=document.createElement('button');
      btn.className='wws-suggest-pill';
      btn.type='button';
      btn.innerHTML='<span class="wws-suggest-jp">'+chip.jp+'</span><span class="wws-suggest-en">'+chip.en+'</span>';
      btn.addEventListener('mousedown',function(e){e.preventDefault();insertSuggestion(chip);});
      btn.addEventListener('touchstart',function(e){e.preventDefault();insertSuggestion(chip);},{passive:false});
      wrap.appendChild(btn);
    })(suggs[i]);
  }
}

function insertSuggestion(chip){
  var ta=el('wws-ta');
  if(!ta)return;
  var token=getCurrentToken(ta.value,selStart);
  var before,after,newPos;
  if(token){
    before=ta.value.slice(0,token.start);
    after=ta.value.slice(token.end);
    newPos=token.start+chip.jp.length;
  }else{
    before=ta.value.slice(0,selStart);
    after=ta.value.slice(selStart);
    newPos=selStart+chip.jp.length;
  }
  ta.value=before+chip.jp+after;
  ta.focus();
  ta.setSelectionRange(newPos,newPos);
  selStart=newPos;selEnd=newPos;
  updateChipLighting();
  updateSuggestions();
}

/* ── UI builders ── */
function buildDots(){
  var wrap=el('wws-dots');
  wrap.innerHTML='';
  for(var i=0;i<SCENARIOS.length;i++){
    (function(idx){
      var d=document.createElement('button');
      d.className='wws-dot'+(idx===cur?' wws-dot--active':'');
      if(progress[idx]==='got-it')d.classList.add('wws-dot--got-it');
      else if(progress[idx]==='almost')d.classList.add('wws-dot--almost');
      else if(progress[idx]==='practice')d.classList.add('wws-dot--practice');
      d.title='Scenario '+(idx+1);
      d.setAttribute('aria-label','Go to scenario '+(idx+1));
      d.onclick=function(){goTo(idx);};
      wrap.appendChild(d);
    })(i);
  }
}

function buildProgress(){
  var pct=Math.round((cur/SCENARIOS.length)*100);
  el('wws-prog-fill').style.width=pct+'%';
  el('wws-prog-label').textContent=(cur+1)+' / '+SCENARIOS.length;
}

function buildCard(){
  var s=SCENARIOS[cur];
  var area=el('wws-card-area');
  area.innerHTML='';
  var card=document.createElement('div');
  card.className='wws-card';

  var html='<div class="wws-card-emoji">'+s.emoji+'</div>';
  html+='<div class="wws-card-label">Situation '+(cur+1)+' of '+SCENARIOS.length+'</div>';
  html+='<div class="wws-situation">'+s.situation+'</div>';

  html+='<div class="wws-input-area">';
  html+='<label class="wws-input-label" for="wws-ta">What would you say? Type in Japanese:</label>';
  html+='<textarea class="wws-textarea" id="wws-ta" placeholder="Type your response in Japanese… (romaji autocomplete: try \'go\' for ごめん)" rows="3" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"><'+'\/textarea>';
  html+='<div class="wws-suggest" id="wws-suggest"></div>';
  html+='</div>';

  html+='<div class="wws-chips-label">Vocabulary — click to insert at cursor:</div>';
  html+='<div class="wws-chips" id="wws-chips">';
  for(var i=0;i<s.chips.length;i++){
    html+='<button class="wws-chip" data-jp="'+encodeURIComponent(s.chips[i].jp)+'" data-idx="'+i+'">';
    html+='<span class="wws-chip-jp">'+s.chips[i].jp+'</span>';
    html+='<span class="wws-chip-en">'+s.chips[i].en+'</span>';
    html+='</button>';
  }
  html+='</div>';

  html+='<div class="wws-grade-wrap" id="wws-grade-wrap"></div>';

  html+='<div class="wws-actions">';
  html+='<button class="wws-btn wws-btn--check" id="wws-check">Check answers</button>';
  html+='<button class="wws-btn wws-btn--hint" id="wws-hint">💡 Hint</button>';
  html+='<button class="wws-btn wws-btn--skip" id="wws-skip">Skip →</button>';
  html+='</div>';

  html+='<div class="wws-hint-box" id="wws-hint-box"><div class="wws-hint-num" id="wws-hint-num"></div><div id="wws-hint-text"></div></div>';

  html+='<div class="wws-answers" id="wws-answers">';
  html+='<div class="wws-answers-title">Model Answers</div>';
  for(var j=0;j<s.answers.length;j++){
    html+='<div class="wws-answer-block">';
    html+='<div class="wws-answer-label">'+s.answers[j].label+'</div>';
    html+='<div class="wws-answer-jp">'+s.answers[j].jp+'</div>';
    html+='<div class="wws-answer-romaji">'+s.answers[j].romaji+'</div>';
    html+='<div class="wws-answer-en">'+s.answers[j].en+'</div>';
    html+='</div>';
  }
  html+='<div class="wws-grammar">';
  html+='<div class="wws-grammar-title">Grammar &amp; Vocabulary Notes</div>';
  for(var k=0;k<s.grammar.length;k++){
    html+='<div class="wws-grammar-item">';
    html+='<div class="wws-grammar-term">'+s.grammar[k].term+'</div>';
    html+='<div class="wws-grammar-note">'+s.grammar[k].note+'</div>';
    html+='</div>';
  }
  html+='</div>';
  html+='<div class="wws-assess" id="wws-assess">';
  html+='<div class="wws-assess-title">How did you do?</div>';
  html+='<div class="wws-assess-btns">';
  html+='<button class="wws-assess-btn wws-assess-btn--got-it" data-result="got-it">✓ Got it</button>';
  html+='<button class="wws-assess-btn wws-assess-btn--almost" data-result="almost">〜 Almost</button>';
  html+='<button class="wws-assess-btn wws-assess-btn--practice" data-result="practice">✗ Need practice</button>';
  html+='</div>';
  html+='<div class="wws-assess-note" id="wws-assess-note"></div>';
  html+='</div>';
  html+='<div class="wws-next-row" id="wws-next-row">';
  if(cur>0){
    html+='<button class="wws-btn wws-btn--skip" id="wws-prev">← Previous</button>';
  }else{
    html+='<span></span>';
  }
  html+='<button class="wws-btn wws-btn--next" id="wws-next">'+(cur<SCENARIOS.length-1?'Next →':'Finish')+'</button>';
  html+='</div>';
  html+='</div>';

  card.innerHTML=html;
  area.appendChild(card);
  wireEvents();
}

function wireEvents(){
  var ta=el('wws-ta');
  var chips=qsa('.wws-chip');
  var hintBtn=el('wws-hint');
  var checkBtn=el('wws-check');
  var skipBtn=el('wws-skip');
  var nextBtn=el('wws-next');
  var prevBtn=el('wws-prev');
  var assessBtns=qsa('.wws-assess-btn');

  ta.addEventListener('compositionstart',function(){composing=true;});
  ta.addEventListener('compositionend',function(){
    composing=false;
    updateChipLighting();
    updateSuggestions();
  });
  ta.addEventListener('input',function(){
    if(!composing){
      updateChipLighting();
      updateSuggestions();
    }
  });
  ta.addEventListener('blur',function(){
    selStart=ta.selectionStart;selEnd=ta.selectionEnd;
    setTimeout(function(){
      var wrap=el('wws-suggest');
      if(wrap&&document.activeElement&&!document.activeElement.classList.contains('wws-suggest-pill')){
        wrap.innerHTML='';
      }
    },200);
  });
  ta.addEventListener('keyup',function(){selStart=ta.selectionStart;selEnd=ta.selectionEnd;});
  ta.addEventListener('click',function(){selStart=ta.selectionStart;selEnd=ta.selectionEnd;});

  for(var i=0;i<chips.length;i++){
    chips[i].addEventListener('click',function(){
      var jp=decodeURIComponent(this.getAttribute('data-jp'));
      insertChip(jp);
    });
  }

  hintBtn.addEventListener('click',function(){showNextHint();});
  checkBtn.addEventListener('click',function(){revealAnswers();});
  skipBtn.addEventListener('click',function(){skipScenario();});
  if(nextBtn)nextBtn.addEventListener('click',function(){advance(1);});
  if(prevBtn)prevBtn.addEventListener('click',function(){advance(-1);});

  for(var j=0;j<assessBtns.length;j++){
    assessBtns[j].addEventListener('click',function(){
      setAssessment(this.getAttribute('data-result'));
    });
  }

  ta.focus();
}

function insertChip(jp){
  var ta=el('wws-ta');
  var start=selStart,end=selEnd;
  var val=ta.value;
  if(start===undefined||start===null)start=val.length;
  if(end===undefined||end===null)end=val.length;
  ta.value=val.substring(0,start)+jp+val.substring(end);
  var newPos=start+jp.length;
  ta.focus();
  ta.setSelectionRange(newPos,newPos);
  selStart=newPos;selEnd=newPos;
  updateChipLighting();
  updateSuggestions();
}

function updateChipLighting(){
  var ta=el('wws-ta');
  if(!ta)return;
  var val=ta.value;
  var chips=qsa('.wws-chip');
  for(var i=0;i<chips.length;i++){
    var jp=decodeURIComponent(chips[i].getAttribute('data-jp'));
    if(val.indexOf(jp)>=0){chips[i].classList.add('wws-chip--lit');}
    else{chips[i].classList.remove('wws-chip--lit');}
  }
}

function showNextHint(){
  var s=SCENARIOS[cur];
  if(hintLevel>=s.hints.length)return;
  hintLevel++;
  var box=el('wws-hint-box');
  el('wws-hint-num').textContent='Hint '+hintLevel+' of '+s.hints.length;
  el('wws-hint-text').textContent=s.hints[hintLevel-1];
  box.classList.add('wws-vis');
  var btn=el('wws-hint');
  if(hintLevel>=s.hints.length){btn.textContent='No more hints';btn.disabled=true;}
  else{btn.textContent='💡 Next hint';}
}

function revealAnswers(){
  if(answered)return;
  answered=true;
  var ta=el('wws-ta');
  var userText=ta?ta.value.trim():'';
  var result=gradeInput(userText,SCENARIOS[cur].answers);
  showGrade(result);
  el('wws-answers').classList.add('wws-vis');
  el('wws-assess').classList.add('wws-vis');
  if(userText)preSetAssessment(result.grade);
  var checkBtn=el('wws-check');
  if(checkBtn){checkBtn.disabled=true;checkBtn.textContent='✓ Revealed';}
  var suggest=el('wws-suggest');
  if(suggest)suggest.innerHTML='';
}

function setAssessment(result){
  if(assessed)return;
  assessed=true;
  progress[cur]=result;
  buildDots();
  var notes={
    'got-it':'Nice work! Moving on will really lock it in.',
    'almost':'Almost there — the model answers are a great reference to reread.',
    'practice':'No worries — the more you see it, the more natural it feels. You can always come back.'
  };
  var noteEl=el('wws-assess-note');
  if(noteEl)noteEl.textContent=notes[result]||'';
  var btns=qsa('.wws-assess-btn');
  for(var i=0;i<btns.length;i++){
    btns[i].classList.remove('wws-pre-select');
    if(btns[i].getAttribute('data-result')===result){btns[i].classList.add('wws-chosen');}
    else{btns[i].disabled=true;btns[i].style.opacity='0.4';}
  }
  var nextRow=el('wws-next-row');
  if(nextRow)nextRow.classList.add('wws-vis');
}

function skipScenario(){
  if(!answered){revealAnswers();}
  var nextRow=el('wws-next-row');
  if(nextRow)nextRow.classList.add('wws-vis');
}

function advance(dir){
  var next=cur+dir;
  if(next<0)return;
  if(next>=SCENARIOS.length){showComplete();return;}
  goTo(next);
}

function goTo(idx){
  cur=idx;hintLevel=0;answered=false;assessed=false;
  el('wws-complete').classList.remove('wws-vis');
  el('wws-card-area').style.display='';
  buildProgress();buildDots();buildCard();
  window.scrollTo({top:el('wws-app').getBoundingClientRect().top+window.scrollY-80,behavior:'smooth'});
}

function showComplete(){
  el('wws-card-area').style.display='none';
  buildProgress();
  el('wws-prog-fill').style.width='100%';
  el('wws-prog-label').textContent='Complete!';
  var got=0,almost=0,practice=0;
  for(var i=0;i<progress.length;i++){
    if(progress[i]==='got-it')got++;
    else if(progress[i]==='almost')almost++;
    else if(progress[i]==='practice')practice++;
  }
  el('wws-complete-stats').innerHTML=
    '<div class="wws-stat-block"><div class="wws-stat-num wws-stat-num--got">'+got+'</div><div class="wws-stat-lbl">Got it</div></div>'+
    '<div class="wws-stat-block"><div class="wws-stat-num wws-stat-num--almost">'+almost+'</div><div class="wws-stat-lbl">Almost</div></div>'+
    '<div class="wws-stat-block"><div class="wws-stat-num wws-stat-num--practice">'+practice+'</div><div class="wws-stat-lbl">Need practice</div></div>';
  el('wws-complete').classList.add('wws-vis');
  buildDots();
  window.scrollTo({top:el('wws-app').getBoundingClientRect().top+window.scrollY-80,behavior:'smooth'});
}

var WWS={restart:function(){for(var i=0;i<progress.length;i++)progress[i]=null;goTo(0);}};
window.WWS=WWS;

buildProgress();
buildDots();
buildCard();
})();
</script>
