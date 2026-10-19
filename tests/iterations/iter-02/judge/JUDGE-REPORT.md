# iter-02 judge report: plumbing-01, bulk mode (TEST Plumbing, no niche pack)

TEST run. Judge: an independent re-audit of the writer's single reply against `core/` (the rubric), the TEST persona, the pasted inputs, the scanner and the judge-only source script. I fixed nothing.

"L28" means line 28 of `run/writer-turn-1.md`.

**Verdict in one line:** a clear step up from iter-01. Every iter-01 writer slip that involved facts, safety or sample content is gone. Every number traces to the pack, every safety point sits at its step, and no claim is pinned on the wrong company. The script is safe to upload. But `VERDICT: PASS` still isn't fully earned: on a strict run I find a **FIX-THEN-PASS** and no Hold. Four things open it:
- The persona's "short sentences" are still missed (17.2 words per sentence, against 18.2 in iter-01). The new D1b check let the writer quote one short line and call it met.
- The flapper branch comes after a 2.5-minute fill-valve replacement. Fluidmaster calls the flapper the most common cause, and the brief says "free adjustments first, parts last", yet the flapper's free checks start at about 9:18.
- Originality and E3 are overclaimed.
- There are a handful of low items.

The script grew to 1,941 words (about 12:56). That's honest by the progression test, but it comes from two iter-02 library changes that have no ordering or compression rule to go with them.

## Evidence files (all in this folder)

| File | What it is |
|---|---|
| `script-from-writer-turn-1.md` | The script part of writer turn 1 (L1-L136: the TEST line through the closing line). It's identical to `writer-work/script-body.txt` apart from the two header lines. |
| `scan-full.txt` | Scanner run: `--rules` persona, `--pack` research pack, `--refs` source script and voice samples, under `timeout 30`. **Exit 0 in 0.1 s. The hyphen hang did not recur** (the script contains "two-inch", "three-inch", "Ten-Minute", "one-page", "24-page", "4-second"). |
| `numcheck-probe-rerun.txt` | iter-01's six-line probe of invented numbers, re-run on the fixed scanner (see D4). |
| `script-body.txt`, `vo-copy-from-writer-turn-1.md`, `vo-stripped.txt` | Used for the mechanical VO check. |
| `script-spoken.txt` | The script without marker lines, used for word counts and n-grams. |
| `mechanical-checks.txt` | Output of the tag-density, sentence-length, n-gram and word-count scripts. |

Scanner result: fix-on-sight 0, shape-test flags 0, "Most..." 0, reframes 0, filler 0, echo 1 (`number x4: "10"`), numbers not in pack 0, copied 0 against both the source and the samples. I agree that the "10" echo is a false positive: 10 to 15 seconds (L46), under 10 minutes (L54), 10 to 15 minutes (L89) and after 10 minutes (L95) are four different facts. `tests/run_checks.py`: 23/23.

---

## 1. Gate behavior (bulk mode)

| Check | Expected | Writer | Result |
|---|---|---|---|
| Questions | None; straight to the full output (workflow 2, "Bulk mode") | None. L1 `TEST: DO NOT UPLOAD.`, L2 `SCRIPT TYPE: Talking Head`, then the script | **PASS** |
| Channel | Named in the message ("channel is TEST Plumbing") | Accepted | PASS |
| research-pack | Verified on date; title matches; live facts fresh (no niche pack, so re-checked for this script); no blocking gap | "Verified on: 2026-10-19" (today), title word for word, P1-P3 dated 2026-10-19, all seven GAPS "Not blocking". The pasted pack is byte-identical to `tests/fixtures/inputs/test-plumbing-research-pack.md`. | PASS |
| rotation-log | Up to five lines; fewer accepted as stated (iter-02 fix 10) | Two lines accepted, no question asked (`writer-work/plan.md`: "rotation log 2 lines") | PASS |
| voice-samples | 2-3 excerpts from different videos, about 60-90 s each, with sources; if none starts at 0:00, accept and report A2 "not run" | Three channels, 0:21-1:35 (74 s), 1:10-2:35 (85 s), 3:08-4:33 (85 s). Accepted; A2 reported "not run". | PASS |
| TEST line first | Every test output (fix 9) | L1 | PASS |

The gate is correct. One note. Fix 7 changed the `voice-samples` input to ask for at least one sample that starts at the video's opening. But the gate accepts samples without one, and the fixture samples weren't updated, so in this test A2 still can't run. Fix 7 had no effect on A2 (see library fix 7).

---

## 2. Format and skeleton (workflow.md sections 4-6)

