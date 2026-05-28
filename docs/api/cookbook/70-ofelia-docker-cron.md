# Cookbook 70: Use Ofelia for Docker-native cron

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

## Goal

Use Ofelia for Docker-native cron — production-ready pattern using Multilogin X API.

## Prerequisites

- Multilogin desktop running for Launcher calls
- `MULTILOGIN_TOKEN` (or automation token — recommended for cron)
- `MULTILOGIN_FOLDER_ID`, `MULTILOGIN_PROFILE_ID` in `.env`

## Steps

### 1. Search the right endpoints

```bash
npm run api:search -- ofelia docker cron
# or
npx mlx-labs search ofelia docker cron
```

### 2. Sketch (Python)

```python
import os
from lib.mlx_client import MLXClient

c = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
folder = os.environ["MULTILOGIN_FOLDER_ID"]
# Use Ofelia for Docker-native cron — implement the flow with the endpoints printed above
```

### 3. Sketch (Node)

```javascript
import { MLXClient } from "../../lib/mlx_client.mjs";

const c = new MLXClient({ token: process.env.MULTILOGIN_TOKEN });
// use ofelia for docker-native cron — wire to your scheduler / queue
```

## Production notes

- Use **automation tokens** for cron / CI to avoid daily refresh churn.
- Add **exponential backoff + jitter** (recipe 57) on every outbound call.
- Emit **structured logs** (`profile_id`, `op`, `duration_ms`) so any of recipes 52 / 68 / 79 can scoop them up.

## Related

- [Cookbook index](README.md) · [API hub](../README.md) · [Quick start](../quick-start.md)
- [Comparison matrix](../../comparisons/comparison-matrix.md)

**Keywords:** multilogin api cookbook · ofelia docker cron
