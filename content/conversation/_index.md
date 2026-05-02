---
title: "Japanese Conversation Practice — Real Scenario Roleplay"
description: "Practise speaking Japanese with real-life scenarios. Use your microphone to respond in Japanese — konbini, izakaya, asking directions, hotel check-in. Free interactive speaking practice."
date: 2025-01-01
showtoc: false
---

Pick a scenario and have a real Japanese conversation. The other character speaks — you respond using your microphone. Works best in **Chrome or Edge on desktop**.

<div id="cv-selector">
  <div class="cv-beta-notice">
    🧪 <strong>Beta feature</strong> — this works best in <strong>Chrome or Edge on desktop</strong>. Speech recognition can be temperamental: it needs mic permission, a quiet environment, and clear speech. Firefox and Safari don't support it at all — you'll get a text input instead. If it misbehaves, hit the microphone button again or switch to typing. We're working on improving it!
  </div>
  <div id="cv-no-speech" class="cv-warn" style="display:none">⚠️ Speech recognition isn't supported in your browser — Chrome or Edge on desktop works best. You can still practise by typing your responses below.</div>
  <div class="cv-scenario-grid">
    <div class="cv-sc-card" data-id="konbini">
      <div class="cv-sc-emoji">🏪</div>
      <div class="cv-sc-title">コンビニ</div>
      <div class="cv-sc-en">Convenience Store</div>
      <div class="cv-sc-meta">5 turns · Beginner</div>
    </div>
    <div class="cv-sc-card" data-id="izakaya">
      <div class="cv-sc-emoji">🍺</div>
      <div class="cv-sc-title">居酒屋</div>
      <div class="cv-sc-en">Izakaya / Bar</div>
      <div class="cv-sc-meta">5 turns · Beginner</div>
    </div>
    <div class="cv-sc-card" data-id="directions">
      <div class="cv-sc-emoji">🗺️</div>
      <div class="cv-sc-title">道を聞く</div>
      <div class="cv-sc-en">Asking Directions</div>
      <div class="cv-sc-meta">4 turns · Beginner</div>
    </div>
    <div class="cv-sc-card" data-id="hotel">
      <div class="cv-sc-emoji">🏨</div>
      <div class="cv-sc-title">ホテル</div>
      <div class="cv-sc-en">Hotel Check-in</div>
      <div class="cv-sc-meta">5 turns · Beginner</div>
    </div>
  </div>
</div>

<div id="cv-main" style="display:none">
  <div class="cv-topbar">
    <button id="cv-back-btn" class="cv-back-btn">← Scenarios</button>
    <div id="cv-topbar-title" class="cv-topbar-title"></div>
    <div id="cv-topbar-score" class="cv-topbar-score"></div>
  </div>
  <div id="cv-scene-desc" class="cv-scene-desc"></div>
  <div id="cv-log" class="cv-log"></div>
  <div id="cv-bar" class="cv-bottom-bar"></div>
</div>

<div id="cv-end" style="display:none">
  <div class="cv-end-inner">
    <div id="cv-end-emoji" class="cv-end-emoji"></div>
    <div id="cv-end-title" class="cv-end-title"></div>
    <div id="cv-end-score" class="cv-end-score"></div>
    <div id="cv-end-msg" class="cv-end-msg"></div>
    <div class="cv-end-btns">
      <button id="cv-retry-btn" class="cv-end-btn cv-end-btn--primary">Try again</button>
      <button id="cv-other-btn" class="cv-end-btn">Other scenarios</button>
    </div>
  </div>
</div>

