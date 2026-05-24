#!/usr/bin/env python3
"""Stop profile via Launcher API."""
from __future__ import annotations

import os
import sys

from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from lib.mlx_client import MLXClient  # noqa: E402


def main() -> None:
    profile_id = os.getenv("MULTILOGIN_PROFILE_ID")
    if not profile_id:
        print("Set MULTILOGIN_PROFILE_ID", file=sys.stderr)
        sys.exit(1)
    client = MLXClient.from_env()
    print(client.stop_profile(profile_id))


if __name__ == "__main__":
    main()
