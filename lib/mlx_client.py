"""Multilogin X API Python client.

Based on official Postman collection structure (api.multilogin.com + launcher.mlx.yt).
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any

from lib.constants import DEFAULT_LAUNCHER, MULTILOGIN_API


@dataclass
class MLXClient:
    token: str
    launcher_url: str = DEFAULT_LAUNCHER
    refresh_token: str | None = None

    @classmethod
    def from_env(cls) -> MLXClient:
        token = os.getenv("MULTILOGIN_TOKEN", "")
        if not token:
            raise ValueError("Set MULTILOGIN_TOKEN in .env")
        return cls(
            token=token,
            launcher_url=os.getenv("MULTILOGIN_LAUNCHER_URL", DEFAULT_LAUNCHER),
            refresh_token=os.getenv("MULTILOGIN_REFRESH_TOKEN"),
        )

    @classmethod
    def signin(cls, email: str, password: str) -> MLXClient:
        body = cls._request(
            "POST",
            f"{MULTILOGIN_API}/user/signin",
            json_body={"email": email, "password": password},
            token=None,
        )
        data = body.get("data", body)
        return cls(
            token=data["token"],
            refresh_token=data.get("refresh_token"),
        )

    @classmethod
    def automation_token(cls, bearer: str) -> MLXClient:
        body = cls._request(
            "GET",
            f"{MULTILOGIN_API}/workspace/automation_token",
            token=bearer,
        )
        data = body.get("data", body)
        return cls(token=data.get("token") or data.get("automation_token") or bearer)

    def refresh(self, workspace_id: str | None = None) -> None:
        if not self.refresh_token:
            raise ValueError("No refresh_token available")
        payload: dict[str, Any] = {"refresh_token": self.refresh_token}
        if workspace_id:
            payload["workspace_id"] = workspace_id
        body = self._request(
            "POST",
            f"{MULTILOGIN_API}/user/refresh_token",
            json_body=payload,
            token=self.token,
        )
        data = body.get("data", body)
        self.token = data["token"]
        self.refresh_token = data.get("refresh_token", self.refresh_token)

    def start_profile(
        self,
        folder_id: str,
        profile_id: str,
        *,
        automation_type: str = "playwright",
        headless: bool = False,
    ) -> dict[str, Any]:
        qs = urllib.parse.urlencode(
            {"automation_type": automation_type, "headless_mode": str(headless).lower()}
        )
        url = (
            f"{self.launcher_url}/api/v2/profile/f/{folder_id}/p/{profile_id}/start?{qs}"
        )
        return self._request("GET", url, token=self.token)

    def stop_profile(self, profile_id: str) -> dict[str, Any]:
        qs = urllib.parse.urlencode({"profile_id": profile_id})
        url = f"{self.launcher_url}/api/v1/profile/stop?{qs}"
        return self._request("GET", url, token=self.token)

    def stop_all_profiles(self) -> dict[str, Any]:
        url = f"{self.launcher_url}/api/v1/profile/stop_all"
        return self._request("GET", url, token=self.token)

    def profile_search(self, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._request(
            "POST",
            f"{MULTILOGIN_API}/profile/search",
            json_body=payload or {},
            token=self.token,
        )

    def profile_create(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self._request(
            "POST",
            f"{MULTILOGIN_API}/profile/create",
            json_body=payload,
            token=self.token,
        )

    def quick_profile_v3(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self._request(
            "POST",
            f"{self.launcher_url}/api/v3/profile/quick",
            json_body=payload,
            token=self.token,
        )

    @staticmethod
    def _request(
        method: str,
        url: str,
        *,
        json_body: dict[str, Any] | None = None,
        token: str | None = None,
    ) -> dict[str, Any]:
        headers = {"Accept": "application/json"}
        data = None
        if json_body is not None:
            headers["Content-Type"] = "application/json"
            data = json.dumps(json_body).encode()
        if token:
            headers["Authorization"] = f"Bearer {token}"

        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            err_body = e.read().decode()
            raise RuntimeError(f"HTTP {e.code} {url}: {err_body}") from e
