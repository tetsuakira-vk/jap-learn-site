/**
 * Language Learning Curve — Japanese Edition
 * Pure client-side · No dependencies except Chart.js (CDN)
 *
 * ─────────────────────────────────────────────────────────────
 * LANGUAGE CONFIG
 * To adapt this tool for another language, swap this config
 * object with different level names, word counts, and labels.
 * ─────────────────────────────────────────────────────────────
 */
const LANG_CONFIG = {
  name: 'Japanese',
  levels: [
    { id: 'N5',            label: 'N5',          words: 800,   color: '#27ae60', desc: 'Survival basics, tourism' },
    { id: 'Conversational',label: 'Conversational',words: 2000, color: '#f39c12', desc: 'Everyday conversation' },
    { id: 'N4',            label: 'N4',          words: 1500,  color: '#2ecc71', desc: 'Daily situations, basic kanji' },
    { id: 'N3',            label: 'N3',          words: 3750,  color: '#3498db', desc: 'Intermediate, simple manga' },
    { id: 'N2',            label: 'N2',          words: 6000,  color: '#9b59b6', desc: 'Workplace-ready, news' },
    { id: 'Fluent',        label: 'Fluent',      words: 8000,  color: '#e67e22', desc: 'Near-native comprehension' },
    { id: 'N1',            label: 'N1',          words: 10000, color: '#c0392b', desc: 'Near-native, literary' },
  ],
  // Comprehension model: word counts for 95% / 98% coverage
  coverage95: 2000,
  coverage98: 8000,
  // Comprehension context-specific word thresholds
  comprehensionContexts: [
    { label: 'Casual conversation', coverage95: 2000, coverage98: 4000 },
    { label: 'Manga / simple text', coverage95: 3000, coverage98: 6000 },
    { label: 'News articles',       coverage95: 5000, coverage98: 8000 },
    { label: 'Novels',              coverage95: 7000, coverage98: 10000 },
  ],
};

/* ──────────────────────────────────────────
   CHART.JS GLOBAL DEFAULTS (dark theme)
   ────────────────────────────────────────── */
Chart.defaults.color = '#9999aa';
Chart.defaults.borderColor = 'rgba(255,255,255,0.07)';
Chart.defaults.font.family = "'Inter','Segoe UI',system-ui,sans-serif";

/* ──────────────────────────────────────────
   HELPERS
   ────────────────────────────────────────── */
const $ = id => document.getElementById(id);

function lerp(a, b, t) { return a + (b - a) * t; }

/**
 * Ebbinghaus retention model
 * R = e^(-t / stability)
 */
function retention(t, stability) {
  return Math.exp(-t / stability);
}

/**
 * SM-2 simplified: returns array of {day, stability, retention%}
 * for each review in the sequence. easeFactor default 2.5.
 */
function sm2Schedule(reviews = 6, easeFactor = 2.5) {
  const schedule = [];
  let day = 0;
  let stability = 1; // days until ~37% retention after first exposure

  for (let i = 0; i < reviews; i++) {
    day = i === 0 ? 1 : Math.round(day * easeFactor);
    stability = day * 1.4; // stability ≈ 1.4× interval after success
    schedule.push({
      review: i + 1,
      day,
      stability: parseFloat(stability.toFixed(1)),
      retention: parseFloat((retention(day * 0.8, stability) * 100).toFixed(1)),
    });
  }
  return schedule;
}

/**
 * Consistency multiplier — study irregularity penalty.
 * 7 days/week = 1.0; lower = sub-linear efficiency loss.
 */
function consistencyMultiplier(daysPerWeek) {
  return 0.4 + (daysPerWeek / 7) * 0.6;
}

/**
 * Daily new words acquirable given study time and consistency.
 * ~20 min per solid new word (conservative; context input can improve this).
 */
function dailyNewWords(studyMinutes, daysPerWeek) {
  const cm = consistencyMultiplier(daysPerWeek);
  return (studyMinutes * cm) / 20;
}

/**
 * Months needed to go from currentVocab to targetVocab.
 * Returns null if already there.
 */
function monthsToVocab(currentVocab, targetVocab, wordsPerDay) {
  if (currentVocab >= targetVocab) return 0;
  const daysNeeded = (targetVocab - currentVocab) / wordsPerDay;
  return daysNeeded / 30.4;
}

/**
 * Logarithmic comprehension estimate (Nation/Laufer model).
 * Returns 0–98 (%).
 */
function comprehensionPct(vocab, coverageMax = 8000) {
  if (vocab <= 0) return 0;
  const pct = (Math.log(vocab + 1) / Math.log(coverageMax + 1)) * 98;
  return Math.min(98, parseFloat(pct.toFixed(1)));
}

