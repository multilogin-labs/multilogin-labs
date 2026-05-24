# Revoke Device for 2FA — Python

```python
from lib.mlx_client import MLXClient

client = MLXClient.from_env()
# See lib/mlx_client.py for POST https://api.multilogin.com/2fa/device/revoke
```

Endpoint: `POST https://api.multilogin.com/2fa/device/revoke`

[Endpoint doc](../../endpoints/revoke-device-for-2fa.md)
