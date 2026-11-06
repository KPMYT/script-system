# DRAFT: P21, the HVAC rebuild (Roger the HVAC Guy)

Not part of the library yet. Built 2026-11-06 (session 16) from `drafts/lite-roger-the-hvac-guy-DRAFT.md` (the iter-12 one-page winner, 46 of 60 against the account pack's 44), the account's current `hvac-scripts` and `roger-the-hvac-guy-persona` skills, and `HANDOFF.md` §3, for the operator to see before anything replaces the library or goes to the account. Laid out like `drafts/p21-style/`, as the two skills would be uploaded.

| File | What it is | Replaces |
|---|---|---|
| `hvac-scripts/SKILL.md` | The steps: inputs, NOT READY, the video type and its model, write, read aloud, check, the output (about 1,100 words) | the account's `hvac-scripts/SKILL.md` (11,240 words), its `unit-plan-template.md`, and, for this channel, `core/workflow.md` sections 2 to 6 and every other core file |
| `hvac-scripts/check.py` | The hard-rules check (about 480 lines; no counts to meet) | the core scanner, the HVAC scanner block and the full audit, for this channel |
| `hvac-scripts/references/models/` | 8 real on-camera transcripts, one per file, with what to take, what not to take and signature phrases quoted exactly from the transcript: R35 (single-product fix), R34 (N things), R25 (mistakes, never-do), R23 (how-to), R27 and R28 (hidden cause), R22 (seasonal), R42 (product swap; the closest on disk for a head-to-head verdict) | the 31 model beat maps and `INDEX.md`, `excerpts.md` (9,124 words), `voice-samples.md` (1,276) |
| `hvac-scripts/references/price-guide.md` | The price guide, copied unchanged (byte for byte the account's and the library's) | the same file |
| `roger-the-hvac-guy-persona/SKILL.md` | Roger's one page (about 1,400 words) | the account's profile (1,196 words) and the HVAC rules spread across the pack |

**What does not change:** `script-writer` (START, the channel question, the channel list) and every other channel's skills.

**Models:** taken from the account's INDEX, HVAC-native ones only (R22 onward), each with its full transcript in `studies/hvac/data/`; timestamps removed, nothing else changed. "Take", "Don't take" and the timings come from the account's model files and `meta.md`. Not kept: R39 (the account file holds two stretches only and says its register is not a voice model), R04 and the other plumbing models (no transcript in `studies/hvac/`), R30, R31 and R41 (live parts), R38 (brand verdict: still NOT READY).

## iter-12's findings, and where each one went

| Finding (`tests/iterations/iter-12/RESULTS.md`, judge report) | On the page | In `check.py` |
|---|---|---|
| Run A clearer by ear (9 against 7): a do-along a listener can follow | plain signposts, number only real actions, say where the hands go, every check in the step where it's done | (by eye) |
| Run A more trusted (9 against 8): reasons, honest limits | the reason behind each step in one sentence; the honest limit; both sides, then the verdict | (by eye) |
| B: the pump check after the restart | every check in the step where it's done, in the hands' order | FAIL "while you're flushing" (or pouring, rinsing...) after the power is back on |
| B: the carbon monoxide aside between "fill the trap" and "power on" | never between power off and power back on: after the restart, or its own step | FAIL a carbon monoxide alarm between power off and power back on |
| B: "Then check the furnace": where to hold the tester | the tester held to the power cable going into the unit | FAIL a tester step that never says where |
| Both: vinegar "through the trap" when poured at a cleanout or vent tee | "it runs down the line, not back through the trap" | FAIL "through the trap" when the script pours at a cleanout or vent tee |
| A: "Step three" with nothing to do; repeated "I'd..." closers | number only real actions; don't end every step on the same kind of line | INFO phrases said three times or more |
| B: "the trade calls" three times | no tag repeated on each trade word | INFO the same |
| A's opening a stack of facts | point first, then honest scope, then straight into the first step; the scene optional | INFO the opening's length |

**The check on iter-12's scripts** (brief: `tests/iterations/iter-17/brief.txt`): run B fails 5, the judge's four faults (tester place, carbon monoxide placement, pump check order, "through the trap") and one 38-word sentence; run A fails 1 ("through the trap"). False alarms found and fixed on the way: "power off at the switch" read as the tester's place; "before the power goes back on" read as a restart; "each cup ... cents" read as cents outside a cost per use; a clause before a list of three read as a list of four. A test copy with planted faults (greeting, tease, "I tested", the name, two tenures, a gas smell without the steps, a carbon monoxide alarm without the steps, a marker, a mid-video subscribe, a guaranteed saving, cents) failed each one.

## Rules carried (from the account's skills, `HANDOFF.md` §3 and the lite draft)

- **Persona:** the same man and voice as Roger the Pipe Guy, 45 years at most once (the title's number wins), the filter check with his coffee, no other detail, no customer stories, no greeting or sign-off, the two Rogers never mention each other, DIY limits by the title and brief, "a tech you trust", swearing off.
- **The basics:** Classic (no markers); ElevenLabs; words per minute as the profile has it (unset, counted at 150); the VO copy per `core/workflow.md` §6.
- **The opening (HVAC's own, the plumbing rules it took on 2026-10-29, always modelled on a winner):** point first, honest scope, the first real step by about 45 seconds, as short as the model's; no tool list (each tool named once); one end-paid promise at most, no time on it; no "no tech needed" with a call point; carbon monoxide never the hook; the breakdown moment as an option.
- **Emotion, villain, proof, voice:** the HVAC pack's rules without their rates: the viewer's own house, one real pain, the four HVAC feelings, the title's feeling back now and then, the villain as two facts never joined into a motive, disgust at a big price, end each step on a win, finish on relief, "but" turns, questions, trade words explained, no first-person tests, no pointing, no customer stories; the voice forms (units, ratings, refrigerants, ranges, "nine-one-one", "carbon monoxide", no slashes, no sentence over 35 words).
- **Money:** the brief, then the price guide; rounded ranges, cents only for a cost per use; no guaranteed saving; the comparison early; the title's figure paid at its step; extra tools priced or "optional"; brands only when the brief confirms.
- **Safety:** all twelve defaults (the outage, space-heater and air-sealing ones by pointer to the price guide's section 9, which holds them); the carbon monoxide and gas-leak steps in full (the require-if rule: the account's scanner patterns, plus "whatever appliance" as an accepted wording and nine-one-one as a gas-leak step, both from the price guide's section 9); stop signs that name their trigger; the brief wins.
- **CTA and ending:** no book, no mid-video ask; relief and one small thing for tonight; one fresh subscribe line naming Roger the HVAC Guy; the comment ask with a question about their own house or numbers and "I read every one"; nothing after; no recap or homework list.
- **Length:** at least 12 minutes; 12 to 20; never pad; NOT READY when the brief can't fill it. **Bans:** the account's banned list and Ray Dutton's catchphrases (all in `check.py`). The brand-verdict NOT READY.

## Dropped (counts and templates only)

1. The opening's six numbered jobs in a fixed order, and each video type's "Opening, in order" column (templates); the 110-word and "Number one within about 75 words" limits as checks (now INFO).
2. The six-part item shape for lists (a template), and the 150-250 words per item guide (operator "agree", 2026-10-27).
3. About 7 "but" per 1,000 words and a "but" turn in every item; a question about every two items; an "I" verdict in most items; one line of insistence per video; one closing frame on at most a third of the items; the villain and the title's word "every few items".
4. Money counts: one dollar figure per item, figures on about half the items, one in the opening (now guidance and INFO); the rotation of money devices.
5. "Ways to promise more value": two or three per video and the device list; a forward line at least every five minutes.
6. The rotation log as an input, its fields, and "no model used in the last five scripts" (now: don't reuse the comment question or opening shape of earlier scripts in this chat); naming three differences from the model; the unit plan.
7. The persona device's "at most twice, under about 40 words"; the "at most once" stock-phrase list (now INFO, not FAIL); the core humanizer counts ("Most people" once, one reframe).
8. The full audit and its output blocks (VERDICT, FORMAT CHECK, ROTATION LOG ENTRY, AUDIT EVIDENCE); the excerpts, voice samples and beat maps as writer inputs.

## Doubts for the operator

1. **Words per minute.** The profile leaves it unset, so 12 minutes is counted at 150 (1,800 words). Roger the Pipe Guy's same voice was measured at 170 (2026-10-29): at that speed 1,800 words play in about 10.6 minutes.
2. **The thermostat-up check** for metal-armoured cable is the account's own default, kept as it is; the iter-12 judge said it isn't proof the power is off. Changing it needs your yes.
3. **Head-to-head titles** point to R42 (good, better, best, then the verdict), the closest on disk; the rule explainer has no model, as before.
4. **The rotation log** is no longer asked for, so a repeat of an earlier chat's comment question isn't caught.
5. **The price guide is unchanged,** so its "How to use it" still names `SKILL.md` "Money framing" (gone) and "at most one price per item".
6. **`check.py`'s new safety checks** (the tester's place, the carbon monoxide placement, the job order, "through the trap") are word patterns fitted to iter-12; other wordings can slip past. The gas-leak "light switch" step, as in the account's scanner, passes on any "light switch" in the script.
7. **"I read every one"** (also Ray Dutton's line) stays, as the account has it; still open since 2026-10-27.
8. **The persona page runs about 1,400 words,** over the 1,300 aimed for: the carbon monoxide and gas steps are carried whole.

## On the operator's yes (not done yet)

1. Archive the library's `hvac-scripts/`, `personas/roger-the-hvac-guy.md` and the account's copy into `archive/hvac-pack-2026-10/` (moved, never deleted).
2. Put the new files in their library places; update `tools/build_skills.py`, `tests/run_checks.py`, `README.md`, `HANDOFF.md`, `CHANGELOG.md`.
3. Run iter-17 (the brief is in `tests/iterations/iter-17/brief.txt`) blind against iter-12's two scripts, then build and send the two skills.
