# Multilogin X API — Full Reference

> Community mirror · [Official Postman](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)

# Multilogin X API Documentation

## Table of Contents

- [Introduction](#introduction)
- [Authentication](#authentication)
- [Endpoints Overview](#endpoints-overview)
- [Request and Response Format](#request-and-response-format)
- [Error Handling](#error-handling)
- [API Reference](#api-reference)
  - [Launcher](#launcher)
  - [Profile Access Management](#profile-access-management)
  - [Profile Management](#profile-management)
  - [Browser Profile Data](#browser-profile-data)
  - [Proxy](#proxy)
  - [Pre-made Cookies](#pre-made-cookies)
  - [Script Runner](#script-runner)
  - [Profile Import/Export](#profile-importexport)
  - [Object Storage](#object-storage)
  - [Bookmark Management](#bookmark-management)
  - [2FA](#2fa)

## Introduction

Welcome to the Multilogin X API documentation. This documentation serves to explain how to automate Multilogin X API endpoints by using scripts, bots and automation in general.

Our API enables users and developers to programmatically manage browser profiles, perform actions such as creating, modifying, or deleting profiles, and retrieve data related to profile usage, activity etc.

## Authentication

Most of the API requests must be authenticated using Bearer Token. You can generate Bearer Token by signing in or refreshing it when needed.

The regular token has 30 minutes of lifetime. Upon expiration, you may refresh it with `POST /user/refresh_token` to obtain a new one.

To have higher rate limits and a longer token lifetime, it is recommended to get the [automation token](#workspace-automation-token).

## Endpoints Overview

The Multilogin X API provides endpoints for various actions divided into the following categories:

- **Base URL**: api.multilogin.com
- **Launcher:** Start, stop, get basic information about browser profiles.
- **Profile Management:** Create, update, delete, browser profiles.
- **Profile Access Management**: Sign in, manage your password and token, get basic information on workspaces.
- **Browser Profile Data:** Unlock browser profiles.

## Request and Response Format

The API accepts JSON-formatted requests and returns responses in JSON format.

## Error Handling

The API follows standard HTTP status codes to indicate the success or failure of requests. Error responses include error messages to assist in troubleshooting.

Errors are categorized into the following groups:

1. **Client Errors (4xx):** These errors occur when there is an issue with the client's request, such as invalid parameters or unauthorized access.
   - **400 Bad Request:** The request was invalid or malformed. Check the request parameters and try again. This type typically relates to wrong or invalid data being sent.
   - **401 Unauthorized:** Authentication credentials are missing or invalid. Ensure you are using valid credentials and tokens.
   - **403 Forbidden:** The user does not have permission to access the requested resource.
   - **429 Too Many Request:** The error indicates that the user has sent too many requests in a given amount of time exceeding the rate limit.

2. **Server Errors (5xx):** These errors occur when there is an issue on the server side, such as internal server errors or service unavailable.
   - **500 Internal Server Error:** An unexpected error occurred on the server side. This may happen when the server cannot process your request due to multiple technical reasons. Wrong payloads or inconsistent data sent can also raise this error. Contact support if the issue persists.

For more information on using the Multilogin X API, please refer to the API documentation with code examples or navigate to our [support page](https://help.multilogin.com/en_US/multilogin-x).

Have feedback to share? Take a minute to fill in this quick [survey](https://tally.so/r/nWABkk).

---

## API Reference

### Launcher

For automation users, if you need the agent to be launched automatically every time you restart your device, here is [the article](https://help.multilogin.com/en_US/launchers/how-to-make-the-multilogin-x-agent-auto-launch) from our support knowledge on how to make it happen.

#### Start Browser Profile

**GET** `https://launcher.mlx.yt:45001/api/v2/profile/f/:folder_id/p/:profile_id/start`

This endpoint supports both Strict and Non-Strict modes. In Strict mode, all required parameters must be explicitly specified. In contrast, Non-Strict mode allows for faster usage by applying default values to any unspecified parameters.

Start a browser profile. The endpoint will return a port for automation in the response message if the automation type parameter is passed.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json
- `X-Strict-Mode`: boolean (Default to false)

**Query Parameters**:
- `automation_type`: selenium, puppeteer, playwright (Optional, defaults to selenium)
- `headless_mode`: false, true (Optional, defaults to false)

**Path Variables**:
- `folder_id`: uuid (Required)
- `profile_id`: uuid (Required)

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v2/profile/f/81b5627a-1212-4016-9467-3dbe4d6f78eb/p/81b5627a-1212-4016-9467-3dbe4d6f78eb/start?automation_type=puppeteer&headless_mode=false' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "browser_type": "mimic",
    "core_version": 132,
    "id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
    "is_quick": false,
    "port": "55513"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile started successfully"
  }
}
```

#### Start Quick Profile v3

**POST** `https://launcher.mlx.yt:45001/api/v3/profile/quick`

Create a one-time quick browser profile that opens up after the call is successfully made. Browsing activity and its related data is not saved after the profile has been stopped.

This endpoint supports both Strict and Non-Strict modes. Fingerprint parameters need providing only if flags set to `Custom`.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json
- `X-Strict-Mode`: boolean (Default to false)

**Request Body Parameters**:

Required parameters:
- `browser_type`: "mimic", "stealthfox" (Required, defaults to mimic)
- `os_type`: "linux", "macos", "windows", "android" (Required, defaults to windows)
- `parameters`: Object containing flags, fingerprints, storage, proxy, custom_start_urls

Optional parameters:
- `core_version`: number (defaults to latest)
- `core_minor_version`: number
- `automation`: "selenium"
- `is_headless`: boolean (defaults to false)
- `script_file`: string (for Script Runner)

**Flags** (required in parameters):
- `webrtc_masking`: "natural", "custom", "mask", "disabled"
- `proxy_masking`: "custom", "disabled"
- `geolocation_popup`: "prompt", "allow", "block"
- `audio_masking`: "mask", "natural"
- `graphics_noise`: "mask", "natural"
- `navigator_masking`: "natural", "custom", "mask"
- `localization_masking`: "natural", "custom", "mask"
- `timezone_masking`: "natural", "custom", "mask"
- `graphics_masking`: "natural", "custom", "mask"
- `fonts_masking`: "natural", "custom", "mask"
- `media_devices_masking`: "natural", "custom", "mask"
- `screen_masking`: "natural", "custom", "mask"
- `ports_masking`: "natural", "custom", "mask"
- `geolocation_masking`: "custom", "mask"
- `canvas_noise`: "mask", "natural", "disabled" (optional)
- `startup_behavior`: "recover", "custom" (optional)

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v3/profile/quick' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "browser_type": "mimic",
  "core_version": 124,
  "os_type": "linux",
  "script_file": "example_script3.py",
  "automation": "selenium",
  "is_headless": false,
  "parameters": {
    "flags": {
      "audio_masking": "mask",
      "fonts_masking": "custom",
      "geolocation_masking": "custom",
      "geolocation_popup": "prompt",
      "graphics_masking": "custom",
      "graphics_noise": "mask",
      "localization_masking": "custom",
      "media_devices_masking": "custom",
      "navigator_masking": "custom",
      "ports_masking": "mask",
      "proxy_masking": "custom",
      "screen_masking": "custom",
      "timezone_masking": "custom",
      "webrtc_masking": "custom",
      "canvas_noise": "custom",
      "startup_behavior": "custom"
    },
    "fingerprint": {
      "navigator": {
        "hardware_concurrency": 8,
        "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
      },
      "localization": {
        "languages": "en-US",
        "locale": "en-US",
        "accept_languages": "en-US,en;q=0.5"
      },
      "timezone": {
        "zone": "Asia/Bangkok"
      },
      "graphic": {
        "renderer": "ANGLE (NVIDIA, NVIDIA GeForce RTX 4070 Ti Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "vendor": "Google Inc. (NVIDIA)"
      },
      "webrtc": {
        "public_ip": "123.123.123.123"
      },
      "media_devices": {
        "audio_inputs": 1,
        "audio_outputs": 1,
        "video_inputs": 2
      },
      "screen": {
        "height": 1200,
        "pixel_ratio": 1,
        "width": 1920
      },
      "geolocation": {
        "accuracy": 100,
        "altitude": 100,
        "latitude": 52.02,
        "longitude": -52.1
      }
    },
    "proxy": {
      "host": "host.com",
      "type": "http",
      "port": 8081,
      "username": "username",
      "password": "password",
      "save_traffic": true
    },
    "custom_start_urls": [
      "https://jsonformatter.org/",
      "https://python.org/"
    ]
  }
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "browser_type": "mimic",
    "core_version": 132,
    "id": "d04aa438-d887-11ef-8d6d-0a0027000012",
    "is_quick": true,
    "port": "55579"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Quick profile started successfully"
  }
}
```

#### Start Quick Profile (Deprecated)

**POST** `https://launcher.mlx.yt:45001/api/v2/profile/quick`

> **Note**: To be deprecated. Use Start Quick Profile v3 for starting quick browser profiles.

#### Stop Browser Profile

**GET** `https://launcher.mlx.yt:45001/api/v1/profile/stop`

Stop a browser profile by profile ID.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `profile_id`: uuid (Required)

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/profile/stop?profile_id=81b5627a-1212-4016-9467-3dbe4d6f78eb' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile stopped successfully"
  }
}
```

#### Stop All Profiles

**GET** `https://launcher.mlx.yt:45001/api/v1/profile/stop_all`

Stop all running browser profiles.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/profile/stop_all' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "stopped_profiles": [
      "81b5627a-1212-4016-9467-3dbe4d6f78eb",
      "92c6738b-2323-5127-9578-4ecf5e7f89fc"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "All profiles stopped successfully"
  }
}
```

#### Get Version

**GET** `https://launcher.mlx.yt:45001/api/v1/version`

Get the version of the launcher.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/version' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "version": "1.9.0"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Version retrieved successfully"
  }
}
```

#### Get Profile Status

**GET** `https://launcher.mlx.yt:45001/api/v1/profile/active`

Get the status of a specific browser profile.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `profile_id`: uuid (Required)

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/profile/active?profile_id=81b5627a-1212-4016-9467-3dbe4d6f78eb' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
    "is_active": true,
    "port": "55513"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile status retrieved successfully"
  }
}
```

#### Get All Profiles Status

**GET** `https://launcher.mlx.yt:45001/api/v2/profile/active`

Get the status of all browser profiles.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v2/profile/active' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profiles": [
      {
        "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
        "is_active": true,
        "port": "55513"
      },
      {
        "profile_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
        "is_active": false
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "All profiles status retrieved successfully"
  }
}
```

#### Get All Quick Profiles Status

**GET** `https://launcher.mlx.yt:45001/api/v1/quick-profiles/active`

Get the status of all quick browser profiles.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/quick-profiles/active' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "quick_profiles": [
      {
        "profile_id": "temp_12345",
        "is_active": true,
        "port": "55514"
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Quick profiles status retrieved successfully"
  }
}
```

#### Loaded Browser Cores

**GET** `https://launcher.mlx.yt:45001/api/v1/core/loaded`

Get information about loaded browser cores.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/core/loaded' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "cores": [
      {
        "browser_type": "mimic",
        "version": 132,
        "is_loaded": true
      },
      {
        "browser_type": "stealthfox",
        "version": 130,
        "is_loaded": true
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Loaded cores retrieved successfully"
  }
}
```

#### Browser Core List

**GET** `https://launcher.mlx.yt:45001/api/v1/core/list`

Get list of available browser cores.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/core/list' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "cores": [
      {
        "browser_type": "mimic",
        "version": 132,
        "is_available": true
      },
      {
        "browser_type": "stealthfox",
        "version": 130,
        "is_available": true
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Core list retrieved successfully"
  }
}
```

#### Load Browser Core

**GET** `https://launcher.mlx.yt:45001/api/v1/core/load`

Load a specific browser core.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `browser_type`: string (Required)
- `version`: number (Required)

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/core/load?browser_type=mimic&version=132' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "browser_type": "mimic",
    "version": 132,
    "loaded": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Core loaded successfully"
  }
}
```

#### Delete Browser Core

**DELETE** `https://launcher.mlx.yt:45001/api/v1/core`

Delete a specific browser core.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `browser_type`: string (Required)
- `version`: number (Required)

**Example Request**:
```bash
curl --location --request DELETE 'https://launcher.mlx.yt:45001/api/v1/core?browser_type=mimic&version=131' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "browser_type": "mimic",
    "version": 131,
    "deleted": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Core deleted successfully"
  }
}
```

#### Validate Proxy

**POST** `https://launcher.mlx.yt:45001/api/v1/proxy/validate`

Validate proxy configuration.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "host": "proxy.example.com",
  "type": "http",
  "port": 8080,
  "username": "user",
  "password": "pass"
}
```

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/proxy/validate' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "host": "proxy.example.com",
  "type": "http",
  "port": 8080,
  "username": "user",
  "password": "pass"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "is_valid": true,
    "ip": "123.456.789.10",
    "country": "US",
    "city": "New York"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Proxy validated successfully"
  }
}
```

#### Cookie Import

**POST** `https://launcher.mlx.yt:45001/api/v1/cookies/import`

Import cookies into a profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "cookies": [
    {
      "domain": ".example.com",
      "name": "session",
      "value": "abc123",
      "path": "/",
      "httpOnly": true,
      "secure": true
    }
  ]
}
```

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/cookies/import' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "cookies": [
    {
      "domain": ".example.com",
      "name": "session",
      "value": "abc123",
      "path": "/",
      "httpOnly": true,
      "secure": true
    }
  ]
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "imported": 1,
    "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Cookies imported successfully"
  }
}
```

#### Cookie Export

**POST** `https://launcher.mlx.yt:45001/api/v1/cookies/export`

Export cookies from a profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
}
```

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/cookies/export' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "cookies": [
      {
        "domain": ".example.com",
        "name": "session",
        "value": "abc123",
        "path": "/",
        "httpOnly": true,
        "secure": true,
        "expirationDate": 1735689600
      }
    ],
    "profile_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Cookies exported successfully"
  }
}
```

