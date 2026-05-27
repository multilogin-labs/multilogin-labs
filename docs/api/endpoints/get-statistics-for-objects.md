# Get Statistics for Objects

`GET` · [Object Storage](../categories/object-storage.md)

```http
GET https://api.multilogin.com/storage/statistics
```

## Description

**GET** `https://api.multilogin.com/storage/statistics`

Get storage usage statistics.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

## Example request

:
```bash
curl --location 'https://api.multilogin.com/storage/statistics' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Example response

(200 OK):
```json
{
  "data": {
    "total_objects": 45,
    "total_size_gb": 12.5,
    "by_type": {
      "extension": {
        "count": 20,
        "size_gb": 2.5
      },
      "backup": {
        "count": 25,
        "size_gb": 10.0
      }
    },
    "storage_limit_gb": 100,
    "usage_percentage": 12.5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Statistics retrieved successfully"
  }
}
```

## Code

- [Python example](../examples/python/get-statistics-for-objects.md) · [Node](../examples/node/get-statistics-for-objects.md)
- [Cookbook](../cookbook/README.md) · [mlx_client.py](../../../lib/mlx_client.py)

## Search terms

`multilogin api get statistics for objects` · `multilogin x get statistics for objects`

[← Endpoints index](../endpoints-index.md) · [Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
