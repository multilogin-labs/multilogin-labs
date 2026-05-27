# Profile Search

`POST` · [Profile Management](../categories/profile-management.md)

```http
POST https://api.multilogin.com/profile/search
```

## Description

**POST** `https://api.multilogin.com/profile/search`

Search for profiles based on criteria.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "limit": 10,
  "offset": 0,
  "search_text": "marketing",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "browser_type": "mimic",
  "sort_by": "created_at",
  "sort_order": "desc"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "limit": 10,
  "offset": 0,
  "search_text": "marketing"
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
        "name": "Marketing Profile 1",
        "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
        "browser_type": "mimic",
        "os_type": "windows",
        "created_at": "2024-01-22T00:00:00Z",
        "last_used": "2024-01-23T10:00:00Z"
      }
    ],
    "total": 1,
    "limit": 10,
    "offset": 0
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profiles found successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-search.md) · [Node](../examples/node/profile-search.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile search` · `multilogin x profile search`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
