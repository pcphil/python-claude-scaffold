"""CLI entry point: parses arguments and invokes AgentLoop."""

from __future__ import annotations

import argparse
import sys

from dotenv import load_dotenv

from src.agent.loop import AgentConfig, AgentLoop


def build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser for the ``claude-agent`` CLI.

    Returns:
        Configured :class:`argparse.ArgumentParser`.
    """
    parser = argparse.ArgumentParser(
        prog="claude-agent",
        description="Run a Claude-powered agent from the command line.",
    )
    parser.add_argument(
        "message",
        nargs="?",
        help="Initial user message.  If omitted, enters an interactive REPL.",
    )
    parser.add_argument(
        "--model",
        default="claude-sonnet-4-6",
        help="Anthropic model ID (default: claude-sonnet-4-6).",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=4096,
        dest="max_tokens",
        help="Maximum tokens per response (default: 4096).",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=10,
        dest="max_iterations",
        help="Maximum tool-use rounds (default: 10).",
    )
    parser.add_argument(
        "--skill",
        action="append",
        dest="skills",
        default=[],
        metavar="SKILL",
        help="Activate a named skill (may be repeated).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entry point.

    Loads ``.env``, builds an :class:`AgentLoop`, and either runs a single
    message or starts an interactive REPL.

    Args:
        argv: Argument list (defaults to :data:`sys.argv`).

    Returns:
        Exit code (0 on success, 1 on error).

    Raises:
        NotImplementedError: Always — implement the REPL and single-shot paths.
    """
    load_dotenv()
    parser = build_parser()
    args = parser.parse_args(argv)

    config = AgentConfig(
        model=args.model,
        max_tokens=args.max_tokens,
        max_iterations=args.max_iterations,
        skills=args.skills,
    )
    _loop = AgentLoop(config=config)  # noqa: F841

    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(main())
