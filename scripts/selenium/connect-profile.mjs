/**
 * Connect Selenium to a running Multilogin profile via ChromeDriver / CDP port.
 * Requires: npm install selenium-webdriver
 */
import "dotenv/config";

const PORT = process.env.MULTILOGIN_DEBUG_PORT ?? "35000";

async function main() {
  let webdriver;
  try {
    webdriver = await import("selenium-webdriver");
  } catch {
    console.error("Install: npm install selenium-webdriver");
    process.exit(1);
  }

  const chrome = await import("selenium-webdriver/chrome.js");

  const options = new chrome.Options();
  options.debuggerAddress(`127.0.0.1:${PORT}`);

  const driver = await new webdriver.Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .build();

  await driver.get("https://browserleaks.com/ip");
  console.log("Title:", await driver.getTitle());
  await driver.quit();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
