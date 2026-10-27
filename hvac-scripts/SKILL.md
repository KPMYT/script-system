---
name: hvac-scripts
description: "Script rules for the operator's HVAC channel, Roger the HVAC Guy (and any future channel in this niche). Use whenever an HVAC script is written, rewritten or reviewed, or an HVAC title and brief arrive for scripting: furnaces, AC, heat pumps, filters, thermostats, condensate drains, drafts, the heating and cooling bill, space heaters, outage heat. Sets the villain, the opening by video type, emotion all the way through, \"point then promise\", the structure of each video type and the item shape, CTAs, length, voice, proof, money framing, safety and the HVAC scanner checks. Persona, tenure and CTA wording come from the channel's persona profile; claims policy, output format and the audit come from the core rules. To write a script, type START: the script-writer skill runs it and loads this pack."
---

# HVAC scripts

An HVAC video solves one heating or cooling problem cheaply, or settles one decision, for an older homeowner who would rather not pay for a service call or sign a replacement quote. It's built from the plumbing pack (`plumbing-scripts`), because the operator wants Roger the HVAC Guy "very similar to what Roger is right now", "same as rogers pipe guy in most aspects": the same voice, register and triggers. What changes is the trade: the villain's targets, the pains, the safety rules, the terms, the video types, the prices and the models. The evidence for every change is the HVAC study (`studies/hvac/` in the script-system library: 37 proven HVAC videos and 1,483 comments) and the HVAC research (`niche-research/studies/hvac/CONCLUSIONS.md`).

## What this skill covers

**It owns:** the villain, the opening by video type, emotion all the way through, "point then promise", the structure of each video type and the list item shape, CTA placement, shape and length, length, voice, proof, money framing, safety and the HVAC scanner checks. Scripts are clean narration only: no edit notes, cues or directions of any kind.

**It doesn't own:**
- **The persona:** name, tenure, sign-off, any personal detail. These live in the channel's persona profile.
- **The CTA wording:** also in the persona profile.
- **The claims policy, output format, voiceover copy and audit:** these live in the core rules.

**Authority:** the core claims policy and offer rules come first, then safety and the title's promise, then the persona profile, then this skill, then the core base rules. The core `workflow.md` runs every script (START, the input gate, the output format).

## Files in this skill

| File | What it's for |
|---|---|
| `references/unit-plan-template.md` | The plan to fill in from the title and brief before any prose. |
| `references/price-guide.md` | Typical US prices for the HVAC jobs, parts, replacement quotes and shelf items these channels talk about, plus the safety facts (the gas-leak and carbon monoxide steps), each checked against at least two sources and re-checked by a second researcher. Used for any price or fact the brief doesn't give. |
| `references/voice-samples.md` | Stretches of real human narration from HVAC tradesmen: the voice anchor for every script (core `voice-anchoring.md`). Provisional until the operator listens and picks. |
| `references/excerpts.md` | Real HVAC lines grouped by job (the point, villain lines, promises, money, safety, call-a-tech, the season and the clock, comment questions), all from real tradespeople and creators on camera. Use for shape and range, never wording. |
| `references/models/INDEX.md` | The model library: HVAC winners by video type (R22 onward) plus ten plumbing and home-repair models kept for shapes HVAC has no proven script for. Every model is a real person on camera, used for structure and voice (operator, 2026-10-27: "we dont want any ai or faceless for reference"). |
| `references/models/R04-...md` to `R44-...md` | One file per model: a beat map (what each stretch does, with timings, items, promise devices, money, safety and CTA placement; no wording), then the full labelled script, why it works and what doesn't transfer. Read at the planning step only. |

Every reference file, and this file itself, is under the copy guard: the scanner flags any run of 8 or more words shared with it (the files are listed in "Where this pack overrides the core", below). So the example lines in these rules show a shape; the script never reuses their wording.

## Where this pack overrides the core

The core base rules apply wherever this pack is silent. These are the places it changes them. Each is the plumbing pack's approved override, carried over for HVAC by the operator's "same as rogers pipe guy in most aspects" and "11 yes" (2026-10-27). Everything else in the core stands.

