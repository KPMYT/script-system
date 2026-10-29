# Style pack diagnosis: one hair-and-fashion pack and two profiles (DRAFT)

Written 2026-10-28 by the session 14 chat (branch `claude/youthful-ritchie-zq7e92`), for the next step the operator set: "the pack diagnosis draft for the hair and fashion packs and the two persona profiles". Since then the operator decided hair and fashion are **one pack for now** (HANDOFF §3, session 14). **Nothing in any skill, pack or profile has changed.** This is the plan; every change goes to the operator first.

**The operator's answers (2026-10-29), recorded in `HANDOFF.md` §3 (session 14, the diagnosis):** 1 yes (`style-scripts`); 2 yes (Talking Head); 3 yes (one numberless line); 4 yes (one heritage line, "raised in Paris"); 5 yes (no age, no "one of us"); 6 **no sign-offs** (the script ends on the comment ask); 7 yes; 8 yes (the book texts still to paste); 9 **no subscribe CTA, just the e-book**; 10-12 yes; 13 yes, "unless brief says otherwise" (the brief wins over the defaults); 14 **"we can have opinions against brands"**; 15-17 yes; 18 yes, "make it tts friendly". Later the same day: 21 "salon is not the enemy" (no salon or stylist villain, even in tone); 22 "we dont need ideation yet". Not answered yet: 19 (voice samples), 20 (personal details); "scarlet" (unplaced, asked).

**What was read:**
- the core (`core/`, the scanner included), `tools/build_skills.py`, `tests/run_checks.py`, `HANDOFF.md` §3, `PROPOSALS.md`
- the plumbing pack (the structure every pack starts from), and how the HVAC and electrical packs adapted it
- the style study: `studies/style/comparison/README.md` and files `00`-`08`, the breakout map, our own 38 videos
- the 37 model videos collected this session (`studies/style/models/approved-models.csv`)
- the operator's `style-ideation` and `thumbnails` skills (read-only), and the two Notion channel pages, "FASHION - Scarlett Sterling" and "FASHION - Diane De Chambray" (read-only)

**Helpers did the wide sweeps.** Their notes are in `studies/style/pack-diagnosis-2026-10-28/` (`library-sweep.md`, `persona-sweep.md`), and the comparison of hair and fashion is `studies/style/comparison/08-hair-vs-fashion.md`. The main session spot-checked them against the sources (`studies/style/log.md`, round 6).

**Status key** (as the HVAC draft):
- **KEEP:** copy as it is, with new example lines only.
- **ADAPT:** the same rule, style content.
- **NEW:** style needs something the plumbing pack doesn't have.
- **DROP:** a plumbing-only rule the style evidence doesn't support; the core default stands.
- **ASK:** the operator's call, numbered in section 9 with a recommendation.

---

## 0. The short answer

Style is the furthest niche from plumbing so far:
- the viewers are older (median age 70)
- their problems are practical more than emotional (no stylist who can cut, no clothes that fit)
- most real presenters name no villain (11 of 21)
- the winners hardly mention money (prices in 5 of 45 study videos; ours in 34 of 38)
- and the persona can't do what makes the real presenters work: wear it, try it, show a client

So the plumbing pack's **structure** carries over (inputs, the overrides table, the opening's jobs, the item shape, the ending, models never copied, the banned list, the scanner block, the checklist), but most of its **content** is rewritten, and the emotion section is rebuilt from this niche's own evidence, as the operator asked.

| Part | Verdict | Size of the job |
|---|---|---|
| The script-writer and the core rules | **KEEP.** Nothing in the core stops a style channel. Its locked bans (no intro, no teases) are exactly what the style evidence asks for. | Small: two channel rows, build entries |
| The core scanner | **ADAPT.** Five gaps (section 2), one of them the title-word check you approved (suggestion 2). | Medium: core changes, each with a test (ASK 17) |
| The plumbing pack's rules | About a third KEEP, half ADAPT, the rest NEW or DROP | Large: a real rewrite |
| References | Structure KEEP; content all new: 30 real models and 7 faceless structure-only models, voice samples from women, excerpts. **No price guide.** | Large |
| The two profiles | NEW. Notion, the ideation skill and our 38 scripts disagree on who each woman is (section 5). | Medium, but it needs your decisions |
| Wiring | Rows 10 and 11, build entries, checks, P20 | Small |

---

## 1. Hair and fashion: are the emotions the same?

**Mostly the same, so one pack works, with a short hair note and a short fashion note inside it.** From `studies/style/comparison/08-hair-vs-fashion.md`: every transcript of 38 real-presenter videos (15 hair, 23 fashion) and 20 faceless ones read in full, and 2,138 comments coded by hand.

**What's the same:**
- **The feelings viewers voice:** 29% of hair comments and 29% of fashion comments voice a feeling about herself, and both lead with the same four: permission ("I wear what I want"), relief at an explanation, unhappiness with a body part, and "nobody shows women like me".
- **How presenters voice them:** a feeling in the hook in about half the videos on both sides (7 of 15 hair, 14 of 23 fashion); the presenter's own feeling in about a third on both.
- **The voice counts:** "you", "I" and questions don't differ. Fashion presenters say "but" a little more (8.3 against 6.6 per 1,000 words).

