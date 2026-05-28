#!/usr/bin/env node
/** Generate a Postman environment JSON for Multilogin X. */
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const env = {
  id: "mlx-labs-env",
  name: "Multilogin Labs (community)",
  values: [
    { key: "MULTILOGIN_API", value: "https://api.multilogin.com", enabled: true },
    { key: "MULTILOGIN_LAUNCHER", value: "https://launcher.mlx.yt:45001", enabled: true },
    { key: "MULTILOGIN_TOKEN", value: "", enabled: true, type: "secret" },
    { key: "MULTILOGIN_FOLDER_ID", value: "", enabled: true },
    { key: "MULTILOGIN_PROFILE_ID", value: "", enabled: true },
    { key: "MULTILOGIN_AUTOMATION_TYPE", value: "playwright", enabled: true },
  ],
  _postman_variable_scope: "environment",
};

const out = join(root, "docs/api/postman-environment.json");
writeFileSync(out, JSON.stringify(env, null, 2));
console.log("wrote", out);
