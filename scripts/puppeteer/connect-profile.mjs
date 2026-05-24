/**
 * Connect Puppeteer to an already-running Multilogin profile via CDP.
 */
import "dotenv/config";

const PORT = process.env.MULTILOGIN_DEBUG_PORT ?? "35000";

async function main() {
  let puppeteer;
  try {
    puppeteer = await import("puppeteer-core");
  } catch {
    console.error("Install puppeteer-core: npm install puppeteer-core");
    process.exit(1);
  }

  const browser = await puppeteer.connect({
    browserURL: `http://127.0.0.1:${PORT}`,
    defaultViewport: null,
  });

  const pages = await browser.pages();
  const page = pages[0] ?? (await browser.newPage());

  await page.goto("https://browserleaks.com/ip", { waitUntil: "domcontentloaded" });
  console.log("Connected. Page title:", await page.title());

  await browser.disconnect();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
