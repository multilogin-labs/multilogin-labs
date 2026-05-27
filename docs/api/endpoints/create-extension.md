# Create Extension

`POST` · [Object Storage](../categories/object-storage.md)

```http
POST https://api.multilogin.com/storage/extension/create
```

## Description

**POST** `https://api.multilogin.com/storage/extension/create`

Create and upload a browser extension.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: multipart/form-data
- `Accept`: application/json

**Form Data**:
- `file`: File (Required - .zip or .crx file)
- `name`: string (Required)
- `description`: string (Optional)
- `version`: string (Optional)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/extension/create' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--form 'file=@"/path/to/extension.zip"' \
--form 'name="My Custom Extension"' \
--form 'description="Custom extension for automation"' \
--form 'version="1.0.0"'
```

## Example response

(200 OK):
```json
{
  "data": {
    "extension_id": "ext_123",
    "object_id": "obj_791",
    "name": "My Custom Extension",
    "version": "1.0.0",
    "created_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Extension created successfully"
  }
}
```

## Code

- [Python example](../examples/python/create-extension.md) · [Node](../examples/node/create-extension.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api create extension` · `multilogin x create extension`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
