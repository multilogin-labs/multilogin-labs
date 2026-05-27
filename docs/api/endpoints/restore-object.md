# Restore Object

`GET` · [Object Storage](../categories/object-storage.md)

```http
GET https://api.multilogin.com/storage/object/restore
```

## Description

**GET** `https://api.multilogin.com/storage/object/restore`

Restore a deleted object.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_id`: string (Required)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/object/restore?object_id=obj_789' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "restored": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object restored successfully"
  }
}
```

## Code

- [Python example](../examples/python/restore-object.md) · [Node](../examples/node/restore-object.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api restore object` · `multilogin x restore object`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
