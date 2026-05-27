# Export Status by Profile

`GET` · [Profile Import/Export](../categories/profile-import-export.md)

```http
GET https://api.multilogin.com/profile/export/status
```

## Description

**GET** `https://api.multilogin.com/profile/export/status`

Get export status for specific profile.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `export_id`: string (Required)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/export/status?export_id=export_123' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "export_id": "export_123",
    "status": "completed",
    "progress": 100,
    "download_url": "https://api.multilogin.com/download/export_123",
    "expires_at": "2024-01-25T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Export status retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/export-status-by-profile.md) · [Node](../examples/node/export-status-by-profile.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api export status by profile` · `multilogin x export status by profile`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
