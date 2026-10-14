/**
 * TRADING AI AGENT SKILLS - INTERACTIVE CLIENT APPLICATION
 * High-performance, zero external dependency vanilla JS
 * Full Mobile-View First touch support
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initLanguageToggle();
  initCopyButton();
  initInstrumentSimulator();
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

    // Close when clicking nav items
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
    heroTag: 'UNIVERSAL AGENT SKILLS SUITE v1.0',
    heroTitle: 'Kecerdasan Kuantitatif & Trading Mandiri untuk <span>AI Coding Agents</span>',
    heroDesc: 'Memberi Claude Code, OpenAI Codex, Antigravity, dan OpenCode kemampuan menyadap running trade browser, memproyeksikan harga dengan Google TimesFM, membaca posisi institusi CFTC COT, dan simulasi Paper Trading aman dengan ekspor otomatis ke Excel.',
    btnExplore: 'Jelajahi 12 Skills',
    btnDemo: 'Coba Simulasi Interaktif',
    statSkills: '12 Sub-Skills',
    statSkillsSub: 'Modular & Terpadu',
    statRisk: 'Zero Password',
    statRiskSub: 'Remote CDP Safe',
    statModel: 'Google TimesFM',
    statModelSub: 'Zero-Shot Quantiles',
    statMarket: 'Saham IDX + Multi',
    statMarketSub: 'Crypto, Forex, Futures',
    demoTag: 'SIMULASI HUMAN-IN-THE-LOOP',
    demoTitle: 'Uji Coba Sinyal & Eksekusi Paper Trading',
    demoSubtitle: 'Lihat bagaimana AI Agent mendeteksi anomali volume, memproyeksikan rentang probabilitas TimesFM, dan meminta izin Anda sebelum mencatat order ke database SQLite & Excel.',
    ticketTitle: 'TIKET KONFIRMASI PERSENYALAN',
    approveBtn: '✔ Setujui Transaksi',
    rejectBtn: '✖ Tolak Sinyal',
    approvedToast: 'Transaksi Disetujui! Posisi dicatat ke SQLite & Jurnal Excel (.xlsx)',
    rejectedToast: 'Sinyal Ditolak. Posisi dibatalkan tanpa risiko saldo.',
    skillsTag: 'ARSITEKTUR LENGKAP',
    skillsTitle: '12 Sub-Skills Kuantitatif Terpadu',
    skillsSubtitle: 'Dapat dijalankan satu per satu atau dikoordinasikan secara otomatis oleh Trading Orchestrator.',
    secTitle: 'STANDAR KEAMANAN KREDENSIAL MUTLAK',
    secItem1: 'Kunci API & rahasia tersimpan ketat di .env lokal. TIDAK PERNAH dikirim ke frontend atau context LLM publik.',
    secItem2: 'Sesi browser web broker menggunakan mode Chrome Remote Debugging. Anda login manual, agent hanya membaca WebSocket tanpa melihat password.',
    secItem3: 'Semua eksekusi live mewajibkan izin persetujuan eksplisit pengguna via Terminal, Web, atau Telegram (Human-in-the-Loop).'
  },
  en: {
    heroTag: 'UNIVERSAL AGENT SKILLS SUITE v1.0',
    heroTitle: 'Autonomous Quantitative & Trading Intelligence for <span>AI Coding Agents</span>',
    heroDesc: 'Equips Claude Code, OpenAI Codex, Antigravity, and OpenCode with real-time browser tape interception, Google TimesFM probabilistic forecasting, CFTC COT institutional flow tracking, and offline Paper Trading with automated Excel export.',
    btnExplore: 'Explore 12 Skills',
    btnDemo: 'Try Interactive Demo',
    statSkills: '12 Sub-Skills',
    statSkillsSub: 'Modular & Unified',
    statRisk: 'Zero Password',
    statRiskSub: 'Remote CDP Safe',
    statModel: 'Google TimesFM',
    statModelSub: 'Zero-Shot Quantiles',
    statMarket: 'IDX Stocks + Multi',
    statMarketSub: 'Crypto, Forex, Futures',
    demoTag: 'HUMAN-IN-THE-LOOP SIMULATION',
    demoTitle: 'Live Signal & Paper Trading Execution Test',
    demoSubtitle: 'Experience how the AI Agent detects volume surges, forecasts TimesFM quantile bands, and requests your authorization before updating the SQLite database and Excel journal.',
    ticketTitle: 'SIGNAL CONFIRMATION TICKET',
    approveBtn: '✔ Approve Execution',
    rejectBtn: '✖ Reject Signal',
    approvedToast: 'Order Approved! Position logged to local SQLite & Excel Journal (.xlsx)',
    rejectedToast: 'Signal Rejected. Order dismissed with zero capital risk.',
    skillsTag: 'FULL ARCHITECTURE',
    skillsTitle: '12 Unified Quantitative Sub-Skills',
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

// --- 4. INTERACTIVE INSTRUMENT & PAPER TRADING SIMULATOR ---
const instrumentData = {
  bbca: {
    name: 'BBCA (Bank Central Asia - IDX)',
    market: 'Saham Indonesia (IDX)',
    price: 'Rp 9.850',
    change: '+1.8% today',
    target: 'Rp 10.200 (+3.5%)',
    stopLoss: 'Rp 9.700 (-1.5%)',
    size: '20 Lot (Rp 19.700.000)',
    timesfmP10: 'Rp 9.680',
    timesfmP50: 'Rp 10.150 (+3.0%)',
    timesfmP90: 'Rp 10.350 (+5.1%)',
    rationale: 'Haka Volume Spike + Akumulasi Broker Asing (CS, BK) + TimesFM Bullish Curve'
  },
  antm: {
    name: 'ANTM (Aneka Tambang - IDX)',
    market: 'Saham Komoditas Emas/Nikel',
    price: 'Rp 1.580',
    change: '+3.2% today',
    target: 'Rp 1.690 (+6.9%)',
    stopLoss: 'Rp 1.530 (-3.1%)',
    size: '100 Lot (Rp 15.800.000)',
    timesfmP10: 'Rp 1.520',
    timesfmP50: 'Rp 1.680 (+6.3%)',
    timesfmP90: 'Rp 1.740 (+10.1%)',
    rationale: 'Korelasi CFTC COT Gold All-Time High + Breakout Resistance Volume 2.5x'
  },
  xau: {
    name: 'XAU/USD (Spot Gold)',
    market: 'Global Commodity & Forex',
    price: '$2,685.40',
    change: '+0.95% today',
    target: '$2,720.00 (+1.28%)',
    stopLoss: '$2,668.00 (-0.65%)',
    size: '0.50 Lot ($500 Margin)',
    timesfmP10: '$2,665.20',
    timesfmP50: '$2,715.00 (+1.10%)',
    timesfmP90: '$2,735.80 (+1.87%)',
    rationale: 'Post-NFP Deviation Momentum + Extreme Commercial Hedging Unwind'
  },
  btc: {
    name: 'BTC/USDT (Bitcoin)',
    market: 'Crypto Spot / Futures',
    price: '$64,250',
    change: '+4.2% today',
    target: '$67,500 (+5.05%)',
    stopLoss: '$62,800 (-2.25%)',
    size: '0.10 BTC ($6,425)',
    timesfmP10: '$62,500',
    timesfmP50: '$66,800 (+3.96%)',
    timesfmP90: '$69,200 (+7.70%)',
    rationale: 'Whale Orderbook Absorption + Orderflow CVD Divergence Bullish'
  }
};

let simulatedEquity = 100000000; // Rp 100 Juta initial paper trading balance
let simulatedTradesCount = 0;

function initInstrumentSimulator() {
  const assetTabs = document.querySelectorAll('.asset-tab');
  const symbolEl = document.getElementById('chartSymbol');
  const priceEl = document.getElementById('chartPrice');
  const p10El = document.getElementById('p10Val');
  const p50El = document.getElementById('p50Val');
  const p90El = document.getElementById('p90Val');
  const ticketTarget = document.getElementById('ticketTarget');
  const ticketSL = document.getElementById('ticketSL');
  const ticketSize = document.getElementById('ticketSize');
  const ticketRationale = document.getElementById('ticketRationale');

  function updateDisplay(key) {
    const data = instrumentData[key];
    if (!data) return;

    if (symbolEl) symbolEl.innerText = data.name;
    if (priceEl) priceEl.innerHTML = `${data.price} <span class="price-change">${data.change}</span>`;
    if (p10El) p10El.innerText = data.timesfmP10;
    if (p50El) p50El.innerText = data.timesfmP50;
    if (p90El) p90El.innerText = data.timesfmP90;
    if (ticketTarget) ticketTarget.innerText = data.target;
    if (ticketSL) ticketSL.innerText = data.stopLoss;
    if (ticketSize) ticketSize.innerText = data.size;
    if (ticketRationale) ticketRationale.innerText = data.rationale;

    // Reset status toast
    const toastEl = document.getElementById('ticketToast');
    if (toastEl) toastEl.style.display = 'none';
  }

  assetTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      assetTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const assetKey = tab.getAttribute('data-asset');
      updateDisplay(assetKey);
    });
  });

  // Action buttons
  const approveBtn = document.getElementById('approveTradeBtn');
  const rejectBtn = document.getElementById('rejectTradeBtn');
  const toastEl = document.getElementById('ticketToast');
  const equityEl = document.getElementById('simEquityVal');
  const tradesCountEl = document.getElementById('simTradesCount');

  if (approveBtn) {
    approveBtn.addEventListener('click', () => {
      simulatedTradesCount += 1;
      const profitIncrement = Math.floor(Math.random() * 850000) + 350000;
      simulatedEquity += profitIncrement;

      if (equityEl) equityEl.innerText = 'Rp ' + simulatedEquity.toLocaleString('id-ID');
      if (tradesCountEl) tradesCountEl.innerText = `${simulatedTradesCount} Trades Logged`;

      if (toastEl) {
        toastEl.className = 'forecast-badge-box';
        toastEl.style.background = '#ecfdf5';
        toastEl.style.borderColor = '#6ee7b7';
        toastEl.style.color = '#064e3b';
        toastEl.style.display = 'block';
        toastEl.innerHTML = `<strong>✔ ${i18nData[currentLang].approvedToast}</strong><br/>Simulated Profit: +Rp ${profitIncrement.toLocaleString('id-ID')} | Trailing Stop Active`;
      }
    });
  }

  if (rejectBtn) {
    rejectBtn.addEventListener('click', () => {
      if (toastEl) {
        toastEl.className = 'forecast-badge-box';
        toastEl.style.background = '#fef2f2';
        toastEl.style.borderColor = '#fca5a5';
        toastEl.style.color = '#7f1d1d';
        toastEl.style.display = 'block';
        toastEl.innerHTML = `<strong>✖ ${i18nData[currentLang].rejectedToast}</strong>`;
      }
    });
  }

  // Initialize with BBCA
  updateDisplay('bbca');
}

// --- 5. SKILL FILTER TABS ---
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

// --- 6. INSTALLATION GUIDE TABS ---
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

# Metode 2: Beri prompt ke agent:
"Pasang agent skills dari https://github.com/lensetek/Trading-AI-Agent-Skills dan siapkan paper trading."`
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
