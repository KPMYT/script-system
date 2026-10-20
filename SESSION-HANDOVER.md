# Session handover

The live note passed from one Claude Code chat to the next. A new chat reads `CLAUDE.md`, then this file, then `HANDOFF.md`, `README.md` and `PINNED.md`, and carries on from "Next actions". The outgoing chat rewrites this file before every handover.

**Last updated:** 2026-10-20, end of session 3 (branch `claude/compassionate-pascal-ez3imz`, merged into `main`).

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

From session 2, still true:
- **Never change a rule, file or skill without the operator's explicit yes to that specific change.** Show the exact change first (a draft file is good), then apply.
- **Don't build tests or test material on your own initiative.** Testing happens on the operator's call.
- **Work niche by niche.** Plumbing is the current niche.
- **Notion and Google Drive are read-only** unless the operator says otherwise.
- **Keep messages plain,** with numbered items the operator can answer "1 yes, 2 no".

Learned in session 3:
- **The operator wants depth and examples.** The first comparison was "not as detailed as I'd hoped". They then asked for many verbatim examples, more hook structures and more on emotions. Give quoted evidence, counts and before/after rewrites, not summaries.
- **The operator reads on the web page.** Put long findings on the private artifact page and send the link. Send draft files with SendUserFile so they open in the app.
- **Verify what helpers report.** Spot-check their quotes and counts against the transcripts before passing findings on. Every report so far held up; two counts differed by method, and both figures were given.
- **Locked decisions:** when an instruction collides with one (HANDOFF section 3), say so plainly, write a proposal in `PROPOSALS.md`, and wait for the yes. P3 went this way and was approved.
- **Use helper agents in parallel** for collection and analysis, each writing only its own files. Commit their work as it lands; the stop hook insists on a clean tree.

## Branches

- Every chat works on its own `claude/...` branch; `main` is the shared starting point and the GitHub default.
- This chat's branch is `claude/compassionate-pascal-ez3imz`, merged into `main` at this handover.
- Earlier branches (`claude/kind-cori-wxoupp`, `claude/loving-edison-b6z86r`, `claude/wizardly-shannon-m0qqnw`) are contained in `main`. Leave them.
- **A second chat may be running in parallel:** the operator planned a separate chat to review the first Hank Hardwood script test. When both chats change shared files (`CHANGELOG.md` especially), merge carefully, keeping both sides.

---

## Where things stand

### Session 3 (2026-10-20), in short

**1. The plumbing study.** It lives in `studies/plumbing/`, collected with NexLev by one helper agent per channel and checked by the main session.
- **The 80 videos:**
  - Own channels: Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter.
  - Competitors: Silver Cymbal, Roger Wakefield, Got2Learn, Arrow Pest Service (pest control, a parallel niche) and TheCheapFix (the AI channel).
  - Per channel: the 5 most recent plus the 5 most-viewed from the last 24 months. Got2Learn's second group is its all-time top 5, because the channel stopped uploading.
- **Per video:** transcript, comments, a normal-based ratio, and a notes file.
- **Also there:** `notes/INDEX.md`, `transcripts-combined/` and `log.md`.

**2. The comparison** is in `studies/plumbing/comparison/`; its README is the summary and file list.
- **First pass:** `stats.md`, then `01` own channels, `02` competitors, `03` own vs competitors.
- **Deep pass:**
  - `04` hooks (19 structures)
  - `05` emotions (18)
  - `06` titles and promises (25 formulas)
  - `07` body craft
  - `08` suggestions with examples
  - `09` every difference across 24 variables
  - `10` the 43 winning openers torn down, with the opener playbook by video type
  - `11` reasons to stay (19 value-promise devices)
- **The private web page:** https://claude.ai/artifact/SGRPBBUCWdG8YUFWkuW6Fd (version 5). Its source is in `comparison/page/plumbing-script-study.html`; `md2page.py` turns the markdown reports into page sections. To update it, edit that file and publish it to the same URL (Artifact tool, `url` set).

**3. Scanner.** `core/script-scanner.py` gained new checks; tests 14-18 were added, and all 23 pass.
- **Fix-on-sight:**
  - production notes read aloud
  - the same sentence twice in a row
  - persona facts from the profile's scanner block (`name:`, `book:`, `tenure:`)
  - eleven more tease phrasings ("stay till the end", "stick with me", "wait until you hear" and others)
- **Judged:** a flag when a script talks about its own thumbnail or title.
- **Profiles:** Hank's and Dale's carry `tenure: none`.
- **Tested** against all 125 real transcripts: it catches every known slip, with no false name or production-note findings.
- **Skills rebuilt** in `dist/`.

