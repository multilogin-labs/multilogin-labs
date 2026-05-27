# Get All Profiles Status

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v2/profile/active
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v2/profile/active`

Get the status of all browser profiles.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v2/profile/active' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profiles": [
      {
        "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
        "is_active": true,
        "port": "55513"
      },
      {
        "profile_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
        "is_active": false
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "All profiles status retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/get-all-profiles-status.md) · [Node](../examples/node/get-all-profiles-status.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get all profiles status` · `multilogin x get all profiles status`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
