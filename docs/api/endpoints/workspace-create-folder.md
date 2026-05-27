# Workspace Create Folder

`POST` · [Profile Access Management](../categories/profile-access-management.md)

```http
POST https://api.multilogin.com/workspace/folder/create
```

## Description

**POST** `https://api.multilogin.com/workspace/folder/create`

Create a new folder in the workspace.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "name": "New Folder",
  "description": "Folder for new campaigns"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/workspace/folder/create' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "name": "New Folder",
  "description": "Folder for new campaigns"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "folder_id": "93d7849c-3434-6238-0689-5fdf6f8f90gd",
    "name": "New Folder",
    "description": "Folder for new campaigns",
    "created_at": "2024-01-20T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Folder created successfully"
  }
}
```

## Code

- [Python example](../examples/python/workspace-create-folder.md) · [Node](../examples/node/workspace-create-folder.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api workspace create folder` · `multilogin x workspace create folder`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
