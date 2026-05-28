"""Sublime Text plugin: Multilogin X API search."""
import json
import os
import urllib.request
import webbrowser

import sublime
import sublime_plugin

REMOTE_INDEX = (
    "https://raw.githubusercontent.com/multilogin-labs/"
    "multilogin-labs/main/docs/api/endpoints.json"
)
DOC_BASE = (
    "https://github.com/multilogin-labs/multilogin-labs/blob/main/docs/api/endpoints/"
)


def load_endpoints():
    """Try local repo first, fall back to GitHub."""
    candidates = []
    for f in sublime.active_window().folders():
        candidates.append(os.path.join(f, "docs", "api", "endpoints.json"))
    for c in candidates:
        if os.path.exists(c):
            with open(c, "r", encoding="utf-8") as fh:
                return json.load(fh)
    try:
        with urllib.request.urlopen(REMOTE_INDEX, timeout=4) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception:
        return []


class MlxSearchEndpointsCommand(sublime_plugin.WindowCommand):
    def run(self):
        endpoints = load_endpoints()
        if not endpoints:
            sublime.error_message("Could not load Multilogin endpoints.json")
            return
        items = [
            ["{} {}".format(e["method"], e["name"]), e["category"], e["url"]]
            for e in endpoints
        ]

        def on_done(idx):
            if idx >= 0:
                webbrowser.open(DOC_BASE + endpoints[idx]["slug"] + ".md")

        self.window.show_quick_panel(items, on_done)
