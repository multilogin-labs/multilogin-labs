# Cookbook 58: Rotate 2FA backup codes

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

## Goal

Rotate 2FA backup codes — production-ready pattern using Multilogin X API.

## Prerequisites

- Multilogin desktop running for Launcher calls
- `MULTILOGIN_TOKEN` (or automation token — recommended for cron)
- `MULTILOGIN_FOLDER_ID`, `MULTILOGIN_PROFILE_ID` in `.env`

## Steps

### 1. Search the right endpoints

```bash
npm run api:search -- 2fa backup rotate
# or
npx mlx-labs search 2fa backup rotate
```

### 2. Python sketch

```python
import os
from lib.mlx_client import MLXClient

c = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
folder = os.environ["MULTILOGIN_FOLDER_ID"]
# Implement the flow using the endpoints printed above
```

### 3. Node sketch

```javascript
import { MLXClient } from "../../lib/mlx_client.mjs";

const c = new MLXClient({ token: process.env.MULTILOGIN_TOKEN });
// Implement: rotate 2fa backup codes
```

## Production notes

- Add **retry with exponential backoff** for 429 — see [recipe 57](57-ratelimit-backoff.md).
- Use **automation token** for long-running scripts ([guide](../../guides/multilogin-automation-token.md)).
- Log timing per step — feed into [recipe 52](52-metrics-prometheus-exporter.md).

## Related

- [Cookbook index](README.md) · [API hub](../README.md) · [Quick start](../quick-start.md)
- [Comparison matrix](../../comparisons/comparison-matrix.md)

**Keywords:** multilogin api cookbook · 2fa backup rotate
