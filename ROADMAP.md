# Roadmap

## Shipped (v3 enrichment)

- [x] **All 90 endpoint pages** enriched with curl + JSON from official API reference
- [x] API [quick-start](docs/api/quick-start.md) + [cookbook](docs/api/cookbook/) (8 recipes)
- [x] Node [mlx_client.mjs](lib/mlx_client.mjs)
- [x] [tools/enrich_endpoints.py](tools/enrich_endpoints.py) for regeneration
- [x] GitHub Pages workflow (docs mirror)

## Shipped (v2 content explosion)

- [x] **SEARCH_INDEX** — 100+ keywords mapped to guides
- [x] **13 comparisons** — AdsPower through Undetectable
- [x] **13 platform playbooks** — TikTok through Pinterest
- [x] **18 country playbooks** — global MMO markets
- [x] **11 use-case guides** — scraping, airdrop, agency, etc.
- [x] FAQ · Glossary · Troubleshooting · Docs hub
- [x] Python + Node scripts (launch, stop, connect)
- [x] Plan calculator · Proxy check tool
- [x] 16-language README + 15 locale files

## Next

- [ ] GitHub Pages site mirror
- [ ] Warmup scheduler CLI
- [ ] MoreLogin deep-dive (long-form)
- [ ] Video embed section
- [ ] GitHub Discussions FAQ

**Partner:** [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
## Shipped (v4 — mega enrichment)

- [x] **55+ guides**, **30 cookbooks**, **30 country playbooks**
- [x] **16 comparisons** + [comparison matrix](docs/comparisons/comparison-matrix.md)
- [x] **Learning paths** — [docs/learn/](docs/learn/)
- [x] **llms.txt** + **robots.txt** + **API cheatsheet**
- [x] Platform enrich (API blocks) + Instagram, Shopee, Binance
- [x] `tools/upgrade_repo.py` — one-command regeneration
- [x] GitHub Pages `docs/index.html` + sitemap (450+ URLs)

## Shipped (v5 — auto-development sweep)

- [x] **OpenAPI 3.0** spec from 90 endpoints + **Swagger UI**
- [x] **Interactive calculator** — [docs/calculator.html](docs/calculator.html)
- [x] **Warmup scheduler** CLI — `npm run warmup`
- [x] **Weekly auto-upgrade** GitHub Action + lint-links workflow
- [x] **Long-form deep-dive** for AdsPower, GoLogin, Octo, Dolphin
- [x] **12 Vietnamese guides** in [docs/guides/vi/](docs/guides/vi/)
- [x] **Benchmarks page**, **RSS feed**, **changelog**
- [x] README badges + **star history** + GitHub stats

## Shipped (v6 — "be the most-starred repo" pass)

- [x] **AWESOME.md** — antidetect ecosystem star magnet
- [x] **CLI**: `npx mlx-labs` ([cli/](cli/)) + Python `mlx-labs` ([python/](python/))
- [x] **Docker**: [Dockerfile](Dockerfile), [compose](docker-compose.yml), GHCR workflow
- [x] **Architecture diagrams**: [docs/architecture.md](docs/architecture.md) (Mermaid)
- [x] **Org profile** README at [.github/profile/README.md](.github/profile/README.md)
- [x] **Discussions templates** + comparison/playbook issue templates
- [x] **CITATION.cff**, **CODE_OF_CONDUCT**, **FUNDING**, **CODEOWNERS**, **SUPPORT**, **SPONSORS**
- [x] **Workflows**: docker, release, codeql, stale, labels, lint-links + typos
- [x] **README** stargazers wall, contributors graph, used-by table, three-up TL;DR
- [x] **OG / SEO** metadata in `docs/index.html`, social preview spec
- [x] **`.github/topics.md`** — 20 GitHub topics for discovery

## Shipped (v7 — discoverability + tooling)

- [x] **Full-text Lunr.js search** at [docs/search.html](docs/search.html) — 500+ pages
- [x] **Cookbook 41–60** — 60 total recipes
- [x] **All 11 API category pages** enriched (overview, examples, use cases)
- [x] **Locale guides** PT-BR / ID / ES — 30 new pages in [docs/guides/](docs/guides/)
- [x] **VS Code extension** scaffold — [extensions/vscode-mlx-search/](extensions/vscode-mlx-search/)
- [x] **Browser bookmarklets** — [tools/bookmarklet.html](tools/bookmarklet.html)
- [x] **Postman environment** generator — [docs/api/postman-environment.json](docs/api/postman-environment.json)
- [x] **`examples/`** — 4 runnable mini projects (Playwright, CSV, cron, Discord)
- [x] **VHS tape** for animated CLI demo — [demo/cli.tape](demo/cli.tape)
- [x] **Dependabot** + **PR summary auto-comment** workflows

## Shipped (v8 — global launch)

- [x] **Locale guides** RU + TR + FR + AR — 40 new pages
- [x] **Benchmark runner** `npm run bench` + public CSV at `docs/benchmarks/`
- [x] **Videos page** — [docs/videos.md](docs/videos.md)
- [x] **Editor extensions**: VS Code (live), JetBrains scaffold, Raycast scaffold, Sublime scaffold
- [x] **Algolia DocSearch** application JSON + **Giscus** config + giscus.html
- [x] **Blog** with 5 launch posts at [docs/blog/](docs/blog/)
- [x] **Launch checklist** [.github/LAUNCH_CHECKLIST.md](.github/LAUNCH_CHECKLIST.md)
- [x] **Helm chart + Terraform** templates in [deploy/](deploy/)
- [x] **Showcase**, **Newsletter**, **Discussions seed**, weekly **star-history snapshot** workflow

## Shipped (v9 — agents, edges, integrations)

- [x] **Cookbook 61–80** — 80 recipes total (k6, OpenTelemetry, Vercel cron, n8n, Make, Zapier, Supabase, Airtable, Notion, Sentry, Datadog, Go/Rust snippets, GH Actions cron…)
- [x] **Cloudflare Worker** template — search proxy + partner redirect ([integrations/cloudflare-worker/](integrations/cloudflare-worker/))
- [x] **Telegram bot** ([integrations/telegram-bot/](integrations/telegram-bot/)) + **Discord bot** ([integrations/discord-bot/](integrations/discord-bot/))
- [x] **Browser MV3 extension** Chrome / Firefox — [extensions/browser-mlx/](extensions/browser-mlx/)
- [x] **WordPress plugin** with `[mlx_partner]` shortcode
- [x] **Full Postman v2.1 collection** ([docs/api/postman-collection.json](docs/api/postman-collection.json))
- [x] **AGENTS.md** + `.cursor/rules/repo.mdc` for autonomous coding agents
- [x] **Press kit** — [press-kit/](press-kit/) (logo SVG, 1200 × 630 banner, palette, boilerplate)
- [x] **Social preview SVG** — [docs/social-preview.svg](docs/social-preview.svg)
- [x] **AdsPower → Multilogin migration tool** ([tools/migrate-adspower.mjs](tools/migrate-adspower.mjs))
- [x] Total Markdown count → **625**, sitemap → **624**

## Next (v10 ideas)

- [ ] First 5 community CSVs in `docs/benchmarks/`
- [ ] Real CLI `cli.gif` recorded with VHS
- [ ] Algolia DocSearch application submitted
- [ ] Cookbook locales (RU / TR / VI translations of top 20 recipes)
- [ ] Shopify embedded app scaffold
- [ ] Self-hostable status page for Multilogin services
- [ ] Migration tool for GoLogin / Octo Browser
- [ ] AI agent demo notebook (LangGraph / CrewAI driving Multilogin)

