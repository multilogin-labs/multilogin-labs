# mlx-search · VS Code extension scaffold

Search 90 Multilogin X API endpoints from the VS Code command palette.

## Status

**Scaffold** — install dependencies and `npx vsce package` to build a `.vsix`. PRs welcome.

## Dev

```bash
cd extensions/vscode-mlx-search
npm install
npx --yes @vscode/test-electron --version    # sanity
code --install-extension mlx-search-*.vsix
```

## Manifest highlights

```jsonc
// package.json
{
  "name": "mlx-search",
  "displayName": "Multilogin X API search",
  "version": "0.1.0",
  "engines": { "vscode": "^1.85.0" },
  "main": "./extension.js",
  "contributes": {
    "commands": [
      { "command": "mlx.search", "title": "Multilogin: Search 90 API endpoints" }
    ]
  }
}
```

See [extension.js](extension.js) for the implementation.
