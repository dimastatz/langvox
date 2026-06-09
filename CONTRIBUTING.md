# Contributing to AudioTrace

Contributions are welcome — especially new provider adapters, persona
definitions for simulation, and compliance rule sets.

## Development setup

```bash
git clone https://github.com/audiotrace/audiotrace
cd audiotrace

# FFmpeg is required on your system:
#   macOS:  brew install ffmpeg
#   Debian: sudo apt-get install ffmpeg

pip install -e ".[dev]"
pytest
```

## Before opening a PR

Run the same checks CI runs:

```bash
ruff check .
ruff format .
mypy src/audiotrace
pytest
```

Or reproduce CI exactly in Docker:

```bash
docker build -f docker/Dockerfile.test -t audiotrace-test .
docker run --rm audiotrace-test pytest
```

## Working on a feature

- Features are specified in [`docs/prd/`](docs/prd/README.md). Read the relevant
  PRD before starting; if there isn't one, open an issue or draft a PRD first.
- `src/audiotrace/models.py` is the public data contract — treat changes to it
  as breaking, and keep the README's `CallReport` tree in sync.
- See [`docs/roadmap.md`](docs/roadmap.md) for priorities and ordering.

## Guidelines

- Keep public API changes documented in the README.
- Add tests for new behavior; keep the suite green.
- Match the style of surrounding code (ruff enforces formatting and linting).
