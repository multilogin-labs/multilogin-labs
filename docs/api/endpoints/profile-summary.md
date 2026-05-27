# Profile Summary

`GET` · [Profile Management](../categories/profile-management.md)

```http
GET https://api.multilogin.com/profile/summary
```

## Description

**GET** `https://api.multilogin.com/profile/summary`

Get summary information for a profile.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `profile_id`: uuid (Required)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/summary?profile_id=95f9061e-5656-845a-2801-7fff8f0f12if' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "name": "Profile Name",
    "browser_type": "mimic",
    "os_type": "windows",
    "created_at": "2024-01-22T00:00:00Z",
    "last_used": "2024-01-23T10:00:00Z",
    "total_sessions": 45,
    "total_duration_minutes": 1250,
    "cookies_count": 234,
    "extensions_count": 5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile summary retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/profile-summary.md) · [Node](../examples/node/profile-summary.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api profile summary` · `multilogin x profile summary`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
