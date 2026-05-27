# Workspace Update Folder

`POST` · [Profile Access Management](../categories/profile-access-management.md)

```http
POST https://api.multilogin.com/workspace/folder/update
```

## Description

**POST** `https://api.multilogin.com/workspace/folder/update`

Update folder information.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "folder_id": "93d7849c-3434-6238-0689-5fdf6f8f90gd",
  "name": "Updated Folder Name",
  "description": "Updated description"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/workspace/folder/update' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "folder_id": "93d7849c-3434-6238-0689-5fdf6f8f90gd",
  "name": "Updated Folder Name",
  "description": "Updated description"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "folder_id": "93d7849c-3434-6238-0689-5fdf6f8f90gd",
    "name": "Updated Folder Name",
    "description": "Updated description",
    "updated_at": "2024-01-21T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Folder updated successfully"
  }
}
```

## Code

- [Python example](../examples/python/workspace-update-folder.md) · [Node](../examples/node/workspace-update-folder.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api workspace update folder` · `multilogin x workspace update folder`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
