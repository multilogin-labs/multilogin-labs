# Get Object Meta by ID

`GET` · [Object Storage](../categories/object-storage.md)

```http
GET https://api.multilogin.com/storage/object/meta
```

## Description

**GET** `https://api.multilogin.com/storage/object/meta`

Get metadata for a specific object.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_id`: string (Required)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/object/meta?object_id=obj_789' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "object_type": "extension",
    "file_name": "adblock.zip",
    "file_size_mb": 2.5,
    "created_at": "2024-01-24T00:00:00Z",
    "last_accessed": "2024-01-25T10:00:00Z",
    "checksum": "abc123def456",
    "profile_count": 5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object metadata retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/get-object-meta-by-id.md) · [Node](../examples/node/get-object-meta-by-id.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get object meta by id` · `multilogin x get object meta by id`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
