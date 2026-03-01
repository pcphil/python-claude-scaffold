"""AgentSkillLoader — discovers and loads skills from .agent/ Markdown files."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class AgentSkillLoader:
    """Loads declarative Markdown skills from the ``.agent/`` directory.

    Each ``.md`` file under ``.agent/skills/`` is read and its content is
    made available as a system-prompt fragment that the agent can inject.

    Attributes:
        agent_dir: Path to the ``.agent/`` directory (default: ``.agent``).
        _loaded: Mapping of skill name → Markdown content, populated by
            :meth:`load`.
    """

    agent_dir: Path = field(default_factory=lambda: Path(".agent"))
    _loaded: dict[str, str] = field(default_factory=dict, init=False, repr=False)

    def load(self) -> dict[str, str]:
        """Discover and read all skill Markdown files.

        Walks ``agent_dir/skills/`` and reads every ``*.md`` file.  The stem
        of the filename becomes the skill name.

        Returns:
            Mapping of ``skill_name`` → raw Markdown string.

        Raises:
            NotImplementedError: Always — implement to populate :attr:`_loaded`.
        """
        raise NotImplementedError

    def get(self, name: str) -> str | None:
        """Return the Markdown content for a named skill.

        Args:
            name: Stem of the ``.md`` file (e.g. ``"chain_of_thought"``).

        Returns:
            Raw Markdown string, or ``None`` if the skill is not loaded.
        """
        raise NotImplementedError

    def list_skills(self) -> list[str]:
        """Return all loaded skill names.

        Returns:
            Sorted list of skill name strings.
        """
        raise NotImplementedError

    def as_system_prompt_fragment(self, names: list[str] | None = None) -> str:
        """Compose loaded skills into a single system-prompt string.

        Args:
            names: Subset of skill names to include.  Defaults to all loaded
                skills when ``None``.

        Returns:
            Concatenated Markdown content separated by ``---`` dividers.
        """
        raise NotImplementedError
