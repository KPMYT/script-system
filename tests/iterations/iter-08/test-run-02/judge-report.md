# TEST (iter-08): judge report, run 02

Diane de Chambray, "5 French Haircuts That Flatter ANY Face Shape After 60 (And Take 10 Years Off)". A new title. The VA pasted one rotation log line from the channel's earlier script. All material is TEST. Judged on 2026-10-29 against `tests/iterations/iter-08/judge-rubric.md`.

**Inputs read:**
- the run: `test-run-02/output.md`, `script.txt`, `chat.md` and `scanner-main-session.txt` (with `verify_output.py`'s findings)
- the VA's inputs: `brief-02.txt` and `rotation-log-diane.txt`
- the references: `refs/egJ5B6d879c-ours-transcript.txt` (our old video on this title, 2,911 views, 4.8x) and `refs/9LvzTBzXL5k-M07-transcript.txt` (the winner, Glam Girl Gabi, 1.9M)
- the style pack: `style-scripts/SKILL.md`, `style-scripts/references/hooks.md`, `style-scripts/references/models/M07-glam-girl-gabi-best-bangs-face-shape.md` and `F05-french-fashion-10-winter-clothes-french-way.md`
- the persona: `personas/diane-de-chambray.md` and `personas/books/diane-de-chambray-book.md`
- the core: `core/workflow.md` §1-5 and `core/channels.md`

**Facts from the main session, taken as given:**
- The scanner found 0 fix-on-sight problems and 0 numbers missing from the brief.
- 2,178 spoken words, about 12.7 minutes at 172 words a minute.
- Five items of 450, 351, 403, 394 and 368 words. Item one starts at about 29 seconds.
- The title words "ten years" are said 2 times.
- `verify_output.py` found 0 discrepancies.

## 1. Verdict

It meets the operator's bar. I would upload it after a short list of line fixes.

**What works:**
- **The hook** carries M07's opening format in order (contrast, question, cause, scope). It runs 82 words, and item one starts at about 29 seconds. The title's promise word is in the first sentence: "The right haircut after 60 can take ten years off your face, or it can frame the very things you'd rather nobody noticed."
- **Every cut solves a practical problem and explains why.** It gives the exact words to say in the chair: "Ask for collarbone length, long layers from the cheekbone down, and ends left full, not thinned out." The stylist is never the villain.
- **It speaks to the hair-side fear of change**, before the fix, in her own words: "If short hair frightens you, it's probably because of one particular short cut."
- **All three hair safety defaults are present,** each in one line: heat protectant, the doctor line for sudden shedding, and the 48-hour patch test before a gloss.
- **The French claims are hedged** ("plenty of French women wear it with bangs"). The brief's banned "most women I know in Paris" is correctly left out.
- **The ending is right:** the book once mid-video with a true fact, a one-line reminder at the end, then a question about her taken from the rotation list. There are no prices, intros, teases, slogans or sign-off.

It is far better than our old script on this title (64/140). That script had a name intro, a question held to the end three times, strangers judging her at the bakery, a $60-$150 price on a non-budget title, a long QR walkthrough, a subscribe ask and "A bientot".

**What lets it down:**
- **"ANY Face Shape" is said only once,** in the hook. Cuts three and four leave face shapes unaddressed.
- **"Take 10 Years Off" is said twice, the bare minimum.** One of the two casts doubt on the other cuts: "If any cut on this list is going to take ten years off, my bet is this one."
- **The French lens disappears after cut one.** Cuts two to four never say why they are French.
- **Every item but the last ends the same way:** the result, then a forward line into the next cut. That chain is F05's device, and the audit wrongly says the script doesn't use it.
- **"You" is below the pack's guide:** 38.7 per 1,000 for the whole family against about 45.
- **A few lines don't land on one listen** (section 4).

## 2. Scores (1-10)

The hook counts double. The total is out of 140.

| Category | New | Ours (egJ5B6d879c) | Winner (M07) |
|---|---|---|---|
| The hook (x2) | 8 (16) | 3 (6) | 4 (8) |
| Keeping the title's promise | 7 | 6 | 6 |
| Clarity on one listen | 8 | 6 | 8 |
| Emotion | 8 | 5 | 8 |
| Voice and persona | 8 | 3 | 5 |
| Claims and proof | 9 | 4 | 4 |
| Money | 10 | 3 | 10 |
| Safety | 9 | 5 | 8 |
| Written for the voice | 9 | 6 | 6 |
| CTA and ending | 9 | 2 | 3 |
| Length and pacing | 8 | 6 | 6 |
| Originality vs the models | 9 | 7 | 8 |
| Audit honesty | 7 | 5 (n/a, neutral) | 5 (n/a, neutral) |
| **Total / 140** | **117** | **64** | **85** |

**How the references were scored.** Neither reference has an audit, so both get a neutral 5 for audit honesty. M07 is a real stylist on camera. It was scored against the same persona rules: clients, her own face and celebrity names cost it under "Voice and persona" and "Claims and proof". So its total shows how well it fits our rules, not what it is worth on YouTube.

**Why the new script lost points:**
- **The hook (8, not 9-10):**
  - The feeling line is softer and vaguer than the model's.
  - "every one of them dries on its own" adds a second promise.
  - Sentence three carries a three-part list with a colon, which is a lot for the first ten seconds.
- **Promise (7):** "ANY" is said once and isn't paid cut by cut. "Ten years" is at the minimum, and one of its two uses hedges against the other four cuts.
- **Audit honesty (7):** one false claim about F05, and two small overstatements (section 4).

### My counts

I ran `python3 -I` on `script.txt` with the CTA marker lines removed, and on the transcripts with timestamps stripped. Tokens are letters and digits with apostrophes kept. My word count for the new script is 2,194 against the scanner's 2,178; use the scanner's for length.

| Per 1,000 words | New (2,194) | Ours (2,734) | M07 (2,067) |
|---|---|---|---|
| "you" family (you, your, you're/'d/'ve/'ll, yours, yourself) | 85 = 38.7 | 130 = 47.5 | 114 = 55.2 |
| "you" and "your" alone | 75 = 34.2 | 113 = 41.3 | 95 = 46.0 |
| "but" | 11 = 5.0 | 4 = 1.5 | 10 = 4.8 |
| "I" (I, I'd, I'm, I've, I'll) | 12 = 5.5 | 12 = 4.4 | 21 = 10.2 |
| questions ("?") | 6 = 2.7 | 6 = 2.2 | 9 = 4.4 (auto-captions, punctuation partial) |

**Reading the counts:**
- **Questions:** 6 in all. Five are in the body ("Which one is your cut doing right now?", "So how do you make the French one fit your face?", "So what do you say in the chair?", "Is your hair silver, or on its way there?", "Have you worn your hair long for most of your life?"), plus the comment ask. That is inside the pack's 4-8.
- **"But":** 5.0 per 1,000, exactly at the pack's floor ("about five or more"), and present in 5 of 5 items.
- **"I":** about half the guide's 10 per 1,000. This is reported, never a fail. Every "I" is an opinion or an approved line: "I'd leave it behind", "I understand why you'd hesitate", "I used to think bangs belonged to younger faces, and I changed my mind" (the profile's detail 1, said once), "If I had to choose one length for almost every face, I'd choose this one", "which I love on this cut", "I'd pick the bob or the lob first", "I'd say twice", "I think it's the most elegant way". There are no experience claims.

