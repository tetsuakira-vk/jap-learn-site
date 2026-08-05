/* Japanese Unlocked — Shared Nav + Footer Injection */
(function () {
  const NAV_ITEMS = [
    {
      jp: '文字', en: 'Scripts',
      children: [
        { href: '/redesign/hiragana/', label: 'Hiragana', hint: 'あ' },
        { href: '/redesign/katakana/', label: 'Katakana', hint: 'ア' },
        { href: '/redesign/kanji/', label: 'Kanji', hint: '漢' },
      ]
    },
    {
      jp: '語彙', en: 'Vocabulary',
      children: [
        { href: '/redesign/vocab/phrases/', label: 'Phrases' },
        { href: '/redesign/vocab/numbers/', label: 'Numbers' },
        { href: '/redesign/vocab/dictionary/', label: 'Dictionary' },
      ]
    },
    {
      jp: '文法', en: 'Grammar',
      children: [
        { href: '/redesign/grammar/particles/', label: 'Particles' },
        { href: '/redesign/grammar/verbs/', label: 'Verbs' },
        { href: '/redesign/grammar/patterns/', label: 'Patterns' },
        { href: '/redesign/grammar/sentence-quiz/', label: 'Sentence Quiz' },
      ]
    },
    {
      jp: '練習', en: 'Practice',
      children: [
        { href: '/redesign/courses/what-would-you-say/', label: 'What Would You Say?' },
        { href: '/redesign/courses/shadowing/', label: 'Shadowing' },
        { href: '/redesign/courses/immersive-reader/', label: 'Immersive Reader' },
        { href: '/redesign/courses/sentence-forge/', label: 'Sentence Forge' },
        { href: '/redesign/courses/conversation/', label: 'Conversation' },
      ]
    },
    {
      jp: 'JLPT', en: 'JLPT',
      children: [
        { href: '/redesign/jlpt/n5/', label: 'N5' },
        { href: '/redesign/jlpt/n4/', label: 'N4' },
        { href: '/redesign/jlpt/n3/', label: 'N3' },
        { href: '/redesign/jlpt/n2/', label: 'N2' },
        { href: '/redesign/jlpt/n1/', label: 'N1' },
        { href: '/redesign/jlpt/mock/', label: 'Mock Tests' },
      ]
    },
    {
      jp: '遊', en: 'Games',
      children: [
        { href: '/redesign/games/battle/', label: 'Kanji Quest' },
        { href: '/redesign/games/match/', label: 'Memory Match' },
        { href: '/redesign/games/rhythm/', label: 'Rhythm' },
      ]
    },
    {
      jp: '歩', en: 'Walk',
      href: '/redesign/walk/'
    },
  ];

  const THEMES = [
    { id: 'light', label: 'Clean',  swatch: '#FAFAF8' },
    { id: 'warm',  label: 'Warm',   swatch: '#F0EBE2' },
    { id: 'dark',  label: 'Night',  swatch: '#111110' },
  ];

  const path = window.location.pathname;

  function isActive(href) {
    if (!href) return false;
    return path === href || path.startsWith(href);
  }

  function buildNavHTML() {
    const linksHTML = NAV_ITEMS.map(item => {
      const hasDrop = item.children && item.children.length;
      const activeClass = (hasDrop
        ? item.children.some(c => isActive(c.href))
        : isActive(item.href)) ? ' active' : '';

      if (hasDrop) {
        const dropItems = item.children.map(c =>
          `<li><a href="${c.href}"${isActive(c.href) ? ' aria-current="page"' : ''}>${c.label}${c.hint ? `<span style="font-family:var(--serif);color:var(--accent);opacity:.7;margin-left:6px">${c.hint}</span>` : ''}</a></li>`
        ).join('');
        return `
          <li class="${activeClass ? 'active' : ''}">
            <a href="#" onclick="return false" aria-haspopup="true">
              <span>${item.jp}</span>
              <span class="nav-sub">${item.en}</span>
            </a>
            <ul class="nav-drop" role="menu">${dropItems}</ul>
          </li>`;
      }
      return `
        <li class="${activeClass ? 'active' : ''}">
          <a href="${item.href}"${isActive(item.href) ? ' aria-current="page"' : ''}>
            <span>${item.jp}</span>
            <span class="nav-sub">${item.en}</span>
          </a>
        </li>`;
    }).join('');

    const currentTheme = localStorage.getItem('ju-theme') || 'light';
    const themeOptsHTML = THEMES.map(t =>
      `<button class="theme-opt${currentTheme === t.id ? ' active' : ''}" data-theme-set="${t.id}">
        <span class="theme-swatch" style="background:${t.swatch}"></span>${t.label}
      </button>`
    ).join('');

    return `
      <nav class="site-nav" role="navigation" aria-label="Main navigation">
        <a class="nav-brand" href="/redesign/">
          <span class="nav-jp">日</span>
          Japanese Unlocked
        </a>
        <ul class="nav-links" role="list">${linksHTML}</ul>
        <div class="nav-theme" aria-label="Theme picker">
          <button class="nav-theme-btn" aria-label="Change theme" title="Change theme">◐</button>
          <div class="theme-picker" role="menu">${themeOptsHTML}</div>
        </div>
        <button class="nav-hamburger" aria-label="Open menu" aria-expanded="false">☰</button>
      </nav>`;
  }

  function buildDrawerHTML() {
    const currentTheme = localStorage.getItem('ju-theme') || 'light';
    let sectionsHTML = NAV_ITEMS.map(item => {
      if (item.children) {
        const links = item.children.map(c =>
          `<a class="nav-drawer-item" href="${c.href}">${c.label}</a>`
        ).join('');
        return `
          <div class="nav-drawer-section">
            <span class="nav-drawer-label"><span class="drawer-jp">${item.jp}</span>${item.en}</span>
            ${links}
          </div>`;
      }
      return `
        <div class="nav-drawer-section">
          <a class="nav-drawer-item" href="${item.href}">${item.jp} ${item.en}</a>
        </div>`;
    }).join('');

    const themeOptsHTML = THEMES.map(t =>
      `<button class="theme-opt${currentTheme === t.id ? ' active' : ''}" data-theme-set="${t.id}">
        <span class="theme-swatch" style="background:${t.swatch}"></span>${t.label}
      </button>`
    ).join('');

    return `
      <div class="nav-drawer" id="ju-drawer" aria-modal="true" role="dialog">
        <div class="nav-drawer-overlay"></div>
        <div class="nav-drawer-panel">
          <button class="nav-drawer-close" aria-label="Close menu">✕</button>
          ${sectionsHTML}
          <div class="nav-drawer-section" style="padding:14px 14px 0">
            <span class="nav-drawer-label">Theme</span>
            <div style="padding:10px 6px 14px;display:flex;flex-direction:column;gap:2px">${themeOptsHTML}</div>
          </div>
        </div>
      </div>`;
  }

  function buildFooterHTML() {
    return `
      <footer class="site-footer">
        <span class="footer-jp">日本語アンロック</span>
        <span>© ${new Date().getFullYear()} Japanese Unlocked — all content free, always</span>
        <nav style="display:flex;gap:20px;font-size:12px">
          <a href="/redesign/about/" style="color:var(--mid)">About</a>
          <a href="/redesign/resources/" style="color:var(--mid)">Resources</a>
          <a href="/videos/" style="color:var(--mid)">Videos</a>
        </nav>
      </footer>`;
  }

  function applyTheme(t) {
    const theme = t || 'light';
    document.documentElement.setAttribute('data-theme', theme);
    document.querySelectorAll('.theme-opt').forEach(el => {
      el.classList.toggle('active', el.dataset.themeSet === theme);
    });
  }

  function init() {
    /* ── Inject nav ── */
    const navSlot = document.getElementById('ju-nav');
    if (navSlot) navSlot.innerHTML = buildNavHTML() + buildDrawerHTML();

    /* ── Inject footer ── */
    const footerSlot = document.getElementById('ju-footer');
    if (footerSlot) footerSlot.innerHTML = buildFooterHTML();

    /* ── Apply stored theme ── */
    const stored = localStorage.getItem('ju-theme') || 'light';
    applyTheme(stored);

    /* ── Theme switcher ── */
    document.addEventListener('click', function (e) {
      const btn = e.target.closest('[data-theme-set]');
      if (btn) {
        const t = btn.dataset.themeSet;
        localStorage.setItem('ju-theme', t);
        applyTheme(t);
      }
    });

    /* ── Mobile drawer ── */
    const drawer = document.getElementById('ju-drawer');
    function openDrawer() {
      if (drawer) {
        drawer.classList.add('open');
        document.querySelector('.nav-hamburger')?.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden';
      }
    }
    function closeDrawer() {
      if (drawer) {
        drawer.classList.remove('open');
        document.querySelector('.nav-hamburger')?.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    }
    document.addEventListener('click', function (e) {
      if (e.target.closest('.nav-hamburger')) openDrawer();
      if (e.target.closest('.nav-drawer-overlay') || e.target.closest('.nav-drawer-close')) closeDrawer();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeDrawer();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
