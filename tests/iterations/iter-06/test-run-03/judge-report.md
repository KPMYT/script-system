# TEST: judge report, iter-06 run 03 (Roger the HVAC Guy, batch 1 #4, round 2)

**Title:** "11 Furnace Mistakes HVAC Companies Hope You Keep Making"

**What was judged:**
- The output: `test-run-03/output.md` and `script.txt` (3,383 spoken words, about 22.6 minutes), plus `chat.md`.
- The scanner run: `scanner-main-session.txt`. Its counts are taken as facts: fix-on-sight 0, numbers not found 0, one staccato run to judge, one machine-caught reframe.
- The input: `brief-04.txt`, with its REFERENCE line ignored.
- The reference: `refs/qbWN3OViWxQ-transcript.txt`, Ray Dutton's Garage (faceless, never a model), about 2,318 words.
- Round 1 for comparison: `test-run-01/` (script and judge report).

**Rules checked:**
- `hvac-scripts/SKILL.md` as it stands after `../CHANGES.md`
- `references/price-guide.md`
- models R24 and R25
- `personas/roger-the-hvac-guy.md`
- core `workflow.md` §4-5, `greenlight-audit.md`, `claims-policy.md`, `humanizer.md`

**The chat:** a straight run. START, the channel, then all three inputs in one turn. The gate asked for exactly the title, the brief and the rotation log, then delivered. The menu still reads 1-6 and then 8 (known, `CHANGES.md` operator item 4).

---

## 1. Verdict

**The emotion fix worked.** This is a clearly better script than round 1, and the closest an HVAC script has come to the operator's "make the viewer feel it":
- Every item now opens on something the viewer sees or hears: "Go stand in front of your furnace." "It's the coldest night of the week." "You hear your furnace try."
- Every bridge turns on "but".
- The "you" family rose from 30 to 40 per 1,000 words, above the plumbing script the operator passed. "But" rose from 3.6 to 6.5 per 1,000.
- "Mistake" comes back nine times.
- Item six is the best stretch on the channel so far: "Your stomach drops, because you've got a rough idea what a new furnace costs."
- The round 1 factual bridges are gone, and so is the doubled personal detail.
- The flame sensor job now has the full safety sequence: thermostat down, power off and proved off with a tester checked on a live outlet, gas off, burners let cool, put back together in order, and a named trigger.

**I would not upload it as delivered.** It needs one fix round (FIX-THEN-PASS) for four reasons:
1. **A carbon monoxide step is still narrowed.** Step 6 reads "If they find the furnace is the cause". This is round 1's W11, unfixed.
2. **Three new lines say things neither the brief nor the guide supports**, and two of them touch safety:
   - "I'd keep a spare igniter on the shelf" implies a hands-on part swap with no safety steps and no "it has to match your furnace".
   - "You can often spot it yourself through the little window", followed by "the igniter is the first thing to suspect", contradicts the script's own items eight and nine. A blocked trap or vent gives the same symptom: the small fan runs and there's no glow.
   - "If your furnace locked itself out, switch it off and back on ... and it'll try again" has no limit and no call trigger.
3. **The opening still lands "Number one" at about 40 seconds**, not 30, and its first line, "Most of the furnace calls that land in the dead of winter start with a mistake you could stop making", is a sweeping claim nobody can check.
4. **The script has grown to 22.6 minutes**, past the 12-20 sweet spot, with six items over 250 words. The new emotion has also settled into a formula: nine of eleven items close on the same "[small effort], and [good result]" line.

**The audit block isn't honest enough to stand on its own.** It reads "Rules (F): clean" over the narrowed carbon monoxide step. It names a false-positive reframe and misses the real one. It drops the model differences that round 1 listed.

## 2. Scores (1-10)

