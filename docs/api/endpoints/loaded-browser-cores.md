# Loaded Browser Cores

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v1/core/loaded
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v1/core/loaded`

Get information about loaded browser cores.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/core/loaded' \
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
        "is_loaded": true
      },
      {
        "browser_type": "stealthfox",
        "version": 130,
        "is_loaded": true
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Loaded cores retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/loaded-browser-cores.md) · [Node](../examples/node/loaded-browser-cores.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api loaded browser cores` · `multilogin x loaded browser cores`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
