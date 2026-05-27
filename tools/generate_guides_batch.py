#!/usr/bin/env python3
"""Generate SEO guide markdown files."""
from pathlib import Path

AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)

GUIDES = [
    (
        "multilogin-google-ads-accounts",
        "Multilogin for Google Ads multiple accounts",
        "google ads multilogin",
        "Isolate Google Ads MCC and client accounts with separate browser fingerprints and billing profiles.",
        [
            "One Mimic profile per Ads account — never share cookies with Search Console.",
            "Match timezone and language to billing country.",
            "Use residential proxy in same region as payment method.",
            "Enable 2FA on each profile; store backup codes in secure vault.",
        ],
    ),
    (
        "multilogin-shopee-lazada-seller",
        "Shopee & Lazada multi-store with Multilogin",
        "shopee lazada multilogin seller",
        "Southeast Asia marketplace sellers run multiple shops with device isolation.",
        [
            "Cloud phone for mobile seller apps; Mimic for seller center web.",
            "One store per phone — Indonesia/Philippines/Vietnam proxies.",
            "Warm accounts with organic orders before scaling ads.",
            "See [Indonesia playbook](../playbooks/indonesia.md).",
        ],
    ),
    (
        "multilogin-crypto-exchange",
        "Crypto exchange multi-account (CEX)",
        "multilogin binance exchange kyc",
        "Separate exchange accounts for trading teams — compliance is your responsibility.",
        [
            "Unique profile per account; never reuse KYC documents across banned accounts.",
            "Match IP to declared residence; avoid VPN datacenter IPs.",
            "API keys only on automation profiles with locked-down access.",
        ],
    ),
    (
        "multilogin-linkedin-automation",
        "LinkedIn outreach at scale",
        "linkedin multilogin automation",
        "Sales teams manage multiple LinkedIn identities without session collision.",
        [
            "Mimic + residential proxy per persona.",
            "Limit daily connection requests to avoid restrictions.",
            "Use [team workspace](multilogin-team-workspace.md) for handoffs.",
        ],
    ),
    (
        "multilogin-reddit-account-farming",
        "Reddit account management",
        "reddit multilogin accounts",
        "Community marketing with isolated karma-building profiles.",
        [
            "Aged proxies; slow warmup commenting.",
            "One subreddit niche per profile cluster.",
        ],
    ),
    (
        "multilogin-telegram-multi-session",
        "Telegram multiple accounts",
        "telegram multilogin",
        "Run Telegram Web or mobile sessions in parallel cloud phones.",
        [
            "Cloud phone per SIM-backed account when possible.",
            "Web Telegram in Mimic for support bots.",
        ],
    ),
    (
        "multilogin-mobile-proxy-guide",
        "Mobile proxy setup for Multilogin",
        "multilogin mobile proxy 4g",
        "Mobile IPs reduce platform friction for social and marketplaces.",
        [
            "Assign proxy at profile level before first login.",
            "Validate with [proxy check](../../tools/proxy-check.mjs) or Launcher validate endpoint.",
            "Rotate only between sessions, not mid-session.",
        ],
    ),
    (
        "multilogin-residential-proxy",
        "Residential proxies with Multilogin",
        "multilogin residential proxy",
        "Built-in Multilogin proxy vs bring-your-own SOCKS5/HTTP.",
        [
            "Generate via API: [cookbook 13](../api/cookbook/13-generate-multilogin-proxy.md).",
            "Pro plans include proxy GB — track usage in dashboard.",
        ],
    ),
    (
        "multilogin-linux-server",
        "Multilogin on Linux VPS",
        "multilogin linux headless vps",
        "Run desktop app on Linux server with Xvfb or dedicated VM.",
        [
            "Launcher must reach local Multilogin agent — not cloud-only.",
            "Use automation token; schedule [cron](multilogin-cron-automation.md).",
        ],
    ),
    (
        "multilogin-windows-vps",
        "Windows VPS for Multilogin farms",
        "multilogin windows vps rdp",
        "Common setup for agencies: Windows Server + RDP + Multilogin desktop.",
        [
            "One VPS per operator or use folder permissions.",
            "Stop all profiles on maintenance: [guide](multilogin-stop-all-profiles.md).",
        ],
    ),
    (
        "multilogin-n8n-integration",
        "n8n + Multilogin API workflows",
        "multilogin n8n automation",
        "Trigger profile start/stop from n8n HTTP nodes.",
        [
            "Store automation token in n8n credentials.",
            "POST signin only in secure credential store.",
            "Chain: start profile → wait → webhook to your app.",
        ],
    ),
    (
        "multilogin-agency-setup",
        "Agency Multilogin workspace setup",
        "multilogin agency white label",
        "Folders per client, role-based access, billing separation.",
        [
            "Business plan for 300+ profiles and team seats.",
            "Tag profiles: `client-slug`, `platform`, `status`.",
            "Export reports via profile search API.",
        ],
    ),
    (
        "multilogin-ebay-seller",
        "eBay multiple seller accounts",
        "ebay multilogin seller",
        "Isolate eBay seller identities with consistent device + IP history.",
        [
            "Mimic profile per seller account.",
            "PayPal/payout details must align with profile geo.",
        ],
    ),
    (
        "multilogin-etsy-shop",
        "Etsy multi-shop management",
        "etsy multilogin",
        "Handmade sellers operating several brands in one workspace.",
        [],
    ),
    (
        "multilogin-pinterest-pins",
        "Pinterest marketing accounts",
        "pinterest multilogin",
        "Affiliate and brand accounts with separate cookies.",
        [],
    ),
    (
        "multilogin-snapchat-ads",
        "Snapchat Ads manager isolation",
        "snapchat ads multilogin",
        "Ad accounts for agencies — browser isolation per client.",
        [],
    ),
    (
        "multilogin-onlyfans-creator",
        "Creator platform isolation",
        "onlyfans multilogin creator",
        "Separate creator identities — one profile per brand.",
        [],
    ),
    (
        "multilogin-upwork-freelancer",
        "Upwork & Fiverr multiple profiles",
        "upwork fiverr multilogin",
        "Freelance teams — check platform ToS before multi-accounting.",
        [],
    ),
    (
        "multilogin-discord-accounts",
        "Discord community accounts",
        "discord multilogin",
        "Moderation and community bots across servers.",
        [],
    ),
    (
        "multilogin-shopify-stores",
        "Shopify multi-store",
        "shopify multilogin stores",
        "Dropshipping operators managing several Shopify admin sessions.",
        [],
    ),
    (
        "multilogin-stripe-accounts",
        "Stripe Connect / multiple businesses",
        "stripe multilogin",
        "Separate browser sessions per Stripe dashboard login.",
        [],
    ),
    (
        "multilogin-captcha-bypass",
        "Reduce captchas with clean fingerprints",
        "multilogin captcha fingerprint",
        "Consistent fingerprints + quality proxies lower captcha rate.",
        [
            "Avoid datacenter IPs on Google/login flows.",
            "Use [fingerprint masking](multilogin-fingerprint-masking.md).",
        ],
    ),
    (
        "multilogin-2fa-workflow",
        "2FA with Multilogin profiles",
        "multilogin 2fa totp",
        "Store authenticator seeds per profile; API supports 2FA on signin.",
        [
            "See [authentication](../api/authentication.md) for 2FA signin flow.",
        ],
    ),
    (
        "multilogin-profile-search-tags",
        "Search profiles by tags API",
        "multilogin profile search tags",
        "Organize farms with tags; query via profile search endpoint.",
        [
            "Cookbook: [bulk search](../api/cookbook/03-bulk-profile-search.md).",
        ],
    ),
    (
        "multilogin-migrate-from-adspower",
        "Migrate from AdsPower to Multilogin",
        "migrate adspower multilogin",
        "Export cookies and recreate profiles; compare [vs AdsPower](../comparisons/multilogin-vs-adspower.md).",
        [
            "Import cookies: [cookbook 09](../api/cookbook/09-import-cookies.md).",
            "Use quick profile for one-off tests.",
        ],
    ),
    (
        "multilogin-migrate-from-gologin",
        "Migrate from GoLogin",
        "migrate gologin multilogin",
        "Step-by-step move with proxy and fingerprint parity.",
        [],
    ),
    (
        "multilogin-pricing-guide-2026",
        "Multilogin pricing explained 2026",
        "multilogin price cost plans",
        "Pro vs Business, annual discount, trial, promo codes SAAS50 MIN50.",
        [
            "Run [plan calculator](../../tools/plan-calculator.mjs).",
            f"[Partner pricing]({AFFILIATE})",
        ],
    ),
    (
        "multilogin-affiliate-earnings",
        "Multilogin affiliate & partner links",
        "multilogin affiliate partner",
        "This repo is a partner hub — use official pricing links with UTM.",
        [],
    ),
    (
        "multilogin-zapier-make",
        "Zapier / Make.com + Multilogin",
        "multilogin zapier make integration",
        "HTTP webhooks to Launcher and Cloud API from no-code tools.",
        [],
    ),
    (
        "multilogin-whatsapp-business",
        "WhatsApp Business multi-device",
        "whatsapp business multilogin cloud phone",
        "Cloud phone profiles for WhatsApp Business per brand line.",
        [],
    ),
]

