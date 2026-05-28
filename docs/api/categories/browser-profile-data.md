# Browser profile data — Cookies, history, storage

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Read and write low-level browser data inside a profile.

## Endpoints in this category

- **`GET`** [Unlock Locked Profiles](../endpoints/unlock-locked-profiles.md) — `https://api.multilogin.com/profile/unlock`

## Common use cases

- Audit cookies for compliance after a campaign
- Pre-load localStorage with feature flags
- Clear specific data without nuking the whole profile

## Quick example

```bash
curl "https://api.multilogin.com/profile/$PROFILE/cookies" \
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" 
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Related guide](../cookbook/10-export-cookies.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin browser profile data api · multilogin x · cookies, history, storage