**Items that name a feeling: 2 of 5, plus two feeling words in bridges.**
- Cut two: "If the last bangs you had took months to grow out, I understand why you'd hesitate."
- Cut four: "If short hair frightens you, it's probably because of one particular short cut."
- In bridges: "If bangs make you nervous, the next cut is the gentlest way to try them" (into cut two). Cut five's opening, "Have you worn your hair long for most of your life? You don't have to cut it short because you've turned 60.", is permission, with the attachment implied but not named.

Each feeling sits before the fix, in one plain sentence, on the fear of the change, which is the pack's hair note. That is above the pack's "about one in four" without feeling heavy.

**Title words:**
| Title words | Times said | Notes |
|---|---|---|
| "French" | 8 | |
| "haircut(s)" | 9 | |
| "flatter(s)" | 2 | both in the hook |
| "face shape" | 2 | the hook and cut two, "Each face shape gets something different from them" |
| "ANY" with face shape | 1 | the hook only |
| "after 60" / "turned 60" | 2 | |
| "five" | 2 | |
| "ten years" | 2 | the hook and cut three |
| "younger" | 2 | "younger faces" in the changed-mind line, and "looks younger than hair that's held in place" |

The scanner's TITLE WORDS line only checked "ten years". Nothing checks "ANY", the title's own capitalized promise word (see library fix L4).

