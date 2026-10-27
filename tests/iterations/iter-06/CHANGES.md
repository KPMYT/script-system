# TEST: iter-06, what the judges found and what was changed

Both runs: **fix, then pass** (judge reports in `test-run-01/` and `test-run-02/`). Both scripts are safe and clean on the scanner: 0 bans, 0 copied runs, 0 numbers outside the brief and price guide, 17.8 and 20.2 minutes. Every price traces; the gas-leak and carbon monoxide steps match price guide §9 (run 01 shortened one CO step). Both beat their reference videos on the opening, number load, safety, and the CTA and ending. **Neither is yet at the operator's "make the viewer feel it" bar.**

## The main session's check of the judge reports (2026-10-27)

Confirmed against the scripts:
- Run 02's opening runs 187 words (about 1:15) before the first section; run 01's runs 114 (about 46 s), so item one lands after the pack's 30 s.
- Run 02: "Furnaces usually have a small door switch that keeps everything off while the door's open" is in neither the brief nor the guide, and the viewer removes the burner door, not the blower door the switch usually sits on. The trap's call trigger is "unless you've cleaned one before", not a named sign. "Never ... bypass" names only the limit switch, though the pack's rule names the pressure switch too. The replacement step doesn't repeat the shut-down.
- Run 01: "Those first four are all about air" is false after the writer's reorder (item two is the furnace switch). "The next three are parts somebody gets paid to replace" leans toward a motive.
- The same counts measured on the plumbing script the operator passed (iter-04 run 03) and on these two:

| Script | "you" per 1,000 | "you"/"your" family | "but" per 1,000 | questions per 1,000 |
|---|---|---|---|---|
| Plumbing run 03 (passed) | 26.4 | 39.2 | 6.9 | 2.3 |
| HVAC run 01 | 21.1 | 30.0 | 3.6 | 2.6 |
| HVAC run 02 | 21.0 | 27.0 | 4.1 | 2.6 |

**Why the scripts were flat: a build slip in the pack, not the writer.** The HVAC pack's emotion section said it carried the plumbing rule "over whole", but its build left out the plumbing rule's "Did it / Didn't" example lines, the operator's own words on "but" and on the title's feeling, and the measured counts. The plumbing scripts rose from 20.7 to 39.2 "you" when those went in (iter-04 runs 02 to 03).

## Library changes (logged in `CHANGELOG.md`)

`hvac-scripts/SKILL.md`:
1. **Emotion:** the plumbing rule's examples and the operator's words put back, with HVAC lines where the study has them (rules 1, 4, 5, 8, 9 and 11), the measured gap, a target of about 7 "but" per 1,000, and a new line: a bridge that sums up the items so far must be true of the order the script has them.
2. **Money devices:** "the same part, two prices by the clock" now means two prices (the shelf against the night call); with the weekday visit added it's the three-prices device. The two read the same before, so the rotation couldn't tell them apart.
3. **Safety default 1:** the tester is tried on something known to be live first; the burners and metal are let cool; the shut-down is said again wherever a later step opens the furnace again.

`hvac-scripts/references/price-guide.md`: rows for the non-contact voltage tester, emery cloth and a scrub pad, from a researcher and a second checker (`studies/hvac/price-research-2026-10/E-research.md`, `E-verify.md`).

niche-research: brief #14's flame-sensor line corrected ($10-$30; "up to about $300 at night or on a weekend"); it had been missed in the first corrections pass.

## Writer slips (the rule was there)

The door-switch fact, the trap trigger, the pressure switch left out of "never bypass", the false "first four" bridge, the motive-leaning bridge, the long openings, the second "one more visit", the second first-of-the-month mention, and the audit blocks' wrong claims (run 01: the reframe count, "item shape on all eleven", "every carbon monoxide step"; run 02: "Rules (F): clean" and three "brief facts" that aren't in the brief).

## For the operator (core or cross-channel, not changed)

