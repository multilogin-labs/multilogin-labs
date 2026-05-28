#!/usr/bin/env node
/** Build a full Postman v2.1 collection from endpoints.json. */
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const eps = JSON.parse(readFileSync(join(root, "docs/api/endpoints.json"), "utf8"));

const grouped = new Map();
for (const e of eps) {
  if (!grouped.has(e.category)) grouped.set(e.category, []);
  grouped.get(e.category).push(e);
}

function urlObj(rawUrl) {
  const u = new URL(rawUrl.replace(/\/:([a-zA-Z_]+)/g, "/{{$1}}"));
  const pathSegs = u.pathname.split("/").filter(Boolean);
  const variables = [];
  for (const seg of pathSegs) {
    const m = seg.match(/^\{\{([a-zA-Z_]+)\}\}$/);
    if (m) variables.push({ key: m[1], value: "" });
  }
  return {
    raw: rawUrl
      .replace("https://launcher.mlx.yt:45001", "{{MULTILOGIN_LAUNCHER}}")
      .replace("https://api.multilogin.com", "{{MULTILOGIN_API}}")
      .replace(/\/:([a-zA-Z_]+)/g, "/{{$1}}"),
    host: [u.hostname.includes("launcher") ? "{{MULTILOGIN_LAUNCHER}}" : "{{MULTILOGIN_API}}"],
    path: pathSegs,
    variable: variables,
  };
}

const items = [...grouped.entries()].map(([cat, list]) => ({
  name: cat,
  item: list.map((e) => ({
    name: e.name,
    request: {
      method: e.method,
      header: [
        { key: "Authorization", value: "Bearer {{MULTILOGIN_TOKEN}}" },
        { key: "Content-Type", value: "application/json" },
      ],
      url: urlObj(e.url),
      description: `Generated from docs/api/endpoints/${e.slug}.md\n\nDocs: https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/endpoints/${e.slug}.md`,
    },
    response: [],
  })),
}));

const collection = {
  info: {
    _postman_id: "mlx-labs-collection",
    name: "Multilogin Labs · Multilogin X (community)",
    description:
      "Community Postman collection auto-generated from docs/api/endpoints.json.\n" +
      "Partner pricing: https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549\n" +
      "Repo: https://github.com/multilogin-labs/multilogin-labs",
    schema:
      "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
  },
  variable: [
    { key: "MULTILOGIN_API", value: "https://api.multilogin.com" },
    { key: "MULTILOGIN_LAUNCHER", value: "https://launcher.mlx.yt:45001" },
    { key: "MULTILOGIN_TOKEN", value: "" },
    { key: "MULTILOGIN_FOLDER_ID", value: "" },
    { key: "MULTILOGIN_PROFILE_ID", value: "" },
  ],
  item: items,
};

const out = join(root, "docs/api/postman-collection.json");
writeFileSync(out, JSON.stringify(collection, null, 2));
console.log("postman collection: %d categories, %d endpoints → %s", items.length, eps.length, out);
