# Script System: what's in each file

The whole system is one library. `core/` holds the rules every channel uses. Each niche gets its own pack (so far, `woodworking-scripts/`). Each channel gets a persona profile in `personas/`. Typing **START** runs `core/workflow.md`, which pulls in everything else.

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
| `script-scanner.py` | The program that mechanically checks a script: banned phrases, dashes and odd characters, niche bans, filler counts, echoes, numbers missing from the research pack, and (with `--refs`) any run of 8+ words copied from the niche pack's reference files. |

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

## ideation/

Copies of the operator's claude.ai ideation skills, brought in to be edited here with the operator's approval. The operator uploads the edited version back to claude.ai.

| Folder | What's in it |
|---|---|
| `woodworking-ideation/` | The woodworking ideation skill, edited 2026-10-20: Hank and Dale only (both on camera, single builds), titles may exaggerate freely, and the new for-profit pipeline in `references/pipeline.md` (Etsy-first product scan of 30, title and thumbnail-text options, picks, fact-bank briefs, optional research pack). It's an overlay on `ideation-core`. |
| `ideation-core/` | The shared ideation base (format bank, rules, audience profiles), an unchanged copy kept so it can be installed on VA accounts. Not edited. |

## tools/ and dist/

| File or folder | What's in it |
|---|---|
| `tools/build_skills.py` | Builds the installable skills from the library into `dist/`. Run it after any change, then re-upload. |
| `dist/` | **Generated, never edited by hand.** One skill per layer: `script-writer.skill` (the core, START), `woodworking-scripts.skill` (the niche pack), `hank-hardwood-persona.skill` and `dale-oakfield-persona.skill` (profile plus book), `woodworking-ideation.skill`, `ideation-core.skill`; the unzipped folders; and `INSTALL.md` (how to install them, not itself a skill). The build checks claude.ai's upload rules (one SKILL.md, frontmatter, name, description up to 1,024 characters). |

## personas/

One persona profile per channel, written from `core/persona-profile-template.md`.

| File | What's in it |
|---|---|
| `hank-hardwood.md` | Hank Hardwood's profile: settings, his ten shop details, the approved personality, and the CTA rules (two short CTAs to the QR code, with book pages when the video's build is in the book). |
| `dale-oakfield.md` | Dale Oakfield's Workshop's profile: settings, the grandfather detail, the approved personality, the Bertha-style CTA rules, and his ending. |
| `books/hank-hardwood-book.md` | The full text of Hank's ebook, "100 Ways to Make Your First $1,000 with Woodworking", with a marker for every page (PDF page and printed page), a chapter page map and an index of all 100 builds. Used to find which pages cover a video's topic for the CTA, and which facts a CTA may state about the book. |
| `books/dale-oakfield-book.md` | The same for Dale's ebook, "The Ultimate DIY Woodworking Guide", with a chapter page map (the book prints no page numbers, so it uses PDF pages). |

## studies/

Research data: collect and describe only, never edited to fit a conclusion.

| Folder | What's in it |
|---|---|
| `woodworking/` | The woodworking-for-profit study (2026-10-17): Hank, Dale and two competitors, 45 videos. Transcripts, comments, views against each channel's normal, one descriptive notes file per video, and combined transcripts. Method in `study-brief.md`, every step in `log.md`. |
| `plumbing/` | The plumbing study (started 2026-10-20): Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter and five competitors (one a pest-control parallel niche, one an AI channel), 5 most recent plus 5 most-viewed (last 24 months) per channel. Same layout and method as woodworking; see its `study-brief.md` and `log.md`. |

## tests/

`run_checks.py`: 18 automated checks across the whole library, including the copy guard. Run it after any edit.

## tests/iterations/

One folder per round of changes (`refs-01/`, `iter-00/`, …), each with `CHANGES.md` (file | what changed | why) and `before/` copies of every file it modified.

## SESSION-HANDOVER.md

The live note between Claude Code chats: where the last chat stopped, operator decisions, the active channel list, open questions and the next actions. Rewritten at every handover.

## PINNED.md

The to-do list, the decisions made, the decisions still open, and the data to pull.
