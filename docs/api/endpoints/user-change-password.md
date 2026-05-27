# User Change Password

`POST` · [Profile Access Management](../categories/profile-access-management.md)

```http
POST https://api.multilogin.com/user/change_password
```

## Description

**POST** `https://api.multilogin.com/user/change_password`

Change user password.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "current_password": "oldpassword123",
  "new_password": "newpassword456"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/user/change_password' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "current_password": "oldpassword123",
  "new_password": "newpassword456"
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
    "message": "Password changed successfully"
  }
}
```

## Code

- [Python example](../examples/python/user-change-password.md) · [Node](../examples/node/user-change-password.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api user change password` · `multilogin x user change password`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
