set shell := ["bash", "-uc"]

host := env_var_or_default("HOST", "127.0.0.1")
port := env_var_or_default("PORT", "8000")

default:
    @just --list

dev:
    @if [ -z "$${BALL_SIM_DEV_SHELL:-}" ]; then \
        exec env BALL_SIM_DEV_SHELL=1 nix develop "path:$$(pwd)" --command just _dev; \
    else \
        exec just _dev; \
    fi

[private]
_dev:
    @python_cmd="$(command -v python3 || command -v python)"; \
        printf 'Serving http://%s:%s\n' '{{host}}' '{{port}}'; \
        printf 'Watching index.html and matter.min.js with entr\n'; \
        find index.html matter.min.js -type f | entr -n -r "$python_cmd" -m http.server '{{port}}' --bind '{{host}}'
