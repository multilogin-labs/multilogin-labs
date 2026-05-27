# Profile Import

`POST` · [Profile Import/Export](../categories/profile-import-export.md)

```http
POST https://api.multilogin.com/profile/import
```

## Description

**POST** `https://api.multilogin.com/profile/import`

Import profiles from a file.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "file_url": "https://example.com/profiles.mlx",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "password": "decryption_password_if_needed"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/import' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "file_url": "https://example.com/profiles.mlx",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "import_id": "import_456",
    "status": "processing",
    "total_profiles": 5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Import started successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-import.md) · [Node](../examples/node/profile-import.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile import` · `multilogin x profile import`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
