# Getting Started with Multilogin

> Partner pricing: [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)  
> Promo codes: **`SAAS50`** or **`MIN50`**

## 1. Create an account

1. Open the [pricing page](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).
2. Start the **$2 / 3-day trial** or pick a Pro/Business plan.
3. Apply **`SAAS50`** or **`MIN50`** at checkout.

## 2. Install the app

Download from [multilogin.com/download](https://multilogin.com/download/) and sign in.

## 3. Create your first profile

1. **Create profile** → choose Mimic (Chromium) or Stealthfox (Firefox).
2. Set fingerprint mode to **automatic** (based on real-user data).
3. Attach a proxy (built-in Multilogin proxy or your own residential).
4. Save and **Launch** once manually to verify the session.

## 4. Get your API token

1. App → **Settings** → **API** (or Workspace → API).
2. Copy the bearer token into `.env`:

```bash
cp .env.example .env
# Edit MULTILOGIN_TOKEN and MULTILOGIN_PROFILE_ID
```

Automation token is available from **Pro 10** and above.

## 5. Run a script from this repo

```bash
npm install
# Optional: npm install playwright puppeteer-core

npm run api:launch
npm run playwright:connect
```

## 6. Next steps

- [Proxy setup](proxy-setup.md)
- [Antifingerprint checklist](antifingerprint-checklist.md)
- [Official API docs](https://multilogin.com/help/en_US/api)
