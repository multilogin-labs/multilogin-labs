# Generate Proxy

`POST` · [Proxy](../categories/proxy.md)

```http
POST https://api.multilogin.com/proxy/generate
```

## Description

**POST** `https://api.multilogin.com/proxy/generate`

Generate proxy configuration.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "country": "US",
  "city": "New York",
  "provider": "residential",
  "protocol": "http"
}
```

## Example request

:
```bash
curl --location 'https://api.multilogin.com/proxy/generate' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "country": "US",
  "city": "New York",
  "provider": "residential",
  "protocol": "http"
}'
```

## Example response

(200 OK):
```json
{
  "data": {
    "proxy": {
      "host": "proxy.provider.com",
      "port": 8080,
      "username": "generated_user",
      "password": "generated_pass",
      "type": "http",
      "country": "US",
      "city": "New York"
    }
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Proxy generated successfully"
  }
}
```

## Code

- [Python example](../examples/python/generate-proxy.md) · [Node](../examples/node/generate-proxy.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api generate proxy` · `multilogin x generate proxy`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