#### Convert QBP to Profile

**POST** `https://launcher.mlx.yt:45001/api/v1/profile/convert_qbp`

Convert a Quick Browser Profile to a regular profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "qbp_id": "temp_12345",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "profile_name": "Converted Profile"
}
```

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/profile/convert_qbp' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "qbp_id": "temp_12345",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "profile_name": "Converted Profile"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profile_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
    "profile_name": "Converted Profile",
    "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "QBP converted successfully"
  }
}
```

#### Get QBP Status

**GET** `https://launcher.mlx.yt:45001/api/v1/profile/qbp_status`

Get status of a Quick Browser Profile.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `qbp_id`: string (Required)

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v1/profile/qbp_status?qbp_id=temp_12345' \
--header 'Accept: application/json'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "qbp_id": "temp_12345",
    "is_active": true,
    "port": "55514"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "QBP status retrieved successfully"
  }
}
```

### Profile Access Management

#### User Sign In

**POST** `https://api.multilogin.com/user/signin`

Sign in to get a Bearer token for API authentication.

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/user/signin' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "email": "user@example.com",
  "password": "password123"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
    "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Signed in successfully"
  }
}
```

#### User Refresh Token (Switch Workspace)

**POST** `https://api.multilogin.com/user/refresh_token`

Refresh authentication token or switch workspace.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "workspace_id": "new-workspace-id" // Optional, for switching workspace
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/user/refresh_token' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Token refreshed successfully"
  }
}
```

#### User Revoke Token

**POST** `https://api.multilogin.com/user/revoke_token`

