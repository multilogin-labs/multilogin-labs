#!/usr/bin/env node
/** Search Multilogin API endpoints from endpoints.json */
import { readFileSync } from "fs";
import { fileURLToPath } from "url";
import { dirname, join } from "path";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const eps = JSON.parse(readFileSync(join(root, "docs/api/endpoints.json"), "utf8"));
const q = process.argv.slice(2).join(" ").toLowerCase();

if (!q) {
  console.log("Usage: npm run api:search -- profile start");
  console.log(`Index: ${eps.length} endpoints`);
  process.exit(0);
}

const terms = q.split(/\s+/).filter(Boolean);
const hits = eps.filter((e) => {
  const hay = `${e.name} ${e.url} ${e.category} ${e.slug}`.toLowerCase();
  return terms.every((t) => hay.includes(t));
});

for (const e of hits.slice(0, 20)) {
  console.log(`${e.method.padEnd(6)} ${e.name}`);
  console.log(`       ${e.url}`);
  console.log(`       docs/api/endpoints/${e.slug}.md\n`);
}
console.log(hits.length, "matches");
