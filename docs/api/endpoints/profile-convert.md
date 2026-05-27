# Profile Convert

`POST` · [Profile Management](../categories/profile-management.md)

```http
POST https://api.multilogin.com/profile/convert
```

## Description

**POST** `https://api.multilogin.com/profile/convert`

Convert profile between different browser types.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "target_browser_type": "stealthfox",
  "keep_original": true
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/convert' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "target_browser_type": "stealthfox",
  "keep_original": true
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "original_profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "converted_profile_id": "97h1283g-7878-067c-4023-9hhh0h2h34kh",
    "target_browser_type": "stealthfox"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile converted successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-convert.md) · [Node](../examples/node/profile-convert.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile convert` · `multilogin x profile convert`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
