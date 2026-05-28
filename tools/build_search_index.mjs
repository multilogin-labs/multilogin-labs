#!/usr/bin/env node
/** Build a Lunr-friendly JSON index of all docs/*.md for client-side search. */
import { readFileSync, writeFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const docs = join(root, "docs");

const docsList = [];

function walk(dir) {
  for (const entry of readdirSync(dir)) {
    const p = join(dir, entry);
    const s = statSync(p);
    if (s.isDirectory()) {
      walk(p);
      continue;
    }
    if (!p.endsWith(".md")) continue;
    const text = readFileSync(p, "utf8");
    const titleMatch = text.match(/^#\s+(.+)$/m);
    const title = titleMatch ? titleMatch[1].trim() : entry;
    const body = text
      .replace(/```[\s\S]*?```/g, " ")
      .replace(/[#*_>`\[\]]/g, " ")
      .replace(/\s+/g, " ")
      .trim()
      .slice(0, 1500);
    const rel = relative(docs, p).replace(/\\/g, "/");
    docsList.push({
      id: rel,
      title,
      url: rel,
      body,
    });
  }
}

walk(docs);

writeFileSync(join(docs, "search-index.json"), JSON.stringify(docsList));
console.log(`indexed ${docsList.length} docs → docs/search-index.json`);
