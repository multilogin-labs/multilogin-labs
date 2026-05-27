# Import Bookmarks

`POST` · [Bookmark Management](../categories/bookmark-management.md)

```http
POST https://api.multilogin.com/bookmarks/import
```

## Description

**POST** `https://api.multilogin.com/bookmarks/import`

Import bookmarks to a profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "bookmarks": [
    {
      "title": "New Bookmark",
      "url": "https://newsite.com",
      "folder": "Personal"
    }
  ],
  "merge": true
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/bookmarks/import' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "bookmarks": [
    {
      "title": "New Bookmark",
      "url": "https://newsite.com",
      "folder": "Personal"
    }
  ],
  "merge": true
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "imported": 1,
    "total_bookmarks": 2
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Bookmarks imported successfully"
  }
}
```

## Code

- [Python example](../examples/python/import-bookmarks.md) · [Node](../examples/node/import-bookmarks.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api import bookmarks` · `multilogin x import bookmarks`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
