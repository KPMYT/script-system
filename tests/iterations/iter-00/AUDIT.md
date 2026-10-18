# iter-00 audit: the library before any fixes

**Date:** 2026-10-18 · **Scope:** every library file (`core/`, `woodworking-scripts/` including `references/`, `personas/`, `tests/`, `README.md`, `PINNED.md`), compared with each other, with `HANDOFF.md` section 3, and with `archive/facelessos-original/` (all 23 files). Nothing was fixed. Line numbers are for the files as of this commit.

**Test run:** `python3 tests/run_checks.py` gave **17/17 passed** after the restructure (study moved into `studies/woodworking/`, library at the root). The suite passes, but it misses several of the problems below; see A14.

**IDs** are kept as first issued, so a removed finding leaves a gap in the numbering.

**Severity:** **high** = gives a wrong or unsafe result, or blocks START. **medium** = a real conflict that a model could resolve either way. **low** = wording, housekeeping, or a borderline case.

**Count:** A, contradictions: 16 · B, lost from the originals: 7 · C, breaks a locked decision: 5 · D, stops START: 5.

---

## A. Contradictions between library files

**A1. The copy guard never runs** · high · **mostly fixed by refs-01 Task 4** (workflow 3.4 and audit D3 now pass `--refs`). Still open: the evidence block's Scanner line has no `copied` count.
- `core/workflow.md:73` and `core/greenlight-audit.md:54` (D3) run the scanner without `--refs`.
- But `core/script-scanner.py:19` and `woodworking-scripts/references/reference-scripts.md:5` say copied runs are flagged, and `core/greenlight-audit.md:73` (E2) requires zero lines copied from competitor transcripts or the excerpt library.
- As written, the copy guard is only ever exercised by the tests.
- **Fix:** add the niche pack's reference files as `--refs` in workflow 3.4 and audit D3 (for woodworking, `references/excerpts.md` and `references/reference-scripts.md`). Add `copied 0` to the evidence block's Scanner line (`core/greenlight-audit.md:132`).

**A2. `reference-scripts.md` is not linked from anywhere** · medium · **mostly fixed by refs-01 Tasks 3-4** (SKILL table and README map now list it and `most-viewed-24mo/`). Still open: workflow 3.1 doesn't load it.
- The file says it's read at the planning step (`reference-scripts.md:5`).
- Nothing points to it: it's missing from the SKILL file table (`woodworking-scripts/SKILL.md:21-29`) and from the README map (`README.md:24-33`), and the workflow's Plan step doesn't load it (`core/workflow.md:69`).
- The same goes for `woodworking-scripts/archive/most-viewed-24mo/`.
- **Fix:** add a row for each to the SKILL table and the README map. Add "the niche pack's reference scripts, if it has them, for structure and pacing" to workflow 3.1.

**A3. The pointing exception is fix-on-sight in the pack's own scanner block** · medium
- `woodworking-scripts/SKILL.md:181` allows "right here" and "look at this" at listings shown as real screenshots.
- But `SKILL.md:215-217` bans both phrases as fix-on-sight with no exception, and `core/workflow.md:96` and `core/greenlight-audit.md:89` (F7) have no exception either.
- **Fix:** drop the "except…" clause from `SKILL.md:181`. `SKILL.md:134` (name the platform and the price) already covers the screenshot cue.

**A4. Two different rules for the last line** · medium
- `core/retention-mechanics.md:19` says "The video ends on a practical next action", and `:163` says the last thing heard "should be a practical next action".
- `core/cta-and-endings.md:67`, `core/workflow.md:128-130` and `core/variety-rotation.md:104-106` allow a sign-off or a callback instead.
- **Fix:** in retention-mechanics, say the *final content beat* (before the end CTA) leaves the viewer something to do, and point to `cta-and-endings.md` for the closing line.

**A5. An upbeat sign-off fails H13 on sight** · medium
- `core/humanizer.md:151` applies H13 (upbeat closers, fix-on-sight, `:290`) to the script's final line "whatever the channel's ending format is".
- But the persona's sign-off is "the one fixed exception" (`core/variety-rotation.md:106`) and is required as the last line when the profile has one (`core/workflow.md:129`).
- **Fix:** add one line to H13: a sign-off listed in the persona profile is exempt.

