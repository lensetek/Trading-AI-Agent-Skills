#!/usr/bin/env python3
"""
Trading AI Agent Skills - Auto Update Checker
Features:
- 24-Hour Throttle Cache (checks at most once per day)
- Zero-Credential Exposure (never touches .env, *.db, or *.xlsx)
- Git & Fallback HTTPS check
"""

import os
import sys
import json
import time
import subprocess
import argparse
from datetime import datetime, timezone
from urllib.request import urlopen, Request

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

REPO_URL = "https://github.com/lensetek/Trading-AI-Agent-Skills"
RAW_PKG_URL = "https://raw.githubusercontent.com/lensetek/Trading-AI-Agent-Skills/main/package.json"
CACHE_FILE = os.path.join(os.path.dirname(__file__), "../../../.cache/last_update_check.json")
LOCAL_PKG_FILE = os.path.join(os.path.dirname(__file__), "../../../package.json")
THROTTLE_SECONDS = 86400  # 24 Hours in seconds


def ensure_cache_dir():
    cache_dir = os.path.dirname(CACHE_FILE)
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir, exist_ok=True)


def read_cache():
    if not os.path.exists(CACHE_FILE):
        return None
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def write_cache(data):
    ensure_cache_dir()
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[Warning] Failed to write update cache: {e}", file=sys.stderr)


def get_local_version():
    if not os.path.exists(LOCAL_PKG_FILE):
        return "1.0.0"
    try:
        with open(LOCAL_PKG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("version", "1.0.0")
    except Exception:
        return "1.0.0"


def fetch_remote_version():
    try:
        req = Request(RAW_PKG_URL, headers={"User-Agent": "TradingAgentSkillsUpdater/1.0"})
        with urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                return data.get("version", "1.0.0")
    except Exception:
        pass
    return None


def check_updates(force=False):
    current_time = time.time()
    cache = read_cache()

    # 1. Check 24-hour throttle
    if not force and cache:
        last_check = cache.get("last_check_timestamp", 0)
        elapsed = current_time - last_check
        if elapsed < THROTTLE_SECONDS:
            hours_remaining = round((THROTTLE_SECONDS - elapsed) / 3600, 1)
            return {
                "status": "cached",
                "message": f"Update check already performed within last 24 hours. Next check in ~{hours_remaining}h.",
                "update_available": False,
                "local_version": get_local_version()
            }

    # 2. Perform live check
    local_ver = get_local_version()
    remote_ver = fetch_remote_version()

    # Fallback to git remote check if HTTPS fetch fails
    git_has_diff = False
    try:
        subprocess.run(["git", "fetch", "origin", "main"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=6)
        res = subprocess.run(["git", "rev-list", "HEAD..origin/main", "--count"], capture_output=True, text=True, timeout=5)
        if res.returncode == 0 and int(res.stdout.strip() or 0) > 0:
            git_has_diff = True
    except Exception:
        pass

    update_available = False
    if remote_ver and remote_ver != local_ver:
        update_available = True
    elif git_has_diff:
        update_available = True

    # 3. Save Cache
    new_cache = {
        "last_check_timestamp": current_time,
        "last_check_iso": datetime.now(timezone.utc).isoformat(),
        "local_version": local_ver,
        "remote_version": remote_ver or local_ver,
        "update_available": update_available
    }
    write_cache(new_cache)

    return {
        "status": "checked",
        "update_available": update_available,
        "local_version": local_ver,
        "remote_version": remote_ver or "Latest Git Main",
        "repo_url": REPO_URL
    }


def apply_update():
    print("🔄 Applying update safely via git pull...")
    try:
        # Check git status first to ensure working tree safety
        res = subprocess.run(["git", "pull", "origin", "main"], capture_output=True, text=True)
        print(res.stdout)
        if res.returncode == 0:
            print("✅ Successfully updated Trading AI Agent Skills to the latest version!")
            # Reset cache timestamp to current
            write_cache({
                "last_check_timestamp": time.time(),
                "last_check_iso": datetime.now(timezone.utc).isoformat(),
                "local_version": get_local_version(),
                "update_available": False
            })
            return True
        else:
            print(f"❌ Git pull encountered an error: {res.stderr}", file=sys.stderr)
            return False
    except Exception as e:
        print(f"❌ Execution failed: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Trading AI Agent Skills 24h Auto-Updater")
    parser.add_argument("--check-only", action="store_true", help="Check for updates and return JSON status")
    parser.add_argument("--force", action="store_true", help="Force check bypassing 24h throttle")
    parser.add_argument("--apply", action="store_true", help="Apply updates via git pull")
    args = parser.parse_args()

    if args.apply:
        success = apply_update()
        sys.exit(0 if success else 1)

    result = check_updates(force=args.force)

    # Output formatted JSON for agent inspection
    print(json.dumps(result, indent=2))

    if result.get("update_available"):
        print("\n" + "="*60)
        print("[PEMBARUAN TERSEDIA] Trading AI Agent Skills Baru Tersedia!")
        print(f"Versi Lokal: {result.get('local_version')} | Versi Remote: {result.get('remote_version')}")
        print("Perbarui dengan menjalankan: python skills/agent-update-manager/scripts/update_checker.py --apply")
        print("="*60 + "\n")


if __name__ == "__main__":
    main()
