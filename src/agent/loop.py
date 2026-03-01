"""AgentLoop — the main conversation loop against the Anthropic API."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import anthropic

from src.agent.skill_loader import AgentSkillLoader
from src.memory.context_manager import ContextManager
from src.tools.definitions import TOOL_DEFINITIONS  # noqa: F401


@dataclass
class AgentConfig:
    """Configuration for a single AgentLoop run.

    Attributes:
        model: Anthropic model ID to use.
        max_tokens: Maximum tokens in each assistant response.
        max_iterations: Hard cap on tool-use rounds to prevent infinite loops.
        system_prompt: Base system prompt (skills are appended).
        skills: Skill names to activate from :attr:`skill_loader`.
    """

    model: str = "claude-sonnet-4-6"
    max_tokens: int = 4096
    max_iterations: int = 10
    system_prompt: str = "You are a helpful AI assistant."
    skills: list[str] = field(default_factory=list)


@dataclass
class AgentLoop:
    """Drives a multi-turn, tool-using conversation with Claude.

    The loop sends user messages to the Anthropic API, handles ``tool_use``
    responses by dispatching to registered handlers, and continues until the
    model returns a ``stop_reason`` of ``"end_turn"`` or the iteration cap is
    hit.

    Attributes:
        config: Run-time configuration.
        client: Anthropic API client.
        memory: Unified memory facade.
        skill_loader: Loader for ``.agent/`` Markdown skills.
        _tool_registry: Name → handler mapping built at startup.
        _messages: Mutable conversation history.
    """

    config: AgentConfig = field(default_factory=AgentConfig)
    client: anthropic.Anthropic = field(default_factory=anthropic.Anthropic)
    memory: ContextManager = field(default_factory=ContextManager)
    skill_loader: AgentSkillLoader = field(default_factory=AgentSkillLoader)
    _tool_registry: dict[str, Any] = field(default_factory=dict, init=False, repr=False)
    _messages: list[dict[str, Any]] = field(default_factory=list, init=False, repr=False)

    def setup(self) -> None:
        """Initialise the tool registry and load skills.

        Call once before the first :meth:`run` invocation.

        Raises:
            NotImplementedError: Always — implement to wire tools and skills.
        """
        raise NotImplementedError

    def run(self, user_message: str) -> str:
        """Send *user_message* and drive the loop to completion.

        Appends the user message to :attr:`_messages`, calls the API, handles
        any ``tool_use`` blocks, and returns the final text response.

        Args:
            user_message: The human turn to send to the model.

        Returns:
            The assistant's final text response.

        Raises:
            NotImplementedError: Always — implement the main loop body.
        """
        raise NotImplementedError

    def _handle_tool_use(self, tool_use_block: Any) -> Any:  # noqa: ANN401
        """Dispatch a ``tool_use`` block to the appropriate handler.

        Args:
            tool_use_block: The ``ToolUseBlock`` returned by the API.

        Returns:
            JSON-serialisable result forwarded back as a ``tool_result``.

        Raises:
            NotImplementedError: Always — implement tool dispatch logic.
        """
        raise NotImplementedError

    def reset(self) -> None:
        """Clear conversation history and short-term memory.

        Raises:
            NotImplementedError: Always — implement reset logic.
        """
        raise NotImplementedError
