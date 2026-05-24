/**
 * Connect Playwright to an already-running Multilogin profile.
 * 1. Start profile in app or: npm run api:launch
 * 2. Note the debugger port from the response
 */
import "dotenv/config";

const PORT = process.env.MULTILOGIN_DEBUG_PORT ?? "35000";

async function main() {
  let playwright;
  try {
    playwright = await import("playwright");
  } catch {
    console.error("Install playwright: npm install playwright");
    process.exit(1);
  }

  const browser = await playwright.chromium.connectOverCDP(
    `http://127.0.0.1:${PORT}`
  );

  const context = browser.contexts()[0] ?? (await browser.newContext());
  const page = context.pages()[0] ?? (await context.newPage());

  await page.goto("https://browserleaks.com/ip");
  const title = await page.title();
  console.log("Connected. Page title:", title);

  await browser.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
