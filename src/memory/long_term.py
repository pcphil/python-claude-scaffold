"""Long-term, file-backed storage that persists across agent sessions."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class LongTermMemory:
    """JSON-file-backed persistent key/value store.

    Data survives process restarts.  The backing file is created on first
    write if it does not already exist.

    Attributes:
        file_path: Path to the JSON file used for persistence.
        _cache: In-process cache of the file contents.
    """

    file_path: Path = field(default_factory=lambda: Path(".memory/long_term.json"))
    _cache: dict[str, Any] = field(default_factory=dict, init=False, repr=False)

    def _load(self) -> None:
        """Load the JSON file into :attr:`_cache`.

        Creates the parent directory and an empty store if the file does not
        exist.
        """
        raise NotImplementedError

    def _save(self) -> None:
        """Persist :attr:`_cache` to :attr:`file_path`."""
        raise NotImplementedError

    def store(self, key: str, value: Any) -> None:  # noqa: ANN401
        """Persist *value* under *key*.

        Args:
            key: Unique identifier for this memory entry.
            value: JSON-serialisable value.
        """
        raise NotImplementedError

    def recall(self, key: str) -> Any:  # noqa: ANN401
        """Retrieve a persisted value by *key*.

        Args:
            key: Identifier used when the value was stored.

        Returns:
            The persisted value, or ``None`` if the key does not exist.
        """
        raise NotImplementedError

    def list_keys(self) -> list[str]:
        """Return all persisted keys.

        Returns:
            Sorted list of key strings.
        """
        raise NotImplementedError

    def delete(self, key: str) -> bool:
        """Remove a persisted key.

        Args:
            key: Key to remove.

        Returns:
            ``True`` if removed, ``False`` if not present.
        """
        raise NotImplementedError
