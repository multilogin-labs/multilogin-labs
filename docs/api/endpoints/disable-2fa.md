# Disable 2FA

`POST` · [2FA](../categories/2fa.md)

```http
POST https://api.multilogin.com/2fa/disable
```

## Description

**POST** `https://api.multilogin.com/2fa/disable`

Disable 2FA for the account.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "password": "current_password",
  "code": "123456"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/2fa/disable' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "password": "current_password",
  "code": "123456"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "2fa_enabled": false,
    "disabled_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "2FA disabled successfully"
  }
}
```

---

## Additional Resources

- **Support Page**: [https://help.multilogin.com/en_US/multilogin-x](https://help.multilogin.com/en_US/multilogin-x)
- **Feedback Survey**: [https://tally.so/r/nWABkk](https://tally.so/r/nWABkk)
- **Automation Token**: For higher rate limits and longer token lifetime, use the Workspace Automation Token endpoint

## Notes

- All timestamps are in ISO 8601 format
- UUIDs are used for all ID fields
- Bearer tokens expire after 30 minutes (regular) or as specified (automation)
- Rate limits apply to all endpoints - check response headers for limit information
- All endpoints return consistent error response format with error_code and message

---

*This documentation is complete and includes all endpoints from the Multilogin X API. For the most up-to-date information, always refer to the official API documentation.*

## Code

- [Python example](../examples/python/disable-2fa.md) · [Node](../examples/node/disable-2fa.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api disable 2fa` · `multilogin x disable 2fa`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
