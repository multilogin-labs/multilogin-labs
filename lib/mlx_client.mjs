/**
 * Multilogin X API client (Node.js)
 * @see lib/mlx_client.py
 */
import "dotenv/config";
import { DEFAULT_LAUNCHER, MULTILOGIN_API } from "./constants.mjs";

export class MLXClient {
  constructor(token, launcherUrl = process.env.MULTILOGIN_LAUNCHER_URL ?? DEFAULT_LAUNCHER) {
    this.token = token;
    this.launcherUrl = launcherUrl;
  }

  static fromEnv() {
    const token = process.env.MULTILOGIN_TOKEN;
    if (!token) throw new Error("Set MULTILOGIN_TOKEN");
    return new MLXClient(token);
  }

  async #request(method, url, { json } = {}) {
    const res = await fetch(url, {
      method,
      headers: {
        Authorization: `Bearer ${this.token}`,
        Accept: "application/json",
        ...(json ? { "Content-Type": "application/json" } : {}),
      },
      body: json ? JSON.stringify(json) : undefined,
    });
    const body = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(`${res.status} ${url}: ${JSON.stringify(body)}`);
    return body;
  }

  async startProfile(folderId, profileId, { automationType = "playwright", headless = false } = {}) {
    const qs = new URLSearchParams({
      automation_type: automationType,
      headless_mode: String(headless),
    });
    const url = `${this.launcherUrl}/api/v2/profile/f/${folderId}/p/${profileId}/start?${qs}`;
    return this.#request("GET", url);
  }

  async stopProfile(profileId) {
    const qs = new URLSearchParams({ profile_id: profileId });
    return this.#request("GET", `${this.launcherUrl}/api/v1/profile/stop?${qs}`);
  }

  async stopAllProfiles() {
    return this.#request("GET", `${this.launcherUrl}/api/v1/profile/stop_all`);
  }

  async profileSearch(payload = {}) {
    return this.#request("POST", `${MULTILOGIN_API}/profile/search`, { json: payload });
  }

  async profileCreate(payload) {
    return this.#request("POST", `${MULTILOGIN_API}/profile/create`, { json: payload });
  }
}
