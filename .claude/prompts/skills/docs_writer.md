# Skill: Docs Writer

Style guide for writing and updating project documentation in this scaffold.

## Audience

Developers forking this scaffold to build their own Claude-powered application.
Assume familiarity with Python and git; do not assume familiarity with the
scaffold's internal conventions.

## Voice and Tense

- Use **present tense**: "The loop sends a request" not "The loop will send a request".
- Use **active voice**: "ContextManager stores entries" not "Entries are stored by ContextManager".
- Prefer **concrete examples** over abstract descriptions.

## Structure

- Use ASCII diagrams for structural and component relationships; avoid prose-only
  descriptions of how modules connect.
- Keep `README.md` under **120 lines**; move detail to `docs/`.
- Keep each section of `docs/architecture.md` **independently readable** —
  a reader who skips to "Memory Layer" must not need to have read "Agent Loop" first.
- Use level-2 headings (`##`) for major sections; level-3 (`###`) for subsections.
  Do not go deeper than `###`.

## Accuracy Rules

- **Never describe a stub as implemented.** Any class or function whose body is
  `raise NotImplementedError` must be labelled `(stub — NotImplementedError)` in
  every doc section that references it.
- Commands and paths must match the actual repository layout. Verify with Glob/Grep
  before writing.
- Dependency names and versions must be read from `pyproject.toml`, not assumed.

## README Checklist

- [ ] One-line project description at the top.
- [ ] Features list (mark stubs explicitly).
- [ ] Quick Start using `uv venv` + `uv pip install -e ".[dev]"`.
- [ ] Project Structure tree (key paths only, not exhaustive).
- [ ] Slash Commands table (one row per `.claude/commands/*.md` file).
- [ ] Running Tests / Lint section.

## Architecture Doc Checklist

- [ ] Top-level ASCII component diagram.
- [ ] One section per major layer: Agent Loop, Memory, Tools, Skills, CLI.
- [ ] Design Decisions section (key choices made and why).
- [ ] Extension Points table (where to add new tools, skills, hooks).

## Example ASCII Diagram Format

```
src/
├── agent/
│   ├── loop.py          # AgentLoop (stub)
│   ├── run.py           # CLI entry point
│   └── skill_loader.py  # Loads .claude/prompts/*.md
├── memory/
│   ├── short_term.py    # ShortTermMemory (stub)
│   ├── long_term.py     # LongTermMemory (stub)
│   └── context.py       # ContextManager (stub)
└── tools/
    ├── definitions.py   # TOOL_DEFINITIONS list
    └── handlers.py      # Tool handlers (stubs)
```
