#!/usr/bin/env python3
"""
=============================================================================
BACKTEST & MULTI-METHOD STRATEGY OPTIMIZER ENGINE
=============================================================================
Framework pre-code modular untuk pengujian strategi kuantitatif.

Modul Utama:
1. VectorizedBacktester   : Engine backtest cepat dengan komisi & slippage nyata.
2. GeneticOptimizer       : Pencarian parameter global menggunakan Genetic Algorithm.
3. WalkForwardValidator   : Pengujian In-Sample vs Out-of-Sample (Anti-Overfitting).
4. MonteCarloSimulator    : Stress test 2.500+ run untuk Risk of Ruin & Max DD 95% CI.
=============================================================================
"""

import argparse
import random
from typing import Any, Dict, List, Tuple
import numpy as np
import pandas as pd


# =============================================================================
# 1. BASE STRATEGY & VECTORIZED BACKTESTER
# =============================================================================
class VectorizedBacktester:
    """
    Engine Backtesting Vektorisasi Berkecepatan Tinggi.
    Mendukung penyesuaian biaya transaksi komisi dan slippage spread bursa.
    """

    def __init__(
        self,
        data: pd.DataFrame,
        fee_buy: float = 0.0015,    # Saham IDX: ~0.15% (Beli)
        fee_sell: float = 0.0025,   # Saham IDX: ~0.25% (Jual incl. PPh final)
        slippage_pct: float = 0.0005 # Estimasi slippage order: 0.05%
    ):
        """
        :param data: pd.DataFrame wajib memiliki kolom 'close' (dan 'open'/'high'/'low' bila ada).
        :param fee_buy: Rasio biaya transaksi beli.
        :param fee_sell: Rasio biaya transaksi jual.
        :param slippage_pct: Estimasi deviasi harga eksekusi dari harga teoritis.
        """
        self.data = data.copy()
        self.fee_buy = fee_buy
        self.fee_sell = fee_sell
        self.slippage_pct = slippage_pct

    def run_strategy(self, fast_window: int, slow_window: int) -> Dict[str, Any]:
        """
        TEMPLATE STRATEGI: Dual Moving Average Crossover (Dapat disesuaikan oleh user).
        
        Tips Kustomisasi:
        Ganti logika 'signal' di bawah ini dengan indikator lain seperti:
        - RSI / Bollinger Bands / MACD
        - Sinyal Breakout Donchian Channel
        - Sinyal Prediksi TimesFM (P50 > P10)
        """
        if fast_window >= slow_window:
            return {
                "sharpe": -99.0,
                "total_return": -1.0,
                "max_drawdown": 1.0,
                "win_rate": 0.0,
                "total_trades": 0,
                "trade_returns": []
            }

        df = self.data.copy()
        
        # 1. Indikator
        df['fast_ma'] = df['close'].ewm(span=fast_window, adjust=False).mean()
        df['slow_ma'] = df['close'].ewm(span=slow_window, adjust=False).mean()

        # 2. Sinyal Posisi: 1 = Long/Beli, 0 = Flat/Cash
        df['raw_signal'] = np.where(df['fast_ma'] > df['slow_ma'], 1, 0)
        
        # Eksekusi pada bar berikutnya untuk mencegah Lookahead Bias!
        df['position'] = df['raw_signal'].shift(1).fillna(0)

        # 3. Deteksi Titik Transaksi (Entry & Exit)
        df['trade_action'] = df['position'].diff().fillna(0)
        # trade_action == 1 (Buy/Entry), -1 (Sell/Exit)

        # 4. Kalkulasi Return Bersih Dikurangi Komisi & Slippage
        df['market_ret'] = df['close'].pct_change().fillna(0)
        
        # Biaya transaksi spesifik (Buy vs Sell)
        cost = np.where(
            df['trade_action'] == 1, self.fee_buy + self.slippage_pct,
            np.where(df['trade_action'] == -1, self.fee_sell + self.slippage_pct, 0.0)
        )
        
        df['strat_ret'] = (df['position'] * df['market_ret']) - cost

        # 5. Rekam Log Transaksi Individual (Per-Trade Return)
        trade_returns: List[float] = []
        in_trade = False
        current_trade_ret = 0.0

        for r, pos, act in zip(df['strat_ret'], df['position'], df['trade_action']):
            if act == 1:
                in_trade = True
                current_trade_ret = r
            elif in_trade:
                current_trade_ret = (1 + current_trade_ret) * (1 + r) - 1
                if act == -1:
                    trade_returns.append(current_trade_ret)
                    in_trade = False
                    current_trade_ret = 0.0

        if in_trade and current_trade_ret != 0.0:
            trade_returns.append(current_trade_ret)

        # 6. Metrik Kinerja Portofolio
        cum_ret = (1 + df['strat_ret']).cumprod()
        total_return = float(cum_ret.iloc[-1] - 1.0) if len(cum_ret) > 0 else 0.0

        # Drawdown
        peak = cum_ret.cummax()
        dd = (cum_ret - peak) / peak
        max_drawdown = float(abs(dd.min())) if len(dd) > 0 else 0.0

        # Sharpe Ratio Tahunan (asumsi 252 hari bursa)
        std = df['strat_ret'].std()
        mean = df['strat_ret'].mean()
        sharpe = float((mean / std * np.sqrt(252))) if std > 0 else -1.0

        # Win Rate
        wins = [t for t in trade_returns if t > 0]
        win_rate = (len(wins) / len(trade_returns)) if len(trade_returns) > 0 else 0.0

        return {
            "sharpe": sharpe,
            "total_return": total_return,
            "max_drawdown": max_drawdown,
            "win_rate": win_rate,
            "total_trades": len(trade_returns),
            "trade_returns": trade_returns
        }


