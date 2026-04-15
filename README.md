# Ball Sim

A touch-friendly ball physics playground built as a static web page with Matter.js.

## Live Demo

https://jason9075.github.io/ball-sim/

## Features

- Add physics balls by tapping or clicking the canvas.
- Drag balls with mouse or touch input.
- Clear all balls with one control.
- Runs entirely in the browser with no build step.

## Local Development

Serve the static files from the project root:

```sh
python3 -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000/
```

If you use Nix and Just:

```sh
just dev
```
