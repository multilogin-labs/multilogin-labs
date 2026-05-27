# Recipe: Quick profile for one-off scraping

Use **Quick Profile v3** when you don't need a saved profile — data is discarded after stop.

`POST https://launcher.mlx.yt:45001/api/v3/profile/quick`

```python
from lib.mlx_client import MLXClient

client = MLXClient.from_env()
payload = {
    "browser_type": "mimic",
    "os_type": "windows",
    "automation": "playwright",
    "is_headless": False,
    "parameters": {
        "flags": {
            "webrtc_masking": "mask",
            "proxy_masking": "custom",
            "audio_masking": "mask",
        },
        "proxy": {
            "type": "http",
            "host": "proxy.example.com",
            "port": 8080,
            "username": "user",
            "password": "pass",
        },
    },
}
result = client.quick_profile_v3(payload)
print("Port:", result["data"]["port"])
```

Full params: [start-quick-profile-v3.md](../endpoints/start-quick-profile-v3.md)
