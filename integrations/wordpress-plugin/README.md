# mlx-wordpress · partner banner shortcode

WordPress plugin that adds a `[mlx_partner]` shortcode rendering an inline CTA card with the **Multilogin partner UTM** and `SAAS50` / `MIN50` promo codes.

## Install (manual zip)

1. Zip the `wordpress-plugin/` folder.
2. WP Admin → Plugins → Add New → Upload Plugin.
3. Activate.
4. Insert `[mlx_partner]` in any post / page / Gutenberg shortcode block.

## Shortcode options

```
[mlx_partner label="Try Multilogin" theme="dark"]
```

| Option | Default | Notes |
|---|---|---|
| `label` | `Start $2 trial · SAAS50` | Button text |
| `theme` | `light` | `light` or `dark` |

## Why use a plugin instead of a raw link

- Always the canonical partner UTM — no copy-paste typos.
- Renders consistent styling across themes.
- One place to update if the deal changes.

PR welcome to ship to wordpress.org.
