# Skills

Skills are modular, composable capabilities that extend the agent's behaviour.
There are two kinds:

## 1. Prompt Skills (`.agent/skills/*.md`)

Declarative Markdown files loaded by `AgentSkillLoader` and injected into the
system prompt.  They describe *how* the model should reason or respond.

Examples: `chain_of_thought.md`, `self_critique.md`

## 2. Code Skills (`src/skills/*/skill.py`)

Python classes that implement the `BaseSkill` Protocol.  They execute logic and
return a string contribution to the next prompt.

Examples: `src/skills/example/skill.py`

## Adding a Prompt Skill

1. Create `.agent/skills/<name>.md`.
2. Write clear, actionable instructions (see existing skills for format).
3. Activate via `--skill <name>` on the CLI or `AgentConfig.skills`.

## Adding a Code Skill

1. Create `src/skills/<name>/` with `__init__.py`, `skill.py`, and `SKILL.md`.
2. Implement `BaseSkill` in `skill.py`.
3. Add a test in `tests/unit/`.
4. Register in the skill loader (once `skill_loader.py` is implemented).
