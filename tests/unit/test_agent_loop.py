"""Unit tests for AgentLoop — verifies stubs raise NotImplementedError."""

from __future__ import annotations

import pytest

from src.agent.loop import AgentConfig, AgentLoop


def test_setup_raises() -> None:
    """AgentLoop.setup() must raise NotImplementedError until implemented."""
    loop = AgentLoop()
    with pytest.raises(NotImplementedError):
        loop.setup()


def test_run_raises() -> None:
    """AgentLoop.run() must raise NotImplementedError until implemented."""
    loop = AgentLoop()
    with pytest.raises(NotImplementedError):
        loop.run("hello")


def test_reset_raises() -> None:
    """AgentLoop.reset() must raise NotImplementedError until implemented."""
    loop = AgentLoop()
    with pytest.raises(NotImplementedError):
        loop.reset()


def test_default_config() -> None:
    """AgentConfig defaults are sane."""
    config = AgentConfig()
    assert config.model == "claude-sonnet-4-6"
    assert config.max_tokens == 4096
    assert config.max_iterations == 10
    assert config.skills == []


def test_loop_accepts_config(mock_client: object) -> None:
    """AgentLoop can be constructed with a custom AgentConfig."""
    config = AgentConfig(model="claude-haiku-4-5-20251001", max_tokens=1024)
    loop = AgentLoop(config=config)
    assert loop.config.model == "claude-haiku-4-5-20251001"
    assert loop.config.max_tokens == 1024
