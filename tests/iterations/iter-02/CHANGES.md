# iter-02: library fixes from the iter-01 judge, and the second run

Started 2026-10-19. Fixes the library problems in `../iter-01/judge/JUDGE-REPORT.md` (section 6, "LIBRARY problems"), then runs the plumbing-01 test again. Writer slips (W1-W10) need no library change; the second run shows whether they recur. `before/` holds a copy of every file this iteration modified, as it was at commit b2b1ec5.

## Library fixes

| Judge # | File | What changed | Why |
|---|---|---|---|
| 1 | `core/script-scanner.py` | Number check: (a) a hyphenated number word ("two-inch") no longer loops forever; (b) money ("$6.48", "15 bucks", "six bucks") must match money in the pack, so "$200 for a visit" can't borrow "200 gallons"; (c) small money amounts pass only exact or rounded to a whole dollar, so "$6.90" against "$6.48" is flagged; (d) the pack's GAPS section is never a source; (e) numbers in a rules file's PERSONA PROFILE block (the offer's facts) count as a source; (f) small numbers written as digits are checked (only number words of three or less are skipped). | The writer and the judge both had to hand-edit a copy to run the check, and the judge's probe got four invented numbers through. |
| 1 | `tests/run_checks.py` | Check 9c: no hang on hyphenated number words; money matches money; GAPS and invented prices flagged; offer facts accepted. Check 14 now ignores the template's parenthetical hints when matching field names. Suite: 23 checks. | Regression test for the hang and the looser matching. |
| 2 | `core/greenlight-audit.md`, `core/humanizer.md` | F8 rewritten: every research-pack safety point that belongs to a step is said at that step; a safety line is reworded, never cut, to fix an echo or scanner flag; listed in the evidence block. H18 says the same. | With no niche pack, F8 pointed at nothing, and a shut-off was deleted to clear an echo flag. |
| 3 | `core/greenlight-audit.md`, `core/variety-rotation.md`; fixture brief | E3: the brief names the reference video, its angle and its structure (never its transcript), or E3 reads "no reference given". Evidence block: `Not a clone (E3)` line. Rotation log gains `structure: [which]` (for E1 #6). The fixture brief now carries the reference video's title, angle and structure. | The writer couldn't run E3 or E1 #6 and guessed. Whether a competitor's title may be used word for word is an ideation question, now open for the operator. |
| 4 | `core/script-structures.md` | The brief's format wins over the title-shape table. New row and structure **3b, Diagnose and fix** (symptom hook covering every version the title promises, the sorting test as the first payoff, then each cause cheapest first: how to tell, why in a sentence, the fix as steps with safety at its step, how you know it worked; each diagnosis said once). "Why it happens": Layer 1 sits right after the hook only when it's a sentence or two that delivers part of the promise. | The fallback put background right after the hook (against retention section 3), had no rule for "why … and how to fix it", and caused the slow start and the triple diagnosis. |
| 5 | `core/greenlight-audit.md`, `core/voice-anchoring.md` | New D1b: the persona's "How they talk" lines are audited, and the profile wins over the samples on the persona (sentence length, register). Evidence block: `persona line`. | The persona's "short sentences" were never checked (18.2 words per sentence against the source's 11.0). |
| 6 | `core/research-and-sourcing.md`, `core/workflow.md`; fixture research pack | Default pack: STEPS must be complete for every fix the title promises (shut-off, remove, install, test), or it's a blocking gap; safety points tied to their steps. Workflow: a step the pack doesn't list means NOT READY, and samples, excerpts and reference scripts never supply facts, numbers or steps. The fixture pack was updated by the research subagent to match. | "Replace the fill valve" was a one-line step, and the writer borrowed flapper steps from a voice sample. |
| 7 | `core/greenlight-audit.md`, `core/workflow.md` | Evidence block gains `Hook` (A2, or "not run"), `Safety`, `Not a clone (E3)` and `Custom element (E4)` lines; Originality now lists each signal with its evidence. The `voice-samples` input asks for at least one sample starting at the video's opening. | A2, E3, E4 and safety were silently skipped; originality #2 was claimed with no evidence. |
| 8 | `core/variety-rotation.md` | The opening move is the move of the first sentence; the thumbnail scene can sit inside any move; "problem at its worst" and "universal situation" told apart. | The writer logged the second sentence's move. |
| 9 | `core/workflow.md` | The TEST line goes first on every test output, even a one-line reply. | Ambiguous. |
| 10 | `core/workflow.md` | A rotation log of fewer than five lines is accepted as stated. | The gate can't check the channel's script count. |
| 11 | `core/research-and-sourcing.md` | The pack's suggested honest wording follows D4 (time and cost round up). | The pack had rounded time down. |
| 12 | `core/cta-and-endings.md`, `core/persona-profile-template.md`; fixture persona | The end CTA carries the offer and at most the persona's one ask; the persona sets what's asked for, never its words. | "One ask per moment" and CTA rotation collided with a fixed end-ask line. |
| 13 | `core/workflow.md` | Tag density: about one per 80-120 words across the script, never more than two in any 80 words. | Ambiguous scope. |
| 14 | `core/research-and-sourcing.md` | Prices are spoken undated; the pack carries the checked date; a niche pack may add "prices subject to change". | Unclear whether spoken prices need a date. |
| 15 | `core/humanizer.md` | H18's third mention is fix-on-sight. | H18 had no tier. |
| 16 | `core/persona-profile-template.md`; fixture persona | The added-value promise names what the viewer gets, never an outcome. The fixture's "so you buy the right part the first time" became a plain description. | Read like a result guarantee. |
| 17 | `core/research-and-sourcing.md` | Attribute once per source per section; steps need no attribution. | 24 source mentions in 77 sentences read like a citation list. |

## Test runs after the fixes

- `python3 tests/run_checks.py`: 23/23 passed.

## The second run (plumbing-01, bulk mode)

One operator message with START TEST, the channel and all five inputs (`run/operator-turn-1.md`); a fresh writer chat (`run/writer-turn-1.md`, scratch in `writer-work/`); a fresh judge (`judge/JUDGE-REPORT.md`).

**Gate:** correct. No questions, straight to the full output, TEST line first; a two-line rotation log accepted; A2 reported "not run" (no sample starts at 0:00).

**Format:** passes. VO copy identical to the script with tags stripped; 18 tags, one per 108 words, never more than two in any 80.

**Scanner:** no hang (0.1 s); fix-on-sight 0; copied 0 against the source and the samples; every number in the pack.

**Judge's verdict: FIX-THEN-PASS, no Hold, and safe to upload unread** (nothing false, unsafe or off-policy). Fixed since iter-01: no misattribution; every step from the pack, none from the samples; all seven safety points at their steps; both kinds of running in the hook; both part swaps taught in full (the source points to other videos); first action at about 1:00 (was 2:25); no triple diagnosis; opening move logged correctly; 25+ numbers all traced, none rounded the flattering way.

**Still wrong:**
1. Persona voice: 17.2 words per sentence (source 11.0); D1b let the writer quote one short line as proof.
2. Branch order: the fill-valve replacement ($14.98) comes before the flapper's two free checks, against the brief's "free adjustments first, parts last"; the flapper (the most common cause) starts at about 7:34.
3. Length: 1,941 words, about 12:56 at 150 wpm (source 969; iter-01 1,402). Honest by the progression test (80-120 words to trim); the extra is the two full repair procedures (681 words) that iter-02 now requires.
4. Evidence overclaims: originality 7/7 should be 5/7; the E3 contrast isn't real; "Rules (F): clean" is false.
5. Low: some parts unexplained (refill tube, lock ring, shank washer, piston valve); the float-ball valve left without a fix; "502" will be misread; the shut-off goes by six names.

**Library fixes the judge ranks next (for iter-03):**
1. High: the number check still passes "$200 for a visit" (a quoted comment in the pack), "20 years" (matched to "20 minutes") and "9,000 gallons". Match numbers with their units, exclude quoted comments as a source, extend check 9c.
2. High: D1b can't fail. Scanner reports sentence-length figures; personas get a numeric target; the evidence line reports the numbers.
3. Medium: structure 3b has no branch-order rule after the sorting test (order by how common the cause is, or every free check before any part when the brief says "parts last").
4. Medium (made worse by iter-02): the 3b hook prescribes the reference video's own opening; keep the coverage requirement, rotate the move.
5. Medium-low (made worse by iter-02): "reword safety lines" plus the echo flag pushes writers into renaming things (H-rules ban that); exempt repeated safety instructions from the echo count instead.
6. Medium-low: research verification (pack step 1 contradicts F3's water-on check; the NYC figures don't reconcile; variants like the float-ball valve need steps or a scope line).
7. Low: the voice-samples fixture still has no opening sample, so A2 has never run; the evidence block should record what each audit round fixed and quote the brief's reference fields; define E4 for scripts; attribution density has no check; "up to half an hour" turns a floor into a ceiling; pronunciation of part numbers.

**Operator decision raised by this run:** how deep "how to fix it" goes. Teaching both part swaps in full roughly doubles the source's length (about 13 minutes against 6). See `SESSION-HANDOVER.md`, open questions.

## Test runs

- `python3 tests/run_checks.py`: 23/23 passed (before and after the run).
