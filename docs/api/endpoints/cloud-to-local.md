# Cloud to Local

`POST` · [Object Storage](../categories/object-storage.md)

```http
POST https://api.multilogin.com/storage/cloud_to_local
```

## Description

**POST** `https://api.multilogin.com/storage/cloud_to_local`

Transfer object from cloud to local storage.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "object_id": "obj_789",
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/cloud_to_local' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "object_id": "obj_789",
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "transferred": true,
    "local_path": "/profiles/95f9061e/objects/obj_789"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object transferred to local successfully"
  }
}
```

## Code

- [Python example](../examples/python/cloud-to-local.md) · [Node](../examples/node/cloud-to-local.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api cloud to local` · `multilogin x cloud to local`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
