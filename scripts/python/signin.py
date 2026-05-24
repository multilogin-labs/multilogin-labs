#!/usr/bin/env python3
"""Sign in and print tokens (store in .env — never commit)."""
from __future__ import annotations

import os
import sys

from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from lib.mlx_client import MLXClient  # noqa: E402


def main() -> None:
    email = os.getenv("MULTILOGIN_EMAIL")
    password = os.getenv("MULTILOGIN_PASSWORD")
    if not email or not password:
        print("Set MULTILOGIN_EMAIL and MULTILOGIN_PASSWORD", file=sys.stderr)
        sys.exit(1)
    client = MLXClient.signin(email, password)
    print("token:", client.token[:20] + "...")
    print("refresh_token:", (client.refresh_token or "")[:20] + "...")


if __name__ == "__main__":
    main()
