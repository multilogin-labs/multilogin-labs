# Verify 2FA

`POST` · [2FA](../categories/2fa.md)

```http
POST https://api.multilogin.com/2fa/verify
```

## Description

**POST** `https://api.multilogin.com/2fa/verify`

Verify 2FA code during login.

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "email": "user@example.com",
  "temp_token": "temp_token_from_login",
  "code": "123456"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/2fa/verify' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "email": "user@example.com",
  "temp_token": "temp_token_from_login",
  "code": "123456"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "2FA verified successfully"
  }
}
```

## Code

- [Python example](../examples/python/verify-2fa.md) · [Node](../examples/node/verify-2fa.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api verify 2fa` · `multilogin x verify 2fa`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