| Item | Result | Evidence |
|---|---|---|
| Skeleton order | PASS | The TEST line, SCRIPT TYPE, the script, VERDICT, FORMAT CHECK, ROTATION LOG ENTRY, AUDIT EVIDENCE (all 11 template lines, in order) and VO COPY. Nothing comes after the VO copy. |
| Clean prose | PASS | No headings, brackets, stage directions, links, emoji, colons or ellipses in L4-L136. |
| One sentence per line | PASS | 113 sentences, each on its own line. |
| Marker lines | PASS | L37 and L129 read `===START CTA(TEST: The 10-Minute Toilet Fix Guide)===`, character for character the persona's printed title. `===END CTA===` sits directly under the last sentence (L42, L134). Each marker is alone on its line, with a blank line before and after each block. |
| Mid-CTA includes the return line | PASS | L41, "So, the level's set, and water's still getting into that tube.", is inside the markers. |
| End CTA through its ask, then one closing line | PASS | L133, "And hit subscribe, so the next plumbing fix turns up in your feed.", then L136, "Tonight, lift that tank lid and check the water against the overflow tube.": 13 words, the last line, a practical next action. |
| Stats as digits | PASS (iter-01's W6 fixed) | L20 "3 to 5 gallons a minute", L53 "5 to 7 years", L84 "every 5 years", L85 "a 4-second burst of water every 5 minutes". |
| Measurements spelled out | PASS | "about half an inch" (L28, L76), "an eighth of a turn" (L45), "about three inches" (L66). |
| Things a voice might misread | **Low** | L107 "Fluidmaster's two-inch 502 flapper": TTS will say "five hundred two", but the part is said "five-oh-two" (workflow 4, "Spell out anything a voice might misread, the way it's said"). "400H" (L26, L54) is probably fine. |
| Named person introduced by full name once | PASS | L109 "Bob Vila's guide". |
| FORMAT CHECK line | PASS | Matches the template field for field, and it's true. |
| ROTATION LOG ENTRY fields | PASS on fields, one accuracy note | All 14 fields are present, including the new `structure: diagnose and fix (core fallback)`. `opening:` is now the first sentence's move (fix 8 worked). The note is the doubter label, under F9. |
| **VO COPY: identical words** | **PASS, verified mechanically** | Stripping `^\[[a-z -]+\] ` from the VO copy and running `diff` against L4-L136 shows no differences, marker lines included (`vo-stripped.txt`). |
| Tag density, script-wide | PASS | 18 tags over 1,941 spoken words: 1 per 108 words (rule: about 1 per 80-120). |
| **"No more than two in any 80 words"** (new) | **PASS** | Sliding 80-word window: the maximum is 2. The six windows with two are L179+L183 (49 words apart), L183+L188 (49), L205+L210 (74), L236+L240 (46), L274+L280 (60) and L280+L286 (59). None has three. |
| No adjacent tags; max one per sentence | PASS | No two consecutive lines are tagged. |
| Allowed tags only | PASS | [matter-of-fact] x4, [thoughtful] x3, [warm] x3, [short pause] x3, [emphatic] x2, [slower] x2, [slightly amused] x1. |
| [slightly amused] only on honest candor | PASS, with a note | L205, "[slightly amused] That's the maker's number, and I'd give myself longer.": a true limit on a manufacturer's claim. As in iter-01, the amused tone sits on a line about a named company. It's not a fail, but a voice actor could make it sound like a dig. |
| CTA sections: one [warm] at the start, nothing else | PASS | L188 and L280. |
| Pauses only at a natural beat | **Borderline** | L231 (section turn) and L286 (before the closing line) are fine. L183 "[short pause] Let the tank fill." sits four lines before the mid-CTA lead-in, not right before it, and after no reveal. It's defensible as a literal wait, but it isn't one of the three beats workflow 6 lists. |
| Markers untagged and reproduced | PASS | Yes. |

---

## 3. Independent audit (greenlight-audit.md)

### Group A: the hook

- **A1 PASS.** L4, "Why won't your toilet stop running, with water spilling down that open pipe in the middle of the tank?", names the subject and the thumbnail scene in the first sentence. The first sentence is a question, not a greeting.
- **A2 NOT RUN, correctly reported.** None of the samples starts at 0:00 (L143).
- **A3 PASS.** Both kinds of running: L4 and L5 ("Or maybe yours does stop, and then every few minutes it fills itself back up with nobody near it."), fixing iter-01's W10. "One of three things": the level at L23-L35, the fill valve at L44-L79, the flapper at L81-L127. "Before you buy a single part": the sort at L16-L21, the pencil and dye tests at L88-L96, and the free fixes before each part. "The first check takes seconds": L16-L21. "Up to half an hour": L88-L90.
- **A4 PASS.**
  - L7 "listed at $14.98 against $6.48 for a flapper" names both parts, fixing iter-01's W9.
  - L6 "In most cases" is the pack's GAPS wording.
  - L9 "The flapper test takes up to half an hour" is the pack's prescribed wording. The pack's own source, Korky, says "at least 25 minutes", which is a floor. "Up to" turns that floor into a ceiling. The rounding direction is right, but the phrasing isn't. LIBRARY (low), since the wording came from the pack.

### Group B: retention

- **B1 PASS.** L4's question is answered throughout. L18's "Is the water in the tank rising so high that it's spilling over the top of it?" is answered at L19-L21.
- **B2 BORDERLINE PASS.** The hook (L4-L9) itself delivers part of the promise (the cost turn, the timing). The line after it, L11 "Find the shut-off valve behind the toilet before you start.", is safety prep rather than a payoff. It's mandated by S1, S2 and S5 at step 1, so it isn't background. The lid comes off at about 1:00 and the sort test lands at about 1:30-2:05, against iter-01's 2:25 to the first action. The source has the tank open at 0:25.
- **B3 PASS, with trim noted** (section 4). Every paragraph adds information or moves toward the goal.
- **B4 PASS with a structural reservation.** There's no slow start and no context dump. But for the viewer whose toilet refills every few minutes (half the hook's audience, and the cause Fluidmaster calls "the most common problem", F6), nothing after the sort test applies until L81, at about 7:34. In between sit the level fix, the debris flush and a 386-word (about 2:34) fill-valve replacement. That's a broken-promise risk for that viewer, though not a broken promise.
- **B5 PASS on bridges, FAIL (medium) on pacing for one branch.** The bridges are honest and short-range: L23 cost or effort, L35 "the next step tells you which" (delivered at L44-L52), L81-L82 progress and self-recognition, L98 cost. "No flat stretch longer than about 90 seconds without a payoff" holds for a fill-valve viewer, but not for a flapper viewer (about 5.5 minutes, L23-L79, with nothing that applies to them). The library has no rule for branch order after a sort test. LIBRARY (fix 3).
- **B6 PASS.** L83's reasoning chains with "so" and "when".
- **B7 FAIL (low-medium).** There are runs of four to six long sentences outside steps and lists. The hook runs 19, 19, 27 and 32 words (L4-L7). Another run is L82-L88 (25, 29, 24, 19, 20, 19), for example L83 "Once a flapper wears, water slips past it into the bowl, so the tank level drops, and when the float drops with it, it turns the water back on." Only 12 of 113 sentences are 8 words or fewer, and 25 are 23 or more.
- **B8 n/a.** Not a list. The order is a branch order (see B4/B5 and F1).
- **B9 PASS.** No repeated emphasis, piled qualifiers or throat-clearing. iter-01's "explains it like this" is gone.

