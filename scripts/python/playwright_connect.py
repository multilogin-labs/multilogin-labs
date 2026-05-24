#!/usr/bin/env python3
"""Connect Playwright to a running Multilogin profile over CDP.

Usage:
    1. Start profile (app or launch_profile.py)
    2. python scripts/python/playwright_connect.py
"""
from __future__ import annotations

import os
import sys

from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv("MULTILOGIN_DEBUG_PORT", "35000")


def main() -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Install: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)

    cdp_url = f"http://127.0.0.1:{PORT}"

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(cdp_url)
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://browserleaks.com/ip")
        print("Connected. Page title:", page.title())
        browser.close()


if __name__ == "__main__":
    main()
