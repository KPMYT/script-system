# TEST: judge report, iter-07 run 02

Scarlett Starling, "You're Styling Your Bob WRONG After 60 — 5 Secrets To Turn Heads Instantly". All material is TEST. Judged on 2026-10-29 against `tests/iterations/iter-07/judge-rubric.md`.

Inputs read: `test-run-02/chat.md`, `output.md`, `script.txt`, `scanner-main-session.txt` (with `verify_output.py`'s findings), `brief-02.txt`, `refs/h9MsF44shdQ-ours-transcript.txt` (our old script, 514 views), `refs/vFul5tvg1Cw-M12-transcript.txt` (the winner, Justin Hickox, 3.2M), `style-scripts/SKILL.md`, `style-scripts/references/hooks.md`, `style-scripts/references/voice-samples.md`, `personas/scarlett-starling.md`, `personas/books/scarlett-starling-book.md`, `core/workflow.md` §1-6, `core/script-scanner.py` (the example guard).

Facts from the main session, taken as given:
1. The scanner's one fix-on-sight (the copy guard matching the book's 8-word spoken title against the profile) is a library gap, not a writer slip.
2. `verify_output.py`'s one "quote not in the script" is the writer quoting M04's hook line as the model it graded against: a tool false positive, not an audit error.
3. The gate question is judged under "The gate" below.

## 1. Verdict

Yes, this meets the operator's bar, and I would upload it after a one-line fix (the tuck instruction in item four, which is backwards). The hook is 104 words. It carries M08's moves in order, item one starts at about 37 seconds, and it names the right hair feeling first: "If your bob never looks right at home". Every item does what the pack asks. It shows the look in her own mirror, says why in plain words ("that shape pulls the eye straight down to the jawline"), turns on a "but" or a question, gives the brief's fix, gives a check she can run alone (side view, a profile photo, the head-shake, two photos in daylight, the window), and ends on the result. The blame moves off her once, in fresh words: "But the cut didn't go anywhere. The blow-dry in the chair put lift in at the roots, and nobody showed you that step." There are no intros, teases, slogans, house vocabulary, prices, a subscribe ask or a sign-off. The ending is the book reminder, then the question about her. It is far better than our old script (69/140), which opened with a name intro and a tease, used three "Picture/Imagine/Think of" scenes, and closed with a subscribe ask, "which one first" and "stay polished and stay sterling". On our rubric it also beats the winner. The winner's strength is a real stylist doing a live demo, which a persona can't copy. The script is let down by small things: a backwards tuck instruction, the heat-safety line said three times, item one at 456 words, two muddy lines, and "I" used at about half the guide rate.

### The gate (fact 3)

The gate behaved correctly. In turn 1 the title came on the START line with no channel, so reply 1 was the numbered channel list and nothing else (`core/workflow.md` §1.1). In turn 2, "just write it, I'm in a rush", the chat refused without lecturing, said what was still needed, and listed the channels again (`workflow.md` §1.1 "Anything else gets the list again" and §2 "No way around it"). It did not ask for the brief before the channel was chosen, so there was still only one question at a time. In turn 3, "it's for Scarlett" on its own is not the exact name §1 asks for, but the same message pasted "CHANNEL: Scarlett Starling (ch. 1, the affluent American)" with the exact name. The TITLE line matched the START line word for word, and the brief and "rotation log: none" were both there. Every input passed, so going straight to the run was right (§2, bulk mode). One small library point: §1 says to accept "the number or the exact name". It should say whether a first name that matches one channel only (here, and "Scarlett, the rich American one" in run 01) counts as a match.

## 2. Scores

1 to 10 each. The hook counts double. Total out of 140.

| Category | New | Ours (h9MsF44shdQ) | Winner (M12) |
|---|---|---|---|
| The hook (x2) | 8 (16) | 2 (4) | 5 (10) |
| Keeping the title's promise | 9 | 5 | 8 |
| Clarity on one listen | 8 | 6 | 5 |
| Emotion | 8 | 4 | 6 |
| Voice and persona | 8 | 3 | 5 |
| Claims and proof | 9 | 6 | 4 |
| Money | 10 | 7 | 4 |
| Safety | 9 | 6 | 7 |
| Written for the voice | 10 | 8 | 6 |
| CTA and ending | 9 | 2 | 2 |
| Length and pacing | 7 | 5 | 5 |
| Originality vs the models | 9 | 7 | 8 |
| Audit honesty | 9 | 5 (n/a, neutral) | 5 (n/a, neutral) |
| **Total / 140** | **121** | **68** | **75** |

