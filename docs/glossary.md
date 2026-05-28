# Glossary — Antidetect & MMO

> [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

| Term | Definition |
|---|---|
| **Antidetect browser** | Browser that masks or randomizes fingerprints so each profile appears as a unique device. |
| **Fingerprint** | Combined signals (Canvas, WebGL, fonts, timezone, etc.) used to identify a browser instance. |
| **Mimic** | Multilogin's Chromium-based antidetect engine. |
| **Stealthfox** | Multilogin's Firefox-based antidetect engine. |
| **Cloud phone** | Real Android device hosted in the cloud — persistent apps, SIM-less, hardware IDs. |
| **Profile** | Isolated browser or mobile environment with its own cookies, proxy, and fingerprint. |
| **Residential proxy** | IP from real ISP/home connection — high trust for social platforms. |
| **Mobile proxy** | Cellular IP — strong for TikTok/Instagram app flows. |
| **Sticky session** | Keeping the same exit IP for hours/days on one account. |
| **Warmup** | Gradual human-like activity before monetization or ads. |
| **Sybil detection** | Platform logic linking multiple accounts to one operator. |
| **CDP** | Chrome DevTools Protocol — used to connect Playwright/Puppeteer to running profiles. |
| **Launcher API** | Local Multilogin service that starts/stops profiles for automation. |
| **Automation token** | API bearer token for script access (Pro 10+). |
| **RPM** | API requests per minute limit by plan tier. |
| **MMO** | Make Money Online — multi-account, affiliate, e-commerce, farming workflows. |
| **Phone farming** | Operating many mobile identities via cloud phones or devices. |
| **Multi-accounting** | Running multiple platform accounts with isolated identities. |
| **ORM** | Online reputation management — multiple accounts for reviews/mentions. |
| **Traffic arbitrage** | Buying cheap traffic, monetizing across multiple ad/publisher accounts. |
| **folder_id** | Workspace folder UUID — required in Launcher start URL path. |
| **profile_id** | Unique UUID for one browser or cloud phone profile. |
| **Quick profile** | Temporary profile created via API v3 — auto-deleted after stop. |
| **headless_mode** | Launcher flag to run browser without visible window for automation. |
| **Cloud API** | `api.multilogin.com` — workspace, profiles, proxy, auth. |
| **Postman collection** | Official Multilogin X API reference for testing endpoints. |
| **Cookie import** | Restore session state when migrating from another antidetect tool. |
| **OpenAPI** | Industry-standard machine-readable API description (Swagger 3.0). |
| **Swagger UI** | Interactive HTML explorer rendered from OpenAPI — see [api/swagger.html](api/swagger.html). |
| **Webhook** | Outbound HTTP call from your service to receive event notifications. |
| **CDP port** | Local TCP port exposing Chrome DevTools Protocol on a launched profile. |
| **Workspace** | Top-level Multilogin team container (folders, profiles, members). |
| **Folder** | Sub-container inside a workspace; required in Launcher start URL. |
| **Member role** | Owner / admin / user — controls which folders and profiles each seat sees. |
| **Promo code** | Coupon at checkout — `SAAS50`, `MIN50` for Multilogin Labs partner link. |
| **Partner link** | UTM-tagged pricing URL crediting Multilogin Labs as referrer. |
| **Trial** | $2 / 3-day evaluation tier — 5 profiles, API, proxy GB, mobile minutes. |
| **Warmup scheduler** | Local CLI in this repo that staggers profile starts with jitter. |

See also: [SEARCH_INDEX.md](SEARCH_INDEX.md) · [faq.md](faq.md)