## 3. The hook, side by side

### The model: M07

Glam Girl Gabi, "Best Bangs for your Face Shape (At Any Age!)", `hooks.md`, the best N, hair. It is marked "In part": moves 1, 2 and 4 are usable. Its hook is 625 words as kept, with item one at 4:16 (215 seconds once the banned parts are taken out).

Its moves:
1. contrast, 25 words: "Bangs can transform you into the most gorgeous version of yourself, or they can draw arrows to absolutely everything that you hate about your face."
2. question to her, 5 words: "What's it going to be?"
3. (not usable) the client question, 24 words
4. the cause, 33 words: "Flattering bangs aren't just about face shape, they are about balance..."
5. to 15. (not usable) the mapping task, four mirror questions, the cause, the feeling, the celebrity example, reassurance, the credential with clients, permission, a pattern, her own face, the cause again
16. scope, what comes next, 19 words: "Let's move on and break down the different types of bangs and who they tend to flatter the best."
17. item one

### The new hook, in full: 82 words, item one at word 83 (about 29 seconds)

> The right haircut after 60 can take ten years off your face, or it can frame the very things you'd rather nobody noticed.
>
> Which one is your cut doing right now?
>
> A haircut flatters through three things: where its length ends, where the volume sits, and what the bangs and the part do.
>
> Get those three right, and these cuts can flatter any face shape.
>
> These five French haircuts are built exactly that way, and every one of them dries on its own.
>
> Cut number one. The French bob.

| M07 move | New move | Words |
|---|---|---|
| 1. contrast (best version or arrows at what you hate) | contrast: "can take ten years off your face, or it can frame the very things you'd rather nobody noticed" | 23 |
| 2. question to her | "Which one is your cut doing right now?" | 8 |
| 4. the cause (balance, not face shape) | the cause: three levers (length, volume, bangs and part), then "these cuts can flatter any face shape" | 34 |
| 16. scope, what comes next | scope with the count: "These five French haircuts are built exactly that way, and every one of them dries on its own." | 17 |
| item one | "Cut number one." | |

### Judgment

**What it gets right:**
- **It follows the model.** It is the model's format, carried in order with fresh words. It is far shorter than the model (82 against 625) and well under 110 words.
- **It gets to item one fast:** at about 29 seconds, against the pack's 45.
- **The promise comes first.** "Take ten years off" is in sentence one, "any face shape" in sentence four, and the count in the last move. It holds no intro, age slogan, tease, task, "Picture…" or recap.
- **It asks about her own mirror:** "Which one is your cut doing right now?".
- **The why starts in the hook,** as in 7 of the 16 best hooks.

**Where it falls short:**
- **Move 16 isn't in the model's usable list.** It is in the model's order and works as the late count line, as in 11 of 11 winning hooks with a count line, so it is a fair carry. `hooks.md` should say so (library fix L1).
- **The feeling is softened into a polite blur.** The model names it: "draw arrows to absolutely everything that you hate about your face". Ours says "the very things you'd rather nobody noticed". It is kind, but on one listen she can't picture what is meant. The pack's hair note wants "the cut that never looks right" in her words. Something like "or it can sit in exactly the wrong place and pull your whole face down" is kind and concrete.
- **"and every one of them dries on its own" is a second promise.** That is on the hook's banned list, though it does carry the French air-dry habit. Better: let the scope line carry "French" without a second benefit ("These five French haircuts are built exactly that way."), and give the air-dry promise in cut one, where the heritage line already makes it.

