# Validate Proxy

`POST` · [Launcher](../categories/launcher.md)

```http
POST https://launcher.mlx.yt:45001/api/v1/proxy/validate
```

## Description

**POST** `https://launcher.mlx.yt:45001/api/v1/proxy/validate`

Validate proxy configuration.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "host": "proxy.example.com",
  "type": "http",
  "port": 8080,
  "username": "user",
  "password": "pass"
}
```

## Example request

:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/proxy/validate' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "host": "proxy.example.com",
  "type": "http",
  "port": 8080,
  "username": "user",
  "password": "pass"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "is_valid": true,
    "ip": "123.456.789.10",
    "country": "US",
    "city": "New York"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Proxy validated successfully"
  }
}
```

## Code

- [Python example](../examples/python/validate-proxy.md) · [Node](../examples/node/validate-proxy.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api validate proxy` · `multilogin x validate proxy`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
