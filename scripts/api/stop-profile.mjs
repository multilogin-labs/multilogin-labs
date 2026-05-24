/**
 * Stop a Multilogin profile via Launcher API.
 * GET /api/v1/profile/stop?profile_id=
 */
import "dotenv/config";

const LAUNCHER = process.env.MULTILOGIN_LAUNCHER_URL ?? "https://launcher.mlx.yt:45001";
const TOKEN = process.env.MULTILOGIN_TOKEN;
const PROFILE_ID = process.env.MULTILOGIN_PROFILE_ID;

if (!TOKEN || !PROFILE_ID) {
  console.error("Set MULTILOGIN_TOKEN and MULTILOGIN_PROFILE_ID in .env");
  process.exit(1);
}

const url = `${LAUNCHER}/api/v1/profile/stop?${new URLSearchParams({ profile_id: PROFILE_ID })}`;

const res = await fetch(url, {
  method: "GET",
  headers: {
    Authorization: `Bearer ${TOKEN}`,
    Accept: "application/json",
  },
});

const body = await res.json().catch(() => ({}));
if (!res.ok) {
  console.error("Stop failed:", res.status, body);
  process.exit(1);
}
console.log("Profile stopped.", JSON.stringify(body, null, 2));