Revoke an authentication token.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/user/revoke_token' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}'
```

**Example Response** (200 OK):
```json
{
  "data": {},
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Token revoked successfully"
  }
}
```

#### User Change Password

**POST** `https://api.multilogin.com/user/change_password`

Change user password.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "current_password": "oldpassword123",
  "new_password": "newpassword456"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/user/change_password' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "current_password": "oldpassword123",
  "new_password": "newpassword456"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {},
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Password changed successfully"
  }
}
```

#### User Workspaces

**GET** `https://api.multilogin.com/user/workspaces`

Get list of user's workspaces.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/user/workspaces' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "workspaces": [
      {
        "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
        "name": "My Workspace",
        "role": "owner",
        "created_at": "2024-01-01T00:00:00Z"
      },
      {
        "workspace_id": "83d7849c-3434-6238-0689-5fdf6f8f90gd",
        "name": "Team Workspace",
        "role": "member",
        "created_at": "2024-01-15T00:00:00Z"
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Workspaces retrieved successfully"
  }
}
```

#### User Token List

**GET** `https://api.multilogin.com/user/tokens`

Get list of active tokens.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/user/tokens' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "tokens": [
      {
        "token_id": "token_123",
        "created_at": "2024-01-01T00:00:00Z",
        "expires_at": "2024-01-01T00:30:00Z",
        "type": "regular"
      },
      {
        "token_id": "token_456",
        "created_at": "2024-01-01T00:00:00Z",
        "expires_at": "2024-12-31T23:59:59Z",
        "type": "automation"
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Tokens retrieved successfully"
  }
}
```

#### Workspace Restrictions

**GET** `https://api.multilogin.com/workspace/restrictions`

Get workspace restrictions and limits.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/workspace/restrictions' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "max_profiles": 1000,
    "max_users": 10,
    "max_folders": 50,
    "features": {
      "automation": true,
      "api_access": true,
      "team_management": true
    }
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Restrictions retrieved successfully"
  }
}
```

#### Workspace Folders

**GET** `https://api.multilogin.com/workspace/folders`

Get all folders in the workspace.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/workspace/folders' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "folders": [
      {
        "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
        "name": "Default",
        "profile_count": 10,
        "created_at": "2024-01-01T00:00:00Z"
      },
      {
        "folder_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
        "name": "Marketing",
        "profile_count": 5,
        "created_at": "2024-01-15T00:00:00Z"
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Folders retrieved successfully"
  }
}
```

#### Workspace Folders For User

**GET** `https://api.multilogin.com/workspace/folders/user`

Get folders accessible by the current user.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/workspace/folders/user' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "folders": [
      {
        "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
        "name": "Default",
        "permissions": ["read", "write", "delete"],
        "profile_count": 10
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "User folders retrieved successfully"
  }
}
```

#### Workspace Statistics

**GET** `https://api.multilogin.com/workspace/statistics`

Get workspace usage statistics.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/workspace/statistics' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "total_profiles": 150,
    "active_profiles": 25,
    "total_users": 5,
    "storage_used_gb": 45.2,
    "api_calls_this_month": 15000
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Statistics retrieved successfully"
  }
}
```

#### Workspace Automation Token

**GET** `https://api.multilogin.com/workspace/automation_token`

Get workspace automation token for extended API access.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/workspace/automation_token' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "automation_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expires_at": "2024-12-31T23:59:59Z",
    "rate_limit": 10000
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Automation token retrieved successfully"
  }
}
```

#### Workspace Create Folder

**POST** `https://api.multilogin.com/workspace/folder/create`

Create a new folder in the workspace.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "name": "New Folder",
  "description": "Folder for new campaigns"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/workspace/folder/create' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "name": "New Folder",
  "description": "Folder for new campaigns"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "folder_id": "93d7849c-3434-6238-0689-5fdf6f8f90gd",
    "name": "New Folder",
    "description": "Folder for new campaigns",
    "created_at": "2024-01-20T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Folder created successfully"
  }
}
```

#### Workspace Update Folder

**POST** `https://api.multilogin.com/workspace/folder/update`

