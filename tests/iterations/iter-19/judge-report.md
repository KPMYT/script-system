# TEST (iter-19): judge report, four plumbing scripts on P22

**Judged:** `tests/iterations/iter-19/run-{roger,mark,vintage,werner}/script.txt`, against the P22 rules (the operator's words, as given in the judging brief and on the four persona pages), the published videos on the same titles, and iter-16's versions (Mark, Vintage, Werner).

**Facts given to the judge (machine runs, 2026-11-15):**
- `plumbing-scripts/check.py`: PASS on all four. INFO lines: openings of 133 / 124 / 154 / 143 words (about 47 / 41 / 49 / 47 seconds at the channel's speed); lengths of 2,483 / 2,552 / 2,678 / 2,642 words (14.6 / 14.1 / 14.1 / 14.6 minutes).
- `tools/verify_output.py`: no audit evidence block in any output (expected for this run). Item word counts: Roger 438 / 372 / 406 / 287 / 843; Mark 1,461 / 490 / 477; Werner 253 / 216 / 288 / 208 / 272 / 501 / 278 / 228 / 190. For Vintage it found 7 items, not 8, because it misses the lowercase "number eight". It still times everything at 150 words a minute.

Scored by reading. The checker's pass is not counted as evidence of quality.

---

## 1. Scores

1 is poor and 10 is excellent. "Pub" means the published video's captions. "i16" means iter-16, the same brief written on the old rules. The Vintage Pipefitter has no book, so (g) is n/a there.

| Row | Roger i19 | Roger pub | Mark i19 | Mark pub | Mark i16 | Vintage i19 | Vintage pub | Vintage i16 | Werner i19 | Werner pub | Werner i16 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (a) hook pull | 7 | 5 | 6 | 4 | 5 | 6 | 5 | 5 | 6 | 5 | 5 |
| (b) reason to stay / loops | 7 | 4 | 5 | 3 | 4 | 6 | 5 | 5 | 6 | 4 | 4 |
| (c) flow | 7 | 7 | 5 | 6 | 6 | 7 | 6 | 6 | 6 | 6 | 6 |
| (d) one real tradesman | 8 | 8 | 6 | 6 | 6 | 7 | 7 | 7 | 8 | 7 | 8 |
| (e) emotion and stakes | 7 | 7 | 6 | 6 | 6 | 7 | 7 | 6 | 6 | 6 | 6 |
| (f) DIY confidence | 9 | 5 | 9 | 8 | 7 | 7 | 6 | 5 | 9 | 4 | 5 |
| (g) book line | 7 | 2 | 7 | 3 | 3 | n/a | n/a | n/a | 7 | 3 | 3 |
| (h) ending | 6 | 5 | 5 | 4 | 4 | 5 | 4 | 6 | 8 | 6 | 5 |
| **Average** | **7.3** | **5.4** | **6.1** | **5.0** | **5.1** | **6.4** | **5.7** | **5.7** | **7.0** | **5.1** | **5.3** |

**The averages:**
- iter-19 averages 6.7 across the four scripts, against 5.3 for the published videos and 5.4 for iter-16's three.
- By row, across the four iter-19 scripts: hook 6.3, reason to stay 6.0, flow 6.3, voice 7.3, emotion 6.5, DIY confidence 8.5, book 7.0, ending 6.0.

**What moved and what did not:**
- **The rows that rose** are the ones P22 wrote rules for: DIY confidence (f), the book (g), and hook and loops (a, b).
- **Flow, voice and emotion stayed flat.**
- **Endings rose least.** The new briefs still carry the old rules' closing tally (see section 3).

---

## 2. Per script

### Roger the Pipe Guy: "You've Been Using Hydrogen Peroxide WRONG (It Stopped Working)" (2,483 words, 14.6 min)

**The hook, in full (everything before item one):**
> If you poured hydrogen peroxide into your toilet and the ring is still there, peroxide isn't the problem. It works. You heard a cup of it would clean the bowl overnight, so you tipped one in before bed. In the morning the gray ring was right where you left it. But the way most of us buy it, keep it and pour it, that peroxide never had a chance. There are five mistakes that kill it, and we'll take them one at a time. The fifth explains why some rings won't budge whatever you pour on them, and once you know it, you won't waste another bottle. Nobody prints any of this on the label. And people haul good toilets to the curb over a stain a two dollar bottle would have lifted.

**What works:**
- **The best P22 hook of the four.**
  - The point comes first ("peroxide isn't the problem. It works.") and the failed try is lived ("tipped one in before bed").
  - The count is clean ("five mistakes").
  - There is one reason to stay, and mistake five pays it: the fingernail test, then citric acid.
  - The villain closes the hook as two plain facts.
- **Against the published hook, the two retention leaks are gone.**
  - The published second sentence gave mistake one away: "The bottle under your sink probably doesn't."
  - At 0:33 it said "Everything here is yours to do. The one call in this video is a clog". That is the 0:30 to 0:45 drop in `analysis-retention.md`.
  - Neither is here.
- **The bridges are real loops,** and each is different:
  - "But even a fresh bottle will let you down if you pour it the way most people do."
  - "That gets the peroxide onto the ring. The next mistake is what most people do in the first few minutes after."
  - "Now back to the bottle, because the fourth mistake is about where you keep it."
- **His voice holds:**
  - "Keeping a bottle on hand is good thrift, and I'd never knock it." (He credits the habit before correcting it.)
  - "I hate seeing that money spent on a bowl that was never broken."
  - "In forty-five years" appears once, backing a verdict.
- **DIY first.** A stiff valve gets the gentle way: "If it's stiff, don't force it... Leave it be, flush once, and scoop the bowl low". The only call is the main line, with its trigger.
- **The book line is the fix the retention data asked for.** It has no fix or page numbers, sits once at 52%, and comes right after the flapper aside it relates to.

**What fails P22:**
- **Rule 5, no recap.**
  > "So match the fix to the problem. Slime, smell and the stains they leave get peroxide. A hard, rough ring gets citric acid on its own night. A clog gets the plunger, after the tub test."

  This is a run-back, sitting between the last tip and tonight's one thing. The writer's notes admit it was kept because the brief's "Where it ends" asked for it.
- **Rule 1, the promise is paid and then buried.** Mistake five delivers the promise in about 300 words (the fingernail test and the citric acid). Then it carries on for another 500 words of off-title material: mixing, the clog, the tub test, the main-line call and the plunger. Item five is 843 words, twice any other. The payoff is the climax, and here it is followed by a second, different topic.
- **Rule 1, the payoff is announced in a stock way.** "Number five is the one I promised you" is the same signal Mark and Vintage use (see section 3).
- **Rule 4, the book line comes in cold, and its match is generic.**
  > "My book, One Hundred Old-House Fixes That Save You Thousands, goes deeper into toilets and the tank. It's for older houses and the people who'd rather fix them."

  Nothing leads into it from the step. "Toilets and the tank" is a weak match for a peroxide-and-stains video, though far better than the published "Fixes 37 through 42, printed pages 48 through 51". It is not the operator's own shape ("I go into more of this in my book... it's perfect for X and Y").
- **Rule 5, tonight's thing belongs to mistake one,** not the last tip: "Pull that brown bottle out and splash a little in the sink." It is fine as an action. But the last tip's own test, the fingernail, would have closed the loop the hook opened.

**The 3 fixes:**
1. Cut the "So match the fix to the problem" recap. End mistake five on its own test, with tonight's thing coming out of it.
2. Move the clog and main-line block out of the payoff: either earlier as its own beat, or trimmed to the danger line alone. Mistake five should end on the ring that finally makes sense.
3. Lead into the book line from the flapper step, in his words ("I go into more of the tank in my book..."), and drop the cold "My book, [title]," opener.

---

### Mark Silverbridge: "These 3 Powders Will Save You HOURS of Scrubbing Toilets, Tubs and Sinks" (2,552 words, 14.1 min)

**The hook, in full:**
> Scrubbing that ring out of your toilet every weekend will not keep it gone. The base of your faucet has a white crust that will not shift. There is a gray line round the tub that comes back every few weeks. The store sells a spray for each of these. Not one label tells you what the stain actually is. Three cheap powders from the grocery store will do that scrubbing for you, and each one does a job the other two cannot. You want a fix that works tonight, not another wasted bottle or a scratched tub. I will give you all three, with the dose and the wait for each. And the last powder beats the one stain bleach keeps losing to.

**What works:**
- **The reveal is held,** the operator's own example rule.
  - The published video named all three in its third sentence ("Citric acid, baking soda, and borax. About $20 for all three.").
  - Here the opening says only "three cheap powders", and each is named at its own number.
  - Number two even holds the name inside the item: "Before I name it, look at that gray line round your tub."
- **The loops after each reveal are good:**
  - "it does two jobs in this video. The second job may keep a showerhead off your shopping list, so hold on for it."
  - "this is the one you will reach for most"
  - "the same bowl of water does the sink and the grout"
- **The villain is quiet and right:** "Nobody in the showroom asks whether the old one just needed its rim jets cleared."
- **No plumber anywhere,** no contractions, and "forty years" said once with a verdict.
- **The book line matches its step,** the weak flush right after the rim jets: "goes further into the weak flush, with what each fix saves you."

**What fails P22:**
- **Rule 1, the promise is the thinnest thing in the script.** The hook's one promise is "the last powder beats the one stain bleach keeps losing to". The payoff, the grout, gets three sentences:
  > "Dip a cloth in it and run it along the grout lines behind the faucet. Let it sit there a while. Then wipe it, and rinse it with clean water."

  "A while" is not a dose or a wait. That breaks the hook's own "with the dose and the wait for each". It never says why borax reaches the pores when bleach cannot. And item three opens on the sink, not the grout, so the promised stain arrives second inside its own item.
- **Flow: the balance is lopsided.**
  - Item one (citric acid) is 1,461 words, 57% of the script. The promised item three is 477 (19%).
  - The length came from building out item one: the rim jets, the showroom, pumice, the tank tablets and the flapper. The payoff did not grow.
- **Voice: British English in an American tradesman's mouth.** "round" is used for "around" nine times ("a gray line round the tub", "wrap it round the base", "tie the top of the bag round the shower arm", "stir it round"), plus "Go and run a fingernail". iter-16 had the same habit.
- **Voice: the page's feeling table is read out.** "You want a fix that works tonight, not another wasted bottle or a scratched tub" is the persona table's row ("a cheap fix that works tonight | another wasted bottle, a scratched fixture") almost word for word. "I will give you all three, with the dose and the wait for each" is a line that only ticks a box.
- **Rule 5, a tally before the ending, and tonight's thing from item one.**
  > "All three powders together come to about 20 dollars. The weekly scrubbing comes down to a few minutes of wiping... One small thing for tonight. Go and run a fingernail across that toilet ring."

  The tally is a recap the page bans, and the brief asked for it. Tonight's thing points back to item one, so the video ends on the toilet rather than on the promise it paid last.
- **Length: right on the floor.** 2,552 words against a 2,534 floor, 18 words over.

**The 3 fixes:**
1. Build item three around the promise: lead with the grout, give the soak a real time, explain why borax gets into the pores, and give "done" a look. The brief has these points; they went to item one instead.
2. Cut the tally. Take tonight's thing from item three: the grout behind the faucet, tonight, with the sink soak.
3. Use American English ("around", "go run") and drop the lines copied from the feeling table and the dose-and-wait filler line.

---

### The Vintage Pipefitter: "8 Things You Should NEVER Pour Down Your Drains" (2,678 words, 14.1 min)

**The hook, in full:**
> What you pour down your drains every week is building a clog you can't see, and it's growing in your pipes right now. Think about your kitchen sink. It ran fine on Sunday, and on Thursday night it quits, with gray water sitting in the basin. That clog didn't start on Thursday. It's been filling for months, one ordinary habit at a time. Getting a kitchen line cleared out runs about 150 to 400 dollars, depending on where you live, and nobody wants a bill like that for something they did without knowing. So what went down your kitchen sink this week? There are eight things that should never go down your drains, and the swap for almost every one of them costs next to nothing. A couple of them you were probably taught were good for your pipes. And the last one hands you the one thing that does belong down a drain.

**What works:**
- **The list is held.** The published hook ran three items down ("Number six is the one everybody swears is safe and it's boiling water"). iter-16's hook put the main-line call in. This one names no item and no plumber.
- **Two loops, both paid:** "taught were good for your pipes" (boiling water) and "the one thing that does belong down a drain" (washing soda).
- **The best item-to-item hand-offs of the four:**
  - "When a sink does slow down, most folks reach for the same thing, and that's number two."
  - "Then the grease from number one comes along and glues them in place."
- **The old-ways persona is alive:** "The old kitchens always kept a can of drippings by the stove, and they had it right." "Here's the old painter's way." He credits the doubter: "Now, some of you have poured that stuff for years, and your pipes are fine. Maybe they are."
- **The facts are tidier than the published video's.** The published one had "$2,000 to $5,000" and an invented "$13,000" total. Here it is "several hundred dollars to a couple of thousand", and there is no total.

**What fails P22:**
- **Rule 1, no failed try in the hook.** The scene is there (the Thursday sink) but not what they tried. The page's own example is "what people pour, buy or try first", and the jug belongs here. The hook also runs 49 seconds, over the 45.
- **Rule 1, the promise is paid by an add-on, not by the last tip.** Number eight is bleach and mixing. The promised "one thing that does belong down a drain" comes after it as a ninth beat: "Now, I promised you the one thing that does belong down a drain. It's washing soda." The page says "the last tip must pay it".
- **Rule 2, a call outside the three dangers:** "If that drain won't clear with the cleaner sitting in it, that's a time to have somebody come out, and you tell them exactly what you poured." That is not gas, live wiring or the main line. The brief asked for it, and the writer flagged it in the notes. The checker did not catch it.
- **Rule 2, the body keeps pointing at the phone.** There are four separate prices for someone coming out:
  - hydro jetting, "350 to 800 dollars"
  - "a service call of a few hundred dollars"
  - "Having someone come out to unjam a disposal runs about 75 to 175 dollars"
  - the main line

  The villain is allowed, but here the price usually stands in for the fix. In the disposal item, the fix ("switch it off and leave it off while you look") stops before the hex-key reset any DIY viewer would expect.
- **Old-rule language in the body.** Item seven ends "That's where this job stops being yours." That is the exact limit-line wording P22 took out of openings, and it reads as a sign-off.
- **Rule 5, a run-back, and tonight's thing from item one:**
  > "Every one of these habits costs you an old can, a bucket and a strainer, and most of that's already under your sink. Add a little trash can with a lid by the toilet, and that's the whole kit. So here's your one small thing for tonight. The next time there's bacon fat in the pan..."

  The page says "never a run-back over the items". And "the next time there's bacon fat" is not tonight.
- **Voice: four signature asides in one script.** "Now here's the thing", "I'll tell you", "Between you and me" and "here's the part people skip" are each used once, which is allowed. Together they read like the page's list being ticked off.
- **Length: right on the floor.** 2,678 against 2,660. The notes say the first draft was 13.8 minutes and lines were added until it passed.

**The 3 fixes:**
1. Make number eight pay the promise: bleach out, washing soda in, as one item. Or reorder so washing soda is the last numbered item. End that item with tonight's thing (a pitcher of washing soda tonight, or the bacon can, said as tonight).
2. Put the failed try in the hook (the jug), and take the chemical-cleaner "somebody come out" line back to the operator. Either it joins the danger list or it gets a DIY path.
3. Cut the run-back kit list and "That's where this job stops being yours". Use at most two asides.

---

### Werner Finkbeiner: "Why Your Sink Stopper Gets Stuck: The $5 Grease Every German Plumber Carries" (2,642 words, 14.6 min)

**The hook, in full:**
> Your bathroom sink stopper is not stuck because the sink is old. It is stuck because of something on its stem, and you have never seen that stem, because nobody ever told you to lift the stopper out and look.
>
> You push the rod behind the faucet, and the stopper stays down. You pull it, and the stopper stays up. So you jiggle the rod, you push harder, and one day you just leave it open.
>
> Nobody mentions that the cure is a small tube of grease that costs about five dollars. That silence is the expensive part.
>
> There are nine numbered things in this video. The ninth takes five minutes once a year, and it keeps this from ever coming back.
>
> One honest word first. Grease does not mend a part that has cracked or worn through. That needs a new part.

**What works:**
- **The reveal is held as the title words it.**
  - The published first sentence named "silicone grease, about $5, the one in every German plumber's van" and put a plumber's $100 visit in the hook.
  - Here it is "a small tube of grease" until number five ("Silicone plumber's grease"). No plumber appears in the opening.
- **The villain line is the best single line of the four:** "That silence is the expensive part."
- **The promise is paid in full** by Wartung: "Five minutes a year, and the hair never gets time to become a rope."
- **The ending is the only one that does exactly what P22 says:** the last tip, tonight's one thing ("lift the stopper straight out, and look at the stem"), an easy question ("what was on your stem?"), then "I read every one."
- **The voice is right for him:**
  - verb-forward and understated ("The pipe is fine. The pipe was never the problem.")
  - the German claims are hedged and come from the brief, with two German words, each explained
  - one personal detail (the spring check)
  - no contractions
- **DIY confidence improved on the brief.** The brief said a rusted drain body "is a call". The script makes it "the one bigger job on this sink" with "do not force a nut that has rusted solid". That is P22 rule 2 applied correctly.
- **The book block follows the spec:** the mentor line word for word, no numbers, 59 words, and a line back into the video. The published video named "Chapter 3" and mentioned the book twice; iter-16 named chapter six twice.

**What fails P22:**
- **Rule 2 in spirit, and the retention data: a limit line in the last seconds of the hook.** "One honest word first. Grease does not mend a part that has cracked or worn through. That needs a new part."
  - It sits right where the Roger data found a 10 to 18 point drop on all five videos ("the line saying what's yours and where it becomes a call").
  - It deflates the promise made one sentence earlier. Number eight then says it all again.
  - It came from the brief's "Honest limit, early", written for the old rules.
- **Rule 3, the loop after the reveal comes late.** The grease is named at the top of number five. The next loop ("That one tube goes onto four small parts of your sink in the next two numbers. And the last of them brings back a click") arrives about 270 words later, after the shelf trap and the German habit. The operator said "instantly".
- **Rule 1, the count is clerical.** "There are nine numbered things in this video" counts causes, a product, two repairs, a limit and a check as "things". Four of the nine are causes with no action.
  - The viewer gets no fix until about 6 minutes in (hook plus items 1 to 4 is about 1,110 words).
  - "Count the tips" means counting what they get to do. This reads like a table of contents.
- **Flow: the book block splits a pair.** It sits between number six (the lift rod, apart and back together) and number seven (the push button, apart and back together). It is placed after the item it fits, as the rule says, but it breaks the one place where the two repairs read as a set.
- **Voice: an echo of the page's own example.** "You did not pay for a repair. You paid for knowing where to look" copies the persona page's illustration ("You did not pay for the repair. You paid for knowing which screw."). Here it is also slightly off: the viewer paid nothing.

**The 3 fixes:**
1. Cut "One honest word first..." from the hook. Number eight already covers it, where it belongs.
2. Put the four-uses loop in the sentence right after "Silicone plumber's grease. A small tube...". Move the shelf trap and the German habit after it.
3. Count what they do, not what they learn. For example: "four places a stopper hides its trouble, and two repairs that take twenty minutes", or "nine things to check and fix". Either way, the first hands-on action should come before the six-minute mark.

---

## 3. Across all four

### What got better (P22 is working)
- **No plumber in any opening.** Every published video and two of iter-16's three had one.
- **The reveal is held in all four,** including the two titles that hold something back (Mark's powders, Werner's grease). All four published openings gave something away.
- **Book lines carry no numbers and come once.** On Roger, this is the line that cost 37% of the viewers still watching.
- **A count and one reason to stay in every hook, and the last tip pays it** (fully in Roger and Werner, thinly in Mark, by an add-on in Vintage).
- **The calls in the body follow the rules:** main line only for Roger and Vintage, none for Mark and Werner. The exception is Vintage's chemical-cleaner line.
- **The hooks are 41 to 49 seconds,** close to the 45 target.

### What is turning into a template
- **"Reason to stay": one sentence at the end of the count, always the same build.**
  - Roger: "The fifth explains why some rings won't budge..."
  - Mark: "And the last powder beats the one stain bleach keeps losing to."
  - Vintage: "And the last one hands you the one thing that does belong down a drain."
  - Werner: "The ninth takes five minutes once a year, and it keeps this from ever coming back."

  The sentence is "The last/fifth/ninth [does something for you]", and it is the last or second-to-last line of the hook every time. Three of four pay it off with the same announcement: "Number five is the one I promised you" (Roger), "Number three is the one I promised at the start" (Mark), "Now, I promised you the one thing" (Vintage). One viewer watching two of these channels would hear the machinery.
- **Hook skeleton.** All four run point, scene, villain, count, last-tip promise, in nearly the same order. Roger alone moves the villain to the end, and it reads best for it. The page says "in the order that suits the title", but the bullet order is being copied as a sequence.
- **Book lines: the same three-part skeleton.**
  - Roger: "My book, [title], goes deeper into toilets and the tank. It's for [who]. It's at the link in the description and the QR code on screen."
  - Mark: "My book, [title], goes further into the weak flush, with what each fix saves you. It is at the link in the description and the QR code on screen."

  Both open cold on "My book," with no lead-in from the step. Neither uses the operator's own shape ("I go into more of this in my book... it's perfect for X and Y"). Werner's is fixed by design, so it does not count. With two channels already on the same skeleton, by the next batch it will be a stock line.
- **The feeling table is pasted in.**
  - Mark's hook has "You want a fix that works tonight, not another wasted bottle or a scratched tub" (the table row).
  - Vintage's hook has "nobody wants a bill like that for something they did without knowing" (the table's "a bill they caused without knowing").
  - The Vintage notes say this line was added to lengthen the script.
- **Endings: a tally, then tonight's thing from item one.** The tally appears in Roger, Mark and Vintage, and two of those take tonight's thing from item one. Every brief has a "payoff" or "Where it ends" line written for the old rules that asks for this. The writers followed the brief, and the page's "no recap" lost. Werner, whose brief payoff is only "the visit he didn't need; the tube in the drawer", is the one clean ending.

### Briefs written for the old rules are steering against P22
The iter-19 briefs for Mark, Vintage and Werner are "copied unchanged from iter-16". They still say:
- "Honest limit, early" (Werner): this became the hook's limit line.
- a chemical-cleaner stop sign (Vintage): this became a non-danger call.
- "A closing tally may add..." (Mark) and the payoff and kit list (Vintage): these became recaps.
- "chapter 6", "page 36" book matches: the writers correctly ignored these.

All four pages say "The brief wins on facts", and the writers stretched "facts" to cover placement and structure. Three of the four P22 failures trace back to the brief, not to the page.

### Length: all four are on the 14-minute floor

| | Floor | Script | Above floor |
|---|---|---|---|
| Roger | 2,380 | 2,483 | +4.3% |
| Mark | 2,534 | 2,552 | +0.7% |
| Vintage | 2,660 | 2,678 | +0.7% |
| Werner | 2,534 | 2,642 | +4.3% |

The page says "Fourteen is the floor, never the target", but all four landed within about 4% of it. Why:
1. **The briefs are sized for the old videos.** They were written from published videos of 11:00 (Vintage), 12:40 (Mark) and 13:13 (Roger), and none was enlarged for a 14-minute floor. iter-16's versions were 12.3 to 13.7 minutes.
2. **The checker makes the floor a FAIL,** so writers stop adding once it passes. The Vintage notes show it: "length 2,629 words (13.8 min)" FAIL, then additions to clear it.
3. **The escape hatch is never used.** The page says "If the brief cannot reach 14 minutes, say so and ask for more points." No writer did. The Vintage writer added the feeling-table line and other small additions. The Mark writer built out item one.
4. **The opening limit and the floor pull against each other.** The Vintage notes say: "Trimming it further would drop below 14 minutes".

**Padding:** not blatant, but present in two scripts: Mark's lopsided item one (57% of the script), and Vintage's additions (the hook's want/fear line, the extra snake-price line, four asides). None of the four has the material for 18 to 25 minutes. The way to get there is a bigger brief, not a longer write.

One caution on speeds, to measure rather than act on. Words per minute worked out from the published captions came out under the page figures: Roger about 161 against 170, Werner about 166 against 181, Vintage about 181 against 190, Mark 180 against 181. Captions write prices as digits, which lowers the word count, so this is only a hint. If Werner's real speed is near 166, his 14-minute floor is too high by about 200 words.

---

## 4. Library fixes suggested, with the evidence

These are for the main session or the operator. Anything that touches a locked decision goes to `PROPOSALS.md`. None is made here.

### Rule wording on the four persona pages
1. **"The brief wins on facts"** should become **"The brief wins on facts (doses, prices, steps, safety facts); never on what goes in the opening, the order, the calls, the book or the ending."** Evidence: Werner's hook limit line comes from "Honest limit, early"; Vintage's non-danger call; the tallies in Mark and Vintage.
2. **Refresh the briefs for P22 before the next run.** Remove old-rule lines ("honest limit, early", "closing tally", chapter and page book matches). Size each brief for 14 minutes or more of material, with the meat in the last item. Evidence: all three iter-16 briefs, and four for four on the floor.
3. **The reason to stay should say that the last numbered item itself pays it, as its fullest item, and that it is never announced as "the one I promised".** Evidence: Vintage's add-on ninth beat; Mark's three-sentence grout payoff; "the one I promised" in three of four scripts.
4. **Tonight's one thing should grow out of the last tip,** with nothing between the last tip and tonight's thing. Evidence: Roger, Mark and Vintage all put a tally or kit list there, and two of those took tonight's thing from item one.
5. **"After the reveal, open the next loop at once": define "at once"** as the sentence right after the name, before any explanation. Evidence: Werner's loop came about 270 words after the reveal.
6. **"The count" should define what counts:** "count what they will do (fixes, steps, uses), not causes or sections; the first hands-on action by about 2 minutes." Evidence: Werner's "nine numbered things", four of them causes, and no action until about 6 minutes.
7. **Book line: add the operator's own shape as one example among several, and ban the cold opener.** For example: "Lead in from the step you just finished ('I go into more of this in my book...'); never start on 'My book, [title],'; never the same wording on two channels." Evidence: Roger and Mark share a skeleton word for word.
8. **The feeling table: add "The table is for you to aim with. Never say its words."** Evidence: Mark's and Vintage's hooks.
9. **Mark's page: add "American English: 'around', never 'round'; 'go do', never 'go and do'".** Evidence: nine uses of "round" in iter-19 and the same habit in iter-16.
10. **Vintage's page: cap the signature asides at two per script.** Evidence: four in iter-19.
11. **A question for the operator (PROPOSALS, not a fix):** is "a drain with chemical cleaner in it that won't clear" a danger call? The page's safety block makes it dangerous (no plunging), but the call list leaves it out. The writer had to choose, and chose the brief.
12. **Length: add "If your draft lands within about 5% of the floor, check whether the brief ran out, and say so in the notes."** Evidence: four for four within about 4%, and no writer asked for more points.

### The checker (`plumbing-scripts/check.py`)
1. **Flag a limit line in the opening** ("honest word", "does not mend", "stops being yours", "one call", "yours to do", "need a new part"). Werner passed with one.
2. **Flag non-danger calls:** "have somebody come out", "someone come out", "hand it to someone", "that one is a call" outside a main-line, gas or wiring context. Vintage passed with "that's a time to have somebody come out".
3. **Flag a recap or tally in the last two paragraphs before the comment ask** ("all three", "together come to", "every one of these", "the whole kit", "match the fix", "so here's how it sorts out"). Roger, Mark and Vintage all passed with one.
4. **Report the reason-to-stay sentence** (the line after the count that names the last or Nth item) and the last item's word share. Warn when the last item is under the item average, or when one item is over 45% of the script. Evidence: Mark at 57% and 19%.
5. **Warn on "the one I promised", "I promised you" and "as promised"** as stock payoff announcers.
6. **Fix the dollar counter in the opening** so it counts "150 to 400 dollars" written out. Vintage was reported as 0.
7. **Fix the count detector.** It read Vintage's count as "one ordinary habit" instead of "eight things".
8. **Warn on Britishisms for the American channels** ("round the", "go and"), Werner excepted.
9. **Report near-floor length as INFO** ("2,552 words, 0.7% over the floor: did the brief run out?"), so the floor reads as a floor, not a target.

### `tools/verify_output.py`
1. **Time it at each channel's speed** (170, 181, 190, 181), not 150. It still reports "item one at 50 to 62 seconds at 150" and "17.8 minutes".
2. **Find lowercase "number eight" and "the last one, number N" as items.** It found 7 items in Vintage's 8.
