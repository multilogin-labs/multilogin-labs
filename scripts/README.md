# Scripts

Examples for automating Multilogin profiles. Requires an active subscription with API access (Pro 10+).

## Setup

```bash
cp ../.env.example ../.env
# Fill MULTILOGIN_TOKEN, MULTILOGIN_PROFILE_ID
npm install
```

## Commands

| Command | Description |
|---|---|
| `npm run api:launch` | Start profile via launcher API |
| `npm run playwright:connect` | Connect Playwright to running profile |
| `npm run puppeteer:connect` | Connect Puppeteer to running profile |
| `npm run selenium:connect` | Connect Selenium to running profile |
| `npm run plan` | Interactive plan recommendation CLI |

Install optional deps when needed:

```bash
npm install playwright puppeteer-core
```

Official docs: https://multilogin.com/help/en_US/api
