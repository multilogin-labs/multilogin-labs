const vscode = require("vscode");
const fs = require("fs");
const path = require("path");

const REPO_DOCS = "https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/endpoints/";

function loadEndpoints() {
  const candidates = [
    path.join(vscode.workspace.rootPath || "", "docs/api/endpoints.json"),
    path.join(__dirname, "..", "..", "docs", "api", "endpoints.json"),
  ];
  for (const p of candidates) {
    if (p && fs.existsSync(p)) {
      return JSON.parse(fs.readFileSync(p, "utf8"));
    }
  }
  return [];
}

function activate(context) {
  context.subscriptions.push(
    vscode.commands.registerCommand("mlx.search", async () => {
      const endpoints = loadEndpoints();
      if (endpoints.length === 0) {
        vscode.window.showWarningMessage(
          "Could not find docs/api/endpoints.json. Open the multilogin-labs repo as a workspace.",
        );
        return;
      }
      const items = endpoints.map((e) => ({
        label: `${e.method} ${e.name}`,
        description: e.category,
        detail: e.url,
        slug: e.slug,
      }));
      const picked = await vscode.window.showQuickPick(items, {
        matchOnDescription: true,
        matchOnDetail: true,
        placeHolder: "Search Multilogin X API endpoints (90)",
      });
      if (picked) {
        vscode.env.openExternal(vscode.Uri.parse(REPO_DOCS + picked.slug + ".md"));
      }
    }),
  );
}

function deactivate() {}

module.exports = { activate, deactivate };
