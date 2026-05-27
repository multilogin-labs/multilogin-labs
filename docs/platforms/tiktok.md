# TikTok multi-account playbook

> [Multilogin partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

## Recommended stack

| Layer | Choice |
|---|---|
| Device | **Cloud phone** (Android 12–14) — not emulator |
| Proxy | Mobile or residential, geo = target country |
| Browser backup | Mimic profile for web creator studio |
| Plan | Pro 50+ for mobile minutes + proxy GB |

## Setup checklist

1. Create cloud phone profile → match GPS to proxy city.
2. Install TikTok from Multilogin app store — don’t sideload random APKs.
3. Warm up 3–5 days: watch, like, follow — no links or promos.
4. One phone = one TikTok identity. Never switch proxy mid-session.
5. Use tags in dashboard: `tiktok`, `warmup`, `monetized`.

## Automation

- Web flows: [Playwright script](../../scripts/playwright/connect-profile.mjs)
- API launch: [launch-profile.mjs](../../scripts/api/launch-profile.mjs)

## Common bans & fixes

| Issue | Fix |
|---|---|
| Zero views | IP flagged — rotate to mobile proxy, re-warm |
| Login loop | Clear app data only via new cloud phone clone |
| Device ban | Retire profile; don’t reuse fingerprint chain |

**[→ Start trial with cloud phone minutes included](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)**

## Automation (API)

```bash
# Start profile (Launcher must run locally)
npm run api:search -- profile start
python scripts/python/launch_profile.py
```

- [Quick start](../api/quick-start.md) · [Cookbook](../api/cookbook/README.md)
- Guide: [platform-specific](../guides/README.md)

## Scaling checklist

| Stage | Action |
|---|---|
| Day 1–3 | Proxy + fingerprint lock, no mass actions |
| Day 4–7 | Organic warmup (watch, browse, light engage) |
| Week 2+ | Ads / seller / monetization per platform rules |
| Scale | [Clone profiles](../api/cookbook/06-clone-profile-farm.md), tag by client |

## Related

- [Country playbooks](../playbooks/README.md)
- [Comparisons](../comparisons/README.md)
- [Integrations](../integrations/README.md)

**Keywords:** multilogin tiktok · TikTok multi account · antidetect TikTok
