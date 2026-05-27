# Start Browser Profile with Selenium

`GET` · [Script Runner](../categories/script-runner.md)

```http
GET https://launcher.mlx.yt:45001/api/v2/profile/f/:folder_id/p/:profile_id/start?automation_type=selenium&script_file=script.py
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v2/profile/f/:folder_id/p/:profile_id/start?automation_type=selenium&script_file=script.py`

Start a browser profile with Selenium automation and run a script.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Path Variables**:
- `folder_id`: uuid (Required)
- `profile_id`: uuid (Required)

**Query Parameters**:
- `automation_type`: selenium (Required)
- `script_file`: string (Required - name of the script file)
- `headless_mode`: boolean (Optional, defaults to false)

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v2/profile/f/81b5627a-1212-4016-9467-3dbe4d6f78eb/p/95f9061e-5656-845a-2801-7fff8f0f12if/start?automation_type=selenium&script_file=automation_script.py' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "browser_type": "mimic",
    "core_version": 132,
    "id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "is_quick": false,
    "port": "55513",
    "script_status": "running",
    "script_file": "automation_script.py"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile started with script runner successfully"
  }
}
```

## Code

- [Python example](../examples/python/start-browser-profile-with-selenium.md) · [Node](../examples/node/start-browser-profile-with-selenium.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api start browser profile with selenium` · `multilogin x start browser profile with selenium`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
