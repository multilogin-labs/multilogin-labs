#!/usr/bin/env python3
"""Generate additional API cookbook recipes."""
from pathlib import Path

AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)

RECIPES = [
    ("21", "delete-profile-cleanup", "Delete profile and cleanup", "profile remove delete"),
    ("22", "search-profiles-by-tag", "Search profiles by tag", "profile search tag filter"),
    ("23", "test-proxy-connection", "Test proxy before launch", "proxy validate connection"),
    ("24", "signin-and-refresh-token", "Signin + refresh token flow", "signin refresh token 2fa"),
    ("25", "parallel-playwright-sessions", "Parallel Playwright sessions", "playwright parallel multiple"),
    ("26", "quick-profile-one-shot", "Quick profile one-shot scrape", "quick profile v3"),
    ("27", "move-profile-folder", "Move profile between folders", "folder transfer workspace"),
    ("28", "update-profile-metadata", "Update profile name and notes", "profile update metadata"),
    ("29", "launcher-health-check", "Launcher health check", "launcher status ping"),
    ("30", "full-session-restart-loop", "Restart loop for long jobs", "restart profile cron"),
]

BODY = """# Cookbook {num}: {title}

> [Partner pricing →]({affiliate})

## Goal

{goal}

## Prerequisites

- Multilogin desktop running (for Launcher calls)
- `MULTILOGIN_EMAIL`, `MULTILOGIN_PASSWORD` or automation token
- `MULTILOGIN_FOLDER_ID`, `MULTILOGIN_PROFILE_ID` in `.env`

## Steps

### 1. Authenticate

```bash
# Python
python scripts/python/signin.py
export MULTILOGIN_TOKEN=$(python -c "import os; print(os.environ.get('MULTILOGIN_TOKEN',''))")
```

Or use automation token — see [05-automation-token-setup](05-automation-token-setup.md).

### 2. API call

See [endpoints index](../endpoints-index.md) and search:

```bash
npm run api:search -- {search}
```

### 3. Example (Python)

```python
from lib.mlx_client import MLXClient
import os

client = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
# Implement: see endpoint page for exact method/path
```

### 4. Example (Node)

```javascript
import {{ MLXClient }} from "../../lib/mlx_client.mjs";
const client = new MLXClient({{ token: process.env.MULTILOGIN_TOKEN }});
```

## Related endpoints

Search [SEARCH_KEYWORDS.md](../SEARCH_KEYWORDS.md) for: `{search}`.

## Next

- [Cookbook index](README.md)
- [Quick start](../quick-start.md)

**Keywords:** multilogin api cookbook · {search}
"""


def main():
    base = Path(__file__).resolve().parents[1] / "docs" / "api" / "cookbook"
    created = []
    for num, slug, title, search in RECIPES:
        fname = f"{num}-{slug}.md"
        path = base / fname
        if path.exists():
            continue
        path.write_text(
            BODY.format(
                num=num,
                title=title,
                affiliate=AFFILIATE,
                goal=f"Automate: {title.lower()}.",
                search=search,
            ),
            encoding="utf-8",
        )
        created.append((num, title, fname))
        print("created", fname)

    readme = base / "README.md"
    if readme.exists() and created:
        text = readme.read_text(encoding="utf-8")
        for num, title, fname in created:
            row = f"| {num} | [{title}]({fname}) |"
            if fname not in text:
                text = text.replace(
                    "\n## Index\n",
                    f"\n| {num} | [{title}]({fname}) | |\n",
                ) if "## Index" in text else text + f"\n| {num} | [{title}]({fname}) | |\n"
        # append table rows before footer
        if "| 20 |" in text:
            extra = "".join(
                f"| {n} | [{t}]({f}) | {t} |\n"
                for n, t, f in created
                if f not in text
            )
            if extra:
                readme.write_text(
                    text.replace("| 20 |", "| 20 |").rstrip()
                    + "\n" + extra,
                    encoding="utf-8",
                )
    print(f"created {len(created)} recipes")


if __name__ == "__main__":
    main()
