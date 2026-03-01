# TODO

Agent task tracking file.  Add items here as you work; cross them off when done.

## Implement stubs

- [ ] `src/memory/short_term.py` — implement `store`, `recall`, `list_keys`, `delete`, `clear`
- [ ] `src/memory/long_term.py` — implement `_load`, `_save`, `store`, `recall`, `list_keys`, `delete`
- [ ] `src/memory/context_manager.py` — implement `store`, `recall`, `list_keys`, `delete`
- [ ] `src/tools/handlers.py` — implement all four handlers + `build_tool_registry`
- [ ] `src/skills/example/skill.py` — implement `run`
- [ ] `src/agent/skill_loader.py` — implement `load`, `get`, `list_skills`, `as_system_prompt_fragment`
- [ ] `src/agent/loop.py` — implement `setup`, `run`, `_handle_tool_use`, `reset`
- [ ] `src/agent/run.py` — implement single-shot and REPL paths in `main`

## Tests

- [ ] Add real assertions to `tests/unit/test_memory.py` once memory is implemented
- [ ] Add real assertions to `tests/unit/test_tools.py` once tools are implemented
- [ ] Complete `tests/integration/test_agent_integration.py` once loop is implemented

## Documentation

- [ ] Fill in `docs/architecture.md` extension points once implementation is stable

## CI / CD

- [ ] Add secrets (`ANTHROPIC_API_KEY`) to GitHub Actions for integration test job
- [ ] Enable `pre-commit` in CI once all hooks pass on clean codebase
