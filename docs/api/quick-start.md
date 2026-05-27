# Multilogin X API — Quick Start (5 minutes)

> [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · Codes **SAAS50** · **MIN50**

## Prerequisites

1. Multilogin app **installed and running**
2. Plan with **API access** (Pro 10+)
3. **Automation token** (recommended) or sign-in token

## Step 1 — Environment

```bash
cp .env.example .env
```

```env
MULTILOGIN_TOKEN=your_automation_token
MULTILOGIN_FOLDER_ID=uuid-from-app
MULTILOGIN_PROFILE_ID=uuid-from-app
MULTILOGIN_LAUNCHER_URL=https://launcher.mlx.yt:45001
MULTILOGIN_AUTOMATION_TYPE=playwright
```

Find `folder_id` + `profile_id`: Multilogin UI → profile → DevTools, or `POST /profile/search`.

## Step 2 — Start profile (Launcher)

```http
GET https://launcher.mlx.yt:45001/api/v2/profile/f/{folder_id}/p/{profile_id}/start?automation_type=playwright&headless_mode=false
Authorization: Bearer YOUR_TOKEN
```

**Python**

```bash
pip install -r requirements.txt
python scripts/python/launch_profile.py
```

**Node**

```bash
npm run api:launch
```

Response includes `data.port` — use for Playwright/Puppeteer/Selenium.

Details: [start-browser-profile.md](endpoints/start-browser-profile.md)

## Step 3 — Connect Playwright

```bash
# Set port from step 2
export MULTILOGIN_DEBUG_PORT=55513
python scripts/python/playwright_connect.py
```

## Step 4 — Stop profile

```bash
python scripts/python/stop_profile.py
# or: npm run api:stop
```

## Common flows

| Goal | Guide |
|---|---|
| First-time API auth | [authentication.md](authentication.md) |
| Create profile via API | [profile-create.md](endpoints/profile-create.md) |
| Quick disposable profile | [start-quick-profile-v3.md](endpoints/start-quick-profile-v3.md) |
| List/search profiles | [profile-search.md](endpoints/profile-search.md) |
| Validate proxy before use | [validate-proxy.md](endpoints/validate-proxy.md) |
| Full automation recipes | [cookbook/README.md](cookbook/README.md) |

## Next

- [Endpoints index — 90 APIs](endpoints-index.md)
- [Python client](../../lib/mlx_client.py)
- [SEARCH_KEYWORDS](SEARCH_KEYWORDS.md)
