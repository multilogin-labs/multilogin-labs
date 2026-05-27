# Upload Object

`POST` · [Object Storage](../categories/object-storage.md)

```http
POST https://api.multilogin.com/storage/upload
```

## Description

**POST** `https://api.multilogin.com/storage/upload`

Upload an object to storage.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: multipart/form-data
- `Accept`: application/json

**Form Data**:
- `file`: File (Required)
- `object_type`: string (Required - extension, backup, etc.)
- `profile_id`: uuid (Optional - for profile-specific objects)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/upload' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--form 'file=@"/path/to/file.zip"' \
--form 'object_type="extension"' \
--form 'profile_id="95f9061e-5656-845a-2801-7fff8f0f12if"'
```

## Example response

(200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "object_type": "extension",
    "file_name": "extension.zip",
    "file_size_mb": 2.5,
    "upload_url": "https://storage.multilogin.com/obj_789"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object uploaded successfully"
  }
}
```

## Code

- [Python example](../examples/python/upload-object.md) · [Node](../examples/node/upload-object.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api upload object` · `multilogin x upload object`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