Update folder information.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "folder_id": "93d7849c-3434-6238-0689-5fdf6f8f90gd",
  "name": "Updated Folder Name",
  "description": "Updated description"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/workspace/folder/update' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "folder_id": "93d7849c-3434-6238-0689-5fdf6f8f90gd",
  "name": "Updated Folder Name",
  "description": "Updated description"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "folder_id": "93d7849c-3434-6238-0689-5fdf6f8f90gd",
    "name": "Updated Folder Name",
    "description": "Updated description",
    "updated_at": "2024-01-21T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Folder updated successfully"
  }
}
```

#### Workspace Remove Folders

**POST** `https://api.multilogin.com/workspace/folders/remove`

Remove one or more folders from the workspace.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "folder_ids": [
    "93d7849c-3434-6238-0689-5fdf6f8f90gd",
    "94e8950d-4545-7349-1790-6eef7f9f01he"
  ]
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/workspace/folders/remove' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "folder_ids": [
    "93d7849c-3434-6238-0689-5fdf6f8f90gd"
  ]
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "removed": 1,
    "folder_ids": [
      "93d7849c-3434-6238-0689-5fdf6f8f90gd"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Folders removed successfully"
  }
}
```

#### Workspace Leave

**POST** `https://api.multilogin.com/workspace/leave`

Leave a workspace (for non-owner members).

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/workspace/leave' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {},
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Left workspace successfully"
  }
}
```

### Profile Management

#### Profile Create

**POST** `https://api.multilogin.com/profile/create`

Create a new browser profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "name": "New Profile",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "browser_type": "mimic",
  "os_type": "windows",
  "parameters": {
    "flags": {
      "audio_masking": "mask",
      "fonts_masking": "natural",
      "geolocation_masking": "mask",
      "geolocation_popup": "prompt",
      "graphics_masking": "mask",
      "graphics_noise": "mask",
      "localization_masking": "mask",
      "media_devices_masking": "natural",
      "navigator_masking": "mask",
      "ports_masking": "mask",
      "proxy_masking": "disabled",
      "screen_masking": "mask",
      "timezone_masking": "mask",
      "webrtc_masking": "mask"
    },
    "storage": {
      "bookmarks": true,
      "cookies": true,
      "extensions": true,
      "history": true,
      "local_storage": true,
      "passwords": true
    }
  }
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/create' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "name": "New Profile",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "browser_type": "mimic",
  "os_type": "windows",
  "parameters": {
    "flags": {
      "audio_masking": "mask",
      "fonts_masking": "natural",
      "geolocation_masking": "mask",
      "geolocation_popup": "prompt",
      "graphics_masking": "mask",
      "graphics_noise": "mask",
      "localization_masking": "mask",
      "media_devices_masking": "natural",
      "navigator_masking": "mask",
      "ports_masking": "mask",
      "proxy_masking": "disabled",
      "screen_masking": "mask",
      "timezone_masking": "mask",
      "webrtc_masking": "mask"
    }
  }
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "name": "New Profile",
    "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
    "browser_type": "mimic",
    "os_type": "windows",
    "created_at": "2024-01-22T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile created successfully"
  }
}
```

#### Profile Search

**POST** `https://api.multilogin.com/profile/search`

Search for profiles based on criteria.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "limit": 10,
  "offset": 0,
  "search_text": "marketing",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "browser_type": "mimic",
  "sort_by": "created_at",
  "sort_order": "desc"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/search' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "limit": 10,
  "offset": 0,
  "search_text": "marketing"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profiles": [
      {
        "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
        "name": "Marketing Profile 1",
        "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
        "browser_type": "mimic",
        "os_type": "windows",
        "created_at": "2024-01-22T00:00:00Z",
        "last_used": "2024-01-23T10:00:00Z"
      }
    ],
    "total": 1,
    "limit": 10,
    "offset": 0
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profiles found successfully"
  }
}
```

#### Profile Remove

**POST** `https://api.multilogin.com/profile/remove`

Remove one or more profiles.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ],
  "permanently": false
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/remove' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ],
  "permanently": false
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "removed": 1,
    "profile_ids": [
      "95f9061e-5656-845a-2801-7fff8f0f12if"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profiles removed successfully"
  }
}
```

#### Profile Update

**POST** `https://api.multilogin.com/profile/update`

Update profile information and settings.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "name": "Updated Profile Name",
  "parameters": {
    "flags": {
      "proxy_masking": "custom"
    },
    "proxy": {
      "host": "new-proxy.example.com",
      "type": "http",
      "port": 8080,
      "username": "user",
      "password": "pass"
    }
  }
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/update' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "name": "Updated Profile Name"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "name": "Updated Profile Name",
    "updated_at": "2024-01-23T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile updated successfully"
  }
}
```

#### Profile Move

**POST** `https://api.multilogin.com/profile/move`

Move profiles to a different folder.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ],
  "folder_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/move' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ],
  "folder_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "moved": 1,
    "profile_ids": [
      "95f9061e-5656-845a-2801-7fff8f0f12if"
    ],
    "folder_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profiles moved successfully"
  }
}
```

#### Profile Partial Update

**POST** `https://api.multilogin.com/profile/partial_update`

Partially update specific profile settings.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "updates": {
    "name": "Partially Updated Name",
    "notes": "Updated notes"
  }
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/partial_update' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "updates": {
    "name": "Partially Updated Name",
    "notes": "Updated notes"
  }
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "updated_fields": ["name", "notes"],
    "updated_at": "2024-01-23T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile partially updated successfully"
  }
}
```

#### Profile Restore

**POST** `https://api.multilogin.com/profile/restore`

Restore previously deleted profiles.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/restore' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "restored": 1,
    "profile_ids": [
      "95f9061e-5656-845a-2801-7fff8f0f12if"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profiles restored successfully"
  }
}
```

#### Profile Metas

**POST** `https://api.multilogin.com/profile/metas`

Get metadata for multiple profiles.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if",
    "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  ]
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/metas' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profiles": [
      {
        "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
        "name": "Profile Name",
        "browser_type": "mimic",
        "os_type": "windows",
        "created_at": "2024-01-22T00:00:00Z",
        "last_used": "2024-01-23T10:00:00Z",
        "storage_size_mb": 125.5
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile metas retrieved successfully"
  }
}
```

#### Profile Summary

**GET** `https://api.multilogin.com/profile/summary`

