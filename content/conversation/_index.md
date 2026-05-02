---
title: "Japanese Conversation Practice — Real Scenario Roleplay"
description: "Practise speaking Japanese with real-life scenarios. Use your microphone to respond in Japanese — konbini, izakaya, asking directions, hotel check-in. Free interactive speaking practice."
date: 2025-01-01
showtoc: false
---

Pick a scenario and have a real Japanese conversation. The other character speaks — you respond out loud using your microphone. Works best in **Chrome or Edge on desktop**.

<div id="cv-selector">
  <div id="cv-no-speech" class="cv-warn" style="display:none">⚠️ Your browser doesn't support speech recognition (try Chrome or Edge on desktop). You can still practise by typing your responses instead.</div>
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
  <div id="cv-panel" class="cv-panel"></div>
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
    id: 'konbini',
    title: 'コンビニ',
    titleEn: 'Convenience Store',
    emoji: '🏪',
    desc: 'You walk into a 7-Eleven. The staff greet you and help with your purchase.',
    turns: [
      {
        npc: 'いらっしゃいませ！',
        npcEn: 'Welcome!',
        npcNote: 'The standard konbini greeting — no response needed. Just listen.',
        userTask: null
      },
      {
        npc: 'ご注文はお決まりですか？',
        npcEn: 'Have you decided what you\'d like?',
        userTask: 'Order something — ask for a rice ball and/or coffee',
        userHint: 'おにぎりとコーヒーをください',
        keywords: ['おにぎり','コーヒー','ください','ちょうだい','一つ','ひとつ','ふたつ','飲み物','食べ物','お茶'],
        successNpc: 'かしこまりました。おにぎりとコーヒーですね。',
        successNpcEn: 'Certainly. A rice ball and coffee, right?',
        failNpc: 'すみません、もう一度お願いします。',
        failNpcEn: 'Sorry, could you repeat that?'
      },
      {
        npc: 'お弁当は温めますか？',
        npcEn: 'Shall I warm up your bento?',
        userTask: 'Say yes please, or no thank you',
        userHint: 'はい、お願いします　／　いいえ、大丈夫です',
        keywords: ['はい','お願い','いいえ','大丈夫','けっこう','いいです','ええ'],
        successNpc: 'かしこまりました。',
        successNpcEn: 'Understood.',
        failNpc: 'もう一度おっしゃっていただけますか？',
        failNpcEn: 'Could you say that one more time?'
      },
      {
        npc: 'ポイントカードはお持ちですか？',
        npcEn: 'Do you have a points card?',
        userTask: 'Say you don\'t have one',
        userHint: 'いいえ、持っていません',
        keywords: ['いいえ','ない','ありません','持っていません','けっこう','ないです','いいえ'],
        successNpc: 'わかりました。お会計は680円です。',
        successNpcEn: 'Understood. Your total is 680 yen.',
        failNpc: 'ポイントカードはいかがですか？',
        failNpcEn: 'Would you like a points card?'
      },
      {
        npc: '680円です。ありがとうございます！',
        npcEn: 'That\'s 680 yen. Thank you!',
        userTask: 'Thank the staff and say goodbye',
        userHint: 'ありがとうございました！',
        keywords: ['ありがとう','どうも','また','さようなら','では','じゃあ','はい'],
        successNpc: 'ありがとうございました！またお越しくださいませ！',
        successNpcEn: 'Thank you very much! Please come again!',
        failNpc: 'またお越しくださいませ。',
        failNpcEn: 'Please come again.'
      }
    ]
  },
  {
    id: 'izakaya',
    title: '居酒屋',
    titleEn: 'Izakaya / Bar',
    emoji: '🍺',
    desc: 'You\'re at a traditional Japanese izakaya for the evening. Order drinks and food, then settle the bill.',
    turns: [
      {
        npc: 'いらっしゃいませ！何名様ですか？',
        npcEn: 'Welcome! How many people?',
        userTask: 'Tell them how many people (1 or 2)',
        userHint: '二人です　／　一人です',
        keywords: ['一人','二人','ひとり','ふたり','一名','二名','いち','に','1','2'],
        successNpc: 'ありがとうございます。こちらへどうぞ。',
        successNpcEn: 'Thank you. This way please.',
        failNpc: '何名様でしょうか？',
        failNpcEn: 'How many guests, please?'
      },
      {
        npc: 'ご注文はお決まりですか？',
        npcEn: 'Are you ready to order?',
        userTask: 'Order a beer and a snack (e.g. edamame or karaage)',
        userHint: 'ビールをふたつと枝豆をください',
        keywords: ['ビール','枝豆','唐揚げ','焼き鳥','刺身','ください','お願い','酒','サワー'],
        successNpc: 'かしこまりました！少々お待ちください。',
        successNpcEn: 'Certainly! Please wait a moment.',
        failNpc: 'ご注文はなんでしょうか？',
        failNpcEn: 'What would you like to order?'
      },
      {
        npc: 'お待たせしました！ご注文の品はお揃いでしょうか？',
        npcEn: 'Sorry for the wait! Does everything look right?',
        userTask: 'Confirm everything is here and thank them',
        userHint: 'はい、大丈夫です。ありがとうございます。',
        keywords: ['はい','大丈夫','ありがとう','いいです','そうです','揃って'],
        successNpc: 'ごゆっくりどうぞ！',
        successNpcEn: 'Please take your time!',
        failNpc: '何かご不便はありますか？',
        failNpcEn: 'Is there anything wrong?'
      },
      {
        npc: 'ご注文はよろしいでしょうか？',
        npcEn: 'Would you like to order anything else?',
        userTask: 'Ask for the bill',
        userHint: 'お会計をお願いします',
        keywords: ['お会計','会計','払う','勘定','チェック','いくら','お金','計算'],
        successNpc: 'かしこまりました。少々お待ちください。',
        successNpcEn: 'Of course. One moment please.',
        failNpc: 'もう一杯いかがですか？',
        failNpcEn: 'Would you like another drink?'
      },
      {
        npc: 'お待たせしました。3,200円になります。',
        npcEn: 'Sorry for the wait. That\'ll be 3,200 yen.',
        userTask: 'Pay and thank the staff',
        userHint: 'はい、どうぞ。ありがとうございました！',
        keywords: ['ありがとう','どうも','どうぞ','はい','また','おいしかった'],
        successNpc: 'ありがとうございました！またぜひいらしてください！',
        successNpcEn: 'Thank you very much! Please come back again!',
        failNpc: 'ありがとうございます。',
        failNpcEn: 'Thank you.'
      }
    ]
  },
  {
    id: 'directions',
    title: '道を聞く',
    titleEn: 'Asking Directions',
    emoji: '🗺️',
    desc: 'You\'re lost near the station. Stop someone on the street and ask for help.',
    turns: [
      {
        npc: '（道行く人が歩いています）',
        npcEn: '(A person is walking by)',
        npcNote: 'You need to get their attention first!',
        userTask: 'Get their attention and ask where the station is',
        userHint: 'すみません、駅はどこですか？',
        keywords: ['すみません','駅','どこ','場所','ちょっと','教えて','電車'],
        successNpc: 'あ、駅ですか。あの交差点を右に曲がってください。5分くらいです。',
        successNpcEn: 'Ah, the station? Turn right at that intersection. About 5 minutes.',
        failNpc: 'はい？',
        failNpcEn: 'Yes?'
      },
      {
        npc: 'わかりましたか？',
        npcEn: 'Did you understand?',
        userTask: 'Ask them to repeat it slowly',
        userHint: 'すみません、もう一度ゆっくりお願いします',
        keywords: ['もう一度','ゆっくり','繰り返し','もう少し','もう一回','ゆっくり'],
        successNpc: 'はい、もちろん。交差点を右に曲がって、まっすぐ行ってください。',
        successNpcEn: 'Of course. Turn right at the intersection and go straight.',
        failNpc: 'えっと、もう一度言いましょうか？',
        failNpcEn: 'Shall I say it again?'
      },
      {
        npc: '右に曲がって、まっすぐ行けばわかりますよ。',
        npcEn: 'Turn right and go straight — you\'ll see it.',
        userTask: 'Tell them you understand and thank them',
        userHint: 'はい、わかりました。ありがとうございます！',
        keywords: ['わかりました','ありがとう','了解','なるほど','わかります','はい'],
        successNpc: 'よかった！気をつけてどうぞ！',
        successNpcEn: 'Great! Take care!',
        failNpc: '大丈夫ですか？',
        failNpcEn: 'Are you okay?'
      },
      {
        npc: '気をつけてどうぞ！',
        npcEn: 'Take care!',
        userTask: 'Say thank you and goodbye',
        userHint: 'ありがとうございました！失礼します。',
        keywords: ['ありがとう','さようなら','では','じゃあ','また','失礼','どうも'],
        successNpc: 'いいえ、どういたしまして！いってらっしゃい！',
        successNpcEn: 'Not at all! Off you go!',
        failNpc: 'どういたしまして！',
        failNpcEn: 'You\'re welcome!'
      }
    ]
  },
  {
    id: 'hotel',
    title: 'ホテル',
    titleEn: 'Hotel Check-in',
    emoji: '🏨',
    desc: 'You\'ve arrived at your hotel in Japan. Check in, confirm your booking, and ask about breakfast.',
    turns: [
      {
        npc: 'いらっしゃいませ。ご予約はされていますか？',
        npcEn: 'Welcome. Do you have a reservation?',
        userTask: 'Confirm your reservation and give your name',
        userHint: 'はい、予約しています。[your name]です。',
        keywords: ['はい','予約','しています','名前','私','あります','ええ'],
        successNpc: 'ありがとうございます。お名前をいただけますか？',
        successNpcEn: 'Thank you. Could I have your name please?',
        failNpc: 'ご予約はございますか？',
        failNpcEn: 'Do you have a booking?'
      },
      {
        npc: 'ありがとうございます。シングルルーム、2泊のご予約ですね。',
        npcEn: 'Thank you. That\'s a single room for 2 nights.',
        userTask: 'Confirm that\'s correct',
        userHint: 'はい、そうです',
        keywords: ['はい','そうです','正しい','合って','間違いない','ええ','そう'],
        successNpc: 'かしこまりました。パスポートをご提示いただけますか？',
        successNpcEn: 'Understood. Could you show me your passport please?',
        failNpc: 'よろしいでしょうか？',
        failNpcEn: 'Is that correct?'
      },
      {
        npc: 'ありがとうございます。チェックアウトは午前11時です。',
        npcEn: 'Thank you. Check-out is at 11am.',
        userTask: 'Ask what time breakfast is',
        userHint: '朝食は何時からですか？',
        keywords: ['朝食','朝ごはん','朝ご飯','何時','時間','いつ','ブレックファスト','あさ'],
        successNpc: '朝食は7時から10時です。レストランは1階にございます。',
        successNpcEn: 'Breakfast is from 7am to 10am. The restaurant is on the first floor.',
        failNpc: 'ご質問はありますか？',
        failNpcEn: 'Do you have any questions?'
      },
      {
        npc: 'こちらがお部屋の鍵です。お部屋は3階でございます。',
        npcEn: 'Here is your room key. Your room is on the third floor.',
        userTask: 'Thank them and ask where the elevator is',
        userHint: 'ありがとうございます。エレベーターはどこですか？',
        keywords: ['エレベーター','どこ','ありがとう','場所','階段','エレベータ'],
        successNpc: 'エレベーターはあちらでございます。ごゆっくりお過ごしください。',
        successNpcEn: 'The elevator is over there. Please enjoy your stay.',
        failNpc: 'ご不明な点はございますか？',
        failNpcEn: 'Is there anything you need help with?'
      },
      {
        npc: 'ごゆっくりお過ごしください！',
        npcEn: 'Enjoy your stay!',
        userTask: 'Thank them warmly',
        userHint: 'ありがとうございます。よろしくお願いします。',
        keywords: ['ありがとう','どうも','よろしく','お願い','どうぞ','はい'],
        successNpc: 'どうぞよろしくお願いします！またなにかあればフロントまでどうぞ。',
        successNpcEn: 'We look forward to serving you! Come to the front desk if you need anything.',
        failNpc: 'ありがとうございます。',
        failNpcEn: 'Thank you.'
      }
    ]
  }
];

