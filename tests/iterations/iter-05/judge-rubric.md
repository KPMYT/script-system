# TEST: judge rubric, electrical test run 01 (Frederick Barnes, iter-05)

The judge's rubric. The writer never sees this file or the reference transcript. Built 2026-10-27 from the plumbing run 03 judge report's categories (`tests/iterations/iter-04/test-run-03/judge-report.md`), adapted to the electrical pack.

## Inputs for the judge

- The output as delivered: `test-run-01/output.md` (the script alone: `test-run-01/script.txt`).
- The inputs: `brief-A12.txt` (title, brief; the rotation log was "none").
- The scanner run by the main session on the delivered script, and `tools/verify_output.py` on the output: `test-run-01/scanner-main-session.txt` and `test-run-01/verify-output.txt`. Treat their counts as facts.
- The reference video, same title topic: `refs/0h_r2bD5bMs-transcript.txt` (Everyday Home Repairs, "Plug Won't Stay In Outlet", 2.5M views, 11:13). It is also model E08 in the library (`electrical-scripts/references/models/E08-...md`), so the writer could legitimately study its beats, never its wording.
- The rules: `electrical-scripts/SKILL.md` (above all "The opening", "Emotion, all the way through", "The video types" / "The rung shape in fix videos", "The stakes", "Voice", "Written for the voice", "Proof", "Safety", "CTAs", "The ending", "Length", "Before handing over"), `personas/frederick-barnes.md`, and the core: `core/workflow.md` §4-5, `core/greenlight-audit.md`, `core/claims-policy.md`, `core/humanizer.md`.

## Score each, 1-10, for the script and for the reference video

| Category | What it asks |
|---|---|
| Opening (first 45 s) | The point in the first sentence (the problem now, the answer named by about 15 s); the fix-video order; one stake in proportion; at most one value promise (P11), never items in order; no greeting, intro, vague tease or recap; first check or step by about 45 s. |
| Keeping promises | Every forward line paid within about five minutes; the title's "real reason" actually delivered, early and clearly. |
| Clarity on one listen | Plain words, every term explained the first time, short sentences (the SENTENCES line: mean, share at 6 words or fewer, none over 35). |
| Number load | At most one figure in the opening, one or two per rung, never three in a sentence; every figure traced to the brief or the facts guide (row named). |
| Stakes (no money) | No prices or money words anywhere; the stake said once where it's real; fire as the stake, never the topic (fire words about two per 1,000 at most; death words at most twice and only where real). |
| Safety | Power off and prove it dead (tester checked on a live outlet, every wire, the tester re-checked) before any hands in the box; how power comes back and the test after; the stop signs (scorched wires, melted box, aluminum or old wiring) send it to a licensed electrician; no line that draws hands into a live box; nothing removed from the brief's safety. |
| Voice and persona | Frederick: calm, plain, warm, first person to one homeowner; "I" for verdicts; no job stories or claimed experience, no tests or measurements claimed, no name intro, the tenure at most once; no old tics. |
| Written for the voice | Units, sizes and codes in words; letters only where said as letters; no brackets or voice tags; "live" only before a noun. |
| CTA and ending | No mid-video CTA; the one-line subscribe ask alone inside ===START CTA(NO BOOK)=== / ===END CTA===, no safety-result promise; the comment ask after it ends the script, with a specific question and "I read every comment" / "every one". |
| Length and pacing | At least 12 minutes at 195 wpm (2,340 spoken words), 15-22 the aim, with nothing padded (no warning said twice, no restated point). |
| Originality vs the models | No lifted wording (copy guard), structure differs from E08 in at least three named ways, facts the reference video doesn't use. |
| Emotion | The pack's eleven emotion rules: the viewer in the scene, one spine feeling at nearly every rung, strong plain words, "but" turns, a question about every two rungs, "I" verdicts in most rungs and one insistence line, capability balancing fear, wins at the end of rungs, the title's feeling and key word ("real reason", "won't stay in") coming back, relief before the end. Count "you", "but", questions per 1,000 words. |
| Audit honesty | Does the evidence block match the script? Use `verify-output.txt`; quote any claim that's wrong. |

## The report

Save as `test-run-01/judge-report.md`, labelled TEST:
1. Verdict: is it up to the operator's bar ("make the viewer feel it", simpler and stronger), and would you upload it? One paragraph.
2. The score table (script vs reference).
3. Every failure with the quoted line, the rule it breaks (file and section) and the fix. Separate **library fixes** (a rule is missing, unclear or wrong) from **writer slips** (the rule was there and wasn't followed).
4. What the script does better than the reference, quoted.
5. The top five changes, ranked.