TEMPLATE = """# {title}

> [Partner pricing →]({affiliate}) · **`SAAS50`** · **`MIN50`**

{intro}

## Why Multilogin

| Feature | Benefit |
|---|---|
| Antidetect browser | Isolated fingerprints per account |
| Cloud phone | Real Android — not emulator |
| API (90 endpoints) | [Automate](../api/quick-start.md) start/stop at scale |
| Built-in proxy | Mobile & residential in-dashboard |

## Setup steps

{steps}

## API & scripts

1. [Quick start](../api/quick-start.md) — token, folder_id, profile_id.
2. [Cookbook](../api/cookbook/README.md) — copy-paste recipes.
3. [mlx_client.py](../../lib/mlx_client.py) · [launch-profile.mjs](../../scripts/api/launch-profile.mjs)

## Related

- [SEARCH_INDEX](../SEARCH_INDEX.md)
- [FAQ](../faq.md)
- [Comparisons](../comparisons/README.md)

**Keywords:** {keywords} · multilogin x · multilogin labs
"""


def main():
    out = Path(__file__).resolve().parents[1] / "docs" / "guides"
    rows = []
    for slug, title, kw, intro, tips in GUIDES:
        steps = "\n".join(f"{i+1}. {t}" for i, t in enumerate(tips)) if tips else (
            "1. Create profile in Multilogin app.\n"
            "2. Assign proxy matching target geo.\n"
            "3. Warm account before monetization.\n"
            "4. Automate via API when stable."
        )
        path = out / f"{slug}.md"
        if path.exists():
            continue
        path.write_text(
            TEMPLATE.format(
                title=title,
                affiliate=AFFILIATE,
                intro=intro,
                steps=steps,
                keywords=kw,
            ),
            encoding="utf-8",
        )
        rows.append((title, slug))
        print("created", slug)

    readme = out / "README.md"
    existing = readme.read_text(encoding="utf-8") if readme.exists() else ""
    new_lines = []
    for title, slug in rows:
        line = f"| [{title}]({slug}.md) | {title.split('—')[0].strip()[:60]} |"
        if slug not in existing:
            new_lines.append(line)
    if new_lines and "| Guide |" in existing:
        insert = "\n".join(new_lines) + "\n"
        readme.write_text(
            existing.replace(
                "\n[API hub](../api/README.md)",
                "\n" + insert + "\n[API hub](../api/README.md)",
            ),
            encoding="utf-8",
        )
    print(f"done: {len(rows)} new guides")


if __name__ == "__main__":
    main()
