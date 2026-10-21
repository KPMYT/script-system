# Script System: what's in each file

The whole system is one library. `core/` holds the rules every channel uses. Each niche gets its own pack (so far, `woodworking-scripts/` and `plumbing-scripts/`). Each channel gets a persona profile in `personas/`. Typing **START** runs `core/workflow.md`, which pulls in everything else.

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
| `script-scanner.py` | The program that mechanically checks a script: banned phrases (including retention teases), dashes and odd characters, production notes read aloud ("CTA", "stinger", "mid-roll", "continuing with the final sections"), the same sentence twice in a row, the persona's fixed facts from its profile (a different years-in-the-trade figure, a near-miss of the channel, persona or book name), the script talking about its own thumbnail or title (judged), niche bans, filler counts, echoes, numbers missing from the research pack, and (with `--refs`) any run of 8+ words copied from the niche pack's reference files. |

## woodworking-scripts/ (the woodworking niche pack)

| File | What's in it |
|---|---|
| `SKILL.md` | All woodworking-for-profit rules: inputs, freshness, viewer, skeleton, steps, length, money math, proof, where to sell, safety, voice, AI-visual writing, banned list, scanner rules. |
| `references/research-pack-template.md` | What a woodworking research pack must contain. |
| `references/unit-plan-template.md` | The plan filled in before writing, so length comes from the content. |
| `references/voice-samples.md` | Three real narration samples from winning competitors: the voice anchor. |
| `references/excerpts.md` | Winning competitors' lines in 15 groups by job (10-15 each), each marked as usable, rewrite or doesn't transfer. |
| `references/reference-scripts.md` | Eight complete winning scripts, labelled with the skeleton, each with why it works, the unit plan it implies and what doesn't transfer. Read at the planning step; never copy wording. |
| `archive/` | The full BeardedViking and WhosTheVoss transcripts, plus `most-viewed-24mo/` (each channel's 10 most-viewed from the last 24 months, with views and normal), used for calibration only. |

## plumbing-scripts/ (the plumbing niche pack)

| File | What's in it |
|---|---|
| `SKILL.md` | All plumbing rules, approved by the operator (2026-10-21): where the pack overrides the core (one table), inputs (title and brief; no research pack), the viewer, the villain, the opening, point then promise, promise devices, the ten video types with their models, using the models (never a copy), CTAs, the ending (comment line last), length (12 minutes minimum), voice, proof, money framing, safety (the brief wins), the banned list, the scanner block and the before-handing-over checklist. |
| `references/unit-plan-template.md` | The plan filled in from the title and brief before writing, with a MODELS block. |
| `references/voice-samples.md` | Three verbatim stretches of real human narration (Got2Learn, Silver Cymbal, Roger Wakefield): the voice anchor. |
| `references/excerpts.md` | 204 lines in 16 groups by job, tagged [real] or [structure only], with source, timestamp and views against normal. |
| `references/models/` | 38 model files, each a beat map plus the full labelled script, why it works and what doesn't transfer: R01-R20 the real channels (structure and voice), S01-S18 our hits and TheCheapFix (structure only). `INDEX.md` sorts them by video type. |
| `archive/` | The four real channels' transcripts (Silver Cymbal, Roger Wakefield, Got2Learn, Arrow Pest Service). Calibration only; not in the installed skill. |
| `model-file-spec.md` | How the model files were built, for adding models later. Not in the installed skill. |

## ideation/

Copies of the operator's claude.ai ideation skills, brought in to be edited here with the operator's approval. The operator uploads the edited version back to claude.ai.

| Folder | What's in it |
|---|---|
| `woodworking-ideation/` | The woodworking ideation skill, edited 2026-10-20: Hank and Dale only (both on camera, single builds), titles may exaggerate freely, and the new for-profit pipeline in `references/pipeline.md` (Etsy-first product scan of 30, title and thumbnail-text options, picks, fact-bank briefs, optional research pack). It's an overlay on `ideation-core`. |
| `ideation-core/` | The shared ideation base (format bank, rules, audience profiles), an unchanged copy kept so it can be installed on VA accounts. Not edited. |

## tools/ and dist/

| File or folder | What's in it |
|---|---|
| `tools/build_skills.py` | Builds the installable skills from the library into `dist/` (one `.skill` file each, `script-writer` also as a `.zip`, plus the full bundle as one zip). Run it after any change, then re-upload. |
| `tools/verify_plumbing_models.py` | Checks every plumbing model file's labelled script against its study transcript, word for word (session 4). |
| `dist/` | **Generated, never edited by hand.** One skill per layer: `script-writer.skill` (the core, START), `woodworking-scripts.skill` and `plumbing-scripts.skill` (the niche packs), `hank-hardwood-persona.skill`, `dale-oakfield-persona.skill`, `roger-the-pipe-guy-persona.skill` and `mark-silverbridge-persona.skill` (profile plus book), `vintage-pipefitter-persona.skill` (profile only), `woodworking-ideation.skill`, `ideation-core.skill`; the unzipped folders; `script-writer.zip` (the same skill as `script-writer.skill`); and `INSTALL.md` (how to install them, not itself a skill). The build checks claude.ai's upload rules (one SKILL.md, frontmatter, name, description up to 1,024 characters). |

## personas/

One persona profile per channel, written from `core/persona-profile-template.md`.

| File | What's in it |
|---|---|
| `hank-hardwood.md` | Hank Hardwood's profile: settings, his ten shop details, the approved personality, and the CTA rules (two short CTAs to the QR code, with book pages when the video's build is in the book). |
| `dale-oakfield.md` | Dale Oakfield's Workshop's profile: settings, the grandfather detail, the approved personality, the Bertha-style CTA rules, and his ending. |
| `books/hank-hardwood-book.md` | The full text of Hank's ebook, "100 Ways to Make Your First $1,000 with Woodworking", with a marker for every page (PDF page and printed page), a chapter page map and an index of all 100 builds. Used to find which pages cover a video's topic for the CTA, and which facts a CTA may state about the book. |
| `books/dale-oakfield-book.md` | The same for Dale's ebook, "The Ultimate DIY Woodworking Guide", with a chapter page map (the book prints no page numbers, so it uses PDF pages). |
| `roger-the-pipe-guy.md`, `mark-silverbridge.md`, `vintage-pipefitter.md` | The three plumbing profiles, approved 2026-10-21, ready since the plumbing pack entered the library: settings, voices, fixed tenures 45/40/50, the personality kept close to Notion, CTA rules (Roger and Mark: a short mid-video book ask and a one-line end reminder, naming the link and the QR code; Vintage: a one-line subscribe ask), and scanner blocks (Mark's also bans contractions). |
| `books/roger-the-pipe-guy-book.md`, `books/mark-silverbridge-book.md` | Roger's "100 Old-House Fixes That Save You Thousands" (124 pages, 100 fixes) and Mark's "50 Easy Plumbing Fixes That Will Save You $10,000" (122 pages, 50 fixes), with printed page markers, chapter maps and fix indexes. |

## studies/

Research data: collect and describe only, never edited to fit a conclusion.

| Folder | What's in it |
|---|---|
| `woodworking/` | The woodworking-for-profit study (2026-10-17): Hank, Dale and two competitors, 45 videos. Transcripts, comments, views against each channel's normal, one descriptive notes file per video, and combined transcripts. Method in `study-brief.md`, every step in `log.md`. |
| `plumbing/` | The plumbing study (started 2026-10-20): Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter and five competitors (one a pest-control parallel niche, one an AI channel), 5 most recent plus 5 most-viewed (last 24 months) per channel. Same layout and method as woodworking; see its `study-brief.md` and `log.md`. Got2Learn's second group is its all-time top 5 (it stopped uploading). `comparison/` holds the analysis: measured numbers, own hits against recent uploads, competitor profiles, a side-by-side on 12 dimensions, and a summary with suggestions for the plumbing script rules (none applied). |

## drafts/

Drafts waiting for the operator's yes go here; nothing in it is part of the library until it's approved and moved. There are none open now (the folder is made again when one is): the plumbing pack moved into `plumbing-scripts/` on 2026-10-21.

## tests/

`run_checks.py`: 35 automated checks across the whole library, including the copy guard, the fraction-word scanner check, the "e-book" ban on every profile, and the plumbing pack (its inputs, scanner block, Mark's contraction ban, the copy guard over every model file, the plumbing profiles and the channel list). Run it after any edit.

## tests/iterations/

One folder per round of changes (`refs-01/`, `iter-00/`, `iter-01/`, …), each with `CHANGES.md` (file | what changed | why) and `before/` copies of every file it modified. `iter-01/` is the first real script test (Hank, the lazy Susan): its inputs and output in `test-run/`, the findings and the operator's decisions in `REVIEW.md`.

## SESSION-HANDOVER.md

The live note between Claude Code chats: where the last chat stopped, operator decisions, the active channel list, open questions and the next actions. Rewritten at every handover.

## PINNED.md

The to-do list, the decisions made, the decisions still open, and the data to pull.
