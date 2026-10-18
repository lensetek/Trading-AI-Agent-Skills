/**
 * TRADING AI AGENT SKILLS - CLIENT APPLICATION v1.2.0
 * High-performance, zero external dependency vanilla JS
 * Full Mobile-View First touch support
 * Zero-gimmick landing page logic: navigation, i18n, filters, and code copier.
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initLanguageToggle();
  initCopyButton();
  initSkillFilters();
  initInstallTabs();
});

// --- 1. MOBILE DRAWER NAVIGATION ---
function initMobileMenu() {
  const toggleBtn = document.querySelector('.mobile-menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (toggleBtn && navLinks) {
    toggleBtn.addEventListener('click', () => {
      navLinks.classList.toggle('open');
      const isOpen = navLinks.classList.contains('open');
      toggleBtn.setAttribute('aria-expanded', isOpen);
      toggleBtn.innerHTML = isOpen ? '✕' : '☰';
    });

    navLinks.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        toggleBtn.innerHTML = '☰';
      });
    });
  }
}

// --- 2. BILINGUAL CONTENT ENGINE (ID / EN) ---
const i18nData = {
  id: {
    heroTag: 'UNIVERSAL AGENT SKILLS SUITE v1.2.0',
    heroTitle: 'Kecerdasan Kuantitatif & Trading Mandiri untuk <span>AI Coding Agents</span>',
    heroDesc: 'Koleksi modular Agent Skills terstandarisasi untuk Claude Code, OpenAI Codex, Antigravity, OpenCode, Cursor, dan Windsurf. Membekali AI Agent Anda kemampuan menyadap running trade browser, membaca transmisi indeks global (MSCI, EIDO, CFTC COT), mendeteksi wash trading, memproyeksikan harga dengan Google TimesFM, dan menjalankan Paper Trading mandiri dengan ekspor jurnal Excel.',
    btnExplore: 'Jelajahi 13 Sub-Skills',
    skillsTag: 'ARSITEKTUR LENGKAP',
    skillsTitle: '13 Sub-Skills Kuantitatif Terpadu',
    skillsSubtitle: 'Dapat dijalankan satu per satu secara independen atau dikoordinasikan secara otonom oleh Trading Orchestrator.',
    secTitle: 'STANDAR KEAMANAN KREDENSIAL MUTLAK',
    secItem1: 'Kunci API & rahasia tersimpan ketat di .env lokal. TIDAK PERNAH dikirim ke frontend atau context LLM publik.',
    secItem2: 'Sesi browser web broker menggunakan mode Chrome Remote Debugging. Anda login manual, agent hanya membaca WebSocket tanpa melihat password.',
    secItem3: 'Semua eksekusi live mewajibkan izin persetujuan eksplisit pengguna via Terminal, Web, atau Telegram (Human-in-the-Loop).'
  },
  en: {
    heroTag: 'UNIVERSAL AGENT SKILLS SUITE v1.2.0',
    heroTitle: 'Autonomous Quantitative & Trading Intelligence for <span>AI Coding Agents</span>',
    heroDesc: 'Standardized modular Agent Skills suite for Claude Code, OpenAI Codex, Antigravity, OpenCode, Cursor, and Windsurf. Equips your AI agents with browser tape interception, global benchmark transmission (MSCI, EIDO, CFTC COT), wash trade detection, Google TimesFM probabilistic forecasting, and offline Paper Trading with automated Excel export.',
    btnExplore: 'Explore 13 Sub-Skills',
    skillsTag: 'FULL ARCHITECTURE',
    skillsTitle: '13 Unified Quantitative Sub-Skills',
    skillsSubtitle: 'Can be invoked individually or coordinated autonomously by the Trading Orchestrator.',
    secTitle: 'ZERO-COMPROMISE CREDENTIAL SECURITY',
    secItem1: 'API keys & broker secrets reside strictly in local .env. NEVER serialized to frontend or leaked to public LLMs.',
    secItem2: 'Browser sniffing relies on Chrome Remote Debugging. You authenticate manually; the agent only captures WebSockets without touching passwords.',
    secItem3: 'All live executions require affirmative Human-in-the-Loop confirmation via Terminal CLI, Web, or Telegram.'
  }
};

let currentLang = 'id';

function initLanguageToggle() {
  const langBtn = document.getElementById('langToggleBtn');
  if (!langBtn) return;

  langBtn.addEventListener('click', () => {
    currentLang = currentLang === 'id' ? 'en' : 'id';
    langBtn.innerHTML = currentLang === 'id' ? '🇮🇩 ID | EN' : '🇬🇧 EN | ID';
    applyTranslations();
  });
}

function applyTranslations() {
  const t = i18nData[currentLang];
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (t[key]) {
      el.innerHTML = t[key];
    }
  });
}

// --- 3. COPY INSTALL COMMAND BUTTON ---
function initCopyButton() {
  const copyBtn = document.getElementById('copyCmdBtn');
  const cmdText = document.getElementById('commandText');

  if (copyBtn && cmdText) {
    copyBtn.addEventListener('click', () => {
      const textToCopy = cmdText.innerText;
      navigator.clipboard.writeText(textToCopy).then(() => {
        const originalText = copyBtn.innerText;
        copyBtn.innerText = 'Copied! ✓';
        copyBtn.style.background = '#047857';
        setTimeout(() => {
          copyBtn.innerText = originalText;
          copyBtn.style.background = '';
        }, 2000);
      });
    });
  }
}

// --- 4. SKILL FILTER TABS ---
function initSkillFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const skillCards = document.querySelectorAll('.skill-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const category = btn.getAttribute('data-category');

      skillCards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        if (category === 'all' || cardCategory === category) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

// --- 5. INSTALLATION GUIDE TABS ---
const installSnippets = {
  claude: `# Claude Code (Anthropic)
# Metode 1: Pasang via NPX Skills
npx skills install https://github.com/lensetek/Trading-AI-Agent-Skills

# Metode 2: Berikan prompt langsung ke Claude Code:
> Tolong pasang dan pelajari agent skills dari https://github.com/lensetek/Trading-AI-Agent-Skills ke dalam workspace ini.`,

  codex: `# OpenAI Codex / Custom Agent
# Metode 1: Pasang via NPX Skills
npx skills install https://github.com/lensetek/Trading-AI-Agent-Skills

# Metode 2: Daftarkan direktori skills ke sistem path agent:
codex --skill-path ./skills`,

  antigravity: `# Google Antigravity / Gemini CLI
# Metode 1: Pasang via NPX Skills
npx skills install https://github.com/lensetek/Trading-AI-Agent-Skills

# Metode 2: Tautkan sebagai plugin lokal atau berikan prompt:
antigravity plugin add https://github.com/lensetek/Trading-AI-Agent-Skills`,

  opencode: `# OpenCode / Cursor / Windsurf
# Metode 1: Pasang via NPX Skills
npx skills install https://github.com/lensetek/Trading-AI-Agent-Skills

# Setelah terinstal, custom agents akan ter-generate otomatis
# di .opencode/agents/ → Bisa dipanggil dengan @<skill-name>

# Metode 2: Beri prompt ke agent:
"Pasang agent skills dari https://github.com/lensetek/Trading-AI-Agent-Skills dan siapkan paper trading. Buat juga file agent untuk OpenCode v2 di .opencode/agents/ sambil tetap mempertahankan folder skills/ untuk kompatibilitas lintas-agent."`
};

function initInstallTabs() {
  const tabBtns = document.querySelectorAll('.install-tab-btn');
  const codeEl = document.getElementById('installCodeBlock');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const target = btn.getAttribute('data-target');
      if (codeEl && installSnippets[target]) {
        codeEl.innerText = installSnippets[target];
      }
    });
  });
}
