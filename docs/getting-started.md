# Getting Started with Multilogin

> Partner pricing: [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)  
> Promo codes: **`SAAS50`** or **`MIN50`**

## 1. Create an account

1. Open the [pricing page](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).
2. Start the **$2 / 3-day trial** or pick a Pro/Business plan.
3. Apply **`SAAS50`** or **`MIN50`** at checkout.

## 2. Install the app

Download from [multilogin.com/download](https://multilogin.com/download/) and sign in. **Keep the app running** for Launcher API calls.

## 3. Create your first profile

1. **Create profile** → Mimic or Stealthfox.
2. Fingerprint **automatic**.
3. Attach proxy (built-in or your own).
4. Note **folder_id** and **profile_id** (DevTools or API search).

## 4. Get your API token

**Option A — Automation token (recommended):**  
`GET https://api.multilogin.com/workspace/automation_token`  
Or: App → Settings → API. Requires **Pro 10+**.

**Option B — Sign in:**  
`POST https://api.multilogin.com/user/signin`  
See [api/authentication.md](api/authentication.md).

```bash
cp .env.example .env
# MULTILOGIN_TOKEN, MULTILOGIN_FOLDER_ID, MULTILOGIN_PROFILE_ID
```

## 5. Start a profile (official Launcher API)

```http
GET https://launcher.mlx.yt:45001/api/v2/profile/f/{folder_id}/p/{profile_id}/start?automation_type=playwright
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

Full reference: [api/endpoints/start-browser-profile.md](api/endpoints/start-browser-profile.md)

## 6. Connect automation

Response includes `data.port` — connect Playwright/Puppeteer/Selenium to that CDP port.

## 7. Next steps

- [API hub — 90 endpoints](api/README.md)
- [Endpoints index](api/endpoints-index.md)
- [Python client](../lib/mlx_client.py)
- [Proxy setup](proxy-setup.md)
- [SEARCH_INDEX](SEARCH_INDEX.md)
