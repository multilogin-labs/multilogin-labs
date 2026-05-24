/**
 * Start a Multilogin profile via Launcher API (official v2 path).
 * GET /api/v2/profile/f/:folder_id/p/:profile_id/start
 */
import "dotenv/config";

const LAUNCHER = process.env.MULTILOGIN_LAUNCHER_URL ?? "https://launcher.mlx.yt:45001";
const TOKEN = process.env.MULTILOGIN_TOKEN;
const FOLDER_ID = process.env.MULTILOGIN_FOLDER_ID;
const PROFILE_ID = process.env.MULTILOGIN_PROFILE_ID;
const AUTOMATION = process.env.MULTILOGIN_AUTOMATION_TYPE ?? "playwright";

if (!TOKEN || !FOLDER_ID || !PROFILE_ID) {
  console.error("Set MULTILOGIN_TOKEN, MULTILOGIN_FOLDER_ID, MULTILOGIN_PROFILE_ID in .env");
  process.exit(1);
}

const qs = new URLSearchParams({
  automation_type: AUTOMATION,
  headless_mode: "false",
});
const url = `${LAUNCHER}/api/v2/profile/f/${FOLDER_ID}/p/${PROFILE_ID}/start?${qs}`;

const res = await fetch(url, {
  method: "GET",
  headers: {
    Authorization: `Bearer ${TOKEN}`,
    Accept: "application/json",
  },
});

const body = await res.json().catch(() => ({}));
if (!res.ok) {
  console.error("Failed to start profile:", res.status, body);
  process.exit(1);
}

const port = body.data?.port ?? body.port;
console.log("Profile started.");
console.log("Automation port:", port ?? "(see response)");
console.log(JSON.stringify(body, null, 2));
