# Download Object

`GET` · [Object Storage](../categories/object-storage.md)

```http
GET https://api.multilogin.com/storage/object/download
```

## Description

**GET** `https://api.multilogin.com/storage/object/download`

Get download URL for an object.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_id`: string (Required)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/object/download?object_id=obj_789' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "download_url": "https://download.multilogin.com/obj_789?token=abc123",
    "expires_at": "2024-01-24T01:00:00Z",
    "file_name": "extension.zip",
    "file_size_mb": 2.5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Download URL generated successfully"
  }
}
```

## Code

- [Python example](../examples/python/download-object.md) · [Node](../examples/node/download-object.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api download object` · `multilogin x download object`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
