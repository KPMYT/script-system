# TEST: our script against Roger's own hits (test run 02)

Analyst comparison, written 2026-10-21. Read-only on everything else. Compared:

- **Ours:** `script.txt`, "15 Plumbing Mistakes Quietly Costing You THOUSANDS", 3,000 words. No timestamps, so times are estimated at the pack's 150 words a minute (about 20:00).
- **S03, 453x:** "5 Things You Should NEVER Pour Down Your Drain" (WfAwg1l0xCE), 2,464 words, 18:24. This is the closest type to ours.
- **S07, 364x:** "Why Plumbers' Own Drains Never Clog" (YjPAVZAffh0), 3,010 words, 18:44.
- **Original:** the published video on our title (3tsYa7aOprw), 3,344 words, 21:12, 692 views on day one. That is about 0.26x the channel normal of 2,688, but day one can't be compared with the hits' lifetime views.

**Limits.**
- The counts are my own regex counts and are approximate.
- The original's sentence stats come from auto-captions, so its punctuation is unreliable.
- The hits are AI-written and tagged [structure only]. The quotes below show what each move does. They are never wording to borrow.

---

## 0. The numbers side by side

| Measure | Ours | S03 453x | S07 364x | Original |
|---|---|---|---|---|
| Spoken words | 3,000 | 2,464 | 3,010 | 3,344 |
| Words a minute (from timestamps) | n/a (150 assumed) | **134** (segments 78-163) | 161 (111-202) | 158 (132-186) |
| Mean / median sentence (words) | 14.0 / 13 | 15.9 / 15 | 13.7 / 13 | 14.0 / 12 |
| Sentences of 6 words or fewer | 19% | 11% | 21% | 22% |
| **"you/your" per 1,000** | **20.7** | **41.0** | **42.9** | 29.6 |
| "I/me/my" per 1,000 | 4.3 | 4.5 | 9.3 | 3.3 |
| Questions to the viewer | **0** (the 3 "?" are for a contractor) | 5 | 2 | about 7 |
| Sentence-opening imperatives per 1,000 | **9.0** | 2.8 | 5.3 | 4.8 |
| Dollar figures per 1,000 | **8.3** (25 figures) | 4.5 | 5.6 | 3.0 |
| Intensifiers per 1,000 ("actually", "completely", "every single") | 0.3 | 6.9 | 4.7 | 1.5 |
| Surprise / myth words per 1,000 ("think", "surprise", "realize", "harmless") | 1.7 | **6.9** | 1.3 | 0.9 |
| Disgust words per 1,000 | 0.3 | 2.4 | 1.0 | 0 |
| Old-house / family words per 1,000 | 4.0 | 0.4 | 2.0 | 5.4 |
| Title words spoken | **0** ("mistake" 0, "quietly" 0) | 7 ("never pour") | 11 | 21 ("mistake") |
| Items / median words per item | 15 / about 187 (about 75 s) | 5 / about 420 (about 186 s) | 5 habits + 5 cases / about 240 | 15 / about 170 |

The biggest single gap is that **the hits say "you" twice as often as we do**. Our script tells the viewer what to do (9.0 imperatives per 1,000), but it rarely puts him inside the mistake.

---

## 1. Emotions triggered, and how

Codes are from `05-emotions.md`.