**A6. Voice samples: one file asks a question that the gate forbids** · medium
- `core/voice-anchoring.md:29` says that with no niche pack and no persona samples, the run should "stop and ask for 2-3 transcripts".
- `core/workflow.md:38-40` says to ask only for required inputs, and the no-pack defaults (`:24`, `:30-34`) don't include voice samples.
- **Fix:** add `voice-samples` (2-3 verbatim transcripts with sources) to the default inputs in workflow section 2, required only when neither the niche pack nor the persona profile has samples.

**A7. Two forms of NOT READY** · low
- `core/workflow.md:23` prints `NOT READY: [channel]'s persona profile isn't set up yet.`
- `core/workflow.md:152-158` and `core/greenlight-audit.md:113-117` say every NOT READY output starts `NOT READY: DO NOT UPLOAD.`
- **Fix:** make `:23` use the standard block, with the persona reason on the next line.

**A8. The rotation log has no end-CTA field** · medium
- `core/variety-rotation.md:98` says to log the mid-CTA's opening and the end-CTA's wording.
- The format at `:117` has only a `mid-CTA:` field, so end-CTA wording can't be checked against the log (cross-script rule 4, `:129`).
- **Fix:** add `end-CTA: "[first 6-10 words]"` after the `mid-CTA` field.

**A9. The unit plan records less than the workflow and the skill ask for** · low
- `core/workflow.md:69` says the plan records the variation choices against the rotation log (nine slots).
- But the unit plan's VARIATION CHECK (`woodworking-scripts/references/unit-plan-template.md:55-58`) covers only the opening, the adversary and the swears.
- Its FLEXIBLE CHOICES (`:41-45`) also leave out two of the skill's flexible parts: the listing angle and which money-block element comes first (`SKILL.md:82-83`).
- **Fix:** add the hook turn, bridges, return, personality and closing moves to VARIATION CHECK, and the two missing choices to FLEXIBLE CHOICES.

**A10. Can a named company be the villain?** · medium
- `core/claims-policy.md:44` allows "casting a company or category as the villain… as tone".
- `core/offer-rules.md:47` always bans "negative claims about named companies". `core/research-and-sourcing.md:42` allows only "an industry or category", and `woodworking-scripts/SKILL.md:166` says "never named companies".
- **Fix:** change `claims-policy.md:44` to "an industry or category" (e.g. "the big stores").

**A11. A core example rounds a cost down; the pack says round up** · medium
- `core/humanizer.md:230` (H22) turns $3.10 into "costs about three bucks".
- `woodworking-scripts/SKILL.md:119` says round up. The pack wins here, but future niches will copy the core example.
- See B2 for the full fix.

**A12. An excerpt's rewrite note misses a banned opener** · low
- `woodworking-scripts/references/excerpts.md:33-34` marks "Today I'm going to show you how to build…" as ✎, but its note fixes only the guarantee.
- `woodworking-scripts/SKILL.md:68` bans "today we're going to".
- **Fix:** add "and drop the 'Today I'm going to show you' opener" to the ✎ note.

**A13. README and PINNED are out of date** · low · **partly fixed by refs-01** (test count is now 17; reference files listed). Still open: the map rows for `studies/`, `archive/facelessos-original/`, `HANDOFF.md`, `CLAUDE.md`, `CHANGELOG.md`, `PROPOSALS.md`.
- `README.md:41` and `PINNED.md:8` say 13 checks; there are 17.
- The README map has no rows for `references/reference-scripts.md`, `archive/most-viewed-24mo/`, `archive/facelessos-original/`, `studies/`, `tests/iterations/`, `HANDOFF.md`, `CLAUDE.md`, `CHANGELOG.md` or `PROPOSALS.md` (`CLAUDE.md` rule 7).
- **Fix:** update both.

