"""Tool handler implementations wired to the ContextManager."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from src.memory.context_manager import ContextManager
from src.tools.base import ToolExecutionError  # noqa: F401


@dataclass
class MemoryStoreTool:
    """Handler for the ``memory_store`` tool.

    Attributes:
        memory: The shared ContextManager instance.
    """

    name: str = "memory_store"
    memory: ContextManager = None  # type: ignore[assignment]

    def run(self, tool_input: dict[str, Any]) -> dict[str, Any]:
        """Store a value in memory.

        Args:
            tool_input: Must contain ``key`` and ``value``; optionally ``persist``.

        Returns:
            ``{"stored": true}`` on success.

        Raises:
            ToolExecutionError: If required fields are missing or storage fails.
        """
        raise NotImplementedError


@dataclass
class MemoryRecallTool:
    """Handler for the ``memory_recall`` tool.

    Attributes:
        memory: The shared ContextManager instance.
    """

    name: str = "memory_recall"
    memory: ContextManager = None  # type: ignore[assignment]

    def run(self, tool_input: dict[str, Any]) -> dict[str, Any]:
        """Recall a value from memory.

        Args:
            tool_input: Must contain ``key``.

        Returns:
            ``{"key": ..., "value": ...}`` — value is ``null`` if not found.

        Raises:
            ToolExecutionError: If ``key`` is missing from *tool_input*.
        """
        raise NotImplementedError


@dataclass
class MemoryListTool:
    """Handler for the ``memory_list`` tool.

    Attributes:
        memory: The shared ContextManager instance.
    """

    name: str = "memory_list"
    memory: ContextManager = None  # type: ignore[assignment]

    def run(self, tool_input: dict[str, Any]) -> dict[str, Any]:
        """List all memory keys.

        Args:
            tool_input: Optionally contains ``include_long_term`` (bool).

        Returns:
            ``{"keys": [...]}``
        """
        raise NotImplementedError


@dataclass
class MemoryDeleteTool:
    """Handler for the ``memory_delete`` tool.

    Attributes:
        memory: The shared ContextManager instance.
    """

    name: str = "memory_delete"
    memory: ContextManager = None  # type: ignore[assignment]

    def run(self, tool_input: dict[str, Any]) -> dict[str, Any]:
        """Delete a key from memory.

        Args:
            tool_input: Must contain ``key``; optionally ``from_long_term``.

        Returns:
            ``{"deleted": true|false}`` indicating whether the key existed.

        Raises:
            ToolExecutionError: If ``key`` is missing from *tool_input*.
        """
        raise NotImplementedError


def build_tool_registry(memory: ContextManager) -> dict[str, Any]:
    """Instantiate all tool handlers and return a name → handler mapping.

    Args:
        memory: Shared ContextManager passed to every handler.

    Returns:
        Dict mapping tool name strings to handler instances.
    """
    raise NotImplementedError