var state = { scenario: null, turnIdx: 0, score: 0, attempts: 0, hasSpeech: false };
var sel   = document.getElementById('cv-selector');
var main  = document.getElementById('cv-main');
var end   = document.getElementById('cv-end');
var cvLog = document.getElementById('cv-log');
var panel = document.getElementById('cv-panel');

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
  sel.style.display = 'block';
  main.style.display = 'none';
  end.style.display = 'none';
}

function loadScenario(id) {
  state.scenario = SCENARIOS.find(function(s) { return s.id === id; });
  state.turnIdx = 0; state.score = 0; state.attempts = 0;
  sel.style.display = 'none'; end.style.display = 'none'; main.style.display = 'block';
  document.getElementById('cv-topbar-title').textContent = state.scenario.emoji + ' ' + state.scenario.title + ' — ' + state.scenario.titleEn;
  document.getElementById('cv-scene-desc').textContent = state.scenario.desc;
  cvLog.innerHTML = '';
  updateScore();
  showTurn();
}

function updateScore() {
  var total = state.scenario.turns.filter(function(t) { return !!t.userTask; }).length;
  document.getElementById('cv-topbar-score').textContent = state.score + ' / ' + total;
}

function showTurn() {
  if (state.turnIdx >= state.scenario.turns.length) { showEnd(); return; }
  var turn = state.scenario.turns[state.turnIdx];
  state.attempts = 0;
  addBubble('npc', turn.npc, turn.npcEn, turn.npcNote || '');
  renderPanel(turn);
}

