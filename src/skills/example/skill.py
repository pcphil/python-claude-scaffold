"""Example skill — minimal reference implementation of BaseSkill."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ExampleSkill:
    """Echoes the ``input`` context key back with a ``[example]`` prefix.

    This class exists solely as a copy-paste template.  Replace the body of
    :meth:`run` with real logic when forking.

    Attributes:
        name: Skill identifier used by the skill loader.
        description: Short description shown in logs.
    """

    name: str = "example"
    description: str = "Echoes the input context key back with a [example] prefix."

    def run(self, context: dict[str, Any]) -> str:
        """Return the context ``input`` value prefixed with ``[example] ``.

        Args:
            context: Must contain an ``input`` key with a string value.

        Returns:
            ``[example] {context['input']}``

        Raises:
            NotImplementedError: Always — replace with real logic.
        """
        raise NotImplementedError
