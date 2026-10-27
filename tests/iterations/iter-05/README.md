# TEST: iter-05, the first electrical test (Frederick Barnes)

All material here is TEST. Run 2026-10-27 by the electrical scripting chat (session 9), after P13 was applied and Frederick marked ready.

| File | What it is |
|---|---|
| `brief-A12.txt` | The input: idea A12, "The REAL Reason Your Plug Won't Stay In The Outlet", and its brief, copied from `KPMYT/niche-research` `studies/electrical/ideation/briefs-2026-10-27.tsv` (row 4, main at 9262565). Rotation log: none. |
| `refs/0h_r2bD5bMs-transcript.txt` | The reference video (judge only): Everyday Home Repairs, "Plug Won't Stay In Outlet", 2.5M views, the same topic. It is also model E08 in the library, so the writer could study its beats (never its wording). |
| `judge-rubric.md` | The judge's rubric (the writer never saw it). |
| `test-run-01/` | The run: `chat.md` (the VA's turns and the chat's replies), `plan.md` (the writer's unit plan), `output.md` (the full output as delivered, VO copy included), `script.txt` (the script alone), `scanner-main-session.txt` (the scanner, run by the main session with `--final` and every copy-guard file), `verify-output.txt` (`tools/verify_output.py`), `judge-report.md`. |

How it ran (`CLAUDE.md`, "Testing with subagents"):
- **Writer:** a helper that could read only the three built skills (`script-writer`, `electrical-scripts`, `frederick-barnes-persona`, copied from `dist/` at build 518f0ea) and run their scanner, as a VA's claude.ai chat would.
- **Operator:** a helper playing the VA, who typed START, picked Frederick, then tried "just write it" with only the title, then left out the rotation log, before giving all three inputs. The main session relayed each message word for word.
- **Judge:** a helper with the rubric, the scanner and verifier results, the brief, the facts guide and the reference transcript.
