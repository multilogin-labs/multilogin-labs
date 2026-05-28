#!/usr/bin/env python3
"""Enrich API category pages with overview, examples, and links."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT_DIR = ROOT / "docs" / "api" / "categories"
EPS = json.loads((ROOT / "docs" / "api" / "endpoints.json").read_text(encoding="utf-8"))

AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)

# Per-category metadata for enrichment
META = {
    "2fa": {
        "title": "2FA — Two-factor authentication",
        "summary": "Manage workspace and account-level 2FA: enable, verify, devices, backup codes.",
        "use_cases": [
            "Force 2FA for all members in an agency workspace",
            "Backup-code rotation script for compliance audits",
            "Provision new operator device after onboarding",
        ],
        "code_lang": "bash",
        "example": """# Enable 2FA on the current account
curl -X POST https://api.multilogin.com/2fa/enable \\
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{"code":"123456"}'""",
        "related_guide": "../../guides/multilogin-2fa-workflow.md",
    },
    "launcher": {
        "title": "Launcher — Local profile control",
        "summary": "Start, stop, and monitor profiles on the local Multilogin desktop. Required for Playwright/Puppeteer/Selenium.",
        "use_cases": [
            "Open a profile and connect Playwright to its CDP port",
            "Launch quick profiles on demand for scraping",
            "Stop all profiles for emergency / shift change",
        ],
        "code_lang": "bash",
        "example": """# Start profile in playwright mode
curl "https://launcher.mlx.yt:45001/api/v2/profile/f/$FOLDER/p/$PROFILE/start?automation_type=playwright" \\
  -H "Authorization: Bearer $MULTILOGIN_TOKEN"

# Stop profile
curl "https://launcher.mlx.yt:45001/api/v1/profile/stop?profile_id=$PROFILE" \\
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" """,
        "related_guide": "../../guides/multilogin-api-playwright.md",
    },
    "profile-management": {
        "title": "Profile management — Create, update, delete, search",
        "summary": "Full lifecycle operations for browser and cloud-phone profiles.",
        "use_cases": [
            "Bulk create profiles with proxy + tags from a CSV",
            "Update profile name/notes after each campaign",
            "Search by tag for daily warmup batches",
        ],
        "code_lang": "python",
        "example": """from lib.mlx_client import MLXClient
import os

c = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
profiles = c.search_profiles({"tag": "warmup", "limit": 50})
for p in profiles:
    print(p["id"], p["name"], p.get("tags"))""",
        "related_guide": "../../guides/multilogin-profile-search-tags.md",
    },
    "profile-access-management": {
        "title": "Profile access management — Sharing & permissions",
        "summary": "Share profiles with team members, transfer ownership, manage roles.",
        "use_cases": [
            "Onboard a new agency member to a client folder",
            "Revoke access when an operator leaves",
            "Audit who has access to which profile",
        ],
        "code_lang": "bash",
        "example": """curl -X POST https://api.multilogin.com/profile/share \\
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{"profile_id":"...","member_email":"ops@example.com","role":"editor"}'""",
        "related_guide": "../../guides/multilogin-team-workspace.md",
    },
    "profile-import-export": {
        "title": "Profile import / export — Migration",
        "summary": "Move profiles between workspaces, back up cookies, and migrate from other antidetect tools.",
        "use_cases": [
            "Migrate from AdsPower/GoLogin to Multilogin",
            "Backup before bulk delete",
            "Move profiles between client workspaces",
        ],
        "code_lang": "python",
        "example": """from lib.mlx_client import MLXClient
import json, os

c = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
# Export single profile
data = c.export_profile(os.environ["MULTILOGIN_PROFILE_ID"])
open("profile_backup.json", "w").write(json.dumps(data, indent=2))""",
        "related_guide": "../cookbook/12-profile-export-migrate.md",
    },
    "bookmark-management": {
        "title": "Bookmark management — Profile bookmarks",
        "summary": "Programmatically read and write bookmarks inside a profile.",
        "use_cases": [
            "Pre-seed bookmarks for new operator onboarding",
            "Audit bookmarks across many profiles",
            "Sync curated link sets to a campaign cluster",
        ],
        "code_lang": "bash",
        "example": """curl -X POST "https://api.multilogin.com/profile/$PROFILE/bookmarks" \\
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{"items":[{"title":"Multilogin","url":"https://multilogin.com/"}]}'""",
        "related_guide": None,
    },
    "pre-made-cookies": {
        "title": "Pre-made cookies — Session bootstrap",
        "summary": "Inject cookies into a profile before first login. Useful for migrations.",
        "use_cases": [
            "Restore session from a different antidetect tool",
            "Hand off warmed account to a different operator",
            "Recover from accidental cookie wipe",
        ],
        "code_lang": "python",
        "example": """import os, json
from lib.mlx_client import MLXClient

c = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
cookies = json.loads(open("cookies.json").read())
c.import_cookies(os.environ["MULTILOGIN_PROFILE_ID"], cookies)""",
        "related_guide": "../cookbook/09-import-cookies.md",
    },
    "proxy": {
        "title": "Proxy — Built-in residential & mobile",
        "summary": "Generate Multilogin-managed proxy credentials and assign them to profiles.",
        "use_cases": [
            "Auto-assign country-matched proxy on profile create",
            "Refresh sticky session before warmup wave",
            "Rotate exit IPs between sessions",
        ],
        "code_lang": "bash",
        "example": """# Generate residential proxy in Vietnam
curl -X POST https://api.multilogin.com/proxy/generate \\
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{"country":"vn","type":"residential","sticky_seconds":1800}'""",
        "related_guide": "../cookbook/13-generate-multilogin-proxy.md",
    },
    "object-storage": {
        "title": "Object storage — Workspace files & artifacts",
        "summary": "Upload screenshots, exports, and shared assets at workspace level.",
        "use_cases": [
            "Store proof-of-task screenshots for clients",
            "Share warmup logs across the team",
            "Persist exported profiles for retention policy",
        ],
        "code_lang": "bash",
        "example": """curl -X POST https://api.multilogin.com/storage/upload \\
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \\
  -F "file=@screenshot.png" \\
  -F "tag=campaign-q3" """,
        "related_guide": None,
    },
    "browser-profile-data": {
        "title": "Browser profile data — Cookies, history, storage",
        "summary": "Read and write low-level browser data inside a profile.",
        "use_cases": [
            "Audit cookies for compliance after a campaign",
            "Pre-load localStorage with feature flags",
            "Clear specific data without nuking the whole profile",
        ],
        "code_lang": "bash",
        "example": """curl "https://api.multilogin.com/profile/$PROFILE/cookies" \\
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" """,
        "related_guide": "../cookbook/10-export-cookies.md",
    },
    "script-runner": {
        "title": "Script runner — Server-side automation",
        "summary": "Run JavaScript snippets inside a profile from the API. Great for headless flows.",
        "use_cases": [
            "Run a quick scrape without a full Playwright stack",
            "Pre-action diagnostics inside the profile",
            "Self-healing: detect captcha and stop session",
        ],
        "code_lang": "bash",
        "example": """curl -X POST https://api.multilogin.com/scripts/run \\
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{"profile_id":"...","script":"return document.title"}'""",
        "related_guide": "../cookbook/14-script-runner.md",
    },
}

