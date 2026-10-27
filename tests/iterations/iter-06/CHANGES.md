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
