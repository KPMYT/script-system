# iter-16 run-vintage: writer's notes

**Channel:** The Vintage Pipefitter. **Title:** 8 Things You Should NEVER Pour Down Your Drains.
**Video type:** Never-do list. **Model read:** `R16-silver-cymbal-string-trimmer-hacks.md` (flow only).
**Files read:** plumbing-scripts `SKILL.md`, vintage-pipefitter-persona `SKILL.md`, R16, `price-guide.md`, the brief, `core/workflow.md` (its top lines, section 1 and section 6 only). `check.py` was run with `--help` but its source was not read.

## Check runs

**Run 1: FAIL (2)**
- `FAIL length: 2182 words (11.5 minutes at 190); needs at least 2280 (12 minutes)`
- `FAIL long sentence: 39 words: "But when an old drain pipe finally gives out, replacing a room or two of it can run from several hundred dollars to a co..."`
- `INFO the opening: 400 words before item one, about 126 seconds`
- `INFO dollar figures in the opening: 1`

Fixes:
- Split the long sentence in two.
- Length: built out brief points with everyday sense, no filler. Added: hot water after the fat doesn't carry it, because the water cools too. Run hot tap water after snaking to see the drain run clear. Switch off a humming disposal and keep your hand out of it. The laundry sink drains slower after every paint job. A flashlight check of the joints under the sink. A jar test showing the paper comes apart and the wipe stays whole.
- Opening: cut it from about 175 to 159 words (by-eye rule "first item by about 45 seconds").
- Changed "The first one is grease." to "Number one is grease." After that change the checker measured the opening at 159 words; before it, it put item one at about 400 words.

**Run 2: PASS** (2344 words). By-eye fixes after that: varied a repeated "The swap is..." and a repeated "chase", and replaced an invented "an hour later" with "whole".

**Final:** `RESULT: PASS`, 2341 words, about 12.3 minutes. The opening reaches item one at 159 words, about 50 seconds (INFO only). There is one dollar figure in the opening.

## Unclear or contradictory
1. The price guide says "At most one price per item", but the brief gives three prices for item 2 (repipe, snake, enzyme). I kept the snake figure, said the repipe in words and gave the enzyme no price.
2. In the brief, "a tin can, a bucket, a strainer and a trash can" is a four-item list, which breaks "Lists of three at most". I left it out.
3. The skill says "None of the other core files are read", yet Step 5 sends the writer to workflow.md section 6. That section says the VO copy comes "straight after the audit evidence", but the plumbing output has no audit evidence.
4. The persona says the first item comes "by about 45 seconds", and the checker reports 50 seconds as INFO, not a failure. I left it at 50 seconds.
5. The checker seems to recognise item one only from "Number one", not from "The first one".
6. Harness: the shared scratchpad's `vo.txt` was overwritten by another parallel run (it held Werner text). I caught this and rebuilt the VO copy in memory.