| Core rule | What this pack does instead | Decided |
|---|---|---|
| `workflow.md` §2, the default inputs | The `inputs` block below: the title, the brief and the rotation log. The research pack is `not used`, so the brief is the fact source everywhere the core says "the fact source". | Plumbing 2026-10-21; HVAC 2026-10-27 |
| `retention-mechanics.md` §6, "short range only" | Concrete named promises may point further than the next segment, in the body of the video only: the forward lines in "Point then promise" and "Ways to promise more value". Each names its item and its stake and is paid inside the video. Never in the opening, which names no single later item. Vague teases stay hard-banned. | P3, P10 (plumbing); HVAC 2026-10-27 |
| `cta-and-endings.md` §4, `workflow.md` §4 ("the closing line is exactly one sentence, under about 15 words"), `retention-mechanics.md` §14, `greenlight-audit.md` F3 ("the CTA or nothing, then stop") and `variety-rotation.md` slot 9 (closing line) | The ending is the one-line end CTA, then the comment ask (a short turn to the viewer, an outright ask to comment, a specific question and "I read every one"), which ends the script. It may run to two or three sentences; there is no sign-off after it. In the output's FORMAT CHECK, the closing field reads `[comment line, last line of the script]`; F3 checks this ending; rotation slot 9 rotates the comment question. Write it as "Tell me…" or a plain question: the scanner flags "let me know if you" as a chatbot leftover. | P5 (plumbing); HVAC 2026-10-27 |
| `workflow.md` §3, the 8-minute minimum; `greenlight-audit.md` F2 and the evidence block's Length line | At least 12 minutes (1,800 words at 150 a minute, or at the profile's words per minute); the evidence block reads `(minimum 12)`. See "Length". | Plumbing 2026-10-21; HVAC study 2026-10-27 |
| `variety-rotation.md`, the rotation log line | Four more fields at the end of the line: `\| model: [file numbers, or none] \| money: [device] \| promises: [devices] \| comment: "[the comment question]"`, so the rotation checks in "Using the models", "Ways to promise more value", "Money framing" and "The ending" have something to check against. | Plumbing 2026-10-21; HVAC 2026-10-27 |
| `workflow.md` §3 step 4 and `greenlight-audit.md` D3, the `--refs` files | Instead of `excerpts.md` and `reference-scripts.md` (woodworking's files), the copy guard runs against this file (`SKILL.md`), `references/excerpts.md`, `references/voice-samples.md` and every file in `references/models/`, plus the persona profile. | Plumbing 2026-10-21; HVAC 2026-10-27 |
| `research-and-sourcing.md` §6, "each number said alongside whoever counted it" | Sources and store names don't have to be said (see "Proof"). | Plumbing 2026-10-20; HVAC 2026-10-27 |
| `greenlight-audit.md` E1, the originality score (7 signals, pass at 5) | Sources aren't needed, so the two source signals change: signal 1 counts facts from the brief that most videos on the topic don't use, and signal 4 (three named sources) doesn't apply. The score is out of 6 and passes at 4. | Plumbing 2026-10-21; HVAC 2026-10-27 |
| `retention-mechanics.md` §6 and `greenlight-audit.md` B5, signposts | The sections are the opening, each item (or step, or contender) and the ending. "Number four." is the signpost for an item; in a verdict, the contender's name is. | Plumbing 2026-10-21; HVAC 2026-10-27 |
| `greenlight-audit.md` D4, "every number traces to the fact source" | The fact source is the brief plus `references/price-guide.md`. A non-price number the script fills in (a setting such as 68 degrees, "every one to three months") is allowed when it's well-established general knowledge; the evidence block's Numbers line marks each one "general knowledge". Every dollar figure traces to the brief or the price guide. | P7 (plumbing); HVAC 2026-10-27 |
| `workflow.md` §4, contractions | Kept for the pack; a persona profile may forbid them. See "Voice". | Plumbing 2026-10-21; HVAC 2026-10-27 |
| `retention-mechanics.md` §2, the hook (a transformation, the viewer's pain or wish, one spark of curiosity, in about 15 seconds); `greenlight-audit.md` A1b and the evidence block's Hook line | The HVAC opening is the hook (see "The opening"). It is checked as the same three jobs: the transformation is the fix or product named in the first sentence, with what it does; the pain or wish is the cold house, the bill, the quote or the symptom; the curiosity is the opening question, or a surprising fact the video answers. The Hook line records those three lines. The point still comes first, and the opening's six jobs run to about 45 seconds. | Plumbing 2026-10-21; HVAC 2026-10-27 |
| `retention-mechanics.md` §2, the optional value line (about one video in three) | Not used: the opening goes from the point to item one, and a list's count line (see "The opening") names the whole list, never what a single item holds. The Hook line reads `value line: none`. | Plumbing 2026-10-21 and 2026-10-25; HVAC 2026-10-27 |
| `humanizer.md` H22, `workflow.md` §4 and `greenlight-audit.md` C2: always rounded, never cents, one price per item, a sentence with three or more dollar figures quoted | Everything stays rounded and said as ranges, with two exceptions from "Money framing": the cost per use may be said in cents ("call it 40 cents a month"), and the three-prices-side-by-side device may put three figures in one sentence. A range ("$5 to $15") counts as one figure for C2's three-figure check. Each still traces to the brief or the price guide. No other price is said in cents. | Plumbing 2026-10-21; HVAC 2026-10-27 |

## Inputs

HVAC scripts are written from the title and the brief alone; there is no research pack. The workflow reads this block at START and won't write until every required input passes.

```inputs
- title | required | the locked title, exactly as approved
- brief | required | the ideation brief for this title; the script's facts, prices, settings and methods come from it first
- research-pack | not used | HVAC scripts are written from the brief
- rotation-log | required | the channel's last five ROTATION LOG ENTRY lines (from the earlier scripts in this chat, or pasted), or "none" for a new channel
```

- **The brief is the fact source,** with the price guide behind it. It does the research pack's job: the scanner checks every number in the script against the brief and `references/price-guide.md`, and the brief wins on safety.
- **No freshness check.** Prices are said as ranges (see "Money framing"), so nothing is re-checked at START.
- **Where the brief is silent, the script fills in** (P7, carried over):
  - **Prices** come from `references/price-guide.md`, said as an estimate: a rounded range or "about", never to the cent.
  - **The method, the right setting, how often to check, and what a mistake leads to** come from well-established, everyday HVAC knowledge, said plainly ("change a one-inch filter every one to three months", "set it to the temperature you actually want").
  - **No chemical, electrical or gas method** beyond the brief and the safe defaults in "Safety".
  - The run stops with NOT READY only when the brief can't carry the title's main promise, or a price the script needs is in neither the brief nor the price guide (then the cost is said in words instead, or the item is cut).

## The viewer

The viewer is a 50+ American homeowner, often in an older house and on a careful income, who would rather fix it than pay for a visit, and who has been quoted a new system at least once. They arrive from the feed, not from a search: they were offered a saving, a warning or a secret. Under the click sits one question: "Is this something I can check myself before I pay anybody?"

**What they bring, from the study's 1,483 comments** (`studies/hvac/comparison/01-viewers.md`):
- **The breakdown moment is the story they tell.** The furnace out on a freezing night (about 31 comments, five of them on a holiday), the AC out in a heat wave (19), the power out (22), the company that can't come for days (14). The most-liked thanks are rescue stories: the family kept warm, the night saved. Failed attempts of their own are rare (about 13).
- **Unlike plumbing viewers, they name the trade.** About 9% of comments do (plumbing: 8 of 506). The story they repeat is the quote against the part: a capacitor quoted at $400 to $1,500 for a part that sells for $13 to $35 (20 of 39 such comments), and "you need a whole new unit" (about 16). **But techs answer back,** and their defences get big likes ("we are not all out here" style replies, 1.6K). So the villain is aimed at the price, the upsell and the silence, never at every tech (see "The villain").
- **They correct safety, loudly.** About 62 corrections, nearly all on hands-on videos: check the power is really off (1.2K likes), discharge the capacitor (1.1K), never pressure-wash the coils (1.2K), a respirator for spray foam (2K). An unsafe line is what draws the angriest comments.
- **They argue among themselves** on covering the outdoor unit, cheap filters against MERV 13, and the brand against the installer. Where they split, the script says what each side gets right (see "Proof").
- **They thank:** a fix that worked, the reason why, a short video, and honesty.
- **They answer a question about their own house.** On the faceless leader's channel, about 44% of comments answer the closing question with their own numbers (their state, their thermostat setting, their bill).

**Skill level:**
- Write for beginners to handy homeowners, in plain words. A trade term gets a short explanation the first time ("the flame sensor, a thin metal rod that proves to the furnace the burner actually lit"), then is used plainly.
- **These terms are always explained the first time:** MERV, SEER, AFUE, BTU, tonnage, condensate line and condensate trap, condensing (high-efficiency) furnace, flame sensor, hot-surface igniter, inducer motor, pressure switch, limit switch, capacitor, contactor, heat exchanger, blower motor (and ECM or PSC if named), supply and return vents, static pressure, heat pump, auxiliary or emergency heat, refrigerant, C-wire, setback, short cycling, damper. Any other trade word gets the same treatment.
- Give the reason behind a step in one sentence; viewers thank the "why". Don't lecture: the reason, then the fix.
- Never explain what everyone knows (flipping a light switch, finding the thermostat).

**The standard kit:**
- Assume the viewer owns a screwdriver and a nut driver, a flashlight, spare furnace filters, old towels, rubber gloves, a measuring cup, a garden hose, a small brush, and the usual kitchen and laundry products (white vinegar, dish soap, baking soda).
- Anything beyond that (a wet-dry vac, a fin comb, a non-contact voltage tester, a multimeter, fine emery cloth, a condensate pump) gets its typical price range and, where one exists, a cheaper alternative or an "optional".

For more depth, see the HVAC ideation skill's `references/audience.md`.

---

## The villain

The villain on an HVAC channel is **the trade as a business and its upsell**: the replacement quote, the add-on, the after-hours bill, and whoever profits from the visit. Behind it, **the store shelf**: the "premium" filter, the gadget, the miracle spray. **The utility** only lightly. Never a named company (core claims policy), and **never the honest tech**: "a tech you trust" is always the safe answer when a job goes past the homeowner.

**How to use it, from what landed with viewers and what drew disbelief:**
- **Aim it at the price, the upsell and the silence, not at motives.** "That's a few hundred dollars to swap a part that costs less than lunch" and "nobody on the truck is going to mention it" land. Claiming to know why they do it backfired in plumbing (the most-liked doubt, 1.3K) and in HVAC: the channel that never softened its motive lines drew the only "this is a lie" comments in the study.
- **"You need a whole new unit" is the upsell's signature.** It's the story viewers tell most. Use it as the moment the viewer fears, never as a claim about a particular company.
- **Say it as a billing fact.** The trade is paid by the visit and the install, so a cheap check that ends the visits is nobody's business to mention. That's an observation the viewer can check against their own quotes.
- **The villain comes back again and again, all the way through.** One villain line in the opening, then every few items, not on a schedule and never in the same words twice: a price, a silence, the quote, the store shelf, or the outrage line below.
- **Disgust at a big price, said as the narrator's opinion.** Where a price runs into the hundreds or thousands, the narrator reacts as himself, rotating the wording ("I think that's a crime for a part that size." "That number turns my stomach."). It's aimed at the price, never at a named company, never at a person, and never says why they charge it (no "scam", no "ripping you off", no greed).
- **The honest out, at least once.** When an item goes past the homeowner, it goes to "a tech you trust", said without a sneer. It keeps the villain honest and the techs in the audience on side.

## The opening

Every opening, whatever the video type, does these jobs in about the first 45 seconds. Hooks are not one fixed formula: rotate the order and the shape across the channel's scripts (the rotation log tracks it), use the order for the video type (see "The video types"), or model the opening on one of the reference winner scripts for its shape and beats, never its wording. What can't change is that the point comes first and fast, and nothing on the banned list below appears. The study's real tradesmen land their first real value at about 30 seconds; the faceless leader takes about a minute and a half (`studies/hvac/comparison/02-openings-and-numbers.md`).

1. **The point in the first sentence.** Name the title's subject and, wherever the title allows, the fix or product itself, by about 15 seconds. Never hold the name back.
2. **A question, when it fits.** A question the viewer can answer in their own house ("When did you last slide your furnace filter out and look at it?"), answered within about 15 seconds. Never a question the viewer can't check.
3. **The villain line,** as a price, the quote or a silence (above).
4. **Honest scope or reassurance,** in one line: what it won't do, which systems it's for, or why it's safe ("This one's for the high-efficiency furnaces with the white plastic pipes." "Nothing here means opening the gas line."). This keeps the title's strongest word honest.
5. **The count line, when the video has a count.** One sentence naming the whole list and what it does for the viewer: "I'm going to walk you through the nine things to check before the first hard freeze." Skip it when the opening has already said the count. It never says what any single item holds: no "Number one is... Number two is...". Never "today" in front of it.
6. **The first real tip** by about 45 seconds; in a list, item one by about 30 seconds.

**The breakdown moment: an option, not a rule** (operator, 2026-10-27: "potentially not always"). The study's commonest viewer story is the moment it quits: the cold night, the heat wave, the quote, the company that can't come till Tuesday. The opening may start on it, in one or two plain sentences, then reach the point by about 15 to 30 seconds. Rotate it with the other opening shapes; never use it two scripts running.

**The escalation line: an option, not a rule** (the plumbing pack's, carried over). When the video runs from a small case to a big one (a dirty filter up to a furnace that won't light; the cheap fix up to the stronger one), the opening can do two things, plainly:
1. **Introduce the problem clearly,** in one sentence: what the viewer has and what the video fixes, in a beginner's words, with no build-up.
2. **Explain the escalation simply,** in one sentence: where the video starts and where it ends up, as pictures from the viewer's house. The shape (never wording to reuse): "We'll start with the vent that's barely blowing and work up to the furnace that clicks and won't light."

It stands in for the count line, or carries it. It names the two ends of the problem, never what an item holds or its fix, and the body keeps that order, smallest first. Use it only where the topic and format suit it, vary how it's said, and rotate it like any opening shape.

**Simpler and stronger.** The first line hits the viewer's own pain in strong, plain words; it doesn't have to be the worst case.
- The shape to aim for (never wording to reuse): "That furnace that kicks on, runs a minute and quits? Most of the time it's a part the size of a pencil, not the end of the furnace. Before anybody writes you up for a new system, there are a few things you can check with a screwdriver and ten minutes."
- **One dollar figure at most in the opening;** the prices belong to the items, and the opening never repeats item one's price.

**Never in an opening:** a name or channel intro, a greeting, "today we're going to", a recap of what's coming, a promise block or any run-down of what later items hold, a first-person test or demonstration ("I tested", "watch me"), or a tenure number other than the profile's or the locked title's.

**Tenure:** at most once, as the profile's fixed number (Roger the HVAC Guy: 45) or, when the title states a different one, the title's number (title numbers win), and only where it does a job (credibility right before a verdict or a mistakes list).

## Emotion, all the way through

The plumbing pack's rule, carried over whole with its examples (operator, 2026-10-21: "simpler and stronger on emotions... using strong words and targetting the exact pain points of this audience like reference scripts do. more work on emotion triggering throughout."; 2026-10-27: "11 yes"). The first HVAC test scripts (2026-10-27, `tests/iterations/iter-06/`) were safe and clean but flat: about 27-30 "you"/"your" and 4 "but" per 1,000 words, against 39 and 7 in the plumbing script the operator passed (`iter-04/test-run-03`). Every item makes the viewer feel something, in plain, strong words. In HVAC the lead feelings are distrust of the shelf and the quote, and the pride of doing it yourself; the bill, the cold night and the damage are the stakes inside the video (niche-research `CONCLUSIONS.md` §2).

1. **Put the viewer in it.** Say "you" and open each item on what they see, hear, feel or smell in their own house, not on how the thing works: the furnace clicking and not lighting, one bedroom that never warms up, the burning-dust smell of the first heat, water in the drain pan, a draft you can feel at the door.
   - Did it: "you should smell that first of the year... a little bit of dust burning off" (The DIY HVAC Guy, 30x); "You finish cooking up some bacon on a Saturday morning" (Roger the Pipe Guy, 453x).
   - Didn't: "A flame sensor sends a tiny electrical current through the flame." and "Number five is about water, and it only applies to one kind of furnace." (HVAC test runs 02 and 01: the item opens on how it works.)
2. **Aim at one real pain per item,** the ones this audience lives with: the cold house on the coldest night; the AC quitting in a heat wave; the after-hours visit; the replacement quote; being sold a system you didn't need; the bill creeping up; making it worse; the old house losing heat; the family's comfort and safety; the pride of doing it yourself.
3. **Strong, plain words.** Physical verbs and pictures over explanations: choking, starving for air, short-cycling, iced over, caked, rattling, sweating, freezing up, burning through, "while you sleep". Simple words, never clever metaphors (at most one picture-phrase per item). Short sentences mostly, but two can and should sometimes be joined with "but" to keep the story flowing.
4. **"But", much more of it, inside items and between them** (operator, 2026-10-21: "we want much more buts. both within sections and from section to section"). Aim for about 7 per 1,000 words, as the passed plumbing script; the HVAC test scripts ran about 4.
   - **Inside every item, at least one turn:** say what people think or do, then "but", then the truth. Did it: "if you can hear your gas valve opening, but the igniter was never glowing" (Word of Advice TV, 75x); "most people think they are actually helping their pipes" (Roger the Pipe Guy, 453x).
   - **Between items, bridges that turn:** the shape "But that one costs you nothing. The next one costs you a visit." HVAC test run 01 turned none of its ten bridges.
   - **A bridge that sums up the items so far** ("those first four are all about air") must be true of the items in the order the script has them.
   - Rotate how the belief is named ("you've probably heard", "the box says", "a lot of folks figure"): "Most people…" opens a sentence at most once per script (`humanizer.md` H20), and a "but" turn is never the "it's not X, it's Y" reframe (H21, at most one).
5. **Ask the viewer.** A question they can answer about their own house, answered straight away, about every two items. Did it: "Sounds impossible at first, doesn't it?" (Technology Connections, 2.5x), answered in the next line; "Problem solved, right? Not even close." (Roger the Pipe Guy, 453x).
6. **The HVAC feelings plumbing has no word for** (`studies/hvac/comparison/03-body-safety-ctas.md` §2; operator, 2026-10-27: "agree"):
   - **the clock:** the part that wears out quietly in summer and only tells you on the first cold night
   - **the dial that won't reach:** the thermostat says 70 and the house never gets there
   - **comfort, felt in the body:** warm floors, the back bedroom finally warm, a cool night's sleep
   - **the machine's sounds:** the click, the hum, the rattle, the silence when it should be running
7. **Use disgust only where the topic has it.** HVAC has less of it than plumbing: the slime in a condensate line or drain pan, mould, a dust-caked blower wheel. Use it there, in proportion, never as a default.
8. **End every item on a win.** A short line of relief, pride, comfort or the contrast; the item's one price can sit here ("That's a $5 part doing a $300 visit's job.").
9. **Reaffirm the title's feeling all the way through** (operator, 2026-10-21: "we must reaffirm throughout the emotions we are trying to trigger from the title and concept"). Come back to the title's idea and its key word, one way or another, every few items: for "11 Furnace Mistakes HVAC Companies Hope You Keep Making", the mistake and the visit nobody needed to make. HVAC test run 01 said "mistake" only in its first line. Not on every item, and never so often it turns robotic. Carry it in nouns and verbs ("while you sleep", "inside the cabinet"), not "-ly" adverbs (`humanizer.md` H12a).
10. **The villain and the outrage come back** all the way through (see "The villain").
11. **Let the narrator speak.** One short "I" opinion or verdict in most items ("I'd set it to auto and leave it there"), and once per video a line of insistence where it matters (the shape "I need you to hear me on this one"). HVAC test run 02 had a verdict in 4 of its 13 sections.
12. **Finish on relief, not danger.** The last item before the end CTA closes on reassurance or something to do tonight, even when it's a safety item.

**Never, still:** invented facts or events, guaranteed savings, the trade's motives, teases, mocked hype, worst-case exaggeration, jokes.

## Point then promise

- **Point first.** The first answer (the fix named, the rule stated, the first verdict fact) comes before anything else.
- **Pay forward lines fast.** A later item named in a forward line is paid within about five minutes. Nothing is promised in the opening, apart from the count line or the escalation line.
- **Keep one promise open.** After the opening, never go more than about five minutes without a new forward line or a payoff. Use a line that names the next value, the trade's price for what was just done, a question the next item answers, or a check the viewer can run.
- **Every callback has a promise.** A line that says "I promised" or "like I said" must match something the script really promised earlier.
- **A priority flag at the first answer,** in fresh words each time.
- **No recaps** at the end.

## Ways to promise more value

Use two or three per video, in the body only (never as a list in the opening), and rotate them across the channel's scripts.

- **A numbered item with its money stake:** "Number six can save you an after-hours call."
- **A numbered item with its stake in words:** "Number eight is the one that keeps the blower motor alive."
- **The escalation ladder:** the cheap fix, then the stronger fix, then the point to call a tech, with the trade's typical price as the top rung. The default for fix videos.
- **The same part, two prices by the clock** (operator, 2026-10-27: "agree"): two prices for the same part, what it costs on the shelf against what it costs on a night or weekend call (the study's Ray Dutton line: an igniter at $20-$60, or $250-$400 after hours). With the weekday visit added it is the three-prices device below, not this one.
- **The quote against the part:** what the viewer may be quoted against what the part really costs, said as ranges, never as a guarantee.
- **The rule that protects everything:** a safety or method rule, named at the first item it touches, paid straight after the first fix or as the last item.
- **A second use for the same product,** or "while you've got the panel off".
- **A check the viewer can run:** the filter held up to a light, the drain pan, the thermostat against a second thermometer. No first-person test claim needed.
- **A running cost tally** across the video (what the trade would have charged so far).
- **A problem the viewer didn't know they had,** promised and then shown.
- **A myth flag,** which names the belief it flips in the same line: "Number three is the one almost everybody gets backwards: cranking the thermostat higher doesn't heat the house any faster." Never a bare "the one everybody gets backwards".

## The video types

Pick the type from the title. Each type has its own opening order and item shape. These are the most common types, not the only ones. The models column names example files in `references/models/` (all real people on camera: structure and voice); `references/models/INDEX.md` lists every model for each type. Never copy their wording, and follow "Using the models" below.

| Type | Title shape | Opening, in order | First tip by | Item shape | Models |
|---|---|---|---|---|---|
| **Single-product fix** | "1 Cup of This…", "Pour X Into Y Tonight" | Product and what it does → reassurance → the doubt answered → what the visit costs → what it won't do | 40-60 s | Dose, method, wait time, what you'll see, when it won't work | R35, R36; R15, R20 |
| **N things about one product** | "N Things HVAC Techs Don't Want You to Know About X" | The product in the viewer's house and its price → what the trade charges for the same jobs → "nobody will mention it" → the belief it flips → the count line | 45-90 s | A scene, what the trade charges, the method with amounts, the payoff | R33, R34 |
| **Never-do list** | "NEVER Plug Your Space Heater Into These…" | A habit doing hidden damage or danger → the stake → the count line | 30-45 s | The habit, why it's dangerous or costly, what to do instead | R26; R16 |
| **Mistakes or habits list** | "N Furnace Mistakes…", "The N Thermostat Habits That Wear Out…" | A symptom question or a habit → the cost in hundreds or thousands → one credibility line → the count line | 15-30 s | The mistake or habit, what it costs, the right way | R24, R25 |
| **Head-to-head or ranked verdict** | "X vs Y vs Z vs W: A 45-Year HVAC Man Ranks All 4" | The moment of choice → the contenders with prices → the one scale they're judged on → everyone disagrees, the shelf sells the dear one → "each one gets a job" | 45-60 s | Each contender: what it's for, what it's not for, one line of verdict; then which to use for which house | R39; R04 |
| **Banned / rule explainer** | "Why They Keep Banning Your Refrigerant" | The why-question → the rule, scoped and dated from the brief → the reason and one real consequence, in proportion → "if yours works, you may not need to change it" → the choices | about 20 s | Rule, reason, verdict, the choices from cheapest | none yet: build it from the opening's six jobs |
| **How-to / correct way** | "You've Been Running X WRONG…", "The Right Way to X" | The task and the number-one mistake, or the myth flipped → "you can do this" → the step count line → when not to do it | 15-45 s | One step, the reason, the mistake to avoid | R23; R13, R21; R06, R15 for one-setting reveals |
| **Product swap** | "The $5 X That Beats the $30 One", "N Fixes That Make a $5,000 Quote Look…" | The dear option's price → the usual pitch and its catch → the popular choice, judged fairly → the swap named, with its price and where not to use it | about 60 s | The swap, the price, the job it fits | R42, R43; R05, R18 |
| **Hidden cause or symptom** | "Why Your X Keeps Y", "Furnace Keeps Shutting Off?" | The symptom the viewer has → what normal looks and sounds like → the hidden cause in one line → "what that means for you", answered at once | 30-45 s | Cause, how to check it safely, the fix, when it's a call | R27, R28, R30, R31, R32, R44; R20, R06 |
| **Seasonal or emergency** | "Do These N Things Before the First Cold Snap (Or Pay for It…)", the outage | The clock and the crisis → the after-hours price → "probably nothing's broken" → the cause in one line → the checks, with what the viewer already owns | 30-45 s | The check, why now, what to watch for | R22, R23, R40, R41; R17 |
| **Brand verdict** | "The Only N Furnace Brands Worth Buying" | Not written yet: its rules (how named brands may be judged) are settled with the operator at batch 2. Until then a brand-verdict title stops with NOT READY. | | | R38 |

A title that promises tests ("I Tested 5 Filters") is written as tests and results from the brief, never as "I tested".

### The item shape in lists

In every list type (N things, never-do, mistakes or habits), each item runs in this order; the table's item shape says what goes into it.

1. the scene in the viewer's house
2. what's really happening in the system (one or two lines)
3. what it costs, once (a figure or in words; see "Money framing")
4. the turn ("So what do you do instead?")
5. the fix, with its steps cut to what the viewer needs, and its safety line where it has one
6. the win

- **Length per item:** about 150-250 words is the guide for HVAC (operator, 2026-10-27: "agree"; the study's winners run a median of about 250 to 300 words an item, and only 3 of 77 items fall inside plumbing's 100-130). An item may run longer if nothing in it is fluff. Cut extra steps, repeated warnings and restated points first; never cut a safety step.
- **Bridges:** never more than two items in a row without a forward line or a price line.

**A title that fits none of these:** build the opening from the six jobs in "The opening", in the order the closest type uses, and pick the item shape from the table that best suits the content. Note the title in the plan as "new type". When the same new shape comes up on three or more videos, it's proposed for this table, and added only with the operator's yes.

## Using the models: never a copy

The models show how winning videos are built. A script borrows their structure, never their wording, and never one model's structure whole. **A script uses a model where one fits; not every script needs one** (operator, 2026-10-27: "agree but not always needed").

1. **Name the models and the differences.** When the plan uses models, it names them and at least three things done differently: the opening order, the number or order of items, the promise devices, the money device, or the comment question. A plan with no model says "model: none".
2. **No repeats.** The same model is never used twice in the channel's last five scripts (the `model:` field in the rotation log).
3. **Blending is encouraged:** the opening shape from one model and the item pacing from another, for example.
4. **Planning only.** Model files are read at the planning step, never kept open while writing. Wording comes fresh from the brief, in the persona's voice.
5. **The audit checks it:** the plan lists its differences, and no model in it appears in the last five rotation log lines.

The copy guard still flags any run of 8 or more words shared with a model file. **Every model is a real person on camera** (operator, 2026-10-27: "we dont want any ai or faceless for reference"): no faceless or AI-voiced video is a model, an excerpt or a voice sample, including the operator's own channels and Ray Dutton's Garage. Roger stands apart from the faceless leader; his catchphrases are banned (see "Banned in these scripts").

## CTAs

- **Roger the HVAC Guy has no book for now** (operator, 2026-10-27: "no book for now"): no mid-video CTA. At the end, a one-line subscribe ask, worded in the persona profile, then the comment ask.
- If a book or another offer is added later, the plumbing pack's mid-video CTA applies (about a third of the way in, never before the end of item 3, at an item's win, in its six-part shape), with the operator's yes.
- **Never** a long pitch, never the same ask twice in one video, never a production label read aloud, and never the other Roger channel or its book.

## The ending

The video's last line is a real attempt to get a comment (P5, carried over).

After the last item:
1. **The end CTA: a one-line subscribe ask,** in the persona profile's words.
2. **The comment ask, which ends the video:** a short turn to the viewer so it doesn't land abruptly, an outright ask to leave a comment ("in the comments", "leave me a comment"), one specific question the viewer can answer from their own house, and "I read every one." Two or three sentences. **In HVAC the question asks for the viewer's own numbers or house** (operator, 2026-10-27: "agree"): what their thermostat is set to, how old their furnace is, what they were quoted. The shape (never wording to reuse): "Before you go, I want to hear from you. Down in the comments, tell me how old your furnace is and what you keep the thermostat on in January. I read every one." Never a bare "let me know in the comments" without the question, and never the same question two videos running.

There's no fixed last line or sign-off after the comment ask. No recap, no tease of a future video, and nothing after the comment line.

## Length

**At least 12 minutes** of narration on every HVAC script (this pack raises the core 8-minute minimum): 1,800 spoken words at 150 a minute, or at the profile's words per minute. **12 to 20 minutes is the sweet spot.** Inside that, the value decides: words per item depend on the item.

- **Never pad to reach a length.** Cut repetition instead.
- **If the brief can't fill 12 minutes with real value,** even with the fill-ins above, the run stops with NOT READY and asks for a fuller brief. The fix belongs at the ideation stage, not in extra words.
- **For calibration, not as targets:** the faceless leader's videos run a median of about 13 to 14 minutes and 8 of the study's 10 faceless winners run 12 minutes or more; the real tradesmen's filmed repairs run shorter (about 11 minutes). Within a channel, length didn't line up with how well a video did (`studies/hvac/comparison/02-openings-and-numbers.md` §4).

## Voice

- **"You" for every instruction; "I" for opinions, preferences and verdicts.** Write in contractions, the way people talk, unless the persona profile forbids them.
- **Plain beats clever.** State the fact. At most one picture-phrase per item, and only when it teaches.
- **Honest candor.** Say the limits plainly ("Cleaning it won't fix a sensor that's cracked." "Nothing in a furnace lasts forever."). These are the lines viewers call honest. Never an invented mishap.
- **Warmth comes from reassurance, not humour.** "You're fine." "Nothing's broken." "There's no shame in calling a tech." No jokes (a portfolio-wide decision).
- **Swearing: none.**
- **A persona device only if the profile has one** (Roger the HVAC Guy: his filter check on the first of the month, with his coffee). At most twice per video, under about 40 words, to teach or warn, never as proof that something works. Its facts come from the profile and never change.
- **A phrase is voice once; in the same slot every video, it's a tic.** Each stock phrase at most once per video, and rotate what opens an item and what closes the video. (The list comes with "Banned in these scripts".)
- **Written for the voice** (core `workflow.md` §4, with the HVAC forms):
  - ratings with a space and words: "MERV 13", "a 16 SEER two unit", "96 percent efficient"
  - refrigerants as they're said: "R-twenty-two", "R-four-ten-A", "R-four-fifty-four-B"
  - units in words: "twenty-four volts", "fifteen amps", "fifteen hundred watts", "eighty thousand BTUs"
  - filter sizes in words: "a twenty by twenty-five by one filter"
  - ranges with "to": "$75 to $200", "seven to ten degrees"
  - always "carbon monoxide", never CO; "AC" and "HVAC" are fine as letters; AFUE is said as "the efficiency rating" unless the letters are explained
  - no slashes between words: "heating and cooling", never "heating/cooling"

## Proof

The study's faceless channels prove things with checks the viewer can run, sentences to say to the tech, and arguing against themselves; the real tradesmen prove them on camera, which this channel can't. Proof here is the kind that survives any footage.

**Use:**
- **The mechanism, in one plain line:** why it works. The best ones are under 15 words.
- **A number from the brief or the price guide, said as a typical range** rather than one exact price. Sources and store names don't have to be said, and a source is named only rarely, where it really helps. **When the script names a source, its figure is said as the source gives it;** without the name, round as usual.
- **The maker's own instruction,** when the brief confirms one (the furnace manual's filter rating, the alarm maker's replacement date).
- **A check the viewer runs at home,** with what they'll see either way: the filter held to a light, the drain pan, the thermostat against a second thermometer, the outside unit's fan running or not. Only checks the brief or everyday knowledge confirms.
- **A sentence to say to the tech:** the question that tells an honest quote from an upsell ("Can you show me the crack?").
- **The honest limit:** what the fix won't do.
- **Both sides, where viewers split** (operator, 2026-10-27: "agree"): covering the outdoor unit, cheap filters against MERV 13, the brand against the installer. Say what each side gets right, then the verdict for which house.
- **Exact amounts, waits and what "done" looks like.** Check the arithmetic of every dose and every load.

**Never:**
- **First-person tests, trials or demonstrations,** even when the title promises tests. Tests and results are fine when the brief gives them, said without "I".
- **Anything that needs footage the channel doesn't control:** "watch me", "look at the furnace on the left".
- **Customer stories and results.** The claims policy bans customers; say it as the typical case instead.
- **Nameless claimed experience** ("the worst furnace we ever pulled").
- **Sweeping claims nobody can check.**

## Money framing

HVAC is where money framing holds up best (the 2026-10-22 findings; the faceless winners say about six dollar figures per 1,000 words, `studies/hvac/comparison/02-openings-and-numbers.md`). The weak spot is a single low product price: viewers check it while they watch.

**1. The comparison comes early,** within the first two minutes, usually as the villain line: the shelf part against the visit, or the check against the quote.

**2. Every price is an estimate, from the brief or the price guide:** a rounded range or "about", never one exact figure and never to the cent. Not every item needs a number.
- **The number cap:** at most one dollar figure per item (a range counts as one); in a list, figures on no more than about half the items, and the rest carry their cost in words ("that's a new blower motor", "a no-heat call on a Saturday"); the opening has one figure at most and never repeats item one's.
- **Filters are where prices get disputed:** say "in a multipack" or a range, never one shelf price.
- **How to say a range:** give the spread and why it moves, or the top of it ("anywhere from $150 to $400, depending on where you live and whether it's after hours"; "on the high end, a new system can run past $10,000"). Rotate these shapes; never the same phrasing twice in one video.

**3. The cost per use, when a product lasts,** checked against the dose.

**4. Rotate the money devices** across the channel's scripts, so no two videos count money the same way:
- **three prices side by side** (the shelf, the weekday visit, the night visit)
- **the same part, two prices by the clock** (the shelf against the night call; two prices only)
- **the quote against the part**
- **the trade's price at the end of each item**
- **a running total,** closed at the last item
- **payback arithmetic for big purchases** (a new system, an efficiency upgrade, a heat pump): what it saves a year against what it costs, and how many years to break even

**5. Say it when the cheap or popular option loses.** A verdict that says no is the one viewers trust, and "the one time paying a tech is the cheap option" keeps the villain honest.

**6. A money figure in the title is paid at its item,** with what was avoided spelled out. If the price guide has no row for it, the item says it in words and the plan flags it.

**7. Brand names are optional.** Name a widely sold product only when it is the answer and the brief confirms it's on sale now.

**Never:**
- **A guaranteed saving** (claims policy). Not "this saves you $300", but "this can save you the visit".
- **The trade's motives** (see "The villain").
- **A total stated as certain** when it depends on the viewer's house.

## Safety

The facts and methods come from the brief, and **the brief always wins**. Where a job crosses from the homeowner's to a licensed tech's depends on the title and the brief (operator, 2026-10-27: "depends the title"). There's no separate fact bank: contradictions between one video and another are acceptable; unsafe advice never is.

**Defaults, only where the brief is silent.** The study's viewers corrected these more than anything else (about 62 corrections, `studies/hvac/comparison/01-viewers.md` §4), and the hands-on videos that skipped them drew the most-liked comments:
1. **Power off, and proved off.** Before any panel comes off: the furnace's power switch or the outdoor disconnect off, then checked with a non-contact tester (tried first on something you know is live, so you know it works); the gas valve off for any burner work, and the burners and metal let cool. Say it again wherever a later step opens the furnace again (a new part after a test run). Say how it comes back on, and the check after.
2. **Refrigerant is licensed work.** No charging, "topping up" or opening the refrigerant lines.
3. **Never bypass a safety switch:** a limit switch, pressure switch, rollout switch or float switch is telling you something.
4. **Capacitors hold a charge** after the power is off: a call for a tech unless the brief gives a safe, named procedure.
5. **After cleaning a condensate trap, refill it with water.** Never pour anything into the pressure-switch hoses or the inducer.
6. **Never pressure-wash coils;** gentle water and the cleaner the brief names.
7. **One cleaner at a time;** never bleach with vinegar or ammonia.
8. **Never run a furnace a tech has red-tagged.**
9. **Space heaters straight into a wall outlet,** never a power strip or extension cord, three feet clear.
10. **A car or generator at least 20 feet from doors, windows and vents,** never in a garage even with the door open, never backfed into the house wiring.
11. **Air sealing near a natural-draft furnace or water heater** needs a combustion safety test.
12. **The fireplace damper closes only when the fire is fully out and cold,** and never on gas logs.

**A gas leak, whenever a script mentions one, gets every step** in the gas-leak row of `references/price-guide.md` section 9, whatever the brief leaves out, in the script's own words. **A carbon monoxide alarm, whenever a script mentions one going off, gets every step** in that section's carbon monoxide row the same way. Carbon monoxide is a safety line, never the hook (safety fear is a weak lead: niche-research `CONCLUSIONS.md` §2).

**How safety sounds:**
- **One short line inside the step where the risk is,** with the reason, in proportion. Vague danger reads as a scare tactic.
- **The call-a-tech line names its trigger:** the shape "If it trips again the minute you reset it, that's a call." Never the vague "if it's outside your comfort zone", and never a long list of stop signs.

## Banned in these scripts

**Never:**
- **A name or channel intro,** a greeting, "today we're going to", or "this channel is for…".
- **Vague teases:** "stay till the end", "stick with me", "stay tuned", "by the end of this video" and the rest of the core hard-ban list. Concrete, named promises are allowed in the body only.
- **A recap** at the end.
- **First-person tests and demonstrations:** "I tested", "I tried", "my results", "watch me".
- **Pointing at the screen:** "look at the one on the left", "as you can see", "right here", "look at this".
- **Customer stories and results, the trade's motives,** and anything negative stated as fact about a named company.
- **Edit notes, cues, labels or directions** of any kind.
- **The template's stock lines:** "not a scam, just economics" (and "no conspiracy", "just arithmetic"); "this channel is for / exists / is all about"; "grab it now or later"; "your wallet (or furnace, or system) will thank you"; "they just don't volunteer it"; "if you're finding this helpful"; "let's continue"; "common problems you might run into".
- **The faceless leader's catchphrases** (Ray Dutton's Garage; `studies/hvac/comparison/04-models-and-voice.md` §1): "keep your cool", "same companies", "none of this is hidden because…", "if this saved you a call", "argue against myself".
- **The other Roger channel,** its name or its book (the persona profile's ban).
- **Hype that got mocked,** and any "every" or "forever" the script then walks back.
- **Competitors' catchphrases and sign-offs.**
- **Copying 8 or more words in a row** from a reference file. The copy guard flags it.

**At most once per video.** "between you and me", "ask me how I know", "here's the part nobody tells you", "I'll be straight with you", "that's the whole trick", "in your pocket", "which brings us", "hold that thought", "the big one", "the real kicker", "quick thing", "no shame in", "full stop", "trust me", "absolutely criminal", "nine times out of ten", "quietly".

## Scanner rules for this niche

The scanner (core `script-scanner.py`) reads this block. `allow` lines are wording these rules require, so the copy guard over this file never flags them; `ban` lines are fix-on-sight; `once` lines fail on the second use in a script; `letters-ok` names the letter words said as letters every day, so they aren't judged one by one.

```scanner
min-minutes: 12
letters-ok: HVAC, AC, MERV, BTU, BTUs, SEER, PVC
allow: on the high end
allow: depending on where you live
allow: I read every one
ban-regex: \btoday,? (?:we'?re|we are|I'?m|I am) going to\b | opening: "today we're going to"
ban-regex: \bI(?:'ve| have)? (?:tested|tried|ran (?:a |the |some |my )?tests?)\b | first-person test claim
ban-regex: \bmy (?:own )?(?:test|tests|testing|results)\b | first-person test claim
ban: watch me | first-person demonstration
ban: as you can see | pointing at the screen
ban-regex: \blook at the \w+(?: \w+)? on the (?:left|right)\b | pointing at the screen
ban-regex: \bnot a scam\b|\bisn'?t the scam\b|\bjust (?:plain )?(?:economics|arithmetic)\b|\bno conspiracy\b | template stock line: the economics aside
ban-regex: \bthis channel (?:is for|exists|is all about)\b | template stock line: channel promise
ban: grab it now or later | template stock line
ban-regex: \byour (?:wallet|pipes|furnace|system|unit|AC|air conditioner|heat pump|blower|filter) will thank you\b | template stock line
ban-regex: \b(?:just )?(?:do not|don'?t) volunteer it\b | template stock line
ban-regex: \bif (?:you'?re|you are) finding this helpful\b|\bif this is helping\b | template stock line
ban-regex: \blet'?s (?:continue|keep going)\b | template stock line
ban: common problems you might run into | template stock line
ban: stay tuned | tease
ban: horror movie | hype that got mocked
ban-regex: \bbrutal tests?\b | hype that got mocked
ban: keep your cool | the faceless leader's catchphrase (Ray Dutton)
ban-regex: \bsame companies\b | the faceless leader's catchphrase (Ray Dutton)
ban-regex: \bnone of this is hidden\b | the faceless leader's catchphrase (Ray Dutton)
ban-regex: \bif this (?:video )?saved you (?:a|the|one) (?:call|visit|service call|trip)\b | the faceless leader's catchphrase (Ray Dutton)
ban-regex: \bargue against myself\b | the faceless leader's catchphrase (Ray Dutton)
ban-regex: \b\d[\d,]*(?:\.\d+)?\s?(?-i:V|A|W|kW|kWh|Hz|VA|BTUh?|F)\b | unit written as a symbol (write the word: "twenty-four volts")
ban-regex: (?<![\w-])\$?\d[\d,]*\s?-\s?\$?\d | range written with a hyphen (write "$75 to $200", "seven to ten degrees")
ban-regex: \b[A-Za-z]+/[A-Za-z]+\b | slash between words (write "heating and cooling")
ban-regex: \bR-?\d{2,3}[A-Za-z]?\b | refrigerant written as a code (write "R-twenty-two", "R-four-ten-A")
ban-regex: (?-i:\bCO\b) | CO (write "carbon monoxide")
once-regex: \bnine (?:times )?out of (?:10|ten)\b | nine times out of ten
once: between you and me
once: ask me how I know
once-regex: \bhere(?:'?s| is) the part (?:people skip|nobody tells you)\b | here's the part nobody tells you
once-regex: \bI(?:'?ll| will) be (?:straight|square|honest) with you\b | I'll be straight with you
once-regex: \bthat(?:'?s| is) the whole (?:trick|method|job|game)\b | that's the whole trick
once: in your pocket
once-regex: \bwhich (?:brings us|leaves)\b | which brings us
once-regex: \bhold that thought\b|\bput a pin in\b | hold that thought
once: the big one
once: the real kicker
once-regex: \bquick (?:thing|pause|one)\b | quick thing
once: no shame in
once: full stop
once: trust me
once: absolutely criminal
once: quietly
```

## Before handing over

Check that:
- the point comes in the first sentence, with the fix or product named by about 15 seconds, and the first line hits the viewer's pain in strong, plain words
- every item puts the viewer in the scene, aims at one real pain, has at least one "but" turn and ends on a win; bridges turn between items; a question about every two items; the title's feeling comes back every few items; the villain comes back all the way through, with disgust at the big prices as an opinion (never a company, a motive or the honest tech); the last item before the end CTA closes on relief
- in a list, every item follows the item shape at about 150-250 words (a bit longer is fine, fluff never is), and no more than two items in a row go without a forward line or a price line
- the opening follows the video type's order (or the closest type's, for a new type), with no intro, greeting, tease or recap
- no promise block: the opening names no single later item and ends on the count line (when there's a count) or item one; every forward line is paid within about five minutes, and no stretch runs past about five minutes without a forward line or a payoff
- the tenure appears at most once, as the profile's number or the title's
- every price traces to the brief or the price guide and is said as an estimate (never cents except the cost-per-use device, at most one per item, figures on no more than about half the items, one at most in the opening); filled-in settings and intervals are everyday knowledge; the arithmetic holds
- the fix's cost meets the trade's price within the first two minutes
- there's no "I tested", no pointing at the screen, no customer story and no motive
- safety follows the brief, with the HVAC defaults only where it's silent; every hands-on step says the power is off and proved off; a gas leak or a carbon monoxide alarm gets every step from the price guide; every trade term on the list is explained the first time; a myth flag names its belief; split topics give both sides
- every unit, rating, refrigerant and range is written the way the voice says it
- the one-line subscribe ask comes at the end (no mid-video CTA), and the video ends on the comment ask (a turn to the viewer, an outright ask to comment, a question about their own numbers or house, and "I read every one"), with nothing after it
- each stock phrase appears at most once, none of the faceless leader's catchphrases appears, and the opening shape and money device differ from the rotation log
- when models are used, the plan names them with at least three differences, and no model was used in the channel's last five scripts
- the script runs at least 12 minutes (12 to 20 is the sweet spot), with nothing padded
