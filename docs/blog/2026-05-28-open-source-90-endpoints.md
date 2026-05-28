# Why we open-sourced 90 Multilogin endpoints

> 2026-05-28 · [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`**

Multilogin Labs publishes a community-maintained, machine-readable inventory of the **Multilogin X API**: 90 endpoints, an [OpenAPI 3.0 spec](../api/openapi.json), an [interactive Swagger UI](../api/swagger.html), 60 cookbook recipes, and Python + Node clients.

## Why open-source it

1. **Onboarding speed** — agencies hire and rotate operators every month. A single search box (`npm run api:search`) replaces 20 minutes of manual hunting.
2. **Tool comparisons** — when a team asks "should we leave AdsPower?", the answer rarely fits in a tweet. We turned that question into [16 detailed comparison pages](../comparisons/comparison-matrix.md) with real migration plans.
3. **Country playbooks** — TikTok in Vietnam ≠ TikTok in Brazil ≠ TikTok in Saudi Arabia. We documented [30 markets](../playbooks/README.md).
4. **Affiliate trust** — every page links the **same** partner URL with the **same** UTM. No bait-and-switch. No hidden vendors.

## What's inside

- 500+ markdown pages, all greppable, all in one repo.
- A [Lunr.js full-text search](../search.html) that indexes the whole hub.
- An [npx `mlx-labs` CLI](../../cli/) and a [`pip install mlx-labs`](../../python/) — the same surface from terminal, IDE, or browser bookmarklet.
- A Docker image at `ghcr.io/multilogin-labs/multilogin-labs` so CI can spin up the toolset in seconds.

## Where it goes next

- More locales (we already ship VI / PT-BR / ID / ES / RU / TR / FR / AR).
- Public benchmark CSVs measured by community runs.
- IDE extensions: VS Code, JetBrains, Sublime, Raycast.

If your team builds on Multilogin, [PRs welcome](../../CONTRIBUTING.md).

[← Blog index](README.md) · [Changelog](../changelog.md) · [Twitter / X share](https://x.com/intent/tweet?text=Multilogin+Labs+open-sourced+90+API+endpoints+%2B+OpenAPI+spec&url=https%3A%2F%2Fgithub.com%2Fmultilogin-labs%2Fmultilogin-labs)
