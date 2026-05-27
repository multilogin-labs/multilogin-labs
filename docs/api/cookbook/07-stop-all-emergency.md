# Recipe: Emergency stop all profiles

`GET https://launcher.mlx.yt:45001/api/v1/profile/stop_all`

```python
from lib.mlx_client import MLXClient
MLXClient.from_env().stop_all_profiles()
```

Node: extend `lib/mlx_client.mjs` or call launcher URL directly.

[stop-all-profiles.md](../endpoints/stop-all-profiles.md)
