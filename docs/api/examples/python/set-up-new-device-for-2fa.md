# Set up New Device for 2FA — Python

```python
from lib.mlx_client import MLXClient

client = MLXClient.from_env()
# See lib/mlx_client.py for POST https://api.multilogin.com/2fa/device/setup
```

Endpoint: `POST https://api.multilogin.com/2fa/device/setup`

[Endpoint doc](../../endpoints/set-up-new-device-for-2fa.md)
