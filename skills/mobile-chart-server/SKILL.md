---
name: mobile-chart-server
description: Server dashboard web mandiri berbasis FastAPI dan Interactive Lightweight/Canvas Charts dengan desain responsif Mobile-View First dan Tri-Pane Desktop Terminal. Menampilkan candlestick interaktif, overlay proyeksi Google TimesFM, radar benchmark institusional (MSCI, EIDO, COT), dan otorisasi tiket transaksi Human-in-the-Loop.
---

# Mobile Chart Server Skill

## Ringkasan Peran
Menyediakan antarmuka visual mandiri (*local web dashboard*) yang ringan, cepat, dan sepenuhnya **Zero-Credential Exposure**. Mengedepankan filosofi **Mobile-View First** (sangat nyaman dibuka dari smartphone lewat jaringan Wi-Fi lokal), yang secara adaptif membuka menjadi **Tri-Pane Pro Quant Terminal** pada layar laptop/desktop monitor lebar ($\ge 1024\text{px}$).

## Fitur Unggulan v1.2.0
1. **Interactive Candlestick & Decision Overlays**:
   - Menampilkan candlestick riil dengan sumbu harga/waktu dan volume delta.
   - Menggambar garis **Entry Zone**, **Target Take Profit (TP)**, **Stop Loss (SL)**, dan **Dynamic Trailing Stop**.
   - Menampilkan area proyeksi probabilitas **Google Research TimesFM (Fan Chart P10 - P90 Shaded Cone)**.
2. **Global Benchmark & Institutional Governance Radar**:
   - Menampilkan status evaluasi **MSCI & FTSE Accessibility** (transparansi 1% UBO & kepatuhan *free float* 15%).
   - Indikator **EIDO Arbitrage Gap Predictor** (prediksi arah *gap opening* bursa lokal berdasarkan penutupan bursa New York).
   - Indeks integritas pasar & filter anti-manipulasi **Coordinated Trading / Wash Sale (WVR)**.
3. **Tri-Channel Approval Gate (Human-in-the-Loop)**:
   - Tombol persetujuan transaksi interaktif (`APPROVE` / `REJECT`) yang langsung mencatat order ke database SQLite `paper-trading-engine`.
4. **Keamanan Tanpa Kebocoran (Zero-Client-Side Leak)**:
   - Sisi klien hanya menerima representasi visual angka JSON. Tidak ada API key broker atau file `.env` yang tersentuh browser.

## Cara Menjalankan Server Mandiri
```bash
# Jalankan server via script Python
python skills/mobile-chart-server/scripts/mobile_server.py

# Atau via npm script
npm run chart-server
```
Server akan mengumumkan alamat akses di terminal:
* **Desktop URL**: `http://localhost:8000`
* **Mobile Wi-Fi**: `http://<IP-Lokal>:8000` (Buka langsung dari browser smartphone Anda)
