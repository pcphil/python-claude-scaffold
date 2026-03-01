"""Anthropic tool definitions for the built-in memory tools."""

from __future__ import annotations

from typing import Any

# Each entry is a dict conforming to the Anthropic ``Tool`` schema.
# Pass this list as the ``tools=`` argument when creating a message.
TOOL_DEFINITIONS: list[dict[str, Any]] = [
    {
        "name": "memory_store",
        "description": (
            "Store a value in agent memory under a given key. "
            "Use persist=true to write to long-term (file-backed) storage."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "Unique identifier for this memory entry.",
                },
                "value": {
                    "description": "JSON-serialisable value to store.",
                },
                "persist": {
                    "type": "boolean",
                    "description": "Write to long-term storage when true. Defaults to false.",
                    "default": False,
                },
            },
            "required": ["key", "value"],
        },
    },
    {
        "name": "memory_recall",
        "description": (
            "Retrieve a previously stored value by key. "
            "Returns null if the key does not exist."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "Key to look up.",
                },
            },
            "required": ["key"],
        },
    },
    {
        "name": "memory_list",
        "description": "List all keys currently held in agent memory.",
        "input_schema": {
            "type": "object",
            "properties": {
                "include_long_term": {
                    "type": "boolean",
                    "description": "Include long-term storage keys. Defaults to true.",
                    "default": True,
                },
            },
            "required": [],
        },
    },
    {
        "name": "memory_delete",
        "description": "Delete a key from agent memory.",
        "input_schema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "Key to delete.",
                },
                "from_long_term": {
                    "type": "boolean",
                    "description": "Also delete from long-term storage. Defaults to false.",
                    "default": False,
                },
            },
            "required": ["key"],
        },
    },
]
