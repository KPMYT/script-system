# TEST: iter-05, the first electrical test (Frederick Barnes)

All material here is TEST. Run 2026-10-27 by the electrical scripting chat (session 10), after P13 was applied and Frederick marked ready.

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

## Result of run 01 (judge, 2026-10-27)

**Fix, then pass; not uploaded as delivered.** Safe and accurate (every figure traces to the brief or the facts guide), well ahead of the reference on safety, stakes, CTA and ending, but from about 6:30 it reads like a manual, and the prove-dead step has gaps. Scores, script against reference: opening 8/5, promises 8/7, clarity 6/6, number load 9/6, stakes 8/4, safety 6/4, voice 8/6, written for the voice 9, CTA and ending 9/3, length 7/6, originality 8, emotion 7/5, audit honesty 8. The chat refused "just write it" and the missing rotation log correctly.

The main session's check of the report: L1 (prove-dead order), L2 (the store step before the look inside, script line 109) and L3 (lines 11 and 196 echo the pack's own example lines) are confirmed against the script and `electrical-scripts/SKILL.md`. **L9 is wrong:** the VA pasted only the brief paragraph, never the "REFERENCE (judge only)" line (`chat.md` turn 4 now says so plainly). The library fixes L1-L8 wait for the operator's yes.