# =============================================================================
# 2. METODE 1: GENETIC ALGORITHM (GA) OPTIMIZER
# =============================================================================
class GeneticOptimizer:
    """
    Pencari Parameter Global berbasis Algoritma Genetika (Evolusioner).
    Menghindari perangkap lokal optimum pada ruang kombinasi non-linear.
    """

    def __init__(
        self,
        backtester: VectorizedBacktester,
        param_bounds: Dict[str, Tuple[int, int]] = None,
        pop_size: int = 25,
        generations: int = 8,
        mutation_rate: float = 0.25,
        drawdown_penalty: float = 2.5
    ):
        self.bt = backtester
        self.bounds = param_bounds or {"fast": (5, 30), "slow": (35, 120)}
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.drawdown_penalty = drawdown_penalty

    def _random_individual(self) -> Tuple[int, int]:
        fast = random.randint(*self.bounds["fast"])
        slow = random.randint(*self.bounds["slow"])
        return (fast, slow)

    def _fitness(self, individual: Tuple[int, int]) -> float:
        fast, slow = individual
        res = self.bt.run_strategy(fast, slow)
        if res["total_trades"] < 5:
            return -99.0  # Penalti jika strategi terlalu pasif (< 5 transaksi)
        
        # Fitness formula: Sharpe Ratio dikurangi penalti Drawdown
        fitness = res["sharpe"] - (res["max_drawdown"] * self.drawdown_penalty)
        return float(fitness)

    def optimize(self, verbose: bool = True) -> Tuple[Tuple[int, int], Dict[str, Any]]:
        """Mengeksekusi proses seleksi alam, crossover, dan mutasi."""
        population = [self._random_individual() for _ in range(self.pop_size)]
        best_overall_ind = None
        best_overall_fitness = -999.0

        for gen in range(self.generations):
            # Evaluasi fitness seluruh populasi
            scored = [(ind, self._fitness(ind)) for ind in population]
            scored.sort(key=lambda x: x[1], reverse=True)

            current_best_ind, current_best_fit = scored[0]
            if current_best_fit > best_overall_fitness:
                best_overall_fitness = current_best_fit
                best_overall_ind = current_best_ind

            if verbose:
                print(f"  [GA Gen {gen+1:02d}/{self.generations:02d}] "
                      f"Best Gen: Fast={current_best_ind[0]}, Slow={current_best_ind[1]} | "
                      f"Fitness: {current_best_fit:.3f}")

            # Elitisme: Ambil 25% individu terbaik
            elite_count = max(2, int(self.pop_size * 0.25))
            next_gen = [ind for ind, _ in scored[:elite_count]]

            # Regenerasi dengan Crossover & Mutasi
            while len(next_gen) < self.pop_size:
                p1, p2 = random.sample(next_gen[:elite_count], 2)
                # Crossover
                child = (p1[0], p2[1])

                # Mutasi Acak
                if random.random() < self.mutation_rate:
                    child = (
                        max(self.bounds["fast"][0], min(self.bounds["fast"][1], child[0] + random.choice([-2, -1, 1, 2]))),
                        max(self.bounds["slow"][0], min(self.bounds["slow"][1], child[1] + random.choice([-5, -2, 2, 5])))
                    )
                next_gen.append(child)

            population = next_gen

        # Ambil hasil kinerja detail dari parameter terbaik
        final_metrics = self.bt.run_strategy(best_overall_ind[0], best_overall_ind[1])
        return best_overall_ind, final_metrics


