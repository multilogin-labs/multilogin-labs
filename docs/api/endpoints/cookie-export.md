# Cookie Export

`POST` · [Launcher](../categories/launcher.md)

```http
POST https://launcher.mlx.yt:45001/api/v1/cookies/export
```

## Description

**POST** `https://launcher.mlx.yt:45001/api/v1/cookies/export`

Export cookies from a profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
}
```

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/cookies/export' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "cookies": [
      {
        "domain": ".example.com",
        "name": "session",
        "value": "abc123",
        "path": "/",
        "httpOnly": true,
        "secure": true,
        "expirationDate": 1735689600
      }
    ],
    "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Cookies exported successfully"
  }
}
```

## Code

- [Python example](../examples/python/cookie-export.md) · [Node](../examples/node/cookie-export.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api cookie export` · `multilogin x cookie export`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
