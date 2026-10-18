# refs-01: reference excerpts, reference scripts and the copy guard

Started 2026-10-18. Every file touched in this iteration, in order. Previous versions stay in git history; nothing was deleted.

| File | What changed | Why |
|---|---|---|
| `../../CLAUDE.md` (repo root) | Added the script-library exception: edits allowed inside `script-library/` for this phase; `data/` and `notes/` stay collect-and-describe only. Added `script-library/` to the structure list. | User instruction for the new phase. |
| `core/script-scanner.py` | Task 4: added optional `--refs FILE...`. Any run of 8+ consecutive words in the spoken script that also appears in a reference file is fix-on-sight `[COPIED FROM REFERENCE: file]`. Case, punctuation and `[bracketed]` tags are ignored; overlapping runs merge into one finding. Usage docstring and exit-code note updated. | Copy guard: reference files are for shape and pacing, never wording. |
| `tests/run_checks.py` | Task 4: `run_scan()` takes `refs`; added checks 12 (copied line caught, case/punctuation ignored), 12b (under 8 shared words not flagged), 12c (the clean test script passes against the pack's real reference files), 12d (a line lifted from the pack's own reference file is caught). Removed a dangling "# 12." comment that had no check under it. | Task 4 tests. Suite: 17/17 passing. |
