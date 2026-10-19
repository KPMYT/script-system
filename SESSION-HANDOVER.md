# Session handover

The live note passed from one Claude Code chat to the next. A new chat reads `CLAUDE.md`, then this file, then `HANDOFF.md`, `README.md` and `PINNED.md`, and carries on from "Next actions". The outgoing chat rewrites this file before every handover.

**Last updated:** 2026-10-19, end of session 1.

---

## The handover rule

- When this chat reaches roughly 50% of its context, Claude tells the operator at the end of a message that it's time for a new chat.
- Before that, Claude: (1) rewrites this file, (2) logs it in `CHANGELOG.md`, (3) runs `python3 tests/run_checks.py`, (4) commits and pushes, (5) makes sure the work is on `main` (see "Branches"), and (6) gives the operator the opening message for the new chat.
- The operator is not technical. Explain Claude Code and git steps plainly and do them for them where possible.

## Branches

Every Claude Code chat works on its own `claude/...` branch. Work only reaches the next chat if it's merged into the branch new chats start from (the GitHub default branch).
- **Now:** the default branch is `claude/kind-cori-wxoupp`, which does not have session 1's work. Session 1's work is on `claude/loving-edison-b6z86r`.
- **Plan (waiting on the operator's OK):** create `main` from session 1's branch, the operator sets `main` as the GitHub default branch, and every chat merges its work into `main` before handing over.
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

1. Set up `main` (walked through with the operator on 2026-10-19). Check that it's the GitHub default.
2. C7: leave the table, move it, or delete it?

## Next actions (in order)

1. Check that this chat started from `main`. Get the C7 answer.
2. **Baseline check of the core:**
   - Apply the audit's core-level fixes: C2, C1, B1, B2, A3-A8, A10, A14, A15 and the rest that touch `core/`.
   - Create `tests/fixtures/` (a TEST persona and a TEST research pack) and a way for START to load them (D2).
   - Run the first writer / operator / judge test (`CLAUDE.md`, "Testing with subagents") as `tests/iterations/iter-01/`.
3. **Finalize woodworking for profit:**
   - Apply the pack-level fixes from the audit.
   - The operator writes Hank's and Dale's persona profiles; Claude drafts from the template if asked.
   - A test run on a real research pack.
4. **Plumbing:** run a competitor study into `studies/plumbing/`, then build the niche pack.
