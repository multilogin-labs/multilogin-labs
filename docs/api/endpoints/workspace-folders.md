# Workspace Folders

`GET` · [Profile Access Management](../categories/profile-access-management.md)

```http
GET https://api.multilogin.com/workspace/folders
```

## Description

**GET** `https://api.multilogin.com/workspace/folders`

Get all folders in the workspace.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/workspace/folders' \
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
        "profile_count": 10,
        "created_at": "2024-01-01T00:00:00Z"
      },
      {
        "folder_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
        "name": "Marketing",
        "profile_count": 5,
        "created_at": "2024-01-15T00:00:00Z"
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Folders retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/workspace-folders.md) · [Node](../examples/node/workspace-folders.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api workspace folders` · `multilogin x workspace folders`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
