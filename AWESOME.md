# Awesome Multilogin & Antidetect

> A curated, opinionated list of resources for **multi-account operators**, **MMO teams**, and **developers** working with antidetect browsers, cloud phones, and proxy automation.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Multilogin Partner](https://img.shields.io/badge/Multilogin-Official%20Partner-0066FF?style=flat-square)](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

> **Disclosure:** the **Multilogin** links use the official partner UTM. Other vendor links are unaffiliated.

## Contents

- [Antidetect browsers](#antidetect-browsers)
- [Cloud phones / Android farms](#cloud-phones--android-farms)
- [Proxy providers](#proxy-providers)
- [Browser automation](#browser-automation)
- [API & SDKs](#api--sdks)
- [Anti-bot / fingerprint research](#anti-bot--fingerprint-research)
- [Comparisons (this repo)](#comparisons-this-repo)
- [Country & platform playbooks (this repo)](#country--platform-playbooks-this-repo)
- [Open-source tools](#open-source-tools)
- [Tutorials & courses](#tutorials--courses)
- [Communities](#communities)
- [Books / references](#books--references)
- [Contribute](#contribute)

## Antidetect browsers

- **[Multilogin](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)** — Mimic + Stealthfox, real Android cloud phones, 90 API endpoints. *(partner)*
- [AdsPower](https://www.adspower.com/) — Chromium antidetect, popular in Asia.
- [GoLogin](https://gologin.com/) — Cloud antidetect with Orbita browser.
- [Octo Browser](https://octobrowser.net/) — Polished UX, EU-friendly.
- [Dolphin Anty](https://anty.dolphin.tech/) — Affiliate-focused.
- [Incogniton](https://incogniton.com/) — Budget-friendly browser.
- [Kameleo](https://kameleo.io/) — Developer-leaning.
- [MoreLogin](https://www.morelogin.com/) — Browser + emulator hybrid.
- [Undetectable](https://undetectable.io/) — Local profile storage.
- [Nstbrowser](https://www.nstbrowser.io/) — Automation-first.

## Cloud phones / Android farms

- **[Multilogin Cloud Phone](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)** — Real hardware Android 12–14. *(partner)*
- [Geelark](https://geelark.com/) — Cloud Android with profile pooling.
- [VMOS Cloud](https://vmoscloud.com/) — Emulator-style cloud phone.
- [Nox / LDPlayer / BlueStacks](#) — Local emulators (high detection risk for ToS-strict platforms).

## Proxy providers

> Always read each provider's ToS. Quality > price for MMO ops.

- Residential: Bright Data, Oxylabs, Smartproxy, IPRoyal, SOAX, NetNut.
- Mobile / 4G: Airproxy, Proxy-cheap, Mobile-grade rotators.
- Datacenter (low-trust accounts only): Webshare, Proxy-seller.
- ISP / static: Nimble, Bright Data ISP, Rayobyte ISP.

## Browser automation

- [Playwright](https://playwright.dev/) — Multi-engine, fast, official Microsoft.
- [Puppeteer](https://pptr.dev/) — Chrome DevTools driver.
- [Selenium](https://www.selenium.dev/) — OG, broad ecosystem.
- [Playwright-extra](https://github.com/berstend/puppeteer-extra/tree/master/packages/playwright-extra) + stealth plugins.
- [DrissionPage](https://github.com/g1879/DrissionPage) — Hybrid requests + browser (Python).

### Connecting to Multilogin

- [Cookbook 01 — Playwright full session](docs/api/cookbook/01-playwright-full-session.md)
- [Cookbook 08 — Selenium grid pattern](docs/api/cookbook/08-selenium-grid-style.md)
- [Guide — Puppeteer](docs/guides/multilogin-api-puppeteer.md)

## API & SDKs

- **[Multilogin OpenAPI 3.0 spec](docs/api/openapi.json)** — generated from this repo.
- **[Swagger UI explorer](docs/api/swagger.html)** — interactive 90 endpoints.
- [Postman collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9) — official.
- [`lib/mlx_client.py`](lib/mlx_client.py) — MIT Python client.
- [`lib/mlx_client.mjs`](lib/mlx_client.mjs) — MIT Node client.

## Anti-bot / fingerprint research

- [BrowserLeaks](https://browserleaks.com/) — Test fingerprint signals.
- [Pixelscan](https://pixelscan.net/) — Antidetect quality test.
- [CreepJS](https://abrahamjuliot.github.io/creepjs/) — Deep browser introspection.
- [AmIUnique](https://amiunique.org/) — Fingerprint uniqueness.
- [WebGL Report](https://webglreport.com/) — GPU/canvas signals.
- [Webgl-fingerprint-defender](https://github.com/joue-quroi/webgl-fingerprint-defender) — Reference impl.

## Comparisons (this repo)

- [📊 Comparison matrix — 16 tools](docs/comparisons/comparison-matrix.md)
- [Multilogin vs AdsPower](docs/comparisons/multilogin-vs-adspower.md) (deep-dive)
- [Multilogin vs GoLogin](docs/comparisons/multilogin-vs-gologin.md) (deep-dive)
- [Multilogin vs Octo](docs/comparisons/multilogin-vs-octo-browser.md) (deep-dive)
- [Multilogin vs Dolphin](docs/comparisons/multilogin-vs-dolphin-anty.md) (deep-dive)
- [+12 more in `docs/comparisons/`](docs/comparisons/README.md)

## Country & platform playbooks (this repo)

- [30 country playbooks](docs/playbooks/README.md) — VN, ID, BR, IN, USA, DE, FR, ES, IT, JP, KR, TH, MX, NG, PK, EG, TR, PL, UA, AU, CA, MY, SG, TW, SA, AR, CO + diaspora.
- [13 platform playbooks](docs/platforms/README.md) — TikTok, Meta, Amazon, YouTube, LinkedIn, X, Telegram, WhatsApp, Discord, Reddit, Pinterest, Snapchat, Google Ads.
- [11 use-case guides](docs/use-cases/README.md) — scraping, airdrop, agency, dropship, traffic arbitrage, ORM, etc.

## Open-source tools

### In this repo

- [`tools/warmup-scheduler.mjs`](tools/warmup-scheduler.mjs) — staggered profile warmup with jitter.
- [`tools/api-search.mjs`](tools/api-search.mjs) — search 90 endpoints from CLI.
- [`tools/plan-calculator.mjs`](tools/plan-calculator.mjs) + [web version](docs/calculator.html).
- [`tools/proxy-check.mjs`](tools/proxy-check.mjs) — sanity-check a proxy URL.
- [`tools/generate_openapi.mjs`](tools/generate_openapi.mjs) — regen OpenAPI 3.0 spec.

### Elsewhere

- [`fakebrowser`](https://github.com/kkoooqq/fakebrowser) — research-only fingerprint kit.
- [`proxy-chain`](https://github.com/apify/proxy-chain) — Node proxy server.

## Tutorials & courses

- [Multilogin Academy](https://multilogin.com/academy/) — official.
- [Multilogin help center](https://multilogin.com/help/en_US).
- This repo: [55+ guides](docs/guides/README.md) · [12 hướng dẫn tiếng Việt](docs/guides/vi/README.md) · [Learning paths](docs/learn/README.md).

## Communities

- GitHub: this repo's [Discussions](https://github.com/multilogin-labs/multilogin-labs/discussions).
- Reddit: `r/multilogin` (community) · `r/MakeMoneyOnline` · `r/affiliatemarketing`.
- Discord servers for affiliate ad networks (search per niche).
- Telegram: language-specific MMO communities (use Multilogin to operate them safely).

## Books / references

- *The Manager's Guide to Web Application Security* — general anti-bot context.
- [Web Almanac chapter on Bots](https://almanac.httparchive.org/) — annual research.
- *Tracking the Trackers* (academic) — fingerprinting fundamentals.

## Contribute

PRs welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

Specifically helpful:

- New comparison entries with measured numbers.
- More language localizations under `locales/` and `docs/guides/<lang>/`.
- Cookbook recipes for niche stacks (n8n, Make, Bubble, Zapier).
- Anti-bot research links you trust.

---

**[→ Try Multilogin with partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)** · Codes **SAAS50** / **MIN50**
