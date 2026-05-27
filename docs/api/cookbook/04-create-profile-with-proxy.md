# Recipe: Create profile + validate proxy

## 1. Validate proxy (Launcher)

`POST https://launcher.mlx.yt:45001/api/v1/proxy/validate`

## 2. Create profile

`POST https://api.multilogin.com/profile/create`

```python
from lib.mlx_client import MLXClient

client = MLXClient.from_env()
client.profile_create({
    "name": "Farm-Profile-001",
    "folder_id": "YOUR_FOLDER_UUID",
    "browser_type": "mimic",
    "os_type": "windows",
    "parameters": {
        "flags": {"webrtc_masking": "mask", "proxy_masking": "custom"},
        "proxy": {
            "type": "http",
            "host": "proxy.example.com",
            "port": 8080,
            "username": "user",
            "password": "pass",
        },
    },
})
```

[profile-create.md](../endpoints/profile-create.md) · [validate-proxy.md](../endpoints/validate-proxy.md)
