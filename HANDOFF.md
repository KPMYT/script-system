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
- **Titles and thumbnail text may exaggerate freely,** including tenure and income claims. Ideation doesn't hard-code claim bans. The script delivers such titles through the numbers, and the narration still never claims sales or history. *(For tenure, superseded on 2026-10-21 by "title numbers win": a years figure in the locked title may be said in the script, on every channel.)*
- **Active woodworking channels:** Hank and Dale, both on camera (Talking Head), both single builds. Kenji is stopped. Sam relaunches later as woodworking for profit.
- **Packaging:** one skill per layer, at the operator's request: `script-writer` (the core, START), `woodworking-scripts` (the niche pack), one persona skill per channel (profile plus book), and alongside them `woodworking-ideation` and `ideation-core`. Everything is built from the repo by `tools/build_skills.py`; the operator stores the files in Drive and installs them on each account.

### Operator decisions, 2026-10-20 (plumbing, after the study)

Recorded from the operator's reply to the plumbing comparison (`studies/plumbing/comparison/`). They are applied when the plumbing niche pack and the plumbing persona profiles are written.
- **The Vintage Pipefitter:** no CTAs at all for now (mid-video and end both dropped). An email-collecting CTA will be discussed later. (This replaces the earlier two-line free-e-book plan.)
- **Roger the Pipe Guy and Mark Silverbridge:** the mid-video CTA and the outro CTA go back to the old, much shorter structure their hits used (`studies/plumbing/comparison/01-own-channels.md` and `07-body-craft.md` §10 quote it).
- **No name or channel intros on any channel.** The core already bans them by default (`retention-mechanics.md`), and both woodworking profiles say "Greeting: none"; the plumbing profiles follow.
- **Fixed tenures, formalised 2026-10-20 ("lets formalize from now"): Roger the Pipe Guy 45 years, Mark Silverbridge 40 years, The Vintage Pipefitter 50 years.** *(Vintage changed to 45 on 2026-10-21, P6, to match the ideation skill.)* Each goes in the persona profile's `tenure:` line, and the scanner fails any other figure. (Earlier the same day Mark was set at 45; the operator replaced it with 40.)
- **Concrete forward promises are allowed in the plumbing pack (P3, approved):** a promise block after the first answer may name two or three later items with their stake, provided each is paid inside the video; vague teases stay banned everywhere. *(Changed 2026-10-25, P10: no promise block in the opening; named promises stay in the body only. See "Operator decisions, 2026-10-25".)* This is the plumbing pack's override of the locked "long-range promises are banned" rule, which stays as it is for every other niche.
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

### Operator decisions, 2026-10-21 (merging the two chats)

The operator's reply to the merge proposal: "Please do this and ensure there are no issues, no cross contamination no contradictions." Read as yes to the merge and to the three suggestions put with it (marked here so they're easy to revisit):
- **The two chats' work is merged** (`claude/pensive-gates-4c5yrt` into this chat's branch), both sides kept.
- **Plumbing's opening is the hook:** it's checked as the hook's three jobs (the fix named = the transformation; the failed attempt, the bill or the symptom = the pain; the opening question or the promise block = the curiosity). *(Read from "do this".)*
- **The promise block replaces the value line in plumbing.** *(Read from "do this".)* *(The promise block was removed on 2026-10-25; the value line stays unused in plumbing.)*
- **Two plumbing money devices are exceptions to "never cents, one price per item":** the cost per use in cents ("call it 50 cents a pop") and three prices side by side. Everything else is rounded. *(Read from "do this".)*
- **Applying earlier decisions where the files still disagreed** (post-merge audit): "title numbers win" written into the claims policy for `tenure: none` and into Hank's and Dale's profiles; "right here" and "look at this" made core hard bans ("banned everywhere"); the end CTA not logged in the rotation log (2026-10-20); Dale's approved family detail excepted in the offer rules (P2); the plumbing rotation log line carries the money device, the promise devices and the comment question, which its approved rules already check.

### Operator decisions, 2026-10-21 (after the post-merge audit)

