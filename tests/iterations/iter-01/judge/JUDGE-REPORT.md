# iter-01 judge report: plumbing-01 (TEST Plumbing, no niche pack)

TEST run. Judge: independent re-audit of the writer's output against `core/` (the rubric), the TEST persona, the pasted inputs, the scanner and the judge-only source script.

Line references like "L28" point to `run/writer-turn-4.md`.

**Verdict in one line:** the gate behaved correctly on all five turns and the format is close to perfect. The script is accurate, sourced and better than the source on substance. But the writer's `VERDICT: PASS` / `Rules (F): clean` is not true. I find a FIX-THEN-PASS: a misattributed claim about a named company, a safety line deleted to clear an echo flag, a fill-valve replacement with no shut-off and no steps, step content borrowed from a voice sample, an echo, and a persona voice that isn't met. No Hold. Several of these trace back to gaps in the library rather than to the writer.

## Evidence files (all in this folder)

| File | What it is |
|---|---|
| `script-from-writer-turn-4.md` | The script part of writer turn 4 (SCRIPT TYPE through the closing line). Identical to `writer-work/final-script.md` apart from the SCRIPT TYPE header. |
| `scan-full.txt` | The full scanner run (`--rules` persona, `--pack` research pack, `--refs` source script and voice samples). **It hung in the number check and was killed by `timeout 20` (exit 124).** Everything above the number section printed. |
| `script-numcheck-split.md` / `scan-numcheck-split.txt` | The same run on a copy where "two-inch", "three-inch", "Ten-Minute" and "one-page" are split into two words. It finished (exit 0). |
| `numcheck-probe.md` / `numcheck-probe-output.txt` | A six-line probe of invented numbers, showing what the number check lets through (section 3, D4). |
| `script-body.txt`, `vo-copy-from-writer-turn-4.md`, `vo-stripped.txt` | Used for the mechanical VO check: the script, the VO copy, and the VO copy with its tags stripped. |
| `source-spoken.txt` | The source's spoken words, with timestamps removed, used for counting. |

Scanner result (split copy): fix-on-sight 0, shape-test flags 0, "Most..." 0, reframes 0, filler 0, echo 1 (`number x4: "10"`), numbers not in pack 0, copied 0 against both the source and the samples. A manual n-gram check finds no shared 6-word run with the samples. The source shares only "an inch below the top of the", which is a measurement phrase and fine. The hang reproduces on a one-line file, "Two-inch flappers.", so the bug is in the script side of `word_numbers()`. The pack contains no hyphenated number words. I did not fix the scanner.

---

## 1. Gate behavior

| Turn | Operator | Expected (PROTOCOL) | Writer replied | Result |
|---|---|---|---|---|
| 1 | `START TEST`, no channel | One question plus the numbered TEST list, nothing else | "TEST: DO NOT UPLOAD." / "Which channel is this script for? Reply with the number or the exact name." / "1. TEST Plumbing" | **PASS.** The TEST line is required by `workflow.md` 1.3, so it's not "something else". |
| 2 | `1` | One numbered message listing all five missing inputs, one line on validity each, nothing about tone, length, type, provider or CTA | "TEST Plumbing it is. Please paste these five inputs:" plus title, brief, research-pack, rotation-log and voice-samples, one line each. The research-pack line correctly adds "re-checked for this script since the channel has no niche pack" (research-and-sourcing 7). | **PASS** |
| 3 | Title, brief and 2-line log; "just write it" | Refuse; ask only for research-pack and voice-samples | "I can't write it without the other two, though, even for a simple topic: …" then lists only those two | **PASS.** Nit: workflow 2 says "reply naming only what's missing". The two sentences of reasons are extra but harmless. |
| 4 | Pack and samples | No questions; full skeleton or a correct NOT READY | Full skeleton, no questions. The gate checks were right: Verified on 2026-10-19, title matches word for word, P1-P3 dated today, every gap "Not blocking", samples 74 s / 85 s / 85 s from three channels with sources. | **PASS** on gate behavior. Whether it *should* have been PASS is section 3. |
| 5 | `START TEST` again | Only `Start a new chat for the next script.` | Exactly that line | **PASS** |

**Ambiguities the writer had to resolve:**
- **TEST label on the one-script-per-chat reply.** `workflow.md` 1.3 says "The first line of every test output is `TEST: DO NOT UPLOAD.`" `workflow.md` 2 says "reply only: `Start a new chat for the next script.`" The two contradict each other. The writer chose "only", which is defensible. LIBRARY (low).
- **A rotation log with fewer than five lines.** "Fewer only if the channel has fewer scripts" can't be checked at the gate. The writer assumed "channel has 2 scripts" (`writer-work/plan.md`, GATE STATUS); the operator never said so. LIBRARY (low): the rule should say what to do (accept, or ask the VA to confirm the count).
- **Turn 3's explanation.** The "naming only what's missing" rule and the "No way around it" rule don't say whether a reason may be given. That's harmless here.

---

## 2. Format and skeleton (workflow.md sections 4-6)

