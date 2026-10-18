# Changelog

Every change to the library, newest first. Format: date | files | what changed | why.

Earlier history: the script-library phase before this file existed is logged in `tests/iterations/refs-01/CHANGES.md`, and everything is in git history.

| Date | Files | What changed | Why |
|---|---|---|---|
| 2026-10-18 | `CHANGELOG.md`, `PROPOSALS.md` (new) | Created both files. `PROPOSALS.md` starts with one open item, P1, from the iter-00 audit. | `CLAUDE.md` working rules 1 and 2. |
| 2026-10-18 | `tests/iterations/iter-00/AUDIT.md` (new) | Audit of the library against itself, `HANDOFF.md` section 3 and `archive/facelessos-original/`. Findings only; nothing fixed. Test run recorded in it: `python3 tests/run_checks.py`, 17/17 passed. | Operator's task: audit before any fixes. |
| 2026-10-18 | whole repo (moves only) | **Study moved:** `data/`, `notes/`, `inputs/`, `log.md` and `transcripts-combined/` to `studies/woodworking/` with `git mv`, contents unchanged. The old study instructions (the root `CLAUDE.md` before the operator's upload replaced it, recovered from commit `531cf51`) were saved unchanged as `studies/woodworking/study-brief.md`. **Library to the root:** `script-library/core/`, `woodworking-scripts/`, `personas/`, `tests/`, `PINNED.md` and `README.md` moved to the repo root; `script-library/iterations/refs-01/` moved to `tests/iterations/refs-01/`. **Archive:** `script-system-repo-upload/archive/facelessos-original/` moved to `archive/facelessos-original/`. **Duplicates removed:** the rest of `script-system-repo-upload/` was removed with `git rm`. Its `CLAUDE.md`, `HANDOFF.md`, `PINNED.md` and `README.md` were byte-identical to the root copies; its library files were the same as `script-library/`'s, or older (no copy guard in `script-scanner.py` and `run_checks.py`, no `reference-scripts.md`, no `archive/most-viewed-24mo/`). They stay in git history at commit `85e06e7`. | New layout in `CLAUDE.md`: library at the root, research in `studies/`, originals in `archive/`. The GitHub upload had landed in a `script-system-repo-upload/` subfolder next to the newer `script-library/`. |
