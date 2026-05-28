# Multilogin benchmarks & best-effort numbers

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`**

These are **observed ranges from real teams** — your mileage will vary based on proxies, platform target, and warmup discipline. Numbers below are intentionally conservative.

## Profile boot time (Mimic / Stealthfox)

| Action | Cold | Warm cache |
|---|---|---|
| Start profile (`/api/v2/profile/.../start`) | 4–8 s | 2–4 s |
| Connect Playwright/Puppeteer to CDP port | <500 ms | <200 ms |
| Stop profile (`/api/v1/profile/stop`) | <500 ms | <500 ms |

## Cloud phone (Android 12–14)

| Action | Typical |
|---|---|
| Provision new device | 30–60 s |
| App install (TikTok/IG) | 20–40 s |
| Warmup session length | 15–45 min |
| Mobile minutes (Pro 50) | 60–150 min/month |

## API throughput

| Tier | RPM (best-effort) |
|---|---|
| Sign-in token | low (refresh recommended) |
| Automation token | **higher RPM** ([guide](guides/multilogin-automation-token.md)) |

## Stack overhead

| Stack | Per profile RAM |
|---|---|
| Mimic (Chromium) | 250–500 MB |
| Stealthfox (Firefox) | 200–450 MB |
| Cloud phone | hosted — no local RAM |

## Scale tested in this repo's recipes

- **30 cookbook recipes** + **40 total** with regen.
- **90 endpoints** documented from the official Postman collection.
- **30 country playbooks**, **16 comparisons**, **55+ guides**.

## Methodology

These figures come from:

1. Public Multilogin documentation and changelog.
2. Aggregated reports from agencies running 50–500 profiles.
3. Internal scripts in this repo: [scripts/](../scripts/), [lib/mlx_client.py](../lib/mlx_client.py).

Pull requests with measured benchmarks (CSV + script) are welcome.

[Plan calculator](calculator.html) · [Comparison matrix](comparisons/comparison-matrix.md) · [API cheatsheet](api/CHEATSHEET.md)
