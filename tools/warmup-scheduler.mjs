#!/usr/bin/env node
/**
 * Warmup scheduler — start a list of profiles in waves with jitter.
 *
 * Usage:
 *   node tools/warmup-scheduler.mjs --profiles ID1,ID2,ID3 \
 *        --folder $MULTILOGIN_FOLDER_ID \
 *        --interval 600 --jitter 180 --duration 25
 *
 * - interval: avg seconds between starts
 * - jitter:   random +/- seconds applied per profile
 * - duration: minutes each profile stays open
 *
 * Requires Multilogin desktop running (Launcher API at localhost).
 */
import { setTimeout as sleep } from "node:timers/promises";
import {
  AFFILIATE_URL,
  DEFAULT_LAUNCHER,
  PROMO_CODES,
} from "../lib/constants.mjs";

const args = Object.fromEntries(
  process.argv.slice(2).reduce((acc, cur, i, a) => {
    if (cur.startsWith("--")) acc.push([cur.slice(2), a[i + 1]]);
    return acc;
  }, []),
);

if (!args.profiles || !args.folder) {
  console.log(
    `Multilogin warmup scheduler\n\n` +
      `Usage: node tools/warmup-scheduler.mjs --profiles A,B,C --folder UUID [--interval 600] [--jitter 120] [--duration 20]\n\n` +
      `Trial + partner pricing: ${AFFILIATE_URL}\n` +
      `Codes: ${PROMO_CODES.join(", ")}\n`,
  );
  process.exit(0);
}

const PROFILES = args.profiles.split(",").map((s) => s.trim()).filter(Boolean);
const FOLDER = args.folder;
const INTERVAL = Number(args.interval ?? 600);
const JITTER = Number(args.jitter ?? 120);
const DURATION = Number(args.duration ?? 20) * 60;
const TOKEN = process.env.MULTILOGIN_TOKEN;
const LAUNCHER = process.env.MULTILOGIN_LAUNCHER || DEFAULT_LAUNCHER;
const AUTOMATION = process.env.MULTILOGIN_AUTOMATION_TYPE || "playwright";

if (!TOKEN) {
  console.error("Missing MULTILOGIN_TOKEN — see docs/api/quick-start.md");
  process.exit(1);
}

const headers = { Authorization: `Bearer ${TOKEN}` };

async function start(profileId) {
  const url = `${LAUNCHER}/api/v2/profile/f/${FOLDER}/p/${profileId}/start?automation_type=${AUTOMATION}`;
  const res = await fetch(url, { headers });
  return res.ok;
}

async function stop(profileId) {
  const url = `${LAUNCHER}/api/v1/profile/stop?profile_id=${profileId}`;
  await fetch(url, { headers });
}

function jitterMs() {
  const j = (Math.random() * 2 - 1) * JITTER;
  return Math.max(15, INTERVAL + j) * 1000;
}

(async () => {
  console.log(
    `[warmup] ${PROFILES.length} profiles · interval ${INTERVAL}s ±${JITTER}s · duration ${DURATION / 60}min`,
  );
  for (const id of PROFILES) {
    const ok = await start(id);
    console.log(`[start] ${id} -> ${ok ? "ok" : "fail"}`);
    setTimeout(async () => {
      await stop(id);
      console.log(`[stop ] ${id}`);
    }, DURATION * 1000);
    await sleep(jitterMs());
  }
  console.log("[warmup] all wave triggers fired; stops will happen on schedule");
})();