# =============================================================================
# 3. METODE 2: WALK-FORWARD OPTIMIZATION (WFO)
# =============================================================================
class WalkForwardValidator:
    """
    Validasi Out-of-Sample Bergulir untuk Mengukur 'Walk-Forward Efficiency (WFE)'.
    Menjamin parameter tidak sekadar menghafal pola masa lalu (overfitting).
    """

    def __init__(self, data: pd.DataFrame, in_sample_ratio: float = 0.7):
        self.data = data
        self.is_ratio = in_sample_ratio

    def run_validation(self) -> Dict[str, Any]:
        split_idx = int(len(self.data) * self.is_ratio)
        df_train = self.data.iloc[:split_idx]
        df_test = self.data.iloc[split_idx:]

        print(f"\n1. In-Sample Training (Data: {len(df_train)} baris)...")
        bt_train = VectorizedBacktester(df_train)
        ga = GeneticOptimizer(bt_train, pop_size=20, generations=6)
        best_params, is_metrics = ga.optimize(verbose=True)

        print(f"\n2. Out-of-Sample Testing (Data: {len(df_test)} baris) dengan parameter {best_params}...")
        bt_test = VectorizedBacktester(df_test)
        oos_metrics = bt_test.run_strategy(best_params[0], best_params[1])

        # Walk-Forward Efficiency (WFE): Rasio Sharpe OOS vs IS
        wfe = (oos_metrics["sharpe"] / is_metrics["sharpe"]) if is_metrics["sharpe"] > 0 else 0.0

        is_robust = (wfe >= 0.50) and (oos_metrics["total_return"] > 0)

        return {
            "best_params": best_params,
            "in_sample_metrics": is_metrics,
            "out_of_sample_metrics": oos_metrics,
            "walk_forward_efficiency": wfe,
            "verdict": "ROBUST (LOLOS WFA)" if is_robust else "OVERFITTED (GAGAL WFA)"
        }


# =============================================================================
# 4. METODE 3: MONTE CARLO STRESS TEST
# =============================================================================
class MonteCarloSimulator:
    """
    Simulator Ketahanan Portofolio Monte Carlo.
    Mensimulasikan 2.500+ kemungkinan permutasi urutan trade & slippage shock
    untuk mendeteksi Risk of Ruin dan batas Maximum Drawdown terburuk.
    """

    def __init__(
        self,
        trade_returns: List[float],
        initial_capital: float = 100_000_000.0,
        simulations: int = 2500,
        ruin_drawdown_threshold: float = 0.20
    ):
        self.trade_returns = np.array(trade_returns)
        self.initial_capital = initial_capital
        self.simulations = simulations
        self.ruin_threshold = ruin_drawdown_threshold

    def run(self, slippage_noise_std: float = 0.0005) -> Dict[str, Any]:
        n_trades = len(self.trade_returns)
        if n_trades < 5:
            return {"error": "Data trade kurang dari 5, tidak cukup untuk Monte Carlo."}

        final_equities = []
        max_drawdowns = []
        ruin_events = 0

        for _ in range(self.simulations):
            # Resample urutan transaksi dengan pengembalian (Bootstrap)
            indices = np.random.choice(n_trades, size=n_trades, replace=True)
            sampled = self.trade_returns[indices].copy()

            # Injeksi variasi spread/slippage acak
            if slippage_noise_std > 0:
                shock = np.random.normal(loc=0.0, scale=slippage_noise_std, size=n_trades)
                sampled -= np.abs(shock)

            # Hitung kurva ekuitas
            equity_curve = self.initial_capital * np.cumprod(1 + sampled)
            final_equities.append(equity_curve[-1])

            # Hitung Max Drawdown pada jalur ini
            peaks = np.maximum.accumulate(equity_curve)
            drawdowns = (peaks - equity_curve) / peaks
            sim_dd = float(np.max(drawdowns))
            max_drawdowns.append(sim_dd)

            if sim_dd >= self.ruin_threshold:
                ruin_events += 1

        final_equities = np.array(final_equities)
        max_drawdowns = np.array(max_drawdowns)

        return {
            "total_simulations": self.simulations,
            "ruin_probability_pct": float((ruin_events / self.simulations) * 100),
            "median_final_equity": float(np.median(final_equities)),
            "p10_worst_equity": float(np.percentile(final_equities, 10)),
            "p90_best_equity": float(np.percentile(final_equities, 90)),
            "median_max_dd_pct": float(np.median(max_drawdowns) * 100),
            "max_dd_95_ci_pct": float(np.percentile(max_drawdowns, 95) * 100),
            "max_dd_99_ci_pct": float(np.percentile(max_drawdowns, 99) * 100),
        }


