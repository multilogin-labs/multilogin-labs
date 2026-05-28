"""Tiny CLI: `mlx-labs <command>`."""
from __future__ import annotations

import sys
from pathlib import Path

AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)
REPO = "https://github.com/multilogin-labs/multilogin-labs"


COMMANDS = {
    "help": "Show this help",
    "links": "Print partner pricing + promo codes",
    "endpoints": "Print API endpoints JSON if available",
    "cheatsheet": "Print API cheatsheet if available",
}


def main() -> int:
    args = sys.argv[1:]
    if not args or args[0] in {"help", "-h", "--help"}:
        return print_help()
    cmd = args[0]
    if cmd == "links":
        return print_links()
    if cmd == "endpoints":
        return cat_repo_file("docs/api/endpoints.json")
    if cmd == "cheatsheet":
        return cat_repo_file("docs/api/CHEATSHEET.md")
    print(f"unknown command: {cmd}", file=sys.stderr)
    return print_help(2)


def print_help(code: int = 0) -> int:
    cmds = "\n".join(f"  {k:<11} {v}" for k, v in COMMANDS.items())
    print(
        f"""mlx-labs · community Python CLI

Commands:
{cmds}

Repo: {REPO}
Partner: {AFFILIATE}
Codes:   SAAS50 · MIN50
"""
    )
    return code


def print_links() -> int:
    print(f"Partner pricing: {AFFILIATE}")
    print("Codes: SAAS50 · MIN50")
    print(f"Repo: {REPO}")
    print("Docs: https://multilogin-labs.github.io/multilogin-labs/")
    return 0


def cat_repo_file(rel: str) -> int:
    candidates = [
        Path.cwd() / rel,
        Path(__file__).resolve().parents[3] / rel,
    ]
    for path in candidates:
        if path.exists():
            sys.stdout.write(path.read_text(encoding="utf-8"))
            return 0
    print(
        f"{rel} not found locally. Clone the repo: git clone {REPO}",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
