# Verify 2FA — Python

```python
from lib.mlx_client import MLXClient

client = MLXClient.from_env()
# See lib/mlx_client.py for POST https://api.multilogin.com/2fa/verify
```

Endpoint: `POST https://api.multilogin.com/2fa/verify`

[Endpoint doc](../../endpoints/verify-2fa.md)
