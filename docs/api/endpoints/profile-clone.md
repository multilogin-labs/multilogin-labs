# Profile Clone

`POST` · [Profile Management](../categories/profile-management.md)

```http
POST https://api.multilogin.com/profile/clone
```

## Description

**POST** `https://api.multilogin.com/profile/clone`

Clone an existing profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "name": "Cloned Profile",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "include_cookies": true,
  "include_extensions": true,
  "include_bookmarks": true
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/clone' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "name": "Cloned Profile",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "original_profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "cloned_profile_id": "96g0172f-6767-956b-3912-8ggg9g1g23jg",
    "name": "Cloned Profile",
    "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile cloned successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-clone.md) · [Node](../examples/node/profile-clone.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile clone` · `multilogin x profile clone`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
