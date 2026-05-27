#!/usr/bin/env bash
# One-command doc regeneration
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/upgrade_repo.py
python3 tools/generate_sitemap.mjs 2>/dev/null || node tools/generate_sitemap.mjs
echo "Done. Markdown count: $(find docs -name '*.md' | wc -l | tr -d ' ')"
