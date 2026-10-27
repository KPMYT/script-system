# Wiring and scanner checks for an HVAC pack (Roger the HVAC Guy)

2026-10-27. Read-only diagnosis by a helper for the HVAC scripting chat. Nothing in the library was changed. The only file written in the repo is this one.

- **Sources:** `main` at `7fdd1a2` (the same commit as this chat's branch `claude/hvac-research-czb2hy`), `origin/claude/festive-planck-2e8f22` (plumbing: escalation line, R21, "fp" below) and `origin/claude/intelligent-ride-v1at70` (electrical pack, "el" below).
- **Scratch work (TEST data, outside the repo):** `/tmp/claude-0/-home-user/f63a7813-66f7-513b-a288-eabac2c20b9a/scratchpad/h3/`. It holds:
  - `test-profile-roger-the-hvac-guy.md`, a copy of `personas/roger-the-pipe-guy.md` with the name changed, tenure 45 and a placeholder book
  - `test-pack-hvac-scripts.md`, the plumbing scanner block unchanged
  - `test-pack-hvac-scripts-v2.md`, with the proposed HVAC bans added
  - `run_cases.py` and `results.json`
- **Line numbers** are for `main` unless a branch is named.
- **Measured vs my reading:** what the scanner did is measured. What a text-to-speech voice would do is my reading; no audio was made.

---

## 1. Every registration point

These are the places a new pack and channel must be added so that START offers Roger the HVAC Guy, the skills build, and the checks pass.

| # | Where | What's there for plumbing now | What HVAC needs |
|---|---|---|---|
| 1 | `core/channels.md:10-17` (table), `:8`, `:19-23` | Rows 3-5: `\| 3 \| Roger the Pipe Guy \| \`plumbing-scripts\` \| \`personas/roger-the-pipe-guy.md\` \| ready \|`. START shows only this list; `:8` says only **ready** rows can be scripted. | A new row `\| 8 \| Roger the HVAC Guy \| \`hvac-scripts\` \| \`personas/roger-the-hvac-guy.md\` \| pending \|` (row 7 is Frederick on el). Turn it to `ready` only after a test run passes, as Frederick and Sam did. |
| 2 | `core/workflow.md:21-24` | Shows the channels.md list. A profile that's missing or marked pending gives `NOT READY`. The pack is found by its name in channels.md. | Nothing to edit. Both the channels.md status **and** the profile's `Status:` line must say ready. `workflow.md` names no niche except as examples (`:75` "the plumbing pack sets 12 minutes", `:79` "woodworking: ...; a pack may name others, as plumbing does"), so HVAC needs no core edit to run. |
| 3 | `core/persona-profile-template.md:10-71` | The template: `Words per minute` (`:19`), the `inputs` and `scanner` blocks, and `name:`, `book:` and `tenure:` (`:68-70`). | Write `personas/roger-the-hvac-guy.md` from it, using Roger's profile as the model (row 4). |
| 4 | `personas/roger-the-pipe-guy.md` | `:10` `Status: ready`; `:11` `Niche pack: plumbing-scripts`; `:16` `Words per minute ...: not set` (so the scanner uses 150); `:43` rogerthepipeguybooks.com; scanner block `:71-79`: two `allow:` lines (the link-and-QR line, the book's spoken title), `name: Roger the Pipe Guy`, `book: ...`, `tenure: 45`, and the two e-book bans. | The copy needs:<br>- `Status: pending` and `Niche pack: hvac-scripts`<br>- a words-per-minute figure, or "not set"<br>- `name: Roger the HVAC Guy`, and `tenure: 45` (or another figure)<br>- `book:` and its `allow:` line only if he gets a book (Vintage has none: then no `book:` line)<br>- **keep both e-book bans** (check 28 tests every profile)<br>- his own book site, or "subscribe only"<br>- the plumbing-only lines rewritten (section 2, rows 9-10). |
| 5 | `personas/README.md:3` | Prose naming the written profiles. | Add a sentence for the new profile. |
| 6 | New folder `hvac-scripts/` | Copy `plumbing-scripts/`. Take it from fp, which adds the escalation line (`SKILL.md:126`) and R21. | Change in the copy:<br>- the frontmatter `name: hvac-scripts` and a new description (the 1,024-character limit applies; plumbing's is 734)<br>- the inputs block (fp `:62`), the overrides table (fp `:36`), the scanner block (fp `:383`) and "Before handing over" (fp `:422`)<br>- `references/price-guide.md` becomes an HVAC price guide, with the gas-leak row and a CO row<br>- `excerpts.md`, `voice-samples.md` and `models/` from the HVAC study<br>- `model-file-spec.md` and `archive/` stay out of the installed skill. |
| 7 | `tools/build_skills.py:28` | The script-writer description ends: "Channels ready now: Hank Hardwood, Dale Oakfield's Workshop and Sawdust Sam (woodworking for profit); Roger the Pipe Guy, Mark Silverbridge and The Vintage Pipefitter (plumbing)." It is now 688 characters. | Add "Roger the HVAC Guy (HVAC)" once he is ready. With HVAC and Frederick both added it is about 750 characters, under 1,024 (checked by `validate()`, `:125-135`). |
| 8 | `tools/build_skills.py:41-51` | The table of other skills: `plumbing-scripts` → the **plumbing-scripts** skill; each `personas/<slug>.md` → the **<slug>-persona** skill. | Two rows: `the niche pack \`hvac-scripts\`` → **hvac-scripts** (with `references/models/`), and `personas/roger-the-hvac-guy.md` → **roger-the-hvac-guy-persona**. **el didn't add its rows**, so the HVAC chat should check both are there after merging. |
| 9 | `tools/build_skills.py:68-78` | The two scanner command lines, woodworking and plumbing. Plumbing's is `--pack BRIEF <plumbing-scripts>/references/price-guide.md ... --refs <plumbing-scripts>/SKILL.md .../excerpts.md .../voice-samples.md .../models/*.md <channel-persona>/SKILL.md`. | A third, "HVAC" command: the same shape with `<hvac-scripts>`, its price guide in `--pack`, and its own copy-guard files in `--refs`. Without it, a VA chat has no command written out for HVAC. el didn't add one either. |
| 10 | `tools/build_skills.py:145-152` (`PERSONAS`) | `"roger-the-pipe-guy": ("Roger the Pipe Guy", "personas/roger-the-pipe-guy.md", "personas/books/roger-the-pipe-guy-book.md")` | `"roger-the-hvac-guy": ("Roger the HVAC Guy", "personas/roger-the-hvac-guy.md", <book or None>)`. The persona skill's description comes from `:180-182`, under 1,024 characters. |
| 11 | `tools/build_skills.py:155-158` (`PACKS`) | `"plumbing-scripts": ("archive", "model-file-spec.md")` | `"hvac-scripts": ("archive", "model-file-spec.md")`. The main loop (`:201`) builds every entry. |
| 12 | `tools/build_skills.py:85-107` (`INSTALL`) | "Eleven skill files", a table of 12 rows, and step 1's list of names. Hard-coded counts and names. | The count, two rows (hvac-scripts, roger-the-hvac-guy-persona) and the step lists. el left this alone too. |
| 13 | `README.md` | `:3` "so far, `woodworking-scripts/` and `plumbing-scripts/`"; `:36` the plumbing section; `:65` the list of `dist/` skills; `:67-80` personas; `:82-96` studies; `:99` "52 automated checks". | An `## hvac-scripts/` section, a persona row, the `dist/` names, a `studies/hvac/` row (this folder) and the check count (CLAUDE.md rule 7). |
| 14 | `tests/run_checks.py:12`, `:254-255` | Constants `PL`, `PLR`, `ROGER`, `MARK`, `VINT`, `PL_REFS`. | Add `HV=f"{ROOT}/hvac-scripts"`, `HVR`, `ROGER_HVAC`, `HV_REFS` (el's pattern: `EL`, `ELR`, `FRED`, `EL_REFS`). |
| 15 | `tests/run_checks.py:330-337` (check 26) | A regex for the three plumbing rows (`:334` hard-codes `` `plumbing-scripts` `` and `ready`), plus each profile's `Status: ready` and `Niche pack: plumbing-scripts`. | A matching HVAC check: row 8 is on `hvac-scripts`, and the status in channels.md and the profile agree (pending now, ready later). |
| 16 | `tests/run_checks.py` checks 21, 22, 24, 25/25b, 32, 34, 36 | All plumbing-specific:<br>- 21: inputs block<br>- 22: each scanner ban fires, plus a clean paragraph<br>- 24: the copy guard over every ref file<br>- 25/25b: Roger, Mark, Vintage facts<br>- 32: the runtime is 150 wpm for Roger, minimum 12<br>- 34: the CTA wording passes the copy guard<br>- 36: the price guide's rows and checks | An HVAC twin of each, as el did (el's 46-51). Check 36 also needs `"price-guide.md" in build_skills.py`, which an HVAC price guide would pass anyway. |
| 17 | `tests/run_checks.py:348-352` (check 28) | Every `personas/*.md` with a scanner block must flag "e-book". | Automatic: the HVAC profile is picked up. It passes only if it keeps the two bans. |
| 18 | `tests/run_checks.py:17-18`, `:41-53` (check 1b), `:59` (check 2) | File-reference and stale-word checks cover only `core/`, `woodworking-scripts/`, `plumbing-scripts/` and `personas/`. | An HVAC pack's broken references or stale words would **not** be caught. Add `HV` to those globs. el didn't extend them either. A profile pointing at a missing `personas/books/roger-the-hvac-guy-book.md` **would** fail 1b. |
| 19 | `core/script-scanner.py:218-247` | How the scanner reads a block: any `` ```scanner `` block in any `--rules` file, with the keys `ban`, `ban-regex`, `once`, `once-regex`, `lift`, `allow`, `name`, `book`, `tenure` and `min-minutes`. | The HVAC pack's block and the profile's block need nothing new. Copy plumbing's `min-minutes: 12`. |
| 20 | `core/script-scanner.py:215` | Words per minute: `^Words per minute[^:\n]*:\s*(\d+)`, taken from any rules file; the last match wins, and the default is 150 (`:621`). | The figure must be the first number after the colon. Roger's "not set" gives 150. |
| 21 | `--refs` (the copy guard) | Not set in code: it's whatever the pack's overrides row lists (plumbing `SKILL.md:47`) and the command in row 9. Check 37 tests the string `--refs <plumbing-scripts>/SKILL.md` in `build_skills.py`. | The HVAC pack's override row names its own `SKILL.md`, `excerpts.md`, `voice-samples.md`, `models/*.md` and the profile, and leaves the price guide out, as plumbing does. If an HVAC model is copied from a plumbing model (S13 Mark's furnace condensate line and S18 TheCheapFix HVAC are HVAC topics), keep it in both packs' refs. |
| 22 | `tools/verify_plumbing_models.py:5`, `:11` | Hard paths: `plumbing-scripts/references/models/[RS]*.md` and `studies/plumbing/data/*/*/<id>/transcript.txt`. | A copy (`verify_hvac_models.py`), or the pack name as a setting, so the HVAC model scripts are checked word for word against their transcripts. |

---

## 2. Hard-coded plumbing or Roger assumptions

I searched `core/`, `tools/` and `tests/` for plumb, Roger, pipe, toilet, drain, gas, water, price-guide, Hank and woodwork. Most hits are examples in prose (`humanizer.md:33/43/46/185/216`, `variety-rotation.md:35/39/44/66`, `retention-mechanics.md:16/19/90`), which are harmless. The ones that matter:

| # | Where | Assumption | What it does to HVAC |
|---|---|---|---|
| 1 | `script-scanner.py:387` `_TRADE` | The words that count as "the trade": `experience`, `trade`, `plumbing`, `plumber`, `pipefitt…`, `tools`, `bench`, `shop`, `job`, `field`, woodworking words and `doing this`. No hvac, heating, cooling, furnace or technician. | **A wrong tenure passes silently:** "In my 40 years in HVAC", "40 years as an HVAC tech" and "40 years in heating and cooling" all pass against tenure 45 (cases c36, c37, c37b). The same gap hits el: "I spent 25 years as an electrician" passes against Frederick's 35 (tested with el's files). |
| 2 | `script-scanner.py:394` (`TENURE_RX[2]`) | The "-year" nouns: `plumber`, `pipefitter`, `veteran`, `master`, `tradesman`, `woodworker`, `carpenter`, `pro` and `career`. | "a 40-year HVAC man" passes (c38). **Title numbers don't unlock:** `title_tenure` (`:407-413`) uses the same list, so the title "Don't Replace Your Furnace Yet: A 50-Year HVAC Tech's Warning" isn't read. The script's "50 years" then **fails falsely** (c46), while "A 50-Year Plumber's Verdict" passes (c46b). "What 50 Years in HVAC Taught Me" fails the same way (c46c). It only bites when the title's figure isn't 45. |
| 3 | `script-scanner.py:392` (`TENURE_RX[1]`) | `working`, `worked` and `spent` count as the persona's own years with no subject check. Only `been` is checked (`:435`). | **False failure:** "That old compressor kept working for 20 years" fails as a tenure (c40). Plumbing has the same bug ("That old water heater kept working for 20 years" fails with the real Roger profile), but equipment lifespans are said far more in HVAC. |
| 4 | `script-scanner.py:435` | "my X has been ... for N years" counts as the persona ("My hands have been in pipes for 30 years", check 29). | **False failure:** "My furnace has been running for 20 years" fails (c41; "The furnace has..." passes, c42). |
| 5 | `script-scanner.py:432` | `TENURE_RX[0]` counts "N years of experience" whenever I, me, my or we is within 40 characters. | **False failure:** "Techs with 20 years of experience told me the same thing" fails (c43). |
| 6 | `script-scanner.py:392` | "for N years" is required. | "I've been doing this 40 years" (no "for") passes silently (c35), and so does "After 40 years, I can tell you" (no trade word). This affects every niche. |
| 7 | `script-scanner.py:138` `SPOKEN_LETTERS_OK` | Fixed at OK, TV, QR, DIY, US and USA. No scanner key lets a pack add to it. | Every HVAC, AC, MERV, SEER, BTU and AFUE is a judge line. The judge list prints only 25 (`:627`). In a test with 14 paragraphs naming MERV, HVAC and BTU, then one thumbnail line and one staccato run, the count read 44 and **neither the packaging flag nor the staccato flag was printed**: the letters pushed them off the list. |
| 8 | `script-scanner.py:128` | The symbol rule is `[&+#=~@]`, and the fraction rule needs digits (`:126`). | "A/C" and "heating/cooling" pass silently (c49), though `workflow.md:107` bans "/". |
| 9 | `personas/roger-the-pipe-guy.md:23`, `:51`, `:59-60` | His one personal detail is "his own drain routine ... first Saturday"; "standing next to him at the sink"; the hard no's say "never recommend caustic chemical drain cleaners, never encourage DIY on gas, sewage, electrical". | These need rewording for HVAC. The "gas and electrical" hard no **clashes** with ordinary HVAC topics (thermostat wiring, capacitors on 240 volts, gas furnaces): the operator must say where the line is. |
| 10 | `plumbing-scripts/SKILL.md` | The "Roger and Mark" CTA wording (`:48`, `:429`), the gas-leak row "of `references/price-guide.md` section 9" (`:350`), the five safety defaults about drains, and "your (wallet\|pipes) will thank you" (`:56` of the block). | All of these copy across blindly. "Your furnace will thank you" passes the copied ban (c51). The HVAC price guide needs a gas-leak row and a carbon monoxide row before the Safety section's pointer works. |
| 11 | `plumbing-scripts/SKILL.md:3` (description) | "Use whenever a plumbing script is written ... or a plumbing title and brief arrive", "and any future channel in this niche". | On claude.ai an HVAC title (a furnace drain line, say) could trigger `plumbing-scripts` instead of `hvac-scripts`. The HVAC description should name its own triggers. Adding "not HVAC" to plumbing's description changes a skill, so it needs the operator's yes. |
| 12 | `script-scanner.py:254-256`, `:173-178`; `tests/run_checks.py:381-382` | Minor: `UNIT_WORDS` has no ton, volt or amp ("a three-ton unit" is never number-checked); `INSTRUCTION_VERBS` has no change, replace or swap ("Swap the filter." counts toward staccato, a judge line); check 32 expects 150 wpm for Roger. | No failures. An HVAC copy of check 32 uses the HVAC profile's figure. |

**Also, a near-miss between the two Rogers:** with `name: Roger the HVAC Guy`, the line "Roger the Pipe Guy has that covered" fails as `[PERSONA FACT: near-miss name]` (c47). The reverse also fails on the real Pipe Guy profile. An `allow:` line doesn't help, because it only exempts lines from the copy guard. Any cross-promotion between the two channels needs a scanner change, or the other channel isn't named.

---

## 3. Merge-conflict map

**Trial merge** (scratch clone of the repo): main + fp merges clean; adding el on top then conflicts in `HANDOFF.md`, `PROPOSALS.md` and `tests/run_checks.py`. Neither branch touches `core/script-scanner.py`.

| Shared file | fp changes | el changes | What HVAC will change | Conflict risk |
|---|---|---|---|---|
| `tests/run_checks.py` | Header comment; **check 46** (escalation line, R21) appended after 45 | **Checks 46-51** appended after 45 (`EL`, `ELR`, `FRED`, `EL_REFS`; el's 46 reuses `want` from check 21) | Its own checks, appended at the end | **Conflict** (both write at the same spot); **46 is used twice** |
| `PROPOSALS.md` | **P11** = the escalation line (plumbing, approved) | **P11** = one value promise in the electrical opening (approved) | Any HVAC proposal | **Conflict, and P11 is confirmed to mean two different things** |
| `HANDOFF.md` §3 | "Operator decisions, 2026-10-27 (the drywall video)" after the 2026-10-25 block | "Operator decisions, 2026-10-27 (the electrical pack and Frederick Barnes)" at the same spot | An "Operator decisions (HVAC)" block | Conflict (same insertion point) |
| `CHANGELOG.md` | 2 rows at the **top** (newest first) | 2 rows at the **bottom** of the table (against the newest-first order) | Rows | Auto-merged in the trial; el's rows are in the wrong place |
| `README.md` | `:45` the models row (39 files, R21) | `:3` the intro ("so far ... and `electrical-scripts/`"), a new pack section, a Frederick row, a `studies/electrical/` row | `:3` again, a pack section, a persona row, a studies row | `:3` is edited by el and HVAC, so a likely conflict |
| `core/channels.md` | none | Row 7 Frederick, `pending` (el `:18`) | Row 8 | Adjacent lines, so a likely conflict; keep both |
| `tools/build_skills.py` | none (fp rebuilt `dist/`) | `PERSONAS` + frederick (el `:152`), `PACKS` + electrical (el `:159`, leaves out only `model-file-spec.md`) | The same two dictionaries, plus rows 7-9 and 12 of section 1 | Adjacent lines, likely conflict; keep both |
| `personas/` | none | `frederick-barnes.md` (new) | `roger-the-hvac-guy.md` (new) | none |
| `dist/` | Fully rebuilt (new dated zips; the 2026-10-25 zip removed) | not rebuilt | A rebuild | Binary conflicts if two branches both commit `dist/`. Rebuild once, after merging. |

**Checks run:** main 52/52; fp 53/53; el 57/58. el's check 49 fails because `electrical-scripts/references/excerpts.md` and `voice-samples.md` don't exist yet (refs=32, while the check wants 35 or more). That is el's work in progress, not an HVAC problem.

**An el bug that HVAC would inherit if it copied el's unit regex:** el's ban `\b\d[\d,.]*\s?(?-i:V|A|W|kW|kWh|mA|Hz|VA)\b` lets "." into the number. So "The rule changed in 2023. A tamper-resistant outlet is required now." **fails** as "unit written as a symbol" (tested with el's SKILL.md), and so does "Number 3. A dirty filter". The version in section 4 uses `[\d,]*(?:\.\d+)?` and passes both. Worth telling the electrical chat.

**Recommendations for numbering and placement:**
1. **Merge order:** fp is already on the account, so it's likely to land first. Then fp keeps check 46 and P11, and el becomes checks 47-52 and P12. That is el's job when it merges; HVAC shouldn't renumber other chats' work.
2. **HVAC check numbers: take a block clear of both, 60-69**, under `# ---- the HVAC pack and Roger the HVAC Guy ----`, appended last. Numbers 47-59 stay free for el's renumbering and any plumbing follow-ups. Say this in the CHANGELOG row.
3. **HVAC proposals: give a working name in the draft ("P-HVAC-a") and take the next free P-number only when merging into `main`.** If fp then el land first, that is P13. Put the HVAC block last in `PROPOSALS.md`.
4. **Channel row 8**, `pending`. **Build entries** go after el's lines in `PERSONAS` and `PACKS`. **README:** write the intro as "so far, `woodworking-scripts/`, `plumbing-scripts/`, `electrical-scripts/` and `hvac-scripts/`".
5. **One chat fixes the shared scanner gaps** (section 2, rows 1-8), since both new packs need them: the electrician, HVAC and heating words; "doing this N years"; the subject check for `working` and `spent`; a pack `letters-ok:` key or a bigger judge list; "/" between words. These are core changes and need a test for each. Agree which chat does them so the two don't edit the same scanner lines.
6. CHANGELOG rows go newest first at the top. `dist/` is rebuilt only after the merge.
7. **Copy the plumbing pack from fp, not main** (fp has the escalation line and R21). Note that P11 (fp) was approved for plumbing: whether the escalation line carries over to HVAC is the operator's call, since "very similar to what Roger is right now" (HANDOFF 2026-10-23) points to yes.

---

## 4. Scanner tests on HVAC language

**How it was run:** the same call `run_checks.py` makes (`run_scan`, `tests/run_checks.py:95-98`): `python3 core/script-scanner.py FILE --rules test-pack-hvac-scripts.md test-profile-roger-the-hvac-guy.md --pack test-brief.md [--title T]`. Each line ran as its own one-sentence script. "Fail" means exit code 1 (fix on sight). "Judge" means a line to judge by hand that doesn't fail. TEST data only.

| Form (as written in the line) | Scanner | What the voice likely does (reading) | Pack needs |
|---|---|---|---|
| "MERV 13" / "a MERV 8 filter" | pass, judge (letters MERV) | "merv thirteen", as techs say it | nothing (judge) |
| "MERV-13" | pass, judge | probably fine; the hyphen is a small risk | spoken-form rule: write "MERV 13" |
| "16 SEER2" | **fail**: letters-and-digits code | might say "seer-two" or spell it out | spoken form "16 SEER two" (passes) |
| "SEER" | pass, judge | "seer", fine | nothing |
| "96% AFUE" | **fail**: percent sign | n/a | "96 percent" (passes); AFUE stays a judge line |
| "AFUE" | judge | may try to say it as a word ("a-foo-ee") | spoken form: "the efficiency rating", or "A F U E" |
| "an 80,000 BTU furnace" | pass, judge (BTU) | "eighty thousand B T U", fine | nothing |
| "80K BTU" | **fail**: number written short | — | covered by the core |
| "R-410A" / "R-454B" | **fail**: letters-and-digits code | "R four hundred ten A" is likely; techs say "four-ten-A" | spoken form: "R-four-ten-A", "R-four-fifty-four-B" |
| "R-22" | **pass silently** | probably "R twenty-two"; could come out "R minus 22" | ban-regex for refrigerant codes (below), "R-twenty-two" |
| "24-volt" | pass | fine | nothing |
| "24V" / "240V" | **fail**: letters-and-digits code | "twenty-four V" | covered |
| "24 V" / "240 V" (with a space) | **pass silently** | "twenty-four V" | **ban-regex** for units as symbols |
| "1/2 inch", "3/4-inch PVC" | **fail**: fraction with a slash | — | covered; "three-quarter-inch PVC" (PVC is a judge line, said as letters) |
| "a 20x25x1 filter", "16x25x4" | **fail**: size with x | "twenty x twenty-five x one" | covered; spoken form "a twenty by twenty-five by one filter" (passes) |
| "68°F", "7-10°F" | **fail**: non-standard character ° | — | covered |
| "68 degrees" | pass | fine | nothing |
| "7-10 degrees", "15-20 years" | **pass silently** | "seven ten degrees" or "seven minus ten" | **ban-regex** for ranges written with a hyphen |
| "HVAC" | pass, judge | "H V A C" or "H-vac", both fine | nothing; but see the 25-line judge cap (section 2, row 7) |
| "CO" | pass, judge | might come out "co" (as in co-op) | **ban-regex**: always "carbon monoxide" (a safety term) |
| "ECM", "PSC" | pass, judge | letters, fine, but the viewer won't know them | content rule: explain once, or say "a variable-speed blower motor" |
| "C-wire" | pass, no flag | "see wire", fine | nothing |
| "a 3-ton unit" | pass | fine | nothing |
| "5 psi" | **fail**: unit abbreviation, psi | — | covered ("five pounds of pressure") |
| "15 amps", "1,500 watts" | pass | fine | nothing |
| "1500 W" | **pass silently** | "fifteen hundred W" | ban-regex for units (below) |
| "$75-$200" | **pass silently** | uncertain: "seventy-five dollars, two hundred dollars" | ban-regex for ranges; write "$75 to $200" (the core's own form, `workflow.md:108`) |
| "$5 to $15" | pass | fine | nothing |
| "a 20-year-old furnace", "furnaces last 15 to 20 years", "a 10-year parts warranty" | pass, no tenure flag | fine | nothing |
| "a 45,000 BTU model, the 59SC5A045" | the model code **fails** (letters-and-digits); **no** tenure flag from "45" | — | the scanner works as meant |
| "After 45 years" (the right tenure) | pass | — | nothing |
| "I've been doing this 40 years" | **pass silently** (wrong tenure) | — | scanner fix (section 2, row 6) |
| "I've been doing this for 40 years", "I've worked on furnaces for 40 years", "40 years in the trade" | **fail**: tenure (right) | — | nothing |
| "40 years in HVAC", "40 years as an HVAC tech", "40 years in heating and cooling", "a 40-year HVAC man" | **pass silently** (wrong tenure) | — | scanner fix (section 2, rows 1-2) |
| "That old compressor kept working for 20 years" | **FALSE FAIL**: tenure | — | scanner fix (row 3) |
| "My furnace has been running for 20 years" | **FALSE FAIL**: tenure | — | scanner fix (row 4); or write "That furnace has been..." |
| "Techs with 20 years of experience told me..." | **FALSE FAIL**: tenure | — | scanner fix (row 5) |
| Title "A 50-Year HVAC Tech's Warning" + "50 years" | **FALSE FAIL**: tenure (the title isn't read) | — | scanner fix (row 2) |
| "Roger the Pipe Guy has that covered" | **fail**: near-miss name | — | decide whether cross-promotion is allowed |
| "A/C", "heating/cooling" | **pass silently** | "A slash C" | ban-regex for a slash between words |
| "Your furnace will thank you" | **pass** (the plumbing ban covers wallet and pipes only) | — | widen the ban |

**Proposed additions to the HVAC scanner block**, tested in `test-pack-hvac-scripts-v2.md`. Each one fails its bad forms and passes "in 2025. A new unit", "Number 3. A dirty filter", "MERV-13", "3-ton", "C-wire", "$5 to $15", "R-twenty-two", "carbon monoxide", "a twenty by twenty-five by one filter", "the co-op", "Call 911" and "a 10-year parts warranty":

```
ban-regex: \b\d[\d,]*(?:\.\d+)?\s?(?-i:V|A|W|kW|kWh|Hz|VA|BTUh?|F)\b | unit written as a symbol (write the word: 'twenty-four volts')
ban-regex: (?<![\w-])\$?\d[\d,]*\s?-\s?\$?\d | range written with a hyphen (write '$75 to $200', 'seven to ten degrees')
ban-regex: \b[A-Za-z]+/[A-Za-z]+\b | slash between words (write 'AC', 'heating and cooling')
ban-regex: \bR-?\d{2,3}[A-Za-z]?\b | refrigerant written as a code (write 'R-twenty-two', 'R-four-ten-A')
ban-regex: (?-i:\bCO\b) | CO (write 'carbon monoxide')
ban-regex: \byour (?:wallet|pipes|furnace|system|unit|AC|air conditioner|heat pump) will thank you\b | template stock line
```

The range and slash rules apply to every niche, so they could go in the core scanner instead (`SPOKEN`, `:120-135`). That is a core change, with tests.

**Spoken-form rules for the HVAC pack's voice section:**
- **Ratings:** "MERV 13" with a space; "16 SEER two"; "96 percent".
- **AFUE:** "the efficiency rating", or "A F U E".
- **Refrigerants:** "R-four-ten-A", "R-twenty-two", "R-four-fifty-four-B".
- **Volts and filters:** "twenty-four volts"; "a twenty by twenty-five by one filter".
- **Ranges:** "seven to ten degrees", "$75 to $200".
- **Carbon monoxide:** always the words, never CO.
- **Explain once:** ECM, PSC, C-wire, heat exchanger, capacitor, condensate line.

### The two Rogers: the near-miss name check (`script-scanner.py:453-500`)

The check flags a phrase that shares a key word with the profile's `name:` (words over 3 letters: "Roger", "Pipe", "HVAC"). It only flags when **at least two of the words are capitalised** and one capitalised word isn't part of the name. It ignores case and spacing when matching the exact name. A shortened form inside the name ("the HVAC Guy" when the name is "Roger the HVAC Guy") always passes.

**(a) With the real Pipe Guy files** (`plumbing-scripts/SKILL.md` and `personas/roger-the-pipe-guy.md`):

| Line | Result |
|---|---|
| "...my friend Roger the HVAC Guy has you covered." | **fail**: near-miss "Roger the HVAC Guy" |
| "Roger the HVAC guy covers furnaces." (lower-case guy) | **fail**: near-miss "Roger the HVAC" |
| "I cover furnaces over on my HVAC channel." | **pass**, no flag |
| "Subscribe to the HVAC Guy for more." | **pass**, no flag |
| "Subscribe to Roger the Pipe Guy for more." (control) | pass |

**(b) With the TEST HVAC profile** (`name: Roger the HVAC Guy`):

| Line | Result |
|---|---|
| "...Roger the Pipe Guy has that covered." | **fail**: near-miss "Roger the Pipe Guy" |
| "Subscribe to Roger the Plumber for more." | **fail**: near-miss |
| "Roger the Heating Guy", "Roger the Furnace Man", "Roger The Plumber Guy" | **fail**: near-miss, each |
| "Subscribe to Roger the HVAC guy for more." (lower-case guy) | **pass**: case is ignored for the name itself |
| "That's Roger's rule for filters." / "Roger here..." / "I'm Roger..." | **pass**, no flag (one capitalised word isn't enough). "Roger here" and "I'm Roger" are name intros the plumbing pack bans in its rules (`SKILL.md` "Banned": "a name or channel intro"), but **its scanner block has no ban for them**, so they pass. |
| "Subscribe to **the Pipe Guy** for more." | **pass silently**: the other channel's short name |
| "subscribe to roger the pipe guy for more." (all lower case) | **pass silently** |

**What this means:**
- **False failures:** any script that names the sister channel on purpose fails, in both directions, and nothing in the profile can exempt it. `allow:` lines only cover the copy guard, and there is no "lift" for a persona fact. If the operator wants the two channels to cross-promote ("my friend Roger the Pipe Guy covers drains"), the scanner needs a new key (for example `also-name:`, a name that may appear as it is), and that is a core change. Otherwise the rule is simply: never name the other channel.
- **Wrong-channel slips that pass:**
  - the other channel's short name ("the Pipe Guy" on HVAC, "the HVAC Guy" on Pipe)
  - "my HVAC channel" on the Pipe Guy
  - anything in lower case
  - a bare "Roger" or "Roger's", which is harmless (both channels are Roger) but ties nothing to a channel

  A VA chat that copies a Pipe Guy CTA into an HVAC script ("Grab it, the Pipe Guy's book...") would pass on the name check. It would be caught only by the book or link check: the copy guard against the profile, or a ban on the old book's site.
- **Yes, a profile can ban the other channel's name outright.** `ban-regex:` lines work in a profile's scanner block (`script-scanner.py:232-233`; Mark's contraction ban is one). Tested in `test-profile-roger-the-hvac-guy-ban.md` with `ban-regex: \broger the pipe guy\b|\bthe pipe guy\b | the other channel's name`:
  - "Roger the Pipe Guy has that covered" fails (both the ban and the near-miss fire)
  - "Subscribe to the Pipe Guy" now fails
  - "Subscribe to Roger the HVAC Guy" still passes

  Bans are case-insensitive, so the lower-case slip is caught too. **Recommended:** the HVAC profile bans `the pipe guy` and `rogerthepipeguybooks`; the Pipe Guy's profile bans `the hvac guy` and `my hvac channel`. Changing the Pipe Guy's profile changes a ready channel, so it needs the operator's yes. A ban on "the pipe guy" would also catch a deliberate cross-mention, so this is the same operator decision as the cross-promotion question above.

**Stability:** cases c30, c35, c40, c46 and c47 ran a second time with the same results (exit codes and findings identical). The near-miss lines "Roger the HVAC Guy" (Pipe Guy profile) and "Roger the Pipe Guy" (HVAC profile) were also run twice, with the same result.

---

## 5. `python3 tests/run_checks.py` on main

**52/52 passed** on `main` (`7fdd1a2`, the same commit as this branch). For the merge picture, run from untouched copies of each branch with `LIB_ROOT`: fp 53/53, el 57/58 (check 49; see section 3).

**Spot-checked file:line references** (re-opened to confirm):
- `core/script-scanner.py:387` (`_TRADE`)
- `tools/build_skills.py:28` (the script-writer description)
- `tests/run_checks.py:334` (the channel-row regex)
- `core/channels.md:17` (row 6, Sam)
- `plumbing-scripts/SKILL.md:377` / `:416` (the scanner block and "Before handing over" on main; fp `:383` / `:422`)
