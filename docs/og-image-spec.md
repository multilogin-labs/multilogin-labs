# Social preview (Open Graph) image — spec

GitHub social previews are **1280 × 640 px**. Same image is reused on Twitter / LinkedIn cards, Slack unfurls, etc.

## Recommended layout

```
+----------------------------------------------------------+
|  [logo]  multilogin-labs                                 |
|                                                          |
|  Antidetect · Cloud Phone · MLX API                      |
|                                                          |
|  90 endpoints · 40 cookbooks · 30 countries · 16 langs   |
|                                                          |
|         multilogin.com/pricing — SAAS50 · MIN50          |
+----------------------------------------------------------+
```

## Color palette

| Use | Hex |
|---|---|
| Primary | `#0066FF` |
| Dark | `#003580` |
| Background | `#0d1117` |
| Text | `#e6edf3` |
| Accent | `#FF6D00` (promo callout) |

## Recommended fonts

- Display: **Inter Bold** or **Fira Code Bold**
- Body: **Inter Medium**

## Generators (no design skill needed)

- [og-image.vercel.app](https://og-image.vercel.app/)
- [bannerbear.com](https://www.bannerbear.com/)
- Figma — community templates "GitHub social preview 1280x640"

## How to set on GitHub

1. Save the PNG as `docs/social-preview.png`.
2. Repo → **Settings → General → Social preview → Upload**.
3. Same image is what unfurls everywhere.

## ASCII fallback (text-only OG)

For Pages-side social cards, see [`<meta property="og:*">`] tags inside [`docs/index.html`](index.html).
