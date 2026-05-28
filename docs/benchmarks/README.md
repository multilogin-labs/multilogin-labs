# Benchmarks — public CSV results

Run the [benchmark](../../tools/benchmark.mjs) on your machine and submit a CSV PR.

```bash
export MULTILOGIN_TOKEN=...
export MULTILOGIN_FOLDER_ID=...
export MULTILOGIN_PROFILE_ID=...
node tools/benchmark.mjs --runs 5
```

Each run produces `docs/benchmarks/<timestamp>.csv` with columns:

| run | step | ms | ok | err |
|---|---|---|---|---|

## Steps measured

| Step | Description |
|---|---|
| `start` | Launcher `GET /api/v2/profile/f/.../p/.../start` |
| `playwright_connect` | Connect to CDP port (skipped if Playwright not installed) |
| `stop` | Launcher `GET /api/v1/profile/stop?profile_id=...` |

## Submit your run

1. Run with at least 5 iterations.
2. Anonymize: don't include profile UUIDs in the filename.
3. PR adding the CSV — title `bench: <CPU/OS/connection>`.
4. We'll merge after review and aggregate quarterly.

## Aggregated public results

| Hardware | OS | Connection | Median start (ms) | Median stop (ms) | CSV |
|---|---|---|---|---|---|
| _your run_ | _macOS / Win / Linux_ | _broadband / mobile_ | _?_ | _?_ | _link_ |

See [docs/benchmarks.md](../benchmarks.md) for documented baseline ranges.
