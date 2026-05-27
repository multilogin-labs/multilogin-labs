# Integrations — Multilogin X

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

Connect Multilogin to your stack via **HTTP API** (90 endpoints) and **Launcher** (local profile control).

| Integration | Guide |
|---|---|
| Playwright | [multilogin-api-playwright](../guides/multilogin-api-playwright.md) · [cookbook 01](../api/cookbook/01-playwright-full-session.md) |
| Puppeteer | [multilogin-api-puppeteer](../guides/multilogin-api-puppeteer.md) |
| Selenium | [multilogin-api-selenium](../guides/multilogin-api-selenium.md) · [cookbook 08](../api/cookbook/08-selenium-grid-style.md) |
| Postman | [postman-setup](../api/postman-setup.md) |
| n8n | [multilogin-n8n-integration](../guides/multilogin-n8n-integration.md) |
| Zapier / Make | [multilogin-zapier-make](../guides/multilogin-zapier-make.md) |
| Docker / CI | [multilogin-docker-ci](../guides/multilogin-docker-ci.md) |
| Cron | [multilogin-cron-automation](../guides/multilogin-cron-automation.md) |

## Clients in this repo

| Language | Path |
|---|---|
| Python | [lib/mlx_client.py](../../lib/mlx_client.py) |
| Node.js | [lib/mlx_client.mjs](../../lib/mlx_client.mjs) |
| Scripts | [scripts/api/](../../scripts/api/) · [scripts/python/](../../scripts/python/) |

## CLI tools

```bash
npm run api:search -- profile start
npm run sitemap
node tools/plan-calculator.mjs
node tools/proxy-check.mjs
```

[API hub](../api/README.md) · [SEARCH_INDEX](../SEARCH_INDEX.md)
