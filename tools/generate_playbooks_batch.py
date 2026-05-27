#!/usr/bin/env python3
"""Generate country playbook markdown."""
from pathlib import Path

AFFILIATE = (
    "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner"
    "&a_aid=saas&a_bid=f5fad549"
)

COUNTRIES = [
    ("germany", "Germany", "DE", "EUR", "Amazon DE, eBay Kleinanzeigen, Meta Ads EU"),
    ("france", "France", "FR", "EUR", "Amazon FR, Cdiscount, TikTok FR"),
    ("spain", "Spain", "ES", "EUR", "Amazon ES, Wallapop, Instagram ES"),
    ("italy", "Italy", "IT", "EUR", "Amazon IT, Subito, TikTok IT"),
    ("canada", "Canada", "CA", "CAD", "Amazon CA, Shopify, Meta Ads NA"),
    ("australia", "Australia", "AU", "AUD", "Amazon AU, eBay AU, TikTok AU"),
    ("malaysia", "Malaysia", "MY", "MYR", "Shopee MY, Lazada, TikTok Shop"),
    ("singapore", "Singapore", "SG", "SGD", "Shopee SG, crypto, B2B SaaS"),
    ("taiwan", "Taiwan", "TW", "TWD", "Shopee TW, PChome, LINE marketing"),
    ("saudi-arabia", "Saudi Arabia", "SA", "SAR", "Noon, Amazon SA, Snapchat"),
    ("argentina", "Argentina", "AR", "ARS", "Mercado Libre, Meta LATAM"),
    ("colombia", "Colombia", "CO", "COP", "Mercado Libre CO, WhatsApp commerce"),
]

TEMPLATE = """# {name} MMO playbook ({code})

> [Multilogin partner pricing →]({affiliate}) · **`SAAS50`** · **`MIN50`**

## Market overview

Operators in **{name}** use Multilogin for multi-account social, e-commerce, and ads. Currency: **{currency}**. Popular stacks: {platforms}.

## Recommended setup

| Item | Recommendation |
|---|---|
| Proxy | Residential or mobile in **{code}** |
| Device | Cloud phone for TikTok/Shopee apps; Mimic for web |
| Plan | Pro 50+ for proxy GB + mobile minutes |
| Language | Match OS locale to target platform |

## Workflow

1. Create folder `{code_lower}-clients` in workspace.
2. One profile per account — tag `geo-{code_lower}`.
3. Warm 3–7 days before ads or seller actions.
4. Use [API quick start](../api/quick-start.md) for batch launch.

## Platforms

- [TikTok](../platforms/tiktok.md) · [Amazon](../platforms/amazon.md) · [Meta](../platforms/facebook.md)
- [Guides](../guides/README.md) · [SEARCH_INDEX](../SEARCH_INDEX.md)

## Compliance

Follow local laws and each platform's Terms of Service. This guide is operational, not legal advice.

**[→ Start $2 trial]({affiliate})**
"""


def main():
    out = Path(__file__).resolve().parents[1] / "docs" / "playbooks"
    new = []
    for slug, name, code, currency, platforms in COUNTRIES:
        path = out / f"{slug}.md"
        if path.exists():
            continue
        path.write_text(
            TEMPLATE.format(
                name=name,
                code=code,
                code_lower=code.lower(),
                currency=currency,
                platforms=platforms,
                affiliate=AFFILIATE,
            ),
            encoding="utf-8",
        )
        new.append((name, slug))
        print("created", slug)

    readme = out / "README.md"
    if readme.exists() and new:
        t = readme.read_text(encoding="utf-8")
        for name, slug in new:
            row = f"| [{name}]({slug}.md) | {name} |"
            if slug not in t:
                t += f"\n{row}"
        readme.write_text(t, encoding="utf-8")
    print(f"done: {len(new)} playbooks")


if __name__ == "__main__":
    main()