1. A brief price that disagrees with the price guide's row: should the input gate flag it? (Today the brief wins.)
2. The profiles say the subscribe line's opening words go in the rotation log, but the log line has no field for them (plumbing too).
3. Scanner: a reframe split across two sentences isn't caught; no limit on a repeated word like "figure" (4 times in run 02, as in plumbing run 03).
4. The channel menu shows "8. Roger the HVAC Guy" with no 7: row 7 (electrical) is on the electrical branch, so the gap closes when the branches merge.

---

# Round 2 (runs 03 and 04, skills rebuilt at aa5f0b8 with the fixes above)

Both runs: **fix, then pass**, each about six lines from upload (judge reports in `test-run-03/` and `test-run-04/`). The emotion fix worked:

| Script | "you"/"your" family per 1,000 | "but" per 1,000 | questions per 1,000 | minutes |
|---|---|---|---|---|
| Plumbing run 03 (passed) | 39.2 | 6.9 | 2.3 | 20.2 |
| HVAC run 01 → run 03 (#4) | 30.0 → 39.9 | 3.6 → 6.5 | 2.6 → 3.5 | 20.2 → 22.6 |
| HVAC run 02 → run 04 (#14) | 27.0 → 40.6 | 4.1 → 7.3 | 2.6 → 2.2 | 17.8 → 15.4 |

Fixed from round 1: the false and motive-leaning bridges (run 03), the title's feeling coming back ("mistake" nine times), scenes opening every item, the tester tried on a live outlet, the cool-down, "never bypass" covering the pressure switch, the night price, the door-switch fact. Scanner clean on both (0 fix-on-sight, 0 copied, 0 untraced numbers).

The main session's check of the judge reports, confirmed against the scripts: run 04's opening is 177 words and run 03's 99 before "Number one"; run 04's replacement line is one 55-word sentence; run 04's invoice line ("The invoice will say something like flame sensor service") is in neither the brief nor the guide; both list runs (01 and 03) wrote "If they find the furnace is the cause", dropping the guide's "or another appliance"; the pack's own villain example joins its two facts with "so", and run 03 copied that shape with "since".

## Library changes after round 2 (`hvac-scripts/SKILL.md`)

1. The opening's time limits in words: about 110 spoken words before the first real tip, and "Number one" within about 75 in a list (in "The opening" and the handover checklist). Both rounds overran the seconds.
2. A carbon monoxide or gas step may be said shorter, never narrower.
3. A part the brief leaves to a tech is never set up as the viewer's job ("keep a spare igniter").
4. Item closes vary: one frame on no more than about a third of the items (run 03 used one on nine of eleven).
5. "nine-one-one", never "911" (spoken forms, and a scanner ban).
6. Where a metal-armoured cable blocks the tester, a second, tool-free check (thermostat up, no hum or click, the board's light out).
7. The persona device: one detail, at most twice (the profile and the pack read differently before).

Writer slips left (the rules were there): the unsupported lines (the invoice line, "you can often spot it through the little window", "switch it off and back on ... it'll try again" with no limit, "Most of the furnace calls..."), the 55-word sentence, and the audit blocks still saying "Rules (F): clean" over a narrowed safety step.

## For the operator (not changed)

5. The villain rule's example line ("The trade is paid by the visit and the install, so a cheap check that ends the visits is nobody's business to mention") joins the two facts with "so", and the writer copied that shape with "since", one step from a motive. Reword it so the two facts stand as separate sentences? It's the plumbing pack's line too.
6. Scanner (core, every channel): list sentences over about 35 words; catch an "it's not X, it's Y" split across two sentences; check the seven carbon monoxide steps are all there.

## Status

Roger the HVAC Guy is marked **ready** (as Sawdust Sam was on 2026-10-24: the profile and pack are complete, so the operator's own test scripts can run, and those tests decide any further changes). Round 2's remaining faults are writer slips of the kind every niche's tests have shown, and every library gap the judges named is fixed above.
