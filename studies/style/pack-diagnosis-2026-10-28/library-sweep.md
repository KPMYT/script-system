# Library sweep for the style pack diagnosis (helper A notes, 2026-10-28)

Notes for the main session's style pack diagnosis draft (hair and fashion, one pack for now; Scarlet Starling and Diane de Chambray). Written in the shape of `drafts/hvac-pack-diagnosis-DRAFT.md`. **Nothing in the library was changed.** Every number below carries its source; where a figure is mine (a scratch run), it says so. Scratch scripts and the plain-text transcripts are in `/tmp/claude-0/-home-user-script-system/1606fe5d-4351-58e1-8e5d-ec273208b30e/scratchpad/sweepA/` (not in the repository).

**Read:** `HANDOFF.md` §3 (all blocks; the three 2026-10-28 style blocks in full), `PROPOSALS.md` P18, `plumbing-scripts/SKILL.md` (whole), `hvac-scripts/SKILL.md` and `electrical-scripts/SKILL.md` (overrides, inputs, emotion, types, item shapes, CTAs, length, voice, scanner blocks), the three `model-file-spec.md` files and `references/` lists, every `core/*.md`, `core/script-scanner.py` (whole), `core/channels.md`, `tools/build_skills.py`, `tests/run_checks.py`, the style `comparison/` files README, 00, 01 (sections 1-5), 02, 03, 04, 06, 07, `round2/BREAKOUT-MAP.md` (top tables), `own-baseline-2026-10/SUMMARY.md`, `models/approved-models.csv`, and, for context only, the installed `style-ideation` skill on the account (`/root/.claude/skills/synced/.../style-ideation/`), which is not in this repository.

**Status key** (as the HVAC draft): **KEEP** copy as it is (new example lines only); **ADAPT** same rule, style content; **NEW** style needs something plumbing hasn't got; **ASK** the operator's call (numbered in §5). **DROP** = a plumbing-only override the style evidence doesn't support (the core default stands).

---

## 0. The short answer

Style is the furthest niche from plumbing so far. The audience is older (median 70, `01` §1), the pain is practical more than emotional (`07` A1), there is often no villain (real presenters name none in 11 of 21, `03` §4), there's almost no money in the winners' scripts (money figures in 5 of 45 study videos, `02` §5), and the persona can't do what makes the real presenters work (wear it, try it, show a client). So the plumbing pack's **structure** carries over (inputs, overrides table shape, opening jobs, item shape idea, the ending, models never copied, banned list, scanner block, checklist), but most of its **content** is rewritten, and its emotion section is rebuilt from `03` and `07` (operator: "not copied from plumbing").