TEMPLATE = """# {title}

> [Partner pricing →]({affiliate}) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

{summary}

## Endpoints in this category

{endpoint_list}

## Common use cases

{use_cases}

## Quick example

```{code_lang}
{example}
```

## Related

- [Cookbook ×40](../cookbook/README.md){related_link}
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin {slug} api · multilogin x · {extra_keywords}
"""


def build_endpoint_list(category_label: str) -> str:
    rows = []
    for e in EPS:
        if e["category"].lower().replace(" ", "-") != category_label:
            continue
        rows.append(
            f"- **`{e['method']}`** [{e['name']}](../endpoints/{e['slug']}.md) — `{e['url']}`"
        )
    return "\n".join(rows) if rows else "_(see API hub)_"


def main():
    for path in sorted(CAT_DIR.glob("*.md")):
        slug = path.stem
        meta = META.get(slug)
        if not meta:
            continue
        related_link = ""
        if meta.get("related_guide"):
            related_link = f"\n- [Related guide]({meta['related_guide']})"
        content = TEMPLATE.format(
            title=meta["title"],
            affiliate=AFFILIATE,
            summary=meta["summary"],
            endpoint_list=build_endpoint_list(slug),
            use_cases="\n".join(f"- {u}" for u in meta["use_cases"]),
            code_lang=meta["code_lang"],
            example=meta["example"],
            related_link=related_link,
            slug=slug.replace("-", " "),
            extra_keywords=meta["title"].split("—")[-1].strip().lower(),
        )
        path.write_text(content, encoding="utf-8")
        print("enriched", slug)


if __name__ == "__main__":
    main()
