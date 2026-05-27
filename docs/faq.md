# FAQ — Multilogin Labs

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`**

## General

**What is Multilogin?**  
Cloud-based multi-account platform: antidetect browser profiles, real Android cloud phones, built-in proxies, team collaboration, API automation.

**Is Multilogin legal?**  
Tool for privacy and legitimate multi-account workflows. You are responsible for complying with each platform's Terms of Service.

**Multilogin vs antidetect browser?**  
Multilogin is an antidetect solution plus cloud phones, proxies, and team features — not browser-only.

## Pricing & trial

**How much is Multilogin?**  
Pro 10 from ~$7.08/mo (annual) or $11/mo. See [plan calculator](../tools/plan-calculator.mjs) or [SEARCH_INDEX](SEARCH_INDEX.md).

**Is there a free trial?**  
**$2 for 3 days** — 5 profiles, API, 200 MB proxy, 60 mobile minutes.

**Promo codes?**  
**`SAAS50`** and **`MIN50`** at checkout via [partner link](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).

**Annual discount?**  
~**35% off** vs monthly on Pro and Business.

## Plans

**Which plan for solo use?** → **Pro 10** (10 profiles)  
**Small team 20–50 accounts?** → **Pro 50**  
**Agency 100+?** → **Pro 100** or **Business** (300–10,000 profiles)

**Does Pro 10 include API?**  
Yes — automation token from Pro 10 upward.

**Cloud phone minutes?**  
Included on Pro 50+ (60–150+ min/mo). Pro 10 trial includes one-time minutes.

## Technical

**Mimic vs Stealthfox?**  
Mimic = Chromium. Stealthfox = Firefox-based. See [glossary](glossary.md).

**Cloud phone vs emulator?**  
Multilogin uses **real Android hardware** in the cloud — not emulators.

**Where is data stored?**  
Local or encrypted cloud — per profile settings.

**Supported automation?**  
Playwright, Puppeteer, Selenium, REST API. See [scripts](../scripts/).

**Launcher URL?**  
Default `https://launcher.mlx.yt:45001` — set in `.env`.

## Proxy

**Included proxy traffic?**  
Pro 10: 1 GB/mo · Pro 50: 3 GB · Pro 100: 5 GB · Business: 10 GB+. Rollover unused.

**Extra proxy cost?**  
$3.50/GB premium residential.

**One proxy per profile?**  
**Yes** — best practice for ban prevention. [proxy-setup.md](proxy-setup.md)

## Bans & safety

**Can I avoid bans 100%?**  
No tool guarantees zero bans. Isolation + warmup + quality proxy minimizes risk. [troubleshooting.md](troubleshooting.md)

**GDPR / 2FA?**  
Multilogin is GDPR compliant with 2FA support.

## Comparisons

See [comparisons/](comparisons/README.md) — AdsPower, GoLogin, Octo, MoreLogin, DuoPlus, Dolphin, Incogniton, Kameleo, VMOS, BitBrowser, and more.

## Repo

**Where are scripts?**  
[scripts/](../scripts/) (Node) · [scripts/python/](../scripts/python/) (Python)

**How to contribute?**  
[CONTRIBUTING.md](../CONTRIBUTING.md)

**Full keyword list?**  
[SEARCH_INDEX.md](SEARCH_INDEX.md)

## API (Multilogin X)

**How many API endpoints?**  
**90** documented in [api/endpoints-index.md](api/endpoints-index.md).

**Launcher vs Cloud API?**  
- Cloud: `https://api.multilogin.com` — profiles, workspace, proxy  
- Launcher: `https://launcher.mlx.yt:45001` — start/stop profiles (app must run)

**How to start profile via API?**  
`GET /api/v2/profile/f/{folder_id}/p/{profile_id}/start` — see [quick-start](api/quick-start.md).

**folder_id vs profile_id?**  
Both UUIDs from Multilogin app. Required for Launcher start. See [guide](guides/multilogin-folder-id-profile-id.md).

**Automation token vs sign-in token?**  
Automation token = longer life + higher RPM. Recommended for scripts. [authentication](api/authentication.md)

**Playwright with Multilogin?**  
Start profile with `automation_type=playwright`, connect to returned port. [cookbook](api/cookbook/01-playwright-full-session.md)

**API errors 401?**  
Token expired — refresh or use automation token. [troubleshooting](troubleshooting.md)

**Postman?**  
[postman-setup.md](api/postman-setup.md) + [official collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)

## Comparisons

**Multilogin vs AdsPower / GoLogin / Octo?**  
[comparisons/](comparisons/README.md) — 13 detailed guides.

**Best alternative to VMOS emulator?**  
[multilogin-vs-vmos-cloud](comparisons/multilogin-vs-vmos-cloud.md) — real Android hardware.
