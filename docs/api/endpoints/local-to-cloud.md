# Local to Cloud

`POST` · [Object Storage](../categories/object-storage.md)

```http
POST https://api.multilogin.com/storage/local_to_cloud
```

## Description

**POST** `https://api.multilogin.com/storage/local_to_cloud`

Transfer object from local to cloud storage.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "local_path": "/profiles/95f9061e/objects/obj_789",
  "object_type": "extension",
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/local_to_cloud' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "local_path": "/profiles/95f9061e/objects/obj_789",
  "object_type": "extension"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "object_id": "obj_790",
    "object_type": "extension",
    "cloud_url": "https://storage.multilogin.com/obj_790",
    "transferred": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object transferred to cloud successfully"
  }
}
```

## Code

- [Python example](../examples/python/local-to-cloud.md) · [Node](../examples/node/local-to-cloud.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api local to cloud` · `multilogin x local to cloud`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
