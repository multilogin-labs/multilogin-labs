# Enable 2FA — Python

```python
from lib.mlx_client import MLXClient

client = MLXClient.from_env()
# See lib/mlx_client.py for POST https://api.multilogin.com/2fa/enable
```

Endpoint: `POST https://api.multilogin.com/2fa/enable`

[Endpoint doc](../../endpoints/enable-2fa.md)
