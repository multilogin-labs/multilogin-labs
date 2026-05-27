# Import Status by Profile

`GET` · [Profile Import/Export](../categories/profile-import-export.md)

```http
GET https://api.multilogin.com/profile/import/status
```

## Description

**GET** `https://api.multilogin.com/profile/import/status`

Get import status for specific import job.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `import_id`: string (Required)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/import/status?import_id=import_456' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "import_id": "import_456",
    "status": "completed",
    "progress": 100,
    "imported_profiles": 5,
    "failed_profiles": 0,
    "profile_ids": [
      "new_profile_1",
      "new_profile_2"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Import status retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/import-status-by-profile.md) · [Node](../examples/node/import-status-by-profile.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api import status by profile` · `multilogin x import status by profile`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
