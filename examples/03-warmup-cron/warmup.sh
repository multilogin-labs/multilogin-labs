#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."

# load env
if [ -f .env ]; then
  set -a; . .env; set +a
fi

PROFILES="${WARMUP_PROFILES:?Set WARMUP_PROFILES=ID1,ID2,ID3}"
FOLDER="${MULTILOGIN_FOLDER_ID:?Set MULTILOGIN_FOLDER_ID}"

node tools/warmup-scheduler.mjs \
  --profiles "$PROFILES" \
  --folder "$FOLDER" \
  --interval 600 \
  --jitter 180 \
  --duration 25 \
  >> warmup.log 2>&1
