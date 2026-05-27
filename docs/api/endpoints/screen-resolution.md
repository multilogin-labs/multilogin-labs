# Screen Resolution

`GET` · [Profile Management](../categories/profile-management.md)

```http
GET https://api.multilogin.com/profile/screen_resolutions
```

## Description

**GET** `https://api.multilogin.com/profile/screen_resolutions`

Get available screen resolutions for profiles.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `os_type`: string (Optional - windows, macos, linux, android)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/screen_resolutions?os_type=windows' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "resolutions": [
      {
        "width": 1920,
        "height": 1080,
        "label": "Full HD"
      },
      {
        "width": 1366,
        "height": 768,
        "label": "HD"
      },
      {
        "width": 2560,
        "height": 1440,
        "label": "QHD"
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Screen resolutions retrieved successfully"
  }
}
```

### Browser Profile Data

## Code

- [Python example](../examples/python/screen-resolution.md) · [Node](../examples/node/screen-resolution.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api screen resolution` · `multilogin x screen resolution`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
