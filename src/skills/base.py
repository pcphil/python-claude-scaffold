"""BaseSkill Protocol — the interface every skill must implement."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class BaseSkill(Protocol):
    """Interface for agent skills.

    A skill is a named, self-contained capability that can be invoked by the
    agent loop.  Skills receive the current conversation context and return a
    string contribution to inject into the next user message or system prompt.
    """

    #: Unique, snake_case identifier used to look up and invoke the skill.
    name: str

    #: Short human-readable description surfaced in logs and the skill loader.
    description: str

    def run(self, context: dict[str, Any]) -> str:
        """Execute the skill with the given context.

        Args:
            context: Arbitrary key/value pairs describing the current state
                (conversation history, memory snapshot, active persona, etc.).

        Returns:
            A string to inject into the agent's next prompt, or an empty
            string if the skill has no contribution.
        """
        ...
