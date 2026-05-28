# jetbrains-mlx · IntelliJ / WebStorm / PyCharm plugin scaffold

Search Multilogin X API endpoints from the JetBrains Find Action / Search Everywhere.

## Status

**Scaffold** — clone, run `./gradlew runIde` for live testing. PRs welcome.

## Files

- `build.gradle.kts` — plugin build config
- `src/main/resources/META-INF/plugin.xml` — IDE manifest
- `src/main/kotlin/dev/mlxlabs/MlxSearchAction.kt` — action that opens a quick-pick dialog over `endpoints.json`

## Build

```bash
./gradlew buildPlugin   # produces build/distributions/jetbrains-mlx-*.zip
```

Then **Settings → Plugins → Install plugin from disk…**

## Related

- VS Code: [`extensions/vscode-mlx-search`](../vscode-mlx-search/)
- CLI: [`cli/`](../../cli/) — `npx mlx-labs search ...`