/** Level classification from vocabulary size */
function levelFromVocab(vocab) {
  const sorted = [...LANG_CONFIG.levels].sort((a, b) => a.words - b.words);
  let current = sorted[0];
  for (const lv of sorted) {
    if (vocab >= lv.words) current = lv;
  }
  return current;
}

/** Format months nicely */
function fmtMonths(m) {
  if (m <= 0) return '✓ Done';
  if (m < 1) return '< 1 mo';
  if (m < 24) return `${Math.round(m)} mo`;
  return `${(m / 12).toFixed(1)} yr`;
}

/* ──────────────────────────────────────────
   CHART INSTANCES (kept for destroy/remake)
   ────────────────────────────────────────── */
let charts = {};

function destroyCharts() {
  for (const k in charts) {
    if (charts[k]) { charts[k].destroy(); charts[k] = null; }
  }
}

/* ──────────────────────────────────────────
   CHART 1 — FORGETTING CURVE
   ────────────────────────────────────────── */
function buildForgettingChart() {
  const days = Array.from({length: 31}, (_, i) => i);
  const noReview  = days.map(d => parseFloat((retention(d, 1.5) * 100).toFixed(2)));
  const withSR    = [];
  // Simulate stepped SR: each review bumps stability
  let stab = 1.5;
  let reviewDays = [1, 3, 7, 14, 30];
  for (const d of days) {
    if (reviewDays.includes(d)) stab *= 2.5;
    withSR.push(parseFloat((retention(d > 0 ? d : 0.01, stab) * 100).toFixed(2)));
  }
  // Clamp to 100
  withSR[0] = 100; noReview[0] = 100;

  const ctx = $('forgettingChart').getContext('2d');
  charts.forgetting = new Chart(ctx, {
    type: 'line',
    data: {
      labels: days,
      datasets: [
        {
          label: 'Without review',
          data: noReview,
          borderColor: '#e74c3c',
          backgroundColor: 'rgba(231,76,60,0.08)',
          borderWidth: 2.5,
          tension: 0.4,
          fill: true,
          pointRadius: 0,
        },
        {
          label: 'With spaced repetition',
          data: withSR,
          borderColor: '#27ae60',
          backgroundColor: 'rgba(39,174,96,0.08)',
          borderWidth: 2.5,
          tension: 0.4,
          fill: true,
          pointRadius: days.map(d => [1,3,7,14,30].includes(d) ? 5 : 0),
          pointBackgroundColor: '#27ae60',
          pointBorderColor: '#0d0d0f',
          pointBorderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 900, easing: 'easeOutQuart' },
      plugins: {
        legend: { position: 'top', labels: { padding: 20, usePointStyle: true } },
        tooltip: {
          callbacks: {
            label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y.toFixed(1)}%`,
            title: ctx => `Day ${ctx[0].label}`,
          },
        },
      },
      scales: {
        x: {
          title: { display: true, text: 'Days since learning', padding: {top:8} },
          grid: { color: 'rgba(255,255,255,0.04)' },
        },
        y: {
          min: 0, max: 100,
          title: { display: true, text: 'Retention (%)' },
          grid: { color: 'rgba(255,255,255,0.04)' },
          ticks: { callback: v => `${v}%` },
        },
      },
    },
  });
}

/* ──────────────────────────────────────────
   CHART 2 — VOCABULARY PROJECTION
   ────────────────────────────────────────── */
function buildVocabChart(currentVocab, studyMinutes, daysPerWeek) {
  const months = Array.from({length: 61}, (_, i) => i);
  const base = dailyNewWords(studyMinutes, daysPerWeek);
  const opt  = base * 1.2;
  const pes  = base * 0.8;

  function projectVocab(wordsPerDay) {
    return months.map(m => Math.round(currentVocab + wordsPerDay * m * 30.4));
  }

  const central    = projectVocab(base);
  const optimistic = projectVocab(opt);
  const pessimistic= projectVocab(pes);

  const ctx = $('vocabChart').getContext('2d');

  // Level threshold annotations
  const levelLines = LANG_CONFIG.levels
    .filter(l => l.words > currentVocab)
    .sort((a, b) => a.words - b.words);

  const levelColors = {
    N5: '#27ae60', N4: '#2ecc71', N3: '#3498db',
    N2: '#9b59b6', N1: '#c0392b', Conversational: '#f39c12', Fluent: '#e67e22',
  };

  // Band dataset (optimistic - pessimistic as fill)
  charts.vocab = new Chart(ctx, {
    type: 'line',
    data: {
      labels: months,
      datasets: [
        {
          label: 'Optimistic',
          data: optimistic,
          borderColor: 'rgba(39,174,96,0.6)',
          backgroundColor: 'rgba(39,174,96,0.1)',
          borderWidth: 1.5,
          borderDash: [5,4],
          tension: 0.3,
          fill: '+1',
          pointRadius: 0,
        },
        {
          label: 'Central estimate',
          data: central,
          borderColor: '#c0392b',
          backgroundColor: 'rgba(192,57,43,0.08)',
          borderWidth: 3,
          tension: 0.3,
          fill: false,
          pointRadius: months.map(m => m === 0 ? 6 : 0),
          pointBackgroundColor: '#c0392b',
        },
        {
          label: 'Pessimistic',
          data: pessimistic,
          borderColor: 'rgba(39,174,96,0.3)',
          backgroundColor: 'rgba(39,174,96,0.05)',
          borderWidth: 1.5,
          borderDash: [5,4],
          tension: 0.3,
          fill: false,
          pointRadius: 0,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 1200, easing: 'easeOutQuart' },
      plugins: {
        legend: {
          position: 'top',
          labels: { padding: 20, usePointStyle: true },
        },
        tooltip: {
          callbacks: {
            label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y.toLocaleString()} words`,
            title: ctx => `Month ${ctx[0].label}`,
          },
        },
        annotation: undefined,
      },
      scales: {
        x: {
          title: { display: true, text: 'Months from now' },
          grid: { color: 'rgba(255,255,255,0.04)' },
          ticks: { callback: v => v % 12 === 0 ? `${v}m` : v % 6 === 0 ? v : '' },
        },
        y: {
          title: { display: true, text: 'Total vocabulary' },
          grid: { color: 'rgba(255,255,255,0.04)' },
          ticks: { callback: v => v >= 1000 ? `${(v/1000).toFixed(0)}k` : v },
        },
      },
    },
    plugins: [{
      id: 'levelLines',
      afterDraw(chart) {
        const { ctx: c, scales: { x, y } } = chart;
        const chartArea = chart.chartArea;
        levelLines.forEach(lv => {
          const yPos = y.getPixelForValue(lv.words);
          if (yPos < chartArea.top || yPos > chartArea.bottom) return;
          c.save();
          c.strokeStyle = levelColors[lv.id] || '#ffffff';
          c.globalAlpha = 0.5;
          c.lineWidth = 1;
          c.setLineDash([6, 4]);
          c.beginPath();
          c.moveTo(chartArea.left, yPos);
          c.lineTo(chartArea.right, yPos);
          c.stroke();
          c.globalAlpha = 0.85;
          c.fillStyle = levelColors[lv.id] || '#ffffff';
          c.font = 'bold 10px Inter,sans-serif';
          c.fillText(`${lv.label} (${(lv.words/1000).toFixed(lv.words<1000?0:1)}k)`, chartArea.left + 6, yPos - 4);
          c.restore();
        });
      },
    }],
  });
}

