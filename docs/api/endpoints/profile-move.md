# Profile Move

`POST` · [Profile Management](../categories/profile-management.md)

```http
POST https://api.multilogin.com/profile/move
```

## Description

**POST** `https://api.multilogin.com/profile/move`

Move profiles to a different folder.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ],
  "folder_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/move' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ],
  "folder_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "moved": 1,
    "profile_ids": [
      "95f9061e-5656-845a-2801-7fff8f0f12if"
    ],
    "folder_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profiles moved successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-move.md) · [Node](../examples/node/profile-move.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile move` · `multilogin x profile move`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
