# Building a 100-profile agency stack with Multilogin

> 2026-05-25 · [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

Reference architecture for a 100-profile, 5-operator agency. Diagrams in [docs/architecture.md](../architecture.md).

## Workspace shape

- 1 workspace per agency entity (billing, audit).
- 1 folder per client.
- Tags: `client-<slug>`, `platform-<name>`, `geo-<cc>`, `status-<warmup|active|cooldown>`.

## Plan

- **Pro 100** with annual billing (~35% discount). Run [`npm run plan -- --profiles 100 --team 5 --mobile`](../../tools/plan-calculator.mjs).
- Use **automation token** for all CI/cron — never sign-in tokens for scripts.

## Roles

| Operator | Folder access | Allowed tools |
|---|---|---|
| Lead | All folders | Workspace admin |
| Senior | Multiple clients | Mimic + cloud phone + API |
| Junior | One client | Mimic only |
| Auditor | All folders, read-only | Profile search |
| Bot | All folders, automation token | Scripts only |

## Daily flow

1. Cron triggers [warmup scheduler](../../tools/warmup-scheduler.mjs) on `tag:warmup`.
2. Senior operator runs campaign via [Playwright cookbook 01](../api/cookbook/01-playwright-full-session.md).
3. Bot exports profile statuses via [cookbook 56](../api/cookbook/56-csv-export-status.md) → Slack channel.
4. Anomalies trigger [cookbook 53/54](../api/cookbook/53-slack-alerting.md) Slack/Discord webhooks.

## Safety rails

- **No shared credentials** — every operator has their own seat.
- **Webhook on stop_all** — alerts the lead when emergency stop fires.
- **Quarterly key rotation** — automation token re-issued every 90 days.

[← Blog index](README.md) · [Agency setup guide](../guides/multilogin-agency-setup.md)
