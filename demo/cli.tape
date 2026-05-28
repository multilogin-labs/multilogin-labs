# VHS tape (https://github.com/charmbracelet/vhs) — record an animated GIF of the CLI.
# Render: vhs demo/cli.tape --output demo/cli.gif

Output demo/cli.gif

Set FontSize 18
Set Width 1200
Set Height 720
Set Theme "Dracula"
Set TypingSpeed 35ms
Set Padding 30

Type "npx mlx-labs help"
Sleep 600ms
Enter
Sleep 4s

Type "clear"
Enter

Type "npx mlx-labs search profile start"
Sleep 600ms
Enter
Sleep 5s

Type "clear"
Enter

Type "npx mlx-labs plan -- --profiles 50 --team 3 --mobile"
Sleep 600ms
Enter
Sleep 4s
