# Workspace Automation Token

`GET` · [Profile Access Management](../categories/profile-access-management.md)

```http
GET https://api.multilogin.com/workspace/automation_token
```

## Description

**GET** `https://api.multilogin.com/workspace/automation_token`

Get workspace automation token for extended API access.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/workspace/automation_token' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "automation_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expires_at": "2024-12-31T23:59:59Z",
    "rate_limit": 10000
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Automation token retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/workspace-automation-token.md) · [Node](../examples/node/workspace-automation-token.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api workspace automation token` · `multilogin x workspace automation token`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
