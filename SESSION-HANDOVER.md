# Session handover

The live note passed from one Claude Code chat to the next. A new chat reads `CLAUDE.md`, then this file, then `HANDOFF.md`, `README.md` and `PINNED.md`, and carries on from "Next actions". The outgoing chat rewrites this file before every handover.

**Last updated:** 2026-10-21, end of session 4 (branch `claude/magical-bell-pkebg2`, merged into `main`).

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

From sessions 2 and 3, still true:
- **Never change a rule, file or skill without the operator's explicit yes to that specific change.** Show the exact change first (a draft file is good), then apply.
- **Don't build tests or test material on your own initiative.** Testing happens on the operator's call.
- **Work niche by niche.** Plumbing is the current niche.
- **Notion and Google Drive are read-only** unless the operator says otherwise.
- **Keep messages plain,** with numbered items the operator can answer "1 yes, 2 no".
- **The operator wants depth and examples:** quoted evidence, counts, before/after lines.
- **Verify what helpers report** against the sources before passing it on.
- **Locked decisions:** when an instruction collides with one, say so plainly, write a proposal in `PROPOSALS.md`, and wait for the yes (P3, P4 and P5 went this way).

Learned in session 4:
- **Answers are short; read them carefully.** "2 yes" can mean yes to a question and its premise; when an answer is genuinely ambiguous (session 4: "title numbers win", "not personally tested"), state the reading and ask once. The operator once sent a message with a template blank unfilled ("[your answer: approved, or what to change]"): say so rather than assume approval.
- **The brief is king.** The operator wants scripts based on the brief: no research pack for plumbing, safety follows the brief, a missing fact stops the run rather than being invented.
- **Lenient where it can be, strict on copying.** Safety was loosened ("a BIT lenient"; boiling-water checks dropped), but the operator pushed hard for scripts never to copy the models (38 models, five no-copy rules).
- **Use waiting time.** When helpers run, offer the next independent step ("is there something we can do in the meantime?").
- **Helpers in parallel worked well** (up to six at once, each writing only its own files, every quote then checked by script). The stop hook demands a clean tree, so commit helpers' work in progress as it lands.

## Branches

- Every chat works on its own `claude/...` branch; `main` is the shared starting point and the GitHub default.
- This chat's branch is `claude/magical-bell-pkebg2`, merged into `main` at this handover.
- Earlier branches are contained in `main`. Leave them.
- `claude/pensive-gates-4c5yrt` exists on GitHub and isn't in `main`; it's probably the parallel chat that reviewed the first Hank Hardwood script test. Don't merge it without the operator; when it comes into `main`, merge carefully (keep both sides of `CHANGELOG.md`).

---

## Where things stand

### Session 4 (2026-10-21), in short

The plan to deployment, confirmed by the operator: **1** finish the plumbing rules → **2** reference files → **3** persona profiles → **4** into the library → **5** test → **6** deploy. **Steps 1-3 are done.**

**Step 1. The plumbing rules** (`drafts/plumbing-scripts-skill-DRAFT.md`): every section approved. New this session:
- **Inputs:** the title and the brief only (no research pack); the rotation log stays.
- **The viewer, voice** (no swearing; a persona device only if the profile has one), **proof** (tests and results from the brief, never "I tested"), **money framing** (ranges, the comparison within two minutes, rotate the money devices), **safety** (the brief always wins; five safe defaults only where the brief is silent).
- **The ten video types** approved as the common ones, not the only ones, with a rule for titles that fit none.
- **Using the models: never a copy** (five rules; see step 2).
- **CTAs:** Roger and Mark, a short mid-video ask after the first payoff and a one-line end reminder; Vintage, a one-line subscribe ask at the end only.
- **The ending (P5):** the one-line end CTA, then a specific comment question with "I read every one" as the video's last line; no sign-off.
- **Length:** at least 12 minutes; 12-20 the sweet spot; value decides.
- **Banned list, scanner block** (first-person tests, pointing at the screen, template stock lines, mocked hype; 15 phrases once per script), **before-handing-over checklist.**
- No edit notes in scripts, and no "writing for the footage" section.

**Step 2. The reference files** (`drafts/plumbing-scripts-refs/`):
- `references/unit-plan-template.md` (with a MODELS block), `voice-samples.md` (three real-channel stretches), `excerpts.md` (204 lines in 16 groups, tagged [real] or [structure only]).
- `references/models/`: **38 model files**, each a beat map plus the full labelled script, why it works and what doesn't transfer. R01-R20 are the real channels (structure and voice); S01-S18 are our hits and TheCheapFix (structure only). `INDEX.md` sorts them by video type. Four types have only one or two models (never-do, banned explainer, product swap, hidden cause); the operator declined a NexLev top-up.
- `archive/`: the four real channels' transcripts.
- Every quote and script was checked word for word (`tools/verify_plumbing_models.py`). `model-file-spec.md` is how the model files were built.

