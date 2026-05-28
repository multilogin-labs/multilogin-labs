# Pre-made cookies — Session bootstrap

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Inject cookies into a profile before first login. Useful for migrations.

## Endpoints in this category

- **`GET`** [Target Website List](../endpoints/target-website-list.md) — `https://api.multilogin.com/cookies/websites`
- **`POST`** [Create Cookies Metadata](../endpoints/create-cookies-metadata.md) — `https://api.multilogin.com/cookies/metadata/create`
- **`GET`** [Cookies List](../endpoints/cookies-list.md) — `https://api.multilogin.com/cookies/list`
- **`PUT`** [Update Cookies Metadata](../endpoints/update-cookies-metadata.md) — `https://api.multilogin.com/cookies/metadata/update`

## Common use cases

- Restore session from a different antidetect tool
- Hand off warmed account to a different operator
- Recover from accidental cookie wipe

## Quick example

```python
import os, json
from lib.mlx_client import MLXClient

c = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
cookies = json.loads(open("cookies.json").read())
c.import_cookies(os.environ["MULTILOGIN_PROFILE_ID"], cookies)
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Related guide](../cookbook/09-import-cookies.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin pre made cookies api · multilogin x · session bootstrap
