#!/usr/bin/env python3
"""Generate cookbook recipes 41–60 with richer content."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs" / "api" / "cookbook"
AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)

RECIPES = [
    ("41", "audit-cookies-bulk", "Audit cookies across many profiles", "cookies audit compliance"),
    ("42", "playwright-multi-tab", "Multi-tab Playwright workflow", "playwright tabs context"),
    ("43", "puppeteer-screenshot-grid", "Screenshot grid for QA", "screenshot grid qa"),
    ("44", "selenium-explicit-wait", "Selenium explicit waits pattern", "selenium wait explicit"),
    ("45", "session-replay-record", "Record + replay session events", "session replay record"),
    ("46", "anti-bot-test-loop", "Run anti-bot tests on a profile", "antibot fingerprint test"),
    ("47", "captcha-solver-hookin", "Captcha solver integration shape", "captcha solver hook"),
    ("48", "cookie-jar-export-rotate", "Cookie jar rotation helper", "cookie rotate jar"),
    ("49", "proxy-failover", "Proxy failover and retry logic", "proxy failover retry"),
    ("50", "bulk-tag-rename", "Bulk rename tags across profiles", "tag rename bulk"),
    ("51", "scheduled-warmup-cron", "Scheduled warmup with cron", "warmup cron schedule"),
    ("52", "metrics-prometheus-exporter", "Prometheus metrics exporter shape", "prometheus metrics"),
    ("53", "slack-alerting", "Slack alert on profile errors", "slack alert webhook"),
    ("54", "discord-alerting", "Discord webhook for status pings", "discord alert webhook"),
    ("55", "csv-import-profiles", "Import profiles from CSV", "csv import bulk profiles"),
    ("56", "csv-export-status", "Export profile status to CSV", "csv export reporting"),
    ("57", "ratelimit-backoff", "Exponential backoff for rate limits", "ratelimit backoff retry"),
    ("58", "two-fa-rotate-backup", "Rotate 2FA backup codes", "2fa backup rotate"),
    ("59", "agency-onboarding-script", "Agency onboarding script", "agency onboarding"),
    ("60", "self-hosted-runner-pattern", "Self-hosted CI runner pattern", "self hosted runner ci"),
]

BODY = """# Cookbook {num}: {title}

> [Partner pricing →]({affiliate}) · **`SAAS50`** · **`MIN50`** · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

## Goal

{goal}

## Prerequisites

- Multilogin desktop running for Launcher calls
- `MULTILOGIN_TOKEN` (or automation token — recommended for cron)
- `MULTILOGIN_FOLDER_ID`, `MULTILOGIN_PROFILE_ID` in `.env`

## Steps

### 1. Search the right endpoints

```bash
npm run api:search -- {search}
# or
npx mlx-labs search {search}
```

### 2. Python sketch

```python
import os
from lib.mlx_client import MLXClient

c = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
folder = os.environ["MULTILOGIN_FOLDER_ID"]
# Implement the flow using the endpoints printed above
```

### 3. Node sketch

```javascript
import {{ MLXClient }} from "../../lib/mlx_client.mjs";

const c = new MLXClient({{ token: process.env.MULTILOGIN_TOKEN }});
// Implement: {title_lower}
```

## Production notes

- Add **retry with exponential backoff** for 429 — see [recipe 57](57-ratelimit-backoff.md).
- Use **automation token** for long-running scripts ([guide](../../guides/multilogin-automation-token.md)).
- Log timing per step — feed into [recipe 52](52-metrics-prometheus-exporter.md).

## Related

- [Cookbook index](README.md) · [API hub](../README.md) · [Quick start](../quick-start.md)
- [Comparison matrix](../../comparisons/comparison-matrix.md)

**Keywords:** multilogin api cookbook · {search}
"""


def main():
    readme = (BASE / "README.md").read_text(encoding="utf-8")
    created = []
    for num, slug, title, search in RECIPES:
        fname = f"{num}-{slug}.md"
        path = BASE / fname
        if path.exists():
            continue
        path.write_text(
            BODY.format(
                num=num,
                title=title,
                title_lower=title.lower(),
                affiliate=AFFILIATE,
                goal=f"{title} — production-ready pattern using Multilogin X API.",
                search=search,
            ),
            encoding="utf-8",
        )
        created.append((num, title, fname))
        print("created", fname)

    if created:
        if "**40 recipes**" in readme:
            readme = readme.replace("**40 recipes**", "**60 recipes**")
        elif "**30 recipes**" in readme:
            readme = readme.replace("**30 recipes**", "**60 recipes**")

        rows = "".join(
            f"| {n} | [{t}]({f}) |\n"
            for n, t, f in created
            if f not in readme
        )
        readme = readme.rstrip() + "\n" + rows
        (BASE / "README.md").write_text(readme, encoding="utf-8")
    print(f"created {len(created)} recipes")


if __name__ == "__main__":
    main()
