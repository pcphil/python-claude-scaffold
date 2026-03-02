# Skill: Debugging

Systematic root-cause analysis protocol. Fix the cause, not the symptom.

## Protocol

1. **Reproduce** — find the smallest input that reliably triggers the bug.
   Write it as a failing test in `tests/unit/` before touching any production code.

2. **Bisect** — narrow the fault location top-down:
   - Which module?
   - Which class or function?
   - Which line or expression?

3. **Isolate** — call the suspect function in isolation (REPL or a temporary test).
   Eliminate all other variables so only one thing can be wrong at a time.

4. **Hypothesize** — form at least two falsifiable hypotheses about the root cause.
   Write them down before testing either one.

5. **Verify** — test each hypothesis with the smallest possible experiment.
   Accept or reject based on evidence; do not move the goalposts.

6. **Fix** — address the root cause identified in step 5.
   Do not patch the symptom or add a workaround that hides the problem.

7. **Document** — if the bug was non-trivial, append one line to `tasks/lessons.md`:
   ```
   - [YYYY-MM-DD] <root cause> → <fix applied>
   ```

## Heuristics

- **Check the obvious first** — off-by-one errors, wrong type, unexpected `None`,
  missing `await`, incorrect import.
- **Read the full traceback** before forming any hypothesis; the answer is often in
  the last three lines.
- **Change one thing at a time** — simultaneous changes make it impossible to know
  which fix worked.
- **Trust the test, not your intuition** — if the test says it's broken, it's broken;
  if the test passes, investigate whether the test is correct before declaring victory.

## When to Apply

- Any bug report or unexpected behaviour.
- A test that fails for reasons that are not immediately obvious.
- Performance regressions (substitute "slowdown" for "bug" throughout the protocol).