| Item | Result | Evidence |
|---|---|---|
| TEST line first | PASS | L1 |
| SCRIPT TYPE | PASS | "SCRIPT TYPE: Talking Head" (persona: Talking Head) |
| Clean prose (no headings, brackets, stage directions, links, emoji) | PASS | None in L5-L101. Zero colons and zero ellipses. |
| One sentence per line | PASS | 77 spoken sentences, each on its own line |
| Marker lines | PASS | Both start markers read `===START CTA(TEST: The 10-Minute Toilet Fix Guide)===`, matching the persona's printed title character for character. Each marker is alone on its line. The CTA text starts on the next line and `===END CTA===` sits directly under the last sentence. A blank line comes before and after each block. |
| Mid-CTA block includes the return line | PASS | L49, "So, the float's set lower, and water's still finding its way into that tube.", is inside the markers |
| End CTA through its ask; then one closing line | PASS | L96-98 end on "Subscribe too, so the next fix shows up in your feed." L101 "Grab a pencil, take the lid off, and start with that overflow tube." is 13 words and the last line. |
| Number style | **FAIL (low)** | L24: "three to five gallons a minute". `workflow.md` 4 says "Prices, years and stats are digits". This is a stat (W3), so it should be "3 to 5 gallons a minute". |
| Measurements spelled out | PASS | "about half an inch", "an eighth of a turn" |
| FORMAT CHECK line | PASS | Matches the template field for field |
| ROTATION LOG ENTRY fields | PASS on fields, **FAIL (medium) on accuracy** | Every field is present, including `end-CTA: "For the trip to the hardware store, the"` (8 words) and `mid-CTA` (8 words). Accuracy problems are under F9 below: the opening-move label and the adversary voicing. |
| AUDIT EVIDENCE fields | PASS on fields, **FAIL on truth** | All seven lines are present. The Scanner line carries `copied 0` with the reason ("copy guard run against the three voice samples; no niche pack refs exist"), and the number-check workaround is disclosed. What's claimed but not true is listed in section 3's last part. |
| VO COPY: identical words | **PASS (verified mechanically)** | Stripping `^\[[a-z -]+\] ` from the VO copy and running `diff` against L5-L101 gives no differences, marker lines included (`vo-stripped.txt`). |
| Tag density | PASS (high end) | 16 tags over 1,402 spoken words is 1 per 88 words (rule: about 1 per 80-120). Local clusters: three tags within six sentences at L169-L174 ([thoughtful], [slightly amused], [emphatic], about 80 words), and three within L148-L156. That's within the rule as written, which doesn't say whether density is a script average or local. LIBRARY (low). |
| No adjacent tags, max one per sentence | PASS | No two consecutive sentences are tagged |
| Allowed tags only | PASS | [matter-of-fact] x3, [thoughtful] x3, [warm] x3, [emphatic] x2, [slower] x2, [short pause] x2, [slightly amused] x1 |
| [slightly amused] only on honest candor | PASS | L172, "[slightly amused] That's the maker talking, and I'd plan on longer than that the first time." It's a true limit on a maker's claim. Watch that the tone doesn't read as mocking a named company. |
| CTA sections: at most one [warm], nothing else | PASS | L156 and L206 each carry one [warm] at the start and nothing else |
| Pauses | PASS | L152 is the beat before the mid-CTA lead-in; L211 is before the closing line |
| Markers untagged and reproduced | PASS | Yes |
| Nothing after the VO copy | PASS | Yes |

---

## 3. Independent audit (greenlight-audit.md)

### Group A: the hook

- **A1 PASS.** L5, "Your toilet keeps running, so you lift the lid off the tank, and there's water spilling into that open tube standing up in the middle.", names the subject and matches the thumbnail. It's 25 words, about 10 seconds, with no greeting. Weakness compared with the source: the hook pictures only the never-stops case (water into the overflow). The other half of "keeps running", the toilet that refills every few minutes, isn't mentioned until L17, about 1:15 in. The source covers both in its first sentence.
- **A2 NOT RUN, and not reported.** All three voice samples are mid-video clips (0:21, 1:10, 3:08), so there's no real hook to grade against. By the rule, A2 should read "not run". The writer's evidence says nothing about A2, because the evidence block has no field for it. LIBRARY (medium): add an A2 line to the evidence block, and have the no-pack `voice-samples` input include at least one opening (the first 15-20 seconds of a winner).
- **A3 PASS.** The promise map holds. Three causes: L34-40, L52-64, L69-89. "Tell which within about 15 minutes": L29-31 and L71-74. "Why": L17-25.
- **A4 FAIL (low).** L7 says "the fix turns out to be one screw they could've turned themselves, or a rubber flapper listed at $6.48." One of the three causes the hook announces (a worn fill valve) costs $14.98-$18.99 (L60), and the fourth cause goes to a plumber (L92). The writer's own promise map shows the stretch: "fix is a screw or a part listed at $6.48 -> … fill valve $14.98 (P2)". It's within framing limits, but not exact.

