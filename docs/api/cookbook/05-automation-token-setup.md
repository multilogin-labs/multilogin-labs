# Recipe: Automation token for production scripts

Regular sign-in tokens expire in ~30 minutes. Use **automation token** for cron/CI.

## Get token

`GET https://api.multilogin.com/workspace/automation_token`

Requires existing Bearer auth (sign-in once).

## Python

```python
from lib.mlx_client import MLXClient

# After signin once:
session = MLXClient.signin("email", "password")
auto = MLXClient.automation_token(session.token)
print("Save to .env:", auto.token)
```

## Store in `.env`

```env
MULTILOGIN_TOKEN=automation_token_here
```

Never commit tokens. Add `.env` to `.gitignore` (already done).

[workspace-automation-token](../endpoints/workspace-automation-token.md) · [authentication](../authentication.md)
