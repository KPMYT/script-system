# Analysis: Werner's and Frederick's first library uploads (2026-10-29)

The main session's review of the two caption transcripts in `transcripts/` against the plumbing pack and Werner's profile, the electrical pack, Frederick's profile and the facts guide, Werner's book file, and his own earlier video on the same topic. Findings only: nothing in the library changed because of this file. The candidate fixes in §3 wait for the operator's yes.

Cautions: one video per channel, 9 hours old, no retention data. The captions are what the voice said, not the script, so a garbled line may be the voice or the caption system; where it matters, it says "worth a listen". `PINNED.md` sets the bar for changing a rule at a pattern across three or more videos.

The scanner was run on both transcripts (timestamps stripped) with each channel's pack and profile, `--refs` on the profile, the pack's excerpts and, for Frederick, model E01. Its results are quoted where they matter; its caption-made flags (fractions written "1/4", run-on caption sentences) are left out.

---

## 1. Werner Finkbeiner: "How to Unclog a Toilet For Beginners (The German Way)" (`kZ09VQIqAS4`)

**In one line:** the voice is right and the escalation is the best structural idea on the channel so far, but the video is too short, breaks two plumbing rules a VA's audit should have caught, gets one fact wrong, and is largely a re-run of the channel's own video from two weeks earlier, with very little "German way" in it.

### What works

- **The register is Werner's.** No contractions anywhere; short object-first sentences ("Then, firm." "The sleeve matters."); "So." as a turn; flat verdicts ("That is level three, and level three is where you stop being brave." [7:18]). It sounds like one person all the way through.
- **The escalation line in the opening works exactly as the pack's option intends:** "There are three levels of a blocked toilet: slow, rising, and over the rim. Each one has its own first move, and the first move decides whether this is 5 minutes or a service call." [0:52]. It names the two ends, not what an item holds, and the body keeps the order.
- **The opener puts the viewer in the scene** with the mistake they're about to make: "the first thing most Americans do is the one thing that makes it worse. They flush again." [0:04]. Americans in the third person, the habit never taught: as the profile asks.
- **Honest stops, early and flat:** "do not force it" on a crusty valve [1:28]; "here I stop. And so should you if any of these three are true" [9:09]; "30 years, and I still stop at those three." [9:31] (the tenure once, doing a job). The "weak flush but never blocked" caveat [4:20] is a good, specific honest line that saves the viewer from plunging an empty toilet.
- **Price lines in his flat register:** "The trade charges $250 to $550 to lift a toilet, and I think that is a hard number for an hour and a wax ring." [9:35]. Aimed at the price, not a person.
- **The mid-video CTA is right:** the fixed mentor line word for word [4:50], "Free, because your own hands do the work", and the book match is correct (repair 50, "Clear a Clogged Toilet Without Reaching for a Snake First", chapter 6, in `personas/books/werner-finkbeiner-book.md`), the link and the QR code, a return line.
- **The close is good writing:** "the next blocked toilet is a small thing that happens on a Tuesday and is gone before the coffee is cold." [10:40]. The comment question is specific and answerable ("which level your toilet was at when you found this video, and whether you knew where the shutoff handle was").

### Rule breaks (the audit should have stopped these)

