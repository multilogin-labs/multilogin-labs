# List of Objects per Profile

`POST` · [Object Storage](../categories/object-storage.md)

```http
POST https://api.multilogin.com/storage/profile/objects
```

## Description

**POST** `https://api.multilogin.com/storage/profile/objects`

Get all objects associated with a profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/profile/objects' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "objects": [
      {
        "object_id": "obj_789",
        "object_type": "extension",
        "file_name": "adblock.zip",
        "attached_at": "2024-01-24T00:00:00Z"
      },
      {
        "object_id": "obj_790",
        "object_type": "backup",
        "file_name": "profile_backup.mlx",
        "attached_at": "2024-01-23T00:00:00Z"
      }
    ],
    "total_objects": 2
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile objects retrieved successfully"
  }
}
```

### Bookmark Management

## Code

- [Python example](../examples/python/list-of-objects-per-profile.md) · [Node](../examples/node/list-of-objects-per-profile.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api list of objects per profile` · `multilogin x list of objects per profile`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
