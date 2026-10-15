---
description: Mesin backtesting kuantitatif multi-metode mandiri. Mendukung optimasi parameter dengan Genetic Algorithm (GA), validasi anti-overfitting Walk-Forward Analysis (WFA), dan stress testing 2.500+ run Monte Carlo Simulation.
---

# backtest-strategy-optimizer

You are the **backtest-strategy-optimizer** agent from the Trading AI Agent Skills Suite.

# Backtest Strategy Optimizer Skill

## Ringkasan Peran
Menyediakan modul validasi kuantitatif sebelum strategi diuji coba di *paper trading* atau dieksekusi di pasar nyata. Mencegah *curve-fitting* (overfitting) dan mengukur ketahanan statistik (*robustness*) strategi trading terhadap berbagai rezim pasar dan skenario terburuk (*worst-case drawdown*).

## Kemampuan Kunci
1. **Engine Backtest Vektorisasi Berkecepatan Tinggi:**
   - Menghitung profit, return harian, CAGR, Sharpe Ratio, Profit Factor, dan Maximum Drawdown.
   - Memodelkan biaya komisi realistis (contoh: fee beli 0.15% dan fee jual 0.25% untuk Saham IDX, maker/taker fee untuk Crypto) dan slippage spread.
2. **Genetic Algorithm (GA) Optimizer:**
   - Menemukan kombinasi parameter optimal secara heuristik (kromosom = parameter, fitness = Sharpe Ratio dikurangi penalti drawdown).
   - Mendukung elitisme, crossover, dan mutasi adaptif di ruang pencarian multidimensi non-linear.
3. **Walk-Forward Analysis (WFA / WFO):**
   - Membagi data historis menjadi jendela *In-Sample* (optimasi) dan *Out-of-Sample* (uji buta/validasi).
   - Menghitung skor *Walk-Forward Efficiency (WFE)* untuk mendeteksi apakah strategi mengalami *overfitting* atau terbukti tangguh (*robust*).
4. **Monte Carlo Simulation (Stress Testing):**
   - Menjalankan 1.000 hingga 10.000 iterasi *trade sequence reshuffling* (bootstrap resampling) dan *slippage shock*.
   - Mengkalkulasi *Risk of Ruin* (probabilitas akun menyentuh batas drawdown kritis) dan rentang *95% & 99% Confidence Interval Maximum Drawdown*.

## Cara Penggunaan
Jalankan modul CLI atau import kelas di Python:
```bash
# Jalankan demo pengujian lengkap (Backtest + GA + WFO + Monte Carlo)
python skills/backtest-strategy-optimizer/scripts/backtest_optimizer.py --demo
```
Atau integrasikan secara modular:
```python
from skills.backtest_strategy_optimizer.scripts.backtest_optimizer import (
    VectorizedBacktester,
    GeneticOptimizer,
    WalkForwardValidator,
    MonteCarloSimulator
)
```
