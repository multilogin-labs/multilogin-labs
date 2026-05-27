# Script List

`GET` · [Script Runner](../categories/script-runner.md)

```http
GET https://api.multilogin.com/script/list
```

## Description

**GET** `https://api.multilogin.com/script/list`

Get list of available scripts.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `status`: string (Optional - running, completed, failed)
- `limit`: number (Optional)
- `offset`: number (Optional)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/script/list?status=running' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "scripts": [
      {
        "script_id": "script_123",
        "name": "Social Media Automation",
        "type": "python",
        "status": "running",
        "created_at": "2024-01-24T00:00:00Z",
        "last_run": "2024-01-24T10:00:00Z"
      }
    ],
    "total": 1,
    "limit": 10,
    "offset": 0
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Scripts retrieved successfully"
  }
}
```

### Profile Import/Export

## Code

- [Python example](../examples/python/script-list.md) · [Node](../examples/node/script-list.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api script list` · `multilogin x script list`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
