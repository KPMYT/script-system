# TEST: judge report, iter-06 run 01 (Roger the HVAC Guy, batch 1 #4)

**Title:** "11 Furnace Mistakes HVAC Companies Hope You Keep Making"
**Judged:** `test-run-01/output.md` and `script.txt` (3,037 spoken words, about 20.2 minutes), `chat.md`, `scanner-main-session.txt` (counts taken as facts: every check 0), `brief-04.txt` (its REFERENCE line ignored). Reference: `refs/qbWN3OViWxQ-transcript.txt` (Ray Dutton's Garage, "5 AC Mistakes HVAC Companies Hope You Keep Making", about 2,318 words with the timestamps stripped, 14:03; faceless, never a model). Rules: `hvac-scripts/SKILL.md`, `references/price-guide.md`, `references/models/INDEX.md`, R24, R25, `personas/roger-the-hvac-guy.md`, core `workflow.md` §4-5, `greenlight-audit.md`, `claims-policy.md`, `humanizer.md`.

**The gate (chat.md):** handled correctly. It refused "just write it, the brief is basically the title", asked for the brief, then for the rotation log, and wrote only after "none". One small thing: the channel menu reads 1-6 then **8** (no 7), because row 7 of `core/channels.md` is missing on this branch. A VA may wonder where 7 went (library note, below).

---

## 1. Verdict

This is a clean, safe, honest script. It's easy to follow and it keeps the rules far better than the reference. Every brief item is there, every price traces, the carbon monoxide steps are close to complete, the villain stays on the price and the quote, and the ending is right. **But it isn't yet at the operator's bar of "make the viewer feel it, simpler and stronger".**
- The first line is soft ("end in a paid visit").
- Item one starts about 46 seconds in, where the type wants 15 to 30.
- The "but" turns are spread thinly: exactly one per item, and two of those aren't belief turns.
- "You" comes at about two-thirds the reference's rate.
- After line 1 the title's feeling comes back only as the word "visit".

There are also two factual slips in the bridges, both caused by the reorder or the villain wording:
- "Those first four are all about air." Item two is the power switch, not air.
- "The next three are parts somebody gets paid to replace." Item seven tells the viewer *to* pay for the igniter, and item eight is a whole furnace.

The audit block passes the script with a second "it's not X, it's Y" reframe in it. **I would upload it after one fix round (FIX-THEN-PASS), not as delivered.** The fixes are all local: about 15 lines.

## 2. Scores (1-10)

| Category | Script | Reference (Ray Dutton) | Why, in one line |
|---|---|---|---|
| Opening (first 45 s) | 7 | 4 | Script: the point and count in sentence 1, a house question answered at once, the villain as a silence, scope, tenure; but 114 words (about 46 s) before "Number one" and a soft first line. Ref: a strong scene, but motives ("quietly hoping you never stop"), a name intro and a "saved the biggest for last" tease, and item one at 0:57. |
| Keeping promises | 7 | 5 | Script: all eleven paid and the title paid without accusing; two bridge lines promise things that aren't so ("first four are all about air"; "parts somebody gets paid to replace"). Ref: "the last one clears 10,000" is paid with "$8,000". |
| Clarity on one listen | 8 | 8 | Script: every listed trade term explained on first use (blower, limit switch, static pressure, supply and return, condensing furnace, condensate line and trap, pressure switch, inducer, flame sensor, hot-surface igniter, heat exchanger, red tag); a few stray lines ("The fix is the airflow."). Ref: plain and vivid, "manual J" explained. |
| Number load | 9 | 5 | Script: none in the opening, dollar figures on 5 of 11 items, at most one per item, all traced. Ref: item four alone carries "10 or $20 a pound", "40, 70, even $90 a pound" and "100 to $400". |
| Money framing | 8 | 7 | Script: the comparison at about 1:45 ($75 to $200 against "a few dollars in a multipack"); the quote-against-the-part ladder across items six to eight is the best stretch. Ref: the refrigerant markup is strong but stacked. |
| Safety | 8 | 4 | Script: power off and proved off before the trap and sensor, gas valve off, the trap refilled, nothing into the hoses or inducer, never bypass the limit switch, the red tag respected, named triggers; missing a cool-down before the flame sensor, how to use the tester, and step 6 of the alarm is narrowed. Ref: calls the red tag an "urgency tactic" and gives no alarm steps. |
| Voice and persona | 8 | 4 | Script: blunt and plain, opinions in most items, 45 once and doing a job, no stories or tests, no Ray catchphrases; the personal detail comes back a second time at the end. Ref: a name intro, 25 years, "same companies", "Keep your cool", motive lines throughout. |
| Written for the voice | 9 | 6 | Script: ranges with "to", no symbols, no brackets, straight quotes, and the VO copy matches word for word with 32 tags (about 1 per 95 words); "911" in digits is the only risk. Ref: "3-4°", "10 or $20" (caption forms; judged lightly). |
| CTA and ending | 9 | 4 | Script: no mid-CTA, one fresh subscribe line naming Roger the HVAC Guy, then a turn, an outright ask, an own-house question and "I read every one", with nothing after. Ref: a great comment question, then subscribe, a next-video tease and a catchphrase sign-off. |
| Length and pacing | 7 | 8 | Script: 20.2 min, the top of the sweet spot; items 5, 6 and 8 run 317-389 words; little real padding, but a few soft lines. Ref: 14 min, five long items that move. |
| Originality vs the models | 8 | 7 | Script: differs from R24 and R25 in four named, true ways; mostly facts the reference doesn't use (the only overlaps are closing vents and the heat-exchanger camera, both from the brief). Ref: its own lab-study angle on shading. |
| Emotion | 7 | 8 | Script: good machine sounds ("No hum, no click, nothing."), the clock (Saturday night, the coldest night) and relief before the end; thin "but" turns, a lower "you" rate, the title's feeling rarely back, and items 5 and 10 don't open on a scene. Ref: intense and physical ("cooking the most expensive parts", "it's rent"), but it runs on motive. |
| Audit honesty | 7 | n/a | Mostly accurate. Wrong on the reframe count (says 1; there are 2), on "item shape on all eleven", on "every carbon monoxide alarm step", and silent on the false bridge lines. |

**My counts, from `script.txt` (3,037 words) against the reference (2,318 words, timestamps stripped):**

| Per 1,000 words | Script | Reference |
|---|---|---|
| "you" (the word alone) | 21.1 (64) | 38.0 (88) |
| "you" family (you, your, you're, you've, you'd, you'll, yourself) | 30.0 (91) | 55.7 (129) |
| "but" | 3.6 (11) | 1.7 (4) |
| question marks | 2.6 (8) | 0.9 (2; the auto-captions drop most question marks, so this undercounts) |

**Per item** (lines from `script.txt`):

| Section | Words | "but" | Questions | Dollar figures |
|---|---|---|---|---|
| Opening | 114 | 0 | 1 | 0 |
| 1 Dirty filter | 271 | 1 | 1 (rhetorical) | 1 ($75 to $200; filter in words) |
| 2 Switch or breaker | 268 | 1 | 1 | 0 (the "one and a half to three times" multiplier) |
| 3 Closed vents | 205 | 1 | 0 | 0 |
| 4 Blocked returns | 215 | 1 | 1 | 0 |
| 5 Condensate trap | 369 | 1 | 0 | 1 ($100 to $250) |
| 6 Flame sensor | 317 | 1 | 2 | 1 ($100 to $250) |
| 7 Igniter | 195 | 1 | 0 | 1 ($150 to $400; "into the thousands" in words) |
| 8 Heat exchanger | 389 | 1 | 1 | 1 ($3,500 to $9,000) |
| 9 Intake and exhaust pipes | 224 | 1 | 0 | 0 |
| 10 Fan on | 189 | 1 | 1 | 0 ("a few hundred dollars and up" in words) |
| 11 Storage | 228 | 1 | 0 | 0 |
| Ending | 53 | 0 | 0 | 0 |

- **The number cap holds.** Dollar figures sit on 5 of 11 items (45%); counting item 2's multiplier, 6 of 11 (55%, about half). No item has two. The opening has none. No sentence has three. Every figure traces:
  - $75 to $200: brief item 1
  - $100 to $250 for the trap: guide §2, "clogged condensate line or trap cleared"
  - $100 to $250 for the flame sensor: brief item 7
  - $150 to $400: brief item 8
  - $3,500 to $9,000: guide §4, the standard row's low end to the high-efficiency row's top, said "depending on the model"
  - blower "a few hundred dollars and up": guide §2, $400 to $900
  - the multiplier: guide §1, the after-hours row
  - Nothing comes from a "don't quote" line: no "$100" igniter, and no "a heat exchanger costs more than a new furnace".
- **Item length.** Six items fall inside 150-250 words. Two run a little over (271, 268), and three run well over: the trap (369), the flame sensor (317) and the heat exchanger (389). The heat exchanger's extra length is mostly the required carbon monoxide steps, and that's fair. The trap and the sensor have trimmable lines (below).
- **The reorder.** Brief order: filter, vents, returns, trap, pipes, switch, flame sensor, igniter, heat exchanger, fan, storage. Script order: filter, **switch**, vents, returns, trap, **flame sensor, igniter, heat exchanger**, **pipes**, fan, storage. All eleven brief items are present, each with its brief fact and fix. The reorder mostly works:
  - the free "no power" check comes early;
  - the sensor, igniter and heat exchanger run as a rising quote ladder (cleaning, a repair, a whole furnace), which is the script's best money device;
  - the pipes item calls back cleanly to "those white plastic pipes from number five";
  - the scariest item sits at eight, so the video still finishes on relief.
  
  But moving the switch to number two breaks the "air" grouping, and the bridge at line 74 says it anyway (failure W1).

## 3. Failures

### Writer slips (the rule was there)

**W1. A false bridge, caused by the reorder.**
> "Those first four are all about air." (line 74)

Item two is the furnace switch and the breaker, not air. **Rule:** `greenlight-audit.md` A4 and B5 (a bridge must be true, and the next segment must deliver it); SKILL "Point then promise". **Fix:** either swap items 2 and 4 (filter, vents, returns, then the switch, then the trap), so "Those first three are all about air" becomes true and "That one costs nothing" still bridges into the trap; or keep the order and say "Three of those first four come down to air."

**W2. A villain bridge that misdescribes what follows and leans toward motive.**
> "That trap is a part nobody's paid to mention. / The next three are parts somebody gets paid to replace." (lines 96-97)

- **Inaccurate.** Item seven tells the viewer *to* have the igniter replaced ("Leave the igniter itself to a tech you trust"), and item eight is a whole furnace, not a part.
- **Close to motive.** "Gets paid to replace", hung over three items whose message is "don't let them replace it", invites the listener to fill in *why*. That is the inference the pack forbids ("Aim it at the price, the upsell and the silence, not at motives"; SKILL "The villain" and "Emotion", "Never, still: ... the trade's motives").

It doesn't state a motive, so it isn't a hard fail. But it's the weakest villain line in the script. **Fix:** a price fact: "The next three are where a small repair can turn into a big quote."

**On the opening's villain line:** "over a check nobody on the truck is paid to mention" (line 4) stays inside the rule. It's the pack's sanctioned billing fact: SKILL "The villain" says "a cheap check that ends the visits is nobody's business to mention", and it describes how the visit is paid, not what anyone wants. It is, though, very close to the pack's own example line ("nobody on the truck is going to mention it").

**W3. The same villain words twice.**
> "nobody on the truck is paid to mention" (line 4) / "a part nobody's paid to mention" (line 96)

**Rule:** SKILL "The villain": "never in the same words twice". **Fix:** the W2 rewrite removes the second one.

**W4. A second "it's not X, it's Y" reframe, and the audit reports one.**
> "That's normal, and it's a repair, not the end of the furnace." (line 126, the one the audit counted)
> "because a lot of the time that sensor doesn't need replacing at all. / It needs cleaning." (lines 105-106, not counted)

**Rule:** `humanizer.md` H21 and `greenlight-audit.md` D5: at most one per script. **Fix:** "That's a lot of money to wipe off a rod. You'd figure it needs a new one, but a lot of the time a good cleaning is all that sensor needs." This also gives item six the "but" turn it lacks (W8).

**W5. The opening runs long, so item one starts late.**
The opening is 114 words, about 46 seconds; "Number one." follows. The first real step (hold the filter to a light) lands at about 2:00. **Rule:** SKILL "The video types", mistakes list: "First tip by 15-30 s"; "The opening" job 6: "in a list, item one by about 30 seconds". **Fix:** cut it to about 70 words. Merge lines 5 and 6:
> "Nothing here means opening a gas line or working on anything live, and in 45 years these are the ones I'd stop first."

Then trim the villain line to one clause.

**W6. The first line hits no pain.**
> "These are the eleven furnace mistakes that end in a paid visit, and nearly every one is something you can fix or check yourself, for a few dollars."

It's correct but flat: no cold house, no bill, no strong word. **Rule:** SKILL "Simpler and stronger": "The first line hits the viewer's own pain in strong, plain words." **Fix (the shape):** the count plus a felt cost, such as "Eleven furnace mistakes, and every one of them ends with a cold house and a man at the door with a bill." Keep "nearly every one you can fix yourself" for the next line.

**W7. Two items don't open on the scene.**
- Item five opens on how the furnace works ("That's the high-efficiency furnace, also called a condensing furnace..."). The scene ("Picture the furnace trying to start, running a few seconds and quitting, or a puddle on the floor beside it.") comes fourth.
- Item ten opens on a definition ("Your thermostat has a fan setting, usually with two choices").

**Rule:** SKILL "Emotion" 1 ("open each item on what they see, hear, feel or smell... not on how the thing works") and "The item shape in lists" (the scene comes first). The audit's "item shape on all eleven" is wrong. **Fix:** open item five on the puddle, or on the furnace that starts and quits. Open item ten on the cold draft from the vents between cycles (it's already at line 184).

