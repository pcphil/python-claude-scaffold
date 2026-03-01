"""Unit tests for the memory layer — stubs raise NotImplementedError."""

from __future__ import annotations

import pytest

from src.memory.context_manager import ContextManager
from src.memory.long_term import LongTermMemory
from src.memory.short_term import ShortTermMemory


class TestShortTermMemory:
    def test_store_raises(self) -> None:
        mem = ShortTermMemory()
        with pytest.raises(NotImplementedError):
            mem.store("key", "value")

    def test_recall_raises(self) -> None:
        mem = ShortTermMemory()
        with pytest.raises(NotImplementedError):
            mem.recall("key")

    def test_list_keys_raises(self) -> None:
        mem = ShortTermMemory()
        with pytest.raises(NotImplementedError):
            mem.list_keys()

    def test_delete_raises(self) -> None:
        mem = ShortTermMemory()
        with pytest.raises(NotImplementedError):
            mem.delete("key")

    def test_clear_raises(self) -> None:
        mem = ShortTermMemory()
        with pytest.raises(NotImplementedError):
            mem.clear()


class TestLongTermMemory:
    def test_store_raises(self, tmp_path: object) -> None:
        from pathlib import Path

        mem = LongTermMemory(file_path=Path(str(tmp_path)) / "mem.json")  # type: ignore[arg-type]
        with pytest.raises(NotImplementedError):
            mem.store("key", "value")

    def test_recall_raises(self, tmp_path: object) -> None:
        from pathlib import Path

        mem = LongTermMemory(file_path=Path(str(tmp_path)) / "mem.json")  # type: ignore[arg-type]
        with pytest.raises(NotImplementedError):
            mem.recall("key")


class TestContextManager:
    def test_store_raises(self) -> None:
        ctx = ContextManager()
        with pytest.raises(NotImplementedError):
            ctx.store("key", "value")

    def test_recall_raises(self) -> None:
        ctx = ContextManager()
        with pytest.raises(NotImplementedError):
            ctx.recall("key")

    def test_list_keys_raises(self) -> None:
        ctx = ContextManager()
        with pytest.raises(NotImplementedError):
            ctx.list_keys()

    def test_delete_raises(self) -> None:
        ctx = ContextManager()
        with pytest.raises(NotImplementedError):
            ctx.delete("key")
