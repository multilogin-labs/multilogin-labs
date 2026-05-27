# Cookies List

`GET` · [Pre-made Cookies](../categories/pre-made-cookies.md)

```http
GET https://api.multilogin.com/cookies/list
```

## Description

**GET** `https://api.multilogin.com/cookies/list`

Get list of available cookie templates.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `website_id`: string (Optional)
- `tag`: string (Optional)
- `limit`: number (Optional)
- `offset`: number (Optional)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/cookies/list?website_id=facebook&limit=10' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "cookies": [
      {
        "cookie_id": "cookie_123",
        "name": "Facebook Aged Account",
        "website_id": "facebook",
        "age_days": 365,
        "quality_score": 95,
        "price": 5.99
      }
    ],
    "total": 1,
    "limit": 10,
    "offset": 0
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Cookies retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/cookies-list.md) · [Node](../examples/node/cookies-list.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api cookies list` · `multilogin x cookies list`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
