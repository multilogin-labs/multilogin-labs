# Profile Partial Update

`POST` · [Profile Management](../categories/profile-management.md)

```http
POST https://api.multilogin.com/profile/partial_update
```

## Description

**POST** `https://api.multilogin.com/profile/partial_update`

Partially update specific profile settings.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "updates": {
    "name": "Partially Updated Name",
    "notes": "Updated notes"
  }
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/partial_update' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "updates": {
    "name": "Partially Updated Name",
    "notes": "Updated notes"
  }
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "updated_fields": ["name", "notes"],
    "updated_at": "2024-01-23T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile partially updated successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-partial-update.md) · [Node](../examples/node/profile-partial-update.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile partial update` · `multilogin x profile partial update`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
