#!/usr/bin/env python3
"""Stop a Multilogin profile via launcher API."""
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

if not TOKEN or not PROFILE_ID:
    print("Set MULTILOGIN_TOKEN and MULTILOGIN_PROFILE_ID", file=sys.stderr)
    sys.exit(1)

req = urllib.request.Request(
    f"{LAUNCHER}/api/v2/profile/stop",
    data=json.dumps({"profileId": PROFILE_ID}).encode(),
    method="POST",
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    },
)

try:
    with urllib.request.urlopen(req) as resp:
        print(json.dumps(json.loads(resp.read().decode()), indent=2))
except urllib.error.HTTPError as e:
    print(e.read().decode(), file=sys.stderr)
    sys.exit(1)
