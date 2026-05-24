# Antifingerprint Checklist

Use this before scaling any multi-account operation with Multilogin.

## Profile-level

- [ ] Fingerprint mode: **automatic** from real-user dataset
- [ ] Browser core matches target (Mimic for Chromium sites, Stealthfox when needed)
- [ ] Timezone = proxy geo
- [ ] Language / locale = proxy country
- [ ] WebRTC: **altered** or disabled leak to real IP
- [ ] Canvas / WebGL / Audio: **noise or mask** enabled (default in Multilogin)
- [ ] Do not copy cookies between profiles without export/import workflow

## Session-level

- [ ] Unique proxy per profile
- [ ] No shared payment methods across unrelated profiles
- [ ] Separate email/phone recovery per identity
- [ ] Human-like warmup (browse, scroll, idle) before high-risk actions
- [ ] Consistent user-agent chain for the profile lifetime

## Team / scale

- [ ] Tag profiles by client, platform, and risk tier
- [ ] Use profile templates for bulk create — don’t hand-configure 100+
- [ ] API rate limits: respect plan RPM (50–100 depending on tier)
- [ ] Audit workspace logs for accidental profile sharing

## Platform-specific notes

| Platform | Tip |
|---|---|
| Facebook / Meta | Residential + aged cookie; avoid headless on review flows |
| Google | Match OS fingerprint to account history |
| TikTok | Prefer mobile proxy or cloud phone for app parity |
| Amazon | Stable IP + consistent shipping address per profile |

## Tools in this repo

- Launch & automate: [`scripts/`](../scripts/)
- Proxy template: [`configs/proxy-template.json`](../configs/proxy-template.json)

Need a plan with API + proxy bonus? [**Partner pricing →**](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
