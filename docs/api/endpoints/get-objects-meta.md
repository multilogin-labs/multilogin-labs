# Get Objects Meta

`GET` · [Object Storage](../categories/object-storage.md)

```http
GET https://api.multilogin.com/storage/objects/meta
```

## Description

**GET** `https://api.multilogin.com/storage/objects/meta`

Get metadata for multiple objects.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_type`: string (Optional)
- `limit`: number (Optional)
- `offset`: number (Optional)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/objects/meta?object_type=extension&limit=10' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "objects": [
      {
        "object_id": "obj_789",
        "object_type": "extension",
        "file_name": "adblock.zip",
        "file_size_mb": 2.5,
        "created_at": "2024-01-24T00:00:00Z",
        "profile_count": 5
      }
    ],
    "total": 1,
    "limit": 10,
    "offset": 0
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Objects metadata retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/get-objects-meta.md) · [Node](../examples/node/get-objects-meta.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get objects meta` · `multilogin x get objects meta`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
