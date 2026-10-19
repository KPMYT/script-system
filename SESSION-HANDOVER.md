# Session handover

The live note passed from one Claude Code chat to the next. A new chat reads `CLAUDE.md`, then this file, then `HANDOFF.md`, `README.md` and `PINNED.md`, and carries on from "Next actions". The outgoing chat rewrites this file before every handover.

**Last updated:** 2026-10-19, end of session 2.

---

## The handover rule

- When this chat reaches roughly 50% of its context, Claude tells the operator at the end of a message that it's time for a new chat.
- Before that, Claude: (1) rewrites this file, (2) logs it in `CHANGELOG.md`, (3) runs `python3 tests/run_checks.py`, (4) commits and pushes, (5) makes sure the work is on `main` (see "Branches"), and (6) gives the operator the opening message for the new chat.
- The operator is not technical. Explain Claude Code and git steps plainly and do them for them where possible.

## Branches

Every Claude Code chat works on its own `claude/...` branch. `main` is the shared branch every new chat starts from, and GitHub's default (`CLAUDE.md` rule 8).
- **Session 2 checked it:** this chat started from `main` at session 1's last commit, and `main` is the GitHub default. Nothing more to set up.
- **At every handover,** merge this chat's branch into `main` and push `main`. Standing permission; no force-push, no branch deletion.
- **Old branches:** `claude/kind-cori-wxoupp`, `claude/loving-edison-b6z86r` (session 1) and `claude/wizardly-shannon-m0qqnw` (session 2) are all contained in `main`. Leave them.
- This repo is separate from every other repo (for example the book-creation one). Nothing here touches them.

---

## Where things stand

**Done in session 2 (2026-10-19):**
- **iter-01:** applied the iter-00 audit's core-level fixes (A1, A2, A4-A8, A10, A11, A13-A16, B1-B7, C1, C2, C5, C6). Added **START TEST** and `tests/fixtures/` (plumbing-01: a TEST channel with no niche pack, so the core fallbacks get exercised; TEST persona, brief, rotation log, three real voice samples, a web-verified research pack, and a judge-only source script). Ran the first writer / operator / judge test.
- **iter-02:** fixed the 17 library problems the iter-01 judge found (scanner hang and number matching, safety bound at its step, E3 reference via the brief, a new Diagnose-and-fix fallback structure, persona voice check D1b, complete fix steps in the research pack, a fuller evidence block). Ran the test again in bulk mode with a fresh writer and judge.
- Tests: 23/23 passing.

**Test results so far (same title both times: "Why Your Toilet Keeps Running, and How to Fix it"):**

| | iter-01 | iter-02 |
|---|---|---|
| Gate (asking, refusing "just write it", bulk mode, one script per chat) | 5/5 correct | correct |
| Format, markers, VO copy | pass | pass |
| Judge's verdict | FIX-THEN-PASS, **not** safe unread (false claim about a company, safety line deleted, steps borrowed from a voice sample) | FIX-THEN-PASS, **safe to upload unread** (nothing false, unsafe or off-policy) |
| Length (source: 969 words, about 6 min) | 1,402 words, about 9:20 | 1,941 words, about 13 min |
| Still wrong | | persona's short sentences missed; fill-valve swap before the flapper's free checks; evidence block overclaims |

**The core baseline:** the core now works end to end on a channel with no niche pack: the gate, the run, the scanner, the audit, the format and the VO copy all function, and the second script was accurate and safe. It isn't finished: the writer's own audit still over-reports, and the iter-03 fixes below remain.

