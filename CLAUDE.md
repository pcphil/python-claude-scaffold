# CLAUDE.md

Project instructions for Claude Code.  Read this file at the start of every
session before making any changes.

## Project Overview

This is a **Python + Node.js boilerplate** for Claude-powered applications.
`src/` is intentionally empty — rename `src/project_name/` to your package name
and start implementing. The tooling, hooks, and `.agent/` prompts are pre-wired.

## Key Files

| Path | Purpose |
|------|---------|
| `src/project_name/` | Rename to your package; add modules here |
| `src/project_name/config/` | Configuration helpers |
| `src/project_name/utils/` | Shared utilities |
| `.agent/` | Declarative Markdown prompts (skills, personas, strategies) |
| `.claude/commands/` | Slash commands: `/commit`, `/test`, `/review`, `/lint` |
| `tasks/todo.md` | Current task list |
| `tasks/lessons.md` | Post-correction patterns |

## Workflow

1. Check `tasks/todo.md` for the next open item.
2. Rename `src/project_name/` to your package name and update `pyproject.toml`.
3. Implement modules under `src/<your_package>/`.
4. After each file, run `pytest tests/unit/ -v`.
5. After full implementation, run `ruff check src/ tests/ && mypy src/`.
6. Append a lesson to `tasks/lessons.md` after any non-trivial fix.

## Coding Conventions

- **Python 3.11+** — use `from __future__ import annotations` in every module.
- **Type hints everywhere** — `mypy --strict` must pass.
- **`@dataclass`** for concrete classes; `Protocol` + `@runtime_checkable` for interfaces.
- **Line length**: 100 characters (ruff).
- **Imports**: sorted by ruff-I; stdlib → third-party → local.

## Running the Project

```bash
# Create venv and install (uv recommended)
uv venv
uv pip install -e ".[dev]"

# Tests
pytest tests/unit/ -v

# Lint
ruff check src/ tests/
mypy src/

# Docker
docker compose run --rm test
```

## Slash Commands

- `/commit` — create a conventional commit
- `/test` — run pytest
- `/review` — structured code review
- `/lint` — ruff + mypy

## Hooks

- **PostToolUse(Write|Edit)** → `.claude/hooks/post-write-format.sh`
  Runs `ruff format` + `ruff check --fix` on any `.py` file just written.

## Memory

- Short-term: implement as an in-process dict, cleared on agent reset.
- Long-term: implement as a JSON file at `.memory/long_term.json` (gitignored).
- Use a single ContextManager interface everywhere.

## Do Not

- Do not add `__all__` unless a module is a public API.
- Do not implement stubs speculatively — only implement what a test requires.
- Do not push to `main` without passing CI (lint + unit tests).
- Do not read any .env files