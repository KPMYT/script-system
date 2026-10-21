---
name: plumbing-scripts
description: Script rules for the operator's plumbing channels (Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter, and any future channel in this niche). Use whenever a plumbing script is written, rewritten or reviewed, or a plumbing title and brief arrive for scripting. Sets the villain, the opening by video type, "point then promise", the structure of each video type, CTAs, length, voice, proof, money framing, safety and the plumbing scanner checks. Persona, tenure, book and CTA wording come from the channel's persona profile; claims policy, output format and the audit come from the core rules.
---

<!--
DRAFT 2, 2026-10-20; batch 2 in progress from 2026-10-21. NOT IN THE LIBRARY YET. When approved it becomes the skill `plumbing-scripts` (one skill, one SKILL.md,
like `woodworking-scripts`), built by tools/build_skills.py into dist/plumbing-scripts.skill.
Status tags: [DECIDED] the operator has ruled; [APPROVED] the operator said yes to this draft wording (2026-10-20);
[DRAFT: for your yes] written, waiting; [LATER] heading only, written in a later batch.
P3 (concrete forward promises in the plumbing pack) was approved by the operator on 2026-10-20.
Sources: studies/plumbing/comparison/ (04 hooks, 06 titles, 07 body craft, 09 differences, 10 opener teardowns, 11 reasons to stay)
and HANDOFF.md section 3, "Operator decisions, 2026-10-20 (plumbing, after the study)".
-->

# Plumbing scripts

A plumbing video solves one household problem cheaply, or settles one decision, for an older homeowner who would rather not pay for a service call. The winners in this niche (Got2Learn, Roger Wakefield, Silver Cymbal, TheCheapFix, and our own hits) get to the point fast, then give the viewer more reasons to stay by promising specific, priced payoffs, and pay those promises inside the video. This skill copies that shape for channels with no real person on camera.

## What this skill covers

**It owns:** the villain, the opening by video type, "point then promise", the structure of each video type, CTA placement and length, length, voice, proof, money framing, safety and the plumbing scanner checks. Scripts are clean narration only: no edit notes, cues or directions of any kind [DECIDED 2026-10-21].

**It doesn't own:**
- **The persona:** name, tenure, sign-off, any mentor or family detail. These live in the channel's persona profile.
- **The book and CTA wording:** also in the persona profile.
- **The claims policy, output format, voiceover copy and audit:** these live in the core rules.

**Authority:** the core claims policy and offer rules come first, then safety and the title's promise, then the persona profile, then this skill, then the core base rules. The core `workflow.md` runs every script (START, the input gate, the output format).

## Files in this skill [DRAFT: being built in step 2]

