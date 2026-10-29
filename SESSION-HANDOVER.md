# Session handover

The live note passed from one Claude Code chat to the next. A new chat reads `CLAUDE.md`, then this file, then `HANDOFF.md`, `README.md` and `PINNED.md`, and carries on from "Next actions". The outgoing chat rewrites this file before every handover.

**Last updated:** 2026-10-29, session 14, the style pack chat (branch `claude/youthful-ritchie-zq7e92`, merged into `main`). Session 14 is summarised first, then session 13 (Werner and Frederick, a parallel chat the same day), then session 12 (the style study); sessions 5-11 follow. **Numbering:** this chat called itself session 13 while it ran (the parallel chat took that number first); it is session 14 from this merge on, and its proposals are P19 and P20 (it opened them as P18 and P19).

---

## The handover rule

- **When:** the operator says when it's time (Claude can't see its own context percentage; don't guess early).
- **Steps, in order:**
  1. rewrite this file
  2. log it in `CHANGELOG.md`
  3. run `python3 tests/run_checks.py`
  4. commit and push
  5. merge this chat's branch into `main` and push `main` (standing permission; never force-push, never delete branches)
  6. give the operator the opening message for the new chat
- **The operator** is not technical. Explain Claude Code and git steps plainly and do them for them where possible.

## How to work with the operator

