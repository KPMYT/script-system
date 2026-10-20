# Session handover

The live note passed from one Claude Code chat to the next. A new chat reads `CLAUDE.md`, then this file, then `HANDOFF.md`, `README.md` and `PINNED.md`, and carries on from "Next actions". The outgoing chat rewrites this file before every handover.

**Last updated:** 2026-10-20, end of session 2.

---

## The handover rule

- When this chat reaches roughly 50% of its context, Claude tells the operator at the end of a message that it's time for a new chat.
- Before that, Claude: (1) rewrites this file, (2) logs it in `CHANGELOG.md`, (3) runs `python3 tests/run_checks.py`, (4) commits and pushes, (5) makes sure the work is on `main` (see "Branches"), and (6) gives the operator the opening message for the new chat.
- The operator is not technical. Explain Claude Code and git steps plainly and do them for them where possible.
- **Context:** Claude can't see its own context percentage. Don't guess a handover early; the operator says when (in session 2 Claude called it at 34%, which was wrong).

## How to work with the operator (learned the hard way in session 2)

- **Never change a rule, file or skill without the operator's explicit yes to that specific change.** Show the exact change first (a draft file is good), then apply. In session 2 Claude changed core rules around a self-built plumbing test without asking, and the operator had all of it undone. Don't repeat that.
- **Don't build tests or test material on your own initiative.** Testing happens later, on the operator's call, with material the operator chooses.
- **Work niche by niche.** Don't touch a niche (plumbing, etc.) before the operator gets to it.
- **Notion is read-only.** Never write anything in Notion unless the operator specifically says so. The same applies to Google Drive.
- **Keep messages plain and short,** with numbered items the operator can answer "1 yes, 2 no".

## Branches

Every Claude Code chat works on its own `claude/...` branch. `main` is the shared branch every new chat starts from, and it's the GitHub default.
- **At every handover,** merge this chat's branch into `main` and push `main`. Standing permission; no force-push, no branch deletion.
- **Old branches:** `claude/kind-cori-wxoupp`, `claude/loving-edison-b6z86r` (session 1) and `claude/wizardly-shannon-m0qqnw` (session 2) are all contained in `main`. Leave them.
- This repo is separate from every other repo (for example the book-creation one). Nothing here touches them.

---

## Where things stand

