# Cloudflare Worker · Multilogin Labs search proxy

Tiny edge worker that:

- `GET /` → redirects to the GitHub Pages hub.
- `GET /go` → 302 to **partner pricing** (UTM preserved).
- `GET /search?q=playwright` → JSON of matching endpoints.
- `GET /endpoints` → cached `endpoints.json`.
- `GET /docs/<slug>` → 302 to GitHub doc page.

## Deploy

```bash
npm i -g wrangler
cd integrations/cloudflare-worker
wrangler deploy
```

Bind to a custom domain (e.g. `mlx.example.com`) in the Cloudflare dashboard.

## Use cases

- Replace `https://api.your-domain.com/search?q=...` in your tooling.
- Power Telegram / Discord bots without burning your own server.
- Vanity short URL: `https://mlx.example.com/go` → partner trial.

## Files

| File | Purpose |
|---|---|
| `wrangler.toml` | Worker config + vars |
| `src/index.js` | Single-file router |

## Related

- [npx mlx-labs CLI](../../cli/) · [Browser extension](../../extensions/browser-mlx/)
