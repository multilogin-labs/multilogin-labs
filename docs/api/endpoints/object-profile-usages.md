# Object Profile Usages

`GET` · [Object Storage](../categories/object-storage.md)

```http
GET https://api.multilogin.com/storage/object/usages
```

## Description

**GET** `https://api.multilogin.com/storage/object/usages`

Get profiles using a specific object.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_id`: string (Required)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/object/usages?object_id=obj_789' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "profiles": [
      {
        "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
        "profile_name": "Marketing Profile 1",
        "attached_at": "2024-01-24T00:00:00Z"
      }
    ],
    "total_usages": 1
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object usages retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/object-profile-usages.md) · [Node](../examples/node/object-profile-usages.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api object profile usages` · `multilogin x object profile usages`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
