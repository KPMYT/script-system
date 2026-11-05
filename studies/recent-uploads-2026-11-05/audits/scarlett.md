# Audit: Scarlett Starling, three newest uploads (2026-11-05)

Channel `UCTMwV-uy20eaRwFfc4Sx13g`. The first three uploads since the style pack and Scarlett's profile were built (2026-10-28/29).

- **Source:** YouTube's automatic captions, pulled with NexLev `get_bulk_video_transcripts` on 2026-11-05 (all three came back; none empty). Transcripts: `../transcripts/scarlett-<videoId>.txt`.
- **Views** are the public counts at collection on 2026-11-05 (given by the main session). One to four days old, so they say nothing yet.
- **Caution: these are captions, not the VAs' scripts.** They record what the voice said, in the caption system's spelling and punctuation ("7/8", "3 ft", "PC ends", "low lightss"). Sentence counts and question marks taken from them are approximate. Timestamps below are the start of the caption segment holding the quote, so they can sit a few seconds off the 30-second lines in the transcript files.
- **Rules audited against:** `style-scripts/SKILL.md` (whole), `style-scripts/references/hooks.md`, `personas/scarlett-starling.md`, `personas/books/scarlett-starling-book.md`, `HANDOFF.md` §3 (Operator decisions, 2026-10-29, session 14), `core/retention-mechanics.md` §14, `core/greenlight-audit.md` B9, `core/humanizer.md` H21, `core/cta-and-endings.md`. Baseline: `studies/style/comparison/README.md` findings 15-19 (our 38 pre-library scripts).
- **Scanner:** `core/script-scanner.py` on timestamp-stripped copies (kept outside the repo), `--rules style-scripts/SKILL.md personas/scarlett-starling.md`, `--refs` the profile, the pack, `excerpts.md`, `voice-samples.md`, `hooks.md` and every model file, `--title` each title. No copy-guard hits, no ban-list hits on any video. Its caption-made flags are left out below ("3 ft", "7/8", and the 49-word run-on at 10:08 in the leggings video).
- **Words a minute** = caption words over the whole video length. **Minutes at profile speed** = caption words / 169 (Scarlett's profile).

## Library-made or old-style? Library-made, all three

The study found the same packaging in all 38 old scripts (finding 15): "I'm Scarlet Sterling and this channel is for women over 60…" between 0:25 and 1:16, the book pitched twice before 7:28, and "Until next time, stay polished and stay sterling". None of that is in any of the three. Every library marker is there:

| Marker | Old scripts (study baseline) | Granny cut (`Jgp7nzZpN9k`) | Leggings (`XaSctY7Qeyc`) | Elegant women (`4kVamjO4Y4U`) |
|---|---|---|---|---|
| Self-introduction / "this channel is for women over 60" | 38 of 38 | none | none | none |
| Sign-off ("stay polished and stay sterling") | 25 of 25 (Scarlett) | none | none | none |
| Opening on a `hooks.md` model | n/a (36 of 38 opened on "Picture…") | M04's three moves, 40 words, the same length as M04 | M30's moves 1-4 | closest M06 (reading, see below) |
| Item one at | median 1:39 | 0:18 | 0:33 | 0:37 |
| Book pitches | twice, 2:18-7:28 | once mid (4:28) + one end line | once mid (4:18) + one end line | once mid (4:04) + one end line |
| Comment ask | "which one will you try first" (1 answer in about 42 comments) | how long she's worn her cut and what she calls it | the leggings rule she was handed, kept or broken | the piece she's kept 20 years or more |
| Title's promise word said | "instantly" in 0 of 14 "instantly" titles | "younger instantly" 3 times (0:12, 7:46, 14:42), "younger" 6, "avoid" 2 | "frumpy" 7 (first at 0:00) | "elegant" 11 (first at 0:00) |
| "small gold hoops" / "reads as" / "quietly" / "from across the room" | 22 / 112 uses / 32 / 18 videos | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| "but" per 1,000 words | 1.0-1.1 | 5.4 | 5.1 | 5.0 |
| "you/your" per 1,000 | 34-40 | 57 | 45 | 46 |
| "I" per 1,000 (with I'd, I'm, I've, I'll) | 4-6 | 3.8 | 6.2 | 4.1 |
| Questions (approx.) | 0.4-1.4 a script | 5 | 9 | 7 |
| Credential line | none in 38 | "a lifetime of dressing well" (8:58) | none | "a lifetime of dressing well" (12:57) |
| Approved personal detail | none | none | the season's closet edit (15:08) | the hall mirror (2:08) |
| Mid CTA book match | none | the Hair Hack chapter, Ways 197 and 198 (correct) | the Pants Vocabulary, Way 105 (correct, word for word) | the Tailor's Secret, Ways 11, 12, 15 (correct) |

The only baseline gap still open is **"I"**: 3.8 to 6.2 per 1,000 against the pack's guide of about 10 (reported, never a fail), the same range as the old scripts (4-6).

---

## 1. "AVOID the "Granny" Cut! 7 Haircuts That Make Women Over 60 Look Younger Instantly" (`Jgp7nzZpN9k`)

Published 2026-11-04 · 15:41 · 365 views at collection.

**In one line:** the best-built of the three: a 40-word hook carried move for move from M04, item one at 0:18, the title said in full and often, a correct book match and both safety defaults in place; the faults are a mid-video CTA that runs long with an off-topic fact, a closing run-back of the chair words, and one reframe too many.

### What works

- **The hook is M04's format, applied** (`hooks.md`: feared look > cause > count > item one, 40 words). Ours is 40 words: "Forgive me, but the granny cut adds years to a face." [0:00] (the feared look, the hard word flagged once as the pack asks) / "The shape does it, never the length. Short, rounded, sprayed, flat at the back." [0:02] (the cause) / "Seven haircuts look younger instantly after 60, and one is a small change from yours." [0:12] (the count, with M04's "there's something on this list that you're probably doing right now" turned into "one is a small change from yours") / "Number one, the textured pixie." [0:18].
- **The title is paid in its own words.** "look younger instantly" at 0:12; "looks younger instantly" at 7:46; "A bang that moves looks younger instantly" [14:42]; "That dome is the shape to avoid" [0:54]; "it's the fringe to avoid" [13:28]. The old scripts never said "instantly" (finding 17).
- **Her own mirror, then the why, in every item:** "Look at your shortcut straight on in your bathroom mirror. If the top sits in a smooth rounded dome and nothing moves when you turn your head, that is the first part of the problem." [0:18]; "A dome puts the roundness of the cut on top of the roundness of your face" [0:31].
- **The words to say in the chair, the pack's hair fix** (how to be heard, never blame): "Ask for it in those words. Crown cut high. PC ends. Clean nape. A soft side fringe." [1:52]; "say no blunt perimeter because you want your bottom edge soft, not a ruler line." [3:41].
- **The blame moves off her, in fresh words:** "That cut wasn't wrong for you. It was wrong for hair that has gone finer than it used to be" [3:16].
- **Permission with the villain the pack allows** (advice she was handed): "You may have been told that your long hair has to go at 60. I don't believe it." [8:53]; "Length is neutral." [9:04].
- **The credential once, before a verdict, as the profile asks:** "And a lifetime of dressing well has not changed my mind." [8:58].
- **Feeling lines, short and plain:** "Nervous about bangs? That's fair. And this is the gentle way in." [14:02].
- **Safety defaults 2 and 3, one line each, in proportion:** "If your shedding started suddenly or there are patches, that's a question for your doctor, not your stylist." [8:35]; "use a heat protectant first on a lower setting because fine or gray hair scorches faster than it used to." [11:56].
- **Bridges without teases:** "That's the short end of the list done. Three of the seven keep your length and that's where the next one starts." [8:43]; "The next cut takes those layers further and it's the easiest one on the list to keep up." [10:32]. Item seven pays back the hook's dome: "Here is where the second half of the dome gets fixed. The front." [12:55].
- **The comment ask is about her and ends the video:** "Down in the comments, tell me how long you've worn the cut you have right now and what you call it." [15:25].

