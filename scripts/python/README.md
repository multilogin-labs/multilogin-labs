# Python scripts

Automation for **Multilogin X API** (official Launcher + Cloud API).

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Required in `.env`:
- `MULTILOGIN_TOKEN` (automation token recommended)
- `MULTILOGIN_FOLDER_ID` + `MULTILOGIN_PROFILE_ID` for start

## Scripts

| File | Description |
|---|---|
| [signin.py](signin.py) | `POST /user/signin` → tokens |
| [launch_profile.py](launch_profile.py) | Launcher v2 start (playwright/puppeteer/selenium) |
| [stop_profile.py](stop_profile.py) | Launcher v1 stop |
| [playwright_connect.py](playwright_connect.py) | Attach Playwright to CDP port |
| [selenium_connect.py](selenium_connect.py) | Attach Selenium |

## Client library

Use [lib/mlx_client.py](../../lib/mlx_client.py) for all 90 endpoints — see [docs/api/](../../docs/api/).

```python
from lib.mlx_client import MLXClient

client = MLXClient.from_env()
result = client.start_profile(folder_id, profile_id, automation_type="playwright")
```

Docs: [api/endpoints-index.md](../../docs/api/endpoints-index.md)
