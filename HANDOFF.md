# Handoff: how this system was built, and why

Context carried over from the claude.ai conversation that designed this library (October 2026). Read with `README.md` (what each file is) and `PINNED.md` (open items).

---

## 1. What this is

A script-writing system for a portfolio of faceless and AI-avatar YouTube channels aimed at viewers over 50 (practical education, some channels selling e-books). It replaced a bought product, FacelessOS, which was built for entertainment documentaries and full of material that didn't fit. FacelessOS was rebuilt as our own library. The original files are kept in `archive/facelessos-original/` for comparison only.

## 2. Architecture and precedence

- **Core (`core/`):** base rules for every channel.
- **Niche packs** (e.g. `woodworking-scripts/`) override core base rules wherever they say so explicitly. Where they're silent, core applies.
- **Persona profiles** (`personas/`): per-channel settings (voice, CTA, offers, script type). They can override niche and core where explicit.
- **`core/claims-policy.md` and `core/offer-rules.md` sit above everything.** Packs and profiles can tighten them, never loosen them.
- **Every script starts with START** (`core/workflow.md`): pick the channel, the input gate (refuses to write until every input is valid), then an uninterrupted run to the final output.

## 3. Decisions, and why (locked unless the operator changes them)

### From the woodworking-for-profit study

The data: BeardedViking and WhosTheVoss winners against Dale and Hank's own videos. Hank's old faceless videos were deliberately excluded.

- **No persona or channel intro.** The winners never introduce themselves.
- **Get to the first material fast:** within about 15 seconds. BeardedViking does it in 5-15 seconds.
- **No retention teases** ("stick around," "bonus at the end"), no problem essays, at most one sentence of context.
- **Length comes from the content, never word budgets.** Each unit (material, step, tip, cost line) takes what it needs. Trivial items are batched, repeated steps collapse, and the plan comes before the prose. *(Changed 2026-10-20: every script now has an 8-minute minimum; see "Operator decisions, 2026-10-20".)*
- **The money block is a bookend:** promised in line one, proven at the end with listings, price, cost, fees and what's left.
- **Proof is always researched online listings,** worded honestly: "listed at" for asking prices, "sold for" only with sales evidence.
- **Where to buy,** with "prices subject to change" said once.
- **Tool alternatives are shown, and safety is one line inside the step.**
- **Voice:** "you" for steps, "I" for opinions. Honest candor yes, jokes no (AI humor is hard to prompt).
- **Adversaries:** the doubter (the default), big box markup, scammers, overpriced materials. Categories only. Never clickbait YouTube or the algorithm. The old "hardwood crowd" is retired.
- **Swearing:** mild words, 1-3 per video, aimed at targets, never in CTAs, titles or thumbnails.
- **Visuals are AI-generated from the script.** Every step names a visible object and action, and the script never points at something it doesn't name.
- **Steps are instructions to the viewer,** never "I'm cutting." The persona never claims sales, customers or history.
- **Single builds only for now.** Listicles come later, written fresh from research packs, never re-cut from finished videos.
- **CTA test:** Hank gets a short CTA right after the first payoff; Dale stays as he is. Compare each channel before and after.
- **Ideation must stop producing titles the script can't deliver.** Exaggeration in degree is allowed.
- **No hourly-wage framing** (the operator dropped it).

### From the FacelessOS rebuild

- **Kept and rewritten:** humanizer, voice anchoring, scanner, retention mechanics, variety rotation, CTA mechanics, research rules, fallback structures, audit.
- **Cut:** the master file, quick start, title formulas, celebrity, true crime, hero's journey, visual scripting, the hook swipe files, retention coaching, the "Four Pillars" header, word-count tables, editor notation.
- **Vidrush voiceover prose is the only format;** Talking Head markers or Classic.
- **Humanizer:**
  - H1-H23 (H20 "Most people…" allowed once; H23 filler phrases at most once each)
  - hard bans include the retention teases and "let's get into it"
  - a niche pack or persona profile can lift a ban only by naming it
- **Voice samples:** 2-3 verbatim clips of human narration from niche winners, stored in the niche pack. Never AI-written uploads.
- **Rehooks:** short-range bridges between segments are allowed and encouraged. Long-range promises are banned.
- **CTAs:**
  - content, length and style come from the persona profile
  - every CTA promises real added value
  - mid-CTA after the first payoff
  - the ending is the CTA or nothing, then exactly one closing line
  - never name a future video (the script has no idea what comes next)
