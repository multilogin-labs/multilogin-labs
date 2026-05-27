# Convert QBP to Profile

`POST` · [Launcher](../categories/launcher.md)

```http
POST https://launcher.mlx.yt:45001/api/v1/profile/convert_qbp
```

## Description

**POST** `https://launcher.mlx.yt:45001/api/v1/profile/convert_qbp`

Convert a Quick Browser Profile to a regular profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "qbp_id": "temp_12345",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "profile_name": "Converted Profile"
}
```

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/profile/convert_qbp' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "qbp_id": "temp_12345",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "profile_name": "Converted Profile"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profile_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
    "profile_name": "Converted Profile",
    "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "QBP converted successfully"
  }
}
```

## Code

- [Python example](../examples/python/convert-qbp-to-profile.md) · [Node](../examples/node/convert-qbp-to-profile.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api convert qbp to profile` · `multilogin x convert qbp to profile`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
