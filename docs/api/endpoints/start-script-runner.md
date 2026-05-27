# Start Script Runner

`POST` · [Script Runner](../categories/script-runner.md)

```http
POST https://api.multilogin.com/script/start
```

## Description

**POST** `https://api.multilogin.com/script/start`

Start a script runner session.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "script_content": "from selenium import webdriver\n# Your script here",
  "script_type": "python",
  "parameters": {
    "timeout": 300,
    "headless": false
  }
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/script/start' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "script_content": "from selenium import webdriver\ndriver.get(\"https://example.com\")",
  "script_type": "python"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "session_id": "script_session_123",
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "status": "running",
    "started_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Script started successfully"
  }
}
```

## Code

- [Python example](../examples/python/start-script-runner.md) · [Node](../examples/node/start-script-runner.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api start script runner` · `multilogin x start script runner`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
