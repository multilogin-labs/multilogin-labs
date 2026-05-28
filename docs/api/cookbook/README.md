# Multilogin X API Cookbook


**80 recipes**

| # | Recipe |
|---|---|
| 01 | [01-playwright-full-session](01-playwright-full-session.md) |
| 02 | [02-quick-profile-scrape](02-quick-profile-scrape.md) |
| 03 | [03-bulk-profile-search](03-bulk-profile-search.md) |
| 04 | [04-create-profile-with-proxy](04-create-profile-with-proxy.md) |
| 05 | [05-automation-token-setup](05-automation-token-setup.md) |
| 06 | [06-clone-profile-farm](06-clone-profile-farm.md) |
| 07 | [07-stop-all-emergency](07-stop-all-emergency.md) |
| 08 | [08-selenium-grid-style](08-selenium-grid-style.md) |
| 09 | [09-import-cookies](09-import-cookies.md) |
| 10 | [10-export-cookies](10-export-cookies.md) |
| 11 | [11-workspace-folders](11-workspace-folders.md) |
| 12 | [12-profile-export-migrate](12-profile-export-migrate.md) |
| 13 | [13-generate-multilogin-proxy](13-generate-multilogin-proxy.md) |
| 14 | [14-script-runner](14-script-runner.md) |
| 15 | [15-unlock-profile](15-unlock-profile.md) |
| 16 | [16-active-profiles-status](16-active-profiles-status.md) |
| 17 | [17-refresh-token-cron](17-refresh-token-cron.md) |
| 18 | [18-playwright-headless](18-playwright-headless.md) |
| 19 | [19-profile-partial-update](19-profile-partial-update.md) |
| 20 | [20-bulk-stop-and-restart](20-bulk-stop-and-restart.md) |
| 21 | [21-delete-profile-cleanup](21-delete-profile-cleanup.md) |
| 22 | [22-search-profiles-by-tag](22-search-profiles-by-tag.md) |
| 23 | [23-test-proxy-connection](23-test-proxy-connection.md) |
| 24 | [24-signin-and-refresh-token](24-signin-and-refresh-token.md) |
| 25 | [25-parallel-playwright-sessions](25-parallel-playwright-sessions.md) |
| 26 | [26-quick-profile-one-shot](26-quick-profile-one-shot.md) |
| 27 | [27-move-profile-folder](27-move-profile-folder.md) |
| 28 | [28-update-profile-metadata](28-update-profile-metadata.md) |
| 29 | [29-launcher-health-check](29-launcher-health-check.md) |
| 30 | [30-full-session-restart-loop](30-full-session-restart-loop.md) |

[API hub](../README.md)
| 31 | [31-webhook-style-polling.md](31-webhook-style-polling.md) |
| 32 | [32-batch-create-ten-profiles.md](32-batch-create-ten-profiles.md) |
| 33 | [33-export-profile-list-csv.md](33-export-profile-list-csv.md) |
| 34 | [34-rotate-proxy-on-profile.md](34-rotate-proxy-on-profile.md) |
| 35 | [35-playwright-screenshot-audit.md](35-playwright-screenshot-audit.md) |
| 36 | [36-selenium-parallel-grid.md](36-selenium-parallel-grid.md) |
| 37 | [37-puppeteer-stealth-connect.md](37-puppeteer-stealth-connect.md) |
| 38 | [38-2fa-signin-script.md](38-2fa-signin-script.md) |
| 39 | [39-workspace-member-invite.md](39-workspace-member-invite.md) |
| 40 | [40-disaster-recovery-stop-all.md](40-disaster-recovery-stop-all.md) |
| 41 | [Audit cookies across many profiles](41-audit-cookies-bulk.md) |
| 42 | [Multi-tab Playwright workflow](42-playwright-multi-tab.md) |
| 43 | [Screenshot grid for QA](43-puppeteer-screenshot-grid.md) |
| 44 | [Selenium explicit waits pattern](44-selenium-explicit-wait.md) |
| 45 | [Record + replay session events](45-session-replay-record.md) |
| 46 | [Run anti-bot tests on a profile](46-anti-bot-test-loop.md) |
| 47 | [Captcha solver integration shape](47-captcha-solver-hookin.md) |
| 48 | [Cookie jar rotation helper](48-cookie-jar-export-rotate.md) |
| 49 | [Proxy failover and retry logic](49-proxy-failover.md) |
| 50 | [Bulk rename tags across profiles](50-bulk-tag-rename.md) |
| 51 | [Scheduled warmup with cron](51-scheduled-warmup-cron.md) |
| 52 | [Prometheus metrics exporter shape](52-metrics-prometheus-exporter.md) |
| 53 | [Slack alert on profile errors](53-slack-alerting.md) |
| 54 | [Discord webhook for status pings](54-discord-alerting.md) |
| 55 | [Import profiles from CSV](55-csv-import-profiles.md) |
| 56 | [Export profile status to CSV](56-csv-export-status.md) |
| 57 | [Exponential backoff for rate limits](57-ratelimit-backoff.md) |
| 58 | [Rotate 2FA backup codes](58-two-fa-rotate-backup.md) |
| 59 | [Agency onboarding script](59-agency-onboarding-script.md) |
| 60 | [Self-hosted CI runner pattern](60-self-hosted-runner-pattern.md) |
| 61 | [Run warmup from GitHub Actions cron](61-github-actions-cron.md) |
| 62 | [Hand off Playwright codegen to a profile](62-playwright-codegen-handoff.md) |
| 63 | [Minimal Go client snippet](63-go-client-snippet.md) |
| 64 | [Minimal Rust client snippet](64-rust-client-snippet.md) |
| 65 | [k6 load test against Launcher](65-k6-load-test.md) |
| 66 | [Mock MLX client for Vitest](66-vitest-mock-mlx.md) |
| 67 | [Pytest fixtures for Multilogin tests](67-pytest-fixtures.md) |
| 68 | [Send timings to Datadog](68-datadog-metrics.md) |
| 69 | [Capture errors to Sentry](69-sentry-error-capture.md) |
| 70 | [Use Ofelia for Docker-native cron](70-ofelia-docker-cron.md) |
| 71 | [Vercel cron triggers warmup](71-vercel-cron-warmup.md) |
| 72 | [Cloudflare Worker proxies search](72-cloudflare-worker-search.md) |
| 73 | [n8n workflow that watches profile errors](73-n8n-workflow.md) |
| 74 | [Make.com scenario blueprint](74-make-com-scenario.md) |
| 75 | [Zapier zap for new-profile alerts](75-zapier-zap.md) |
| 76 | [Sync profile metadata to Supabase](76-supabase-sync.md) |
| 77 | [Sync profile metadata to Airtable](77-airtable-sync.md) |
| 78 | [Mirror profiles into a Notion database](78-notion-sync.md) |
| 79 | [OpenTelemetry traces for profile ops](79-telemetry-opentelemetry.md) |
| 80 | [Plug rotating residential proxy provider](80-rotating-residential-proxy.md) |
