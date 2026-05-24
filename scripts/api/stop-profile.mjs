/**
 * Stop a running Multilogin profile via launcher API.
 */
import "dotenv/config";

const LAUNCHER = process.env.MULTILOGIN_LAUNCHER_URL ?? "https://launcher.mlx.yt:45001";
const TOKEN = process.env.MULTILOGIN_TOKEN;
const PROFILE_ID = process.env.MULTILOGIN_PROFILE_ID;

if (!TOKEN || !PROFILE_ID) {
  console.error("Set MULTILOGIN_TOKEN and MULTILOGIN_PROFILE_ID in .env");
  process.exit(1);
}

const res = await fetch(`${LAUNCHER}/api/v2/profile/stop`, {
  method: "POST",
  headers: {
    Authorization: `Bearer ${TOKEN}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ profileId: PROFILE_ID }),
});

const body = await res.json().catch(() => ({}));
if (!res.ok) {
  console.error("Stop failed:", res.status, body);
  process.exit(1);
}
console.log("Profile stopped.", JSON.stringify(body, null, 2));