| Emotion | Ours | S03 453x | Original |
|---|---|---|---|
| Habit recognition, mild embarrassment (E9) | Rare. The habit is described in the third person: "A toilet that hisses, trickles, or refills itself in the middle of the night can waste up to about 200 gallons a day." | The engine of every item. The viewer is cast as the one doing it: [0:43] "You finish cooking up some bacon on a Saturday morning"; [6:31] "You rinse out your French press or dump your coffee filter over the sink." Comments answer in kind: "coffee grounds?? OOPS!" (26). | "letting a toilet run and calling it a quirk"; "deciding it can wait until the weekend after next" |
| Myth-bust surprise (E12) | Four soft flags: "That word means it'll go down the toilet, and that's all it means."; "Running hot water while you pour doesn't fix it." The #7 promise ("almost everybody gets backwards") never names the belief it flips. | In 4 of 5 items: [3:20] "most people think they are actually helping their pipes"; [9:32] "This one catches a lot of people offguard"; [10:46] "What a lot of folks do not realize". Rewarded in comments: "Never heard of the rinsing of pasta, potato etc being a problem for drains!" (125). | "even a frost-free spigot… can't drain with a hose corked onto the end of it" |
| Hidden, slow damage (E4) | "You find out in spring, the first time you turn it on"; "never gets fixed, because nobody sees it" | [0:00] "quietly destroying their pipes from the inside out"; [1:20] "that buildup gets thicker and thicker" | "The expensive stuff always starts out quiet."; "You won't hear it happen." |
| Big-bill fear, then a cheap fix (E1 into E14) | A three-rung ladder: "$150 to $300 for the camera, $300 to $1,000 to cut the roots out, and $5,000 to $20,000"; "and that's if it's clean water" | One bill per item, set against the fix: [5:10] "$2,000 to $5,000 or more… All because of a product that costs about $8 a bottle." | "A new rod is a $30 part. A new water heater installed runs well north of a thousand" |
| Disgust (E7) | Almost none. The nearest is "catches some paper, gets fed, and grows". | [1:57] "fatbergs… the size of small cars"; [9:57] "a gluey mess"; [7:39] "a dense, sludgy blockage" | "build a rope no plunger can touch" |
| Emergency dread (E5) | "instead of at two in the morning with water coming through the ceiling"; "it pours for as long as nobody's home to hear it" | "a backup that can flood your kitchen" | "almost always when nobody's home to hear it" |
| Protectiveness (E16) | Strongest of the three: "Older folks and little kids burn faster than that."; "if anybody in the house says they smell it, believe them." | None. | "the person standing in the kitchen when a pipe lets go, might not be you" |
| Relief at the end (E14) | The video closes on a gas evacuation, "Don't go back in until they tell you it's safe," and then the book. | [17:35] "Sometimes the best plumbing advice is the simplest." | "Call the licensed trade and sleep fine." |

**The arc.** S03 runs "cost fear, then cheap fix" five times and closes on simplicity (`05-emotions.md` §2A). Ours runs fear and procedure fifteen times and closes on danger. We trigger the same emotions as S03. The difference is that S03 hangs every one on a scene the viewer is standing in, and we hang ours on facts.

---

## 2. Pacing

- **Words a minute.**
  - S03 is the slowest hit at 134 (the own-hit median is 138). The voice slows on the money peak: the segment at [5:10] runs at 107 wpm. One comment: "To make this watchable, increase the speed to 150%" (70 likes).
  - S07 and the original run at about 160. Ours has no voice timing yet.
- **Time to the first payoff.**
  - Ours is fastest. The answer comes at word 19 (about 0:08): "A camera down the sewer line would've found those roots years earlier". Money in words follows at about 0:14, and item one at word 125 (about 0:50).
  - S03 reaches item one at 0:43, but its first price only at [2:34].
  - S07 has the $200 bill at [0:09] but the habit only at [3:16]: "3:15 is where it starts." (2K likes).
  - The original reaches item one at 1:02.
- **Item length.**
  - S03's five items run 352-531 words, about three minutes each, and each one is a full story.
  - Ours run 141-245 words, about 75 seconds each.
  - Ours are closer to the original (about 170) and to S07's troubleshooting cases than to S03.
- **Rises and dips.**
  - Ours peaks at #3, "If you do only one thing from this video, do this one." (about 4:05). The next peaks are #7 (about 9:20) and #15 (about 18:20).
  - Sentences shorten through the back half, from a mean of 17.2 words in item 1 to 9.8 in item 14. Items 12-14 read as checklists: "Read the meter, or snap a picture of it. Wait at least half an hour".
  - S03 has no checklist dips. Every item climbs from scene to mechanism to bill, then lands on "So, what should you do instead?"

---

## 3. Language

- **Second person.**
  - S03 makes "you" the one doing the mistake: "You pour them down a slow drain, wait a few minutes, and the water starts flowing again. Problem solved, right? Not even close."
  - Ours makes "you" the one taking orders: "Turn off the little valve on the wall and hold the handle down until the tank's empty."
- **Strong verbs.**
  - Ours: "packed solid", "lets go", "splits the pipe", "goes to work on the tank", "pours".
  - S03: "quietly destroying", "eating away at your pipes", "burn a small channel".
  - The original is the most vivid: "drain bank accounts", "Flushes turn lazy", "rubber doesn't age politely", "almost insulting".
- **Folksy phrases.**
  - Ours: "a couple hundred bucks", "leave the cheater bar in the toolbox", "takes a big socket and some muscle", "without blinking", "a few hundred dollars well spent".
  - S03: "you would be amazed", "a world of trouble down the road", "Not even close".
