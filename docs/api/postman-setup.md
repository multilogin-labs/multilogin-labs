# Multilogin X API — Postman Setup

> Official collection: [Postman Documenter](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)

## Steps

1. Install [Postman](https://www.postman.com/downloads/)
2. Open the [Multilogin X API collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)
3. Click **Run in Postman** (if available) or import from Multilogin support
4. Create environment variables:
   - `token` — Bearer token or automation token
   - `folder_id` — profile folder UUID
   - `profile_id` — profile UUID
   - `launcher_url` — `https://launcher.mlx.yt:45001`

## First requests

| Order | Request | Purpose |
|---|---|---|
| 1 | User Sign In | Get token |
| 2 | Workspace Automation Token | Long-lived automation |
| 3 | Start Browser Profile | Launch + get port |
| 4 | Stop Browser Profile | Clean shutdown |

## Mirror in this repo

Every Postman endpoint has a page: [endpoints-index.md](endpoints-index.md)

Community docs: [reference-full.md](reference-full.md) · [cookbook/](cookbook/)

## Low-code guides (Multilogin official)

- [Start profile with Postman](https://multilogin.com/help/starting-a-profile-with-postman)
- [Stop profile with Postman](https://multilogin.com/help/en_US/stopping-a-profile-with-postman)
- [API beginners guide](https://multilogin.com/help/en_US/multilogin-x-api-beginners-guide)

[Partner pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
