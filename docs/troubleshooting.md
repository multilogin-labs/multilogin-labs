# Troubleshooting

> [Partner support](https://multilogin.com/help/en_US) · [pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

## Launcher & API

| Error | Fix |
|---|---|
| `401 Unauthorized` | Regenerate API token; check `.env` `MULTILOGIN_TOKEN` |
| `Connection refused` on launcher | Open Multilogin app; verify `MULTILOGIN_LAUNCHER_URL` |
| Profile won't start | Stop other sessions; check plan profile limit |
| Port not returned | Update app; retry with `automation: true` in payload |
| Python SSL error | Trust local launcher cert or use Node script first to verify |

## Proxy

| Symptom | Fix |
|---|---|
| Proxy check fails | Re-enter credentials; verify provider balance |
| Wrong country shown | Sticky session expired — assign new session ID |
| Slow pages | Closer geo node; switch ISP vs residential |
| Instant ban on login | Datacenter IP on strict platform — use residential/mobile |

## Bans & detection

| Symptom | Fix |
|---|---|
| Checkpoint after login | Warmup longer; match timezone/locale to IP |
| Account disabled | Retire profile chain; don't reuse fingerprint |
| Zero TikTok views | Mobile/cloud phone + mobile proxy |
| Linked accounts flagged | Strict 1 proxy + 1 payment method per identity |
| Canvas mismatch | Use automatic fingerprint; don't manual-spoof inconsistently |

## Automation

| Symptom | Fix |
|---|---|
| Playwright can't connect | Confirm debug port from start response; set `MULTILOGIN_DEBUG_PORT` |
| Selenium detached | Use `debuggerAddress` not WebDriver launch |
| Headless detected | Use headed mode for review/sensitive flows |
| Rate limited API | Respect plan RPM; add delays between starts |

## Billing

| Question | Answer |
|---|---|
| Upgrade mid-cycle | Prorated instantly |
| Downgrade | Next billing cycle |
| Unused proxy GB | Rolls over on Multilogin premium traffic |
| Promo not applied | Enter **SAAS50** or **MIN50** at checkout via [partner URL](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) |

## Still stuck?

- [Multilogin Knowledge Base](https://multilogin.com/help/en_US)
- [FAQ](faq.md)
- [GitHub issue](https://github.com/multilogin-labs/multilogin-labs/issues/new/choose)