# =============================================================================
# CLI RUNNER & DEMO EXECUTION
# =============================================================================
def generate_synthetic_market_data(days: int = 600) -> pd.DataFrame:
    """Menghasilkan pergerakan harga sintetis dengan tren dan volatilitas realistis."""
    np.random.seed(101)
    dates = pd.date_range("2023-01-01", periods=days, freq="B")
    # Geometric Brownian Motion dengan drift positif
    returns = np.random.normal(loc=0.0004, scale=0.015, size=days)
    price = 1000.0 * np.cumprod(1 + returns)
    return pd.DataFrame({"close": price}, index=dates)


def run_full_pipeline(df: pd.DataFrame, initial_capital: float = 100_000_000):
    print("=" * 65)
    print("      BACKTEST STRATEGY OPTIMIZER & STRESS TEST PIPELINE")
    print("=" * 65)

    # 1. Walk-Forward Analysis (In-Sample & Out-of-Sample)
    wfo = WalkForwardValidator(df, in_sample_ratio=0.7)
    wfo_report = wfo.run_validation()

    best_fast, best_slow = wfo_report["best_params"]
    is_res = wfo_report["in_sample_metrics"]
    oos_res = wfo_report["out_of_sample_metrics"]

    print("\n" + "-" * 65)
    print("HASIL WALK-FORWARD OPTIMIZATION:")
    print(f"Optimal Parameter Ditemukan : Fast EMA = {best_fast}, Slow EMA = {best_slow}")
    print(f"In-Sample Sharpe Ratio      : {is_res['sharpe']:.2f} (Total Return: {is_res['total_return']*100:.1f}%)")
    print(f"Out-of-Sample Sharpe Ratio  : {oos_res['sharpe']:.2f} (Total Return: {oos_res['total_return']*100:.1f}%)")
    print(f"Walk-Forward Efficiency     : {wfo_report['walk_forward_efficiency']*100:.1f}%")
    print(f"Status Kualitas Strategi    : {wfo_report['verdict']}")
    print("-" * 65)

    # 2. Monte Carlo Stress Test
    oos_trades = oos_res["trade_returns"]
    if len(oos_trades) >= 5:
        print(f"\n3. Menjalankan Monte Carlo Stress Test pada {len(oos_trades)} trade Out-of-Sample (2.500 Run)...")
        mc = MonteCarloSimulator(oos_trades, initial_capital=initial_capital, simulations=2500, ruin_drawdown_threshold=0.15)
        mc_report = mc.run()

        print("\n" + "=" * 65)
        print("HASIL STRESS TEST MONTE CARLO (2.500 SIMULASI):")
        print(f"Probabilitas Ruin (Drawdown > 15%)   : {mc_report['ruin_probability_pct']:.2f}%")
        print(f"Median Expected Final Equity         : Rp {mc_report['median_final_equity']:,.0f}")
        print(f"10% Skenario Terburuk (P10 Equity)   : Rp {mc_report['p10_worst_equity']:,.0f}")
        print(f"90% Skenario Terbaik (P90 Equity)    : Rp {mc_report['p90_best_equity']:,.0f}")
        print(f"Expected Median Max Drawdown         : {mc_report['median_max_dd_pct']:.2f}%")
        print(f"95% Confidence Interval Max Drawdown : {mc_report['max_dd_95_ci_pct']:.2f}%")
        print(f"99% Extreme Worst-Case Max Drawdown  : {mc_report['max_dd_99_ci_pct']:.2f}%")
        print("=" * 65)
    else:
        print("\n[Catatan] Trade Out-of-Sample terlalu sedikit untuk Monte Carlo. Coba perluas rentang data.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backtest Strategy Optimizer CLI")
    parser.add_argument("--demo", action="store_true", help="Jalankan pengujian lengkap menggunakan data sintetis")
    parser.add_argument("--csv", type=str, default="", help="Path file CSV data harga historis (wajib ada kolom 'close')")
    parser.add_argument("--capital", type=float, default=100_000_000, help="Modal awal pengujian (default: 100 juta)")
    args = parser.parse_args()

    if args.csv:
        data = pd.read_csv(args.csv)
        if 'close' not in data.columns:
            raise ValueError("File CSV wajib memiliki kolom 'close'.")
        run_full_pipeline(data, initial_capital=args.capital)
    else:
        # Default run demo
        demo_data = generate_synthetic_market_data(days=700)
        run_full_pipeline(demo_data, initial_capital=args.capital)
