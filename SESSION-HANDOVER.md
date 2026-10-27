# Session handover

The live note passed from one Claude Code chat to the next. A new chat reads `CLAUDE.md`, then this file, then `HANDOFF.md`, `README.md` and `PINNED.md`, and carries on from "Next actions". The outgoing chat rewrites this file before every handover.

**Last updated:** 2026-10-27, session 8, the electrical scripting chat (branch `claude/intelligent-ride-v1at70`, merged into `main`). Session 8 is summarised first; sessions 5-7 follow.

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
- **Work niche by niche.** Plumbing is the current niche.
- **Notion and Google Drive are read-only** unless the operator says otherwise.
- **Keep messages plain,** with numbered items the operator can answer "1 yes, 2 no". Tables help.
- **The operator wants depth and examples:** quoted evidence, counts, before/after lines.
- **Verify what helpers report** against the sources before passing it on (this session's checks caught real errors every round).
- **Locked decisions:** when an instruction collides with one, say so plainly, write a proposal in `PROPOSALS.md`, and wait for the yes.
- **Answers are short.** When one is genuinely ambiguous, state the reading and ask once. "Do this" / "yes agree for all" covered the whole proposal it answered; record the reading in HANDOFF so it can be revisited.
- **Use waiting time; run helpers in parallel; commit their work as it lands** (the stop hook demands a clean tree, and the scanner's `.pyc` cache file is tracked, so commit it when it changes).

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
- Earlier branches are contained in `main`. Leave them.

---

## Where things stand

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
- **The electrical pack exists but hasn't been tested or built into `dist/`;** Frederick is pending. No HVAC pack exists yet (a separate chat).
- **Werner's lines** in the plumbing ideation and thumbnails skills are not cleaned up (waits for a yes).
- **The thumbnails skill** (not in the repo) still says Mark has "no tenure number fixed yet" and Vintage "45 years" (now correct); Werner is still unnamed there and in `core/channels.md` (no profile yet).

## Open questions for the operator

**Electrical (asked 2026-10-27, unanswered at handover; answer "1 yes, 2 yes…"):**
- E1. **The core checker fixes in `PROPOSALS.md` P13** (shared by every channel): the tenure bug ("thirty-five years" and "forty-five" read as a wrong figure; "forty years as an electrician" slips through), number words in the fact check, letter sets judged once, voice tags in scripts, a real length fail, the item and sentence report, a verifier for delivered outputs, extra evidence lines that quote the script, a 35-word sentence limit. Apply all?
- E2. **Numbers in words** for volts, amps, watts and wire sizes, against core "stats are digits" (P13 item 6).
- E3. **Titles with another years figure** (two ideation titles say "30 years"): back to ideation unless 35 (P13 item 7).
- E4. **Federal Pacific independent test results**: may they be said with the source named (P13 item 8, plus the offer-rules scope)?
- E5. **Frederick's voice**: ElevenLabs or Minimax and which voice. Then the voice check in his profile, then status ready (Sam's precedent) so tests can run.
- E6. **The electrical ideation skill** (niche-research) still allows "after all the houses I've worked in": change it?
- Also open: **P12** (count "doesn't X. It Y." as the one reframe, every channel).

**Older:**
1. ~~Frederick's background and his new book~~: answered 2026-10-27 (retired electrician, 35 years; no book for now).
2. **Roger the HVAC Guy against Ray Dutton's Garage:** how it stands apart (the 2026-10-22 research suggested old-house heat and the winter bill).
3. **Whether the new packs need a script transcript study here** (`studies/<niche>/`, as `CLAUDE.md` "Adding a niche" says) on top of the research in niche-research: the scripting chats ask once.
4. From session 3, still unanswered: the "title's strongest word" rule; the woodworking ideation and Hank script test outcomes; "avatar + object + text, always" in the woodworking ideation skill.

## Next actions (in order)

**Electrical chat (next):**
1. Read `CLAUDE.md`, this file, `HANDOFF.md` section 3 (2026-10-27), `PROPOSALS.md` P11-P13, `electrical-scripts/SKILL.md`, `personas/frederick-barnes.md` and the CHANGELOG rows of 2026-10-27.
2. Get the operator's answers to E1-E6 above. Apply what's approved (P13's scanner patches are drafted and tested in the review reports R4-R7 and their scratch notes; re-test them here, add the run_checks lines that wait for them: R4's check 52 tenure and number parts).
3. Once the voice is confirmed: the voice check in the profile, Frederick to ready, then the test cycle (`CLAUDE.md` "Testing with subagents"): a writer that sees only the library and one of the 17 briefs (niche-research `studies/electrical/ideation/briefs-2026-10-27.xlsx`; start with a fix or how-to title such as A12 or A1), an operator helper, and a judge against the rubric, the scanner and the reference video. Save it in `tests/iterations/iter-05/`.
4. Rebuild the skills (`python3 tools/build_skills.py`) and send the operator the new and changed `.skill` files (electrical-scripts, frederick-barnes-persona, script-writer once Frederick is ready).

**HVAC:** a separate scripting chat for Roger the HVAC Guy, as below.

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
| Werner Finkbeiner | **stopped** (2026-10-22) | his lines still in plumbing ideation and the thumbnails skill |
| Dale Oakfield | woodworking for profit | |
| Hank Hardwood | woodworking for profit | |
| Norbert Daniels | home security: the retired Locksmith | |
| Lance Kavanaugh | home security: the Navy veteran | |
| Frederick Barnes | home electrical (2026-10-27): retired electrician, 35 years, Talking Head, no book; profile built, **pending** (voice to confirm) | |
| Roger the HVAC Guy | **new** (2026-10-23): HVAC, Roger's persona and triggers | |
| Scarlet Sterling | style (50+ women): the affluent American | "Scarlett" |
| Diane de Chambray | style: "the French way" | |
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
