# Recipe: Search profiles in workspace

`POST https://api.multilogin.com/profile/search`

```python
from lib.mlx_client import MLXClient

client = MLXClient.from_env()
result = client.profile_search({
    "search_text": "",
    "limit": 100,
    "offset": 0,
})
for p in result.get("data", {}).get("profiles", []):
    print(p.get("id"), p.get("name"))
```

[profile-search.md](../endpoints/profile-search.md)
