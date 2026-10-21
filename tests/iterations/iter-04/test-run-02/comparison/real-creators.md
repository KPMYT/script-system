# TEST: our script vs four real creators (iter-04, test run 02)

Our script: `tests/iterations/iter-04/test-run-02/script.txt`, "15 Plumbing Mistakes Quietly Costing You THOUSANDS" (Roger the Pipe Guy, faceless AI voice, 3,000 words).
Real creators (verbatim labelled scripts in `plumbing-scripts/references/models/`):

| Code | Video | Length | Words | Type |
|---|---|---|---|---|
| **G2L** | Got2Learn, R09 "10 Reasons Why You'd FAIL a Plumbing Inspection!" (7.79M, 63.96x) | 7:36 | 1,247 | mistakes list |
| **RW** | Roger Wakefield, R04 "Don't Buy a New Water Heater Until You Watch This!" (207k, 39.66x) | 9:13 | 1,575 | head-to-head verdict |
| **SC** | Silver Cymbal, R06 "Sneaky Reason LED Bulbs are Dying Faster than Advertised" (1.33M, 18.77x) | 3:29 | 747 | hidden cause |
| **ARW** | Arrow Pest Service, R20 "ROACHES EVERYWHERE-Simple Hack Kills Them All!" (2.60M, 9.58x) | 22:36 | 2,754 | single-product fix (pest parallel) |

Analyst run 2026-10-21. Read-only on the library; this file is the only output.

**Method and limits.** Counts per 1,000 words were made by script on the narration only (labels and timestamps stripped); they are blunt keyword counts, spot-checked by hand. G2L's captions have no punctuation, so its sentence length and question count can't be measured. Our script has no audio, so its timings are estimates at Roger's own measured pace (138 wpm on the hits, 153 on recent uploads; `studies/plumbing/comparison/01-own-channels.md`); at 153 wpm it runs about 19:36. ARW's numbers include on-camera crosstalk (about 29% of its words). **[FACE]** marks anything that depends on a face, a real person or footage and won't transfer to a faceless AI voice.

---

## 1. The numbers side by side

| Measure | OURS | G2L | RW | SC | ARW |
|---|---|---|---|---|---|
| Words a minute | ~153 (est.) | 164 | 171 | 214 | 122 (vacuum stretch ~65) |
| Words per sentence (avg) | 14.0 (50 of 215 over 20 words; max 39) | n/a (run-ons) | 14.6 | 17.5 | 5.9 (crosstalk) |
| First answer | ~0:08 (line 2) | 0:13 | 0:58 | 0:36 | 0:00 cause; bait at 2:04 |
| Words before item one | 125 (~0:49) | 39 | 141 | ~100 | ~313 |
| Typical item | 187 words, ~73 s (range 141-293) | ~110 words, ~40 s | ~90 words, ~35 s | ~30 s blocks | 42-449 words |
| "You/your" per 1k | 20.7 | 26.9 | 52.5 | 34.6 | 41.7 |
| "I/me/my" per 1k | 4.3 | 1.6 | 22.1 | 1.3 | 22.3 |
| Contractions per 1k | 32.3 | 23.7 | 41.7 | 18.6 | 61.0 |
| Questions to the viewer per 1k | **0** (3 "?" are lines to ask a contractor) | n/a | 5.7 | 6.7 | 11.5 |
| "But" pivots per 1k | 1.0 | 2.4 | 7.0 | 20.0 | 1.1 |
| Dollar amounts per 1k | 8.3 (25 amounts) | 0 | 4.4 | 0 | ~0.4 ("50 bucks") |
| Damage/fear words per 1k | 7.7 | 11.9 | 2.5 | 8.0 | 0.7 (fear is on screen) |
| CTA words | 63 mid + 39 end + 20 comment | 24 end | 39 end + 20 card | 0 | ~215 over six asks |

**Read (inferred):** ours is the most money-dense and the most measured, but it talks least *to* the viewer and turns least. Zero viewer questions and 1 "But" per 1,000 words against SC's 6.7 and 20: SC's whole engine ("But what exactly does that mean? Does it even matter?") is absent from ours.

---

## 2. Emotions triggered, and how

