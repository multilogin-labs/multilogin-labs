#!/usr/bin/env python3
"""Enrich endpoint markdown from docs/api/reference-full.md.

Usage:
  python tools/enrich_endpoints.py
  python tools/enrich_endpoints.py --all   # all 90 endpoints (large files)
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AFF = "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549"

TOP_DEFAULT = [
    "start-browser-profile",
    "stop-browser-profile",
    "stop-all-profiles",
    "start-quick-profile-v3",
    "user-sign-in",
    "workspace-automation-token",
    "profile-create",
    "profile-search",
    "profile-clone",
    "validate-proxy",
]


def parse_sections(ref_text: str) -> dict[str, tuple[str, str]]:
    parts = re.split(r"\n#### ", ref_text)
    out: dict[str, tuple[str, str]] = {}
    for part in parts[1:]:
        nl = part.find("\n")
        title = part[:nl].strip()
        body = part[nl:].strip()
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        out[slug] = (title, body)
    return out


def build_page(ep: dict, title: str, body: str) -> str:
    cat_slug = re.sub(r"[^a-z0-9]+", "-", ep["category"].lower()).strip("-")
    slug = ep["slug"]
    desc = body.split("**Example Request**")[0].strip()[:5000]
    md = f"""# {title}

`{ep['method']}` · [{ep['category']}](../categories/{cat_slug}.md)

```http
{ep['method']} {ep['url']}
```

## Description

{desc}

"""
    if "**Example Request**" in body:
        req = body.split("**Example Request**", 1)[1]
        if "**Example Response**" in req:
            req = req.split("**Example Response**", 1)[0]
        md += f"## Example request\n\n{req.strip()[:3500]}\n\n"
    if "**Example Response**" in body:
        resp = body.split("**Example Response**", 1)[1].split("\n####", 1)[0].strip()[:3000]
        md += f"## Example response\n\n{resp}\n\n"
    md += f"""## Code

- [Python example](../examples/python/{slug}.md) · [Node](../examples/node/{slug}.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api {slug.replace('-', ' ')}` · `multilogin x {title.lower()}`

[← Endpoints index](../endpoints-index.md) · [Partner pricing]({AFF})
"""
    return md


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    ref = (ROOT / "docs/api/reference-full.md").read_text(encoding="utf-8")
    sections = parse_sections(ref)
    eps = json.loads((ROOT / "docs/api/endpoints.json").read_text())
    targets = [e["slug"] for e in eps] if args.all else TOP_DEFAULT

    for ep in eps:
        if ep["slug"] not in targets:
            continue
        slug = ep["slug"]
        if slug not in sections:
            print("skip (no section):", slug)
            continue
        title, body = sections[slug]
        path = ROOT / "docs/api/endpoints" / f"{slug}.md"
        path.write_text(build_page(ep, title, body), encoding="utf-8")
        print("ok", slug)


if __name__ == "__main__":
    main()
