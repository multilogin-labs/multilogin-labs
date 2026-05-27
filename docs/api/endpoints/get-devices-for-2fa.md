# Get Devices for 2FA

`GET` · [2FA](../categories/2fa.md)

```http
GET https://api.multilogin.com/2fa/devices
```

## Description

**GET** `https://api.multilogin.com/2fa/devices`

Get list of trusted devices.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/2fa/devices' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "devices": [
      {
        "device_id": "device_456",
        "device_name": "My Laptop",
        "device_type": "desktop",
        "trusted_until": "2024-02-23T00:00:00Z",
        "last_used": "2024-01-24T10:00:00Z"
      }
    ],
    "total": 1
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Devices retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/get-devices-for-2fa.md) · [Node](../examples/node/get-devices-for-2fa.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get devices for 2fa` · `multilogin x get devices for 2fa`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