**W8. The "but" turns are spread thinly.**
Eleven "but"s in 3,037 words (3.6 per 1,000): exactly one per item, none in the bridges. Two aren't belief-then-truth turns:
- item one: "but once it's caked";
- item six: "Very fine emery cloth works too, but it's optional."

**Rule:** SKILL "Emotion" 4: "much more of it, inside items and between them"; "Inside every item, at least one turn: say what people think or do, then 'but', then the truth"; "Between items, bridges that turn". **Fix:**
- item one: add a belief turn ("You'd figure a filter that still lets air through is fine. But...");
- item six: use the W4 rewrite;
- turn two or three bridges ("But that one costs you nothing. The next one can cost you a furnace.").

**W9. The title's feeling barely comes back.**
"Mistake" appears once, in line 1. "Companies" appears once, as "another company". The idea that the trade does well when you keep doing these comes back only as the word "visit" (9 times). **Rule:** SKILL "Emotion" 9: "Come back to the title's idea and its key word... every few items." **Fix:** two or three items should end on the habit and its bill in fresh words, for example item four: "Leave the couch there, and you'll keep paying for the same visit every winter." Keep it as a billing fact, never a motive.

**W10. Echoes.**
- "one more visit" appears twice (line 162, "A second look costs you one more visit"; line 202, "a dusty, overheated furnace and one more visit").
- "visit" appears 9 times in all.

