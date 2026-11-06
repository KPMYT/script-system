# Run notes: Mark Silverbridge, iter-16

**Title:** These 3 Powders Will Save You HOURS of Scrubbing Toilets, Tubs and Sinks

## Model picked
`R15-silver-cymbal-windshield-inside-clean.md` (Single-product fix). The title fits no row exactly: three powders, not one, and not "N things about one product". I chose Single-product fix as the closest type ("A title that fits none: use the closest type"), because the page's feeling table has the row "One product or powder fixes it" and R15 is a cleaning job.

## Check results
Run 1:
- `FAIL opening list: a list of more than three in the opening ... "Citric acid, baking soda and borax are three cheap powders, and between them they take most of the scrubbing out of your toilets, tubs and sinks."` (two lists of three in one sentence)
- INFO opening 138 words (about 46 seconds); mid book line 106 words at 74%
- `RESULT: FAIL (1)`

Fixes: the first sentence is now "...three cheap powders that take most of the scrubbing out of a toilet, a tub or a sink."; I cut two words from the opening; I trimmed the book paragraph to 79 words (page: 60 to 80).

Run 2: INFO opening 135 words (about 45 seconds); INFO 1 dollar figure in the opening; INFO mid book line 79 words at 75%; INFO 2,338 words, about 12.9 minutes; `RESULT: PASS`. `output.md` also passes.

## Unclear or contradictory
- Book placement: the page says "about a third of the way in, never before the end of the third item". The brief has four items, so the end of item three falls at 75%. I followed "never" and put the book after item three.
- The brief has four numbered items but the title says "3 Powders" (citric acid covers items one and two). I kept the brief's four.
- The price guide says "At most one price per item", but the brief gives several for item one (toilet, pumice, flapper). I gave the toilet's figure and said the pumice and flapper prices in words.
- "Where the job stops being theirs": the brief names no call, so I used the scratch and the refinishing bill.