**A14. The test suite doesn't look at personas/, README or PINNED** · medium
- `tests/run_checks.py:14` builds its file list from `core/` and `woodworking-scripts/` only. Broken references and stale text in `personas/`, `README.md` and `PINNED.md` aren't checked, which is how A13 got through.
- Check 8 (`:126-129`) tests a lift only on a single-phrase ban, so C2 wasn't caught.
- **Fix:** add `personas/*.md`, `README.md` and `PINNED.md` to checks 1-2. Add a check that every library file appears in the README map, and add check 8b for C2.

**A15. Stale path and leftover labels** · low
- `woodworking-scripts/archive/most-viewed-24mo/INDEX.md:3` refers to `data/competitors/`, which is now `studies/woodworking/data/competitors/`.
- `core/script-scanner.py:111-112` still matches `HOUSE FORMAT`, `TYPE CONFIRMED`, `VOICE CONFIRMED` and `BUILD SHEET`, labels from the retired house-rules prompt. They're harmless because the scanner stops at VERDICT first.
- **Fix:** update the path. Remove the four labels and add them to the STALE list in `run_checks.py:34-35`.

**A16. "With no face on screen"** · low
- `core/retention-mechanics.md:18` assumes a faceless channel, but Hank is an AI-avatar face channel (Talking Head).
- **Fix:** "Without a real person on camera, trust comes from competence…"

---

## B. Valuable material in the originals that was lost (and isn't covered by HANDOFF section 3)

Everything under a cut or rejected item was left out on purpose: title formulas, celebrity, true crime, hero's journey, retention coaching, both hook swipe files, Four Pillars, word-count tables, editor notation, jokes, long-range teases, the API/plan material. `house-rules-prompt.md` is fully carried over. Comment-gap research (`research-and-ideation-skill.md:131-132`) is already parked at `PINNED.md:24`.

**B1. An edit after PASS voids the PASS** · high
- Original: `greenlight-audit-skill.md:22`: "any revision after a PASS sends the script back through the full audit, because edits reintroduce tells."
- Library: `core/greenlight-audit.md:19` re-runs the audit only after fixes inside the run. A VA's "small tweak" after delivery keeps the old PASS and evidence block, and scripts are uploaded unread.
- **Fix:** add to `greenlight-audit.md:19` and `core/workflow.md:164`: "Any change after PASS, however small, voids it. The edited script runs the full audit again and gets a new evidence block."

**B2. Rounding never flatters a number** · high
- Original: `greenlight-audit-skill.md:139` (D5): "no dressing a real number up as something rounder and more dramatic."
- Library: nothing says which way to round outside woodworking. The core example rounds a cost down (`core/humanizer.md:230`, A11), and the scanner accepts a 10% drift from the pack (`core/script-scanner.py:224`, `max(0.1 * p, 0.5)`), so "$46" passes against a pack figure of "$42".
- **Fix:** add to audit D4 (`core/greenlight-audit.md:55`): "Round only toward the cautious side: costs, time and fees up; prices, earnings and savings exact or down." Change the H22 example to "about three bucks ten" or "a little over three bucks". Consider tightening the scanner tolerance for $ amounts.

**B3. Echo of a theme, not just a phrase** · medium
- Original: `humanizer-skill.md:226`: when every section loops back to the same observation, "give the repeated observation one home paragraph."
- Library: `core/humanizer.md:198` (H18) covers facts and phrases only. A theme like "anyone can do this" or "this sells" shares no four-word phrase, so the scanner's echo check never sees it.
- **Fix:** add the theme case and its one-home-paragraph fix to H18.

**B4. Layered explanations: one everyday comparison, and no contradictions** · low
- Original: `script-structures-skill.md:605-607` ("One core idea. One clear analogy.") and `:619` ("Each new detail builds on Layer 1. Never contradicts it.").
- Library: `core/script-structures.md:83-84` has only "the simple version anyone gets".
- **Fix:** Layer 1 gets one core idea and one everyday comparison. Layer 2 builds on it and never contradicts it.