How the references were scored. Our old script and M12 have no audit, so they get a neutral 5 there. M12 is a real stylist working live on camera, with a sponsor, before-and-after photos and a client. It was scored against the same persona rules, so its total shows how well it fits our rules, not what it is worth on YouTube. A real stylist doing a live demo earns trust that no persona script can get. M12 got its 3.2M views on that trust, not on how its script is built.

Counts, by script (`python3 -I`; tokens are letters and digits with apostrophes and hyphens kept. Markers are excluded from the new script, and timestamps and the header line from the transcripts. My word count is 2,168 against the scanner's 2,164. Use the scanner's for length.)

| Per 1,000 words | New (2,168) | Ours (2,774) | M12 (2,476) |
|---|---|---|---|
| "you" (the word alone) | 35 = 16.1 | 42 = 15.1 | 78 = 31.5 |
| "you" family (you, you're/'ll/'ve/'d, your, yours, yourself) | 104 = 48.0 | 124 = 44.7 | 122 = 49.3 |
| "but" | 12 = 5.5 | 3 = 1.1 | 17 = 6.9 |
| "I" (I, I'm, I'd, I've, I'll) | 9 = 4.2 | 4 = 1.4 | 73 = 29.5 |
| questions ("?") | 8 = 3.7 | 0 = 0.0 | 0 = 0.0 (auto-captions have no punctuation: by ear about 3, such as "do you see how strong that line looks") |

New script, items that name a feeling: 3 of 5 clearly, plus a light one in a fourth. Item one: "It's discouraging to walk out of the salon with a bob you love and watch it go wrong by the first wash at home." Item two: "Moving it feels strange at first, but a deep side part, or one just off center, gives the hair on the fuller side somewhere to rise." Item four: "When the jawline softens after 60, it's natural to want your hair to cover it. I understand that instinct." Item five, the light one: "Dark color can feel like the safe choice". Item three has none. This is above the pack's "about one in four", but each is one plain sentence placed before the fix, so it doesn't feel heavy, and it fits a hair title. Questions: 8, the top of the pack's 4 to 8. "But": 5.5 per 1,000, in all 5 items (the pack asks for about five or more). "I": 4.2 per 1,000 against the guide's about 10, reported only and never a fail. Every "I" is an opinion or the approved detail.

Title words (each at least twice, once in the first minute): "styling" 3, "wrong" 2, "60" 2, "secrets" 8, "turn(s) heads" 2, "instant(ly)" 3 (first at about 37 seconds). The count is paid: five secrets, each signposted. Our old script said "wrong" once, never said "instant", and only said "turns heads" in its tease and its last item.

## 3. The hook, side by side

**The model: M08** (Justin Hickox, "You're Styling Your THIN/FINE Hair WRONG! Do THIS Instead- 5 SECRETS", `hooks.md`, styling it wrong, Usable: Yes). It is 175 words as kept, with item one at 1:13 (52 seconds once the omitted parts are taken out). Its moves:
1. count line with the promise word ("five hacks, or it's all wrong"), 18 words
2. the feared look named three times (flat, greasy, stiff: each looks thinner), 74 words
3. reassurance with the count line (five hacks, any length), 34 words
4. the promise word again (less damage too), 49 words
5. item one

(M12, the winner, has the same first three moves: 15, 83 and 38 words, 136 in all. After them come about 580 words of product prep on a model before item one at 3:25. `hooks.md` marks it "In part, moves 1 to 3". Picking M08 gave the writer the same format without the demo.)

**The new hook, in full** (104 words, item one at word 104, about 37 seconds at 169 words a minute):

> If your bob never looks right at home, you may be styling it wrong after 60. Five small secrets decide whether it turns heads or drags your face down.
>
> A flat crown with all the width at the ends makes a triangle that pulls everything lower. Ends curled under and sprayed stiff turn into a helmet. And dull, flat color makes even a good cut look tired.
>
> None of this needs a new haircut. These five fixes work on the bob you already have, fine or thick. And most of them take a few minutes at your own mirror, so the change shows instantly.

