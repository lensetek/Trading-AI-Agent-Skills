# Trading AI Agent Skills Suite 📈🤖
### Quantitative & Multi-Market Intelligence Suite for AI Coding Agents

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![Cross-Agent: Compatible](https://img.shields.io/badge/AI%20Agents-Claude%20Code%20%7C%20Codex%20%7C%20Antigravity%20%7C%20OpenCode-purple.svg)]()
[![Google TimesFM](https://img.shields.io/badge/Model-Google%20TimesFM-orange.svg)](https://github.com/google-research/timesfm)
[![CFTC COT Data](https://img.shields.io/badge/Data-CFTC%20COT%20Reports-gold.svg)](https://www.cftc.gov)

> **Universal Agent Skills Standard:** Koleksi kemampuan (*skills*) kuantitatif dan analisis pasar mandiri yang dapat di-instal ke semua AI coding assistant (**Claude Code, OpenAI Codex, Antigravity, OpenCode, Cursor, Windsurf**). Mendukung Saham Indonesia (IDX), Kripto, Valuta Asing (Forex), dan Komoditas Berjangka.

---

### 🌐 Language Quick Navigation / Pintasan Bahasa
* **🔥 [What's New in v1.2.0 / Apa yang Baru di v1.2.0](#-whats-new-in-v120--apa-yang-baru-di-v120)**
* **🚀 [What's New in v1.1.0 / Apa yang Baru di v1.1.0](#-whats-new-in-v110--apa-yang-baru-di-v110)**
* **🇮🇩 [Bahasa Indonesia](#-bahasa-indonesia)**
  * [1. Ringkasan Eksekutif](#1-ringkasan-eksekutif)
  * [2. Cara Pemasangan Agent Skills (How to Install)](#2-cara-pemasangan-agent-skills-how-to-install)
  * [3. Daftar 13 Modul Sub-Skills](#3-daftar-13-modul-sub-skills)
  * [4. Fitur Unggulan Institusional](#4-fitur-unggulan-institusional)
  * [5. Penggunaan Lintas Agen AI](#5-penggunaan-lintas-agen-ai)
  * [6. Keamanan Kredensial & Manajemen Risiko](#6-keamanan-kredensial--manajemen-risiko)
* **🇬🇧 [English](#-english)**
  * [1. Executive Summary](#1-executive-summary)
  * [2. How to Install Agent Skills](#2-how-to-install-agent-skills)
  * [3. Suite of 13 Modular Skills](#3-suite-of-13-modular-skills)
  * [4. Institutional-Grade Features](#4-institutional-grade-features)
  * [5. Cross-Agent Usage](#5-cross-agent-usage)
  * [6. Credential Safety & Risk Management](#6-credential-safety--risk-management)

---

### 🔥 What's New in v1.2.0 / Apa yang Baru di v1.2.0

* **🏛️ Global Benchmark & Institutional Governance Radar**:
  * **Kriteria Aksesibilitas MSCI & FTSE**: Evaluasi keterbukaan pemilik manfaat (UBO) di atas 1%, batasan *free float* minimum 15% (FIF), dan deteksi risiko konsentrasi kepemilikan semu (*High Shareholding Concentration / HSC*).
  * **EIDO Arbitrage & Gap-Opening Predictor**: Menghitung selisih imbal hasil penutupan ETF EIDO di New York (NYSE) untuk memprediksi arah pembukaan (*gap up / gap down*) IHSG dan saham Big-4 perbankan (`BBCA`, `BBRI`, `BMRI`, `TLKM`).
  * **Transmisi Makro Lintas Aset**: Memetakan kriteria *US Treasury FX Manipulator Watchlist* (Forex), audit ketersediaan stok fisik gudang LME/COMEX (Komoditas), serta audit Tokenomics & rasio Gini wallet paus (Crypto).
* **🛡️ Coordinated Trading & Wash Sale Detection Module**:
  * Algoritma membaca transaksi pita (*tape reading*) di `orderflow-tape-scalper` untuk mendeteksi transaksi melingkar antar-broker terafiliasi (*circular cross trading*) dan memfilter volume palsu (*Wash Volume Ratio / WVR*).
* **🧠 Tri-Layer Decision Engine & Plain-Language Verdict**:
  * Arsitektur pengambilan keputusan 3-lapis di `trading-orchestrator`:
    1. *Layer 1*: Filter Kelayakan Tata Kelola & Anti-Manipulasi (HSC / Wash Sale / Regulatory Risk).
    2. *Layer 2*: Arah Arus Modal Institusi Global (MSCI Rebalancing, CFTC COT, ETF Inflows).
    3. *Layer 3*: Waktu Eksekusi Mikro, TimesFM Probabilistik, dan Optimasi Sizing.
  * Menghasilkan arahan tegas dalam bahasa manusia (`🟢 STRONG BUY`, `🟡 WAIT`, `🔴 AVOID`), Confluence Score (0-100%), serta *Invalidation Rule* eksplisit.
* **📱🖥️ Decision-First Adaptive Pro Terminal**:
  * **Interactive Canvas Candlestick Engine**: Candlestick High-DPI riil dengan volume bars, grid harga, dan *crosshair tooltip*.
  * **Visual Decision Overlays**: Garis Entry Zone, Target TP, Stop Loss, Dynamic Trailing Stop, dan **TimesFM Confidence Fan (P10-P90 Shaded Area)** langsung di atas grafik.
  * **Kalkulator Manajemen Risiko Riil**: Menghitung rasio Risk-to-Reward (R:R), estimasi nominal rupiah/USD maksimal kerugian jika kena SL, dan rekomendasi ukuran lot berbasis batas risiko 1-2% modal.
  * **Adaptive Layout**: Mobile-View First yang otomatis membuka menjadi **Tri-Pane Pro Terminal** di layar laptop/desktop ($\ge 1024\text{px}$).
* **⚡ Standalone Server Mandiri (`skills/mobile-chart-server/scripts/mobile_server.py`)**:
  * Server lokal berbasis **FastAPI & Uvicorn** yang menyajikan REST API data pasar dan antarmuka web mandiri yang bisa dibuka langsung di smartphone lewat jaringan Wi-Fi lokal.

---

* **✨ Sub-Skill Baru ke-13: `backtest-strategy-optimizer`**
  * **Vectorized Backtesting Engine**: Mesin simulasi historis berkecepatan tinggi dengan pemodelan biaya bursa nyata (Saham IDX 0.15% beli, 0.25% jual incl. PPh final; maker/taker fee Crypto) serta slippage spread.
  * **Genetic Algorithm (GA) Optimization**: Algoritma pencarian parameter global heuristik (kromosom = parameter, seleksi elitisme, crossover, & mutasi adaptif) agar tidak terjebak di lokal optimum.
  * **Walk-Forward Analysis (WFA / WFO)**: Validasi *In-Sample* (optimasi) vs *Out-of-Sample* (uji buta bergulir) lengkap dengan metrik *Walk-Forward Efficiency (WFE)* untuk membasmi *curve-fitting* / *overfitting*.
  * **Monte Carlo Simulation (2.500+ Runs)**: Pengacakan urutan transaksi (*Trade Reshuffling / Bootstrap*) + injeksi kejutan slippage acak untuk mengukur *Risk of Ruin* dan rentang *95% & 99% Confidence Interval Maximum Drawdown*.
* **🛠️ Pre-Code Siap Pakai & CLI Runner**:
  * Tersedia script modular mandiri di [`skills/backtest-strategy-optimizer/scripts/backtest_optimizer.py`](file:///c:/Users/ACER/Documents/GitHub/Trading%20AI%20Agent%20Skills/skills/backtest-strategy-optimizer/scripts/backtest_optimizer.py) yang dapat di-import atau dijalankan via CLI (`python backtest_optimizer.py --demo` atau `--csv <path>`).
* **🤖 Dukungan OpenCode v2**:
  * Ditambahkan `.opencode/agents/backtest-strategy-optimizer.md` dan integrasi pipeline orkestrasi kuantitatif di `trading-orchestrator`.

---

## 🇮🇩 Bahasa Indonesia

### 1. Ringkasan Eksekutif
**Trading AI Agent Skills Suite** bukanlah aplikasi tertutup (*black-box SaaS*) yang kaku, melainkan kumpulan modular **Agent Skills** terstandarisasi. Suite ini memberi AI Agent Anda kemampuan penuh untuk mencari dan mengunduh data pasar sendiri, menyadap siaran *running trade* langsung dari browser web trading pengguna, menganalisis saham menggunakan metode fundamental, teknikal, sentimen berita makro (NFP/CPI/BI-Rate), laporan posisi uang pintar **CFTC COT**, dan memproyeksikan lintasan harga probabilistik menggunakan model kecerdasan buatan **Google Research TimesFM**.

Semua sinyal eksekusi tunduk pada protokol **Human-in-the-Loop** (persetujuan eksplisit pengguna via Terminal CLI, Web Dashboard, atau Bot Telegram), dilengkapi simulasi **Paper Trading lokal (SQLite)** dengan ekspor otomatis ke **jurnal spreadsheet Excel (`.xlsx`)** dan visualisasi **Web Chart Mobile-View First**.

---

### 2. Cara Pemasangan Agent Skills (How to Install)

Anda dapat memasang kumpulan agent skills ini ke dalam workspace atau sistem AI Agent Anda menggunakan 3 metode mudah:

#### ⚡ Metode A: Menggunakan Perintah NPX Skills (Paling Praktis)
Jika lingkungan Anda mendukung NPX skills manager:
```bash
npx skills install https://github.com/lensetek/Trading-AI-Agent-Skills
```
*Atau pasang menggunakan CLI bawaan repositori ini:*
```bash
# Pasang ke workspace lokal saat ini:
npx trading-ai-agent-skills

# Atau pasang secara global ke direktori agent Antigravity/Gemini:
npx trading-ai-agent-skills --global
```

#### 💬 Metode B: Menggunakan Prompt Otomatis ke AI Agent
Cukup salin dan kirimkan prompt berikut ke AI Agent Anda (**Claude Code, Codex, Antigravity, OpenCode, Cursor, Windsurf**):

> **Prompt untuk AI Agent:**  
> *"Tolong pasang dan pelajari kumpulan agent skills dari repositori https://github.com/lensetek/Trading-AI-Agent-Skills ke dalam workspace ini. Kloning repositori tersebut, baca panduan README.md serta file SKILL.md di dalam direktori `skills/`, dan siapkan file konfigurasi `.env` dari `.env.example` untuk mode paper trading. Selain itu, buat file custom agent untuk OpenCode v2 di `.opencode/agents/` dengan mengonversi setiap `skills/*/SKILL.md` ke format agent OpenCode (termasuk frontmatter description), sambil tetap mempertahankan folder `skills/` untuk kompatibilitas lintas-agent."*

AI Agent Anda akan langsung mengkloning repo, membaca spesifikasi instruksi tiap sub-skill, dan mengaktifkan kemampuan analisis pasar secara otomatis.

#### 📦 Metode C: Kloning Manual via Git
```bash
# 1. Kloning repositori publik
git clone https://github.com/lensetek/Trading-AI-Agent-Skills.git
cd "Trading-AI-Agent-Skills"

# 2. Pasang pustaka dependensi Python
pip install -r requirements.txt

# 3. Siapkan file konfigurasi aman
cp .env.example .env
```

---

### 3. Daftar 13 Modul Sub-Skills

```
skills/
├── trading-orchestrator/          # Koordinator utama alur analisis & strategi
├── market-data-collector/         # Pengunduh data multi-market (IDX, Yahoo Fin, CCXT)
├── backtest-strategy-optimizer/   # Backtest vektorisasi, Genetic Algorithm, WFO, & Monte Carlo
├── browser-tape-interceptor/      # Sadap running trade web broker via Chrome CDP
├── orderflow-tape-scalper/        # Analisis tape reading, bid/ask depth, bandarmologi
├── timesfm-forecaster/            # AI Time Series Foundation Model Google TimesFM
├── cftc-cot-tracker/              # Pengunduh laporan CFTC COT & jembatan komoditas ke IDX
├── economic-news-trader/          # Kalender NFP, CPI, BI-Rate & pelindung slippage
├── technical-analyst/             # Price action, indikator klasik, SMC/ICT liquidity
├── fundamental-macro-analyst/     # Rasio lapkeu, valuasi emiten & korelasi makro (DXY/Yield)
├── paper-trading-engine/          # Simulator portofolio, trailing stop & ekspor Excel .xlsx
├── mobile-chart-server/           # Web dashboard lokal responsif (Mobile-View First)
└── agent-update-manager/          # Auto-updater 24 jam sekali dari GitHub resmi
```

| Modul | Peran & Kemampuan Utama |
| :--- | :--- |
| **`trading-orchestrator`** | Router pusat yang menerima instruksi bebas, mendistribusikan tugas ke spesialis, dan menyusun laporan trading plan utuh. |
| **`market-data-collector`** | Mengambil data harga historis dan intraday untuk Saham IDX, Crypto (Binance/Indodax via CCXT), Forex, dan Komoditas. |
| **`backtest-strategy-optimizer`** | Backtesting vektorisasi cepat, optimasi parameter Genetic Algorithm (GA), validasi Walk-Forward (WFA), dan stress test 2.500+ iterasi Monte Carlo. |
| **`browser-tape-interceptor`** | Menempelkan (*attach*) sesi browser pengguna via Chrome DevTools Protocol (CDP) untuk menangkap WebSocket running trade tanpa menyentuh password Anda. |
| **`orderflow-tape-scalper`** | Membaca tape secara real-time: deteksi *Hajar Kanan (Haka)* volume masif, *Iceberg Orders*, *Fake Bid/Ask*, dan *Broker Summary* (Bandarmologi). |
| **`timesfm-forecaster`** | Menjalankan model AI **Google TimesFM** (PyTorch) untuk membuat proyeksi pergerakan harga ke depan dan menghitung quantile probabilitas (P10, P50, P90). |
| **`cftc-cot-tracker`** | Mengunduh data resmi CFTC Commitment of Traders tiap akhir pekan, menghitung COT Index (0-100%), dan mengaitkan posisi komoditas global ke saham tambang/energi IDX. |
| **`economic-news-trader`** | Memantau rilis berita berdampak tinggi (NFP, Inflasi AS, Suku Bunga The Fed, BI 7-Day RR). Menerapkan *Pre-News Shield* dan *Post-Release Momentum Scalping*. |
| **`technical-analyst`** | Menghitung Moving Averages, RSI, MACD, Bollinger Bands, Supply & Demand, dan peta likuiditas Smart Money Concepts (SMC). |
| **`fundamental-macro-analyst`** | Menghitung rasio keuangan (PER, PBV, ROE, DER, DCF) dan menganalisis korelasi antar pasar (DXY vs Rupiah vs IHSG vs Yield US Treasury). |
| **`paper-trading-engine`** | Menjalankan simulasi transaksi lokal (SQLite), kalkulasi fee dan slippage realistis, manajemen trailing stop, dan otomatis membuat berkas **Excel (`.xlsx`)**. |
| **`mobile-chart-server`** | Server dashboard lokal mandiri berbasis FastAPI + TradingView Lightweight Charts dengan tampilan responsif berorientasi **Mobile-View First**. |
| **`agent-update-manager`** | Pengecekan pembaruan otomatis ke GitHub resmi 1x sehari (24h throttle cache) dengan proteksi kredensial .env dan konfirmasi pengguna. |

---

### 4. Fitur Unggulan Institusional

#### A. Integrasi Google Research TimesFM
Menggunakan fondasi model time-series decoder-only dari Google untuk memberikan proyeksi pergerakan harga tanpa perlu pelatihan manual (*zero-shot*). Menghasilkan batas bawah pesimis (Quantile P10) sebagai trailing stop dinamis berbasis statistik, garis median (P50) sebagai target utama, dan batas atas optimis (P90) untuk profit target.

#### B. CFTC COT Institutional Tracker (Komoditas ke Saham IDX)
Melacak arah uang institusi hedge fund dunia pada kontrak berjangka Emas (COMEX), Minyak Mentah (NYMEX), dan Tembaga. Data ini langsung dihubungkan ke saham emiten komoditas Bursa Efek Indonesia seperti **ANTM, MDKA, MEDC, ADRO, dan PTBA**.

#### C. Mode Intersepsi Browser Aman (Zero-Password-Risk)
Agent dapat menempel ke sesi Google Chrome pengguna yang sudah berjalan melalui `--remote-debugging-port=9222`. Anda melakukan login secara mandiri dengan keamanan biometrik/2FA Anda sendiri. Agent hanya membaca frame WebSocket untuk mengambil data running trade secara pasif tanpa menyimpan sandi Anda.

#### D. Engine Paper Trading & Ekspor Jurnal Excel Otomatis
Setiap eksekusi simulasi dicatat rapi ke dalam basis data SQLite lokal. Anda cukup memberi perintah: *"Buat jurnal trading minggu ini ke Excel"*, maka sistem akan menghasilkan spreadsheet `.xlsx` profesional dengan formula return, rasio Sharpe, Maximum Drawdown, dan kurva ekuitas.

---

### 5. Penggunaan Lintas Agen AI

#### A. Claude Code (Anthropic)
```bash
claude
# Di dalam prompt:
> Analisis saham BBCA menggunakan metode teknikal dan cek proyeksi TimesFM untuk 1 minggu ke depan.
```

#### B. OpenAI Codex / Custom Agent
```bash
codex --skill-path ./skills
```

#### C. Antigravity / Gemini CLI
Tambahkan path repositori ini ke dalam daftar plugin agent Antigravity Anda:
```bash
antigravity plugin add https://github.com/lensetek/Trading-AI-Agent-Skills
```

---

### 6. Keamanan Kredensial & Manajemen Risiko

> [!IMPORTANT]
> **Aturan Keamanan Baku:**
> 1. **Tidak Ada Kredensial di Client-Side:** Frontend web chart hanya menerima data harga dan grafik. Kunci API broker tidak pernah dikirim ke browser atau diakses dari client-side.
> 2. **Persetujuan Manusia Mutlak (Human-in-the-Loop):** Tidak ada transaksi beli atau jual yang dieksekusi secara sepihak oleh AI tanpa konfirmasi eksplisit dari pengguna.
> 3. **Perlindungan Berkas Rahasia:** Berkas `.env`, basis data transaksi `*.db`, dan berkas laporan `*.xlsx` secara ketat diabaikan oleh `.gitignore`.

---

<br/>

## 🇬🇧 English

### 1. Executive Summary
**Trading AI Agent Skills Suite** is not a rigid monolithic SaaS application, but a standardized collection of modular **Agent Skills**. This suite equips your AI coding agent with the full autonomy to autonomously search and download market data, intercept real-time *running trade* streams directly from your web trading broker session, analyze multi-market instruments using fundamental, technical, macro news sentiment (NFP/CPI/Interest Rates), institutional positioning reports (**CFTC COT**), and zero-shot probabilistic forecasting via **Google Research TimesFM**.

All trade execution is strictly governed by a **Human-in-the-Loop** safety gate (explicit user authorization via CLI Terminal, Web Dashboard, or Telegram Bot), backed by an offline **Paper Trading Engine (SQLite)** with automated export to **Excel (`.xlsx`) trade journals** and a **Mobile-View First Web Chart**.

---

### 2. How to Install Agent Skills

You can install this suite into your AI Agent's workspace using any of the following 3 straightforward methods:

#### ⚡ Method A: Via NPX Skills CLI (Recommended)
If using an agent skills manager:
```bash
npx skills install https://github.com/lensetek/Trading-AI-Agent-Skills
```
*Or install using the bundled CLI script:*
```bash
# Install to current local workspace:
npx trading-ai-agent-skills

# Or install globally to your system agent directory:
npx trading-ai-agent-skills --global
```

#### 💬 Method B: Via AI Agent Prompt (One-Click)
Copy and paste this prompt directly into your AI coding assistant (**Claude Code, Codex, Antigravity, OpenCode, Cursor, Windsurf**):

> **Agent Prompt:**  
> *"Please install and inspect the agent skills suite from https://github.com/lensetek/Trading-AI-Agent-Skills into this workspace. Clone the repository, review the README.md and SKILL.md files inside `./skills/`, and configure `.env` based on `.env.example` for paper trading mode. Also generate OpenCode v2 custom agents in `.opencode/agents/` by converting each `skills/*/SKILL.md` to OpenCode agent format (include description in frontmatter), while keeping the `skills/` folder intact for cross-agent compatibility."*

Your AI Agent will clone the repository, index the skills, and enable autonomous multi-market analysis immediately.

#### 📦 Method C: Manual Git Clone
```bash
git clone https://github.com/lensetek/Trading-AI-Agent-Skills.git
cd "Trading-AI-Agent-Skills"
pip install -r requirements.txt
cp .env.example .env
```

---

### 3. Suite of 13 Modular Skills

| Module | Core Purpose & Capabilities |
| :--- | :--- |
| **`trading-orchestrator`** | Master dispatcher receiving natural instructions, routing tasks to specialist skills, and compiling complete trading plans. |
| **`market-data-collector`** | Fetches historical and intraday market data for IDX Indonesian Stocks, Crypto (via CCXT), Forex, and Global Commodities. |
| **`backtest-strategy-optimizer`** | High-speed vectorized backtesting, Genetic Algorithm (GA) parameter optimization, Walk-Forward Analysis (WFA), and 2,500+ run Monte Carlo stress testing. |
| **`browser-tape-interceptor`** | Attaches to user's existing Chrome browser session via Chrome DevTools Protocol (CDP) to sniff running trade WebSockets safely. |
| **`orderflow-tape-scalper`** | Real-time tape reading: detects aggressive volume sweeps, Iceberg orders, Bid/Ask imbalances, and Broker Summary (Bandarmologi). |
| **`timesfm-forecaster`** | Runs **Google Research TimesFM** (PyTorch) for zero-shot time-series forecasting and probabilistic quantile bands (P10, P50, P90). |
| **`cftc-cot-tracker`** | Downloads weekly CFTC Commitment of Traders reports, computes COT Index (0-100%), and links global commodities to IDX mining/energy stocks. |
| **`economic-news-trader`** | Monitors high-impact events (NFP, US CPI, FOMC, BI 7-Day RR). Enforces *Pre-News Shield* and *Post-Release Momentum Scalping*. |
| **`technical-analyst`** | Computes MAs, RSI, MACD, Bollinger Bands, Supply & Demand levels, and Smart Money Concepts (SMC) liquidity sweeps. |
| **`fundamental-macro-analyst`** | Evaluates financial ratios (P/E, P/B, ROE, D/E, DCF) and analyzes intermarket macro correlations (DXY vs IDR vs Treasury Yields). |
| **`paper-trading-engine`** | Local trade simulator (SQLite), realistic fee/slippage modeling, dynamic trailing stop tracker, and automated **Excel (`.xlsx`)** journal generation. |
| **`mobile-chart-server`** | Standalone local web server powered by FastAPI + TradingView Lightweight Charts optimized for **Mobile-View First** touch interfaces. |
| **`agent-update-manager`** | Automated once-a-day update checker from GitHub (24h throttle cache) with strict credential isolation and human confirmation. |

---

### 4. Institutional-Grade Features

#### A. Google Research TimesFM Forecasting
Leverages Google's state-of-the-art decoder-only foundation model trained on billions of time points. Generates probabilistic forecasts with uncertainty intervals without fine-tuning: P10 quantile acts as a dynamic trailing stop, P50 as median expectation, and P90 as high-probability take profit targets.

#### B. CFTC COT Institutional Tracking
Monitors the real positioning of global hedge funds and commercial hedgers across Gold (COMEX), Crude Oil (NYMEX), and foreign currencies. Direct correlation models bridge global commodity positioning into Indonesian domestic stocks (**ANTM, MDKA, MEDC, ADRO, PTBA**).

#### C. Zero-Password-Risk Browser Interception
Through Chrome's `--remote-debugging-port=9222`, the agent attaches passively to your existing authenticated browser session. You log in manually with your own biometric/2FA security. The agent sniffs WebSocket running trade packets without ever seeing or storing your password.

#### D. Paper Trading Engine & Automated Excel Journaling
All simulated trades are recorded in an encrypted local SQLite database. Simply ask: *"Export this week's trading performance to Excel"*, and the engine outputs a formatted `.xlsx` workbook featuring Win Rate metrics, Sharpe Ratio, drawdown curves, and categorized trade logs.

---

### 5. Cross-Agent Usage

Each skill contains a standard `SKILL.md` declaration with semantic prompt parameters, enabling instant integration into:
- **Claude Code**: Run directly inside the workspace directory.
- **OpenAI Codex**: Point the `--skill-path` parameter to the `./skills` directory.
- **Antigravity / OpenCode / Cursor**: Include the repository in your agent's custom skills configuration.
- **OpenCode v2**: Custom agents are auto-generated in `.opencode/agents/` when installing via `npx trading-ai-agent-skills`, so you can invoke them with `@skill-name`.

---

### 6. Credential Safety & Risk Management

- **Zero Client-Side Exposure:** Private API keys, webhook URLs, and secrets reside strictly in `.env` and are never serialized to the frontend browser interface.
- **Mandatory Human-in-the-Loop:** Automated execution is disabled by default; every live or paper order requires affirmative user authorization (`Y/n`).
- **Git Shield:** Sensitive local databases (`*.db`), export spreadsheets (`*.xlsx`), and `.env` credentials are blocked by `.gitignore`.

---

### 📄 License
This project is licensed under the [MIT License](LICENSE).
