#!/usr/bin/env bash
# post-write-format.sh
# Triggered by PostToolUse on Write|Edit events.
# Runs ruff format + ruff check --fix on any .py file that was just written.
#
# Environment variables provided by Claude Code:
#   CLAUDE_TOOL_USE_NAME   — "Write" or "Edit"
#   CLAUDE_TOOL_INPUT_PATH — absolute path of the file that was written/edited

set -euo pipefail

FILE="${CLAUDE_TOOL_INPUT_PATH:-}"

# Only act on Python files
if [[ -z "$FILE" || "${FILE##*.}" != "py" ]]; then
    exit 0
fi

# Only act if the file actually exists (defensive check)
if [[ ! -f "$FILE" ]]; then
    exit 0
fi

# Run ruff format (silently)
if command -v ruff &>/dev/null; then
    ruff format --quiet "$FILE" || true
    ruff check --fix --quiet "$FILE" || true
fi
