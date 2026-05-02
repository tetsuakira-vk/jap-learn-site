---
title: "About"
description: "About Japanese Unlocked — a free Japanese learning site with interactive quizzes, audio charts, and study guides for hiragana, katakana, kanji, and JLPT. Built alongside the YouTube channel."
date: 2025-01-01
---

## About this site

A free Japanese learning site built to go alongside the YouTube channel. The goal is simple: give you interactive tools — quizzes, reference charts, audio — that make drilling hiragana, katakana, kanji, and grammar actually enjoyable.

Everything here is free. No account. No ads.

[Watch on YouTube →](https://www.youtube.com/@JapaneseLearning-z2x)

---

## What's inside

- **Hiragana & Katakana** — full reference charts, click any character to hear it, then drill with the quiz
- **Kanji** — 50 essential characters with on'yomi and kun'yomi readings
- **JLPT N5 → N1** — vocabulary lists and quizzes for every level, with audio
- **Grammar** — particles explained properly, verb conjugation tables, 50+ sentence patterns with examples
- **Phrases** — real sentences broken into categories, all with audio
- **Numbers** — counting to 10,000 with audio
- **Word of the Day** — a new phrase every day on the homepage

---

## Why Japanese is worth learning

Japanese is spoken by around 125 million people, almost entirely within Japan — which makes it one of the few major world languages where learning it gives you nearly exclusive access to an entire culture.

Reading it unlocks manga in the original, films without subtitles, games that never get translated, and conversations that simply don't exist in English. Japan has one of the richest literary and artistic traditions in the world, and most of it sits behind the language barrier.

It's also just a genuinely fascinating language to learn. Three writing systems. Verb-final sentences. Politeness built into the grammar. Thousands of words borrowed from Chinese, English, Portuguese, and Dutch. Pitch accent that changes meaning. Once it starts clicking, it's hard to stop.

---

## Is Japanese hard?

For native English speakers, honestly — yes, it takes time. The Foreign Service Institute rates it one of the hardest languages for English speakers, estimating around 2,200 hours to professional proficiency. But that number assumes you're doing it inefficiently.

The truth is that hiragana and katakana can be learned in a week or two. Basic conversation opens up within a few months. Reading simple manga becomes possible around the N4 level. Each milestone is tangible and rewarding.

The trick is consistency over intensity. Twenty minutes a day for a year beats a week-long cramming session every few months.

---

## Recommended order

If you're starting from zero:

1. **Hiragana first** — the core phonetic alphabet. Takes about a week with daily practice.
2. **Katakana second** — same sounds, different shapes. Used for foreign loanwords.
3. **Basic grammar** — particles and verb forms. These unlock how sentences actually work.
4. **N5 vocabulary** — the 800 most common words. Learn alongside the YouTube lessons.
5. **Phrases and sentences** — start using real Japanese as early as possible.
6. **Kanji gradually** — don't try to front-load kanji. Pick them up as you encounter them in vocabulary.

---

## A note on the writing systems

Japanese uses three scripts simultaneously, which is the thing that looks most intimidating from the outside:

| Script | Characters | Used for |
|--------|-----------|---------|
| **ひらがな** Hiragana | 46 | Native Japanese words, grammar |
| **カタカナ** Katakana | 46 | Foreign loanwords, emphasis, sound effects |
| **漢字** Kanji | 2,136 (daily use) | Meaning-carrying words, names |

A typical Japanese sentence mixes all three. Once you can read hiragana and katakana, you can sound out any Japanese text even without knowing what it means — which is a huge first step.

---

## Get in touch

Questions, suggestions, or just want to say hi — use the form below.

<form id="contact-form" class="contact-form" novalidate>
  <div class="cf-row">
    <label class="cf-label" for="cf-name">Name</label>
    <input class="cf-input" type="text" id="cf-name" name="name" placeholder="Your name" required>
  </div>
  <div class="cf-row">
    <label class="cf-label" for="cf-email">Email</label>
    <input class="cf-input" type="email" id="cf-email" name="email" placeholder="your@email.com" required>
  </div>
  <div class="cf-row">
    <label class="cf-label" for="cf-message">Message</label>
    <textarea class="cf-input cf-textarea" id="cf-message" name="message" placeholder="Your message…" rows="5" required></textarea>
  </div>
  <input type="checkbox" name="botcheck" style="display:none">
  <div id="cf-msg"></div>
  <button type="submit" class="cf-submit" id="cf-btn">Send message</button>
</form>

<script>
(function() {
  var form = document.getElementById('contact-form');
  var btn  = document.getElementById('cf-btn');
  var msg  = document.getElementById('cf-msg');
  if (!form) return;
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    btn.disabled = true;
    btn.textContent = 'Sending…';
    msg.className = '';
    msg.textContent = '';
    var data = {
      access_key: '61150fb6-a3d6-44ca-b5f2-b323b8a59f1b',
      name: document.getElementById('cf-name').value,
      email: document.getElementById('cf-email').value,
      message: document.getElementById('cf-message').value
    };
    fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(data)
    })
    .then(function(r) { return r.json(); })
    .then(function(res) {
      if (res.success) {
        msg.className = 'cf-msg cf-msg--ok';
        msg.textContent = 'Message sent — thanks! I\'ll get back to you soon.';
        form.reset();
      } else {
        throw new Error(res.message || 'Error');
      }
    })
    .catch(function() {
      msg.className = 'cf-msg cf-msg--err';
      msg.textContent = 'Something went wrong. Please try again or email directly.';
    })
    .finally(function() {
      btn.disabled = false;
      btn.textContent = 'Send message';
    });
  });
})();
</script>
