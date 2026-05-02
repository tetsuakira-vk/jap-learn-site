---
title: "Japanese Learning Phone Widgets — Scriptable Scripts for iPhone"
description: "Free Japanese learning home screen widgets for iPhone using Scriptable — word of the day, daily phrase, and kanji widgets with copy-paste scripts. Android guide included."
date: 2025-01-01
showtoc: true
---

Put Japanese on your home screen. These widgets show a new word or phrase every day — glance at your phone, absorb a little Japanese, build a habit without thinking about it.

---

## iPhone — Scriptable Widgets

**[Scriptable](https://scriptable.app)** is a free iOS app that lets you run JavaScript on your iPhone or iPad and display the output as a home screen widget. All the scripts below are free — copy, paste, done.

### Setup (do this once)

1. Download **[Scriptable](https://apps.apple.com/gb/app/scriptable/id1405459188)** from the App Store — it's free
2. Open Scriptable, tap **+** in the top right to create a new script
3. Paste the script you want (see below), tap the script name to rename it, then tap **Done**
4. Long-press your home screen → tap **+** → search **Scriptable**
5. Choose **Small** size, tap **Add Widget**
6. Long-press the widget → **Edit Widget** → set **Script** to the one you just saved
7. Set **When Interacting** to **Run Script** — done

---

### Script 1 — Word of the Day

Shows one Japanese word per day — kanji, reading, and English meaning. Same word all day, different word each morning.

```javascript
// Japanese Word of the Day — japaneseunlocked.com
// Scriptable small widget

const WORDS = [
  {jp:"水",rd:"みず",en:"water"},{jp:"火",rd:"ひ",en:"fire"},
  {jp:"山",rd:"やま",en:"mountain"},{jp:"川",rd:"かわ",en:"river"},
  {jp:"木",rd:"き",en:"tree / wood"},{jp:"空",rd:"そら",en:"sky"},
  {jp:"海",rd:"うみ",en:"sea / ocean"},{jp:"雨",rd:"あめ",en:"rain"},
  {jp:"風",rd:"かぜ",en:"wind"},{jp:"花",rd:"はな",en:"flower"},
  {jp:"鳥",rd:"とり",en:"bird"},{jp:"犬",rd:"いぬ",en:"dog"},
  {jp:"猫",rd:"ねこ",en:"cat"},{jp:"魚",rd:"さかな",en:"fish"},
  {jp:"食べる",rd:"たべる",en:"to eat"},{jp:"飲む",rd:"のむ",en:"to drink"},
  {jp:"見る",rd:"みる",en:"to see"},{jp:"聞く",rd:"きく",en:"to listen"},
  {jp:"話す",rd:"はなす",en:"to speak"},{jp:"行く",rd:"いく",en:"to go"},
  {jp:"来る",rd:"くる",en:"to come"},{jp:"帰る",rd:"かえる",en:"to go home"},
  {jp:"寝る",rd:"ねる",en:"to sleep"},{jp:"起きる",rd:"おきる",en:"to wake up"},
  {jp:"大きい",rd:"おおきい",en:"big"},{jp:"小さい",rd:"ちいさい",en:"small"},
  {jp:"新しい",rd:"あたらしい",en:"new"},{jp:"古い",rd:"ふるい",en:"old"},
  {jp:"高い",rd:"たかい",en:"tall / expensive"},{jp:"安い",rd:"やすい",en:"cheap"},
  {jp:"おいしい",rd:"おいしい",en:"delicious"},{jp:"楽しい",rd:"たのしい",en:"fun"},
  {jp:"難しい",rd:"むずかしい",en:"difficult"},{jp:"今日",rd:"きょう",en:"today"},
  {jp:"明日",rd:"あした",en:"tomorrow"},{jp:"昨日",rd:"きのう",en:"yesterday"},
  {jp:"学校",rd:"がっこう",en:"school"},{jp:"家",rd:"いえ",en:"home"},
  {jp:"電車",rd:"でんしゃ",en:"train"},{jp:"友達",rd:"ともだち",en:"friend"},
  {jp:"先生",rd:"せんせい",en:"teacher"},{jp:"本",rd:"ほん",en:"book"},
  {jp:"お金",rd:"おかね",en:"money"},{jp:"時間",rd:"じかん",en:"time"},
  {jp:"名前",rd:"なまえ",en:"name"},{jp:"言葉",rd:"ことば",en:"word / language"},
  {jp:"勉強",rd:"べんきょう",en:"study"},{jp:"日本語",rd:"にほんご",en:"Japanese"},
  {jp:"心",rd:"こころ",en:"heart / mind"},{jp:"夢",rd:"ゆめ",en:"dream"},
];

const d = new Date();
const seed = d.getFullYear() * 10000 + (d.getMonth()+1) * 100 + d.getDate();
const word = WORDS[seed % WORDS.length];

const w = new ListWidget();
w.backgroundColor = new Color("#0e0e10");
w.setPadding(14, 16, 12, 16);

const lbl = w.addText("WORD OF THE DAY");
lbl.font = Font.boldSystemFont(7);
lbl.textColor = new Color("#c0392b");
lbl.leftAlignText();

w.addSpacer(8);

const jp = w.addText(word.jp);
jp.font = Font.boldSystemFont(42);
jp.textColor = Color.white();
jp.leftAlignText();
jp.minimumScaleFactor = 0.4;

const rd = w.addText(word.rd);
rd.font = Font.systemFont(13);
rd.textColor = new Color("#ffffff80");
rd.leftAlignText();

w.addSpacer(6);

const en = w.addText(word.en);
en.font = Font.mediumSystemFont(15);
en.textColor = Color.white();
en.leftAlignText();

w.addSpacer();

const foot = w.addText("japaneseunlocked.com");
foot.font = Font.systemFont(7);
foot.textColor = new Color("#ffffff30");
foot.leftAlignText();

Script.setWidget(w);
Script.complete();
if (config.runsInApp) w.presentSmall();
```

---

### Script 2 — Phrase of the Day

Shows a full Japanese phrase each day — Japanese, romaji, and English. Good for a medium widget so the longer phrases don't get cut off.

```javascript
// Japanese Phrase of the Day — japaneseunlocked.com
// Works best as a medium widget

const PHRASES = [
  {jp:"ありがとうございます",rd:"arigatou gozaimasu",en:"Thank you very much"},
  {jp:"すみません",rd:"sumimasen",en:"Excuse me / Sorry"},
  {jp:"おはようございます",rd:"ohayou gozaimasu",en:"Good morning"},
  {jp:"こんにちは",rd:"konnichiwa",en:"Hello / Good afternoon"},
  {jp:"こんばんは",rd:"konbanwa",en:"Good evening"},
  {jp:"おやすみなさい",rd:"oyasuminasai",en:"Good night"},
  {jp:"はじめまして",rd:"hajimemashite",en:"Nice to meet you"},
  {jp:"よろしくお願いします",rd:"yoroshiku onegaishimasu",en:"Please look after me"},
  {jp:"いただきます",rd:"itadakimasu",en:"(said before eating)"},
  {jp:"ごちそうさまでした",rd:"gochisousama deshita",en:"Thanks for the meal"},
  {jp:"大丈夫ですか？",rd:"daijoubu desu ka?",en:"Are you okay?"},
  {jp:"わかりません",rd:"wakarimasen",en:"I don't understand"},
  {jp:"もう一度お願いします",rd:"mou ichido onegaishimasu",en:"Please say that again"},
  {jp:"トイレはどこですか？",rd:"toire wa doko desu ka?",en:"Where is the bathroom?"},
  {jp:"いくらですか？",rd:"ikura desu ka?",en:"How much is it?"},
  {jp:"これをください",rd:"kore wo kudasai",en:"I'll have this please"},
  {jp:"日本語を勉強しています",rd:"nihongo wo benkyou shite imasu",en:"I'm studying Japanese"},
  {jp:"少し日本語が話せます",rd:"sukoshi nihongo ga hanasemasu",en:"I can speak a little Japanese"},
  {jp:"頑張ってください",rd:"ganbatte kudasai",en:"Good luck / Do your best"},
  {jp:"お疲れ様でした",rd:"otsukaresama deshita",en:"Good work / Well done"},
  {jp:"気をつけてください",rd:"ki wo tsukete kudasai",en:"Please take care"},
  {jp:"また明日",rd:"mata ashita",en:"See you tomorrow"},
  {jp:"どうぞよろしく",rd:"douzo yoroshiku",en:"Nice to meet you (casual)"},
  {jp:"ちょっと待ってください",rd:"chotto matte kudasai",en:"Please wait a moment"},
];

const d = new Date();
const seed = d.getFullYear() * 10000 + (d.getMonth()+1) * 100 + d.getDate();
const phrase = PHRASES[seed % PHRASES.length];

const w = new ListWidget();
w.backgroundColor = new Color("#0e0e10");
w.setPadding(14, 16, 12, 16);

const lbl = w.addText("PHRASE OF THE DAY");
lbl.font = Font.boldSystemFont(7);
lbl.textColor = new Color("#c0392b");
lbl.leftAlignText();

w.addSpacer(10);

const jp = w.addText(phrase.jp);
jp.font = Font.boldSystemFont(20);
jp.textColor = Color.white();
jp.leftAlignText();
jp.minimumScaleFactor = 0.5;

w.addSpacer(4);

const rd = w.addText(phrase.rd);
rd.font = Font.italicSystemFont(12);
rd.textColor = new Color("#ffffff55");
rd.leftAlignText();

w.addSpacer(6);

const en = w.addText(phrase.en);
en.font = Font.mediumSystemFont(14);
en.textColor = new Color("#ffffffcc");
en.leftAlignText();

w.addSpacer();

const foot = w.addText("japaneseunlocked.com");
foot.font = Font.systemFont(7);
foot.textColor = new Color("#ffffff30");
foot.leftAlignText();

Script.setWidget(w);
Script.complete();
if (config.runsInApp) w.presentMedium();
```

---

### Script 3 — Random Kanji Drill

Tap the widget to cycle to a new kanji. Good for a small corner widget — see a kanji, try to recall the meaning, glance at the answer.

```javascript
// Japanese Kanji Drill — japaneseunlocked.com
// Small widget — shows a new kanji each day

const KANJI = [
  {k:"日",on:"ニチ",kun:"ひ",en:"sun / day"},
  {k:"月",on:"ゲツ",kun:"つき",en:"moon / month"},
  {k:"火",on:"カ",kun:"ひ",en:"fire"},
  {k:"水",on:"スイ",kun:"みず",en:"water"},
  {k:"木",on:"モク",kun:"き",en:"tree"},
  {k:"金",on:"キン",kun:"かね",en:"gold / money"},
  {k:"土",on:"ド",kun:"つち",en:"earth / soil"},
  {k:"山",on:"サン",kun:"やま",en:"mountain"},
  {k:"川",on:"セン",kun:"かわ",en:"river"},
  {k:"田",on:"デン",kun:"た",en:"rice field"},
  {k:"人",on:"ジン",kun:"ひと",en:"person"},
  {k:"口",on:"コウ",kun:"くち",en:"mouth"},
  {k:"手",on:"シュ",kun:"て",en:"hand"},
  {k:"目",on:"モク",kun:"め",en:"eye"},
  {k:"耳",on:"ジ",kun:"みみ",en:"ear"},
  {k:"足",on:"ソク",kun:"あし",en:"foot / leg"},
  {k:"力",on:"リョク",kun:"ちから",en:"power / strength"},
  {k:"大",on:"ダイ",kun:"おお",en:"big / large"},
  {k:"小",on:"ショウ",kun:"ちい",en:"small"},
  {k:"中",on:"チュウ",kun:"なか",en:"inside / middle"},
  {k:"上",on:"ジョウ",kun:"うえ",en:"above / up"},
  {k:"下",on:"カ",kun:"した",en:"below / down"},
  {k:"左",on:"サ",kun:"ひだり",en:"left"},
  {k:"右",on:"ウ",kun:"みぎ",en:"right"},
  {k:"本",on:"ホン",kun:"もと",en:"book / origin"},
  {k:"国",on:"コク",kun:"くに",en:"country"},
  {k:"年",on:"ネン",kun:"とし",en:"year"},
  {k:"円",on:"エン",kun:"まる",en:"yen / circle"},
  {k:"学",on:"ガク",kun:"まな",en:"study / learn"},
  {k:"生",on:"セイ",kun:"いき",en:"life / birth"},
];

const d = new Date();
const seed = d.getFullYear() * 10000 + (d.getMonth()+1) * 100 + d.getDate();
const kanji = KANJI[seed % KANJI.length];

const w = new ListWidget();
w.backgroundColor = new Color("#0e0e10");
w.setPadding(12, 14, 10, 14);

const lbl = w.addText("KANJI");
lbl.font = Font.boldSystemFont(7);
lbl.textColor = new Color("#c0392b");
lbl.leftAlignText();

w.addSpacer(4);

const k = w.addText(kanji.k);
k.font = Font.boldSystemFont(52);
k.textColor = Color.white();
k.leftAlignText();
k.minimumScaleFactor = 0.4;

const readings = w.addText(kanji.on + " · " + kanji.kun);
readings.font = Font.systemFont(10);
readings.textColor = new Color("#ffffff60");
readings.leftAlignText();

w.addSpacer(3);

const en = w.addText(kanji.en);
en.font = Font.mediumSystemFont(13);
en.textColor = Color.white();
en.leftAlignText();

w.addSpacer();

const foot = w.addText("japaneseunlocked.com");
foot.font = Font.systemFont(7);
foot.textColor = new Color("#ffffff30");
foot.leftAlignText();

Script.setWidget(w);
Script.complete();
if (config.runsInApp) w.presentSmall();
```

---

## Android — What Are the Options?

Android doesn't have a clean equivalent to Scriptable. Here's the honest breakdown:

**Option 1 — Tasker** (paid, ~£3)
The most powerful automation app on Android. You can write scripts that update a widget with new Japanese content daily. It's capable but has a steep learning curve — not beginner-friendly. If you're already a Tasker user, it can do everything the Scriptable widgets above do.

**Option 2 — KWGT Kustom Widget**
Good for beautiful static widgets but doesn't support fetching or cycling content via JavaScript. Not suitable for a "word of the day" without Tasker feeding it data.

**Option 3 — Home Screen Shortcut (simple, free)**
The easiest option: add a home screen shortcut directly to [japaneseunlocked.com](/) or a specific page like the [vocabulary list](/vocab/) or [phrases page](/phrases/). Open your browser, navigate to the page, tap the share button → **Add to Home Screen**. Not a widget but it's one tap away and always up to date.

Android widget support is something we're looking into — if you want to be notified when an Android version drops, [sign up for the word-of-the-day email](/resources/) and we'll announce it there.

---

## Tips for Getting the Most Out of the Widgets

- **Small widget** works best for Word of the Day and Kanji Drill — put it on your lock screen or in a corner
- **Medium widget** is better for Phrase of the Day so longer phrases don't get truncated
- The scripts use the **date as a seed** so you see the same entry all day, and a fresh one each morning
- To add more words: extend the `WORDS` / `PHRASES` / `KANJI` arrays at the top of the script — any object with the same keys will work
- Combine with the [Vocabulary pages](/vocab/) — if you see a word you don't recognise, tap through to look it up
