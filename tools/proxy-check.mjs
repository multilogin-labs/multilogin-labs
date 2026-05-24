#!/usr/bin/env node
/** Quick proxy HTTP reachability check (not full Multilogin integration). */
import "dotenv/config";

const url = process.argv[2] ?? process.env.PROXY_CHECK_URL ?? "https://api.ipify.org?format=json";

const start = Date.now();
try {
  const res = await fetch(url, { signal: AbortSignal.timeout(15000) });
  const text = await res.text();
  console.log(`OK ${res.status} in ${Date.now() - start}ms`);
  console.log(text.slice(0, 200));
} catch (err) {
  console.error("Proxy/network check failed:", err.message);
  process.exit(1);
}