- **Questions.**
  - Ours asks the viewer none.
  - S03 asks five, all rhetorical turns: "So, it seems perfectly fine to just rinse it right down the sink with some hot water, right?"; "So, what happens?"
  - The original: "Dry fingers? Close the cabinet. Wet fingers? You just saved a floor."
- **Repetition for emphasis.**
  - S03 repeats the title phrase in every header: "The fourth thing you should never pour down your drain is…" It also uses "every single day" twice and "never pour them down any drain. Period."
  - S07: "Zero grease down the drain. None. Not even a little bit. Not even with hot water running."
  - Ours has hammered pairs ("A leaking tank can't be fixed. It gets replaced."; "Gas is different."), but it never says the title's word "mistake", and it never says "quietly".

---

## 4. Structure

| | Ours | S03 453x | Original |
|---|---|---|---|
| Opening | Worst-case picture, then the answer, the price, the silence, the tenure and three numbered stakes. 125 words, about 0:50. | A belief ("You might think your kitchen sink can handle just about anything"), reassurance, the count, then two promises: one stake and one banned tease. 109 words, 0:43. | Pointing, the roots, the count, the #15 stake, a name intro and a recap. About 179 words, 1:02. |
| Body | 15 items. Each opens on a gerund header ("Ignoring a running toilet."), then the inner order varies: cost, check, steps, trigger. | 5 items, all in a fixed order: scene, then "here is what is actually happening inside your pipes", then the bill, then "So, what should you do instead?" | 15 items: a label, a picture, the cost to catch it, the cost to ignore it. |
| Ending | #15 gas, a one-line book reminder, then the comment line. | The bonus, "Thanks for sticking with me", then like and subscribe (it cuts off). | The book (75 words), subscribe, the comment ask, then "Now go walk that old house tonight." |

S03 makes up for its slow open with an inner order that never changes, and viewers could retell it. The top comment (1.5K likes) is a viewer's own numbered list of all five items. Ours has no fixed inner order, so 15 items blur together.

---

## 5. Transitions

| Type | Ours (exact) | Hits / original (exact) |
|---|---|---|
| Stake in the header | Only #3's priority flag and #15's "This is the one I said I'd never let you touch." | S03 [3:20] "this one is a real eyeopener"; [12:50] "this is the one that surprises most homeowners" |
| What the next item protects | "That one protects a wall. The next one protects your water heater."; "The next one is a cheap part standing between your washer and a flooded laundry room." | Original: "from the biggest pipe you own to a leak you can hear from the hallway" |
| Season | "The next one's about the weather, and this is the time of year for it." | Original: "Mistake number four is waiting outside your house right now" |
| Callback to the hook | "Now the one I said almost everybody gets backwards." | S07 [16:12] "Now, for that bonus tip I promised at the beginning." |
| Cross-reference back | "Go back to number one."; "the same roots from number one"; "back to number two" | Original: "those wipes have a partner in crime at the other sink in the house" |
| Bare cut ("Number N.") | 9 of 14 joins | S03: every join is the header formula ("The [nth] thing you should never pour down your drain is…"), and 3 of 5 headers add a stake |
| Return after the CTA | "Now, about that sound in the night." (picks up the open question) | S03 [9:13] / S07 [7:32] "All right, let's continue." (a banned stock line) |

Ours has better bridges than the hits. Its weak spot is the run from #8 to #13: five bare cuts in a row, with no stake in any header.

---

## 6. Personality

- **Ours (4.3 "I" per 1,000).** Short verdicts and candour:
  - "I get why people reach for the jug… That's being careful with money, and there's nothing wrong with that."
  - "I'd put the money toward the next heater instead."
  - "the one job I'd never let you touch"
  - one routine detail: "My own drains get a look the first Saturday of every month, with my coffee"
- **S03 (4.5 per 1,000).** A conversational shrug, with surprise and emphasis:
  - "Now, I know this one might sound obvious, but you would be amazed"
  - "And honestly, I understand why"
  - "Trust me"
  - two banned history lines: "I cannot tell you how many times I have been called out"
- **S07 (9.3 per 1,000).** Insistence and care. The study codes this as "care" (§2B):
  - [7:41] "And I need you to hear me on this one."
  - [2:24] "I cannot stress this enough."
  - "I don't care what anybody told you."