- **Research stage rules:**
  - facts are always verified
  - framing (stakes, villain tone, title degree) may be exaggerated, but not to an extreme
  - freshness windows are set per niche
  - a mandatory verification pass
  - titles that can't be supported get flagged back to ideation
- **Audit:**
  - groups A-F, with a short visible evidence block (scripts are uploaded without anyone reading them)
  - at most three rounds
  - NOT READY prints no script
  - only PASS scripts are uploaded
- **Rotation log:** the VA pastes the last five lines. Scripts are made in bulk on different PCs, so there's no shared file.
- **Greetings:** off by default; a niche or persona can allow one.

### Operator decisions, 2026-10-20 (Hank and Dale profiles)

These change or extend earlier decisions above, by the operator's choice.
- **Persona profiles come from Notion** (Channel List, TEAM ACCESS), checked and changed with the operator, then saved in `personas/`.
- **The enemy for both channels is big business and the corporations.** It's a category, never a named company, and it replaces the pack's default doubter.
- **Dale may name one fixed family detail:** he learned at his grandfather's bench, and his grandfather made him promise to write it all down. This is the one exception to "the persona never claims history", added to `core/claims-policy.md` (see `PROPOSALS.md`, P2).
- **The CTA test is now Hank against Dale:**
  - Hank keeps two short CTAs (mid and end) pointing to the QR code.
  - Dale uses the Bertha's Clean Home style: one ~35-word pitch pointing to the description link, five one-line book mentions as narration, no end CTA, no subscribe ask, and an ending of a comments request plus "Now go make some sawdust."
  - This replaces "Dale stays as he is".
