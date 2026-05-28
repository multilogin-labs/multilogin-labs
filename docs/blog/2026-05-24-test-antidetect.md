# How to test antidetect quality

> 2026-05-24 · [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

Before scaling a profile farm, run every cluster through these public fingerprint tests.

## Test sites

| Site | What it catches |
|---|---|
| [BrowserLeaks](https://browserleaks.com/) | WebRTC, canvas, WebGL, fonts, timezone, language |
| [Pixelscan](https://pixelscan.net/) | Antidetect score, fingerprint coherence |
| [CreepJS](https://abrahamjuliot.github.io/creepjs/) | Deep fingerprint analysis, automation detection |
| [AmIUnique](https://amiunique.org/) | Uniqueness score against the AmIUnique database |
| [WebGL Report](https://webglreport.com/) | GPU and renderer fingerprints |

## What "good" looks like

- **Country / timezone / language consistent** with the proxy IP. Disagreement is a red flag for any platform's heuristics.
- **WebRTC public IP equals proxy IP**. Multilogin disables WebRTC leak by default — confirm.
- **Canvas hash unique per profile**, but **stable across sessions**. Random per-tab canvas is detectable.
- **GPU vendor matches OS** — a "Linux + ANGLE D3D" profile is suspicious.
- **CreepJS lies score is 0–1**, not 5+.

## Workflow

1. Start a freshly-warmed profile via [Cookbook 01](../api/cookbook/01-playwright-full-session.md).
2. Visit each test site in turn.
3. Save screenshots — [Cookbook 35 screenshot grid](../api/cookbook/35-playwright-screenshot-audit.md).
4. Track a quarterly score per cluster in `docs/benchmarks/`.

## Common Multilogin-side fixes

- Mismatch on timezone → set in profile settings to match proxy.
- Webgl renderer mismatch → toggle profile fingerprint preset.
- Font list too small → enable system fonts in profile.

[← Blog index](README.md) · [Fingerprint masking guide](../guides/multilogin-fingerprint-masking.md)
