# Cookbook 30: Restart loop for long jobs

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

## Goal

Automate: restart loop for long jobs.

## Prerequisites

- Multilogin desktop running (for Launcher calls)
- `MULTILOGIN_EMAIL`, `MULTILOGIN_PASSWORD` or automation token
- `MULTILOGIN_FOLDER_ID`, `MULTILOGIN_PROFILE_ID` in `.env`

## Steps

### 1. Authenticate

```bash
# Python
python scripts/python/signin.py
export MULTILOGIN_TOKEN=$(python -c "import os; print(os.environ.get('MULTILOGIN_TOKEN',''))")
```

Or use automation token — see [05-automation-token-setup](05-automation-token-setup.md).

### 2. API call

See [endpoints index](../endpoints-index.md) and search:

```bash
npm run api:search -- restart profile cron
```

### 3. Example (Python)

```python
from lib.mlx_client import MLXClient
import os

client = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
# Implement: see endpoint page for exact method/path
```

### 4. Example (Node)

```javascript
import { MLXClient } from "../../lib/mlx_client.mjs";
const client = new MLXClient({ token: process.env.MULTILOGIN_TOKEN });
```

## Related endpoints

Search [SEARCH_KEYWORDS.md](../SEARCH_KEYWORDS.md) for: `restart profile cron`.

## Next

- [Cookbook index](README.md)
- [Quick start](../quick-start.md)

**Keywords:** multilogin api cookbook · restart profile cron
