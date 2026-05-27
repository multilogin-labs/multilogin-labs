# Profile Metas

`POST` · [Profile Management](../categories/profile-management.md)

```http
POST https://api.multilogin.com/profile/metas
```

## Description

**POST** `https://api.multilogin.com/profile/metas`

Get metadata for multiple profiles.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if",
    "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  ]
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/metas' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profiles": [
      {
        "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
        "name": "Profile Name",
        "browser_type": "mimic",
        "os_type": "windows",
        "created_at": "2024-01-22T00:00:00Z",
        "last_used": "2024-01-23T10:00:00Z",
        "storage_size_mb": 125.5
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile metas retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-metas.md) · [Node](../examples/node/profile-metas.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile metas` · `multilogin x profile metas`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
