# Session handover

The live note passed from one Claude Code chat to the next. A new chat reads `CLAUDE.md`, then this file, then `HANDOFF.md`, `README.md` and `PINNED.md`, and carries on from "Next actions". The outgoing chat rewrites this file before every handover.

**Last updated:** 2026-10-21, end of session 5 (branch `claude/exciting-lamport-jasm2p`, merged into `main`).

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
- This chat's branch `claude/exciting-lamport-jasm2p` is merged into `main` at this handover.
- **`claude/pensive-gates-4c5yrt` (the parallel chat's woodworking tests iter-01 to iter-03) was merged in this session** with both sides kept (`CHANGELOG.md` has every row of both), so it's in `main` now.
- Earlier branches are contained in `main`. Leave them.

---

## Where things stand

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

- **The emotion rules, item shape, CTA template and the judge's six fixes aren't applied** (the draft).
- **No plumbing script has passed the judge yet;** Mark and Vintage haven't been tested.
- **The thumbnails skill** (not in the repo) still says Mark has "no tenure number fixed yet" and Vintage "45 years" (now correct); Werner is still unnamed there and in `core/channels.md` (no profile yet).

## Open questions for the operator

1. **Parts 3-5 of the draft** (the item shape and length, Roger's and Mark's CTA template, the judge's six fixes): the operator called the analysis "strong and correct" but didn't say yes to each. Ask once.
2. From session 3, still unanswered: the "title's strongest word" rule; the woodworking ideation and Hank script test outcomes; "avatar + object + text, always" in the woodworking ideation skill.

## Next actions (in order)

1. Check this chat started from `main` (`git fetch origin`, `git log -1 origin/main`).
2. **Apply the emotion draft** (`drafts/plumbing-emotion-and-cta-DRAFT.md`), after asking once about Parts 3-5:
   - **Part 1 + the operator's additions:** a new "Emotion, all the way through" section in `plumbing-scripts/SKILL.md`. Villain sporadically throughout, opinion-outrage at big prices ("that is absolutely criminal they charge that much", never a company or a motive), much more "but" inside and between items, the title's emotions reaffirmed throughout, questions.
   - **Part 2:** the simpler, stronger opening. Check it against the Voice section ("plain beats clever", which stays for wording) and the banned list.
   - **Part 3:** the item shape and length (about 100-130 words an item in long lists; never more than two hard cuts in a row).
   - **Part 4:** the CTA order from Roger's hits (after item 2 or 3, about a third in; aside, tied to the help, "one of a hundred fixes", pages, link and QR code, return). Update the "CTAs" section and Roger's and Mark's profiles' "Style and length" (the 20-60 words). It implements the locked "structure their hits used"; log it.
   - **Part 5:** the six fixes:
     - the number cap
     - straight quotes, plus the evidence line from a real scanner run (core `workflow.md`, `greenlight-audit.md`)
     - `plumbing-scripts/SKILL.md` into the copy-guard files (overrides row, build_skills scanner command, test)
     - full gas steps
     - the trade-terms list
     - "gets backwards" names the belief
   - Update the scanner block if needed (for example "criminal" must not trip a ban), add tests, update the README map and CHANGELOG, and remove the draft file once its content is in the pack (git keeps it).
3. **Rebuild, send only the changed skill files** (likely `plumbing-scripts`, `script-writer`, maybe the Roger and Mark persona skills), then **test run 03** on the same title and brief. Judge it against run 02, the original and Roger's hits on the same dimensions as the comparisons.
4. Then, on the operator's call: tests for Mark and Vintage; the thumbnails skill's tenure lines; Werner Finkbeiner's profile; the remaining iter-00 audit findings.

## Active channels (confirmed by the operator, 2026-10-19)

The spellings here are correct; where a skill differs, the skill has the typo.

| Channel | Niche | Typo in the skills |
|---|---|---|
| Roger The Pipe Guy | plumbing (45 years) | |
| Mark Silverbridge | plumbing (40 years) | |
| Vintage Pipefitter | plumbing (45 years) | |
| Werner Finkbeiner | plumbing ("the German way") | fixed in plumbing ideation (session 5); check the thumbnails skill |
| Dale Oakfield | woodworking for profit | |
| Hank Hardwood | woodworking for profit | |
| Norbert Daniels | home security: the retired Locksmith | |
| Lance Kavanaugh | home security: the Navy veteran | |
| Frederick Barnes | home security: the retired Fireman | |
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
