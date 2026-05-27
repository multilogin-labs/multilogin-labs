# Browser Core List

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v1/core/list
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v1/core/list`

Get list of available browser cores.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/core/list' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "cores": [
      {
        "browser_type": "mimic",
        "version": 132,
        "is_available": true
      },
      {
        "browser_type": "stealthfox",
        "version": 130,
        "is_available": true
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Core list retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/browser-core-list.md) · [Node](../examples/node/browser-core-list.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api browser core list` · `multilogin x browser core list`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
