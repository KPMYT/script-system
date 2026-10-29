# TEST: iter-08, the second style round (Scarlett Starling, Diane de Chambray)

All material here is TEST. Run 2026-10-29 by the session 15 chat (branch `claude/stoic-mayer-d4kg3a`) on the operator's word ("good go for a test round then let me know"), with the library at `020409e` (the iter-07 fixes applied; Scarlett's voice provider ElevenLabs). Like for like: two new titles our channels already published, before the library existed, and a rerun of iter-07 run 03 on the same brief and VA turns.

| File | What it is |
|---|---|
| `brief-01.txt`, `brief-02.txt` | The new inputs, written by a helper to the operator's ideation brief spec (`ideation-core` and `style-ideation`, the installed skills), from the title alone: no models, study files or old scripts. |
| `brief-03.txt` | iter-07's `brief-03.txt`, unchanged (the rerun). |
| `rotation-log-scarlett.txt`, `rotation-log-diane.txt` | The rotation logs the VA pasted in runs 01 and 02: the ROTATION LOG ENTRY lines of iter-07's runs 01-02 (Scarlett) and run 03 (Diane), as a channel's earlier scripts. Run 03 used "none", as in iter-07. |
| `refs/` | The reference transcripts (judge only): our own old scripts on the same titles (`yl-Vq9WyLzY` jeans, 12,620 views; `egJ5B6d879c` French haircuts, 2,911; `ISAL4NBlshQ` French frumpy, 3,826) and a winner per run (M26 Diana GOSS, 1.35M; M07 Glam Girl Gabi, 1.9M; M21 Marie-Anne Lecoeur, 1.04M). |
| `va-turn-plans.md` | The VA's turns (the operator helper): a first name only and a missing title (run 01), the channel on the START line and "just write it, skip the log" (run 02), iter-07 run 03's turns word for word (run 03). |
| `judge-rubric.md` | The judge's rubric, copied from iter-07 with the runs, references and iter-07 fixes updated, plus an unscored check of the chat and the rotation. The writer never saw it. |
| `CHANGES.md` | The results (118, 117 and 124 of 140 against 60-65 for our old scripts), the library fixes the judges name (M1-M9, T1, proposed) and the writer slips. |
| `test-run-01/` (Scarlett, jeans), `test-run-02/` (Diane, French haircuts), `test-run-03/` (Diane, frumpy rerun) | Each run: `chat.md` (the VA's turns and the chat's replies, word for word), `output.md`, `script.txt`, `scanner-main-session.txt` (with `verify_output.py`), `judge-report.md`. |

How it ran (`CLAUDE.md`, "Testing with subagents"), as iter-07:
- **The skills:** built by `tools/build_skills.py` from a scratch copy of the library in which both channels read "ready" (TEST only: in the library they stay pending). Each writer got only `script-writer`, `style-scripts` and the channel's persona skill.
- **Writer:** a helper reading only those built skills and running their scanner, as a VA's claude.ai chat would; each VA turn relayed word for word by the main session.
- **Judge:** a helper with the rubric, the main session's scanner and verifier results, the brief, the pack, the hook bank, the profile, the book index and the reference transcripts.