Still true from sessions 2-4:
- **Never change a rule, file or skill without the operator's explicit yes to that specific change.** Show the exact change first (a draft file is good), then apply.
- **Don't build tests or test material on your own initiative.** Testing happens on the operator's call.
- **Work niche by niche.** The current niche is style (women over 50): Scarlett Starling and Diane de Chambray (sessions 12 and 14).
- **Notion and Google Drive are read-only** unless the operator says otherwise.
- **Keep messages plain,** with numbered items the operator can answer "1 yes, 2 no". Tables help.
- **The operator wants depth and examples:** quoted evidence, counts, before/after lines.
- **Verify what helpers report** against the sources before passing it on (this session's checks caught real errors every round).
- **Locked decisions:** when an instruction collides with one, say so plainly, write a proposal in `PROPOSALS.md`, and wait for the yes.
- **Answers are short.** When one is genuinely ambiguous, state the reading and ask once. "Do this" / "yes agree for all" covered the whole proposal it answered; record the reading in HANDOFF so it can be revisited.
- **Use waiting time; run helpers in parallel; commit their work as it lands** (the stop hook demands a clean tree, and the scanner's `.pyc` cache file is tracked, so commit it when it changes).

Learned in session 14:
- **Start by checking the clone is complete:** `git rev-parse --is-shallow-repository`. This container started with only 50 commits, and check 58 (it reads an old commit) failed on `main` until `git fetch --unshallow origin`.
- **Never `git stash` while helpers are writing,** and never `pkill -f <name>` with the name in your own command line (it kills the shell running it). Commit helpers' work as it lands; the stop hook demands a clean tree.
- **Image-only PDFs from Drive:** the Drive tools return no text and cap downloads at 10 MB. A file shared by link downloads with `curl -L "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"` into its own scratch folder; `apt-get install -y tesseract-ocr`, then `pdftoppm` one page at a time and `tesseract` with `OMP_THREAD_LIMIT=1` and four in parallel (about 1,500 pages in under an hour).
- **The operator wants plain wording for questions:** "your 1 - 8 are worded confusing. please simplify". Say what went wrong, then the fix, with an example; no file names or jargon in the question itself.

Learned in session 5:
- **How the operator tests:** they run the skills on claude.ai (`/script-writer`, pick the channel, paste title, brief, rotation log) and paste the whole output back. Save each run in `tests/iterations/iter-NN/test-run-NN/` (labelled TEST), run the scanner on it yourself, fetch the channel's real video on the same title with NexLev (`youtube_channel_videos`, then `get_video_transcript`) and have a judge helper compare. The writer's own audit can be wrong: run 02 claimed "mechanical 0" with 97 curly quotes.
- **Like-for-like tests:** the same title and brief as a published video, compared with that video and with the hits.
- **Emotion is the gap.** The operator wants scripts that make the viewer feel it: strong plain words, the exact pain points, the villain all through, opinion-outrage at big prices, lots of "but", questions, the title's feeling repeated. Not worst-case exaggeration. Not "up to scratch" yet.
- **Prices:** always estimated, never cents, researched and double-checked; the operator likes agents checking agents.
- **Web search is capped at about 200 searches per round, shared by all helpers.** Split big research into rounds (research, then gaps, then verification).
- **What's on the account:** check `/root/.claude/skills/synced/<id>/` against `dist/` (`diff -rq -I 'Version:'`) and send only the files that changed. The operator confused the CTA script types once (Roger is Classic: no markers).

## Branches

- Every chat works on its own `claude/...` branch; `main` is the shared starting point.
- Session 7's branch `claude/amazing-lamport-08irk0` is merged into `main` at this handover. It carried in two branches that had never reached `main`: `claude/zealous-goldberg-c43er6` (session 6) and `claude/relaxed-faraday-u4j0df` (the Frederick chat, 2026-10-22).
- Session 5's branch `claude/exciting-lamport-jasm2p` was merged at its handover.
- **`claude/pensive-gates-4c5yrt` (the parallel chat's woodworking tests iter-01 to iter-03) was merged in this session** with both sides kept (`CHANGELOG.md` has every row of both), so it's in `main` now.
- **Session 9's branch `claude/hvac-research-czb2hy` (the HVAC pack) is merged into `main` at its handover,** with `main`'s session 8 (electrical) merged in first and both sides kept in every shared file (`core/channels.md` rows 7 and 8, `tools/build_skills.py`, `tests/run_checks.py` checks 46-52 and 60-68, `README.md`, `HANDOFF.md`, `personas/README.md`).
- **Session 10's branch `claude/electrical-scripting-session-ayrkjc` is merged into `main` at its handover,** with `main` (session 9, HVAC) merged in first and both sides kept: `core/script-scanner.py` (the electrician tenure words and P13's fixes together with the HVAC tenure words, the "no for" pattern, third-party years and `letters-ok`; letter sets judged once, with the niche's `letters-ok` skipped), `core/channels.md` (Frederick **ready**, row 7; Roger the HVAC Guy, row 8), `tools/build_skills.py` (both channels; `--final` on every scanner command, HVAC's included), `README.md`. One collision fixed: session 10's check 60 is now **69** (HVAC's are 60-68). 76 checks pass.
- **Session 11 (2026-10-27, branch `claude/wonderful-curie-0puxc3`) merged Werner's branch `claude/vigilant-keller-um63cs` into `main`,** which also carried the plumbing branch `claude/festive-planck-2e8f22` (the escalation line, model R21; merged into Werner's branch there). Both sides kept. Collisions fixed: Werner's channel row is **9** (Roger the HVAC Guy keeps 8); Werner's check 61 is now **70** (HVAC holds 60-68); the plumbing escalation line's "P11" is now **P17** (P11 is the electrical value promise, P14-P16 are Werner's). No branch with unmerged work is left outside `main`.
- **`dist/` is not rebuilt at this merge** (on purpose). A build of `main` checked against the account on 2026-10-27 (session 11): every script skill matches apart from frontmatter quote marks, except `script-writer`, which differs only by Roger the HVAC Guy's row (Werner moves to row 9) and the HVAC scanner changes (HVAC tenure words, `letters-ok`, third-party years, the "been/spent/worked" subject fix). The HVAC chat (finishing in its own chat) rebuilds and sends `script-writer`, `hvac-scripts` and `roger-the-hvac-guy-persona` together, so Roger the HVAC Guy is never on the channel list before his pack is on the account.
- **Session 12's branch `claude/wonderful-mccarthy-rbuweh` (the style study) is merged into `main` at its handover** (fast-forward: `main` had nothing new). It changed no library file: only `studies/style/`, `drafts/style-study-plan-DRAFT.md`, `HANDOFF.md` §3, `README.md`, `CHANGELOG.md` and this file.
- **Session 14's branch `claude/youthful-ritchie-zq7e92` (the style pack) is merged into `main` at its handover,** with `main` (session 13, the Werner and Frederick review, branch `claude/loving-planck-iad0s6`) merged in first and both sides kept: `core/script-scanner.py` (session 13's opening keys, homework ban and "Level" signposts together with session 14's title words, channel-intro ban, style tenure words and style signposts), `tests/run_checks.py`, `HANDOFF.md`, `CHANGELOG.md`, `PROPOSALS.md`. Collisions fixed: session 14's checks 73-82 (and 81b) are now **83-92 (91b)** (session 13 holds 73-77); its P18 and P19 are now **P19 and P20** (session 13 holds P18). 96 checks pass.
- **`dist/` is not rebuilt at this merge.** Session 13 rebuilt and sent nine skills; since then the core changed (session 14: the channel gate in `workflow.md` §1, the scanner's title words, style tenure words and signposts, CTA blocks out of the item counts), so the next `script-writer` build differs from the account. Send it together with `style-scripts` and the two style personas once the style channels are ready, or sooner if the operator wants the channel-gate change on every channel now.
- Earlier branches are contained in `main`. Leave them.

---

## Where things stand

### Session 14 (2026-10-28/29), in short: the style pack, Scarlett Starling and Diane de Chambray (branch `claude/youthful-ritchie-zq7e92`)

Every operator answer is in `HANDOFF.md` §3 (the session 14 blocks); the study log is `studies/style/log.md` (round 6).
1. **The models** (P19: outliers of the last 24 months plus a few big older ones, nothing before 2022): 30 real presenters (M01-M30, two of them from a targeted item-list search) and 7 faceless structure-only videos (F01-F06, F08; F07 dropped, mostly music), all collected with transcripts, comments and notes (`studies/style/models/approved-models.csv`). No real presenter has a jewelry, glasses or earring video above the floor.
2. **Hair against fashion** (`studies/style/comparison/08-hair-vs-fashion.md`): mostly the same feelings; the blame (hair: the stylist; fashion: the fit), the named feeling (hair: fear of the change; fashion: the body) and the hard words (fashion) differ. One pack with a hair note and a fashion note.
3. **The diagnosis** (`drafts/style-pack-diagnosis-DRAFT.md`, answered) and **P20, core scanner changes** (every channel): a `title-words` key (each title word said twice, once in the first minute), "this channel is for" a hard ban, style tenure words, "Rule number three" signposts, the build script's unclosed code block.
4. **Built:** `style-scripts/` (SKILL.md; the hook rule: every hook carries one winning model's format from `references/hooks.md`, short, aimed at the title's feeling; `hooks.md`, 37 model files and INDEX, 81 excerpts, four provisional voice samples, the unit plan); `personas/scarlett-starling.md` (two t's: "scarlett it is written as") and `personas/diane-de-chambray.md`, both **pending**; both books indexed from OCR of the operator's PDFs (`personas/books/`: 300 Ways, 101 Secrets confirmed); channel rows 10 and 11; build entries; README.
5. **The operator's style rules** (HANDOFF): no sign-offs (the comment ask about her ends the video); the book is the only CTA, no subscribe ask; the salon is never the enemy; no ages and no "one of us"; prices only on budget titles; opinions against brands allowed; the safety defaults unless the brief says otherwise; French words written for the voice; Scarlett's credential numberless ("a lifetime of dressing well"); Diane's one heritage line ("the way I was raised in Paris"); three personal details each, drafted by Claude.
6. **Tests** (`tests/iterations/iter-07/`, writer, VA and judge kept apart, like for like): 117, 121 and 116 of 140 (hook double-weighted) against 68, 68 and 65 for our old scripts on the same titles; every judge "fix, then pass". The operator's answers to the fixes are applied (the channel gate confirms a clear one-channel reply, on every channel; the book title allowed; "age" and "weight" title words, lightly; item length by count; Diane's hedges; plain checks and varied endings). Not applied: an added feeling move in hooks ("we model off winning hooks for now still").

### Session 13 (2026-10-29), in short: the Werner and Frederick upload review (branch `claude/loving-planck-iad0s6`)

1. **Reviewed** the first library-made upload on each relaunched channel (Werner's toilet video, 11:06; Frederick's outlet video, 19:52): `studies/recent-uploads-2026-10-29/` (caption transcripts, `analysis.md`).
2. **The operator's answers, applied** (HANDOFF "Operator decisions, 2026-10-29"; P18):
   - plumbing words per minute set from the newest voiceovers (Roger 170, Mark 181, Vintage 190, Werner 181); the minimum stays 12 minutes, now counted at them ("Real speed, keep 12"); Frederick 162
   - plumbing opening: a short hook on a named model's beats, first tip by about 45 seconds, no tool list and the kit named once, at most one promise and only one paid at the end (P18), no "no plumber needed" when a step ends in a call, the silence line in plain words
   - every channel: the close gives one small thing to do, never a homework list (core §14, B9, packs, scanner hard ban)
   - electrical: one step, one job; the buying step adapts to what the look found; facts guide 1.17a, 1.18, 4.30, 6.19a
   - scanner: `opening-ban-regex`, `opening-promise-regex`, `judge-regex`, "Level" signposts; checks 73-76 (84 pass)
3. **Second round (same day):** HVAC took the plumbing opening rules and always models off winners; plumbing talking-point briefs are enough; Pfusch stays; no sibling check. Check 77.
4. **Skills rebuilt** into `dist/`; nine differ from the account and were sent (plumbing and HVAC re-sent after the second round): `script-writer`, `plumbing-scripts`, `electrical-scripts`, `hvac-scripts` (the ending line only), and the personas of Roger the Pipe Guy, Mark, the Vintage Pipefitter, Werner and Frederick.
5. **A check of the newest plumbing uploads with the new rules:** item one at 51-73 seconds on six of eight lists; two of the Vintage Pipefitter's three newest under 12 minutes; one Vintage opening with two promises. These rules now catch all three.

### Session 12 (2026-10-28), in short: the style study for Scarlet Starling and Diane de Chambray (branch `claude/wonderful-mccarthy-rbuweh`)

A research-only session: no library file, skill or rule changed. Everything is in `studies/style/` (start at its `log.md` and `comparison/README.md`). Every operator answer is in `HANDOFF.md` §3, the three style blocks of 2026-10-28.

1. **The plan** (`drafts/style-study-plan-DRAFT.md`, approved) followed the HVAC method: own baseline, scrape, outliers, script and comment study, analysis.
2. **Own baseline** (`own-baseline-2026-10/`): all 38 videos (Scarlet 25, Diane 13, from 2026-09-20). Normals: Scarlet 532, Diane 607. Top: necklaces 39,935, jeans 12,620.
3. **The scrape and outliers** (`discovery/`, `round2/`):
   - 357 channels screened; 236 kept after the language check (13 Spanish, German and French channels dropped; their titles are auto-translated)
   - 2,478 outliers, in `round2/BREAKOUT-MAP.md`
   - the operator's own list of winners resolved (`inputs/`)
   - NexLev ran out of its 2,000 weekly calls once; the operator topped up. About 1,500 calls in all.
4. **The script and comment study:** 45 videos (21 real, 24 faceless or AI, 4 copycat pairs), two Spanish ones swapped, a check round, and analysis files `comparison/00`-`07`. Findings and 14 suggestions are in `comparison/README.md`. The biggest gaps in our scripts:
   - the same self-introduction and book pitch in all 38
   - teases
   - the title's word never said ("instantly" in 14 titles, 0 videos)
   - "but", "I" and questions far below the winners
   - a house vocabulary ("small gold hoops" in 22 of 38)
5. **The operator's answers** (HANDOFF §3):
   - **Packs:** three, hair, fashion and makeup (the reading needs confirming).
   - **Models:** real people only ("they are the source material"), Justin Hickox included, 24 months plus big outliers, 20-30, each verified by the operator. Voice samples come from women only.
   - **Emotions:** the rules are built from this niche, not copied from plumbing. "Practical solutions to emotional problems."
   - **Suggestions:** 2, 4, 5, 7, 9, 10 yes; 6 and 11 with conditions; 8 to the profiles; 12 maybe from the brief.
   - **Names:** the channel is **Scarlet Starling**; Vivienne Morgan is a competitor AI channel.
6. **The emotion and age analysis** (`comparison/07-emotions-and-age.md`):
   - the operator's three feelings (unheard, frumpy, losing her spark) are rare in what viewers write; permission or pride (113) and relief at being understood (46) lead
   - real presenters name a feeling in about a quarter of items, one sentence, often their own; ours 1 in 11
   - age brackets are not distinct enough for four rule sets; the suggestion is one set with a light over-70 lean (not answered yet)
7. **Model candidates:** `models/candidates-for-review.md`, 72 rows (rows 1-38 women, last 12 months; 39-42 Justin's last 12 months; 43-64 12-24 months; 65-72 big older outliers). 15 are already collected. **Waiting for the operator's picks.**

### Session 10 (2026-10-27), in short: the electrical tests, Frederick ready (branch `claude/electrical-scripting-session-ayrkjc`)

1. **The operator's answers** (HANDOFF section 3, "the electrical scripting chat (session 10)"): E1 apply all of P13; E2 numbers in words; E3 **no**, title numbers win (P13 item 7 rejected); E4 yes to both (offer-rules §5 scoped to CTAs, pitches, descriptions and pinned comments; Federal Pacific's independent test results with the source); E5 **ElevenLabs** (voice name and ID not given yet), "mark ready, check later"; E6 leave the ideation skill; **P12 rejected.**
2. **P13 applied (core, every channel):** the tenure check reads "thirty-five years" and catches electrician wording; amp, volt, watt and gauge words are number-checked; letter sets and two-way words judged once with a count ("live", "lives"); voice tags in the script and **sentences over 35 words are fix-on-sight**; `--final` fails a script under the minimum; ITEMS and SENTENCES report lines (keys `item-words`, `first-item-seconds`, `sentence-max`, and `example-guard`, a 5-word guard on a pack's quoted example sentences); the audit's evidence block quotes the script (Items, Sentences, I-verdicts, Turns, Title word); **`tools/verify_output.py`** re-counts a saved output against its evidence (the main session runs it before every judge: `CLAUDE.md`).
3. **Frederick Barnes is ready** (`core/channels.md` row 7); his profile has the 92-word voice-check paragraph for the operator to generate.
4. **Three test runs** (`tests/iterations/iter-05/`, brief A12 "The REAL Reason Your Plug Won't Stay In The Outlet", writer, VA and judge kept apart): 101, 110, 111 of 130. The chat refused "just write it" and a missing rotation log. Each run's library fixes were applied before the next (L1-L8, N1-N5, N7-N10; the operator: "answer the questions yourself based on what you think is best"), above all the prove-dead order at a device, "look before you shop", the two-slot fallback, "open ground" explained, a short-sentence floor (12%, one per item), and the pack's example lines moved off locked topics. The run 03 judge: ready to deploy once N7 and N8 were in (they are); check the prove-dead step on the first real script.
5. **The model library:** the operator removed the five models before 2022 and the science channel (E08, E12, E17, E20, E23, E38; kept in `studies/electrical/models-removed-2026-10-27/`); 31 remain, all 2022 on, structure only.
6. **Uploaded by the operator:** `script-writer`, `electrical-scripts`, `frederick-barnes-persona` (session 10's build). The Werner chat has since uploaded its own `script-writer` on top of it (see "Branches").
7. **Google Sheet:** the 17 electrical ideas (title, brief, thumbnail text, thumbnail instructions with reference links, reference video) added to the operator's "FREDERICK BARNES" sheet, rows 41-59, below the old fire-prevention ideas (left untouched).

### Session 9 (2026-10-27), in short: the HVAC pack and Roger the HVAC Guy (branch `claude/hvac-research-czb2hy`)

The HVAC research chat (it also did the HVAC study in `KPMYT/niche-research`, batch 1's 16 ideas, thumbnails and briefs, and the `hvac-ideation` skill).

1. **Operator decisions** (HANDOFF section 3, three blocks of 2026-10-27): Roger the HVAC Guy is the same man and voice as Roger the Pipe Guy (45 years), no book for now (a one-line subscribe ask, then the comment ask); DIY limits "depend the title"; the two Rogers never mention each other; the study's 12 suggestions answered (2-9 and 12 agreed; items about 150-250 words; models where one fits; voice samples decided later); **every reference is a real person on camera** ("we dont want any ai or faceless for reference"), Silver Cymbal added.
2. **Built:** `hvac-scripts/` (SKILL.md from the plumbing pack, changed only where HVAC differs; the unit plan; voice samples, provisional; 151 real on-camera excerpts; 31 model files R04-R44 with INDEX; the **price guide**, 125 rows, four researchers and four checkers plus a fifth pair for three shelf items, research in `studies/hvac/price-research-2026-10/`); `personas/roger-the-hvac-guy.md`; `core/channels.md` row 8; scanner changes (HVAC trade words in tenure, a `letters-ok` key, third-party years skipped); run_checks 60-68. The study is in `studies/hvac/`.
3. **Tested** (`tests/iterations/iter-06/`, the writer, VA and judge kept apart): two rounds on batch 1 #4 and #14. Round 1 was safe and clean but flat; the cause was the pack's own emotion section missing the plumbing rule's examples, now put back. Round 2: "you"/"your" about 40 and "but" 6.5-7.3 per 1,000 words, level with the passed plumbing script; both **fix, then pass** (about six lines each, writer slips). Every library gap the judges named is fixed (`iter-06/CHANGES.md`). **Roger the HVAC Guy is ready** (as Sam was: the operator's own tests decide next).
4. **niche-research:** batch 1's briefs corrected from the price research (35 figures in 15 briefs; the signed-off originals kept), `studies/hvac/ideation/batch1-briefs-2026-10-27-corrected.*`.
5. **`dist/` rebuilt** after session 11's merge (all nine channels; seventeen skills). Sent to the operator: `script-writer`, `hvac-scripts`, `roger-the-hvac-guy-persona` and `plumbing-scripts` (the villain example); the other thirteen match the account in content. **After the tests the operator answered H1-H3, H5 and H6** (HANDOFF "after the HVAC tests"): the villain example reworded in both packs, the `require-if` scanner key (every carbon monoxide and gas-leak step), split reframes counted and "don't" instructions not, brief and title always win, the ElevenLabs voice the same as Roger the Pipe Guy's (already so; the voice samples stay provisional). Merged with session 10 again afterwards (the HVAC checks renumbered 71-72; 78 pass).

### Session 8 (2026-10-27), in short: the electrical pack and Frederick Barnes (branch `claude/intelligent-ride-v1at70`)

The same chat finished the electrical ideation in `KPMYT/niche-research` (17 initial ideas with thumbnail instructions and briefs; the `electrical-ideation` skill, which the operator installed), then built the script skills here.

1. **Operator decisions** (HANDOFF section 3, "Operator decisions, 2026-10-27"): Frederick is the electrical channel; 35 years; no book (a very short subscribe ask, then the comment ask, "we say we read every comment"); Talking Head; models from real channels with 1M+ views, recent; 12-minute minimum, 15-22 the aim; villain optional; the brief can add safety, never remove it; named panels only with CPSC or inspector words; no job stories; no swearing; **P11** (one value promise allowed in the electrical opening, "by the end of this video you'll know…", never items one to three; electrical only).
2. **Built:** `electrical-scripts/` (SKILL.md, unit plan, facts guide of 277 checked rows with no prices, 37 model files E01-E38 with beat maps and "Emotion voicing", INDEX, voice samples, excerpts, model-file-spec); `personas/frederick-barnes.md` (status **pending**); `core/channels.md` row 7 (pending); build and install text for 13 skills (`tools/build_skills.py`); run_checks 46-52. Study files in `studies/electrical/` (model picks, transcripts, the 99-lesson file, the facts research and re-check, the seven review reports).
3. **Reviewed by seven checker helpers** (formats, emotion, models, voice and scanner, safety and claims, persona and workflow fit, coverage of the 99 past problems; reports in `studies/electrical/pack-review-2026-10-27/`): 17 blockers, 73 major, 81 minor in all. Every pack- and persona-level fix is applied (CHANGELOG rows of 2026-10-27). The facts guide was re-checked row by row (214 rows: 165 confirmed, 35 adjusted, 9 thin). All 59 checks pass.
4. **Not done yet:** the skills aren't rebuilt into `dist/` (build after the operator's answers below); no test script has been written; Frederick stays pending until his voice is confirmed.


### Session 7 (2026-10-23), in short: two new channels, research first

1. **The operator chose two new channels** (HANDOFF section 3, "Operator decisions, 2026-10-23"):
   - **Roger the HVAC Guy:** a new channel; Roger the Pipe Guy carries on.
   - **Frederick Barnes, a new brand:** electrical DIY, electrical safety and fire prevention. This replaces the 2026-10-22 "broad home DIY" direction. His background is open; his book changes.
2. **Both packs are built from the plumbing pack, later.** Research comes first, in the other repository, **`KPMYT/niche-research`** ("keep niche reserach and scripting in seperate repos"):
   - two research chats there, one for HVAC and one for electrical and fire prevention, following its `RESEARCH-BRIEF.md`
   - then conclusions
   - then, on the operator's call, the ideation skills, base ideation plans and thumbnail plans, also there
   - then two scripting chats here
3. **The 2026-10-22 research was recovered.** The "Roger the Pipe Guy sub-brand opportunities" chat never pushed, so its transcript was read in full and saved to niche-research (`recovered/`, `findings/2026-10-22-hvac-and-electrical.md`). Key points, not re-checked:
   - HVAC is crowded (Ray Dutton's Garage is Roger's model in HVAC; there's also a "John The HVAC Guy").
   - HVAC runs on distrust of the trade, mistakes and the bill, but not on fear of damage.
   - Electrical runs on mistakes and "the hidden thing", not on money.
4. **Two loose ends merged:** session 6 and the Frederick branch (above). All 46 checks pass.

### Session 6 (2026-10-21), in short (branch `claude/zealous-goldberg-c43er6`)

1. **The plumbing emotion draft is applied** (Parts 1-5, each a yes):
   - "Emotion, all the way through"
   - the list item shape
   - Roger's and Mark's CTA template
   - the judge's six fixes
2. **Test run 03** (`tests/iterations/iter-04/test-run-03/`) closed most of the emotional gap against run 02 ("you" 21 to 39 per 1,000 words, "but" 1.3 to 6.9, questions 0 to 7).
3. **The operator's answers to run 03** are applied (HANDOFF section 3):
   - the mid-video CTA a third in, never before the end of item 3
   - an outright comment ask at the end
   - item length a guide, not a cap
   - "but" to join sentences
   - the title's word back more often
   - named-source figures
4. **The skills were rebuilt and are on the account:** at 2026-10-23 the synced copies match `dist/`, apart from quote marks in the frontmatter.

### Session 5 (2026-10-21), in short

1. **Step 4 done: the plumbing pack is in the library** (`plumbing-scripts/`). Draft comment and status tags stripped; a table "Where this pack overrides the core" names every core rule it changes; Roger, Mark and Vintage are `ready` in `core/channels.md`.
2. **The two chats merged** (this one and `pensive-gates`), then **six audit helpers** checked everything for contradictions and cross-contamination. About 40 fixes followed, every finding re-checked first: scanner bugs (pipe ages read as tenure, "a hundred and fifty" read as 50, "at the very end" in build steps, runtime at 150 wpm for every channel), core wording that contradicted decisions (Dale's family line vs the offer rules, "I read every one" vs the offer rules, the end CTA log, title numbers win for `tenure: none`), plumbing overrides (hook, value line, cents devices, sources, signposts, ending), allow lines so profiles' required CTA wording passes the copy guard.
3. **Decisions this session** (all in HANDOFF section 3):
   - Plumbing never needs sources; the originality score drops that signal.
   - The rotation log comes from the same chat.
   - **Vintage's tenure is 45** (P6): Roger 45, Mark 40, Vintage 45.
   - **P7:** where the brief is silent, the script fills in; prices from the brief, then the **price guide**, always as estimates, never cents, at most one per item, most items costed in words.
   - Range wording: "anywhere from X to Y, depending on where you live", "on the high end, up to X".
4. **The price guide** (`plumbing-scripts/references/price-guide.md`): about 140 jobs, parts, damage costs, shelf items and safety facts, researched by four helpers plus a gap pass, re-checked by four others against different sources; each row marked confirmed / adjusted / thin / in words. Evidence in `studies/plumbing/price-research-2026-10/`. Safety facts corrected along the way (scalding at 140 degrees is six seconds, not five; never credit "3-5% per 10 degrees" to DOE; the gas steps follow the utilities).
5. **The plumbing ideation skill** is in the library (`ideation/plumbing-ideation/`): Mark 40, "Finkbinder" corrected to Finkbeiner (outside the archive), and briefs now give each item its cost and the right way.
6. **Step 5 begun: two plumbing tests** (`tests/iterations/iter-04/`, Roger, "15 Plumbing Mistakes Quietly Costing You THOUSANDS", the same brief as the real video 3tsYa7aOprw):
   - **Run 01:** refused with NOT READY (the brief priced 2 of 15 items). Led to P7 and the price guide.
   - **Run 02:** written in full, 3,000 words. The judge: better than the original (opening 8 vs 4, CTA and ending 8 vs 3, safety 8 vs 6) but **not up to scratch**: number load 4 vs 7 (25 dollar amounts), 97 curly quotes, two lines echo the pack's own examples, incomplete gas steps, five unexplained trade terms. Three comparisons (real creators, TheCheapFix, Roger's 453x and 364x hits) found the emotional gap: few "you"s, no questions, almost no "but", items ending on instructions rather than wins, the villain and the title's feeling dropped after the opening, little disgust, items too long, and the CTA not in Roger's hit order.
7. **The draft for the next chat:** `drafts/plumbing-emotion-and-cta-DRAFT.md`, with the operator's reply at the top.

### Built and on the account

- **The operator uploaded:** `script-writer`, `plumbing-scripts`, `plumbing-ideation` (build `70f71d5`), and the other script skills from build `f62cd9e` (same content as now). At the end of session 5 the account matched `dist/` exactly.
- **Not changed since:** nothing in the skills changed after `70f71d5` except the draft and test files, which aren't in any skill. A rebuild is needed only once the draft is applied.

### Not yet true

- **No plumbing script has passed the judge yet** (run 03 was close; no run 04). Mark and Vintage haven't been tested.
- **Frederick Barnes is ready and on the account** (three test runs, session 10); his ElevenLabs voice name, ID and voice check are still to come. The HVAC pack is built and tested (session 9); Roger the HVAC Guy is ready but not on the account yet.
- **Werner's lines** in the plumbing ideation and thumbnails skills are not cleaned up (waits for a yes).
- **The thumbnails skill** (not in the repo) still says Mark has "no tenure number fixed yet" and Vintage "45 years" (now correct); Werner is still unnamed there (he is row 9 in `core/channels.md`, ready).

## Open questions for the operator

**Werner and Frederick (open at the session 13 handover):**
- ~~W13 Pfusch~~ ("leave for now"); ~~W14 a sibling check~~ ("not your problem"); ~~W15 HVAC~~ (applied, "always model off winners").
- W16. **Roger the HVAC Guy's words per minute** is still unset (counted at 150). His ElevenLabs voice is Roger the Pipe Guy's, which reads at 170: set 170 so the HVAC 12 minutes is real too?
- E9. **Lines that don't survive the voice** (explained in chat 2026-10-29): add rules for a quoted label read aloud, a comma that turns a statement into a question, lists of fragments, and pronoun-packed short lines?
- ~~The plumbing briefs~~: talking-point briefs are fine; each point is built out with P7's fill-ins (applied).

**Style (open at the session 14 handover):**
- S6. **Scarlett's voice company:** ElevenLabs like Diane's "Sylvie", or another? Her profile doesn't say (Notion gives an ID in a non-ElevenLabs format), so the test writers guessed the VO copy's format.
- S7. **The voice samples:** the operator's listen to Tracy Campoli or Melissa Murrell for Scarlett (Melissa is British) and Marie-Anne Lecoeur for Diane (`style-scripts/references/voice-samples.md`, provisional).
- S8. **Diane's personality section** is shorter than Scarlett's (no pacing, audience or hard-no lines in her own section): add them to match? Asked, not answered.
- ~~S1-S5~~ answered (HANDOFF session 14 blocks).

**HVAC (asked 2026-10-27; H1, H2, H3, H5 and H6 answered the same day, see HANDOFF "after the HVAC tests"; H4 still open):**
- H1. ~~The villain example line~~ (answered: "up to you"; reworded) in the HVAC and plumbing packs joins its two facts with "so" ("The trade is paid by the visit and the install, so a cheap check that ends the visits is nobody's business to mention"), and the HVAC writer copied it with "since", one step from a motive. Reword it as two separate sentences?
- H2. ~~Core scanner checks~~ (answered: "ok yes"; built) (every channel): list sentences over about 35 words; catch "it's not X, it's Y" split across two sentences; check every carbon monoxide step is there. *Partly settled in session 10:* sentences over 35 words are now fix-on-sight (P13); the split reframe was rejected (P12 "No"); the carbon monoxide step check is still open.
- H3. ~~A brief price that disagrees with the price guide:~~ (answered: "brief always wins") should the input gate flag it? Today the brief wins.
- H4. **The rotation log** has no field for the subscribe line's opening words, though the profiles say they go there (plumbing too).
- H5. ~~Batch 1 title notes:~~ (answered: "title always wins also") #3 "The $5 Filter ... Better Than the $30 One" (a MERV 8 runs $6-$10, a MERV 11-13 $10-$25) and #14's "$300" (the top, at night or on a weekend); niche-research `batch1-brief-corrections-2026-10-27.md`.
- H6. **Voice samples and words per minute** for Roger the HVAC Guy: still the operator's listen ("same as plumbing voice" meant the ElevenLabs voice, which is already Roger the Pipe Guy's).

**Electrical (open at the session 10 handover):**
- E7. **Frederick's ElevenLabs voice:** the voice name and ID, then the clip of the voice-check paragraph in his profile: how it says GFCI, AFCI and UL, whether the contractions and "live" are clean, and the clip's seconds (sets his real words per minute; scripts are sized at 195).
- E8. **The old fire-prevention rows** (1-38) in the FREDERICK BARNES sheet: keep, move to another tab, or mark retired?
- The ideation-side items in niche-research's handover (the registry; A29's "I Find"; two "30 years" titles, which now keep 30 in their scripts since title numbers win).

**Older:**
1. ~~Frederick's background and his new book~~: answered 2026-10-27 (retired electrician, 35 years; no book for now).
2. **Roger the HVAC Guy against Ray Dutton's Garage:** how it stands apart (the 2026-10-22 research suggested old-house heat and the winter bill).
3. **Whether the new packs need a script transcript study here** (`studies/<niche>/`, as `CLAUDE.md` "Adding a niche" says) on top of the research in niche-research: the scripting chats ask once.
4. From session 3, still unanswered: the "title's strongest word" rule; the woodworking ideation and Hank script test outcomes; "avatar + object + text, always" in the woodworking ideation skill.

## Next actions (in order)

**Style (next):**
1. Read `CLAUDE.md`, this file, `HANDOFF.md` §3 (the session 14 blocks), `style-scripts/SKILL.md`, both style profiles and `tests/iterations/iter-07/CHANGES.md`.
2. Get S6-S8. Then a second test round (iter-08) on the fixed library, the same way (a brief writer, the VA helper, writers on built skills, judges with the rubric in `iter-07/`), ideally new titles plus one rerun, so the fixes are tested.
3. When a round passes and the voice samples are heard: set both channels **ready** (`core/channels.md`, both profiles), add them to the script-writer's "Channels ready now" description and the INSTALL text in `tools/build_skills.py`, rebuild `dist/`, and send `script-writer`, `style-scripts`, `scarlett-starling-persona` and `diane-de-chambray-persona` together.
4. Kept for later: the makeup pack; the copycat-pair notes (`studies/style/comparison/05`, `05b`); the ideation skill's brief spec ("we dont need ideation yet": it suggests "women I know in Paris", French phrases and dollar figures the pack treats as background).

**Electrical (next, on the operator's call):**
1. Read `CLAUDE.md`, this file, `HANDOFF.md` section 3 (the 2026-10-27 blocks), `tests/iterations/iter-05/README.md` and the three judge reports there.
2. When the operator sends the voice details: fill in the profile's voice provider line and the voice check, adjust words per minute if the clip says so, rebuild and send `frederick-barnes-persona` (and `script-writer` only together with the HVAC chat's `hvac-scripts` and `roger-the-hvac-guy-persona`, or once they are on the account).
3. Check the first real Frederick script the operator pastes back: the prove-dead step against Safety rules 1 and 2, then the run 03 judge's non-blocking notes (open-box "I" lines, sentence length creeping up, procedure-first step openings).
4. A14 (the LED glow) has no topic model since E38 went: use the closest explainer, as INDEX says.

**Merging branches:** done in session 11 (Werner and festive-planck are in `main`). Any chat that merges later: merge `main` into its branch first and keep both sides; check numbers in use are 1-77 and 83-92 (plus letter suffixes such as 46b and 91b; 71-72 are the HVAC chat's, 73-77 session 13's, 83-92 session 14's); proposals in use are P1-P20.

**HVAC chat (next):** read `tests/iterations/iter-06/CHANGES.md` and the HANDOFF blocks of 2026-10-27; get H1-H6; the operator's own test scripts on batch 1 (the corrected briefs) decide further fixes. Both of those branches are in `main` now (session 11): merge `main` into the HVAC branch first (Werner is channel row 9, his check is 70, the plumbing escalation line is P17), then rebuild `dist/` and send `hvac-scripts.skill`, `roger-the-hvac-guy-persona.skill` and the new `script-writer`. Batch 2 needs the brand-verdict rules first (a brand verdict stops NOT READY today).

**Original plan (sessions 7-8):**
1. ~~The research, in `KPMYT/niche-research`~~ (done for both niches).
2. **Two scripting chats here,** one for Roger the HVAC Guy and one for Frederick Barnes (the electrical one ran in session 8). Each:
   - checks it started from `main`
   - reads the niche's `CONCLUSIONS.md` in niche-research
   - asks question 3 above
   - builds the niche pack from `plumbing-scripts/` ("Adding a niche" in `CLAUDE.md`)
   - builds the persona profile
   - adds tests
   - adds the channel to `core/channels.md`

   Every rule and skill change is shown to the operator first. The two chats keep to their own pack folders; shared files get one row each, and both sides are kept on merge.
3. **On the operator's call:** plumbing test run 04; tests for Mark and Vintage; the thumbnails skill's tenure lines; Werner's cleanup; the remaining iter-00 audit findings.

## Active channels (confirmed by the operator, 2026-10-19)

The spellings here are correct; where a skill differs, the skill has the typo.

| Channel | Niche | Typo in the skills |
|---|---|---|
| Roger The Pipe Guy | plumbing (45 years) | |
| Mark Silverbridge | plumbing (40 years) | |
| Vintage Pipefitter | plumbing (45 years) | |
| Werner Finkbeiner | plumbing, the German way: **relaunched** 2026-10-27, 30 years, Talking Head, *Werner's 101 Free Repairs*; **ready** (channel row 9), merged into `main` in session 11 | his old lines still in plumbing ideation and the thumbnails skill |
| Dale Oakfield | woodworking for profit | |
| Hank Hardwood | woodworking for profit | |
| Norbert Daniels | home security: the retired Locksmith | |
| Lance Kavanaugh | home security: the Navy veteran | |
| Frederick Barnes | home electrical (2026-10-27): retired electrician, 35 years, Talking Head, no book; **ready** and on the account (session 10; ElevenLabs voice name to add) | |
| Roger the HVAC Guy | HVAC (2026-10-23): Roger's persona and triggers; **ready** (session 9), not on the account yet | |
| Scarlett Starling | style (50+ women): the affluent American; `style-scripts` pack and profile built, **pending** (channel row 10; session 14); the name is never spoken in a script | "Scarlett Sterling" (ideation) |
| Diane de Chambray | style: "the French way"; `style-scripts` pack and profile built, **pending** (channel row 11; session 14) | ideation: "name TBC" |
| Helena Hart | air travel: the former flight attendant | air-travel skill says "name TBC" |
| Backyard Brenda | animals: chickens | "Backyard Bertha" |
| Walter Wren | animals: backyard birds | |
| Luca Merino | animals: cats | "Luca Marino" |
| Beau Carter | animals: dogs | |
| Gideon Grant | philosophy (Stoic) | |

Not active: Master Kenji and Sawdust Sam (woodworking), and the fabrics channels.

## The operator's skills

- **Where they sync:** read-only, to `/root/.claude/skills/synced/<id>/`.
- **The script skills on the account (end of session 5):** `script-writer`, `woodworking-scripts`, `plumbing-scripts`, the five persona skills (Hank, Dale, Roger, Mark, Vintage), `woodworking-ideation`, `plumbing-ideation`, `ideation-core`; all match `dist/`.
- **How changes reach the account:** make them here, rebuild with `python3 tools/build_skills.py`, check which differ from the synced copies, send the operator only those `.skill` files, and the operator replaces them (delete the old, upload the new).
