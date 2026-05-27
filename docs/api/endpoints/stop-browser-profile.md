# Stop Browser Profile

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v1/profile/stop
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v1/profile/stop`

Stop a browser profile by profile ID.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `profile_id`: uuid (Required)

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/profile/stop?profile_id=81b5627a-1212-4016-9467-3dbe4d6f78eb' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile stopped successfully"
  }
}
```

## Code

- [Python example](../examples/python/stop-browser-profile.md) · [Node](../examples/node/stop-browser-profile.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api stop browser profile` · `multilogin x stop browser profile`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
