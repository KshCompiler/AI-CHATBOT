---
name: readme
description: Use whenever meaningful changes land in this project (new dependencies, new files/modules, changed setup steps, new features) to write or update README.md so it accurately documents the project like a senior engineer's onboarding doc. Trigger on requests like "update the readme", "document this", "write a readme", or proactively right before a commit that changes project structure, dependencies, or usage.
---

# README maintenance

Keep `README.md` at the project root accurate, current, and written the way a
senior engineer would document a real project for a new teammate — clear,
concrete, no fluff, no invented features.

## When to act

- User explicitly asks for a README to be written or updated.
- You are about to commit changes that alter: dependencies (`pyproject.toml`,
  `requirements.txt`, lockfiles), project structure (new top-level
  files/folders), setup/run steps, environment variables, or the project's
  actual functionality.
- Do NOT rewrite the README for trivial changes (typo fixes, comment edits,
  formatting) — only when something a reader relies on actually changed.

## How to write it

1. **Survey before writing.** Read the actual dependency files, entry points,
   and any notebooks/scripts to determine what the project really does and
   how it's actually run. Never describe functionality that isn't in the
   code yet.
2. **Update in place, don't start over.** If `README.md` already has
   sections, preserve accurate ones and only revise what changed — diff
   mentally against current project state rather than regenerating from
   scratch each time.
3. **Structure** (skip sections that don't apply, don't pad):
   - Title + one-sentence description of what the project is.
   - Features / what it does.
   - Tech stack (languages, frameworks, key libraries — pull from the
     dependency file, not guesswork).
   - Prerequisites (Python version from `.python-version` or
     `requires-python`, package manager in use — e.g. `uv` if a `uv.lock`
     is present).
   - Setup / installation steps that actually work with this repo's tooling
     (e.g. `uv sync` if uv-managed, not `pip install` unless that's really
     the flow).
   - Environment variables required (name them, e.g. `GROQ_API_KEY` in
     `.env` — never include real values, only placeholders).
   - Usage — a real, runnable example based on actual entry points/cells.
   - Project structure — a short annotated file tree of what matters.
4. **Never leak secrets.** If a `.env` exists, only ever reference variable
   *names*, never values, when documenting it.
5. **Be honest about gaps.** If the project is a work-in-progress notebook
   rather than a packaged app, say so — don't inflate it with sections like
   "Contributing" or "License" that don't apply yet.

## After writing

Mention in your response what changed in the README and why (e.g. "added
the Groq setup section since we just wired up the LLM"), so the user can
spot-check accuracy rather than trusting it blindly.
