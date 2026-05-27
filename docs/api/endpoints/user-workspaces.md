# User Workspaces

`GET` · [Profile Access Management](../categories/profile-access-management.md)

```http
GET https://api.multilogin.com/user/workspaces
```

## Description

**GET** `https://api.multilogin.com/user/workspaces`

Get list of user's workspaces.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/user/workspaces' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "workspaces": [
      {
        "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
        "name": "My Workspace",
        "role": "owner",
        "created_at": "2024-01-01T00:00:00Z"
      },
      {
        "workspace_id": "83d7849c-3434-6238-0689-5fdf6f8f90gd",
        "name": "Team Workspace",
        "role": "member",
        "created_at": "2024-01-15T00:00:00Z"
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Workspaces retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/user-workspaces.md) · [Node](../examples/node/user-workspaces.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api user workspaces` · `multilogin x user workspaces`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
