# Copy Bookmarks

`POST` · [Bookmark Management](../categories/bookmark-management.md)

```http
POST https://api.multilogin.com/bookmarks/copy
```

## Description

**POST** `https://api.multilogin.com/bookmarks/copy`

Copy bookmarks between profiles.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "source_profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "target_profile_ids": [
    "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  ],
  "merge": false
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/bookmarks/copy' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "source_profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "target_profile_ids": [
    "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  ],
  "merge": false
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "source_profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "copied_to": 1,
    "bookmarks_copied": 15
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Bookmarks copied successfully"
  }
}
```

### 2FA

## Code

- [Python example](../examples/python/copy-bookmarks.md) · [Node](../examples/node/copy-bookmarks.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api copy bookmarks` · `multilogin x copy bookmarks`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