function renderPanel(turn) {
  panel.innerHTML = '';
  if (!turn.userTask) {
    panel.innerHTML =
      '<div class="cv-panel-note">' + (turn.npcNote || 'Listen carefully.') + '</div>' +
      '<div class="cv-panel-btns">' +
        '<button class="cv-hear-btn" id="cv-hear-npc">▶ Hear it</button>' +
        '<button class="cv-next-btn" id="cv-cont">Continue →</button>' +
      '</div>';
    document.getElementById('cv-hear-npc').addEventListener('click', function() { cvSpeak(turn.npc); });
    document.getElementById('cv-cont').addEventListener('click', function() { state.turnIdx++; showTurn(); });
    return;
  }

  var hasType = !state.hasSpeech;
  panel.innerHTML =
    '<div class="cv-task"><strong>Your turn:</strong> ' + turn.userTask + '</div>' +
    '<div class="cv-hint-row">' +
      '<button class="cv-hint-btn" id="cv-hint-btn">💡 Show hint</button>' +
      '<div class="cv-hint" id="cv-hint">' + turn.userHint + '</div>' +
    '</div>' +
    (state.hasSpeech
      ? '<div class="cv-speak-row">' +
          '<button class="cv-speak-btn" id="cv-speak-btn">🎤 Speak</button>' +
          '<button class="cv-type-toggle" id="cv-type-toggle">⌨ Type instead</button>' +
        '</div>'
      : '') +
    '<div class="cv-type-row" id="cv-type-row"' + (hasType ? '' : ' style="display:none"') + '>' +
      '<input class="cv-type-input" type="text" id="cv-type-input" placeholder="Type your Japanese…">' +
      '<button class="cv-submit-btn" id="cv-submit-btn">Submit</button>' +
    '</div>' +
    '<div class="cv-feedback" id="cv-feedback" style="display:none"></div>';

  document.getElementById('cv-hint-btn').addEventListener('click', function() {
    var h = document.getElementById('cv-hint');
    h.classList.toggle('open');
    this.textContent = h.classList.contains('open') ? '💡 Hide hint' : '💡 Show hint';
  });

  if (state.hasSpeech) {
    document.getElementById('cv-speak-btn').addEventListener('click', function() { startListening(turn); });
    document.getElementById('cv-type-toggle').addEventListener('click', function() {
      document.getElementById('cv-type-row').style.display = 'flex';
      this.style.display = 'none';
    });
  }

  var submitBtn = document.getElementById('cv-submit-btn');
  if (submitBtn) {
    submitBtn.addEventListener('click', function() {
      var v = document.getElementById('cv-type-input').value.trim();
      if (v) checkResponse(v, turn);
    });
    document.getElementById('cv-type-input').addEventListener('keydown', function(e) {
      if (e.key === 'Enter' && this.value.trim()) checkResponse(this.value.trim(), turn);
    });
  }
}

