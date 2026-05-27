# Update Cookies Metadata

`PUT` · [Pre-made Cookies](../categories/pre-made-cookies.md)

```http
PUT https://api.multilogin.com/cookies/metadata/update
```

## Description

**PUT** `https://api.multilogin.com/cookies/metadata/update`

Update cookie template metadata.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "metadata_id": "cookie_meta_123",
  "name": "Updated Social Media Cookies",
  "description": "Updated description",
  "tags": ["social", "automation", "premium"]
}
```

## Example request

:
```bash
curl --location --request PUT 'https://api.multilogin.com/cookies/metadata/update' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "metadata_id": "cookie_meta_123",
  "name": "Updated Social Media Cookies",
  "tags": ["social", "automation", "premium"]
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "metadata_id": "cookie_meta_123",
    "name": "Updated Social Media Cookies",
    "description": "Updated description",
    "tags": ["social", "automation", "premium"],
    "updated_at": "2024-01-24T12:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Cookie metadata updated successfully"
  }
}
```

### Script Runner

## Code

- [Python example](../examples/python/update-cookies-metadata.md) · [Node](../examples/node/update-cookies-metadata.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api update cookies metadata` · `multilogin x update cookies metadata`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
