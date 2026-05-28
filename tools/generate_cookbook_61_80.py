#!/usr/bin/env python3
"""Generate cookbook recipes 61–80 (advanced + integration patterns)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs" / "api" / "cookbook"
AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)

RECIPES = [
    ("61", "github-actions-cron",         "Run warmup from GitHub Actions cron",     "github actions cron warmup"),
    ("62", "playwright-codegen-handoff",  "Hand off Playwright codegen to a profile","playwright codegen profile"),
    ("63", "go-client-snippet",           "Minimal Go client snippet",                "go golang client snippet"),
    ("64", "rust-client-snippet",         "Minimal Rust client snippet",              "rust client reqwest"),
    ("65", "k6-load-test",                "k6 load test against Launcher",            "k6 load test launcher"),
    ("66", "vitest-mock-mlx",             "Mock MLX client for Vitest",               "vitest mock unit test"),
    ("67", "pytest-fixtures",             "Pytest fixtures for Multilogin tests",     "pytest fixtures conftest"),
    ("68", "datadog-metrics",             "Send timings to Datadog",                  "datadog statsd metrics"),
    ("69", "sentry-error-capture",        "Capture errors to Sentry",                 "sentry error tracking"),
    ("70", "ofelia-docker-cron",          "Use Ofelia for Docker-native cron",        "ofelia docker cron"),
    ("71", "vercel-cron-warmup",          "Vercel cron triggers warmup",              "vercel cron serverless"),
    ("72", "cloudflare-worker-search",    "Cloudflare Worker proxies search",         "cloudflare worker search"),
    ("73", "n8n-workflow",                "n8n workflow that watches profile errors", "n8n workflow automation"),
    ("74", "make-com-scenario",           "Make.com scenario blueprint",              "make integromat scenario"),
    ("75", "zapier-zap",                  "Zapier zap for new-profile alerts",        "zapier zap webhook"),
    ("76", "supabase-sync",               "Sync profile metadata to Supabase",        "supabase sync postgres"),
    ("77", "airtable-sync",               "Sync profile metadata to Airtable",        "airtable sync metadata"),
    ("78", "notion-sync",                 "Mirror profiles into a Notion database",   "notion sync database"),
    ("79", "telemetry-opentelemetry",     "OpenTelemetry traces for profile ops",     "opentelemetry tracing"),
    ("80", "rotating-residential-proxy",  "Plug rotating residential proxy provider", "rotating residential proxy"),
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

### 2. Sketch (Python)

```python
import os
from lib.mlx_client import MLXClient

c = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
folder = os.environ["MULTILOGIN_FOLDER_ID"]
# {title} — implement the flow with the endpoints printed above
```

### 3. Sketch (Node)

```javascript
import {{ MLXClient }} from "../../lib/mlx_client.mjs";

const c = new MLXClient({{ token: process.env.MULTILOGIN_TOKEN }});
// {title_lower} — wire to your scheduler / queue
```

## Production notes

- Use **automation tokens** for cron / CI to avoid daily refresh churn.
- Add **exponential backoff + jitter** (recipe 57) on every outbound call.
- Emit **structured logs** (`profile_id`, `op`, `duration_ms`) so any of recipes 52 / 68 / 79 can scoop them up.

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
        for old, new in (
            ("**60 recipes**", "**80 recipes**"),
            ("**40 recipes**", "**80 recipes**"),
            ("**30 recipes**", "**80 recipes**"),
        ):
            if old in readme:
                readme = readme.replace(old, new)
                break

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
