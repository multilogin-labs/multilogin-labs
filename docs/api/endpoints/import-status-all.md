# Import Status All

`GET` · [Profile Import/Export](../categories/profile-import-export.md)

```http
GET https://api.multilogin.com/profile/import/status/all
```

## Description

**GET** `https://api.multilogin.com/profile/import/status/all`

Get status of all import jobs.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/import/status/all' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "imports": [
      {
        "import_id": "import_456",
        "status": "completed",
        "created_at": "2024-01-24T00:00:00Z",
        "imported_profiles": 5
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "All import statuses retrieved successfully"
  }
}
```

### Object Storage

## Code

- [Python example](../examples/python/import-status-all.md) · [Node](../examples/node/import-status-all.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api import status all` · `multilogin x import status all`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
