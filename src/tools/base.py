"""Tool protocols and base exceptions."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


class ToolExecutionError(Exception):
    """Raised when a tool handler fails during execution.

    Attributes:
        tool_name: Name of the tool that failed.
        message: Human-readable description of the failure.
    """

    def __init__(self, tool_name: str, message: str) -> None:
        self.tool_name = tool_name
        self.message = message
        super().__init__(f"[{tool_name}] {message}")


@runtime_checkable
class BaseTool(Protocol):
    """Interface every tool handler must satisfy.

    A tool handler receives the ``input`` dict that Anthropic sends for a
    ``tool_use`` content block and returns a JSON-serialisable result.
    """

    #: Must match the ``name`` field in the tool definition sent to the API.
    name: str

    def run(self, tool_input: dict[str, Any]) -> Any:  # noqa: ANN401
        """Execute the tool with the given inputs.

        Args:
            tool_input: Dict of parameter names → values as sent by the model.

        Returns:
            A JSON-serialisable result forwarded back to the model as a
            ``tool_result`` block.

        Raises:
            ToolExecutionError: If execution fails in a recoverable way.
        """
        ...
