# Contributing

Thanks for helping grow Multilogin Labs.

## What to contribute

- Automation scripts (Playwright, Puppeteer, Selenium, API — **Node.js or Python**)
- Proxy and fingerprint guides
- Translations in `locales/`
- Bug fixes and doc improvements

## Guidelines

1. Keep scripts minimal and documented.
2. Never commit `.env` or API tokens.
3. Link partner pricing as:  
   `https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549`
4. Match existing code style (ES modules, Node 18+).

## Run locally

```bash
cp .env.example .env
npm install
npm run api:launch
```

Open a PR with a clear description and test steps.
