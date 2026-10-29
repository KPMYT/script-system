# TEST: iter-08, what the second style round found (2026-10-29)

All three judges: **fix, then pass** ("I would upload it after one short fix round"). Totals out of 140, the hook double-weighted (references scaled from 130 where they have no audit block):

| Run | New | Our old script | The winner | Hook (model, words, item one) |
|---|---:|---:|---:|---|
| 01 Scarlett, jeans (new title) | 118 | 60 (`yl-Vq9WyLzY`, 12,620 views) | 88 (M26) | M19, 109 words (model 235), about 39 s; 8/10 |
| 02 Diane, French haircuts (new title) | 117 | 64 (`egJ5B6d879c`, 2,911 views) | 85 (M07) | M07, 82 words, about 29 s; 8/10 |
| 03 Diane, frumpy (rerun of iter-07 run 03) | 124 (iter-07: 116) | 65 (`ISAL4NBlshQ`) | 100 (M21) | M28, 78 words (model 78), about 28 s; 8/10 |

Counts per 1,000 words (the judges' counts): "but" 5.0-5.8; "you" and "your" 30 (run 01), 34 (run 02), 42 (run 03), against the pack's "about 45"; questions 2.7 (six a script); "I" 4.4-6.4, every one an opinion or an approved detail. All three: 0 fix-on-sight on the main session's scanner; 12.7 to 13.3 minutes; no intro, tease, price, house vocabulary, subscribe ask or sign-off; the comment ask about her, last.

**The iter-07 fixes, checked:** the channel gate confirmed "Scarlett", "the French channel" and "START the french lady" in one line each; the gate asked for the missing title alone (run 01) and refused "just write it, skip the log" (run 02); the rotation held (no model, hook model or comment question from the pasted logs); Diane's hedges ("plenty of", "many", "you'll often see"; "women I know in Paris" left out though the brief asked for it); the book's spoken title in every CTA; item lengths inside the new bands; no spoken pronunciation guide; "weight" paid as plain permission. **Half working:** item endings still lean on result-then-bridge (runs 02, 03); "you" and "your" short of 45 in runs 01 and 02.

## Library fixes the judges name

**Applied 2026-10-29** on the operator's answer ("the french angle doesnt have to be the entire list, its quite dependant on title and brief / the rest are good"): M1-M6, M8, M9 and T1; **M7 in a softer form**: how far the French angle runs depends on the title and the brief, never forced into every item. Both channels set **ready** the same day (S7 left to Claude, S8 yes).

| # | Fix | Runs | Where |
|---|---|---|---|
| M1 | **Signposts the scanner can't read.** Run 01 opened its units on plain words ("The first pair is the everyday jean"), which the pack allows, so the scanner's item lengths and item-one timing silently didn't run. The scanner reads ordinal signposts too ("the first / second … pair, part, cut, rule") and prints "NOT CHECKED" when it finds none. | 01 | core scanner |
| M2 | **A type for "the mistake, then N pairs"** ("The X Mistake … and the 3 Pairs That …"): the mistake as one or two units, then each swap a full item of 300-450 words, signposted "Pair one."; the mistake done by about a third of the way in, the CTA after it. | 01 | pack |
| M3 | **The title's feeling fades in the body.** "Frumpy" said twice in the hook, then not again for eleven minutes (run 03); "older" and "ten years" gone for five minutes (run 01); "any face shape" said once (run 02). The scanner reports each title word's longest gap and its rate per 1,000 (a report, never a fail: "dont overdo it"); the pack asks for the feeling word at least once in the body's second half; the title's capitalized words (ANY, NEVER, OLDER) count as title words. | 01, 02, 03 | core scanner, pack |
| M4 | **"You" and "your" printed by the scanner** next to SENTENCES and in the audit's Voice line, so a script under about 35 per 1,000 gets a look before hand-off. | 01, 02 | core scanner, audit |
| M5 | **The book pitch repeats across videos.** Scarlett's CTA reused the necklace script's benefit ("every Way gives you the swap and the payoff"); Diane's two frumpy runs said the same benefit in near-identical words. The book's fact and benefit rotate (never the last script's), and each profile lists three or four benefit angles from its book index. | 01, 03 | core rotation, profiles |
| M6 | **The pack's own example line copied.** "None of these five rules asks you to lose weight" is the pack's example (Emotion rule 8) almost word for word; the example guard skips lowercase quotes. Write the example as a shape, and let the guard read lowercase quoted clauses. | 03 | pack, core scanner |
| M7 | **Diane's French angle through the list.** On a French-titled list, most items carry one hedged French reason in English (air-dried hair, gray worn on purpose, the low chignon); run 02's French angle stopped after cut one. | 02 | Diane's profile |
| M8 | **The hook's feeling when the model names none** (not the declined iter-07 L6, which added a move): one line in "The opening" step 5, "where the hook model names no fear, the title's own words carry the feeling; no move is added", so the two rules stop pulling against each other on M28 titles. | 03 | pack |
| M9 | Small ones: a count of a list the brief gives ("the four parts") is allowed in the Numbers line (01); Diane's "one hundred and one" stops being flagged (a `book-facts` count, 03); `hooks.md` lists M07's closing scope move as usable (02); the audit's Originality line names what each model lent as well as what differs (02). | 01, 02, 03 | pack, profile, `hooks.md`, audit |
| T1 | Tool (Claude's own): `verify_output.py` skips a quote that is part of the locked title ("NEVER Look Frumpy" in the Promise map). | 03 | tool |

Outside this library (the operator's ideation skill, "we dont need ideation yet"): the brief spec still asks for "most women I know in Paris" (brief-02), which Diane's profile bans; the writer handled it.

Not a fix: run 02's judge noted that the library marks Diane "pending", which stops a live run at NOT READY. That is by design: test runs use a build with both channels set to ready, and the channels go ready on the operator's word.

## Writer slips (the rule was there)

- Run 01: the hook's first two sentences don't join ("…they stop wearing them. What's really aging them is one mistake…"); the brief's "each part adds years" never said; two checks announced ("You can check your own pair in a minute."); pair two's signpost buried in an if-clause; three falls lines across two pairs.
- Run 02: "ANY Face Shape" under-paid (cut four tells long and square faces to pick another cut; "If any cut on this list is going to take ten years off, my bet is this one" doubts the other four); endings all result then bridge; the audit claims it avoids F05's forward lines, which it uses; a 34-word patch-test sentence; "chin-length" asked for after telling round faces to go past the chin.
- Run 03: the hook's cause names "fabric", which no rule teaches (iter-07's script had a fabric check); the same "it feels safe" empathy beat in rules one and three; M21's "fitted does not mean tight" echoed for the second run running ("Fit doesn't mean tight"); "The French habit is one statement at a time." unhedged; three of six questions "So what…".
