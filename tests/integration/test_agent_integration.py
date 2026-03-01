"""Integration tests — skipped unless ANTHROPIC_API_KEY is set."""

from __future__ import annotations

import pytest

from src.agent.loop import AgentConfig, AgentLoop


@pytest.mark.integration
def test_agent_loop_end_to_end(anthropic_api_key: str) -> None:
    """Full round-trip: single user message → text response.

    This test is skipped automatically when ANTHROPIC_API_KEY is absent
    (see conftest.py).

    Once AgentLoop is implemented, this test verifies:
    - setup() completes without error
    - run() returns a non-empty string
    - reset() leaves the loop ready for another run
    """
    config = AgentConfig(
        model="claude-haiku-4-5-20251001",
        max_tokens=256,
        max_iterations=3,
    )
    loop = AgentLoop(config=config)

    # All stubs raise NotImplementedError — update assertions as you implement.
    with pytest.raises(NotImplementedError):
        loop.setup()