<script>
(function() {

var SCENARIOS = [
  {
    id: 'konbini', title: 'コンビニ', titleEn: 'Convenience Store', emoji: '🏪',
    desc: 'You walk into a 7-Eleven. The staff greet you and help with your purchase.',
    turns: [
      {
        npc: 'いらっしゃいませ！', npcEn: 'Welcome!',
        npcNote: 'The standard konbini greeting — no response needed.',
        userTask: null
      },
      {
        npc: 'ご注文はお決まりですか？', npcEn: 'Have you decided what you\'d like?',
        userTask: 'Order something — ask for a rice ball and/or coffee',
        userHint: 'おにぎりとコーヒーをください', userHintRomaji: 'onigiri to koohii wo kudasai',
        keywords: ['おにぎり','コーヒー','ください','ちょうだい','一つ','ひとつ','ふたつ','飲み物','食べ物','お茶'],
        successNpc: 'かしこまりました。おにぎりとコーヒーですね。', successNpcEn: 'Certainly. A rice ball and coffee, right?',
        failNpc: 'すみません、もう一度お願いします。', failNpcEn: 'Sorry, could you repeat that?',
        tip: 'ください (kudasai) turns any item into a polite request — just say [item] + をください.'
      },
      {
        npc: 'お弁当は温めますか？', npcEn: 'Shall I warm up your bento?',
        userTask: 'Say yes please, or no thank you',
        userHint: 'はい、お願いします　／　いいえ、大丈夫です', userHintRomaji: 'hai, onegaishimasu  /  iie, daijoubu desu',
        keywords: ['はい','お願い','いいえ','大丈夫','けっこう','いいです','ええ'],
        successNpc: 'かしこまりました。', successNpcEn: 'Understood.',
        failNpc: 'もう一度おっしゃっていただけますか？', failNpcEn: 'Could you say that one more time?',
        tip: '大丈夫です (daijoubu desu) means "it\'s fine / no problem" — a very natural, gentle way to decline.'
      },
      {
        npc: 'ポイントカードはお持ちですか？', npcEn: 'Do you have a points card?',
        userTask: 'Say you don\'t have one',
        userHint: 'いいえ、持っていません', userHintRomaji: 'iie, motte imasen',
        keywords: ['いいえ','ない','ありません','持っていません','けっこう','ないです'],
        successNpc: 'わかりました。お会計は680円です。', successNpcEn: 'Understood. Your total is 680 yen.',
        failNpc: 'ポイントカードはいかがですか？', failNpcEn: 'Would you like a points card?',
        tip: '持っていません (motte imasen) = "I don\'t have it." ありません also works — both are natural here.'
      },
      {
        npc: '680円です。ありがとうございます！', npcEn: 'That\'s 680 yen. Thank you!',
        userTask: 'Thank the staff and say goodbye',
        userHint: 'ありがとうございました！', userHintRomaji: 'arigatou gozaimashita!',
        keywords: ['ありがとう','どうも','また','さようなら','では','じゃあ','はい'],
        successNpc: 'ありがとうございました！またお越しくださいませ！', successNpcEn: 'Thank you very much! Please come again!',
        failNpc: 'またお越しくださいませ。', failNpcEn: 'Please come again.',
        tip: 'ありがとうございました uses past-tense ました — warmer and more final than ありがとうございます at the end of a transaction.'
      }
    ]
  },
  {
    id: 'izakaya', title: '居酒屋', titleEn: 'Izakaya / Bar', emoji: '🍺',
    desc: 'You\'re at a traditional Japanese izakaya for the evening. Order drinks, confirm your food, then ask for the bill.',
    turns: [
      {
        npc: 'いらっしゃいませ！何名様ですか？', npcEn: 'Welcome! How many people?',
        userTask: 'Tell them how many people — 1 or 2',
        userHint: '二人です　／　一人です', userHintRomaji: 'futari desu  /  hitori desu',
        keywords: ['一人','二人','ひとり','ふたり','一名','二名','いち','に','1','2'],
        successNpc: 'ありがとうございます。こちらへどうぞ。', successNpcEn: 'Thank you. This way please.',
        failNpc: '何名様でしょうか？', failNpcEn: 'How many guests, please?',
        tip: '一人 (hitori) and 二人 (futari) are irregular counters for people — worth memorising separately from other counters.'
      },
      {
        npc: 'ご注文はお決まりですか？', npcEn: 'Are you ready to order?',
        userTask: 'Order a beer and a snack (edamame, karaage, yakitori…)',
        userHint: 'ビールをふたつと枝豆をください', userHintRomaji: 'biiru wo futatsu to edamame wo kudasai',
        keywords: ['ビール','枝豆','唐揚げ','焼き鳥','刺身','ください','お願い','酒','サワー'],
        successNpc: 'かしこまりました！少々お待ちください。', successNpcEn: 'Certainly! Please wait a moment.',
        failNpc: 'ご注文はなんでしょうか？', failNpcEn: 'What would you like?',
        tip: 'ふたつ (futatsu) = two of something. ひとつ (hitotsu) = one. These work for most objects in casual ordering.'
      },
      {
        npc: 'お待たせしました！ご注文の品はお揃いでしょうか？', npcEn: 'Sorry for the wait! Does everything look right?',
        userTask: 'Confirm everything is here and thank them',
        userHint: 'はい、大丈夫です。ありがとうございます。', userHintRomaji: 'hai, daijoubu desu. arigatou gozaimasu.',
        keywords: ['はい','大丈夫','ありがとう','いいです','そうです'],
        successNpc: 'ごゆっくりどうぞ！', successNpcEn: 'Please take your time!',
        failNpc: '何かご不便はありますか？', failNpcEn: 'Is there anything wrong?',
        tip: '大丈夫 (daijoubu) is incredibly useful — "fine", "OK", "no problem." One of the first words worth mastering.'
      },
      {
        npc: 'ご注文はよろしいでしょうか？', npcEn: 'Would you like to order anything else?',
        userTask: 'Ask for the bill',
        userHint: 'お会計をお願いします', userHintRomaji: 'okaikei wo onegaishimasu',
        keywords: ['お会計','会計','払う','勘定','チェック','いくら','お金'],
        successNpc: 'かしこまりました。少々お待ちください。', successNpcEn: 'Of course. One moment please.',
        failNpc: 'もう一杯いかがですか？', failNpcEn: 'Would you like another drink?',
        tip: 'お会計をお願いします is the most natural way to ask for the bill. In casual places you might also say チェック (chekku).'
      },
      {
        npc: 'お待たせしました。3,200円になります。', npcEn: 'Sorry for the wait. That\'ll be 3,200 yen.',
        userTask: 'Pay and thank the staff',
        userHint: 'はい、どうぞ。ありがとうございました！', userHintRomaji: 'hai, douzo. arigatou gozaimashita!',
        keywords: ['ありがとう','どうも','どうぞ','はい','また','おいしかった'],
        successNpc: 'ありがとうございました！またぜひいらしてください！', successNpcEn: 'Thank you very much! Please come back!',
        failNpc: 'ありがとうございます。', failNpcEn: 'Thank you.',
        tip: 'おいしかった！ (oishikatta) = "It was delicious!" — a lovely extra to add when leaving a restaurant or izakaya.'
      }
    ]
  },
  {
    id: 'directions', title: '道を聞く', titleEn: 'Asking Directions', emoji: '🗺️',
    desc: 'You\'re lost near the station. Stop someone on the street and ask for help finding your way.',
    turns: [
      {
        npc: '（道行く人が歩いています）', npcEn: '(A person is walking by)',
        npcNote: 'Get their attention — you make the first move here.',
        userTask: 'Get their attention and ask where the station is',
        userHint: 'すみません、駅はどこですか？', userHintRomaji: 'sumimasen, eki wa doko desu ka?',
        keywords: ['すみません','駅','どこ','場所','ちょっと','教えて','電車'],
        successNpc: 'あ、駅ですか。あの交差点を右に曲がってください。5分くらいです。', successNpcEn: 'Ah, the station? Turn right at that intersection. About 5 minutes.',
        failNpc: 'はい？', failNpcEn: 'Yes?',
        tip: 'すみません (sumimasen) gets attention politely. Then [place] はどこですか is the key question pattern for finding anything.'
      },
      {
        npc: 'わかりましたか？', npcEn: 'Did you understand?',
        userTask: 'Ask them to say it again slowly',
        userHint: 'すみません、もう一度ゆっくりお願いします', userHintRomaji: 'sumimasen, mou ichido yukkuri onegaishimasu',
        keywords: ['もう一度','ゆっくり','繰り返し','もう少し','もう一回'],
        successNpc: 'はい、もちろん。交差点を右に曲がって、まっすぐ行ってください。', successNpcEn: 'Of course. Turn right at the intersection and go straight.',
        failNpc: 'えっと、もう一度言いましょうか？', failNpcEn: 'Shall I say it again?',
        tip: 'もう一度 (mou ichido) = one more time. ゆっくり (yukkuri) = slowly. These two words together will help you constantly in Japan.'
      },
      {
        npc: '右に曲がって、まっすぐ行けばわかりますよ。', npcEn: 'Turn right and go straight — you\'ll see it.',
        userTask: 'Tell them you understand and thank them',
        userHint: 'はい、わかりました。ありがとうございます！', userHintRomaji: 'hai, wakarimashita. arigatou gozaimasu!',
        keywords: ['わかりました','ありがとう','了解','なるほど','わかります','はい'],
        successNpc: 'よかった！気をつけてどうぞ！', successNpcEn: 'Great! Take care!',
        failNpc: '大丈夫ですか？', failNpcEn: 'Are you okay?',
        tip: 'わかりました (wakarimashita) is past tense — "I understood / I\'ve got it." More final than わかります.'
      },
      {
        npc: '気をつけてどうぞ！', npcEn: 'Take care!',
        userTask: 'Thank them and say goodbye',
        userHint: 'ありがとうございました！失礼します。', userHintRomaji: 'arigatou gozaimashita! shitsurei shimasu.',
        keywords: ['ありがとう','さようなら','では','じゃあ','また','失礼','どうも'],
        successNpc: 'いいえ、どういたしまして！いってらっしゃい！', successNpcEn: 'Not at all! Off you go!',
        failNpc: 'どういたしまして！', failNpcEn: 'You\'re welcome!',
        tip: '失礼します (shitsurei shimasu) literally means "I am being rude" — it\'s a polite exit phrase used when leaving someone or ending a call.'
      }
    ]
  },
  {
    id: 'hotel', title: 'ホテル', titleEn: 'Hotel Check-in', emoji: '🏨',
    desc: 'You\'ve arrived at your hotel in Japan. Check in, confirm your booking, and ask about breakfast.',
    turns: [
      {
        npc: 'いらっしゃいませ。ご予約はされていますか？', npcEn: 'Welcome. Do you have a reservation?',
        userTask: 'Confirm your reservation and give your name',
        userHint: 'はい、予約しています。[your name]です。', userHintRomaji: 'hai, yoyaku shite imasu. [your name] desu.',
        keywords: ['はい','予約','しています','名前','私','あります','ええ'],
        successNpc: 'ありがとうございます。お名前をいただけますか？', successNpcEn: 'Thank you. Could I have your name please?',
        failNpc: 'ご予約はございますか？', failNpcEn: 'Do you have a booking?',
        tip: '予約しています (yoyaku shite imasu) = "I have a reservation." The て + います form shows an ongoing or completed state.'
      },
      {
        npc: 'ありがとうございます。シングルルーム、2泊のご予約ですね。', npcEn: 'Thank you. That\'s a single room for 2 nights.',
        userTask: 'Confirm that\'s correct',
        userHint: 'はい、そうです', userHintRomaji: 'hai, sou desu',
        keywords: ['はい','そうです','正しい','合って','間違いない','ええ','そう'],
        successNpc: 'かしこまりました。パスポートをご提示いただけますか？', successNpcEn: 'Understood. Could you show me your passport?',
        failNpc: 'よろしいでしょうか？', failNpcEn: 'Is that correct?',
        tip: 'そうです (sou desu) = "That\'s right." Short, natural, and used constantly for confirming details.'
      },
      {
        npc: 'ありがとうございます。チェックアウトは午前11時です。', npcEn: 'Thank you. Check-out is at 11am.',
        userTask: 'Ask what time breakfast is served',
        userHint: '朝食は何時からですか？', userHintRomaji: 'choushoku wa nanji kara desu ka?',
        keywords: ['朝食','朝ごはん','朝ご飯','何時','時間','いつ','ブレックファスト','あさ'],
        successNpc: '朝食は7時から10時です。レストランは1階にございます。', successNpcEn: 'Breakfast is from 7am to 10am. The restaurant is on the first floor.',
        failNpc: 'ご質問はありますか？', failNpcEn: 'Do you have any questions?',
        tip: 'から (kara) = from. 何時から (nanji kara) = from what time? Pair it with まで (made = until) to ask for a full time range.'
      },
      {
        npc: 'こちらがお部屋の鍵です。お部屋は3階でございます。', npcEn: 'Here is your room key. Your room is on the third floor.',
        userTask: 'Thank them and ask where the elevator is',
        userHint: 'ありがとうございます。エレベーターはどこですか？', userHintRomaji: 'arigatou gozaimasu. erebeetaa wa doko desu ka?',
        keywords: ['エレベーター','どこ','ありがとう','場所','エレベータ'],
        successNpc: 'エレベーターはあちらでございます。ごゆっくりお過ごしください。', successNpcEn: 'The elevator is over there. Please enjoy your stay.',
        failNpc: 'ご不明な点はございますか？', failNpcEn: 'Is there anything you need help with?',
        tip: 'エレベーター is straight from English "elevator" — Japan uses many loanwords (外来語, gairaigo) for modern facilities.'
      },
      {
        npc: 'ごゆっくりお過ごしください！', npcEn: 'Enjoy your stay!',
        userTask: 'Thank them warmly',
        userHint: 'ありがとうございます。よろしくお願いします。', userHintRomaji: 'arigatou gozaimasu. yoroshiku onegaishimasu.',
        keywords: ['ありがとう','どうも','よろしく','お願い','どうぞ','はい'],
        successNpc: 'どうぞよろしくお願いします！またなにかあればフロントまでどうぞ。', successNpcEn: 'We look forward to serving you! Come to the front desk if you need anything.',
        failNpc: 'ありがとうございます。', failNpcEn: 'Thank you.',
        tip: 'よろしくお願いします (yoroshiku onegaishimasu) has no single English translation — roughly "I\'m in your care." You\'ll hear it in almost every formal interaction.'
      }
    ]
  }
];

// ── State ──
var state = { scenario: null, turnIdx: 0, score: 0, attempts: 0, hasSpeech: false };

// ── DOM ──
var sel   = document.getElementById('cv-selector');
var main  = document.getElementById('cv-main');
var end   = document.getElementById('cv-end');
var cvLog = document.getElementById('cv-log');
var bar   = document.getElementById('cv-bar');

// ── Init ──
function init() {
  state.hasSpeech = !!(window.SpeechRecognition || window.webkitSpeechRecognition);
  if (!state.hasSpeech) document.getElementById('cv-no-speech').style.display = 'block';
  document.querySelectorAll('.cv-sc-card').forEach(function(card) {
    card.addEventListener('click', function() { loadScenario(card.dataset.id); });
  });
  document.getElementById('cv-back-btn').addEventListener('click', showSelector);
  document.getElementById('cv-retry-btn').addEventListener('click', function() { loadScenario(state.scenario.id); });
  document.getElementById('cv-other-btn').addEventListener('click', showSelector);
}

function showSelector() {
  sel.style.display = 'block'; main.style.display = 'none'; end.style.display = 'none';
}

function loadScenario(id) {
  state.scenario = SCENARIOS.find(function(s) { return s.id === id; });
  state.turnIdx = 0; state.score = 0; state.attempts = 0;
  sel.style.display = 'none'; end.style.display = 'none'; main.style.display = 'block';
  document.getElementById('cv-topbar-title').textContent = state.scenario.emoji + ' ' + state.scenario.title + ' — ' + state.scenario.titleEn;
  document.getElementById('cv-scene-desc').textContent = state.scenario.desc;
  cvLog.innerHTML = ''; bar.innerHTML = '';
  updateScore();
  showTurn();
}

function updateScore() {
  var total = state.scenario.turns.filter(function(t) { return !!t.userTask; }).length;
  document.getElementById('cv-topbar-score').textContent = state.score + ' / ' + total;
}

// ── Turn flow ──
function showTurn() {
  if (state.turnIdx >= state.scenario.turns.length) { showEnd(); return; }
  var turn = state.scenario.turns[state.turnIdx];
  state.attempts = 0;
  addNpcBubble(turn.npc, turn.npcEn);
  if (!turn.userTask) {
    setBarListen(turn);
  } else {
    addHintBubble(turn);
    setBarSpeak(turn);
  }
}

// ── Bubble helpers ──
function addNpcBubble(jp, en) {
  var div = document.createElement('div');
  div.className = 'cv-bubble cv-bubble--npc';
  var safeJp = jp.replace(/'/g, "\\'");
  var hearBtn = (!jp.startsWith('（'))
    ? '<button class="cvb-hear" onclick="(function(){if(!window.speechSynthesis)return;window.speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(\'' + safeJp + '\');u.lang=\'ja-JP\';u.rate=0.82;window.speechSynthesis.speak(u);})()">▶</button>'
    : '';
  div.innerHTML = hearBtn + '<div class="cvb-jp">' + jp + '</div>' + (en ? '<div class="cvb-en">' + en + '</div>' : '');
  cvLog.appendChild(div);
  scroll();
  if (!jp.startsWith('（')) cvSpeak(jp);
}

function addHintBubble(turn) {
  var existing = document.getElementById('cv-hint-bubble');
  if (existing) existing.parentNode.removeChild(existing);
  var div = document.createElement('div');
  div.className = 'cv-bubble cv-bubble--hint';
  div.id = 'cv-hint-bubble';
  div.innerHTML =
    '<div class="cvb-hint-label">💡 Hint</div>' +
    '<div class="cvb-jp">' + turn.userHint + '</div>' +
    '<div class="cvb-romaji">' + turn.userHintRomaji + '</div>';
  cvLog.appendChild(div);
  scroll();
}

function removeHintBubble() {
  var h = document.getElementById('cv-hint-bubble');
  if (h) h.parentNode.removeChild(h);
}

function addUserBubble(transcript, status) {
  removeHintBubble();
  var div = document.createElement('div');
  div.className = 'cv-bubble cv-bubble--user cv-bubble--' + status;
  div.innerHTML = '<div class="cvb-jp">' + transcript + '</div>';
  cvLog.appendChild(div);
  scroll();
}

function addTipBubble(tip) {
  var div = document.createElement('div');
  div.className = 'cv-bubble cv-bubble--tip';
  div.innerHTML = '<span class="cvb-tip-icon">💬</span> ' + tip;
  cvLog.appendChild(div);
  scroll();
}

function scroll() { cvLog.scrollTop = cvLog.scrollHeight; }

// ── Bottom bar states ──
function setBarListen(turn) {
  bar.innerHTML =
    '<div class="cvb-task-row">' + (turn.npcNote || 'Listen, then continue.') + '</div>' +
    '<div class="cv-action-row">' +
      '<button class="cv-hear-btn" id="cv-hear-npc">▶ Hear it</button>' +
      '<button class="cv-next-btn" id="cv-cont-btn">Continue →</button>' +
    '</div>';
  document.getElementById('cv-hear-npc').addEventListener('click', function() { cvSpeak(turn.npc); });
  document.getElementById('cv-cont-btn').addEventListener('click', function() { state.turnIdx++; showTurn(); });
}

function setBarSpeak(turn) {
  var typeFallback = !state.hasSpeech;
  bar.innerHTML =
    '<div class="cvb-task-row"><strong>Your turn:</strong> ' + turn.userTask + '</div>' +
    '<div class="cv-action-row">' +
      (state.hasSpeech ? '<button class="cv-speak-main" id="cv-speak-btn">🎤 Speak</button>' : '') +
      (state.hasSpeech ? '<button class="cv-type-link" id="cv-type-link">⌨ type instead</button>' : '') +
    '</div>' +
    '<div class="cv-type-row" id="cv-type-row"' + (typeFallback ? '' : ' style="display:none"') + '>' +
      '<input class="cv-type-input" type="text" id="cv-type-input" placeholder="Type in Japanese…">' +
      '<button class="cv-submit-btn" id="cv-submit-btn">Send</button>' +
    '</div>';

  if (state.hasSpeech) {
    document.getElementById('cv-speak-btn').addEventListener('click', function() { startListening(turn); });
    document.getElementById('cv-type-link').addEventListener('click', function() {
      document.getElementById('cv-type-row').style.display = 'flex';
      this.style.display = 'none';
      document.getElementById('cv-type-input').focus();
    });
  }
  var sub = document.getElementById('cv-submit-btn');
  if (sub) {
    sub.addEventListener('click', function() {
      var v = document.getElementById('cv-type-input').value.trim();
      if (v) checkResponse(v, turn);
    });
    document.getElementById('cv-type-input').addEventListener('keydown', function(e) {
      if (e.key === 'Enter' && this.value.trim()) checkResponse(this.value.trim(), turn);
    });
  }
}

function setBarNext() {
  var isLast = (state.turnIdx + 1 >= state.scenario.turns.length);
  bar.innerHTML =
    '<div class="cv-action-row">' +
      '<button class="cv-next-btn cv-next-btn--go" id="cv-next-btn">' + (isLast ? 'Finish →' : 'Next →') + '</button>' +
    '</div>';
  document.getElementById('cv-next-btn').addEventListener('click', function() { state.turnIdx++; showTurn(); });
}

function setBarWaiting() {
  bar.innerHTML = '<div class="cv-waiting"><span></span><span></span><span></span></div>';
}

// ── Listening ──
function startListening(turn) {
  var SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRec) return;
  var btn = document.getElementById('cv-speak-btn');
  var rec = new SpeechRec();
  rec.lang = 'ja-JP'; rec.continuous = false; rec.interimResults = false; rec.maxAlternatives = 3;
  rec.onstart  = function() { if(btn){btn.textContent='🔴 Listening…';btn.disabled=true;} };
  rec.onend    = function() { if(btn){btn.textContent='🎤 Speak';btn.disabled=false;} };
  rec.onerror  = function(e) {
    if(btn){btn.textContent='🎤 Speak';btn.disabled=false;}
    if (e.error==='no-speech') {
      bar.querySelector('.cvb-task-row') && (bar.querySelector('.cvb-task-row').innerHTML = '<strong>Your turn:</strong> ' + turn.userTask + ' <span style="color:#c0392b;font-size:0.8rem">(no speech detected — try again)</span>');
    } else if (e.error==='not-allowed') {
      bar.innerHTML = '<div class="cv-warn">Mic access denied — allow microphone access in your browser and refresh.</div>';
    }
  };
  rec.onresult = function(event) {
    if(btn){btn.textContent='🎤 Speak';btn.disabled=false;}
    checkResponse(event.results[0][0].transcript, turn);
  };
  try { rec.start(); } catch(e) {}
}

// ── Check response ──
function checkResponse(transcript, turn) {
  state.attempts++;
  var matched = turn.keywords.some(function(kw) { return transcript.includes(kw); });

  if (matched) {
    state.score++;
    updateScore();
    addUserBubble(transcript, 'ok');
    setBarWaiting();
    setTimeout(function() {
      addNpcBubble(turn.successNpc, turn.successNpcEn);
      if (turn.tip) addTipBubble(turn.tip);
      setBarNext();
    }, 700);

  } else if (state.attempts >= 2) {
    addUserBubble(transcript, 'skip');
    setBarWaiting();
    setTimeout(function() {
      addNpcBubble(turn.successNpc, turn.successNpcEn);
      if (turn.tip) addTipBubble(turn.tip);
      setBarNext();
    }, 700);

  } else {
    // first fail — keep hint bubble visible, re-render speak bar with retry label
    addUserBubble(transcript, 'fail');
    setBarWaiting();
    setTimeout(function() {
      addNpcBubble(turn.failNpc, turn.failNpcEn);
      addHintBubble(turn);
      setBarRetry(turn);
    }, 700);
  }
}

function setBarRetry(turn) {
  bar.innerHTML =
    '<div class="cvb-task-row"><strong>Try again:</strong> ' + turn.userTask + '</div>' +
    '<div class="cv-action-row">' +
      (state.hasSpeech ? '<button class="cv-speak-main" id="cv-speak-btn">🎤 Speak again</button>' : '') +
      (state.hasSpeech ? '<button class="cv-type-link" id="cv-type-link">⌨ type instead</button>' : '') +
    '</div>' +
    '<div class="cv-type-row" id="cv-type-row"' + (!state.hasSpeech ? '' : ' style="display:none"') + '>' +
      '<input class="cv-type-input" type="text" id="cv-type-input" placeholder="Type in Japanese…">' +
      '<button class="cv-submit-btn" id="cv-submit-btn">Send</button>' +
    '</div>';
  if (state.hasSpeech) {
    document.getElementById('cv-speak-btn').addEventListener('click', function() { startListening(turn); });
    document.getElementById('cv-type-link').addEventListener('click', function() {
      document.getElementById('cv-type-row').style.display = 'flex';
      this.style.display = 'none';
      document.getElementById('cv-type-input').focus();
    });
  }
  var sub = document.getElementById('cv-submit-btn');
  if (sub) {
    sub.addEventListener('click', function() {
      var v = document.getElementById('cv-type-input').value.trim();
      if (v) checkResponse(v, turn);
    });
    document.getElementById('cv-type-input').addEventListener('keydown', function(e) {
      if (e.key === 'Enter' && this.value.trim()) checkResponse(this.value.trim(), turn);
    });
  }
}

// ── Speech synthesis ──
function cvSpeak(text) {
  if (!window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  var u = new SpeechSynthesisUtterance(text);
  u.lang = 'ja-JP'; u.rate = 0.82;
  window.speechSynthesis.speak(u);
}

// ── End screen ──
function showEnd() {
  main.style.display = 'none'; end.style.display = 'block';
  var total = state.scenario.turns.filter(function(t) { return !!t.userTask; }).length;
  var pct = total > 0 ? Math.round((state.score / total) * 100) : 0;
  document.getElementById('cv-end-emoji').textContent = pct >= 80 ? '🎉' : pct >= 50 ? '👍' : '💪';
  document.getElementById('cv-end-title').textContent = pct >= 80 ? '素晴らしい！ Excellent!' : pct >= 50 ? 'よくできました！ Good job!' : 'がんばって！ Keep practising!';
  document.getElementById('cv-end-score').textContent = state.score + ' / ' + total + ' correct';
  document.getElementById('cv-end-msg').textContent   = pct >= 80 ? 'You handled the whole conversation naturally. Try the other scenarios!' : pct >= 50 ? 'You got through most of it — try again to improve your score.' : 'Japanese conversations take practice. Have another go!';
}

init();
})();
</script>
