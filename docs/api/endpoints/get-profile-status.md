# Get Profile Status

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v1/profile/active
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v1/profile/active`

Get the status of a specific browser profile.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `profile_id`: uuid (Required)

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/profile/active?profile_id=81b5627a-1212-4016-9467-3dbe4d6f78eb' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
    "is_active": true,
    "port": "55513"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile status retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/get-profile-status.md) · [Node](../examples/node/get-profile-status.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get profile status` · `multilogin x get profile status`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
