# mlx-telegram-bot

Telegram bot for Multilogin X API search.

```bash
cd integrations/telegram-bot
npm install
TELEGRAM_BOT_TOKEN=... npm start
```

## Commands

- `/start` — intro + buttons (trial, Swagger, hub)
- `/search profile start` — top 8 matching endpoints
- `/cheatsheet`, `/plan`, `/trial`

## Deploy

- Cloudflare Workers (rewrite to Webhook mode).
- Fly.io / Railway / Render — free tiers fit the load.
- Self-hosted via systemd — see [examples/03-warmup-cron](../../examples/03-warmup-cron/).

[Discord bot](../discord-bot/) · [Cloudflare Worker](../cloudflare-worker/)
