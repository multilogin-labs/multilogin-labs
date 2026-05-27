# Recipe: Selenium over Multilogin CDP port

Same pattern as Playwright — start profile with `automation_type=selenium`, use returned port.

```bash
python scripts/python/launch_profile.py
# MULTILOGIN_AUTOMATION_TYPE=selenium in .env
export MULTILOGIN_DEBUG_PORT=<port from response>
python scripts/python/selenium_connect.py
```

[start-browser-profile.md](../endpoints/start-browser-profile.md)
