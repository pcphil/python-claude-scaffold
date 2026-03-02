# Python + Node.js Claude Scaffold

A clean, forkable boilerplate for building Claude-powered Python applications.
Provides project structure, tooling, and `.agent/` prompts pre-wired — ready
for you to add your implementation.

## Features

- **`.agent/` prompts** — declarative Markdown skills, personas, and strategies
- **`.claude/` harnesses** — hooks, slash commands, and settings wired up
- **Typed skeleton** — `src/project_name/` ready to rename and implement

## Quick Start

```bash
# Install Python dependencies
pip install -e ".[dev]"

# Copy and fill in your API key
cp .env.example .env
$EDITOR .env

# Rename the placeholder package and start building
mv src/project_name src/<your_package>
# Update pyproject.toml: packages = [{include = "<your_package>", from = "src"}]

# Run tests (empty suite — add your own)
pytest tests/unit/ -v

# Lint
ruff check src/ tests/
mypy src/
```

## Project Structure

```
src/
└── project_name/   # Rename to your package
    ├── config/
    └── utils/

.agent/             # Declarative Markdown → injected into system prompts
├── skills/         # chain_of_thought.md, self_critique.md
├── personas/       # engineer.md, researcher.md
└── strategies/     # workflow.md, research_workflow.md

.claude/            # Claude Code harnesses
├── commands/       # /commit, /test, /review, /lint
└── hooks/          # post-write-format.sh, session-start-banner.sh
```

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