/* ──────────────────────────────────────────
   CHART 3 — TIME TO TARGET
   ────────────────────────────────────────── */
function buildTimeChart(currentVocab, studyMinutes, daysPerWeek, targetId) {
  const base = dailyNewWords(studyMinutes, daysPerWeek);
  const opt  = base * 1.2;

  const sorted = [...LANG_CONFIG.levels].sort((a, b) => a.words - b.words);

  const labels   = [];
  const realistic= [];
  const optimistic=[];
  const colors   = [];

  for (const lv of sorted) {
    labels.push(lv.label);
    const r = monthsToVocab(currentVocab, lv.words, base);
    const o = monthsToVocab(currentVocab, lv.words, opt);
    realistic.push(Math.max(0, parseFloat(r.toFixed(1))));
    optimistic.push(Math.max(0, parseFloat(o.toFixed(1))));

    if (currentVocab >= lv.words) colors.push('#27ae60');        // achieved
    else if (lv.id === targetId)   colors.push('#2980b9');       // target
    else                            colors.push('#3a3a4a');       // beyond
  }

  const ctx = $('timeChart').getContext('2d');
  charts.time = new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [
        {
          label: 'Realistic estimate (months)',
          data: realistic,
          backgroundColor: colors.map(c => c + 'cc'),
          borderColor: colors,
          borderWidth: 1.5,
          borderRadius: 6,
        },
        {
          label: 'Optimistic estimate (months)',
          data: optimistic,
          backgroundColor: colors.map(c => c + '44'),
          borderColor: colors.map(c => c + '88'),
          borderWidth: 1.5,
          borderRadius: 6,
          borderDash: [4,3],
        },
      ],
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 900, easing: 'easeOutQuart' },
      plugins: {
        legend: { position: 'top', labels: { padding: 20, usePointStyle: true } },
        tooltip: {
          callbacks: {
            label: ctx => {
              const v = ctx.parsed.x;
              return ` ${ctx.dataset.label}: ${v <= 0 ? '✓ Already achieved' : fmtMonths(v)}`;
            },
          },
        },
      },
      scales: {
        x: {
          title: { display: true, text: 'Months from now' },
          grid: { color: 'rgba(255,255,255,0.04)' },
          ticks: { callback: v => v === 0 ? 'Now' : `${v}m` },
        },
        y: {
          grid: { display: false },
        },
      },
    },
  });
}

