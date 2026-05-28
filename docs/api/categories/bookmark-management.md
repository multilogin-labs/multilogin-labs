# Bookmark management — Profile bookmarks

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Programmatically read and write bookmarks inside a profile.

## Endpoints in this category

- **`GET`** [Export Bookmarks](../endpoints/export-bookmarks.md) — `https://api.multilogin.com/bookmarks/export`
- **`POST`** [Import Bookmarks](../endpoints/import-bookmarks.md) — `https://api.multilogin.com/bookmarks/import`
- **`POST`** [Copy Bookmarks](../endpoints/copy-bookmarks.md) — `https://api.multilogin.com/bookmarks/copy`

## Common use cases

- Pre-seed bookmarks for new operator onboarding
- Audit bookmarks across many profiles
- Sync curated link sets to a campaign cluster

## Quick example

```bash
curl -X POST "https://api.multilogin.com/profile/$PROFILE/bookmarks" \
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"items":[{"title":"Multilogin","url":"https://multilogin.com/"}]}'
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin bookmark management api · multilogin x · profile bookmarks
