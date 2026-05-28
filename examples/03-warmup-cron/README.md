# Example 03 · Warmup via cron

```bash
crontab -e
# Run warmup wave Mon-Fri 09:00 local time
0 9 * * 1-5 /path/to/warmup.sh
```

See [cookbook 51](../../docs/api/cookbook/51-scheduled-warmup-cron.md).
