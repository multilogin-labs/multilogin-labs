# browser-mlx · Chrome / Firefox extension

A 340 px popup that searches the **90 Multilogin X API endpoints** and one-click opens Swagger / plan calculator / partner pricing.

## Install (unpacked)

### Chrome / Edge / Brave

1. `chrome://extensions/` → enable **Developer mode**.
2. **Load unpacked** → choose `extensions/browser-mlx/`.

### Firefox

1. `about:debugging#/runtime/this-firefox`.
2. **Load Temporary Add-on…** → pick `extensions/browser-mlx/manifest.json`.

## Files

| File | Purpose |
|---|---|
| `manifest.json` | MV3 manifest (Chrome + Firefox) |
| `popup.html` | UI (340 px) |
| `popup.js` | Fetches `docs/api/endpoints.json`, caches 24 h, fuzzy filter |

## Roadmap

- [ ] Real `icon-*.png` assets (currently referenced; ship with PR).
- [ ] Context menu: select text → search Multilogin endpoints.
- [ ] Sync caches across browser.

## Related

- [VS Code](../vscode-mlx-search/) · [JetBrains](../jetbrains-mlx/) · [Sublime](../sublime-mlx/) · [Raycast](../raycast-mlx/)
- [CLI `npx mlx-labs`](../../cli/) · [Bookmarklets](../../tools/bookmarklet.html)