### Group B: retention

- **B1 PASS.** "Why won't it stop, and do you have to pay somebody…?" (L6) is answered at L17-25, L7 and L92. "Still got water trickling…?" (L42) is answered at L43 and L52-58.
- **B2 BORDERLINE, from a library conflict.** The line after the hook is L10, "A running toilet comes down to two parts in that tank.", which is background. `retention-mechanics.md` 3 says the line after the hook "never sets up background", and `script-structures.md`'s shared rules repeat that. But the same file's "Why it happens" structure puts **Layer 1** (the simple version plus an everyday comparison) straight after the hook. The writer followed the structure. LIBRARY (high, see fix 4).
- **B3 PASS, with padding noted.** L18, "Korky, a company that makes toilet repair parts, explains it like this.", announces rather than adds. L25, "So it's one of three things, a float set too high, a fill valve that won't shut off, or a leaking flapper.", restates L8. L39 adds nothing (and is wrong, see F5).
- **B4 FAIL (medium): slow start and context dump.** The first thing the viewer *does* is L27, "Lift the lid off and set it down on a towel.", which comes about 360 words (about 2:25) in. Everything before it is hook plus explanation (L10-25, 273 words). The source is in the tank at 0:25 and on the first test by about 0:40. Partly LIBRARY (the structure mandates layers before "what to do"; fix 4), partly writer (the 115-word parts tour could be half that).
- **B5 PASS.** Bridges are honest and short-range. L43, "there's one more free thing to try before you buy a new one", is delivered at L52-56. L66-67 likewise. No stretch longer than about 90 seconds without a payoff.
- **B6 PASS.** The reasoning uses "so" and "because" (L19, L23).
- **B7 FAIL (low).** Sentences average 18.2 words (median 18). Only 3 of 77 are 8 words or fewer, 18 are 23 or more, and 34 of 77 sentences contain ", and". It's an even, mid-to-long, compound rhythm. The source averages 11.0 words, with 33 of 88 sentences at 8 words or fewer. See also D1, persona.
- **B8 PASS / n/a.** Not a ranked list. The order follows Fluidmaster's check sequence (F3/F6) and the brief's "free first, parts last".
- **B9 FAIL (low).** L18 announces the obvious ("explains it like this").

### Group C: clarity

- **C1 PASS.** One thread.
- **C2 FAIL (low).** L85, "unhook the old flapper from the ears on each side": "ears" is never explained. Flapper, fill valve, overflow tube, seat and flush valve are all explained.
- **C3 PASS.**
- **C4 n/a.**
- **C5 FAIL (medium): the fill-valve fix isn't delivered as a fix the viewer can do.** L58-64 give the diagnosis, the lifespan, two prices, the maker's install-time claim, the height mark and "hand-tighten it". There's no shut-off, no draining the tank, no supply line and no lock nut. The brief promises "each cause gets a fix the viewer can do". The research pack's step 5 is only "Replace the fill valve", so the writer couldn't add steps. It should have stopped (workflow 3: "a missing fact … stops with NOT READY") or the pack should have carried the steps. LIBRARY (fix 6) plus writer judgment. The ending doesn't recap: PASS.

### Group D: voice

