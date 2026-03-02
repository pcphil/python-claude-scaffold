---
allowed-tools: Bash
argument-hint: "[pytest path or marker, e.g. tests/unit/ or -m integration]"
---

# /test — Run the Test Suite

Run pytest and report results.

## Steps

1. Determine the test scope:
   - If `$ARGUMENTS` is provided, pass it directly to pytest.
   - Otherwise default to `pytest tests/unit/ -v`.
2. Run: `pytest $ARGUMENTS --tb=short -q`
3. If tests fail:
   a. Show the full failure output for each failing test.
   b. Identify whether the failure is expected (stub raises `NotImplementedError`)
      or unexpected.
   c. For unexpected failures, suggest a fix.
4. Report a summary: `X passed, Y failed, Z skipped`.
