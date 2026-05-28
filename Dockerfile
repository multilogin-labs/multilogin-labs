# Multilogin Labs sandbox — runs scripts and tools, NOT Multilogin desktop.
# Multilogin app must run on host or another container with a desktop env.
FROM node:20-bookworm-slim AS node-base

ENV PYTHONUNBUFFERED=1 \
    NODE_ENV=production \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv git curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY package.json ./
COPY requirements.txt* ./
RUN npm install --omit=optional --no-audit --no-fund \
 && if [ -f requirements.txt ]; then python3 -m pip install --break-system-packages -r requirements.txt; fi

COPY . .

# Default to printing the help banner. Override with: docker run ... node tools/api-search.mjs ...
CMD ["node", "tools/api-search.mjs"]

LABEL org.opencontainers.image.title="Multilogin Labs" \
      org.opencontainers.image.description="Community automation hub for Multilogin antidetect & cloud phone." \
      org.opencontainers.image.source="https://github.com/multilogin-labs/multilogin-labs" \
      org.opencontainers.image.url="https://multilogin-labs.github.io/multilogin-labs/" \
      org.opencontainers.image.licenses="MIT"
