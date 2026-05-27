# User Revoke Token

`POST` · [Profile Access Management](../categories/profile-access-management.md)

```http
POST https://api.multilogin.com/user/revoke_token
```

## Description

**POST** `https://api.multilogin.com/user/revoke_token`

Revoke an authentication token.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/user/revoke_token' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}'
```

## Example response

(200 OK):
```json
{
  "data": {},
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Token revoked successfully"
  }
}
```

## Code

- [Python example](../examples/python/user-revoke-token.md) · [Node](../examples/node/user-revoke-token.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api user revoke token` · `multilogin x user revoke token`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
