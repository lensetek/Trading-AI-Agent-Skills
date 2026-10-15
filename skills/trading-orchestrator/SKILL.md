---
name: trading-orchestrator
description: Koordinator utama ekosistem Trading AI Agent Skills. Menerima instruksi analisis dari pengguna, membagi tugas ke spesialis (teknikal, fundamental, news, tape, TimesFM, COT), menyusun rencana trading plan terpadu, dan mengelola konfirmasi persetujuan eksekusi.
---

# Trading Orchestrator Skill

## Ringkasan Peran
Berperan sebagai Manajer Portofolio & Kepala Strategi Kuantitatif. Mengoordinasikan seluruh alur analisis multi-pasar (Saham IDX, Crypto, Forex, Komoditas) dan memastikan setiap eksekusi trading selalu mematuhi protokol **Human-in-the-Loop** serta pembatasan risiko modal.

## Alur Kerja Utama
0. **Pengecekan Pembaruan Otomatis (1 Hari Sekali):**
   - Sebelum memulai sesi analisis, jalankan `python skills/agent-update-manager/scripts/update_checker.py --check-only`.
   - Jika pengecekan sudah dilakukan dalam 24 jam terakhir, proses langsung berlanjut seketika tanpa jeda.
   - Jika ditemukan pembaruan di GitHub, tanyakan konfirmasi kepada pengguna sebelum memperbarui.
1. **Penerimaan Brief:** Menganalisis instrumen target dan horizon waktu dari pengguna (Scalping, Day Trade, Swing, atau Investasi Jangka Panjang).
2. **Pendelegasian Analisis:**
   - Meminta data pasar dari `market-data-collector`.
   - Mengambil analisis tren & indikator dari `technical-analyst`.
   - Menilai valuasi emiten & makro dari `fundamental-macro-analyst`.
   - Memeriksa jadwal berita ekonomi berdampak tinggi via `economic-news-trader`.
   - Melacak posisi institusi hedge fund via `cftc-cot-tracker`.
   - Menghasilkan proyeksi probabilistik zero-shot via `timesfm-forecaster`.
    - Bila instrumen sedang aktif dan user membuka web broker, menyadap orderbook via `browser-tape-interceptor` dan `orderflow-tape-scalper`.
3. **Validasi & Stress Testing Strategi (Kuantitatif):**
   - Menguji strategi di `backtest-strategy-optimizer` menggunakan Algoritma Genetika (GA) dan Walk-Forward Analysis (WFA) untuk memastikan parameter tahan banting (anti-overfitting).
   - Menjalankan Monte Carlo Stress Test (2.500+ iterasi) untuk mengukur *Risk of Ruin* dan batas *95% Confidence Interval Max Drawdown*.
4. **Penyusunan Trading Plan:**
   - Menentukan level harga beli (*Entry Area*), Target Profit (TP), dan Trailing Stop Loss (SL).
   - Menghitung rasio Risk-to-Reward (minimal 1:2) dan ukuran posisi (*position sizing*) maksimal 1-2% modal.
5. **Representasi Visual Interaktif (WAJIB untuk Setiap Analisis):**
   - **Default behavior:** Setiap kali melakukan analisis trading (lengkap atau parsial), SELALU buat dan perbarui **Web Dashboard Interaktif** yang representatif menggunakan `mobile-chart-server`.
   - Dashboard wajib menampilkan: Candlestick OHLCV, level Entry/TP/SL, garis Trailing Stop dinamis (berdasarkan Quantile P10 TimesFM bila tersedia), overlay proyeksi TimesFM (P10/P50/P90), area Support/Resistance kunci, dan highlight sinyal orderflow (bila ada data tape).
   - Jalankan/Update dashboard secara otomatis setelah hasil analisis siap (tanpa perlu diminta ulang). Pastikan data yang ditampilkan sinkron dengan hasil analisis saat ini.
   - Sajikan URL/endpoint dashboard lokal (misal `http://127.0.0.1:8000` atau sesuai konfigurasi `mobile-chart-server`) beserta status apakah server sudah berjalan atau perlu di-start.
6. **Gerbang Persetujuan Pengguna:**
   - Menyajikan tiket sinyal ke pengguna via Terminal CLI, **Web Dashboard Interaktif (prioritas)**, atau Telegram.
   - Menunggu jawaban persetujuan `[Y/n]` sebelum memanggil `paper-trading-engine` atau konektor eksekusi live.