### Our old script's hook, for comparison

About 339 words; item one at 1:52. Its moves:
1. the villain: "Somewhere along the way, someone looked at you and told you your face shape."
2. the repair-job scene
3. a question with the promise: "somehow look 10 years lighter?"
4. the name intro and channel promise: "I'm Diana Shambre and this is where women over 60 come to borrow the French way"
5. the count with a tease: "somewhere in the middle, the one cut that works on every face shape"
6. the cause (the set, the helmet, the scraped bun)
7. the faceless reframe: "Your face shape was never the problem. The repair job was."
8. the chart in four lines
9. a held item: "I'm saving that question for the very end"

The feeling is sharper than the new hook's (the chart she obeyed), but it breaks five hook bans.

## 4. Failures

### Writer slips (the rule was there)

**W1. "ANY Face Shape" is under-paid, and one "ten years" line doubts the others.** Rules broken: `SKILL.md`, "The opening" 4 and "Emotion" rule 8; the rubric's "every title word said at least twice"; the brief, "each of these five adapts to the face by adjusting those three".
- "Any face shape" is said once: "Get those three right, and these cuts can flatter any face shape."
- **Cut one** fits oval, heart, square and round, but never long, though the trace lists long one line earlier.
- **Cut three** names only round and square, then hedges: "If I had to choose one length for almost every face, I'd choose this one."
- **Cut four** opts out: "On a long or square face, I'd pick the bob or the lob first, and there's nothing wrong with that." It's an honest limit, since the brief only gives oval, heart and round for the pixie, but it leaves the title's capitalized word unpaid for that cut.
- "If any cut on this list is going to take ten years off, my bet is this one." puts the title's promise in doubt for the other four.

Fix:
- Say "any face shape" once more in the body, in fresh words, where the levers pay it. For example, at the start of cut five: "This is the cut that shows the promise best: the length stays, and only where the layers start changes for your face."
- Give cut one a long-face line from the brief's basics (bangs and width at the sides).
- Give cut three a heart and long line (fullness at chin level; the curtain bangs from cut two).
- Turn the pixie's limit into the levers rather than an opt-out. For example: "On a long or square face, keep the wispy fringe and a little fullness at the sides", from the brief's face-shape basics.
- Recast the cut-three line as a superlative, not a condition: "Of all five, this is the one I'd bet on to take the most years off."

**W2. The item endings don't vary.** Rule broken: `SKILL.md`, "The item shape", "Vary the item endings": "End some items on the result, some on a question to her, some on the permission line, some on the bridge." The iter-07 fix is only half working: the end lines differ in content but not in form. All four items that can end on a bridge end on the result, then a forward line naming the next cut:
- "If bangs make you nervous, the next cut is the gentlest way to try them."
- "Now, if your hair is fine and every cut seems to go flat by lunchtime, the next one was made for you."
- "The next one sounds like the biggest step of the five, but plenty of women find it the easiest to wear day to day."
- "But maybe you've heard all this and you still want your length. Then keep it, because the last cut is for you."

None ends on a question to her or stops on the result with the next item opening cold.

Fix: end cut three on its verdict ("and this cut moves.") and open cut four cold. End cut two on a question to her mirror.

**W3. The audit says the script avoids F05's device, but it uses it.** Rule broken: `core/greenlight-audit.md`, the evidence must match the script; `SKILL.md`, "Using the models" 1. The audit's Originality line says the structure differs from F05 by "no forward line on every item". As quoted in W2, every item that has a next one ends on a forward line naming the next problem. That is F05's "chained forward lines" (F05 model file, "What sets it apart"). Borrowing it is allowed. Claiming not to is an audit error.

Two smaller overstatements:
- The Promise map says "each cut's face-by-face fit (cuts one to five, with the honest limit in cut four)". Cut three names only two shapes, and cut one misses long.
- The Hook line counts "83 words". The hook is 82 words, with item one at word 83.

Fix: name what each model lent, as well as what differs. Here F05 lent the chained forward lines and the short hook-to-item-one; M07 lent the hook format and the face check.