Get summary information for a profile.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `profile_id`: uuid (Required)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/summary?profile_id=95f9061e-5656-845a-2801-7fff8f0f12if' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "name": "Profile Name",
    "browser_type": "mimic",
    "os_type": "windows",
    "created_at": "2024-01-22T00:00:00Z",
    "last_used": "2024-01-23T10:00:00Z",
    "total_sessions": 45,
    "total_duration_minutes": 1250,
    "cookies_count": 234,
    "extensions_count": 5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile summary retrieved successfully"
  }
}
```

#### Profile Clone

**POST** `https://api.multilogin.com/profile/clone`

Clone an existing profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "name": "Cloned Profile",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "include_cookies": true,
  "include_extensions": true,
  "include_bookmarks": true
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/clone' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "name": "Cloned Profile",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "original_profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "cloned_profile_id": "96g0172f-6767-956b-3912-8ggg9g1g23jg",
    "name": "Cloned Profile",
    "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile cloned successfully"
  }
}
```

#### Profile Convert

**POST** `https://api.multilogin.com/profile/convert`

Convert profile between different browser types.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "target_browser_type": "stealthfox",
  "keep_original": true
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/convert' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "target_browser_type": "stealthfox",
  "keep_original": true
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "original_profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "converted_profile_id": "97h1283g-7878-067c-4023-9hhh0h2h34kh",
    "target_browser_type": "stealthfox"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile converted successfully"
  }
}
```

#### Screen Resolution

**GET** `https://api.multilogin.com/profile/screen_resolutions`

Get available screen resolutions for profiles.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `os_type`: string (Optional - windows, macos, linux, android)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/screen_resolutions?os_type=windows' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "resolutions": [
      {
        "width": 1920,
        "height": 1080,
        "label": "Full HD"
      },
      {
        "width": 1366,
        "height": 768,
        "label": "HD"
      },
      {
        "width": 2560,
        "height": 1440,
        "label": "QHD"
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Screen resolutions retrieved successfully"
  }
}
```

### Browser Profile Data

#### Unlock Locked Profiles

**GET** `https://api.multilogin.com/profile/unlock`

Unlock profiles that are locked due to unexpected closure.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `profile_ids`: comma-separated string of profile IDs (Optional - unlocks all if not specified)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/unlock?profile_ids=95f9061e-5656-845a-2801-7fff8f0f12if' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "unlocked": 1,
    "profile_ids": [
      "95f9061e-5656-845a-2801-7fff8f0f12if"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profiles unlocked successfully"
  }
}
```

### Proxy

#### Generate Proxy

**POST** `https://api.multilogin.com/proxy/generate`

Generate proxy configuration.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "country": "US",
  "city": "New York",
  "provider": "residential",
  "protocol": "http"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/proxy/generate' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "country": "US",
  "city": "New York",
  "provider": "residential",
  "protocol": "http"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "proxy": {
      "host": "proxy.provider.com",
      "port": 8080,
      "username": "generated_user",
      "password": "generated_pass",
      "type": "http",
      "country": "US",
      "city": "New York"
    }
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Proxy generated successfully"
  }
}
```

#### Fetch Proxy Data

**GET** `https://api.multilogin.com/proxy/data`

Fetch proxy information and validate connectivity.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `host`: string (Required)
- `port`: number (Required)
- `type`: string (Required - http, https, socks5)
- `username`: string (Optional)
- `password`: string (Optional)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/proxy/data?host=proxy.example.com&port=8080&type=http' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "proxy": {
      "host": "proxy.example.com",
      "port": 8080,
      "type": "http",
      "is_active": true,
      "ip": "123.456.789.10",
      "country": "US",
      "city": "New York",
      "isp": "Example ISP",
      "latency_ms": 125
    }
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Proxy data fetched successfully"
  }
}
```

### Pre-made Cookies

#### Target Website List

**GET** `https://api.multilogin.com/cookies/websites`

Get list of supported websites for pre-made cookies.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/cookies/websites' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "websites": [
      {
        "website_id": "google",
        "name": "Google",
        "domain": ".google.com",
        "available_cookies": 150
      },
      {
        "website_id": "facebook",
        "name": "Facebook",
        "domain": ".facebook.com",
        "available_cookies": 200
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Websites retrieved successfully"
  }
}
```

#### Create Cookies Metadata

**POST** `https://api.multilogin.com/cookies/metadata/create`

Create metadata for cookie templates.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "name": "Social Media Cookies",
  "description": "Cookie set for social media automation",
  "website_ids": ["facebook", "instagram", "twitter"],
  "tags": ["social", "automation"]
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/cookies/metadata/create' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "name": "Social Media Cookies",
  "description": "Cookie set for social media automation",
  "website_ids": ["facebook", "instagram"],
  "tags": ["social", "automation"]
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "metadata_id": "cookie_meta_123",
    "name": "Social Media Cookies",
    "description": "Cookie set for social media automation",
    "website_ids": ["facebook", "instagram"],
    "tags": ["social", "automation"],
    "created_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Cookie metadata created successfully"
  }
}
```

#### Cookies List

**GET** `https://api.multilogin.com/cookies/list`

Get list of available cookie templates.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `website_id`: string (Optional)
- `tag`: string (Optional)
- `limit`: number (Optional)
- `offset`: number (Optional)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/cookies/list?website_id=facebook&limit=10' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "cookies": [
      {
        "cookie_id": "cookie_123",
        "name": "Facebook Aged Account",
        "website_id": "facebook",
        "age_days": 365,
        "quality_score": 95,
        "price": 5.99
      }
    ],
    "total": 1,
    "limit": 10,
    "offset": 0
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Cookies retrieved successfully"
  }
}
```

#### Update Cookies Metadata

**PUT** `https://api.multilogin.com/cookies/metadata/update`

Update cookie template metadata.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "metadata_id": "cookie_meta_123",
  "name": "Updated Social Media Cookies",
  "description": "Updated description",
  "tags": ["social", "automation", "premium"]
}
```

**Example Request**:
```bash
curl --location --request PUT 'https://api.multilogin.com/cookies/metadata/update' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "metadata_id": "cookie_meta_123",
  "name": "Updated Social Media Cookies",
  "tags": ["social", "automation", "premium"]
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "metadata_id": "cookie_meta_123",
    "name": "Updated Social Media Cookies",
    "description": "Updated description",
    "tags": ["social", "automation", "premium"],
    "updated_at": "2024-01-24T12:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Cookie metadata updated successfully"
  }
}
```

### Script Runner

#### Start Browser Profile with Selenium

**GET** `https://launcher.mlx.yt:45001/api/v2/profile/f/:folder_id/p/:profile_id/start?automation_type=selenium&script_file=script.py`

