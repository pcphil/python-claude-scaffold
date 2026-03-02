---
allowed-tools: Bash
argument-hint: "[path to lint, defaults to src/ tests/]"
---

# /lint — Run Ruff and Mypy

Lint and type-check the codebase.

## Steps

1. Determine the target path:
   - Use `$ARGUMENTS` if provided.
   - Default to `src/ tests/`.
2. Run ruff check:
   ```bash
   ruff check $TARGET
   ```
3. Run mypy:
   ```bash
   mypy src/
   ```
   (mypy is scoped to `src/` regardless of `$ARGUMENTS`.)
4. If there are ruff violations:
   - List each violation with file, line, and rule code.
   - Suggest fixes for the most common rules.
5. If there are mypy errors:
   - List each error with file, line, and the type mismatch.
   - Suggest the correct annotation.
6. Report overall status: **clean** or **X violations found**.
