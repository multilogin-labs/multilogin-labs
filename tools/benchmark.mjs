#!/usr/bin/env node
/**
 * Multilogin Labs benchmark runner.
 *
 * Measures profile boot, Playwright connect, and stop times across N runs.
 * Writes results to docs/benchmarks/<timestamp>.csv.
 *
 * Usage:
 *   MULTILOGIN_TOKEN=... MULTILOGIN_FOLDER_ID=... MULTILOGIN_PROFILE_ID=... \
 *     node tools/benchmark.mjs --runs 5
 *
 * No external deps for the launcher path — uses native fetch.
 * Playwright connection step is optional (skipped if not installed).
 */
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { setTimeout as sleep } from "node:timers/promises";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const argv = Object.fromEntries(
  process.argv.slice(2).reduce((acc, cur, i, a) => {
    if (cur.startsWith("--")) acc.push([cur.slice(2), a[i + 1]]);
    return acc;
  }, []),
);

const TOKEN = process.env.MULTILOGIN_TOKEN;
const FOLDER = process.env.MULTILOGIN_FOLDER_ID;
const PROFILE = process.env.MULTILOGIN_PROFILE_ID;
const LAUNCHER = process.env.MULTILOGIN_LAUNCHER || "https://launcher.mlx.yt:45001";
const AUTOMATION = process.env.MULTILOGIN_AUTOMATION_TYPE || "playwright";
const RUNS = Number(argv.runs ?? 3);

if (!TOKEN || !FOLDER || !PROFILE) {
  console.error(
    "Missing env vars. Set MULTILOGIN_TOKEN, MULTILOGIN_FOLDER_ID, MULTILOGIN_PROFILE_ID.",
  );
  process.exit(1);
}

const headers = { Authorization: `Bearer ${TOKEN}` };

async function timeIt(label, fn) {
  const start = performance.now();
  let ok = true;
  let err = null;
  let out = null;
  try {
    out = await fn();
  } catch (e) {
    ok = false;
    err = e.message || String(e);
  }
  const ms = performance.now() - start;
  console.log(`  ${ok ? "✓" : "✗"} ${label}: ${ms.toFixed(0)} ms${err ? " · " + err : ""}`);
  return { label, ms, ok, err, out };
}

async function startProfile() {
  const url = `${LAUNCHER}/api/v2/profile/f/${FOLDER}/p/${PROFILE}/start?automation_type=${AUTOMATION}`;
  const res = await fetch(url, { headers });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

async function tryPlaywrightConnect(port) {
  if (!port) return { skipped: "no port" };
  try {
    const { chromium } = await import("playwright");
    const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`);
    const ctx = browser.contexts()[0];
    if (ctx) {
      const page = ctx.pages()[0] || (await ctx.newPage());
      await page.goto("about:blank");
    }
    await browser.close();
    return { connected: true };
  } catch (e) {
    return { skipped: e.message };
  }
}

async function stopProfile() {
  const url = `${LAUNCHER}/api/v1/profile/stop?profile_id=${PROFILE}`;
  const res = await fetch(url, { headers });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return true;
}

const rows = [["run", "step", "ms", "ok", "err"]];
for (let i = 1; i <= RUNS; i++) {
  console.log(`\n[run ${i}/${RUNS}]`);

  const startRes = await timeIt("start", startProfile);
  const port = startRes.out?.status?.port || startRes.out?.data?.port || startRes.out?.port;
  rows.push([i, "start", Math.round(startRes.ms), startRes.ok, startRes.err ?? ""]);

  const connectRes = await timeIt("playwright connect", () => tryPlaywrightConnect(port));
  rows.push([i, "playwright_connect", Math.round(connectRes.ms), connectRes.ok, connectRes.err ?? ""]);

  await sleep(800);

  const stopRes = await timeIt("stop", stopProfile);
  rows.push([i, "stop", Math.round(stopRes.ms), stopRes.ok, stopRes.err ?? ""]);

  if (i < RUNS) await sleep(1500);
}

const dir = join(ROOT, "docs", "benchmarks");
mkdirSync(dir, { recursive: true });
const stamp = new Date().toISOString().replace(/[:.]/g, "-");
const csv = rows.map((r) => r.map((x) => `"${String(x).replace(/"/g, '""')}"`).join(",")).join("\n");
const path = join(dir, `${stamp}.csv`);
writeFileSync(path, csv + "\n");
console.log("\nWrote", path);
