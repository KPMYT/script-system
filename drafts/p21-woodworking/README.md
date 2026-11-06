# DRAFT: P21, the woodworking rebuild (Hank Hardwood, Dale Oakfield's Workshop)

Not part of the library yet. Built 2026-11-06 from `drafts/lite-hank-hardwood-DRAFT.md` (the iter-13 one-page winner, 49 against 46 of 60) and the account's current skills (`woodworking-scripts`, `hank-hardwood-persona`, `dale-oakfield-persona`, all 2026-10-21, identical to the repo's `woodworking-scripts/` and `personas/`), on the shape of `drafts/p21-style/`. For the operator to see before anything replaces the library or goes to the account. Sawdust Sam is not active and is left out: his persona and pack stay as they are.

The folders are laid out exactly as the three skills would be uploaded.

| File | What it is | Replaces |
|---|---|---|
| `woodworking-scripts/SKILL.md` | The steps: inputs, NOT READY, the video type and its model, write, read aloud, check, the output (about 1,250 words) | the account's `woodworking-scripts` (4,138 words) with `excerpts.md` (11,608), `reference-scripts.md` (23,692), `voice-samples.md` (922) and `unit-plan-template.md` (430); and, for these two channels only, `core/workflow.md` sections 2 to 6 and the other core files (the research stage excepted) |
| `woodworking-scripts/check.py` | The hard-rules check (no counts to meet) | the core scanner, the humanizer pass and the full audit, for these two channels |
| `woodworking-scripts/references/models/` | Six real makers' transcripts, one per file (W01 to W06), with what to take, what not to take and signature phrases quoted exactly | the voice samples, the excerpts and the labelled reference scripts |
| `woodworking-scripts/references/research-pack-template.md` | The research pack's layout, copied unchanged | the same file |
| `hank-hardwood-persona/SKILL.md` | Hank's one page (about 1,570 words) | the account's profile (1,709 words) and the pack's rules for him |
| `dale-oakfield-persona/SKILL.md` | Dale's one page (about 1,640 words) | the account's profile (1,596 words) and the pack's rules for him |
| `*/personas/books/*-book.md` | The two book texts, copied unchanged | the same files |

**What does not change:** `script-writer` (START, the channel question, the channel list), `core/research-and-sourcing.md` (still used to build a missing pack), Sawdust Sam's files, and every other channel's skills.

**Test briefs:** `tests/iterations/iter-18/brief-hank.txt` (iter-13's brief, header changed) and `brief-dale.txt` (talking points from Dale's PbK8YeMSqWM, the dog bowl stand; why that video is in its header).

## The models (`references/models/`)