| File | What it's for |
|---|---|
| `references/unit-plan-template.md` | The plan to fill in from the title and brief before any prose. |
| `references/voice-samples.md` | Three stretches of real human narration from the real channels' winners: the voice anchor for every script (core `voice-anchoring.md`). |
| `references/excerpts.md` | Real lines grouped by job (the point, promises, money, limits, call-a-pro, comment questions). Lines from our hits and TheCheapFix are marked "structure only". Use for shape and range, never wording. |
| `references/reference-scripts.md` | Complete winning scripts from the real channels (Got2Learn, Silver Cymbal, Roger Wakefield, Arrow), labelled. Read at the planning step for structure and pacing. |
| `references/structure-models.md` | Complete scripts of the biggest AI-voiced plumbing hits (our own and TheCheapFix's), labelled. Structure only: never their voice or wording, and their banned lines are marked. |
| `archive/` | Full transcripts of the four real channels. Calibration only; don't read them while writing. |

Every reference file is under the copy guard: the scanner flags any run of 8 or more words shared with it [DECIDED: the real channels for voice; our hits and TheCheapFix for structure only, 2026-10-21].

## Inputs [APPROVED 2026-10-21]

Plumbing scripts are written from the title and the brief alone; there is no research pack [DECIDED 2026-10-21]. The workflow reads this block at START and won't write until every required input passes.

```inputs
- title | required | the locked title, exactly as approved
- brief | required | the ideation brief for this title; every fact, price, dose and method in the script comes from it
- research-pack | not used | plumbing scripts are written from the brief
- rotation-log | required | the channel's last five ROTATION LOG ENTRY lines, or "none" for a new channel
```

- **The brief is the fact source.** It does the research pack's job: the scanner checks every number in the script against the brief, and the brief wins on safety.
- **No freshness check.** Prices are said as ranges (see "Money framing"), so nothing is re-checked at START.
- **If the brief is missing something the script needs** (the trade's typical price, a dose, a wait time), the run stops with NOT READY and names it. It never invents the fact.

## The viewer [APPROVED 2026-10-21]

The viewer is a 50+ American homeowner, often in an older house and on a careful income, who would rather fix it than pay for a visit. They arrive from the feed, not from a search: they were offered a saving, a fear or a secret. Under the click sits one question: "Can I do this myself without making it worse?"

**What they bring, from the study's comments:**
- **The bill is the pain, not the plumber.** Comments name prices and labour often and the plumber rarely (8 of 506 on our hits). Many viewers like their own plumber, which is why the villain is aimed at the price.
- **They've already tried something.** The jug, the plunger, the fizzing volcano: "I tried an extra large size of Drano. That didn't work." A failed attempt is the strongest opening feeling in the data. Say why it failed in one plain sentence, then give the fix.
- **They have decades of habits.** "Never had a clog in 40 years." Confirm the good habits. When correcting a loved one (baking soda and vinegar), credit their thrift first: about 23 comments defended it against "it's theater."
- **They protect each other.** Safety corrections are among the most-liked comments (4.3K likes on borax not being boric acid). An unsafe line produces the angriest comments a channel gets.
- **They're impatient.** It's the commonest negative feeling in the study: "3:15 is where it starts." (2K likes). Get to the answer.
- **They ask the doing questions.** How much water, is it safe for septic, for plastic pipe, for old cast iron, which pipe do I have. Answer the ones that apply inside the script, at the step where they'd ask.
- **What they thank:** a fast answer, the reason why, a product they can find, steps clear enough to try, and the pride of doing it themselves ("72 years old and looking forward to seeing what else I can do").

**Skill level:**
- Write for beginners to handy homeowners, in plain words. A trade term gets a short explanation the first time ("the P-trap, the U-shaped bend under the sink"), then is used plainly.
- Give the reason behind a step in one sentence; viewers thank the "why" (1.4K likes on Got2Learn). Don't lecture on the cause: "We don't need all that explanation of what causes the clog. Just tell us how to unclog it."
- Never explain what everyone knows (turning off a tap, fetching a bucket).

**The standard kit:**
- Assume the viewer owns a plunger, a bucket, old towels, rubber gloves, a flashlight, an adjustable wrench, pliers, a screwdriver, a measuring cup, and the usual kitchen and laundry products (baking soda, white vinegar, dish soap).
- Anything beyond that (drain snake, closet auger, wet-dry vac, pipe wrench, a specialty product) gets its typical price range and, where one exists, a cheaper alternative or an "optional."

For more depth, see `plumbing-ideation/references/audience.md` (§1 for this viewer, §4 for money language, §7 for safety).

---

## The villain [DECIDED; wording APPROVED]

The villain on every plumbing channel is **the trade**: plumbers as a business, the plumbing industry, and whoever profits from the service call. Never a named company (core claims policy).

**How to use it, from what landed with viewers and what drew disbelief:**
- **Aim it at the price and the silence, not at motives.** "A drain call for that runs about a hundred and fifty dollars" and "nobody in the trade will mention it" land. Claiming to know what plumbers secretly do at home, or that they hide fixes on purpose, drew the most-liked doubt in our data (1.3K likes).
- **Say it as a billing fact.** The trade is paid by the visit, so a five-dollar fix that ends the visits is nobody's business to mention. That's an observation the viewer can check against their own bills.
- **One villain line in the opening, then let the prices carry it.** The trade's typical price at the end of an item ("you just did it for a couple of dollars") does the work for the rest of the video.
- **The store shelf is a second, softer villain:** the jug, the tablet, the marketing on the label. Use it where the fix replaces a product.

## The opening [APPROVED]

Every opening, whatever the video type, does these jobs in about the first 45 seconds. Hooks are not one fixed formula: rotate the order and the shape across a channel's scripts (the rotation log tracks it), use the order for the video type (see "The video types"), or model the opening on one of the reference winner scripts for its shape and beats, never its wording. What can't change is that the point comes first and fast, and nothing on the banned list below appears.

1. **The point in the first sentence.** Name the title's subject and, wherever the title allows, the fix or product itself, by about 15 seconds. Never hold the name back: the two hits that hid the product for five and seven minutes drew the angriest comments in the study.
2. **A question, when it fits.** A question the viewer can answer in their own house ("When did you last lift the lid off your toilet tank?"), answered within about 15 seconds. Never a question the viewer can't check.
3. **The villain line,** as a price or a silence (above).
4. **Honest scope or reassurance,** in one line: what it won't do, or why it's safe ("It won't touch a hair clog." "Nothing here harms a septic tank."). This keeps the title's strongest word honest.
5. **The promise block** (this pack's override of core `retention-mechanics.md` §6, approved as P3). Right after the point, promise two or three specific later payoffs. Each names its item and its stake: "Number six saves you a two-hundred-dollar call." "And the last one is the rule that keeps all of this safe on old pipes." Never a vague tease: the hard-ban list ("stay till the end", "stick with me", "by the end of this video" and the rest) still applies.
6. **The first real tip** by about 45 seconds; in a list, item one by about 30 seconds.

**Never in an opening:** a name or channel intro, a greeting, "today we're going to", a recap of what's coming, a first-person test or demonstration ("I tested", "watch me"), or a tenure number other than the profile's.

**Tenure:** at most once, as the profile's fixed number (Roger 45, Mark 40, Vintage 50) or, when the title states a different one, the title's number (title numbers win), and only where it does a job (credibility right before a verdict or a mistakes list).

## Point then promise [APPROVED]

The competitors give the point first and promise second; our hits did the reverse and made the viewer wait. From now on:

- **Point first.** The first answer (the fix named, the rule stated, the first verdict fact) comes before the first forward promise.
- **Promise straight after.** The promise block follows within about 30 seconds of the first answer.
- **Pay the first promise early.** The first promised item is paid within about five minutes. Nothing promised in the opening is held past the middle of the video, except the safety rule or a second use for the product.
- **Keep one promise open.** After the opening, never go more than about five minutes without a new forward line or a payoff. Use a line that names the next value ("The next one is the reason your tank sweats in July."), the trade's price for what was just done, a question the next item answers, or a check the viewer can run.
- **Every callback has a promise.** A line that says "I promised" or "like I said" must match something the script really promised earlier.
- **A priority flag at the first answer:** "If you do only one thing from this video, do this one." Viewers pointed at that line when it came late.
- **No recaps** at the end [DECIDED].

## Ways to promise more value [APPROVED]

Use two or three per video, and rotate them across a channel's scripts.

- **A numbered item with its money stake:** "Number four saves you a three-hundred-dollar camera inspection."
- **A numbered item with its stake in words:** "Number eight is the step that protects old cast-iron pipe."
- **The escalation ladder:** the cheap fix, then the stronger fix, then the point to call, with the trade's typical price as the top rung. The default for fix videos.
- **The rule that protects everything:** a safety or method rule promised early, paid straight after the first fix or as the last item.
- **A second use for the same product,** or "while you're under there".
- **A check the viewer can run:** lift the lid, the food-colouring test, the fizz test. No first-person test claim needed.
- **A running cost tally** across the video (what the trade would have charged so far).
- **The trade's price at the end of each item.**
- **A problem the viewer didn't know they had,** promised and then shown.
- **A myth flag:** "Number three is the one everybody gets backwards."

## The video types [APPROVED 2026-10-21]

Pick the type from the title. Each type has its own opening order and item shape. These are the most common types, not the only ones (operator, 2026-10-21). The models are full labelled scripts for the planning step: RS = `references/reference-scripts.md` (real channels: structure and voice), SM = `references/structure-models.md` (our hits and TheCheapFix: structure only). Never copy their wording.

| Type | Title shape | Opening, in order | First tip by | Item shape | Models |
|---|---|---|---|---|---|
| **Single-product fix** | "1 Cup of This…", "Pour X Into Y Tonight" | Product and what it does → reassurance → the doubt answered ("Too simple? It works on…") → what the jug or the visit costs → what it won't do → the promise block | 40-60 s | Dose, method, wait time, what you'll see, when it won't work | RS7 (Arrow, rats); SM6 (Roger, 1 cup) |
| **N things about one product** | "N Things Plumbers Don't Want You to Know About X" | The product in the viewer's house and its price → what the trade charges for the same jobs → "nobody will mention it" → the belief it flips → the count, with one money item and one safety item → one rule | 45-90 s | A scene, what the trade charges, the method with amounts, the payoff | SM1 (Vintage, peroxide); SM5 (TheCheapFix, peroxide); RS2 for list pacing |
| **Never-do list** | "N Things You Should NEVER…" | A habit doing hidden damage → the avoidable cost → the trade bills for the result → the count → one numbered item with its stake | 30-45 s | The habit, why it does damage, what to do instead | SM3 (Roger, never pour) |
| **Mistakes list** | "N Mistakes That…", "DO NOT Install X Until…" | A symptom question or neglect → the cost in hundreds or thousands → one credibility line → the count → one numbered stake | 15-30 s | The mistake, what it costs, the right way | SM4 (Mark, water heater) |
| **Head-to-head verdict** | "X vs Y vs Z: A [tenure]-Year Plumber's Verdict" | The failed attempt or the moment of choice → the contenders with prices → everyone disagrees, the pitch sells the dear one → "each one gets a job" → one concrete extra | 45-60 s | Each contender: what it's for, what it's not for, one line of verdict; then which to use for which job | RS4 (Wakefield, tank vs tankless); SM2 (Mark, borax) |
| **Banned / code explainer** | "Here's Why X Is NOT ALLOWED Anymore" | The why-question, or the viewer finding the fixture → the rule, scoped ("most codes", never "illegal") → the reason and one real danger, in proportion → "if yours works, you may not need to change it" → the fixes | about 20 s | Rule, reason, verdict, the fixes from cheapest | RS1 (Got2Learn, S-traps) |
| **How-to / correct way** | "The CORRECT Way to X", "How to X (Before It…)" | The task and the number-one mistake, or the myth flipped → "you can do this" → the step count and the step that decides it → when not to do it | 15-45 s | One step, the reason, the mistake to avoid | RS3 (Got2Learn, unsoldering) |
| **Product swap** | "X Is Expensive. Use THIS Instead!" | The pro's price → the usual DIY option and its catch → the popular shortcut, judged fairly → the swap named, with its price and where not to use it | about 60 s | The swap, the price, the job it fits | RS5 (Silver Cymbal, spray foam) |
| **Hidden cause** | "Why Your X Keeps Y" | The thing the viewer trusts → what it's really doing → the hidden cause in one line → "what that means for you", answered at once | 30-45 s | Cause, how to check, the fix | RS6 (Silver Cymbal, LED bulbs) |
| **Seasonal or emergency** | "Do This Before the First Freeze" | The clock and the crisis → "put the phone down" with the after-hours price → "probably nothing's broken" → the cause in one line → the fixes with what the viewer already owns | 30-45 s | The step, why now, what to watch for | none yet: build from the opening jobs |

A title that promises tests ("I Tested 5 Drain Cleaners") is written as tests and results from the brief, never as "I tested" [DECIDED 2026-10-21].

**A title that fits none of the ten:** build the opening from the six jobs in "The opening", in the order the closest type uses, and pick the item shape from the table that best suits the content. Note the title in the plan as "new type". When the same new shape comes up on three or more videos, it's proposed for this table, and added only with the operator's yes.

## CTAs [APPROVED 2026-10-21]

- **Roger the Pipe Guy and Mark Silverbridge:** back to the short CTAs their hits used. One mid-video ask, straight after the first real payoff, in about 20-60 words: one sentence for the ask, then straight back into the next item. At the end, a one-line reminder [DECIDED 2026-10-21]. Wording comes from the persona profile.
- **The Vintage Pipefitter:** no mid-video CTA. At the end, a one-line subscribe ask, worded in the persona profile [DECIDED 2026-10-21]. Something fuller (an email CTA) will be decided later.
- **Never a long QR walkthrough,** never the same pitch twice in one video, and never a production label read aloud.

## The ending [APPROVED 2026-10-21]

Every plumbing channel ends the way Bertha's Clean Home does: the video's last line is a real attempt to get a comment. This overrides core `cta-and-endings.md` §4 for plumbing (P5).

After the last item:
1. **The end CTA: a one-line reminder,** in the persona profile's words, on every channel.
2. **The comment line, which is the last line of the video:** one specific question the viewer can answer from their own house, plus one small detail about them, and "I read every one." For example: "Tell me how old your house is and which drain gives you the most grief. I read every one." Never a bare "let me know in the comments", and never the same question two videos running.

There's no fixed last line or sign-off after the comment line [DECIDED 2026-10-21]. No recap, no tease of a future video, and nothing after the comment line.

## Length [DECIDED 2026-10-21]

**At least 12 minutes** of narration on every plumbing script (this pack raises the core 8-minute minimum): 1,800 spoken words at 150 a minute, or at the profile's words per minute. **12 to 20 minutes is the sweet spot.** Inside that, the value decides: words per item depend on the item [DECIDED].

- **Never pad to reach a length.** Cut repetition instead: the same check said twice five minutes apart, or the promise restated, is padding.
- **If the brief can't fill 12 minutes with real value,** the run stops with NOT READY and asks for a fuller brief (more items, more detail). The fix belongs at the ideation stage, not in extra words.
- **For calibration, not as targets:** our hits ran 17 to 21 minutes, and the competitors' median was about 13. The length complaints on our hits were about the wait before the answer and the repetition, not the runtime: TheCheapFix and Arrow ran as long and drew about one length complaint each.

## Voice [APPROVED 2026-10-21]

Our hits sounded more like a person than our recent uploads: 1.5-2 times the first person on all three channels, more "you", and plain routine lines where the recent uploads used crafted metaphor. Even the hits used the least first person of any human-voiced channel in the study (5.3-8.8 per 1,000 words against 15.2-25.1).

- **"You" for every instruction; "I" for opinions, preferences and verdicts.** "Pour it in slowly." "I'd leave the jug on the shelf for old cast iron." Write in contractions, the way people talk.
- **Plain beats clever.** State the fact. At most one picture-phrase per item, and only when it teaches ("a colony of bacteria wearing a glue coat" explains biofilm). Mark's similes rose from 0.3 to 1.7 per 1,000 words in his recent uploads, with nothing to show for it.
- **Honest candor.** Say the limits plainly: "Peroxide does not dissolve rock." "Nothing in plumbing is permanent." These are the lines viewers call honest. Never an invented mishap.
- **Warmth comes from reassurance, not humour.** "You're fine." "Nothing's broken." "There's no shame in calling a pro." No jokes (a portfolio-wide decision).
- **Swearing: none** in plumbing scripts. (The woodworking allowance doesn't carry over; nothing in the plumbing study calls for it.)
- **A persona device only if the profile has one:** a mentor line or a household routine (Vintage's Uncle Ray, Roger's first-Saturday check). At most twice per video, under about 40 words, to teach or warn, never as proof that something works. Its facts (names, ages, places) come from the profile and never change.
- **A phrase is voice once; in the same slot every video, it's a tic.** Vintage used "Nine times out of 10" in 9 of 10 videos. Each stock phrase at most once per video, and rotate what opens an item and what closes the video. (The list of limited phrases comes with "Banned in these scripts".)

## Proof [APPROVED 2026-10-21; tests-and-results line updated per the operator, 2026-10-21]

The clearest difference in the study: the face channels, and Got2Learn filming his own hands, drew no complaints about the footage, while our hits drew about 38 (Mark about 28). Most of that is the camera. But the script made it worse every time it said "I tested", "watch me" or "look at". Proof in these scripts is the kind that survives any footage.

**Use:**
- **The mechanism, in one plain line:** why it works. "Its entire job is to corrode so your tank does not." The best ones are under 15 words.
- **A number from the brief, said as a typical range** rather than one exact price: "somewhere between four hundred and eight hundred dollars for the unit." A source may be named when it helps ("the Department of Energy puts it at…"), but sources and store names don't have to be said [DECIDED].
- **The maker's own warning,** when the brief confirms one: "Kohler, American Standard and Toto all warn against chlorine tablets in their own instructions."
- **A check the viewer runs at home,** with what they'll see either way: the fizz test for old peroxide, food colouring in the tank for a leaking flapper. Only checks the brief confirms really work (food colouring can't find a leak at the toilet's base).
- **The honest limit:** what the fix won't do. "Peroxide does not dissolve rock."
- **Exact amounts, waits and what "done" looks like:** "One cup of washing soda stirred into two or three cups of hot tap water. Leave it six to eight hours." Check the arithmetic of every dose: one hit called two cups "half of a 16-ounce bottle" (it's the whole bottle), and four comments caught it.
- **The typical case, as a general statement:** "Plenty of people replace a toilet when the rim jets only needed cleaning."

**Never:**
- **First-person tests, trials or demonstrations,** even when the title promises tests [DECIDED 2026-10-21]. "I put all three through eight brutal tests" drew "Where is the footage of him doing the tests?" Tests and results are fine when the brief gives them, said without "I": "In pull tests, the push-fit gave way first." "Side by side, the enzyme cleaner took three nights; the jug took fifteen minutes and the clog was back in a week."
- **Anything that needs footage the channel doesn't control:** "watch me", "look at the toilet on the left", "there's a stack of receipts on my bench right now".
- **Customer stories and results:** "I had a homeowner tell me…", "an exterminator quoted a lady three hundred dollars". The claims policy bans customers; say it as the typical case instead.
- **Nameless claimed experience:** "the worst tank we've ever opened".
- **Sweeping claims nobody can check:** "this trick has saved homeowners across America hundreds of dollars".

## Money framing [APPROVED 2026-10-21]

All 15 of our hits set the fix's cost against what the trade charges. In this niche that comparison is the entry ticket, not an extra. The weak spot is a single low product price: viewers check it on Amazon while they watch. Service-call ranges drew almost no disputes.

**1. The comparison comes early,** within the first two minutes, usually as the villain line.
- Did it: "That little brown bottle sitting in your medicine cabinet cost about $1 at most drug stores. And yet the average homeowner pays a plumber $300 or more every single year…" (TheCheapFix, 2.18M views; first sentence).
- Didn't: Vintage's enzyme video names no product and no price at the point; the per-night cost arrives more than five minutes later.

**2. Every price is a range from the brief,** never one exact figure.
- Drew fire: "usually around eight to twelve dollars a bottle" brought "This guy prices are from 1924, Amazon - BIO-CLEAN $79.95." "A dollar or two" for peroxide brought "Peroxide is now priced close to 5.00 since COVID." TheCheapFix's "$1 a bottle" brought "Maybe 30 years ago!" (48 likes).
- Survived: "An after hours no heat call lands somewhere between $200 and $400 in most of the country, more at night or on a weekend" (Mark). No disputes.
- Write: "A flapper runs about five to fifteen dollars. Having someone fit it usually starts around a hundred and fifty."

**3. The cost per use, when a product lasts,** checked against the dose.
- Did it: "That box is about $4 to $5 and it gives you the better part of a dozen treatments. Call it 50 cents a pop." (Roger, hit).
- Check: "a box lasts two years of monthly treatments" has to survive the arithmetic. A 55-ounce box at half a cup a month doesn't make two years.

**4. Rotate the money devices** across a channel's scripts, so no two videos count money the same way:
- **Three prices side by side:** "50 cents versus 20 bucks versus 300. That's the whole game." (Roger, hit).
- **The trade's price at the end of each item:** "This is exactly what professional kitchen cleaning services charge $40 a visit for. You just did it for cents." (TheCheapFix, hit).
- **A running total,** closed at the last item: "Total spent, $2. Total saved off the new toilet, right around 500." (Vintage, hit).
- **Payback arithmetic for big purchases** (water heaters, softeners, tankless): "If you save $20 a month, but spend an extra three, four grand to install it, it's going to take you over 12 years just to break even." (Roger Wakefield, hit).

**5. Say it when the cheap or popular option loses.** "That is a 30-year payback period. That is not great." (Mark, his biggest hit). A verdict that says no is the one viewers trust, and "the one situation where paying somebody is the cheap option" (Mark) keeps the villain honest.

**6. A money figure in the title is paid at its item,** with what was avoided spelled out. TheCheapFix's "#4 Saves $300" lands at item four as the new toilet nobody has to buy: "you absolutely do not need to pay a plumber $300 to $500 to replace your fixture."

**7. Brand names are optional** [DECIDED: sources and store names aren't required]. Name a widely sold product only when it is the answer and the brief confirms it's on sale now. Viewers acted on the one brand our hits named: "I ordered some Arm & Hammer super washing soda… The water is draining for the first time in months!" (304 likes).

**Never:**
- **A guaranteed saving** (claims policy). Not "this saves you $300", but "this can save you the $300 visit".
- **The trade's motives** (see "The villain"). Not "that's how he pays his mortgage", but "a drain call starts around a hundred and fifty".
- **A total stated as certain** when it depends on the viewer's house. Not "this is a $5 fix", but "if it's the flapper, that's a five-to-fifteen-dollar fix".

## Safety [APPROVED 2026-10-21; the brief always wins]

The facts and methods come from the brief, and **the brief always wins** [DECIDED 2026-10-21]. There's no separate fact bank: contradictions between one video and another are acceptable [DECIDED].

**Defaults, only where the brief is silent.** These five drew the angriest comments in the study (about 18 on boiling water and 17 on washing soda that set hard: "Thanks to this video I had to hire a plumber!"), so the script uses the safe version unless the brief says otherwise:
1. **Hot tap water,** not boiling water, for drains, toilets and plastic pipe.
2. **Washing soda dissolved first** in hot tap water, not poured in dry.
3. **One cleaner at a time;** never bleach with ammonia, vinegar or any acid, or peroxide with vinegar. Peroxide means the 3% drugstore bottle.
4. **Nothing added to a drain that already has a chemical drain cleaner in it,** plunging included. It can splash back.
5. **Gas lines and live wiring are a call, not a project.** Before any water-heater job, the power or the gas goes off, in one line.

**How safety sounds:**
- **One short line inside the step where the risk is,** with the reason, in proportion. "It will put you on the floor" (chlorine gas) drew no complaints; vague danger drew "This is nothing but a scare tactic video."
- **The call-a-pro line names its trigger:** "Two drains backing up at once is the main line. That's a call." Never the vague "if it's outside your comfort zone", and never a long list of stop signs.

## Banned in these scripts [APPROVED 2026-10-21]

**Never:**
- **A name or channel intro,** a greeting, "today we're going to", or "this channel is for…" (all three channels used the same channel-promise line in their recent uploads).
- **Vague teases:** "stay till the end", "stick with me", "by the end of this video" and the rest of the core hard-ban list. Concrete, named promises are the plumbing exception (P3).
- **A recap** at the end.
- **First-person tests and demonstrations:** "I tested", "I tried", "my results", "watch me".
- **Pointing at the screen:** "look at the one on the left", "as you can see", "right here", "look at this".
- **Customer stories and results, the trade's motives,** and anything negative stated as fact about a named company.
- **Edit notes, cues, labels or directions** of any kind.
- **The recent template's stock lines,** which showed no lift and made the three channels sound alike: "not a scam, just economics" (and "no conspiracy", "just arithmetic"); "this channel is for / exists / is all about"; "grab it now or later"; "your wallet (or pipes) will thank you"; "they just don't volunteer it"; "if you're finding this helpful"; "let's continue"; "common problems you might run into".
- **Hype that got mocked:** "horror movie", "brutal tests", and any "every" or "forever" the script then walks back.
- **Competitors' catchphrases and sign-offs.**
- **Copying 8 or more words in a row** from a reference file. The copy guard flags it.

**At most once per video.** A phrase is voice once; in the same slot every video it's a tic. "Nine times out of 10" is fine [DECIDED], and it's on this list with the others: "between you and me", "ask me how I know", "here's the part nobody tells you", "I'll be straight with you", "that's the whole trick", "in your pocket", "which brings us", "hold that thought", "the big one", "the real kicker", "quick thing", "no shame in", "full stop", "trust me".

## Scanner rules for this niche [APPROVED 2026-10-21]

The scanner (core `script-scanner.py`) reads this block. `ban` lines are fix-on-sight; `once` lines fail on the second use in a script (scanner support built 2026-10-21, test 20). There are no checks for boiling water or dry washing soda: the brief wins on safety, and the operator said "dont even flag them" (2026-10-21).

```scanner
ban-regex: \bI(?:'ve| have)? (?:tested|tried|ran (?:a |the |some |my )?tests?)\b | first-person test claim
ban-regex: \bmy (?:own )?(?:test|tests|testing|results)\b | first-person test claim
ban: watch me | first-person demonstration
ban: as you can see | pointing at the screen
ban: right here | pointing at the screen
ban: look at this | pointing at the screen
ban-regex: \blook at the \w+(?: \w+)? on the (?:left|right)\b | pointing at the screen
ban-regex: \bnot a scam\b|\bisn'?t the scam\b|\bjust (?:plain )?(?:economics|arithmetic)\b|\bno conspiracy\b | template stock line: the economics aside
ban-regex: \bthis channel (?:is for|exists|is all about)\b | template stock line: channel promise
ban: grab it now or later | template stock line
ban-regex: \byour (?:wallet|pipes) will thank you\b | template stock line
ban-regex: \b(?:just )?(?:do not|don'?t) volunteer it\b | template stock line
ban-regex: \bif (?:you'?re|you are) finding this helpful\b|\bif this is helping\b | template stock line
ban-regex: \blet'?s (?:continue|keep going)\b | template stock line
ban: common problems you might run into | template stock line
ban: horror movie | hype that got mocked
ban-regex: \bbrutal tests?\b | hype that got mocked
once-regex: \bnine (?:times )?out of (?:10|ten)\b | nine times out of 10
once: between you and me
once: ask me how I know
once-regex: \bhere'?s the part (?:people skip|nobody tells you)\b | here's the part nobody tells you
once-regex: \bI'?ll be (?:straight|square|honest) with you\b | I'll be straight with you
once-regex: \bthat'?s the whole (?:trick|method|job|game)\b | that's the whole trick
once: in your pocket
once-regex: \bwhich (?:brings us|leaves)\b | which brings us
once-regex: \bhold that thought\b|\bput a pin in\b | hold that thought
once: the big one
once: the real kicker
once-regex: \bquick (?:thing|pause|one)\b | quick thing
once: no shame in
once: full stop
once: trust me
```

## Before handing over [APPROVED 2026-10-21]

Check that:
- the point comes in the first sentence, with the fix or product named by about 15 seconds
- the opening follows the video type's order (or the closest type's, for a new type), with no intro, greeting, tease or recap
- the promise block follows the first answer; every promise is paid, the first within about five minutes, and no stretch runs past about five minutes without a forward line or a payoff
- the tenure appears at most once, as the profile's number or the title's
- every number, price, dose and wait traces to the brief; prices are ranges; the dose arithmetic holds
- the fix's cost meets the trade's price within the first two minutes
- there's no "I tested", no pointing at the screen, no customer story and no motive
- safety follows the brief, with the five defaults only where it's silent
- the CTAs follow the persona profile: the mid-video ask after the first payoff (Roger and Mark), and a one-line end reminder on every channel
- the video ends on the comment line (a specific question and "I read every one"), with nothing after it
- each stock phrase appears at most once, and the opening shape and money device differ from the rotation log
- the script runs at least 12 minutes (12 to 20 is the sweet spot), with nothing padded
