---
allowed-tools: Bash, Read, Edit, Write, Glob, Grep
argument-hint: "[--readme-only | --arch-only | --all (default)]"
---

# /docs-update — Refresh README and Architecture Docs

Inspect recent git changes and rewrite `README.md` and/or `docs/architecture.md`
so they accurately reflect the current state of the project.

## Steps

1. **Understand what changed**
   - Run `git log --oneline -10` for recent commit summaries.
   - Run `git diff HEAD~1..HEAD --name-only` for files changed in the last commit.
   - Run `git diff --stat` for any pending (unstaged) changes.

2. **Read current docs**
   - Read `README.md`.
   - Read `docs/architecture.md`.

3. **Scan project structure**
   - Glob `src/**/*.py` to list all modules.
   - Read `pyproject.toml` for dependencies and entry points.
   - Read `CLAUDE.md` for the authoritative project description.
   - Glob `.claude/commands/*.md` to list current slash commands.
   - Glob `.agent/**/*.md` to list current agent skills, personas, and strategies.

4. **Determine scope** from `$ARGUMENTS`
   - No argument or `--all`: update both README and architecture docs.
   - `--readme-only`: update `README.md` only; skip `docs/architecture.md`.
   - `--arch-only`: update `docs/architecture.md` only; skip `README.md`.

5. **Update README.md** (unless `--arch-only`)

   Apply the docs_writer style guide (`.agent/skills/docs_writer.md`):
   - Features list reflects actual capabilities; mark stubs `(stub — NotImplementedError)`.
   - Quick Start commands use `uv venv` / `uv pip install` pattern from `CLAUDE.md`.
   - Project Structure tree reflects actual directories and key files.
   - Slash Commands section lists every file found under `.claude/commands/`.
   - Keep the file under 120 lines; move excess detail to `docs/`.

6. **Update docs/architecture.md** (unless `--readme-only`)

   Apply the docs_writer style guide:
   - ASCII component tree reflects the actual module layout under `src/`.
   - Design Decisions section matches current coding conventions in `CLAUDE.md`.
   - Extension Points table lists actual hook points (tools, skills, memory, hooks).
   - Mark any component that raises `NotImplementedError` as `(stub)`.
   - Keep each section independently readable (no forward references required).

7. **Report** — print a brief summary:
   - Which files were modified and the nature of each change.
   - Which files were left unchanged and why.
