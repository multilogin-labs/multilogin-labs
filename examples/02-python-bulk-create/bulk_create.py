"""Bulk create Multilogin profiles from a CSV file."""
from __future__ import annotations

import csv
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lib.mlx_client import MLXClient  # type: ignore  # noqa: E402


def main(csv_path: str) -> int:
    token = os.environ["MULTILOGIN_TOKEN"]
    folder = os.environ["MULTILOGIN_FOLDER_ID"]
    client = MLXClient(token=token)

    with open(csv_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for i, row in enumerate(reader, 1):
            payload = {
                "name": row.get("name") or f"profile-{i}",
                "browser_type": row.get("browser") or "mimic",
                "tags": [t.strip() for t in (row.get("tags") or "").split("|") if t.strip()],
                "folder_id": folder,
            }
            print(f"creating {payload['name']}...")
            try:
                created = client.create_profile(payload)
                print("  ok", created.get("id"))
            except Exception as exc:  # pragma: no cover
                print("  fail", exc)
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "profiles.csv"))
