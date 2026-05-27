# User Sign In

`POST` · [Profile Access Management](../categories/profile-access-management.md)

```http
POST https://api.multilogin.com/user/signin
```

## Description

**POST** `https://api.multilogin.com/user/signin`

Sign in to get a Bearer token for API authentication.

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/user/signin' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "email": "user@example.com",
  "password": "password123"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
    "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Signed in successfully"
  }
}
```

## Code

- [Python example](../examples/python/user-sign-in.md) · [Node](../examples/node/user-sign-in.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api user sign in` · `multilogin x user sign in`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
