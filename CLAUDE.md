# CLAUDE.md

Project instructions for Claude Code.  Read this file at the start of every
session before making any changes.

## Project Overview

This is a **Python + Node.js scaffold** for Claude-powered applications.  Every
concrete class is a stub (`raise NotImplementedError`) waiting to be implemented.
Node.js lives exclusively in `src/scripts/` for utility tasks.

## Key Files

| Path | Purpose |
|------|---------|
| `src/agent/loop.py` | Main agent loop (implement first after memory) |
| `src/agent/run.py` | CLI entry point |
| `src/agent/skill_loader.py` | Loads `.agent/*.md` into system prompts |
| `src/memory/` | Short-term + long-term + ContextManager |
| `src/tools/` | Tool definitions + handlers |
| `src/skills/` | BaseSkill Protocol + example |
| `.agent/` | Declarative Markdown prompts (skills, personas, strategies) |
| `.claude/commands/` | Slash commands: `/commit`, `/test`, `/review`, `/lint` |
| `tasks/todo.md` | Current task list |
| `tasks/lessons.md` | Post-correction patterns |

## Workflow

1. Check `tasks/todo.md` for the next open item.
2. Implement in this order: memory → tools → skills → agent loop → CLI.
3. After each file, run `pytest tests/unit/ -v` to confirm stubs raise as expected.
4. After full implementation, run `ruff check src/ tests/ && mypy src/`.
5. Append a lesson to `tasks/lessons.md` after any non-trivial fix.

## Coding Conventions

- **Python 3.11+** — use `from __future__ import annotations` in every module.
- **Type hints everywhere** — `mypy --strict` must pass.
- **`@dataclass`** for concrete classes; `Protocol` + `@runtime_checkable` for interfaces.
- **Stubs raise `NotImplementedError`** — never return a fake value.
- **Line length**: 100 characters (ruff).
- **Imports**: sorted by ruff-I; stdlib → third-party → local.

## Running the Project

```bash
# Install
pip install -e ".[dev]"

# Tests
pytest tests/unit/ -v

# Lint
ruff check src/ tests/
mypy src/

# CLI
python -m src.agent.run --help

# Node env check
cd src/scripts && node utils/validate-env.mjs

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

- Short-term: in-process dict, cleared on `AgentLoop.reset()`.
- Long-term: JSON file at `.memory/long_term.json` (gitignored).
- ContextManager is the single interface — use it everywhere.

## Do Not

- Do not add `__all__` unless a module is a public API.
- Do not implement stubs speculatively — only implement what a test requires.
- Do not push to `main` without passing CI (lint + unit tests).