**Rule:** `humanizer.md` H18. **Fix:** item eleven: "...and a service call you didn't need."

**W11. Step 6 of the carbon monoxide alarm is narrowed.**
> "If they find the furnace is the cause, don't run it again until a trained tech has fixed it." (line 156)

Price guide §9 says "the furnace **or another appliance**". **Rule:** SKILL "Safety": "gets every step"; the audit's "every carbon monoxide alarm step from price guide 9" is wrong. **Fix:** "If they find the furnace, or any other appliance, is the cause..." The other six steps, the four beeps and the single chirp are all present and in order, and nothing banned is added (no "silence it and open the windows").

**W12. The personal detail comes back.**
> "On the first of every month I pull my furnace filter and look at it, with my coffee." (line 18)
> "...when you're done, the filter's easy to reach on the first of the month." (line 207)

The second is a callback rather than a retelling. The SKILL allows the device twice, but the persona profile says "at most one per script", and the rubric checks at most once. **Fix:** "...the filter's easy to reach next time you check it." (Library L3 settles the conflict.)

**W13. Unclear or unsupported lines.**
- "The fix is the airflow." (line 14). This is a stray line before the cost, out of the item shape's order (cost, turn, fix). Cut it.
- "Boxes hide a slow leak until it's soaked through the cardboard." (line 199). A leak of what? Name it ("a slow drip from the condensate line") or cut it.
- "One brings fresh air in for the burners, and the other carries the exhaust out." (line 167). Some condensing furnaces have only the exhaust pipe. Say "On most, one brings fresh air in...".
- "Each of these ends with a truck in the driveway" (line 4). It's "each", and the fan setting (item ten) doesn't end in a truck. "Most of these" is safer (SKILL banned list: "any 'every' or 'forever' the script then walks back").
- "the wait can run into days" (line 170). This is supported only by the study's viewer stories (SKILL "The viewer"), not by the brief or the guide. Acceptable with "can", but it's a fact claim.