- **Original.** Positioning lines:
  - "I'm on the homeowner's side of every estimate. You know that by now."
  - "no matter what the video with the confident guy says"

Ours has as much personality as S03, but it is all judgement and no warmth or insistence. Nothing in it says "this one matters to me."

---

## 7. The villain

- **Ours.** The trade's silence, said once in the hook: "Nobody gets paid for the flood that never happens, so nobody calls to remind you to look." Also the shelf, credited before it's corrected ("I get why people reach for the jug"), the label ("That word means it'll go down the toilet, and that's all it means.") and bad work ("plumbing is one of the trades where bad work hides"). That's about 4 villain lines.
- **S03.** No trade villain at all. The shelf product is an item: [3:38] "Products like these are marketed as a quick fix… Problem solved, right? Not even close." That's about 2 lines, and the biggest own hit had no enemy (`05-emotions.md` §2A).
- **S07.** The trade, on price and on motive: [0:05] "charges you 200 bucks, and goes home to pipes that flow perfectly"; [0:28] "your clogged drain is how he pays his mortgage". The motive line is banned, and it drew the most-liked doubt in the data (1.3K). The shelf: "the skull and crossbones"; "one of the biggest lies in household products". That's about 7 lines.
- **Original.** "remember how this business works. There's no invoice for the problem you never had."; "the trade mostly gets paid after things turn loud"; "keeps your money out of other people's trucks". That's about 5 lines, some of them motive.

Our level is right for the evidence. After the hook, though, the trade (the locked villain) almost disappears. #14 is the natural place for a second price-and-silence line, and it has none.

---

## 8. Money pain points

| | Biggest figure and its wording | Device |
|---|---|---|
| Ours | "$5,000 to $20,000 if the line has to be dug up or relined"; "a flooded basement commonly runs anywhere from $2,000 to $7,000 to clean up, and that's if it's clean water"; "you can pay twice… And insurance may not cover it." | A ladder of prices; 25 figures on 11 of 15 items |
| S03 | "$2,000 to $5,000 or more… All because of a product that costs about $8 a bottle."; "a $2 strainer is a lot cheaper than a $600 plumber visit"; "$10,000 or more" (septic) | The bill against the cheap fix, one per item; 11 figures in all |
| S07 | "$400 and $600 spent on something that is almost entirely preventable… maybe $40 total over 10 years" | One decade tally |
| Original | "drain bank accounts"; "well north of a thousand"; "10 minutes, $10, done."; "$15, 20 minutes, one flood that never happens." | Few figures, and the price is folded into a hammered triplet |

