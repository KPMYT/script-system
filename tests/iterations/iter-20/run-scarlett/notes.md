TEST (iter-20): writer notes, Scarlett Starling

## Title, type and models
- Title: 10 Things Elegant Women Over 50 Are NOT Wearing This Winter
- Video type: **Never these, wear these instead** (a list of pieces, each "never" paid by a "wear this"; the title's "NOT wearing" is the never-list). Close second: "Mistakes that age you" (fashion, M18), not used.
- Model (flow only): `style-scripts/references/models/M13-adore-your-wardrobe.md` (the table's only Scarlett model for this type). Taken: the "never" said once with its reason, then the "wear this"; spoken signposts; chatty, direct moves between items. Not taken: her words, plugs, body jokes, persona intro, likes/subscribe ask.
- Hook beats: `H01-paris-never-ages-hooks.md` (beats only; none of its signature phrases used).
- Book facts: `personas/books/scarlett-starling-book.md` (Way 5, "Judge a Jacket's Length by Your Seat, Not the Mirror Alone", chapter "The Foundation: How to Find and Buy the Right Fit"; 300 numbered Ways; over a thousand pages; each Way gives the swap and the payoff). Book block placed at the end of item 3, as the brief's match says.

## Check runs
1. Run 1: `FAIL voice: a symbol, bracket or label '(' on line 1: "TEST (iter-20)"`. INFO: hook 204 words (aim 100 to 160); a softener "may" in the hook (it was the month, "than you did in May"); 2,542 words.
   - Changed: cut the hook and removed "May". Kept the TEST label (required by the task).
2. Run 2: same single FAIL (the label). Hook 184 words.
   - Changed: trimmed the hook again to about 157 words; the reason to stay became "and get wrong most often".
   - Same text without the two label lines (scratch copy): RESULT: PASS.
3. Run 3: same single FAIL (the label). Hook 160 words (157 without the label). 2,500 words.
   - By-eye fix from the page's check list (no template): six tips opened their answer with "So ..."; reworded five (items 3, 4, 7, 9 and 10 now open their answers differently; item 6 keeps "So"). "many a mother's jewelry box" in place of "your mother's", to keep clear of the relatives rule.
4. Final: on `script.txt` as saved, `RESULT: FAIL (1)`, the only FAIL being the TEST label line. On the same script without the label: `RESULT: PASS`, 2,497 words, about 14.8 minutes at 169 a minute. `output.md` carries `CHECK: RESULT: PASS` (the script it contains has no label).

## By-eye checks (page list)
- Hook: six beats in order, names no tip and no topic, item one at about 157 words. No softeners.
- Want and fear: polished, put together, elegant / dated, bulky, invisible, all back in the body; the title's feeling returns in the second half ("Elegant in winter was never about owning more"); "NOT" said where true (item 9).
- No answer in the hook, a signpost or a bridge; bridges hand on a feeling or problem.
- Turns: every tip turns at least once ("but", "yet", "except"); 11 "but", 5 questions.
- Openers vary (piece, question, a single line, mirror, "isn't a piece of clothing", a belief, a phone moment, hands, a question, a test); endings vary (shop window, steady, compliment, permission, rested, compliment, verdict, tonight, permission, heads turn).
- "When I was designing" once (item 8, the runway hands, where it explains the point). "Ladies" once, in the sign-off.
- Safety lines: lugged sole and low block heel, boots pulled on sitting down; scarf ends clear of car doors and escalators; lash extensions removed at the salon, never pulled off.
- Ending: item 10, the book reminder (seat check, Way five), comment question about her own life (oldest coat), then the sign-off after `===END CTA===`.

## Unclear or contradictory
1. **The TEST label fails the check.** The task requires the first line `TEST (iter-20)`; `check.py` reads it as script text and fails the parentheses (voice rule), and also counts it into the hook and the first sentence. With the label the result can never be PASS. Either the check should skip a leading TEST label, or the label should drop the brackets (e.g. `TEST iter-20`).
2. **The pack says "None of the other core files are read"** but its output step points to `core/workflow.md` section 4 (marker layout) and section 6 (VO copy). I read only those two sections.
3. **"my book"?** The page never says Scarlett wrote the book, and the book's narrator has a separate history, so the CTA says "one of the Ways in Three Hundred Budget-Friendly Ways to Look Expensive", never "my book".
4. **Persona "never a date"** vs the brief's "1960s London" for the Chelsea name: said as "from London in the sixties" (no digits), taking it as a brief fact, not Scarlett's own date.
5. **Item 7 in the brief** gives two answers (swap the accessories for cognac shoe, belt and bag; and "change one accessory, just one"). Both kept, the second as the simpler option.
6. **Word count:** the check counts 2,497; a plain whitespace split gives 2,503. Used the check's figure.
7. The pack says "Not makeup or skincare"; item 5 is makeup, allowed by the brief's note (operator, 2026-11-17). Kept the product as the problem, never her skin or face.
