# Get List of Object Types

`GET` · [Object Storage](../categories/object-storage.md)

```http
GET https://api.multilogin.com/storage/types
```

## Description

**GET** `https://api.multilogin.com/storage/types`

Get available object types.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/types' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "types": [
      {
        "type_id": "extension",
        "name": "Browser Extension",
        "max_size_mb": 50,
        "allowed_formats": [".zip", ".crx"]
      },
      {
        "type_id": "backup",
        "name": "Profile Backup",
        "max_size_mb": 500,
        "allowed_formats": [".mlx", ".zip"]
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object types retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/get-list-of-object-types.md) · [Node](../examples/node/get-list-of-object-types.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get list of object types` · `multilogin x get list of object types`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
