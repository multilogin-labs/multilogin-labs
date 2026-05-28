# Architecture — Multilogin Labs stack

> [Partner pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · Codes **SAAS50** · **MIN50**

How a typical multi-account operation is wired with Multilogin.

## High-level

```mermaid
flowchart LR
  subgraph User["Your machine / VPS"]
    Script["Python / Node script\n(scripts/, lib/mlx_client.*)"]
    App["Multilogin desktop"]
    Launcher["Launcher API\nlauncher.mlx.yt:45001"]
    App --- Launcher
    Script -- "REST" --> Launcher
  end

  subgraph Cloud["Multilogin cloud"]
    Auth["Auth & Workspace\napi.multilogin.com"]
    Phone["Cloud phone\nAndroid 12–14"]
    Proxy["Built-in proxy\nresidential / mobile"]
  end

  Script -- "Bearer JWT" --> Auth
  Launcher -- "Profile assets" --> Auth
  Launcher -- "Run mobile flows" --> Phone
  Launcher -- "Egress" --> Proxy

  subgraph Targets["Target platforms"]
    TikTok
    Meta
    Amazon
    Stripe["Stripe / CEX"]
  end

  Proxy --> TikTok
  Proxy --> Meta
  Proxy --> Amazon
  Phone --> TikTok
  Phone --> Stripe
```

## Authentication flow

```mermaid
sequenceDiagram
  participant Dev as Developer script
  participant Auth as api.multilogin.com
  participant Launcher as launcher.mlx.yt:45001
  participant Browser as Profile (Mimic / Stealthfox)

  Dev->>Auth: POST /user/signin (email, password, 2FA)
  Auth-->>Dev: token (JWT)
  Note over Dev,Auth: Or use long-lived automation token

  Dev->>Launcher: GET /api/v2/profile/f/{folder}/p/{profile}/start<br>Authorization: Bearer <token>
  Launcher-->>Dev: { port, status }
  Dev->>Browser: Connect Playwright/Puppeteer to CDP port
  Browser-->>Dev: Page interactions
  Dev->>Launcher: GET /api/v1/profile/stop?profile_id=...
```

## Profile lifecycle

```mermaid
stateDiagram-v2
  [*] --> Created
  Created --> Configured: assign proxy + fingerprint
  Configured --> Warmup: organic activity 3-7 days
  Warmup --> Active: ready for monetization
  Active --> Active: daily sessions via API
  Active --> Cooldown: temp restriction
  Cooldown --> Active: rotate proxy / wait
  Active --> Retired: account banned / no longer used
  Retired --> [*]
```

## Recommended folder structure for agencies

```mermaid
flowchart TD
  WS["Workspace (Business plan)"] --> F1["folder: client-acme"]
  WS --> F2["folder: client-globex"]
  WS --> F3["folder: internal-test"]
  F1 --> P1["TikTok shop\n(cloud phone)"]
  F1 --> P2["Meta Ads BM\n(Mimic + residential)"]
  F1 --> P3["Amazon seller\n(Mimic + sticky residential)"]
  F2 --> P4["Etsy shops\n(Mimic + ISP proxy)"]
```

## Data flow for warmup scheduler

```mermaid
sequenceDiagram
  participant CLI as warmup-scheduler.mjs
  participant Launcher
  participant Profiles as N profiles

  CLI->>CLI: jitter wait (interval ± jitter)
  loop For each profile
    CLI->>Launcher: start profile
    Launcher-->>CLI: ok
    Note over CLI: setTimeout(stop, duration)
  end
  CLI-->>Launcher: stop on schedule (per profile)
```

## See also

- [API CHEATSHEET](api/CHEATSHEET.md) · [Quick start](api/quick-start.md) · [Swagger UI](api/swagger.html)
- [Cookbook ×40](api/cookbook/README.md) · [Comparison matrix](comparisons/comparison-matrix.md)
