# mlx-labs · community CLI

Tiny CLI wrapping the most useful tools from [`multilogin-labs/multilogin-labs`](https://github.com/multilogin-labs/multilogin-labs).

## Install

```bash
# zero-install via npx (after npm publish)
npx mlx-labs <command>

# or local
git clone https://github.com/multilogin-labs/multilogin-labs.git
cd multilogin-labs/cli && npm link
mlx-labs help
```

## Commands

| Command | Description |
|---|---|
| `help` | Print all commands |
| `version` | Print CLI version |
| `search <terms>` | Search 90 Multilogin API endpoints |
| `endpoints` | Dump the entire endpoints JSON |
| `cheatsheet` | Print one-page API cheatsheet |
| `plan -- --profiles 50 --team 3 --mobile` | Recommend a plan |
| `warmup --profiles A,B,C --folder UUID` | Run warmup scheduler |
| `guides` · `cookbook` | List repo guides / cookbook |
| `links` | Print partner pricing + codes |
| `upgrade` | Regenerate everything (maintainers) |

## Partner pricing

[multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`

MIT.
