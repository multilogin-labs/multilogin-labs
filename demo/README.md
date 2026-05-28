# Demos & screenshots

## Animated CLI demo

We use [Charm VHS](https://github.com/charmbracelet/vhs) to record clean terminal animations.

```bash
brew install vhs                       # macOS
vhs demo/cli.tape --output demo/cli.gif
```

Embed in README:

```markdown
![CLI demo](demo/cli.gif)
```

## Static screenshots

Place into `demo/screenshots/` and reference in `docs/index.html` or relevant docs.

| Slot | Suggested content |
|---|---|
| `demo/screenshots/swagger.png` | Swagger UI showing the 90 endpoints |
| `demo/screenshots/calculator.png` | The plan calculator with a recommendation |
| `demo/screenshots/search.png` | Lunr search returning hits for "playwright" |
| `demo/screenshots/star-history.png` | Star history graph |

## Submit yours

PR welcome — add a screenshot with anonymized data and link it from the corresponding doc page.
