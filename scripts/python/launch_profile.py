#!/usr/bin/env python3
"""Start a Multilogin profile via the local launcher API.

Docs: https://multilogin.com/help/en_US/api

Usage:
    cp .env.example .env   # set MULTILOGIN_TOKEN, MULTILOGIN_PROFILE_ID
    pip install -r requirements.txt
    python scripts/python/launch_profile.py
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

from dotenv import load_dotenv

load_dotenv()

LAUNCHER = os.getenv("MULTILOGIN_LAUNCHER_URL", "https://launcher.mlx.yt:45001")
TOKEN = os.getenv("MULTILOGIN_TOKEN")
PROFILE_ID = os.getenv("MULTILOGIN_PROFILE_ID")


def start_profile() -> dict:
    if not TOKEN or not PROFILE_ID:
        print("Set MULTILOGIN_TOKEN and MULTILOGIN_PROFILE_ID in .env", file=sys.stderr)
        sys.exit(1)

    url = f"{LAUNCHER}/api/v2/profile/start"
    payload = json.dumps({"profileId": PROFILE_ID, "automation": True}).encode()
    req = urllib.request.Request(
        url,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req) as resp:
            body = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"Failed to start profile: {e.code} {err}", file=sys.stderr)
        sys.exit(1)

    port = body.get("port") or (body.get("data") or {}).get("port")
    print("Profile started.")
    print(f"Connect automation to port: {port or '(see response)'}")
    print(json.dumps(body, indent=2))
    return body


if __name__ == "__main__":
    start_profile()
