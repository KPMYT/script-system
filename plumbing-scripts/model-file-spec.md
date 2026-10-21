# Model file spec (plumbing references)

How every file in `references/models/` was built (session 4, 2026-10-21). Kept for adding models later; not part of the skill.

Every model is ONE markdown file in plumbing-scripts/references/models/, named
`<ID>-<channel-slug>-<short-topic-slug>.md`, e.g. `R08-got2learn-solder-correct-way.md`, `S10-mark-silverbridge-s-traps.md`.
Channel slugs: got2learn, silver-cymbal, roger-wakefield, arrow-pest-service, roger-the-pipe-guy, mark-silverbridge, vintage-pipefitter, thecheapfix.

R files = real (human) channels: borrow structure AND voice. S files = AI-voiced hits (our own channels and TheCheapFix): STRUCTURE ONLY, never voice or wording.

## File layout (exactly these sections, in this order)

```
# <ID>. <Video title, exactly as in studies/plumbing/notes/INDEX.md, curly quotes straightened>

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

Bullets, each quoting the line with its [m:ss]: everything a faceless AI-voiced plumbing channel can't or mustn't use, per plumbing-scripts/SKILL.md ("Proof", "Banned in these scripts", "Safety", "The opening"): on-camera demos and pointing, first-person tests and history, customer stories, greetings and name intros, teases, recaps, the trade's motives, unsafe methods (boiling water down drains or into toilets or PVC, washing soda poured dry, mixing cleaners), tenure figures that differ from the fixed ones (Roger 45, Mark 40, Vintage 50 when the models were built; 45 since 2026-10-21), single exact product prices, long CTAs, the draft's banned stock lines, and any factual slip the study flagged or you notice (mark your own as "check against the brief").
```

## The ten video types (use these names)
single-product fix; N things about one product; never-do list; mistakes list; head-to-head verdict; banned / code explainer; how-to / correct way; product swap; hidden cause; seasonal or emergency. Use "other: <short description>" if none fits (e.g. long list of tips).

## Sources
- Transcripts: /home/user/script-system/studies/plumbing/data/{own,competitors}/<channel-folder>/<videoId>/transcript.txt, plus meta.md and comments.md.
- Views/normal and titles: /home/user/script-system/studies/plumbing/notes/INDEX.md. Notes: studies/plumbing/notes/{own,competitors}/<channel>__<id>.md.
- Analysis: /home/user/script-system/studies/plumbing/comparison/ (04 hooks, 07 body craft, 10 opener teardowns, 11 reasons to stay, 01 own channels, 02 competitors).
- The rules: plumbing-scripts/SKILL.md (read it first).
- Format examples already done: the retired reference-scripts.md and structure-models.md (in git history; their content is now in R01-R07 and S01-S06) (labelled scripts, why it works, doesn't transfer). Reuse their verified content where your model is one of theirs.

## Rules
- Write ONLY your assigned files in models/. Don't edit, commit or push anything else. Don't write helper scripts into the shared scratchpad root; use a subfolder named after your agent task (e.g. scratchpad/models-C/).
- Verify by script that the labelled script text (labels removed) matches the transcript word for word, and that every quote in "Doesn't transfer" and "Why it works" is verbatim with the right timestamp.
- Plain, clear English in your own text; no em dashes, no curly quotes, no ellipsis characters.
- When done, reply with: each file name, its video type, spoken words, item count, and anything you couldn't do or flagged.
