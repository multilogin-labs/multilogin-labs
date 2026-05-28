# AGENTS.md · Multilogin Labs

> Repository memo for autonomous coding agents (Cursor, Claude Code, Aider, Codex, Copilot, Cody, …) working inside this repo.

This file follows the emerging **AGENTS.md convention** for shared agent context. If your tool reads this file, follow it; if not, copy the content into your own format.

---

## TL;DR for agents

- **Project**: Multilogin Labs hub — docs, examples, CLIs, integrations, and SEO content for the Multilogin X API.
- **Affiliate**: every "Pricing" / "Trial" / "Buy" link **must** route through `https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549`. Do **not** strip the UTM/aid/bid params.
- **Languages**: Markdown 95 %, plus Node.js (≥ 18, ESM), Python 3.10+, a tiny PHP plugin, and a Cloudflare Worker.
- **Generators**: never edit generated files by hand. Regenerate via `bash tools/upgrade_all.sh`.
- **Counts**: cookbook = **80 recipes**, API endpoints = **90**, comparisons = **20+**, locales = **EN + VI + PT-BR + ID + ES + RU + TR + FR + AR**.

## Where things live

```
docs/
  api/                    # OpenAPI, Swagger, cookbook, endpoints, categories
    endpoints.json        # SOURCE OF TRUTH for all API tooling
    cookbook/             # 80 recipes (numbered)
    categories/           # 11 enriched category pages
    endpoints/<slug>.md   # generated per-endpoint pages
  comparisons/            # 20+ vendor comparisons (long-form)
  guides/                 # SEO long-tails
  guides-vi/, -pt-br/, -id/, -es/, -ru/, -tr/, -fr/, -ar/   # locales
  blog/                   # 5 seeded posts
  index.html              # landing page on GitHub Pages
  search.html             # Lunr.js client-side search
  calculator.html         # plan calculator
tools/                    # Node + Python generators
cli/                      # `mlx-labs` Node CLI
python/                   # `mlx-labs` Python package
extensions/               # VS Code · JetBrains · Sublime · Raycast · Browser MV3
integrations/             # Cloudflare Worker · Telegram bot · Discord bot · WordPress
deploy/                   # Helm chart · Terraform
examples/                 # Runnable mini-projects
.github/                  # Issue/PR/Discussion templates, workflows
```

## Source of truth

- `docs/api/endpoints.json` — change here, not in generated `.md` files.
- `tools/upgrade_repo.py` — orchestrator; everything else is called from here or `tools/upgrade_all.sh`.
- `README.md`, `docs/changelog.md`, `docs/SEARCH_INDEX.md`, `llms.txt` — keep in sync after content changes.

## How to make a change

1. **Add an endpoint?** edit `docs/api/endpoints.json` → run `bash tools/upgrade_all.sh` → commit everything that changed.
2. **Add a guide?** drop a Markdown file under `docs/guides/` (or a locale subdir). Re-run `tools/build_search_index.mjs` and `tools/generate_sitemap.mjs`.
3. **Add a cookbook recipe?** create a new generator script (numbered) under `tools/`, mirror the style of `tools/generate_cookbook_61_80.py`. Increment the count in `docs/api/cookbook/README.md`.
4. **Add a locale?** copy `tools/generate_locale_guides_v2.py` and add a new locale block; output to `docs/guides-<locale>/`.

## Coding rules

- ESM Node; no CommonJS new modules.
- Python: type hints in new modules; no third-party deps unless already in `python/pyproject.toml`.
- No secrets in repo. Workflows use `${{ secrets.* }}`; CLIs use `MULTILOGIN_TOKEN` env var.
- Keep markdown lint clean (`markdownlint .`) and link-checked (`lychee README.md`).

## Affiliate / disclosure

This repo is a **partner / affiliate** site. Every page must:

- Surface the partner pricing URL above (or `https://github.com/multilogin-labs/multilogin-labs#trial`) at least once.
- Link `SAAS50` and `MIN50` promo codes where pricing is mentioned.
- Avoid trademark misuse — Multilogin is owned by Multilogin Software Inc.

## CI surface

| Workflow | Trigger | Purpose |
|---|---|---|
| `pages.yml` | push to main | Deploy GitHub Pages |
| `weekly-upgrade.yml` | cron weekly | Re-run generators, open PR |
| `lint-links.yml` | PR | markdownlint + link check + typos |
| `docker.yml` | tag | Build/push GHCR image |
| `release.yml` | tag | GitHub release w/ assets |
| `codeql.yml` | push/PR | Security analysis |
| `stale.yml` | cron | Close stale issues/PRs |
| `labels.yml` | push | Sync labels from `.github/labels.yml` |
| `pr-summary.yml` | PR | Sticky comment with stats |
| `star-history.yml` | cron weekly | Snapshot stars to CSV |

## Don'ts

- ❌ Don't replace `f5fad549` aid in any URL.
- ❌ Don't hand-edit `docs/api/openapi.{json,yaml}`, `docs/api/postman-*.json`, `docs/sitemap.xml`, `docs/search-index.json`.
- ❌ Don't add tracking/analytics scripts. Pages must run with **no JavaScript trackers**.
- ❌ Don't switch the project to TypeScript without a migration plan in `ROADMAP.md`.

## Useful commands

```bash
bash tools/upgrade_all.sh        # full regen
node tools/generate_sitemap.mjs  # sitemap only
node tools/build_search_index.mjs # Lunr index
node tools/generate_postman_collection.mjs
python3 tools/upgrade_repo.py    # python-only steps
npx mlx-labs search "profile start"  # quick CLI sanity
```

---

See also: `.cursor/rules/` for project-specific rules · `CONTRIBUTING.md` · `docs/architecture.md`.
