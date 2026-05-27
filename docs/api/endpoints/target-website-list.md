# Target Website List

`GET` · [Pre-made Cookies](../categories/pre-made-cookies.md)

```http
GET https://api.multilogin.com/cookies/websites
```

## Description

**GET** `https://api.multilogin.com/cookies/websites`

Get list of supported websites for pre-made cookies.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/cookies/websites' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "websites": [
      {
        "website_id": "google",
        "name": "Google",
        "domain": ".google.com",
        "available_cookies": 150
      },
      {
        "website_id": "facebook",
        "name": "Facebook",
        "domain": ".facebook.com",
        "available_cookies": 200
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Websites retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/target-website-list.md) · [Node](../examples/node/target-website-list.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api target website list` · `multilogin x target website list`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
