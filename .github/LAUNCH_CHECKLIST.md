# Launch checklist

> One-shot promotion plan to push **multilogin-labs/multilogin-labs** into trending.

## Pre-launch (do once)

- [ ] **Settings → About**: paste 20 topics from [`.github/topics.md`](topics.md) + website `https://multilogin-labs.github.io/multilogin-labs/`.
- [ ] **Settings → Social preview**: upload `docs/social-preview.png` (see [og-image-spec.md](../docs/og-image-spec.md)).
- [ ] **Settings → Features**: enable Discussions, Sponsorships, Issues, Wiki off.
- [ ] **Settings → Pages**: source = GitHub Actions; verify `pages.yml` workflow ran.
- [ ] **Settings → General**: add `LICENSE` confirmation, `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CITATION.cff` are detected.
- [ ] **Settings → Sponsors**: enable + verify `FUNDING.yml` shows.
- [ ] **Org profile repo `.github` exists** (or create it) with [`.github/profile/README.md`](profile/README.md) copy.
- [ ] Tag a release: `git tag v1.0.0 && git push origin v1.0.0` — `release.yml` will publish.

## Day 0 — content

- [ ] Pin a Discussions post: "👋 Welcome — start here" linking [SEARCH_INDEX](../docs/SEARCH_INDEX.md), [API CHEATSHEET](../docs/api/CHEATSHEET.md), [Awesome](../AWESOME.md).
- [ ] Open one **good first issue**: "Add a comparison row for <vendor>" with `help wanted` + `comparison` labels.
- [ ] Record CLI demo with [`demo/cli.tape`](../demo/cli.tape) and add to README.

## Day 1 — share

| Platform | Where | Pitch (≤140 chars) |
|---|---|---|
| **Hacker News** | [Show HN form](https://news.ycombinator.com/submit) | "Show HN: Multilogin Labs — open-source antidetect docs, 90 API endpoints, 60 cookbooks, OpenAPI, CLI" |
| **Reddit /r/opensource** | new post | Same as above + screenshot of the matrix. |
| **Reddit /r/MakeMoneyOnline** | new post | Lead with the [comparison matrix](../docs/comparisons/comparison-matrix.md). |
| **Reddit /r/affiliatemarketing** | new post | Lead with [agency stack post](../docs/blog/2026-05-25-agency-stack.md). |
| **X / Twitter** | thread | Pinned tweet → repo link. Use star-history graph image. |
| **Dev.to** | mirror [open-source 90 endpoints blog](../docs/blog/2026-05-28-open-source-90-endpoints.md) | Add `#opensource #api #automation` tags. |
| **Hashnode** | same mirror | Set canonical URL to docs/blog/. |
| **Product Hunt** | optional, on a Tuesday | Lead with the calculator + Swagger UI. |
| **Indie Hackers** | "I open-sourced..." | Soft pitch, link to repo. |

## Day 2 — community seeding

- [ ] Submit to [awesome lists](https://github.com/topics/awesome) where relevant: `awesome-antidetect`, `awesome-mmo`, `awesome-multi-account`.
- [ ] Add to [github.com/topics/awesome-list](https://github.com/topics/awesome-list) discoverability via topic tag.
- [ ] Drop a non-spammy comment on related repos (only if your scripts are actually relevant).
- [ ] Reply to existing Reddit threads asking "What's the best Multilogin alternative?" with a link to the [matrix](../docs/comparisons/comparison-matrix.md).

## Week 1 — keep momentum

- [ ] Daily: triage issues, accept good PRs, post one short thread of "today I shipped...".
- [ ] Mid-week: post the [migration story](../docs/blog/2026-05-26-migrate-adspower.md) on Reddit.
- [ ] End of week: publish star-history snapshot + thank early stargazers.

## Pitfalls to avoid

- ❌ Don't open-issue spam other tools' repos.
- ❌ Don't rebrand competitor docs verbatim.
- ❌ Don't promise platform safety — the partner page already covers compliance.
- ❌ Don't bury the partner link with hidden redirects — UTM stays public.
- ❌ Don't repost the same blog body across HN / Reddit / Dev.to without rewriting the intro.

## Success metrics (90-day)

| Metric | Target |
|---|---|
| Stars | 1,000 |
| Forks | 100 |
| Discussions | 50 threads |
| Pull requests merged | 30 |
| Page views (Pages) | 50,000 |
| `npx mlx-labs` installs | 5,000 |
| Docker pulls | 1,000 |

[Sponsors](SPONSORS.md) · [Roadmap](../ROADMAP.md) · [Awesome](../AWESOME.md)
