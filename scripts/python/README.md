# Python scripts

Automation examples for developers in **India**, **China**, and other Python-first markets.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium   # only for playwright_connect.py

cp .env.example .env
# MULTILOGIN_TOKEN, MULTILOGIN_PROFILE_ID, MULTILOGIN_DEBUG_PORT
```

## Scripts

| File | Description |
|---|---|
| [launch_profile.py](launch_profile.py) | Start profile via launcher API (stdlib + dotenv) |
| [playwright_connect.py](playwright_connect.py) | Attach Playwright over CDP |
| [selenium_connect.py](selenium_connect.py) | Attach Selenium to debugger port |

## Run

```bash
python scripts/python/launch_profile.py
python scripts/python/playwright_connect.py
python scripts/python/selenium_connect.py
```

Node.js equivalents: [../api/](../api/) · [../playwright/](../playwright/)

Partner pricing: https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549
