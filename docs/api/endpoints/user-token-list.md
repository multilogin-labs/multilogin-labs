# User Token List

`GET` · [Profile Access Management](../categories/profile-access-management.md)

```http
GET https://api.multilogin.com/user/tokens
```

## Description

**GET** `https://api.multilogin.com/user/tokens`

Get list of active tokens.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/user/tokens' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "tokens": [
      {
        "token_id": "token_123",
        "created_at": "2024-01-01T00:00:00Z",
        "expires_at": "2024-01-01T00:30:00Z",
        "type": "regular"
      },
      {
        "token_id": "token_456",
        "created_at": "2024-01-01T00:00:00Z",
        "expires_at": "2024-12-31T23:59:59Z",
        "type": "automation"
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Tokens retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/user-token-list.md) · [Node](../examples/node/user-token-list.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api user token list` · `multilogin x user token list`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
