# Profile Update

`POST` · [Profile Management](../categories/profile-management.md)

```http
POST https://api.multilogin.com/profile/update
```

## Description

**POST** `https://api.multilogin.com/profile/update`

Update profile information and settings.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "name": "Updated Profile Name",
  "parameters": {
    "flags": {
      "proxy_masking": "custom"
    },
    "proxy": {
      "host": "new-proxy.example.com",
      "type": "http",
      "port": 8080,
      "username": "user",
      "password": "pass"
    }
  }
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/update' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "name": "Updated Profile Name"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "name": "Updated Profile Name",
    "updated_at": "2024-01-23T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile updated successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-update.md) · [Node](../examples/node/profile-update.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile update` · `multilogin x profile update`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
