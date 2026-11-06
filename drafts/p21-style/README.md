# DRAFT: P21, the style rebuild (Scarlett Starling, Diane de Chambray)

Not part of the library yet. Built 2026-11-06 (session 16) from `drafts/lite-scarlett-starling-DRAFT.md` and `drafts/lite-diane-de-chambray-DRAFT.md` (the iter-08 and iter-10 winners), for the operator to see before anything replaces the library or goes to the account.

The folders are laid out exactly as the three skills would be uploaded.

| File | What it is | Replaces |
|---|---|---|
| `style-scripts/SKILL.md` | The steps: inputs, the video type and its model, write, read aloud, check, the output | the account's `style-scripts` (8,261 words, plus `hooks.md` 19,126 and 37 model beat maps) and, for these two channels only, `core/workflow.md` sections 2 to 6 and every other core file |
| `style-scripts/check.py` | The hard-rules check (about 300 lines; no counts to meet) | the core scanner and the full audit, for these two channels |
| `style-scripts/references/models/` | 11 real women's transcripts (M01, M04, M07, M09, M13, M18, M19, M21, M24, M28, M30), one per file, with what to take, what not to take and her signature phrases. M23 was dropped (framed on weight loss) | the model beat maps, `hooks.md`, the excerpts and the voice samples |
| `scarlett-starling-persona/SKILL.md` | Scarlett's one page | the account's profile (2,106 words) |
| `diane-de-chambray-persona/SKILL.md` | Diane's one page | the account's profile (2,474 words) |
| `*/personas/books/*-book.md` | The two book indexes, unchanged | the same files |
| `model-picks.md` | Which model goes with which video type, and why (helper's research, re-checked) | the model INDEX |

**What does not change:** `script-writer` (START, the channel question, the channel list) and every other channel's skills. Electrical, plumbing, HVAC and woodworking are untouched by this draft.

## What changed from the tested one-page drafts (iter-10's fixes)

| iter-10 finding | Fix on the page |
|---|---|
| Openings ran 145 to 161 words against the models' 73 to 82: "no more than about 170" read as a target | "Keep it as short as the model's opening" |
| "When I was designing" exactly twice, "my dear friends" exactly three times: limits read as quotas | "once, if it truly explains a point; many scripts won't need it"; the endearment "wherever it comes naturally; there is no number to reach" |
| The end book line over-claimed ("Everything we've talked about... goes deeper in The French Way") | "claiming only what the book match confirms (never 'everything...')"; the check fails it |
| Models' signature lines leaked ("I bet that's happened at your house, too"; "I hear it all the time") | each model file lists her signature phrases; the page says never use them; the check fails them |
| "Instantly" never said in the hair colors script | "say the title's promise plainly at least once, with its sharpest word, where it's true" (the check only reports it) |
| An invented client quote ("Women say to me...") | "No client stories and no 'women tell me'"; the check fails it |
| "Your check is" four times, items ending alike | "never announce a check"; the check fails it |
| The safety line dropped in the wrong place | "one short line inside the item it belongs to" |
| A second count in the opening ("and three that do the opposite") | "one count only" on both pages |

## The hook, the feelings and the flow (operator, 2026-11-06: "simplifing to the point the hook is as strong as we always wanted targetting the right emotions, and the video actually flows")

Both pages now carry, as plain guidance with no counts, what the operator decided on 2026-10-31 and what the study found:
- **The hook:** the title paid off in the first sentence; the blame taken off her (what she can't change isn't the problem); within reach; straight into item one with a reason to stay. As short as the model's opening. The old five-move formula, its 110-word cap and its title-word counts are gone.
- **The feeling:** one table per page of what each kind of title makes her want and fear (from the 2026-10-31 emotion bank, cut to six or seven rows), named in the hook and brought back; practical fixes for emotional problems; her own mirror; the why as the relief; the blame off her in fresh words; the trigger said on the garment; permission, never a slogan; each item ending on the result.
- **The flow:** point first; one-line bridges between items; the title's feeling back now and then, never as a refrain; questions to her now and then. The old "but", "I" and question rates are gone.
- **"Granny" or "old lady":** at most once, flagged as harsh (the operator's 2026-10-31 rule; the check fails a second one).
- **Lengths:** Scarlett's page about 1,350 words, Diane's about 1,500, the pack about 950, against about 46,000 words of rules before.

## Added back from the operator's decisions (they were in the 2026-10-31 skills, not in the test drafts)

- The book block after at least two full items, at the item closest to the book (operator, 2026-10-29).
- The book's other true facts (pages, frameworks, quick wins), and the book's own people never named.
- The small personal habits (2026-10-29 and 10-31), worded as optional.
- The safety defaults, the money rule, the age slogans and old house lines, operator wording winning.
- The Talking Head CTA markers and the VO copy, which production needs (the test scripts were plain text).

## On the operator's yes (not done yet)

1. Archive the current library copy: `style-scripts/`, `personas/scarlett-starling.md`, `personas/diane-de-chambray.md` and the account's 2026-10-31 copy into `archive/style-pack-2026-10/` (moved, never deleted).
2. Put the new files in their library places, update `tools/build_skills.py`, `tests/run_checks.py` (the style checks 83 to 92 test the old pack), `README.md`, `HANDOFF.md`, `CHANGELOG.md`.
3. Build and send three skills: `style-scripts`, `scarlett-starling-persona`, `diane-de-chambray-persona` (delete the old, upload the new).
