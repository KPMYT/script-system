# Session handover

The live note passed from one Claude Code chat to the next. A new chat reads `CLAUDE.md`, then this file, then `HANDOFF.md`, `README.md` and `PINNED.md`, and carries on from "Next actions". The outgoing chat rewrites this file before every handover.

**Last updated:** 2026-10-19, end of session 1.

---

## The handover rule

- When this chat reaches roughly 50% of its context, Claude tells the operator at the end of a message that it's time for a new chat.
- Before that, Claude: (1) rewrites this file, (2) logs it in `CHANGELOG.md`, (3) runs `python3 tests/run_checks.py`, (4) commits and pushes, (5) makes sure the work is on `main` (see "Branches"), and (6) gives the operator the opening message for the new chat.
- The operator is not technical. Explain Claude Code and git steps plainly and do them for them where possible.

## Branches

Every Claude Code chat works on its own `claude/...` branch. `main` is the shared branch every new chat starts from (`CLAUDE.md` rule 8).
- **Set up 2026-10-19:** `main` was created from session 1's final commit. The operator was walked through making it the GitHub default (Settings, General, Default branch). If this chat didn't start from `main`, that step wasn't done: walk the operator through it again.
- **At every handover,** merge this chat's branch into `main` and push `main`. Standing permission; no force-push, no branch deletion.
- **Old branches:** `claude/kind-cori-wxoupp` (the previous default) and `claude/loving-edison-b6z86r` (session 1) are fully contained in `main`. Leave them.
- This repo is separate from every other repo (for example the book-creation one). Nothing here touches them.

---

## Where things stand

**Done in session 1 (2026-10-18/19):**
- Restructured the repo: the woodworking study is in `studies/woodworking/`, the library is at the root, and the FacelessOS originals are in `archive/facelessos-original/`.
- Merged refs-01 from another chat: excerpts expanded to 15 groups, `reference-scripts.md` wired in, and the copy guard (`--refs`) now runs in the workflow and the audit.
- Wrote the first audit: `tests/iterations/iter-00/AUDIT.md`. **None of its fixes are applied yet.**
- Created `CHANGELOG.md` and `PROPOSALS.md` (P1 is open).
- Tests: 17/17 passing.

**The library is a baseline only: built, mechanically tested, never run end to end.**
- Built and niche-neutral by design:
  - the core rule files and the scanner
  - the fallback structures and the default research pack for niches without a pack
- Not yet true:
  - the audit fixes are unapplied (the core ones matter for every niche)
  - the core isn't packaged as an installable skill, so typing START in a VA's chat does nothing yet
  - there's no test fixture and no way to run START on TEST data
  - no persona profile exists, so every START ends at NOT READY
  - the installed `woodworking-scripts` skill on the operator's account hasn't been compared with this repo's copy

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

1. C7: leave the table, move it, or delete it?

## Next actions (in order)

**Rule for every chat: make no rule changes until the operator confirms each one.** Session 2 applied the audit fixes and changed core rules around a plumbing test built from Claude's own material, without checking with the operator. All of it was undone at the operator's request (see `CHANGELOG.md`, 2026-10-20). The iter-00 audit's findings are still unapplied, and each one is discussed with the operator before anything changes.

1. Check that this chat started from `main` (`git branch -a`, `git log -1 origin/main`).
2. **Agree with the operator how to test the core.** The goal is to test the core workflow (START, the input gate, the run to a finished script) for any niche, and the basic quality of its output. Test only: report findings, and change nothing without the operator's yes. Before testing, ask the operator:
   - which test material to use (a niche and the winning competitor scripts they choose, or a neutral made-up topic not tied to any of their niches)
   - what "basic quality" means to them
3. **Proposed rule from the operator, not yet written in:** scripts are value-driven by default, never under 8 minutes, longer is fine, and niche packs may add guidance. It changes the locked decision "length comes from the content, never word budgets", so confirm the exact wording first (for example, how 8 minutes converts to words for each channel, and what happens when a topic runs short).
4. Still open: C7 (the woodworking word-count table: keep, move or delete).
