# Script System: what's in each file

The whole system is one library. `core/` holds the rules every channel uses. Each niche gets its own pack (`woodworking-scripts/`, `plumbing-scripts/`, `hvac-scripts/`, `style-scripts/` and `electrical-scripts/`). Each channel gets a persona page in `personas/`. Typing **START** runs `core/workflow.md`, which asks for the channel and pulls in everything else.

**P21 (applied 2026-11-06 for style, plumbing, HVAC and woodworking; operator: "yes use defaults"):** those four packs are now the simple version: `SKILL.md` (the steps), `check.py` (the hard-rules check) and `references/` (real model transcripts, plus the price guide or the research-pack template), and each of their channels has a one-page persona page. For these channels the pack replaces `core/workflow.md` sections 2 to 6 and the other core files. Electrical keeps the full core way. The old packs and profiles are in `archive/pre-p21-2026-11-06/`. Sawdust Sam is dropped (operator, 2026-11-06).

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

## woodworking-scripts/ (the woodworking niche pack; P21, 2026-11-06)

| File | What's in it |
|---|---|
| `SKILL.md` | The steps for the woodworking-for-profit channels (Hank Hardwood, Dale Oakfield's Workshop): inputs, NOT READY, the video type and its model, write, read aloud, check, the output. The research pack is still a required input (operator default, 2026-11-06). |
| `check.py` | The hard-rules check (no counts to meet): `python3 check.py SCRIPT --channel hank|dale --title "..." --brief BRIEF` [--pack PACK]. FAIL lines must be fixed; INFO lines are for reading. |
| `references/models/` | Six real makers' transcripts (W01 to W06, WhosTheVoss and Bearded Viking), one per file, with what to take, what not to take and signature phrases quoted exactly. |
| `references/research-pack-template.md` | The research pack's layout, unchanged. |

Built from `drafts/p21-woodworking/` (kept there; its `README.md` lists every file, what it replaces, what was dropped and the doubts). The old pack is in `archive/pre-p21-2026-11-06/woodworking-scripts/`.

## plumbing-scripts/ (the plumbing niche pack; P21, 2026-11-06)

| File | What's in it |
|---|---|
| `SKILL.md` | The steps for the plumbing channels (Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter, Werner Finkbeiner): inputs, NOT READY, the video type and its model, write, read aloud, check, the output. |
| `check.py` | The hard-rules check (no counts to meet): `python3 check.py SCRIPT --channel roger|mark|vintage|werner --title "..." --brief BRIEF` [--prices FILE]. FAIL lines must be fixed; INFO lines are for reading. |
| `references/models/` | Seven real on-camera transcripts (R04, R13, R14 Roger Wakefield; R06, R15, R16, R18 Silver Cymbal), kept at seven (operator default, 2026-11-06). |
| `references/price-guide.md` | The plumbing price guide, unchanged (byte-identical to the archived one; research in `studies/plumbing/price-research-2026-10/`). |

Built from `drafts/p21-plumbing/` (kept there; its `README.md` lists every file, what it replaces, what was dropped and the doubts). The old pack is in `archive/pre-p21-2026-11-06/plumbing-scripts/`.

## hvac-scripts/ (the HVAC niche pack; P21, 2026-11-06)

| File | What's in it |
|---|---|
| `SKILL.md` | The steps for the HVAC channel (Roger the HVAC Guy): inputs, NOT READY, the video type and its model, write, read aloud, check, the output. Words per minute stays unset, counted at 150 (operator default, 2026-11-06). |
| `check.py` | The hard-rules check (no counts to meet): `python3 check.py SCRIPT --channel roger-hvac --title "..." --brief BRIEF` [--prices FILE]. FAIL lines must be fixed; INFO lines are for reading. |
| `references/models/` | Eight real on-camera HVAC transcripts (R22, R23, R25, R27, R28, R34, R35, R42). |
| `references/price-guide.md` | The HVAC price guide and safety facts, unchanged (byte-identical to the archived one; research in `studies/hvac/price-research-2026-10/`). |

Built from `drafts/p21-hvac/` (kept there; its `README.md` lists every file, what it replaces, what was dropped and the doubts). The old pack is in `archive/pre-p21-2026-11-06/hvac-scripts/`.

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

## style-scripts/ (the hair-and-fashion niche pack; P21, 2026-11-06)

| File | What's in it |
|---|---|
| `SKILL.md` | The steps for the hair-and-fashion channels for women over 60 (Scarlett Starling, Diane de Chambray; both still pending): inputs, NOT READY, the video type and its model, write, read aloud, check, the output. |
| `check.py` | The hard-rules check (no counts to meet): `python3 check.py SCRIPT --channel scarlett|diane --title "..." --brief BRIEF`. FAIL lines must be fixed; INFO lines are for reading. |
| `references/models/` | Eleven real women's transcripts (M01, M04, M07, M09, M13, M18, M19, M21, M24, M28, M30) and `H01-paris-never-ages-hooks.md` (three hooks, up to item one), each with what to take, what not to take and her signature phrases. The model picks and why are in `drafts/p21-style/model-picks.md`. |

Built from `drafts/p21-style/` (kept there; its `README.md` lists every file, what it replaces, what was dropped and the doubts). The old pack is in `archive/pre-p21-2026-11-06/style-scripts/`.

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
| `dist/` | **Generated, never edited by hand.** Since P21 (2026-11-06) the four rebuilt packs ship whole (`SKILL.md`, `check.py`, `references/`) and a P21 persona page is copied as its skill's `SKILL.md` with its own frontmatter (the build stamps the version line); no `sawdust-sam-persona`. Earlier layout: one skill per layer: `script-writer.skill` (the core, START), `woodworking-scripts.skill` and `plumbing-scripts.skill` (the niche packs), `hank-hardwood-persona.skill`, `dale-oakfield-persona.skill`, `roger-the-pipe-guy-persona.skill` and `mark-silverbridge-persona.skill` (profile plus book), `vintage-pipefitter-persona.skill` (profile only), `woodworking-ideation.skill`, `ideation-core.skill`; the unzipped folders; `script-writer.zip` (the same skill as `script-writer.skill`); and `INSTALL.md` (how to install them, not itself a skill). The build checks claude.ai's upload rules (one SKILL.md, frontmatter, name, description up to 1,024 characters). |

## personas/

One page per channel. The nine P21 channels' pages (2026-11-06) are their persona skills' `SKILL.md`, frontmatter included, copied from `drafts/p21-*/<channel>-persona/SKILL.md`: who the channel is, the opening (with "Hold the reveal"), the feeling, the flow, the hard rules, the book and the ending. Frederick Barnes keeps the older profile form (`core/persona-profile-template.md`). The old profiles, and Sawdust Sam's (dropped 2026-11-06), are in `archive/pre-p21-2026-11-06/personas/`.

| File | What's in it |
|---|---|
| `hank-hardwood.md`, `dale-oakfield.md` | Hank's and Dale's one-page briefs (P21). Dale keeps exactly five book mentions (operator default, 2026-11-06). |
| `roger-the-pipe-guy.md`, `mark-silverbridge.md`, `vintage-pipefitter.md`, `werner-finkbeiner.md` | The four plumbing one-page briefs (P21); Werner's carries the German way. |
| `roger-the-hvac-guy.md` | Roger the HVAC Guy's one-page brief (P21; no book; words per minute unset, counted at 150). |
| `scarlett-starling.md`, `diane-de-chambray.md` | The two style one-page briefs (P21; both channels still pending). |
| `frederick-barnes.md` | Frederick Barnes's profile (electrical, not P21; unchanged): retired electrician, 35 years, Talking Head, 162 words a minute, no book, a one-line subscribe ask, scanner bans. |
| `books/hank-hardwood-book.md`, `books/dale-oakfield-book.md` | Hank's and Dale's book texts with page markers and chapter maps. |
| `books/roger-the-pipe-guy-book.md`, `books/mark-silverbridge-book.md`, `books/werner-finkbeiner-book.md` | Roger's and Mark's books (page markers, chapter maps, fix indexes) and Werner's book index (every repair with its page and Money Saved). |
| `books/scarlett-starling-book.md`, `books/diane-de-chambray-book.md` | Indexes of the two style books from OCR: chapters, every item with its PDF page, the facts a CTA may state, and the book's own stories, which never go in a script. |

Every book file here is byte-identical to the copy its P21 persona skill carries (checked with `cmp`, 2026-11-06), at the same path `personas/books/...`.

## archive/

| Folder | What's in it |
|---|---|
| `facelessos-original/` | The original bought FacelessOS files and the old house-rules prompt. Read-only. |
| `pre-p21-2026-11-06/` | **Read-only.** The library before P21 (moved with `git mv` on 2026-11-06): the old `style-scripts/`, `plumbing-scripts/`, `hvac-scripts/` and `woodworking-scripts/` packs, the nine channels' old profiles, and Sawdust Sam's profile and book (dropped). Its `README.md` says what's there and why. The core scanner checks in `tests/run_checks.py` use these files as read-only fixtures. |

## studies/

Research data: collect and describe only, never edited to fit a conclusion.

| Folder | What's in it |
|---|---|
| `woodworking/` | The woodworking-for-profit study (2026-10-17): Hank, Dale and two competitors, 45 videos. Transcripts, comments, views against each channel's normal, one descriptive notes file per video, and combined transcripts. Method in `study-brief.md`, every step in `log.md`. |
| `plumbing/` | The plumbing study (started 2026-10-20): Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter and five competitors (one a pest-control parallel niche, one an AI channel), 5 most recent plus 5 most-viewed (last 24 months) per channel. Same layout and method as woodworking; see its `study-brief.md` and `log.md`. Got2Learn's second group is its all-time top 5 (it stopped uploading). `price-research-2026-10/` holds the price research and re-checks behind the plumbing price guide. `comparison/` holds the analysis: measured numbers, own hits against recent uploads, competitor profiles, a side-by-side on 12 dimensions, and a summary with suggestions for the plumbing script rules (none applied). |
| `electrical/` | The electrical pack's own study files (2026-10-27): `model-picks-2026-10-27.csv` (the 38 picked model videos, E01-E38), `transcripts/` (raw NexLev transcripts behind the 37 model files built, the six later removed included), `lessons-for-the-pack-2026-10-27.md` (99 problems from the plumbing and woodworking script tests and how each was fixed: the checklist the electrical pack is reviewed against), `facts-research-2026-10-27/` (the facts guide's research and re-check notes) and `models-removed-2026-10-27/` (the six model files the operator removed from the library on 2026-10-27, five posted before 2022 and one science-hobbyist channel, with a README saying why). The niche research itself is in the niche-research repository. |
| `recent-uploads-2026-10-25/` | The newest upload on each of the seven channels (Roger twice), 2026-10-25: the caption transcripts (what the voice really said), lengths and views, before-and-after video lengths per channel, and the main session's analysis (the voice's misreads, the plumbing promise blocks, a review against the studies, and the average view duration question). |
| `recent-uploads-2026-10-29/` | Werner's and Frederick's first uploads since their 2026-10-27 relaunch, 2026-10-29: the caption transcripts (plus Werner's older video on the same topic), lengths, views and words a minute, and the main session's review of both against their packs and profiles, with eight candidate fixes for the operator's yes. |
| `recent-uploads-2026-11-05/` | Every upload from 2026-10-29 to 11-04 on Roger the Pipe Guy, Mark Silverbridge, the Vintage Pipefitter, Werner Finkbeiner, Scarlett Starling and Diane de Chambray (33 videos): caption transcripts, one audit per channel against its pack, profile and the operator's 2026-10-29 decisions, two re-checks, and `SUMMARY.md` with open questions for the operator. |
| `hvac/` | The HVAC script and comment study (started 2026-10-27) for the Roger the HVAC Guy pack: 37 proven HVAC videos picked by video type (real people for voice and structure, faceless channels such as Ray Dutton's Garage for structure only, and Roger the Pipe Guy's own AC drain video). Transcripts, comments, views against each channel's normal and one descriptive notes file per video. Method in `study-brief.md`, the selection in `inputs/videos.md`, every round in `log.md`, the round 1 check in `check-round1.md`. `comparison/` holds the analysis (the viewers, the measured openings and numbers, the body, safety and CTAs, models and voice) and a `README.md` with the main findings and 12 suggestions for the HVAC pack (none applied). |
| `hvac/price-research-2026-10/` | The evidence behind `hvac-scripts/references/price-guide.md` (2026-10-27): the job lists (`jobs.md`), four first-pass researchers (`A-research.md` to `D-research.md`) and four second-pass checkers using other publishers (`A-verify.md` to `D-verify.md`), with every source, date and verdict. `README.md` explains the method, the counts and the brief figures that didn't hold up. |
| `hvac/pack-diagnosis-2026-10-27/` | Two helpers' notes behind the HVAC pack diagnosis (2026-10-27): `references-and-models.md` (the plumbing models, voice samples, excerpts, price guide and unit plan checked for HVAC; HVAC model candidates by video type with IDs and views; a seed list of HVAC prices from batch 1's briefs) and `wiring-scanner-checks.md` (every place a new pack and channel is plugged in, the scanner run on HVAC wording, the two Rogers' name check, and the clashes with the plumbing and electrical branches). Read-only research; nothing applied. |
| `home-diy/frederick-baseline-2026-10/` | Frederick Barnes before the library (2026-10-22): his 23 scripts as written with the old system (verbatim, from Drive), which became which video and the public views (one 434k hit, the rest 23 to 5.3k), counts per script, the scanner's output and the main session's analysis against the library. The baseline for his move from home security and fire prevention to home DIY. |
| `plumbing/werner-baseline-2026-10/` | Werner Finkbeiner before the library (2026-10-27): his 14 scripts as written with the old system (verbatim, from Drive), which became which video with lengths and views (10 to 1,000; 11 subscribers), counts per script and the scanner's output. The baseline for his relaunch. |
| `style/` | The style niche study (started 2026-10-28) for Scarlet Sterling and Diane de Chambray: hair and fashion for women over 50, with makeup and skincare scanned as adjacents. `own-baseline-2026-10/` holds both channels' uploads, transcripts, comments and notes; `discovery/` the scoping scrape (real and faceless channels, one raw file per lane); `round2/` the finished screen (236 channels kept), 2,478 outliers and `BREAKOUT-MAP.md`; `inputs/` the operator's list and the 45 study videos; `data/` and `notes/` the study videos' transcripts, comments and notes; `comparison/` the analysis and `README.md` (findings and 14 suggestions, none applied), `07` the emotions and age brackets, `08` hair against fashion (2026-10-28, session 13); `models/` the model candidates, `approved-models.csv` (M01-M30 real presenters, F01-F08 faceless structure-only, F07 dropped; all collected into `data/` and `notes/`) and the item-list search; `pack-diagnosis-2026-10-28/` the two helper sweeps behind the pack diagnosis (`library-sweep.md`, `persona-sweep.md`). Method in `study-brief.md`, every round in `log.md`. |

## drafts/

- `p21-style/`, `p21-plumbing/`, `p21-hvac/`, `p21-woodworking/` (2026-11-06): the P21 rebuilds, each laid out exactly as its skills are uploaded, each with a `README.md` (every file, what it replaces, what was dropped, the doubts). **Applied 2026-11-06** (operator: "yes use defaults"): the library copies now live at `<niche>-scripts/` and `personas/`; these folders are kept as the record, and `tests/run_checks.py` and `tools/build_skills.py` compare the build against them. `p21-style/model-picks.md` is the style model research.
- `lite-*-DRAFT.md` (2026-11-05): the one-page writer briefs tested in iter-08 to iter-13 (style, Scarlett, Diane, Roger, Frederick, Roger the HVAC Guy, Hank); the base for P21's rebuild. `style-lite-DRAFT.md` is iter-08's first version.

Drafts waiting for the operator's yes go here; nothing in it is part of the library until it's approved and moved. Now: `style-pack-diagnosis-DRAFT.md` (2026-10-28, session 13): what the one hair-and-fashion pack and the Scarlett Starling and Diane de Chambray profiles keep, adapt and add from the core and the plumbing pack, the hair and fashion emotion comparison, the scanner gaps, the reference material, the order of work and 23 questions with recommendations (nothing applied). `style-study-plan-DRAFT.md` (2026-10-28): the plan for the style niche study (Scarlet Sterling and Diane de Chambray), phases and six questions, waiting for the operator's yes. `hvac-pack-diagnosis-DRAFT.md` (2026-10-27): what the HVAC pack and Roger the HVAC Guy's profile keep, adapt and add from the plumbing pack and Roger the Pipe Guy's profile, section by section, the scanner gaps HVAC hits, the order of work and 11 questions for the operator (nothing applied). `werner-relaunch-DRAFT.md` (2026-10-27), the Werner relaunch: what was built, his old scripts against the library, and twelve questions (W1-W12) with proposals P14-P16; answered and applied the same day (Werner ready), kept as the record. `tts-hook-and-length-DRAFT.md` (2026-10-25): Parts 1 and 2 applied the same day (writing every word for the voice; a count line in place of the plumbing promise block, P10); Part 3, the plumbing words per minute, waits. `sawdust-sam-DRAFT.md` (2026-10-23), the Sawdust Sam relaunch draft, applied the same day except his personal details (question 8), which wait for the operator's pick; kept as the record of the questions and evidence. The plumbing emotion draft was applied on 2026-10-21 (in git history). The plumbing pack itself moved into `plumbing-scripts/` on 2026-10-21.

## tests/

`run_checks.py`: automated checks across the whole library. **P21 (2026-11-06):** the core scanner checks use the archived packs as read-only fixtures; the checks of rules that P21 kept are retargeted to each pack's `check.py` and the new pages; checks 10, 21, 34, 37, 41, 42, 61 and 87 are retired (numbers kept in comments); new checks 94-98 test the P21 packs (each `check.py` passes its saved test scripts in iter-14 to iter-18, every model's signature phrases are exact quotes, the price guides are unchanged, every page holds the reveal, the build list has the 13 P21 skills and no Sawdust Sam). Before P21 (72 numbered checks at the 2026-10-27 merge): including the copy guard, the fraction-word scanner check, the "e-book" ban on every profile, and the plumbing pack (its inputs, scanner block, Mark's contraction ban, the copy guard over its own SKILL.md and every model file, the emotion rules, item shape, CTA template and number cap, the plumbing profiles and the channel list), and the core's straight-quotes and real-scanner-line rules, the written-for-the-voice scanner check (44), the plumbing count line in place of the promise block (45), the electrical pack and Frederick (46-52), the P13 core checker fixes (53-57: tenure in words, number words, letter sets once, voice tags, the 35-word sentence limit, `--final`, the ITEMS and SENTENCES report, `verify_output.py`), the electrical test fixes (58, 59 and 69), the plumbing escalation line (46b), Werner's profile and book index (70), the HVAC test answers (71: `require-if`, every carbon monoxide and gas-leak step; 72: the reframe split across two sentences), and the HVAC pack (60-68: file references, its inputs and scanner block, tenure in HVAC words, letter words, the two Rogers' name bans, real-people-only models with the copy guard, the channel row and build entries, the price guide). Run it after any edit.