**W14. Small trims for the long items (no safety step cut).**
- Item five: "That water drains out through the condensate line, a small plastic drain line, and on the way it passes through..." can lose "a small plastic drain line" (the trap's definition already carries it).
- Item six: "Skip anything coarse, because scratches give the dust something to grab." can go.
- Item two: the thermostat-battery aside can shrink to one clause.

**Rule:** SKILL "The item shape in lists": about 150-250 words, "Cut extra steps, repeated warnings and restated points first".

### Library fixes (a rule is missing, unclear or wrong)

**L1. "Let it cool" is missing from the safety defaults.**
The flame sensor sits in the flame, and item six goes from "Turn the gas valve on the furnace to off" straight to "Take the front panel off" with no wait. The rubric checks for "let it cool", but `hvac-scripts/SKILL.md` "Safety" default 1 says only power off, proved off, and the gas valve off. **Proposed:** add to default 1, "for burner work, let the burners and the area around them cool before touching anything (no time figure; until it's cool to the touch)". R24's filter item shows a related habit (thermostat down and wait before cutting power); the pack could note it for filter changes too.

**L2. How to prove the power off isn't said, and the tester has no price.**
"Prove it's off with that tester" (line 109) doesn't say where to hold it, or to check the tester on a live outlet first. SKILL "Safety" default 1 says "checked with a non-contact tester" without the method. "The standard kit" says anything beyond the kit "gets its typical price range", but `price-guide.md` has no non-contact voltage tester row, so the writer could only say "inexpensive". **Proposed:** add the two-line method (try it on a working outlet, then hold it to the furnace's power cord or the wires at the switch box) and a price row (`price-guide.md` §5), researched and re-checked as the guide's other rows were.