| Category | Run 03 (round 2) | Run 01 (round 1) | Reference (Ray Dutton) | Why, in one line |
|---|---|---|---|---|
| Opening (first 45 s) | 7 | 7 | 4 | Better: the first line names the subject with "dead of winter", the curiosity line "your furnace was never even broken" (paid at five), and the villain as a billing fact. But 99 words (about 40 s) to "Number one", and "Most of the furnace calls..." is an uncheckable sweep. |
| Keeping promises | 8 | 7 | 5 | Every forward line is paid: "Number six is the one that can keep you from buying a furnace you never needed" pays about two minutes later; "the rule that protects you" is paid at eight and reused at eleven. Every bridge is true. One win line ("your heat comes back on by itself") fights the reset line before it. |
| Clarity on one listen | 8 | 8 | 8 | Every listed term is explained first time, including the tester. "Locked itself out" isn't explained, and the igniter check misleads (W3). |
| Number load | 9 | 9 | 5 | Dollar figures on 5 of 11 items, at most one per item, one in the opening, never three in a sentence, every one traced. |
| Money framing | 8 | 8 | 7 | The comparison ($75 to $200 against $5 to $15) comes by about 1:32. The quote against the part runs through six, seven and eleven ("The part itself is tens of dollars, and a replacement quote is thousands. That gap is the whole mistake."). |
| Safety | 7 | 8 | 4 | Much better procedures, but four gaps: carbon monoxide step 6 still narrowed; the spare-igniter line implies a part swap with no safety; the lockout reset has no trigger; "or the inducer" is left out of the never-pour line. |
| Voice and persona | 8 | 8 | 4 | 45 once, where it does a job. The detail once. An "I" verdict in 10 of 11 items and one insistence line ("Now listen close..."). Two "I'd do it myself before I'd pay somebody" lines in the same shape. |
| Written for the voice | 9 | 9 | 6 | Ranges with "to", "seventy" and "sixty" in words, no symbols or brackets. The VO copy matches the script word for word (37 tags, about 1 per 91 words). "911" is still in digits. |
| CTA and ending | 9 | 9 | 4 | A fresh subscribe line carrying the title's feeling ("without the extra visits"), then a turn, an outright ask, an own-house-and-numbers question and "I read every one". Nothing after it. |
| Length and pacing | 6 | 7 | 8 | 22.6 minutes: over the sweet spot. Items six, eight and eleven run about 410 words each (the first two mostly earned by safety), and about 150-200 words are trimmable. |
| Originality vs the models | 8 | 8 | 7 | Copy guard 0. Facts the reference never uses (it's about AC). Three or more real differences from R24 and R25. But the opening villain line is a near-paraphrase of the pack's own example sentence. |
| Emotion | 8 | 7 | 8 | All eleven items open on a scene; "but" turns inside every item and on every bridge; a question in 8 of 11 items; the dial ("Your thermostat says seventy, the house says sixty"), the sounds ("No hum. No click. Nothing.") and the clock. Held back by formula: the same win shape nine times, and belief frames repeated. |
| Audit honesty | 6 | 7 | n/a | "Rules (F): clean" is wrong. The reframe evidence names the wrong line. The "Most..." count disagrees with the scanner. The model differences are missing. |

The reference scores are unchanged from the run 01 report. The reference is the same, and I re-checked the counts below.

**My counts** (whole words, from `script.txt`; the reference with its timestamps stripped):

| Per 1,000 words | Run 03 | Run 01 | Plumbing run 03 (passed) | Reference |
|---|---|---|---|---|
| "you" (the word alone) | 23.6 (80) | 21.1 (64) | 26.4 | 38.0 (88) |
| "you" family (you, your, you're, you've, you'd, you'll, yourself) | 39.9 (135) | 30.0 (91) | 39.2 | 55.7 (129) |
| "but" | 6.5 (22) | 3.6 (11) | 6.9 | 1.7 (4) |
| questions | 3.5 (12) | 2.6 (8) | 2.3 | 0.9 (2; the captions drop most) |

**Per section** (line numbers from `script.txt`; bridges counted separately):

| Section | Lines | Words | "but" | Questions | Dollar figures |
|---|---|---|---|---|---|
| Opening | 1-6 | 99 | 0 | 0 | 1 ($75 to $200) |
| 1 Dirty filter | 8-26 | 267 | 2 | 2 | 1 ($5 to $15) |
| 2 Closed vents | 30-43 | 218 | 1 | 1 | 0 |
| 3 Blocked returns | 47-61 | 175 | 1 | 2 | 0 |
| 4 Storage | 65-82 | 194 | 1 | 3 | 0 |
| 5 Switch or breaker | 87-108 | 239 | 1 | 0 | 0 (the after-hours multiplier in words) |
| 6 Heat exchanger | 112-145 | 412 (251 without the carbon monoxide steps) | 1 | 1 | 1 ($3,500 to $6,500) |
| 7 Igniter | 149-169 | 262 | 1 | 1 | 1 ($150 to $400) |
| 8 Condensate trap | 174-198 | 408 | 1 | 0 | 1 ($15 to $25, the tester) |
| 9 Intake and exhaust pipes | 202-220 | 265 | 1 | 1 | 0 |
| 10 Fan on | 225-237 | 193 | 1 | 1 | 0 ("several hundred dollars" in words) |
| 11 Flame sensor | 241-268 | 406 | 1 | 0 | 1 ($100 to $250) |
| Ten bridges | | 190 | 10 | 0 | 0 |
| Ending | 270-274 | 55 | 0 | 0 | 0 |

**The opening.** It runs 99 words, so "Number one" comes at about 40 seconds at 150 a minute (round 1: 114 words, 46 s). The first real tip is the house check "held it up to a window", at about 40 s. The first instruction, "Check it every month", comes at about 1:40. The mistakes-list type wants 15 to 30 seconds. The opening does all of its jobs:
- the point (furnace calls and the mistake behind them)
- the curiosity ("never even broken")
- the villain line
- the tenure as credibility, the count and the scope

It is simply one clause too many in each of lines 4 and 6.

**The number cap holds.** Every figure traces:
- $75 to $200: brief item 1
- $5 to $15: brief item 1
- $3,500 to $6,500: price guide §4, the standard furnace row
- $150 to $400: brief item 8
- $15 to $25: price guide §5, the tester row
- $100 to $250: brief item 7
- "tens of dollars": the brief's $20 to $50 igniter and $10 to $30 sensor
- "thousands": price guide §4
- "several hundred dollars": price guide §2, the blower at $400 to $900
- "a few dollars": price guide §5, the scrub pads
- "pennies": brief item 4. The audit's math is right: $4 to $5 a gallon over 16 cups is about 25 to 30 cents.
- the multiplier: price guide §1, the after-hours row
- "several gallons": price guide §9
- "a regular service call, more on a weekend": price guide §2, in words

Nothing comes from a "don't quote" line.

**The order.** All eleven brief items are present: filter, vents, returns, storage, switch, heat exchanger, igniter, trap, pipes, fan, flame sensor. Every bridge is true of that order. For example, "Those last few were about a furnace shutting down when it shouldn't" covers seven, eight and nine, and all three shut down.

---

## 3. Failures

### Writer slips (the rule was there)

**W1. Carbon monoxide step 6 is still narrowed, and the audit says nothing.**
> "If they find the furnace is the cause, it doesn't run again until a trained tech has fixed it." (line 139)

Price guide §9 says "the furnace **or another appliance**". It's also said as a description ("it doesn't run"), not an instruction. The other six steps are all present and in order:
- four quick beeps and a pause
- never ignore it, and don't hunt for the cause
- out into fresh air
- count heads
- call 911 or the fire department from outside
- stay out until the responders say it's safe
- medical help for a headache or dizziness

Nothing banned is added. The single-chirp line that round 1 had is gone. It's a note in the row, not a step, so that's acceptable.
- **Rule:** SKILL "Safety", a carbon monoxide alarm "gets every step"; run 01 W11 (the same slip).
- **Fix:** "If they find the furnace, or any other gas appliance, is the cause, don't run it again until a trained tech has fixed it."

**W2. "I'd keep a spare igniter on the shelf" implies a hands-on job with no safety, and neither the brief nor the guide supports it.**
> "Where the winters run below zero, I'd keep a spare igniter on the shelf. / A part about the length of your finger, and the furnace you were told to haul away lights right back up." (lines 168-169)

A spare on the shelf only helps if the viewer fits it, or a tech agrees to fit a part the customer supplies. The script gives none of what that job needs:
- power off and proved off, gas off, and let it cool
- the igniter must match the furnace model
- the element is fragile and mustn't be touched with bare fingers

Round 1 handled this right: "Leave the igniter itself to a tech you trust, because it's fragile and it has to match your furnace."
- **Rule:** SKILL "Safety" default 1 ("every hands-on step says the power is off and proved off"); "Inputs": "No chemical, electrical or gas method beyond the brief and the safe defaults"; core D4 and F6 (a claim with no source).
- **Fix:** cut both lines and close on the round 1 shape. For example: "Let the tech fit it, because it's fragile and it has to match your furnace. An igniter is a repair bill, not a furnace payment." Keep the win.

**W3. The igniter check contradicts the script's own items eight and nine.**
> "You can often spot it yourself through the little window in the front panel. / If you hear that small fan run and you never see an orange glow, the igniter is the first thing to suspect." (lines 166-167)

There are two problems:
- **Unsupported.** Many furnaces have a small sight window, often in the lower door for the status light, but "often" seeing the igniter through it is in neither the brief nor the guide.
- **Misleading.** On a standard hot-surface sequence the igniter is powered only after the pressure switch proves the draft. A clogged trap (item eight) or a snowed-in pipe (item nine) gives exactly this symptom: the small fan runs and there's never a glow. A viewer with a clogged trap who follows item seven buys an igniter, maybe the spare from W2.
- **Rule:** SKILL "Proof": "Only checks the brief or everyday knowledge confirms"; "Never: sweeping claims nobody can check".
- **Fix:** "If the small fan runs and nothing ever glows, ask the tech straight out whether it's the igniter, and to show you." Or cut the line, and let the sentence to say to the tech ("Is it the igniter?") carry the item.

**W4. The lockout reset has no limit and no trigger, and its win line contradicts it.**
> "If your furnace locked itself out, switch it off and back on at its switch, and it'll try again." (line 218) / "A broom and two minutes outside, and your heat comes back on by itself." (line 220)

The brief is silent on the reset. Power-cycling after a lockout is everyday advice, but the script:
- says it as a certainty ("it'll try again")
- doesn't explain "locked itself out"
- gives no stop sign
- then says the heat comes back "by itself", against the step just given

A reset repeated over a fault is how a safety lockout gets ignored. Item five's breaker step gets this right ("one time ... If it snaps right back off ... stop there").
- **Rule:** SKILL "Safety", "How safety sounds": the call-a-tech line names its trigger; default 3 (a safety switch is telling you something).
- **Fix:** "If it still won't start once the pipes are clear, switch it off and back on once at its switch. If it quits again, that's a call." Then a win without "by itself": "A broom and two minutes outside, and the heat's back."

**W5. The first line is a sweeping claim, and the opening still runs past 30 seconds.**
> "Most of the furnace calls that land in the dead of winter start with a mistake you could stop making this week." (line 1)

"Most" of winter furnace calls is in neither the brief nor the guide. The brief says only that these mistakes "lead to service calls". The line also leans on the homeowner, blaming them, which the pack's viewer won't enjoy. "Number one" comes after 99 words, about 40 s; the type wants 15 to 30 s.
- **Rules:**
  - SKILL "Proof", "Never: sweeping claims nobody can check"
  - SKILL "The video types", mistakes list: first tip by 15-30 s
  - SKILL "The opening" job 6: "in a list, item one by about 30 seconds"
- **Fix:**
  - Line 1, the shape: "A lot of the furnace calls that land in the dead of winter start with a habit you could break this week."
  - Line 6: cut to "I've spent 45 years around furnaces, and not one of these eleven means opening a gas line or touching a live wire."
  - Line 4: trim to one clause (see W6).
  - That brings the opening to about 75 words, about 30 s.

**W6. The opening villain line is a near-copy of the pack's own example sentence. On motive, it stays inside the rule as written, but only just.**
> "Just getting a truck to your driveway runs $75 to $200, and since the trade gets paid by the visit, the habit that ends those visits is nobody's job to mention." (line 4)

SKILL "The villain": "The trade is paid by the visit and the install, so a cheap check that ends the visits is nobody's business to mention." The script swaps three words ("so a cheap check" to "since ... the habit", "the" to "those", "business" to "job"). No 8-word run is shared, so the copy guard passes. But the SKILL says its example lines show a shape and are never reused.

**Does it cross into the trade's motives?** By the pack's letter, no. It's the pack's own sanctioned billing fact. "Nobody's job" names a role, not a wish, and there's no "hope", "want", "waiting on" or "quietly". Ray Dutton's opening ("quietly hoping you never stop", "the exact service call they've been waiting on") is what crossing looks like.

But the "since" makes it a because-sentence about why nobody speaks up. A viewer hears an incentive explaining a silence, which is one short step from "they keep quiet because it pays". That's the inference the pack warns drew "this is a lie" comments. It's the closest line in the script to motive, and the pack's own example carries the same "so". That part is a library question (L2).
- **Rule:** SKILL "Using the models" and "Files in this skill" (example lines are a shape, never wording); "The villain", "not at motives".
- **Fix:** keep the two facts side by side with no "since": "Just getting a truck to your driveway runs $75 to $200. The habit that ends those visits isn't on anybody's checklist." Or use the profile's family: "And there's no money in the visit that never happens."

**W7. A split-sentence reframe, and the audit's reframe evidence names the wrong line.**
> "That mistake won't show up on a repair bill. / At its worst, it shows up as a fire that starts in the one room nobody's watching." (lines 74-75)

This is the "it's not X, it's Y" shape across a sentence break: won't show up as a bill; shows up as a fire. The scanner can't catch it (known, `CHANGES.md` operator item 3).

The line the scanner did catch, "don't try to get around that pressure switch. It's telling you something", is a reason, not an X/Y contrast: a false positive. The audit reports "reframes 1" and names that false positive. Under the scanner's floor rule ("the audit's count may never be lower"), the honest count is 2, against a limit of 1.
- **Rule:** `humanizer.md` H21; `greenlight-audit.md` D5; run 01 W4 (the same class of miss).
- **Fix:** "At its worst, that mistake ends in a fire in the one room nobody's watching." In the audit, record the machine catch as judged (a reason, not a reframe), with a hand count of 0 after the fix.

**W8. The emotion has settled into a formula.**
The fixes went in item by item, and the same moves now sit in the same slots:
- **The win.** Nine of eleven items close on "[small effort or cost], and [good result]":
  - "Opening a vent costs you nothing, and your furnace stops fighting you."
  - "Ten minutes of moving furniture, and the air's moving again."
  - "An empty corner costs nothing, and it's the cheapest fire protection in your house."
  - "Two minutes, one switch, and your house warms up..."
  - "A part about the length of your finger, and the furnace..."
  - "The vinegar costs you pennies, and your furnace runs its whole cycle again."
  - "A broom and two minutes outside, and your heat comes back on..."
  - "One button on the wall, and your blower gets to rest..."
  - "A few minutes, a scrub pad that costs a few dollars, and warm air..."
- **The belief frames repeat:**
  - "You'd think..." at lines 15 and 207
  - "It sounds like..." at lines 157 and 249
  - "Plenty of..." at lines 94 and 181
  - "It feels like good use of the space" at line 70, and "a mistake that feels like good sense" at line 30
- **The turn line:** "So what do you do instead?" appears twice, at lines 18 and 124 (the SKILL's own example of the turn, word for word).
- **The "I" verdict:** "I'd move the couch myself before I'd pay anybody to come tell me..." (line 60) and "I'd rather shovel that path myself than pay somebody to shovel it for me..." (line 219) are the same sentence.

Heard in a row, this is the "tic" the SKILL warns about.
- **Rule:** SKILL "Voice": "A phrase is voice once; in the same slot every video, it's a tic ... rotate what opens an item"; `humanizer.md` H18 (echo); SKILL "Emotion" 4: "Rotate how the belief is named".
- **Fix:** keep the effort-and-result win on four or five items. End the others on comfort in the body ("and the back bedroom's warm by supper"), on the contrast with the bill, or on a plain "You're fine." Swap one "You'd think", one "It sounds like" and one "Plenty of" for "the box says", "you've probably heard" or a straight question. Change one "So what do you do instead?" to "Here's the fix." Rewrite line 219 as a price line ("That's an emergency rate for a shovel's work.").

**W9. The run grew to 22.6 minutes, and some of it is soft.**
Round 1 ran 20.2 minutes; this runs 22.6, past the 12-20 sweet spot. Items six and eight are long mostly because of required safety, and that's fair. Item six without its carbon monoxide steps is 251 words. Item eleven is a full DIY procedure. But about 150 to 200 words can go without touching a safety step:

| Line(s) | What to do |
|---|---|
| 14 | "The burners go out, the fan keeps blowing, and a few minutes later the whole thing starts over, again and again, and that's hard on every part in there." (31 words) can be half that. |
| 166-168 | Cut (W2, W3). |
| 210 | "And of course it happens on a cold night, because that's when the snow is deepest." restates line 203's scene. |
| 261 | "Skip coarse sandpaper, because a scratched rod picks up grime even faster." (round 1's judge flagged the same line). |
| Bridges | Shorten the three longest: line 84-85 (26 words), lines 171-172 (23) and lines 222-223 (30). |

- **Rule:** SKILL "Length" ("12 to 20 minutes is the sweet spot", "Never pad"); "The item shape in lists" (about 150-250 words; "Cut extra steps, repeated warnings and restated points first").
- **Fix:** the cuts above, plus W5's opening trim. That's about 3,150 words, about 21 minutes.

**W10. "Two white pipes" as the test for a condensing furnace, and two smaller unsupported lines.**
- **The pipes.** "If you've got two white plastic pipes running out the side of your house, you've got a high-efficiency furnace" (line 175) and "One pulls in fresh air for the burners, and the other pushes the exhaust out" (line 205). Some condensing furnaces run a single exhaust pipe and take their air from the room. Those owners will decide item eight isn't for them. Round 1's W13 flagged the same point. **Fix:** "one or two white plastic pipes", and "On most, one pulls in fresh air...".
- **"Rare."** "a cracked heat exchanger is a big, rare quote" (line 147). The script only needs "big".
- **The never-pour line.** "Never pour anything into the small rubber hoses that run up to the pressure switch" (line 192) leaves out the inducer, which SKILL "Safety" default 5 names. **Fix:** "...or into the inducer, that small fan motor."

**W11. The audit block's wrong or missing claims.**

| The block says | The truth |
|---|---|
| "Rules (F): clean" | F8 fails on W1; F6 and D4 fail on W2, W3 and W5. |
| "reframes 1 ('don't try to get around that pressure switch...', machine-caught)" | The machine catch is a false positive. The real reframe (W7) is uncounted. |
| "'Most...' 1 (the first line)" | The scanner reports 0. That's harmless as a stricter count, but the Scanner line says "run on the delivered text", so its numbers should be the scanner's. |
| Hook "modelled on R25 [0:00] (the title's subject as the first line...)" | R25 opens on a question, not a statement. "Modelled on R24 [0:00] (subject, then the question the list answers)" doesn't fit either: the script asks no question that the list answers. |
| The model differences | Round 1 listed four. This block lists none, though SKILL "Using the models" 5 says the audit checks them. The differences exist: eleven items against five and six; R25 holds the safety item to last, this script puts it at six; both models carry no dollar figures; this script bridges every item; R24 counts down and has a mid-video CTA. They just aren't recorded. |

- **Fix:** correct each line, and run the audit again from group A.

### Library fixes (a rule is missing, unclear or wrong)

**L1. The opening's 30 seconds still isn't in the handover checklist.** This was run 01's L4, and it wasn't changed. "Before handing over" still checks only "the fix or product named by about 15 seconds". Both HVAC mistakes-list openings have missed 30 s (46 s, then 40 s). **Proposed:** add "in a list, 'Number one' within about 75 spoken words" to "Before handing over" and to the evidence block's Hook line.

**L2. The pack's sanctioned villain sentence carries a "so" that reads as motive.** SKILL "The villain": "The trade is paid by the visit and the install, so a cheap check that ends the visits is nobody's business to mention." The writer copied its shape almost word for word (W6). Joined by "so" or "since", the two facts become a because-sentence about why nobody speaks. **Proposed** (for the operator's yes, since it touches the villain rule): reword the example so the two facts sit side by side ("The trade is paid by the visit. A cheap check that ends the visits isn't on anybody's list."). Add one line: "Say how they're paid and what goes unsaid; never join them with 'so', 'since' or 'because'."

**L3. No rule rotates the item's win.** SKILL "Emotion" 8 asks for a win on every item, and gives one example shape ("That's a $5 part doing a $300 visit's job."). With "Voice" saying only "rotate what opens an item and what closes the video", nothing stops the same close on every item (W8). **Proposed:** "Rotate the win's shape: the effort against the result, comfort in the body, the bill avoided, plain reassurance. No shape on more than about a third of the items." The same note could cover the belief frame ("no frame twice").

**L4. The rubric and the SKILL say different things about the carbon monoxide steps.** The writer narrowed step 6 two rounds running, and both audits passed it. The SKILL says "every step ... in the script's own words", and "own words" seems to be read as licence to narrow "or another appliance" to the furnace on a furnace video. **Proposed:** in SKILL "Safety", add "own words may shorten a step, never narrow it: step 6 always covers any appliance". Add a scanner judgment line: when "carbon monoxide alarm" appears, list the seven step keywords found and missing.

**L5. No rule for "keep a spare part".** The pack covers DIY steps but not lines that imply DIY: "keep a spare", "have one on hand". **Proposed:** in "Safety", add "A line that suggests the viewer fit a part (a spare on the shelf) either carries that job's full safety steps or sends the job to a tech."

**L6. The scanner's H21 net still misses the split reframe, and it raised a false positive.** This repeats run 01's L5 (`CHANGES.md` operator item 3). This run adds the other side: "don't X. It's telling you something" was caught as a reframe. **Proposed:** the judgment-tier pattern from run 01's L5, plus "won't ... It ... shows up as" across a break. Don't count "It's telling you" after an instruction.

**L7. Still open from run 01:**
- L3: the personal detail's limit. The SKILL says "At most twice", the profile says "at most one". The writer used it once.
- L7: "911" in digits.
- L8: the menu skips 7.

Nothing new on these.

---

## 4. What the script does better than the reference

**The villain stays on price and silence, not wanting.**
- Script: "Signing for that kind of money on a sentence nobody showed you makes me sick." / "Paying after-hours money for somebody to flip a switch makes my teeth hurt."
- Reference: "the company who services it is quietly hoping you never stop" / "the exact service call they've been waiting on all summer".

**The honest tech is kept, and the red tag is respected.**
- Script: "A tech who finds one and tells you is doing his job, and doing you a favor. But a real crack leaves proof." / "If the tech red-tags the furnace ... don't run it while you wait for that second opinion."
- Reference: "The cracked heat exchanger they'll try to red tag off a photo on a phone", the red tag framed as a sales tactic, with no alarm steps at all.

**A sentence to say to the tech.**
- Script: "Say it plain: show me where it's cracked." / "Is it the igniter? If it is, ask for an igniter, and have them show you anything else they say is wrong."

**Safety inside the step, with named triggers.**
- Script: "Touch it to an outlet you know is live first, so you know the tester works, then hold it against the power cable going into the furnace. No beep, no power." / "If it snaps right back off as soon as you push it on, stop there. That's a call, and a fair one." / "If the trap's clean and full and it still shuts down, don't try to get around that pressure switch."

**The machine's sounds and the dial that won't reach.**
- Script: "Your thermostat says seventy, the house says sixty, and there's no sound coming from the basement. No hum. No click. Nothing." / "You hear your furnace try. A small fan kicks on, there's a click or two, and nothing lights."

**Plain pictures that teach.**
- Script: "your furnace is trying to breathe with a hand over its mouth" / "block it and you've built yourself a dirty filter without the filter" / "an igniter is a wear part, like the bulb in a lamp".

**Numbers one at a time.**
- Script: one figure per item at most. "The part itself is tens of dollars, and a replacement quote is thousands. That gap is the whole mistake."
- Reference: "somewhere around 10 or $20 a pound ... 40, 70, even $90 a pound, and the whole recharge runs you 100 to $400" in one breath.

**Both sides where viewers split.**
- Script: "if somebody in your house has allergies, those can be worth it. But a dense filter fills up faster..." / "Some folks run the fan on all the time ... that's a fair choice. But for most houses in winter..."

**The ending.**
- Script: "One last thing, and it's about your house. Leave me a comment with the year your furnace went in and the biggest repair quote anybody's ever handed you for it. I read every one." Nothing comes after it.
- Reference: a subscribe ask, a next-video tease and "Keep your cool and I'll see you in the next one" after its question.

---

## 5. Top five changes, ranked

1. **Close the safety gaps** (W1, W2, W4, W10):
   - carbon monoxide step 6 says "or any other appliance" and is said as an instruction
   - cut "I'd keep a spare igniter on the shelf" and put back "let the tech fit it, it has to match your furnace"
   - the lockout reset becomes "once; if it quits again, that's a call"
   - add the inducer to the never-pour line
   - Library: L4, L5.
2. **Take out the unsupported lines** (W3, W5, W10):
   - the igniter window check, which contradicts items eight and nine
   - "Most of the furnace calls..."
   - "two white plastic pipes" as the only test
   - "rare"
3. **Make the opening simpler and faster** (W5, W6): about 75 words, so "Number one" lands by about 30 s. Rewrite the villain line so it doesn't copy the pack's example or hang on "since". Library: L1, L2.
4. **Break the formula without losing the gains** (W7, W8): rotate the item wins and the belief frames, and fix the item-four split reframe. Keep the "you" level, the "but" level and the scenes exactly as they are. Library: L3, L6.
5. **Trim to about 21 minutes, and make the audit honest** (W9, W11): about 200 words out, no safety step touched. Correct "Rules (F)", the reframe evidence, the "Most..." count and the Hook line's model claims. Restore the model differences, then re-run the audit from group A.

---

## Round 1 against round 2

**What improved:**
- **Emotion (the point of the round).** The "you" family went from 30.0 to 39.9 per 1,000, "but" from 3.6 to 6.5, and questions from 2.6 to 3.5. All eleven items open on a scene. Every bridge turns. "Mistake" comes back nine times, against once. The narrator gives a verdict in 10 of 11 items.
- **True bridges, and no motive-leaning bridge.**
- **Safety procedures.** The tester is tried on a live outlet first, the burners are let cool, the gas handle positions are given, and everything goes back together in order. All of these come from the library fixes.
- **The personal detail,** said once.

**What got worse:**
- **New unsupported lines,** two of them touching safety: the spare igniter, the window check and the lockout reset.
- **Length,** from 20.2 to 22.6 minutes.
- **A formula,** in the wins and the belief frames.
- **The audit block** is thinner: no model differences, and a wrong reframe line.

**Each round 1 failure:**

| Run 01 failure | Status in run 03 |
|---|---|
| W1 "Those first four are all about air" (false bridge) | **Fixed.** Every bridge is true of the order. |
| W2 "parts somebody gets paid to replace" (near-motive) | **Fixed.** Gone; no bridge leans on motive. |
| W3 "paid to mention" twice | **Fixed.** The villain is in new words each time. |
| W4 second reframe, audit says one | **Not fixed.** A new split reframe (item four), and the audit names a false positive (W7). |
| W5 opening 114 words, item one at about 46 s | **Improved, not fixed.** 99 words, about 40 s (W5; library L1 still open). |
| W6 first line hits no pain | **Partly fixed.** "dead of winter" and the mistake are there, but the line is now an uncheckable "Most..." (W5). |
| W7 items five and ten don't open on a scene | **Fixed.** All eleven open on a scene. |
| W8 thin "but" turns | **Fixed.** 6.5 per 1,000, a belief turn in every item, every bridge turned; now formulaic (W8). |
| W9 the title's feeling barely returns | **Fixed.** "Mistake" nine times; "the extra visits" in the subscribe line. |
| W10 "one more visit" echo | **Fixed;** new echoes in its place (W8). |
| W11 carbon monoxide step 6 narrowed | **Not fixed.** The same line, and the audit again says nothing (W1). |
| W12 personal detail twice | **Fixed.** Once. |
| W13 unclear lines (the "airflow" stray, the "slow leak", "each of these", "the wait can run into days", "two pipes") | **Mostly fixed.** The stray, the leak and the "days" are gone. "Each of these" became the "Most of..." sweep. "Two pipes" is unchanged (W10). |
| W14 trims for the long items | **Worse.** Six items over 250 words (run 01: five), 22.6 minutes (W9). |
| L1 cool-down missing (library) | **Fixed** in the pack and applied: "give the burners time to cool". |
| L2 tester method and price (library) | **Fixed** in the pack and the guide, and applied at items eight and eleven. |
| L3 personal-detail limit conflict | **Not changed** in the library; the writer used it once. |
| L4 opening timing not in the checklist | **Not changed** (L1 here). |
| L5 scanner misses the split reframe | **Not changed;** it recurred (L6 here). |
| L6 "but" and "you" floors | **Changed** (the target of about 7 "but" and the measured gap), and it worked. |
| L7 "911", L8 menu skips 7 | **Not changed** (known). |