**B5. The audit needs a strong model, but nothing sets one** · medium
- Original: `model-selection-guide-skill.md:204-205` and `00_QUICK_START.md:164`: use the most capable model for the audit, because the drafting model checks its own work.
- Library: `core/greenlight-audit.md:10` repeats the rule. But the run is one chat with no questions (`core/workflow.md:61-63`), so the audit runs on whatever model the VA opened. Nothing tells the VA to choose one.
- **Fix:** add a line before START (`core/workflow.md:19`) and in the VA instructions: open the chat on the most capable model the account offers.

**B6. One script per chat** · medium
- Original: `00_QUICK_START.md:382` ("Start a NEW chat for each script") and `:411` ("Reusing a brief across topics is how facts bleed between scripts").
- Library: VAs work in bulk (`HANDOFF.md:71`), and bulk mode (`core/workflow.md:57`) lets several STARTs run in one chat. Prices and cut lists from one pack can leak into the next script, and D4 misses a leaked number that happens to be in the new pack.
- **Fix:** add to bulk mode: "One script per chat. Start a new chat for every START."

**B7. Sentences outside the steps can name nothing showable** · medium
- Original: `faceless-scripts-os-master.md:677-685` (Vidrush): transitions with no visual keyword make the tool repeat footage. "Every sentence should contain at least one searchable keyword (person, place, object, or event)."
- Library: only *step* lines must name a visible object (`woodworking-scripts/SKILL.md:179`). Doubter, candor and money lines can run on with nothing to show. The study's most-liked complaints were about narration not matching footage (`HANDOFF.md:96`).
- This fits the locked visuals rule (`HANDOFF.md:36`). Don't bring back `visual-scripting-skill.md`'s editor notation (`:283-285`): that one was cut.
- **Fix:** add to `core/workflow.md:96`: outside steps, no more than about two sentences in a row without naming something showable (the piece, the tool, the listing, the price). Add the matching check to audit F7.

---

## C. Library content that breaks a locked decision

**C1. A long-range promise is allowed in the fallback structures** · high
- `core/script-structures.md:30`: "An honest escalation promise: 'the fixes get more useful as we go.'" It's relied on at `:62` and in audit B8 (`core/greenlight-audit.md:39`).
- Breaks: `HANDOFF.md:27` (no retention teases) and `:53` (long-range promises are banned).
- **Fix:** remove the option and its ordering exception. Keep the countdown exception (`script-structures.md:62`, `core/retention-mechanics.md:121`) and the "hook's escalation promise" clause in B8.

**C2. Lifting one AI-vocabulary word lifts all four** · high
- `core/script-scanner.py:41` puts delve, tapestry, unleash and robust in one ban, and `:276` lifts it if the lift text matches any part. Tested: `lift: robust` turns off all four, and `lift: AI vocabulary` would too.
- Breaks: `HANDOFF.md:51` and `core/humanizer.md:280`: a ban is lifted only by naming that one ban.
- **Fix:** split `:41` into four entries. Add test 8b: lifting one word leaves the other three enforced.

**C4. A two-build reference script under "single builds only"** · low
- `woodworking-scripts/references/reference-scripts.md:20`, `:678`: entry 4 is two builds in one video.
- Breaks: `HANDOFF.md:38` (single builds only for now), but only as a model a planner might copy.
- **Fix:** add one line to entry 4: "Two builds: structure reference only, we script single builds." Or swap in the 9.2x single build left out at `:11`.

**C5. Laughing voice tags with no jokes** · low
- `core/workflow.md:178` allows `[slightly amused]` and `[chuckles]`.
- Breaks: `HANDOFF.md:33` (jokes no). A chuckle tag on a line that isn't funny reads as forced humor.
- **Fix:** drop `[chuckles]`, or limit both tags to honest-candor lines.

**C6. Retention mechanics invites retention-graph diagnosis** · low
- `core/retention-mechanics.md:3`: "…and when a retention graph shows viewers leaving."
- Breaks: retention coaching is rejected (`HANDOFF.md:82`; `PINNED.md:54`: graphs are analyzed with Claude when needed).
- **Fix:** drop that clause from the description.

