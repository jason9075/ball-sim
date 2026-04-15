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

Start the Nix-managed dev server:

```sh
just dev
```

Then open:

```text
http://127.0.0.1:8000/
```

`just dev` enters the flake dev shell automatically, serves the static files, and restarts the server with `entr` when `index.html` or `matter.min.js` changes.

You can override the bind host or port:

```sh
HOST=0.0.0.0 PORT=8080 just dev
```
