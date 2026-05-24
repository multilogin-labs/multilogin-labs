#!/usr/bin/env python3
"""Start profile using official Launcher API v2 path."""
from __future__ import annotations

import os
import sys

from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from lib.mlx_client import MLXClient  # noqa: E402


def main() -> None:
    folder_id = os.getenv("MULTILOGIN_FOLDER_ID")
    profile_id = os.getenv("MULTILOGIN_PROFILE_ID")
    automation = os.getenv("MULTILOGIN_AUTOMATION_TYPE", "playwright")

    if not folder_id or not profile_id:
        print("Set MULTILOGIN_FOLDER_ID and MULTILOGIN_PROFILE_ID", file=sys.stderr)
        sys.exit(1)

    client = MLXClient.from_env()
    result = client.start_profile(
        folder_id,
        profile_id,
        automation_type=automation,
        headless=False,
    )
    print(result)


if __name__ == "__main__":
    main()