/* ──────────────────────────────────────────
   CHART 4 — COMPREHENSION DONUT
   ────────────────────────────────────────── */
function buildComprehensionChart(vocab) {
  const contexts = LANG_CONFIG.comprehensionContexts;
  const values   = contexts.map(c => {
    return parseFloat(comprehensionPct(vocab, c.coverage98).toFixed(1));
  });

  const convPct = values[0];
  $('donut-pct').textContent = `${convPct}%`;

  const palette = ['#c0392b', '#9b59b6', '#3498db', '#27ae60'];

  const ctx = $('compChart').getContext('2d');
  charts.comp = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: contexts.map(c => c.label),
      datasets: [{
        data: values,
        backgroundColor: palette.map(c => c + 'cc'),
        borderColor: palette,
        borderWidth: 2,
        hoverOffset: 8,
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      cutout: '68%',
      animation: { duration: 1000, easing: 'easeOutQuart' },
      plugins: {
        legend: {
          position: 'right',
          labels: {
            padding: 16,
            usePointStyle: true,
            generateLabels: chart => {
              const data = chart.data;
              return data.labels.map((label, i) => ({
                text: `${label} — ${data.datasets[0].data[i]}%`,
                fillStyle: data.datasets[0].backgroundColor[i],
                strokeStyle: data.datasets[0].borderColor[i],
                hidden: false,
                index: i,
              }));
            },
          },
        },
        tooltip: {
          callbacks: {
            label: ctx => ` Comprehension: ${ctx.parsed}%`,
          },
        },
      },
    },
  });
}

/* ──────────────────────────────────────────
   CHART 5 — SPACED REPETITION SCHEDULE
   ────────────────────────────────────────── */
function buildSRSection() {
  const schedule = sm2Schedule(6);

  // Build visual grid
  const grid = $('sr-grid');
  grid.innerHTML = '';

  // First: show initial learning cell
  const learnCell = document.createElement('div');
  learnCell.className = 'sr-cell';
  learnCell.innerHTML = `
    <div class="sr-review-num">Day 0 — Learn</div>
    <div class="sr-day">New</div>
    <div class="sr-day-label">word</div>
    <div class="sr-stab">Stability: ~1 day</div>
  `;
  grid.appendChild(learnCell);

  schedule.forEach(s => {
    const cell = document.createElement('div');
    cell.className = 'sr-cell';
    cell.innerHTML = `
      <div class="sr-review-num">Review ${s.review}</div>
      <div class="sr-day">Day ${s.day}</div>
      <div class="sr-day-label">interval</div>
      <div class="sr-stab">Stability: ~${s.stability}d</div>
    `;
    grid.appendChild(cell);
  });

  // Lapse cell
  const lapseCell = document.createElement('div');
  lapseCell.className = 'sr-cell lapse';
  lapseCell.innerHTML = `
    <div class="sr-review-num">If you miss</div>
    <div class="sr-day" style="color:#e74c3c">Lapse</div>
    <div class="sr-day-label">reset interval</div>
    <div class="sr-stab" style="color:#e74c3c">Stability ÷ 2</div>
  `;
  grid.appendChild(lapseCell);

  // SR Decay chart — show retention curves for different stabilities
  const days  = Array.from({length: 31}, (_, i) => i);
  const stabilities = [1, 3, 7, 14, 30, 90];
  const colours = ['#e74c3c','#e67e22','#f1c40f','#27ae60','#3498db','#9b59b6'];

  const ctx = $('srDecayChart').getContext('2d');
  charts.srDecay = new Chart(ctx, {
    type: 'line',
    data: {
      labels: days,
      datasets: stabilities.map((s, i) => ({
        label: `After review ${i+1} (S=${s}d)`,
        data: days.map(d => parseFloat((retention(d, s) * 100).toFixed(1))),
        borderColor: colours[i],
        backgroundColor: 'transparent',
        borderWidth: 1.8,
        tension: 0.4,
        pointRadius: 0,
      })),
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: { duration: 700 },
      plugins: {
        legend: { position: 'top', labels: { padding: 12, usePointStyle: true, font: { size: 11 } } },
        tooltip: {
          callbacks: {
            label: ctx => ` ${ctx.dataset.label}: ${ctx.parsed.y}%`,
            title: ctx => `Day ${ctx[0].label}`,
          },
        },
      },
      scales: {
        x: {
          title: { display: true, text: 'Days' },
          grid: { color: 'rgba(255,255,255,0.03)' },
        },
        y: {
          min: 0, max: 100,
          title: { display: true, text: 'Retention %' },
          ticks: { callback: v => `${v}%` },
          grid: { color: 'rgba(255,255,255,0.03)' },
        },
      },
    },
  });
}

