# Stop Script Runner

`POST` · [Script Runner](../categories/script-runner.md)

```http
POST https://api.multilogin.com/script/stop
```

## Description

**POST** `https://api.multilogin.com/script/stop`

Stop a running script.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "session_id": "script_session_123"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/script/stop' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "session_id": "script_session_123"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "session_id": "script_session_123",
    "status": "stopped",
    "stopped_at": "2024-01-24T00:05:00Z",
    "execution_time_seconds": 300
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Script stopped successfully"
  }
}
```

## Code

- [Python example](../examples/python/stop-script-runner.md) · [Node](../examples/node/stop-script-runner.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api stop script runner` · `multilogin x stop script runner`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
