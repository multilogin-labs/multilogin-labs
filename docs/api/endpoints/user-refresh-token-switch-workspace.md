# User Refresh Token (Switch Workspace)

`POST` · [Profile Access Management](../categories/profile-access-management.md)

```http
POST https://api.multilogin.com/user/refresh_token
```

## Description

**POST** `https://api.multilogin.com/user/refresh_token`

Refresh authentication token or switch workspace.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "workspace_id": "new-workspace-id" // Optional, for switching workspace
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/user/refresh_token' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Token refreshed successfully"
  }
}
```

## Code

- [Python example](../examples/python/user-refresh-token-switch-workspace.md) · [Node](../examples/node/user-refresh-token-switch-workspace.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api user refresh token switch workspace` · `multilogin x user refresh token (switch workspace)`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