/* ──────────────────────────────────────────
   STAT CARDS
   ────────────────────────────────────────── */
function populateStats(vocab, studyMinutes, daysPerWeek, targetId) {
  const base      = dailyNewWords(studyMinutes, daysPerWeek);
  const targetLv  = LANG_CONFIG.levels.find(l => l.id === targetId) || LANG_CONFIG.levels[3];
  const months    = monthsToVocab(vocab, targetLv.words, base);
  const rec       = Math.round(base);

  // Words/day needed to hit target in 12 months
  const wpd12 = vocab >= targetLv.words
    ? 0
    : Math.ceil((targetLv.words - vocab) / (12 * 30.4));

  const conv = comprehensionPct(vocab, LANG_CONFIG.comprehensionContexts[0].coverage98);

  const proj = [6, 12, 24].map(m => Math.round(vocab + base * m * 30.4));

  $('sc-months-val').textContent = vocab >= targetLv.words ? '✓' : fmtMonths(months);
  $('sc-wpd-val').textContent     = vocab >= targetLv.words ? 'Achieved!' : `${wpd12}/day`;
  $('sc-comp-val').textContent    = `${conv}%`;
  $('sc-rec-val').textContent     = `${rec}/day`;
  $('sc-p6').textContent          = `${(proj[0]/1000).toFixed(1)}k`;
  $('sc-p12').textContent         = `${(proj[1]/1000).toFixed(1)}k`;
  $('sc-p24').textContent         = `${(proj[2]/1000).toFixed(1)}k`;

  // Level badge
  const lv = levelFromVocab(vocab);
  $('level-badge').textContent = lv.label;
  $('level-hint').textContent  = lv.desc;

  // Dashboard summary
  const targetName = targetLv.label;
  const monthsStr = vocab >= targetLv.words ? 'already at or past your target' : `${fmtMonths(months)} to reach ${targetName}`;
  $('dashboard-summary').textContent =
    `At ${vocab.toLocaleString()} words, studying ${studyMinutes} min/day for ${daysPerWeek} days/week — ${monthsStr}.`;
}

/* ──────────────────────────────────────────
   MAIN FORM HANDLER
   ────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  // Live slider outputs
  const studySlider = $('study-time');
  const consSlider  = $('consistency');
  studySlider.addEventListener('input', () => {
    $('study-time-out').textContent = `${studySlider.value} min/day`;
  });
  consSlider.addEventListener('input', () => {
    const v = parseInt(consSlider.value);
    $('consistency-out').textContent = v === 7 ? '7 days/week (every day!)' : `${v} days/week`;
  });

  // Form submit
  $('learner-form').addEventListener('submit', e => {
    e.preventDefault();

    const vocab       = Math.max(0, parseInt($('vocab').value) || 0);
    const studyMins   = parseInt(studySlider.value);
    const daysPerWeek = parseInt(consSlider.value);
    const months      = parseInt($('months-studying').value) || 0;
    const targetEl    = document.querySelector('input[name="target"]:checked');
    const targetId    = targetEl ? targetEl.value : 'N2';

    // Destroy existing charts before rebuilding
    destroyCharts();

    // Show dashboard
    const dash = $('dashboard');
    dash.classList.remove('hidden');

    // Build everything
    populateStats(vocab, studyMins, daysPerWeek, targetId);
    buildForgettingChart();
    buildVocabChart(vocab, studyMins, daysPerWeek);
    buildTimeChart(vocab, studyMins, daysPerWeek, targetId);
    buildComprehensionChart(vocab);
    buildSRSection();

    // Smooth scroll to dashboard
    setTimeout(() => {
      dash.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 80);
  });
});
