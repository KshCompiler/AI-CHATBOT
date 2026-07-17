---
name: readme
description: Use whenever the user asks to commit and push in this project. Before staging, read the project's actual files (dependencies, entry points, notebooks/scripts) and rewrite README.md to fully document the current state of the project, then proceed with commit and push.
---

# README maintenance

Before every commit-and-push, regenerate `README.md` from scratch by reading
the project's current files, so it always fully documents the project as it
stands right now — not as a log of what changed.

## When to act

Any time the user asks to commit and push (or just push, or just commit),
in this project. Run this before staging/committing.

## How to write it

1. **Read the real files first.** Open the dependency files
   (`pyproject.toml`, `requirements.txt`, lockfiles), entry points, and any
   notebooks/scripts to determine what the project actually does and how
   it's actually run right now. Never describe functionality that isn't in
   the code.
2. **Write the full current picture, not a diff.** Treat every regeneration
   as writing the README for the first time: describe the project as it is
   today, in full. Do not phrase anything in terms of before/after,
   previously/now, added/removed, or reference the history of how it got
   this way — a reader should never be able to tell the README was edited
   before.
3. **Structure** (skip sections that don't apply, don't pad):
   - Title + one-sentence description of what the project is.
   - Features / what it does.
   - Tech stack (languages, frameworks, key libraries — pulled from the
     dependency files, not guesswork).
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
   *names*, never values.
5. **Be honest about gaps.** If the project is a work-in-progress notebook
   rather than a packaged app, say so plainly — don't add sections like
   "Contributing" or "License" that don't apply yet.

## After writing

Stage the updated `README.md` along with the other changes being committed,
then proceed with the commit and push as requested. Don't narrate what
changed in the README itself.
