# Proxy — Built-in residential & mobile

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · **`SAAS50`** · **`MIN50`** · [← API hub](../README.md) · [Cheatsheet](../CHEATSHEET.md) · [Swagger UI](../swagger.html)

Generate Multilogin-managed proxy credentials and assign them to profiles.

## Endpoints in this category

- **`POST`** [Generate Proxy](../endpoints/generate-proxy.md) — `https://api.multilogin.com/proxy/generate`
- **`GET`** [Fetch Proxy Data](../endpoints/fetch-proxy-data.md) — `https://api.multilogin.com/proxy/data`

## Common use cases

- Auto-assign country-matched proxy on profile create
- Refresh sticky session before warmup wave
- Rotate exit IPs between sessions

## Quick example

```bash
# Generate residential proxy in Vietnam
curl -X POST https://api.multilogin.com/proxy/generate \
  -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"country":"vn","type":"residential","sticky_seconds":1800}'
```

## Related

- [Cookbook ×40](../cookbook/README.md)
- [Related guide](../cookbook/13-generate-multilogin-proxy.md)
- [Quick start](../quick-start.md) · [Authentication](../authentication.md)
- [SEARCH_INDEX](../../SEARCH_INDEX.md)

**Keywords:** multilogin proxy api · multilogin x · built-in residential & mobile