**L3. The personal detail's limit disagrees in three places.**
- `personas/roger-the-hvac-guy.md`: "at most one per script".
- `hvac-scripts/SKILL.md` "Voice": "At most twice per video".
- This rubric: at most once.

**Proposed:** one rule, stated in the profile ("one detail, said once; a later callback counts as the second use"), with the SKILL pointing to it.

**L4. The opening's timing isn't in the handover checklist.**
The SKILL gives "about 45 seconds" for the opening's six jobs and "item one by about 30 seconds" for a list, but "Before handing over" checks only "the fix or product named by about 15 seconds". The writer met the 45 and missed the 30. **Proposed:** add "in a list, 'Number one' within about 75 spoken words" to the checklist.

**L5. The scanner's H21 net misses the split-sentence reframe.**
The scanner's H21 net missed "doesn't need replacing at all. / It needs cleaning." (machine count 0). **Proposed:** a judgment-tier pattern for "doesn't need X ... It needs Y" and "isn't X ... It's Y" across a sentence break, so the hand count has a floor.

**L6. "But" and "you" have no measurable floor.**
"Much more" "but" was met at the minimum (one per item), and the pack gives no "you" density. The reference runs about 38 "you" per 1,000 words; this script runs 21. **Proposed for `PROPOSALS.md` (evidence: this run):** a guide figure, such as at least one belief turn per item plus turning bridges on at least a third of the item changes, and a "you" floor taken from the study's real-person winners (to be measured, not guessed).

