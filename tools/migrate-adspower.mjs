#!/usr/bin/env node
/**
 * Migrate AdsPower CSV exports into a Multilogin-flavored JSON payload.
 *
 * Usage:
 *   node tools/migrate-adspower.mjs --input ads.csv --output mlx.json [--folder <id>]
 *
 * AdsPower's "Account Center → Export" gives a CSV. We map the most-common
 * columns to a Multilogin profile create payload. Unknown columns fall into
 * `notes` so nothing is lost.
 */
import { readFileSync, writeFileSync } from "node:fs";

function parseArgs(argv) {
  const out = {};
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--input") out.input = argv[++i];
    else if (a === "--output") out.output = argv[++i];
    else if (a === "--folder") out.folder = argv[++i];
    else if (a === "--help" || a === "-h") out.help = true;
  }
  return out;
}

function help() {
  console.log(
    "migrate-adspower — AdsPower CSV → Multilogin profile JSON\n\n" +
      "  --input <file>   AdsPower CSV export\n" +
      "  --output <file>  JSON output (array of payloads)\n" +
      "  --folder <id>    Target Multilogin folder ID (optional)\n" +
      "\n" +
      "Then create profiles with:\n" +
      "  npx mlx-labs create --from mlx.json\n",
  );
}

function parseCSV(text) {
  const rows = [];
  let i = 0;
  let cur = "";
  let row = [];
  let inQuotes = false;
  while (i < text.length) {
    const c = text[i];
    if (inQuotes) {
      if (c === '"' && text[i + 1] === '"') {
        cur += '"';
        i += 2;
        continue;
      }
      if (c === '"') {
        inQuotes = false;
        i++;
        continue;
      }
      cur += c;
      i++;
      continue;
    }
    if (c === '"') {
      inQuotes = true;
      i++;
      continue;
    }
    if (c === ",") {
      row.push(cur);
      cur = "";
      i++;
      continue;
    }
    if (c === "\n" || c === "\r") {
      if (cur || row.length) {
        row.push(cur);
        rows.push(row);
        row = [];
        cur = "";
      }
      if (c === "\r" && text[i + 1] === "\n") i++;
      i++;
      continue;
    }
    cur += c;
    i++;
  }
  if (cur || row.length) {
    row.push(cur);
    rows.push(row);
  }
  if (!rows.length) return [];
  const header = rows.shift().map((h) => h.trim());
  return rows
    .filter((r) => r.length && r.some((v) => v.trim()))
    .map((r) => Object.fromEntries(header.map((h, idx) => [h, r[idx] || ""])));
}

function pick(rec, ...keys) {
  for (const k of keys) {
    if (k in rec && rec[k]) return rec[k];
    const lc = Object.keys(rec).find((x) => x.toLowerCase() === k.toLowerCase());
    if (lc && rec[lc]) return rec[lc];
  }
  return "";
}

function toMultilogin(rec, folder) {
  const proxyType = pick(rec, "proxy_type", "type") || "http";
  const host = pick(rec, "proxy_host", "ip", "host");
  const port = pick(rec, "proxy_port", "port");
  const user = pick(rec, "proxy_user", "username");
  const pass = pick(rec, "proxy_pass", "password");

  const proxy =
    host && port
      ? {
          type: proxyType.toLowerCase(),
          host,
          port: Number(port) || 0,
          username: user || undefined,
          password: pass || undefined,
        }
      : undefined;

  return {
    name: pick(rec, "name", "profile_name", "user_name") || `migrated-${rec.id || ""}`,
    folder_id: folder || undefined,
    os_type: (pick(rec, "os") || "win").toLowerCase().includes("mac") ? "macos" : "win",
    browser_type:
      (pick(rec, "browser") || "mimic").toLowerCase().includes("stealthfox")
        ? "stealthfox"
        : "mimic",
    proxy,
    notes:
      "Migrated from AdsPower\n" +
      Object.entries(rec)
        .filter(([k]) =>
          ![
            "name",
            "profile_name",
            "user_name",
            "proxy_type",
            "type",
            "proxy_host",
            "ip",
            "host",
            "proxy_port",
            "port",
            "proxy_user",
            "username",
            "proxy_pass",
            "password",
            "os",
            "browser",
          ].includes(k.toLowerCase()),
        )
        .map(([k, v]) => `${k}=${v}`)
        .join("\n"),
  };
}

const args = parseArgs(process.argv);
if (args.help || !args.input) {
  help();
  process.exit(args.help ? 0 : 1);
}
const text = readFileSync(args.input, "utf8");
const rows = parseCSV(text);
const payloads = rows.map((r) => toMultilogin(r, args.folder));
const output = args.output || args.input.replace(/\.csv$/i, ".mlx.json");
writeFileSync(output, JSON.stringify(payloads, null, 2));
console.log(`migrated ${rows.length} rows → ${output}`);
