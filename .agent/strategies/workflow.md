# Strategy: Default Workflow

A general-purpose workflow for tackling ambiguous or multi-step tasks.

## Phases

### 1. Plan
- Restate the goal in your own words.
- Identify unknowns and list the questions that must be answered first.
- Break the goal into a concrete, ordered task list.
- Spawn sub-agents or use tools to gather missing information.

### 2. Sub-agents
- Delegate parallel, independent sub-tasks where possible.
- Each sub-agent receives a scoped, self-contained prompt.
- Collect and reconcile results before proceeding.

### 3. Lessons
- After completing a task (or a significant sub-task), write a one-line lesson
  to `tasks/lessons.md` in the format:
  ```
  - [YYYY-MM-DD] <what went wrong or what worked well>
  ```
- Review `tasks/lessons.md` at the start of similar future tasks.

### 4. Prove
- Verify the outcome against the original goal.
- Run tests, linters, or any other automated checks.
- If verification fails, loop back to **Plan** with updated information.

## Heuristics

- Prefer reversible actions over irreversible ones.
- When in doubt, ask the user before taking a destructive step.
- Write the simplest code that satisfies the goal; optimise only when measured.
