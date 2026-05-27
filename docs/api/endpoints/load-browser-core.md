# Load Browser Core

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v1/core/load
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v1/core/load`

Load a specific browser core.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `browser_type`: string (Required)
- `version`: number (Required)

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/core/load?browser_type=mimic&version=132' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "browser_type": "mimic",
    "version": 132,
    "loaded": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Core loaded successfully"
  }
}
```

## Code

- [Python example](../examples/python/load-browser-core.md) · [Node](../examples/node/load-browser-core.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api load browser core` · `multilogin x load browser core`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
