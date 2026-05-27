# Profile Restore

`POST` · [Profile Management](../categories/profile-management.md)

```http
POST https://api.multilogin.com/profile/restore
```

## Description

**POST** `https://api.multilogin.com/profile/restore`

Restore previously deleted profiles.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/restore' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "restored": 1,
    "profile_ids": [
      "95f9061e-5656-845a-2801-7fff8f0f12if"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profiles restored successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-restore.md) · [Node](../examples/node/profile-restore.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile restore` · `multilogin x profile restore`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