**Step 3. Persona profiles** (`personas/roger-the-pipe-guy.md`, `mark-silverbridge.md`, `vintage-pipefitter.md`): approved, status pending until step 4. Kept close to the Notion pages. Books converted from Drive into `personas/books/` (Roger 124 pages, 100 fixes; Mark 122 pages, 50 fixes).

**Core changes this session (all in `dist/`, rebuilt):**
- **Claims policy:** fixed years in the trade allowed (the profile's `tenure:` figure, or the title's number: "title numbers win", every channel); "personally tested" stays banned (P4).
- **Scanner:** `--title` (a years figure in the locked title passes); `once:` / `once-regex:` lines (a phrase allowed once per script). Tests 19 and 20 (25 checks).
- **Workflow and audit:** the research pack is niche-dependent; a niche pack may mark it `not used`, and the brief becomes the fact source.

### Key decisions (full list in `HANDOFF.md` section 3, the 2026-10-20 and 2026-10-21 plumbing blocks)

- Tenures fixed: Roger 45, Mark 40, Vintage 50; a title's number wins. Mark's book says 35: "change nothing" (scripts never cite the book's figure).
- No "I tested" anywhere; tests and results from the brief, said without "I".
- The brief wins on safety; no scanner checks for boiling water or dry washing soda.
- References: the real channels for voice; our hits and TheCheapFix for structure only.
- Every Roger and Mark CTA names the description link and the QR code. Roger's one personal detail: the first-Saturday drain check with his coffee. Mark: no contractions. Vintage: no personal name, no Uncle Ray.

### Not yet true

- **The plumbing pack isn't in the library:** the draft and its references sit in `drafts/`; the three channels aren't in `core/channels.md`; there are no plumbing tests; `build_skills.py` doesn't build `plumbing-scripts` or the three persona skills.
- **The rotation log's `model:` field** is written into the plumbing draft as an override; `core/variety-rotation.md` itself is unchanged.
- **The operator hasn't re-uploaded skills.** `script-writer` changed again this session (claims policy, workflow, audit, scanner) and was never uploaded; the persona skills changed in session 3.
- **No plumbing script has been written or tested yet.**

## Open questions for the operator

1. **From session 3, still unanswered:** the "title's strongest word" rule; the outcomes of the woodworking ideation test and the Hank script test; writing "avatar + object + text, always" into the woodworking ideation skill.
2. **When to run the first plumbing test** (step 5), and on which channel and title.

## Next actions (in order)

1. Check this chat started from `main` (`git fetch origin`, `git log -1 origin/main`).
2. **Step 4: into the library** (show the operator the plan in one message first, then do it):
   - `drafts/plumbing-scripts-skill-DRAFT.md` becomes `plumbing-scripts/SKILL.md` (strip the status tags and the draft comment; keep the content); `drafts/plumbing-scripts-refs/references/` and `archive/` move under `plumbing-scripts/` (leave `model-file-spec.md` out of the skill).
   - Make the explicit override statements the core needs: the `inputs` block with `research-pack | not used`, retention-mechanics §6 (P3), cta-and-endings §4 (P5), the 12-minute minimum, the rotation log's `model:` field (variety-rotation), the plumbing voice's contractions with Mark's exception in his profile.
   - Add Roger, Mark and Vintage to `core/channels.md`; set their profiles to `ready`.
   - Tests in `tests/run_checks.py`: the plumbing inputs block parses; the scanner block's bans and once-limits fire (and pass a clean plumbing paragraph); Mark's contraction ban; the copy guard runs against `excerpts.md` and every model file; the three profiles' scanner blocks give name, book and tenure; file references resolve.
   - Extend `tools/build_skills.py` to build `plumbing-scripts.skill` and `roger-the-pipe-guy-persona`, `mark-silverbridge-persona`, `vintage-pipefitter-persona`; check the size against claude.ai's limits (the models folder is large: if it's too big for one skill, ask the operator).
   - README file map, CHANGELOG, checks.
3. **Step 5: the first plumbing test,** on the operator's call, with the writer / operator / judge roles from `CLAUDE.md`.
4. **Step 6: deploy:** rebuild, send the operator the `.skill` files (`script-writer`, `plumbing-scripts`, three persona skills) and explain the upload.
5. **Then, on the operator's call:** the plumbing ideation fixes ("Finkbinder" to Finkbeiner and the other typos in the channel table, steering for the villain and tenures); Werner Finkbeiner; the remaining iter-00 audit findings.

## Active channels (confirmed by the operator, 2026-10-19)

The spellings here are correct; where a skill differs, the skill has the typo.

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

- **Where they sync:** read-only, to `/root/.claude/skills/synced/<id>/`.
- **On the account at the start of session 3 (unchanged since, as far as this chat knows):**
  - `woodworking-scripts`, `hank-hardwood-persona`, `dale-oakfield-persona`, `woodworking-ideation` and `ideation-core`
  - the untouched ideation skills, and `thumbnails`
  - **not** `script-writer`
- **How changes reach the account:** make them here, rebuild with `python3 tools/build_skills.py`, send the operator the `.skill` files (or the zips), and the operator re-uploads.
