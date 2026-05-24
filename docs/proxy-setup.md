# Proxy Setup for Multilogin

> Plans include monthly premium proxy traffic. [See pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

## Proxy types

| Type | Best for |
|---|---|
| **Multilogin built-in** | Quick start, included GB on plan, rollover |
| **Residential** | Social, ads, marketplaces — highest trust |
| **Mobile** | TikTok, Instagram, app-style flows |
| **ISP / datacenter** | Scraping at scale (higher block risk on social) |

## Rules that prevent bans

1. **One proxy per profile** — never rotate IP mid-session on a warmed account.
2. **Geo match** — timezone, language, and IP country must align.
3. **Verify before launch** — use Multilogin’s proxy checker in the profile editor.
4. **Sticky sessions** — keep the same exit IP for 24h+ on aged accounts.
5. **Separate pools** — don’t mix “burner” and “money” accounts on the same subnet.

## Template

See [`configs/proxy-template.json`](../configs/proxy-template.json) for a copy-paste structure.

## Built-in proxy bonus by plan

| Plan | Monthly proxy bonus |
|---|---|
| Pro 10 | 1 GB |
| Pro 50 | 3 GB |
| Pro 100 | 5 GB |
| Business | 10 GB+ |

Extra traffic: **$3.50 / GB** (unused rolls over).

## Troubleshooting

| Symptom | Fix |
|---|---|
| Profile shows wrong country | Re-check proxy credentials; clear DNS cache |
| Slow page loads | Switch closer geo or use ISP instead of far residential |
| Instant ban on new account | Warm up IP; avoid datacenter on strict platforms |