**W4. The French lens stops after cut one.** Rule broken: `personas/diane-de-chambray.md`, "The French Way" 3: "The French practice is the reason; the viewer's own closet is the fix".
- Cut one carries all of it: "plenty of French women wear it with bangs"; "The way I was raised in Paris, a haircut had to dry on its own and still look right weeks later."; "Many French women still cut their hair that way".
- Cut five has only "what the French call a chignon".
- Cuts two, three and four ("Curtain bangs on a shoulder-length cut", "The collarbone lob", "The soft pixie") never say what makes them French.

The brief's documented habits sit right there:
- the air-dry cut, which cut three already uses: "It air-dries."
- gray worn on purpose and kept glossy, which cut four already uses: "a sharp short cut makes gray look intentional"

Neither is tied to the French practice, so for a title that starts "5 French Haircuts" she has to take it on trust.

Fix: one hedged French clause in cuts three and four, in English, from the documented ground. For example: "Gray worn on purpose and kept shiny is one of the things you'll often see in Paris." That respects the one-or-two French words cap, which correctly kept out "le carré long", "la frange rideau" and "la coupe garçonne". See library fix L3.

**W5. A few lines that won't land on one listen.** Rule broken: `SKILL.md`, "Voice" (plain over clever) and the rubric's clarity test.
- "On a long or square face, I'd pick the bob or the lob first, and there's nothing wrong with that." Nothing wrong with what? Fix: "...and that's a fine choice, not a failure."
- In cut one, round faces are told to "take it past the chin and sweep it into a side part", then everyone is told to "Ask for a chin-length bob cut to air-dry". A round-faced viewer asks for the wrong length. Fix: "Ask for a bob cut to air-dry, at the length that suits your face, with soft, textured ends and no graduation at the nape."
- "A silver gloss is still color, so do a patch test 48 hours before, at home or in the salon, as the box instructions tell you, because a reaction to dye can be serious." At 34 words, this is the longest sentence in the script, and a salon gloss has no box. Fix: split it. "A silver gloss is still color. Ask for a patch test 48 hours before, and if you do it at home, follow the box, because a reaction to dye can be serious."
- "On a long face, they shorten the length". Fix: "they make a long face look shorter".
- "so the eye travels up and across instead of around" is abstract; "lifts the eye" is enough.

**W6. "You" is below the guide.** Rule broken: `SKILL.md`, "Voice": "'you' and 'your' together about 45 per 1,000 words".
- The whole family runs at 38.7 per 1,000; "you" and "your" alone at 34.2.
- The why lines go third-person on the face. For example: "The pieces around the jaw are soft, so a square jaw looks gentler." "It's at its best on oval and heart-shaped faces, because those faces carry short sides easily."

Fix: put her in those lines ("If your jaw is square, the soft pieces make it look gentler").

**W7. Small voice notes.**
- "the gray worn on purpose" and "it looks like you chose it on purpose" are an echo in back-to-back sentences.
- "women of a certain age" is a stock euphemism. Plainer: "the advice handed to women years ago".
- The mid-CTA's benefit is a feature ("every one tells you how to do it and when to skip it", true per the book index). The profile's added-value promise ("the system behind today's tip") would make shape part 4 a real benefit.

None of these is a fail.

### On the points the main session asked me to check

**How "Take 10 Years Off" and "ANY Face Shape" are paid.**
- "Ten years" comes in the hook ("can take ten years off your face"), hedged with "can", and in cut three, with a real why: "Hair that moves when you turn your head looks younger than hair that's held in place, and this cut moves."
- The other cuts end on look results that serve the promise without saying it: "your eyes look brighter either way", "your whole face looks brighter and more awake", "It lifts your whole face".
- "ANY" is paid by the method (the three levers, the mirror trace, five shapes in cut one) and by cut five, which fits all five shapes. It is not paid cut by cut (W1).
- The book CTA never says "younger", which is correct per the book index.

