const TOKEN = process.env.MULTILOGIN_TOKEN;
const FOLDER = process.env.MULTILOGIN_FOLDER_ID;
const PROFILE = process.env.MULTILOGIN_PROFILE_ID;
const WEBHOOK = process.env.DISCORD_WEBHOOK_URL;
const LAUNCHER = process.env.MULTILOGIN_LAUNCHER || "https://launcher.mlx.yt:45001";

if (!TOKEN || !FOLDER || !PROFILE || !WEBHOOK) {
  console.error("Set MULTILOGIN_TOKEN, MULTILOGIN_FOLDER_ID, MULTILOGIN_PROFILE_ID, DISCORD_WEBHOOK_URL");
  process.exit(1);
}

async function notify(msg) {
  await fetch(WEBHOOK, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ content: msg }),
  });
}

const url = `${LAUNCHER}/api/v2/profile/f/${FOLDER}/p/${PROFILE}/start?automation_type=playwright`;
const res = await fetch(url, { headers: { Authorization: `Bearer ${TOKEN}` } });
if (!res.ok) {
  await notify(`⚠️ Multilogin profile ${PROFILE} failed to start: HTTP ${res.status}`);
  console.error("alerted");
  process.exit(2);
}
console.log("profile started cleanly");