## tests/iterations/

One folder per round of changes (`refs-01/`, `iter-00/`, `iter-01/`, …), each with `CHANGES.md` (file | what changed | why) and `before/` copies of every file it modified. `iter-01/` is the first real script test (Hank, the lazy Susan): its inputs and output in `test-run/`, the findings and the operator's decisions in `REVIEW.md`. `iter-06/` (TEST, 2026-10-27) is the first HVAC test: Roger the HVAC Guy, batch 1 #4 and #14, two rounds (runs 01-02, then 03-04 after the fixes), each with the chat, output, script, the main session's scanner run and a judge report; `CHANGES.md` holds the findings, the fixes and the questions for the operator; `judge-rubric.md` and `refs/` are the judge's. `iter-08/` to `iter-13/` (TEST, 2026-11-05) are the A/B tests behind P21: one-page brief against the full skills, blind, one title each (style, plumbing, three style titles against the published videos, electrical, HVAC, woodworking); each has a `README.md` and `RESULTS.md`. `iter-08/account-skills-2026-11-05/` is the only git copy of the account's 2026-10-31 style skills.

## SESSION-HANDOVER.md

The live note between Claude Code chats: where the last chat stopped, operator decisions, the active channel list, open questions and the next actions. Rewritten at every handover.

## PINNED.md

The to-do list, the decisions made, the decisions still open, and the data to pull.