**The hair-side rules.**
- **The stylist is never the enemy.** The only fault-finding is with the dated cut ("That shape was made to be set and sprayed, and I'd leave it behind") and with old advice ("the advice handed to women of a certain age was to go short and have it set").
- **How to be heard in the chair is the strongest thing in the script.** Every cut has an "Ask for…" line taken straight from the brief, and the terms are explained: graduation, point-cut, lob, face-framing pieces, thinning shears, blunt line, gloss, brassy. There are lines to say ("If you say only one sentence, say 'please don't thin my ends.'") and in-chair checks ("Before you leave the chair, twist it up once and see whether the shorter layers fall softly around your face."). The fix is never blame: "that's an easy fix while you're still sitting there."
- **The safety defaults:**
  - heat: "put a heat protectant on first, and keep the heat lower on fine or gray hair"
  - thinning: "But if it's coming out suddenly or in patches, take that to your doctor before you take it to a haircut."
  - dye: the 48-hour patch test (clumsy, W5)

  Each is one line, in proportion. Nothing claims to regrow hair.
- **The over-70 lean:** "without holding your arms up behind your head" and "A low chignon is kinder to stiff shoulders than a high one".

**Diane's French lens.**
- Every French claim is hedged: "plenty of French women", "Many French women", "what the French call a chignon".
- The heritage line is said once, behind a practice: "The way I was raised in Paris, a haircut had to dry on its own and still look right weeks later."
- The one approved detail is used once: the changed mind.
- The French word "chignon" is written plainly, with no accents and no pronunciation guide. The brief's four French cut names were rightly left out under the one-or-two cap.
- The brief's "(hedge to 'most women I know in Paris')" was correctly overridden by the profile's ban, and the audit says so.
- The lens is thin, not wrong (W4).

**Numbers written for the voice.**
- "after 60" and "48 hours" are digits, as `workflow.md` §4 has for stats.
- "two to three inches", "four to six weeks" and "a couple of minutes" are in words, with the units as full words.
- "101" in the CTA is a profile fact and a digit, which is allowed.
- No symbols, no brackets in the script, straight quotes only.
- No price at all. This is not a budget title, so the brief's $40-$100 gloss, $50-$70 US cut and €35-€50 Paris cut stay background, which is correct.

