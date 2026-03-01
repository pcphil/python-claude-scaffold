"""Shared pytest fixtures."""

from __future__ import annotations

import os
from unittest.mock import MagicMock

import pytest


@pytest.fixture()
def anthropic_api_key() -> str:
    """Return the Anthropic API key, skipping the test if absent.

    Yields:
        The value of the ``ANTHROPIC_API_KEY`` environment variable.
    """
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key:
        pytest.skip("ANTHROPIC_API_KEY not set — skipping integration test")
    return key


@pytest.fixture()
def mock_client() -> MagicMock:
    """Return a MagicMock standing in for ``anthropic.Anthropic``.

    The mock's ``messages.create`` method returns a minimal response object
    with ``stop_reason = "end_turn"`` and a single text content block.
    """
    client = MagicMock()
    response = MagicMock()
    response.stop_reason = "end_turn"
    content_block = MagicMock()
    content_block.type = "text"
    content_block.text = "Mock response"
    response.content = [content_block]
    client.messages.create.return_value = response
    return client