| Part | Verdict | Size of the job |
|---|---|---|
| Core rules and the script-writer | **KEEP**, nothing in the core stops a style channel. Two core questions: accented letters (French words fail the scanner) and the scanner's style blind spots (tenure words, signposts, no title-word key) | Small rule-wise; medium in the scanner (ASK) |
| Plumbing pack rules | About 35% KEEP, 45% ADAPT, 20% NEW or DROP | Large: a real rewrite |
| References | Structure KEEP; content all new: 30 real models (M01-M30) and 8 faceless structure-only (F01-F08), voice samples from women, excerpts; **no price guide** | Large |
| Two profiles | New; four decisions (credential shape, Diane's identity, book, script type) | Medium |
| Wiring | Rows 10 and 11, build entries, checks from 73 (or 80), P19 | Small |

---

## 1. The core and the script-writer

The core names no niche except in examples; the humanizer already draws examples from "style" (`core/humanizer.md`, intro). **No core rule has to change for a style channel to run.** What follows is every place style touches it.

| Where | Now | Style needs | Verdict |
|---|---|---|---|
| `workflow.md` §2, inputs and the gate | Default title, brief, research pack, rotation log; a pack may mark the research pack `not used` | Title, brief, rotation log; research pack `not used` (as plumbing, HVAC, electrical). The ideation briefs are "facts only", one paragraph, and must carry "real dollar figures" (installed `ideation-core/references/rules-and-specs.md` §4): that is where our 34-of-38 price habit comes from (`02` §5) | KEEP the gate; the pack's `inputs` block ADAPT |
| `workflow.md` §2, "just write it" | Refused | Same | KEEP |
| `research-and-sourcing.md` §7, freshness | Each pack lists its live facts | Trend and season titles ("Fall 2026", "trends 2026"; 104 trend/season breakouts, `BREAKOUT-MAP.md`) carry dated claims; brand lines and prices change. HVAC's operator said "no dated-facts rule" (HANDOFF 2026-10-27) | ASK 14 (default: none, as HVAC) |
| `voice-anchoring.md`, "no samples, no script" | 2-3 verbatim clips of human narration in the pack | From real women only (HANDOFF 2026-10-28, "Voice samples stay with real women"). Candidates: Marie-Anne Lecoeur, Tracy Campoli, Woman in midlife, Melissa Murrell, Diana GOSS, reserve Kelly Snider (`04` §5). "Nothing was listened to" (`04`, limits) | KEEP the rule; NEW content |
| `voice-anchoring.md`, the four tells | Wise Narrator, Staccato, Reading-not-speaking | Our scripts are full of the Wise Narrator: "A brooch is bought, a rosette is made"; "Chic was never the receipt. It's the choosing." (`06` §15, `03` §1.8). The F/AI slogans ("Elegance is never an accident") are H10 poster quotes | KEEP (the core already catches the shape; the pack names style examples) |
| `claims-policy.md`, "never allowed" | Ages, named relatives, years of experience (except `tenure:`), credentials, places, having "made, sold, tested, built, lived or collected", customers | The real presenters' "I" (23.4 per 1,000, `02` §1) comes mostly from wearing it, trying it and their clients; a persona can't. Our own scripts already slip: "I tried that look once and spent most of a dinner…" (Diane `41ezk-kRd7Y`), "any single piece of jewelry I own" (Scarlet `w6w_ktMBHXM`) (my grep). Suggestion 4 ("one soft credential") fits the existing exceptions only as a `tenure:` figure (Scarlet's "forty years of dressing for…") or the "one approved heritage line" (Diane's "raised in Paris", P14) | KEEP; the credential's shape is ASK 3; Diane's identity ASK 4 |
| `claims-policy.md`, ages | Never | Real women rarely say their age (2 of 16, `04` §6a); F/AI personas do ("I'm over 60 myself", `03` §3.2). The in-group "we" ("so many of us", "nearly all of us": 15 of our 38, `06` §15) implies the persona's age | KEEP the ban; the "we" in-group is ASK 5 |
| `claims-policy.md`, health | No health, efficacy, treatment or prevention claims | Hair thinning, gray hair, scalp, "anti-aging", menopause are next door. The ideation skill already bans diet, weight-loss, medical and procedure content and keeps thinning a styling topic (installed `style-ideation/SKILL.md` §3 rules 2-3). Viewers bring illness: chemo or cancer 5, feet or balance 6 (`01` §1) | KEEP; the pack names the style cases |
| `claims-policy.md`, guarantees | None | "INSTANTLY Younger", "Take 10 YEARS Off" titles (14 and 11 of our titles, my count from `meta.md`). The title wins, the script can't guarantee | KEEP; copy electrical's "the title's promise, word by word" paragraph (ADAPT) |
| `claims-policy.md`, named companies | Neutral mentions fine; nothing false as fact | Brands as benchmarks (operator's "yes" to suggestion 6); real presenters name brands in 13 of 21 (`02` §5) | KEEP |
| `offer-rules.md` | "The book", price-silent, no invented backstory, §5 scoped to offers (P13) | Both channels sell a book ("300 budget-friendly ways to look expensive"; "The French Way, 389 pages", `06` §11); Diane's book "carries invented women (Marie, Sophie and Claudette)" (`04` §6c), which, like Werner's book stories, never go in a script | KEEP; book text needed for the book match (ASK 7) |
| `retention-mechanics.md` §2, no greeting or channel intro (locked) | Banned by default | Supported: 31 of 42 winners introduce no one (`README` finding 15); ours do in 38 of 38 | KEEP |
| `retention-mechanics.md` §6 and `humanizer.md`, teases (locked) | Hard-banned; rehooks short-range only | Supported: real hooks tease in 1 of 21; F/AI 12 of 24; ours 28 of 38 by reading (`02` §2.3, `README` finding 16). The plumbing pack's P3 override (named forward promises in the body) has no style evidence behind it: real videos hold nothing for the end (1 of 21, `04` §3a) | KEEP the core; **DROP** P3 for style (ASK 11 to confirm) |
| `retention-mechanics.md` §2, value line | Optional, one video in three | Real hooks carry a promise of N items in 10 of 21 (`02` §2.3); plumbing replaced the value line with the count line | ADAPT (as plumbing: count line, no value line) |
| `retention-mechanics.md` §2, the hook's three jobs | Transformation, pain or wish, curiosity | Transformation = the look the title promises; pain = the feared look or the practical problem; curiosity = the why (relief at an explanation: "now I understand why" 18 comments on real videos, 0 on faceless, `01` §2) | ADAPT |
| `humanizer.md` H12a ("quietly") | Judgment, fix on sight | "quietly" 74 times in 32 of 38 ours, 20 in 6 faceless, 0 real (`04` §3d). HVAC limits it to once (`hvac-scripts` scanner block) | KEEP; the pack adds a scanner line (§3) |
| `humanizer.md` H21 (one reframe) | At most one | "It's not you, it's the blouse" is the F/AI formula, 12 of 24 (`03` §2.1). Two of our titles are reframes ("It's NOT Your Weight, It's These 5 Things"): saying the title's reframe uses the one | KEEP |
| `humanizer.md` H20 ("Most people…") | Once | The scanner already counts "Most women" (`MOST_OPENER`) | KEEP |
| `cta-and-endings.md` §4, the closing line | One sentence, the sign-off or a next action | Plumbing's P5 ending (comment ask last, no sign-off) or the core's sign-off? Ours end on fixed sign-offs (25 of 25 Scarlet, 12 of 13 Diane, `06` §11) | ASK 9 |
| `cta-and-endings.md` §5, banned echoes | Includes "open your camera, the same one you use to take pictures" | Our QR lesson ("point the camera at that square the way you would at a grandchild", `03` §7) is the same family; QR code named in 38 of 38 ours, 8 of 42 winners (`06` §5) | KEEP; pack bans the long QR walkthrough (as plumbing) |
| `variety-rotation.md` | Nine slots, the rotation log | Fine; the pack adds fields (model, type, comment question; plus the opening scene device) | KEEP + ADAPT fields |
| `workflow.md` §4, written for the voice | Units, symbols, fractions, two-way words | Style trips: heights ("5'2"" fails, good), brand names with "&" (H&M, M&S fail as symbols: write "H and M", "Marks and Spencer"), French accents fail as non-standard characters ("Chérie", "Voilà", "À bientôt": 21 hits in 9 of our 38, my scan, §3) | KEEP; accents are ASK 13 (a core scanner question) |
| `workflow.md` §3, the 8-minute minimum | A pack may raise it | Real median 11.9 min; faceless 15.6; ours 16.4 and 16.9, all 12:30 or longer (`02` §1) | ASK 8 |
| `greenlight-audit.md` E1 (sources) | 7 signals, pass at 5 | Style needs no named sources; "studies show" is a faceless habit (15 times in 6 faceless videos, once real, `04` §3b) | ADAPT (plumbing's out of 6, pass at 4) |
| `greenlight-audit.md` A2 (graded against real hooks) | Needs the pack's excerpts | Real women's hooks (`02` §2.2 quotes them) | KEEP; NEW excerpts |
| `greenlight-audit.md` evidence "Title word" line | Quoted by the writer | Suggestion 2 asks a scanner check; none exists (§3.5) | KEEP + NEW key (ASK 12) |
| `script-scanner.py` | See §3 | Tenure words, signposts, accents and the title-word count are style gaps | ASK 12 |

**Bottom line for §1:** the locked bans (intro, teases, "right here", the hard-ban list) are exactly what the style evidence asks for. Suggestion 1 ("write every style script through the library") removes our self-introduction and most teases by itself.

---

## 2. The plumbing pack, section by section

In `plumbing-scripts/SKILL.md` order. HVAC and electrical are cited where they already solved a style problem.

### 2.1 What it covers, authority, files — KEEP structure, ADAPT the description

The description must name style triggers (haircut, bob, pixie, gray hair, fine hair, outfit, wardrobe, colours, glasses, necklaces, earrings, scarf, body shape, "look younger", "look expensive", frumpy, French way) and say **no makeup** (operator, 2026-10-28: "for now hair and fashion will be one pack"), so a lipstick title doesn't load it. Files table: unit plan, voice samples, excerpts, models INDEX and files. **No price guide** (§2.14). Possibly a short facts-and-safety guide (ASK 10).

### 2.2 The overrides table

| Plumbing row | Style plan | Evidence |
|---|---|---|
| Inputs: title, brief, rotation log; research pack `not used` | KEEP | Briefs are the fact source; style facts are few and mostly opinion |
| P3/P10 named forward promises in the body | **DROP** (core short-range rehooks stand) | Real hooks hold nothing: 1 of 21 (`04` §3a); ours hold or tease in 12 of 14 noted |
| P5 ending (end CTA, then comment ask last) | KEEP or core sign-off: **ASK 9** | Ours: fixed sign-offs in 37 of 38 (`06` §11) |
| 12-minute minimum | ASK 8 (12 is defensible: 21 of 24 faceless and 25+13 ours run 12+, `02` §1) | Real median 11.9 |
| Rotation-log fields | ADAPT: `model`, `type`, `opening device` (scene, question, verdict…), `comment` | Our "Picture…" opener in 36 of 38 (`06` gap 5) is exactly what rotation exists to stop |
| Copy guard over SKILL.md, excerpts, voice samples, models, profile | KEEP; add `example-guard: 5` (electrical) | Our house vocabulary is a copy-guard problem in slow motion |
| Mid-video CTA a third in, never before item 3 | ADAPT per profile (ASK 7) | Style lists run a median of 6.5-7 items (`02` §3.2): "never before item 3" in a 5-item list is 60% in |
| No sources; originality out of 6, pass at 4 | KEEP | Sources aren't how style earns trust |
| Signposts ("Number four.") | ADAPT: numbered or "the next…" sentence | Real lists lean on "the next…" sentences (9 of 16); faceless number (14 of 24); Diane numbers all 13 (`02` §3.2). The scanner only finds "Number N." (§3.4) |
| D4: brief plus price guide; general knowledge marked | ADAPT: brief only; general styling knowledge marked | No price guide |
| Contractions kept | KEEP | Real speech |
| The opening checked as the hook's three jobs | KEEP | §1 |
| No value line | KEEP | Count line instead |
| Cents exceptions (cost per use; three prices side by side) | **DROP** | Prices only on budget titles (§2.14) |
| NEW rows | Prices said only on budget titles (overrides H22's "one price per item" sense); `first-item-seconds: 45`; `item-words` band | §2.8, §2.14 |

### 2.3 Inputs — KEEP, with one ADAPT

KEEP title, brief, rotation log, research pack `not used`, the fill-in rule shape. ADAPT P7: where the brief is silent, the script may fill in **well-established styling knowledge** (proportion, contrast, the neckline and the necklace, the rise of a jean), marked "general knowledge"; **never** prices (none unless the title is a budget title and the brief gives them), never product availability, never a health, scalp or dye-chemistry fact beyond the brief and the safe defaults. **Is there a "price guide" equivalent?** No: real presenters say prices in 5 of 21, faceless in 4 of 24 (`03` §9), so a price guide would feed the habit the study says to drop. **A brand or benchmark list?** Possibly later, but brands change and the brief should carry them (the plumbing rule "name a product only when the brief confirms it's on sale now" carries over). No NOT READY on missing prices; NOT READY only when the brief can't carry the title's promise.

### 2.4 The viewer — ADAPT, heavily (from `01` and `07`)

Replace plumbing's homeowner with:
- **Age:** median 70 of 149 who give one; 51% are 70+, 32% in their 60s, 10% in their 50s (`01` §1). The operator: "leaning into the over 70 crowd" (HANDOFF 2026-10-28); one emotion set with a light over-70 lean: comfort, mobility, the older client (S4, approved 2026-10-28).
- **Practical problems first:** no stylist who can cut 28; no clothes that fit 28; a changed body 18; health or mobility 22 (`01` §2). Top-liked: "it's nearly impossible to find stylists that can actually cut a bob" [1K].
- **They want the why:** "now I understand why" 23 comments (18 real, 0 faceless) (`01` §2). Explanation is the relief.
- **They want brands and where to buy:** 30 of ~117 requests (`01` §4), top "tell us the brands that make pants that fit" [246].
- **They want their body shown:** bigger bodies and tummies 23 requests; models too slim 78 complaints (8.7% of faceless comments, `01` §5). The script can't choose pictures, but it can name the body ("a fuller middle", "a softer jawline") and never assume a slim one.
- **They push back on rules:** "I'll wear what I want" 55 comments; disputed advice 62 (tucking 10, bare arms 9, the French winter list's climate 8) (`01` §5). Give the reason and the out ("If you love it, keep it").
- **They're proud:** a style kept for decades 33; pride in age 14 (`01` §2).
- **Terms explained the first time** (NEW list): undertone, contrast, silhouette, proportion, rise, drape, structured, capsule, balayage, lowlights, blending, demarcation line, toner, gloss, face-framing layers, blunt cut, curtain bangs, lob, root lift, diffuser, heat protectant, ponte, A-line, midi.
- **The standard kit:** a full-length mirror, a phone camera, a closet, a hairdryer and round brush. Anything else (a steamer, a diffuser, a silk scarf) is named with what it does.

### 2.5 The villain — ADAPT to **optional** (as electrical)

Evidence (`03` §4, videos): real presenters name **no adversary in 11 of 21**; F/AI cast a system with a motive (industry 5, trends and influencers 8, received advice 11); ours blame "the advice we were handed" (Scarlet 5, Diane 7) and, on Diane, the shop counter (7). Salons as the problem: real 2, F/AI 3, ours 1+1, **both withdrawn in speech, and both titles sit below normal** (0.74 and 0.25). Younger women: real 1, F/AI 3. The past self: real 1, F/AI 5, Scarlet 4, Diane 2.

Plan: the villain is optional ("only where the title carries it"). Allowed targets, aimed at the habit and the default, never a motive: **received advice** ("somewhere along the way plum got filed under too much"), **the shop's default** (sizing, the sales rack, makers who don't cut for her body: 28 + 14 viewer complaints, `07` A1), **the rushed salon default** ("a lot of salons have a default for women past 60, short and set": a fact, never "they want you back every four weeks"), **trends** (lightly), **the dated version of herself** (gently). **Never**: younger women or other women (ideation rule 1, "never shame the woman… or other women"), stylists as people, "the fashion industry doesn't want you to know" (a motive). **A title that promises a villain** ("Hairdressers Won't Suggest Them") is paid as a fact, never withdrawn in the first 80 seconds as ours did. Plumbing's "two facts side by side, never joined by so/since/because" carries over (KEEP).

### 2.6 The opening — ADAPT

Evidence: real hooks median **172 words / 57 s** recounted to the first word of item one (`02` §2.1), or **about 90 words** over 19 scripted hooks with the first item at **0:45** (`04` §3a); item one inside a minute in 11 of 21 real, 3 of 25 Scarlet (`02` §2.1). Moves per hook: median **2** real, 5 faceless, 5-6 ours (`02` §2.3). Age line in 3 of 21 real hooks, 20 of 24 faceless, 38 of 38 ours. The title's count in the first 20 s: 12 of 28 winners, 5 of 38 ours (`06` gap 4). The title's promise word: "instantly" in 14 of our titles, said in none of those videos (`02` §6; my recount agrees: the strict word "instantly" is said in 0 of the 14, "instant" once in 3).

Plan: KEEP plumbing's jobs 1, 2, 4, 5, 6 with style content: (1) **the point and the title's promise word in the first sentence or two**, in the title's own words ("younger", "expensive", "instantly") (suggestion 2, approved); (2) a question when it fits, about her own mirror or closet; (3) the villain line **only if the title carries one**; (4) reassurance or scope in one line (body-shape titles open on it: "it doesn't mean there is something wrong with your figure", Diana GOSS, `03` §2.1); (5) the count line; (6) item one by about **45 s** (`first-item-seconds: 45`). At most two or three moves. **Never**: a name or channel intro, "this channel is for women over 60" (ours, 17 videos, `06` §15), an age slogan, the age as a refrain (say it where the title says it, suggestion 10), a tease or held item, a "Picture…" scene as the default opener (36 of 38 ours vs 15 of 42 winners, `06` gap 5), a task before item one ("Go and get the pair you wear most": 7 of ours, 0 study, `02` §2.3). Credential: once at most, where it does a job (8 of 21 real hooks carry one, `02` §2.3), in the profile's words (ASK 3). Plumbing's escalation line (P17) is an option there; style has fewer escalating topics (KEEP as option, low use).

### 2.7 Emotion — **NEW section, built from `03` and `07` only**

The operator: "practical solutions to emotional problems"; "the emotion rules are built from this niche's winners and comments, not copied from plumbing" (HANDOFF 2026-10-28). The operator's three feelings are weak in what viewers write: frumpy 25, losing her spark 17, invisible 6 (1 a complaint), "unheard" 0 as a word; **permission and rebellion 113 (10,346 likes) and relief at being understood 46** lead (`07` A1).

Plumbing's 11 rules against the style evidence:

| Plumbing rule | Style evidence | Verdict |
|---|---|---|
| 1. Put the viewer in it (scene, what she sees) | Supported, but through **her own** mirror, photo, closet, salon chair, fitting room: the winners' judgement comes from her mirror, body or age; ours from an imagined stranger ("the woman at the next table") and staged scenes (`06` gap 8; "Picture a gallery afternoon" 7 videos) | ADAPT |
| 2. One real pain per item | **Contradicted in frequency.** Real presenters name an inner feeling in **31 of 115 items (27%)**; the rest in look words (64% of items), `07` A2. Ours 1 in 11 | REPLACE: a feeling in about a quarter of items, one sentence (median about 12 words, 4-29), before the fix more often (24 items) than after (15) |
| 3. Strong, plain words | Supported, aimed at the garment: "old lady" 10 times (Marie-Anne), "frumpy" 4 real videos, "mumsy", "stuffed sausage" (`03` §2.2). Real say "tummy"/"belly" (4 videos); ours "the middle" | ADAPT (garment-aimed; ideation bans "fat", "ugly", "mutton dressed as lamb") |
| 4. "But", much more | Supported: real 6.5 per 1,000, faceless 4.8, ours 1.0-1.1; 36 of our 38 below the lowest real video (2.9) (`02` §1) | KEEP (target about 5+) |
| 5. Ask the viewer | Supported: questions 2.6 per 1,000 real (hand-adjusted median), 0.4-1.4 ours; the item pivot "So, what can you do instead?" (Marie-Anne ×6) | KEEP |
| 6. Disgust where the topic has it | No style evidence | DROP; replace with the flagged hard word (below) |
| 7. End every item on a win | Supported as **the look result** ("youthful", "10 lb thinner") and the compliment from others (chains 13, 17 in `07` A2); "the result is more often seen than felt" | ADAPT |
| 8. Reaffirm the title's feeling | Strongly supported: title keywords 16.7 per 1,000 real, Scarlet 8.2 (`02` §6); "younger" said in 3 of our 8 "younger" titles (`06` gap 4) | KEEP + scanner key (ASK 12) |
| 9. The villain all through | Contradicted: 11 of 21 real name none | DROP (optional, §2.5) |
| 10. The narrator's "I" verdict | Supported: "I" 23.4 per 1,000 real; "I think" 30 times, "I love" 23 (`04` §3c); the presenter's own feeling in 10 of 21 real videos (`07` A2). The persona can't claim a body or a try-on, so "I" = opinion, preference, "what I'd do", "my rule" | ADAPT (ASK 6 on the target) |
| 11. Finish on relief | Supported as **permission**; F/AI end on slogans (5 of 7 winners, `03` §8.4), which are banned | ADAPT |

New rules the style evidence adds:
- **Permission, in plain specific words, never as a slogan.** Real: "You don't have to suffer to be stylish" (`03` §1.6). Slogans (no age limit, never too late, you've earned it, you deserve) are in 17 of 24 F/AI, 0 of 21 real, 0 of 38 ours (`03` short version 1).
- **The why is the relief.** The mechanism line (the eye, light, proportion, contrast) is what viewers thank (§2.4).
- **The blame moves off her, once, in fresh words.** Real say it 4 times in other words; the F/AI formula "it's not you, it's the X" 12 of 24 (`03` §2.1). It counts as the one H21 reframe.
- **The hard word, flagged.** "Old lady" or "granny" only as the feared look, in quotes, announced ("harsh but true", "tough love"), at most once (suggestion 9, yes). Viewers reject it: "Waiting for the day when being old isn't an insult" [390] (`01` §5). Our softeners sit in the same sentence; the winners' sit before or right after (`03` §2.3).
- **Practical before feeling, and the over-70 lean:** comfort, the feet, balance, a stylist who can't cut fine hair (S4).
- **The operator's feelings, lightly:** "frumpy" yes where the title has it; "invisible" sparingly (suggestion 11); "losing her spark" as a picture, rarely.
- **Measured targets** (floors, never quotas, electrical's style): "you" about 45 (real 48.9, faceless 46.5); "but" about 5; questions 4-8 a script; "I" ASK 6 (real 23.4 can't be reached honestly; the faceless winners run 6.8-8.1).

### 2.8 Point then promise; ways to promise more value — ADAPT, shrink

KEEP point first, the priority flag, no recaps (recaps are an F/AI habit: 12 of 24 vs 2 of 21 real, `02` §6). DROP the plumbing devices that need money (trade's price, running tally, cost per use) and P3's named forward items. KEEP bridges that turn ("the next" is a real bridge: 0.70 per 1,000 real, Scarlet 0.30, `02` §3.3), the check she can run at home, the myth flag that names its belief, and a second use for the same piece.

### 2.9 The video types — NEW table (12 study types and our 38 mapped)

From `04` §1 and §2.13 (our 38 mapped there; my tally of that table below).

| Pack type (proposed) | Study types | Our titles in it | Status |
|---|---|---:|---|
| **Mistakes that age you** (whole look or one item; hair mistakes) | T1, T2, T6's mistakes variant | 6: S frumpy, S 10 outfit mistakes, S jeans mistake (T2/T8), S 7 hair mistakes (T6/T7), D frumpy rules, D American mistakes | NEW; the main engine: 279 breakouts, 27 at 500K+ (`BREAKOUT-MAP.md`) |
| **Never these, wear these instead** (item list) | T3 | 8: S necklaces, S wealthy glasses, S 10 glasses, S earrings, D Parisian glasses, D 7 glasses, D earrings, D 3 necklaces (T9/T3) | NEW; one study example only (Vivian Sinclair); F01-F02 cover it |
| **The best N** (cuts, colours, pieces) | T5, T6, T9 | 11: S bob never, S face shape, S hairdressers cuts, S pixie, D face shape, D French bob, D salons cuts; S 8 colours, S colour combos, S fall colours, D colour combos | NEW |
| **You're styling it wrong: N secrets** (technique) | T7 | 2: S bob wrong, S thinning hair | NEW (how-to shape) |
| **How to wear X** | T4 | 2: S scarf, D scarf knots | NEW |
| **Body-shape fixes** (silhouette, never weight) | T8 | 3: S apple, S slimmer, D apple | NEW; opens on body reassurance |
| **The rules she never breaks** (the woman who gets it right; the French rules) | T10 | 2: S turn heads, S expensive tricks | NEW; Diane's lens lives here and in T9 |
| **The why explainer** ("Why your haircut never looks right") | no study type; "truths / why explainer" 18 breakouts, 17 real (`BREAKOUT-MAP.md`); M01 | 0 | NEW, optional |
| Not ours: **gray journey** (story), **makeover** (a real client) | T11, T12 | 0 | Out (a persona has no hair to grow out and no client; the "methods" version of T11 runs as a best-N or explainer) |
| Makeup | — | 4 (S makeup rules, S lipstick, S concealer, D lipstick) | **Out**: the makeup pack later |

Total 38: 6 + 8 + 11 + 2 + 2 + 3 + 2 = 34 style titles, plus the 4 makeup titles (my tally of `04` §2.13, each title counted once by its first type there). The two biggest pack types (never/instead item lists and the best-N lists, 19 of our 34 style titles) have the thinnest study coverage: T3 has one study video (`04`, limits). The pack should say: "a title that fits none" falls back to the closest type and is logged as "new type" (KEEP plumbing's rule).

### 2.10 The item shape and item length — NEW (from `02` §3)

Evidence: items per video median 6.5 real, 7 faceless, 7 Scarlet, 6 Diane; pooled words per item **241 real, 258 faceless, 266 Scarlet, 285 Diane**; 22 of 107 real items are under 150 words, 18 over 400 (`02` §3.2). Real lists balloon on one item (Diana GOSS's fit item 833 vs 170-280); faceless lists are even. In mistake lists, a swap label in 23 of 36 real items and nearly every unlabelled one still names the replacement. Real item frame (Marie-Anne): "The next thing that screams old lady is…" → "So, what can you do instead?" → "My pro tip is…". Faceless: "Mistake one…" → "Here's the problem" → "So, what's the solution?" → a one-line rule.

Proposed shape: (1) the look, in her own mirror or closet (what she sees; occasionally what she feels); (2) why it ages or why it works: the mechanism in one or two plain lines; (3) the turn ("So what do you do instead?", rotated: it's Marie-Anne's line and a candidate once-phrase); (4) the swap, specific (a cut, a length, a colour, a fabric, a brand as benchmark where the brief gives one); (5) the check she can run (mirror, photo, the window, the hat test: real presenters' own device); (6) the result in look words, or a compliment, or once in a while how it feels. **Length guide: about 180-300 words an item, longer when the item carries the video** (`item-words: 150-350` as a report band). No more than two items without a bridge (KEEP).

### 2.11 Using the models — ADAPT

KEEP the five never-copy rules and HVAC's "a model where one fits, not every script" (operator 2026-10-27, "agree but not always needed"). Library (HANDOFF session 13; P18): **30 real presenters** in `studies/style/models/approved-models.csv` (M01-M30: 12 hair, 15 fashion plus M29-M30 from the item search, 1 French angle; 4 of them Justin Hickox, a man), **8 faceless structure-only** (F01-F08: Vivian Sinclair ×2, Golden Melanin, AnniePicks, French Fashion, Emiko Sato, Ageless Glamour, Ever Chic At 50). Real = structure, voice and emotion; F = structure only ("never voice or wording", session 13). Men (Justin Hickox) give structure and emotion but never voice samples. Model files: KEEP electrical's spec with its "Emotion voicing" section (`electrical-scripts/model-file-spec.md`); the tag line takes plumbing's two forms (`[real]` / `[structure only]`), the F files labelled like plumbing's S files. Banned labels to add for style: `[TRY-ON: banned]` (first-person wearing), `[CLIENT: banned]`, `[AGE SLOGAN: banned]`, `[SPONSOR]`. "Doesn't transfer" lists: try-ons, "as you can see", her own age and body, clients, sponsor reads, the course pitch, "I bought this in Zara".

### 2.12 CTAs and the ending — ADAPT (profile-led)

Ours: the book twice in all 38 (mid pitch 148-234 words at 2:18-7:28; end block 84-215 words) plus subscribe and "which… first" (`06` §11). Real winners: mid-video CTA in 16 of 21, own product in about 15, subscribe in 6 of 21, "I read every one" in 0 of 21 (faceless 8 of 24) (`03` §8.3). **Comment asks about her** drew answers (24 of 29 gave a place; about 20 of 46 an age and place); ours (30 "which… first" asks) drew 1 answer in about 42 comments (`03` §8.5). Plan: the book CTA's place and shape per profile (operator: suggestion 8 "per channel, set in the persona profiles"); the comment ask about her (her age, where she's watching, what she has kept twenty years; suggestion 7, yes), rotated, never the same twice running; "I read every one" is a faceless tell in this niche (ASK 9 with the ending). Never a long QR walkthrough.

### 2.13 Length — ADAPT

Real median 11.9 min (2,031 words), 10 of 21 at 12+; faceless 15.6 (2,482), 21 of 24 at 12+; ours 16.4 and 16.9 (2,804 and 2,852 words), all 12:30+ (`02` §1). Pace 170-171 wpm ours and real, 156-157 faceless; our caption wpm overall Scarlet 169, Diane 172 (`own-baseline` SUMMARY). Inside our channels the top five run longer than the bottom six (3,075 vs 2,702 words, `06` §14), but the title explains more. Plan: profile wpm 170 (from the real voiceovers, as HANDOFF 2026-10-20 requires); minimum ASK 8 (12 minutes = 2,040 words at 170); "VAs don't ask for length" (KEEP).

### 2.14 Voice — ADAPT

KEEP "you" for instructions, "I" for opinions, plain over clever, honest candour, warmth from reassurance, no jokes, swearing none, one picture-phrase per item. ADAPT:
- **"I" without claims:** "I think", "I love", "I'd", "what I'd tell a friend", "my rule"; never "I wore", "I bought", "I tried", "my client". Real figures: "I" 23.4, "I think" 30 times in 7 videos, "I love" 23 (`04` §3c).
- **Brands named** where the brief gives them, as benchmarks or examples (real 13 of 21; ours 1 of 38, `02` §5).
- **No house vocabulary** (§3): "reads as" (112 uses in 33 of ours), "quietly", "from across the room", "small gold hoops", "gallery", "book club", "camel" (46 uses in 21), "quiet luxury" (20 uses), "for generations", "on purpose / chosen / decided" (31 of 38), the three-word wraps ("Simple, warm, and impossible to argue with") (`06` §15).
- **Diane's tics:** "the French answer / fix / way" 1.38 per 1,000 in 13 of 13, "try this / test" in 13 of 13, "What I see" 7 of 13 (`02` §3.3): once-list.
- **Terms of address:** real "ladies" (7), "you guys" (6); Diane "chérie" (5). A profile device, capped.
- **Spoken forms:** heights in words ("five foot two"); brand names with "&" in words; a size as said ("a size twelve"); "a two-inch heel"; French words per ASK 13.
- **The persona device** (KEEP rule, profile content): Scarlet's "Mine lives on a hook by the front door" and "My own is berry" (`04` §6c) are possession claims under the claims policy unless the profile lists them.

### 2.15 Proof — ADAPT

Plumbing's "Use / Never" holds, with style content. **Use:** the mechanism in one line (why a shorter cut lifts: "the weight pulls down"); the check she runs (mirror, phone photo, daylight at a window, the thumb-over-the-frame test Diane uses); a stylist's or tailor's rule credited generally ("tailors work to the shoulder seam"); the honest limit ("not every trend is for everyone", Adore Your Wardrobe); a brand's real fact from the brief. **Never:** "I tried / tested / wore", try-on narration ("as you see here"), clients (named or not: Vivian's Clarice and "I'll call her Susan" are F/AI inventions, `04` §6b), "I've worked with hundreds of women", "studies show / psychologists say" (15 times in 6 faceless, `04` §3b), the persona's age or body as proof (ideation: "no first-person face-as-proof on a synthetic presenter").

### 2.16 Money — ADAPT, mostly DROP

Operator, suggestion 6: "yes, but it depends on the title ('if the price mentions budget or cheap things')". Evidence: money figures 0.14 per 1,000 real, 0.15 faceless, 1.30-1.59 ours; 34 of 38 ours vs 5 of 45 study (`02` §5). Viewers dispute prices here too: "$15 to $25? Maybe in 1960!" (`03` §1.8). Plan: no price unless the title promises budget, cheap, "without spending" or a figure; then from the brief, rounded, as a range, at most one or two a script; "look expensive" is delivered through cut, fabric, fit and colour, never a receipt. Brands as benchmarks ("the famous expensive brand"), never a negative claim about a named brand. Plumbing's money section (devices, payback, cents) DROPs. **The ideation brief spec's "real dollar figures" will keep putting prices in briefs:** the pack must say the brief's prices are background unless the title is a budget title (ASK 15 on the ideation side, which isn't in this repository).

### 2.17 Safety — NEW (small, real)

Real risks this niche touches, where the brief is silent:
1. **Hair dye:** the patch test before home colour, every time (box instructions); no box dye over salon bleach or henna without a strand test; any scalp reaction is a stop and a doctor.
2. **Heat tools:** heat protectant, a lower setting on fine, thinning or gray hair; no iron near the scalp or ears held still.
3. **Thinning hair and scalp:** styling only; sudden shedding or patches are a doctor's or dermatologist's question (claims policy, ideation rule 3); no oils, supplements or products claimed to regrow hair.
4. **Shoes and falls:** viewers bring it: feet or balance 6, "we are more prone to tripping… know where the cracks and bumps on the sidewalk are" [115], "since having had a stroke I have no choice but to wear the same type of runners" (`01` §1). Heel height, backless shoes, slick soles: the safe choice is said plainly, never shamed.
5. **No diet, weight-loss, supplement or exercise plan** (ideation rule 2): "slimmer" is line and silhouette.
6. **Prescription glasses:** the optician fits the lenses; frame advice only (Vivian's own limit, "I am not an optician", `03` §3.2).
The brief wins on safety, as plumbing (KEEP), but never removes items 1, 3 and 5 (electrical's "the brief can add safety, never remove it"). A small facts guide with two sources per row is ASK 10.

### 2.18 Banned list and scanner block — ADAPT (details in §3)

KEEP: intro and greeting, "this channel is for", teases, recaps, first-person tests, pointing at the screen, customer stories, edit notes, competitors' catchphrases, the 8-word copy guard. DROP plumbing's template stock lines that never appear in style ("not a scam, just economics", "your pipes will thank you") unless the main session wants them as harmless guards. ADD: the house vocabulary, age slogans, the not-your-fault formula, our old sign-offs, our tease forms, persona age, try-on and client claims, borrowed authority, health words, the long QR lesson, `min-minutes`, `first-item-seconds: 45`, `example-guard: 5`, `item-words`, and the hard-word `require-if`.

### 2.19 Before handing over — ADAPT

KEEP the checklist's shape. Style lines: the title's promise word said early and at least twice; no intro, no age line in the opening unless the title has it, no slogan; item one by about 45 s; a feeling in about a quarter of items, permission in plain words, the why in every item; "but", "you" and questions at the targets; the villain only if the title carries it; no house vocabulary; prices only on budget titles; brands only from the brief; the hard word at most once and flagged; the French claims hedged (Diane); safety defaults; the comment ask about her; the CTA per profile.

---

## 3. The scanner on style wording

### 3.1 How it's called

`python3 core/script-scanner.py SCRIPT --rules <pack>/SKILL.md <persona>/SKILL.md --pack BRIEF [guide] --title "LOCKED TITLE" --refs <pack>/SKILL.md <pack>/references/excerpts.md <pack>/references/voice-samples.md <pack>/references/models/*.md <persona>/SKILL.md --final` (the HVAC and electrical commands in `tools/build_skills.py`). Pack keys it reads: `ban`, `ban-regex`, `once`, `once-regex`, `lift`, `allow`, `min-minutes`, `item-words`, `first-item-seconds`, `sentence-max`, `example-guard`, `letters-ok`, `require-if`; profile keys `name`, `book`, `tenure`, and a "Words per minute" line (`core/script-scanner.py` docstring and `read_rules`). **There is no "judge" key** (a pack can't make a phrase a judge line, only fix-on-sight or once).

### 3.2 Runs on our own transcripts (core only, `--final`, no pack)

Converted from captions to plain text (timestamps stripped, six sentences a paragraph). **Caveats:** captions write numbers as digits and drop punctuation in places, so SPOKEN and sentence findings partly reflect the captions, not the delivered scripts.

| Video | Spoken words | ITEMS line | Fix on sight | Notable |
|---|---:|---|---:|---|
| Scarlet `w6w_ktMBHXM` (necklaces, top) | 4,078 | 5 items found, item one at word 197 | 9 | 7 sentences over 35 words; "16 to 18 in" as a unit; 3 reframes ("doesn't read as a necklace at all. It reads as a line") |
| Scarlet `h9MsF44shdQ` (bob wrong) | 2,773 | **no signposts found** | 3 | the secrets aren't "Number N." |
| Diane `ISAL4NBlshQ` (frumpy, top) | 2,085 | **item one at word 1,838** (it found the closing "Check one…" recap) | 5 | "1/3 over 2/3"; "À bientôt" fails as non-standard characters; one line "talks about its own packaging" ("let me put this video's title to bed") |
| Diane `kWzjIzbdB00` (glasses) | 3,944 | 3 items, item one at word 142 | 8 | **hard ban "By the end you'll know"** caught; "Voilà" fails; reframes 2; "you see" ×3 over the filler limit |

Across all 38 (my batch, core only): sentences over 35 words in 34 of 38 (106 hits); staccato judge lines in 27; non-standard characters in 9 (21 hits, all French accents); two-way "lives" in 19, "live" 7, **"bow" 4**, "wound" 3; hard-ban teases caught in about 13 videos (15 hits: "by the end, you'll" 4, "at the very end" 4, "by the end of this video" 2, five others once). The study finds teases in 28 of 38 hooks by reading (`README` finding 16): **the core list misses most of our tease forms** ("We'll get to those", "still ahead", "the one I promised").

**What the core misses entirely:** the self-introduction ("I'm Scarlet Sterling and this channel is for women over 60…") passes: the "this channel is for" ban lives only in the plumbing and electrical blocks.

### 3.3 Candidate ban lines, tested

Run as a scratch pack block (`candidate-pack.md`) on our 38 and on the 63 English study transcripts in `studies/style/data/` (36 real-presenter, 27 faceless or AI; the two dropped Spanish videos left out). Cells: videos with a hit / hits. "(over once)" counts only scripts that used a once-phrase twice or more.

| Line (regex in short) | Scarlet (25) | Diane (13) | Real (36) | Faceless/AI (27) | Verdict |
|---|---|---|---|---|---|
| V1 `\b(?:small\|little\|tiny) gold hoops?\b` ban | 15 / 17 | 9 / 9 | 0 | 0 | **ban** (the study's 22 of 38 counts phrase forms more widely) |
| V2a `\breads? as\b` ban | 17 / 56 | 10 / 23 | 3 / 3 | 11 / 31 | **ban** (real presenters say it 3 times) |
| V2b `\b(?:reads?\|reading) (?:like )?(?:tired\|polished\|expensive\|dated…)\b` ban | 17 / 46 | 5 / 9 | 1 / 2 ("camel always reads expensive", Tracy) | 1 / 1 | **ban**; the adjective list needs care |
| V3 `\bquietly\b` once | 18 over once / 55 | 4 / 9 | 0 | 7 / 29 | **once** (as HVAC) |
| V4 `\bfrom across (?:the\|a) room\b` ban | 10 / 12 | 7 / 9 | 0 | 0 | **ban** |
| V5 sentence opening "Picture" / "Imagine" once | 17 over once / 63 | 6 / 21 | 0 | 4 / 19 | **once**; the visuals still have to be named plainly (core: the edit shows only what the narration names) |
| V6 `\bgallery\b` ban | 19 / 21 | 1 / 1 | 0 | 3 / 4 | ban (or once) |
| V7 `\bbook club\b` ban | 16 / 16 | 0 | 0 | 1 / 1 | ban |
| V8 `\bwhenever (?:it )?suits you\b` ban | 7 / 7 | 3 / 3 | 0 | 0 | ban |
| V9 `\bfor generations\b` once | 1 over once | 0 | 0 | 0 | once (12 of ours use it, `06` §15) |
| V10 "Two women…" opener ban | 1 | 1 | 0 | 0 | ban (5 videos by `06` §15's wider count) |
| A1 `age is (?:just\|only) a number` | 0 | 0 | 0 | 0 | ban anyway (operator: "no age slogans") |
| A2 `no age limit\|no expiration date` | 0 | 0 | 1 / 1 ("style has no expiration date, and neither do you", Marnie Goldberg) | 6 / 7 | ban |
| A3 `you(?:'ve\| have) earned (?:it\|this\|both\|the right)` | 0 | 0 | 0 | 4 / 4 | ban |
| A4 `you deserve` | 0 | 0 | 0 | 7 / 8 | ban |
| A5 `never too late\|it's not too late` | 0 | 0 | 0 | 2 / 2 | ban |
| A6 `(?:style\|elegance\|beauty) is not about age` | 0 | 0 | 0 | 1 / 1 | ban |
| R1 `it's (usually) not you\|not your (age\|body\|weight…)` | 0 | 0 | 0 | 5 / 7 | ban the formula (ours say it in other words: 9 Scarlet, 7 Diane, `03` §2.1; H21 still counts) |
| H1 `old lad(?:y\|ies)\|grann(?:y\|ies)\|grandma` once | 0 | 0 | 2 over once / 12 | 2 / 12 | once |
| H2 `require-if: old lady\|granny\|grandma => harsh but true\|tough love\|not on you\|with love\|gently\|brutally honest` | 0 | 0 | 2 missing | 1 missing | **works**: the existing `require-if` key can enforce "flagged" |
| I1 `I'?m (?:Scarlet\|Diane)\b\|this channel (?:is for…)\|I show women` | 24 / 41 | 12 / 18 | 0 | 0 | ban (names belong in the profile block) |
| T1 `we'll get to (those\|that…)\|still (?:to come\|ahead)\|I'm saving\|saved … for last\|the one I promised\|coming up` | 15 / 19 | 8 / 13 | 4 / 5 | 3 / 3 | ban; narrow "I'm saving" to "I'm saving (the\|it\|that\|this\|one)" (a real false hit: Justin's "I'm saving you money") |
| S1 `stay polished and stay sterling\|à bientôt` | 24 / 24 | 8 / 8 | 0 | 1 / 1 | profile bans (sign-offs are profile matter; ASK 9) |
| C1 `I(?:'ve)? (?:tested\|tried\|wore\|bought\|own\|ordered)` | 1 | 1 | 6 / 18 | 2 / 2 | ban (ours: "I tried that look once", "jewelry I own") |
| C2 `my (?:clients?\|salon\|chair\|husband\|daughter…)` | 0 | 0 | 8 / 17 | 4 / 6 | ban |
| C3 `I've worked with hundreds…\|years beside a fitting room mirror` | 0 | 0 | 0 | 2 / 2 | ban |
| C4 `(?:studies\|research\|psychologists…) (?:show\|say\|found)` | 0 | 0 | 1 | 2 / 2 | ban |
| C5 `I'?m (?:over )?(?:50\|60\|70\|\d\d)( years old\| myself)?` | 0 | 0 | 4 / 5 | 2 / 2 | ban (claims: ages) |
| C6 `regrow\|reverse(s) aging\|stops hair loss\|anti-aging` | 1 ("foundation sold as anti-aging", a fair mention) | 0 | 1 | 1 ("the cure", figurative) | ban without "cure"; judge "anti-aging" in context |

More once-candidates from the counts (not run): "camel" (21 of ours, 46 uses), "quiet luxury" (20 uses in 9), "the French answer/fix/way" (Diane 13 of 13), "try this tomorrow" (Diane), "what I see" (Diane 7 of 13), "so many of us / nearly all of us" (15), "on an ordinary Tuesday" (6), "somewhere along the way" (6), "So, what can you do instead?" (Marie-Anne's own pivot: the pack's turn question, rotate it).

### 3.4 Lines I wrote, and what fired (core plus a test profile `tenure: none`)

| Line | Result |
|---|---|
| "If you're 5'2" and under…" | **fix** (inch/foot mark) — good |
| "…at H&M and M&S, and J.Crew…" | **fix** ("&" symbol) — write "H and M", "Marks and Spencer"; "J.Crew" passes |
| "Chérie… Voilà. À bientôt." | **fix** ×4 (non-standard characters) — ASK 13 |
| "Number one is the bow blouse…" | judge ("bow" two ways) — expect it in many style scripts |
| "Use an SPF 30…" | judge (letters "SPF") — makeup pack mostly |
| "I've been doing hair for 30 years…" | **fix** (tenure none) — caught via "been … for N years" |
| "I'm 62, and I wore this exact cut…" | **passes** — age and lived claim uncaught (C5, C1 above) |
| "In forty years of dressing for boardrooms and galas…" | **passes** even with `tenure: none` |
| "As a stylist for 30 years…"; "After 30 years in fashion"; "a 25-year stylist"; "I have spent 20 years in the fashion world" (with `tenure: 40`) | **all pass** — "stylist", "fashion", "dressing", "styling" aren't in the scanner's trade words (`_TRADE`), and "spent … in" needs "for" — the same class of gap as P16 |
| "Rosemary oil regrows thinning hair…" | **passes** (C6) |
| "Good silk scarves run $50-$80…"; "A 3-inch heel…"; "a size 12" | pass (no money/hyphen ban in core; HVAC bans hyphen ranges in its own block) |
| "Age is just a number, and you've earned the right…"; "It's not you, it's the blouse." | pass in core; caught by A1, A3, R1 |
| "Picture a Sunday brunch. Small gold hoops… reads as expensive from across the room."; "quietly" ×2 | pass in core; caught by V1, V2a, V4, V3 |
| Name test: "Scarlet Sterling", "Diane Dechambre" with `name: Scarlet Starling` / `name: Diane de Chambray` | **fix** (near-miss names) — good; since scripts never say the name (S3), the profiles can simply ban both names |

### 3.5 The title-word check (suggestion 2): not there yet

The scanner reads `--title` only for a years figure (`title_tenure`). Nothing counts the title's words in the script; `require-if` can't help (its trigger is in the script, not the title). Our evidence (my count from `meta.md` titles): "instantly" in 14 titles, said 0 times in 11 and "instant" once in 3; "younger" in 8, said 0 in 5; "10 years" in 11, said 0 in 6 and once in 5; "slimmer" in 3, 0 in 2. "Expensive" and "French" are said 5-22 times wherever the title has them.

**A key it could take** (describe only; core change, ASK 12):
```
title-words: instantly, younger, older, expensive, slimmer, thicker, frumpy, chic, 10 years | 2 | 60
```
For each listed word (stemmed: instant/instantly, slim/slimmer) that appears in `--title`, count it in the spoken text; fewer than 2 is fix on sight (or a judge line, if the operator prefers), and if none falls in the first 60 seconds at the profile's wpm, a second finding. It prints a TITLE WORDS report line ("instantly 0 of 2, first at —") that the evidence block's "Title word" line copies. A test: a title with "INSTANTLY Younger", a script saying "instantly" once and "younger" twice, one at 0:20, fails on "instantly" only.

### 3.6 Other scanner gaps style hits (all core)

1. **Tenure words:** "stylist", "styling", "fashion", "dressing (women)", "hairdresser", "colorist", "wardrobe"; "spent N years in…" without "for". Matters only if a profile sets `tenure:` (ASK 3); with `tenure: none` the phrasing "In forty years of dressing…" still passes.
2. **Signposts:** `SIGNPOST` finds "Number one", "Step one", "Mistake one", "Tip one" but not "Rule number three", "Knot number one", "Mistake number one", "Secret number five" or "The first cut is…" (Scarlet uses ordinal sentences in 16 of 25, `02` §3.2). The ITEMS line, which the evidence block copies, will be wrong on most style scripts (seen above on Diane `ISAL4NBlshQ` and Scarlet `h9MsF44shdQ`). Fix: allow "[Word] number N" and add Rule, Secret, Cut, Color, Shade, Knot, Habit, Trick, Style; or a pack key `signposts:`.
3. **Accented letters** (ASK 13): `OTHER_NON_ASCII` fails every accent. Options: write French without accents, or a pack/profile key such as `chars-ok: é è à ô ç`.
4. **No pack-level judge key:** "flag the first use" (suggestion 9) is enforced instead by `once` plus the softener `require-if` (H2 above works).
5. **Two-way "bow":** fine as is; the pack writes "a bow blouse" (a noun before a noun) and the judge reads it.

---

## 4. Wiring for a new pack and two channels

| Place | Now | Add | Note |
|---|---|---|---|
| `core/channels.md` | Rows 1-9 (9 = Werner Finkbeiner) | **Row 10 Scarlet Starling**, **row 11 Diane de Chambray**, niche pack `style-scripts` (name ASK 1), profiles `personas/scarlet-starling.md`, `personas/diane-de-chambray.md`, status pending until a test passes | |
| `tools/build_skills.py` description | 770 characters now (my count) | "Scarlet Starling and Diane de Chambray (women's style over 50)" adds about 64: about 834, under 1,024 | |
| `build_skills.py` "the other skills it reads" table | 14 rows | `style-scripts` and the two `-persona` rows | the electrical branch once forgot these (HVAC draft §1) |
| `build_skills.py` scanner commands | Woodworking, plumbing, electrical, HVAC | A style command (no price guide: `--pack BRIEF` alone) | **Existing bug:** the electrical command's code fence is never closed, so "HVAC (the same shape…)" sits inside the electrical block and the HVAC command renders as plain text (lines 86-94) |
| `build_skills.py` `PERSONAS`, `PACKS`, `INSTALL` | 9 personas, 4 packs, "Seventeen skill files" | 2 personas (books if any), `"style-scripts": ("archive", "model-file-spec.md")`, INSTALL rows and the counts ("Seventeen" → 20 with the three) and the "Using them" line for style inputs | |
| `tests/run_checks.py` | Numbers 1-72 in use with suffixes 1b, 6b, 7b, 12b, 12c, 12d, 25b, 46b; 80 checks pass now ("80/80 passed" counts checks, not numbers) | **73 onward** if no other chat has open work; **80-89** if one might (HVAC took 60-69 for that reason). Twins of 21/46/61 (inputs), 22/47/62 (scanner block), 24/49 (copy guard), 25/50 (profile facts), 26/67 (channel row and build), 66 (models: real tagged `[real]`, F files tagged structure only, unlike HVAC's "no S files"), plus title-word and signpost tests if built | Checks 1b and 2 cover only core, woodworking and plumbing files: add the style pack. Check 2's stale list includes "house rules": the pack must say "house vocabulary". Checks 28 (every profile flags "e-book") and 34 apply to the new profiles automatically |
| `PROPOSALS.md` | P1-P18 | **P19** next (for example the core scanner changes, or anything touching a locked rule) | P18 was the model floors |
| `README.md` file map | Packs: woodworking, plumbing, HVAC, electrical; `studies/style/` row; drafts | A `style-scripts/` section (SKILL.md, references, model-file-spec), the two profiles and any books under `personas/`, the diagnosis draft under `drafts/`, this folder under `studies/style/`; the intro line's pack list | `personas/README.md` lists profiles too |
| `CHANGELOG.md`, `HANDOFF.md` | | Rows as usual | |
| Copy-guard `--refs` | | SKILL.md, excerpts, voice samples, models/*.md (F files included), profile | |

---

## 5. ASK items (decisions only the operator can make)

1. **Pack name:** `style-scripts` (matches `style-ideation`; makeup later as `makeup-scripts`), or `hair-fashion-scripts`?
2. **Script type** for both channels: Talking Head (CTA markers, as Frederick, Sam and Werner) or Classic?
3. **The soft credential (suggestion 4):** which option: (a) soft backstory only, (b) a fixed tenure figure in the profile (Scarlet's "forty years of dressing for…", which needs the scanner's style tenure words), or (c) none?
4. **Diane's identity:** French-born (one approved heritage line, "raised in Paris", P14 style) or an American who learned it in Paris (as our 13 scripts speak: "how we buy it here")?
5. **"We" and "us":** may the persona speak as one of the women over 60 ("so many of us", "women our age"), which implies her age under the claims policy?
6. **The "I" target:** real women run 23 per 1,000 words, faceless winners 7-8, ours 4-6. Set a floor (about 10-12, from opinions only), or leave it to judgement?
7. **The book CTA per profile:** where (after item 2 or 3, a third in?) and how long, and are the two books' texts available for the book match?
8. **Length minimum:** keep the core 8 minutes, or 12 like the trade packs (12 minutes = about 2,040 words at 170)?
9. **The ending:** plumbing's (comment ask last, no sign-off), or the core's (one closing line, a sign-off)? And keep "I read every one" (0 of 21 real presenters say it; 8 of 24 faceless do)?
10. **A small facts and safety guide** (dye patch test, heat, falls, thinning hair, each row with two sources), or the brief plus six safe defaults only?
11. **Forward promises:** confirm that plumbing's named-promise override (P3) does not carry to style (real presenters hold nothing for the end).
12. **Scanner work (core, every channel):** a `title-words` key (suggestion 2's check), style signposts ("Rule number three", "The first cut is…") and style tenure words: yes, and which chat does them?
13. **French words with accents** ("chérie", "à bientôt", "voilà"): write them without accents, or allow accented letters through a pack/profile key (core scanner change)?
14. **Dated facts on trend and season titles** ("Fall 2026"): no rule (as HVAC), or only from the brief with its date?
15. **The ideation briefs:** they're built to carry dollar figures; should the style briefs stop doing so except on budget titles (the ideation skill is outside this repository)?
16. **Brands said negatively:** may the script give an opinion against a named brand ("I'd leave the Birkenstocks for the garden"), or only name brands as benchmarks and good examples?
</content>
</invoke>
