# Revoke Device for 2FA

`POST` · [2FA](../categories/2fa.md)

```http
POST https://api.multilogin.com/2fa/device/revoke
```

## Description

**POST** `https://api.multilogin.com/2fa/device/revoke`

Revoke a trusted device.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "device_id": "device_456"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/2fa/device/revoke' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "device_id": "device_456"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "device_id": "device_456",
    "revoked": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Device revoked successfully"
  }
}
```

## Code

- [Python example](../examples/python/revoke-device-for-2fa.md) · [Node](../examples/node/revoke-device-for-2fa.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api revoke device for 2fa` · `multilogin x revoke device for 2fa`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
