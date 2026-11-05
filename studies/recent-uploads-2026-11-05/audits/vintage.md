# The Vintage Pipefitter: audit of the seven newest uploads (2026-11-05)

**Channel:** The Vintage Pipefitter, `UCyImxEdbXY3x0w51WQtOG9Q`. Persona `personas/vintage-pipefitter.md`, pack `plumbing-scripts/SKILL.md`, 190 words a minute (the profile's figure).

**Sources:** captions fetched with NexLev `get_bulk_video_transcripts` on 2026-11-05 (all seven came back, all "English (auto-generated)"); video lengths, publish dates and views from the 2026-11-05 collection. Saved as `transcripts/vintage-<videoId>.txt` (lines of about 30 seconds, words exactly as captioned). Left out on purpose: `yVwCoTug6d4`, a 2:50:14 compilation.

**Rules read:** `plumbing-scripts/SKILL.md` (whole), `personas/vintage-pipefitter.md`, `HANDOFF.md` §3 "Operator decisions, 2026-10-29", `PROPOSALS.md` P17 and P18, core `cta-and-endings.md`, `retention-mechanics.md` §14, `workflow.md` §6 (voiceover tags), `plumbing-scripts/references/price-guide.md`. The Vintage Pipefitter has no book and no mid-video CTA, so there is no book match to check.

**Cautions:**
- These are YouTube's automatic captions of the voiceover: **what the voice said, not the VA's script**. Caption punctuation is the caption system's guess, so sentence counts, question marks and "sentence over 35 words" flags are approximate (the long-sentence flags are left out below for that reason).
- The captions split the channel name ("Vintage Pipe Fitter") and write "1/2 in", "$2.00", "140°"; the scanner's flags on those are caption-made and left out.
- Timestamps are the start of the caption segment that holds the quoted words, so they can be a second or two early. Each quote can be found in the transcript line at or just before that time.
- The briefs for these videos are not in the repo. The plumbing fact source is the brief plus the price guide, so a price that isn't in the price guide may still have come from the brief. Where a figure differs from the guide, it says "differs from the price guide", not "wrong".
- No channel of the operator's is connected to NexLev, so there is no retention data. Views are public counts at collection, 1 to 7 days after publishing.
- The plumbing rules this review checks (12 minutes at 190 words a minute, one opening promise, first item by about 45 seconds, no "no plumber needed" line) were committed on 2026-10-29 at about 04:12-04:39 UTC. The 2026-10-29 video may have been scripted before the VAs had the new skills; when each script was written is not known.

**Scanner:** `python3 core/script-scanner.py <timestamp-stripped captions> --rules plumbing-scripts/SKILL.md personas/vintage-pipefitter.md --refs personas/vintage-pipefitter.md plumbing-scripts/SKILL.md plumbing-scripts/references/excerpts.md plumbing-scripts/references/voice-samples.md plumbing-scripts/references/models/*.md --pack plumbing-scripts/references/price-guide.md --title "<title>"`, run from a scratch copy. Its findings are quoted where they matter. Left out as caption-made: fractions, units, "$2.00", the degree sign, sentence-length flags, and the copy-guard hit "subscribe to the vintage pipe fitter for more" (S14), which only reaches 8 words because the captions split "Pipefitter" into two words.

---

## The answer to the last review's question

The 2026-10-28 check found **two of the channel's three newest videos under 12 minutes at his real speed, and one opening with two promises.**

- **The three newest videos (2 to 4 November): fixed.** All three run over 12 minutes (12:36, 14:00, 14:22; 13.4 to 14.8 minutes at 190), and none opens with more than one promise. "Why Your Sink Stopper Gets Stuck" carries one, "So, both get fixed here." [0:37], and it is paid at the end of the video (the push-button stopper, from 11:36), as P18 allows.
- **The four before them (29 October to 1 November): not fixed.**
  - **Three are under 12 minutes:** 10:27, 10:07 and 11:08 on the clock, which is 9.8, 9.8 and 10.6 minutes at 190.
  - **Four open with a run of two or three numbered promises.** Three of those run three, one more than the last review found.
  - **The 1 November video breaks both rules,** three days after they landed in the pack.
- **190 words a minute is right for this voice.** Across all seven videos the captions hold 16,676 words in 87.7 minutes, about 190 a minute. Single videos ran from 178 to 202.

| # | Video | Published | Length | Caption words | Words a minute | Minutes at 190 | 12 min? | Opening promises (beyond count or escalation line) |
|---|---|---|---|---|---|---|---|---|
| 1 | 4 Old-Plumber Powders | 11-04 | 12:36 | 2,544 | 202 | 13.4 | yes | 0 |
| 2 | Sink Stopper Gets Stuck | 11-03 | 14:22 | 2,803 | 195 | 14.8 | yes | 1, paid at the end (allowed) |
| 3 | Unclog a Toilet For Beginners | 11-02 | 14:00 | 2,638 | 188 | 13.9 | yes | 0 |
| 4 | Neighbor's Pipes Never Burst | 11-01 | 10:27 | 1,861 | 178 | 9.8 | **no** | **3** |
| 5 | NEVER Call A Plumber Again! 12 Secrets | 10-31 | 15:02 | 2,952 | 196 | 15.5 | yes | **3** |
| 6 | BEST Way To Clean Your Toilet | 10-30 | 10:07 | 1,855 | 183 | 9.8 | **no** | **2** |
| 7 | 8 Things You Should NEVER Pour | 10-29 | 11:08 | 2,023 | 182 | 10.6 | **no** | **3** |

**The length rule, checked carefully for the three short ones.**
- **What the rule says:** at least 12 minutes counted at 190 words a minute, which is about 2,280 spoken words (pack, "Length"; `HANDOFF.md` 2026-10-29: "Real speed, keep 12").
- **How short they were:** the three videos have 1,861, 1,855 and 2,023 words. That is 419, 425 and 257 words short.
- **Two measures, same result:** all three are under 12 minutes on the clock too (10:27, 10:07, 11:08). This voice read them a little slower than 190 (178 to 183), so the clock time is a bit longer than the 190 estimate. Neither measure reaches 12.
- **At the old speed they would have passed (reading, not a rule):** counted at the old 150 words a minute, the three come to 12.4, 12.4 and 13.5 minutes. That fits a length check still run at 150, or not run at all.

---

## 1. "These 4 Old-Plumber Powders Will Save You THOUSANDS in Drain Repairs" (`8vTWjM60GRM`)

Published 2026-11-04 · 12:36 · 698 views at collection

**In one line:** this is the channel at its best. It is a tight four-item list that names all four products in the first nine seconds, keeps the villain as plain billing facts, follows every safety default, and runs 13.4 minutes at 190. The only breaks are a closing run-back over all four boxes and one bare myth flag.

### What works
- **The point in the first breath, with the products named:** "Four boxes of powder, a few dollars a piece, and they'll do more for your drains than anything with a warning label. Washing soda, borax, citric acid, and baking soda." [0:00]. A check the viewer can run tonight follows: "That kitchen sink that takes a full minute to drain... Go time it tonight." [0:09]
- **The villain as two facts side by side, exactly the pack's shape:** "Clearing a mainline runs $300 to $600. And nobody in the trade mentions the four boxes that keep it from getting there." [0:22]
- **Honest scope in the opening:** "None of them opens a drain that stopped dead." [0:39]. It is repeated where it matters, with a named trigger: "If two drains back up at the same time or the toilet bubbles when the kitchen sink runs, that's bigger than one drain. That's the main line." [9:25]
- **Item one at 0:44** ("Number one, washing soda."), right on the 45-second line.
- **Safety by the book.**
  - Washing soda dissolved first in hot tap water, never the kettle: "Dissolve it first." [2:43]; "Hot tap, never the kettle." [2:57]
  - The jug rule: "If you poured a jug of drain cleaner down last night and the water's still standing, don't add this. Don't plunge it either." [3:37]
  - One cleaner at a time, with the reason in proportion: "Bleach and an acid together make a gas that'll put you on the floor." [10:00]
  - Borax kept out of reach: "Borax is harmful if it's swallowed, so keep it where the kids and the dog can't get at it" [5:55]
- **Crediting the old habit before correcting it,** as the pack asks for baking soda and vinegar: "you weren't wrong to try. And you didn't hurt a thing. But the foam was the show." [10:46]
- **The priority flag at the first answer:** "if you do one thing off this whole list, do this one in the kitchen on the first of every month." [3:30]
- **Disgust at the price, said as his opinion:** "Having a plumber swap that cartridge runs $150 to $300. For a part you could hold between two fingers, I think that's a crime." [7:17]
- **One small thing at the end:** "Tonight, half a cup of baking soda down the bathroom sink, run the hot tap after it, and go to bed." [12:06]. Then a one-line subscribe ask [12:19] and a specific comment ask with "I read every one" [12:26].

### Rule breaks
1. **A recap before the close:** "So here's the whole bill. Washing soda in the kitchen, borax in the bathroom, citric acid on the fixtures, baking soda wherever it smells. About $25 for the whole year." [11:39]
   - **The rule:** pack "Point then promise" ("No recaps at the end"), "Banned in these scripts" ("A recap at the end"), and core `retention-mechanics.md` §14. The running-total device is allowed; the run back over all four items is not.
   - **Fix:** keep the money line ("About $25 a year for all four boxes") and drop the list of which box goes where.
2. **A bare myth flag:** "The last one is the gentlest of the four, the cheapest, and the one everybody gets backwards. Number four, baking soda." [10:10]
   - **The rule:** pack "Ways to promise more value": a myth flag "names the belief it flips in the same line... Never a bare 'the one everybody gets backwards'".
   - **Fix:** name the belief in the flag itself: the fizz with vinegar was never what did the work.

### Facts worth checking
- **"Clearing a mainline runs $300 to $600"** [0:22]. Differs from the price guide (measured): snaking the main sewer is "$150 to $500; a stubborn one up to about $650", hydro jetting "usually $350 to $800". It may have come from the brief.
- **The history lines (unchecked; reading):**
  - borax "since 1891" [4:12]
  - "What they had through the whole of the 1800s was a box of washing soda in the kitchen" [1:55]
  - "The old plumbers had all four before the first jug of drain cleaner was bottled" [0:30]

  Citric acid as a household powder that early is the doubtful one. None of these is in the price guide; whether the brief carried them is unknown.
- **"Washing soda turns that fat into something close to soap"** [3:12] and **"Borax strips the soap film and kills the smell at its source"** [5:25]: both are broadly how these products are described, but they are stated as mechanisms. Reading: plausible, not checked.

### Voice and caption oddities (worth a listen)
- "Their maintenance." [0:39] is surely "They're maintenance."
- "a pitch of hot tap water" [2:39] is "pitcher".
- "airator" [6:41] and "the air raators" [8:56] (aerator). The second sounds like the voice stumbled.
- "Number three" is said twice: "Number three, works on the parts the first two never reach..." [6:17] and then "Number three, citric acid." [6:26]. Probably in the script.
- "The jetting then the snake won't cut it." [11:57] is probably "when". The sentence is hard to follow on one listen.

### Numbers (caption-based, approximate)
- **Length and speed:** 12:36; 2,544 caption words; 202 words a minute; 13.4 minutes at 190 (meets 12).
- **First item:** item one at 0:44 (word 143). This is the "N things about one product" type, whose first tip falls at 45-90 seconds.
- **Opening promises:** 0 beyond the count line ("Four boxes and each one has its own job.").
- **CTAs:** no mid-video CTA (correct for this channel); subscribe ask at 12:19; comment ask at 12:26.
- **Tenure:** once, at 0:34 ("45 years in the trade hasn't changed my mind about them").
- **Rates per 1,000 words:** "you/your" about 24; "but" about 2.8; "I" about 3.9.
- **Question marks:** 5.

---

## 2. "Why Your Sink Stopper Gets Stuck (And How to Fix It!)" (`ewBOEjJEzyY`)

Published 2026-11-03 · 14:22 · 266 views at collection

**In one line:** this is a thorough, honest repair video, with the best single safety-and-money passage on the channel (the hand-tight pivot nut and the paper-towel check). But a minute-long tour of the stopper's parts pushes the first real tip to 2:01.

### What works
- **A check in the first sentence, then the hidden cause and the fix:** "Reach behind your bathroom faucet and find the little knob that works the sink stopper. Pull it up. Does the stopper move?" [0:00]; "A broken part is almost never the reason." [0:12]; "The fix is 10 minutes under the sink and a cheap plastic strip." [0:26]
- **One opening promise, paid at the end, as P18 allows:** "That's the push button kind, and it sticks for its own reason. So, both get fixed here." [0:33]. The push-button stopper is the last section (11:36 to 13:26).
- **A scope line that doesn't overclaim:** "Nothing here needs a permit, a new pipe, or a single cut." [0:47]. It doesn't say no plumber, and the video's one call point is named plainly: "That's the one place on this job where I'd have somebody come out before you crack a sink pulling on it." [11:32]
- **The villain as two facts:** "Nobody in the trade mentions it, and a stopper call still bills at the trade's minimum." [6:48]
- **Disgust and pride, both landing:** "and it smells like something died in there" [6:32]; "It's disgusting, but that's the good news. Gunk you can see is gunk you can clean." [6:56]
- **The insistence line where it matters,** with the tenure doing a job: "Listen to me on this part because it matters more than the rest. 45 years in this trade and that little nut is still the one I see cranked down like it's holding up a bridge." [8:43]
- **A check the viewer can run, with both outcomes:** "wipe a dry paper towel under the nut. Dry towel? You're done. Damp towel? A quarter turn more with the pliers and check again." [9:37]
- **The kit is named once, in one short step after the opening** [4:37], as the pack allows.
- **The money close is the "three prices side by side" device, not a recap:** "$3 for the strip, $10 to $25 for a whole new assembly if it ever comes to that, and $100 or more for a plumber to do the same 10 minutes." [13:30]. Then one small thing: "Tonight, before bed, pull that knob up and watch the stopper." [13:47]

### Rule breaks
1. **The first real tip comes at 2:01 (word 400), not by about 45 seconds.** After the opening, "First, what you're dealing with under that sink." [0:53] starts a minute of anatomy: the lift rod, the clevis, the pivot rod, the ball, the tail, ending "That's the whole machine, two rods, a strap, a nut, and a stopper with a tail." [1:42]. The first cause and check only start at "The first reason it sticks is the gunk." [2:01].
   - **The rule:** pack "The opening" (first real tip by about 45 seconds, about 140 words for this channel; the "Hidden cause" row says 30-45 seconds) and "The viewer" ("Don't lecture on the cause").
   - **Fix:** go straight from the opening to the gunk. Name each part in the step that first touches it (the clevis at step six, the pivot nut at step two). Each part is already explained again there.

### Facts worth checking
- **"Fixing a cabinet floor like that runs $150 to $500"** [9:25]. Differs from the price guide (measured): "soaked cabinet floor $150 to $200; a stock cabinet swapped $250 to $600". The range joins two rows. It may have come from the brief.
- **"this is where the trade keeps a cheap secret"** [7:26]. Reading, not a rule: this edges toward the trade hiding fixes on purpose, the line the pack says drew the most-liked doubt. "Nobody in the trade mentions..." (which the script uses at 6:48) is the safer shape.
- Prices that match the guide: pop-up assembly "$10 to $25" (guide: part $10 to $25); "$100 or more" just to come through the door (guide: trip fee about $100 is common).

### Voice and caption oddities (worth a listen)
- **"The [snorts] barbs grab the hair"** [7:45]. The caption system heard a snort mid-sentence. `core/workflow.md` §6 allows only speaking tags in the voiceover copy (`[sighs]`, `[chuckles]` and others; "Never: sound effects"). Either a tag came out as a snort, or the voice glitched. Worth a listen.
- **"That's the thing that was stuck in your trash can. For the price of a cup of coffee, step five, put it back"** [8:15]. The pause landed in the wrong place, so "for the price of a cup of coffee" reads as part of step five.
- **"That's the stuck."** [6:33] and **"Same stuck, different place."** [12:09]. Odd as spoken English. Probably the script, not the voice.
- "10 minutes" is said four times (0:26, 4:25, 13:40, 13:54). The scanner's echo count (H18) flags "10" five times; reading, minor.

### Numbers (caption-based, approximate)
- **Length and speed:** 14:22; 2,803 caption words; 195 words a minute; 14.8 minutes at 190 (meets 12).
- **First tip:** the first real tip (reason one) at 2:01, word 400. The scanner's "item one at 270 seconds" counts "Step one" [4:27].
- **Opening promises:** 1, paid at the end (allowed).
- **CTAs:** subscribe ask at 14:01; comment ask at 14:10.
- **Tenure:** once, at 8:45.
- **Rates per 1,000 words:** "you/your" about 25; "but" about 4.6; "I" about 4.6.
- **Question marks:** 10.

---

## 3. "How to Unclog a Toilet For Beginners" (`7oNBRxJmjxE`)

Published 2026-11-02 · 14:00 · 573 views at collection

**In one line:** this is the cleanest script of the seven, and it follows the new rules almost to the letter. It has a two-sentence escalation opening, the first real tip at 0:45, and 13.9 minutes at 190. It also fixes the two faults the 2026-10-29 review found in Werner's video on the same title (the floor water and plunging a full bowl). No written rule broken.

### What works
- **The how-to opening in the pack's order:**
  - **the task:** "Your toilet's not going down." [0:00]
  - **the number-one mistake:** "The number one mistake is flushing it again to see if it goes, and that's how water ends up on the floor." [0:11]
  - **the trade's price:** "A plumber charges anywhere from $100 to $275 to put an auger down a toilet, depending on where you live." [0:20]
  - **the escalation line:** "We start at a bowl that drains slow and end at water over the rim and across the floor with a first move at every level." [0:28]
  - **when not to do it:** "The one thing that isn't yours is water coming up in the tub when you flush. That's the main line... That's a call." [0:36]
- **No extra promise, no tool list, the first real tip at 0:45:** "Before any of that, find the shutoff." [0:45]
- **Werner's two faults, fixed here.**
  - **The water to worry about:** "It's clean water in there." is said of the tank [5:03], and "Gloves on for all of this because the water in that bowl is not clean water." [7:03]. Werner's video called the floor water "clean tank water".
  - **No plunging a full bowl:** at level two the bowl is let down first: "Now, give it a few minutes. A clog usually lets a little water seep past, and the bowl drops on its own to a level you can work with." [5:09]
- **Safety defaults:**
  - "Hot, never boiling." [2:44]
  - "if somebody already poured a jug of drain cleaner in there, the plunger stays in the closet. It splashes and it burns." [7:07]
  - the snake rule, with the tenure doing a job: "45 years in this trade, and this rule hasn't moved an inch. A regular drain snake never goes in a toilet." [9:00]
- **The insistence line at the moment of danger:** "Listen to me on this one. Do not flush again." [4:26]
- **The money line as an opinion, aimed at the price:** "A plumber charges $250 to $550 to lift a toilet and set it back... I'll tell you, that number makes me angry" [10:35]
- **A small human touch that suits the audience:** "If there were guests in the house, nobody ever has to know." [7:28]
- **Honest call point, named by its trigger:** "Did water come up in the tub or the shower when the toilet overflowed? Are two drains in the house slow at the same time? Then the clog is out in the main line" [13:02]
- **One small thing at the end:** "Tonight, before any of this happens, go find the shutoff behind your toilet and turn it closed and open once" [13:23]

### Rule breaks
None found against the written rules.

### Facts worth checking
- **"That's the whole of what a plumber does for a paper clog, the visit I priced at the top of this video."** [7:14]. The opening priced an auger visit ($100 to $275), not a plunging visit. Reading: a loose callback, not a false one.
- **"The store sells both of them side by side, and not one word on that shelf tells you which is which."** [5:47]. Reading: most plunger packaging does say "toilet" or "sink", so a viewer may push back.
- **"the whole job is two nuts"** [10:51], said just before a two-minute walk-through of pulling and resetting a toilet. Reading: an understatement viewers may notice.
- Prices match the price guide (measured): "$100 to $275" with an auger, and "$250 to $550" if the toilet comes off (guide row "Toilet clog").

### Voice and caption oddities (worth a listen)
- **"Then there's no clog out. Hard water crusts them over and the flush loses its push."** [1:59]. "Them" has nothing to point to: the rim jets aren't named until "For the rim jets, there's no soaking." [3:34]. A sentence naming the rim jets looks dropped, by the voice or in the script. Worth a listen.

### Numbers (caption-based, approximate)
- **Length and speed:** 14:00; 2,638 caption words; 188 words a minute; 13.9 minutes at 190 (meets 12).
- **First tip:** the first real tip (the shutoff) at 0:45, word 149. "Level one" at 1:08.
- **Opening promises:** 0 beyond the escalation line.
- **CTAs:** subscribe ask at 13:38; comment ask at 13:47.
- **Tenure:** once, at 9:01.
- **Rates per 1,000 words:** "you/your" about 27; "but" about 3.0; "I" about 3.0.
- **Question marks:** 8.

---

## 4. "Why Your Neighbor's Pipes Never Burst — The $2 Secret Plumbers Aren't Telling You" (`Ee36yVgRJtY`)

Published 2026-11-01 · 10:27 · 684 views at collection

**In one line:** the winter advice is sound and safe (the thawing and heat-cable lines are right), but the video breaks the 2026-10-29 rules in the opening and on length. It runs 9.8 minutes at 190, opens with three numbered promises and "None of this needs a plumber", and reaches item one at 1:01.

### What works
- **The title's secret in the second sentence, with its price:** "The secret is a gray foam sleeve, plain pipe insulation, about $2.00 and change for a 6-ft length" [0:08]
- **The villain as two plain facts:** "Nobody in the trade comes around in October to point that out. They get the call in January at the holiday rate." [0:38]
- **A myth flipped with the reason, and paid off later:** "You've probably pictured the ice swelling up and cracking the pipe right where it froze... So, the pipe usually splits away from the ice somewhere in the warm stretch" [1:05]. The callback is honest: "Remember number one? That little drip is what lets the pressure out." [6:55]
- **Safety in proportion:**
  - "And never ever overlap it or wrap it over itself. Where the cable crosses itself, it can overheat." [8:06]
  - "Then, warm the pipe you can reach with a hair dryer, working back from the faucet toward the cold spot. Never an open flame. Never a torch." [8:39]
- **A good "you'd think... but" turn:** "You'd think that means it can't freeze, but leave a hose screwed onto it, and the water can't drain out of that long body." [5:35]
- **Disgust as his opinion:** "That makes my blood boil, for a pipe a sleeve would have saved." [7:23]

### Rule breaks
1. **Under 12 minutes:** 1,861 caption words, about 9.8 minutes at 190; the video plays 10:27.
   - **The rule:** pack "Length" and `HANDOFF.md` 2026-10-29: at least 2,280 words.
   - **Fix:** about 420 more words of real value. For example, item one's thaw and drip guidance could be fuller, and items 2 and 4 each give a "where to look" list that could become checks with what the viewer will see. Never padding.
2. **Three promises in the opening:** "Number one is the one everybody gets backwards because the pipe doesn't split where the ice is. Number three is the gap that lets a wrapped pipe freeze anyway and number five is the leak that hides inside your wall until spring." [0:46]
   - **The rule:** P18 and pack "The opening" ("never two"; "never a promise paid earlier in the video"; no "run-down of what later items hold"). All three are paid mid-video (at 1:01, 3:49 and 5:14).
   - **Fix:** cut all three, or keep at most one promise of what the end pays (number eight, the main shutoff).
3. **A blanket no-plumber line when the video has call points:** "None of this needs a plumber and it's all a weekend's work." [0:45], against "If you can't find the frozen spot or the pipe's already split, shut the water off at the main and make the call." [8:52] and "That's a valve to have replaced before winter, not during a flood." [9:34].
   - **The rule:** pack "The opening" job 4 and `HANDOFF.md` 2026-10-29 ("The scope line never says no plumber is needed when a step ends in a call"). The title doesn't promise "no plumber".
   - **Fix:** say where it stops, for example "Everything here is yours until a pipe has already split."
4. **Item one at 1:01 (word 190),** against the first real tip by about 45 seconds (about 140 words). The three promises above are what pushed it out.
5. **Items without a "but" turn or an "I" line.**
   - **The scanner's count:** no "I" line in items 1, 2, 4, 5 and 6; no "but" in items 2, 4 and 8.
   - **The rule:** pack "Emotion, all the way through" §4 ("Inside every item, at least one turn") and §10 ("One short 'I' opinion or verdict in most items").
   - **Fix:** one "I'd..." verdict and one "people figure... but..." turn in each of those items.

### Facts worth checking
- **"The average water damage or freezing insurance claim ran about $12,500."** [1:55], said again at [4:11]. The price guide gives "about $15,000 (Insurance Information Institute, 2019-2023)" (measured). The script's figure is lower, perhaps an older III period, and it may have come from the brief.
- **"$500 to $2,000 once a frozen pipe bursts"** [4:07] matches the guide ("once it bursts, $500 to $2,000").
- **"$200 to $650 for the visit alone"** on a holiday night [7:16] matches the guide's after-hours row.
- **"keep the thermostat at 55° or higher"** [7:00]: everyday general knowledge, fine.
- **"If you do only one thing before the freeze, make it this."** [3:59] comes at item three. The pack puts the priority flag "at the first answer". Reading: minor.

### Voice and caption oddities (worth a listen)
- **"a bare bend between two sleeves is the one spot the cold can still we'll to."** [3:54]. The end of the sentence is lost ("still get to"?). Worth a listen.
- "$2.00 and change for a 6-ft length" [0:08] and "1/2 in or 3/4 in" [3:05] are the caption system's spelling. The scanner's flags on them are caption-made.

### Numbers (caption-based, approximate)
- **Length and speed:** 10:27; 1,861 caption words; 178 words a minute; 9.8 minutes at 190 (**fails 12**).
- **First item:** item one at 1:01 (word 190).
- **Opening promises:** 3.
- **CTAs:** subscribe ask at 10:04; comment ask at 10:13.
- **Tenure:** none.
- **Rates per 1,000 words:** "you/your" about 25; "but" about 3.8; "I" about 3.2.
- **Question marks:** 3. This is low: the pack asks for a question about every two items, which would be about four for eight items.

---

## 5. "NEVER Call A Plumber Again! 12 Secrets They DON'T Want You To Know" (`7SnNq7RXa88`)

Published 2026-10-31 · 15:02 · 241 views at collection

**In one line:** this is the longest and most useful of the older four. It has twelve real, priced, safe items, honest about where the viewer stops, at 15.5 minutes. But its opening joins the trade's silence to a motive with "because", runs three numbered promises, and reaches item one at 1:03.

### What works
- **Honest scope against a title that overclaims:** "Now, I won't pretend you'll never need one. Gas lines, the main sewer, and anything that needs a permit go to a licensed pro and I'll say so when we get there." [0:27]. That is the persona's hard no's, said as part of the brand, as the profile asks.
- **The count line, with the tenure doing a job:** "45 years in this trade and these are 12 things the invoice never mentions." [0:42]
- **The priority flag on a real, checkable tip:** "If you only remember one thing from this whole video, leave that gap at the back." [3:22], followed straight away by a question about the viewer's own house: "When did you last press your foot on the floor right beside your toilet?" [3:26]
- **Safety by the book:**
  - "if there's drain opener sitting in that sink right now, don't plunge it and don't pour anything else in" [8:18]
  - "Dissolve it first because dry powder can set up hard in the pipe." [8:43]
  - the power or gas off before the water heater: "Turn the power off at the breaker or on a gas heater, turn the gas valve to off." [9:31]
  - the scald figure as the guide gives it: "At 140°, water can give an adult a third-degree burn in about 6 seconds. Older skin burns faster." [10:50]
- **The cost-per-use device used correctly:** "Call it about 60 cents a month against a jug you keep buying over and over" [8:47]
- **Trade terms explained the first time,** as the pack lists:
  - "the angle stop, that little valve on the wall behind the toilet" [1:35]
  - "the anode rod" [9:10]
  - "PSI, pounds per square inch" [11:49]
  - "the PRV, a regulator on the main water line" [12:06]
- **A good ending:** "Between you and me, I'd do this one this weekend. 20 minutes, a pair of hoses, and you can leave the house for a few days without lying awake wondering about the laundry room." [14:33]

### Rule breaks
1. **The trade's silence joined to a motive by "because":** "Nobody in the trade is going to explain how simple some of this is because every one of these jobs is a visit they get to bill for." [0:18]
   - **The rule:** pack "The villain" ("Never 'so', 'since' or 'because' between what the trade earns and what it doesn't say"), the persona's "never motives", and `HANDOFF.md` 2026-10-29.
   - **Fix:** two facts side by side, for example "Nobody in the trade explains how simple some of this is. And every one of these jobs is a visit on a bill."
2. **Three promises in the opening:** "Number three can get you a faucet part for free straight from the company that made it. Number five is a check you can run tonight with the food coloring in your kitchen cabinet. And number nine could keep you from buying a bigger water heater you don't need." [0:48]
   - **The rule:** P18 and pack "The opening" (at most one, only of what the end pays; never two; no run-down of later items). All three are paid mid-video.
   - **Fix:** cut them. The count line already carries the opening.
3. **Item one at 1:03 (word 200),** against the first real tip by about 45 seconds, and "in a list, item one by about 30 seconds" (pack "The opening", job 6).

### Facts worth checking
- **"check it every two to three years"** (the anode rod) [9:29]. The price guide's row says "check it once a year; how long it lasts depends on your water, a couple of years to five" (measured: differs from the guide).
- **"A flapper runs about $5 to $25."** [6:35]. The guide gives "$4 to $10" (measured: the top is well above the guide).
- **"Steel-braided hoses cost about $20 to $60."** [14:15]. The guide's washer-hose row is "$15 to $35" a pair, not specific to steel-braided (measured: differs). It may have come from the brief.
- **"A plumber's toilet swap lands anywhere from $250 to $800"** [1:10]. The guide's "new toilet installed" is "$300 to $800" (close; differs at the low end).
- **"About 30% more you can use"** from a mixing valve [10:42]. Reading: the arithmetic holds (with 50-degree inlet water, a tank at 140 mixed down to 120 gives about 29% more), but no guide row gives a percentage.
- **"And most codes call for a pressure-reducing valve."** [12:03]. Codes call for one when the pressure is over 80. The sentence follows "up over 80", but on one listen it can sound as if every house needs one. Reading.
- **"Then caulk around the base but leave the back open."** [3:04]. Common trade advice, but some local codes want the base sealed all round. Reading: worth a hedge ("where your code allows").

### Voice and caption oddities (worth a listen)
- **"Nine times out out 10"** [3:58]: a stutter in the voice, or the captions. Worth a listen.
- "pounds per square inch" and the degree figures are fine as spoken. The scanner's "PSI" and "°" flags are about the captions' spelling.

### Numbers (caption-based, approximate)
- **Length and speed:** 15:02; 2,952 caption words; 196 words a minute; 15.5 minutes at 190 (meets 12).
- **First item:** item one at 1:03 (word 200).
- **Opening promises:** 3.
- **CTAs:** subscribe ask at 14:47; comment ask at 14:51.
- **Tenure:** once, at 0:42.
- **Rates per 1,000 words:** "you/your" about 38; "but" about 6.1; "I" about 4.1.
- **Question marks:** 7.
- **Scanner:** items 1, 5, 8, 9, 10 and 11 have no "I" line (item 9 does have "to me, that price is plain criminal"). About half the items carry a verdict; the pack asks for "most". Reading: borderline.

---

## 6. "The Absolute BEST Way To Clean Your Toilet (No Bleach, No Scrubbing)" (`oJYnV-RePuU`)

Published 2026-10-30 · 10:07 · 1,300 views at collection (the channel's best of the seven so far)

**In one line:** this is a practical, safe cleaning video (the citric-acid-and-bleach warning is exactly right), and it has the most views of the seven. But it runs 9.8 minutes at 190, promises two specific steps in the opening, and has almost no first person or "but".

### What works
- **The title's promise paid in the second sentence:** "You can get that bowl white with a cup of citric acid, a night of soaking, and one pass of the brush. No bleach and no scrubbing." [0:06]
- **The failed attempt, and why it failed, in plain words:** "Bleach makes it look clean on Sunday, and a week or two later the ring's back, a little darker... It's a ledge of hard water minerals, and bleach can't dissolve rock." [0:13]
- **The safety line in the right place, with the reason:** "Never use citric acid in a bowl that has bleach in it, and never add bleach after. An acid and bleach together give off chlorine gas" [3:31]. Then "Make sure you flush twice, so there's no acid left in the bowl." [5:59], before the disinfectant step.
- **The arithmetic holds (measured):** "At one dose a month, you'd be soaking that bowl for more than 12 years before the acid added up to the cheapest new one." [4:44]. $300 at $2 a month is 150 months, about 12½ years.
- **Checks the viewer runs at home:** the hand mirror under the rim [5:05]; the black light at the base [7:14]; food colouring in the tank [8:57].

### Rule breaks
1. **Under 12 minutes:** 1,855 caption words, about 9.8 minutes at 190; the video plays 10:07.
   - **The rule:** pack "Length", at least 2,280 words.
   - **Fix:** about 425 more words of real value. Step nine already holds three extra jobs (the running toilet, the bath fan, the tank tablets) that could each be a full step with its own scene, cause and win.
2. **Two promises in the opening:** "Step three is the soak that scrubs for you while you sleep, and step five comes with a check you can run with a hand mirror." [0:35]
   - **The rule:** P18 (never two; never one paid earlier). They are paid at 2:30 and 4:57. This is the same pattern as the 2026-10-28 "opening with two promises".
   - **Fix:** cut both. "Nine steps, and the first one happens before you touch any water." [0:42] does the opening's job alone.
3. **Items without a "but" turn or an "I" line.**
   - **The scanner's count:** no "I" line in steps 1, 2, 3, 5, 6, 7 and 8; no "but" in steps 2, 3, 5, 6, 7 and 8. "I" runs about 1.1 per 1,000 words, the lowest of the seven.
   - **The rule:** pack "Emotion" §4 (a turn inside every item) and §10 (a verdict in most items).
   - **Fix:** one "I'd..." line and one "you'd think... but" turn in most steps.

### Facts worth checking
- **"scratched glaze grabs the next ring about twice as fast"** [4:31]. A specific figure with no source, and not everyday knowledge. It looks invented. Risky under the claims policy; say "faster" instead.
- **"About 85% of homes in this country have hard water"** [3:08]. Reading: the usual figure (from the USGS) is about 85% of the country by area or water supply, often misquoted as "homes". Not in the price guide.
- **"Buy it in a 5-lb bag and it works out to about $2 a dose."** [3:22]. The guide has citric acid at "1 lb, about $10 to $15" (measured). A cup is roughly half a pound, so at guide prices a dose is about $4.50 to $7. The $2 needs bulk-bag prices the guide doesn't hold. It may have come from the brief.
- **"That's how the professional cleaners do it"** [0:48]. Reading: an unnamed-experience appeal, close to the pack's "nameless claimed experience" (Proof, "Never"). Soft.
- **"Give it a few minutes, then scrub again, and flush."** [5:33], in a "No Scrubbing" video. Reading: a viewer may notice.
- **"A new toilet installed runs anywhere from $300 to $800"** [4:38] matches the guide.

### Voice and caption oddities (worth a listen)
- **">> [sighs and gasps] >> I hate seeing anybody pay that over a ring."** [4:53]. The caption system heard a sigh and a gasp. `[sighs]` is an allowed voiceover tag; a gasp is not something the copy should ask for.
- **"spray [clears throat] the brush head with disinfectant"** [8:10]. A throat-clear mid-instruction.
- **"subscribe to The Vintage Pipe it's your turn."** [9:50]. The channel name is cut off ("Pipefitter. Now it's your turn"?). If the voice dropped it, the subscribe ask lost the name it exists to say. **Worth a listen first.**

### Numbers (caption-based, approximate)
- **Length and speed:** 10:07; 1,855 caption words (the scanner says 1,857); 183 words a minute; 9.8 minutes at 190 (**fails 12**).
- **First step:** step one at 0:45 (word 151).
- **Opening promises:** 2.
- **CTAs:** subscribe ask at 9:50; comment ask at 9:55.
- **Tenure:** none.
- **Rates per 1,000 words:** "you/your" about 31; "but" about 2.2; "I" about 1.1.
- **Question marks:** 4.

---

## 7. "8 Things You Should NEVER Pour Down Your Drains" (`o_4qckQjeYE`)

Published 2026-10-29 · 11:08 · 258 views at collection

**In one line:** strong scenes and good safety, but the video runs 10.6 minutes at 190 and opens with three numbered promises, one of which gives away item six ("it's boiling water"). Item one comes at 0:55, and the closing "$13,000" total is more than the video's own figures add up to.

### What works
- **A scene the viewer lives:** "The bacon grease after Sunday breakfast, the coffee grounds rinsed out of the pot, that splash of bleach to freshen things up." [0:04]
- **A question answered at once:** "So, why does a drain that ran fine on Sunday quit on a Thursday night? Because it didn't quit on Thursday. It's been filling up for months" [0:19]
- **The doubter credited, and the price said as his opinion:** "Somebody's typing in the comments right now that they've poured it down for years and their pipes are fine. Maybe they are." [3:08]; "And I think that's absolutely criminal for something that started as a slow sink." [3:23]
- **The priority flag at the first answer:** "If you change one habit after this video, make it this one because it's the one that fills the most pipes." [2:11]
- **Safety:**
  - the safe-default reason for boiling water ("the white plastic drain pipe under most sinks is rated for about 140°. Boiling water is 212." [7:44])
  - both gas warnings ("Bleach mixed with ammonia makes a toxic gas. Bleach mixed with an acid, like vinegar or some toilet bowl cleaners, gives off chlorine gas." [9:45])
  - washing soda dissolved first [10:22]
- **Callbacks that match real promises:** "Number five, the one I said can cost you a septic system." [6:07]; "Number eight, the mixing rule I promised." [9:34]

### Rule breaks
1. **Under 12 minutes:** 2,023 caption words, about 10.6 minutes at 190; the video plays 11:08.
   - **The rule:** pack "Length", at least 2,280 words.
   - **Fix:** about 260 more words of real value.
2. **Three promises in the opening, one naming an item's content:** "Number five is the one that can cost you a whole septic system. Number six is the one everybody swears is safe and it's boiling water. And number eight is the mixing rule that keeps you safe while you clean." [0:40]
   - **The rule:** P18 (never two) and pack "The opening", job 5 (it "never says what any single item holds").
   - **Fix:** cut them. At most, keep one promise of what the end pays (number eight).
3. **Item one at 0:55 (word 170),** against the first real tip by about 45 seconds. The never-do type's first tip falls at 30-45 seconds (pack "The video types").

### Facts worth checking
- **"Now, add up the low end of every bill on this list, and it comes to more than $13,000."** [10:38]
  - **Measured:** the low ends the video says out loud are $150 (the drain call, 0:30), $300 (jetting, 1:33), $2,000 (pipe replacement, 3:19) and $10,000 (septic, 6:52). Together that is $12,450.
  - **The gap:** the other items carry their cost in words ("a few hundred dollars", "another service call", "a new sink", "one of the priciest drain calls"). So "more than $13,000" leans on numbers the viewer never heard.
  - **The rule:** pack "Money framing" ("Never: A total stated as certain when it depends on the viewer's house").
  - **Fix:** say a total the stated figures reach ("well over $12,000"), or price the missing items.
- **"when a pipe finally gives out, replacing it runs $2,000 to $5,000"** [3:19]. Not in the price guide (repipe of a room or two: "$500 to $2,000"; whole house: a few thousand to about $15,000). It may have come from the brief.
- **"a failed septic system can run $10,000 and up"** [6:52]. The price guide has no septic row (measured). Brief unknown.
- **"that reaction can run close to 200° inside your pipe"** [2:40]. Reading: commonly said of lye cleaners; unchecked.
- **"stir half a cup of washing soda, not baking soda, into a kettle of the hottest tap water"** [10:19]. Reading: "kettle" right after the boiling-water item may cue a viewer to boil it. "Pitcher" or "bucket" is safer.
- **"Potato peels... wind around the blades of a garbage disposal"** [5:19]. Reading: disposals have no blades (they have impellers). Minor; viewers who own one may say so.

### Voice and caption oddities (worth a listen)
- **"Now, I want to turn it [snorts] over to you."** [10:56]. A snort inside the comment ask. `core/workflow.md` §6: CTA sections get "at most one [warm] at the start of each, nothing else inside". Worth a listen.
- "Flower and starches" [4:52] is the caption system's spelling of "flour".

### Numbers (caption-based, approximate)
- **Length and speed:** 11:08; 2,023 caption words; 182 words a minute; 10.6 minutes at 190 (**fails 12**).
- **First item:** item one at 0:55 (word 170).
- **Opening promises:** 3.
- **CTAs:** subscribe ask at 10:51; comment ask at 10:57.
- **Tenure:** none.
- **Rates per 1,000 words:** "you/your" about 30; "but" about 3.5; "I" about 2.5.
- **Question marks:** 10.
- **Scanner:** no "I" line in items 1, 3, 4, 6 and 7; no "but" in items 7 and 8.

---

## Channel level

### Patterns (three or more videos)

1. **A run of numbered promises in the opening: 4 of 7** (videos 4, 5, 6, 7; 29 October to 1 November).
   - Three of the four run three promises.
   - None of the three newest has more than one, and the one in "Sink Stopper" is paid at the end, as allowed.
2. **Under 12 minutes at 190: 3 of 7** (videos 4, 6, 7: 10:27, 10:07, 11:08).
   - The three newest all pass (12:36 to 14:22).
   - Counted at the old 150, all three short ones would have "passed" (12.4 to 13.5 minutes). Reading: the VA's length check was still at 150, or not run.
3. **Item one after about 45 seconds: 4 of 7.**
   - The late four: 2:01 (Sink Stopper), 1:01, 1:03, 0:55.
   - The other three sit right on the line: 0:44, 0:45, 0:45.
   - Every late one had either a promise run-down or an anatomy lesson in front of item one.
4. **The same signature lines in video after video** (each once per video, which the rules allow).
   - "Here's the part people skip" is in 5 of 7, "Nine times out of 10" in 4 of 7, and "Listen to me on this one/part" in 5 of 7.
   - The comment ask opens "Leave me a comment and tell me" in 6 of 7.
   - The subscribe ask uses the same frame in 7 of 7: "If [you'd rather / you like / old-school know-how...], subscribe to the Vintage Pipefitter for more [old school...]". "Old school" or "old-school" is in 6 of 7, and "saves real money" (the profile's own added-value wording) in 3.
   - The pack names "Nine times out of 10" in 9 of 10 Vintage videos as the kind of tic to avoid ("A phrase is voice once; in the same slot every video, it's a tic"). The profile asks that the subscribe line be "worded fresh each time".
   - Reading: within the once-per-video limit, but drifting back toward the old tic.
5. **Little first person, few "but" turns: all 7.**
   - **The measured rates:** "I" runs 1.1 to 4.6 per 1,000 words, under the 5.3 to 8.8 of the channels' own hits that the pack cites as already the low end. "But" runs 2.1 to 6.1 per 1,000, against the pack's "much more buts" (the plumbing pack sets no number).
   - **The scanner's count:** in videos 4, 6 and 7 (and borderline in 5), items have no "I" verdict or no "but" turn, which the pack does require (Emotion §4 and §10).
   - **Better lately:** the three newest have an "I" line and a "but" in every item.
6. **Prices that differ from the price guide: 5 of 7.**
   - main line $300 to $600
   - cabinet floor $150 to $500
   - the $12,500 claim (guide $15,000)
   - flapper $5 to $25 (guide $4 to $10)
   - anode check every two to three years (guide once a year)
   - hoses $20 to $60
   - pipe $2,000 to $5,000
   - septic $10,000+

   The briefs aren't in the repo, so some may be the brief's figures. Either way the VA's audit (D4: each price named to the brief or the guide row) should show where each came from.
7. **Non-speech sounds in the captions: 3 of 7.** "[snorts]" (Sink Stopper [7:45]; Never Pour [10:56], inside the comment ask), "[sighs and gasps]" and "[clears throat]" (Toilet Clean [4:53], [8:10]). The voiceover copy allows `[sighs]` and `[chuckles]`; snorts, gasps and throat-clears may be how this voice performs them. Worth a listen on all four.

**Same-channel topic overlap (reading; the operator has said repeated topics are not the script library's job):**
- monthly washing soda and "the jug burns a channel": videos 1, 5 and 7
- flushable wipes: videos 5 and 7
- tank tablets and the food-colouring flapper test: videos 5 and 6
- rim jets: videos 1, 3 and 6
- Video 3 takes the same title and three-level shape as Werner's 2026-10-28 "How to Unclog a Toilet For Beginners (The German Way)". It avoids both of the errors that review found in Werner's.

### Against the previous reviews
- **Length and the two-promise opening:** fixed in the newest three, not before (see the top of this file).
- **"Nine times out of 10":** was in 9 of 10 older videos; now in 4 of 7, once each.
- **The scope line:** 1 of 7 still says "None of this needs a plumber" with a call point later (video 4).
- **The "because" motive:** 1 of 7 (video 5).
- **"Tonight's homework" style lists:** gone. Every video ends on one small thing. Video 1's "whole bill" line still runs back over the four items.

### Top 3 fixes
1. **Run the length check at 190 every time:** 2,280 words before the voiceover. Three of seven came in 260 to 425 words short, and all three would have passed at the old 150.
2. **Open like the three newest: no numbered promises, item one by about 45 seconds.** Video 3's opening (task, the number-one mistake, the price, the escalation line, the stop point, then the first tip at 0:45) is the model to copy. Cut any "Number three is... number five is..." run-down and any lesson that comes before the first tip.
3. **Vary the fixed lines and keep a verdict in every item.** Rotate "Here's the part people skip", "Listen to me on this", "Leave me a comment and tell me" and the subscribe frame. Give every item one "I'd..." line and one "but" turn (the three newest already do).
