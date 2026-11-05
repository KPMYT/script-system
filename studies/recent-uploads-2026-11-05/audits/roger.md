# Audit: Roger the Pipe Guy, nine newest uploads (2026-11-05)

Channel `UCR2C--KENITllxSo1aAbWWA`. Every upload from 2026-10-29 (the day the session 13 plumbing rules went on the account) to 2026-11-04.

- **Source:** YouTube's automatic captions, pulled with NexLev `get_bulk_video_transcripts` on 2026-11-05. All nine came back with captions; none empty. Transcripts: `../transcripts/roger-<videoId>.txt`.
- **Views** are the public counts at collection on 2026-11-05 (given by the main session). The four newest are one to three days old, so their views say little yet. No retention data (the channel isn't connected to NexLev).
- **Caution: these are captions, not the VAs' scripts.** They record what the voice said, in the caption system's spelling and punctuation ("seratia", "caul", "bofilm", "1 and 1/2", "140°", "31-oz", "I read everyone"). Sentence counts and question marks taken from them are approximate. The captions also carry sound tags ("[sighs]", "[snorts]", "[clears throat]") and ">>" marks; these are left out of the word counts.
- **Timestamps** in `[m:ss]` are the start of the transcript line (about 30 seconds long) in which the quote begins, so each can be found in the transcript file. Times written "at about m:ss" (first item, CTAs) come from the caption segments and are more precise.
- **Rules audited against:** `plumbing-scripts/SKILL.md` (whole), `plumbing-scripts/references/price-guide.md`, `personas/roger-the-pipe-guy.md`, `personas/books/roger-the-pipe-guy-book.md` (fix index), `HANDOFF.md` §3 "Operator decisions, 2026-10-29", `PROPOSALS.md` P10/P17/P18, `core/cta-and-endings.md`, `core/claims-policy.md`, `core/retention-mechanics.md` §14, `core/greenlight-audit.md`.
- **Scanner:** `python3 core/script-scanner.py <copy> --rules plumbing-scripts/SKILL.md personas/roger-the-pipe-guy.md --pack plumbing-scripts/references/price-guide.md --refs plumbing-scripts/SKILL.md plumbing-scripts/references/excerpts.md plumbing-scripts/references/voice-samples.md plumbing-scripts/references/models/*.md personas/roger-the-pipe-guy.md --title "<title>"`, on timestamp-stripped copies kept outside the repo. There are no briefs in the repo, so `--pack` is the price guide alone. Caption-made flags are left out below: the sound tags, "3%", "5-lb", "2 ft", "140°", "1 and 1/2", and the copy guard's hits on the book's title (the title is required wording; the guard finds it in model S06).
- **The scanner's number check is loose:** it passes any number within 10% of any number in the price guide, so it reported "0 numbers not found" on all nine. The prices below were checked by hand against the guide.
- **Words a minute** = caption words over the whole video length. **Minutes at profile speed** = caption words / 170 (Roger's profile). **"you"** counts you, your, yours, you're, you've, you'll, you'd; **"I"** counts I, I'm, I've, I'd, I'll.

## The nine videos

| # | Video | Title | Published | Length | Views | Caption words | Words a minute | Minutes at 170 |
|---|---|---|---|---|---|---|---|---|
| 1 | `XkNGUIYWkCM` | 10 Reasons Why You Should Mix Baking Soda and Hydrogen Peroxide | 2026-11-04 | 15:23 | 410 | 2,552 | 166 | 15.0 |
| 2 | `R2NA3b3S2wQ` | Why Your Shower Drain Keeps Clogging (And How to Vac It Out FAST) | 2026-11-04 | 13:28 | 1,200 | 2,296 | 170 | 13.5 |
| 3 | `vyqjb8WLqzk` | These 4 Liquids Will Clear EVERY Clog in Your House ($3 FIX) | 2026-11-03 | 13:16 | 1,900 | 2,264 | 171 | 13.3 |
| 4 | `8muiJkXGSUM` | Why Your Sink Stopper Gets Stuck — The Real Cause No Plumber Will Tell You | 2026-11-02 | 12:17 | 1,900 | 2,128 | 173 | 12.5 |
| 5 | `CLiGOyCFpZU` | These 4 Liquids Will Clear EVERY Clog in Your House ($3 FIX) | 2026-10-31 | 13:32 | 15,000 | 2,178 | 161 | 12.8 |
| 6 | `AGp_vAn5hqI` | How to Unclog a Drain For Beginners | 2026-10-31 | 12:06 | 2,500 | 2,071 | 171 | 12.2 |
| 7 | `6VK_UQJ7kHQ` | The Absolute BEST Way To Clean Your Toilet In 2026 | 2026-10-30 | 12:57 | 13,000 | 2,123 | 164 | 12.5 |
| 8 | `jXZrwNkf4qQ` | NEVER Call A Plumber Again! How To Install a Toilet FAST Without Leaks | 2026-10-29 | 15:29 | 2,700 | 2,616 | 169 | 15.4 |
| 9 | `8NJL9eGeLcs` | Does Green Gobbler ACTUALLY Work? (And 3 BETTER Ways To Unclog Drains) | 2026-10-29 | 14:42 | 1,200 | 2,485 | 169 | 14.6 |

**All nine pass the 12-minute minimum** (measured: 12:06 to 15:29 on the clock; 12.2 to 15.4 minutes at 170). The profile's 170 words a minute holds: the voice ran 161 to 173 (median 169). The shortest, #6, clears it by six seconds.

---

## Two questions first

### A. #3 and #5 have the same title. Is #3 a re-upload? No: it's a different script.

**Plainly: #3 (`vyqjb8WLqzk`) is not a re-upload and not a re-edit of #5. It is a different script, a different voiceover and a different video, uploaded under #5's title.** The title promises four liquids; #3 is about five dry drain cubes and never says the word "liquid" (measured: "liquid" 0 times in #3, 3 times in #5).

| | #5 `CLiGOyCFpZU` (2026-10-31, 15K) | #3 `vyqjb8WLqzk` (2026-11-03, 1.9K) |
|---|---|---|
| First sentence | "That jug of drain cleaner you poured in last night is sitting in a sink of gray water and you're out 10 bucks." [0:00] | "Five cubes pressed in a plain ice cube tray and a slow drain in your house stops being a phone call." [0:00] |
| The count | "Four liquids clear every everyday clog in your house" [0:00] | "Here are the five, one for every drain in the house." [0:32] |
| The items | 1 dish soap and hot water (kitchen), 2 hydrogen peroxide (bathroom), 3 white vinegar (scale, rim jets), 4 washing soda (kitchen line, standpipe) | 1 kitchen sink (washing soda + baking soda cube), 2 bathroom sink (baking soda + citric acid cube), 3 shower and tub, 4 toilet bowl, 5 laundry standpipe |
| Organised by | the bottle | the drain |
| How it's used | poured | pressed into a tray, dried 24 hours, dropped in dry |
| Washing soda | "Never pour it in dry because dry powder meets water in the trap, the U-bend under the sink, and sets like plaster." [9:57] | "Once a month, drop one cube down the kitchen drain." [2:05] (a dry washing-soda cube) |
| Mid-video CTA | "Before the vinegar, one thing." [5:46], pages 42 to 45 and 56 | "One thing while that cube fizzes" [4:42], pages 42 and 43 |
| Comment ask | "Leave me a comment with how old your house is and which of the four bottles you already had under the sink." [13:02] | "Tell me which drain in your house runs slow first, the kitchen or the shower, and whether you've ever paid somebody to clear it." [13:05] |

What the two share is the channel's stock material, not script text: the grease "like wax on a candle holder" ([1:02] in #5, [0:32] in #3), the jetting price "$350 to $800", the zip strip, the rim jets, the standpipe and the main-line sign. The scanner's copy guard (8 words in a row) runs only against the library, not between videos, so this wasn't checked by machine; reading the two side by side, no sentence repeats.

**Why it matters:** the title is the video's promise. #3's viewer clicked for four liquids at $3 and got five cubes made from three powders that cost "about $15 to $20 for the lot" [11:00]. In audit terms that is the one fault a VA can't fix with edits: `core/greenlight-audit.md`, "The three verdicts", HOLD: "a bait-and-switch, where the hook promises a video the body doesn't contain." Most likely an upload slip (the cube video was given the liquids video's title), but that's a reading: the brief and the intended title aren't in the repo. Worth asking the VA which title the cube script was written for, and retitling #3 to match its content.

### B. Why are #5 (15K) and #7 (13K) so far above the rest? A reading, not a rule.

**Measured first:** the other seven have 410 to 2,700 views. #5 and #7 are five and six days old; #8 and #9 are seven days old and have 2,700 and 1,200; #6 is #5's age and has 2,500. So age alone doesn't explain the gap. #1 to #4 are one to three days old and can't be judged yet.

**What the two openings do that the other seven mostly don't** (reading):

1. **They open on a habit the viewer has already tried, and say it fails.** #5: "That jug of drain cleaner you poured in last night is sitting in a sink of gray water and you're out 10 bucks." [0:00]. #7: "I'll never understand why people keep pouring bleach on a toilet ring." [0:00], then "You scrub till your shoulder aches. It fades a little, and 2 weeks later it's back, darker than before." [0:00]. Both name a product nearly every viewer owns and has used (the jug, the bleach) and call it the wrong tool in the first sentence. The pack calls the failed attempt "the strongest opening feeling in the data". Of the other seven, #9 does this too ("gone to bed hoping, and come back in the morning to the same gray water" [0:00]) and #4 half does it ("you've spent a month fighting it with your fingernails" [0:00]); #1, #2, #3, #6 and #8 open on the fix or the job instead.
2. **They take the blame off the viewer.** #7: "That isn't you doing it wrong. Bleach can't touch what that ring is made of." [0:31]. #5: "But the jug's label leaves one thing out. The clog in your kitchen and the clog in your shower aren't the same clog and no single liquid touches both." [0:00]. Both turn "I failed" into "I was sold the wrong thing", in the first 35 seconds. No other opening in the nine does this as directly.
3. **The whole answer by about 10 seconds, all of it.** #5 names all four liquids in its second and third sentences ("Dish soap, hydrogen peroxide, white vinegar, and washing soda." [0:00]); #7 names the fix in its third ("that brown ring at the waterline gets citric acid overnight, not bleach." [0:00]). Several others name one fix early (#1, #2, #6), but these two give the viewer the full answer to the title up front and make the video the "how" and the "why".
4. **A broad, everyday topic.** Every clog in the house; cleaning the toilet. Both are cleaning-and-upkeep jobs every homeowner does, not a repair a part of the audience needs (a stuck stopper, a toilet install, one product). This is probably as much the title and thumbnail as the script, and the script can't take credit for the click.
5. **They are the two slowest voiceovers** (measured: 161 and 164 words a minute; the other seven 166 to 173). Possibly more pauses; worth a listen, but it may be nothing.

**Where they differ from each other** (so neither is "the formula"): #5's opening is clean by the pack (item one at about 0:43, no promises beyond the count line, an honest scope line for "EVERY": "Every clog means the everyday soft kind. Hair wads, toys, and roots get a tool or a phone call." [0:32]). #7's opening is the pack's banned shape: a run-down of four later steps and step one at about 1:25 (see video 7, rule break 1). So the promise block didn't sink #7, and the clean opening didn't make #5. Without retention data there's no way to tell whether #7's viewers left during that block. The safe reading: the first 15 seconds (the habit, the blame shift, the answer) did the work in both; the 30 seconds after them differ.

---

## 1. "10 Reasons Why You Should Mix Baking Soda and Hydrogen Peroxide" (`XkNGUIYWkCM`)

Published 2026-11-04 · 15:23 · 410 views at collection (one day old).

**In one line:** the cleanest of the nine: a true ten-item list that follows the pack almost line for line (point first, item one at about 0:40, every item opens in the viewer's house and ends on a win, a forward line paid in four minutes, one small thing at the end); one small miss.

### What works

- **Point, price and pain in the first 10 seconds:** "A box of baking soda and the brown bottle of 3% peroxide. About $4 for the two of them and that pink ring in your toilet bowl is gone in half an hour. You've scrubbed that ring before and it came back." [0:00].
- **The villain as two facts side by side, exactly the pack's shape:** "Nobody in the trade will bring up the two cheapest things in your house. And a visit to clear a smelly drain costs you hundreds." [0:00].
- **Honest scope that keeps the title honest:** "This mix won't open a hair clog or eat a crusty mineral ring, but it does all 10 jobs on this list." [0:30]. And it holds that line inside the items: "If it feels like sandpaper, that's mineral from hard water, and that's a citric acid job, not this one." [0:30]; "The paste won't touch the white crust around the holes, though. That's scale" [14:05].
- **The title's word comes back as every signpost:** "Reason one", "Reason two" … "Reason 10" (the pack's "reaffirm the title's feeling").
- **The check before the fix:** "Put a glove on and run a finger across it first. If it smears, you've got bacteria." [0:30]; "Black that lifts with this paste was on the caul. Black that won't lift is under it." [8:50] ("caulk"; the paste as the test is a good, specific idea).
- **Three prices side by side, the pack's money device:** "About $4 for the box and the bottle. $8 to $12 for one jug of foaming drain cleaner that covers the smell for a week. $150 to $350 for a visit to clear one drain." [2:34]. Then the narrator's own disgust: "I think that's an ugly number for a smell." [2:34].
- **Tenure once, right before a verdict:** "45 years in the trade. And my verdict on the jug is simple. It buys you a week." [2:34].
- **Safety in one line, where the risk is:** "Never in a bottle with the lid on because the oxygen it gives off needs somewhere to go." [1:02]; "Nothing follows peroxide down a drain. Don't chase it with vinegar and don't chase it with bleach." [3:39].
- **A forward line paid on time:** "The kitchen is coming at reason eight, and that's where you get the one sign that means stop pouring." [8:20], paid at about 12:16: "And here's the sign I promised you. Two drains backing up at the same time or the tub filling when the toilet flushes is the main line." [11:58].
- **Mid-video CTA in the six-part shape at about 5:38 (37%), after reason 3 of 10:** "Before the tub, a word about my book. If this one's already crossed a few bottles off your list, that's the idea behind" [5:14]; book match correct (pages 42-43 = Fix 31, "Stop Using Chemical Drain Cleaner in Old Pipes"); link and QR code; return line "Now, same paste, same shower, different enemy." [5:46].
- **One small thing at the end, then the comment ask:** "Tonight, before you turn in, run your thumb across that shower head face." [14:36]; "Leave me a comment and tell me which of the 10 you're mixing up first. And whether that ring in your bowl was the pink kind or the crusty kind, I read everyone." [15:07].

### Rule breaks

1. **The baking soda and vinegar habit is corrected without crediting it first.** "Now, you've probably done the baking soda and vinegar volcano down there and watched it foam. But the foam is the show, and those two cancel each other out before they reach the slime." [2:34]. Rule: `plumbing-scripts/SKILL.md`, "The viewer": "When correcting a loved one (baking soda and vinegar), credit their thrift first: about 23 comments defended it." Fix: one line of credit before the "but" ("It's cheap and it's honest, and I see why folks swear by it. But…"). Video 3 does this well: "Vinegar is fine. And if that's your habit, keep it." [4:42].

### Facts worth checking

- **"vinegar and peroxide make a fume you don't want in a closed bathroom"** [3:39]. Measured against the pack: right to keep them apart (safety default 3). The chemistry (peracetic acid) is better described as corrosive than as a fume; video 5 says "corrosive to the pipe and to you" [8:24]. Fine as is; a reading.
- **"$500 to $1,500" for a soaked wall behind a tub** [9:21] traces to the price guide (mold, small area; drywall, larger section). **"$15 to $40"** for a showerhead [14:05] traces (guide: $15 to $40). Measured.

### Voice/caption oddities

- **"The paste is This mix won't open a hair clog"** [0:26 in the captions]. The voice seems to start one sentence and restart another. Worth a listen; if it's audible, it's in the first 30 seconds.
- "seratia" (Serratia), "bofilm" (biofilm), "caul"/"coaul" (caulk), "pore mix" (pour mix): caption spellings, probably fine in the audio. "coaul job" [9:53] worth a listen.
- Sound tags: "[sighs]" right before "I think that's an ugly number for a smell." [2:34]; "[clears throat]" mid-sentence [4:11]; "[snorts]" twice [8:50, 9:53]. See the channel section.

### Numbers

| | |
|---|---|
| Length | 15:23 |
| Caption words | 2,552 |
| Words a minute | 166 |
| Minutes at 170 | 15.0 (passes 12) |
| First real item | Reason one at about 0:40 (scanner: about 45 seconds at 170) |
| Opening promises (beyond the count line) | 0 |
| Mid CTA | about 5:38 (37%), after reason 3 of 10 |
| End CTA | about 14:56; comment ask about 15:07 |
| "you" / "but" / "I" per 1,000 | 29.0 / 4.3 / 5.9 |
| Question marks (approx.) | 2 (captions drop many; the script asks at least five: "What's on the underside?", "Does your bathroom have a window?") |
| Scanner | 10 items, every item has an "I" line and a "but"; longest sentence 35 words; no ban or once-list hits |

---

## 2. "Why Your Shower Drain Keeps Clogging (And How to Vac It Out FAST)" (`R2NA3b3S2wQ`)

Published 2026-11-04 · 13:28 · 1,200 views at collection (one day old).

**In one line:** a strong, practical how-to that names the fix in the first sentence and explains the "why" better than any other video here; one forward line is left hanging for nine minutes, the opening's "nothing touches a chemical" is walked back by the peroxide step, and one fact about the main line is backwards.

### What works

- **The fix in the first sentence, then the pain in the viewer's own shower:** "The fastest way to clear a shower drain that keeps clogging is the wet dry vac in your garage. One pull and the whole hair mat comes up in one slimy piece. Halfway through a shower, the water's over your ankles, gray and soapy, and it's the third time this year." [0:00].
- **A question the viewer can check, answered at once:** "When did you last lift that drain cover? If you can't remember, there's a wad of hair under it the size of a mouse" [0:00].
- **The count line without a promise block:** "Four steps to get it out, then the cheap habits that keep it out." [0:30]. Step one at about 0:41.
- **The step that decides it, flagged and explained:** "Step three. Make the seal, and I'd call this the step that decides whether the vac pulls hair or just makes noise." [2:34]; the tub overflow catch is a real, specific save: "Leave it open, and the vac pulls air through the overflow instead of pulling on the clog." [3:36].
- **Safety in proportion:** "A household vacuum pulling standing water is a shock waiting to happen." [1:01]; "If anybody in the house poured a chemical drain cleaner down there in the last day or two, stop." [4:08].
- **The hidden cause, told as a picture and a timeline:** "A shower drain never clogs all at once. It was fine in January, slow by March, and over your ankles by summer. And that's why it keeps clogging. Nobody ever took the mat out. The jug ate a hole through the middle of it." [6:45]. The best "why" on the channel this week.
- **The villain as two facts:** "Nobody on that aisle mentions the jug can't take the whole mat. And the next visit to snake it runs the same as the last one." [7:16].
- **Mid-video CTA at about 5:53 (44%), after step 4 of 4, against an open question** ("So, why does it come back?" [5:40]): "If that pull just saved you the visit, my book has 100 more like it." Book match correct (pages 43-44 = Fix 33, "Clear a Bathroom Sink Stopper the Easy Way", hair under the stopper). Return line: "So, about [snorts] that mat coming back." [6:13].
- **A fair choice, not a sales line:** "People buy the catcher and never empty it, and a full catcher stops the water the same as a clog would. So, pick whichever one you'll actually empty." [9:51].
- **One small thing, then the comment ask:** "And tonight, all it takes is a screwdriver and a look under that cover." [12:58]; "Leave me a comment and tell me how big that hair mat was when it came up, and how many people share that shower. I read every one." [12:58].

### Rule breaks

1. **A forward line paid about nine minutes later.** "And if you'd rather not buy one at all, there's a cheap plastic tool further on that does a slower version of the same job." [1:01] (at about 1:23); the zip tool arrives at [10:21] ("A plastic zip tool, a flat flexible strip"). Rule: `plumbing-scripts/SKILL.md`, "Point then promise": "A later item named in a forward line is paid within about five minutes." Fix: either give the zip tool as the no-vac option inside step one, or drop the forward line and keep the zip tool where it is as "the first rung".
2. **The opening's scope line is walked back.** "Nothing here touches a chemical or hurts old pipe." [0:30], then "Pour a cup of plain 3% hydrogen peroxide, the cheap drugstore kind, into the drain and leave it 30 minutes." [8:17]. Peroxide is mild, but it is a chemical poured down the drain, and the viewer heard "nothing". Rule: `core/greenlight-audit.md` A4 ("Everything the hook claims is backed by the body") and the pack's opening job 4 (the scope line keeps the title's strongest word honest). Fix: aim the line at what it means: "Nothing here comes out of a drain-cleaner jug or hurts old pipe."

### Facts worth checking

- **The main-line explanation is backwards** (reading, from everyday plumbing knowledge): "The toilet is the lowest drain with the most water. So, when the main line's blocked, a flush has nowhere to go but back up into the tub." [11:53]. The toilet sends the most water at once, but it's the tub or shower that's usually the lowest opening, which is why the water shows up there. Video 6 has it right: "every gallon you send down has nowhere to go but back up through the lowest drain you've got." [10:25]. Fix: "The toilet sends the most water at once, and the tub is the lowest opening, so that's where it comes up."
- **"Bar soap plus the minerals in hard water makes soap scum"** [6:13]: correct.
- Prices measured against the guide: wet-dry vac "about 40 to 60 dollars" [1:01] (guide: $40 to $60); the visit "about 150 to 250" [0:00] (guide: sink, tub or shower clog $100 to $300; inside it, fine); hair catcher "$5 to $15" [9:21] and zip tool "$3 to $5" [10:21] (guide: drain strip about $3; the catcher isn't in the guide, so it must come from the brief).

### Voice/caption oddities

- **">> 45 years in the trade, and that jug of caustic cleaner is still the one thing I'd leave on the shelf. >>"** [8:49]. The caption system marks ">>" when it hears a new speaker. This sentence may sound different from the lines around it (a separately generated clip?). Worth a listen.
- "Links in the description and the QR codes on your screen" [6:13]: probably caption plurals; worth a listen.
- Sound tags: "[clears throat]" [1:01], "[snorts]" twice [4:38, 6:13].

### Numbers

| | |
|---|---|
| Length | 13:28 |
| Caption words | 2,296 |
| Words a minute | 170 |
| Minutes at 170 | 13.5 (passes) |
| First real step | Step one at about 0:41 |
| Opening promises | 0 (count line only) |
| Mid CTA | about 5:53 (44%), after step 4 of 4 |
| End CTA | about 13:06 |
| "you" / "but" / "I" per 1,000 | 20.9 / 6.1 / 5.2 |
| Question marks (approx.) | 6 |
| Scanner | longest sentence 33 words; "100" said four times (the echo check: the book's number) |

---

## 3. "These 4 Liquids Will Clear EVERY Clog in Your House ($3 FIX)" (`vyqjb8WLqzk`)

Published 2026-11-03 · 13:16 · 1,900 views at collection (two days old).

**In one line:** a decent drain-cube script uploaded under the wrong title: the title promises four liquids for $3, the video is five dry cubes and never says "liquid"; inside, the script is sound, but its opening carries three prices, the insistence line is used twice, and the CTA comes before item 3.

### What works

- **Drain by drain, each opening in the viewer's house:** "You rinse the roasting pan on a Sunday night and the water sits in the sink a second longer than it used to. Next month, it's 2 seconds and there's a gurgle when the dishwasher drains." [0:32].
- **The one end-of-video promise P18 allows, paid at the end:** "These cubes are upkeep, not a rescue. And where they stop is the last thing I'll cover." [0:00], paid at about 11:36: "Now, where the cubes stop, they're upkeep. They keep a drain from getting slow, and they won't clear one that's already stopped." [11:30].
- **Credits the viewer's habit before the turn** (what video 1 missed): "Does this do anything baking soda and vinegar wouldn't? Vinegar is fine. And if that's your habit, keep it. But the cube is dry." [4:42].
- **A safety line about the product itself, in plain words:** "They look like candy, and a kid or a dog will treat them like candy." [2:05].
- **The honest limit:** "No cube melts hair. Nothing you pour melts hair." [5:46].
- **Cost per use, the pack's device, and the arithmetic holds:** "A tray for a dollar or two gives you a dozen or so cubes. Call it a dime a cube." [2:37].
- **The year adds up without a guarantee:** "Set that against three or four drain calls at $150 to $350 each. That's where the thousand a year comes from. Nobody's promising it to you." [11:00].
- **Mid-video CTA in shape:** "One thing while that cube fizzes, if that sink is the drain that's been costing you" [4:42]; book match correct (pages 42-43 = Fixes 31 and 32, the jug and the right plunger); link and QR code; return line "Right, the shower and the hair." [5:15].
- **One small thing, then the comment ask:** "So tonight, do one thing. Mix one bowl of washing soda and baking soda, spritz it, press it into a tray, and leave it on the counter to dry." [12:34].

### Rule breaks

1. **The title doesn't match the video** (see "Two questions first", A). Title: "These 4 Liquids Will Clear EVERY Clog in Your House ($3 FIX)". Video: "Five cubes pressed in a plain ice cube tray" [0:00]; five items; no liquid; "about $15 to $20 for the lot" [11:00]; and it says plainly the cubes "won't clear one that's already stopped" [11:30], against "Will Clear EVERY Clog". Rule: `core/greenlight-audit.md`, "The three verdicts": a HOLD for "a bait-and-switch, where the hook promises a video the body doesn't contain"; the pack's opening job 1 ("Name the title's subject"). Fix: retitle #3 for what it is (five drain cubes, upkeep), or take it down if it was uploaded by mistake. The operator's call.
2. **Three money figures in the opening.** "Each one is a plumber at $150 to $350 depending on where you live. Three or four of those in an older house and there's your thousand a year. The powder for a whole tray of cubes costs about a dollar or two." [0:00]. Rule: `plumbing-scripts/SKILL.md`, "The opening" and "Money framing" 2: "One dollar figure at most in the opening". Fix: keep the visit's price; say the rest in words ("a few of those a year adds up fast"; "pocket change for the powder").
3. **The insistence line is used twice.** "Number four is the one place in the house where I need you to hear me on where the cube goes." [7:21] and "Now, the part I need you to hear. The cube goes in the bowl. Never in the tank." [8:54]. Rule: `plumbing-scripts/SKILL.md`, "Emotion" 10: "once per video a line of insistence where it matters". Fix: cut the first; the second is the one that matters.
4. **The mid-video CTA comes after item 2 of 5** (at about 5:10, 39%). Rule: `plumbing-scripts/SKILL.md`, "CTAs" (Roger): "never before the end of item 3". Its timing (about a third of the way in) is right; the item rule is broken. See the channel section: four of nine videos do this, all short lists, where "about a third" and "after item 3" can't both be met.

### Facts worth checking

- **A dry washing-soda cube dropped down the kitchen drain and the standpipe** [2:05, 10:29]. The pack's safety default 2 says "washing soda dissolved first in hot tap water, not poured in dry" (17 angry comments in the study about washing soda that set hard), but the default applies only where the brief is silent, and the brief wins. Video 5, four days earlier, says the opposite: "Never pour it in dry because dry powder meets water in the trap, the U-bend under the sink, and sets like plaster." [9:57]. Contradictions between videos are allowed by the pack, but this one is the study's top safety complaint. Worth checking against the brief; if the brief is silent, the cube should be dissolved in a jug of hot water first.
- **"A tray for a dollar or two gives you a dozen or so cubes"** [2:37] and "about $15 to $20 for the lot" [11:00]: measured against the guide, the lot holds (citric acid about $10 to $15 a pound, washing soda $5 to $6, baking soda a dollar or two).
- **"Grease film is the most common kitchen clog there is."** [1:02]: general knowledge, fine.
- **"I've pulled more rotted flappers out of tanks with a blue tablet in them than I'd like to count."** [8:54]: numberless experience, which the profile allows; fine.

### Voice/caption oddities

- **"[sighs and gasps]"** right after "Lift the strainer." [5:46]. If the voice really gasps there, it lands as a reaction to the gunk, which may even work; worth a listen.
- "The visit is what gets build." [0:00] ("billed"), "litted jar" [2:05] ("lidded"), "hand augur" [12:01]: caption spellings; "build" and "billed" sound alike, fine.
- "I read everyone." [13:05]: caption spelling of "every one".

### Numbers

| | |
|---|---|
| Length | 13:16 |
| Caption words | 2,264 |
| Words a minute | 171 |
| Minutes at 170 | 13.3 (passes) |
| First real item | Number one at about 0:42 |
| Opening promises | 1 ("where they stop is the last thing I'll cover", paid at the end: allowed by P18) |
| Mid CTA | about 5:10 (39%), after item 2 of 5 |
| End CTA | about 12:50 |
| "you" / "but" / "I" per 1,000 | 21.6 / 3.1 / 4.9 |
| Question marks (approx.) | 4 |
| Scanner | longest sentence 35 words; echo: "washing soda and baking soda" three times |

---

## 4. "Why Your Sink Stopper Gets Stuck — The Real Cause No Plumber Will Tell You" (`8muiJkXGSUM`)

Published 2026-11-02 · 12:17 · 1,900 views at collection (three days old).

**In one line:** a clear, well-built fix list that puts the hidden cause up front, as the hidden-cause type asks; the opening runs to 1:09, its "no tool you don't already own" is walked back by the $3 strip, and the CTA sits past halfway.

### What works

- **The hidden cause in the opening, in plain pictures:** "The reason is a part nobody looks at. Under that sink, there's a thin metal rod running straight across the inside of the drain pipe, and every hair that ever went down that drain caught on it." [0:00]; and why the viewer's own try failed: "That's why the jug of drain cleaner you poured in from the top did nothing." [0:31].
- **The villain as a price for the time:** "A plumber's minimum visit for that runs about $100, often more, for 5 minutes with a pair of pliers." [0:31].
- **The machine explained in four parts, in the viewer's words:** "Pull the knob, the strip lifts the rod, the rod tips, and the stopper rises. Four parts. That's the whole machine, and it hasn't changed much since your parents' house." [2:06].
- **A forward line naming a problem the viewer didn't know they had** (one of the pack's promise devices): "And while that rod is out, there's a problem you don't know you have yet. The next one is why people clean the stopper and end up with a rotten cabinet floor." [3:40].
- **Tenure once, doing a job:** "In 45 years, I never once met a pivot nut that wanted more than fingers and a quarter turn. Hand tight." [4:41].
- **A check with both outcomes:** "Dry towel? You're done. A damp spot? Give it a quarter turn more with the pliers and check again." [4:41].
- **Two facts side by side:** "a plumber will charge you a full visit for it, and it's 30 seconds of work for him. Nobody's going to say that over the phone." [8:22].
- **Disgust at the price, as his opinion:** "To have it fitted, the trade charges a few hundred, and that number makes me sick for a part that costs less than a pizza." [10:56].
- **Book match correct:** "The stopper cleaning from number one is on pages 43 and 44." [6:48] (Fix 33).
- **One small thing, then the comment ask:** "So tonight, before you brush your teeth, open the cabinet and shine the flashlight at that pivot nut." [11:26]; "Leave me a comment and tell me which stopper you've got, the pull knob or the push button, and how long it's been stuck." [11:58].

### Rule breaks

1. **Item one lands at about 1:09.** The opening runs about 207 words (scanner: "item one at word 207, about 73 seconds at 170"). Rule: `plumbing-scripts/SKILL.md`, "The opening": "the first real tip, step or item lands by about 45 seconds … about 130 spoken words for Roger" (operator, 2026-10-29). Fix: the cause and the jug line are good; cut the second symptom sentence ("You push it down, and the sink either holds a bowl of dirty water, or it won't hold water at all." [0:00]) and fold "Toothpaste, soap, and the oil off your skin glued it into a mat" into one clause.
2. **The scope line is walked back.** "Nothing here needs a tool you don't already own, and nothing here goes down a drain." [0:31], then "take a plastic drain strip, the floppy one with the barbs, about $3 at any hardware store. Run it down the open drain" [3:09], then silicone plumber's grease [9:56] and a new pop-up assembly [10:56]. The drain strip is outside the pack's standard kit. Rule: `plumbing-scripts/SKILL.md`, "The opening" job 4 (the scope line keeps the title honest; never a blanket line the video walks back) and "Banned": "any 'every' or 'forever' the script then walks back"; `core/greenlight-audit.md` A4. Fix: "Nothing here needs more than a $3 strip and a pair of pliers, and nothing gets poured down the drain."
3. **The mid-video CTA comes at about 6:54, 56% of the way in.** Rule: `plumbing-scripts/SKILL.md`, "CTAs" (Roger): "about a third of the way in, never before the end of item 3". It is after item 3, so the item rule holds, but item one runs 473 words (scanner), so "after item 3" is past halfway. Fix: shorten item one (it carries the anatomy of the whole stopper), or treat this as the short-list conflict in the channel section.

### Facts worth checking

- **Number six's replacement steps skip the seal** (reading, from everyday plumbing knowledge): "Unscrew the big nut where the pipe meets the drain under the sink, and the old assembly lifts out. Drop the new one in, snug that big nut by hand" [11:26]. A new pop-up drain needs plumber's putty or silicone under its top flange and the gasket under the sink, and the tailpiece reconnected; without that, the new drain leaks into the cabinet the video warns about in number two. Worth one line.
- **"Never petroleum jelly because it eats the rubber seals."** [9:56]: correct.
- **Prices:** pop-up assembly "$10 to $25" [10:56] traces (guide: part $10 to $25); "a few hundred" to fit it (guide: about $100 to $350): fine in words. Cabinet floor "$150 to $500 to dry it out and patch it" [4:41]: the guide gives "soaked cabinet floor $150 to $200; a stock cabinet swapped $250 to $600", so $500 stretches the first row; fine if the brief gives it.

### Voice/caption oddities

- **">> [sighs] >>"** right before the price line [0:31], and **">> [laughter] >>"** before "I've seen the faces people make at that moment" [2:38]. A laugh is the one sound tag on the channel that would clash with the pack ("No jokes"). Worth a listen.
- "everyone ends with your stopper lifting" [0:31] is "every one".

### Numbers

| | |
|---|---|
| Length | 12:17 |
| Caption words | 2,128 |
| Words a minute | 173 |
| Minutes at 170 | 12.5 (passes) |
| First real item | Number one at about 1:09 (scanner: about 73 seconds at 170) |
| Opening promises | 0 (count line only: "There are six reasons a stopper sticks" [0:31]) |
| Mid CTA | about 6:54 (56%), after item 3 of 6 |
| End CTA | about 11:55 |
| "you" / "but" / "I" per 1,000 | 27.7 / 4.7 / 4.7 |
| Question marks (approx.) | 5 |
| Scanner | longest sentence 34 words; "Most…" opener once (allowed once); one reframe (allowed one) |

---

## 5. "These 4 Liquids Will Clear EVERY Clog in Your House ($3 FIX)" (`CLiGOyCFpZU`)

Published 2026-10-31 · 13:32 · 15,000 views at collection (the channel's best of the nine).

**In one line:** a tight, confident script: all four answers in the first 10 seconds, an honest scope line for "EVERY", item one at about 0:43 and the best safety rule on the channel; it breaks three smaller rules (a run-back of all four items before the end, two prices in the opening, the CTA after item 2).

### What works

- **The failed attempt, the answer, and the twist in 15 seconds:** "That jug of drain cleaner you poured in last night is sitting in a sink of gray water and you're out 10 bucks. Four liquids clear every everyday clog in your house and not one of them cost more than four bucks. Dish soap, hydrogen peroxide, white vinegar, and washing soda. But the jug's label leaves one thing out." [0:00].
- **"EVERY" kept honest:** "Every clog means the everyday soft kind. Hair wads, toys, and roots get a tool or a phone call." [0:32]. This is the pack's scope job done exactly.
- **The item shape, in order** (scene, what's in the pipe, the cost, the turn, the fix, the win): "You cook bacon on a Saturday morning, rinse the pan, and the water goes down a little slower than it did last week. Nothing dramatic. But that grease didn't leave." [0:32]; "that's $150 to $350 for somebody to run a cable down it" [1:02]; "So, what do you do instead?" [1:34].
- **The priority flag at the first answer:** "Out of everything in this video, this is the one I'd make you do." [1:34].
- **A check the viewer runs, in five words each:** "Slime is gray and it smears. Scale is white and it scratches." [6:51].
- **The silence line as two plain facts:** "Nobody in the trade mentions the jets. And a new toilet installed is a bill in the hundreds." [7:52].
- **The safety rule, stopped for, with the reason and the workaround:** "Now, the rule, and this is the one rule I'd stop the video for. Never put vinegar and peroxide down the same drain on the same day. Together, they make peracetic acid, and that's corrosive to the pipe and to you. Peroxide on Saturday, vinegar on Sunday." [7:52].
- **Cost per use, and the arithmetic holds** (a 55-ounce box is about seven cups, so about 14 half-cup pours at $5 to $6): "A half cup at a time, a box gives you a dozen or so pours. Call it 40 cents a pour, give or take a dime." [10:28].
- **Three prices side by side:** "A dollar a bottle versus $10 for the jug versus $300 for the visit. Same clog." [12:00].
- **Book match correct and well tied:** "Pages 42 to 45 cover which drains can't take hot water and what to reach for instead of the jug. Page 56 has the signs that mean it's your main line and not your drain." [5:46] (Fixes 31-36 and 46).
- **One small thing:** "Tonight, pull the stopper out of the bathroom sink and look at it. That's the whole decision sitting in your hand." [12:31].

### Rule breaks

1. **A run-back of all four items before the end.** "Now, which bottle goes where? Because this is where people get it wrong. Kitchen sink gets the soap and the kettle first, and washing soda when that only half works. Bathroom sink, tub, and shower get peroxide and the zip strip for the hair. The toilet gets the soap pour for a paper clog, and vinegar down the overflow tube for a weak flush. The laundry standpipe gets washing soda with the washer off." [10:58]. Rule: `plumbing-scripts/SKILL.md`, "Point then promise" ("No recaps at the end") and `core/greenlight-audit.md` B9 ("recaps anywhere in the script"). Fix: cut it; the items already said which drain each bottle is for. (Reading: it may help some viewers; but it's 40 seconds of repeats, and the pack's length rule calls a restated point padding.)
2. **Two money figures in the opening:** "you're out 10 bucks" and "not one of them cost more than four bucks" [0:00]. Rule: "One dollar figure at most in the opening" (`plumbing-scripts/SKILL.md`, "The opening"). Minor; the first line is the strongest in the nine, so the fix is to say the second in words ("and every one of them is cheaper than the jug").
3. **The mid-video CTA comes after item 2 of 4** (at about 5:49, 43%). Rule: `plumbing-scripts/SKILL.md`, "CTAs" (Roger): "never before the end of item 3". See the channel section (short lists).

### Facts worth checking

- **"not one of them cost more than four bucks"** [0:00] and **"A dollar a bottle"** [12:00], measured against the price guide: washing soda (55 oz) about $5 to $6; white vinegar (1 gallon) about $4 to $5. Peroxide (about $1) and dish soap fit; two of the four don't. The title's "$3 FIX" is never said in the script. Viewers check shelf prices while they watch (the pack's "Money framing": "Peroxide is now priced close to 5.00 since COVID"). Fix: "and none of them costs more than a few bucks".
- **"White plastic drain pipe is only rated to about 140°"** [1:34]: the PVC figure is right (140 degrees Fahrenheit); fine as general knowledge.
- **Vinegar down the overflow tube "because the tube feeds the rim"** [7:52]: correct.
- **Peroxide and vinegar make peracetic acid** [7:52]: correct.

### Voice/caption oddities

- **"The slime is is It's sticky"** [3:40]: the voice seems to stumble. Worth a listen.
- **"Now, >> [snorts] >> where it stops."** [12:31]: a snort and a speaker change in the middle of the stop-sign line. Worth a listen.
- "[snorts]" twice more, mid-sentence: "First, [snorts] pull the stopper" [4:12], "three or four [snorts] bucks" [5:15].
- "no pore cleans what's sitting on the stopper" [4:12] is "no pour".

### Numbers

| | |
|---|---|
| Length | 13:32 |
| Caption words | 2,178 |
| Words a minute | 161 (the slowest of the nine) |
| Minutes at 170 | 12.8 (passes) |
| First real item | Number one at about 0:43 (scanner: about 44 seconds at 170) |
| Opening promises | 0 (count line only) |
| Mid CTA | about 5:49 (43%), after item 2 of 4 |
| End CTA | about 13:08 |
| "you" / "but" / "I" per 1,000 | 25.7 / 2.3 / 4.1 |
| Question marks (approx.) | 5 |
| Scanner | 28% of sentences six words or fewer (the most clipped of the nine); longest sentence 34 words |

---

## 6. "How to Unclog a Drain For Beginners" (`AGp_vAn5hqI`)

Published 2026-10-31 · 12:06 · 2,500 views at collection.

**In one line:** a good beginner's escalation (slow, clogged, blocked) with the main-line stop explained better than anywhere else on the channel; but it lists the three tools in the opening and twice more, item one is late, and the CTA comes after level one of three.

### What works

- **The escalation line, as P17 describes it:** "We'll start with a sink that drains slow, move up to one that stands full for minutes, and finish on the one where nothing goes down at all." [0:30]. The body keeps that order.
- **A question the viewer answers in their own sink:** "Does the water in your bathroom sink sit there for a minute after you pull the plug? That's a clog starting." [0:00].
- **The why, in one sentence, for a beginner:** "Water doesn't compress, so every stroke you push goes straight at the plug. Ever plunged a sink and felt nothing push back? That's air escaping." [5:10].
- **The beginner mistakes a plumber would catch:** the overflow slot, the second bowl of a double sink ("the two bowls share one drain, so you need a wet rag or a second plunger pressed over the other side" [5:10]).
- **Safety in one line, with its reason:** "If you already poured a chemical drain cleaner down there, do not plunge it and do not snake it." [7:16]; "That's not a scare line. That's the one way a beginner gets hurt on this job." [7:46].
- **The main line stop, with what to do while waiting:** "Stop running water, every tap, every flush, because every gallon you send down has nowhere to go but back up through the lowest drain you've got. Then make the call." [10:25].
- **Tenure once, at the stop sign:** "45 years of this and that's the one rule I'd put over the door." [10:25].
- **Book match correct:** "Pages 42 to 45 walk the plunger, the stopper, and the trap the same way. And page 56 has the main line warning signs." [3:37].
- **One small thing:** "So, go pull the stopper on the slowest sink in your house tonight and see what comes up with it." [11:27].

### Rule breaks

1. **A tool list in the opening, and the kit named three times.** "A drain strip, a cup plunger, and a hand snake do the same job, and all three cost less than half of one visit." [0:30]; each is named again at its step ("the first tool, the plastic drain strip" [1:32]; "The tool is a cup plunger." [4:38]; "Here's the second tool, a hand snake" [6:14]); and a third time before the end: "So, the money. A strip, a plunger, a hand snake. Under $50 for all three" [10:55]. Rule: `plumbing-scripts/SKILL.md`, "The opening": "No tool list in the opening, and the kit is named once in the whole video … never both and never twice" (operator, 2026-10-29: "same with the tool kit being listed twice"). Fix: open on "three cheap tools" without naming them; keep each tool in its own level; close on the money in one line ("All three together cost less than one visit") without the list.
2. **Level one lands at about 0:51.** Scanner: "item one at word 152 (about 54 seconds at 170)". Rule: the first real step by about 45 seconds (about 130 words for Roger). Fix: cutting the tool list in break 1 fixes this too.
3. **The mid-video CTA comes after level one of three** (at about 3:46, 31%). Rule: `plumbing-scripts/SKILL.md`, "CTAs" (Roger): "never before the end of item 3". Its timing is right; with three levels the item rule can't be met. See the channel section.

### Reading, not a rule

- **"And the trade knows it. There's a reason the snake's the first thing out of the truck."** [7:46]. It stops short of a motive, but "the trade knows it" and "there's a reason" claim to know what plumbers think, which the pack's villain rule steers away from ("Claiming to know what plumbers secretly do … drew the most-liked doubt in our data"). Two facts would do it: "The snake is the first thing out of the truck. You just bought your own."
- **The escalation line is close to the pack's own example** ("We'll start with a sink that's draining slow and work up to a toilet that won't go down at all."). Ours: "We'll start with a sink that drains slow, move up to one that stands full for minutes, and finish on the one where nothing goes down at all." [0:30]. Under the copy guard's 8 words, but the pack says its examples show "a shape; the script never reuses their wording".
- **The comment ask asks three things:** "tell me which drain in your house is slow right now, what level it's at and what you've already poured down it." [11:27]. The pack asks for "one specific question … plus one small detail".

### Facts worth checking

- **"boiling water can crack the porcelain in the sink, too"** [2:04]: cracking is mainly a toilet-bowl risk; a sink is less likely, and the PVC point before it is the real reason. Fine; a reading.
- **"Washing soda … eats grease and soap scum without touching the pipe."** [2:36]: "without touching the pipe" is a strong word for a strong alkali on old metal. A reading.
- **Prices:** "$100 to $300" and "1 and 1/2 to 3 times that" after hours [0:00] trace exactly to the guide; strip "about $3" [1:32] and snake "$25 to $35" [6:14] trace.

### Voice/caption oddities

- **">> [sighs and gasps] >>"** right after "there's no shame in that." [10:55]. Worth a listen: a gasp after the reassurance line would undercut it.
- "[clears throat]" twice, mid-sentence: "you're buying [clears throat] level three" [1:01]; "Some houses, [clears throat] older ones especially" [9:21].

### Numbers

| | |
|---|---|
| Length | 12:06 |
| Caption words | 2,071 |
| Words a minute | 171 |
| Minutes at 170 | 12.2 (passes, by six seconds on the clock) |
| First real step | Level one at about 0:51 (scanner: about 54 seconds at 170) |
| Opening promises | 0 (escalation line only) |
| Mid CTA | about 3:46 (31%), after level 1 of 3 |
| End CTA | about 11:45 |
| "you" / "but" / "I" per 1,000 | 27.5 / 3.4 / 2.9 |
| Question marks (approx.) | 6 |
| Scanner | "That's the whole job" once (allowed once); "no shame in" once (allowed once) |

---

## 7. "The Absolute BEST Way To Clean Your Toilet In 2026" (`6VK_UQJ7kHQ`)

Published 2026-10-30 · 12:57 · 13,000 views at collection (the channel's second best).

**In one line:** the strongest first 30 seconds of the nine and good teaching all the way through (drop the water first, acid for mineral, the black-light floor check), but the opening is the shape P10 and P18 ban (a run-down of four later steps), step one comes at about 1:25, and "None of this needs a plumber" is followed by a wax-ring call.

### What works

- **The narrator's own opinion as the first line, then the answer:** "I'll never understand why people keep pouring bleach on a toilet ring. The absolute best way to clean your toilet is eight steps done in one order. And that brown ring at the waterline gets citric acid overnight, not bleach." [0:00].
- **A question with the viewer's own answer, then the blame shift:** "When did you last scrub that ring? Last week, probably. And the week before." [0:00]; "That isn't you doing it wrong. Bleach can't touch what that ring is made of." [0:31].
- **The outrage at a big price, as his reaction:** "And this is the part that gets me. Every year, folks pay somewhere between $250 and $800 to have a perfectly good toilet hauled out and a new one put in over a stain that comes off for pocket change." [0:31].
- **A step nobody teaches, with the physics in one line:** "That rush of water starts a siphon, the same pull that empties the bowl when you flush." [2:04]; "Can your cleaner work through 2 in of toilet water? It can't." [2:36].
- **The why behind the fix:** "But, bleach kills germs. It can't dissolve mineral. All it does is fade the color." [5:45]; "And if your ring is orange, that's rust, and bleach can set it darker." [5:45].
- **Tenure once, before a verdict:** "I've been in this trade 45 years, and bleach on a mineral ring is about the biggest waste of elbow grease I know." [6:16].
- **The safety rule, flagged and plain:** "Acid and bleach never go in the same clean. Citric acid, vinegar, or limescale remover mixed with bleach gives off chlorine gas." [7:48].
- **Disgust where the topic has it:** "You'll find a black slimy crust that never sees daylight." [3:39]; "turn off the bathroom light and shine a cheap black light at the floor, and that halo lights right up. It's a little sickening the first time." [9:56].
- **Mid-video CTA at about 4:53 (38%), tied to the step just given, book match correct:** "By the way, if skipping those tablets just saved you a flapper and an ugly water bill" [4:41]; "The food coloring test that catches a silent tank leak is on page 37, and the running toilet and flapper fixes are on pages 48 and 49." [4:41] (Fixes 28, 37, 38).
- **A cost per use whose arithmetic holds** (a cup of citric acid weighs roughly half a pound, so a 5-pound bag is about 10 to 20 doses): "A 5-lb bag covers somewhere around 10 to 20 cleanings" [6:47].
- **The comment ask:** "Leave me a comment and tell me what color your ring is. Brown, orange, gray, or pink? And how many people share that bathroom? I read everyone." [12:31].

### Rule breaks

1. **A promise block in the opening: five promises.** "none of it hurts a septic tank as long as you check one label I'll point you to. Step two costs nothing, and it's the reason your cleaner never reached that ring. Step four is where that ring finally lets go. Right after it comes the rule that keeps every bit of this safe, because two of these products must never meet in the same bowl. And step six finds the bathroom smell nobody can ever track down." [0:31]. Rules: `plumbing-scripts/SKILL.md`, "Never in an opening": "any promise but the one end-of-video promise above, a promise block or any run-down of what later items hold" (P10, operator 2026-10-25); "One end-of-video promise, at most" (P18, 2026-10-29); job 5: the count line "never says what any single item holds". All four are paid mid-video (step 2 at 2:04, step 4 at 5:24, the rule at 8:07, step 6 at 9:56), not at the end. Fix: keep "eight steps done in one order" as the count line and go straight to step one. (This was published the day after the P18 rules went on the account; it may have been scripted before. See the channel section.)
2. **Step one lands at about 1:25.** Scanner: "item one at word 237 (about 84 seconds at 170)". Rule: first real step by about 45 seconds (130 words). Fix: break 1's cut brings step one to about 0:55; the rest of the opening is the strongest on the channel and can stay.
3. **"None of this needs a plumber", then a call.** "None of this needs a plumber, and none of it hurts a septic tank" [0:31], then step six: "you're looking at the wax ring, the seal under the toilet letting water out. That's a call." [10:29]. Rule: `plumbing-scripts/SKILL.md`, "The opening" job 4: "Never a blanket 'nothing here needs a plumber' … when the video has a point where the viewer stops and calls: say where it stops instead" (operator, 2026-10-29). The scanner's judge check looks for "nothing here needs a plumber" and missed "None of this needs a plumber" (a gap worth noting for the scanner). Fix: "Everything here is yours, right up to a wet floor at the base."

### Facts worth checking

- **"Every year, folks pay somewhere between $250 and $800 to have a perfectly good toilet hauled out and a new one put in"** [0:31]. Price guide: new toilet installed "$300 to $800". The $250 isn't in the guide; it may be from the brief. Measured.
- **"About 85% of homes in this country have hard water"** [5:24]. A commonly quoted figure (it usually refers to the share of the US with hard water, from the USGS), not in the price guide; fine as general knowledge, but it's said as a fact about homes. Worth checking against the brief.
- **"a silent leak like that can waste up to about 200 gallons a day"** [4:09]: traces to the guide (EPA: up to 200 gallons a day).
- **"$1 to $2 a dose"** for citric acid [6:47]. The guide prices citric acid at "about $10 to $15" a pound, which would make a 5-pound bag $50 to $75 and a dose $2.50 to $7.50. Real 5-pound bags sell for far less than five 1-pound bags, so the script may be right and the guide's row the outlier; worth checking either way, as viewers check these prices.
- **The step-two technique, bleach on rust, pumice wet only, acid and bleach never together:** all correct.

### Voice/caption oddities

- **Eight ">>" marks and seven sound tags,** the most of the nine, clustered around 7:18 to 11:00: ">> [sighs and gasps] >>" after "Those are the little holes under the rim that send water down the bowl when you flush." [7:18]; ">> [clears throat] >>" [8:52]; ">> [snorts] [sighs and gasps] >>" right after the wax-ring price [10:29]. Worth a listen: if the voice really gasps and snorts there, a viewer will hear it.
- "2 in of toilet water" [2:36] is "2 inches"; "5-lb" [6:47] is "5-pound": caption shorthand.

### Numbers

| | |
|---|---|
| Length | 12:57 |
| Caption words | 2,123 |
| Words a minute | 164 |
| Minutes at 170 | 12.5 (passes) |
| First real step | Step one at about 1:25 (scanner: about 84 seconds at 170) |
| Opening promises | 5 (the label, steps 2, 4 and 6, the rule) |
| Mid CTA | about 4:53 (38%), at the end of step 3 of 8 |
| End CTA | about 12:31 |
| "you" / "but" / "I" per 1,000 | 28.3 / 5.2 / 4.2 |
| Question marks (approx.) | 9 |
| Scanner | 5 items found (steps 1-5; "Step six" isn't said as a signpost and steps 6-8 run on); two sentences over 35 words; echo "all the way around" three times |

---

## 8. "NEVER Call A Plumber Again! How To Install a Toilet FAST Without Leaks" (`jXZrwNkf4qQ`)

Published 2026-10-29 · 15:29 · 2,700 views at collection.

**In one line:** a thorough, safe 15-step how-to with a running tally and a useful soft-floor stop; the opening previews steps 4 and 7, the close runs back over the job, most steps have no narrator verdict, and the title's "NEVER Call A Plumber" sits against the video's own (honest) call point.

### What works

- **The stake nobody sees, in plain words:** "A bad toilet seal doesn't always leave a puddle. The water can run straight down into your floor and rot the wood under your feet while the bathroom looks perfectly fine." [0:00].
- **A myth handled fairly and scoped:** "And that video going around where somebody sets a toilet down on a bead of silicone, no wax ring, no bolts, skip it. Most codes in this country want a toilet sealed on a ring and bolted to the floor" [0:33]. "Most codes", never "illegal", as the pack asks.
- **Safety, one line where the risk is:** "don't force it. An old valve can snap off in your hand and then you've got water you can't stop." [1:04]; "The rag keeps sewer gas out of your house and keeps a drop nut from vanishing down the drain." [2:06].
- **The honest stop, with its trigger:** "press on the floor around it. If it's soft or spongy, stop. That's rot and that's a call for a plumber or a carpenter before any toilet goes back down." [4:43].
- **The running tally, promised and closed** (the pack's money device): "Keep a tally as we go because we're going to stack it up against that plumber's bill at the end." [6:49], closed: "Under $40 in parts, all in, against that plumber's bill from the start." [14:06].
- **Tenure once, before a verdict:** "I've been in this trade 45 years and when a brand new toilet leaks at the base, a low flange is the first thing I'd check." [4:12].
- **Reassurance in the right place:** "Worried you'll crack the porcelain? Your weight won't. That toilet is built to hold a person every day. What cracks it is a wrench, and that's the next step." [8:22].
- **The test, with what the viewer will see:** "Water you can't see shows up on a dry paper towel right away as a dark spot." [12:31].
- **Book match correct:** "The toilet that rocks and the leak that turns out to be a floor problem are both on pages 50 and 51." [6:17] (Fixes 41 and 42).
- **The comment ask:** "Tell me what year your house was built and whether the toilet in it is still the one it came with. I read every one." [15:08].

### Rule breaks

1. **The opening previews two later steps.** "There are 15 steps. Step four is the one that decides whether a new toilet leaks at the base and it's also where you find out if your floor has gone soft. Step seven is where people wreck their own seal without ever knowing it." [0:00]. Rules: `plumbing-scripts/SKILL.md`, "Never in an opening": "a promise block or any run-down of what later items hold" (P10, 2026-10-25); job 5 ("It never says what any single item holds"); P18 (two promises, both paid mid-video). Fix: "There are 15 steps." and straight to the silicone warning and step one.
2. **Step one lands at about 0:59.** Scanner: "item one at word 183 (about 65 seconds at 170)". Rule: first real step by about 45 seconds. Fix: break 1's cut does it.
3. **The close runs back over the job.** "No silicone shortcut, either. Your toilet's bolted down, sealed on a proper ring, and tested 10 times over. And if that seal ever does give out someday, it'll tell you at the back before it ever gets into your floor." [14:38]. The tally close before it is the pack's money device and is fine; this is a run-down of what was just built. Rule: `core/greenlight-audit.md` B9 ("a run-down of what was just built counts"); `core/retention-mechanics.md` §14. Fix: cut to the tally and "You can stand in that bathroom tonight and know it's done right." [14:38].
4. **Most steps have no narrator verdict.** Scanner: no "I" line in steps 1, 3, 6, 7, 8, 9, 10, 11, 12 and 14 (10 of 15). Rule: `plumbing-scripts/SKILL.md`, "Emotion" 10: "One short 'I' opinion or verdict in most items". "I" runs 2.3 per 1,000 words, the lowest with #9 (2.4). Fix: one short line per step in Roger's voice ("I'd buy the thick ring every time on an old floor").

### Facts worth checking

- **The title against the video.** "NEVER Call A Plumber Again!" while the video, rightly, says "that's a call for a plumber or a carpenter" [4:43]. The pack: "Only a title that promises no plumber ('NO Plumber') is said that way, and then the video has no call point." The script made the honest choice and never repeats the title's claim; the conflict belongs to the title, at ideation. "FAST" is also never paid (the script says "one afternoon" [0:00]).
- **"a plumber charges about $450 to do this job"** [0:00] and **"labor on this job runs $150 to $440, depending on where you live"** [2:06]. Neither is in the price guide (wax ring reset $100 to $300; new toilet installed $300 to $800), and the two don't quite agree with each other. They may be from the brief. Measured.
- **"Caulking all the way around the base hides a leak instead of stopping it."** [13:03]. Leaving the back open is common advice, but some local codes and inspectors want the base sealed all round. Said flatly as fact; worth a "check what your town wants" or a check against the brief. A reading.
- **Flange height, the shims (plastic, not wood), even tightening, the 10-flush paper-towel test:** all sound.

### Voice/caption oddities

- **"[sighs]" right before "I think that's an ugly number"** [2:38], and **"[clears throat]" inside it** ("I think that's an ugly number [clears throat] for lifting a toilet"). Worth a listen. "[clears throat]" twice more mid-sentence [8:22, 10:26] and "[snorts]" [12:01].

### Numbers

| | |
|---|---|
| Length | 15:29 |
| Caption words | 2,616 |
| Words a minute | 169 |
| Minutes at 170 | 15.4 (passes) |
| First real step | Step one at about 0:59 (scanner: about 65 seconds at 170) |
| Opening promises | 2 (steps 4 and 7) |
| Mid CTA | about 6:05 (39%), after step 5 of 15 |
| End CTA | about 15:04 |
| "you" / "but" / "I" per 1,000 | 38.6 / 4.6 / 2.3 |
| Question marks (approx.) | 9 |
| Scanner | 15 steps, 113-248 words each; no "but" in steps 2, 5, 11, 15; two sentences over 35 words |

---

## 9. "Does Green Gobbler ACTUALLY Work? (And 3 BETTER Ways To Unclog Drains)" (`8NJL9eGeLcs`)

Published 2026-10-29 · 14:42 · 1,200 views at collection.

**In one line:** a fair, well-researched verdict that answers the title in its first sentence and gets the dose arithmetic right, but it spends four minutes on the product before any fix, previews the three ways in the opening, pitches the book before the first way, and uses loaded lines about a named company.

### What works

- **The title's question answered in the first sentence, scoped by clog:** "Does Green Gobbler actually work? On a bathroom sink slowed down by hair and soap scum, it can, but slowly and usually overnight. On a kitchen drain packed with food or grease, it's the wrong bottle. And on a bottle cap or a toy, it does nothing at all." [0:00].
- **The failed attempt:** "And if you've already poured one in, gone to bed hoping, and come back in the morning to the same gray water sitting in the sink, you know exactly how that feels." [0:00].
- **Fair to the product, which the pack asks of verdicts:** "Now, does a gentler label mean it's useless? No. Gentle is good news if you've got old pipes, but gentle also means slow" [2:04]; "That wasn't the bottle failing a fair fight. It was the wrong tool sent to the wrong job." [3:37]; "I'll give them credit for saying it." [4:09].
- **Dose arithmetic checked and right** (the pack's Proof rule): "For a toilet, it's 32 oz, which is a touch more than the whole 31-oz bottle, and it sits at least 2 hours. So, one bottle is just shy of two sink doses, and it doesn't quite cover a single toilet." [4:39]. 31 / 16 = 1.94.
- **The money verdict that says when the pro is the cheap option:** "That's the one time paying somebody is the cheap way out." [13:27].
- **Practical saves inside the steps:** "Bail the standing water out of the sink first, or it all comes down into the cabinet the second the trap comes loose." [8:48]; "If it's old metal that flakes when you touch it, stop there." [9:50].
- **Safety in one line, with the reason:** "If you already poured a caustic drain cleaner down there, the lye kind, do not plunge that sink. It splashes back up out of the drain, and it doesn't care whether your face is in the way." [11:54].
- **The comment ask:** "tell me which drain clogs first at your place and what you poured down it the last time you were hoping a bottle would save you a call. I read everyone." [14:29].

### Rule breaks

1. **A promise block in the opening: three promises.** "Way number two pulls out the things no liquid can touch, and all it takes is two plastic nuts and a bucket. Way number three is for grease, and it comes with the one safety rule that keeps a drain chemical out of your eyes. And after the three, the one sign that means it isn't your sink at all" [0:32]. Rules: `plumbing-scripts/SKILL.md`, "Never in an opening" (P10) and P18. The count line before it ("here's the honest verdict on the bottle, and then three ways to beat it, each one matched to the clog it's made for." [0:32]) is all the opening needs.
2. **The first fix comes at about 6:15.** "First, what you're really buying." starts at about 1:30, and the product history, the other channel's test and the dosing run to about 5:40. Scanner: "item one at word 1028 (about 363 seconds at 170)". The verdict is in the first sentence (point first holds), but the first thing the viewer can do arrives at 4:36 (the label dose) and the first of the three ways at 6:15. Rule: `plumbing-scripts/SKILL.md`, the video-type table (head-to-head verdict: first tip by 45-60 seconds) and "The opening" (first real tip by about 45 seconds). The viewer note in the pack: "3:15 is where it starts." (2K likes). Fix: cut the packet history to two lines and the other channel's test to one, and start way one by about 2:00.
3. **The mid-video CTA comes before any of the three ways.** "By the way, before the first of the three, if that just kept a bottle out of the wrong drain" [5:41]. Rules: `plumbing-scripts/SKILL.md`, "CTAs" (Roger): "never before the end of item 3"; `core/cta-and-endings.md` §2: "Goes right after the first real payoff … never before the first delivered value". Fix: after way one's win ("you just did it in about 6 minutes and the bottle never left the shelf." [7:46]).
4. **Loaded lines about a named company.** "The front of that packet talked about green and biodegradable, but the label on it said danger, causes burns. Same packet. That's the store shelf for you. The friendly word goes on the front in big letters, and the warning goes where you have to hunt for it." [1:30]; "gentle also means slow, and slow is the part they don't print in big letters." [2:04]. Rules: `core/claims-policy.md`, "Named companies and people": "Nothing false or unsupported is ever stated as fact about a named company"; `plumbing-scripts/SKILL.md`, "Banned": "anything negative stated as fact about a named company" and "The villain": "Never a named company". The label facts may be true and in the brief; "where you have to hunt for it" and "the part they don't print in big letters" say why the company did it, which is the motive the pack keeps off even the trade. Fix: keep the facts (what the old packet said, what the new label says) and drop the "why".

### Facts worth checking

- **"If you bought Green Gobbler, there's already one sitting in the box."** [6:43]. Earlier the free zip tool came with "the old powder" [3:07]; the bottle on sale now is a liquid. Whether today's bottle comes with a tool needs checking against the brief.
- **"Its own answers page says it works on hair, soap scum, toilet paper, wipes, and other organic matter."** [4:09]. "Wipes" from a liquid is a surprising claim, and every other video on the channel says wipes need a tool or a call. Check the brief's wording.
- **"Angie's 2026 numbers put a standard main line clearing at $147 to $352"** [13:27] (Angi). Not in the price guide (main line snaking $150 to $500); a named source said with its own figure, which the pack allows "only rarely, where it really helps", so it must come from the brief. Measured.
- **"A 31-oz bottle runs about $14"** [2:04]: the guide has Green Gobbler only by the gallon (about $25). From the brief, presumably. Measured.
- **"A plumber with a big following put the old powder through a hard test on camera."** [2:36]: someone else's test, told without "I" and without a name. The pack allows tests "when the brief gives them, said without 'I'". Fine if it's in the brief.

### Voice/caption oddities

- **"[snorts]" mid-sentence, three times:** "swell, [snorts] and pack in solid" [3:37]; "Way number one, for [snorts] hair." [6:11]; "Food [snorts] is where the bottle really loses." [7:46]. And **">> [sighs and gasps] >>"** right after "Way number three, for grease." [10:20]. Worth a listen.
- "Angie's" is "Angi's" (the company renamed itself in 2021); if the voice says "Angie's", it's fine to the ear.

### Numbers

| | |
|---|---|
| Length | 14:42 |
| Caption words | 2,485 |
| Words a minute | 169 |
| Minutes at 170 | 14.6 (passes) |
| First real item | the label dose at about 4:36; Way number one at about 6:15 (scanner: about 363 seconds at 170) |
| Opening promises | 3 (ways two and three, the main-line sign) |
| Mid CTA | about 5:41 (39%), before way 1 of 3 |
| End CTA | about 14:15 |
| "you" / "but" / "I" per 1,000 | 35.4 / 7.6 / 2.4 |
| Question marks (approx.) | 8 |
| Scanner | three sentences over 35 words (longest 42); one reframe (allowed one); "PVC", "ABS", "VOCs" said as letters (judge) |

---

## The channel: patterns across the nine

A pattern here means three or more videos.

### What the channel now does well (measured)

- **Length: fixed.** All nine pass 12 minutes at 170 (12.2 to 15.4). The 2026-10-29 review found the plumbing scripts "all coming short"; Roger's now aren't, and his voice ran 161 to 173 words a minute, so the profile's 170 is right.
- **The ending: fixed on all nine.** One end CTA naming the link and the QR code, then a comment ask with a real question and "I read every one", nothing after it. Seven of nine close on one small thing to do tonight ("Tonight, pull the stopper out of the bathroom sink and look at it." #5 [12:31]); none uses "tonight's homework" (the Werner fault of 2026-10-29).
- **The book match: right on all nine.** Every page number checks against the book's fix index (pages 37, 42-45, 48-51, 56).
- **Tenure once on all nine,** always 45, always beside a verdict or a stop sign.
- **The main-line stop sign** ("two drains backing up at once") is in all nine, as a call with its trigger, the way the pack asks.
- **Two facts side by side, not "because":** every silence line in the nine is the pack's shape ("Nobody in the trade mentions the jets. And a new toilet installed is a bill in the hundreds." #5 [7:52]). No line joins the trade's price to its silence with "because", "so" or "since".

### Patterns to fix

1. **The promise block in the opening: 3 videos (#7, #8, #9), all three of the oldest.** Five, two and three promises of later steps. Banned since 2026-10-25 (P10); P18 (2026-10-29) allows one promise, paid at the end. **None of the six later videos (#1 to #6, 2026-10-31 to 11-04) has one** (measured). So this has likely already stopped, perhaps because the 10-29 rules reached the account after these three were scripted (a reading: the scripts' dates aren't known).
2. **The first real item is later than 45 seconds: 5 videos** (#4 1:09, #6 0:51, #7 1:25, #8 0:59, #9 6:15). Three of them are the promise-block videos; #4 and #6 are later and have no promise block, so the long opening is still happening without it: #4 runs two symptom sentences, the cause and a price before item one; #6 lists the tools.
3. **The scope line walked back: 3 videos.** #2 "Nothing here touches a chemical" (then peroxide), #4 "Nothing here needs a tool you don't already own" (then a $3 strip), #7 "None of this needs a plumber" (then a call). The 2026-10-29 rule covers the plumber case; the same habit shows up with tools and chemicals. The fix is the same: say where it stops, not that it never does.
4. **The mid-video CTA before the end of item 3: 4 videos** (#3 after item 2 of 5, #5 after item 2 of 4, #6 after level 1 of 3, #9 before way 1 of 3), and **past halfway on #4** (56%, after item 3 of 6). All five are short lists. Roger's rule says "about a third of the way in, never before the end of item 3", written for lists of 10 to 15; with three to six items the two halves can't both hold. The VAs (or the writer) chose "a third" every time. **This is a gap in the rule, not a writing fault:** the operator could say which wins on a short list. A suggestion only: "after the first item's win and about a third of the way in; never before item 3 in a list of 10 or more".
5. **Sound tags in the captions on all nine** (measured: 30 tags; 22 ">>" marks): "[snorts]" 11, "[clears throat]" 11, "[sighs and gasps]" 5, "[sighs]" 3, "[laughter]" 1. Many fall mid-sentence ("three or four [snorts] bucks" #5 [5:15]; "an ugly number [clears throat] for lifting a toilet" #8 [2:38]). YouTube's caption system writes these when it hears a non-speech sound, so the voice (ElevenLabs "Ron") is very likely making breaths, sighs or snorts the script didn't ask for, or the scripts carry voice tags. Worth one listen to #7 (8 ">>" and 7 tags) at 7:18, 8:52 and 10:29 to decide whether it's audible and needs a voice-settings change.
6. **The grease "like candle wax on a holder": 6 videos** (#1, #2, #3, #5, #6, #9). It's in Roger's profile as an example of his analogies, but the pack's voice rule says "a phrase is voice once; in the same slot every video, it's a tic". The first-Saturday coffee routine is in 5 (#1, #2, #3, #6, #9) and "makes me sick" in 4 (#4, #5, #6, #7); both are allowed, but a viewer who watches three in a row will hear them three times. A reading, not a rule.

### Compared with the 2026-10-29 review (Werner)

| Werner's faults, 2026-10-29 | Roger, 2026-10-29 to 11-04 |
|---|---|
| Under 12 minutes (11:06) | fixed: all nine 12:06+ |
| Promises in the opening | in #7, #8, #9 (the three oldest); none after 10-30 |
| First step at 1:04 | still late in 5 of 9 |
| The kit listed twice | once: #6 (three times) |
| "Nothing here needs a plumber", then a call | once as a plumber (#7), twice as tools or chemicals (#2, #4) |
| A "because" between the trade and its silence | none |
| A homework list at the end | none; one run-back of the job (#8) and one of the items (#5) |

### Top 3 fixes

1. **Fix #3's title** (or take it down): the cube video is under the liquids video's title. It's the only HOLD-level fault in the nine and the only one a viewer can see without listening.
2. **Get item one in by 45 seconds on every video:** no previews of later steps, no tool list, no second symptom sentence. Five of nine miss it, and the two that miss it without a promise block (#4, #6) show it's a habit of its own.
3. **The scope line says where it stops, never "nothing" or "none":** for plumbers, tools and chemicals alike (#2, #4, #7). One sentence, and the scanner's judge check could be widened to "none of this needs a plumber" (the operator's call; nothing changed here).

Also for the operator to decide: which half of the mid-CTA rule wins on short lists (pattern 4), and one listen to the voice's sighs and snorts (pattern 5).
