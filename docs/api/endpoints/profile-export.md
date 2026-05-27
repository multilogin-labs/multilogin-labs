# Profile Export

`POST` · [Profile Import/Export](../categories/profile-import-export.md)

```http
POST https://api.multilogin.com/profile/export
```

## Description

**POST** `https://api.multilogin.com/profile/export`

Export profiles to a file.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ],
  "format": "mlx",
  "include_cookies": true,
  "include_extensions": true,
  "include_bookmarks": true,
  "password": "optional_encryption_password"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/export' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ],
  "format": "mlx"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "export_id": "export_123",
    "download_url": "https://api.multilogin.com/download/export_123",
    "expires_at": "2024-01-25T00:00:00Z",
    "file_size_mb": 45.2
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Export started successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-export.md) · [Node](../examples/node/profile-export.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile export` · `multilogin x profile export`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
