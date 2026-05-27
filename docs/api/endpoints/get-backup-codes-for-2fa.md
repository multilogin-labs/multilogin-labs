# Get Backup Codes for 2FA

`GET` · [2FA](../categories/2fa.md)

```http
GET https://api.multilogin.com/2fa/backup_codes
```

## Description

**GET** `https://api.multilogin.com/2fa/backup_codes`

Get backup codes for 2FA recovery.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/2fa/backup_codes' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "backup_codes": [
      {
        "code": "12345678",
        "used": false
      },
      {
        "code": "87654321",
        "used": false
      },
      {
        "code": "11223344",
        "used": true
      }
    ],
    "unused_count": 2,
    "generated_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Backup codes retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/get-backup-codes-for-2fa.md) · [Node](../examples/node/get-backup-codes-for-2fa.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get backup codes for 2fa` · `multilogin x get backup codes for 2fa`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
