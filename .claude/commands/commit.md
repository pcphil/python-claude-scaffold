---
allowed-tools: Bash
argument-hint: "[optional: commit message override]"
---

# /commit — Create a Conventional Commit

Create a well-formed commit for all staged (and optionally unstaged) changes.

## Steps

1. Run `git status` and `git diff --cached` to review what is staged.
2. If nothing is staged, run `git diff` to see unstaged changes and ask the
   user which files to stage.
3. Analyse the diff and draft a commit message following
   [Conventional Commits](https://www.conventionalcommits.org/):
   ```
   <type>(<scope>): <short summary>

   [optional body]

   Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
   ```
   Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `build`, `ci`.
4. If `$ARGUMENTS` is provided, use it as the commit message summary instead.
5. Stage any unstaged files the user confirmed in step 2.
6. Run `git commit -m "$(cat <<'EOF'\n...\nEOF\n)"` with the drafted message.
7. Confirm success with `git log --oneline -1`.