Start a browser profile with Selenium automation and run a script.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Path Variables**:
- `folder_id`: uuid (Required)
- `profile_id`: uuid (Required)

**Query Parameters**:
- `automation_type`: selenium (Required)
- `script_file`: string (Required - name of the script file)
- `headless_mode`: boolean (Optional, defaults to false)

**Example Request**:
```bash
curl --location 'https://launcher.mlx.yt:45001/api/v2/profile/f/81b5627a-1212-4016-9467-3dbe4d6f78eb/p/95f9061e-5656-845a-2801-7fff8f0f12if/start?automation_type=selenium&script_file=automation_script.py' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "browser_type": "mimic",
    "core_version": 132,
    "id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "is_quick": false,
    "port": "55513",
    "script_status": "running",
    "script_file": "automation_script.py"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile started with script runner successfully"
  }
}
```

#### Start Script Runner

**POST** `https://api.multilogin.com/script/start`

Start a script runner session.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "script_content": "from selenium import webdriver\n# Your script here",
  "script_type": "python",
  "parameters": {
    "timeout": 300,
    "headless": false
  }
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/script/start' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "script_content": "from selenium import webdriver\ndriver.get(\"https://example.com\")",
  "script_type": "python"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "session_id": "script_session_123",
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "status": "running",
    "started_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Script started successfully"
  }
}
```

#### Stop Script Runner

**POST** `https://api.multilogin.com/script/stop`

Stop a running script.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "session_id": "script_session_123"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/script/stop' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "session_id": "script_session_123"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "session_id": "script_session_123",
    "status": "stopped",
    "stopped_at": "2024-01-24T00:05:00Z",
    "execution_time_seconds": 300
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Script stopped successfully"
  }
}
```

#### Script List

**GET** `https://api.multilogin.com/script/list`

Get list of available scripts.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `status`: string (Optional - running, completed, failed)
- `limit`: number (Optional)
- `offset`: number (Optional)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/script/list?status=running' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "scripts": [
      {
        "script_id": "script_123",
        "name": "Social Media Automation",
        "type": "python",
        "status": "running",
        "created_at": "2024-01-24T00:00:00Z",
        "last_run": "2024-01-24T10:00:00Z"
      }
    ],
    "total": 1,
    "limit": 10,
    "offset": 0
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Scripts retrieved successfully"
  }
}
```

### Profile Import/Export

#### Profile Export

**POST** `https://api.multilogin.com/profile/export`

Export profiles to a file.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ],
  "format": "mlx",
  "include_cookies": true,
  "include_extensions": true,
  "include_bookmarks": true,
  "password": "optional_encryption_password"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/export' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ],
  "format": "mlx"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "export_id": "export_123",
    "download_url": "https://api.multilogin.com/download/export_123",
    "expires_at": "2024-01-25T00:00:00Z",
    "file_size_mb": 45.2
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Export started successfully"
  }
}
```

#### Export Status by Profile

**GET** `https://api.multilogin.com/profile/export/status`

Get export status for specific profile.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `export_id`: string (Required)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/export/status?export_id=export_123' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "export_id": "export_123",
    "status": "completed",
    "progress": 100,
    "download_url": "https://api.multilogin.com/download/export_123",
    "expires_at": "2024-01-25T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Export status retrieved successfully"
  }
}
```

#### Export Status All

**GET** `https://api.multilogin.com/profile/export/status/all`

Get status of all exports.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/export/status/all' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "exports": [
      {
        "export_id": "export_123",
        "status": "completed",
        "created_at": "2024-01-24T00:00:00Z",
        "profile_count": 1
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "All export statuses retrieved successfully"
  }
}
```

#### Profile Import

**POST** `https://api.multilogin.com/profile/import`

Import profiles from a file.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "file_url": "https://example.com/profiles.mlx",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb",
  "password": "decryption_password_if_needed"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/import' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "file_url": "https://example.com/profiles.mlx",
  "folder_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "import_id": "import_456",
    "status": "processing",
    "total_profiles": 5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Import started successfully"
  }
}
```

#### Import Status by Profile

**GET** `https://api.multilogin.com/profile/import/status`

Get import status for specific import job.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `import_id`: string (Required)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/import/status?import_id=import_456' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "import_id": "import_456",
    "status": "completed",
    "progress": 100,
    "imported_profiles": 5,
    "failed_profiles": 0,
    "profile_ids": [
      "new_profile_1",
      "new_profile_2"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Import status retrieved successfully"
  }
}
```

#### Import Status All

**GET** `https://api.multilogin.com/profile/import/status/all`

Get status of all import jobs.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/profile/import/status/all' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "imports": [
      {
        "import_id": "import_456",
        "status": "completed",
        "created_at": "2024-01-24T00:00:00Z",
        "imported_profiles": 5
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "All import statuses retrieved successfully"
  }
}
```

### Object Storage

#### Upload Object

**POST** `https://api.multilogin.com/storage/upload`

Upload an object to storage.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: multipart/form-data
- `Accept`: application/json

**Form Data**:
- `file`: File (Required)
- `object_type`: string (Required - extension, backup, etc.)
- `profile_id`: uuid (Optional - for profile-specific objects)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/upload' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--form 'file=@"/path/to/file.zip"' \
--form 'object_type="extension"' \
--form 'profile_id="95f9061e-5656-845a-2801-7fff8f0f12if"'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "object_type": "extension",
    "file_name": "extension.zip",
    "file_size_mb": 2.5,
    "upload_url": "https://storage.multilogin.com/obj_789"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object uploaded successfully"
  }
}
```

#### Create and Upload

**POST** `https://api.multilogin.com/storage/create_upload`

Create storage object and get upload URL.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "object_type": "extension",
  "file_name": "my-extension.zip",
  "file_size_bytes": 2621440,
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/create_upload' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "object_type": "extension",
  "file_name": "my-extension.zip",
  "file_size_bytes": 2621440
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "upload_url": "https://upload.multilogin.com/obj_789",
    "upload_method": "PUT",
    "expires_at": "2024-01-24T01:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Upload URL created successfully"
  }
}
```

#### Object Profile Usages

**GET** `https://api.multilogin.com/storage/object/usages`

Get profiles using a specific object.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_id`: string (Required)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/object/usages?object_id=obj_789' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "profiles": [
      {
        "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
        "profile_name": "Marketing Profile 1",
        "attached_at": "2024-01-24T00:00:00Z"
      }
    ],
    "total_usages": 1
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object usages retrieved successfully"
  }
}
```

#### Get List of Object Types

**GET** `https://api.multilogin.com/storage/types`