**Still not true:**
- the core isn't packaged as an installable skill, so typing START in a VA's chat does nothing yet (audit D3)
- no real persona profile exists (Hank, Dale), so every real START ends at NOT READY
- the installed `woodworking-scripts` skill on the operator's account hasn't been compared with this repo's copy
- the woodworking pack-level audit fixes (A3, A9's template, A12, C4, C7, D5) aren't applied

## Operator decisions so far

- Audit C3 (Dale's CTA) and B8 (descriptions and pinned comments) are removed. **Ignore descriptions and pinned comments for now.**
- C7 (the word-count table in `woodworking-scripts/SKILL.md`): Claude recommends leaving it. Waiting on the operator.
- **Order of work:**
  1. Confirm the core works as a baseline for any niche.
  2. Finalize woodworking for profit (Hank and Dale).
  3. Plumbing.
  4. The other niches, one at a time.
- **Persona profiles:** probably written by the operator. The VA then does the channel setup (YouTube, Drive, Notion).
- **Channel setup skill:** the goal. It builds a channel from a niche pack and a persona profile, and the VA runs it. The platform choice (Claude Code, Claude or Cowork) is still to be advised.
- **Ideation:** the skills live on the operator's claude.ai account, outside this repo. They may later be brought in here, audited and connected to the scripts (especially the brief). Where ideas get generated long term is still open.
- **Research stage:** whether it belongs with ideation or with the script is still open, to be decided by testing.

## Active channels (confirmed by the operator, 2026-10-19)

The spellings here are correct. Where the skills spell a name differently, the skills have a typo; fix those when the ideation skills are audited.

| Channel | Niche | Typo in the skills |
|---|---|---|
| Roger The Pipe Guy | plumbing | |
| Mark Silverbridge | plumbing | |
| Vintage Pipefitter | plumbing | |
| Werner Finkbeiner | plumbing ("the German way") | "Finkbinder" |
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

Every Claude Code chat gets the operator's claude.ai skills, synced read-only to `/root/.claude/skills/synced/<id>/` (the folder name can change).
- **Ideation:** `ideation-core` (the master format bank and registry), plus `plumbing-`, `woodworking-`, `home-security-`, `style-`, `air-travel-`, `animals-`, `philosophy-` and `fabrics-ideation`.
- **Also:** `thumbnails` and `woodworking-scripts`.
- **The installed `woodworking-scripts` is old:** a single 202-line `SKILL.md`, with no references, no core, and a different text from this repo's. This repo is the newer master. The core itself isn't installed on the account at all.

## Open questions for the operator

1. **C7** (the word-count table in `woodworking-scripts/SKILL.md`): leave it (Claude's recommendation), move it to a calibration file, or delete it? Still unanswered.
2. **How deep "how to fix it" goes.** Teaching every part swap in full made the test script about 13 minutes against the competitor's 6 (which sends viewers to "a separate video"). Options: (a) full steps every time (current rule); (b) the diagnosis and free fixes in full, part swaps as a short summary; (c) decided per title in the brief. Claude recommends (c), with (a) as the default.
3. **Competitor titles word for word.** The TEST title was the competitor's exact title. Is copying a winning title verbatim allowed, or must ideation always change it? (An ideation rule; it affects the not-a-clone check.)
4. **P1** in `PROPOSALS.md` is still open.

## Next actions (in order)

1. Check this chat started from `main` (`git fetch origin`, `git log -1 origin/main`). Ask the operator the open questions above.
2. **iter-03: finish the core baseline.** Apply the judge's ranked list in `tests/iterations/iter-02/CHANGES.md` ("Library fixes the judge ranks next"):
   - number check: match numbers with their units, don't count quoted comments as a source, extend check 9c with "$200 for a visit", "20 years" and "9,000 gallons"
   - D1b that can fail: the scanner reports sentence-length figures, personas get a numeric target, the evidence line reports the numbers
   - structure 3b: branch order after the sorting test (free checks before parts; most common cause first); rotate the hook's move instead of prescribing the reference video's opening
   - safety repeats: exempt repeated safety instructions from the echo count, instead of "reword"
   - research verification: step 1 vs the water-on check, figures that must reconcile, variants need steps or a scope line
   - low items: an opening voice sample in the fixture (so A2 runs), round-by-round notes and the brief's reference fields in the evidence block, E4 defined for scripts, part-number pronunciation
   - then run plumbing-01 again with a fresh writer and judge (`tests/iterations/iter-01/PROTOCOL.md`). Aim: the judge agrees with the writer's PASS.
   - consider a second fixture set in another niche (not plumbing) to confirm the core isn't tuned to one topic.
3. **Finalize woodworking for profit:**
   - apply the pack-level fixes from the iter-00 audit (A3, A9's template, A12, C4, C7, D5)
   - the operator writes Hank's and Dale's persona profiles; Claude drafts from the template if asked (check 14 verifies every field)
   - a TEST run through the woodworking pack, then a real research pack
4. **Packaging (audit D3):** decide how the core and packs become an installable skill that triggers on START, then install on the VA accounts.
5. **Plumbing:** a competitor study into `studies/plumbing/`, then the niche pack. The plumbing-01 fixture's voice samples and research pack are a head start, but they're TEST data and never go into the pack as-is.