**C7. The word-count table in the woodworking skill** · low (recommendation: leave it as it is)
- What it is: `woodworking-scripts/SKILL.md:99-109`, under "Length comes from the content", is a table of how many words each kind of line ran in the winning scripts (a material line 8-24 words, a step line 8-31, a money line 5-28, and so on), plus whole scripts at 1,135-2,408 words. It's measured from BeardedViking and WhosTheVoss.
- Why it's flagged: two locked decisions brush against it. FacelessOS's word-count tables were cut (`HANDOFF.md:46`), and length must come from the content, never word budgets (`HANDOFF.md:28`). A model that sees "1,135-2,408 words" could treat it as a target and pad or squeeze.
- Why it's probably fine: it's our own study data, not the FacelessOS tables. It's labelled "these show the usual spread, they are not targets" right above it, and `HANDOFF.md` section 4 keeps the same figures.
- **Options:** (a) leave it (recommended); (b) move it to `references/calibration.md` so the writer doesn't see numbers while writing; (c) delete it. None of them changes a rule.

Also logged in `PROPOSALS.md` (P1): the reason given for a locked decision is not quite right ("the winners never introduce themselves", `HANDOFF.md:25`). BeardedViking's top video opens with a credibility line (`voice-samples.md:13`). The rule itself isn't in question.

---

## D. What would stop the START workflow from running

**D1. No channel can be scripted** · high (known, `PINNED.md:14`)
- Both channels are `pending` (`core/channels.md:12-13`) and `personas/` holds no profiles (`personas/README.md:5`).
- `core/workflow.md:23` stops every START at NOT READY. Talking Head markers also need the offer's printed title from the profile (`:117`).
- **Fix:** write `hank-hardwood.md` and `dale-oakfield.md`, then mark them ready.

**D2. There's no way to run START on test data** · high
- `CLAUDE.md` says test data lives in `tests/fixtures/` and never in `core/channels.md` or `personas/`. But the workflow finds channels only in `channels.md` (`core/workflow.md:21-23`), so a TEST persona can't reach the gate.
- `tests/fixtures/` doesn't exist yet.
- **Fix:** create `tests/fixtures/` (a TEST persona and a TEST research pack). Add one rule to workflow section 1: `START TEST [fixture]` loads the profile from `tests/fixtures/` and labels every output TEST.

**D3. Typing START triggers nothing unless the library is installed** · high (open, `PINNED.md:50-51`)
- `core/workflow.md:8` assumes START loads this file. Only `woodworking-scripts/` is packaged as a skill (`SKILL.md` frontmatter), and the core files have no skill wrapper.
- The installed `woodworking-scripts` skill may also differ from this repo's copy.
- **Fix:** decide the packaging (for example, one skill whose description triggers on START, with `core/` as its reference files, version-stamped), then install that on the VA accounts.

**D4. Every research pack is built by hand** · medium (known, `PINNED.md:21`)
- The gate needs a verified pack (`core/workflow.md:45-49`), and the research stage doesn't exist (`:79`). Until it does, each START depends on a hand-made pack that follows `woodworking-scripts/references/research-pack-template.md`.
- **Fix:** build the research stage, or write a short VA how-to for filling the template, including the verification pass.

**D5. A dead pointer outside the repo** · low
- `woodworking-scripts/SKILL.md:53` points to `woodworking-ideation/references/audience.md` and `word-bank.md`, which live in the ideation skill, not here. `run_checks.py:19` whitelists them. It won't stop a run, but where the ideation skill isn't installed the pointer goes nowhere.
- **Fix:** keep the two lines the script needs (the viewer, the vocabulary) in `SKILL.md` and mark the pointer optional, or copy the sections in.

**Nothing in START depends on the originals.** Every file and label `core/workflow.md` uses exists in the library (SCRIPT TYPE, VERDICT, FORMAT CHECK, ROTATION LOG ENTRY, AUDIT EVIDENCE, VO COPY). The only leftovers are the harmless scanner labels in A15.
