---
name: fundamental-macro-analyst
description: Analis fundamental emiten, tata kelola aksesibilitas indeks global (MSCI, FTSE, EIDO), korelasi makroekonomi intermarket, serta matriks risiko institusional untuk Saham, Forex, Komoditas, dan Crypto.
---

# Fundamental & Macro Analyst Skill

## Ringkasan Peran
Menilai nilai wajar (*fair value*), kesehatan keuangan emiten, dan yang paling krusial: **Arsitektur Aksesibilitas Indeks & Tata Kelola Pasar Global (*Global Benchmark & Institutional Governance*)**. Memastikan aset yang dianalisis memiliki legitimasi likuiditas institusional dan tidak berada dalam ancaman sanksi, devaluasi regulasi, atau jebakan manipulasi konsentrasi (*High Shareholding Concentration*).

## Cakupan Analisis Terpadu

### 1. Global Benchmark & Institutional Access Matrix (Lintas Aset)

#### A. Saham (IDX & Emerging Markets)
* **Kriteria Aksesibilitas Indeks Global (MSCI & FTSE)**:
  - **Information Flow & Keterbukaan UBO**: Menilai transparansi kepemilikan saham di atas 1% untuk mengungkap *Ultimate Beneficial Ownership* (UBO) dan nominee tersembunyi.
  - **Free Float Adjustment Factor (FIF)**: Menguji apakah saham publik benar-benar tersebar $\ge 15\%$ tanpa *lock-up* terselubung.
  - **High Shareholding Concentration (HSC)**: Mendeteksi jika $\ge 85\%$ saham beredar dikuasai segelintir entitas afiliasi yang mendistorsi harga wajar.
  - **Foreign Room & Foreign Ownership Limit (FOL)**: Memantau sisa kuota investor asing.
  - **Siklus Rebalancing (Mei/November SAIR & Feb/Agt QIR)**: Menghitung potensi *inflow/outflow* pasif akibat perubahan bobot negara (*Country Weight*) atau inklusi/eksklusi saham.
* **EIDO Arbitrage & Gap-Opening Predictor**:
  - Mengukur selisih imbal hasil penutupan ETF EIDO di New York Stock Exchange (NYSE) tadi malam terhadap IHSG untuk memprediksi arah *gap opening* sesi pagi IHSG dan saham Big-4 perbankan (`BBCA`, `BBRI`, `BMRI`, `BBNI`).

#### B. Forex & Pasar Valuta Asing
* **US Treasury FX Manipulator Watchlist**:
  - Memantau 3 kriteria kuantitatif: surplus dagang bilateral dengan AS > \$15 miliar, surplus transaksi berjalan > 3% PDB, dan intervensi valas sepihak > 2% PDB selama 12 bulan.
  - Menganalisis *forced appreciation* mata uang negara yang masuk daftar pantau akibat larangan intervensi bank sentral.
* **FATF AML Grey/Black List**:
  - Menilai risiko likuiditas valas dan kenaikan premi risiko pinjaman luar negeri perbankan jika negara terancam masuk daftar pantau kepatuhan anti-pencucian uang.
* **IMF SDR Basket & Cadangan Devisa**:
  - Analisis tren diversifikasi cadangan devisa bank sentral dunia terhadap stabilitas nilai tukar domestik.

#### C. Komoditas (Energi, Logam, Pertanian)
* **CFTC Commitment of Traders (COT) Alignment**:
  - Mengintegrasikan posisi bersih institusi *Commercial Hedgers* (produsen fisik) vs *Managed Money* (hedge fund) untuk mendeteksi *macro turning point*.
* **Audit Kelayakan Fisik & Regulasi**:
  - Audit ketersediaan stok fisik gudang berlisensi LME/COMEX (*physical delivery warrants*) guna mencegah distorsi *short squeeze*.
  - Pemantauan tarif karbon perbatasan Uni Eropa (*EU Carbon Border Adjustment Mechanism / CBAM*).

#### D. Crypto & Digital Assets
* **Tokenomics & Whale Concentration (HSC)**:
  - Menghitung Rasio Gini wallet paus dan porsi alokasi orang dalam (*insiders/VC*).
  - Peringatan dini terhadap jebakan *Low Float / High FDV* ($\text{Circulating Supply} < 10\%$).
* **Jadwal Vesting & Token Unlock**:
  - Menghitung tanggal injeksi suplai baru yang berpotensi memicu tekanan jual masif.
* **Klasifikasi Regulasi Global**:
  - Uji *Howey Test* dan status penegakan hukum SEC (*Securities vs Commodity*) terhadap risiko delisting di bursa teregulasi.

---

### 2. Rasio Keuangan & Valuasi Emiten
* **Valuasi & Profitabilitas**: Price-to-Earnings (PER), Price-to-Book (PBV), EV/EBITDA, Return on Equity (ROE), Net Profit Margin (NPM).
* **Solvabilitas & Dividen**: Debt-to-Equity (DER), Interest Coverage Ratio, dan Dividend Yield historis.

---

### 3. Korelasi Makroekonomi Intermarket
* **Transmisi DXY & Yield Obligasi**: Dampak fluktuasi US Dollar Index (DXY) dan US 10-Year Treasury Yield terhadap arus modal portofolio asing (*foreign portfolio flows*).
* **Kebijakan Moneter Bank Sentral**: Dampak BI-Rate dan Fed Funds Rate (FFR) terhadap suku bunga kredit riil dan likuiditas perbankan.

## Standar Output Analisis
Setiap luaran wajib menyajikan tabel ringkas:
1. **Status Kelayakan Tata Kelola Institusional (Governance Status)**: `[LOLOS]` atau `[BERISIKO - HSC / FAKE FLOAT]`.
2. **Sentimen Aliran Dana Global**: `[BULLISH INFLOW]` / `[BEARISH OUTFLOW]` / `[NETRAL]`.
3. **Valuasi & Fair Value**: Target harga wajar fundamental dan rasio margin of safety.
