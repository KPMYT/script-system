# TEST: iter-07, what the three runs found (2026-10-29)

All three judges: **fix, then pass** ("I would upload it after one short fix round"). Totals out of 140, the hook double-weighted (references without an audit block scaled from 130):

| Run | New | Our old script | The winner | Hook (model, words, item one) |
|---|---:|---:|---:|---|
| 01 Scarlett, necklaces | 117 | 68 (`w6w_ktMBHXM`, our best video) | 73 (F01) | M29, 65 words (model 72), about 23 s; 8/10 |
| 02 Scarlett, bob | 121 | 68 (`h9MsF44shdQ`) | 75 (M12) | M08, 104 words (model 175), about 37 s; 8/10 |
| 03 Diane, frumpy | 116 | 65 (`ISAL4NBlshQ`) | 100 (M21) | M28, 75 words (model 78), about 26 s; 7/10 |

Counts per 1,000 words (new against our old scripts): "but" 5.5-5.8 (ours 0.5-1.1); "you" and "your" 43-50 (ours 32-45); questions 2.7-3.7 (ours 0-1.0); "I" 4.2-6.2. No intro, tease, price, house vocabulary, subscribe ask or sign-off in any run; the gate refused "just write it", the vague channel names and the missing rotation log.

## Library fixes the judges name (proposed; nothing applied until the operator's yes)

| # | Fix | Runs | Where |
|---|---|---|---|
| L1 | An `allow:` line for each book's spoken title in both profiles (the copy guard flags the 8-word title the CTA must say), and the numbers check accepts numbers in the profile's `book:` line | 01, 02 | profiles; core scanner |
| L2 | `verify_output.py` skips a quote the evidence attributes to a model ("graded against M04 ...") | 01, 02 | tool |
| L3 | The channel gate: a reply that names exactly one channel ("Scarlett", "the French channel") is confirmed in one line instead of the list again; anything else gets the list with one line saying why | 01, 02, 03 | core `workflow.md` §1 (every channel) |
| L4 | Title words: add "age" and "weight" to `title-words`; say how a title's "NEVER" about French women is paid (by its hedged meaning) and how "It's Not Their Weight" is paid without the banned formula (a plain permission line: "none of these rules asks you to lose weight") | 01, 03 | pack |
| L5 | The item length band depends on the count: about 180-300 words in lists of six or more, about 300-450 in lists of five or fewer (five items can't reach 12 minutes inside 150-350); the report band widens to 150-480 | 03 (also 02) | pack |
| L6 | The hook aims at her: when the hook model names no feeling (M28), her feeling goes into its contrast or cause move, in the second person; the audit's Hook line gives the pain in her words | 03 (also 01) | pack, `hooks.md` |
| L7 | "you about 45 per 1,000" means "you" and "your" together | 01, 02 | pack |
| L8 | Scarlett's profile names no voice provider, so the writer guessed the VO copy's format | 01, 02 | profile (operator) |
| L9 | The item shape: the check needs no announcement ("Here's the check"), and item endings rotate (not check, result, bridge every time) | 01, 03 | pack |
| L10 | Diane's lens: "most" only for the broad French habits; a specific garment or shoe takes "plenty of" or "many"; a ban on "women I know in Paris" (the brief spec suggests it) | 03 | profile |
| L11 | A spoken pronunciation guide ("said ver-may") never goes in the script; a hint, if needed, goes in the VO copy only | 01 | pack |
| L12 | Whole-look titles may keep one short face paragraph from the brief (no products, no results); makeup-led titles wait for the makeup pack | 03 | pack |
| L13 | The scanner's item word counts leave out the CTA blocks and the ending (they overstated the long-item flags) | 02 | core scanner (report only) |

Outside this library (the operator's ideation skill, "we dont need ideation yet"): the brief spec suggests "most women I know in Paris" and French phrases, and asks for dollar figures that the style pack treats as background.

## Writer slips (the rule was there)

- Run 02: the tuck line is backwards ("the side opposite your part, the one with less hair"); the heat-safety line said three times; item one runs long before the CTA.
- Run 01: "Put the wrong necklace with it." names no concrete look; "older" lands on the outfit, not on her; the title's feeling comes back only about 6 times per 1,000 words; a pronunciation guide in the script.
- Run 03: the hook talks about French women, not to her; "weight" said once; three French claims past the brief ("In France, most women wear ballet flats..."); "comfortable in her age" lost with the French phrase.
