# Strategy: Research Workflow

A structured approach for investigative tasks where the answer is not yet known.

## Phases

### 1. Survey
- Read existing documentation, code, and prior art.
- Note what is already known and what sources are available.
- Identify the key concepts and their relationships.

### 2. Hypothesise
- List candidate answers or explanations.
- Assign a rough confidence level (high / medium / low) to each.
- Identify the single observation that would best distinguish between them.

### 3. Verify
- Test each hypothesis against evidence (code execution, source review, etc.).
- Update confidence levels based on findings.
- Discard falsified hypotheses; strengthen supported ones.

### 4. Document
- Write a concise summary of findings in `tasks/lessons.md`.
- Include: question → answer → confidence → supporting evidence.
- Note hypotheses that were ruled out and why.

### 5. Act
- Translate verified findings into concrete recommendations or code changes.
- Link each action back to the evidence that justifies it.

## Quality Gates

- Do not proceed from **Hypothesise** to **Verify** with fewer than two
  competing hypotheses — if only one exists, look harder for alternatives.
- Do not proceed from **Verify** to **Document** until at least one hypothesis
  has been confirmed or refuted with evidence.
