# Get All Quick Profiles Status

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v1/quick-profiles/active
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v1/quick-profiles/active`

Get the status of all quick browser profiles.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/quick-profiles/active' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "quick_profiles": [
      {
        "profile_id": "temp_12345",
        "is_active": true,
        "port": "55514"
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Quick profiles status retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/get-all-quick-profiles-status.md) · [Node](../examples/node/get-all-quick-profiles-status.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get all quick profiles status` · `multilogin x get all quick profiles status`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
