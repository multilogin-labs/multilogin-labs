# Enable/Disable 2FA for Workspace

`POST` · [2FA](../categories/2fa.md)

```http
POST https://api.multilogin.com/2fa/workspace
```

## Description

**POST** `https://api.multilogin.com/2fa/workspace`

Enable or disable 2FA requirement for workspace.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
  "require_2fa": true,
  "enforcement_date": "2024-02-01T00:00:00Z"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/2fa/workspace' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
  "require_2fa": true,
  "enforcement_date": "2024-02-01T00:00:00Z"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
    "require_2fa": true,
    "enforcement_date": "2024-02-01T00:00:00Z",
    "affected_users": 5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Workspace 2FA requirement updated successfully"
  }
}
```

## Code

- [Python example](../examples/python/enable-disable-2fa-for-workspace.md) · [Node](../examples/node/enable-disable-2fa-for-workspace.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api enable disable 2fa for workspace` · `multilogin x enable/disable 2fa for workspace`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
