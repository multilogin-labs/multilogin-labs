import { chromium } from "playwright";

const TOKEN = process.env.MULTILOGIN_TOKEN;
const FOLDER = process.env.MULTILOGIN_FOLDER_ID;
const PROFILE = process.env.MULTILOGIN_PROFILE_ID;
const LAUNCHER = process.env.MULTILOGIN_LAUNCHER || "https://launcher.mlx.yt:45001";

if (!TOKEN || !FOLDER || !PROFILE) {
  console.error("Set MULTILOGIN_TOKEN, MULTILOGIN_FOLDER_ID, MULTILOGIN_PROFILE_ID");
  process.exit(1);
}

const URLS = [
  "https://browserleaks.com/",
  "https://pixelscan.net/",
  "https://abrahamjuliot.github.io/creepjs/",
];

const startUrl = `${LAUNCHER}/api/v2/profile/f/${FOLDER}/p/${PROFILE}/start?automation_type=playwright`;
const res = await fetch(startUrl, { headers: { Authorization: `Bearer ${TOKEN}` } });
const body = await res.json();
const port = body.status?.port || body.data?.port || body.port;
if (!port) {
  console.error("No port returned from Launcher", body);
  process.exit(2);
}

const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const ctx = browser.contexts()[0] || (await browser.newContext());
const page = ctx.pages()[0] || (await ctx.newPage());

let i = 0;
for (const url of URLS) {
  await page.goto(url, { waitUntil: "domcontentloaded" });
  await page.screenshot({ path: `screenshot-${++i}.png`, fullPage: true });
  console.log("captured", url);
}

await browser.close();
await fetch(`${LAUNCHER}/api/v1/profile/stop?profile_id=${PROFILE}`, {
  headers: { Authorization: `Bearer ${TOKEN}` },
});
