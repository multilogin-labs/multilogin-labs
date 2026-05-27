# Export Bookmarks

`GET` · [Bookmark Management](../categories/bookmark-management.md)

```http
GET https://api.multilogin.com/bookmarks/export
```

## Description

**GET** `https://api.multilogin.com/bookmarks/export`

Export bookmarks from a profile.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `profile_id`: uuid (Required)
- `format`: string (Optional - json, html)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/bookmarks/export?profile_id=95f9061e-5656-845a-2801-7fff8f0f12if&format=json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "bookmarks": [
      {
        "id": "bookmark_1",
        "title": "Example Site",
        "url": "https://example.com",
        "folder": "Work",
        "created_at": "2024-01-20T00:00:00Z"
      }
    ],
    "total": 1,
    "export_format": "json"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Bookmarks exported successfully"
  }
}
```

## Code

- [Python example](../examples/python/export-bookmarks.md) · [Node](../examples/node/export-bookmarks.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api export bookmarks` · `multilogin x export bookmarks`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
