# Script System: what's in each file

The whole system is one library. `core/` holds the rules every channel uses. Each niche gets its own pack (so far, `woodworking-scripts/`, `plumbing-scripts/`, `electrical-scripts/` and `hvac-scripts/`). Each channel gets a persona profile in `personas/`. Typing **START** runs `core/workflow.md`, which pulls in everything else.

## core/ (every channel)

| File | What's in it |
|---|---|
| `workflow.md` | **The entry point.** START, picking the channel, the input gate (refuses to write until every input is valid), the run with no questions, the Vidrush script format and Talking Head markers, the output layout, the ElevenLabs voiceover copy, and the NOT READY rule. |
| `channels.md` | The channel list START shows, with each channel's niche pack, persona profile and status. |
| `persona-profile-template.md` | The blank template for each channel's settings: persona, script type, voice provider, CTA setup and offers. |
| `claims-policy.md` | What a persona may and may not claim: opinions yes, checkable life facts no; no health claims, guarantees, or false facts about named companies. |
| `offer-rules.md` | How any offer (e-book, email list, affiliate, subscribe) may be talked about: facts only from the profile, an added-value promise, price-silent paid products. |
| `cta-and-endings.md` | CTA mechanics (placement after the first payoff, what every CTA contains) and how videos end: the CTA or nothing, then one closing line. |
| `humanizer.md` | The 23 "AI tells" (H1-H23), the hard-ban list (including retention teases), the "use sparingly" phrases, and the clean-up procedure. |
| `voice-anchoring.md` | How scripts are matched to real human narration, the sentence-by-sentence shape test, and the four written-not-spoken tells. |
| `retention-mechanics.md` | Holding attention: the first seconds, the line after the hook, the progression test, short rehooks, list order and pacing guides. |
| `variety-rotation.md` | Keeps scripts from sounding alike: nine rotating slots (move and wording), the rotation log line, and the cross-script rules. |
| `research-and-sourcing.md` | The research stage's rules: facts versus allowed framing, verify-or-cut, evidence wording, freshness, the verification pass, the default research pack, and flagging titles back to ideation. |
| `script-structures.md` | Fallback structures for niches without their own: list, how-to, why it happens, comparison, essay, transformation. Plus the hook options. |
| `greenlight-audit.md` | The final quality gate: checks A-F, three verdicts, the three-round cap, and the evidence block. |
| `script-scanner.py` | The program that mechanically checks a script: banned phrases (including retention teases), dashes and odd characters, forms the voice misreads (2x4, 8 ft, 3/8, 19%, symbols, KD19, "haha"), production notes read aloud ("CTA", "stinger", "mid-roll", "continuing with the final sections"), the same sentence twice in a row, the persona's fixed facts from its profile (a different years-in-the-trade figure, a near-miss of the channel, persona or book name), the script talking about its own thumbnail or title (judged), niche bans, filler counts, echoes, numbers missing from the research pack, and (with `--refs`) any run of 8+ words copied from the niche pack's reference files. |

## woodworking-scripts/ (the woodworking niche pack)