**The rotation.**
| Field | The log | This script |
|---|---|---|
| Models | M28, F06, M21 | M07, F05 |
| Hook model | M28 | M07 |
| Comment question | her age and where she's watching from | "What's the haircut you've worn the longest, and how long have you had it?" (from the pack's rotation list, about her) |
| Opening | the contrarian opinion | the either-or |
| Mid-CTA opener | "A quick aside, while your jackets are on your mind" | "Since so much of a good haircut comes down to what you ask for" (the audit says round 1 caught it too close to the log's and fixed it) |
| Personal detail | the scarf knot | the changed mind |

Nothing repeats.

### Library fixes (a rule is missing, unclear or wrong)

**L1. `hooks.md`, M07, "Usable for".** It lists "Moves 1, 2 and 4". The writer also carried move 16 (scope, what comes next) as the closing count line. That fits the bank's own finding that the count line is one of the last two moves in 11 of 11 hooks that have one. Fix: "Moves 1, 2, 4 and 16 (as the count line)". Better still, a general line in "How to use this file": "An In part model's closing scope or count move may always be carried."

**L2. `greenlight-audit.md` E1 signal 6 (and `SKILL.md`, "Using the models" 1).** The audit lists only what differs from each model, so it can claim a difference that isn't there (W3). Fix: the Originality line names, for each model, one thing it lent and three things done differently, each checkable in the script.

**L3. `personas/diane-de-chambray.md`, "The French Way".** Nothing says how often the lens returns on a "French"-titled list, and the one-or-two French words cap means the brief's French cut names can't carry it. Fix: "On a title that names the French way or French items, most items carry one hedged French reason in English, from the brief or the documented ground (air-dried hair, gray worn on purpose, the low chignon, the small wardrobe), never a new custom."

**L4. The scanner's title words.** The style `title-words` list caught only "ten years". The title's capitalized promise word "ANY" and its subject "face shape" went unchecked. Fix: count every capitalized word in the locked title (ANY, NEVER, OLDER) as a title word. Or have the audit's Promise map give a count for each title phrase, with the line that pays it.

**L5. The ideation brief spec (outside this repo's library, `style-ideation`).** The brief told the writer to "hedge to 'most women I know in Paris'", which Diane's profile bans. The writer handled it right, but the brief writer should stop producing it. Note it for the ideation skill.

**L6. `core/workflow.md` §1.2 against test runs.** Diane's profile and `channels.md` row both read "pending", and §1.2 says a pending profile stops with NOT READY. The chat ran, which is what a test needs. But as written, a VA could not run this channel, and a writer that followed §1.2 exactly would fail the test. Fix: say how a pending channel is test-run (for example, "a TEST run may proceed; a live run stops"). Or flip the status once the operator signs off.

## 5. What the new script does better

### Than our old script (egJ5B6d879c)

- **No intro, no held item, item one at 29 seconds against 1:52.** The old one said "I'm Diana Shambre and this is where women over 60 come to…" and "I'm saving that question for the very end". The new one is in the first cut by its sixth line: "Cut number one. The French bob."
- **Her own mirror instead of judging strangers.** The old one: "Then the woman behind you at the bakery counter leans over and asks, 'Who cuts your hair?'" The new one: "Sit down in front of the mirror and take a photo from the front. The ends should rest on your collarbone, and the front pieces should start around your cheekbones."
- **Hedged French.** The old one: "French women are known for going longer between cuts, often 10 or 12 weeks." and "a French woman just lets it air dry… Voila." The new one: "Many French women still cut their hair that way".
- **No price.** The old one: "A good haircut in America runs somewhere between $60 and $150." The new one says none.
- **Safety where the old one had none.** The old script had round brushes and no heat line. The new one: "put a heat protectant on first, and keep the heat lower on fine or gray hair".
- **A clean CTA and ending.** The old one ran a QR walkthrough ("Point your phone's camera at the code"), "Whenever it suits you is the right time", the wrong "389 pages", a subscribe ask, "which of these five cuts is going to the salon with you" and "Abento". The new one: "My book, The French Way, has a chapter on hair, with a Secret on cutting to open the face and another on booking a proper consultation." It ends on "What's the haircut you've worn the longest, and how long have you had it?"
- **The why for fine hair, which the old one never gave:** "Fine hair looks thin when the ends are thinned out, because light passes straight through them."
- **"But" at 5.0 per 1,000 against 1.5.**

**What the old one still does better, worth keeping in mind:**
- It addresses all four face shapes in every cut, which pays "ANY" harder: "One fringe, four faces, four different jobs".
- Its "worst day" chair question is a strong tool the new one lacks: "ask how it will look in 10 weeks. If all you do is wash it and let it dry".
- Its shake test.

### Than the winner (M07)

- **Item one at 29 seconds against 4:16,** with no task, celebrity comparison or client claims before it.
- **The words for the chair in every cut.** M07 gives none: "Ask for curtain bangs that start just below the brow at the center and blend into layers at the cheekbones. The word 'blend' matters, because it means the bangs grow into the rest of the cut instead of hanging there on their own."
- **It pays the age in the title.** M07 never says "At Any Age". The new one: "You don't have to cut it short because you've turned 60."
- **It shows the method on her own face,** inside item one, without naming anyone else's features: "Pull your hair straight back, stand close to the bathroom mirror, and trace the outline of your face on the glass with a bar of soap or an old lipstick."
- **It ends on a question about her** instead of two video plugs.

**Where M07 is still ahead:**
- its opening line is sharper ("draw arrows to absolutely everything that you hate about your face")
- its permission ("There are no hard rules.")
- its closing self-test (the hat test)
- about twice the "I" for personality

## 6. The top five changes, ranked

1. **Pay "ANY Face Shape" and "Take 10 Years Off" cut by cut.**
   - Say "any face shape" once more in the body.
   - Give cut one a long-face line, and cut three heart and long lines.
   - Turn the pixie's opt-out into the levers ("keep the wispy fringe and a little fullness at the sides").
   - Recast "If any cut on this list is going to take ten years off" so it doesn't doubt the other four.

   (W1; library fix L4 so the scanner counts "ANY".)
2. **Vary the item endings, and make the audit tell the truth about borrowed structure.**
   - End at least one item on its result with no forward line, and one on a question to her.
   - Fix the audit's false "no forward line on every item" claim.
   - The Originality line names what each model lent.

   (W2, W3; library fix L2.)
3. **Carry the French lens through the list.** One hedged French reason, in English, in cuts three and four, from the brief's documented habits: the air-dry cut, gray worn on purpose and kept glossy. (W4; library fix L3.)
4. **Fix the one-listen lines.**
   - In the hook, make the feeling concrete and drop the second promise ("every one of them dries on its own").
   - Fix "there's nothing wrong with that".
   - Fix cut one's "chin-length" ask for round faces.
   - Split the 34-word patch-test sentence and drop the box from the salon case.

   (W5; section 3.)
5. **Raise "you" toward 45 per 1,000.** Put her in the why lines ("If your jaw is square…"), and make the mid-CTA's benefit the profile's added-value promise instead of a feature. Also, in `hooks.md`, list M07's move 16 as carryable (L1), and settle how a pending channel is test-run (L6).

## The iter-07 fixes, checked

| Fix | Working? | Evidence |
|---|---|---|
| Item endings vary; the check is given plainly, never announced | Half | The checks are plain and unannounced: "If they fall open again by themselves the next morning, they were cut well."; "Before you leave the chair, twist it up once…". The endings don't vary: four of four end on the result plus a forward line (W2). |
| No spoken pronunciation guide | Yes | "twist it into a loose, low bun at the nape, what the French call a chignon." No guide in the script or the VO copy. |
| "You" and "your" about 45 per 1,000 | Not yet | 38.7 (family) and 34.2 (you/your alone) (W6). |
| Diane's "most" for broad habits, "plenty of"/"many" for a specific piece, no "women I know in Paris" | Yes | "plenty of French women wear it with bangs" (a specific look); "Many French women still cut their hair that way" (a broad habit, hedged even more cautiously than "most"). The brief's "most women I know in Paris" was refused, and the audit says why. |
| A whole-look title may keep one short face paragraph | n/a | A hair title. No face or makeup paragraph, correctly. |
| The book's spoken title in the CTA | Yes | "My book, The French Way, has a chapter on hair…"; the end reminder: "The French Way is linked in the description." |
| Item length by count | Yes | Five items at 450, 351, 403, 394 and 368, all inside 300-450. Item one sits at the top because it carries the face-shape method. |
| The hook stays a winning model's format, applied | Yes | M07's contrast > question > cause > scope, in order, 82 words (section 3). |

## The chat and the rotation (not scored)

**The channel gate.** "START the french lady" clearly means one channel. The chat confirmed in one line, "Diane de Chambray, right?", and carried on at "yes", as `workflow.md` §1.1 now asks. It did not send the list.

**The input gate.**
- Reply 2 asked for the three inputs in one numbered message, each with one line on what a valid one looks like, and nothing else.
- When the title and brief arrived without the log, reply 3 named only the missing item.
- At "just write it, skip the log", reply 4 refused in one short reason with no lecture: "I can't start writing without the rotation log. It's how each script stays different from the last few on the channel." It then asked again for only the log, including the "none" option. That is correct under §2, "No way around it".
- At the one-line log, the chat went straight to the run without asking why there was only one line. That is fine under §2 ("fewer only if the channel has fewer scripts").

**The rotation.** No model, hook model or comment question from the pasted log was reused (see the table under "The rotation" in section 4). The new log line records `model: M07, F05 | type: the best N | hook: M07 | comment: "the haircut you've worn the longest, and how long you've had it"`.

**One note for the main session.** Diane's profile and `channels.md` row both say "pending". `workflow.md` §1.2 says to stop at NOT READY for a pending profile. The chat ran, which is right for a test, but the rule as written would block a VA and contradicts the test. See library fix L6.