**Session 2 (2026-10-19/20), in short:**
1. Claude applied the iter-00 audit fixes and ran its own plumbing tests without asking. **The operator had all of it removed** (every library file restored to session 1's state, test records deleted; it survives only in git history before commit 4ab9468).
2. Then, step by step with the operator's approval:
   - **The books:** both ebooks' full text in `personas/books/`, with page markers. Hank's book prints page numbers (two lower than the PDF count), Dale's prints none. There's a chapter page map, and an index of Hank's 100 builds.
   - **The persona profiles:** `personas/hank-hardwood.md` and `personas/dale-oakfield.md`, from the Notion channel pages (Channel List, TEAM ACCESS), reviewed and changed with the operator. Both channels are marked ready in `core/channels.md`.
   - **Core additions:**
     - **the book match:** the plan step searches the persona's book, CTAs cite only the matched pages, and audit F4 checks them
     - **the family-detail exception:** one approved family detail (claims policy, P2)
     - **the rotation log** gains `details:` and `book:` fields
     - **the copy guard** now includes the persona profile, with `allow:` lines for fixed wording (scanner support plus check 13)
     - **the 8-minute minimum** (workflow, audit F2 and the evidence-block Length line, with the scanner printing the spoken word count)
     - **H13** exempts a persona's fixed last line
   - **The woodworking pack:** "right here" and "look at this" are banned even at screenshots, and the word-count table notes the 8-minute minimum (C7 settled: keep it).
   - **Ideation:** `ideation/woodworking-ideation/` was copied in and edited: Hank and Dale only, on camera, single builds; titles may exaggerate freely; the new for-profit pipeline in `references/pipeline.md`. `ideation/ideation-core/` holds an unchanged copy.
   - **Packaging:**
     - `tools/build_skills.py` builds one skill per layer into `dist/`: `script-writer` (core, START), `woodworking-scripts` (niche), `hank-hardwood-persona` and `dale-oakfield-persona` (profile plus book), `woodworking-ideation` and `ideation-core`.
     - It also builds `INSTALL.md`, a zip of the `.skill` files and a readable zip.
     - The build checks claude.ai's upload rules (one SKILL.md, frontmatter, name, description up to 1,024 characters).
3. **The operator uploaded the new skills** to their claude.ai account and kept both zips in Drive. They're starting a first ideation test in Cowork (woodworking ideation for Hank or Dale).
4. Tests: 18/18 passing.

**Not yet true:**
- **No script has been written end to end** with the new skills. The operator's first test (ideation, then research pack, then START) is the first real run.
- **The iter-00 audit's other findings are still unapplied,** and each one needs the operator's yes. Settled so far: A3 (applied), A5 (applied as the H13 exemption), C7 (keep). A8 (no end-CTA log field) and B1 (edit after PASS) are left as they are by choice.
- **Hank's QR code** (his CTAs point to it) hasn't been confirmed to exist.
- **Thumbnail character descriptions** for Hank and Dale (both on camera now) are pending from the operator (`ideation/woodworking-ideation/references/niche-packs.md`).

## Operator decisions so far

Full list in `HANDOFF.md` section 3 ("Operator decisions, 2026-10-20", two blocks). Key points:
- **Order of work:** finish woodworking for profit (Hank and Dale), then plumbing, then the other niches one at a time. Testing comes later.
- **Quality bar for any script:** it follows the core (unless the niche pack overrides, which always wins), is tailored to the audience's emotions, gives appropriate value, opens on a strong hook that plays on pain points and emotions, and is solution-driven.
- **Length:** at least 8 minutes, value-driven, longer is fine, never padded.
- **The enemy** for Hank and Dale is big business and the corporations (never a named company).
- **CTAs:**
  - **Hank:** two short CTAs to the QR code, with book pages when the book match finds them.
  - **Dale:** Bertha's Clean Home style: one ~35-word pitch (grandfather detail, "link below", fresh words each time), five one-line book mentions as narration, no end CTA, no subscribe ask, ending with a comments request ("I read every one") and then "Now go make some sawdust."
- **Ideation:**
  - **Where and what:** it runs in Cowork, Etsy-first, hand-checked. Each scan lists 30 products, then title and thumbnail-text options (format bank plus new creative ones), then the operator's picks, then fact-bank briefs (500-800 words, one cell, " | " between groups, never any structure or language direction), then an optional research pack.
  - **Claims:** titles may exaggerate freely.
  - **Inputs:** the operator also feeds in competitor videos for products and new formats.
- **Ignore descriptions and pinned comments for now.**
- **Channel setup skill** (YouTube, Drive, Notion from a niche pack and a profile) is still the long-term goal.

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

Synced read-only to `/root/.claude/skills/synced/<id>/` (the folder name can change). As of 2026-10-20 the account has:
- **The new script set:** `script-writer`, `woodworking-scripts`, `hank-hardwood-persona` and `dale-oakfield-persona`. The operator confirmed the persona skills in a screenshot; check that `script-writer` and `woodworking-scripts` were uploaded too.
- **Ideation:** `woodworking-ideation` (the new version) and `ideation-core` (unchanged).
- **Other ideation and tools, untouched:** `plumbing-`, `home-security-`, `style-`, `air-travel-`, `animals-`, `philosophy-` and `fabrics-ideation`, plus `thumbnails`.
- **Changes are made here,** then rebuilt with `python3 tools/build_skills.py`, sent to the operator (the `.skill` files plus the zips) and re-uploaded by the operator.

## Open questions for the operator

1. **The first ideation test:** how did it go? Fix whatever the operator reports, but only with their yes to each change.
2. **Hank's QR code:** does it exist (his CTAs point to it)?
3. **Thumbnail looks:** descriptions of the Hank and Dale avatars for the thumbnail packs.
4. **P1** in `PROPOSALS.md` is still open.

## Next actions (in order)

1. Check this chat started from `main` (`git fetch origin`, `git log -1 origin/main`).
2. **Ask the operator how the first ideation test went** (woodworking ideation in Cowork). Read any screenshots or output they share. Propose fixes as drafts; apply only what they approve; rebuild with `tools/build_skills.py` and send the changed `.skill` files.
3. **Support the first script run:** research pack (ideation step 5), then START in a new Cowork chat with `script-writer`. Check the output against the rules with the operator and fix with their yes.
4. **Then, on the operator's call:** the remaining iter-00 audit findings (one by one), plumbing (competitor study into `studies/plumbing/`, then its niche pack, profiles and ideation), and the channel setup skill.