| File | What's in it |
|---|---|
| `SKILL.md` | All woodworking-for-profit rules: inputs, freshness, viewer, skeleton, steps, length, heritage builds (old-world styles: heritage beats, general hedged history, proof from the plain product; 2026-10-23), money math, proof, where to sell, safety, voice, AI-visual writing, banned list, scanner rules. |
| `references/research-pack-template.md` | What a woodworking research pack must contain. |
| `references/unit-plan-template.md` | The plan filled in before writing, so length comes from the content. |
| `references/voice-samples.md` | Three real narration samples from winning competitors: the voice anchor. |
| `references/excerpts.md` | Winning competitors' lines in 15 groups by job (10-15 each), each marked as usable, rewrite or doesn't transfer. |
| `references/reference-scripts.md` | Eight complete winning scripts, labelled with the skeleton, each with why it works, the unit plan it implies and what doesn't transfer. Read at the planning step; never copy wording. |
| `archive/` | The full BeardedViking and WhosTheVoss transcripts, plus `most-viewed-24mo/` (each channel's 10 most-viewed from the last 24 months, with views and normal), used for calibration only. |

## plumbing-scripts/ (the plumbing niche pack)

| File | What's in it |
|---|---|
| `SKILL.md` | All plumbing rules, approved by the operator (2026-10-21): where the pack overrides the core (one table), inputs (title and brief; no research pack), the viewer, the villain (all the way through, with disgust at big prices), the opening, emotion all the way through, point then promise, promise devices, the ten video types with their models and the list item shape, using the models (never a copy), CTAs (Roger's and Mark's six-part mid-video ask after item 2 or 3), the ending (comment line last), length (12 minutes minimum), voice, proof, money framing, safety (the brief wins), the banned list, the scanner block and the before-handing-over checklist. |
| `references/unit-plan-template.md` | The plan filled in from the title and brief before writing, with MODELS and EMOTION blocks. |
| `references/price-guide.md` | Typical US prices (October 2026) for about 140 jobs, parts, damage costs and shelf items, plus the safety facts and settings, each marked confirmed, adjusted, thin or "in words". Researched by four helpers and re-checked by four others against different sources; the evidence is in `studies/plumbing/price-research-2026-10/`. The script uses it for any price the brief doesn't give, always as an estimate. |
| `references/voice-samples.md` | Three verbatim stretches of real human narration (Got2Learn, Silver Cymbal, Roger Wakefield): the voice anchor. |
| `references/excerpts.md` | 204 lines in 16 groups by job, tagged [real] or [structure only], with source, timestamp and views against normal. |
| `references/models/` | 39 model files, each a beat map plus the full labelled script, why it works and what doesn't transfer: R01-R20 the real channels (structure and voice), S01-S18 our hits and TheCheapFix (structure only), and R21, a drywall repair video (not plumbing) kept for two opening moves only (the problem introduced clearly, the escalation explained simply), with no script and no beat map. `INDEX.md` sorts them by video type. |
| `archive/` | The four real channels' transcripts (Silver Cymbal, Roger Wakefield, Got2Learn, Arrow Pest Service). Calibration only; not in the installed skill. |
| `model-file-spec.md` | How the model files were built, for adding models later. Not in the installed skill. |

## hvac-scripts/ (the HVAC niche pack, built 2026-10-27)

For Roger the HVAC Guy. Built from the plumbing pack (as installed on the account, with the escalation line) and changed only where HVAC differs, on the evidence of the HVAC study (`studies/hvac/`) and the operator's answers of 2026-10-27 (`HANDOFF.md` §3). Every reference is a real person on camera (operator: "we dont want any ai or faceless for reference").

| File | What's in it |
|---|---|
| `SKILL.md` | The HVAC rules: the overrides table (the plumbing pack's, carried over), inputs (title, brief, rotation log), the viewer (from 1,483 HVAC comments), the villain (the trade's prices, the upsell and the silence; never the honest tech), the opening (the breakdown moment and the escalation line as options), emotion all the way through (plus the HVAC feelings: the clock, the dial that won't reach, comfort, the machine's sounds), point then promise, the video types and item shape (about 150-250 words an item), the models, CTAs (no book for now), the ending, length (12 minutes), voice (HVAC spoken forms), proof, money framing, the HVAC safety defaults (gas leak and carbon monoxide every step), the banned list (with the faceless leader's catchphrases) and the scanner block. |
| `references/unit-plan-template.md` | The plan, with season and system-scope lines and the HVAC safety defaults. |
| `references/voice-samples.md` | Three provisional voice stretches from real tradesmen on camera (The Funny Carpenter, Word of Advice TV, Silver Cymbal), until the operator listens and picks. |
| `references/excerpts.md` | Real HVAC lines grouped by job, from real people on camera only. |
| `references/price-guide.md` | HVAC prices and the safety facts, two-source checked (research in `studies/hvac/price-research-2026-10/`). |
| `references/models/INDEX.md`, `R04-...md` to `R44-...md` | The model library (built by `tools/build_hvac_model_index.py`): HVAC winners from R22 on, and ten plumbing and home-repair models kept from the plumbing pack. |
| `model-file-spec.md` | How the HVAC model files are built (not part of the skill). |
## electrical-scripts/ (the electrical niche pack)

Built 2026-10-27 for Frederick Barnes from the plumbing pack, with electrical's own formats, emotions and models (research in the niche-research repository, `studies/electrical/`). Reviewed by seven checkers (2026-10-27; reports in `studies/electrical/pack-review-2026-10-27/`); Frederick's status stays pending until his voice provider is confirmed.

| File | What's in it |
|---|---|
| `SKILL.md` | All electrical rules: where the pack overrides the core, inputs (title and brief; no research pack), the viewer, the stakes (no money: fire and shock as stakes, never the topic), the villain (optional), the opening (with P11's one value promise), emotion all the way through (pride and capability first), point then promise, the seven video types with the item and step shapes and their models, using the models, the CTA (one-line subscribe ask, NO BOOK markers), the ending (comment line last, "I read every one"), length (12 minutes minimum, 15 to 22 the aim), voice (units and wire sizes written for the voice), proof, safety (the brief can add, never remove), the banned list, the scanner block and the checklist. |
| `references/unit-plan-template.md` | The plan filled in from the title and brief before writing, with MODELS, EMOTION, FACTS and SAFETY blocks. |
| `references/facts-guide.md` | Well-established US electrical facts (code rules, sizes, safety facts, the emergency steps, the terms to explain), each marked confirmed, adjusted, one source, reading or thin; researched and re-checked by two helpers (evidence in `studies/electrical/facts-research-2026-10-27/`). No prices. |
| `references/voice-samples.md` | Verbatim stretches of real human narration from the models: the voice anchor. |
| `references/excerpts.md` | Real lines from the models grouped by job, with model ID and timestamp. |
| `references/models/` | 31 model files (E01-E37, no E06; E33-E37 added after review R3; E08, E12, E17, E20, E23 and E38 removed 2026-10-27 to `studies/electrical/models-removed-2026-10-27/`): real channels, 1M+ views, all 2022 on; each a beat map, emotion voicing, why it works, the full labelled script and what doesn't transfer. `INDEX.md` sorts them by video type. |
| `model-file-spec.md` | How the model files were built. Not in the installed skill. |

## style-scripts/ (the hair-and-fashion niche pack, built 2026-10-29)

Built for Scarlett Starling and Diane de Chambray from the style study (`studies/style/`) and the approved diagnosis (`drafts/style-pack-diagnosis-DRAFT.md`): one pack for hair and fashion for women over 50; makeup is a separate pack later. Both channels are pending (the operator's voice-sample listen, the book texts, a test run).

| File | What's in it |
|---|---|
| `SKILL.md` | All style rules: where the pack overrides the core, inputs (title and brief; no research pack), the viewer (median age 70), the villain (optional; never the salon), the opening (the title's promise word early, item one by about 45 seconds), emotion built from this niche (practical fixes for emotional problems, a feeling in about a quarter of items, permission never as a slogan, the why as the relief, the flagged hard word) with hair and fashion notes, point then promise, the eight video types and the item shape, using the models, the book as the only CTA, the ending (the comment ask about her, no sign-off), length (12 minutes minimum, 12 to 16 the aim), voice (French words written for the voice), proof, money (prices only on budget titles), the six safety defaults (the brief wins), the banned list, the scanner block (tested on 105 transcripts; `title-words`) and the checklist. |
| `references/unit-plan-template.md` | The plan filled in from the title and brief before writing, with MODELS, OPENING, ITEMS, EMOTION, SAFETY and CTA blocks. |
| `references/hooks.md` | The hook bank: every model's hook up to item one (verbatim for the real presenters, moves only for the faceless), its moves, words, seconds to item one, the feeling it aims at and whether a persona can use it; what the winners' hooks share. Every script's hook carries one of these formats. |
| `references/excerpts.md` | 81 real lines in 14 groups by job (the hook's first line, the why, the turn, the swap, the check, feeling lines, permission, the blame moved off her, the flagged hard word, bridges, comment asks, the honest limit). |
| `references/voice-samples.md` | Four stretches of real women's narration (Tracy Campoli, Melissa Murrell, Marie-Anne Lecoeur, Diana GOSS), **provisional** until the operator's listen. |
| `references/models/` | Model files: 30 real presenters (M01-M30: structure, voice and emotion) and 7 faceless or AI videos (F01-F06, F08: structure only), each a beat map, emotion voicing, why it works, the labelled script, lines worth studying and what doesn't transfer; `INDEX.md` by video type. Picks in `studies/style/models/approved-models.csv`. |
| `model-file-spec.md` | How the model files are built. Not in the installed skill. |

## ideation/

Copies of the operator's claude.ai ideation skills, brought in to be edited here with the operator's approval. The operator uploads the edited version back to claude.ai.

| Folder | What's in it |
|---|---|
| `woodworking-ideation/` | The woodworking ideation skill, edited 2026-10-20 (Hank and Dale) and 2026-10-23 (Sawdust Sam relaunched: old-world builds for profit, steering §3, his thumbnail block and `references/sam-old-world.md`: simple builds only, his title formats, longer briefs): all on camera, single builds, titles may exaggerate freely, and the new for-profit pipeline in `references/pipeline.md` (Etsy-first product scan of 30, title and thumbnail-text options, picks, fact-bank briefs, optional research pack). It's an overlay on `ideation-core`. |
| `plumbing-ideation/` | The plumbing ideation skill, copied from the account 2026-10-21 and edited: Mark's fixed 40 years, Vintage's 45, "Finkbinder" corrected to Finkbeiner (outside the archive), and a brief rule so every item carries its cost and the right way. An overlay on `ideation-core`. |
| `ideation-core/` | The shared ideation base (format bank, rules, audience profiles), an unchanged copy kept so it can be installed on VA accounts. Not edited. |

## tools/ and dist/

| File or folder | What's in it |
|---|---|
| `tools/build_skills.py` | Builds the installable skills from the library into `dist/` (one `.skill` file each, `script-writer` also as a `.zip`, plus the full bundle as one zip). Run it after any change, then re-upload. |
| `tools/verify_output.py` | Re-counts a saved script output against its own AUDIT EVIDENCE block: curly quotes against "mechanical n", words against Length, items and sentences, and every quoted evidence line against the script (P13, 2026-10-27). The main session runs it on every test output before the judge. |
| `tools/verify_plumbing_models.py` | Checks every plumbing model file's labelled script against its study transcript, word for word (session 4). |
| `tools/verify_hvac_models.py`, `tools/build_hvac_model_index.py` | The same check for the HVAC model files, and the builder of the HVAC model index (2026-10-27). |
| `dist/` | **Generated, never edited by hand.** One skill per layer: `script-writer.skill` (the core, START), `woodworking-scripts.skill` and `plumbing-scripts.skill` (the niche packs), `hank-hardwood-persona.skill`, `dale-oakfield-persona.skill`, `roger-the-pipe-guy-persona.skill` and `mark-silverbridge-persona.skill` (profile plus book), `vintage-pipefitter-persona.skill` (profile only), `woodworking-ideation.skill`, `ideation-core.skill`; the unzipped folders; `script-writer.zip` (the same skill as `script-writer.skill`); and `INSTALL.md` (how to install them, not itself a skill). The build checks claude.ai's upload rules (one SKILL.md, frontmatter, name, description up to 1,024 characters). |

## personas/

One persona profile per channel, written from `core/persona-profile-template.md`.

| File | What's in it |
|---|---|
| `hank-hardwood.md` | Hank Hardwood's profile: settings, his ten shop details, the approved personality, and the CTA rules (two short CTAs to the QR code, with book pages when the video's build is in the book). |
| `dale-oakfield.md` | Dale Oakfield's Workshop's profile: settings, the grandfather detail, the approved personality, the Bertha-style CTA rules, and his ending. |
| `books/hank-hardwood-book.md` | The full text of Hank's ebook, "100 Ways to Make Your First $1,000 with Woodworking", with a marker for every page (PDF page and printed page), a chapter page map and an index of all 100 builds. Used to find which pages cover a video's topic for the CTA, and which facts a CTA may state about the book. |
| `books/dale-oakfield-book.md` | The same for Dale's ebook, "The Ultimate DIY Woodworking Guide", with a chapter page map (the book prints no page numbers, so it uses PDF pages). |
| `sawdust-sam.md` | Sawdust Sam's profile (built 2026-10-23, **pending** until his personal details are picked and a test run passes): woodworking for profit the old-world way (every video a heritage build), Talking Head, 174 words a minute, the Jon voice, Hank's CTA structure (two short CTAs naming the QR code and the top link) for *The Old Ways*, and scanner bans on invented trips, encounters and teachers. |
| `books/sawdust-sam-book.md` | The text of Sam's book *The Old Ways* to printed page 80 (all Drive's extraction gives), with a chapter page map, the secrets by style (Japanese, Amish, Chinese and the rest) and a secret index; CTAs cite nothing past page 80. |
| `frederick-barnes.md` | Frederick Barnes's profile (built 2026-10-27, **pending** until the voice provider is confirmed, then ready so the operator's test scripts can run, as Sam's was; the tests decide any changes): home electrical, retired electrician, 35 years, Talking Head, 195 words a minute, no book (a one-line subscribe ask in NO BOOK markers), voice to confirm, scanner bans on the name intro, the old firefighter framing and invented personal details. |
| `werner-finkbeiner.md` | Werner Finkbeiner's profile (relaunched 2026-10-27, **ready** the same day; channel row 9): plumbing the German way, 30 years, Talking Head, the Herrmann voice, no contractions, his German background (P14) and two soft details, a quick mid-video CTA for *Werner's 101 Free Repairs* built on a fixed trade-mentor line, no subscribe ask, the comment line last, the German-way rules (every German claim from the brief, hedged; the American fix; no euros), and scanner bans on his old intro, teases and recaps, relatives, hometowns, arrival stories, credentials and comedy German. |
| `roger-the-pipe-guy.md`, `mark-silverbridge.md`, `vintage-pipefitter.md` | The three plumbing profiles, approved 2026-10-21, ready since the plumbing pack entered the library: settings, voices, fixed tenures 45/40/45, the personality kept close to Notion, CTA rules (Roger and Mark: a short mid-video book ask and a one-line end reminder, naming the link and the QR code; Vintage: a one-line subscribe ask), and scanner blocks (Mark's also bans contractions). |
| `roger-the-hvac-guy.md` | Roger the HVAC Guy's profile (2026-10-27; **ready** after two rounds of tests, `tests/iterations/iter-06/`): Roger the Pipe Guy's profile with only the trade changed (the same man and voice, 45 years), no book for now (a one-line subscribe ask), his filter check on the first of the month, and a ban on the other Roger channel's name. Roger the Pipe Guy's profile carries the matching ban. |
| `books/roger-the-pipe-guy-book.md`, `books/mark-silverbridge-book.md` | Roger's "100 Old-House Fixes That Save You Thousands" (124 pages, 100 fixes) and Mark's "50 Easy Plumbing Fixes That Will Save You $10,000" (122 pages, 50 fixes), with printed page markers, chapter maps and fix indexes. |
| `books/werner-finkbeiner-book.md` | An index of Werner's *Werner's 101 Free Repairs* from the operator's paste (2026-10-27): the chapters and every repair with its page and Money Saved, not the full text. |
| `scarlett-starling.md` | Scarlett Starling's profile (2026-10-29, **pending**; channel row 10): hair and fashion for women over 60, Talking Head, 169 words a minute, no age, years or career, one numberless credential line, the name never spoken, *300 Budget-Friendly Ways to Look Expensive* as the only CTA (once mid-video, a one-line end reminder), no sign-off, and scanner bans on her old intro, sign-off, no-rush close, provenance line and comment ask. |
| `books/scarlett-starling-book.md`, `books/diane-de-chambray-book.md` | Indexes of the two style books from OCR of the operator's image-only PDFs (2026-10-29): *300 Budget-Friendly Ways to Look Expensive* (28 chapters, 300 Ways, five titles unreadable and described) and *The French Way* (an introduction, ten chapters and a conclusion, 101 Secrets), each with the chapter page map, every item with its PDF page, the facts a CTA may state, and the book's own stories and characters, which never go in a script. |
| `diane-de-chambray.md` | Diane de Chambray's profile (2026-10-29, **pending**; channel row 11): the French way for women over 60, Talking Head, 172 words a minute, the Sylvie voice, one heritage line ("the way I was raised in Paris"), the French-lens rules (every claim from the brief or the documented staples, hedged; the American fix; no invented customs; French words written for the voice), *The French Way* as the only CTA, no sign-off, and scanner bans on her old intro, sign-offs, unhedged claims and the book's unconfirmed count. |

## studies/

Research data: collect and describe only, never edited to fit a conclusion.

| Folder | What's in it |
|---|---|
| `woodworking/` | The woodworking-for-profit study (2026-10-17): Hank, Dale and two competitors, 45 videos. Transcripts, comments, views against each channel's normal, one descriptive notes file per video, and combined transcripts. Method in `study-brief.md`, every step in `log.md`. |
| `plumbing/` | The plumbing study (started 2026-10-20): Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter and five competitors (one a pest-control parallel niche, one an AI channel), 5 most recent plus 5 most-viewed (last 24 months) per channel. Same layout and method as woodworking; see its `study-brief.md` and `log.md`. Got2Learn's second group is its all-time top 5 (it stopped uploading). `price-research-2026-10/` holds the price research and re-checks behind the plumbing price guide. `comparison/` holds the analysis: measured numbers, own hits against recent uploads, competitor profiles, a side-by-side on 12 dimensions, and a summary with suggestions for the plumbing script rules (none applied). |
| `electrical/` | The electrical pack's own study files (2026-10-27): `model-picks-2026-10-27.csv` (the 38 picked model videos, E01-E38), `transcripts/` (raw NexLev transcripts behind the 37 model files built, the six later removed included), `lessons-for-the-pack-2026-10-27.md` (99 problems from the plumbing and woodworking script tests and how each was fixed: the checklist the electrical pack is reviewed against), `facts-research-2026-10-27/` (the facts guide's research and re-check notes) and `models-removed-2026-10-27/` (the six model files the operator removed from the library on 2026-10-27, five posted before 2022 and one science-hobbyist channel, with a README saying why). The niche research itself is in the niche-research repository. |
| `recent-uploads-2026-10-25/` | The newest upload on each of the seven channels (Roger twice), 2026-10-25: the caption transcripts (what the voice really said), lengths and views, before-and-after video lengths per channel, and the main session's analysis (the voice's misreads, the plumbing promise blocks, a review against the studies, and the average view duration question). |
| `recent-uploads-2026-10-29/` | Werner's and Frederick's first uploads since their 2026-10-27 relaunch, 2026-10-29: the caption transcripts (plus Werner's older video on the same topic), lengths, views and words a minute, and the main session's review of both against their packs and profiles, with eight candidate fixes for the operator's yes. |
| `hvac/` | The HVAC script and comment study (started 2026-10-27) for the Roger the HVAC Guy pack: 37 proven HVAC videos picked by video type (real people for voice and structure, faceless channels such as Ray Dutton's Garage for structure only, and Roger the Pipe Guy's own AC drain video). Transcripts, comments, views against each channel's normal and one descriptive notes file per video. Method in `study-brief.md`, the selection in `inputs/videos.md`, every round in `log.md`, the round 1 check in `check-round1.md`. `comparison/` holds the analysis (the viewers, the measured openings and numbers, the body, safety and CTAs, models and voice) and a `README.md` with the main findings and 12 suggestions for the HVAC pack (none applied). |
| `hvac/price-research-2026-10/` | The evidence behind `hvac-scripts/references/price-guide.md` (2026-10-27): the job lists (`jobs.md`), four first-pass researchers (`A-research.md` to `D-research.md`) and four second-pass checkers using other publishers (`A-verify.md` to `D-verify.md`), with every source, date and verdict. `README.md` explains the method, the counts and the brief figures that didn't hold up. |
| `hvac/pack-diagnosis-2026-10-27/` | Two helpers' notes behind the HVAC pack diagnosis (2026-10-27): `references-and-models.md` (the plumbing models, voice samples, excerpts, price guide and unit plan checked for HVAC; HVAC model candidates by video type with IDs and views; a seed list of HVAC prices from batch 1's briefs) and `wiring-scanner-checks.md` (every place a new pack and channel is plugged in, the scanner run on HVAC wording, the two Rogers' name check, and the clashes with the plumbing and electrical branches). Read-only research; nothing applied. |
| `home-diy/frederick-baseline-2026-10/` | Frederick Barnes before the library (2026-10-22): his 23 scripts as written with the old system (verbatim, from Drive), which became which video and the public views (one 434k hit, the rest 23 to 5.3k), counts per script, the scanner's output and the main session's analysis against the library. The baseline for his move from home security and fire prevention to home DIY. |
| `plumbing/werner-baseline-2026-10/` | Werner Finkbeiner before the library (2026-10-27): his 14 scripts as written with the old system (verbatim, from Drive), which became which video with lengths and views (10 to 1,000; 11 subscribers), counts per script and the scanner's output. The baseline for his relaunch. |
| `style/` | The style niche study (started 2026-10-28) for Scarlet Sterling and Diane de Chambray: hair and fashion for women over 50, with makeup and skincare scanned as adjacents. `own-baseline-2026-10/` holds both channels' uploads, transcripts, comments and notes; `discovery/` the scoping scrape (real and faceless channels, one raw file per lane); `round2/` the finished screen (236 channels kept), 2,478 outliers and `BREAKOUT-MAP.md`; `inputs/` the operator's list and the 45 study videos; `data/` and `notes/` the study videos' transcripts, comments and notes; `comparison/` the analysis and `README.md` (findings and 14 suggestions, none applied), `07` the emotions and age brackets, `08` hair against fashion (2026-10-28, session 13); `models/` the model candidates, `approved-models.csv` (M01-M30 real presenters, F01-F08 faceless structure-only, F07 dropped; all collected into `data/` and `notes/`) and the item-list search; `pack-diagnosis-2026-10-28/` the two helper sweeps behind the pack diagnosis (`library-sweep.md`, `persona-sweep.md`). Method in `study-brief.md`, every round in `log.md`. |

## drafts/

Drafts waiting for the operator's yes go here; nothing in it is part of the library until it's approved and moved. Now: `style-pack-diagnosis-DRAFT.md` (2026-10-28, session 13): what the one hair-and-fashion pack and the Scarlett Starling and Diane de Chambray profiles keep, adapt and add from the core and the plumbing pack, the hair and fashion emotion comparison, the scanner gaps, the reference material, the order of work and 23 questions with recommendations (nothing applied). `style-study-plan-DRAFT.md` (2026-10-28): the plan for the style niche study (Scarlet Sterling and Diane de Chambray), phases and six questions, waiting for the operator's yes. `hvac-pack-diagnosis-DRAFT.md` (2026-10-27): what the HVAC pack and Roger the HVAC Guy's profile keep, adapt and add from the plumbing pack and Roger the Pipe Guy's profile, section by section, the scanner gaps HVAC hits, the order of work and 11 questions for the operator (nothing applied). `werner-relaunch-DRAFT.md` (2026-10-27), the Werner relaunch: what was built, his old scripts against the library, and twelve questions (W1-W12) with proposals P14-P16; answered and applied the same day (Werner ready), kept as the record. `tts-hook-and-length-DRAFT.md` (2026-10-25): Parts 1 and 2 applied the same day (writing every word for the voice; a count line in place of the plumbing promise block, P10); Part 3, the plumbing words per minute, waits. `sawdust-sam-DRAFT.md` (2026-10-23), the Sawdust Sam relaunch draft, applied the same day except his personal details (question 8), which wait for the operator's pick; kept as the record of the questions and evidence. The plumbing emotion draft was applied on 2026-10-21 (in git history). The plumbing pack itself moved into `plumbing-scripts/` on 2026-10-21.

## tests/

`run_checks.py`: automated checks across the whole library (72 numbered checks at the 2026-10-27 merge), including the copy guard, the fraction-word scanner check, the "e-book" ban on every profile, and the plumbing pack (its inputs, scanner block, Mark's contraction ban, the copy guard over its own SKILL.md and every model file, the emotion rules, item shape, CTA template and number cap, the plumbing profiles and the channel list), and the core's straight-quotes and real-scanner-line rules, the written-for-the-voice scanner check (44), the plumbing count line in place of the promise block (45), the electrical pack and Frederick (46-52), the P13 core checker fixes (53-57: tenure in words, number words, letter sets once, voice tags, the 35-word sentence limit, `--final`, the ITEMS and SENTENCES report, `verify_output.py`), the electrical test fixes (58, 59 and 69), the plumbing escalation line (46b), Werner's profile and book index (70), the HVAC test answers (71: `require-if`, every carbon monoxide and gas-leak step; 72: the reframe split across two sentences), and the HVAC pack (60-68: file references, its inputs and scanner block, tenure in HVAC words, letter words, the two Rogers' name bans, real-people-only models with the copy guard, the channel row and build entries, the price guide). Run it after any edit.

## tests/iterations/

One folder per round of changes (`refs-01/`, `iter-00/`, `iter-01/`, …), each with `CHANGES.md` (file | what changed | why) and `before/` copies of every file it modified. `iter-01/` is the first real script test (Hank, the lazy Susan): its inputs and output in `test-run/`, the findings and the operator's decisions in `REVIEW.md`. `iter-06/` (TEST, 2026-10-27) is the first HVAC test: Roger the HVAC Guy, batch 1 #4 and #14, two rounds (runs 01-02, then 03-04 after the fixes), each with the chat, output, script, the main session's scanner run and a judge report; `CHANGES.md` holds the findings, the fixes and the questions for the operator; `judge-rubric.md` and `refs/` are the judge's.

## SESSION-HANDOVER.md

The live note between Claude Code chats: where the last chat stopped, operator decisions, the active channel list, open questions and the next actions. Rewritten at every handover.

## PINNED.md

The to-do list, the decisions made, the decisions still open, and the data to pull.
