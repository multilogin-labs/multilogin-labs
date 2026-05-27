# Workspace Remove Folders

`POST` · [Profile Access Management](../categories/profile-access-management.md)

```http
POST https://api.multilogin.com/workspace/folders/remove
```

## Description

**POST** `https://api.multilogin.com/workspace/folders/remove`

Remove one or more folders from the workspace.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "folder_ids": [
    "93d7849c-3434-6238-0689-5fdf6f8f90gd",
    "94e8950d-4545-7349-1790-6eef7f9f01he"
  ]
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/workspace/folders/remove' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "folder_ids": [
    "93d7849c-3434-6238-0689-5fdf6f8f90gd"
  ]
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "removed": 1,
    "folder_ids": [
      "93d7849c-3434-6238-0689-5fdf6f8f90gd"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Folders removed successfully"
  }
}
```

## Code

- [Python example](../examples/python/workspace-remove-folders.md) · [Node](../examples/node/workspace-remove-folders.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api workspace remove folders` · `multilogin x workspace remove folders`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
