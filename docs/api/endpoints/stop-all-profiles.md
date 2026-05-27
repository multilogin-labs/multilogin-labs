# Stop All Profiles

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v1/profile/stop_all
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v1/profile/stop_all`

Stop all running browser profiles.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/profile/stop_all' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "stopped_profiles": [
      "81b5627a-1212-4016-9467-3dbe4d6f78eb",
      "92c6738b-2323-5127-9578-4ecf5e7f89fc"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "All profiles stopped successfully"
  }
}
```

## Code

- [Python example](../examples/python/stop-all-profiles.md) · [Node](../examples/node/stop-all-profiles.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api stop all profiles` · `multilogin x stop all profiles`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
