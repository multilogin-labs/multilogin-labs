# Create and Upload

`POST` · [Object Storage](../categories/object-storage.md)

```http
POST https://api.multilogin.com/storage/create_upload
```

## Description

**POST** `https://api.multilogin.com/storage/create_upload`

Create storage object and get upload URL.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "object_type": "extension",
  "file_name": "my-extension.zip",
  "file_size_bytes": 2621440,
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/create_upload' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "object_type": "extension",
  "file_name": "my-extension.zip",
  "file_size_bytes": 2621440
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "upload_url": "https://upload.multilogin.com/obj_789",
    "upload_method": "PUT",
    "expires_at": "2024-01-24T01:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Upload URL created successfully"
  }
}
```

## Code

- [Python example](../examples/python/create-and-upload.md) · [Node](../examples/node/create-and-upload.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api create and upload` · `multilogin x create and upload`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