| Emotion | OURS | G2L | RW | SC | ARW |
|---|---|---|---|---|---|
| Fear of the big bill | Strong, every item: "$5,000 to $20,000 if the line has to be dug up or relined"; "and that's if it's clean water" | none | "save you from making a several thousand mistake" | implied only | "It's not cheap" |
| Dread of hidden damage | Strong: "A root as thin as a hair gets in, catches some paper, gets fed, and grows."; "the water goes into the wall instead of the hose" | Strong: "giving you no visual hint that your pipes is blocked" | weak | Strong: "your bulb will literally self-destruct" | Strong: "the real problem is hiding in areas that you can't see" |
| Emergency dread | "at two in the morning with water coming through the ceiling"; "get everybody out of the house now" | none | none | none | none |
| Disgust | Weak: only the roots opener and "bacon fat turns white in the pan overnight" | none | none | none | Max **[FACE]**: "Look, there's feces up here."; "One almost fell on me."; "an egg capsule that's got 30 to 50 new cockroaches in it" |
| Distrust / betrayal | Mild: "Nobody gets paid for the flood that never happens"; "That word means it'll go down the toilet, and that's all it means." | none | Strong: "here's the math that the salesman won't show you" | Strongest: "things get really shady"; "this single phrase is literally admitting" | mild |
| Anger at price/profit | none | none | "why most plumbers try to charge a whole lot more than they really should" (banned motive) | "the answer, unfortunately, is money" | none |
| Curiosity | "Number seven is the one almost everybody gets backwards." | "here's why" (4:13) | held reveal (0:22, banned tease) | "there is a secret you want to be aware of" | "change everything you thought you knew" (banned tease) |
| Rule-fear / judgment | "you can pay twice" | Core: "for an inspector this is an automatic fail" ("fail" x8) | "a hidden cost of ownership" | none | none |
| Relief / permission | "That's still a homeowner job, and still a cheap part."; "most of them take a flashlight and five minutes" | "yes it would still work but…"; "there are no problems" (small holes) | "it's a fantastic product" (for the right house) | "it is very unlikely that that bulb will die sooner" | "Listen, anybody can do this." |
| Pride / thrift credited | Best of the five: "That's being careful with money, and there's nothing wrong with that." | "A lot of people will make this mistake when doing their own plumbing" | "we flush our own water heater now because of what you show us" (story, banned) | none | "This is how you do it." |
| Protectiveness | "Older folks and little kids burn faster than that."; "if anybody in the house says they smell it, believe them." | none | "If you have a large family" | none | "yes, it's safe for pets. when it's used according to the label" |
| Belonging / warmth | "My own drains get a look the first Saturday of every month, with my coffee" | none | "I believe an educated customer is the best customer." | "most of us have never noticed it" | **[FACE]** "I love doing this with you, too, baby girl." (1.3K-like comment on the bond) |
| Regret arithmetic | none | none | "Think about how much $20 a month would have saved me over 25 years." | "last 6 to 8 months" vs "up to 21 years" | none |
| Satisfaction | none named | none | none | none | **[FACE]** "It just shreds them up to pieces. There's nothing left." |

**How the creators trigger it (inferred):** each has **one dominant emotion repeated with the same trigger**: G2L the inspector's fail, SC the betrayal by the label, RW the sales-pitch math, ARW disgust plus warmth. Ours spreads eight emotions evenly across fifteen items, each item starting from zero. The emotions study found the hits work the same way: "The pain is named in the first 15 seconds… relief comes *repeatedly*" (`05-emotions.md` §2). Ours does the relief; it lacks the repeated single trigger.

---

## 3. Pacing

