# Fetch Proxy Data

`GET` · [Proxy](../categories/proxy.md)

```http
GET https://api.multilogin.com/proxy/data
```

## Description

**GET** `https://api.multilogin.com/proxy/data`

Fetch proxy information and validate connectivity.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `host`: string (Required)
- `port`: number (Required)
- `type`: string (Required - http, https, socks5)
- `username`: string (Optional)
- `password`: string (Optional)

## Example request

:
```bash
curl --location 'https://api.multilogin.com/proxy/data?host=proxy.example.com&port=8080&type=http' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "proxy": {
      "host": "proxy.example.com",
      "port": 8080,
      "type": "http",
      "is_active": true,
      "ip": "123.456.789.10",
      "country": "US",
      "city": "New York",
      "isp": "Example ISP",
      "latency_ms": 125
    }
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Proxy data fetched successfully"
  }
}
```

### Pre-made Cookies

## Code

- [Python example](../examples/python/fetch-proxy-data.md) · [Node](../examples/node/fetch-proxy-data.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api fetch proxy data` · `multilogin x fetch proxy data`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