**4. The plumbing script rules.** Draft 2 is `drafts/plumbing-scripts-skill-DRAFT.md`, outside the library. When approved, it becomes the one skill `plumbing-scripts`, like `woodworking-scripts`.
- **Approved by the operator:** the villain, the opening (hooks rotate, and an opening may be modelled on a reference winner's shape), "point then promise", and the ways to promise more value.
- **Waiting:** the ten video types (the operator asked to see the list; it was given in the final message of session 3).
- **Headings only, still to write:** inputs, viewer, voice, proof, money, safety block, banned list, scanner block, before-handing-over.

**5. Decisions.** All are in `HANDOFF.md` section 3, "Operator decisions, 2026-10-20 (plumbing, after the study)", and P3 is approved in `PROPOSALS.md`.

### Key plumbing decisions (full list in HANDOFF)

- **Tenures, fixed:** Roger the Pipe Guy 45, Mark Silverbridge 40, The Vintage Pipefitter 50.
- **CTAs:**
  - Roger and Mark go back to the short mid-video and outro CTAs their hits used.
  - Vintage has no CTA for now; an email CTA will be discussed later.
- **The villain is the trade** (prices and silence, never motives, never a named company).
- **Openers:** point first and fast, then two or three concrete, named promises paid inside the video (P3). Vague teases stay banned. Openers are modelled on the winners, by video type.
- **No name intros, no recaps.**
- **No first-person test or demo claims** unless the title or brief calls for one.
- **Safety:** unsafe advice is never allowed; contradictions between one video and another are acceptable.
- **Footage mismatch** is the editor's job.
- **Fine as they are:** "Nine times out of 10" is fine, and sources and store names aren't required.
- **Reference transcripts:** those of the real-life channels (Silver Cymbal, Roger Wakefield, Got2Learn, Arrow) go into the plumbing skill under the copy guard. TheCheapFix and the own channels are excluded.

### Not yet true

- **No plumbing persona profiles exist.** Roger's, Mark's and Vintage's personalities still need confirming with the operator ("not necessarily yet"); draft them from the Notion channel pages, read-only.
- **The plumbing pack** isn't in the library, isn't in `core/channels.md`, and has no tests.
- **The operator hasn't re-uploaded skills since the scanner changes.** `script-writer` and both persona skills changed. `script-writer` was never uploaded at all (it was missing from the account at the start of session 3); the operator held off because they weren't at the script stage yet.
- **The first Hank Hardwood script test** was ready at the end of session 3. Its review happens in a separate chat.
- **The woodworking ideation test** in Cowork was still running; no feedback yet.
- **Unanswered:** whether to add a rule that the script delivers the title's strongest word (comparison point 11, explained to the operator).

## Open questions for the operator

1. **The ten video types** in the draft: approve, change or add?
2. **Persona profiles for Roger, Mark and Vintage:** when to confirm them (personality, book, CTA wording)?
3. **The "title's strongest word" rule:** add it?
4. **The woodworking ideation test and the Hank script test:** what came out?
5. **Thumbnail looks:** the rule is "avatar + object + text, always" (operator, session 3). It isn't written into the woodworking ideation skill yet; that waits for the operator's yes after the ideation test.

## Next actions (in order)

1. Check this chat started from `main` (`git fetch origin`, `git log -1 origin/main`).
2. **Plumbing pack, batch 2,** in `drafts/plumbing-scripts-skill-DRAFT.md`, section by section for the operator's yes. Sources: comparison `07`, `08`, `09`, `11`, and the HANDOFF decisions.
   - Write: the viewer; voice; proof (no first-person tests; ranges); money framing (fix cost against the trade's price); the safety block and fact bank (hot tap water, never boiling, in drains, toilets and PVC; washing soda dissolved first; 3% peroxide; one product per drain; never after a chemical cleaner); writing for the footage; the banned list; inputs and freshness; before handing over.
   - Write the scanner block: "boiling" near drain, toilet, pipe or PVC; "pour it dry" and dry washing soda; first-person test or demo claims, liftable when the title or brief calls for one.
3. **Plumbing pack references:**
   - the research-pack and unit-plan templates
   - voice samples (real human narration from the winners)
   - excerpts
   - reference scripts
   - `archive/` with the real-life channels' compiled transcripts (from `studies/plumbing/transcripts-combined/` 4-7)
   - tests in `tests/run_checks.py` (the copy guard against the new references)
   - `tools/build_skills.py`, extended to build `plumbing-scripts`
4. **Persona profiles** for Roger (45), Mark (40) and Vintage (50, no CTA), each with a `scanner` block (`name:`, `tenure:`, `book:` where there is one), reviewed with the operator. Then add the rows to `core/channels.md`.
5. **Then, on the operator's call:** a first plumbing script test; the plumbing ideation fixes ("Finkbinder" to Finkbeiner and the other typos in the channel table, steering for the villain and tenures); Werner Finkbeiner; the remaining iter-00 audit findings.

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
- **On the account at the start of session 3:**
  - `woodworking-scripts`, `hank-hardwood-persona`, `dale-oakfield-persona`, `woodworking-ideation` and `ideation-core`
  - the untouched ideation skills, and `thumbnails`
  - **not** `script-writer`
- **How changes reach the account:** make them here, rebuild with `python3 tools/build_skills.py`, send the operator the `.skill` files (or the zips), and the operator re-uploads.
