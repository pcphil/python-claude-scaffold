# Architecture

## Overview

```
CLI (src/agent/run.py)
    └── AgentLoop (src/agent/loop.py)
            ├── AgentSkillLoader (src/agent/skill_loader.py)
            │       └── .claude/prompts/skills/*.md
            ├── ContextManager (src/memory/context_manager.py)
            │       ├── ShortTermMemory
            │       └── LongTermMemory (.memory/long_term.json)
            └── Tool Registry
                    ├── MemoryStoreTool
                    ├── MemoryRecallTool
                    ├── MemoryListTool
                    └── MemoryDeleteTool
```

## Design Decisions

### Stubs First
Every concrete class starts as a `@dataclass` with typed attributes and methods
that raise `NotImplementedError`.  This makes the interface visible immediately
and ensures tests can verify expected behaviour before implementation.

### Protocol Interfaces
`BaseTool`, `BaseSkill`, `ShortTermMemoryProtocol`, and `LongTermMemoryProtocol`
are `@runtime_checkable` `Protocol` classes.  This enables duck typing while
still allowing `isinstance()` checks in tests.

### Memory Hierarchy
- **Short-term** — in-process dict, cleared on `AgentLoop.reset()`.
- **Long-term** — JSON file under `.memory/`, survives process restarts.
- **ContextManager** — unified facade; short-term takes precedence on recall.

### Tool Definitions
Tool schemas live in `src/tools/definitions.py` and are passed as-is to the
Anthropic API.  Handlers in `src/tools/handlers.py` receive the `input` dict
and return a JSON-serialisable result.

### `.claude/prompts/` Prompts
Declarative Markdown loaded at runtime by `AgentSkillLoader`.  No code in these
files — only instructions for the model.  This keeps prompt engineering separate
from application logic.

## Extension Points

| Concern | Where to add |
|---------|-------------|
| New memory backend | Implement `LongTermMemoryProtocol`, swap in `ContextManager` |
| New tool | Add definition to `definitions.py`, add handler to `handlers.py`, register in `build_tool_registry` |
| New skill | Add `*.md` to `.claude/prompts/skills/` and/or add a `BaseSkill` subclass to `src/skills/` |
| New persona/strategy | Add `*.md` to `.claude/prompts/personas/` or `.claude/prompts/strategies/` |
