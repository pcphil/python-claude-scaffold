"""Short-term, in-memory storage for the current agent session."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ShortTermMemory:
    """Session-scoped in-memory key/value store.

    All data is lost when the process exits.  Use :class:`LongTermMemory`
    for values that must survive across sessions.

    Attributes:
        _store: Internal dict backing the memory.
    """

    _store: dict[str, Any] = field(default_factory=dict, init=False, repr=False)

    def store(self, key: str, value: Any) -> None:  # noqa: ANN401
        """Store *value* under *key* in the session.

        Args:
            key: Unique identifier for this memory entry.
            value: Arbitrary JSON-serialisable value.
        """
        raise NotImplementedError

    def recall(self, key: str) -> Any:  # noqa: ANN401
        """Retrieve a value by *key*.

        Args:
            key: Identifier used when the value was stored.

        Returns:
            The stored value, or ``None`` if the key is absent.
        """
        raise NotImplementedError

    def list_keys(self) -> list[str]:
        """Return all keys held in short-term memory.

        Returns:
            Sorted list of key strings.
        """
        raise NotImplementedError

    def delete(self, key: str) -> bool:
        """Remove *key* from memory.

        Args:
            key: Key to remove.

        Returns:
            ``True`` if removed, ``False`` if not present.
        """
        raise NotImplementedError

    def clear(self) -> None:
        """Remove all entries from short-term memory."""
        raise NotImplementedError
