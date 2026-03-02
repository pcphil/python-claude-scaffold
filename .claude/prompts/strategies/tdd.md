# Strategy: Test-Driven Development

Red-Green-Refactor cycle adapted to this project's pytest + ruff setup.

## Cycle

### 1. Red — Write a Failing Test

- Create or extend a test file under `tests/unit/`.
- The test must capture the requirement precisely: given this input, expect this output.
- Run: `.venv/Scripts/pytest tests/unit/ -v`
- **Confirm** the new test fails with the *expected* error (not an import error or typo).

### 2. Green — Minimum Production Code

- Write the smallest change that makes the failing test pass.
- Do not add logic that no test currently requires.
- Run: `.venv/Scripts/pytest tests/unit/ -v`
- **Confirm** all tests pass (new and existing).

### 3. Refactor — Clean Without Changing Behaviour

- Remove duplication; improve names; clarify intent.
- Do **not** add new behaviour during this phase.
- Run: `.venv/Scripts/pytest tests/unit/ -v && .venv/Scripts/ruff check src/ tests/`
- **Confirm** tests still pass and linter is clean.

### 4. Commit

- One logical Red-Green-Refactor cycle = one commit.
- Use `/commit` to generate a Conventional Commit message.

## When to Apply

- **New features** — write the test first, then implement.
- **Bug fixes** — write a test that reproduces the bug before touching production code;
  a passing test proves the fix and prevents regression.

## When Not to Apply

- **Exploratory spikes** — discovery work where the interface is unknown; delete the
  spike before merging.
- **Doc-only changes** — no behaviour change means no new test needed.

## Heuristics

- If writing the test feels hard, the interface is probably wrong — redesign before
  proceeding.
- One assertion per test where possible; multiple related assertions are acceptable
  when they test a single logical behaviour.
- Test names follow `test_<unit>_<scenario>_<expected_outcome>` (e.g.
  `test_context_manager_add_entry_returns_updated_state`).
