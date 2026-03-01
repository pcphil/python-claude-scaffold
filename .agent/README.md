# .agent/ — Declarative Agent Prompts

This directory contains Markdown files that are loaded at runtime and injected
into the Claude system prompt.  Each file is self-contained and focuses on a
single concern.

## Directory Layout

```
.agent/
├── skills/         # Reasoning and response techniques
├── personas/       # Role-specific behaviour profiles
└── strategies/     # High-level workflow patterns
```

## How It Works

`AgentSkillLoader` discovers all `*.md` files under this directory, indexes
them by stem (filename without extension), and exposes them via
`as_system_prompt_fragment()`.  The agent loop selects which files to include
based on the active configuration.

## Adding a New Prompt

1. Create a `*.md` file in the appropriate sub-directory.
2. Keep the file focused — one skill / persona / strategy per file.
3. Reference it by stem name in `AgentConfig.skills` or the CLI `--skill` flag.
