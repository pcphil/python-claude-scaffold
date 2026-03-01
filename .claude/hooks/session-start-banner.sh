#!/usr/bin/env bash
# session-start-banner.sh
# Prints the tail of tasks/lessons.md at the start of a bash session so that
# recent lessons are visible in the Claude Code context.
#
# This hook fires on the first PreToolUse(Bash) event of each session.
# A sentinel file prevents it from running more than once per session.

set -euo pipefail

SENTINEL="${TMPDIR:-/tmp}/.claude-banner-shown-$$"

# Only print once per shell session (process group)
SENTINEL="/tmp/.claude-banner-${PPID}"
if [[ -f "$SENTINEL" ]]; then
    exit 0
fi
touch "$SENTINEL"

LESSONS="${CLAUDE_PROJECT_DIR:-$(pwd)}/tasks/lessons.md"

if [[ -f "$LESSONS" ]]; then
    echo ""
    echo "━━━ Recent Lessons (tasks/lessons.md) ━━━"
    tail -n 10 "$LESSONS"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
fi
