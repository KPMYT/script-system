# TEST (iter-08): judge report, run 03

Diane de Chambray, "Why French Women Over 60 NEVER Look Frumpy — It's Not Their Weight, It's These 5 Rules". This is a rerun of iter-07 run 03 on the same brief and the same VA turns, after the fixes in `iter-07/CHANGES.md`.

**Judged against:** `iter-08/judge-rubric.md`, `style-scripts/SKILL.md`, `style-scripts/references/hooks.md`, `personas/diane-de-chambray.md` (with "THE FRENCH WAY"), `personas/books/diane-de-chambray-book.md`, the core files the rubric names, `brief-03.txt`, `refs/ISAL4NBlshQ-ours-transcript.txt` (our old script, 3,826 views), `refs/ixlexruRC6c-M21-transcript.txt` (Marie-Anne Lecoeur, 1.04M), and `iter-07/test-run-03/script.txt` and `judge-report.md` (116/140).

**The main session's facts, taken as facts:**
- The scanner found 0 fix-on-sight.
- 2,204 spoken words, about 12.8 minutes at 172 words a minute.
- Five items of 459, 357, 433, 340 and 393 words. Item one starts at word 79, about 28 seconds in.
- Title words: "weight" 2, "frump" 3.
- `verify_output.py` reported one discrepancy, "NEVER Look Frumpy", which is a false hit (§4, library fix L3).

**The three "numbers not found", checked:**
- **101 traces to the profile.** Its True facts say "one hundred and one numbered Secrets", confirmed in the book index ("101 Secrets, numbered 1 to 101").
- **"All six" traces to the brief,** which lists six neutrals: navy, black, gray, camel, cream and white.
- **"Six weeks later" is general knowledge.** The pack's D4 override names "cuts about every six to eight weeks" as an allowed general-knowledge number.

The output's explanation holds on all three. Why 101 was still flagged is in §4 (library fix L4).

## 1. Verdict

**Yes, I'd upload it after one short fix pass.** It is clearly better than iter-07's run and far better than our old script. On our rubric it also beats the winner.

**"Practical solutions to emotional problems"** is still the script's strength, and it is stronger than in iter-07:
- **The over-70 lean is concrete:** "And if buttons have started giving your fingers trouble, choose a pull-on trouser that fits well at the waist, and let the tailor take care of the hem."; "If you're less steady than you used to be, choose a shoe with a back and a sole that grips, and keep any heel low and wide."
- **Permission is plain:** "If you don't like tucking, don't."; "And repeating the same outfit twice in one week is fine."; "That's normal, but nobody's asking you to decide today."
- **The brief's attitude is back, in English:** "being comfortable in your own skin, at your own age".

**The hook** carries M28 move for move: credential, contrast, cause, count. It runs 78 words (M28 also runs 78), with item one at about 28 seconds and no scene, intro, tease or task. "frumpy" and "weight" both come in sentence two. It is short and clear. It aims at pride and permission, like its model, rather than at her fear. That was the operator's choice ("we model off winning hooks for now still"), so I judge it against M28, and it passes.

**What keeps it from a straight upload:**
- **"frumpy", the title's feeling, disappears.** It comes twice in the hook and then not again until word 2,124 of 2,208, about eleven minutes later.
- **The hook's cause line promises "fabric",** and the script never teaches it. Iter-07's script did, with its fabric check.
- **Rule three repeats rule one's empathy beat:** "feels like the safe choice. I understand that completely." / "I understand why it feels safe when your middle is fuller."
- **Two lines borrow wording.** "None of these five rules asks you to lose weight" is the pack's own example almost word for word. "Fit doesn't mean tight" is M21's "fitted does not mean tight", for the second run in a row.

All of these are small edits. None needs a new draft.

## 2. Scores (1-10)

**Method:** The references keep the scores the iter-07 judge gave them: same transcripts, same rubric categories. I re-checked their counts below. They have no audit block, so their totals are out of 130 and scaled to 140.