**What differs (large and steady):**

| | Hair | Fashion | How sure |
|---|---|---|---|
| **Who gets the blame** | the stylist: complaints on 12 of 15 hair videos (0 of 23 fashion); "not listened to" on 9 of 15 (2 of 23) | clothes that don't fit or aren't made for her: 12 of 23 fashion videos (0 of 15 hair) | strong (p ≤ 0.001) |
| **The feeling the script names** | fear of the change and the process ("petrified" of a short cut, nervous about bangs, the patience of going gray): 10 of 21 hair feeling items | the body, comfort and confidence: 37 of 47 fashion feeling items | strong (p = 0.0002); the faceless scripts split the same way |
| **Hard words** ("frumpy", "old lady", "mumsy", "dowdy") | 1 of 15 scripts; hair says "aging" and "older" | 13 of 23 scripts | strong (p = 0.002) |
| **Topics of their own** | the gray grow-out (hiding it, being judged), styling it yourself at home | feet, shoes and health; petite sizing; heat | a handful of videos each |

**What this means for the pack:** one emotion section for both (3.7), plus two short notes:
- **Hair:** the pain is the salon that didn't listen and the fear of the change. The feeling line goes on the nerve before the cut ("if a short cut scares you…"), the fix includes what to say to the stylist, and the stylist is never the villain as a person (3.5). Hard words are rarely needed.
- **Fashion:** the pain is the body changing and clothes not made for her. The feeling line goes on the body and comfort; hard words belong here, still at most once and flagged.

**Caution:** one coder; format travels with the group (the salon cut-alongs and gray-hair stories are all hair, the "frumpy" titles all fashion); only 4 faceless hair videos; makeup isn't in the sample.

---

## 2. The core and the scanner

### 2.1 The core rules: KEEP

No core rule has to change for a style channel to run. What each part means for style:

