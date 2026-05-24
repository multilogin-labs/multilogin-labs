#!/usr/bin/env python3
"""Connect Selenium to a running Multilogin profile via Chrome debugger.

Usage:
    1. Start profile with automation enabled
    2. python scripts/python/selenium_connect.py
"""
from __future__ import annotations

import os
import sys

from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv("MULTILOGIN_DEBUG_PORT", "35000")


def main() -> None:
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
    except ImportError:
        print("Install: pip install selenium", file=sys.stderr)
        sys.exit(1)

    options = Options()
    options.add_experimental_option("debuggerAddress", f"127.0.0.1:{PORT}")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://browserleaks.com/ip")
        print("Connected. Page title:", driver.title)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
