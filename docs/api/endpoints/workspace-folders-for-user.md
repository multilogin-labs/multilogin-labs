# Workspace Folders For User

`GET` · [Profile Access Management](../categories/profile-access-management.md)

```http
GET https://api.multilogin.com/workspace/folders/user
```

## Description

**GET** `https://api.multilogin.com/workspace/folders/user`

Get folders accessible by the current user.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/workspace/folders/user' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "folders": [
      {
        "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
        "name": "Default",
        "permissions": ["read", "write", "delete"],
        "profile_count": 10
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "User folders retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/workspace-folders-for-user.md) · [Node](../examples/node/workspace-folders-for-user.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api workspace folders for user` · `multilogin x workspace folders for user`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
