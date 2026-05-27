# Instagram multi-account playbook

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

**Use case:** Reels, shops, DM outreach

## Recommended stack

| Layer | Choice |
|---|---|
| Device | Cloud phone and/or Mimic |
| Proxy | Mobile/residential matching target country |
| Plan | Pro 50+ for scale |

## Checklist

1. One identity = one proxy subnet = one payment cluster.
2. Warm 3–7 days before monetization.
3. Tag profiles: `instagram`, `warmup`, `client-slug`.
4. Automate via [API quick start](../api/quick-start.md).


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

**Keywords:** multilogin instagram · Instagram multi account · antidetect Instagram


**[→ $2 trial](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)**