| M08's move | The new hook's move | Words |
|---|---|---|
| 1. count line with the promise word | 1. the feeling plus the promise word ("If your bob never looks right at home, you may be styling it wrong after 60."), then the count line with the promise word ("Five small secrets decide whether it turns heads or drags your face down.") | 16 + 13 |
| 2. the feared look, three times | 2. the feared look, three times: the triangle, the helmet, dull color | 38 |
| 3. reassurance with the count line | 3. reassurance with the count line ("None of this needs a new haircut. These five fixes work on the bob you already have, fine or thick.") | 20 |
| 4. the promise word again | 4. the promise word again ("so the change shows instantly") | 17 |
| 5. item one | item one, at about 37 seconds | |

Judgement: the moves are carried in order and nothing is added. There is one well-judged change. M08 opens with a conditional ("if you don't know these five hacks"); the new hook opens on the hair feeling the pack names ("the cut that never looks right"), then gives the count. That is `SKILL.md` "The opening" rule 5 overriding a literal copy, and it is the right call. The audit's move list should have said so. The hook stays under the model and under 110 words, with one idea a sentence. There is no scene, no "Picture", no intro, no age slogan (the age is the title's), no tease, task or recap. The three feared looks name the problems of three of the five items, but that is M08's own move, not a recap. What holds it at 8 and not 10:
- "you may be styling it wrong" hedges the title's WRONG. M08 and M12 say "probably ... totally wrong".
- "pulls everything lower" is vague right after "drags your face down", which already said it better.
- "instantly" waits until the last sentence. "Turns heads" lands in sentence two, which is fine.
- At 104 words it sits above the winners' median of about 80. The feared-look move could lose about 10 words.

Our old script's hook, for contrast, ran about 370 words to item one at about 2:30. It opened on an object scene ("There's a round brush in your bathroom drawer that may be quietly adding years to a perfectly good bob"), then "I'm Scarlet Sterling and this channel is for women over 60", then a tease ("And the last secret takes 2 seconds and costs nothing"), a recap of what was coming, and "so many of us".

## 4. Failures

### Writer slips (the rule was there and wasn't followed)