- **First payoff.** Ours is the fastest real answer: line 2 names the fix and its price ("A camera down the sewer line would've found those roots years earlier for a couple hundred bucks"). G2L reaches item one sooner (0:13 against our ~0:49), because our opening also carries a villain line, tenure and a three-item promise block.
- **Item length.** Ours runs about 73 s per item, nearly double G2L's ~40 s and RW's ~35 s. The extra is procedure: #2 has a 5-step flapper swap, #5 a 7-step anode check ("Shut the cold water to the tank, open a hot faucet to let the pressure off, and drain a few gallons."). G2L gives the check in one line: "check your toilet's instructions for these measurements."
- **Sentence length.** Ours averages 14.0 words, close to RW's 14.6, and mixes well ("A leaking tank can't be fixed. It gets replaced."). But 50 sentences run over 20 words, e.g. the 39-word "If it won't budge, leave the cheater bar in the toolbox and have it replaced on a weekday, on your schedule, instead of at two in the morning with water coming through the ceiling."
- **Energy rises (ours):** the opening; #3 ("If you do only one thing from this video, do this one."); #7 ("I get why people reach for the jug."); #15 ("get everybody out of the house now"). **Dip:** #8 to #14 (about 10:25 to 18:00) are seven items of the same shape (name, mechanism, price, steps) and five of them open on a bare header. The only forward line in that stretch is "The next one is a cheap part standing between your washer and a flooded laundry room." (~15:00).
- **Creators:** G2L is flat by design, with the peak in its longest item (#7, 210 words, "permanent damage"). RW rises at 1:41 ("the math"), at the verdict ("So, what's the verdict?", 4:26, 48% through) and at the quoted scare at 7:06 ("Oh my god, this is going to cost you 10 or 12 grand"), and dips into stories (4:34 to 6:42) and an aside to plumbers (7:59). SC peaks at 0:27 to 0:34 ("shady", "self-destruct") and again at 3:00 ("money"). ARW's peaks are footage **[FACE]** (11:08 to 14:03, roaches off the ceiling, with no instruction for about 3 minutes).

---

## 4. Language

| | OURS | G2L | RW | SC | ARW |
|---|---|---|---|---|---|
| Register | Plain and exact: "the rubber seal at the bottom of the tank that lifts when you flush" | Technical code-speak: "sanitary tee", "standpipe", "long sweep 90", rarely glossed | Talky trade: "cold water sandwich", "plug-andplay", "Guys" (x4) | Plain consumer, with hype: "literally" (x3), "self-destruct" (x2) | Slang and catchphrase: "game changer" (x5), "Let's go" (x9), "Boom" (x5), "Aca La Vista, baby" |
| Strong verbs | "lets go", "seize", "splits", "pours", "swells, crumbles and grows mold" | "siphon out", "fail" | "cutting through", "shines" | "self-destruct", "fight against each other", "cheapen" | "Suck them up", "shreds them", "knock them out" |
| Repetition for emphasis | Cross-reference instead: "the same roots from number one"; "back to number two"; no refrain | Refrain: "automatic fail" (x4) | Doubled opening: "Don't buy a new water heater. Don't buy a new water heater until you watch this." | Keyword drumbeat: "enclosed" (x12) | "Always read the label… Always read the label. The label's the law." |
| Questions | None to the viewer | "here's why" stands in | "Why is there a huge difference? Well, …" | "Does it even matter? Well, …" | "You know why? Because…" |
| You vs I | Mostly imperatives ("Find yours this weekend."); "I" only 13 times | "you'd fail" | "I love it. I really do." | "you'll catch the phrase" | "I'm telling you" (x4) |

**Read:** the "you" gap is partly our style, since imperatives hide the "you" ("Take the lid off the tank"). The real gaps are the questions, the refrain, and "I" lines that carry an opinion.

---

## 5. Structure

| | Opening | Body | Ending |
|---|---|---|---|
| **OURS** | Scene and answer ("That toilet pulled up off the floor…"), the price ladder, a villain line, tenure, then three named promises ("Number three decides whether a leak means a mop or a flooded basement.") | 15 items, each name, mechanism, sign, price, steps, call-a-pro trigger; ordered by system (sewer, toilet, shutoff, outdoor, heater x2, drains x4, pressure, washer, bill, contractor, gas) | Book line, comment question, "I read every one." |
| **G2L** | Greeting **[banned]**, count, stake, "so here we go" | 10 items, rule, number, reason, verdict; simple ones first, venting in the middle | "that's it 10 points", comment, thumbs-up, thanks |
| **RW** | Title said twice, the stakes, a choice question, villain, held reveal **[banned]**, payoff split by audience | 6 factors alternating for and against, the verdict at 48%, who-buys-which, the held reveal paid at 73% | Mission line, subscribe, tease, card |
| **SC** | Trust ("one of the greatest inventions"), betrayal ("shady"), the warning named at 0:38 | The viewer walks their own fixtures; the maker's page as proof; when it doesn't matter; the fix | The fix restated (a recap for us); no CTA |
| **ARW** | Hidden cause in sentence one, tease **[banned]**, footage **[FACE]** | Bait recipe, then the "another level" escalation (vacuum, flush, spray, regulator, bait) | Recap with "guaranteed" **[banned]**, thanks, "God bless" |

**Gap:** every creator's body has an *argument shape*: G2L builds to a verdict, RW alternates toward a verdict, SC walks to a reveal, ARW climbs a ladder. Ours is a catalogue grouped by system. Its only links are three cross-references ("Go back to number one.").

---

## 6. Transitions

| Type | OURS (14 joins) | Creators |
|---|---|---|
| Bare numbered header | 7 of 14 (#6, 8, 9, 10, 11, 13, 14) | G2L varies the header itself: "the second reason why you'd fail an inspection would be"; "violation number four is" |
| Forward line naming the next value | "Number two is a leak you've probably heard at night without knowing what it was."; "The next one is a cheap part standing between your washer and a flooded laundry room." | ARW: "In just a minute, I'm going to show you exactly where to put it" |
| Close-and-open pair | "That one protects a wall. The next one protects your water heater." | RW: "Let's get the painful part out of the way." |
| Season or time hook | "The next one's about the weather, and this is the time of year for it." | none |
| Callback to a promise | "Now the one I said almost everybody gets backwards."; "This is the one I said I'd never let you touch." | RW: "Now, I told you if you'd hang around…" (paid late) |
| Back from the CTA | "Now, about that sound in the night." (good: the ask holds the open loop) | none mid-video |
| **Question bridge** | **none** | SC: "What about these types of fixtures?"; "But what about these other fixtures…"; RW: "Why is there a huge difference?" |
| **Contrast pivot** | rare: "The catch is the valve itself."; "Gas is different." | RW: "But there's a downside people don't talk about"; SC: "But there is a secret you want to be aware of." |
| Escalation | none | ARW: "let's take it to another level"; "Now, one more thing I want to add" |

---

## 7. Personality

- **OURS (low, at the edges):** opening tenure ("In 45 years I've watched all fifteen of these turn small problems into big bills"), verdicts ("I'd put the money toward the next heater instead."), empathy ("I get why people reach for the jug."), one routine (the first Saturday), dry lines ("leave the cheater bar in the toolbox"; "A good plumber answers those without blinking."). About 8 personality lines in 3,000 words, none between #10 and #15.
- **G2L (near zero):** "so here we go". The personality is the hands and the footage **[FACE]**.
- **RW (high, throughout):** opinions ("I love it. I really do."), verdicts ("a luxury performance upgrade"), stories **[banned: customer stories / first-person history]** ("I got called to a doctor's house one day"), mock dialogue ("Dude, you're taking money out of our pocket." / "Really? Just to flush a water heater?"), a mission ("an educated customer is the best customer").
- **SC (low, in tone):** "things get really shady", "in a perfect world", "unfortunately". Personality as judgment, not self.
- **ARW (max)** **[FACE]**: family banter ("cornbread"), faith ("God bless"), the church honey, a catchphrase. It is liked for the people, which can't transfer: "your bond with your daughter" (1.3K likes).

**Transferable:** judgment and opinion said as "I" (RW's "luxury performance upgrade", SC's "shady" toned down). Not transferable: stories, banter, humour (also barred by the portfolio "no jokes" decision).

---

## 8. The villain

| | Who | Exact framing |
|---|---|---|
| OURS | The trade's silence, once; then scattered (labels, chemistry, bad contractors, age) | "Nobody gets paid for the flood that never happens, so nobody calls to remind you to look."; "That word means it'll go down the toilet, and that's all it means."; "plumbing is one of the trades where bad work hides." |
| G2L | The inspector (an authority, not an enemy) | "your inspector will automatically make you fail an inspection and get you to modify it" |
| RW | The salesman and plumbers' motives | "cutting through all the sales pitches"; "the math that the salesman won't show you"; "Because they really don't want to do it." (motive: banned for us) |
| SC | The manufacturers and their fine print | "they really overbuilt those bulbs… fast forward to today and things get really shady"; "these manufacturers kind of get away with this"; "as they cheapen the products over the years" |
| ARW | The pest, hidden; and the homeowner's own failed spray | "They love the fridge."; "They've been trying to spray that in the fridge." |

**Gap:** SC's villain returns three times (0:16, 2:32, 3:00) and is proven by the label itself. Ours names the villain once and drops it. Our rules allow a villain to return as a price or a silence. "Flushable" (#8) is our SC-shaped move, but it's confined to one item.

---

## 9. Money pain

- **OURS (densest, 25 amounts):** catastrophe ladders: "$150 to $300 for the camera, $300 to $1,000 to cut the roots out, and $5,000 to $20,000"; "a flooded basement commonly runs anywhere from $2,000 to $7,000"; "$500 to $2,000 to repair it, and the water cleanup comes on top of that"; paying twice: "once for the bad job and again to tear it out and redo it to code. And insurance may not cover it."; the cheap side: "about $15", "$4 to $10". What's missing: no *running* cost or arithmetic. "That can add tens of dollars a month to the bill" is never multiplied out.
- **G2L:** no money at all. The cost is rework: "would need to be modified".
- **RW:** payback arithmetic: "If you save $20 a month, but spend an extra three, four grand… over 12 years just to break even"; the service call "can cost a few hundred"; the long-run tally ("over 25 years… Enough to pay for a new water heater one time"). His one exact price drew the top dispute ("$500 not 3k", 191 likes).
- **SC:** money as the maker's motive only ("the answer, unfortunately, is money"). The waste is implied by "up to 21 years" against "6 to 8 months".
- **ARW:** cheapness as ease: "We went down to the Dollar General store"; "It's not cheap" (no range).

**Read:** ours wins on money, but by stacking. Judge note: 13 figures on 11 items "number load 4/10". RW lands harder with fewer figures because he does the sum *for* the viewer. That arithmetic is the move.

---

## 10. Other pain points

| Pain | OURS | Creators |
|---|---|---|
| Making it worse | "they can be stuck, or break inside when you force them"; "it can splash back in your face" | G2L: "would need to be modified" |
| Being taken advantage of | "Hiring the cheapest bid without checking the license" | RW: "Are you sure you want to spend 10 or 12 grand for a water heater?" (mock quote); SC: "most of us have never noticed it" |
| Family safety | "Older folks and little kids burn faster than that." | ARW: "safe for pets"; "Any aerosols could cause a fire." |
| Old houses | "old" x23: "old galvanized and cast-iron drain pipe has been thinning from the inside for decades" | SC: "Those original bulbs from 20 years ago" (quality decline) |
| Away or asleep | "it pours for as long as nobody's home to hear it"; "two in the morning" | none |
| Aging body | barely: "it takes a big socket and some muscle" | none |
| Embarrassment | none (sewage is a symptom only) | ARW: an infested kitchen on camera **[FACE]** |
| Failed attempts | "the same clog coming back every few months no matter how many times it gets cleared" (#1 only) | ARW: the homeowner's fridge spray; RW: "nobody does that anyway" |
| Wasted time | none | G2L: redoing the work |

Ours covers more pain points than any creator. It never dwells, though: each gets one line and moves on.

---

## 11. CTAs

| | Where | Words | Wording |
|---|---|---|---|
| OURS | Mid (after #1, ~2:35) + end + comment line | 63 + 39 + 20 | "are on pages 56 to 57 of my book… You can get it from the link in the description and the QR code on screen. Now, about that sound in the night." / "Tell me how old your house is and which of these fifteen you've caught yourself doing. I read every one." |
| G2L | End | 24 | "give this video a thumbs up if you learned something from it" |
| RW | End | 39 + 20 | "If you appreciate getting the real unfiltered truth without a sales pitch, do me a favor and hit that subscribe button." |
| SC | none | 0 | (ends on the fix) |
| ARW | Six times | ~215 | "Put a comment down… if you have your own homemade roach bait"; "It's got over 1.7 million views." |

Ours is the best-built CTA here: tied to item one, it holds an open loop through the ask, and it ends on a question the viewer answers from their own house. ARW's recipe-sharing comment ask is the one creator CTA worth borrowing as a *shape*: it invites viewers to share their own fix.

---

## (a) What the real creators do that ours lacks, ranked by likely impact

1. **Questions as the engine** (SC 6.7, RW 5.7 per 1k; ours 0). "But what exactly does that mean? Does it even matter? Well, …" Every block opens on the viewer's own doubt and answers it at once. This is the cheapest retention device in the set, and it transfers fully.
2. **One dominant emotion with a recurring trigger.** G2L's "automatic fail" (x4), SC's "enclosed" (x12) and betrayal. Ours resets the emotion every item; the title's stake ("Quietly Costing You THOUSANDS") never returns as a through-line.
3. **The turn inside each item** (SC 20, RW 7 "But" per 1k; ours 1). "it's true, they are more efficient… But here's the math". Our items run one way: problem, price, fix.
4. **Shorter items** (~35-40 s against our ~73 s). The procedure carries the length: "Unhook the old flapper, hook on the new one, and leave just a little slack in the chain."
5. **Opinion in the first person** (RW 22 "I" per 1k, ours 4.3). "A tankless water heater is a luxury performance upgrade." Ours has verdicts, but only about four of them.
6. **Doing the sum for the viewer.** RW's "over 12 years just to break even". Ours gives ranges and leaves the sum to the viewer.
7. **A returning villain with proof the viewer can see.** SC: "this single phrase is literally admitting". Ours: "flushable", once.
8. **Disgust or sensory shock.** ARW's footage **[FACE]** doesn't transfer, but a spoken picture does ("an egg capsule that's got 30 to 50 new cockroaches in it"). The judge also noted our script dropped the original's "build a rope" and "wax poured into a drinking straw".

## (b) What our script does better

- **Money:** concrete ranges on 11 of 15 items ("$150 to $300 for the camera"), where G2L and SC have none, and no single exact price to dispute (unlike RW's "three grand").
- **Promise discipline:** named stakes paid on time ("a mop or a flooded basement", paid at ~4:05), where RW holds his promise to 73% behind "stay till the very end".
- **Safety as care:** sourced ("Those are the Consumer Product Safety Commission's numbers"), with real steps ("call 911 and the gas company, and don't assume somebody else already called"). ARW jokes about eating bait ("You want to eat some of this, Mackenzie?").
- **Respect for the viewer's thrift:** "That's being careful with money, and there's nothing wrong with that." RW and SC have nothing like it.
- **Checks the viewer can run:** six of them (food colouring, the meter, the paper towel, the gauge, the hoses, the licence lookup), against SC's one walk-round.
- **Honest scope:** "Sometimes the low price is the smart move."
- **The CTA:** tied to content, returns to an open loop, ends on a specific question.
- **Nothing that needs a face:** no pointing, no stories, no motives.

## (c) Rule-ready suggestions for the plumbing script pack

Each line gives a creator line to show the move. Never copy the wording. Check each against `HANDOFF.md` §3 before adopting, and log it in `PROPOSALS.md` where it touches a locked rule.

1. **Viewer questions:** at least one question in the viewer's voice every two items, answered in the next sentence (move: SC "Does it even matter? Well, …").
2. **One pivot per item:** each item turns once on "but", from the belief or easy fix to the truth (move: RW "And it's true, they are more efficient… But here's the math").
3. **A stake thread:** the title's stake recurs at the close of at least every third item, the same stake in different words each time, so it isn't a tic (move: G2L "you'd fail automatically" / "an automatic fail").
4. **The villain returns:** the opening's villain (price, silence or label) comes back at least twice more, each time with proof the viewer can check (move: SC 0:16, 2:32, 3:00, ending on "they've put this phrase on the bulb").
5. **One "I" verdict per item** of no more than 15 words: a judgment, not a story (move: RW "A tankless water heater is a luxury performance upgrade.").
6. **Item budget in long lists:** with 12 or more items, keep the median under about 130 words. Give the one decisive step and what "done" looks like, and leave the full procedure to the book (move: G2L "check your toilet's instructions for these measurements").
7. **Do the sum once:** at least one item turns a monthly leak or saving into a year or a decade figure (move: RW "over 12 years just to break even").
8. **No more than two bare headers in a row:** the third join gets a forward line, a question or a pivot (move: SC "But there is a secret you want to be aware of.").
9. **One spoken sensory picture** (disgust or dread) on every gross or hidden-damage item, checkable and never inflated (move: ARW "an egg capsule that's got 30 to 50 new cockroaches in it", spoken, without the footage).
10. **The viewer's-fix comment ask:** rotate in a comment question that asks for the viewer's own method, not only their house (move: ARW "if you have your own homemade roach bait that you like to use").

**Don't transfer [FACE / banned]:** ARW's crosstalk, footage disgust and family bond; G2L's "as we could see here" and his on-camera hands; RW's customer and personal stories, the trade's motives ("they really don't want to do it") and the held reveal; SC's "as we zoom in" and "this one on my ceiling"; humour of any kind (the portfolio-wide "no jokes" decision). Our "QR code on screen" depends on an edit overlay the channel controls, so it's fine as long as the edit carries it.