### Group C: clarity

- **C1 PASS.**
- **C2 FAIL (low): parts used without being explained.** The persona says "calls the parts by their real names and explains each one once", so this also counts against D1b.
  - L63 "with its refill tube, refill clip and shank washer". The refill tube is then used in L67 ("with the refill tube facing the flush valve") and L73 ("Clip the refill tube onto the overflow tube"), and never explained.
  - L66 "leave the lock ring where it is": the lock ring isn't explained.
  - L31 "get a piston-valve type": not explained.
  - iter-01's "ears" is now explained: L113, "There's an ear on each side of the flapper, hooked over a peg on the flush valve".
  - L111 "turning the valve clockwise" says "the valve" in a section that also names the fill valve and the flush valve. It's clear from "Shut the water off", but loose.
- **C3 PASS.**
- **C4 n/a.**
- **C5 PASS, with one gap (low-medium).** Every cause now gets a fix the viewer can do: the level (L26-L28), the debris flush (L44-L50), the fill-valve replacement in full (L57-L78) and the flapper replacement in full (L111-L126). That fixes iter-01's main C5 failure. The gap is L30, "If your fill valve has a float ball instead, it's an older kind that adjusts differently.", which leaves a float-ball owner whose level is too high with no fix. L31 only applies to replacement, and the script never tells them the replacement steps ahead will swap it for a piston type, though the pack supports that (F13 plus 5a-5k). The pack itself lists float balls only as an "Option" with no steps. Mostly LIBRARY (fix 6), partly writer. No recap at the end: PASS.

### Group D: voice

- **D1 PASS on shape against the samples.** The matched line, L113 against Sample 2's "On each side of the flapper you'll see that there's a little wing", is fair. The step hand-offs ("Turn the water off again and flush, then…", "Then twist…") follow the samples' "Once that's disconnected… then we're going to…" shapes.
- **D1b FAIL (medium): the persona's "short sentences" are not met, and the evidence line is a cherry-pick.**
  - The persona says "plain and unhurried, short sentences, 'you' for every step and 'I' for his opinions".
  - The script averages **17.2 words per sentence** (median 17). 12 of 113 sentences are 8 words or fewer, and 25 are 23 or more. iter-01 was 18.2, the source 11.0. A drop of one word is no real change.
  - The writer's "persona line" is "Korky says at least 25, so I'd give it the full half hour.": one of the 12 short sentences, chosen to show the rule rather than to test it.
  - The longest sentences: L20 (38 words), L21 (35), L7 (32, in the hook), L14 (29) and L83 (29).
  - The "you" and "I" usage and the register (dry, candid, never jokey) are met.
  - The new D1b check exists but has no measure, so a single quoted line satisfies it. LIBRARY (fix 2), and WRITER for claiming it.