1. **A backwards instruction.** "The side opposite your part, the one with less hair, is usually the right one." With a side part, the side with less hair is the side the part is on, not the side opposite it. A viewer who follows the first half tucks the full side. Rule: the rubric's "Clarity on one listen" and `SKILL.md` "The item shape" step 4 ("The swap, specific"). Our old script had this right ("Choose the smaller side of your part, the side with less hair"). Fix: "Tuck the smaller side, the side of your part with less hair."
2. **Heat safety said three times.** Item one: "Spray on a heat protectant, and turn the dryer to a lower setting if your hair is fine or color-treated." Item three: "The flat iron sits right on the hair, so the heat protectant matters even more here, and fine or color-treated hair wants the lower setting." The close: "Fine hair wants less product and the lower heat setting." Rule: `SKILL.md` "Safety" ("one short line inside the item, in proportion, never a lecture") and "Length" ("Never pad. Cut repetition"). Fix: keep item one's line, cut item three's line to "Use the heat protectant here too.", and cut "and the lower heat setting" from the close.
3. **Item one runs 456 words before the CTA** (545 with it). Rule: `SKILL.md` "The item shape" ("About 180 to 300 words an item, longer when an item carries the video"). Item one does carry the video, and the audit says so, but it holds two methods, two "I" lines and a long check. Fix: cut about 80 words. "Root lift means a product that helps the hair stand up from the scalp instead of lying flat." can shrink to a clause, and either "I like the rollers best..." or "I'd always choose..." can go.
4. **Two muddy lines.** "it looks set rather than grown" ("grown" doesn't say anything on one listen). Fix: "it looks set in place, not like hair that moves." And "I like the rollers best on the days you want the height to last." (the logic of "I" and "you" is crossed). Fix: "On the days you want the height to last, I'd choose the rollers." Rule: the rubric's "Clarity on one listen" and `SKILL.md` "Voice" ("Plain over clever").
5. **Two delivery tags in a row in the VO copy:** "[warm] I'd always choose height at the top and calm at the bottom." then, on the next sentence, "[short pause] When the height moves up, the whole face looks lifted and rested." Rule: `core/workflow.md` §6 ("Never two in a row"). Fix: drop the [warm]. Otherwise the VO copy is clean. Stripped of tags it matches the script word for word, and it has 22 tags in 2,164 words (about one per 98), with no marker line tagged.
6. **The mid-CTA names the chapter but not the Way.** "it has a whole chapter on hair, called The Hair Hack". This is true, and the pack allows the chapter. But the book match has an exact Way for item one: Way 205, "Invest in the Blow-Dry Routine, Not Just the Cut" (`personas/books/scarlett-starling-book.md`). Rubric: "a true fact from the profile and the book match's Way or Secret". Fix: tie the aside to Way 205 by its title. The end reminder could then say something other than the chapter name again ("there's a whole chapter called The Hair Hack in my book").
7. **Audit, small overclaims.** The Originality line says "1 brief swaps most bob videos skip = 'Roll two or three Velcro rollers into the crown...'", but nothing supports "most bob videos skip" it. The swap comes straight from the brief, and our own old script used a Velcro roller at the crown. The Hook line lists M08's moves as if carried exactly, without saying the new hook opens on the feeling before the count line. Rule: `core/greenlight-audit.md`, where the evidence must match the script. Neither changes the verdict.

Not failures (checked): "Somewhere along the way, someone taught you that a finished bob curls under and stays put." This uses the once-allowed phrase, once. It does echo the shape of the pack's villain example ("somewhere along the way, someone told her short was sensible"), but the scanner's example guard skips quotes that start lower-case (see library fix 4). "nobody showed you that step" blames no one, so the salon is not cast as the villain. The three "staccato" pairs ("Secret number two." / "Move your part.") are a signpost followed by its instruction, so keep them. "Once a week is enough." follows the brief ("about once a week").

### Library fixes (a rule is missing, unclear or wrong)

1. **The book's spoken title trips the copy guard** (fact 1). `personas/scarlett-starling.md` requires "Three Hundred Budget-Friendly Ways to Look Expensive" in the CTA, and the copy guard runs against the profile, so every Scarlett script gets one fix-on-sight that the writer can't fix. Fix: add `allow: Three Hundred Budget-Friendly Ways to Look Expensive` to the profile's scanner block, or have the scanner exempt the profile's own `book:` line automatically, so Diane and every booked channel are covered. Do the same for Diane's profile.
2. **`verify_output.py` treats a quoted model line as a script quote** (fact 2). The Hook evidence line asks for the model's moves, and a writer who quotes the model ("graded against M04 ('Fine hair doesn't have to age you...')") gets a false discrepancy. Fix: skip quotes on the Hook line that follow a model file number (M or F plus digits), or make `greenlight-audit.md` ask for model lines in a marked form (for example `M04: <...>`) that the tool ignores.
3. **The voice provider isn't named.** The profile says "Voice provider: as the channel's voiceovers now (... provider not named)". `core/workflow.md` §6 only says what to do for ElevenLabs v4 or Minimax, so the writer had to guess: "The VO copy is included because the profile doesn't name the voice provider." Fix: name the provider in the profile, or add a §6 default for an unnamed provider (for example, include the VO copy).
4. **The example guard skips lower-case quotes.** `core/script-scanner.py` `example_runs` keeps only quotes that start with a capital and end on . ? or !. The pack's in-sentence examples, such as the villain line ("somewhere along the way, someone told her short was sensible"), are never guarded. Here the echo was mild and the phrase is allowed once, but the gap is real. Fix: keep lower-case quotes of 6 or more words when they sit in an "Allowed:" or example bullet, or restate those examples as capitalised sentences.
5. **The item-word band counts CTA and ending words.** The scanner's item one (545) includes the 89-word mid-CTA. Its item five (473) includes the 83-word closing and the 46-word end CTA, and item five's own content is only 344 words. The "<<" flags overstate the problem. Fix: in `core/script-scanner.py`, exclude the CTA blocks from item counts, and end the last item where the end CTA begins, or report the content words separately.
6. **"You" per 1,000 words is ambiguous.** `SKILL.md` "Voice" says "you about 45 per 1,000 words". The word "you" alone runs at 16 here (M12 at 31). The "you" family (you, your, you're...) runs at 48 (M12 at 49). Fix: say which is counted (the family, judging by the numbers), and have the scanner report it.
7. **The gate's "exact name" rule** (`core/workflow.md` §1.1): say whether a first name that matches exactly one channel, or the exact name inside a pasted CHANNEL: line, counts as the channel. The chat got it right here, but the rule as written would send "it's for Scarlett" back to the list.
8. A note for the brief writer, not the script: the brief says "color one to two shades lighter than the pre-gray natural shade", and the book's Way 201 is "Choose a Color One Shade From Your Natural, Not Two". No CTA cites Way 201, so nothing clashes here. But a future CTA that points at Way 201 on a color title would contradict the script.

## 5. What the new script does better

**Than our old script (h9MsF44shdQ):**
- It gets to item one in 104 words with no intro or tease. The old script took about 370 words, with "I'm Scarlet Sterling and this channel is for women over 60" and "Still ahead are the tool that gives a bob real movement, and the 2-second finish that turns heads at the very end."
- It names the feeling plainly: "It's discouraging to walk out of the salon with a bob you love and watch it go wrong by the first wash at home." The old script used imagined strangers and scenes: "Picture the line at the dry cleaners on a Tuesday", "Think of a gallery afternoon in a charcoal sweater", "Imagine yourself at a wedding reception in a powder blue dress."
- It asks her 8 questions, and every item has a check she can run: "Stand at the mirror and shake your head gently. The hair should swing and fall back into place." The old script asked none.
- It gives permission in plain words: "Do you love a little curve at the ends? Keep it. A soft bend is lovely. The only thing to give up is the hard, set roll." The old script's version was "it has earned its retirement".
- It names the stylist pain without blame: "If you've ever left the chair with something you didn't ask for, a clear sentence and a phone photo of the shape you want make you much easier to hear."
- It leans to the over-70 viewer: "If holding a brush over your head tires your arms, there's an easier way."
- It covers safety the old script missed: "That's a styling effect and nothing more. It does nothing to the hair itself, and if your hair is suddenly shedding or thinning in patches, that's something to show your doctor or dermatologist." It also adds the patch test for home color.
- Its CTA and ending are clean: one 89-word CTA with a return line ("Now, about that part."), then "Leave me a comment and tell me your age and where you're watching from." The old script pitched the book twice, walked through the QR code, said "whichever suits you is perfectly fine", asked her to subscribe and "which of these five secrets you'll try first", and signed off with "stay polished and stay sterling".

**Than the winner (M12):**
- It works by ear: every step is named in words, with nothing pointed at ("this section right here", "see how that started to turn purple").
- It explains every "why" in one plain line: "A center part also cuts the face into two equal halves, and that perfect symmetry can look severe on a softer face." and "wherever the hair points, the eye follows, and the cheekbones are the most lifted part of the face."
- No sponsor, no product demo before item one, and no "Prime day 2024 you can save up to 30%".
- It takes the same objection M12 answers ("show me on somebody with thin fine hair or ... thick hair") and answers it in her terms: "You might be wondering whether these five secrets work on very fine hair or very thick hair. They do, with small changes."

**Where the references still win:** M12's hook says WRONG with full conviction ("you're probably styling your Bob totally wrong"), and it has a secret the new script lacks: dry the nape flat so the back doesn't bulk out ("keep the nape tight"). The brief didn't give it, so this is not a slip. Our old script had better technique detail ("Hair holds the shape it cools in", the nozzle aiming the air down the hair, the ends pointing "down or away from your face, and never under toward your neck"), and it got the tuck side right.

## 6. The top five changes, ranked

1. **Fix the tuck instruction:** "Tuck the smaller side, the side of your part with less hair." It is the one line that sends her the wrong way.
2. **Cut the repeats and trim item one:** keep the heat line once (item one), shorten item three's to "Use the heat protectant here too.", cut "and the lower heat setting" from the close, and take about 80 words out of item one.
3. **Sharpen the hook to about 90 words:** "you're probably styling it wrong after 60" in place of "you may be"; cut "that pulls everything lower" to "that drags your face down" and drop the echo from sentence two; let "instantly" come earlier ("Five small secrets turn heads instantly, or drag your face down.").
4. **Point the mid-CTA at Way 205** ("Invest in the Blow-Dry Routine, Not Just the Cut") to tie it to item one, and word the end reminder without repeating the chapter name.
5. **Clean the two muddy lines and the VO tags:** "it looks set in place, not like hair that moves"; "On the days you want the height to last, I'd choose the rollers."; drop one of the two adjacent tags. While there, give items two and three one more opinion "I" line each (now 4.2 per 1,000 against the guide's about 10, reported only).
