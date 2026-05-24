# Multilogin X API Authentication

## Bearer token

```http
Authorization: Bearer YOUR_TOKEN
Accept: application/json
```

## Flow

1. `POST /user/signin` → token + refresh_token
2. Or `GET /workspace/automation_token` for long-lived automation
3. Refresh: `POST /user/refresh_token` (30 min regular token TTL)

## .env

```
MULTILOGIN_TOKEN=
MULTILOGIN_REFRESH_TOKEN=
MULTILOGIN_FOLDER_ID=
MULTILOGIN_PROFILE_ID=
MULTILOGIN_LAUNCHER_URL=https://launcher.mlx.yt:45001
```

Client: [lib/mlx_client.py](../../lib/mlx_client.py)

[https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
