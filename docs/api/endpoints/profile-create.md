# Profile Create

`POST` · [Profile Management](../categories/profile-management.md)

```http
POST https://api.multilogin.com/profile/create
```

## Description

**POST** `https://api.multilogin.com/profile/create`

Create a new browser profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "name": "New Profile",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "browser_type": "mimic",
  "os_type": "windows",
  "parameters": {
    "flags": {
      "audio_masking": "mask",
      "fonts_masking": "natural",
      "geolocation_masking": "mask",
      "geolocation_popup": "prompt",
      "graphics_masking": "mask",
      "graphics_noise": "mask",
      "localization_masking": "mask",
      "media_devices_masking": "natural",
      "navigator_masking": "mask",
      "ports_masking": "mask",
      "proxy_masking": "disabled",
      "screen_masking": "mask",
      "timezone_masking": "mask",
      "webrtc_masking": "mask"
    },
    "storage": {
      "bookmarks": true,
      "cookies": true,
      "extensions": true,
      "history": true,
      "local_storage": true,
      "passwords": true
    }
  }
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/create' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "name": "New Profile",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "browser_type": "mimic",
  "os_type": "windows",
  "parameters": {
    "flags": {
      "audio_masking": "mask",
      "fonts_masking": "natural",
      "geolocation_masking": "mask",
      "geolocation_popup": "prompt",
      "graphics_masking": "mask",
      "graphics_noise": "mask",
      "localization_masking": "mask",
      "media_devices_masking": "natural",
      "navigator_masking": "mask",
      "ports_masking": "mask",
      "proxy_masking": "disabled",
      "screen_masking": "mask",
      "timezone_masking": "mask",
      "webrtc_masking": "mask"
    }
  }
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "name": "New Profile",
    "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
    "browser_type": "mimic",
    "os_type": "windows",
    "created_at": "2024-01-22T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile created successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-create.md) · [Node](../examples/node/profile-create.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile create` · `multilogin x profile create`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