- **Each channel's full book text is in the library** (`personas/books/`). CTAs cite real pages that cover the video's topic (the book match), and otherwise give the book's general value.
- **Hank has no opening lead-in** ("All righty" was dropped). His sign-off is one sentence: "Keep all ten fingers and I'll see you at the bench."
- **Dale's main pitch keeps Bertha's shape, with fresh words every video.**
- **Every script is at least 8 minutes long,** counted at the channel's words per minute (150 if unset, so 1,200 words). Value-driven only: longer is fine, padding never is. A topic that can't reach 8 minutes goes back for more research. Niche packs may add guidance.
- **"Right here" and "look at this" are banned everywhere,** including at listing screenshots.
- **A persona's fixed last line is exempt from H13** (upbeat closers).
- **Left as they are, by choice:** the rotation log gets no end-CTA field (the operator is fine if an end CTA's wording repeats), and an edit after PASS keeps the PASS.

### Operator decisions, 2026-10-20 (ideation and packaging)

- **Ideation runs in Cowork,** where Claude can browse Etsy in a real browser. **Etsy is the main source;** eBay and Facebook Marketplace are optional spot-checks. Products are found by hand-checking, with no paid tool and no API for now.
- **The woodworking ideation pipeline** goes: product scan (30 products) → title and thumbnail-text options (format bank plus new creative ones) → the operator's picks → briefs → optional research pack. The fallback is invented products, marked as invented, with no sales figures.
- **Briefs** are a bank of facts only, never structure or language direction, about 500-800 words, one spreadsheet cell with " | " between fact groups.
- **Titles and thumbnail text may exaggerate freely,** including tenure and income claims. Ideation doesn't hard-code claim bans. The script delivers such titles through the numbers, and the narration still never claims sales or history.
- **Active woodworking channels:** Hank and Dale, both on camera (Talking Head), both single builds. Kenji is stopped. Sam relaunches later as woodworking for profit.
- **Packaging:** one skill per layer, at the operator's request: `script-writer` (the core, START), `woodworking-scripts` (the niche pack), one persona skill per channel (profile plus book), and alongside them `woodworking-ideation` and `ideation-core`. Everything is built from the repo by `tools/build_skills.py`; the operator stores the files in Drive and installs them on each account.

### Operator decisions, 2026-10-20 (plumbing, after the study)

Recorded from the operator's reply to the plumbing comparison (`studies/plumbing/comparison/`). They are applied when the plumbing niche pack and the plumbing persona profiles are written.
- **The Vintage Pipefitter:** no CTAs at all for now (mid-video and end both dropped). An email-collecting CTA will be discussed later. (This replaces the earlier two-line free-e-book plan.)
- **Roger the Pipe Guy and Mark Silverbridge:** the mid-video CTA and the outro CTA go back to the old, much shorter structure their hits used (`studies/plumbing/comparison/01-own-channels.md` and `07-body-craft.md` §10 quote it).
- **No name or channel intros on any channel.** The core already bans them by default (`retention-mechanics.md`), and both woodworking profiles say "Greeting: none"; the plumbing profiles follow.
- **Fixed tenures, formalised 2026-10-20 ("lets formalize from now"): Roger the Pipe Guy 45 years, Mark Silverbridge 40 years, The Vintage Pipefitter 50 years.** Each goes in the persona profile's `tenure:` line, and the scanner fails any other figure. (Earlier the same day Mark was set at 45; the operator replaced it with 40.)
- **Concrete forward promises are allowed in the plumbing pack (P3, approved):** a promise block after the first answer may name two or three later items with their stake, provided each is paid inside the video; vague teases stay banned everywhere. This is the plumbing pack's override of the locked "long-range promises are banned" rule, which stays as it is for every other niche.
- **Hooks rotate.** The opening jobs are fixed, the order and shape rotate, and an opening may be modelled on a reference winner script's shape (never its wording).
- **Get to the point faster, and very quickly give the viewer more reasons to stay by promising more value,** modelled on how the competitors and our own hits do it.
- **Openers are modelled aggressively on our winners and the competitors' winners,** by video type: what each opener triggers and what it asks. (Analysis: `studies/plumbing/comparison/10-opener-teardowns.md`, `11-reasons-to-stay.md`.)
- **The villain on every plumbing channel is the trade:** plumbers, the plumbing industry and the people who profit from service calls (never a named company, per the claims policy).
- **Footage that doesn't match the narration is the editor's fault,** not a script problem. The script rule about naming what the footage should show stays as it is; nothing more is added for it.
- **Contradictions between videos are acceptable; unsafe advice never is.** The fact bank and the safety block exist for safety, not for cross-video consistency.
- **No recaps** at the end of plumbing videos.
- **Words per point depend on the point;** no fixed length per item.
- **"Nine times out of 10" is fine;** it doesn't go on a banned list.
- **Sources and store names are not required** in plumbing scripts.
- **TheCheapFix is the closest format match, but not the main source of scripting ideas.**
- **The plumbing scripts skill carries compiled transcripts of the real-life (human) competitor channels** as reference material, under the copy guard like the woodworking references: Silver Cymbal, Roger Wakefield, Got2Learn and Arrow Pest Service (confirmed by the operator). Not TheCheapFix and not the operator's own three channels.
- **No first-person claims of tests, demonstrations or on-camera actions, unless the title or brief specifically calls for one.** Every number is sourced or given as a typical range.
- **Years in the trade may be said in the video (P4, 2026-10-21):** "the years of experience can be from the title. we can mention in the video but not personally tested." `core/claims-policy.md` now allows the profile's fixed `tenure:` figure, the same way every time, with no dates, employers, towns or credentials. "Personally tested" stays banned in the claims policy.
- **Tests and results, never "I tested" (2026-10-21):** "we dont in the video say I tested. but we say tests and results." Replaces the earlier "unless the title or brief calls for one": no first-person test or demo claim in any plumbing script; tests and results from the brief or research pack are said without "I".
- **Title numbers win (2026-10-21), on every channel including woodworking:** when a locked title states a years-in-the-trade figure, the script may use the title's figure. Applied: `core/claims-policy.md`, the scanner's `--title` option, `workflow.md`, the audit (D3), the profile template, test 19.
- **No scanner checks for boiling water or dry washing soda (2026-10-21):** "dont even flag them". The brief wins on safety. This replaces the plan to put them in the plumbing scanner block.
- **Safety: the brief always wins (2026-10-21).** No separate fact bank; the plumbing pack's safe methods (hot tap water, washing soda dissolved first, one cleaner at a time, nothing after a chemical cleaner, gas and wiring are a call) are defaults only where the brief is silent.
- **No edit notes in scripts, and no "writing for the footage" section in the plumbing pack (2026-10-21):** "i dont want any edit notes in scripts. nothing." Scripts are clean narration only (already the core rule: Vidrush prose, production notes read aloud are fix-on-sight). The core rule that the narration names what it talks about is unchanged.
- **Plumbing inputs are the title and the brief only (2026-10-21):** "inputs also will be only title and brief". No research pack; the brief is the fact source. The rotation log stays as it is. Whether a niche uses a research pack is now set per niche pack (`not used` in its `inputs` block), applied to `core/workflow.md`, `greenlight-audit.md`, `humanizer.md` and `research-and-sourcing.md`; woodworking keeps its pack. The order of the plan to deployment (finish the rules, references, persona profiles, into the library, test, deploy) is confirmed.
- **Vintage Pipefitter CTA (2026-10-21):** no mid-video CTA; a one-line subscribe ask at the end, "for now". Replaces "no CTAs at all for now"; an email CTA is still to be discussed.
- **Every plumbing channel ends like Bertha's (2026-10-21):** "ALWAYS these channels should have the ending lines like berthas where were trying to get a comment." The end CTA is a one-line reminder on every plumbing channel; the comment line (a specific question, "I read every one") is the video's last line, with no fixed last line or sign-off after it. The plumbing pack overrides `cta-and-endings.md` §4 for this (P5).
- **Plumbing length (2026-10-21):** at least 12 minutes, 12-20 the sweet spot, value-based: "it really should be based on the value there can be in the script." Raises the core 8-minute minimum for plumbing only.
- **Once-per-script phrases (2026-10-21):** the scanner reads `once:` and `once-regex:` lines from a niche pack or profile; a second use is fix-on-sight.
- **Plumbing references: the real channels, plus our own hits and TheCheapFix for structure only (2026-10-21).** Voice samples and the archive come only from Silver Cymbal, Roger Wakefield, Got2Learn and Arrow. The excerpts and full labelled scripts may also use our own hits and TheCheapFix's hits, marked "structure only" (how a script is built, never voice or wording), all under the copy guard. This extends the earlier "not TheCheapFix and not the operator's own three channels", which still holds for the archive and voice samples.
- **More models, and never a copy (2026-10-21):** the plumbing pack gets a model library of about 38 winning videos (3 or more per video type), each one file with a beat map AND the full labelled script ("the full scripts should be attached"). Five no-copy rules: the plan names its models and at least three differences; no model twice in the channel's last five scripts (a `model:` field in the rotation log); blending encouraged; models read at planning only; the audit checks it. Collecting more winners with NexLev: "maybe but not now".
- **Plumbing persona profiles approved (2026-10-21):** Roger, Mark and Vintage, from the Notion pages, kept close to them ("for the most part these can stay pretty much the same"). Every Roger and Mark CTA names both the description link and the QR code; Roger's one personal detail is his first-Saturday drain check with his coffee; Mark keeps no contractions (scanner ban in his profile); Vintage has no personal name and no named mentor (no Uncle Ray) and only a one-line subscribe ask. Mark's book says "35-Year Master Plumber"; the operator: "change nothing" (the channel stays 40, the book stays as it is, and scripts never cite the book's figure).
- **No NexLev mini-study for more models (2026-10-21):** "no we dont need to do this." The model library's sample was accepted: "we will see based on outputs now."
- **The scanner checks matter a great deal to the operator** (spoken production notes, wrong channel or book names, numbers said twice, tenure numbers that differ from the profile, "boiling" near drain or toilet, "pour it dry"). The operator approved the core ones (2026-10-20), now built: production notes read aloud, the same sentence twice, persona facts from the profile (name, book, tenure) and the tease phrasings the scanner missed, plus a judged flag for the script talking about its own thumbnail or title. "Boiling" near drain or toilet, "pour it dry" and first-person test claims go in the plumbing pack's scanner block.

### Operator decisions, 2026-10-20 (first script test review, iter-01)

From the review of Hank's first script (the lazy Susan). Full record in `tests/iterations/iter-01/`.
- **The hook plays on emotion, on every channel:** besides the promise, the opening touches the viewer's pain point or wish and points at the solution. One sentence of it, within the first-material and no-teases rules above. The quality bar (core unless the pack overrides, tailored to the audience's emotions, real value, a strong pain-point hook, solution-driven, easy to follow) is now written into `core/workflow.md`.
- **Fewer numbers, easy to follow, on every channel:** exact figures only where the viewer needs them, the rest rounded the way people talk, one price per item, no fee schedules or lists of listings read aloud.
- **Personality stays in:** an extra sentence of opinion, reaction or honest aside here or there is allowed and isn't padding.
- **Words per minute** are set from each channel's real voiceovers: Hank 185, Dale 170.
- **Hank's CTAs point to both the QR code and the top link in the description,** every time. This changes "pointing to the QR code" above. Hank's longer CTAs are fine as they are. Dale stays as he is ("link below").
- **The offer is always "the book",** never "e-book", on every channel.
- **No shop or seller names** in narration. The editor blurs them on screenshots.
- **Titles may claim the persona's selling and tenure** on Hank too, in his own words ("40 years" stays Dale's). Research doesn't flag these; the narration still never claims them. *(For tenure, superseded on 2026-10-21 by "title numbers win" above: a years figure in the locked title may be said in the script, on every channel.)*
- **When START comes without a research pack,** the script chat builds and verifies one, then checks it at the gate. Writing without a pack is still refused.
- **Swears aimed at the viewer** include orders to the viewer ("So do the damn math" fails).
- **Food items** have their factory glue checked as well as the finish.
- **Steps that must follow the finish** (final assembly, hardware) come after it.
- **Hank's QR code exists** (confirmed by the operator).