**L7. Phone numbers have no voice rule.**
"call 911" is in digits. `workflow.md` §4 covers prices, years, units and codes, but not phone numbers. **Proposed:** "emergency numbers as said: nine-one-one". This only matters if the voice test shows a misread.

**L8. The channel menu skips 7.**
Turn 1 lists 1-6 and then 8. `core/channels.md` on this branch has no row 7 (the electrical channel is on its own branch). This is harmless, but the VA may ask. Renumber, or note the gap in the menu, when the branches merge.

## 4. What the script does better than the reference

**It keeps the villain on the price, not on motives.**
- Script: "That's a lot of money to wipe off a rod, because a lot of the time that sensor doesn't need replacing at all." / "A replacement quote over a burnt-out igniter is a number I'd never sign."
- Reference: "they'll smile the whole way there" / "they wait by the phone for the breakdown to arrive".

**It treats the heat exchanger and the carbon monoxide alarm safely.**
- Script: "A real crack is serious. It can let carbon monoxide into your house, and I'd never tell you to shrug it off. But a few words spoken in your basement aren't proof..." / "If a tech red-tags the furnace, meaning he's marked it unsafe to run, don't run it while you wait for that second opinion. And if your carbon monoxide alarm ever goes off, the quote stops mattering." Then the full alarm drill.
- Reference: "The cracked heat exchanger they'll try to red tag off a photo on a phone": the red tag framed as a sales trick, with no alarm steps.

**It gives the honest out without a sneer.**
- Script: "Leave the igniter itself to a tech you trust, because it's fragile and it has to match your furnace." / "This is the best reason I know for a yearly inspection by a tech you trust."

**Its safety sits inside the step, with named triggers.**
- Script: "Then, before the power goes back on, fill the trap back up with water. That water is a seal." / "If that breaker trips again the minute you reset it, stop there. That's a call." / "leave a cracked or pulled-apart pipe alone, because a leak there is exhaust, and that's a same-day call."

**Its machine sounds and the clock are concrete.**
- Script: "It's cold, the house is quiet, and the furnace isn't making a sound. No hum, no click, nothing." / "The hardest bill to pay is the one for flipping a switch, and on a Saturday night it can cost one and a half to three times what the same visit costs on a Tuesday."

**Its numbers are easy to follow.**
- Script: one figure per item at most, and none in the opening.
- Reference: "somewhere around 10 or $20 a pound ... 40, 70, even $90 a pound, and the whole recharge runs you 100 to $400" in one breath.

**It argues both sides where viewers split.**
- Script: "Now, there's a fair case for leaving it on. The air gets filtered more, and the temperature can feel more even from room to room. But in winter..."

**Its ending is clean.**
- Script: "Leave me a comment with the year your furnace went in, and which of these eleven you caught in your own house. I read every one." Nothing comes after it.
- Reference: after its comment ask come subscribe, a next-video tease and "Keep your cool and I'll see you in the next one."

## 5. Top five changes, ranked

1. **Fix the two false bridges** (W1, W2, W3). Make "Those first four are all about air" true, by swapping items 2 and 4 or rewording to "Three of those first four". Replace "The next three are parts somebody gets paid to replace" with a price fact ("where a small repair can turn into a big quote"). That also removes the repeated "paid to mention" and the near-motive.
2. **Make the start simpler and stronger** (W5, W6). Put the pain in strong words in the first line, and cut the opening from 114 to about 70 words so "Number one" lands by about 30 seconds.
3. **Make the viewer feel it all the way through** (W7, W8, W9). Open items five and ten on the scene. Give items one and six a real belief-then-"but" turn, and turn two or three bridges with "but". End two or three items on the habit and its bill, so the title's feeling comes back in new words.
4. **Close the safety gaps** (W11, L1, L2). Add "or any other appliance" to the alarm's step 6. Add a cool-down before the flame sensor comes out. Have the pack say how to prove the power off with the tester, and give the tester a price row.
5. **Make the audit honest and trim the long items** (W4, W10, W12-W14, L5). Rewrite the second reframe and correct the audit's count. Cut "one more visit" once and drop the second first-of-the-month mention. Trim items five and six toward 250 words without touching a safety step. Re-run the audit from group A.