function startListening(turn) {
  var SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRec) return;
  var btn = document.getElementById('cv-speak-btn');
  var rec = new SpeechRec();
  rec.lang = 'ja-JP'; rec.continuous = false; rec.interimResults = false; rec.maxAlternatives = 3;
  rec.onstart = function() { btn.textContent = '🔴 Listening…'; btn.disabled = true; };
  rec.onend   = function() { btn.textContent = '🎤 Speak'; btn.disabled = false; };
  rec.onerror = function(e) {
    btn.textContent = '🎤 Speak'; btn.disabled = false;
    if (e.error === 'no-speech') showFeedback('No speech detected — try again.', 'neutral');
    else if (e.error === 'not-allowed') showFeedback('Mic access denied. Allow microphone access and try again.', 'fail');
  };
  rec.onresult = function(event) {
    btn.textContent = '🎤 Speak'; btn.disabled = false;
    checkResponse(event.results[0][0].transcript, turn);
  };
  try { rec.start(); } catch(e) {}
}

function checkResponse(transcript, turn) {
  state.attempts++;
  var matched = turn.keywords.some(function(kw) { return transcript.includes(kw); });
  var fb = document.getElementById('cv-feedback');
  fb.style.display = 'block';

  // disable inputs
  var sp = document.getElementById('cv-speak-btn'); if (sp) sp.disabled = true;
  var ti = document.getElementById('cv-type-input'); if (ti) ti.disabled = true;
  var sb = document.getElementById('cv-submit-btn'); if (sb) sb.disabled = true;

  if (matched) {
    state.score++;
    updateScore();
    fb.className = 'cv-feedback cv-fb--ok';
    fb.innerHTML = '<div class="cvf-said">You said: <strong>' + transcript + '</strong></div><div class="cvf-status">✅ Great response!</div>';
    addBubble('user', transcript, '', 'ok');
    setTimeout(function() {
      addBubble('npc', turn.successNpc, turn.successNpcEn, '');
      appendNextBtn(fb);
    }, 600);
  } else if (state.attempts >= 2) {
    fb.className = 'cv-feedback cv-fb--skip';
    fb.innerHTML = '<div class="cvf-said">You said: <strong>' + transcript + '</strong></div><div class="cvf-status">💡 Keep at it! A good answer: <strong>' + turn.userHint + '</strong></div>';
    addBubble('user', transcript, '', 'skip');
    setTimeout(function() {
      addBubble('npc', turn.successNpc, turn.successNpcEn, '');
      appendNextBtn(fb);
    }, 600);
  } else {
    fb.className = 'cv-feedback cv-fb--fail';
    fb.innerHTML = '<div class="cvf-said">You said: <strong>' + transcript + '</strong></div><div class="cvf-status">❌ Not quite — try once more.</div>';
    addBubble('user', transcript, '', 'fail');
    setTimeout(function() {
      addBubble('npc', turn.failNpc, turn.failNpcEn, '');
      // re-enable inputs for retry
      if (sp) sp.disabled = false;
      if (ti) { ti.disabled = false; ti.value = ''; ti.focus(); }
      if (sb) sb.disabled = false;
    }, 600);
  }
}

