/* Shared JLPT mock test engine — used by n5/, n4/, n3/ */

function renderSection(containerId, items, sectionId) {
  const el = document.getElementById(containerId);
  let html = '';
  items.forEach(function(q) {
    if (q.type === 'title') {
      html += '<div class="mock-sect-title">' + q.text + '</div>';
    } else if (q.type === 'sub') {
      html += '<div class="mock-subsect-title">' + q.text + '</div>';
    } else if (q.type === 'passage') {
      html += '<div class="mock-passage">' + q.text + '</div>';
    } else if (q.type === 'notice') {
      html += '<div class="mock-passage mock-notice">' + q.text + '</div>';
    } else if (q.type === 'ordering') {
      html += '<div class="mq" data-answer="' + q.a + '">' +
        '<span class="mq-num">' + q.n + '</span>' +
        '<p class="mq-ordering-stem">' + q.stem + '</p>' +
        '<p class="mq-chunks">' + q.chunks + '</p>' +
        '<p class="mq-ordering-q">★の位置に入るものはどれですか。</p>' +
        '<div class="mq-opts">' + renderOpts(q.o, sectionId + '-q' + q.n) + '</div>' +
        '</div>';
    } else {
      // regular question
      var txt = q.t ? q.t : '';
      html += '<div class="mq" data-answer="' + q.a + '">' +
        '<span class="mq-num">' + q.n + '</span>' +
        (txt ? '<p class="mq-text">' + txt + '</p>' : '') +
        '<div class="mq-opts">' + renderOpts(q.o, sectionId + '-q' + q.n) + '</div>' +
        '</div>';
    }
  });
  el.innerHTML = html;
}

function renderOpts(opts, name) {
  var nums = ['①','②','③','④'];
  return opts.map(function(o, i) {
    return '<label><input type="radio" name="' + name + '" value="' + i + '">' + nums[i] + ' ' + o + '</label>';
  }).join('');
}

function showSection(id) {
  document.querySelectorAll('.mock-sect').forEach(function(s) { s.style.display = 'none'; });
  document.getElementById('sect-' + id).style.display = 'block';
  document.querySelectorAll('.mock-tab').forEach(function(t) { t.classList.remove('active'); });
  document.getElementById('tab-' + id).classList.add('active');
  var tabBar = document.querySelector('.mock-tab-bar');
  if (tabBar) window.scrollTo({ top: tabBar.getBoundingClientRect().top + window.scrollY - 60, behavior: 'smooth' });
}

function submitSection(sectId) {
  var sect = document.getElementById('sect-' + sectId);
  var qs = sect.querySelectorAll('.mq');
  var correct = 0;
  qs.forEach(function(q) {
    var ans = parseInt(q.dataset.answer);
    var chosen = q.querySelector('input:checked');
    var chosenVal = chosen ? parseInt(chosen.value) : -1;
    if (chosenVal === ans) { correct++; q.classList.add('mq-right'); }
    else { q.classList.add('mq-wrong'); }
    q.querySelectorAll('.mq-opts label').forEach(function(lbl, i) {
      if (i === ans) lbl.classList.add('mq-correct-lbl');
      else if (chosen && i === chosenVal) lbl.classList.add('mq-wrong-lbl');
    });
    q.querySelectorAll('input').forEach(function(inp) { inp.disabled = true; });
  });
  var total = qs.length;
  var pct = Math.round(correct / total * 100);
  var scoreEl = document.getElementById('score-' + sectId);
  var grade = pct >= 60 ? 'mock-score-pass' : 'mock-score-fail';
  scoreEl.innerHTML = '得点 / Score: <strong>' + correct + ' / ' + total + '</strong> (' + pct + '%)' +
    (pct >= 60 ? ' ✓ 合格圏内' : ' — keep practising!');
  scoreEl.className = 'mock-score ' + grade;
  scoreEl.style.display = 'block';
  sect.querySelector('.mock-submit').disabled = true;
  var nextBtn = sect.querySelector('.mock-next');
  if (nextBtn) nextBtn.style.display = 'inline-block';
  updateTotal();
}

function updateTotal() {
  var vocabDone = document.getElementById('score-vocab') && document.getElementById('score-vocab').style.display !== 'none';
  var grammarDone = document.getElementById('score-grammar') && document.getElementById('score-grammar').style.display !== 'none';
  if (!vocabDone || !grammarDone) return;
  var totalEl = document.getElementById('mock-total');
  if (!totalEl) return;
  var allRight = document.querySelectorAll('.mq-right').length;
  var allQ = document.querySelectorAll('.mq').length;
  var pct = Math.round(allRight / allQ * 100);
  totalEl.innerHTML = '総合得点 Total Score: <strong>' + allRight + ' / ' + allQ + '</strong> (' + pct + '%)' +
    (pct >= 60
      ? '<br><span class="total-pass">合格圏内 Pass range — well done!</span>'
      : '<br><span class="total-fail">合格基準以下 Below pass mark — keep studying!</span>');
  totalEl.style.display = 'block';
  totalEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
}
