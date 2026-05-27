# Enable 2FA

`POST` · [2FA](../categories/2fa.md)

```http
POST https://api.multilogin.com/2fa/enable
```

## Description

**POST** `https://api.multilogin.com/2fa/enable`

Enable 2FA after setup verification.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "verification_code": "123456"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/2fa/enable' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "verification_code": "123456"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "2fa_enabled": true,
    "enabled_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "2FA enabled successfully"
  }
}
```

## Code

- [Python example](../examples/python/enable-2fa.md) · [Node](../examples/node/enable-2fa.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api enable 2fa` · `multilogin x enable 2fa`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
