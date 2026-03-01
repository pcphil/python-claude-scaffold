"""Unit tests for the tools layer — stubs raise NotImplementedError."""

from __future__ import annotations

import pytest

from src.tools.definitions import TOOL_DEFINITIONS
from src.tools.handlers import (
    MemoryDeleteTool,
    MemoryListTool,
    MemoryRecallTool,
    MemoryStoreTool,
    build_tool_registry,
)


class TestToolDefinitions:
    def test_all_four_tools_defined(self) -> None:
        names = {t["name"] for t in TOOL_DEFINITIONS}
        assert names == {"memory_store", "memory_recall", "memory_list", "memory_delete"}

    def test_each_definition_has_input_schema(self) -> None:
        for defn in TOOL_DEFINITIONS:
            assert "input_schema" in defn
            assert defn["input_schema"]["type"] == "object"

    def test_memory_store_requires_key_and_value(self) -> None:
        store_def = next(d for d in TOOL_DEFINITIONS if d["name"] == "memory_store")
        assert "key" in store_def["input_schema"]["required"]
        assert "value" in store_def["input_schema"]["required"]


class TestMemoryStoreTool:
    def test_run_raises(self) -> None:
        tool = MemoryStoreTool()
        with pytest.raises(NotImplementedError):
            tool.run({"key": "k", "value": "v"})

    def test_name(self) -> None:
        assert MemoryStoreTool().name == "memory_store"


class TestMemoryRecallTool:
    def test_run_raises(self) -> None:
        tool = MemoryRecallTool()
        with pytest.raises(NotImplementedError):
            tool.run({"key": "k"})

    def test_name(self) -> None:
        assert MemoryRecallTool().name == "memory_recall"


class TestMemoryListTool:
    def test_run_raises(self) -> None:
        tool = MemoryListTool()
        with pytest.raises(NotImplementedError):
            tool.run({})

    def test_name(self) -> None:
        assert MemoryListTool().name == "memory_list"


class TestMemoryDeleteTool:
    def test_run_raises(self) -> None:
        tool = MemoryDeleteTool()
        with pytest.raises(NotImplementedError):
            tool.run({"key": "k"})

    def test_name(self) -> None:
        assert MemoryDeleteTool().name == "memory_delete"


def test_build_tool_registry_raises() -> None:
    from src.memory.context_manager import ContextManager

    with pytest.raises(NotImplementedError):
        build_tool_registry(ContextManager())