- **D2 humanizer sweep.**
  - H1-H5, H7-H17, H19 (invented numbers), H22: no hits. Triads are concrete (L63 "refill tube, refill clip and shank washer").
  - **H18 (echo): PASS, with notes.** These are each said twice, the second adding something:
    - the sort diagnosis, at L21 and L82 (L82 is the re-entry bridge)
    - "a new fill valve won't fix it", at L7 and L86 (the second adds the comment)
    - $14.98 (L7, L54) and $6.48 (L7, L107)
    - "half an inch below the top", at L28 and L76
    - chain slack, at L100-L101 and L118-L119 (the second adds "slow, weak flush")

    The pencil test comes back four times (L88, L91, L105, L123), but those are procedural re-tests, not restatements. S4 and S5 repeat by design (F8) and are reworded each time.
  - **H6 (rotating synonyms, fix-on-sight): borderline, caused by a rule.** The water shut-off goes by six labels:
    - L11 "shut-off valve behind the toilet"
    - L44 "the shut-off"
    - L57 "Turn the water off"
    - L75 "the valve behind the toilet"
    - L88 "close the shut-off"
    - L111 "turning the valve"

    `writer-work` shows why. Draft 1's scan flagged "valve behind the toilet" x3 and "shut the water off" x3. Draft 2 renamed them ("Turn the shut-off clockwise till it stops", "close the shut-off"), and draft 3 changed "turn the water on" to "open the shut-off again". H18 now says safety lines are "reworded" rather than repeated, and the scanner still counts them as echoes, so the rule pushes writers toward H6. LIBRARY (fix 5).
  - **Counts:** H20 0 ("In most cases", L6, isn't a "Most people" opener), H21 0, H23 0. These agree with the scanner.
  - **H19 vague:** L107 "a lot of people pay for a visit": the pack's own suggested tone line, with no number depending on it. OK.
- **D3 PASS.** Fix-on-sight 0, copied 0 against the source and the samples. My 6-gram check finds only "an inch below the top of" and "put the cap back on and" shared with the source (a measurement phrase, plus pack step 4's own wording), and "on each side of the flapper" with Sample 2 (the matched shape).
- **D4 PASS on tracing. Every number:**

  | Script number | Line | Pack | Rounding |
  |---|---|---|---|
  | $14.98 | L7, L54 | P2 "listed at $14.98" (Home Depot, 400H-002-P10) | exact |
  | $6.48 | L7, L107 | P1 "listed at $6.48" (2 in. 502P21) | exact |
  | one of three / "in most cases" | L6 | Promise; GAPS ("most of the time" / "in most cases") | as prescribed |
  | "takes seconds" | L8 | step 2 "this check takes seconds" | — |
  | up to half an hour | L9 | GAPS honest wording (F7 "at least 25 minutes", rounded up) | up, correct direction; "up to" misstates a floor (A4) |
  | 3 to 5 gallons a minute; 3,600 gallons a day | L20 | W3 (NYC DEP), attributed | exact. The source's own math is inconsistent (3-5 gal/min is 4,320-7,200 a day). "which they put at" keeps it attributed, but the pack's verification pass should have flagged it (fix 6). |
  | 400H | L26, L54 | F4, P2 | — |
  | half an inch | L28, L76 | F4, F5 | exact ("roughly") |
  | an eighth of a turn | L45 | step 4 "1/8 turn" | exact |
  | 10 to 15 seconds | L46 | step 4 | exact |
  | 5 to 7 years | L53 | F12 (Korky) | exact |
  | under 10 minutes | L54 | F14, said as Fluidmaster's claim, with "I'd give myself longer" (L55) | time rounded up by opinion: good |
  | about three inches | L66 | step 5f "roughly 3"" | exact |
  | thousands of gallons a year | L84 | W1 (EPA WaterSense) | exact |
  | every 5 years | L84 | F12 (EPA) | exact |
  | 4-second burst, every 5 minutes | L85 | DOUBTER (@BasedBullShark), said as a comment | exact |
  | 10 to 15 minutes | L89 | F6 (Fluidmaster) | exact |
  | at least 25 | L90 | F7 (Korky) | exact |
  | the full half hour | L90 | 25 rounded up, as an opinion | up: good |
  | 10 minutes (dye) | L95 | F8 (EPA) | exact |
  | two checks | L98 | count (chain, seat: F9, F10) | — |
  | one to two / one or two links | L100, L118 | F9 (Korky), 9g | exact |
  | two-inch 502 | L107 | P1, F11 | — |
  | two-inch and three-inch | L108 | F11 | — |
  | about 20 minutes, beginner | L109 | F14 (Bob Vila "Total Time: 20 minutes, Skill Level: Beginner") | exact ("about" is neutral) |
  | a fourth cause / the other three | L125 | GAPS "a cracked flush valve is a rarer fourth cause" | — |
  | Ten-Minute, one-page, 24-page, five parts, first link | CTAs | Persona profile offer facts | exact |

  No number is rounded in the flattering direction. Nothing traces to the GAPS section alone (the service-call cost is correctly absent), and nothing comes from the voice samples.

  **The fixed number check is better, but still not trustworthy** (`numcheck-probe-rerun.txt`). Of iter-01's six invented lines, three are now flagged: "$6.90", "45 minutes" and "17 dollars". Three still pass:
  - "A plumber charges $200 for a visit". The money now matches money, as fix 1(b) intended, but it matches the "$200" inside the pack's ADVERSARY comment ("You saved me $200"), a figure the pack says *not* to state as a cost.
  - "The fill valve lasts 20 years" borrows "Total Time: 20 minutes" (no unit matching).
  - "It wastes 9,000 gallons a year" (within 5% of 9,300; arguably cautious).

  CHANGES.md's claim that "$200 for a visit" can't borrow is true only for "200 gallons". LIBRARY (high, fix 1).
- **D5 PASS.** Reframes 0. No poster-quote lines.

### Group E: authenticity

- **E1 PASS at 5/7 with evidence. The writer claimed 7/7.**
  - #1 PASS: the 400H installation PDF, the NYC DEP brochure and the EPA family fact sheet are in the pack. The fact sheet (W2) isn't used in the script, but #1 is about the pack.
  - #3 PASS: L55, L90, L91.
  - #4 PASS: Fluidmaster, Korky, EPA WaterSense, New York City's water department, Bob Vila, Home Depot.
  - #5 PASS: L85-L86 (burst refills mean a fill valve won't fix it); L91-L93 (where the pencil line stops tells flapper from flush valve).
  - **#2 NOT EVIDENCED.** The writer contrasts "free checks first and parts last with listed prices, against the reference's inspector sorting by symptom". But the script also sorts by symptom (L4-L5, L18-L21, L82), and the reference also does free checks before parts (chain, seat, dial, debris flush, then "you might need to replace a part"). The real differences are prices, sources and complete repairs. Those are sourcing and depth, not angle.
  - **#6 PARTIAL, counted.** The order differs: sort test, then fill-valve side, then flapper, against the reference's flapper first. There's no recap. But the opening move is the reference's: a question covering both symptoms, then "one of three". Compare the brief's reference structure ("symptom question and 'one of three problems' promise") with L4-L6. The same three causes with the same sub-steps (level, then debris flush, then replace) appear in both. The rotation log can't help: neither earlier entry has a `structure` field.
  - **#7 thin.** "easy does it" (L71) once, and two or three "I" opinions. I count it, generously.
- **E2 PASS.** Copied 0.
- **E3 PASS with reservations; the writer's evidence is partly overstated.**
  - Title: verbatim the reference's title.
  - Hook move: the same.
  - Cause set: the same, reordered.
  - Voice: clearly differs. No wind-up, no anecdote, a retired-plumber persona with opinions, no like-and-subscribe close.
  - Sourcing: clearly differs. Manufacturer sheets, EPA, NYC DEP and real comments, against one inspector's practice.
  - Angle: differs only in degree (priced, sourced, complete repairs). The writer's "against an inspector sorting by symptom" isn't a real contrast, as under #2.

  Not a clone Hold, since voice and sourcing differ clearly and the angle arguably does. But note that the new 3b hook ("the symptom… covering every version the title promises… plus the promise: which cause it is") is the reference video's own hook, so the library now steers toward it (fix 4).
- **E4 PASS on paper.** The real Home Depot listing screenshots for $6.48 and $14.98 are named in the narration (L54, L107). The writer also lists "the pencil-line and food-coloring shots" and "Talking Head CTA segments", which are generated footage or the channel's standard format, not custom elements. At script stage E4 can only name candidates (fix 9).

### Group F: rules compliance

- **F1 PASS on parts, FAIL (medium) on branch order against the brief.**
  - 3b's fixed parts are all there:
    - a hook covering both versions plus the promise (L4-L9)
    - the sorting test first (L16-L21)
    - each cause with how to tell, why in a sentence, the fix as steps with safety at each step, and how you know it worked (L34, L50, L78, L105, L126)
    - beyond DIY (L125)
    - the ending
  - The structure is recorded in the log.
  - But the brief's Angle is "the cheap order of checks, free adjustments first, parts last", and the script puts a $14.98 part replacement (L57-L79, at about 5:00-7:34) before two free checks (chain and seat, L98-L105, at about 9:18).
  - 3b's "each cause, cheapest and quickest check first" supports the writer's reading (the overflow look takes seconds; the pencil test takes 30 minutes). It doesn't address branches, or likelihood (F6: the flapper is "the most common problem"). LIBRARY (fix 3), and the writer chose the reading that serves fewer viewers.
- **F2 PASS, with a note.** Length came from the content: 1,941 words, and every paragraph passes the progression test. About 80-120 words are trimmable (section 4). The length is driven by two full replacement procedures (681 words, about 4:30) that the library now requires.
- **F3 PASS.**
  - The mid-CTA (L37-L42) comes after the first payoff: the level fix, with "that screw was the whole fix" (L34).
  - It plays against an open question: L35, "clogged with debris or worn out, and the next step tells you which".
  - It has what the offer is (an "e-book download… the Ten-Minute Toilet Fix Guide"), added value (the one-page chart) and where to get it (the first link).
  - It returns with "where things stand" (L41), and has no subscribe ask.
  - The end CTA starts directly after the last content line (L127). It carries the offer facts (24 pages, five parts, the printable checklist), where to get it, and one ask (subscribe, worded fresh). Then one closing line. No recap, no thanks, no named future video.
  - Notes (low):
    - L39 "so you can keep it next to the toilet while you sort this out" implies a printed chart. The profile calls only the parts checklist printable (offer-rules 1, "never… embellish").
    - The chart "matches each symptom to its likely part", which is what this video itself just did. The printable checklist is the real extra, and it isn't said until the end CTA (same as iter-01).
- **F4 PASS.** Price-silent and named as an e-book download, with no backstory or urgency. Money talk is away from both CTAs: draft 4 changed L34 from "and it cost you nothing" to "that screw was the whole fix", and the nearest price after the mid-CTA is L54.
- **F5 PASS.**
  - Every claim about a named company is in the pack:
    - Fluidmaster: L29 F4, L54 F14, L61 S6, L71 S3, L79 S4, L89 F6
    - Korky: L53 F12, L90 F7, L100 F9
    - EPA: L84 W1 and F12, L94 F8
    - NYC DEP: L20 W3, L31 F13
    - Home Depot: P1, P2
    - Bob Vila: F14
  - L29, "Fluidmaster's instructions say it doesn't need to be exact.", is now correctly Fluidmaster's alone (iter-01's W1 fixed).
  - No life facts: "retired plumber" is never said.
  - The catchphrase is used once (L71).
  - Opinions are opinions: L55, L90, L91.
  - No company is cast as a villain. The adversary is the category: "a lot of people pay for a visit" (L107).
- **F6 PASS.**
  - **No content from the voice samples** (iter-01's W2 fixed). Every step in L44-L50, L57-L78 and L111-L126 maps to pack steps 4, 5a-5k and 9a-9j.
  - Sample 3's "bucket underneath… rags, towels" matches pack 5c ("use a bucket or towel"). L59 uses the pack's wording.
  - Sample 2's chain-from-handle step is now pack 9d.
  - One deviation from the pack, which the writer disclosed: L16 "Leave the water on for this first look" overrides pack step 1 ("Shut off the supply valve… then lift off the lid"), because F3 checks the level "with the water on". The writer was right. The pack's step 1 contradicts its own F3 and step 2. LIBRARY (fix 6).
  - Attribution density (research-and-sourcing 6, fix 17: "once per source per section") is **violated (low)**. The fill-valve section names Fluidmaster four times: L54 "Fluidmaster says it installs", L61 "Fluidmaster says replace it", L71 "Fluidmaster warns", L79 "Fluidmaster says they damage". Overall it's 18 source mentions in 113 sentences, against 24 in 77 in iter-01: better, but not to the rule.
- **F7 PASS.** No pointing without naming. No run of three or more sentences names nothing showable. The weakest spots, L8-L9 and L55, are single sentences.
- **F8 PASS** (iter-01's W3 fixed). Every pack safety point is at its step:

  | S | Pack maps to | Script |
  |---|---|---|
  | S1 shut-off, clockwise | steps 1, 4, 5a, 6, 9b | L11-L12 (located, direction given; deliberately left on for F3's look), L44 "Turn the shut-off clockwise till it stops", L57 "Turn the water off again", L88 "close the shut-off", L111 "turning the valve clockwise until it's fully closed" |
  | S2 fragile lid | step 1 | L13-L14 |
  | S3 hand-tight | 5g, 5h | L70-L72 "hand-tight only. Easy does it, because Fluidmaster warns…", "by hand" |
  | S4 no bleach or chlorine drop-ins | after 5k and 9j | L79, L127 |
  | S5 water on the floor | 5i, 9h, any time | L12, L75, L120 |
  | S6 supply connector | 5c | L60-L61 |
  | S7 dye stain | 6 | L96 |

  No safety line was cut to clear a scanner flag. The drafts show safety lines being reworded, never deleted. The evidence block's Safety line is accurate.
- **F9 PASS, with one label note.**
  - Rule 1: question opening plus cost turn is a new combination.
  - Rule 2: three bridge moves, all swapped against 10-12.
  - Rule 3: personality changed.
  - Rule 4: no logged line comes back.
  - Rules 5 and 6: n/a.
  - Closing: a practical next action, the same as 10-05 but not 10-12. Allowed.
  - Label: "doubter in the comment-section voice (real comment)". L85 is a symptom report, not doubt. The pack's actual objection ("I followed along & mine is still running. So now I guess I need to replace that entire fill valve system??") is answered only implicitly (L86). Low.
- **F10 PASS**, apart from the "502" pronunciation note (section 2).

### Claims policy (named companies)

Every attributed claim is in the pack and is said within the pack's wording ("can", "says", "listed at"). L71's "flood the bathroom" and L48's "sprays straight up at you" add concreteness, not facts. Nothing negative is said about any company. **PASS.**

### Nothing from the voice samples as content

**PASS.** Checked step by step above (F6). The only shared 5-grams with the samples are "each side of the flapper", "on each side of the" and "the chain from the flush", all from pack steps 9d and 9g.

### The writer's AUDIT EVIDENCE, line by line

| Line | True? |
|---|---|
| Verdict: PASS (round 2 of 3) | **Not earned** (D1b, B7, F1 branch order, C2). It's also **unverifiable**. Draft 4 to draft 5 (10:35:10 to 10:35:39) changed one word ("getting" to "leaking", L21). If that was round 2's fix, round 2 applied a fix and "can't award its own pass" (audit, "How the audit runs" 4), so a round 3 was needed. Nothing records what each round found. |
| Hook: A2 not run | True. |
| Promise map | True. |
| Numbers | True for every number listed. "400H", "one-page" and the "fourth cause" count are unlisted (trivial). |
| Scanner | True. My independent run matches it exactly. |
| Voice: matched line | Fair. |
| Voice: persona line | **Misleading.** One short sentence quoted from a script that averages 17.2 words per sentence (D1b). |
| Safety | True and complete, including the disclosed step-1 deviation. |
| Originality: 7/7 | **Overstated.** #2 isn't evidenced. #6 is partial (same opening move as the reference). #7 is thin. 5/7 holds. |
| Not a clone (E3) | **Partly overstated.** The voice and sourcing differences are true. The angle contrast ("against an inspector sorting by symptom") isn't real, because the script sorts by symptom too. |
| Custom element (E4) | Partly. The listing screenshots count; the pencil and food-coloring shots and the CTA segments don't. |
| Rules (F): clean | **False on F1** (brief's "parts last" against the fill-valve swap before the flapper's free checks). Low misses on F3 (the L39 embellishment) and F6 (attribution density). The "F9… doubter voice" wording also overstates. |

---

## 4. Against the source and against iter-01

### Against the source (Morgan Inspection, 6:05)

| Point | Source | iter-02 | Better? |
|---|---|---|---|
| Both symptoms in the hook | Yes, first sentence | Yes, L4-L5 | Equal |
| Diagnosis by symptom | On/off is the flapper; constant is level, then fill valve | The same, plus an instant overflow sort (L16-L21) and a dye test | **Yes** |
| Free checks before parts | Chain, seat, dial, debris flush, then replace | Level, flush, then replace; chain, seat, then a new flapper | Equal within each branch. **Worse across branches**: the source reaches the flapper (the most common cause) at 0:25; iter-02 at about 7:34. |
| Fixes the viewer can do | Both replacements sent to "a separate video" | Both replacements in full, with safety at each step | **Much better** |
| Concrete numbers | $15, 5-10 min, ½-1 in, about 5 s, ⅛ turn, 10-15 min, all unsourced | 25-plus numbers, all traced; prices "listed at"; the maker's claim qualified | **Yes** |
| Wind-up, anecdote, "separate video", misnamed "fill tube", recap, thanks-for-watching | All present | None. The overflow tube is named correctly (L17). | Fixed |
| Speed to first action | Tank open 0:25, first test about 0:40 | Lid off about 1:00, sort at about 1:30-2:05 | Slower than the source, much faster than iter-01 |
| Clone (E3) | | No copied wording (no 8-gram; the 6-grams are a measurement phrase and a pack step). Same title verbatim, same hook move, same cause set reordered; voice and sourcing clearly different. | Not a clone; E3 thin on angle |

**Promise delivered at least as well?** Yes, and on "how to fix it" clearly better, because the source punts both replacements. The one way it serves its audience worse is the order: the on-and-off viewer waits more than seven minutes.

### Length

| | Source | iter-01 | iter-02 |
|---|---|---|---|
| Spoken words (excluding marker lines) | 969 | 1,402 | **1,941** |
| Without CTAs | 969 (no offer); about 800 without wind-up, anecdote and outro | 1,277 | 1,819 (CTA blocks: 122) |
| Runtime at 150 wpm | 6:28 (6:05 actual) | 9:21 | **12:56** (12:08 without CTAs) |
| Sentences / mean length | 88 / 11.0 | 77 / 18.2 | 113 / 17.2 |

**Where the extra length comes from:**
- The fill-valve replacement: L57-L79, 386 words.
- The flapper replacement: L111-L127, 295 words.
- Together that's 681 words, about 4:30. iter-01 had neither (that was its C5 failure). Fix 6 now requires them.

**Is it honest?** Every paragraph passes the progression test (retention 4), and none is filler. Trimmable without losing anything, about 80-120 words:
- L115, "Wipe the rim of the drain opening so there's no sediment left for the new one to sit on.", re-teaches L102-L103's seat cleaning, done a minute earlier. It's pack step 9e, but it could be "the rim you just cleaned".
- L118, the chain slack, re-teaches L100. Only L119's "slow, weak flush" is new.
- L30-L31 (41 words) are a dead end as written. Either make them useful (point float-ball owners to the replacement) or cut them to one line.
- L52-L55 (53 words) could lose the repeated $14.98 (L7 already compared the prices).

So the length is honest but long for a "why + fix" video aimed at a homeowner over 50. The real retention problem is the branch order, not padding. Moving the flapper branch first (Fluidmaster's "most common problem") would put the most common case's fix at about 2:00, not 7:34, at no cost in words.

### iter-01 problems: fixed, remaining, new

**Fixed:**
- W1 misattribution: L29 is now Fluidmaster only.
- W2 sample content: every step is from the pack.
- W3 safety: all seven S-points at their steps, none deleted.
- W4 triple diagnosis: now two mentions, the second adding something.
- W6 stat digits.
- W7 "ears" explained.
- W8 padding lines gone.
- W9 the hook names both prices.
- W10 both symptoms in the hook.
- C5: both replacements delivered in full.
- The slow start (2:25 down to about 1:00).
- The opening-move label.
- The evidence block now carries Hook, Safety, E3 and E4 lines.
- The scanner hang.
- The tag-density ambiguity.

**Remaining:**
- The persona's short sentences: 18.2 then, 17.2 now. D1b was added but has no measure.
- The evidence block overclaiming: originality 7/7 (was 6/7), the persona line, an unverifiable round count.
- The mid-CTA value line describes what the video itself does.
- A2 still can't run (the fixture samples weren't updated, and the gate accepts samples with no opening).
- The number check still lets "$200 for a visit" and "20 years" through.
- The "[slightly amused]" line about a named company.

**New:**
- The branch order serves the most common cause last, and puts a part before free checks, against the brief's angle (F1, B5).
- The length is 1,941 words (about 13 minutes).
- Synonym rotation for the shut-off, driven by the "reword safety lines" rule plus the echo flag (H6).
- Unexplained parts: refill tube, lock ring, shank washer, piston-valve.
- The float-ball dead end.
- Attribution clustering (Fluidmaster x4 in one section).
- The CTA chart implies printing.
- 3b's hook template equals the reference's hook (E3, E1 #6).

---

## 5. Would this be safe to upload unread?

**Yes on safety, but its PASS isn't a true PASS.**

Safe:
- Nothing in it is false, fabricated or dangerous.
- Every number traces to a dated, sourced pack line and is rounded the cautious way.
- Every safety point sits at the step that needs it.
- Every claim about a named company is in the pack.
- The offer is price-silent and accurate apart from one mild implication.
- Nothing is copied from the source or the samples.

A viewer who follows it will fix their toilet safely, which iter-01 couldn't promise for the fill valve.

Not a true PASS: by the rubric it's a FIX-THEN-PASS.
- The persona voice is missed (D1b, B7).
- The branch order goes against the brief's angle and buries the most common cause at 7:34 (F1, B5).
- A few low items remain (C2 terms, the L39 embellishment, attribution density).

The evidence block still overclaims in three places (originality, E3 angle, the persona line), and `Rules (F): clean` is false. That matters more than any single line, because "uploaded unread" only works if the audit's word can be trusted. This run's slips are all about quality and retention, not truth or safety, which is real progress. The two checks that slipped (D1b and branch order) are the ones the library can't yet measure or doesn't yet define.

---

## 6. Fixes, ranked

### LIBRARY problems (these matter most)

| # | Severity | File and rule | Problem | Suggested fix |
|---|---|---|---|---|
| 1 | **High** | `core/script-scanner.py` `number_check` / `close`; audit D4; `tests/run_checks.py` 9c | Fix 1 is partial. Re-running iter-01's probe still passes three invented numbers: "$200 for a visit" (it matches the "$200" in the pack's ADVERSARY *comment*, a cost the pack says never to state), "20 years" (matches "20 minutes"), and "9,000 gallons". "Numbers not in pack 0" is still weak evidence on a Hold-level check. CHANGES.md overstates the fix. | Match a number together with its unit or noun (minutes, years, gallons, $). Exclude quoted comments (DOUBTER and ADVERSARY quotes) as a money source, or any line marked "don't state". Add the three probe lines to 9c as must-flag cases. |
| 2 | **High** | `core/greenlight-audit.md` D1b; `core/voice-anchoring.md`; `core/persona-profile-template.md` "How they talk"; scanner | D1b exists but can't fail. "Quote one line that shows it" lets a writer quote one of 12 short sentences from a script averaging 17.2 words (iter-01 18.2, source 11.0). The persona's "short sentences" has now been missed in both runs. | Make it measurable. The scanner reports mean sentence length, the share at 8 words or fewer and at 23 or more, and runs of 4 or more long non-step sentences. The template takes an optional numeric target, or core sets a default when a persona says "short sentences" (for example, mean 13 or under, at least 25% at 8 or under). D1b fails when off target, and the evidence line reports the numbers, not a chosen line. |
| 3 | **Medium** | `core/script-structures.md` 3b; `core/retention-mechanics.md` 10 (B5) | 3b says "each cause, cheapest and quickest check first" but says nothing about branches after the sort test, about likelihood, or about the brief's "free first, parts last" across causes. Result: the flapper (F6, "the most common problem") starts at about 7:34, behind a 2:34 fill-valve replacement, and a $14.98 part comes before two free checks. Viewers on that branch get about 5.5 minutes with nothing for them. | Add to 3b: after the sort test, take the branches in order of how common the pack says each cause is (or by the brief), and keep each branch self-contained. Where the brief says "parts last", every free check across causes comes before any part swap, or the script says plainly where each branch starts ("if the water was below the tube, this next part is yours"). |
| 4 | **Medium** | `core/script-structures.md` 3b hook; audit E3 / E1 #6; `core/variety-rotation.md` | Fix 4 wrote the reference video's own hook into the structure ("the symptom… covering every version the title promises… plus the promise"), almost word for word the judge's description of the source. Every diagnose-and-fix script now opens on the competitor's move and lists the same cause set, which erodes E3 (angle) and E1 #6, and risks template scripting (E2) across a channel. | Keep "cover every version the title promises" as a content requirement, not a move. Let the opening move rotate (a number, the problem at its worst, a contrarian line) per `variety-rotation.md`. Add to E3: when the hook's move and promise match the brief's reference structure, the angle must differ in a stated, checkable way (not "priced" or "sourced", which are sourcing). |
| 5 | Medium-low | `core/humanizer.md` H18 safety clause and H6; scanner echo | Fix 2 says a repeated safety line is "reworded each time". The scanner still counts it as an echo, so the writer renamed the shut-off six ways across the drafts to clear flags ("shut-off valve behind the toilet", "the shut-off", "the water", "the valve behind the toilet", "close the shut-off", "the valve"). That's H6 (fix-on-sight), and "the valve" turns ambiguous next to the fill and flush valves (L111). | Say that the same plain safety instruction, repeated at each step, is not an echo and keeps its plain wording. Have the scanner skip 4-grams inside sentences that carry a shut-off or turn-off instruction, or list them separately as "safety repeats (expected)". |
| 6 | Medium-low | `core/research-and-sourcing.md` 8 (verification pass) and 9 (STEPS completeness) | Three pack defects reached the script: (a) step 1 shuts the water off before step 2's look, which F3 says needs the water on; (b) W3's "3 to 5 gallons per minute or 3,600 gallons a day" doesn't add up; (c) float-ball valves are an "Option" with no steps, so the level-too-high fix doesn't exist for that viewer (L30). The writer handled (a) and (b) well, and (c) not fully. | Verification pass: check each step against the facts it cites, and check a source's own arithmetic (keep and attribute it, or drop it). STEPS completeness: a named variant ("older float-ball valves differ") gets its steps or a scope line the script must say ("if yours has a float ball, replace it with a piston type using the steps below"). |
| 7 | Low | `core/workflow.md` 2 (voice-samples check); fixture `test-plumbing-voice-samples.md` | Fix 7 asks for an opening sample but accepts samples without one, and the fixture wasn't updated, so A2 has been "not run" in both iterations. | Either have the gate ask once for an opening sample (one numbered line) before accepting, or keep accepting and add an opening clip to the fixture so A2 is actually tested. |
| 8 | Low | `core/greenlight-audit.md` evidence block (Verdict, Originality) | The round count can't be checked (draft 4 to 5 changed a word with no record of the finding). Originality #2 and #6 contrasts can be asserted loosely. | Verdict line: "round n; round 1 fixed [..], round 2 fixed [..]". Originality #2 and #6 and E3 must quote the brief's Reference angle and structure fields and name the specific difference. |
| 9 | Low | `core/greenlight-audit.md` E4 | At script stage the writer listed generated shots and the CTA format as custom elements. | Define E4 for scripts: name at least one real-capture element (a listing screenshot, a document page, a real comment) for the editor. Generated footage and the channel's standing format don't count. |
| 10 | Low | `core/research-and-sourcing.md` 6 (fix 17) | "Once per source per section" was ignored (Fluidmaster x4 in L52-L79), and nothing checks it. | Have the scanner count source names per paragraph or block and flag a third mention. |
| 11 | Low | `core/research-and-sourcing.md` 10 (honest wording) | "Up to half an hour" for a test whose source says "at least 25 minutes" turns a floor into a ceiling. | Honest wording keeps the source's direction: "give it a good half hour", "at least 25 minutes". |
| 12 | Low | `core/workflow.md` 4 (voice misreads) | Model numbers ("502") will be read as "five hundred two". | Add model and part numbers to "spell out anything a voice might misread" ("Fluidmaster's five-oh-two flapper"), or tell the writer to name the part without the number. |

**iter-02 changes that made things worse, or didn't work:**
- **Fix 4 (3b):** it fixed the slow start and the triple diagnosis, but its hook is the reference's hook (library fix 4), and it has no branch-order rule (library fix 3).
- **Fix 6 (complete STEPS):** correct in principle and it fixed C5, but with nothing to compress already-taught steps and no branch order, the script grew 38% to about 13 minutes (library fixes 3 and 6).
- **Fix 2 / H18 ("reword"):** it pushes writers toward H6 synonym rotation (library fix 5).
- **Fix 5 (D1b):** no effect, because nothing measures it (library fix 2).
- **Fix 1 (number check):** partial (library fix 1).
- **Fix 7 (opening sample):** no effect in the test (library fix 7).

### WRITER slips (the rule was clear)

| # | Severity | Rule | Line | Fix |
|---|---|---|---|---|
| W1 | Medium | D1b and B7 (persona "short sentences"); the evidence block's "persona line" | Mean 17.2 words per sentence. L7 is 32 words in the hook; L20 38; L21 35; the long run at L82-L88. A short line was quoted as proof. | Split the compound sentences at ", and" or ", so" (33 sentences contain ", and"). Report the persona line honestly. |
| W2 | Medium | F1 (brief Angle "free adjustments first, parts last"); B5 | The fill-valve swap (L57-L79) comes before the flapper's free chain and seat checks (L98-L105), and the most common cause starts at about 7:34. | Run the flapper branch first, or bring the chain and seat checks forward. |
| W3 | Low-medium | Evidence truth ("Evidence both ways") | Originality 7/7 (#2 unevidenced, #6 partial); E3's angle contrast; `Rules (F): clean`; E4 lists generated shots; "round 2 of 3" unverifiable | Report what was actually checked; 5/7. |
| W4 | Low-medium | C5 | L30-L31: the float-ball owner gets no fix. | One line pointing them to the replacement steps (F13 plus 5a-5k). |
| W5 | Low | C2; persona "explains each one once" | L63 "refill tube", "shank washer"; L66 "lock ring"; L31 "piston-valve" unexplained | Half a clause each, or drop the parts the viewer doesn't act on. |
| W6 | Low | research-and-sourcing 6 (attribution once per source per section) | L54, L61, L71, L79: Fluidmaster four times in one section | Keep L54 and L71; make L61 and L79 plain instructions. |
| W7 | Low | offer-rules 1 (never embellish); cta-and-endings 1 (value beyond the video) | L39 "so you can keep it next to the toilet while you sort this out": the chart isn't listed as printable, and it restates what the video does | Lead the mid-CTA with the printable parts checklist for the store trip. |
| W8 | Low | F9 log accuracy | `doubter in the comment-section voice (real comment)`: L85 is a symptom report, not doubt | Log it as it is, or use the pack's real objection ("now I guess I need to replace that entire fill valve system??"), which L86 already answers. |
| W9 | Low | H18, B3 | L115 re-teaches the seat cleaning from L102-L103; L118 re-teaches the chain slack from L100 | "Wipe the rim you just cleaned"; "Clip the chain back with the same slack". |
| W10 | Low | workflow 6 (pauses only at natural beats) | L183 "[short pause] Let the tank fill." | Drop it, or move it to L185, the line right before the mid-CTA. Not inside the CTA block, where only one [warm] is allowed. |
