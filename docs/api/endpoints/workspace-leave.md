# Workspace Leave

`POST` · [Profile Access Management](../categories/profile-access-management.md)

```http
POST https://api.multilogin.com/workspace/leave
```

## Description

**POST** `https://api.multilogin.com/workspace/leave`

Leave a workspace (for non-owner members).

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/workspace/leave' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
}'
```

## Example response

(200 OK):
```json
{
  "data": {},
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Left workspace successfully"
  }
}
```

### Profile Management

## Code

- [Python example](../examples/python/workspace-leave.md) · [Node](../examples/node/workspace-leave.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api workspace leave` · `multilogin x workspace leave`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