### Operator decisions, 2026-10-20/21 (second and third script tests, iter-02 and iter-03)

From the Dale lazy Susan tests. Records in `tests/iterations/iter-02/` and `iter-03/`.
- **Saying the narrator reads every comment is allowed.**
- **Prices are always rounded** in the narration, never cents.
- **The hook** does three jobs in one to three sentences: a transformation the viewer can picture, their pain or wish, and one spark of curiosity the video answers (never a tease). Copy the winners' moves, never their words, and rotate the opening move.
- **Every section change is signposted,** and the move into the materials is announced, straight to the first item and its price or the list announced.
- **No recaps anywhere,** including a run-down of the build before the money.
- **Builds follow the maker's instructions for every part,** even when that costs a cut; the hook never promises what the maker's way breaks.
- **Dale's pitch carries one fixed line, word for word:** "My grandfather taught me everything I know about woodworking and made me promise to write it all down, so I did, every technique and fix in one place." This widens his family detail to "taught me everything I know."
- **The writer's audit notes show the hook's three jobs and every signpost.**
- **The value line:** on about one video in three, one sentence after the hook names what the video delivers (the build, where to sell it, the numbers), all of it in the script, never a tease and never the opening line.
- **Packaging:** each skill is a `.skill` file, `script-writer` also comes as a zip, and the full bundle is a zip. Skills go on the account, not in a project.
- **Rotation log:** the operator isn't tracking it for now.

