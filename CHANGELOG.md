# Changelog

## [3.0.0] — 2026-05-24

### Added — Multilogin X API knowledge base (from official Postman export)
- **docs/api/** — 90 endpoints, 11 categories, 288 files
- Per-endpoint SEO pages + Python/Node example stubs
- [lib/mlx_client.py](../lib/mlx_client.py) — signin, start/stop, search, quick profile
- Fixed launcher scripts to official v2 start + v1 stop paths
- `MULTILOGIN_FOLDER_ID` in `.env.example`
- [tools/generate_api_docs.py](../tools/generate_api_docs.py)

### Removed
- Raw HTML export (content migrated into structured docs)

## [2.0.0] — 2026-05-24

### Added — search-first expansion
- **docs/SEARCH_INDEX.md** — 100+ keyword routes
- **docs/README.md**, **faq.md**, **glossary.md**, **troubleshooting.md**
- **13 comparisons** (+ Dolphin, Incogniton, Kameleo, VMOS, FlashID, BitBrowser, Nstbrowser, Undetectable)
- **10 new platforms** (LinkedIn, YouTube, Google Ads, Telegram, Reddit, X, WhatsApp, Discord, Snapchat, Pinterest)
- **12 new country playbooks** (US, UK, PK, NG, MX, EG, UA, PL, JP, KR, TH, CN diaspora)
- **11 use-case guides** (scraping, airdrop, dropship, SMM, traffic arb, phone farm, affiliate, tickets, crypto, ORM, warmup)
- **stop-profile** scripts (Node + Python), **proxy-check** tool

## [1.2.0] — 2026-05-24

### Added
- Python scripts: `launch_profile.py`, `playwright_connect.py`, `selenium_connect.py`
- `requirements.txt` and `lib/constants.py`
- Comparisons: Multilogin vs MoreLogin, vs DuoPlus
- Country playbooks: Philippines, Turkey, India

## [1.1.0] — 2026-05-24

### Added
- GitHub Profile README banner, stats badges, typing animation
- Navigate hub (comparisons, platforms, playbooks, tools)
- Comparisons: AdsPower, GoLogin, Octo Browser
- Platform playbooks: TikTok, Meta, Amazon
- Country playbooks: Vietnam, Brazil, Indonesia
- Plan calculator CLI (`npm run plan`)
- Selenium connect script
- ROADMAP, SECURITY, awesome-resources
- GitHub issue & PR templates

## [1.0.0] — 2026-05-24

### Added
- Multilingual README (16 languages)
- Docs, scripts, locales, LICENSE, CI workflow
