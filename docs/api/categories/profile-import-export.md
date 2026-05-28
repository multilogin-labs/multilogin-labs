# Profile import / export — Migration

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Move profiles between workspaces, back up cookies, and migrate from other antidetect tools.

## Endpoints in this category

_(see API hub)_

## Common use cases

- Migrate from AdsPower/GoLogin to Multilogin
- Backup before bulk delete
- Move profiles between client workspaces

## Quick example

```python
from lib.mlx_client import MLXClient
import json, os

c = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
# Export single profile
data = c.export_profile(os.environ["MULTILOGIN_PROFILE_ID"])
open("profile_backup.json", "w").write(json.dumps(data, indent=2))
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Related guide](../cookbook/12-profile-export-migrate.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin profile import export api · multilogin x · migration