- **D1 FAIL (medium) against the persona; PASS against the samples on shape.** The writer's matched line (L52 against Sample 2's "Once that water is shut off we're going to go ahead and flush the toilet to empty the tank out.") is a fair shape match. But the persona says "plain and unhurried, **short sentences**", and the script averages 18 words with three short sentences in 77 (B7). The audit has no check for the persona's "How they talk" line. The samples themselves are long run-ons, so "match the samples" and "short sentences" point in opposite directions. LIBRARY (fix 5).
- **D2 humanizer sweep: one FAIL.**
  - H1-H5, H7-H17, H19, H22, H23: no hits. Triads are all concrete, for example L56 "Shut the water off, check for debris, and put the cap back on."
  - **H18 echo FAIL (medium).** "Refills every few minutes = the flapper" is said three times: L17 "If your toilet refills on its own every few minutes, the flapper's leaking.", L67 "or the tank still tops itself up between flushes, the leak's down at the flapper.", and L70 "If yours refills in short bursts every few minutes, that's water slipping past the flapper". Only the third adds anything ("a new fill valve won't touch it"). H18 allows two mentions. The theme of "one of three things" also comes back twice (L8, L25).
  - **Counts:** H20 0 ("Most of the time", L8, isn't a "Most people…" opener), H21 0, H23 0. These agree with the scanner.
  - **H6 (natural variation, not a fail):** the water-off instruction takes several forms: "Turn off the supply valve" (L52), "Shut the water off" (L56, L71), "Turn off the water" (L85), "open the supply valve again" (L89).
- **D3 PASS.** Fix-on-sight 0, copied 0 (refs: source plus samples), "10" x4 judged correctly: four different facts.
- **D4 PASS on tracing, with two notes.** Every number traces to the pack:

  | Script number | Pack line |
  |---|---|
  | $6.48 (L7, L88) | P1 "listed at $6.48", the 2 in. 502P21 |
  | one of three / most of the time (L8, L25) | GAPS honest wording |
  | about 15 minutes (L8) | GAPS honest wording (F6 10-15 min, F8 10 min) |
  | three to five gallons a minute (L24) | W3 |
  | 400H (L35, L60) | F4, P2 |
  | about half an inch (L38, L63) | F4, F5 |
  | an eighth of a turn (L53) | STEPS 4 "1/8 turn" |
  | 10 to 15 seconds (L54) | STEPS 4 |
  | 5 to 7 years (L59) | F12, Korky |
  | $14.98 (L60) | P2 |
  | $18.99 (L60) | P3 |
  | under 10 minutes (L61) | F14, said as the maker's claim |
  | 10 to 15 minutes (L71) | F6 |
  | 10 minutes (L74) | F8 |
  | thousands of gallons a year (L76) | W1 |
  | one or two links (L79) | F9 |
  | two-inch and three-inch (L86) | F11 |
  | every five years (L93) | F12, EPA |
  | Ten-Minute, one-page chart, five parts, first link (CTAs) | Persona profile offer facts |

  **Rounding:** prices are exact, and "I'd plan on longer than that" rounds time up, which is good. The note is "within about 15 minutes" (L8). The pack's own sources give 10-15 min (Fluidmaster), 15-20 min (NYC DEP) and "at least 25 minutes" (Korky). By D4, "time rounds up", so this is rounded down. It's the pack's prescribed "honest wording", so the writer followed it. LIBRARY (low): the research stage's honest wording must itself obey D4.

  **The scanner's "numbers not in pack 0" proves very little** (`numcheck-probe-output.txt`). Against this pack, these invented lines all pass:
  - "$6.90" for the flapper: the tolerance is ±0.5 absolute, so a price can drift up, against D4.
  - "A plumber charges $200 for a visit": $200 is in the pack only inside a comment, and the pack says *not* to state a service-call cost.
  - "The fill valve lasts 20 years": 20 comes from "15-20 minutes".
  - "9,000 gallons a year": within 5% of 9,300.

  Only 45 and 17 were flagged. Numbers of 3 or less are never checked, and offer numbers are checked against the research pack instead of the persona profile. On top of that, the check hangs on any hyphenated number word. LIBRARY (high, fix 1).
- **D5 PASS.** Reframes 0. No poster-quote lines.

### Group E: authenticity

- **E1 PASS (5/7 with evidence; the writer claimed 6/7).**
  - #1: the NYC DEP brochure, the 2009 EPA fact sheet and the 400H installation PDF go beyond page one.
  - #3: editorial voice (L62, L87, L92).
  - #4: Korky, Fluidmaster, EPA WaterSense, NYC DEP, Home Depot.
  - #5: the short-burst refill means a fill valve won't fix it (L70).
  - #7: thin (the catchphrase plus "I" opinions).
  - **#2 claimed without evidence.** The writer has no data on the top videos' angles, and the source's angle is the same: one of three, figure out which, simple fixes first.
  - **#6 claimed missing for an unverifiable reason** ("a why-it-happens structure like the 2026-10-05 drain script"). The rotation log has no structure field, so the writer inferred it from a title. LIBRARY (fix 3).
- **E2 PASS.** Copied 0 against the source and the samples.
- **E3 FAIL (medium) on a strict reading, not a Hold; the writer couldn't run it.**
  - **What mirrors the source:** the title is the source's title, verbatim. The structure mirrors it too: symptom split, three causes, then level, clean, replace.
  - **What differs:** voice (no wind-up, persona opinions) and sourcing (named manufacturer and agency documents against one inspector's experience).
  - **Angle:** it doesn't differ. Source: "almost always one of three common problems … how to figure out which … how to fix it". Script: "Most of the time it's one of three things … you can tell which one". E3 requires all three to differ.
  - The writer never sees the reference video, by design, and the evidence block has no E3 line. LIBRARY (high, fix 3).
- **E4 NOT CHECKABLE AT SCRIPT STAGE; not reported.** Nothing in the output addresses custom elements, though the "listed at" prices would support listing screenshots. LIBRARY (low).

### Group F: rules compliance

- **F1 PASS with notes.** The "Why it happens" fallback is followed: hook, Layer 1 (bathtub comparison L14), Layer 2 (L17-25), "Layer 3" (diagnose your own tank, L27-32), what to do, ending. The brief's "Format: … cause -> how to tell -> how to fix, for each cause" was only partly followed: the causes are front-loaded, then re-diagnosed later, which produced the H18 echo. "Flexible choices recorded" happened only in `writer-work/plan.md`; the output has no field for structure. LIBRARY (fix 4).
- **F2 FAIL (low).** About 150-180 words could go without losing anything: L18, L25, L39, the duplicate diagnosis at L67/L70, and half of the 115-word parts tour (L10-15). See section 4.
- **F3 PASS.**
  - The mid-CTA comes after the first real payoff: the free float fix is complete, ending L40 "it didn't cost you a thing".
  - It plays against an open question: L43 "there's one more free thing to try before you buy a new one".
  - It contains what the offer is ("an e-book download … called the Ten-Minute Toilet Fix Guide"), the added value ("a one-page chart matching each symptom to its likely part") and where to get it ("the first link in the description").
  - It returns with "where things stand" (L49).
  - There's no subscribe ask in the mid-CTA, which matches the persona.
  - The end CTA starts directly after the final content (L93). It carries the profile's added-value promise ("printable parts checklist … so you buy the right part the first time"), the facts ("covers the five parts inside a toilet tank") and where to get it, and ends on the persona's ask. Then one closing line. No recap, no thanks, no named future video.
  - Notes:
    - The mid-CTA's value line, "so you can line up what your tank's doing with the part that fixes it", describes what this very video does. "Printable" is the real extra and isn't said until the end CTA.
    - The end CTA has two asks (the guide, then subscribe). That's allowed by the persona, but it sits awkwardly with "One ask per moment" (cta-and-endings 1).
    - The persona's fixed end-ask wording collides with cta-and-endings 5, "change … the close" every time. LIBRARY (low).
- **F4 PASS.**
  - Offer facts come only from the profile: one-page chart, printable parts checklist, five parts, first link.
  - It's named as an "e-book download", is price-silent, has no backstory and no urgency.
  - The profile's own promise wording, "so you buy the right part the first time", borders on a result guarantee (offer-rules 5). LIBRARY (low).
- **F5 FAIL (medium): a claim attributed to a named company that it didn't make.** L39: "Fluidmaster's instructions say it doesn't need to be exact, and Korky's guide agrees." Only Fluidmaster says "(Does not need to be exact.)" (F4). Korky says only "about 1/2" below" (F5). The pack's "Korky agrees:" refers to the half-inch, not to exactness. claims-policy: "Nothing false or unsupported is ever stated as fact about a named company or person." WRITER. Otherwise PASS:
  - no life facts ("retired plumber" is never said)
  - "easy does it" used once (L28), within the cap
  - opinions are only opinions
  - outcomes are conditional ("If the water stops short of the tube and the valve shuts off, you're done", L40)
- **F6 FAIL (medium): content taken from a voice sample.** L85: "Turn off the water, flush the tank empty, unhook the old flapper from the ears on each side, and unclip the chain from the handle." The pack's step 9 gives only "old flapper unhooked from its ears" (as the visual). "Unclip the chain from the handle" and the flapper-specific "flush the tank empty" come from Sample 2 ("we're going to go ahead and flush the toilet to empty the tank out … disconnect the chain from the flush handle"). The samples file says: "Voice only, never content: the facts in these clips are not research and may not be used in a script." research-and-sourcing 1: "The script stage never adds facts the pack doesn't contain." The step is correct in practice, but the rule is explicit. WRITER, made possible by a thin pack (fix 6). Also "There's always a comment under videos like this…" (L69) is a generalization from two comments. It's acceptable as the comment-section voice, but "always" is framing.
- **F7 PASS.** No pointing without naming. No run of more than two sentences names nothing showable. The weakest spots are L18 and L62, which are single sentences.
- **F8 FAIL (medium): safety points dropped.** With no niche pack there are no "niche safety lines", so the research pack's SAFETY POINTS are the only ones. Results:
  - S1 is used (L52), but **not at the fill-valve replacement** (L58-64): no "turn off the supply" before a part that's screwed into a full, pressurised tank.
  - S2 and S3 are used.
  - **S5 ("water on the floor, immediately turn off water") was in draft 3 and deleted in draft 4.** Draft 3 had "If there's water on the floor, turn off the supply valve behind the toilet right away, clockwise until it's fully closed." Draft 3's scan flagged an echo ("turn off the supply" x3), and draft 4 removed the safety line to clear it.
  - S4 (no bleach or chlorine drop-in tablets, which damage tank parts) was never used.
  - LIBRARY (high, fix 2): no rule says which research-pack safety points must appear, and the echo rule has no exemption for safety instructions. The writer also chose to delete safety rather than rephrase.
- **F9 FAIL (medium): rotation-log accuracy.** Checking the cross-script rules against the two pasted lines:
  - **Rule 1.** The logged combination ("question the viewer is already asking" plus "cost turn") is new. **But the first sentence (L5) is a problem scene, not a question.** The logged move describes L6. Read as its first sentence, the opening is the "problem at its worst" or "universal situation" move. The `variety-rotation.md` example for "problem at its worst" is "The toilet's running again at two in the morning.", which is almost this line. That's the same move as 10-05 ("problem at its worst"), and guardrail 2 says to switch moves against the last 2-3 uploads. The thumbnail-match rule (retention 2: "the first line names what should be on screen") pushes every script toward a scene opener. LIBRARY (fix 8) plus writer labelling.
  - **Rule 2** PASS: two bridge moves (cost or effort at L43, progress at L66), both swapped against 10-12.
  - **Rule 3** PASS.
  - **Rule 4** PASS: no logged line or CTA opening comes back.
  - **Rule 5** n/a (two lines).
  - **Rule 6** n/a.
  - **Adversary field** is inaccurate: "paying for a visit over a few-dollar part, comment-section voice". The adversary is voiced plainly in the hook (L6-7); the comment-section voice is the doubter (L69).
- **F10** PASS apart from the stat-in-words slip (section 2).

### The writer's AUDIT EVIDENCE: claimed but not true or not shown

- `Rules (F): clean`: false. F5 (L39 misattribution), F6 (L85 sample content), F8 (S5 deleted, S1 missing at replacement) and F9 (opening-move label).
- `Originality: 6/7`: #2 has no evidence. The reason given for missing #6 rests on a structure the log doesn't record. The true evidenced score is 5/7, which still passes.
- `Verdict: PASS (round 3 of 3)`: unverifiable. Four drafts and four scans fit "sweep, then three rounds", but draft 2 was modified at 10:04, after its scan at 10:03. Each "full audit from group A" round took about a minute. Round 3's substantive changes (deleting S5, rewording the pencil test) happened between draft 3 and draft 4 with no record of an audit finding behind them. LIBRARY (low): ask the evidence block to list what each round fixed.
- A2, E3, E4 and F8 aren't reported at all; the block has no place for them.
- The promise map's "fix is a screw or a part listed at $6.48 -> … fill valve $14.98" shows the A4 stretch rather than resolving it.
- True and correctly disclosed: copied 0, the number-check workaround, the "10" x4 echo judgment, and every number-to-pack mapping.

---

## 4. Against the source

| Point | Source (Morgan Inspection, 6:05) | Script | Better? |
|---|---|---|---|
| Diagnosis by symptom | On/off is the flapper; constant means water level, then fill valve | The same split, plus an **instant** overflow-tube look (L29-31) and a dye-test alternative (L73-75) | **Yes** |
| Free checks before parts | Chain, smooth seat, level dial, flush the valve, then replace | Level, flush the valve, then replace; chain, seat, then a new flapper | **Equal, better laid out**. The flapper branch is more complete (size, bring the old one, $6.48). |
| Concrete numbers | $15, 5-10 min, ½-1 in, about 5 s, ⅛ turn, 10-15 min (all unsourced) | 18 numbers, all traced and attributed. Prices are "listed at". The maker's time claim is qualified. | **Yes** |
| Wind-up | "In this video, I'm going to show you … Let's get started." | None | Fixed |
| "Separate video" references | Two | None | Fixed. But the fill-valve replacement is now simply missing (C5), where the source at least pointed somewhere. |
| Misnamed part | Calls the overflow tube the "fill tube" | Names the overflow tube correctly and explains it (L15) | Fixed |
| Anecdote | "a canister type valve that I recently fixed for somebody" | None (claims policy) | Fixed |
| Recap | [5:26] recap plus "I bet 3/4 of the time" | No end recap. A mid-script restatement at L25. | Fixed (mostly) |
| Generic ending | "Thanks so much for watching … like … subscribe" | End CTA plus a practical next action | Fixed |
| Speed to first action | Tank open at 0:25, first test by about 0:40 | First action about 2:25 in | **Worse** |
| Both symptoms in the hook | Yes, first sentence | Only the overflow case in the hook | **Worse** |
| Clone (E3) | | Wording no (no 6-word overlap beyond a measurement phrase). Same title verbatim, same angle and structure; voice and sourcing differ. | Strict E3 fail, not a clone Hold |

**Length.**

| | Source | Script |
|---|---|---|
| Spoken words | 969 | 1,402 (excluding marker lines) |
| Without wind-up, anecdote and outro | about 800 | — |
| Without CTAs | — | 1,277 |
| Runtime | 6:05 actual (the presenter runs about 160 wpm); about 6:28 at 150 wpm | **About 9:21** at the persona's 150 wpm; about 8:31 without CTAs |

The script is 45% longer overall and about 60% longer in content words. Most of the extra is real coverage the source lacks: the instant overflow check, the dye test, chain and seat specifics, flapper sizes and buying advice, prices and lifespan, three safety notes and the fourth cause. About 150-180 words is padding or repetition:
- L18 (11 words)
- L25 (22)
- L39 (13)
- the duplicate diagnosis at L67/L70 (about 35)
- L32 could be folded into L29 (about 10)
- the parts tour at L10-15 could lose about 50
- the CTAs are 125 words; the persona allows "two or three lines" for the mid-CTA, and it uses three plus the return

Cut those and it lands near 1,230 words (about 8:10). That's longer than the source for a good reason.

---

## 5. Would this be safe to upload unread?

**No, not as is. It's a FIX-THEN-PASS, not a Hold.**

Nothing in it is fabricated, dangerous or embarrassing. Every number is real and attributed, there are no hard bans, and the offer is clean.

But the system awarded PASS with real findings open:
- a false statement about a named company (L39)
- a safety line deleted to satisfy a scanner flag, and a fill-valve replacement with no shut-off and no steps, so the "how to fix it" promise is under-delivered for one of the three causes
- step content lifted from a voice sample
- an echo
- a voice that misses the persona's "short sentences" by a wide margin

"Uploaded unread" is only safe if the audit's PASS can be trusted, and here the evidence block's `Rules (F): clean` is wrong in four places. The bigger concern is that most of these slipped through because the rubric doesn't ask the question (A2, E3, E4, F8 and the persona voice have no evidence line), or because the tool says "0" when it hasn't really checked (the number check).

---

## 6. Fixes, ranked

### LIBRARY problems (these matter most)

| # | Severity | File and rule | Problem | Suggested fix |
|---|---|---|---|---|
| 1 | **High** | `core/script-scanner.py`, `number_check` / `word_numbers`; audit D4 | (a) Infinite loop on hyphenated number words ("two-inch", "Ten-Minute", "one-page"): the inner loop `break`s without advancing `i`, so a full run hangs. The writer and the judge both had to edit a copy. (b) Context-free matching: any numeral anywhere in the pack passes. Against this pack, invented "$6.90", "$200 for a visit" (a number the pack says *not* to use), "20 years" and "9,000 gallons" all pass. (c) A ±0.5 absolute floor lets prices drift *up*, against D4. (d) Values ≤3 are never checked. (e) Offer numbers are checked against the research pack, not the persona profile. "Numbers not in pack 0" currently proves very little on a Hold-level check. | Fix the loop. Match a number together with its unit or nearby noun. Read a "do not use" / GAPS list from the pack. Use one-directional tolerance (prices exact or down, costs and time up). Take the persona profile as a second number source for CTA lines. Add a regression test to `tests/run_checks.py`. |
| 2 | **High** | `core/greenlight-audit.md` F8; `core/workflow.md` 3; `core/humanizer.md` H18 | With no niche pack, F8 ("the niche's safety lines") points at nothing, so the research pack's SAFETY POINTS have no force. S5 was deleted in draft 4 to clear the scanner's "turn off the supply" x3 echo. S4 was never used. S1 is missing at the fill-valve replacement. | F8: every research-pack safety point tied to a step the script teaches must appear at that step, and the evidence block lists S-lines used or skipped (with a reason). H18 and the scanner's echo: safety instructions are exempt and are rephrased, never deleted. |
| 3 | **High** | `core/greenlight-audit.md` E1 #2, #6 and E3; `core/variety-rotation.md` log format; brief spec | The writer can't run E3 or E1 #6. It never sees the reference video (by design in the test, and nothing passes it in real use). The rotation log has no structure field. The title here is the competitor's title verbatim. The writer guessed #6 from a log title and claimed #2 without data. | Have the brief carry the reference video's title, angle and structure outline (never its transcript). Add `structure: [type]` to the rotation log line. Add an `E3:` line to the evidence block naming the reference and how angle, voice and sourcing differ. Decide whether a verbatim competitor title is allowed (an ideation rule). |
| 4 | **High** | `core/script-structures.md` (picking table, "Why it happens") against `core/retention-mechanics.md` 3 and 5 and audit B2/B4; brief "Format" field | (a) "Why it happens" puts Layer 1 background straight after the hook, while retention 3 and the shared rules say the line after the hook "never sets up background". (b) The picking table has no rule for compound titles ("Why … and How to Fix it"). (c) There's no precedence between the brief's Format field and the fallback structure. Result: about 2:25 before the first action, and the diagnosis said three times (H18). | Add a compound-title row (for example "Why + How to fix": per cause, cause, how to tell, fix, with a one-line Layer 1 inside the first cause). State that the brief's Format wins over the fallback where they differ. Say Layer 1 counts as the "payoff" only if it's a sentence or two and delivers part of the promise. |
| 5 | Medium | `core/greenlight-audit.md` D1; `core/voice-anchoring.md`; persona template "How they talk" | The persona's "How they talk" isn't audited anywhere. The persona says "short sentences", but the script averages 18.2 words with 3 of 77 at 8 words or fewer (the source averages 11.0 words, 33 of 88). The no-pack voice samples are long run-ons, so samples and persona disagree, and nothing says which wins. | Add D1b: test against the persona's "How they talk" lines and quote one line. State that the persona profile wins over samples on sentence length and register. Optionally have the scanner report mean sentence length and the short-sentence share. |
| 6 | Medium | `core/research-and-sourcing.md` 9 (default pack: STEPS, title-claim check); `core/workflow.md` 3 | A "how to fix it" claim was supported by "5. … Replace the fill valve." with no steps. The script couldn't deliver a fix the viewer can do (C5). The writer filled the flapper-removal gap from a voice sample. | Title-claim check: every "how to fix" item maps to a complete step list (shut-off, drain, remove, install, test) or a blocking gap. Workflow: a step the script needs that the pack lacks means NOT READY or cut the claim. Say explicitly that it's never taken from samples. |
| 7 | Medium | `core/greenlight-audit.md` evidence block; A2 | There are no evidence lines for A2, E3, E4 or F8, so the writer silently skipped them. A2 can't be run with mid-video samples, and the no-pack `voice-samples` input never asks for an opening. | Add `Hook: A2 compared with [hooks] or "not run"`, `E3:`, `E4:` and `Safety:` lines. Have the `voice-samples` input include at least one winner's first 15-20 seconds. |
| 8 | Medium | `core/variety-rotation.md` slot 1 and guardrail 2; `core/retention-mechanics.md` 2 | (a) There's no rule for classifying a two-sentence hook. The writer logged the second sentence's move (a question) for a first sentence that's a problem scene. (b) "Problem at its worst" and "universal situation" overlap. (c) The thumbnail-match rule makes a scene opener the default every time, which collides with rotation. | "The opening move is the move of the first sentence." Sharpen the move definitions. Say how to name the thumbnail scene inside a different move (a question, a number, a contrarian line). |
| 9 | Low | `core/workflow.md` 1.3 against 2 | Does the TEST label go on "Start a new chat for the next script."? | Say yes or no explicitly. |
| 10 | Low | `core/workflow.md` 2 rotation-log check | "Fewer only if the channel has fewer scripts" can't be checked at the gate. | Accept fewer lines with a one-line confirmation request, or accept as stated. |
| 11 | Low | `core/research-and-sourcing.md` (GAPS honest wording) against audit D4 | The pack's "within about 15 minutes" rounds time down against its own Korky "at least 25 minutes" and NYC 15-20. | The honest wording the research stage writes must itself follow D4 (time rounds up). |
| 12 | Low | `core/cta-and-endings.md` 1 and 5 against the persona's fixed "End ask" | "One ask per moment" and "change … the close" every time both collide with a persona-fixed subscribe line in the end CTA. | Allow offer plus one ask in the end CTA. Exempt the persona's end-ask wording from rotation, or have the persona give the ask's intent rather than its words. |
| 13 | Low | `core/workflow.md` 6 | It's unclear whether tag density is a script average or local (three tags within six sentences, twice). | "About one per 80-120 words across the script, and no more than two in any 80 words." |
| 14 | Low | `core/research-and-sourcing.md` 6 | Does "a checked date on anything that changes" apply to spoken prices? The upload outlives the price. | State whether prices are said with a month and year ("listed at $6.48 as of October 2026") or left undated. |
| 15 | Low | `core/humanizer.md` tiers | H17, H18 and H19's vague half aren't placed in any tier (fix on sight, cluster, counted, judgment). | Place H18 under "counted" (at most twice) or "fix on sight". |
| 16 | Low | `core/persona-profile-template.md`, added-value promise; `core/offer-rules.md` 5 | The profile's "so you buy the right part the first time" reads like a result guarantee, and the template doesn't warn about that. | Add a template note: the promise names what the viewer gets, never an outcome. |
| 17 | Low | `core/research-and-sourcing.md` 6 against voice | There's no guidance on attribution density: 24 source-name mentions (Fluidmaster 9, Korky 6, WaterSense 4, Home Depot 3, EPA 1, NYC 1) in 77 sentences reads like a citation list, and the samples never cite. | "Attribute numbers, rules and claims once per source per section; steps need no attribution." |

### WRITER slips (the rule was clear)

| # | Severity | Rule | Line | Fix |
|---|---|---|---|---|
| W1 | Medium | claims-policy (named companies), audit F5/F6 | L39 "…and Korky's guide agrees." Korky never said "doesn't need to be exact" | Cut L39, or attribute the exactness to Fluidmaster only |
| W2 | Medium | voice-anchoring ("Voice, never content"); research 1; the samples file header | L85 "flush the tank empty … unclip the chain from the handle" comes from Sample 2 | Use only pack steps, or stop with NOT READY |
| W3 | Medium | F8 (pack S1, S5) | S5 deleted in draft 4 to clear an echo flag; no supply shut-off at L58-64 | Restore S5 (rephrased); add the shut-off before the fill-valve replacement; consider S4 |
| W4 | Medium | H18 | L17 / L67 / L70: the same diagnosis three times | Keep L17 and L70 (L70 adds the doubter answer); cut L67's restatement |
| W5 | Medium | audit "Evidence both ways", F9 accuracy | `Rules (F): clean` is false; Originality #2 is unevidenced; opening move mislabelled; adversary voice mislabelled | Report what was actually checked; log the first sentence's move |
| W6 | Low | workflow 4 (stats are digits) | L24 "three to five gallons a minute" | "3 to 5 gallons a minute" |
| W7 | Low | C2 | L85 "ears" unexplained | "the two little hooks it hangs on" |
| W8 | Low | B3, B9, F2 | L18, L25, L39 padding | Cut |
| W9 | Low | A4 | L7 promises only the screw or the $6.48 flapper | Name "a part that costs a few dollars" or include the fill valve |
| W10 | Low | A1 / brief (both kinds of "keeps running") | The hook pictures only the never-stops case | One clause for the refill-every-few-minutes toilet in the hook |
