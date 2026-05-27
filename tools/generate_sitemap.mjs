#!/usr/bin/env node
/** Generate sitemap.xml for GitHub Pages from markdown paths */
import { readdirSync, statSync, writeFileSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const BASE = "https://multilogin-labs.github.io/multilogin-labs";
const docs = join(ROOT, "docs");

function walk(dir, base = "") {
  const urls = [];
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    const rel = (base ? base + "/" : "") + name;
    if (statSync(p).isDirectory()) urls.push(...walk(p, rel));
    else if (name.endsWith(".md") && name !== "reference-full.md")
      urls.push(rel.replace(/\.md$/, "").replace(/README$/, ""));
  }
  return urls;
}

const paths = walk(docs);
const xml = [
  '<?xml version="1.0" encoding="UTF-8"?>',
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
  ...paths.map((p) => {
    const loc = p ? `${BASE}/docs/${p}.html` : `${BASE}/docs`;
    return `  <url><loc>${loc}</loc></url>`;
  }),
  "</urlset>",
].join("\n");

writeFileSync(join(ROOT, "docs/sitemap.xml"), xml);
console.log("sitemap entries:", paths.length);
