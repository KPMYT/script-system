# TEST: iter-07, the first style tests (Scarlett Starling, Diane de Chambray)

All material here is TEST. Run 2026-10-29 by the session 14 chat (branch `claude/youthful-ritchie-zq7e92`) on the operator's word ("yes run a test"), with the library at the commit after `81b` (the style pack, both profiles, the hook bank, both book indexes). Like for like: three titles our channels already published, before the library existed.

| File | What it is |
|---|---|
| `brief-01.txt`, `brief-02.txt`, `brief-03.txt` | The inputs, written by a helper to the operator's ideation brief spec (`ideation-core` §4 and `style-ideation`), from the title alone: no models, study files or old scripts. The operator's sheet holds no briefs for these titles. Rotation log: none. |
| `refs/` | The reference transcripts (judge only): our own old scripts on the same titles (`w6w_ktMBHXM` necklaces, 39,935 views; `h9MsF44shdQ` bob, 514; `ISAL4NBlshQ` French frumpy, 3,826) and a winner per run (F01 Vivian Sinclair's glasses list, structure only; M12 Justin Hickox's bob, 3.2M; M21 Marie-Anne Lecoeur's "Scream 'Old Lady'", 1.04M). |
| `va-turn-plans.md` | The VA's turns (the operator helper). |
| `CHANGES.md` | The results (117, 121, 116 of 140 against 65-68 for our old scripts), the library fixes the judges name (L1-L13, proposed) and the writer slips. |
| `judge-rubric.md` | The judge's rubric (the writer never saw it). The hook is double-weighted (operator, 2026-10-29). |
| `test-run-01/` (Scarlett, necklaces), `test-run-02/` (Scarlett, bob), `test-run-03/` (Diane, frumpy) | Each run: `chat.md` (the VA's turns and the chat's replies, word for word), `output.md`, `script.txt`, `scanner-main-session.txt`, `judge-report.md`. |

How it runs (`CLAUDE.md`, "Testing with subagents"):
- **The skills:** built by `tools/build_skills.py` from a copy of the library in which both channels read "ready" (TEST only: in the library they stay pending). The writer gets only `script-writer`, `style-scripts` and the channel's persona skill.
- **Writer:** a helper that reads only those built skills and runs their scanner, as a VA's claude.ai chat would.
- **Operator:** a helper playing the VA, with mistakes (a missing input, "just write it", a vague channel name). The main session relays each message word for word.
- **Judge:** a helper with the rubric, the scanner results, the brief, the pack, the hook bank, the profile and the reference transcripts.