Our sums are accurate, but there are too many of them (the judge's "Number load 4"). The hits make one comparison per item land hard. The original's "$15, 20 minutes, one flood that never happens." does with one figure what our ladders do with three.

---

## 9. Other pain points

| Pain | Ours | S03 | Original |
|---|---|---|---|
| Old house | 10 mentions: "Older houses often have clay or cast-iron sewer pipe"; "old galvanized and cast-iron drain pipe has been thinning from the inside for decades" | 1: "If you have got older metal pipes" | "If your house went up before the 80s" |
| Ageing body | "Older folks and little kids burn faster than that." | none | "little kids and older folks reaching for a warm rinse" |
| Family / household | "show everybody in the house where it is"; "make it the rule for the whole house" | "homeowners like yourself" | "the house and the people sleeping in it" |
| Being taken advantage of | "Checking a license is free."; "A good plumber answers those without blinking." | none | "tired of writing checks"; "the inspection report the week you try to sell" |
| Making it worse | "Never plunge, snake, or open a trap on a drain that's got drain cleaner sitting in it"; "It just carries the grease a little farther" | [4:45] "You pour in more chemicals and the cycle repeats. Each time your pipes take more damage." | "you've aged the pipe years in one afternoon" |
| The habit as the viewer's own fault | Lifted off him ("That's being careful with money") | Pinned on "homeowners", never on "you" ("you would be amazed how many homeowners still do this") | "calling it a quirk" |

On the 50+ pains (old house, ageing, family), ours is richer than the 453x hit. Where it falls short is the everyday-kitchen pain the hit lives on: grease, coffee, pasta. The study ranks that pain highest in its comments (`05-emotions.md` §3).

---

## 10. CTAs (the operator's point)

| | Ours | Roger hit template (S07, S08, S09) | S03 453x | Original |
|---|---|---|---|---|
| Position | After item 1, at word 348 of 3,000 (12% in, about 2:20) | After 2 items or the first full method: [7:14] S07 at word 1,156 (38% in), [8:51] S08, [6:47] S09 | After item 3, [9:13] (51% in) | After item 3, [5:44] (28% in) |
| Length | 63 words plus a 7-word return, 4 sentences | 72-77 words, 3-4 sentences | 44 words | about 165 words |
| Opening words | "The warning signs of a failing main line, and why roots love old pipe, are on pages 56 to 57 of my book" | [7:14] "By the way, if you're finding this advice helpful, you should know it's just a small sample of what I've put into my new book" | "Now, if you're finding this video helpful so far" (subscribe) | "One quick thing before we get there." |
| Offer | The book, the pages on this topic, plus a second feature: "a sheet of questions to have ready before any contractor quotes you" | The book. One benefit: "practical old house fixes that can help you avoid expensive repair bills" | Like and subscribe, not the book | The book, with a list of features |
| Direction | "the link in the description and the QR code on screen" | "scan the QR code on the screen right now or just use the first link" (pointing, banned) | none | a QR walkthrough (banned) |
| Return | "Now, about that sound in the night." | "All right, let's continue." (banned) | the same | "Now, let's go save that wall." |
| End CTA | 39 words, one line: "My book… has all hundred fixes and a seasonal calendar… at the link…" | [17:57] "Before you go, I want to make sure you know about my new book… It goes deeper than we can in a single video" (80 words) | like and subscribe | 75-word pitch plus subscribe |

**How ours differs from the hit template** (`07-body-craft.md` §10: the same words in 3 of Roger's 5 hits):

1. **Position.**
   - Ours comes after one item, 12% in.
   - The template comes after the second item, or after the first complete method, 37-38% in, once the viewer has had two payoffs and has decided to stay.
   - Ours also comes straight after a forward line ("Number two is a leak you've probably heard at night…"). The viewer has just been told #2 is next, and the pitch delays it.
2. **Opening words.**
   - The template opens with an aside marker ("By the way"), then a condition on the value just received ("if you're finding this advice helpful"), then a frame: this video is "a small sample" and the book is the rest.
   - Ours opens on content ("The warning signs of a failing main line…"). For about 15 words it sounds like item one going on, and then it turns into a sales line. There's no aside signal, no condition and no "more of what you just got" frame.
3. **Structure.**
   - The template: [aside + condition + sample frame + title] → [one benefit] → [where] → [return]. The title sits in the first sentence, tied to the frame.
   - Ours: [topic + pages + title at the end of a 30-word sentence] → [a second, unrelated feature] → [where] → [return]. That is two value claims where the template makes one, and the book's name comes at word 22.
4. **Length.**
   - About the same: 63-70 words against 72-77.
   - Both run longer than the pack's "about 20-60 words: one sentence for the ask", and ours has 3 sentences.
   - Length isn't what's wrong. Shape and slot are.

**What not to copy.**
- "if you're finding this helpful" and "let's continue" are banned stock lines (SKILL.md, the ban-regex).
- "scan the QR code on the screen right now" is banned as pointing.
- "new book" isn't among the profile's true facts.

The transferable part is the slot order. HANDOFF §3 locks Roger's CTA to "the old, much shorter structure their hits used". The pack and the profile turned that into a word count and a trigger ("after the first real payoff"), and the structure itself was lost.

---

## (a) What the hits do that ours lacks, ranked by likely impact

1. **The viewer is inside each mistake** ("You finish cooking up some bacon on a Saturday morning"). Ours has 20.7 "you" per 1,000 against 41.0. This carries recognition and the "OOPS" response, and it is the hit's core engine.
2. **The belief before the bill** ("most people think they are actually helping their pipes"). Surprise words run 6.9 per 1,000 against 1.7, and our #7 promise is paid weakly.
3. **A fixed inner order, closing on "what to do instead"**, which makes the list easy to retell (the 1.5K-like comment). Ours varies its inner order and runs 9.0 imperatives per 1,000, so it reads as a manual.
4. **The CTA as a framed aside after two payoffs** (S07 [7:14]). Ours comes too early, opens cold, and makes two claims.
5. **An ending on relief or action** ("Sometimes the best plumbing advice is the simplest."; "Set that calendar reminder tonight."). Ours exits on the gas evacuation.
6. **One sensory or disgust image per item** ("fatbergs… the size of small cars"; "a dense, sludgy blockage"). Ours has 0.3 disgust words per 1,000.
7. **The title's word spoken** ("never pour down your drain" 7 times). Ours says "mistake" 0 times and "quietly" 0 times.
8. **Rhetorical questions and insistence** ("Problem solved, right? Not even close."; "And I need you to hear me on this one."). Ours asks the viewer none.
9. **Fewer numbers, harder hits**: 4.5 dollar figures per 1,000 against ours 8.3.

## (b) What ours does better, and what the hits do that we ban for good reason

- **Opening.** The answer comes at about 0:08, with three named stakes ("Number three decides whether a leak means a mop or a flooded basement."). The hit's "number five might surprise you" has no stake, and its "stick around for a bonus tip… hundreds of dollars a year" is never paid.
- **No name intro.** The original has one ("I'm Roger. This is Roger the Pipe Guy"), and all 5 recent uploads have one against 0 of 5 hits.
- **No motive.** S07's "how he pays his mortgage" drew a doubt with 1.3K likes. We say what it costs and that nobody mentions it: "Nobody gets paid for the flood that never happens."
- **No teases and no recap.** The original's "What each mistake looks like, what it costs to catch, and what it costs to ignore." is a recap.
- **No claimed experience.** The hits have "I have seen homes…" and "I've pulled wads of them out of sewer lines". A faceless channel gets checked on lines like these: "you never see Roger the pipe guy in his videos."
- **Safety.**
  - Hot tap water, where the hits pour boiling water. S03 [17:08] "Boil a full kettle" and S07's version drew about 18 angry comments.
  - The splash-back rule; the breaker goes off before a panel comes off.
  - Named call triggers: "if water comes up in the tub when you flush, or two drains back up at once… call today". S03's is vague: "if you have got a stubborn clog that you just cannot clear yourself".
- **Prices as ranges.** S07's single "$3-4 box" drew "it's 22$ for 55oz on amazon".
- **Cross-references, a content return line, and the comment line last.**

## (c) Rule-ready suggestions for the plumbing pack

1. **Second person first.** Every list item opens with the viewer doing the mistake, in one second-person line, before any mechanism or price. The move: S03 [0:43] "You finish cooking up some bacon on a Saturday morning…". Scanner warning: "you" under 30 per 1,000.
2. **Name the belief.** When an item has a belief to flip, name it in its first three sentences, and say what the viewer thinks the habit does. The move: S03 [3:20] "most people think they are actually helping their pipes".
3. **One inner order for every item.** Use the same order in every item of a list video (scene → inside the pipe → one cost → the do-instead), and keep procedure to about three steps per item once a list has 10 or more items. The move: S03 [2:48] "So, what should you do instead?"
4. **Say the title's word.** The title's key noun or verb is spoken in the item headers (at least every third item), and its feeling word ("quietly") is pictured once. The move: S03 "The fourth thing you should never pour down your drain is…"; the original's "Mistake number four."
5. **Mid-CTA slot.** In a list of 8 or more items, the mid-video CTA goes after item 2 or 3, about a third of the way in. It never comes straight after a forward line that names the next item. The move: S07 [7:14], after habits 1 and 2. This matches core §2's "first item or two". The pack's "first real payoff" was read as item one.
6. **Mid-CTA shape.** Use four parts in order: an aside signal → a condition on the value just given → "this video is a slice, the book has the rest" plus this topic's pages → where, then a return that picks up the open item. One benefit only, in fresh words. The move: S07 [7:14] "…just a small sample of what I've put into my new book…" (structure only; the stock opening is banned). This change needs PROPOSALS.md and the locked-decision note, because HANDOFF §3 points at the hits' structure.
7. **Relief before the end CTA.** When the last item is the safety one, the last content line before the end CTA hands back control or relief. The move: S03 [17:35] "Sometimes the best plumbing advice is the simplest."; the original's "Call the licensed trade and sleep fine."
8. **One true sensory or disgust picture per item** where the item has one: what it looks, smells or feels like in the pipe. The move: S03 [7:39] "once they settle and compact… a dense, sludgy blockage".
9. **A rhetorical question at least every three items**, one the viewer answers in his head. The move: S03 [3:38] "Problem solved, right? Not even close."; the original's "Dry fingers? Close the cabinet. Wet fingers? You just saved a floor."
10. **One line of insistence on the priority item.** One "this matters to me" line per video, on the priority item only. The move: S07 [7:41] "And I need you to hear me on this one."
