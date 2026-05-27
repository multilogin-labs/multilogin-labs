# Google Ads playbook

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

**Use case:** MCC, multiple ad accounts

## Recommended stack

| Layer | Choice |
|---|---|
| Profile | Mimic + ISP/residential |
| Plan | Pro 50+ |
| Isolation | 1 identity = 1 proxy = 1 payment cluster |

## Checklist

1. Match timezone/locale to proxy country.
2. Warm up 3–7 days before ads or mass actions.
3. Never cross-import cookies between unrelated brands.
4. Tag profiles in Multilogin dashboard by client/campaign.
5. Use [antifingerprint checklist](../antifingerprint-checklist.md).

## Common issues

| Issue | Fix |
|---|---|
| Instant restriction | Low-trust IP — switch residential/mobile |
| Verification loop | Headed session; consistent fingerprint |
| Linked accounts | Separate proxy subnets per profile group |

**[→ Start $2 trial](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)**

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

**Keywords:** multilogin google ads · Google Ads multi account · antidetect Google Ads
