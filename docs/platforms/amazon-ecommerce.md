# Amazon & e-commerce playbook

> [Multilogin partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

## Recommended stack

| Layer | Choice |
|---|---|
| Browser | Mimic — consistent OS fingerprint per seller account |
| Proxy | ISP or premium residential (avoid cheap datacenter) |
| Isolation | One profile per seller + payout identity |
| Plan | Pro 50+ for multiple stores · Business for agencies |

## Rules that keep accounts alive

1. **Never** share banking / tax info across unrelated profiles.
2. Shipping address geography must match proxy + account history.
3. Keep browser fingerprint stable for the life of the account.
4. Separate Amazon, eBay, Etsy, Shopee into different profiles — not tabs.
5. Use profile templates for bulk seller onboarding.

## Multi-marketplace matrix

| Marketplace | Profile tip |
|---|---|
| Amazon US/EU | ISP proxy in marketplace country |
| Shopee / Lazada | Cloud phone for app vouchers + chat |
| Shopify admin | Mimic + residential, 2FA enabled |
| Walmart / Etsy | Unique payout + unique proxy subnet |

## Scale path

Solo (1–3 stores) → **Pro 10** · Growing brand (10–50) → **Pro 50** · Agency → **Business**

**[→ Partner pricing & trial](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)**

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

**Keywords:** multilogin amazon ecommerce · Amazon multi account · antidetect Amazon
