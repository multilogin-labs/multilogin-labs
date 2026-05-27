# Create Cookies Metadata

`POST` · [Pre-made Cookies](../categories/pre-made-cookies.md)

```http
POST https://api.multilogin.com/cookies/metadata/create
```

## Description

**POST** `https://api.multilogin.com/cookies/metadata/create`

Create metadata for cookie templates.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "name": "Social Media Cookies",
  "description": "Cookie set for social media automation",
  "website_ids": ["facebook", "instagram", "twitter"],
  "tags": ["social", "automation"]
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/cookies/metadata/create' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "name": "Social Media Cookies",
  "description": "Cookie set for social media automation",
  "website_ids": ["facebook", "instagram"],
  "tags": ["social", "automation"]
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "metadata_id": "cookie_meta_123",
    "name": "Social Media Cookies",
    "description": "Cookie set for social media automation",
    "website_ids": ["facebook", "instagram"],
    "tags": ["social", "automation"],
    "created_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Cookie metadata created successfully"
  }
}
```

## Code

- [Python example](../examples/python/create-cookies-metadata.md) · [Node](../examples/node/create-cookies-metadata.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api create cookies metadata` · `multilogin x create cookies metadata`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
