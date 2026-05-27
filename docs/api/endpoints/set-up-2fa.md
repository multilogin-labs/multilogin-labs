# Set up 2FA

`POST` · [2FA](../categories/2fa.md)

```http
POST https://api.multilogin.com/2fa/setup
```

## Description

**POST** `https://api.multilogin.com/2fa/setup`

Initialize 2FA setup for the account.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "method": "authenticator"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/2fa/setup' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "method": "authenticator"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "qr_code": "data:image/png;base64,iVBORw0KGgoAAAANS...",
    "secret": "JBSWY3DPEHPK3PXP",
    "backup_codes": [
      "12345678",
      "87654321",
      "11223344"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "2FA setup initiated successfully"
  }
}
```

## Code

- [Python example](../examples/python/set-up-2fa.md) · [Node](../examples/node/set-up-2fa.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api set up 2fa` · `multilogin x set up 2fa`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
