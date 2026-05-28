#!/usr/bin/env node
/** Generate OpenAPI 3.0 spec from endpoints.json */
import { readFileSync, writeFileSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const eps = JSON.parse(readFileSync(join(root, "docs/api/endpoints.json"), "utf8"));

const servers = [
  { url: "https://api.multilogin.com", description: "Cloud API" },
  { url: "https://launcher.mlx.yt:45001", description: "Local Launcher" },
];

const paths = {};
const tagSet = new Set();

for (const e of eps) {
  const u = new URL(e.url);
  const rawPath = u.pathname.replace(/\/:([a-zA-Z_]+)/g, "/{$1}");
  const method = e.method.toLowerCase();
  if (!paths[rawPath]) paths[rawPath] = {};
  tagSet.add(e.category);

  const params = [...rawPath.matchAll(/\{([a-zA-Z_]+)\}/g)].map((m) => ({
    name: m[1],
    in: "path",
    required: true,
    schema: { type: "string", format: "uuid" },
    description: `${m[1]} UUID from Multilogin app`,
  }));

  paths[rawPath][method] = {
    tags: [e.category],
    summary: e.name,
    operationId: e.slug.replace(/-/g, "_"),
    parameters: params,
    responses: {
      200: { description: "Success" },
      401: { description: "Unauthorized — refresh token" },
      429: { description: "Rate limit — see automation token guide" },
    },
    security: [{ bearerAuth: [] }],
    "x-docs": `https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/endpoints/${e.slug}.md`,
  };
}

const openapi = {
  openapi: "3.0.3",
  info: {
    title: "Multilogin X API (Community Reference)",
    version: "1.0.0",
    description:
      "Community OpenAPI spec generated from official Multilogin Postman collection. " +
      "Partner pricing: https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549",
    contact: { name: "Multilogin Labs", url: "https://github.com/multilogin-labs/multilogin-labs" },
    license: { name: "MIT" },
  },
  servers,
  tags: [...tagSet].map((t) => ({ name: t })),
  components: {
    securitySchemes: {
      bearerAuth: { type: "http", scheme: "bearer", bearerFormat: "JWT" },
    },
  },
  paths,
};

writeFileSync(join(root, "docs/api/openapi.json"), JSON.stringify(openapi, null, 2));
writeFileSync(
  join(root, "docs/api/openapi.yaml"),
  yamlify(openapi),
);
console.log(
  "openapi: %d endpoints, %d paths, %d tags",
  eps.length,
  Object.keys(paths).length,
  tagSet.size,
);

function yamlify(obj, indent = 0) {
  const pad = "  ".repeat(indent);
  if (obj === null) return "null";
  if (typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) {
    if (obj.length === 0) return "[]";
    return obj
      .map((v) => `${pad}- ${yamlify(v, indent + 1).trimStart()}`)
      .join("\n");
  }
  const lines = [];
  for (const [k, v] of Object.entries(obj)) {
    if (typeof v === "object" && v !== null) {
      lines.push(`${pad}${k}:`);
      lines.push(yamlify(v, indent + 1));
    } else {
      lines.push(`${pad}${k}: ${JSON.stringify(v)}`);
    }
  }
  return lines.join("\n");
}