### Rule breaks

1. **The mid-video CTA runs 97 words and carries four book facts, one off-topic.** [4:28-5:05] "My book, 300 budget friendly ways to look expensive, has a chapter called the hair hack. Two of its ways are these exact cuts. … Every one of the 300 ways gives you the swap and the payoff. And one chapter holds 10 nocost quick wins made with what's already in your closet." Rule: `style-scripts/SKILL.md` "CTAs" and the profile's CTA "Style and length": 60 to 90 words; the book by its title "with one true fact", plus the chapter that covers today's topic. The facts are all true (book index: chapter 19, Ways 197 and 198; Ways 251-260), but the quick-wins chapter has nothing to do with haircuts. **Fix:** keep the Hair Hack chapter and its two Ways, drop the quick-wins sentence; that also brings it under 90.
2. **The close runs back over the items.** [14:49] "That is the seventh cut. And now you know what each one does to the shape of your face. So the words for the chair come down to the same few, whichever cut you pick. soft movement, face framing, no blunt perimeter, and point cut ends." All four were said in items two, five and six. Rule: `core/retention-mechanics.md` §14 ("No recap, no wind-down… a closing to-do list… that runs back over what earlier sections already said is a recap, however it is phrased"), `greenlight-audit.md` B9, and the pack's "No recaps". **Fix:** end item seven on its result ("A bang that moves looks younger instantly" is a good last line) and go straight to the book line; if a last action is wanted, one new one, not the list.
3. **Two "not X, it's Y" reframes** (judged count; the scanner's machine count caught one): "The shape does it, never the length." [0:02] and "That cut wasn't wrong for you. It was wrong for hair that has gone finer…" [3:16]. Rule: `core/humanizer.md` H21 (at most one a script) and the pack's Emotion rule 5 (the blame moves off her once; it counts as the one reframe). **Fix:** keep the 3:16 line (it's the blame move); say the hook's cause straight ("The shape does it: short, rounded, sprayed, flat at the back").

### Facts worth checking

- **The end line claims every cut is in the book** [15:16]: "Every cut in this video and the 300 ways around them are in 300 budget friendly ways to look expensive". *Measured from the book index:* the Hair Hack chapter's Way titles cover the layered bob (197), the textured pixie (198) and keeping length with movement (199); no Way title names a shag, a stacked bob, an angled lob or a side-swept bang. The index doesn't hold the full text, so the cuts may be inside other Ways; until someone checks the OCR, this is not one of the profile's "true facts", the only facts a CTA may use. Safer: "the bob and the pixie are both in…".
- *Reading:* "a diagonal line is the most flattering line a cut can draw across a face" [13:49] and "A sides swept fringe grows out without a bad stage" [14:08] are opinions said as facts; "without a bad stage" overpromises.
- *Reading:* "A flat back makes your head look smaller and your neck look longer in the wrong way" [7:14] is an odd claim; a stylist would say a flat back makes the head look flat or the neck look exposed.
- *Reading:* "Hair with the weight taken out of the middle springs up and looks denser, not thinner" [3:41]. True of thick, heavy hair; on very fine hair, internal layers can thin the ends, which is the hair this item is addressed to. Worth a hedge.
- *Reading, close to the line:* "and nobody said so in the chair" [3:16]. The salon is never the enemy, "not even in tone" (`style-scripts/SKILL.md` "The villain"; HANDOFF §3, 2026-10-29). This is mild and the item does give the words for the chair, but it points at the stylist.

### Voice and caption oddities (worth a listen)

- "PC ends" [1:55]: the script surely said "piecey" (captioned "piecy" at 1:03). The scanner flags it as spoken letters. If the voice says "P.C.", spell it "piece-y" in the VO copy.
- "Look at your shortcut straight on" [0:18] (short cut), "low lightss" [12:20], "sides swept" [12:55, 13:28], "seethrough", "nocost", "leavein", "chinlength": caption joins, almost certainly said right.
- **The captions stop mid-sentence:** "Is it the one you've worn the longest, or did you change it at" [15:38], with the video ending at 15:41. The last words (probably "60?") may be in the last 3 seconds without captions, or the voiceover may be cut. Worth a listen to the end.
- The shag definition [10:40] is one 36-word sentence (the scanner's only over-35 flag). It may be caption punctuation; if the script has it as one sentence, split it.

### Numbers (caption-based, approximate)

| Measure | Value |
|---|---|
| Length | 15:41 |
| Caption words | 2,394 |
| Words a minute (actual) | about 153 (the profile says 169; this voice ran slower) |
| Minutes at 169 | about 14.2 (minimum 12: met) |
| Hook | 40 words; item one at 0:18 (scanner: word 40, about 14 seconds at 169) |
| Opening promises | 0 beyond the count line |
| Items | 7, 248-427 words each (scanner; all in the 150-480 band) |
| Mid CTA | 4:28 (28% in), 97 words |
| End book line / comment ask | 15:16 / 15:25 |
| "you/your" per 1,000 | 57 |
| "but" per 1,000 | 5.4 (13) |
| "I" per 1,000 | 2.1 bare "I"; 3.8 with I'd, I'm, I've, I'll |
| Question marks | 5 |
| Contractions per 1,000 | about 15 |
| Sentences of 6 words or fewer | 16.4% (scanner) |

---

## 2. "How to Wear Leggings Over 60 Without Looking Frumpy" (`XaSctY7Qeyc`)

Published 2026-11-03 · 15:56 · 625 views at collection.

**In one line:** a strong, practical how-to-wear video: M30's hook, five rules each with a check she can run, seven outfits that keep the rules, a word-for-word book match; the ending piles up several actions after the last look, and two contrast lines read as poster lines.

### What works

- **The hook is M30's moves 1 to 4, shorter than the model** (M30: feared look > question > count > reassurance/scope, 124 words for those moves; ours 100): "Leggings are the easiest thing in your closet, right up until you catch yourself in a shop window and the whole outfit looks frumpy. So, the leggings go back in the drawer and the stiff pants come out again." [0:00] / "How many pairs do you own that only ever see the inside of your house?" [0:11] / "There are five rules that make leggings look polished after 60. And once you have them, I'll build seven outfits you can copy piece by piece." [0:17] / "All it takes is the right top, the right fabric, and the right length, and the closet you already have." / "Rule one" at 0:33.
- **The title's feeling, named, then answered by a rule:** "This is the rule that decides whether leggings look frumpy or finished" [0:33]; "That's where the uneasy feeling comes from, the tug at the sweater every time you stand up." [0:54].
- **A check she can run, in every rule, given plainly:** "Put the outfit on, turn your back to a full-length mirror, and look over your shoulder." [1:05]; "Now, the bend test. Stand in front of a window in daylight…" [2:08]; "Sit down in them in the store, then stand up. Did the band stay where you put it? Can you breathe?" [3:42]; "Step back about 3 ft from the mirror. From there, the leggings should pass for slim black pants." [10:53].
- **Permission and the out, as the viewer section asks:** "If you can see where your seat ends, the top is too short for leggings, but it's a lovely top for jeans instead. You don't lose it, you just move it." [1:05].
- **Her body named, not assumed slim:** "most women carry a little more there than they used to" [3:16]; "This one is the easiest for a fuller middle" [9:47].
- **Safety default 4, as a choice not a warning:** "I'd keep a block heel over a thin one because it's steadier on a wet sidewalk" [7:08].
- **The book match is exact.** "the one called the pants vocabulary holds a way called fit the waistband to sit without a gap or a dig" [4:23]: chapter 10 and Way 105 in the book index, word for word. "It runs 28 chapters" is a profile fact. 82 words, after rule three of five (27% in), tied to the help just given ("That waistband check is the kind of fix…"), with a return line ("Now, the length, because that's where the frumpy look sneaks back in.").
- **The approved personal detail, once:** "Once a season, I take everything out of the closet and put back only what I'd buy again today." [15:08].
- **The comment ask is the pack's rotation option 3, made specific:** "What was the rule you were handed about leggings years ago? And are you still following it, or did you break it?" [15:46]. Nothing after it.
- No prices on a non-budget title; "camel" once; no "Picture…".

### Rule breaks

1. **The ending gives a list of actions, partly a run-back.** [14:46-15:35] "One last thing before you go shopping… Four pairs cover everything in this video. A black ponte pair for the tunic days and the blazer days. … One navy or brown pair for the column and the softer looks. And one matte faux leather for the evenings." Then the season's edit, then "wash them inside out on cool and hang them to dry. Skip the dryer entirely…". That's about 150 words and five actions after the last look, and the four pairs map back onto looks one, four, five and six. Rule: `core/retention-mechanics.md` §14 ("**One** action"; a closing list that runs back over earlier sections is a recap) and `greenlight-audit.md` B9. **Fix:** keep one: the four-pair list *or* the care line (the care line is new information and the stronger last action), and cut the mapping back to the looks.
2. **A poster line, and a second reframe** (judged): "Comfort you can see is frumpy. Comfort you can't see is polished." [9:29]. Rule: the pack's "Voice" ("Plain over clever. No poster lines…") and `core/humanizer.md` H21 (at most one "not X, it's Y" a script; the first is "the reason the length works isn't modesty. A longer top makes one smooth line" [1:34]). **Fix:** say it plainly ("A sweatshirt shows the comfort; this outfit hides it.") or drop it; the look already makes the point.

### Facts worth checking

- **The end line claims the whole video is in the book** [15:35]: "Everything in this video has a longer version in 300 budget-friendly ways to look expensive". *Measured from the book index:* no Way title or chapter covers leggings; the waistband (Way 105), the hem (chapter 2), colors and shoes are there, but "everything" is not supported by the index. The profile allows only true facts in a CTA. Safer: "the waistband and the hem are both in…".
- *Reading:* "I'd rather see you in one long plain top than three short pretty ones" [1:08] and "I'd rather you bought one pair with the right band than three with the wrong one" [4:05]: the same sentence shape twice; fine, but a habit to watch.
- *Reading:* "A tailor can take an inch or two off a knit hem in a few minutes" [5:20]: a stretch hem needs a stretch stitch or a coverstitch; "in a few minutes" is optimistic, and not every tailor does knits. A hedge would help.
- *Reading:* rule five says "A white sneaker is the one exception, but it only works when everything else on you is dark" [6:51], and look seven pairs "spotless white sneakers" with a sweatshirt and a quilted vest of no stated color. Consistent only if those are dark; worth a word.
- *Reading:* "Of the seven, this is the one that gets a compliment from a stranger" [12:15] is a stranger judging her, which Emotion rule 2 steers away from ("Never an imagined stranger judging her"); here the stranger is kind, so it's borderline.
- *Reading:* "the kind of fix I put in my book" [4:23] is near the profile's banned provenance formula ("Never 'I gathered' or 'I collected'"). It isn't on the list, but it's the same move.

### Voice and caption oddities (worth a listen)

- **"Look for thick matte ponte leggings…"** [10:33]: the signpost for look four. The script almost certainly said "Look four." and the caption system heard "Look for". A listener can hear it the same way, so the fourth outfit loses its number. Signposts like "The fourth look." can't be misheard.
- **"Fix the length, and I do it before anything else in this video"** [5:35]: probably "I'd do it". If the voice says "I do it", it's a first-person experience claim (pack "Proof": never "I wore", "I bought"…). A quick listen settles it.
- "7/8 length" [5:11], "3 ft" [10:53], "Keep the heel at about 2 in" [7:08]: caption digits; check the voice said "seven-eighths", "three feet", "two inches".

### Numbers (caption-based, approximate)

| Measure | Value |
|---|---|
| Length | 15:56 |
| Caption words | 2,752 |
| Words a minute (actual) | about 173 |
| Minutes at 169 | about 16.3 (minimum 12: met; just over the 12-16 aim) |
| Hook | 100 words; item one ("Rule one") at 0:33 |
| Opening promises | 1 beyond the count line ("I'll build seven outfits you can copy piece by piece"), which reads as part of the count line |
| Items | 5 rules (217-304 words) + 7 looks; the scanner reads only the five rules as items, so its "item 5 = 1691" is the looks counted as one |
| Mid CTA | 4:18 (27% in), 82 words |
| End book line / comment ask | 15:35 / 15:46 |
| "you/your" per 1,000 | 45 |
| "but" per 1,000 | 5.1 (14) |
| "I" per 1,000 | 1.8 bare "I"; 6.2 with I'd, I'm, I've, I'll |
| Question marks | 9 |
| Contractions per 1,000 | about 21 |
| Sentences of 6 words or fewer | 15.8% (scanner) |

---

## 3. "7 Style Choices Elegant Women Over 50 Always Make" (`4kVamjO4Y4U`)

Published 2026-11-01 · 13:23 · 108 views at collection.

**In one line:** library-made and good to listen to, with clear checks and real permission lines, but it's the loosest of the three: a 104-word hook with more moves than any model, a 108-word mid CTA with a book claim the index doesn't support, three or four reframes, and a tail on item seven that repeats the mirror check.

### What works

- **The opening puts her at her own closet against the woman who gets it right:** "You know the woman I mean. Nothing she wears is loud, nothing is new, and she still looks more elegant than anyone else in the room. You stand at your own closet with twice as many clothes, and somehow the outfit never quite comes together." [0:00]. The title word "elegant" in the second sentence.
- **The blame moves off her body, in fresh words:** "None of that is your body. That jacket was cut for a different shoulder, and that's the only thing wrong with it." [1:23].
- **The approved hall-mirror detail, doing a job (the check), once:** "I keep one last look in the mirror by my front door before I go anywhere, and that is where a bad hem gives itself away every time." [2:08].
- **Checks she can run:** "can you tell where your waist is? If the answer is no, one of the halves needs to come in." [3:51]; "Hold a few candidates up under your chin in daylight at a window, not under the closet bulb." [5:34]; "crush a corner in your fist for a few seconds and let go." [7:32].
- **Permission, specific:** "If it's pilled, it's not going to look elegant no matter what you pair it with and you have permission to let it go." [7:50]; "Nothing you own is too good for your own life." [12:22].
- **Safety default 4, in proportion:** "A low block heel gives you the lift without asking your balance to do any work. If a heel isn't steady for you, a sleek flat with a pointed toe does the same job" [9:46].
- **The priority flag once:** "If you change one thing after this video, change this one." [8:13].
- **Palette facts line up with the book:** six colors (five neutrals and one accent) [5:02] matches Way 46, "Cap Your Palette at Six Colors".
- **The credential once, at a verdict:** "And after a lifetime of dressing well, I think that's the only opinion you need." [12:57].
- **The comment ask is about her** (rotation option 2): "tell me about the one piece you've kept and worn for 20 years or more. What is it, and why has it lasted?" [13:10]. Nothing after it.

### Rule breaks

1. **The mid-video CTA runs 108 words, and one of its book claims isn't supported.** [4:04-4:41] "And the chapter called The Tailor's Secret walks you through the hem, the sleeve, and the side seam. It opens with one rule worth the whole book, the fit-first rule, which says a well-fitted basic will always beat a badly fitted designer piece." Rule: `style-scripts/SKILL.md` "CTAs" and the profile (60 to 90 words; one true fact plus the chapter; the profile's true facts are the only facts a CTA may state). *Measured from the book index:* the Tailor's Secret holds the hem (Way 11), the side seams (12) and the sleeves (15), so that sentence is right; but the Fit-First Rule is introduced on p. 13, in the introduction, and the chapter opens on Way 11, "Hem Your Trousers to Break Once, Softly". "It opens with" is wrong if "it" is the chapter, and "worth the whole book" is puffery. **Fix:** cut the Fit-First sentence (or say "the book's Fit-First Rule says…", which is a listed fact) and end on the link and the QR code; that lands at about 70 words.
2. **The tail of item seven adds two more habits and repeats the check a third time.** [12:26] "Two last habits go with this, and they're small. Leave your hair slightly undone… And check the whole outfit before you go, in a full-length mirror or on a quick video on your phone, in daylight. The closet light is kind to everything, but it tells you nothing. A full-length mirror in daylight tells you the truth." The full-length mirror check was already given in item one ("look in your full-length mirror" [1:56]) and item five. Rule: `core/retention-mechanics.md` §14 (one action at the end) and the pack's "Length" ("Never pad. Cut repetition: the same check said twice"). **Fix:** end item seven on its own result ("Nothing you own is too good for your own life." is the natural last line) and go to the credential line and the book.
3. **Three to four "not X, it's Y" reframes** (judged count; the scanner's machine count found none): "Looking elegant after 50 has nothing to do with money, and it has nothing to do with trends. It comes from a few choices she makes" [0:18]; "None of that is your body. That jacket was cut for a different shoulder" [1:23]; "It isn't a failure. The fabric just wasn't made to last." [7:54]; "You weren't wrong to put it on. The outfit was finished without it." [11:08]. Rule: `core/humanizer.md` H21 (at most one a script) and the pack's Emotion rule 5 (the blame moves off her **once**). **Fix:** keep 1:23 (the best of them); turn the others into plain statements ("Pilled fabric doesn't recover. Let it go.").

### Facts worth checking

- **The end line claims all seven are in the book** [13:02]: "All seven of these, and the rest of the 300, are waiting in 300 budget-friendly ways to look expensive". *Measured from the book index:* fit (chapters 1-2), the palette (Way 46), fabric (chapter 3, the Fabric Touch Test), one statement accessory (Way 143) and wearing the good pieces (chapter 27) are there; "one loose piece, one fitted piece" and "a little tension" (basic with luxe) have no matching Way title. Probably close to true; not checkable from the index.
- **Mid CTA: "The hem and the balance you just heard are two moves out of 300"** [4:04]. The hem is Way 11; "the balance" (one loose, one fitted) has no matching Way title in the index (the nearest is Way 99, wide-leg trousers balancing a fuller middle).
- *Reading:* "after three washes, it pills at the elbows and under the arms" [6:55]: a specific number said as fact; fabric-dependent.
- *Reading:* "Good fabric feels cool and dry and a cheap one feels slick" [7:17]: many synthetics feel cool too; the Fabric Touch Test in the book is about light, not temperature.
- *Reading:* "A low block heel gives you the lift without asking your balance to do any work" [9:46] overpromises for a 70-year-old viewer; "much less work" is safer.

### Voice and caption oddities (worth a listen)

- **"This is almost nobody talks about, but you can spot it on every well-dressed woman you pass."** [2:28]: a word missing ("This is the one almost nobody talks about"). Either the script or the voice dropped it; a listen settles which.
- "isn't it?" [1:04] after "it's hard to say why": a tag question that the voice may read flat; fine on paper.

### Hook model (reading, not a rule)

The video type is "the rules she never breaks", whose only `hooks.md` entry is F06 (count first, moves only), and this hook doesn't follow F06. The closest real model is M06 ("You know that girlfriend you have that looks 20 years younger…"): ours opens the same way ("You know the woman I mean") and carries M06's promise ("This video is about why, and it's fixable." [0:15]) and reassurance. But it moves the feared look to second place and adds a count line, which M06 doesn't have; six moves and 104 words against the winners' median of 3.5 moves and about 80 words. Under the 110-word ceiling and item one by 45 seconds, so no written rule is broken, but the pack's "Add no move" can't be checked without the VA's plan. The line "the chicest women never look like they tried too hard" [0:31] is close to a slogan.

### Title word "Always"

Said once, inside the mid CTA ("will always beat" [4:33]); the hook carries it as "every single time" [0:28]. The scanner's title-words list has no "always", so nothing was flagged. *Reading:* "every single time" pays the meaning; no fix needed.

### Numbers (caption-based, approximate)

| Measure | Value |
|---|---|
| Length | 13:23 |
| Caption words | 2,218 |
| Words a minute (actual) | about 166 |
| Minutes at 169 | about 13.1 (minimum 12: met) |
| Hook | 104 words; item one at 0:37 (scanner: word 104, about 37 seconds at 169) |
| Opening promises | 1 beyond the count line ("This video is about why, and it's fixable.") |
| Items | 7, 218-386 words each (scanner; all in band) |
| Mid CTA | 4:04 (30% in), 108 words |
| End book line / comment ask | 13:02 / 13:10 |
| "you/your" per 1,000 | 46 |
| "but" per 1,000 | 5.0 (11) |
| "I" per 1,000 | 3.2 bare "I"; 4.1 with I'd, I'm, I've, I'll |
| Question marks | 7 |
| Contractions per 1,000 | about 23 |
| Sentences of 6 words or fewer | 16.4% (scanner) |

---

## Channel level

### Patterns (3 of 3 videos)

1. **All three are library-made.** No intro, no sign-off, the book once mid-video plus one end line, the comment ask about her, item one by 0:37, the title's words said, the house vocabulary gone, "but" up from about 1 to about 5 per 1,000, questions up from under 1.5 to 5-9 a script. Every baseline gap in `studies/style/comparison/README.md` findings 15-19 is closed except "I".
2. **"I" stays at the old level:** 3.8, 6.2 and 4.1 per 1,000 (with contractions) against a guide of about 10 and the old scripts' 4-6. A reported number, never a fail; but it's the one emotion measure that hasn't moved.
3. **The end book line claims more than the index supports:** "Every cut in this video…", "Everything in this video has a longer version…", "All seven of these… are waiting in…". The profile's true facts don't include "everything in this video is in the book", and the index can confirm only part of each.
4. **The ending does more than one thing** after the last item: a run-back of the chair words (granny cut), a list of four pairs plus care steps (leggings), two extra habits plus the mirror check again (elegant). §14's "one action" is the rule.
5. **More than one reframe** in every script (judged: 2, 2 and 3-4), against H21's one.
6. **The mid CTA's book match is right every time** (Ways 197/198, 105, 11/12/15), and the "swap and the payoff" fact appears in all three; two of the three CTAs run past 90 words (97, 108).

### Compared with the previous review

`studies/recent-uploads-2026-10-29/` reviewed Werner and Frederick, not Scarlett, so this is the channel's first upload review. One echo across channels: the leggings CTA opens "Before the fourth rule, one small thing." and Werner's toilet video opened its CTA "Before level two, one small thing." Fine on two channels; worth rotating so it doesn't become the library's signature aside. Werner's review also found a closing homework list; the same §14 problem shows here in a softer form, a week after the operator's decision of 2026-10-29 (one small thing at the end, never a homework list, on every channel).

The granny-cut voice ran at about 153 words a minute against the profile's 169 (the other two: 173 and 166). One video is not a reason to change the profile; if the next uploads also run near 153, the 12-minute floor counted at 169 would still be safe (it errs long).

### Top 3 fixes

1. **End on one thing.** After the last item: its result, the one-line book reminder, the comment ask. No run-back of the chair words, no list of pairs, no second set of habits (§14, B9).
2. **The book lines say only what the index confirms.** Mid CTA 60-90 words with the chapter and one fact; the end line names what's really in the book ("the bob and the pixie are both in…"), never "everything in this video".
3. **One reframe a script, and more "I" as opinion.** Keep the one blame-moves-off-her line; say the rest straight. Let her verdicts carry more of the item ("I'd keep…", "I think…") toward the guide of about 10 per 1,000.