| File | Video | Views / normal | Video type |
|---|---|---|---|
| `W01-whosthevoss-sawdust-fire-starters.md` | 6gmjCVaRfjY | 11.52x | recipe build, no cutting (iter-13's model) |
| `W02-bearded-viking-pumpkins.md` | _vzgcQ-1hhQ | 39.35x | seasonal piece |
| `W03-whosthevoss-train-whistles.md` | 64alAPtMfFw | 9.96x | many from one board; paying for tools |
| `W04-bearded-viking-step-stool.md` | AopDfSQj2FI | 12.65x | small furniture (Dale's test brief) |
| `W05-whosthevoss-storage-riser.md` | arNIvR7AXVE | 8.31x | better than the store's version |
| `W06-whosthevoss-zero-cuts.md` | ZIUYmkpHgP8 | 4.01x | no saw, no cuts |

All six are on-camera makers (NexLev `check_faceless_channel`: isFaceless false), from `studies/woodworking/data/competitors/`, views as of 2026-10-17. Five are entries of the account's `reference-scripts.md`; W06 isn't. Transcripts are the NexLev captions with the timestamps removed and nothing else changed. Every signature phrase was matched against its transcript by a script.

## From iter-13 (the judge's report and `RESULTS.md`)

| Finding | On the pages |
|---|---|
| Run A's hook was the sharpest ("the material already in your shop... $300 if every bag sells") | Hank's opening gives that shape, never its words, and brings the cheap part back once |
| Run A's book setup ("Quick word while the dust settles... Right, the cartons.") | "Open the next step as a small question, give the book while the viewer waits on it, come back naming that same step" |
| Run B's materials read as a numbered list | "a walk down the aisle... never counted off"; the check fails two or more paragraphs counted off |
| Run B's bridge out of the book pitch pointed at something the viewer wasn't holding | the same setup; the check prints the line before the pitch and the line back |
| Run B said online selling twice | "Say each point once (online selling and its fee in one place)"; the check lists the paragraphs |
| Neither said to keep the water topped up or turn the burner off after pouring | a melting-wax safety line on both pages; the check fails both (a burner-off line for a wax fire doesn't count) |

## Rules carried (operator decisions and the current skills)

Persona facts (manner, sentences, "you" and "I", the enemy, Hank's ten shop details, Dale's grandfather), words a minute (Hank 185, Dale 170), Talking Head with CTA markers, the ElevenLabs VO copy, the research pack as a required input (the current pack requires one; "none" means the chat builds it), the 30-day freshness for prices and fees, single builds only, NOT READY rules, the 8-minute floor with length from the content, the opening (the title's promise and number, the pain or wish, one spark; Dale's frustration line; first material within about 15 seconds; materials announced), signposts, steps as instructions with the object and action named, the viewer's tool kit, the maker's instructions, the heritage rules (P8, P9), every safety default, the money math (cost per piece, tools left out, fees as one total, "listed at" and "sold for", a range and one example, his price inside it, "if they all sell", the time as an estimate, no per-hour figure, no guarantee, never cents, rounded, "prices subject to change" once), where to sell, swearing (Hank mild words aimed at a price, never at the viewer, never in CTAs; Dale none), the bans, the book facts and benefits, the page rule, Hank's two CTAs and Dale's Bertha-style pitch with the grandfather line word for word, "link below" and the book mentions, both endings word for word, and the TTS voice rules.

## Rules dropped (counts and templates only)

1. The unit plan template and "fill in the plan before any prose".
2. The fixed skeleton with its flexible parts recorded in the plan (the build's real order and the signposts stay).
3. The calibration table of line lengths (material 8 to 24 words, steps 8 to 31, 18 to 55 step lines).
4. The rotation log input and the ROTATION LOG ENTRY line, replaced by "don't reuse what earlier scripts in this chat used".
5. The value line "on about one video in three".
6. The output's VERDICT, FORMAT CHECK and AUDIT EVIDENCE blocks, the humanizer pass and the full audit, replaced by `check.py` and the page's check list.
7. The voice samples, the excerpt library (15 groups) and the labelled reference scripts with their unit plans, replaced by six model transcripts.
8. Swearing "one to three per video": now three at most, none is fine.
9. Hank's shop details "at most two, never the same one two scripts running": now "one or two if they fit, each once; none is fine", and not the same as earlier scripts in the chat.
10. Dale's "five book mentions" and their "7 to 30 words": KEPT as locked (main session, 2026-11-06: a locked decision changes only on the operator's yes); the operator is asked whether "up to five" is wanted.
11. The heritage beats' "about one per section, a tenth to a fifth of the script, one to four sentences".
12. "Any sentence with three or more dollar figures gets a second look" and the 12-line "Before handing over" checklist.
13. The pack's background fee figures for Etsy, Facebook and fairs (fees now come only from the pack, as the current pack already says).

## The check run on iter-13 run B (`tests/iterations/iter-13/run-B/script.txt`, Hank)

`RESULT: FAIL (5)`, all true: the water top-up and the burner-off lines missing (the judge's gap), two sentences over 35 words (36 and 39), and the materials counted off ("The first thing... Second is... Third is"). 1,991 words, as the judge measured. False alarms found and fixed: "in this one" read as a channel intro (run A); hyphenated words counted twice; "a hundred and eighty" read as 80. A copy of run B with those five things fixed (scratch only) passes; run A fails on its missing markers and the two wax lines.

## Doubts for the operator

1. **The pages are longer than asked** (about 1,570 and 1,640 words, against 900 to 1,300), because the safety defaults, the money math and the book facts are carried unchanged on each page. Cutting them would change rules.
2. **Dale's five mentions to "up to five"** reads P21's "no counts" onto a locked CTA decision (2026-10-20). Your yes or no.
3. **The wax lines** (water topped up, burner off after the last pour) come from the iter-13 judge's reading, not from a sourced safety guide.
4. **The test briefs have no research pack** ("TEST: this brief's figures stand in"), so the writer must be told to treat the brief as the pack, or it will try to build one.
5. **Dale's test video predates the library** and its figures are unsourced (marked check); the name's price add-on and every fee are "not found".

## On the operator's yes (not done yet)

1. Archive the current `woodworking-scripts/`, `personas/hank-hardwood.md` and `personas/dale-oakfield.md` into `archive/woodworking-pack-2026-10/` (moved, never deleted); Sawdust Sam keeps the archived pack until he's active again, or gets his own page.
2. Put the new files in their library places; update `tools/build_skills.py`, `tests/run_checks.py` (its woodworking checks test the old pack), `README.md`, `HANDOFF.md` and `CHANGELOG.md`.
3. Run the iter-18 blind tests with the two briefs, then build and send the three skills.
