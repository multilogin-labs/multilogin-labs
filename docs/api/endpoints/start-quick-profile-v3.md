# Start Quick Profile v3

`POST` · [Launcher](../categories/launcher.md)

```http
POST https://launcher.mlx.yt:45001/api/v3/profile/quick
```

## Description

**POST** `https://launcher.mlx.yt:45001/api/v3/profile/quick`

Create a one-time quick browser profile that opens up after the call is successfully made. Browsing activity and its related data is not saved after the profile has been stopped.

This endpoint supports both Strict and Non-Strict modes. Fingerprint parameters need providing only if flags set to `Custom`.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json
- `X-Strict-Mode`: boolean (Default to false)

**Request Body Parameters**:

Required parameters:
- `browser_type`: "mimic", "stealthfox" (Required, defaults to mimic)
- `os_type`: "linux", "macos", "windows", "android" (Required, defaults to windows)
- `parameters`: Object containing flags, fingerprints, storage, proxy, custom_start_urls

Optional parameters:
- `core_version`: number (defaults to latest)
- `core_minor_version`: number
- `automation`: "selenium"
- `is_headless`: boolean (defaults to false)
- `script_file`: string (for Script Runner)

**Flags** (required in parameters):
- `webrtc_masking`: "natural", "custom", "mask", "disabled"
- `proxy_masking`: "custom", "disabled"
- `geolocation_popup`: "prompt", "allow", "block"
- `audio_masking`: "mask", "natural"
- `graphics_noise`: "mask", "natural"
- `navigator_masking`: "natural", "custom", "mask"
- `localization_masking`: "natural", "custom", "mask"
- `timezone_masking`: "natural", "custom", "mask"
- `graphics_masking`: "natural", "custom", "mask"
- `fonts_masking`: "natural", "custom", "mask"
- `media_devices_masking`: "natural", "custom", "mask"
- `screen_masking`: "natural", "custom", "mask"
- `ports_masking`: "natural", "custom", "mask"
- `geolocation_masking`: "custom", "mask"
- `canvas_noise`: "mask", "natural", "disabled" (optional)
- `startup_behavior`: "recover", "custom" (optional)

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v3/profile/quick' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "browser_type": "mimic",
  "core_version": 124,
  "os_type": "linux",
  "script_file": "example_script3.py",
  "automation": "selenium",
  "is_headless": false,
  "parameters": {
    "flags": {
      "audio_masking": "mask",
      "fonts_masking": "custom",
      "geolocation_masking": "custom",
      "geolocation_popup": "prompt",
      "graphics_masking": "custom",
      "graphics_noise": "mask",
      "localization_masking": "custom",
      "media_devices_masking": "custom",
      "navigator_masking": "custom",
      "ports_masking": "mask",
      "proxy_masking": "custom",
      "screen_masking": "custom",
      "timezone_masking": "custom",
      "webrtc_masking": "custom",
      "canvas_noise": "custom",
      "startup_behavior": "custom"
    },
    "fingerprint": {
      "navigator": {
        "hardware_concurrency": 8,
        "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
      },
      "localization": {
        "languages": "en-US",
        "locale": "en-US",
        "accept_languages": "en-US,en;q=0.5"
      },
      "timezone": {
        "zone": "Asia/Bangkok"
      },
      "graphic": {
        "renderer": "ANGLE (NVIDIA, NVIDIA GeForce RTX 4070 Ti Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "vendor": "Google Inc. (NVIDIA)"
      },
      "webrtc": {
        "public_ip": "123.123.123.123"
      },
      "media_devices": {
        "audio_inputs": 1,
        "audio_outputs": 1,
        "video_inputs": 2
      },
      "screen": {
        "height": 1200,
        "pixel_ratio": 1,
        "width": 1920
      },
      "geolocation": {
        "accuracy": 100,
        "altitude": 100,
        "latitude": 52.02,
        "longitude": -52.1
      }
    },
    "proxy": {
      "host": "host.com",
      "type": "http",
      "port": 8081,
      "username": "username",
      "password": "password",
      "save_traffic": true
    },
    "custom_start_urls": [
      "https://jsonformatter.org/",
      "https://python.org/"
    ]
  }
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "browser_type": "mimic",
    "core_version": 132,
    "id": "d04aa438-d887-11ef-8d6d-0a0027000012",
    "is_quick": true,
    "port": "55579"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Quick profile started successfully"
  }
}
```

## Code

- [Python example](../examples/python/start-quick-profile-v3.md) · [Node](../examples/node/start-quick-profile-v3.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api start quick profile v3` · `multilogin x start quick profile v3`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
