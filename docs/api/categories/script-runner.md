# Script runner — Server-side automation

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Run JavaScript snippets inside a profile from the API. Great for headless flows.

## Endpoints in this category

- **`GET`** [Start Browser Profile with Selenium](../endpoints/start-browser-profile-with-selenium.md) — `https://launcher.mlx.yt:45001/api/v2/profile/f/:folder_id/p/:profile_id/start?automation_type=selenium&script_file=script.py`
- **`POST`** [Start Script Runner](../endpoints/start-script-runner.md) — `https://api.multilogin.com/script/start`
- **`POST`** [Stop Script Runner](../endpoints/stop-script-runner.md) — `https://api.multilogin.com/script/stop`
- **`GET`** [Script List](../endpoints/script-list.md) — `https://api.multilogin.com/script/list`

## Common use cases

- Run a quick scrape without a full Playwright stack
- Pre-action diagnostics inside the profile
- Self-healing: detect captcha and stop session

## Quick example

```bash
curl -X POST https://api.multilogin.com/scripts/run \
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"profile_id":"...","script":"return document.title"}'
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Related guide](../cookbook/14-script-runner.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin script runner api · multilogin x · server-side automation
