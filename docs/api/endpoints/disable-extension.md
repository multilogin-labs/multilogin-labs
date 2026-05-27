# Disable Extension

`POST` · [Object Storage](../categories/object-storage.md)

```http
POST https://api.multilogin.com/storage/extension/disable
```

## Description

**POST** `https://api.multilogin.com/storage/extension/disable`

Disable extension for profiles.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "extension_id": "ext_123",
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/extension/disable' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "extension_id": "ext_123",
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "extension_id": "ext_123",
    "disabled_for": 1,
    "profile_ids": [
      "95f9061e-5656-845a-2801-7fff8f0f12if"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Extension disabled successfully"
  }
}
```

## Code

- [Python example](../examples/python/disable-extension.md) · [Node](../examples/node/disable-extension.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api disable extension` · `multilogin x disable extension`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
