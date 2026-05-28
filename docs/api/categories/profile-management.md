# Profile management — Create, update, delete, search

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Full lifecycle operations for browser and cloud-phone profiles.

## Endpoints in this category

- **`POST`** [Profile Create](../endpoints/profile-create.md) — `https://api.multilogin.com/profile/create`
- **`POST`** [Profile Search](../endpoints/profile-search.md) — `https://api.multilogin.com/profile/search`
- **`POST`** [Profile Remove](../endpoints/profile-remove.md) — `https://api.multilogin.com/profile/remove`
- **`POST`** [Profile Update](../endpoints/profile-update.md) — `https://api.multilogin.com/profile/update`
- **`POST`** [Profile Move](../endpoints/profile-move.md) — `https://api.multilogin.com/profile/move`
- **`POST`** [Profile Partial Update](../endpoints/profile-partial-update.md) — `https://api.multilogin.com/profile/partial_update`
- **`POST`** [Profile Restore](../endpoints/profile-restore.md) — `https://api.multilogin.com/profile/restore`
- **`POST`** [Profile Metas](../endpoints/profile-metas.md) — `https://api.multilogin.com/profile/metas`
- **`GET`** [Profile Summary](../endpoints/profile-summary.md) — `https://api.multilogin.com/profile/summary`
- **`POST`** [Profile Clone](../endpoints/profile-clone.md) — `https://api.multilogin.com/profile/clone`
- **`POST`** [Profile Convert](../endpoints/profile-convert.md) — `https://api.multilogin.com/profile/convert`
- **`GET`** [Screen Resolution](../endpoints/screen-resolution.md) — `https://api.multilogin.com/profile/screen_resolutions`

## Common use cases

- Bulk create profiles with proxy + tags from a CSV
- Update profile name/notes after each campaign
- Search by tag for daily warmup batches

## Quick example

```python
from lib.mlx_client import MLXClient
import os

c = MLXClient(token=os.environ["MULTILOGIN_TOKEN"])
profiles = c.search_profiles({"tag": "warmup", "limit": 50})
for p in profiles:
    print(p["id"], p["name"], p.get("tags"))
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Related guide](../../guides/multilogin-profile-search-tags.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin profile management api · multilogin x · create, update, delete, search
