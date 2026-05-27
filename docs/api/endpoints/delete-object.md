# Delete Object

`GET` · [Object Storage](../categories/object-storage.md)

```http
GET https://api.multilogin.com/storage/object/delete
```

## Description

**GET** `https://api.multilogin.com/storage/object/delete`

Delete an object from storage.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_id`: string (Required)
- `force`: boolean (Optional - force delete even if attached to profiles)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/object/delete?object_id=obj_789&force=false' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "deleted": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object deleted successfully"
  }
}
```

## Code

- [Python example](../examples/python/delete-object.md) · [Node](../examples/node/delete-object.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api delete object` · `multilogin x delete object`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
