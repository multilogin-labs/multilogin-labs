# Recipe: Playwright full session

End-to-end: start Multilogin profile → automate → stop.

## Prerequisites

- App running · `.env` configured · `pip install -r requirements.txt`

## Steps

```bash
# 1. Start profile (returns port in JSON)
python scripts/python/launch_profile.py

# 2. Set port from response, e.g. 55513
export MULTILOGIN_DEBUG_PORT=55513
python scripts/python/playwright_connect.py

# 3. Stop
python scripts/python/stop_profile.py
```

## Python (single script pattern)

```python
import os
from lib.mlx_client import MLXClient
from playwright.sync_api import sync_playwright

client = MLXClient.from_env()
folder = os.environ["MULTILOGIN_FOLDER_ID"]
profile = os.environ["MULTILOGIN_PROFILE_ID"]

result = client.start_profile(folder, profile, automation_type="playwright")
port = result["data"]["port"]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{port}")
    page = browser.contexts[0].pages[0]
    page.goto("https://example.com")
    print(page.title())
    browser.close()

client.stop_profile(profile)
```

[start-browser-profile](../endpoints/start-browser-profile.md) · [stop-browser-profile](../endpoints/stop-browser-profile.md)
