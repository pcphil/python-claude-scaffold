"""Memory protocols: short-term and long-term storage interfaces."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class ShortTermMemoryProtocol(Protocol):
    """In-memory, session-scoped key/value store."""

    def store(self, key: str, value: Any) -> None:  # noqa: ANN401
        """Store a value under *key* for the current session.

        Args:
            key: Unique identifier for this memory entry.
            value: Arbitrary value to store; must be JSON-serialisable.
        """
        ...

    def recall(self, key: str) -> Any:  # noqa: ANN401
        """Retrieve a previously stored value by *key*.

        Args:
            key: Identifier used when the value was stored.

        Returns:
            The stored value, or ``None`` if the key does not exist.
        """
        ...

    def list_keys(self) -> list[str]:
        """Return all keys currently held in short-term memory.

        Returns:
            Sorted list of key strings.
        """
        ...

    def delete(self, key: str) -> bool:
        """Remove a key from short-term memory.

        Args:
            key: Key to remove.

        Returns:
            ``True`` if the key existed and was removed, ``False`` otherwise.
        """
        ...

    def clear(self) -> None:
        """Remove all entries from short-term memory."""
        ...


@runtime_checkable
class LongTermMemoryProtocol(Protocol):
    """Persistent, file-backed key/value store (JSON)."""

    def store(self, key: str, value: Any) -> None:  # noqa: ANN401
        """Persist a value under *key*.

        Args:
            key: Unique identifier for this memory entry.
            value: JSON-serialisable value.
        """
        ...

    def recall(self, key: str) -> Any:  # noqa: ANN401
        """Retrieve a persisted value by *key*.

        Args:
            key: Identifier used when the value was stored.

        Returns:
            The persisted value, or ``None`` if the key does not exist.
        """
        ...

    def list_keys(self) -> list[str]:
        """Return all persisted keys.

        Returns:
            Sorted list of key strings.
        """
        ...

    def delete(self, key: str) -> bool:
        """Remove a persisted key.

        Args:
            key: Key to remove.

        Returns:
            ``True`` if the key existed and was removed, ``False`` otherwise.
        """
        ...