- **Plumbing never needs sources, and the audit doesn't count them:** "for plumbing we do not need sources." The originality score (audit E1) drops the named-sources signal for plumbing, counts the brief's less-used facts for signal 1, and passes at 4 of 6.
- **The Vintage Pipefitter's tenure is 45, not 50 (P6):** "stick with what the ideation skill says. all 45. mark 40." Roger 45, Mark 40, Vintage 45, so the titles the ideation skill writes and the scripts agree.
- **The three merge calls confirmed:** "all three are ok" (plumbing's opening counts as the hook; the promise block replaces the value line; the two cents devices).
- **Hank's and Dale's title-numbers line confirmed:** "yes agree for 5" (a years figure in the title is said as years at the bench, never as years of selling).
- **Where the plumbing brief is silent, the script fills in (P7):** "where the brief doesnt suppliment. the script should fill in here"; "the cost should always be estimated tho. never to the cents amount." Prices come from the brief, then the researched price guide in the plumbing pack (two or more sources per figure, re-checked by a second researcher), always said as estimates; everyday settings and intervals from general knowledge; doses only from the brief or the safe defaults; fewer numbers (at most one price per item). This replaces "a missing fact stops the run" for plumbing.
- **Better briefs:** the plumbing ideation skill is in the library now, and its briefs give each item its cost and the right way.
- **The rotation log comes from the same chat:** "rotation log will always be in the same session so its fine. we have that." A channel's scripts are written in one chat, so the gate takes the ROTATION LOG ENTRY lines from the earlier scripts in it; pasting is only needed in a fresh chat. This replaces "the operator isn't tracking it for now" and "open a new chat for each script".

### Operator decisions, 2026-10-21 (plumbing test run 02: emotion)

From the judge's report and three comparisons of test run 02 (`tests/iterations/iter-04/test-run-02/`). The operator: "your analaysis was strong and correct. this script was not bad but NOT UP TO SCRATCH." To apply in the next chat (`drafts/plumbing-emotion-and-cta-DRAFT.md`):
- **Simpler and stronger on emotion, all the way through:** "it doesnt necessarily mean giving the worst case scenario. it means using strong words and targetting the exact pain points of this audience like reference scripts do."
- **The villain comes back sporadically throughout,** not once.
- **Disgust at a big price, as an opinion:** "that is absolutely criminal they charge that much" (aimed at the price, never a named company or a motive).
- **Much more "but",** inside items and from item to item.
- **Reaffirm the title's and concept's emotions throughout.**
- **Questions to the viewer:** yes.
- **Roger is Classic** (no CTA markers): "YOU ARE RIGHT. ROGER IS CLASSIC I AM WRONG."
- **The hook:** an earlier ask for "more exagerations" was refined to the above; worst-case stakes are not the point.
- **Parts 3-5 of the draft, yes to each (session 6, 2026-10-21, asked once):** the list item shape (scene, what's happening, cost once, the turn, the fix, the win; about 100-130 words an item in lists of 10 or more; never more than two items without a bridge); Roger's and Mark's mid-video CTA in the shape their hits used (after item 2 or 3, about 60-80 words: aside, tied to the help, the book has the rest with pages, one benefit, link and QR code, return), which implements the locked "structure their hits used" above and replaces the pack's "20-60 words after the first payoff"; and all six of the judge's fixes (the number cap: one figure per item, figures on about half the items, one in the opening; straight quotes and a real scanner line, in the core; the plumbing pack's own SKILL.md under the copy guard; every gas-leak step; the trade-terms list; a myth flag names its belief). All applied to `plumbing-scripts/`, the two profiles and the core the same day.
- **After test run 03 (2026-10-21), the operator's answers to the judge's findings:**
  - Curly quotes: "ignore". Reading: no rule change and no new fix; judges don't hold them against a script. (The straight-quotes line from Part 5 stays in the core; ask before removing it.)
  - Item length: "his ones is fine if it runs a bit longer. as long as its not fluff." 100-130 words stays the guide; a bit longer is fine; no enforcement added.
  - Long sentences: no rule; "sentences can and should be joined SOMETIMES with But to keep a narrative flowing."
  - The opening's length, and the pack's example lines being echoed in short phrases: fine as they are.
  - The title's word and feeling: referred to more, "in one way or another", "not every item", never robotic or repetitive.
  - The mid-video CTA: "push it out a bit later": about a third of the way in, never before the end of item 3 (after item 4 or 5 in a list of 15).
  - The ending: "the outro call to action didnt actually say to comment. it was too abrupt." The comment ask now turns to the viewer, asks outright for a comment, then the question and "I read every one" (two or three sentences).
  - A named source keeps its exact figure, "only if the script names the source in it which shouldnt happen often".
- **Reading recorded:** where the item length and the 12-minute minimum collide (a list of 10 or 11 items), the minimum wins: items run a little longer with real value, never padding. The operator's "absolutely criminal" is limited to once per script so the outrage line is reworded each time.

### Operator decisions, 2026-10-22 (Frederick Barnes and Werner)

- **Werner Finkbeiner is stopped:** "werner is killed. dead channel now." His lines in the plumbing ideation skill (the German-way re-makes and his HVAC, energy, mold, pest and home-DIY probe lane) and in the thumbnails skill are not cleaned up yet; that waits for the operator's yes.
- **Frederick Barnes moves to broad home DIY,** no longer framed as a firefighter: "I guess we could turn frederick into a broad DIY guy"; "we wouldnt even really frame it to be like a firefighter anymore". Overlap with the plumbing channels is fine: "i dont care for overlaps."
- **His emotional targets are plumbing's,** on the Silver Cymbal model (asked for confirmation; the evidence is in `studies/plumbing/comparison/02-competitors.md` §2.1 and `05-emotions.md`). Not yet decided: his authority line now the firefighter framing is gone, the offer (the current book, *Prevent The Burning*, is fire-only), length, and the pack (a home-DIY pack modelled on the plumbing pack, after a competitor study).
- **Baseline saved:** his 23 pre-library scripts, views and an analysis are in `studies/home-diy/frederick-baseline-2026-10/`.

### Operator decisions, 2026-10-23 (two new channels)

- **Two new channels.** Both packs are built from the plumbing pack, and the work happens in two new chats running side by side:
  - **Roger the HVAC Guy:** "the only Roger-branded channel that we're going to be doing", picked for the closest audience fit. A new channel; "roger the pipe guy obviously carries on". The persona and niche rules stay "very similar to what Roger is right now", hitting the same triggers. A short competitor study comes first.
  - **Frederick Barnes, a new brand:** he moves from Just Stop Fire to electrical DIY, "how to be safe doing electric, avoid electricity mistakes, and fire prevention as well". This **replaces** the 2026-10-22 "broad home DIY" direction. The audience is shared with plumbing and HVAC, but "the emotions we trigger are different, and we're going to really focus on emotions".
- **Frederick's background is open:** "frederick background is up for debate". **His book changes** from *Prevent The Burning*; the new one isn't chosen.
- **Before the two chats start:** "deep and wide research on YouTube for channels in this niche", run with many helpers.
- **Repositories:** "keep niche reserach and scripting in seperate repos". The niche research (which niches, competitors, audience size, framing) lives in `KPMYT/niche-research`. The 2026-10-22 research was recovered there (`findings/2026-10-22-hvac-and-electrical.md`). The operator's plan: "we can setup 2 research chats under niche research, then we take findinds conclude them and move to working on the scripting in the other repo. (the niche research can also include building the ideation skills and the base ideation + thumb plans)". Whether a pack also needs a script transcript study here (`studies/<niche>/`) is for the scripting chats to ask.
- **Skills:** "never change skills without me knowing. or approving. you always default to me" (the standing rule, restated).

### Operator decisions, 2026-10-23 (Sawdust Sam relaunch)

- **Sawdust Sam relaunches as woodworking for profit, the old-world way:** "the same topics angles and spins as the normal woodworking for profit, but take an ancient approach to it... the core structure of the videos should be the same", with Sam's fascination with foreign and historic approaches and designs as a core part of his personality, "still very direct and very tutorial based". The draft is `drafts/sawdust-sam-DRAFT.md`; two parts of the ask wait on proposals P8 (history without sources) and P9 (proof from the plain product).
- **The keys:** "we will do a lot of japanese, forgotton, amish, asian - we will be testing more but those are the bulk."
- **The book stays as it is:** *The Old Ways* ("the book can remain as is"). Its author story (named mentors, trips, years) still never goes in a script; CTAs use only its contents. The library holds its text to printed page 80 only (Drive's extraction stops there and the 17 MB PDF is over the connector's download limit); CTAs cite nothing past page 80 until the rest is added.
- **P8 and P9 approved** ("p8 - yes", "p9 - yes"): heritage history may be general and hedged without a source, never invented specifics; a heritage build's money is proven by the plain product's listings. Applied in the woodworking pack ("Heritage builds"), the research pack template and a pointer in `core/research-and-sourcing.md`.
- **Talking Head** ("this is talking head now"), **the 8-minute floor** with length from the content ("4, - yes"), **swearing as the pack** ("we can hve it").
- **CTA: Hank's structure** ("same cta as hank we r gna hve as structure. there will be qr code"): two short CTAs, mid and end, each naming the QR code on screen and the top link in the description.
- **Overlap is fine:** "we are allowed overlap. this is never an issue." Hank and Dale may still run heritage titles; the pack's heritage rules apply to them too.
- **Ready (2026-10-24):** "is sawdust sam good to go": the profile is complete, so Sam is `ready` for the operator's test scripts; the tests decide any changes. Personal details: the operator kept "his coffee going cold while he reads about some old carving" and asked for more like it (five added, all about his pull toward the old ways). Ideation: simple builds only, single builds first, the operator's title formats, longer briefs (`ideation/woodworking-ideation/references/sam-old-world.md`). The operator built a separate `sawdustsamthumbnails` skill that names the channel "Sawdust Sam's Workshop"; the profile keeps "Sawdust Sam" (the YouTube name) until the operator says which.
- **Built 2026-10-23:** `personas/sawdust-sam.md` (status pending until the operator picks his personal details and a test run passes), `personas/books/sawdust-sam-book.md`, row 6 in `core/channels.md`, the ideation steering and thumbnail blocks, checks 40-42, the `sawdust-sam-persona` skill.

### Operator decisions, 2026-10-25 (the recent uploads review)

From the review of the seven newest uploads and two VA chats (`studies/recent-uploads-2026-10-25/`, `drafts/tts-hook-and-length-DRAFT.md`).
- **Every word is written the way the voice should say it, on every channel** ("agree with fix part 1"): lumber sizes in words ("two by four"), units and fractions in words, never two numbers side by side, no abbreviations or codes a person wouldn't say, no symbols, no laugh words, words with two pronunciations reworded. Whole-dollar prices stay digits (every recent voiceover read them correctly). Applied to `core/workflow.md` §4, the library's own examples, and a fix-on-sight `[SPOKEN]` family in the scanner (test 44). Sam's bench video had misread every lumber size the script wrote as "2x4" or "2x12".
- **No promise block in the plumbing hook (P10):** "in the hook of plumbing instead of saying 1 and 2 it owuld be better to say something like today i am going to show you the eight things you must check (if it doesnt already)". The opening's job 5 is now the count line: one sentence naming the whole list and what it does for the viewer, never what a single item holds, skipped when the opening already gave the count. *Reading recorded:* the operator's example began "today I am going to", which the plumbing scanner bans in openings; the rule's example drops "today" ("I'm going to show you the eight things you need to check..."), and the ban stands. Named promises stay allowed in the body (P3's forward lines). Applied to `plumbing-scripts/SKILL.md` and its unit plan template (test 45).
- **Plumbing words per minute: not changed yet** ("do not change 3 yet"). The profiles stay unset, so the 12-minute minimum is still counted at 150 words a minute while the voices run about 167 to 190.
- **VAs don't ask for a length** ("tell VAS NOT to ask for length"). Length comes from the content, with the niche minimum; a script that passes is uploaded as it is. Sam's bench chat had passed at about 9.7 minutes before the VA asked for "14-16 MINS".
- **The voiceover copy's tags stay as they are** ("the VO copy tags sound fine for now. leave as is").
- **Sawdust Sam goes into `main`** (the 2026-10-23/24 branch `claude/determined-darwin-3u43bh`, already on the account).


### Operator decisions, 2026-10-27 (the electrical pack and Frederick Barnes)

- **Frederick Barnes is the electrical channel** ("we will do frederick for this"); Jack Redfield stays pinned as a possible second lane (niche-research `studies/electrical/`). **35 years** in the trade. **No book for now:** "CTA will literally just be a very short subscribe one". **Talking Head** script type.
- **Build the pack like plumbing, with electrical's own formats, emotions and reference scripts;** "core structures can be taken from plumbing as long as the necessary changes are made"; every variable reviewed in detail by checker subagents; "all our problems we faced in our plumbing and woodowrking script iteration sessions of scripting. account for them from now" (`studies/electrical/lessons-for-the-pack-2026-10-27.md`).
- **Model scripts:** "from the winners in recent months/years from the real channels that have over 1m views" (`studies/electrical/model-picks-2026-10-27.csv`).
- **Length:** "even 15-22 is sweet spot" (read as: the minimum stays 12 minutes, as plumbing; 15 to 22 is where to aim).
- **Villain:** "villain does not need to be necessary": used only where it fits.
- **Agreed as proposed (2026-10-27):** the brief can add safety but never remove power-off, verify-dead or the call-an-electrician line; named panel brands only with what CPSC or inspectors actually say; no "after all the houses I've worked in" lines, the tenure at most once; no swearing.
- **P11, the opening may carry one value promise** (an escalation, or "by the end of this video you'll know X and Y", never the first items in order): see `PROPOSALS.md` P11. Electrical only.
- **Confirmed later the same day:** the 12-minute minimum with 15 to 22 the aim ("ok to 1"); the ending, a one-line subscribe ask then the comment ask last, as plumbing's P5 ("ok to 2, anad we say we read every comment": the comment line says he reads every comment). Default kept, not asked: the research pack is not used (the brief and the facts guide are the fact source).

### Operator decisions, 2026-10-27, the electrical scripting chat (session 9): answers to E1-E6 and P12

Asked as multiple choice; the operator picked:
- **E1, P13's core checker fixes: "Yes, apply all".** The tenure bug (words and electrician phrasing), number words in the fact check, letter sets and two-way words judged once with a count ("live" added), the "3-in-1" false positive, voice tags in the script are fix-on-sight, `--final` fails a script under the length minimum, the scanner's ITEMS and SENTENCES report, `tools/verify_output.py` (run by the main session on every saved test output before the judge), the core evidence block's quoted lines (Items, Sentences, I-verdicts, Turns, Title word; every quote copied from the script), and **no sentence over 35 words on every channel** (fix-on-sight).
- **E2, numbers in words: "Yes, words".** Electrical writes volts, amps, watts, wire and cable sizes and plug codes in words; years stay digits (overrides row in the electrical pack).
- **E3, titles with another years figure: "No, title wins".** P13 item 7 is rejected: the locked "title numbers win" rule stands for Frederick too (a "30 years" title means 30 in that script).
- **E4, named companies: "Yes to both".** Offer rules §5's named-company ban covers CTAs, pitches, descriptions and pinned comments; in the body, named companies follow the claims policy. Federal Pacific's independent test results may be said with the source named (facts guide 9.15).
- **E5, Frederick's voice: ElevenLabs** (voice name and ID not given yet). **"Mark ready, check later"**, as Sam on 2026-10-24: Frederick is `ready`; the voice-check paragraph is in his profile for the operator to generate and report back.
- **E6, the electrical ideation skill's "after all the houses I've worked in": "No, leave it".** The script pack's scanner still bans the line.
- **P12, "doesn't X. It Y." as the one reframe: "No".** H21 stays as it is.
- **The eight library fixes from electrical test run 01** (`tests/iterations/iter-05/test-run-01/judge-report.md` L1-L8): the operator, "answer the questions yourself based on what you think is best". Claude said yes to all eight: the prove-dead order at a device (every tester checked live before and after; the plug-in tester seen lit before the breaker goes off; two-slot outlets; plate off, reachable terminals, device eased out, then every wire in view); look inside before the shopping step in any swap; the pack's plug and outlet example lines moved to other topics, with a 5-word guard on the pack's quoted example sentences (`example-guard: 5`); at least one sentence of six words or fewer per item and 12% across the script (the punctuated models' middle); "I" lines with the box open only as the stop-sign verdict or after the test; the first-item mark at 45 seconds for fix and how-to (lists still aim at 30); no "first, second, third" inside a numbered step; "lives" as a two-way word (core). Revisit any of these on the operator's word.
- **The electrical model library (2026-10-27):** the operator confirmed the models as structure only ("as long as they are structure only thats fine"; "good" to the unsafe on-camera parts being labelled banned) and removed six: those before 2022 ("remove the ones older than 2022": E08, E12, E17, E23, E38) and the science hobbyist ("remove the science one": E20). 31 models remain, all 2022 on; the six are kept in `studies/electrical/models-removed-2026-10-27/`. A14 (the LED glow) has no topic model now: the closest explainer is used.

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

- **The scanner's number check matches values, not meanings.** "40 pieces" can match a $40 price. For plumbing it reads the brief and the price guide together, and the guide holds so many figures that an invented price near any of them passes: the audit's D4 (each price named to the brief or the guide row) is the real check.
- **Facebook Marketplace's fee for shipped orders** isn't settled in published sources. The research pack must verify it every time.
- **No real end-to-end run has happened yet.** Persona profiles and the research stage don't exist yet.
