"""Unified memory interface combining short-term and long-term stores."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from src.memory.long_term import LongTermMemory
from src.memory.short_term import ShortTermMemory


@dataclass
class ContextManager:
    """Unified facade over short-term and long-term memory.

    Provides a single interface for agent code to read and write memory
    without coupling to a specific backing store.  Short-term memory is
    always queried first; long-term is the fallback.

    Attributes:
        short_term: Session-scoped in-memory store.
        long_term: Persistent file-backed store.
    """

    short_term: ShortTermMemory = field(default_factory=ShortTermMemory)
    long_term: LongTermMemory = field(default_factory=LongTermMemory)

    def store(self, key: str, value: Any, *, persist: bool = False) -> None:  # noqa: ANN401
        """Store *value* under *key*.

        Args:
            key: Unique identifier for this memory entry.
            value: JSON-serialisable value.
            persist: When ``True``, write to long-term storage in addition to
                short-term.
        """
        raise NotImplementedError

    def recall(self, key: str) -> Any:  # noqa: ANN401
        """Retrieve a value, checking short-term then long-term.

        Args:
            key: Identifier to look up.

        Returns:
            The value if found in either store, otherwise ``None``.
        """
        raise NotImplementedError

    def list_keys(self, *, include_long_term: bool = True) -> list[str]:
        """Return all known keys.

        Args:
            include_long_term: When ``True``, merge keys from both stores.

        Returns:
            Sorted, deduplicated list of key strings.
        """
        raise NotImplementedError

    def delete(self, key: str, *, from_long_term: bool = False) -> bool:
        """Remove *key* from memory.

        Args:
            key: Key to remove.
            from_long_term: When ``True``, also remove from long-term storage.

        Returns:
            ``True`` if the key was present in at least one store.
        """
        raise NotImplementedError
