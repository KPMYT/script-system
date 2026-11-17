TEST (iter-20): writer notes, Diane de Chambray, "Why French Women Get More Beautiful With Age"

## What I read
- `style-scripts/SKILL.md`, `personas/diane-de-chambray.md` (2026-11-17 version), `personas/books/diane-de-chambray-book.md` (Secret 22, Proportion Equation, first-week list), `style-scripts/references/models/M28-aliceinparis.md`, `style-scripts/references/models/H01-paris-never-ages-hooks.md`, and `core/workflow.md` sections 4 (Talking Head markers) and 6 (VO copy), because the pack's output step points to them.

## Video type and model
- Type: **The rules she never breaks** (the French rules: each one a habit and a swap). The brief's seven French habits, each with its own swap, fit it better than "The why explainer" (one hidden cause, then fixes), even though the title starts with "Why".
- Model: `M28-aliceinparis.md` (the first listed for Diane), for flow only: straight into item one, each item a practice, the French reason, then what to do instead. I did not read M21.
- Hook beats: `H01-paris-never-ages-hooks.md`, beats only.

## Check runs
1. FAIL (8):
   - three "old house lines": "Color is what people see from across the room."; "It makes anyone shuffle, and a shuffle reads as age long before a line on a face does."; "But an easy, even stride is what reads as elegant, and a good flat gives you that stride." The second and third were close to the brief's own wording. Rewrote all three in fresh words.
   - voice: the '(' in line 1, "TEST (iter-20)" (the label the test asks for).
   - long sentence (47 words): the check read the "You look so put together." quote as running on. Split it.
   - hook list (three FAILs): the first sentence with its commas (merged with the TEST line), the "seven of them, most of them free, and every one..." sentence, and "the shape, the color and the fit, not to her". Rewrote the hook into shorter sentences, and cut the blame line to "the shape and the fit. Never with her."
   - INFO: hook 207 words (over 160).
2. FAIL (3): the TEST label; a 38-word sentence (the quote ending with ." still ran into the CTA's first sentence, so I made it reported speech); the hook's first sentence still counted as a list. I then ran the same check on a scratch copy without the label line to see what was really failing.
3. Copy without the label: FAIL (1), the hook's first sentence. Split it: "Plenty of French women grow more beautiful with age." then the cost in its own sentence. I also trimmed the hook (184 to 165 words).
4. Copy without the label: **RESULT: PASS**. The labelled file: **FAIL (1)**, only `voice: a symbol, bracket or label '(' on line 1: "TEST (iter-20)"`.
5. By-eye fixes from the page's P23 list, then a re-check (PASS without the label, the same single label FAIL with it):
   - "Plenty of Parisian women over sixty" opened a point in three tips (1, 3, 6), so I rewrote it in 3 and 6.
   - "Walk through Paris" came in the hook and in item 2, so the hook's now says "In Paris you'll often see her".
   - A bare "Number N." opened four tips, so I varied the signposts.
   - "never bought" about French women became "not bought".

Final: 2,237 words (script body; 2,240 with the label line), about 13 minutes. Mid book block 90 words at 59%. "But" 7 times, 6 questions. Hook 165 words (the check's INFO says about 100 to 160; item one starts inside a minute at 172 a minute).

## Unclear or contradictory
- **The TEST label fails the check.** The task asks for `TEST (iter-20)` as the first line of script.txt, and check.py fails its '(' as a voice symbol. It also merges the label into the hook's first sentence (the hook-list and first-sentence INFO lines). The labelled file can't reach RESULT: PASS without dropping or changing the label. I kept the label as asked. The script itself, run without the label, passes, and that is the CHECK line in output.md (output.md carries no label, as the VA would get it). The harness should strip the label before checking, or the check should skip a `TEST` first line.
- **"Old house lines" taken from the brief.** Two banned lines were almost word for word the brief's own "why" sentences (item 5). The brief and the check disagree; the writer can't see the banned list, so a writer that keeps the brief's wording fails.
- **Coco Chanel.** The page's "Never" list bars a named house or celebrity under "Who she is" (her own connections). The brief gives the quote with an exact hedge ("usually credited"). I used it as the brief words it, as history and not as Diane's connection. The check didn't flag it; the judge may.
- **Item 7 (care, makeup as tips).** The page bars makeup as a numbered item; the brief (operator, 2026-11-17) allows it as tips inside a care habit. I signposted it as care and kept the makeup steps as short sentences inside.
- **Type choice.** The title starts "Why...", which points at "The why explainer", but the brief is seven French habits each with a swap, which is "The rules she never breaks". The table gives no tie-break for this.
- **Numbered signposts and "no template".** The page wants numbered signposts ("Number one is the earring...") but also says any opener used in three tips is a template. I varied the wording around the number; it isn't clear whether "Number N" itself counts.
- **Hook length.** At 165 words it's a little over "about 100 to 160". I left it there rather than cut a beat.

## Revision v2 (script-v2.txt; script.txt left untouched)
Request: the belief-then-truth turn sat in the same slot in all seven tips, and four tips ended on "try it, and...". Re-read the page's "Turn the thought" (the turn moves; never the same slot) and the new "Never the competitor's opening frame" (the hook doesn't use "There are N things in your closet right now that...", so it was left as it was).

Where the turns sit now:
1. Late, a different kind of turn (the obvious fix and why it fails): "The obvious move is to buy it a size up, to be safe. But a sweater bought for the middle hangs off the shoulders, and the line is gone again." The early "We wear them because..." is gone.
2. Early, as a question answered at once: "Does a set keep you looking done? Only in a photograph."
3. Late, belief then truth: "Plenty of American women were raised to believe that more color keeps a woman lively and young. You'd think one color would make you predictable. But it makes you memorable..." (moved from the start of the tip to near its end).
4. Early, belief then truth (kept where it was): "You were probably taught... But size was never the trick."
5. Late: "I used to think a heel..." now comes after the shoe is named, just before the closing habit.
6. A question: "Doesn't more effort look more polished? Not when you can see it." (it replaces "We pile it on because...").
7. The obvious fix, early: "The obvious fix is more coverage next time. But more coverage is how the mask got there..." (it replaces "We reach for more coverage... because...").

Tip endings now:
1. What she'll see at the next photo: her hand stays put, the woman in the photo has a shoulder and a line, the confidence people call beauty.
2. The compliment: "That's the hair strangers notice, and sooner or later one of them leans over to ask, "Who cuts your hair?""
3. A verdict: the woman in the red scarf, not the woman in the busy blouse (unchanged).
4. Permission: nothing goes to the donation bag; each piece gets paired with its opposite. The "put together" compliment moved up into the lengths line.
5. A verdict: presence is what people mean when they say a French woman gets more beautiful with age (unchanged).
6. A picture and a verdict: "The woman who walks out that door looks like elegance without effort. That can't be bought. It can only be subtracted."
7. A short verdict: "Skin that shows through looks rested. And more than anything, it looks like you."

Check runs on script-v2.txt:
1. FAIL (1): turns, "but" 2.3 per 1,000 words (at least 2.5 needed). Changing the "We... because... But" lines to questions and obvious fixes had cut two buts.
2. Fix: tip 3's late turn "Instead, it makes you memorable" became "But it makes you memorable". That line was already a real turn, so no "but" was added for the count. Result: PASS ("but" 6 times, 2.7 per 1,000 words; 8 questions; 2,200 words, about 12.8 minutes).
3. Changed "the woman on that screen" (the phone) to "the woman in that photo", so it can't read as pointing at the video screen. PASS.

The labelled file passed this time: the earlier FAIL on the "(" in the TEST line no longer appears.
