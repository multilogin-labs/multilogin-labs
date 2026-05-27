# Unlock Locked Profiles

`GET` · [Browser Profile Data](../categories/browser-profile-data.md)

```http
GET https://api.multilogin.com/profile/unlock
```

## Description

**GET** `https://api.multilogin.com/profile/unlock`

Unlock profiles that are locked due to unexpected closure.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `profile_ids`: comma-separated string of profile IDs (Optional - unlocks all if not specified)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/profile/unlock?profile_ids=95f9061e-5656-845a-2801-7fff8f0f12if' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "unlocked": 1,
    "profile_ids": [
      "95f9061e-5656-845a-2801-7fff8f0f12if"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profiles unlocked successfully"
  }
}
```

### Proxy

## Code

- [Python example](../examples/python/unlock-locked-profiles.md) · [Node](../examples/node/unlock-locked-profiles.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api unlock locked profiles` · `multilogin x unlock locked profiles`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
