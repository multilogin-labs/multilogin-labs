# Delete Browser Core

`DELETE` · [Launcher](../categories/launcher.md)

```http
DELETE https://launcher.mlx.yt:45001/api/v1/core
```

## Description

**DELETE** `https://launcher.mlx.yt:45001/api/v1/core`

Delete a specific browser core.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `browser_type`: string (Required)
- `version`: number (Required)

## Example request

:
```bash
curl --location --request DELETE 'https://launcher.mlx.yt:45001/api/v1/core?browser_type=mimic&version=131' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "browser_type": "mimic",
    "version": 131,
    "deleted": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Core deleted successfully"
  }
}
```

## Code

- [Python example](../examples/python/delete-browser-core.md) · [Node](../examples/node/delete-browser-core.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api delete browser core` · `multilogin x delete browser core`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