1. **Under the 12-minute minimum: 11:06.** The script is about 2,010 spoken words. The scanner counts that as "about 13.4 minutes at 150 words a minute; minimum 12" and passes it, because Werner's profile has no words per minute (`HANDOFF.md`: "Plumbing words per minute: not changed yet"). His voice ran at about 181 words a minute here (184 across his 14 older uploads). At that speed the 1,800-word floor is about 10 minutes. This is the case the 2026-10-25 review warned about (`recent-uploads-2026-10-25`, `drafts/tts-hook-and-length-DRAFT.md`, Part 3), now on a second channel.
2. **The trade's motive, joined with "because":** "Nobody in the trade will tell you about the flapper, because a man who knows the flapper does not call." [5:57]. The plumbing pack's villain rule says never "so", "since" or "because" between what the trade earns and what it doesn't say, and Werner's profile says "never motives". It is also the kind of line that drew the study's most-liked doubt (plumbers do tell people about the flapper). The scanner has no check for it.
3. **A promise in the opening:** "If the answer is no, you will know in 2 minutes" [0:19] and "Nothing from a jug goes into a toilet, and you will hear why." [0:47]. The pack (P10): nothing promised in the opening apart from the count line or the escalation line. The escalation line was already there, so these two are extra.
4. **"So, today you learn to unclog a toilet the German way."** [0:10]. A cousin of the banned "today we're going to". The scanner's regex (`today,? (we're|I'm) going to`) doesn't catch this shape.
5. **The first real step comes at 1:04,** against "the first real tip by about 45 seconds". The opening spends 0:28-0:47 listing the whole kit, and then the kit is listed again at 1:59-2:41 ("Now the tools."): the plunger, the bucket, the gloves and the auger twice.
6. **The ending recaps:** "that is the whole of tonight's homework. Find the handle, turn it once, put the flange plunger beside the toilet, not in the garage. Tell everyone in the house the same sentence..." [10:21]. The profile turned his old three-item assignment into "at most one small thing to do", and the pack has no recaps. "Find the handle" is now said four times (1:20, 1:42, 5:53, 10:24).
7. **An overclaim walked back:** "Nothing here needs a plumber." [0:28], then level three ends with "That is the main line, not the toilet, and that is a call." [9:22]. The scope line should say where it stops, not deny that it stops.

### A fact that's wrong, at the moment it matters

- **"Water on the floor, if there is any, is clean tank water."** [6:55]. At level two the bowl has risen to the rim, so what splashes or spills during plunging is bowl water, not tank water. Three minutes later the script says the opposite: "the water that came over the rim was not clean" [9:28]. For a beginner with water on the floor, the first line is the wrong reassurance.
- **A practical gap at the same moment:** level two plunges a bowl that is full to the rim, with no step to bail it down first, so the first push sends it over. Werner's own older video on this topic opens with exactly that step ("you bail one scoop at a time until the bowl is about half full", `transcripts/werner-old11-339UAeV-1LU.txt` [1:05]).
- **The third stop sign isn't explained:** "the water that came over the rim was not clean and it has been sitting" [9:28] is given as a reason to stop, but not why (it's sewage in the floor) or who to call.

### It repeats the channel's own video from two weeks ago

Werner's #11, "How to Unclog ANY Toilet Without a Plunger — The German Kitchen Trick" (`339UAeV-1LU`, 2026-10-13, his most-viewed upload at 1.2K), covers most of the same ground:

| | Old #11 (pre-library) | New video |
|---|---|---|
| Opener | "If your toilet is stopped right now and the water sits high in the bowl, take your hand off the handle. One more flush..." [0:00] | "The toilet is blocked. The water sits high in the bowl... They flush again." [0:00] |
| The fix | dish soap and hot water ("beside your kitchen sink in the bottle you use on the dishes") | "The German household fix is dish soap and hot water." [3:35] |
| Drain cleaner | the reaction gives off heat; porcelain | "The chemicals make heat. Heat can crack porcelain" [3:22] |
| The sink snake | "Its bare steel scrapes the glaze"; "Fush. Botched work. The kind of fix that leaves a bigger job behind it." | "scratches the porcelain inside the bowl... Whoosh, botched work. A repair that leaves a bigger repair behind it." [7:58] |

The new script even sends the viewer back to it at 4:13: "There is a whole video on this channel about that trick... and it goes deeper into the soap and the timing than I will here." That tells a viewer, 37% of the way in, that a better version of this part is elsewhere. Overlap with another channel is fine (operator), but this is the same channel, the same opener image and the same Pfusch line on the same point. The fix belongs at ideation: the brief should have named #11 as a sibling and given this title its own material (the plumbing pack has no "two titles on one topic" rule; the electrical pack does).

### The German way is thin

