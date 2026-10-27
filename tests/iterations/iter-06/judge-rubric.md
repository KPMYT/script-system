# TEST: judge rubric, HVAC test runs (Roger the HVAC Guy, iter-06)

The judge's rubric. The writer never sees this file or the reference transcripts. Built 2026-10-27 from the electrical rubric (`iter-05/judge-rubric.md` on the electrical branch) and the plumbing run 03 judge report's categories (`iter-04/test-run-03/judge-report.md`), adapted to the HVAC pack.

## Inputs for the judge

- The output as delivered: `test-run-NN/output.md` (the script alone: `test-run-NN/script.txt`) and the chat (`test-run-NN/chat.md`).
- The inputs: `brief-NN.txt` (title and brief; the rotation log was "none"). Ignore its REFERENCE line: the writer never saw it.
- The scanner, run by the main session on the delivered script with every copy-guard file: `test-run-NN/scanner-main-session.txt`. Treat its counts as facts.
- The reference video for the title: run 01 `refs/qbWN3OViWxQ-transcript.txt` (Ray Dutton's Garage, "5 AC Mistakes HVAC Companies Hope You Keep Making", 1.1M views; a faceless AI-voiced channel, the title's source, never a model); run 02 `refs/3Jonl_TLkpE-transcript.txt` (Word of Advice TV, "Furnace Not Working - The Most Common Fix", 140x its channel's normal; also model R28, so the writer could study its beats, never its wording).
- The rules: `hvac-scripts/SKILL.md` (above all the overrides table, "The opening", "Emotion", "The video types" and the item shape, "CTAs", "The ending", "Length", "Voice", "Proof", "Money framing", "Safety", the banned list), `hvac-scripts/references/price-guide.md`, `personas/roger-the-hvac-guy.md`, and the core: `core/workflow.md` §4-5, `core/greenlight-audit.md`, `core/claims-policy.md`, `core/humanizer.md`.

## Score each, 1-10, for the script and for the reference video

| Category | What it asks |
|---|---|
| Opening (first 45 s) | The point in the first sentence; the breakdown moment or the quote if used, in one or two sentences; the villain (price, upsell, silence; never the honest tech or a motive); a count line or escalation line, never what each item holds; no greeting, name intro or vague tease; first real tip by about 30 s in a list. |
| Keeping promises | Every forward line paid within about five minutes; the title's promise delivered (#4: eleven mistakes the trade profits from; #14: the $12 part, the $300, and cleaning it yourself). |
| Clarity on one listen | Plain words, every trade term explained the first time, short sentences. |
| Number load | At most one figure in the opening, at most one price per item, figures on no more than about half the items, never three in a sentence (outside the side-by-side device); every price traced to the brief or the price guide (row named), said as a rounded range; nothing from the guide's "don't quote" lines. |
| Money framing | The comparison within two minutes; one money device used well (the clock, the quote against the part, side by side, payback); the title's money figure paid at its item with what was avoided. |
| Safety | Every hands-on step: power off and proved off, gas valve off where the burner is touched, let it cool; no refrigerant work, no bypassing a safety switch, capacitor charge where the outdoor unit is opened; a named call-a-tech trigger, never "if it's outside your comfort zone"; a gas leak or a CO alarm, if mentioned, gets every step from price guide §9; nothing removed from the brief's safety. |
| Voice and persona | Roger: blunt, plain, unhurried, first person to one homeowner; 45 years at most once and only where it does a job; no job stories, tests or demonstrations claimed; the personal detail (the filter on the first of the month) at most once; never the plumbing channel or a book; none of Ray Dutton's catchphrases. |
| Written for the voice | Units, ratings, refrigerants and ranges as they're said; letters only where said as letters (HVAC, AC, MERV and the like are fine); no brackets or voice tags in the script. |
| CTA and ending | No mid-video CTA; the one-line subscribe ask at the end, naming Roger the HVAC Guy, worded fresh; then the comment ask last: a question about the viewer's own house or numbers, plus "I read every one". |
| Length and pacing | At least 12 minutes at about 150 words a minute (about 1,800 spoken words), nothing padded; items about 150-250 words. |
| Originality vs the models | No lifted wording (copy guard); structure differs from any model it names in at least three named ways; facts the reference video doesn't use. |
| Emotion | The pack's emotion rules: the viewer in the scene, the title's feeling coming back in new words, the HVAC feelings (the clock, the dial that won't reach, comfort, the machine's sounds), "but" turns, a question about every two items, the villain returning in new words, the honest out ("a tech you trust"), relief before the end. Count "you", "but" and questions per 1,000 words. |
| Audit honesty | Does the evidence block match the script? Quote any claim that's wrong. |

## The report

Save as `test-run-NN/judge-report.md`, labelled TEST:
1. Verdict: is it up to the operator's bar ("make the viewer feel it", simpler and stronger), and would you upload it? One paragraph.
2. The score table (script vs reference).
3. Every failure with the quoted line, the rule it breaks (file and section) and the fix. Separate **library fixes** (a rule is missing, unclear or wrong) from **writer slips** (the rule was there and wasn't followed).
4. What the script does better than the reference, quoted.
5. The top five changes, ranked.
