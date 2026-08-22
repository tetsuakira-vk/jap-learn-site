/* Japanese Unlocked — Shared Nav + Footer Injection */
(function () {
  const NAV_ITEMS = [
    {
      jp: '文字', en: 'Scripts', href: '/hiragana/',
      children: [
        { href: '/hiragana/', label: 'Hiragana', hint: 'あ' },
        { href: '/katakana/', label: 'Katakana', hint: 'ア' },
        { href: '/kanji/', label: 'Kanji', hint: '漢' },
        { href: '/quiz/', label: 'Script Quiz' },
      ]
    },
    {
      jp: '語彙', en: 'Vocabulary', href: '/vocab/',
      children: [
        { href: '/vocab/phrases/', label: 'Phrases' },
        { href: '/vocab/numbers/', label: 'Numbers' },
        { href: '/vocab/dictionary/', label: 'Dictionary' },
      ]
    },
    {
      jp: '文法', en: 'Grammar', href: '/grammar/',
      children: [
        { href: '/grammar/particles/', label: 'Particles' },
        { href: '/grammar/verbs/', label: 'Verbs' },
        { href: '/grammar/patterns/', label: 'Patterns' },
        { href: '/grammar/sentence-quiz/', label: 'Sentence Quiz' },
      ]
    },
    {
      jp: '練習', en: 'Practice', href: '/courses/',
      children: [
        { href: '/echo/', label: 'Echo 影' },
        { href: '/courses/sentence-forge/', label: 'Sentence Forge' },
        { href: '/courses/immersive-reader/', label: 'Immersive Reader' },
      ]
    },
    {
      jp: 'JLPT', en: 'JLPT', href: '/jlpt/',
      children: [
        { href: '/jlpt/n5/', label: 'N5' },
        { href: '/jlpt/n4/', label: 'N4' },
        { href: '/jlpt/n3/', label: 'N3' },
        { href: '/jlpt/n2/', label: 'N2' },
        { href: '/jlpt/n1/', label: 'N1' },
        { href: '/jlpt/mock/', label: 'Mock Tests' },
      ]
    },
    {
      jp: '遊', en: 'Games', href: '/games/',
      children: [
        { href: '/games/kanadle/', label: 'KANADLE' },
        { href: '/games/battle/', label: 'Kanji Quest' },
        { href: '/games/match/', label: 'Memory Match' },
        { href: '/games/rhythm/', label: 'RAPID' },
      ]
    },
    { jp: 'リソース', en: 'Resources', href: '/resources/' },
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
        return `
          <li class="${activeClass ? 'active' : ''}">
            <a href="${item.href}">
              <span>${item.jp}</span>
              <span class="nav-sub">${item.en}</span>
            </a>
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
        <a class="nav-brand" href="/">
          <span class="nav-jp">日</span>
          Japanese Unlocked
        </a>
        <ul class="nav-links" role="list">${linksHTML}</ul>
        <div class="nav-theme" aria-label="Theme picker">
          <button class="nav-theme-btn" aria-label="Change theme" title="Change theme">◐</button>
          <div class="theme-picker" role="menu">${themeOptsHTML}</div>
        </div>
        <button class="nav-hamburger" aria-label="Open menu" aria-expanded="false">Menu</button>
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
          <button class="nav-drawer-close" aria-label="Close menu">×</button>
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
          <a href="/start/" style="color:var(--mid)">Start Here</a>
          <a href="/about/" style="color:var(--mid)">About</a>
          <a href="/resources/" style="color:var(--mid)">Resources</a>
          <a href="https://www.youtube.com/@JapaneseLearning-z2x" target="_blank" rel="noopener" style="color:var(--mid)">YouTube</a>
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