| Core rule | What it means for style | Verdict |
|---|---|---|
| No greeting or channel intro (locked) | Supported: 31 of 42 winners introduce no one; ours do in 38 of 38. Writing through the library removes "I'm Scarlet Sterling and this channel is for women over 60…" by itself (your suggestion 1). | KEEP |
| Teases hard-banned (locked) | Supported: real hooks tease in 1 of 21; ours in about 28 of 38. | KEEP |
| Claims policy | It forbids ages, years, credentials, places, relatives, customers, and "I made, tested, lived it". Real presenters' "I" comes from wearing it and their clients; a persona can't. One soft credential (suggestion 4) fits only as a fixed `tenure:` line or the one approved heritage line (Werner's P14). Our scripts already slip: "I tried that look once…" (Diane), "jewelry I own" (Scarlet). | KEEP; the credential is ASK 3-4 |
| Claims policy, health | Thinning, gray, scalp and menopause are next door. The ideation skill already keeps thinning a styling topic. | KEEP; the pack names the style cases |
| Claims policy, guarantees | "INSTANTLY younger" titles (14 of ours): the title wins, the script never guarantees. | KEEP |
| Offer rules | Both channels sell a book. Diane's book has invented women (Marie, Sophie, Claudette): true book facts, never the persona's own friends. | KEEP |
| The value line | Real hooks promise N items (10 of 21). | ADAPT, as plumbing: the count line, no value line |
| Sources (audit E1) | Style needs no named sources; "studies show" is a faceless habit (15 times in 6 faceless videos, once real). | ADAPT, as plumbing: out of 6, pass at 4 |
| Voice anchoring | Samples must be real women (HANDOFF). Nobody has listened yet. | KEEP the rule; new content (ASK 19) |

### 2.2 The scanner: five gaps style hits (all core)

Tested on our 38 and on 63 study transcripts (library sweep §3).

| # | Gap | Example | Effect | Fix |
|---|---|---|---|---|
| 1 | **No title-word check** (your suggestion 2) | "Instantly" is in 14 of our titles and said in none of those 14 videos; "younger" in 8 titles, said in 3 | The title's promise goes missing and nothing catches it | A `title-words` key: each listed word in the title must be said at least twice, once in the first minute |
| 2 | **The self-introduction passes** | "I'm Scarlet Sterling and this channel is for women over 60" | Only the plumbing and electrical blocks ban "this channel is for" | Into the pack block, and the core's hard-ban list (every channel) |
| 3 | **Style tenure words** | "As a stylist for 30 years", "After 30 years in fashion", "In forty years of dressing…" all pass | A wrong or invented credential passes silently (the same class as P16) | Add stylist, fashion, dressing, hairdresser, colorist to the trade words |
| 4 | **Style item signposts** | "Rule number three", "Secret number five", "The first cut is…" aren't found | The ITEMS line (which the audit copies) is wrong on most style scripts | Allow "[word] number N" and style words (rule, secret, cut, color, knot, habit) |
| 5 | **French accents fail** | "Voilà", "chérie", "À bientôt" (21 hits in 9 of ours) | Every accented word is a fix | Write them without accents, or a profile key for allowed letters (ASK 18) |

Smaller: "H&M" fails on the "&" (write "H and M"); "bow" is a two-way word ("a bow blouse"), a judge line, fine.

**One existing bug found on the way:** in `tools/build_skills.py`, the electrical scanner command's code block is never closed, so the HVAC command below it shows as plain text in the script-writer skill (confirmed). It's a one-line fix in a ready skill (ASK 17).

---

## 3. The plumbing pack, section by section

In `plumbing-scripts/SKILL.md` order.

### 3.1 What it covers, files: KEEP the structure, ADAPT the description

The description names style triggers (haircut, bob, pixie, gray hair, fine hair, outfits, wardrobe, colors, glasses, necklaces, earrings, scarves, shoes, body shape, look younger, look expensive, frumpy, the French way) and says **no makeup**, so a lipstick title doesn't load it. Files: unit plan, voice samples, excerpts, models. **No price guide.**

### 3.2 The overrides table

| Plumbing row | Style plan | Why |
|---|---|---|
| Inputs: title, brief, rotation log; no research pack | KEEP | The brief is the fact source |
| Named forward promises in the body (P3) | **DROP** (the core's short-range rehooks stand) | Real videos hold nothing for the end (1 of 21) (ASK 16) |
| The ending: end CTA, then the comment ask last (P5) | ADAPT: plus one short sign-off per profile (ASK 6) | Section 3.10 |
| 12-minute minimum | KEEP (ASK 10) | Ours run 16-17 minutes; faceless 15.6; real 11.9 |
| Rotation-log fields | ADAPT: model, type, **opening device**, comment question | Our "Picture…" opener is in 36 of 38: rotation exists to stop that |
| Copy guard | KEEP, plus electrical's 5-word example guard | Our house vocabulary is a copy-guard problem |
| Mid-video CTA a third in, never before item 3 | ADAPT per profile: after the first real payoff (ASK 8) | Style lists run 6-7 items; "after item 3" in a 5-item list is 60% in |
| No sources; originality out of 6, pass at 4 | KEEP | |
| Signposts ("Number four.") | ADAPT: numbered, or a "the next…" sentence | Real presenters use "the next…" (9 of 16); the scanner needs gap 4 fixed |
| Prices from the brief, then the price guide | ADAPT: the brief only; general styling knowledge marked | No price guide (3.14) |
| Contractions kept | KEEP | |
| No value line | KEEP | |
| Cents exceptions | **DROP** | No money devices in style |
| NEW | Prices only on budget titles; item one by about 45 seconds; an item-length band | 3.6, 3.14 |

### 3.3 Inputs: KEEP, with one ADAPT

Title, brief, rotation log, no research pack. Where the brief is silent, the script may fill in **well-established styling knowledge** (proportion, contrast, the neckline and the necklace, the rise of a jean), never a price, a product's availability, or a health, scalp or dye fact beyond the brief and the safety defaults. NOT READY only when the brief can't carry the title's promise, never for missing prices.

### 3.4 The viewer: ADAPT, heavily

Plumbing's homeowner is replaced by this niche's woman (`01`, `07`):
- **Age:** median 70; 51% are 70 or over. One emotion set with a light over-70 lean: comfort, mobility, the older client (S4, agreed).
- **Practical problems first:** no stylist who can cut (28 comments), no clothes that fit (28), health or mobility (22). Top-liked: "it's nearly impossible to find stylists that can actually cut a bob" (1K likes).
- **She wants the why:** "now I understand why" (18 comments on real videos, 0 on faceless). The explanation is the relief.
- **She wants brands and where to buy:** 30 of about 117 requests.
- **She wants her body named:** never assume a slim one ("a fuller middle", "a softer jawline").
- **She pushes back on rules:** "I'll wear what I want" (55). Give the reason, and the out: "if you love it, keep it".
- **Terms explained the first time:** undertone, contrast, silhouette, proportion, rise, drape, capsule, balayage, lowlights, demarcation line, toner, face-framing layers, blunt cut, curtain bangs, lob, root lift, diffuser, heat protectant, A-line, midi.

### 3.5 The villain: optional (as electrical)

Real presenters name **no adversary in 11 of 21**. Plan: the villain only where the title carries one, aimed at a habit or a default, never a motive:
- **allowed:** the advice she was handed ("somewhere along the way, plum got filed under too much"), the shop's default (sizing, makers who don't cut for her body), the rushed salon default (as a fact, never "they want you back every four weeks"), trends (lightly), the dated version of herself (gently)
- **never:** younger women or other women, stylists as people, "the fashion industry doesn't want you to know"
- **a title that promises a villain** ("Hairdressers Won't Suggest Them") is paid as a fact, never withdrawn in the first minute as both our salon scripts did (and both sit below normal: 0.74x and 0.25x) (ASK 21)

Plumbing's "two facts side by side, never joined by so or because" stays (KEEP).

### 3.6 The opening: ADAPT

Real hooks run about 90 scripted words, with item one at about **0:45** (ours: 1:39); two moves (ours five or six); the age said in 3 of 21 (ours 38 of 38); the title's count in the first 20 seconds in 12 of 28 winners (ours 5 of 38).

The plan, from plumbing's jobs:
1. **The point and the title's promise word in the first sentence or two**, in the title's own words ("younger", "expensive", "instantly"): suggestion 2, agreed.
2. A question, when it fits, about her own mirror or closet.
3. The villain line only if the title carries one.
4. Reassurance or scope in one line (body-shape titles open on it: "it doesn't mean there is something wrong with your figure", Diana GOSS).
5. The count line.
6. Item one by about 45 seconds. At most two or three moves.

**Never:** a name or channel intro, an age slogan, the age as a refrain (say it where the title says it), a tease, a "Picture…" scene as the default opener (36 of 38 ours, 15 of 42 winners), a task before item one ("Go and get the pair you wear most").

### 3.7 Emotion: NEW, built from this niche

**Your words:** "practical solutions to emotional problems … we turn their emotional problem and pain into a heard and easy to solve solution with our practical tricks." What the evidence says:
- **In what viewers write:** your three feelings are present but rare: frumpy 25, losing her spark 17, invisible 6. What leads is **permission and rebellion (113 comments, 10,346 likes)** and **relief at being understood (46)**.
- **In what real presenters say:** they name a feeling in **27% of items (31 of 115)**, in one sentence of about 12 words, more often before the fix than after, and in their own person in 10 of 21 videos. Ours: about 1 item in 11.

Plumbing's 11 rules against that evidence:

| Plumbing rule | Style evidence | Verdict |
|---|---|---|
| 1. Put the viewer in it | Yes, through **her own** mirror, photo, closet, salon chair. Ours use an imagined stranger ("the woman at the next table") and staged scenes | ADAPT |
| 2. One real pain per item | **Too often for style.** A feeling in about a quarter of items, one sentence, mostly before the fix | REPLACE |
| 3. Strong, plain words | Yes, aimed at the garment: "frumpy", "mumsy", "tummy" (ours say "the middle") | ADAPT |
| 4. "But", much more | Yes: real 6.5 per 1,000 words, ours 1.0-1.1 (36 of 38 below the lowest real video) | KEEP |
| 5. Ask the viewer | Yes: real about 2.6-3.6 per 1,000 words, ours 0.4-1.4; the pivot "So, what can you do instead?" | KEEP |
| 6. Disgust | No evidence in style | DROP |
| 7. End every item on a win | Yes, as **the look** ("youthful", "taller") or a compliment from others; seen more than felt | ADAPT |
| 8. Reaffirm the title's feeling | Strongly: title words 13.9-16.7 per 1,000 words for winners, ours 8.2 | KEEP, plus the scanner check |
| 9. The villain all through | No: 11 of 21 real name none | DROP (optional, 3.5) |
| 10. The narrator's "I" verdict | Yes, but as **opinion** ("I think", "I love", "what I'd do"), never "I wore", "I bought", "my client" | ADAPT (ASK 11) |
| 11. Finish on relief | Yes, as **permission** in plain words. Faceless winners end on slogans, which are banned | ADAPT |

New rules the evidence adds:
1. **Permission in plain, specific words, never a slogan:** "You don't have to suffer to be stylish." Slogans ("no age limit", "you've earned it", "never too late") are in 17 of 24 faceless or AI videos and 0 of 21 real.
2. **The why is the relief:** one plain line on the mechanism (the eye, light, proportion, contrast) in every item.
3. **The blame moves off her once,** in fresh words, never the faceless formula "it's not you, it's the X" (12 of 24 faceless). It counts as the script's one reframe.
4. **The hard word, flagged:** "old lady" or "granny" only as the feared look, in quotes, announced ("harsh but true"), at most once. Viewers push back: "Waiting for the day when being old isn't an insult" (390 likes). (Suggestion 9, agreed; the scanner's existing `require-if` key can enforce the flag, tested.)
5. **Practical before feeling, with the over-70 lean:** comfort, the feet, balance, a stylist who can't cut fine hair.
6. **Your three feelings, lightly:** "frumpy" where the title has it; "invisible" sparingly; "losing her spark" as a picture, rarely.
7. **Targets** (floors, never quotas): "you" about 45 per 1,000 words; "but" about 5; questions 4-8 a script; "I" in ASK 11.

8. **Hair and fashion notes** (section 1): on hair titles the feeling is the fear of the change and the salon that didn't listen; on fashion titles it's the body, comfort and fit. One rule set; the examples and the item's feeling line follow the title's side.

### 3.8 Point then promise: ADAPT, smaller

KEEP point first, the priority flag, no recaps (recaps are a faceless habit: 12 of 24 against 2 of 21 real). DROP the money devices and the named forward promises. KEEP bridges that turn, the check she can run at home, the myth that names its belief, a second use for the same piece.

### 3.9 The video types: NEW table

All 38 of our titles mapped (library sweep §2.9):

| Pack type | Our titles | Study coverage |
|---|---:|---|
| Mistakes that age you (whole look, one item, hair) | 6 | The main engine: 279 breakouts, 27 at 500K+. Many models |
| Never these, wear these instead (item lists: glasses, necklaces, earrings) | 8 | **Thin:** no real presenter (searched, H7); F01 glasses, F02 earrings, F03 shoes for structure; M29 shoes |
| The best N (cuts, colors, pieces) | 11 | Good |
| You're styling it wrong: N secrets (technique) | 2 | Justin Hickox (M08, M12) |
| How to wear X | 2 | M30 scarves |
| Body-shape fixes (line and silhouette, never weight) | 3 | M17, M23, M24 |
| The rules she never breaks (the French rules; the woman who gets it right) | 2 | M28, F05; Diane's lens lives here |
| The why explainer ("Why your haircut never looks right") | 0 | M01; 18 breakouts, 17 real |
| Makeup | 4 | **Out:** the makeup pack later |

A gray-hair journey and a makeover need a real body or a real client, so they're not types for a persona; their topics run as a best-N list or an explainer. A title that fits none uses the closest type and is logged "new type" (KEEP).

### 3.10 The item shape: NEW

Real lists run 6-7 items of about 240 words each, but uneven: one item often carries the video. The proposed shape:
1. the look, in her own mirror or closet
2. why it ages or why it works, in one or two plain lines
3. the turn ("So what do you do instead?", rotated)
4. the swap, specific: a cut, a length, a color, a fabric, a brand as a benchmark where the brief gives one
5. the check she can run (the mirror, a phone photo, daylight at a window)
6. the result in look words, a compliment, or now and then how it feels

**About 180-300 words an item, longer when an item carries the video.** No more than two items without a bridge (KEEP).

### 3.11 Using the models: ADAPT

KEEP the never-copy rules and "a model where one fits, not every script". The library:
- **30 real presenters** (M01-M30): structure, voice and emotion. Justin Hickox (four models) gives structure and emotion, never voice samples. M05 (RaDona, a salon cut-along) gives voice and emotion only, for the over-70 client.
- **7 faceless** (F01-F06, F08): structure only, never voice or wording (your faceless section). F07 was dropped: mostly music.

Model files follow electrical's spec with its "Emotion voicing" section. Labels to add for style: `[TRY-ON: banned]`, `[CLIENT: banned]`, `[AGE SLOGAN: banned]`, `[SPONSOR]`.

### 3.12 CTAs and the ending: ADAPT, set in the profiles

- **Ours now:** the book pitched twice in all 38 (about 145 words mid-video, plus an end block), "subscribe", and "which one will you try first", which drew one answer in about 42 comments.
- **Real winners:** a mid-video CTA in 16 of 21; subscribe in 6 of 21; "I read every one" in 0 of 21 (faceless 8 of 24).
- **What gets answered:** a question about her. "Where are you watching from?" drew 24 answers in 29 comments.

The plan:
- the book once mid-video after the first real payoff (60-90 words) and one line at the end (ASK 8)
- then the comment ask about her (suggestion 7, agreed), rotated
- then the profile's short sign-off (ASK 6)
- never the long QR walkthrough ("point the camera at that square the way you would at a grandchild")

### 3.13 Length: ADAPT

Real median 11.9 minutes; faceless 15.6; ours 16.4 and 16.9. Words per minute from our voiceovers: Scarlet 169, Diane 172. Minimum 12 minutes (about 2,040 words), aim 12-16 (ASK 10). Never padded.

### 3.14 Voice, proof and money: ADAPT

**Voice:**
- KEEP "you" for instructions and "I" for opinions; plain over clever; candor; warmth; no jokes; no swearing.
- ADAPT: brands named where the brief gives them, as benchmarks or examples (real 13 of 21; ours 1 of 38).
- ADAPT: spoken forms (heights in words, "a size twelve", "H and M").
- NEW: no house vocabulary (3.16).

**Proof:**
- **Use:** the mechanism in one line; the check she runs; a tailor's or stylist's rule credited generally; the honest limit ("not every trend is for everyone").
- **Never:** "I tried, tested or wore"; try-on narration ("as you can see here"); clients; "I've worked with hundreds of women"; "studies show"; the persona's own age or face as proof.

**Money:** no price unless the title promises budget, cheap or "without spending" (your answer to suggestion 6). Then the price comes from the brief, as a range, once or twice a script. "Look expensive" is delivered through cut, fabric, fit and color, never a receipt. The ideation skill's brief spec asks for dollar figures, so the pack says the brief's prices are background unless the title is a budget title (ASK 12).

### 3.15 Safety: NEW, small and real

Defaults where the brief is silent; the brief can add safety, never remove it (electrical's rule):
1. **Hair dye:** the patch test before home color, every time; any scalp reaction is a stop and a doctor.
2. **Heat tools:** heat protectant and a lower setting on fine, thinning or gray hair.
3. **Thinning hair:** styling only; sudden shedding or patches are a doctor's question; nothing claimed to regrow hair.
4. **Shoes and falls:** viewers bring it ("we are more prone to tripping", 115 likes). Heel height, backless shoes and slick soles: the safe choice said plainly, never shamed.
5. **No diet, weight-loss, supplement or exercise plan:** "slimmer" means line and silhouette.
6. **Glasses:** the optician fits the lenses; the script gives frame advice only.

### 3.16 Banned list and scanner block: ADAPT

KEEP the intro, tease, recap, first-person test and customer-story bans and the 8-word copy guard. ADD, every line tested on our 38 and the 63 study transcripts (library sweep §3.3):

| Line | Ours (38) | Real (36) | Faceless (27) | Rule |
|---|---|---|---|---|
| "small gold hoops" | 24 videos | 0 | 0 | ban |
| "reads as" | 27 videos, 79 uses | 3 uses | 11 videos | ban |
| "from across the room" | 17 | 0 | 0 | ban |
| "book club", "gallery", "whenever it suits you" | 16, 20, 10 | 0 | 1-3 | ban |
| "quietly" | 22 over once | 0 | 7 | once |
| "Picture…" / "Imagine…" openers | 23 over once | 0 | 4 | once |
| age slogans ("no age limit", "you've earned it", "you deserve", "never too late") | 0 | 1 | 2-7 each | ban |
| "it's not you, it's the X" | (other words) | 0 | 5 | ban the formula |
| "old lady", "granny" | 0 | 2 over once | 2 | once, and a softener required |
| the old intro, sign-off, no-rush close and "I gathered 300" lines | 24-38 | 0 | 0 | ban (in the profiles) |
| our tease forms ("we'll get to those", "still ahead", "the one I promised") | 23 | 4 | 3 | ban |
| try-on and client claims ("I wore", "my client") | 2 | 6-8 | 2-4 | ban |
| ages ("I'm 62") | 0 | 4 | 2 | ban |
| "studies show", "regrow" | 1 | 1 each | 1-2 | ban |

Plus `min-minutes: 12`, `first-item-seconds: 45`, `example-guard: 5`, an `item-words` band, and once-lists for "camel", "quiet luxury" and "for generations".

### 3.17 Before handing over: ADAPT

The checklist's style lines: the title's promise word said early and at least twice; no intro or slogan; item one by about 45 seconds; a feeling in about a quarter of items; the why in every item; permission in plain words; "but", "you" and questions at the targets; the villain only if the title has one; no house vocabulary; prices only on budget titles; brands only from the brief; the hard word at most once, flagged; the French claims hedged (Diane); the safety defaults; the comment ask about her; the CTA per profile.

---

## 4. The reference material

| File | Verdict | What it takes |
|---|---|---|
| `models/` | **NEW:** 30 real (M01-M30) and 7 faceless (F01-F06, F08), all collected, with notes | Beat maps and labelled scripts in electrical's model format, an INDEX by pack type |
| `voice-samples.md` | **NEW**, real women only. Candidates: Tracy Campoli or Melissa Murrell for Scarlet; Marie-Anne Lecoeur for Diane; Woman in midlife, Diana GOSS in reserve | **Your listen first** (ASK 19): age, accent, register |
| `excerpts.md` | **NEW:** real lines grouped by job (hooks, the turn, the why, permission, the flagged hard word, comment asks about her) | From the 30 real models |
| Price guide | **None.** A price guide would feed the price habit the study says to drop | |
| A facts and safety guide | Not now: the six defaults in 3.15 and the brief (ASK 13) | |
| `unit-plan-template.md` | **ADAPT:** the style types; fields for the title's promise words, the feeling items, the opening device, the comment question | Small |

---

## 5. The two profiles

### 5.1 Three sources disagree

| | Notion channel page (team, edited 2026-09-20/21) | Ideation skill (yours) | Our 38 scripts |
|---|---|---|---|
| **Scarlet's age** | none, ever | 55-60 | none said |
| **Scarlet's credential** | "a curator … not a credentialed expert", "no count of years, no career" | "forty years" of dressing for boardrooms and galas, "fixed forever" | none; the knowledge is the tailors' "for generations" |
| **Diane's origin** | "never claims French birth, nationality, upbringing, or residence" | "French woman … Parisian by upbringing" | in between: never says she's French, but "the women I know in Paris" (7 times) |
| **Diane's age** | none | 55-65 | none |
| **Name** | "Scarlett Sterling", "Diane De Chambray" | "Scarlett Sterling"; the French persona "name TBC" | "Scarlet Sterling", "Diane" (the scripts won't say names now, S3) |
| **Sign-off** | "I'm Scarlett Sterling. Until next time, stay polished and stay sterling." / "Keep it simple, and let them wonder how you do it. À bientôt." | | Scarlet's line in 25 of 25; "À bientôt" closes 12 of 13 |

Your answer to suggestion 4 ("a first-person voice and one soft credential", with my examples "40 years of dressing for…" and "the way I was raised in Paris") sides with the ideation skill. Notion's pages are stricter and match the claims policy. That's ASK 3 and 4.

### 5.2 Scarlet Starling: the draft profile

| Field | Draft | Status |
|---|---|---|
| Status | pending until a test passes | NEW |
| Pack | the hair-and-fashion pack (`style-scripts`) | ASK 1 |
| Script type | Talking Head (Notion; QR code in our scripts) | ASK 2 |
| Words per minute | 169 (25 voiceovers) | NEW |
| Name | never spoken; the profile bans "Scarlet/Scarlett" and "Sterling/Starling" (but "sterling silver" stays allowed) | NEW |
| Who she is | a poised, warm curator of timeless style, talking to one woman over 60 like a friend with impeccable taste. "Her authority is taste, not money." No age, career, relatives or checkable facts | KEEP (Notion, ideation) |
| Soft credential | one fixed line, numberless (recommended) or "40 years" | ASK 3 |
| Personal details (one per script at most) | e.g. the camel coat on the hook by the front door; her berry lip | ASK 20 |
| Enemy | optional: the advice she was handed, fast fashion and the trend cycle, the counter's upsell, the salon default | KEEP (ideation) |
| Book | *300 Budget-Friendly Ways to Look Expensive* (digital download; 300 Ways, 28 chapters, six parts each). Never a price, "anti-aging" or "look younger" | KEEP (Notion); the text is needed (ASK 8) |
| Mid CTA | once, after the first real payoff, 60-90 words, no "I gathered 300 of them", no "nothing about it expires" | ASK 8 |
| Ending | one-line book reminder, the comment ask about her, a short sign-off | ASK 6-7 |
| Hard no's | never shame the woman; no diet or weight-loss; no medical or "reverse aging"; no celebrity as a friend; no age slogans; no face-as-proof; wealth never counted | KEEP (ideation rules 1-7) |

### 5.3 Diane de Chambray: the draft profile

| Field | Draft | Status |
|---|---|---|
| Status, pack, script type | as Scarlet's | ASK 1-2 |
| Words per minute | 172 (13 voiceovers) | NEW |
| Voice | "Sylvie" (ElevenLabs ID in Notion) | KEEP |
| Name | never spoken; bans "Diane" and "de Chambray" ("a chambray shirt" stays allowed) | NEW |
| Who she is | a chic, candid friend who shows women over 60 how French women get dressed and how to borrow it; blunt about clothes, warm about the woman | KEEP (Notion) |
| Origin and credential | ASK 4: Notion's "never French", one approved heritage line ("the way I was raised in Paris", as Werner's), or acquaintance only ("the women I know in Paris") | ASK 4 |
| Personal details | mind-change lines ("I used to think…, and I changed my mind") | ASK 20 |
| Enemy | excess as a habit: the overstuffed closet, logos, the trend cycle, over-styled hair, the shop counter. "American women" only as a collective habit, in the third person, never the viewer | KEEP (ideation) |
| Book | *The French Way* (389 pages, ten chapters, numbered Secrets). Never "101" until it's confirmed, never "20 years younger" (the subtitle contradicts the book), never makeup lessons | KEEP (Notion); the text is needed (ASK 8) |
| French words | one or two a script (chic, voilà), never sentences, never a written accent | ASK 18 |

**The French lens** (her profile, as Werner's "German way"):
1. Every French claim comes from the brief, hedged as people talk ("most French women", "in Paris it's usual"). Never "every", "never" or "all" about French women outside the locked title. Ours hedge 8% of 209 French claims.
2. The French practice is the reason; the viewer's own closet is the fix, with American sizes, shops and seasons. French Fashion's 449K video drew climate pushback: "This might work in France, but in the US we get some serious winters."
3. No invented laws, sayings, statistics or customs: "Half of them skip black in daylight altogether" and the christening medal go unless the brief sources them.
4. A topic with no documented French practice isn't invented; it's flagged back (the ideation's own rule).
5. The risk is real: Marie-Anne Lecoeur, a French stylist, made "AI Gets French Style WRONG!" (138K). The safe ground is the documented staples (trench, Breton top, navy blazer, dark straight jeans, fewer better pieces, air-dried hair, gray worn on purpose).

---

## 6. Wiring

- `core/channels.md`: **row 10 Scarlet Starling, row 11 Diane de Chambray**, `style-scripts`, pending until a test passes.
- `tools/build_skills.py`: the description (about 834 of 1,024 characters), the skills table, a style scanner command (no price guide), `PERSONAS`, `PACKS`, `INSTALL` (three more skills).
- `tests/run_checks.py`: style twins of the pack, scanner-block, copy-guard, profile and channel-row checks, numbered **from 73**; checks 1b and 2 extended to the style pack. (Check 2 flags the phrase "house rules", so the pack says "house vocabulary".)
- `PROPOSALS.md`: **P20** for the core scanner changes.
- `README.md` and `personas/README.md`: the file map.

---

## 7. What's already true

- **Models:** 37 collected with notes, checked (every quote found in its source).
- **Words per minute:** 169 and 172, from our 38 voiceovers.
- **The ban lines:** tested on 101 transcripts (library sweep §3.3).

---

## 8. Proposed order of work

1. **Your answers** to section 9.
2. **The core scanner changes** (P20), each with a test: title words, style signposts, style tenure words, the channel-intro ban, the accents choice, the build-script fix.
3. **The pack** (`style-scripts/`), section by section as in section 3, with every example line new.
4. **The model files** (30 real, 7 faceless) and the INDEX, the excerpts; the voice samples after your listen.
5. **The two profiles**, once ASK 3-8 are answered and the book texts are pasted.
6. **Wiring**, checks, README.
7. **Tests:** writer, VA and judge kept apart, like for like against a real video on the same title. Suggested: Scarlet's necklaces title (our best, 39,935 views) against F01-F02's structure; one hair title against Justin Hickox; one Diane title against Marie-Anne Lecoeur.

---

## 9. Questions for the operator

Each has a recommendation. "Yes to all recommended" is a fine answer; change any by number.

**The pack**

0. **Hair and fashion, one pack:** one emotion section, with a short hair note (the fear of the change; the salon that didn't listen) and a short fashion note (the body, comfort, fit; the hard words), as section 1 found. *Recommended.*
1. **Its name:** `style-scripts` (matches `style-ideation`; the makeup pack later as `makeup-scripts`). *Recommended.*
2. **Script type for both:** Talking Head (Notion says so; the QR code and markers are already used). *Recommended.*

**Who they are**

3. **Scarlet's soft credential:**
   - (a) one numberless line, fixed, e.g. "a lifetime of dressing well" *(recommended: it matches Notion and the claims policy, and implies no age)*
   - (b) "forty years of dressing for…", fixed on the profile's tenure line (the ideation skill's; it implies her age)
4. **Diane's origin:**
   - (a) Notion's: she never claims to be French; she admires and passes on the French way
   - (b) one approved heritage line, fixed, e.g. "the way I was raised in Paris" (as Werner's German background, P14; your yes to suggestion 4 used this example) *(recommended)*
   - (c) acquaintance only: "the women I know in Paris"
5. **Ages and "we":** neither says her age, ever, and neither speaks as "one of us" ("so many of us", "women our age"), which implies her age. *Recommended.*
6. **Sign-offs** (the name can't be said):
   - Scarlet: "Until next time, stay polished." (the old line without the name and the pun)
   - Diane: "Keep it simple, and let them wonder how you do it."
   - *Recommended*, or none (end on the comment ask, as plumbing)
7. **The comment ask and "I read every one":** a question about her, rotated: her age and where she's watching from; a piece she's kept twenty years; the rule she was handed at 50. No "I read every one" (0 of 21 real presenters say it; it's a faceless habit here). *Recommended.*
8. **The book CTA and the book texts:**
   - once mid-video after the first real payoff, 60-90 words, and one line at the end *(recommended)*
   - **please paste both books' contents** (the chapters and the numbered Ways or Secrets) for the book check, and confirm whether *The French Way* really has 101 Secrets
9. **The subscribe line:** one short line at the end, without the channel's name. *Recommended.*

**The scripts**

10. **Length:** at least 12 minutes, aim 12-16. *Recommended.*
11. **"I" (opinions only):** a guide of about 10 per 1,000 words, reported, never a fail (real women run 23 because they wear it; a persona can't honestly). *Recommended.*
12. **Prices:** only on budget titles (your answer); the pack treats any other price in the brief as background. *Recommended.* (The ideation skill's brief spec asks for dollar figures; changing that is your skill, later.)
13. **Safety:** the six defaults in 3.15 in the pack, no researched facts guide for now. *Recommended.*
14. **Brands:** named only as benchmarks and good examples, never an opinion against a named brand. *Recommended.*
15. **Dated facts on trend titles** ("Fall 2026"): no special rule, as HVAC. *Recommended.*
16. **Forward promises:** plumbing's named-promise override doesn't carry to style (real videos hold nothing for the end). *Recommended.*

**The scanner and wiring**

17. **Core scanner changes (P20), every channel, each with a test:** the title-word check (your suggestion 2), style item signposts, style tenure words, the channel-intro ban in the core list; and the one-line fix to the build script's unclosed code block. This chat does them. *Recommended.*
18. **French words:** written without accents ("voila", "cherie", "a bientot"), one or two a script, after a quick voice check. *Recommended.* (The other way is a scanner key for allowed accented letters.)

**Yours to do (nobody else can)**

19. **Voice samples:** a listen to Tracy Campoli and Melissa Murrell (for Scarlet) and Marie-Anne Lecoeur (for Diane), with your pick. Links in `studies/style/comparison/04-models-and-voice.md` §5.
20. **Personal details** (one per script at most): Scarlet's camel coat by the front door and her berry lip; Diane's "I changed my mind" lines. *Recommended*, or name others.
21. **Salon titles:** when a title blames the salon, the script keeps it as tone (the rushed default, never the stylist as a person) and doesn't take it back. *Recommended.*
22. **Notion and the ideation skill:** once 3-6 are decided, the two Notion pages and the ideation skill will disagree with the profiles. Want a list of the lines to change? (Notion and your skills stay read-only for me.)