Get available object types.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/types' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "types": [
      {
        "type_id": "extension",
        "name": "Browser Extension",
        "max_size_mb": 50,
        "allowed_formats": [".zip", ".crx"]
      },
      {
        "type_id": "backup",
        "name": "Profile Backup",
        "max_size_mb": 500,
        "allowed_formats": [".mlx", ".zip"]
      }
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object types retrieved successfully"
  }
}
```

#### Get Statistics for Objects

**GET** `https://api.multilogin.com/storage/statistics`

Get storage usage statistics.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/statistics' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "total_objects": 45,
    "total_size_gb": 12.5,
    "by_type": {
      "extension": {
        "count": 20,
        "size_gb": 2.5
      },
      "backup": {
        "count": 25,
        "size_gb": 10.0
      }
    },
    "storage_limit_gb": 100,
    "usage_percentage": 12.5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Statistics retrieved successfully"
  }
}
```

#### Get Objects Meta

**GET** `https://api.multilogin.com/storage/objects/meta`

Get metadata for multiple objects.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_type`: string (Optional)
- `limit`: number (Optional)
- `offset`: number (Optional)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/objects/meta?object_type=extension&limit=10' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "objects": [
      {
        "object_id": "obj_789",
        "object_type": "extension",
        "file_name": "adblock.zip",
        "file_size_mb": 2.5,
        "created_at": "2024-01-24T00:00:00Z",
        "profile_count": 5
      }
    ],
    "total": 1,
    "limit": 10,
    "offset": 0
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Objects metadata retrieved successfully"
  }
}
```

#### Get Object Meta by ID

**GET** `https://api.multilogin.com/storage/object/meta`

Get metadata for a specific object.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_id`: string (Required)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/object/meta?object_id=obj_789' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "object_type": "extension",
    "file_name": "adblock.zip",
    "file_size_mb": 2.5,
    "created_at": "2024-01-24T00:00:00Z",
    "last_accessed": "2024-01-25T10:00:00Z",
    "checksum": "abc123def456",
    "profile_count": 5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object metadata retrieved successfully"
  }
}
```

#### Delete Object

**GET** `https://api.multilogin.com/storage/object/delete`

Delete an object from storage.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_id`: string (Required)
- `force`: boolean (Optional - force delete even if attached to profiles)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/object/delete?object_id=obj_789&force=false' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "deleted": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object deleted successfully"
  }
}
```

#### Restore Object

**GET** `https://api.multilogin.com/storage/object/restore`

Restore a deleted object.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_id`: string (Required)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/object/restore?object_id=obj_789' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "restored": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object restored successfully"
  }
}
```

#### Cloud to Local

**POST** `https://api.multilogin.com/storage/cloud_to_local`

Transfer object from cloud to local storage.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "object_id": "obj_789",
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/cloud_to_local' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "object_id": "obj_789",
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "transferred": true,
    "local_path": "/profiles/95f9061e/objects/obj_789"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object transferred to local successfully"
  }
}
```

#### Local to Cloud

**POST** `https://api.multilogin.com/storage/local_to_cloud`

Transfer object from local to cloud storage.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "local_path": "/profiles/95f9061e/objects/obj_789",
  "object_type": "extension",
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/local_to_cloud' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "local_path": "/profiles/95f9061e/objects/obj_789",
  "object_type": "extension"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "object_id": "obj_790",
    "object_type": "extension",
    "cloud_url": "https://storage.multilogin.com/obj_790",
    "transferred": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Object transferred to cloud successfully"
  }
}
```

#### Download Object

**GET** `https://api.multilogin.com/storage/object/download`

Get download URL for an object.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `object_id`: string (Required)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/object/download?object_id=obj_789' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "object_id": "obj_789",
    "download_url": "https://download.multilogin.com/obj_789?token=abc123",
    "expires_at": "2024-01-24T01:00:00Z",
    "file_name": "extension.zip",
    "file_size_mb": 2.5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Download URL generated successfully"
  }
}
```

#### Create Extension

**POST** `https://api.multilogin.com/storage/extension/create`

Create and upload a browser extension.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: multipart/form-data
- `Accept`: application/json

**Form Data**:
- `file`: File (Required - .zip or .crx file)
- `name`: string (Required)
- `description`: string (Optional)
- `version`: string (Optional)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/extension/create' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--form 'file=@"/path/to/extension.zip"' \
--form 'name="My Custom Extension"' \
--form 'description="Custom extension for automation"' \
--form 'version="1.0.0"'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "extension_id": "ext_123",
    "object_id": "obj_791",
    "name": "My Custom Extension",
    "version": "1.0.0",
    "created_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Extension created successfully"
  }
}
```

#### Enable Extension

**POST** `https://api.multilogin.com/storage/extension/enable`

Enable extension for profiles.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "extension_id": "ext_123",
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/extension/enable' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "extension_id": "ext_123",
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "extension_id": "ext_123",
    "enabled_for": 1,
    "profile_ids": [
      "95f9061e-5656-845a-2801-7fff8f0f12if"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Extension enabled successfully"
  }
}
```

#### Disable Extension

**POST** `https://api.multilogin.com/storage/extension/disable`

Disable extension for profiles.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "extension_id": "ext_123",
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/extension/disable' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "extension_id": "ext_123",
  "profile_ids": [
    "95f9061e-5656-845a-2801-7fff8f0f12if"
  ]
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "extension_id": "ext_123",
    "disabled_for": 1,
    "profile_ids": [
      "95f9061e-5656-845a-2801-7fff8f0f12if"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Extension disabled successfully"
  }
}
```

#### List of Objects per Profile

**POST** `https://api.multilogin.com/storage/profile/objects`

Get all objects associated with a profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/storage/profile/objects' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "objects": [
      {
        "object_id": "obj_789",
        "object_type": "extension",
        "file_name": "adblock.zip",
        "attached_at": "2024-01-24T00:00:00Z"
      },
      {
        "object_id": "obj_790",
        "object_type": "backup",
        "file_name": "profile_backup.mlx",
        "attached_at": "2024-01-23T00:00:00Z"
      }
    ],
    "total_objects": 2
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Profile objects retrieved successfully"
  }
}
```

### Bookmark Management

#### Export Bookmarks

**GET** `https://api.multilogin.com/bookmarks/export`

Export bookmarks from a profile.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Query Parameters**:
- `profile_id`: uuid (Required)
- `format`: string (Optional - json, html)

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/bookmarks/export?profile_id=95f9061e-5656-845a-2801-7fff8f0f12if&format=json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "bookmarks": [
      {
        "id": "bookmark_1",
        "title": "Example Site",
        "url": "https://example.com",
        "folder": "Work",
        "created_at": "2024-01-20T00:00:00Z"
      }
    ],
    "total": 1,
    "export_format": "json"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Bookmarks exported successfully"
  }
}
```

#### Import Bookmarks

**POST** `https://api.multilogin.com/bookmarks/import`

