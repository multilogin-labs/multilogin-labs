#!/usr/bin/env node
/**
 * mlx-labs — community CLI for Multilogin Labs.
 * Usage: npx mlx-labs <command> [args]
 *
 * Partner pricing: https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549
 */
import { readFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join, resolve } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(here, "..", "..");
const AFFILIATE =
  "https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549";

const [, , raw, ...rest] = process.argv;
const cmd = (raw || "help").toLowerCase();

const COMMANDS = {
  help: { desc: "Show this help", run: help },
  version: { desc: "Print CLI version", run: version },
  search: { desc: "Search the 90 API endpoints (alias of api:search)", run: search },
  endpoints: { desc: "Print every endpoint as JSON", run: endpoints },
  cheatsheet: { desc: "Print the API cheatsheet", run: cheatsheet },
  plan: { desc: "Recommend a Multilogin plan", run: plan },
  warmup: { desc: "Forward to warmup scheduler", run: warmup },
  guides: { desc: "List guides in this repo", run: guides },
  cookbook: { desc: "List cookbook recipes", run: cookbook },
  links: { desc: "Print partner pricing + promo codes", run: links },
  upgrade: { desc: "Run the master upgrade script (requires repo)", run: upgrade },
};

(COMMANDS[cmd] ?? { run: () => help() }).run(rest);

function help() {
  const list = Object.entries(COMMANDS)
    .map(([k, v]) => `  ${k.padEnd(11)} ${v.desc}`)
    .join("\n");
  console.log(`mlx-labs · community CLI for github.com/multilogin-labs/multilogin-labs

Commands:
${list}

Examples:
  npx mlx-labs search profile start
  npx mlx-labs cheatsheet
  npx mlx-labs plan -- --profiles 50 --team 3 --mobile

Partner: ${AFFILIATE}
Codes:   SAAS50 · MIN50
`);
}

function version() {
  const pkg = JSON.parse(readFileSync(join(repoRoot, "package.json"), "utf8"));
  console.log(`mlx-labs ${pkg.version}`);
}

function search(args) {
  const path = join(repoRoot, "tools", "api-search.mjs");
  if (!existsSync(path)) {
    console.error("Run inside the multilogin-labs repo. Clone first: git clone https://github.com/multilogin-labs/multilogin-labs");
    process.exit(2);
  }
  process.argv = [process.argv0, path, ...args];
  import(path);
}

function endpoints() {
  const path = join(repoRoot, "docs", "api", "endpoints.json");
  console.log(readFileSync(path, "utf8"));
}

function cheatsheet() {
  const path = join(repoRoot, "docs", "api", "CHEATSHEET.md");
  console.log(readFileSync(path, "utf8"));
}

function plan(args) {
  const path = join(repoRoot, "tools", "plan-calculator.mjs");
  process.argv = [process.argv0, path, ...args];
  import(path);
}

function warmup(args) {
  const path = join(repoRoot, "tools", "warmup-scheduler.mjs");
  process.argv = [process.argv0, path, ...args];
  import(path);
}

function guides() {
  const path = join(repoRoot, "docs", "guides", "README.md");
  console.log(readFileSync(path, "utf8"));
}

function cookbook() {
  const path = join(repoRoot, "docs", "api", "cookbook", "README.md");
  console.log(readFileSync(path, "utf8"));
}

function links() {
  console.log(`Partner pricing: ${AFFILIATE}`);
  console.log(`Codes: SAAS50 · MIN50`);
  console.log(`Repo: https://github.com/multilogin-labs/multilogin-labs`);
  console.log(`Docs: https://multilogin-labs.github.io/multilogin-labs/`);
  console.log(`Swagger UI: ./docs/api/swagger.html`);
}

function upgrade() {
  const { spawnSync } = require("node:child_process");
  spawnSync("bash", [join(repoRoot, "tools", "upgrade_all.sh")], {
    stdio: "inherit",
  });
}
