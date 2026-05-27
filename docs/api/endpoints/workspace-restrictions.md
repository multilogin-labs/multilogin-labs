# Workspace Restrictions

`GET` · [Profile Access Management](../categories/profile-access-management.md)

```http
GET https://api.multilogin.com/workspace/restrictions
```

## Description

**GET** `https://api.multilogin.com/workspace/restrictions`

Get workspace restrictions and limits.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/workspace/restrictions' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "max_profiles": 1000,
    "max_users": 10,
    "max_folders": 50,
    "features": {
      "automation": true,
      "api_access": true,
      "team_management": true
    }
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Restrictions retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/workspace-restrictions.md) · [Node](../examples/node/workspace-restrictions.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api workspace restrictions` · `multilogin x workspace restrictions`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
