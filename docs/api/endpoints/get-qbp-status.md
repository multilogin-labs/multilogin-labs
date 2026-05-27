# Get QBP Status

`GET` · [Launcher](../categories/launcher.md)

```http
GET https://launcher.mlx.yt:45001/api/v1/profile/qbp_status
```

## Description

**GET** `https://launcher.mlx.yt:45001/api/v1/profile/qbp_status`

Get status of a Quick Browser Profile.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `qbp_id`: string (Required)

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/profile/qbp_status?qbp_id=temp_12345' \
--header 'Accept: application/json'
```

## Example response

(200 OK):
```json
{
  "data": {
    "qbp_id": "temp_12345",
    "is_active": true,
    "port": "55514"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "QBP status retrieved successfully"
  }
}
```

### Profile Access Management

## Code

- [Python example](../examples/python/get-qbp-status.md) · [Node](../examples/node/get-qbp-status.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get qbp status` · `multilogin x get qbp status`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
