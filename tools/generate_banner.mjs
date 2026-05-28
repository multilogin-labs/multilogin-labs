#!/usr/bin/env node
/** Copy the curated SVG banner into docs/ as the social preview. */
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const src = join(root, "press-kit/banner.svg");
const out = join(root, "docs/social-preview.svg");
mkdirSync(dirname(out), { recursive: true });
copyFileSync(src, out);
console.log("social-preview.svg ←", src);
