# Export Status All

`GET` · [Profile Import/Export](../categories/profile-import-export.md)

```http
GET https://api.multilogin.com/profile/export/status/all
```

## Description

**GET** `https://api.multilogin.com/profile/export/status/all`

Get status of all exports.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/export/status/all' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "exports": [
      {
        "export_id": "export_123",
        "status": "completed",
        "created_at": "2024-01-24T00:00:00Z",
        "profile_count": 1
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "All export statuses retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/export-status-all.md) · [Node](../examples/node/export-status-all.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api export status all` · `multilogin x export status all`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
