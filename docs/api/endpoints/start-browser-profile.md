# Start Browser Profile

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v2/profile/f/:folder_id/p/:profile_id/start
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v2/profile/f/:folder_id/p/:profile_id/start`

This endpoint supports both Strict and Non-Strict modes. In Strict mode, all required parameters must be explicitly specified. In contrast, Non-Strict mode allows for faster usage by applying default values to any unspecified parameters.

Start a browser profile. The endpoint will return a port for automation in the response message if the automation type parameter is passed.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json
- `X-Strict-Mode`: boolean (Default to false)

**Query Parameters**:
- `automation_type`: selenium, puppeteer, playwright (Optional, defaults to selenium)
- `headless_mode`: false, true (Optional, defaults to false)

**Path Variables**:
- `folder_id`: uuid (Required)
- `profile_id`: uuid (Required)

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v2/profile/f/81b5627a-1212-4016-9467-3dbe4d6f78eb/p/81b5627a-1212-4016-9467-3dbe4d6f78eb/start?automation_type=puppeteer&headless_mode=false' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "browser_type": "mimic",
    "core_version": 132,
    "id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
    "is_quick": false,
    "port": "55513"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile started successfully"
  }
}
```

## Code

- [Python example](../examples/python/start-browser-profile.md) · [Node](../examples/node/start-browser-profile.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api start browser profile` · `multilogin x start browser profile`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
