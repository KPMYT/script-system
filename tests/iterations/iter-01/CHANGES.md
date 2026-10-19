# iter-01: core baseline fixes, test fixtures, and the first writer / operator / judge run

Started 2026-10-19. Part 1 applies the core-level fixes from `../iter-00/AUDIT.md`. Part 2 adds the TEST fixtures and START TEST. Part 3 is the first test run (its outputs and results are recorded below and in this folder). `before/` holds a copy of every file this iteration modified, as it was at commit 13803b1.

Pack-level findings (A3, A9's unit-plan template, A12, C4, C7, D5) are left for the woodworking-for-profit step. D1 (persona profiles) and D3 (packaging as an installed skill) are still open. D4 (no research stage) is unchanged: the TEST research pack was built by a research subagent following `core/research-and-sourcing.md`.

## Part 1: core fixes from the iter-00 audit

| Finding | File | What changed | Why |
|---|---|---|---|
| A1 (rest) | `core/greenlight-audit.md` | Evidence block's Scanner line gains `copied 0`. | The copy guard's result was the only scanner result not recorded. |
| A2 (rest) | `core/workflow.md` | Run step 1 loads the niche pack's reference scripts (if it has them); step 2 (Plan) uses them for structure and pacing only, never wording. | The reference scripts were wired into the pack but the workflow never loaded them. |
| A4 | `core/retention-mechanics.md` | Sections 1 and 14: the *final content beat* leaves a next action; the closing line after it follows `cta-and-endings.md`. | Two different rules for the last line. |
| A5 | `core/humanizer.md` | H13 exempts the persona's signature sign-off. | The required sign-off failed H13 on sight. |
| A6 | `core/workflow.md`, `core/voice-anchoring.md` | New default input `voice-samples` (2-3 verbatim excerpts with sources), required only when neither the niche pack nor the persona profile has samples, with its check. Voice-anchoring now points to the gate instead of "stop and ask". | A question the gate forbade; channels with no pack had no legal way to get samples. |
| A7 | `core/workflow.md` | A missing or pending persona profile now ends with the standard NOT READY block. | Two forms of NOT READY. |
| A8 | `core/variety-rotation.md` | Rotation log format gains `end-CTA: "[first 6-10 words]"`. | End-CTA wording couldn't be checked against the log. |
| A10 | `core/claims-policy.md` | Only an industry or category is cast as the villain, never a named company. | Contradicted `offer-rules.md`, `research-and-sourcing.md` and the woodworking pack. |
| A11, B2 | `core/humanizer.md`, `core/greenlight-audit.md`, `core/script-scanner.py` | H22 example no longer rounds a cost down ("a little over three bucks", "listed at $40"). Audit D4: rounding only toward the cautious side (costs, time, fees up; prices, earnings, savings exact or down). Scanner's number tolerance tightened from 10% to 5% (minimum 0.5), so "$46" against a pack's "$42" is flagged. | Nothing outside woodworking said which way to round, and the scanner let a 10% flattering drift through. |
| A13 | `README.md`, `PINNED.md` | README map rebuilt: root files, START TEST, `personas/README.md`, tests, fixtures, iterations, `studies/`, `archive/facelessos-original/`; test count updated. PINNED test count and an iter-01 line. | `CLAUDE.md` rule 7. |
| A14 | `tests/run_checks.py` | Check 1 also covers `personas/*.md`, `README.md` and `PINNED.md` (resolved against the whole repo). Check 2 also covers personas and README (PINNED is left out on purpose: it names retired items in its decisions list; README may name the archive it describes). New checks: 8b (one-word lift), 9b (rounding tolerance), 13 (README map lists every library file and folder), 14 (every persona profile fills every template field), 15 (fixtures labelled TEST and never leaking into `core/channels.md` or `personas/`). Suite: 22 checks. | The suite missed stale docs and the grouped-ban lift. |
| A15 | `core/script-scanner.py`, `tests/run_checks.py`, `woodworking-scripts/archive/most-viewed-24mo/INDEX.md` | Removed the retired labels `HOUSE FORMAT`, `BUILD SHEET`, `TYPE CONFIRMED`, `VOICE CONFIRMED` from the scanner and added them to the STALE list. INDEX path now `studies/woodworking/data/competitors/`. | Leftovers from the house-rules prompt; stale path after the restructure. |
| A16 | `core/retention-mechanics.md` | "Without a real person on camera, trust comes from competence…" | Hank is an AI-avatar face channel. |
| B1 | `core/greenlight-audit.md`, `core/workflow.md` | Any change after PASS, however small, voids it: full audit again, new verdict and evidence block. | Lost from the originals; a VA's tweak kept the old PASS. |
| B3 | `core/humanizer.md` | H18 covers a repeated theme in different words: give it one home paragraph. | The scanner's phrase echo can't see a theme. |
| B4 | `core/script-structures.md` | Why-it-happens Layer 1: one core idea and one everyday comparison. Layer 2 builds on it and never contradicts it. | Lost from the originals. |
| B5 | `core/workflow.md` | "Before typing START": a new chat per script, on the most capable model the account offers. | The audit runs on whatever model the VA opened. |
| B6 | `core/workflow.md` | "One script per chat": START in a chat that already printed a finished script gets only `Start a new chat for the next script.` | Facts leak between scripts in one chat. |
| B7 | `core/workflow.md`, `core/greenlight-audit.md` | Outside the steps, no more than about two sentences in a row without naming something showable; audit F7 checks it. | The auto-edit repeats footage on lines with nothing to show; the study's top complaints were narration not matching footage. |
| C1 | `core/script-structures.md`, `core/greenlight-audit.md` | Removed the "honest escalation promise" hook option and its ordering exception; added a line that a promise about later in the video is a banned long-range tease. Audit B8 now reads "the default, a ranked countdown, or the niche pack's rule". (The audit suggested keeping B8's "hook's escalation promise" clause; with the option gone it pointed at nothing, so it was replaced.) | Broke the locked "no long-range promises" decision. |
| C2 | `core/script-scanner.py`, `tests/run_checks.py` | "AI vocabulary" split into four bans (delve, tapestry, unleash, robust). A lift now matches only a ban's exact label or a phrase the ban matches in full, so `lift: robust` lifts only robust, and `lift: AI vocabulary` or `lift: stick` lifts nothing. Test 8b. | Broke the locked rule that a ban is lifted only by naming that one ban. |
| C5 | `core/workflow.md` | `[chuckles]` removed from the VO tags; `[slightly amused]` only on an honest-candor line. | Jokes are a locked no. |
| C6 | `core/retention-mechanics.md` | Description no longer invites retention-graph diagnosis. | Retention coaching was rejected. |

## Part 2: test fixtures and START TEST (audit D2)

| File | What changed | Why |
|---|---|---|
| `core/workflow.md` | Section 1, step 3: `START TEST` runs exactly like START, but the channel list, persona profiles and test research packs come from `tests/fixtures/`; every test output starts `TEST: DO NOT UPLOAD.`; real and test channels can't cross. | There was no way to run START on test data without touching `core/channels.md` or `personas/`. |
| `core/script-scanner.py` | `TEST: DO NOT UPLOAD` lines are skipped as non-spoken. | The test label must not be scanned as narration. |
| `tests/fixtures/` (new) | `README.md`, `channels.md` (TEST Plumbing, no niche pack), `personas/test-plumbing.md` (Talking Head, ElevenLabs, an invented TEST e-book offer), `inputs/` (title and brief, research pack, two-line rotation log, three voice samples), `judge-only/` (the source script and a README). All labelled TEST. | The first fixture set, plumbing-01, tests the core on a channel with no niche pack, so the fallbacks (structures, default research pack, voice-samples input) are exercised. |

**plumbing-01 sources:** the source script (judge only) is Morgan Inspection Services, "Why Your Toilet Keeps Running, and How to Fix it" (83,000 views, outlier 3.73). Voice samples (pulled by a subagent with NexLev, verbatim, filler kept): HowToWith GEO "Toilet Not Filling? QUICK FIX" (844,000, 5.62), The Home Service Pro "What's the Best Choice for Replacing Toilet Flappers?" (104,000, 4.60), Moore Approved "Fix a Running Toilet: Replace Fill Valve & Flapper" (130,743, 2.12). Two caption fixes are noted in the file. The research pack was built and verified on 2026-10-19 by a research subagent from live web sources, without access to the source video.

## Test runs after Part 1-2

- `python3 tests/run_checks.py`: 22/22 passed.
