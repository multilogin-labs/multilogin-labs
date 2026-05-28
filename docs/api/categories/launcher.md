# Launcher — Local profile control

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Start, stop, and monitor profiles on the local Multilogin desktop. Required for Playwright/Puppeteer/Selenium.

## Endpoints in this category

- **`GET`** [Start Browser Profile](../endpoints/start-browser-profile.md) — `https://launcher.mlx.yt:45001/api/v2/profile/f/:folder_id/p/:profile_id/start`
- **`POST`** [Start Quick Profile v3](../endpoints/start-quick-profile-v3.md) — `https://launcher.mlx.yt:45001/api/v3/profile/quick`
- **`POST`** [Start Quick Profile (Deprecated)](../endpoints/start-quick-profile-deprecated.md) — `https://launcher.mlx.yt:45001/api/v2/profile/quick`
- **`GET`** [Stop Browser Profile](../endpoints/stop-browser-profile.md) — `https://launcher.mlx.yt:45001/api/v1/profile/stop`
- **`GET`** [Stop All Profiles](../endpoints/stop-all-profiles.md) — `https://launcher.mlx.yt:45001/api/v1/profile/stop_all`
- **`GET`** [Get Version](../endpoints/get-version.md) — `https://launcher.mlx.yt:45001/api/v1/version`
- **`GET`** [Get Profile Status](../endpoints/get-profile-status.md) — `https://launcher.mlx.yt:45001/api/v1/profile/active`
- **`GET`** [Get All Profiles Status](../endpoints/get-all-profiles-status.md) — `https://launcher.mlx.yt:45001/api/v2/profile/active`
- **`GET`** [Get All Quick Profiles Status](../endpoints/get-all-quick-profiles-status.md) — `https://launcher.mlx.yt:45001/api/v1/quick-profiles/active`
- **`GET`** [Loaded Browser Cores](../endpoints/loaded-browser-cores.md) — `https://launcher.mlx.yt:45001/api/v1/core/loaded`
- **`GET`** [Browser Core List](../endpoints/browser-core-list.md) — `https://launcher.mlx.yt:45001/api/v1/core/list`
- **`GET`** [Load Browser Core](../endpoints/load-browser-core.md) — `https://launcher.mlx.yt:45001/api/v1/core/load`
- **`DELETE`** [Delete Browser Core](../endpoints/delete-browser-core.md) — `https://launcher.mlx.yt:45001/api/v1/core`
- **`POST`** [Validate Proxy](../endpoints/validate-proxy.md) — `https://launcher.mlx.yt:45001/api/v1/proxy/validate`
- **`POST`** [Cookie Import](../endpoints/cookie-import.md) — `https://launcher.mlx.yt:45001/api/v1/cookies/import`
- **`POST`** [Cookie Export](../endpoints/cookie-export.md) — `https://launcher.mlx.yt:45001/api/v1/cookies/export`
- **`POST`** [Convert QBP to Profile](../endpoints/convert-qbp-to-profile.md) — `https://launcher.mlx.yt:45001/api/v1/profile/convert_qbp`
- **`GET`** [Get QBP Status](../endpoints/get-qbp-status.md) — `https://launcher.mlx.yt:45001/api/v1/profile/qbp_status`

## Common use cases

- Open a profile and connect Playwright to its CDP port
- Launch quick profiles on demand for scraping
- Stop all profiles for emergency / shift change

## Quick example

```bash
# Start profile in playwright mode
curl "https://launcher.mlx.yt:45001/api/v2/profile/f/$FOLDER/p/$PROFILE/start?automation_type=playwright" \
  -H "Authorization: Bearer $MULTILOGIN_TOKEN"

# Stop profile
curl "https://launcher.mlx.yt:45001/api/v1/profile/stop?profile_id=$PROFILE" \
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" 
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Related guide](../../guides/multilogin-api-playwright.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin launcher api · multilogin x · local profile control
