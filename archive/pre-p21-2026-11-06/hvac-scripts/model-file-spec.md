# Model file spec (HVAC references)

How every HVAC file in `references/models/` is built (2026-10-27), copied from the plumbing spec (`plumbing-scripts/model-file-spec.md`) and changed only where HVAC differs. Kept for adding models later; not part of the skill.

**Numbering:** the HVAC pack keeps 29 plumbing models under their plumbing IDs (R01, R04, R05, R06, R13, R15-R18, R20, R21, S01-S18; copied unchanged from the installed plumbing pack, 2026-10-27). New HVAC models continue the numbers from **R22**, so every ID is unique across both packs. **Only real people on camera** (operator, 2026-10-27: "we dont want any ai or faceless for reference"): no S files in the HVAC pack, and the plumbing pack's S files and Got2Learn (a faceless voice-over) are not copied. Kept plumbing models: R04, R05, R06, R13, R15, R16, R17, R18, R20, R21.

Every model is ONE markdown file in hvac-scripts/references/models/, named
`<ID>-<channel-slug>-<short-topic-slug>.md`, e.g. `R08-got2learn-solder-correct-way.md`, `S10-mark-silverbridge-s-traps.md`.
Channel slugs: the folder names in `studies/hvac/data/` (e.g. the-diy-hvac-guy, ray-duttons-garage, grayfurnaceman).

R files = real (human) channels: borrow structure AND voice. S files = faceless or AI-voiced videos (Ray Dutton's Garage, Vent Exposed, Lost Survival Knowledge, our own channels): STRUCTURE ONLY, never voice or wording.

## File layout (exactly these sections, in this order)

```
# <ID>. <Video title, exactly as in studies/hvac/notes/INDEX.md, curly quotes straightened>

- **Channel:** <name> · **Video:** <id> · https://www.youtube.com/watch?v=<id>
- **Tag:** [real] (structure and voice)   OR   [structure only] (AI-voiced: never borrow voice or wording)
- **Views / normal:** <N.NNx> (<views> / channel normal <normal>)
- **Length:** <m:ss> · <N> spoken words · **Video type:** <one of the ten types below, or "other: ...">

<For S files only, one bold line:> **STRUCTURE ONLY.** Read for how the video is built. Its voice and wording are AI-written and never borrowed; its banned lines are labelled.

## Beat map

| Time | Beat | What it does (no quoted wording) | Words |
|---|---|---|---|
| 0:00-0:12 | POINT | names the subject and the fix in the first sentence | 28 |
| ... | ... | ... | ... |

- **Items:** how many, how long each runs (shortest, longest, typical), in what order and why that order.
- **Promise devices:** which ones (numbered item + money stake, stake label, escalation ladder, the rule that protects everything, second use, check at home, running tally, trade price per item, problem you didn't know, myth flag, priority flag, question the next item answers), where each is promised and where it's paid.
- **Forward lines:** how many, the longest gap between a forward line or payoff.
- **Money:** the comparison (where it first lands), the device used.
- **CTA placement:** where, how long.
- **Ending:** what the last 30 seconds do.
- **What sets it apart from other models of its type:** 2-3 bullets (this is what a writer blends or varies).

## Why it works

One paragraph, citing the study (studies/plumbing/comparison/ reports, notes files, comments with like counts) where useful.

## Script (verbatim, labelled)

The full transcript, each paragraph starting with its [m:ss] timestamp, labels in square brackets at the start of the passage they cover.
Labels: [POINT] [QUESTION] [VILLAIN] [SCOPE] [PROMISE] [ITEM] (1), (2)... [MECHANISM] [CHECK] [MONEY] [SAFETY] [CALL A PRO] [FORWARD] [ASIDE] [CTA] [END] [COMMENT] [CLOSE]
Banned (label wherever they occur): [INTRO: banned] [TEASE: banned] [RECAP: banned] [POINTING: banned] [FIRST-PERSON DEMO: banned] (also covers first-person tests, history and customer stories) [MOTIVE: banned] [UNSAFE: banned] [PRODUCTION NOTE: banned]
Conventions: two labels on one line = the passage does both, in order; "(2, cont.)" = an item picked up again. Keep the transcript text verbatim (auto-caption mistakes kept); drop only noise tags like [Music], [laughter], [clears throat]; straighten curly quotes. Replace any email address or phone number read out with [contact removed]. A sponsor read over ~150 words may be shortened to "[CTA] (sponsor read, N words, omitted)".

## Doesn't transfer

Bullets, each quoting the line with its [m:ss]: everything a faceless AI-voiced plumbing channel can't or mustn't use, per hvac-scripts/SKILL.md ("Proof", "Banned in these scripts", "Safety", "The opening"): on-camera demos and pointing, first-person tests and history, customer stories, greetings and name intros, teases, recaps, the trade's motives, unsafe methods (working on a live panel or capacitor, no power check with a tester, refrigerant work, bypassing a limit or pressure switch, pressure-washing coils, hose pressure into a drain line, a car or generator near the house or in a garage, spray foam without a respirator, mixing cleaners), tenure figures that differ from Roger's 45, Ray Dutton's catchphrases ("keep your cool", "same companies", "none of this is hidden because", "25 years"), single exact product prices, long CTAs, the draft's banned stock lines, and any factual slip the study flagged or you notice (mark your own as "check against the brief").
```

## The video types (use these names)
single-product fix; N things about one product; never-do list; mistakes list (including the habits variant); head-to-head verdict (including ranked verdicts); banned / code explainer; how-to / correct way; product swap; hidden cause; seasonal or emergency; brand verdict. Use "other: <short description>" if none fits (e.g. long list of tips).

## Sources
- Transcripts: /home/user/script-system/studies/hvac/data/<channel-folder>/<videoId>/transcript.txt, plus meta.md and comments.md.
- Views/normal and titles: /home/user/script-system/studies/hvac/notes/INDEX.md. Notes: studies/hvac/notes/<channel>__<id>.md.
- Analysis: /home/user/script-system/studies/hvac/comparison/ (01 viewers, 02 openings and numbers, 03 body, safety and CTAs, 04 models and voice, README).
- **Long videos** (Technology Connections, 29 and 35 minutes): the script section holds only the stretch the model is for (named in `comparison/04-models-and-voice.md` §2), with a line saying which minutes and why; the beat map still covers the whole video in brief.
- The rules: plumbing-scripts/SKILL.md (read it first).
- Format examples already done: the retired reference-scripts.md and structure-models.md (in git history; their content is now in R01-R07 and S01-S06) (labelled scripts, why it works, doesn't transfer). Reuse their verified content where your model is one of theirs.

## Rules
- Write ONLY your assigned files in models/. Don't edit, commit or push anything else. Don't write helper scripts into the shared scratchpad root; use a subfolder named after your agent task (e.g. scratchpad/models-C/).
- Verify by script that the labelled script text (labels removed) matches the transcript word for word, and that every quote in "Doesn't transfer" and "Why it works" is verbatim with the right timestamp.
- Plain, clear English in your own text; no em dashes, no curly quotes, no ellipsis characters.
- When done, reply with: each file name, its video type, spoken words, item count, and anything you couldn't do or flagged.
