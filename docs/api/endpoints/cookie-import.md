# Cookie Import

`POST` · [Launcher](../categories/launcher.md)

```http
POST https://launcher.mlx.yt:45001/api/v1/cookies/import
```

## Description

**POST** `https://launcher.mlx.yt:45001/api/v1/cookies/import`

Import cookies into a profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "cookies": [
    {
      "domain": ".example.com",
      "name": "session",
      "value": "abc123",
      "path": "/",
      "httpOnly": true,
      "secure": true
    }
  ]
}
```

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/cookies/import' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "cookies": [
    {
      "domain": ".example.com",
      "name": "session",
      "value": "abc123",
      "path": "/",
      "httpOnly": true,
      "secure": true
    }
  ]
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "imported": 1,
    "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Cookies imported successfully"
  }
}
```

## Code

- [Python example](../examples/python/cookie-import.md) · [Node](../examples/node/cookie-import.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api cookie import` · `multilogin x cookie import`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
