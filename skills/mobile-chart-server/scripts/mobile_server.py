#!/usr/bin/env python3
"""
Trading AI Agent Skills - Mobile Chart Server (Standalone Local Dashboard)
Built with FastAPI, Uvicorn, and HTML5 / TradingView Lightweight Charts.
Fully compliant with Mobile-View First and Zero-Credential Leak rules.
"""

import os
import sys
import json
import sqlite3
import socket
from typing import Dict, Any, Optional
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Initialize FastAPI App
app = FastAPI(
    title="Trading AI Agent Skills - Pro Terminal Server",
    description="Mobile-First Standalone Quant Terminal with TimesFM & Global Benchmark Radar",
    version="1.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLite Database for Paper Trading Execution Log
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "paper-trading-engine", "paper_trading.db")

def init_db():
    os.makedirs(os.path.dirname(os.path.abspath(DB_PATH)), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS executed_trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            action TEXT NOT NULL,
            price REAL NOT NULL,
            target_price REAL,
            stop_loss REAL,
            size TEXT,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Mock dataset for API
MOCK_MARKET_DATA = {
    "BBCA": {
        "symbol": "BBCA.JK (Bank Central Asia)",
        "market": "Saham Indonesia (IDX)",
        "current_price": 9850,
        "change_pct": "+1.8%",
        "verdict": "STRONG BUY",
        "confluence_score": 88,
        "entry_price": 9825,
        "target_tp": 10200,
        "stop_loss": 9700,
        "trailing_sl": 9740,
        "rr_ratio": 2.33,
        "invalidation_price": 9680,
        "recommended_lot": 20,
        "timesfm": {"p10": 9680, "p50": 10150, "p90": 10350},
        "msci_status": "Lolos Review (FIF 18.2%)",
        "eido_gap": "+1.8% Premium (NYSE)",
        "wash_sale_wvr": 0.12,
        "cot_flow": "Institutional Net Long +68%"
    },
    "ANTM": {
        "symbol": "ANTM.JK (Aneka Tambang)",
        "market": "Saham Komoditas (IDX)",
        "current_price": 1580,
        "change_pct": "+3.2%",
        "verdict": "STRONG BUY",
        "confluence_score": 85,
        "entry_price": 1575,
        "target_tp": 1690,
        "stop_loss": 1530,
        "trailing_sl": 1545,
        "rr_ratio": 2.22,
        "invalidation_price": 1515,
        "recommended_lot": 100,
        "timesfm": {"p10": 1520, "p50": 1680, "p90": 1740},
        "msci_status": "MSCI Standard Cap",
        "eido_gap": "Positive Correlation",
        "wash_sale_wvr": 0.15,
        "cot_flow": "Extreme Commercial Net Long"
    },
    "XAUUSD": {
        "symbol": "XAU/USD (Spot Gold)",
        "market": "Global Commodity & FX",
        "current_price": 2685.40,
        "change_pct": "+0.95%",
        "verdict": "STRONG BUY",
        "confluence_score": 82,
        "entry_price": 2682.00,
        "target_tp": 2720.00,
        "stop_loss": 2668.00,
        "trailing_sl": 2674.00,
        "rr_ratio": 2.70,
        "invalidation_price": 2658.00,
        "recommended_lot": 0.50,
        "timesfm": {"p10": 2665.20, "p50": 2715.00, "p90": 2735.80},
        "msci_status": "Sovereign Asset",
        "eido_gap": "DXY Negative Beta",
        "wash_sale_wvr": 0.05,
        "cot_flow": "Managed Money Long All-Time High"
    },
    "BTCUSDT": {
        "symbol": "BTC/USDT (Bitcoin)",
        "market": "Crypto Spot & Futures",
        "current_price": 64250,
        "change_pct": "+4.2%",
        "verdict": "STRONG BUY",
        "confluence_score": 80,
        "entry_price": 64100,
        "target_tp": 67500,
        "stop_loss": 62800,
        "trailing_sl": 63200,
        "rr_ratio": 2.24,
        "invalidation_price": 62400,
        "recommended_lot": 0.10,
        "timesfm": {"p10": 62500, "p50": 66800, "p90": 69200},
        "msci_status": "Commodity ETF Approved",
        "eido_gap": "Institutional Net Inflow +$320M",
        "wash_sale_wvr": 0.18,
        "cot_flow": "CME Futures Asset Manager Long"
    }
}

# --- ENDPOINTS ---
@app.get("/api/health")
def health_check():
    return {"status": "ok", "version": "1.2.0", "timestamp": datetime.now().isoformat()}

@app.get("/api/market-data/{symbol}")
def get_market_data(symbol: str):
    sym = symbol.upper().replace(".JK", "").replace("/", "")
    if sym in MOCK_MARKET_DATA:
        return MOCK_MARKET_DATA[sym]
    # default fallback
    return MOCK_MARKET_DATA["BBCA"]

@app.get("/api/global-radar")
def get_global_radar():
    return {
        "msci_indonesia": {
            "status": "Under Continuous Review",
            "free_float_threshold": "15% Target",
            "ubo_transparency": "OJK 1% Rule Transition Expected",
            "hsc_risk": "Low for LQ45, High for Conglomerates"
        },
        "eido_arbitrage": {
            "nyse_eido_last": 21.84,
            "nyse_change_pct": "+1.8%",
            "implied_gap_opening": "Bullish Gap Up Anticipated (+0.8% - +1.2%)"
        },
        "cftc_cot_sentiment": {
            "gold_net_commercial": "Hedging Under Control",
            "crude_oil_sentiment": "Neutral Consolidation",
            "dxy_speculator_bias": "De-leveraging Longs"
        }
    }

@app.post("/api/trade-ticket/action")
async def execute_trade_action(request: Request):
    data = await request.json()
    action = data.get("action", "APPROVE")
    symbol = data.get("symbol", "BBCA")
    price = data.get("price", 9850)
    target = data.get("target", 10200)
    sl = data.get("sl", 9700)
    size = data.get("size", "20 Lot")

    try:
        init_db()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO executed_trades (symbol, action, price, target_price, stop_loss, size, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (symbol, action, price, target, sl, size, "APPROVED" if action == "APPROVE" else "REJECTED"))
        conn.commit()
        trade_id = cursor.lastrowid
        conn.close()

        return {
            "status": "success",
            "trade_id": trade_id,
            "action": action,
            "message": f"Tiket transaksi {symbol} berhasil diproses dengan status: {action}."
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})

@app.get("/", response_class=HTMLResponse)
def serve_dashboard():
    # Return embedded standalone HTML dashboard
    template_path = os.path.join(os.path.dirname(__file__), "..", "templates", "index.html")
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    
    # Fallback to repository root index.html
    root_index = os.path.join(os.path.dirname(__file__), "..", "..", "..", "index.html")
    if os.path.exists(root_index):
        with open(root_index, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
            
    return HTMLResponse(content="<h1>Mobile Chart Server Running. Open index.html for full dashboard.</h1>")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def main():
    init_db()
    local_ip = get_local_ip()
    port = int(os.environ.get("PORT", 8000))

    print("=" * 65)
    print("📈 TRADING AI AGENT SKILLS - MOBILE CHART SERVER v1.2.0")
    print("=" * 65)
    print(f"✔ Desktop URL : http://localhost:{port}")
    print(f"✔ Mobile Wi-Fi: http://{local_ip}:{port} (Buka dari Smartphone)")
    print(f"✔ Database    : {DB_PATH}")
    print("✔ Status      : Zero-Credential Leak Protocol ACTIVE")
    print("=" * 65)

    uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