| Category | New | Ours (ISAL4NBlshQ) | Winner (M21) | Why, in one line |
|---|---|---|---|---|
| The hook (x2) | 8 (16) | 3 (6) | 8 (16) | **New:** M28's four moves in order, 78 words (level with the model), item one at about 28 s, title words in sentence two. But the cause list ("fit, proportion, fabric and finish") doesn't match the five rules, and "with American clothes" is an odd close. **Ours:** opens on a "Lay the outfit on the bed" scene, has a name intro and two teases, item one after about 180 words. **M21:** 29 words; a question, the count with the feared look, the promise; item one at 0:13. |
| Keeping the title's promise | 8 | 8 | 8 | **New:** five rules delivered. "Weight" twice, paid as plain permission ("None of these five rules asks you to lose weight, and this first one shows why."). "NEVER" paid by its hedged meaning ("you'll rarely see"). But "frumpy" never comes back in the body, and the hook's "fabric" is never paid. **Ours:** "Frumpy was never a weight, and it was never a birthday." **M21:** seven things, each with what to wear instead. |
| Clarity on one listen | 9 | 6 | 7 | **New:** mean sentence 14.4 words, longest 30. Gloss, front tuck, column, accent and Breton are all explained. "Proportion" and "finish" are not, and the hook's cause list doesn't map onto the rules. **Ours:** poster lines ("1/3 over 2/3"). **M21:** simple, with caption slips. |
| Emotion | 8 | 5 | 6 | **New:** "but" 5.0 per 1,000, 6 questions. A feeling is named in 4 of 5 items, and two of those are the same "safe" beat. The blame moves off her once, in fresh words; permission is strong; the attitude is restored. But "frumpy" is absent from all of rules one to four. **Ours:** "but" 1.0, imagined strangers. **M21:** warm tough love, but "old lady" over and over. |
| Voice and persona | 9 | 3 | 8 | **New:** heritage line once, behind a practice; one approved detail ("My own habit is one in, one out."); "I" only for opinion; no name, no house vocabulary, no French words. One unhedged French line: "The French habit is one statement at a time." **Ours:** "I'm Diane", "the women I know" twice, "small gold hoops". **M21:** authentic. |
| Claims and proof | 10 | 4 | 7 | **New:** no try-on, client, brand or health claim. The tailor's rule is credited generally ("A good tailor starts every jacket at the shoulder seam"). French claims come from the brief. **Ours:** "389 pages", the circle claim. **M21:** unhedged "This is youthful." |
| Money | 10 | 3 | 10 | **New:** no price. The brief's $15-$25 and $300/$1 a wear stay background. "Expensive" comes from fit and one statement at a time. **Ours:** "$15 to $25", "50 to 90 dollars". **M21:** none. |
| Safety | 10 | 6 | 6 | **New:** "Feet change, and so does balance. If you're less steady than you used to be, choose a shoe with a back and a sole that grips, and keep any heel low and wide." No diet: "None of these five rules asks you to lose weight". No home dye or heat advice is given, so neither line is needed. **Ours:** no footing line. **M21:** "Comfort is non-negotiable", no footing line. |
| Written for the voice | 10 | 5 | 7 | **New:** no symbols or brackets; "one hundred and one" in words; no French words; voice tags only in the VO copy. **Ours:** "À bientôt" with accents, "1/3 over 2/3". **M21:** spoken. |
| CTA and ending | 9 | 2 | 3 | **New:** the book once at word 539 of 2,204 (24%), all six parts, true facts, spoken title, the right chapter. Then the one-line reminder and the comment ask about her, last. The mid CTA is 91 words, a hair over 90, and its benefit line is nearly iter-07's word for word (§4, L5). **Ours:** pitched twice, a no-rush close, subscribe, "À bientôt". **M21:** no offer. |
| Length and pacing | 9 | 6 | 6 | **New:** 2,204 words, 12.8 min. Items 340-459, inside 300-450 except item one at 459, which carries the video. About 40 words of echo. **Ours:** about 12.1 min, padded with scenes and a recap test. **M21:** 923 words. |
| Originality vs the models | 7 | 6 | 9 | **New:** copy guard clean. Differs from M28 in at least four ways: five rules against ten purchases, items of 340-459 words against short ones, a check in each, practices not purchases. But it echoes M21's fitted/tight line and reuses the pack's example line. **Ours:** original, in the house formula. **M21:** its own. |
| Audit honesty | 9 | n/a | n/a | 36 of 37 quoted lines are in the script; the 37th is the title label. Hook line correct (M28's moves, 78 words, about 28 s). Title-word line complete and honest. Two small errors (§4). |
| **Total** | **124 / 140** | **60 / 130 (65 / 140 scaled)** | **93 / 130 (100 / 140 scaled)** | |

**Against iter-07 run 03 (116/140):** +8. Hook 7 to 8, promise 7 to 8, clarity 8 to 9, voice 8 to 9, claims 9 to 10, safety 9 to 10, length 8 to 9, audit 8 to 9; originality 8 to 7.

### My counts

**Method:** `python3 -I`; `script.txt` without the two CTA marker lines; the references without their header line and timestamps.

| | New (iter-08) | iter-07 run 03 | Ours | M21 |
|---|---|---|---|---|
| Words | 2,204 | 2,260 | 2,087 | 923 |
| "you" + "your" (with "yours"), per 1,000 | **42.2** (44 + 49) | 46.5 (37 + 68) | 27.8 (28 + 30) | 56.3 (30 + 22) |
| "you" family (you're, you'll, you'd, you've, yourself), per 1,000 | 47.6 (105) | 50.4 (114) | 32.1 (67) | 56.3 (52) |
| "but", per 1,000 | **5.0** (11) | 5.8 (13) | 1.0 (2) | 9.8 (9) |
| "I" (with I'd, I'm, I'll), per 1,000 | **6.4** (14) | 6.2 (14) | 6.7 (14) | 18.4 (17) |
| Questions, per 1,000 | **2.7** (6) | 2.7 (6) | 1.0 (2) | 13.0 (12) |

**Against the pack's guides:**
- **"you" and "your" (about 45):** 42.2. Met.
- **"but" (five or more per 1,000):** 5.0, exactly at the floor. All 11 are real turns. Down from 5.8.
- **Questions (four to eight a script):** 6, met. Five are in the body and one is the comment ask:
  - "Where does the shoulder seam sit?"
  - "So what do French women do about it?"
  - "So what about the woman who loves color?"
  - "How many of your tops would pass?"
  - "So what do you say in the stylist's chair?"
  - "What's the oldest piece in your closet that you still wear, and how many years have you had it?"

  Three of the five body questions open "So what…" (§4, W7).
- **"I" (about 10, reported):** 6.4. All 14 are opinion or address, none is experience: "I'd spend on the tailor long before I'd spend on a bigger size."; "I'd start with whichever one you already own."; "I love gray with a sharp cut and some shine, but it needs both, or it can look flat."

**Items naming a feeling: 4 of 5.**
- Rule one: "going up a size feels like the safe choice. I understand that completely."
- Rule three: "I understand why it feels safe when your middle is fuller. It covers the part you'd rather not think about."
- Rule four: "a steady flat looks better than any heel you're nervous in."
- Rule five: "the thought of stopping can feel like a much bigger step than it sounds."

Rule two names none. That is above the pack's "about one in four". With items twice the usual length it is not a fail, but rules one and three carry the same feeling (W2).

**Title words (my count):** French 14, women 9, 60 1, look 24, rule 15, **frump 3** (words 29, 39 and 2,124 of 2,208), **weight 2** (words 38 and 478), never 0 (paid as "rarely"; the profile forbids "French women never").

## 3. The hook, side by side

**The model: M28** (Alice in Paris, "10 Things French Women Never Buy", `hooks.md`, Usable: Yes, for Diane only). **78 words, item one at 0:27.**

| M28's move | Words |
|---|---|
| 1. Credential: the lens, she is French | 4 |
| 2. Contrast: what the French don't buy, and why not | 27 |
| 3. Cause: buying with intent | 21 |
| 4. Count line: 10 things, plus "might completely change the way you think about shopping" | 26 |
| Item one | at 0:27 |

The feeling it aims at, per `hooks.md`: "Permission and pride ... no fear named."

**The new hook, in full. 78 words by the scanner (79 if "60" is counted), item one at word 79, about 28 seconds:**

> The way I was raised in Paris, a woman fixed the fit long before she worried about the size.
>
> So you'll rarely see a French woman over 60 look frumpy, and it has nothing to do with her weight.
>
> Frumpy comes from fit, proportion, fabric and finish, and every one of those can be fixed at any size, from your own closet.
>
> Here are the five rules they dress by, and how to borrow each one with American clothes.

| M28's move | The new hook's move | Words |
|---|---|---|
| credential | credential behind a practice: "The way I was raised in Paris, a woman fixed the fit long before she worried about the size." | 19 |
| contrast | contrast, the title's turn: "So you'll rarely see a French woman over 60 look frumpy, and it has nothing to do with her weight." | 20 |
| cause | cause, with a scope clause: "Frumpy comes from fit, proportion, fabric and finish, and every one of those can be fixed at any size, from your own closet." | 23 |
| count line, with a payoff tail | count line, with a payoff tail: "Here are the five rules they dress by, and how to borrow each one with American clothes." | 17 |
| item one at 0:27 | item one at about 0:28 ("Rule number one. Fit comes before size.") | |

**What passes:**
- **The right model for the type.** It is the rules she never breaks, and M28 is the only real Yes hook for Diane in that type.
- **Faithful to the model.** The same four moves in the same order, nothing added, and no longer than the model by the same counter.
- **Fast and clean.** Item one comes well inside 45 seconds. No intro, age slogan, tease, task, recap, "Picture" or second promise.
- **Clear and on-title.** One idea a sentence. Both title words ("frumpy", "weight") and the age come in sentence two, and "NEVER" is paid in its hedged form ("rarely").
- **The heritage line does a job,** as the profile asks: it sits behind a documented practice (tailoring).
- **Closer to her than iter-07.** "you" now comes in sentence two and "your own closet" in sentence three. In iter-07, "you" first came in the last six words.

**What falls short:**
1. **The cause promises one thing and the video teaches another.** The cause lists "fit, proportion, fabric and finish". The rules are fit, color, line, shoes and accessories, and hair and face. "Fabric" is never taught: iter-07 had a fabric check, this script dropped it. Color, the subject of a whole rule, isn't in the list. The cause is the curiosity move, so the video should answer exactly what it names.
2. **"with American clothes" is an odd close.** It sounds as if American clothes were the problem. The profile's wording is "an American closet". "From your own closet" is already said one sentence earlier, so the tail can simply go.
3. **The opening pre-spends rule one.** "a woman fixed the fit long before she worried about the size" comes back seconds later as "Fit comes before size." This is acceptable, since the heritage line must sit behind a practice, but it is the same point twice in 30 seconds.
4. **The feeling is pride, about French women.** That is faithful to M28 and the operator's choice, so it costs nothing here. I only note that "it has nothing to do with her weight" is the one place the hook comes near her worry, and it is in the third person.

**A tightened version with the same moves (69 words):**

> The way I was raised in Paris, a woman fixed the fit long before she worried about the size. So you'll rarely see a French woman over 60 look frumpy, and it has nothing to do with her weight. Frumpy comes from fit, color, line and the finishing touches, and every one can be fixed at any size, from your own closet. Here are the five rules they dress by.

## 4. Failures

### Writer slips (the rule was there)

**W1. The title's feeling never comes back in the body.**
- **The problem:** "frumpy" is said at words 29 and 39 (the hook), then not until "I'd say that's the real reason frumpy so rarely gets a foothold." at word 2,124. Rules one to four carry it only as synonyms ("the outfit looks tired", "looking wider and shorter than you are").
- **Breaks:** `SKILL.md` "Emotion" rule 8 ("Say the title's feeling again every few items, in the title's own words ... a natural return now and then").
- **A regression:** iter-07 said it 5 times.
- **Fix:** one natural return in rule one or three, and one more in rule two or four, on the garment. For example, at rule three's mechanism: "That one wide block is the shape most people mean when they say frumpy."

**W2. The same empathy beat twice, and an echo.**
- **The lines:** Rule one: "If your body has changed and nothing in the store seems cut for it, going up a size feels like the safe choice. I understand that completely." Rule three: "It's comfortable, and I understand why it feels safe when your middle is fuller." The phrase "If your middle is fuller" (rule one) / "when your middle is fuller" (rule three) comes back too.
- **Breaks:** core `humanizer.md` H18 (the second mention must add something) and `SKILL.md` "Length" ("Cut repetition").
- **Repeated from iter-07:** this is iter-07 slip 8 ("I understand the instinct." / "I get the appeal.").
- **Fix:** keep rule one's beat. In rule three, cut "and I understand why it feels safe when your middle is fuller" and keep "It covers the part you'd rather not think about."

**W3. The hook's cause names "fabric", and no rule teaches it.**
- **The line:** "Frumpy comes from fit, proportion, fabric and finish". "Fabric" appears once more, in rule one, only as "the extra fabric doesn't hide anything".
- **Breaks:** core `greenlight-audit.md` C5 (the payoff delivered exactly as promised) and `SKILL.md` "The opening" step 4 (clear and to the point).
- **Fix:** either name what the rules teach (the §3 version), or put back a fabric line in rule two's "fewer, better pieces". Iter-07 had one: the fabric scrunch in the hand, as general knowledge.

**W4. The pack's own example line, reused.**
- **The line:** "None of these five rules asks you to lose weight, and this first one shows why." The pack's line, in `SKILL.md` "Emotion" rule 8, reads "none of these rules asks you to lose weight": six words in a row are identical.
- **Breaks:** `SKILL.md` "Files in this skill" ("the example lines here show a shape; the script never reuses their wording").
- **Why the scanner missed it:** the example guard skips lowercase quotes (L1).
- **Fix:** say it fresh. For example, "Nothing in these five rules involves a scale."
- **Note:** the pack all but prescribes this wording, so the main fix is library fix L1.

**W5. A model echo, second run running.**
- **The line:** "Fit doesn't mean tight". M21 says "fitted does not mean tight" (0:58-1:02), after the same item (baggy, sized-up clothes). Iter-07 had the same echo ("You don't have to wear anything tight. Fitted means...").
- **Breaks:** `SKILL.md` "Using the models" (borrow structure, never wording). The idea is common, but this is M21's sentence with one word changed.
- **Fix:** say the idea through the check instead: "The right fit skims past a fuller middle and falls straight; it doesn't cling, and it doesn't balloon." That line is already in the script, so the first sentence can simply go.

**W6. One unhedged French claim, and a closing line that undercuts the hook.**
- **The unhedged claim:** "The French habit is one statement at a time." Every French claim needs a hedge (profile, THE FRENCH WAY rule 1). One statement at a time is documented ground, but it is stated as a national rule. Fix: "Plenty of French women keep to one statement at a time."
- **The closing line:** "Behind all five rules sits an attitude the French have a phrase for, being comfortable in your own skin, at your own age. I'd say that's the real reason frumpy so rarely gets a foothold." The hook says frumpy comes from fit and the rest; now "the real reason" is an attitude. That undercuts the practical promise and leans toward the Wise Narrator (`SKILL.md` "Voice"). Fix: keep the attitude as permission and drop "the real reason". For example: "It's the habit that holds the five rules together, and it costs nothing."

**W7. The turn question repeats its form.**
- **The lines:** "So what do French women do about it?" / "So what about the woman who loves color?" / "So what do you say in the stylist's chair?"
- **Breaks:** `SKILL.md` "The item shape" (the turn, rotated) and `humanizer.md` (repeated structure).
- **Fix:** turn one of them with a plain "but" or "here's what works instead", which would also lift "but" off the 5.0 floor.

**W8. The item endings still lean on one pattern.**
- **Better than iter-07,** which had check, result and bridge five times. Endings now vary:
  - rule one on a compliment: "It's the same jacket, with the sleeves taken up."
  - rule two on a question: "How many of your tops would pass?"
  - rule five on the result: "looking rested, and looking like yourself."
- **But** rules three and four both close check, then result or verdict, then a bridge, and both bridges use the same "two ends of the line" device: "We'll start at the feet." / "From the feet, we go up to the other end of the line."
- **Breaks:** `SKILL.md` "The item shape", vary the item endings.
- **Fix:** let rule four end on its verdict ("the one that makes an outfit look calm and expensive") and go straight into "Rule number five." The first bridge already set up the face.

**W9. Two terms not explained, unchanged since iter-07.**
- **The terms:** "proportion" (hook) and "finish" (hook).
- **Breaks:** `SKILL.md` "The viewer" ("proportion" is on its list).
- **Fix:** the §3 version drops both.

**W10. The audit's small errors.**
- **The rotation log's "bridges" field** says "the open question into the CTA". No question comes before the CTA; the line is "But fit can only do so much when the colors in your closet won't go together."
- **The Hook line's "pain or wish"** quotes the cause sentence, not a pain. This is the same weakness as iter-07, and the operator didn't take that fix (L6).
- **Breaks:** core `greenlight-audit.md` (the evidence matches the script).

### Library fixes (a rule is missing, unclear or wrong)

**L1. The pack prescribes wording its own guard can't see.**
- **The problem:** `SKILL.md` "Emotion" rule 8 gives the pay line for "It's Not Their Weight" as a quote: "none of these rules asks you to lose weight". `core/script-scanner.py` `example_runs()` keeps only quotes that start with a capital and end on `.?!`, so this lowercase clause is never guarded. The writer used it almost word for word, and every future "not their weight" title will say the same sentence.
- **Fix:** write the instruction as a shape ("a plain permission line that the rules involve no weight loss, in fresh words"). Or let the example guard read lowercase quoted clauses of five or more words inside rule lines.
- **Also run 01's problem.** Iter-07 L4 introduced this example.

**L2. A title word's "twice" can be spent entirely in the hook.**
- **The problem:** `title-words` checks "at least twice, once in the first minute". "frump" passed at words 29 and 39 and then vanished for eleven minutes. Rule 8 asks for a return "every few items", but the scanner doesn't read it.
- **Fix:** the scanner reports the longest gap, in items, for each title feeling word. The pack says "at least once in the body before the last item". A report line is enough, given the operator's "dont overdo it".

**L3. `verify_output.py` flags the title quoted as a label.**
- **The problem:** "NEVER Look Frumpy" in the Promise map is the title's own words, used as a label.
- **Fix:** skip a quote that is a substring of the locked title, as iter-07 L2 did for quotes attributed to a model.

**L4. The numbers check still flags the book's 101.**
- **The problem:** iter-07 L1 made the numbers check accept "numbers in the profile's `book:` line". Diane's scanner `book:` line is "The French Way", with no count. The count lives in the True facts prose ("one hundred and one numbered Secrets"), so 101 is flagged on every Diane CTA that uses it.
- **Fix:** add a `book-facts: 101` style line to the profile's scanner block, or have the numbers check read the CTA SETUP's True facts.

**L5. The CTA benefit line is turning into a fixed sentence.**
- **The lines:** iter-07: "with your colors picked one time, a few pieces that all go together, and a quick check once a week". Iter-08: "with colors you choose once, a few pieces that all work together, and a short weekly check". Both follow the profile's single added-value promise ("a palette chosen once, a handful of pieces that work together, and a short weekly check"), and the copy guard can't catch a paraphrase. A regular viewer will hear the same pitch every video.
- **Fix:** give the profile three or four benefit angles (the Capsule Rule, the Proportion Equation, the Elegance Audit, the first week's five Secrets), and log the angle used in the rotation log's book field so it rotates.

**L6. Not a fix, a note: the hook's feeling.**
- The operator declined iter-07 L6, and this hook is judged against M28 as asked.
- I note only that `SKILL.md` "The opening" step 5 still says "Name the worry the title implies, in her words, early", while the model in use names none. The two will keep pulling against each other on Diane's M28 titles. One line in step 5 ("where the model names no fear, the title's words carry the feeling; no move is added") would end the tension without adding a move.

## 5. What the new script does better

**Than our old script (ISAL4NBlshQ):**
- **Item one in 78 words,** against our scene, name intro and teases: "Lay the outfit on the bed before you put it on." ... "I'm Diane, and I show women over 60 how French women get dressed" ... "And stay for rule five because it costs nothing".
- **Her own mirror, never a stranger.** Ours: "the next table quietly decides you must have help at home". New: "Stand in front of your mirror in the top you wear most. Where does the shoulder seam sit?"
- **Checks she can actually run:**
  - "Then reach forward as if you're hugging someone, and sit down in it. If it pulls across the back or rides up at the neck, it's too small."
  - "Take a full-length photo on your phone, from the front and from the side, once without the third piece and once with it."
  - "Before you leave the house, count the things trying to get noticed."
- **The blame moved off her, onto the shop's default, in fresh words:** "Nobody tells you that store sizes are cut on one average body. Almost nobody matches it at every point, at any age".
- **A clean, true CTA:** "my book, The French Way, has a whole chapter on fit and proportion. Its one hundred and one numbered Secrets each tell you how to do it, and when to skip it." Ours had "389 pages", a second pitch and a no-rush close.
- **No prices,** no "women I know", no sign-off.
- **Turns with "but"** 11 times against 2.
- **Ours still does one thing better:** it says the weight turn as a picture: "If an outfit can look frumpy with no one in it, your body was never the suspect." The new script's turn is plainer, and ours also kept "frumpy" alive through the body (W1).

**Than the winner (M21):**
- **The why in every rule.** For example: "It falls in one width from your shoulders to your knees. There's no point where the body narrows, so the eye takes the whole thing in as one wide block". M21 mostly asserts ("This is youthful.").
- **An out for the woman who won't follow the rule,** where M21 issues bans ("no Crocs, no stocks"):
  - "So what about the woman who loves color? You keep it. Make your favorite color the accent".
  - "And if you love your color, keep it. But choose a shade a little softer".
- **Footing and hands, the over-70 lean,** which M21 never touches.
- **No hard word.** M21 says "old lady" again and again (10 times in the transcript); the pack allows it once, flagged.
- **M21 does better on punch:** a 29-word hook, one-line verdicts, and "but" at 9.8 per 1,000.

## 6. The top five changes, ranked

1. **Bring "frumpy" back in the body, twice, on the garment** (W1). For example, at rule three's mechanism: "That one wide block is the shape most people mean when they say frumpy." Add the scanner's gap report (L2).
2. **Make the hook's cause match the rules and drop the odd tail** (W3, W9): "Frumpy comes from fit, color, line and the finishing touches, and every one can be fixed at any size, from your own closet. Here are the five rules they dress by." Or keep "fabric" and put the fabric check back in rule two.
3. **Cut the second empathy beat and the echo** (W2): in rule three, drop "and I understand why it feels safe when your middle is fuller". Rotate one "So what…" turn into a "but" (W7).
4. **Say the two borrowed lines fresh** (W4, W5): replace "None of these five rules asks you to lose weight" (the pack's example) and "Fit doesn't mean tight" (M21's line). Rewrite the pack's rule 8 example as a shape, or guard lowercase quoted clauses (L1).
5. **Fix the closing line and the one unhedged French claim** (W6): "I'd say that's the real reason frumpy so rarely gets a foothold." becomes a permission line that doesn't contradict the hook, and "The French habit is one statement at a time." becomes "Plenty of French women keep to one statement at a time."

## 7. The iter-07 fixes, the comparison with iter-07, and the chat

### The iter-07 fixes, one by one

| Fix | Working? | The line |
|---|---|---|
| **L9:** item endings vary; the check given plainly, never announced | **Mostly.** No "Here's the check" (iter-07 had it, and "Here's where to start"). Endings: compliment (rule one), question (rule two), result (rule five). Rules three and four still share check, result, bridge (W8). | "Take any top you own this afternoon, and see whether it goes with three of your bottoms." (plain); "How many of your tops would pass?" (a question ending) |
| **L11:** no spoken pronunciation guide | **Yes** (nothing needed one; no French words at all) | "the striped Breton top" |
| **L7:** "you" and "your" about 45 per 1,000 | **Yes,** 42.2 (93 in 2,204) | "Stand in front of your mirror in the top you wear most." |
| **L10:** "most" only for broad habits; "plenty of", "many" or "you'll often see" for a specific piece; no "women I know in Paris" | **Yes,** one miss | broad: "Most of them see the tailor as a normal part of buying clothes."; "Most French women go the other way. They keep a smaller wardrobe built on neutrals"; specific: "you'll often see French women in ballet flats, loafers or a low heel."; "a silk scarf, which plenty of French women tie on almost every day". No circle claim. The miss: "The French habit is one statement at a time." (W6) |
| **L12:** one short face paragraph, no products, no results | **Yes** | "Many French women keep it close to bare, with groomed brows, a little mascara and a red or berry lip. Skincare comes before makeup, and plenty of them buy it from the pharmacy shelf rather than a department store counter." |
| **L1:** the book's spoken title in the CTA | **Yes,** in both CTAs, and the copy guard no longer flags it. 101 is still flagged by the numbers check (L4). | "my book, The French Way, has a whole chapter on fit and proportion." |
| **L5:** item length by count (300-450 for five or fewer) | **Yes:** 459, 357, 433, 340, 393. Item one is 9 over, and it carries the video (shoulder, hems, the hug-and-sit check, the fuller middle, pull-on trousers). | |
| **L4:** "weight" a title word; "NEVER" paid hedged; "not their weight" as plain permission | **Yes,** but see W4 (the wording is the pack's) and W1 (the "frump" return) | "So you'll rarely see a French woman over 60 look frumpy, and it has nothing to do with her weight."; "None of these five rules asks you to lose weight, and this first one shows why." |
| **The hook stays a winning model's format, applied** | **Yes:** M28's four moves in order, 78 words, about 28 s | §3 |
| **L3:** the channel gate | **Yes** | below |
| **L13:** item counts leave out the CTA blocks | **Yes:** item one's 459 excludes the 91-word CTA | |

### Against iter-07 run 03

**What improved:**
- **The hook speaks to her sooner.** Sentence two now has "you'll rarely see", sentence three "your own closet". In iter-07, "you" first came in the last six words.
- **"weight" is said twice,** and "NEVER" is paid as "rarely".
- **All three French overreaches are fixed:** "In France, most women wear ballet flats" became "you'll often see French women in ballet flats"; "the one piece a great many French women wear" became "plenty of French women tie on almost every day"; "Most French women over 60 skip both habits" is gone.
- **The brief's attitude is back:** "being comfortable in your own skin, at your own age".
- **"gloss" is explained:** "a gloss, which is a sheer treatment that adds shine".
- **"Here's the check" is gone,** and the endings vary more.
- **The over-70 lean is stronger:** the pull-on trouser for buttons, a shoe "with a back and a sole that grips".
- **Permission is plainer:** "If you don't like tucking, don't."
- **The items sit in the new band.**

**What didn't improve:**
- The empathy beat is still doubled (iter-07 slip 8, now W2).
- The M21 fitted/tight echo is still there (iter-07 slip 9, now W5).
- "Proportion" is still unexplained.
- The audit's pain field still quotes the cause.

**What got worse:**
- **"frump"** went from 5 to 3, with none in the body (W1).
- **The fabric content** (iter-07's scrunch check) was dropped, while the hook still promises "fabric" (W3).
- **"but"** fell from 5.8 to 5.0.
- **A new lift from the pack's own example line** (W4).
- **The hook** is 3 words longer (75 to 78), now level with the model rather than under it.

### The chat and the rotation (not scored)

**The channel gate works as fixed.**
- "START" got the numbered list of eleven channels.
- "the French channel" got exactly one line: "Diane de Chambray, right?" That is the L3 form, where iter-07 repeated the whole list without a reason.
- The VA's "Diane de Chambray, the French way one" was taken as a yes ("Got it: Diane de Chambray."), and the chat asked for exactly the three inputs the pack lists, with "none" offered for a new channel's log.

**The input gate:**
- The VA sent the title, the brief and "rotation log: none" in one message, and the run went straight to the output. That was correct: every input was present and valid.
- This run's turn plan tried no mistakes ("all correct at once"), so the missing-title and "just write it" refusals weren't exercised here.

**The rotation:**
- The log was "none", so no model or comment question was barred.
- The output's entry is complete, with the pack's four extra fields: `model: M28, F06 | type: the rules she never breaks | hook: M28 | comment: "What's the oldest piece in your closet that you still wear, and how many years have you had it?"`
- The comment ask is about her, from the pack's "piece kept twenty years" option, and it is the script's last line.
