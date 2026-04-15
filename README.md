# Ball Sim

Ball Sim is a touch-friendly physics playground made for my three-year-old son, who loves seeing lots of balls bouncing around on the screen.

It is a simple static web page built with Matter.js. You can add oversized physics balls, drag them around, watch them collide, and clear the scene when it gets too busy. Each ball also shows a small emoji and an easy English word, turning the toy-like motion into a tiny learning moment.

## Live Demo

https://jason9075.github.io/ball-sim/

## Features

- Add large physics balls by tapping, clicking, or pressing the Add Ball button.
- Drag balls with mouse or touch input.
- Clear all balls with one large touch-friendly control.
- Learn simple English words with emoji labels on the balls.
- Keep balls away from the control buttons with a hidden physics barrier.
- Automatically clear the scene when performance gets too low.
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

## License

MIT