The title promises "(The German Way)". The German content is: a 12-second aside on wall-hung toilets with the shutoff behind the flush plate [1:45]; one clause calling dish soap and hot water "the German household fix" [3:35] (it's in every American unclogging guide too, so it doesn't feel German); Pfusch; and Vorsorge [10:16]. The profile's engine ("the German habit and the American one set side by side as two answers to the same physics") isn't really running. The best German idea in the script is the one it opens with, knowing where the water stops before you need it (Vorsorge), and it could carry the whole video if the brief gave it two or three real German facts. Every German claim has to come from the brief, so this is a brief problem first.

### Voice and captions

- **"Pfusch" doesn't survive the voice.** Captioned "Whoosh" here [8:04] and "Fush" in #11. Two for two. The profile allows it (no umlaut), but this voice doesn't say it. Worth a listen; if it sounds as bad as the captions, it should come off the German-word list (or be voice-tested first, as the profile already asks for umlaut words).
- **"Werner's" is captioned "Vana's"** in the mid CTA [4:57] and "Werner's" at the end [10:49]; #11's captions had "Vera's", "Vienna's" and "Vanna". The voice probably says it the German way, which suits him, but the captions (and so YouTube's reading of the video) never get the book's name right. Worth a listen, no action unless it sounds wrong.
- **"Vorsorge" read cleanly.** It is also his old tic: Vorsorge was in 9 of his 14 pre-library scripts (`studies/plumbing/werner-baseline-2026-10/counts.md`). Fine once; worth rotating.
- "In most German bathrooms, the way I was trained, the toilet hangs on the wall" [1:45] reads as if his training made the toilet hang on the wall. Reword when used.

### Numbers (caption-based, approximate)

