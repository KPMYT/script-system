# iter-01 review: Hank Hardwood, first script (the lazy Susan)

Reviewed 2026-10-20 in Claude Code with the operator. Inputs in `test-run/`. The scanner was run on a scratch copy patched for the fraction-word hang; result: zero fix-on-sight, zero numbers missing from the pack, 1,815 spoken words. The writer's verdict was PASS; the review's verdict is FIX-THEN-PASS.

Each finding: the quoted line, the rule, and the operator's decision. "Applied" means a library change in `CHANGES.md`.

## Round 1: rules and scanner

| # | Finding | Operator's decision |
|---|---|---|
| 1 | CTAs run 66 and 67 words ("Getting lettering on wood that looks clean and straight is on pages 161 to 163 of my e-book, ..., and each of the hundred builds in there lists its lumber, its cost and its going price right next to it.") | Hank's longer CTAs are fine. New: Hank's CTAs always say "QR code or top link in the description". Dale stays as he is. Applied. |
| 2 | "So do the damn math." aims the swear at the viewer. | Agreed, critical. Example added to the pack. Applied. |
| 3 | Food contact ("somebody's setting a cheese plate on this thing") but the factory glue in the edge-glued round was never checked. | Agreed. Research pack template and pack safety line. Applied. |
| 4 | "a drill with a three-quarter inch spade bit": no alternative or "optional". | Fine as it is. |
| 5 | Stores named for only two priced items. | Writer miss; no rule change. |
| 6 | Lines close to the rule files' examples ("Somebody's already typing that nobody pays $90 for pine"; "Which brings me to..."). | Watch across the next scripts (rule changes need a pattern on three videos). |
| 7 | Scanner loops forever on "three-quarter", "five-eighths", "one-by-eight". | Fix it, plus a check so it can't return. Applied. |
| 8 | The writer rejected "the Laziest Thing I Sell" under the claims policy; the operator's title decision hadn't reached the script-side files. | Titles may claim selling and tenure on Hank too. Applied (core, pack, ideation). |
| 9 | With no pack, the script chat built and verified its own pack. | Make it official (9a). Applied. |
| 10 | Assembly after the oil broke the pack's literal part order, rightly. | Allow it. Applied. |
| 11 | "There's a shop on Etsy called cbSignWorks..." | Never name shops. Applied. |
| 12 | "my e-book" | Never "e-book", always "book", every channel. Applied (offer rules, both profiles, scanner bans, check 15). |

## Round 2: the writing, against the competitors and Hank's old videos

Measured the same way across the 20 competitor transcripts, Hank's 15 and Dale's 10 in `studies/woodworking/`, and this script:

| | Winners (BV + WTV) | Hank's old videos | This script |
|---|---|---|---|
| Spoken words | ~1,900 typical | ~3,000 | 1,815 |
| Time to first material | 5-33 s | ~1:35 (no-cut video) | ~10 s |
| Share on the build | ~44% | 21-25% | ~43% |
| Intro, teases | none | intro + about 4 teases | none |
| "I/me/my" per 1,000 words | 31-40 | ~10 | ~9 |
| Numbers per minute | 7-11 | ~9 | ~13 |
| Money mentions per minute | ~1 | ~1.4 | ~4 |
| Questions per 1,000 words | 1.3-2.5 | 1.6 | 0.6 |

Strengths: straight to the first material, no intro or teases, no fake claims (the old "The last shelf I sold went for $180" is gone), build share at the winners' level, honest candor ("Pine fights you a little here, and I won't pretend it doesn't"), short honest bridges ("Now the access hole, the one fussy part").

| # | Finding | Operator's decision |
|---|---|---|
| W1 | The hook is all numbers: "$21 in big box parts gets you a lazy Susan, and with a family name burned into the top, the personalized ones are listed online from $70 to past $100." No pain point or emotion; the operator's quality bar wasn't written in any script rule. | Critical, every channel; fix in core and niche, not just Hank. Applied. |
| W2 | Runtime counted at 150 words a minute (12.1 min); Hank's real pace is about 187 (about 9.7 min). | Set Hank 185, Dale 170. Applied. |
| W3 | Too many numbers, read like a price list: 86 words of pack math for a $1.53 base; five figures in one cost sentence; "is listed at" four times; the Etsy fee schedule read out. Money block about 510 words against 150-250 for the winners. | Agreed heavily: easy to follow. Applied (core H22, workflow, audit C2, pack, unit plan). |
| W4 | Personality thinner than both winners and old Hank; shop detail inside the trickiest step; no opinions at choice points. | Allow personality, an extra sentence here or there; don't beat it out. Applied (core progression test, audit B3, pack step rule, detail placement, unit plan opinion moments). |
| W5 | Small slips: "Tools are short.", "number six, five-eighths inch flat head wood screws", "Now" opening three paragraphs. | Agreed. Pack line on specs said the way people ask at the store. Applied. |

## Not checked
- The VO copy wasn't compared word for word with the script (tag count, types and placement were checked: 16 tags, all allowed).

## Still open
- The scanner prints the runtime at a fixed 150 words a minute; profiles now set their own. Changing that needs `core/script-scanner.py` (ask the operator first).
- Finding 6 (example-line echoes): watch over the next scripts.
