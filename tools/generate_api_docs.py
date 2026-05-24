#!/usr/bin/env python3
"""Regenerate docs/api from Postman gist reference.

Usage:
  python tools/generate_api_docs.py /path/to/gist-export.txt
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def parse_gist(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next(i for i, l in enumerate(lines) if i > 5 and l.strip() == "```") + 1
    end = next(i for i in range(len(lines) - 1, start, -1) if lines[i].strip() == "```")
    return "\n".join(lines[start:end])


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not src or not src.exists():
        print("Provide path to Multilogin X API markdown export", file=sys.stderr)
        sys.exit(1)
    content = parse_gist(src)
    out = ROOT / "docs" / "api" / "reference-full.md"
    out.write_text(
        "# Multilogin X API — Full Reference\n\n"
        + f"> Parsed from export · [Official Postman](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)\n\n"
        + content,
        encoding="utf-8",
    )
    count = len(re.findall(r"^#### ", content, re.M))
    print(f"Wrote {out} ({count} endpoint sections)")


if __name__ == "__main__":
    main()
