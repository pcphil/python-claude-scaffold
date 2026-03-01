# Example Skill

**Name:** `example`

## Purpose

A minimal reference implementation of `BaseSkill`.  Fork this file and
`skill.py` to add a new capability to the agent.

## Inputs (context keys)

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `input` | `str` | Yes | The text to echo back. |

## Output

Returns the input string prefixed with `[example] `.

## Usage

```python
from src.skills.example.skill import ExampleSkill

skill = ExampleSkill()
result = skill.run({"input": "hello"})
# → "[example] hello"
```
