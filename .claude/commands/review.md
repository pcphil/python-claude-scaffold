---
allowed-tools: Bash, Read
argument-hint: "[git ref or file path to review]"
---

# /review — Structured Code Review

Perform a structured review of recent changes or a specific file.

## Steps

1. Determine scope:
   - If `$ARGUMENTS` is a file path, read and review that file.
   - If `$ARGUMENTS` is a git ref (e.g. `HEAD~1`), run `git diff $ARGUMENTS`.
   - If `$ARGUMENTS` is empty, run `git diff HEAD` for uncommitted changes.
2. Analyse the diff or file under these headings:
   ### Correctness
   - Logic errors, off-by-one, unhandled edge cases.
   ### Type Safety
   - Missing annotations, incorrect return types, `Any` overuse.
   ### Error Handling
   - Uncaught exceptions, swallowed errors, missing `NotImplementedError` stubs.
   ### Style & Conventions
   - Naming, line length, import order (ruff rules E/F/I/B/SIM).
   ### Tests
   - Is there a corresponding test? Does it cover the happy path and error path?
3. Provide a **Summary** with:
   - Must-fix issues (blocking)
   - Should-fix issues (non-blocking)
   - Nice-to-have suggestions