function appendNextBtn(container) {
  var btn = document.createElement('button');
  btn.className = 'cv-next-btn';
  btn.style.marginTop = '0.75rem';
  btn.textContent = state.turnIdx + 1 >= state.scenario.turns.length ? 'Finish →' : 'Next →';
  btn.addEventListener('click', function() { state.turnIdx++; showTurn(); });
  container.appendChild(btn);
}

function addBubble(speaker, jp, en, status) {
  var div = document.createElement('div');
  div.className = 'cv-bubble cv-bubble--' + speaker + (status ? ' cv-bubble--' + status : '');
  var html = '<div class="cvb-jp">' + jp + '</div>';
  if (en) html += '<div class="cvb-en">' + en + '</div>';
  if (speaker === 'npc' && jp && !jp.startsWith('（')) {
    html += '<button class="cvb-hear" onclick="(function(){' +
      'if(!window.speechSynthesis)return;' +
      'window.speechSynthesis.cancel();' +
      'var u=new SpeechSynthesisUtterance(\'' + jp.replace(/'/g,"\\'") + '\');' +
      'u.lang=\'ja-JP\';u.rate=0.82;window.speechSynthesis.speak(u);' +
    '})()">▶</button>';
    cvSpeak(jp);
  }
  div.innerHTML = html;
  cvLog.appendChild(div);
  cvLog.scrollTop = cvLog.scrollHeight;
}

function cvSpeak(text) {
  if (!window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  var u = new SpeechSynthesisUtterance(text);
  u.lang = 'ja-JP'; u.rate = 0.82;
  window.speechSynthesis.speak(u);
}

function showFeedback(msg, type) {
  var fb = document.getElementById('cv-feedback');
  if (!fb) return;
  fb.style.display = 'block';
  fb.className = 'cv-feedback cv-fb--' + type;
  fb.textContent = msg;
}

function showEnd() {
  main.style.display = 'none'; end.style.display = 'block';
  var total = state.scenario.turns.filter(function(t) { return !!t.userTask; }).length;
  var pct = total > 0 ? Math.round((state.score / total) * 100) : 0;
  document.getElementById('cv-end-emoji').textContent  = pct >= 80 ? '🎉' : pct >= 50 ? '👍' : '💪';
  document.getElementById('cv-end-title').textContent  = pct >= 80 ? '素晴らしい！ Excellent!' : pct >= 50 ? 'よくできました！ Good job!' : 'がんばって！ Keep practising!';
  document.getElementById('cv-end-score').textContent  = state.score + ' / ' + total + ' correct';
  document.getElementById('cv-end-msg').textContent    = pct >= 80 ? 'You handled the whole conversation. Try the other scenarios!' : pct >= 50 ? 'You got through most of it — try again to improve.' : 'Japanese conversations take practice. Have another go!';
}

init();
})();
</script>
