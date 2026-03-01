# Python + Node.js Claude Scaffold

A clean, forkable scaffold for building Claude-powered Python applications. Provides
reusable patterns for agent loops, skill modules, tool definitions, and memory
management — all as typed stubs ready to implement.

## Features

- **Agent loop** — structured conversation management with Claude
- **Skill system** — modular, composable agent capabilities
- **Tool definitions** — memory store/recall/list/delete with Anthropic tool-use format
- **Memory layer** — short-term (in-memory) and long-term (JSON file) storage
- **`.agent/` prompts** — declarative Markdown skills, personas, and strategies
- **`.claude/` harnesses** — hooks, slash commands, and settings wired up
- **Node.js utilities** — `validate-env` script for CI pre-flight checks

## Quick Start

```bash
# Install Python dependencies
pip install -e ".[dev]"

# Copy and fill in your API key
cp .env.example .env
$EDITOR .env

# Run tests (all stubs raise NotImplementedError — expected)
pytest tests/unit/ -v

# Try the CLI
python -m src.agent.run --help

# Validate environment variables
cd src/scripts && node utils/validate-env.mjs
```

## Project Structure

```
src/
├── agent/          # AgentLoop, CLI entry, skill loader
├── skills/         # BaseSkill Protocol + example skill
├── tools/          # BaseTool Protocol, definitions, handlers
└── memory/         # ShortTerm/LongTerm/ContextManager stubs

.agent/             # Declarative Markdown → injected into system prompts
├── skills/         # chain_of_thought.md, self_critique.md
├── personas/       # engineer.md, researcher.md
└── strategies/     # workflow.md, research_workflow.md

.claude/            # Claude Code harnesses
├── commands/       # /commit, /test, /review, /lint
└── hooks/          # post-write-format.sh, session-start-banner.sh
```

## Implementation Guide

Each stub raises `NotImplementedError`. Implement them in this order:

1. `src/memory/` — short_term → long_term → context_manager
2. `src/tools/handlers.py` — wire tool definitions to memory
3. `src/skills/` — extend `BaseSkill`, add to loader
4. `src/agent/loop.py` — main agent loop against Anthropic API
5. `src/agent/run.py` — CLI wiring

See `docs/architecture.md` for design decisions and `tasks/todo.md` for next steps.

## Development

```bash
# Lint
ruff check src/ tests/

# Type check
mypy src/

# Pre-commit hooks
pre-commit install
pre-commit run --all-files
```

## License

MIT