Import bookmarks to a profile.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "bookmarks": [
    {
      "title": "New Bookmark",
      "url": "https://newsite.com",
      "folder": "Personal"
    }
  ],
  "merge": true
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/bookmarks/import' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "bookmarks": [
    {
      "title": "New Bookmark",
      "url": "https://newsite.com",
      "folder": "Personal"
    }
  ],
  "merge": true
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "imported": 1,
    "total_bookmarks": 2
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Bookmarks imported successfully"
  }
}
```

#### Copy Bookmarks

**POST** `https://api.multilogin.com/bookmarks/copy`

Copy bookmarks between profiles.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "source_profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "target_profile_ids": [
    "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  ],
  "merge": false
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/bookmarks/copy' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "source_profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
  "target_profile_ids": [
    "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  ],
  "merge": false
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "source_profile_id": "95f9061e-5656-845a-2801-7fff8f0f12if",
    "copied_to": 1,
    "bookmarks_copied": 15
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Bookmarks copied successfully"
  }
}
```

### 2FA

#### Set up 2FA

**POST** `https://api.multilogin.com/2fa/setup`

Initialize 2FA setup for the account.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "method": "authenticator"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/2fa/setup' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "method": "authenticator"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "qr_code": "data:image/png;base64,iVBORw0KGgoAAAANS...",
    "secret": "JBSWY3DPEHPK3PXP",
    "backup_codes": [
      "12345678",
      "87654321",
      "11223344"
    ]
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "2FA setup initiated successfully"
  }
}
```

#### Enable 2FA

**POST** `https://api.multilogin.com/2fa/enable`

Enable 2FA after setup verification.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "verification_code": "123456"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/2fa/enable' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "verification_code": "123456"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "2fa_enabled": true,
    "enabled_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "2FA enabled successfully"
  }
}
```

#### Verify 2FA

**POST** `https://api.multilogin.com/2fa/verify`

Verify 2FA code during login.

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "email": "user@example.com",
  "temp_token": "temp_token_from_login",
  "code": "123456"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/2fa/verify' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "email": "user@example.com",
  "temp_token": "temp_token_from_login",
  "code": "123456"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user_id": "81b5627a-1212-4016-9467-3dbe4d6f78eb"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "2FA verified successfully"
  }
}
```

#### Set up New Device for 2FA

**POST** `https://api.multilogin.com/2fa/device/setup`

Add a new trusted device for 2FA.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "device_name": "My Laptop",
  "device_type": "desktop",
  "trust_duration_days": 30
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/2fa/device/setup' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "device_name": "My Laptop",
  "device_type": "desktop",
  "trust_duration_days": 30
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "device_id": "device_456",
    "device_name": "My Laptop",
    "trusted_until": "2024-02-23T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Device added successfully"
  }
}
```

#### Get Devices for 2FA

**GET** `https://api.multilogin.com/2fa/devices`

Get list of trusted devices.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/2fa/devices' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "devices": [
      {
        "device_id": "device_456",
        "device_name": "My Laptop",
        "device_type": "desktop",
        "trusted_until": "2024-02-23T00:00:00Z",
        "last_used": "2024-01-24T10:00:00Z"
      }
    ],
    "total": 1
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Devices retrieved successfully"
  }
}
```

#### Get Backup Codes for 2FA

**GET** `https://api.multilogin.com/2fa/backup_codes`

Get backup codes for 2FA recovery.

**Authorization**: Bearer Token

**Headers**:
- `Accept`: application/json

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/2fa/backup_codes' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "backup_codes": [
      {
        "code": "12345678",
        "used": false
      },
      {
        "code": "87654321",
        "used": false
      },
      {
        "code": "11223344",
        "used": true
      }
    ],
    "unused_count": 2,
    "generated_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Backup codes retrieved successfully"
  }
}
```

#### Revoke Device for 2FA

**POST** `https://api.multilogin.com/2fa/device/revoke`

Revoke a trusted device.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "device_id": "device_456"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/2fa/device/revoke' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "device_id": "device_456"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "device_id": "device_456",
    "revoked": true
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Device revoked successfully"
  }
}
```

#### Enable/Disable 2FA for Workspace

**POST** `https://api.multilogin.com/2fa/workspace`

Enable or disable 2FA requirement for workspace.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
  "require_2fa": true,
  "enforcement_date": "2024-02-01T00:00:00Z"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/2fa/workspace' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
  "require_2fa": true,
  "enforcement_date": "2024-02-01T00:00:00Z"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "workspace_id": "92c6738b-2323-5127-9578-4ecf5e7f89fc",
    "require_2fa": true,
    "enforcement_date": "2024-02-01T00:00:00Z",
    "affected_users": 5
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "Workspace 2FA requirement updated successfully"
  }
}
```

#### Disable 2FA

**POST** `https://api.multilogin.com/2fa/disable`

Disable 2FA for the account.

**Authorization**: Bearer Token

**Headers**:
- `Content-Type`: application/json
- `Accept`: application/json

**Request Body**:
```json
{
  "password": "current_password",
  "code": "123456"
}
```

**Example Request**:
```bash
curl --location 'https://api.multilogin.com/2fa/disable' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data '{
  "password": "current_password",
  "code": "123456"
}'
```

**Example Response** (200 OK):
```json
{
  "data": {
    "2fa_enabled": false,
    "disabled_at": "2024-01-24T00:00:00Z"
  },
  "status": {
    "error_code": "",
    "http_code": 200,
    "message": "2FA disabled successfully"
  }
}
```

---

## Additional Resources

- **Support Page**: [https://help.multilogin.com/en_US/multilogin-x](https://help.multilogin.com/en_US/multilogin-x)
- **Feedback Survey**: [https://tally.so/r/nWABkk](https://tally.so/r/nWABkk)
- **Automation Token**: For higher rate limits and longer token lifetime, use the Workspace Automation Token endpoint

## Notes

- All timestamps are in ISO 8601 format
- UUIDs are used for all ID fields
- Bearer tokens expire after 30 minutes (regular) or as specified (automation)
- Rate limits apply to all endpoints - check response headers for limit information
- All endpoints return consistent error response format with error_code and message

---

*This documentation is complete and includes all endpoints from the Multilogin X API. For the most up-to-date information, always refer to the official API documentation.*
 