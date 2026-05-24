/**
 * Start a Multilogin profile via the local launcher API.
 * Docs: https://multilogin.com/help/en_US/api
 */
import "dotenv/config";

const LAUNCHER = process.env.MULTILOGIN_LAUNCHER_URL ?? "https://launcher.mlx.yt:45001";
const TOKEN = process.env.MULTILOGIN_TOKEN;
const PROFILE_ID = process.env.MULTILOGIN_PROFILE_ID;

if (!TOKEN || !PROFILE_ID) {
  console.error("Set MULTILOGIN_TOKEN and MULTILOGIN_PROFILE_ID in .env");
  process.exit(1);
}

async function startProfile() {
  const url = `${LAUNCHER}/api/v2/profile/start`;
  const res = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${TOKEN}`,
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify({
      profileId: PROFILE_ID,
      automation: true,
    }),
  });

  const body = await res.json().catch(() => ({}));

  if (!res.ok) {
    console.error("Failed to start profile:", res.status, body);
    process.exit(1);
  }

  console.log("Profile started.");
  console.log("Connect automation to:", body.port ?? body.data?.port ?? "(see response)");
  console.log(JSON.stringify(body, null, 2));
}

startProfile().catch((err) => {
  console.error(err);
  process.exit(1);
});
