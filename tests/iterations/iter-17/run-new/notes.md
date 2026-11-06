# iter-17 run-new: notes

**Type:** Single-product fix ("1 Cup of This..."). **Model:** `R35-silver-cymbal-unclog-ac-drain.md` (flow only). Step 1 gate: title and brief present, brief carries the promise, not a brand verdict: ready.

## Check results

Run 1: `RESULT: FAIL (2)`
- `FAIL accuracy: poured at a cleanout or vent tee, it treats the line, not the trap: say 'down the line'`: "Poured there, the vinegar runs down the line toward the drain, not back through the trap." Fixed: cut "not back through the trap".
- `FAIL money: cents outside a cost per use`: "That puts one cup at about twenty-five to thirty cents." Fixed: "one cup a month".
- INFO lines (comment question, line before subscribe, opening 111 words / about 44 seconds, coffee habit used, length) needed no change.

Run 2: `RESULT: PASS`.

Eye-check fixes after that (the page's check list, not the program): varied the repeated "called" tag for trade words; dropped an unpaid promise ("it matters when we get to bleach"); added "never bypass the pressure switch" (in the brief's safety notes, missing from my draft); cut "without the service call" from the subscribe line (it read as a guaranteed saving). Run 3: `RESULT: PASS`, 2,295 words, about 15.3 minutes.

## Unclear or contradictory

1. The persona page says "Poured at a cleanout or vent tee, it runs down the line, not back through the trap." `check.py` fails any pour sentence containing "through the trap", so the page's own wording fails the check.
2. Brief: "Flushed via the cleanout: finish with plain water so the trap is full." Water poured at a cleanout downstream of the trap runs down the line, so it doesn't refill the trap. I wrote "finish with a cup of plain water so the trap stays full".
3. Cents: the brief's "about 25 to 30 cents (cost per use)" fails unless the sentence also says "a month", "per" or "each". The page doesn't say that.
4. "Lists of three at most" (page) against the brief's five stop signs. I put each stop in the step where it's found.
5. Workflow section 6: "CTA sections stay warm and even", but a Classic script has no CTA markers. I treated the subscribe line as a CTA: one [warm] tag, nothing else.
6. Word counts disagree: `wc` gives 2,279 and the check gives 2,295. The output uses the check's figure.
