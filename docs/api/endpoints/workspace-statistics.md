# Workspace Statistics

`GET` · [Profile Access Management](../categories/profile-access-management.md)

```http
GET https://api.multilogin.com/workspace/statistics
```

## Description

**GET** `https://api.multilogin.com/workspace/statistics`

Get workspace usage statistics.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/workspace/statistics' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "total_profiles": 150,
    "active_profiles": 25,
    "total_users": 5,
    "storage_used_gb": 45.2,
    "api_calls_this_month": 15000
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Statistics retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/workspace-statistics.md) · [Node](../examples/node/workspace-statistics.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api workspace statistics` · `multilogin x workspace statistics`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
