# Get Version

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v1/version
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v1/version`

Get the version of the launcher.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/version' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "version": "1.9.0"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Version retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/get-version.md) · [Node](../examples/node/get-version.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get version` · `multilogin x get version`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
