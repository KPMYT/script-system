# Script System: what's in each file

The whole system is one library. `core/` holds the rules every channel uses. Each niche gets its own pack (so far, `woodworking-scripts/`). Each channel gets a persona profile in `personas/`. Typing **START** runs `core/workflow.md`, which pulls in everything else. **START TEST** does the same on TEST data from `tests/fixtures/`.

## The repo's root files

| File | What's in it |
|---|---|
| `CLAUDE.md` | The working rules for every Claude Code chat in this repo: layout, locked decisions, logging, tests, handover and `main`. Read first. |
| `SESSION-HANDOVER.md` | The live note between chats: where the last chat stopped, operator decisions, the active channel list, open questions and next actions. Rewritten at every handover. |
| `HANDOFF.md` | How the system was built and why: architecture, the locked decisions (section 3), competitor findings, known limits. |
| `PINNED.md` | The to-do list, the decisions made, the decisions still open, and the data to pull. |
| `CHANGELOG.md` | Every change to the library, newest first: date, files, what changed, why. |
| `PROPOSALS.md` | Evidence that a locked decision might need to change. Nothing in it is applied until the operator decides. |
| `README.md` | This file map. |

## core/ (every channel)

| File | What's in it |
|---|---|
| `workflow.md` | **The entry point.** START (and START TEST), picking the channel, the input gate (refuses to write until every input is valid), the run with no questions, the Vidrush script format and Talking Head markers, the output layout, the ElevenLabs voiceover copy, and the NOT READY rule. |
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

## personas/

| File | What's in it |
|---|---|
| `personas/README.md` | How profiles are named and when a channel is ready. One persona profile per channel; Hank's and Dale's are still to be written. |

## tests/

| File or folder | What's in it |
|---|---|
| `run_checks.py` | 22 automated checks across the library, the README map, persona profiles and the test fixtures, including the copy guard. Run it after any edit; nothing is committed while one fails. |
| `tests/fixtures/` | TEST data for START TEST: `fixtures/README.md` (what's where and who may read it), `channels.md` (the TEST channel list), `tests/fixtures/personas/` (TEST persona profiles), `tests/fixtures/inputs/` (titles, briefs, research packs, rotation logs and voice samples the operator pastes) and `tests/fixtures/judge-only/` (the source scripts the judge compares against; the writer never opens it). |
| `tests/iterations/` | One folder per round of changes or test runs (`refs-01`, `iter-00`, `iter-01`, …), each with its changes (`CHANGES.md`: file, what changed, why), `before/` copies of every file it modified, and any test outputs and results. Never overwritten. |

## Research and originals

| Folder | What's in it |
|---|---|
| `studies/` | Competitor studies, one folder per niche (`studies/woodworking/` so far): data, notes, transcripts. Collect and describe only; never edited to fit a conclusion. |
| `archive/facelessos-original/` | The original bought FacelessOS files and the old house-rules prompt. Read-only, for comparison, never used as rules. |
