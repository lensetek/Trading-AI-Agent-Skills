---
name: agent-update-manager
description: Mengecek pembaruan (update) agent skills dari repositori resmi GitHub sekali sehari secara otomatis dengan pengaman kredensial dan persetujuan pengguna.
---

# Agent Update Manager Skill

## Ringkasan Peran
Bertugas sebagai pengawas pemeliharaan (*maintenance guardian*) yang memastikan kumpulan skill **Trading AI Agent Skills** selalu dalam versi termutakhir dari repositori resmi GitHub (`https://github.com/lensetek/Trading-AI-Agent-Skills`).

## Aturan Pembatasan 24 Jam (Once-A-Day Throttle)
- Untuk mencegah perlambatan eksekusi saat pengguna melakukan analisis trading, pengecekan pembaruan ke jaringan GitHub **hanya dilakukan maksimal 1 kali dalam 24 jam**.
- Status pengecekan disimpan dalam berkas stempel waktu lokal `.cache/last_update_check.json`.
- Jika waktu pengecekan terakhir kurang dari 24 jam, proses pengecekan langsung dilewati (*instant skip* < 5 milidetik).

## Protokol Keamanan Kredensial
- **Perlindungan Berkas Rahasia:** Pembaruan **TIDAK BOLEH** mengubah, menimpa, atau menghapus berkas `.env`, basis data SQLite lokal (`*.db`), atau berkas laporan jurnal Excel (`*.xlsx`).
- **Persetujuan Pengguna (Human-in-the-Loop):** Pembaruan repositori tidak dieksekusi secara sepihak. Agent wajib menyajikan ringkasan versi baru dan meminta konfirmasi `[Y/n]` sebelum menjalankan `git pull`.

## Alur Kerja (Workflow)
1. **Pemeriksaan Cache:** Membaca stempel waktu di `.cache/last_update_check.json`.
2. **Pengecekan Remote (Jika > 24 Jam):**
   - Menjalankan `python skills/agent-update-manager/scripts/update_checker.py --check-only`.
   - Mengambil informasi komit dan versi terbaru dari repositori GitHub.
3. **Notifikasi & Konfirmasi:**
   - Jika ada versi baru:
     ```text
     [PEMBARUAN TERSEDIA]
     Ada pembaruan resmi untuk Trading AI Agent Skills dari repositori GitHub.
     Versi Terbaru: [Versi Baru] | Rincian: [Ringkasan Perubahan]
     Apakah Anda ingin menerapkan pembaruan sekarang? [Setujui / Nanti]
     ```
4. **Penerapan Pembaruan:**
   - Jika pengguna menyetujui, jalankan:
     ```bash
     python skills/agent-update-manager/scripts/update_checker.py --apply
     ```