### Rejected, so they don't come back

- **An API pipeline:** too expensive.
- **Team plan seats for VAs:** VAs use their own Claude or Cowork accounts.
- **An automatic rotation-log file:** VAs work on different PCs.
- **Twin-channel cross-checks.**
- **Adding faceless competitors.**
- **Jokes.**
- **Retention coaching.**
- **The Four Pillars header.**
- **Hourly framing.**
- **Fixed CTA lengths, or e-book-only CTAs.**

## 4. Competitor findings worth keeping (woodworking)

- **Script length:** winning scripts ran 1,135-2,408 words, about 1,900 typical. Dale's and Hank's ran about 2,900.
- **Specific numbers per minute:** about 5.5 for the winners, against 2.9 (Dale) and 3.8 (Hank).
- **Words spent on build steps:** about 44% for the winners, against 21-25% for Dale and Hank.
- **First-person "I" per 1,000 words:** about 28 for the winners (they're real people). Dale about 4, Hank about 7.
- **Channel intro:** never, for the winners. Dale and Hank had one in every video.
- **Retention teases:** none for the winners. Dale averaged three per video.
- **Words spent on CTAs:** about 45-65 for the winners, about 125-130 for Dale and Hank.
- **Comments:** about 40% of Dale's and 36% of Hank's were "AI" or "fake" remarks. The most-liked complaints were about narration not matching the footage.
- **Hank's faceless versus avatar results** were confounded (best-of against all, different video ages). Don't treat them as evidence.

## 5. Known limits

- **The scanner's number check matches values, not meanings.** "40 pieces" can match a $40 price.
- **Facebook Marketplace's fee for shipped orders** isn't settled in published sources. The research pack must verify it every time.
- **No real end-to-end run has happened yet.** Persona profiles and the research stage don't exist yet.
