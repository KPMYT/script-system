# TEST (iter-19) writer notes: The Vintage Pipefitter, "8 Things You Should NEVER Pour Down Your Drains"

## Files read
`plumbing-scripts/SKILL.md`, `personas/vintage-pipefitter.md`, `tests/iterations/iter-19/brief-vintage.txt`, `plumbing-scripts/references/models/R16-silver-cymbal-string-trimmer-hacks.md`, `plumbing-scripts/references/price-guide.md`, `core/workflow.md` section 6 only.

## Model
R16 (Silver Cymbal, string trimmer hacks). The pack's table maps "Never-do list" ("N Things You Should NEVER...") to R16 alone, and the title is that shape exactly. Taken for flow only: each item opens on a moment the viewer has lived, then the cause, the fix, the result; the cheap swap; the safety line inside its own item; short spoken links between items. None of its words, phrases, facts or its subscribe/linked-video lines.

## Check runs
1. FAIL (4):
   - length 2,629 words (13.8 min). The opening was also 166 words (about 52 s), so trimming it made the gap bigger. Added only brief/page content that was missing: the want/fear named in the opening ("a bill ... for something they did without knowing"), a scene line opening item 7 (wipes on the back of the toilet), the main-line "check your other drains first when nothing goes down" (page rule 4), and the snake's payoff against the trade's price in words (item 2).
   - ending: the comment ask and "I read every one." were in separate paragraphs; merged into one last paragraph.
   - safety: item 1 said "a plunger won't touch it, and a snake only pokes a hole" before item 2's chemical check. Reworded to "the usual tricks only poke a hole through the middle of it".
   - safety: "Stop running water right then, and call." was not read as a named call; now "call a licensed plumber". Also removed a "tub gurgles" trigger I had added that was not in the brief or the page.
   - Opening trimmed from 166 to 154 words.
2. PASS (2,665 words). Then by-eye fixes against the page's check list and rule 7 (no invented claim): "a pipe as wide as your thumb" (wrong for a kitchen drain) and "over a few years" (brief says months) fixed; "the one time I'd have somebody come out" (item 2) clashed with item 7's "the one place", softened; strainer "a couple of dollars" (brief says no figure) and "usually free to drop off" (invented) removed; rice swelling "by the next morning" and peels "wrap around the inside" (invented detail) removed; washing soda "helps cut the film the other seven leave behind" (invented claim) replaced. Added the brief's fourth habit item, the lidded trash can, as its own sentence (the list of three rule).
3. FAIL (1): length 2,659, one word short. Added the warning sign to item 3 (the brief asks every point for its sign; item 3 had none).
4. PASS (2,682). Read-aloud fixes: "never costs you a dime more than the bacon" (awkward), and "check for that first" (unclear "that") changed to "check your other drains first".
5. PASS, final: 2,678 words, about 14.1 minutes. Last line: `RESULT: PASS`.

## Unclear or contradictory
- **Length vs opening timing.** The script sits just over the 2,660 floor. The opening is 154 words (about 49 s, against "the first real tip by about 45 seconds"). Trimming it further would drop below 14 minutes; the brief had nothing left that wasn't already built out, so I left it.
- **Calls.** The page allows a call only for gas, live wiring or the main line, but the brief's stop signs add "a jug of chemical cleaner in a drain that won't clear" and item 2 says "if a plumber comes, tell them what's in there". The brief wins on facts, so item 2 keeps one conditional line ("that's a time to have somebody come out ... tell them exactly what you poured"). The check did not flag it; a judge might.
- **The check's count detector** reports "one ordinary habit" as the opening's count; the real count line is "There are eight things that should never go down your drains". INFO only.
- **The check's dollar counter** reports 0 dollar figures in the opening although the opening says "about 150 to 400 dollars": it seems to count only figures written with a dollar sign. The page says prices may be digits or words, and "no symbols", so I wrote "dollars". INFO only.
- **Price per item.** The price guide says "at most one price per item"; the brief gives item 2 three (pipe replacement, snake, enzyme). I said the replacement in words ("several hundred dollars to a couple of thousand") and kept the snake and enzyme figures as the brief gives them. Item 2 still carries two figures.
- **Paint bucket.** The brief says let the bucket settle overnight, then dry the sludge, but not what to do with the clear water on top. Left unsaid rather than invent where it goes.
- **SCRIPT TYPE line.** The step 5 template reads "Classic (Roger, Mark, the Vintage Pipefitter) | Talking Head (Werner)"; I output "SCRIPT TYPE: Classic".
- **VO copy word check.** `core/workflow.md` section 6 checks the VO copy against the script; verified by script: stripping the 27 tags gives the script word for word (about one tag per 99 words, none adjacent).
