# Multilogin X API — one-page cheatsheet

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

## Base URLs

| Service | URL |
|---|---|
| Cloud API | `https://api.multilogin.com` |
| Launcher | `https://launcher.mlx.yt:45001` |

## Auth

```http
POST /user/signin
Authorization: Bearer <token>
```

Use **automation token** for scripts — [guide](../guides/multilogin-automation-token.md).

## Start / stop (Launcher)

```http
GET /api/v2/profile/f/{folder_id}/p/{profile_id}/start?automation_type=playwright
GET /api/v1/profile/stop?profile_id={profile_id}
```

## Quick profile (v3)

```http
POST /v3/profile/quick
```

## Search profiles

```http
POST /v2/profile/search
```

## CLI in this repo

```bash
npm run api:search -- start
python scripts/python/signin.py
python scripts/python/launch_profile.py
```

Full index: [endpoints-index.md](endpoints-index.md) · [90 pages](endpoints/) · [cookbook ×30](cookbook/README.md)
