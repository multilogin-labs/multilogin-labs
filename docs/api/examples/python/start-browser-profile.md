# Start Browser Profile — Python

```python
import os
from lib.mlx_client import MLXClient

client = MLXClient.from_env()
folder_id = os.environ["MULTILOGIN_FOLDER_ID"]
profile_id = os.environ["MULTILOGIN_PROFILE_ID"]

result = client.start_profile(
    folder_id,
    profile_id,
    automation_type=os.getenv("MULTILOGIN_AUTOMATION_TYPE", "playwright"),
    headless=False,
)

port = result["data"]["port"]
print(f"Profile running — connect Playwright to port {port}")
```

CLI: `python scripts/python/launch_profile.py`

[Endpoint doc](../../endpoints/start-browser-profile.md) · [Cookbook](../../cookbook/01-playwright-full-session.md)