2,010 words; "you" about 28 per 1,000; "but" 5.0; "I" 7.5; 6 question marks; about 28% of sentences six words or fewer; no fire words. The scanner found one sentence over 35 words (the rot sentence at 9:51, 36 words). The "you" rate is on the low side for a how-to (the plumbing pack sets no floor; the electrical pack's how-to floor is 30).

### For the next Werner script

- Get the length from the brief at his real speed: about 2,200 words for 12 minutes, 2,700 for 15.
- One kit list, inside the first step that needs it; the first step by 45 seconds.
- Villain lines as two facts side by side, never "because".
- Nothing promised in the opening beyond the escalation or count line.
- Level two: bail first; the floor water is bowl water.
- End on one small thing, not a list.
- A brief with real German material, and a check against his own earlier titles.

---

## 2. Frederick Barnes: "How to Add an Outlet to a Finished Wall the Right Way (No Patching, No Mess)" (`Z8egZKWQeoI`)

**In one line:** a strong, careful, genuinely useful how-to that follows the electrical pack closely and adds real value well beyond its model; the weaknesses are density (two steps over 500 words), a handful of sentences that don't survive the voice, three small accuracy points, and a words-per-minute figure in the profile that is well off.

### What works

- **The opening does all six jobs in 40 seconds,** in the how-to order: the point and the method in the first sentence ("you feed the new outlet from the one on that wall, run the cable behind the baseboard, and the trim hides every cut" [0:00], so the title's "No Patching" fear is answered in ten seconds); a real check question ("Is the outlet you'd feed from in the kitchen or a bathroom?"); the stake as the hidden work ("a cable where a trim nail lands or a box crammed past what it holds"); the scope ("Every step is yours except aluminum wire or anything inside your panel. That's where you stop." [0:28]); a value promise that names only later steps ("By the end of this video, you'll know how to run the cable so a trim nail can never reach it and whether your old box has room for it." Both are steps 6 and 9); step one at 0:40.
- **The safety is right and in proportion.** Look before you shop is followed literally ("Step three, let what you saw do the shopping." [about 6:10]). The prove-dead order is the pack's: plug-in tester lit in each half, breaker off, dark in each half, non-contact tester checked live-dead-live, every wire in the box, the two-probe fallback for a two-slot outlet. It's repeated in full at step seven after the time away, as the pack requires. The single insistence line lands ("35 years at this and I still check my tester on a live outlet first. Every time. Please prove it dead before a finger goes near a wire." [3:04]): the tenure once, right where it does a job.
- **Fire is the stake once, where it's real:** "a bad connection makes heat. That's the one thing in this job that can start a fire. And a plate the size of your palm takes it off the table." [9:58]. One fire line in 20 minutes, answered in the next sentence. This is the move away from the old firefighter scripts done well.
- **Real teaching beyond the model.** E01 (13M views, 10:50, 1,936 words) has no permit, no circuit check, no gauge, no box fill, no conductor length, no GFCI or AFCI. This script adds all of them, each inside the step that needs it, and every figure checks out against the facts guide: kitchen and bathroom circuits (1.12, 1.13), the inch-and-a-quarter or a nail plate (2.9), a quarter inch of jacket in the box, metal boxes included (2.6), no staples on fished cable (2.8), 2 and 2.25 cubic inches (2.1), 6 inches free and 3 past the box, the clockwise hook (3.2), tamper-resistant (4.1), GFCI within 6 feet of a sink (4.5), AFCI on an extension (6.19). The scanner found no numbers outside the fact source and no copy-guard runs from E01.
- **The voice is Frederick's:** calm, plain, "I" for verdicts ("I'd rather spend 10 minutes on that line than an afternoon on a patch." [8:45]), no invented stories, no old tics, no name intro. Pride lands at the close: "Run your hand along the top of that baseboard flat. The only new drywall edge in the room is under a cover plate." [19:13] and "I'd stand behind that work." [18:42].
- **The ending is exactly the pack's:** a 25-word subscribe line, then "tell me what you found when the plate came off. Copper or silver, full box or empty? Anything that surprised you? I read every one."

### What to fix

1. **Two steps are far too long.** The scanner's step words: 1 = 255, **2 = 555**, 3 = 236, 4 = 101, 5 = 243, 6 = 229, 7 = 347, 8 = 112, 9 = 188, **10 = 514**, 11 = 297. The pack's guide for many-step how-tos is 60 to 150 words a step. Step two (about 2:15 to 6:10, nearly four minutes) does the whole prove-dead sequence, the two-slot fallback, the stray-circuit stop, aluminum, brittle insulation, gauge against breaker, the ground and the box: two steps' worth. Step ten (14:39-17:55) carries the pigtail, the hot, neutral and ground explained, connectors, the hook, backstabs, then tamper-resistant, GFCI line and load, and AFCI outlet versus breaker. Splitting each into two steps (prove it dead / look inside; make the connections / choose the outlet) would give the viewer a resting point without cutting a fact. Steps 7, 8 and 10 have no "I" line (scanner).
2. **Sentences that don't survive the voice** (worth a listen; reword in future scripts):
   - "And an outlet added off, one won't pass." [1:32]. The meaning (an outlet fed from a kitchen or bathroom circuit won't pass inspection) is lost on one listen.
   - "It reads, 'Power on a working outlet first. None on yours once the breaker's off, then power on the working one again.'" [3:58]. An instruction written as a list in quotes; the voice read it as one breathless line.
   - "Two lights means it's wired, right?" [18:18]. The script surely said "wired right"; the voice (or the captions) made it a question. "Wired correctly" can't be misheard.
   - The shopping list at 6:48 ran together into one 52-word caption sentence ("If your old box is metal, a cable connector that clamps..., a tamper-resistant outlet, the kind with little shutters inside..."). A list of fragments reads fine on paper and blurs in the voice.
   - "non-cont tester" [2:56] and "ROMX" [6:16] are probably the captions, not the voice; a quick listen settles it.
3. **Three small accuracy points** (none unsafe):
   - "If that breaker is marked for the kitchen or a bathroom, stop and pick another outlet. Those circuits are only allowed to serve those rooms." [1:32]. Facts guide 1.12: the kitchen circuits may also serve the pantry, breakfast room and dining room. A viewer adding a dining-room outlet is told no when the answer can be yes.
   - "If your old outlet is within six feet of a sink, or in a garage, a basement, or outdoors, the new one needs GFCI protection." [about 16:35]. The test is where the **new** outlet sits. On the same wall the two usually agree, but the sentence keys it to the wrong outlet.
   - "An AFCI outlet at the old box wired the same way. Line in and load out to the new cable covers both." [17:18]. The code's outlet-type option for an extended circuit names the first outlet of the existing circuit, which the old box may not be. The script hedges ("Which one your town wants is a question for the inspector"), but the facts guide has no row on this (4.13 covers replacements, 6.19 extensions), so the writer had nothing to check it against. Worth a facts-guide row.
   - Related facts-guide gap: "If they don't [match], that's not a problem for you to solve. It's a question for an electrician" [5:13]. 12-gauge on a 15-amp breaker is fine; only 14-gauge on 20 amps is the problem. As written it sends a common, safe case to an electrician and leaves the viewer not knowing which cable to buy at step three. No facts-guide row covers it.
4. **The subscribe line is the pack's own example shape:** "you'll have the plain safe answer sitting in your feed" against the pack's "the plain, safe answer to the next thing in the house that won't behave" and the profile's "more plain, safe answers". Fine once; it needs fresh words next time or it becomes his new sign-off.
5. **Words a minute: the profile says 195; this voice ran about 162.** The scanner estimated "about 16.5 minutes" for a 19:52 video. The length floor errs on the safe side (2,340 words is about 14½ minutes at 162), so nothing broke, but runtime estimates and the 15-22-minute sweet spot are off by about a fifth. His old voiceovers ran 169 to 209; 162 is below that, so either the voice is new or the short-sentence style adds pauses. The profile's voice check (the 92-word paragraph) is still open and would settle it.

### Numbers (caption-based, approximate)

3,223 words; "you" about 35 per 1,000 (how-to floor 30); "but" 5.6 (floor 5); "I" 6.2 (target 6-12); about 7 real questions in the body (target 4-8); one fire word; about 26% of sentences six words or fewer (floor 12%). Every floor met.

### A note on reading the numbers

This is the channel's first video since the move from fire prevention. Its subscribers came for "A Firefighter's Warning" titles (the 442K "10 Things a Firefighter Would NEVER Leave Plugged In at Night"), and a 20-minute outlet how-to is a search video for a different viewer. Early views won't compare fairly with the old uploads for a while; search videos tend to build slowly. 24 views in 9 hours is ahead of the recent fire uploads' pace (38 to 149 views after several days), for what that's worth at this age.

---

## 3. What the library could change (for the operator's yes)

Nothing here is applied. Each is small; the first two are pending decisions already.

| # | Change | Evidence |
|---|---|---|
| 1 | **Set Werner's words per minute** (about 181; his old uploads ran 184) so the 12-minute floor is counted at his real speed. This is the plumbing words-per-minute decision held since 2026-10-25 ("do not change 3 yet"), now with a second channel under 12 minutes. | Werner 11:06 at 2,010 words; scanner said 13.4 minutes. |
| 2 | **Frederick's words per minute: run the profile's voice check** and set the figure (about 162 on this video, against 195 in the profile). | Scanner estimate 16.5 minutes; actual 19:52. |
| 3 | **Scanner: flag a motive joined to the trade** ("because", "so", "since" between "the trade / plumbers / nobody" and "call / charge / bill") on the plumbing channels. | "Nobody in the trade will tell you about the flapper, because a man who knows the flapper does not call." |
| 4 | **Scanner: widen the "today" opening ban** to "today you learn / today you will / today I will show". | "So, today you learn to unclog a toilet the German way." |
| 5 | **Werner's German words: take Pfusch off the list** unless the voice check passes it. | Captioned "Fush" (#11) and "Whoosh" (this video). |
| 6 | **Plumbing pack: a sibling check against the channel's own earlier titles,** as the electrical pack's "Two titles on one topic" already does. | This video re-runs #11's opener, fix, warnings and Pfusch line, and points viewers back to it. |
| 7 | **Facts guide rows:** the AFCI outlet option on an extension (first outlet of the existing circuit), and wire gauge against breaker size (12-gauge on 15 amps is fine; 14 on 20 is not). | Frederick [17:18] and [5:13]. |
| 8 | **Electrical pack: one step, one job.** A step over about 300 words splits in two. | Frederick's steps two (555 words) and ten (514). |
