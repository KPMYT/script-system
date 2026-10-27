# TEST: iter-06, the first HVAC tests (Roger the HVAC Guy)

All material here is TEST. Run 2026-10-27 by the HVAC research chat, with the library at commit c2f2919 (the HVAC pack, Roger the HVAC Guy's profile and the HVAC price guide). The number iter-06 skips iter-05, which the electrical chat used on its own branch.

| File | What it is |
|---|---|
| `brief-04.txt`, `brief-14.txt` | The inputs: batch 1 #4 "11 Furnace Mistakes HVAC Companies Hope You Keep Making" and #14 "Furnace Keeps Shutting Off? The $12 Part Techs Charge $300 to Replace (Clean It Yourself)", from `KPMYT/niche-research` `studies/hvac/ideation/batch1-briefs-2026-10-27-corrected.tsv` (the briefs with the price research's corrections). Rotation log: none. |
| `refs/` | The reference transcripts (judge only): `qbWN3OViWxQ` (Ray Dutton's Garage, "5 AC Mistakes HVAC Companies Hope You Keep Making", #4's source title; faceless, never a model) and `3Jonl_TLkpE` (Word of Advice TV, "Furnace Not Working - The Most Common Fix", the flame-sensor fix; also model R28). |
| `judge-rubric.md` | The judge's rubric (the writer never saw it). |
| `test-run-01/` (#4), `test-run-02/` (#14) | Each run: `chat.md` (the VA's turns and the chat's replies, word for word), `output.md` (the full output as delivered), `script.txt` (the script alone), `scanner-main-session.txt` (the scanner, run by the main session with every copy-guard file), `judge-report.md`. |

How it ran (`CLAUDE.md`, "Testing with subagents"):
- **The skills:** built by `tools/build_skills.py` from a copy of the library in which Roger the HVAC Guy's profile and channel row read "ready" (TEST only: in the library he stays "pending" until a test passes). The writer got only `script-writer`, `hvac-scripts` and `roger-the-hvac-guy-persona`.
- **Writer:** a helper that could read only those three built skills and run their scanner, as a VA's claude.ai chat would.
- **Operator:** a helper playing the VA. Run 01: START, Roger the HVAC Guy, then "just write it" with only the title, then the brief without the rotation log, then everything. Run 02: START with the title on the same line, a vague channel name ("the hvac one"), then the brief and rotation log. The main session relayed each message word for word.
- **Judge:** a helper with the rubric, the scanner results, the brief, the price guide, the pack and the reference transcript.
