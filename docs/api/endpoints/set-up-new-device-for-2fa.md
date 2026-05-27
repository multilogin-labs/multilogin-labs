# Set up New Device for 2FA

`POST` · [2FA](../categories/2fa.md)

```http
POST https://api.multilogin.com/2fa/device/setup
```

## Description

**POST** `https://api.multilogin.com/2fa/device/setup`

Add a new trusted device for 2FA.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "device_name": "My Laptop",
  "device_type": "desktop",
  "trust_duration_days": 30
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/2fa/device/setup' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "device_name": "My Laptop",
  "device_type": "desktop",
  "trust_duration_days": 30
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "device_id": "device_456",
    "device_name": "My Laptop",
    "trusted_until": "2024-02-23T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Device added successfully"
  }
}
```

## Code

- [Python example](../examples/python/set-up-new-device-for-2fa.md) · [Node](../examples/node/set-up-new-device-for-2fa.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api set up new device for 2fa` · `multilogin x set up new device for 2fa`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
