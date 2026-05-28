#!/usr/bin/env python3
"""Append a long-form deep-dive section to selected comparison files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)

DEEP = {
    "adspower": {
        "name": "AdsPower",
        "audience": "Asian e-commerce sellers, dropshippers, social ads operators",
        "strengths": [
            "Strong Chinese-market UX and templates",
            "Affordable entry tiers for browser-only ops",
            "RPA macro recorder built into the desktop app",
        ],
        "weaknesses": [
            "No real cloud phone — emulator approach for mobile",
            "Proxy is bring-your-own; no included GB/month bundle on most tiers",
            "API is Chromium-debugger centric; less Postman-grade documentation",
        ],
        "switch_when": "you need TikTok/IG app farming, agency team isolation, or 90 documented MLX endpoints with curl examples.",
    },
    "gologin": {
        "name": "GoLogin",
        "audience": "Affiliate marketers and freelancers running 10–100 web profiles",
        "strengths": [
            "Cloud profile sync between machines",
            "Orbita browser fork tuned for fingerprint randomization",
            "Free tier exists for tiny ops",
        ],
        "weaknesses": [
            "No real Android cloud phone for app-based platforms",
            "Mobile minutes / WhatsApp / TikTok app flows require third-party tools",
            "Team plans escalate quickly compared to Multilogin Business",
        ],
        "switch_when": "your roadmap includes app-based monetization, team onboarding, or programmatic access to a documented API.",
    },
    "octo-browser": {
        "name": "Octo Browser",
        "audience": "European traffic teams and SMM agencies",
        "strengths": [
            "Polished UX and stable Chromium fork",
            "Decent API for profile lifecycle",
            "Good support reputation in EU markets",
        ],
        "weaknesses": [
            "Cloud phone is not a first-class product",
            "Built-in proxy bundles less generous than Multilogin Pro plans",
            "Stealthfox-style Firefox engine is limited or absent",
        ],
        "switch_when": "you need both Chromium and Firefox antidetect engines, plus phone-based identities for TikTok, Telegram, and WhatsApp.",
    },
    "dolphin-anty": {
        "name": "Dolphin Anty",
        "audience": "Affiliate networks, ad arbitrage teams, FB Ads farmers",
        "strengths": [
            "Affiliate-friendly pricing and free tier",
            "FB-specific helpers (proxy preset, useful macros)",
            "Sizable user community in CIS region",
        ],
        "weaknesses": [
            "Heavy focus on Facebook can leave gaps for marketplace/seller flows",
            "Cloud phone offering is limited",
            "API lacks the breadth of Multilogin's 90 endpoints",
        ],
        "switch_when": "you scale beyond FB into Amazon/Shopee/TikTok or need a fully documented automation surface.",
    },
}

DEEP_TEMPLATE = """
## Deep-dive: when {name} vs Multilogin really matters

### Audience overlap

{name} is most popular among **{audience}**. Multilogin overlaps that audience but additionally covers agencies running 100–10,000 profiles, marketplace sellers needing **real Android cloud phones**, and developer teams that want a first-class API + cookbook.

### {name} strengths (be honest)

{strengths}

### {name} gaps where Multilogin pulls ahead

{weaknesses}

### The switching trigger

Most teams switch from **{name}** to Multilogin when {switch_when}

### Cost-of-ownership math

A typical small team comparison:

| Component | {name} (typical) | Multilogin Pro 50 |
|---|---|---|
| Browser profiles | included | 50 included |
| Antidetect engines | 1 (Chromium) | **2 (Mimic + Stealthfox)** |
| Cloud phone | extra vendor / emulator | **included minutes (Pro 50+)** |
| Residential proxy | extra (often $50–200/mo) | **bundled GB/month** |
| Documented API | partial | **90 endpoints + cookbook ×40** |
| Postman collection | varies | [yes](../api/postman-setup.md) |

Even before the **SAAS50 / MIN50** partner discount, the bundled stack often costs less than Browser-tool + Proxy + Phone-tool sourced separately.

### 7-day migration plan

1. **Day 1** — Audit current {name} profile count, tag list, proxy assignments. Export cookies where possible.
2. **Day 2** — Activate Multilogin **$2 trial** via the [partner link]({affiliate}). Create the same folder structure.
3. **Day 3** — Use the [import cookies cookbook](../api/cookbook/09-import-cookies.md) to bring sessions across.
4. **Day 4** — Re-assign proxies; validate with [proxy-check](../../tools/proxy-check.mjs) or Launcher proxy validate endpoint.
5. **Day 5** — Add team members; configure [agency setup](../guides/multilogin-agency-setup.md).
6. **Day 6** — Wire automation: [Playwright](../api/cookbook/01-playwright-full-session.md), [Selenium](../api/cookbook/08-selenium-grid-style.md), or [Puppeteer](../guides/multilogin-api-puppeteer.md).
7. **Day 7** — Run [warmup scheduler](../../tools/warmup-scheduler.mjs) on 10–20 profiles before fully cutting over.

### Risk callouts

- **Account history is fragile.** Never reuse cookies across mismatched proxies or fingerprints.
- **Compliance is your responsibility.** Multi-account on platforms with strict ToS (Stripe, Binance, etc.) carries platform risk regardless of tool.
- **Pricing can change.** Always confirm via the [partner pricing page]({affiliate}).

### TL;DR

If {name} is solving 70% of your problem and the remaining 30% involves **cloud phones, second browser engine, agency scale, or documented API**, Multilogin is the upgrade path. Run the **$2 trial** and benchmark side-by-side over a week.

**[→ Start partner trial]({affiliate})**
"""


def main():
    base = DOCS / "comparisons"
    for slug, cfg in DEEP.items():
        path = base / f"multilogin-vs-{slug}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "## Deep-dive: when" in text:
            continue
        block = DEEP_TEMPLATE.format(
            name=cfg["name"],
            audience=cfg["audience"],
            strengths="\n".join(f"- {s}" for s in cfg["strengths"]),
            weaknesses="\n".join(f"- {s}" for s in cfg["weaknesses"]),
            switch_when=cfg["switch_when"],
            affiliate=AFFILIATE,
        )
        if "## Verdict" in text:
            text = text.replace("## Verdict", block + "\n## Verdict")
        else:
            text = text.rstrip() + "\n" + block
        path.write_text(text, encoding="utf-8")
        print("deep-dive", slug)


if __name__ == "__main__":
    main()
