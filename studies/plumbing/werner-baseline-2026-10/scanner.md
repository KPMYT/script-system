# Werner Finkbeiner baseline: scanner results

Run 2026-10-27 from the repo root, once per script:

```
python3 core/script-scanner.py <scratch copy> --rules plumbing-scripts/SKILL.md --title "<title>"
```

**What was scanned.** The library's scanner (`core/script-scanner.py`) reads the ```` ```scanner ```` block in each `--rules` file. `--rules` takes niche packs and/or persona profiles. Werner has no persona profile in `personas/`, so only the plumbing pack was passed. That means no name, book or tenure facts were checked, and the runtime estimate uses the default 150 words a minute. No `--pack` (fact source) was given, so the number check did not run, and no `--refs`, so the copy guard did not run.

**Scanned from a stripped copy, not the saved file.** A trial on `scripts/09-mold-5-minute-habit.md` as saved showed that the scanner trips on three things. The escaped marker lines (`\===START CTA(...)===`) are read as speech: each one gives a "PRODUCTION NOTE: CTA label", several "SPOKEN: symbol" findings and judged "letters 'CTA'" findings, 30 fix-on-sight findings in all for that one script. The escaped voice tags (`\[warm\]`) also slip past its tag filter. And the em dash in this folder's title header line is flagged. So each script was scanned from a temporary copy in a scratch directory outside the repo: header removed, escapes undone, voice tags and the CTA marker lines **removed**, CTA text kept. This is the same "spoken text" that `counts.md` measures, and the scanner's word count matched it for every script.

**Verdict** = the scanner's exit code: FAIL if it found any fix-on-sight problem (exit 1), PASS otherwise. The scanner flags and does not judge: the "judge" findings are candidates for a person to look at, not failures.

## Verdict and counts per script

| # | Verdict | Fix on sight | Judge | Fix-on-sight labels | Judge labels | Echo phrases (H18) | Reframe floor (H21) |
|---|---|---|---|---|---|---|---|
| 1 | FAIL | 7 | 10 | NICHE/PERSONA BAN: template stock line: channel promise ×1; SPOKEN: percent sign (write 'percent') ×6 | trailing 'Not Y.' beat ×2; staccato x2 ×6; not-X-period beat ×1; staccato x5 ×1 | 1 | 1 |
| 2 | FAIL | 1 | 7 | REPEATED SENTENCE ×1 | staccato x2 ×6; staccato x9 ×1 | 4 | 0 |
| 3 | PASS | 0 | 11 | none | staccato x2 ×6; SPOKEN, judge: letters 'PVC' (keep only if people say it as letters; otherwise the words) ×2; SPOKEN, judge: letters 'ABS' (keep only if people say it as letters; otherwise the words) ×1; trailing 'Not Y.' beat ×2 | 2 | 0 |
| 4 | FAIL | 1 | 16 | NICHE/PERSONA BAN: template stock line: channel promise ×1 | staccato x2 ×11; staccato x3 ×2; trailing 'Not Y.' beat ×2; not-X-period beat ×1 | 2 | 1 |
| 5 | FAIL | 1 | 14 | SPOKEN: 'psi' (say 'pounds of pressure' or 'pounds per square inch') ×1 | trailing 'Not Y.' beat ×2; staccato x2 ×7; staccato x3 ×3; staccato x4 ×1; SPOKEN, judge: 'wound' can be said two ways; reword if both fit ×1 | 3 | 0 |
| 6 | FAIL | 1 | 7 | NICHE/PERSONA BAN: template stock line: channel promise ×1 | SPOKEN, judge: letters 'EPA' (keep only if people say it as letters; otherwise the words) ×6; staccato x2 ×1 | 0 | 0 |
| 7 | FAIL | 2 | 15 | NICHE/PERSONA BAN: template stock line: channel promise ×1; HARD BAN: tease: keep watching ×1 | trailing 'Not Y.' beat ×3; not-X-period beat ×1; staccato x3 ×5; staccato x2 ×5; staccato x4 ×1 | 1 | 1 |
| 8 | PASS | 0 | 7 | none | not-X-period beat ×1; trailing 'Not Y.' beat ×1; staccato x2 ×4; talks about its own packaging ×1 | 2 | 1 |
| 9 | FAIL | 1 | 1 | NICHE/PERSONA BAN: template stock line: channel promise ×1 | staccato x2 ×1 | 0 | 0 |
| 10 | FAIL | 1 | 1 | NICHE/PERSONA BAN: template stock line: channel promise ×1 | staccato x3 ×1 | 3 | 0 |
| 11 | FAIL | 1 | 3 | NICHE/PERSONA BAN: template stock line: channel promise ×1 | staccato x2 ×3 | 3 | 0 |
| 12 | FAIL | 1 | 1 | NICHE/PERSONA BAN: template stock line: channel promise ×1 | staccato x2 ×1 | 0 | 0 |
| 13 | PASS | 0 | 1 | none | talks about its own packaging ×1 | 2 | 0 |
| 14 | FAIL | 1 | 9 | NICHE/PERSONA BAN: template stock line: channel promise ×1 | staccato x2 ×6; staccato x3 ×2; staccato x5 ×1 | 0 | 0 |

PASS 3 of 14 (#3, #8, #13). FAIL 11 of 14. "MOST ..." openers: 0 in every script. Filler phrases over the limit (H23): 0 in every script.

## Labels across all 14

| Label | Kind | Total findings | Scripts |
|---|---|---|---|
| NICHE/PERSONA BAN: template stock line: channel promise | fix on sight | 9 | 9 |
| SPOKEN: percent sign (write 'percent') | fix on sight | 6 | 1 |
| REPEATED SENTENCE | fix on sight | 1 | 1 |
| SPOKEN: 'psi' (say 'pounds of pressure' or 'pounds per square inch') | fix on sight | 1 | 1 |
| HARD BAN: tease: keep watching | fix on sight | 1 | 1 |
| staccato x2 | judge | 57 | 12 |
| staccato x3 | judge | 13 | 5 |
| trailing 'Not Y.' beat | judge | 12 | 6 |
| SPOKEN, judge: letters 'EPA' (keep only if people say it as letters; otherwise the words) | judge | 6 | 1 |
| not-X-period beat | judge | 4 | 4 |
| staccato x5 | judge | 2 | 2 |
| SPOKEN, judge: letters 'PVC' (keep only if people say it as letters; otherwise the words) | judge | 2 | 1 |
| staccato x4 | judge | 2 | 2 |
| talks about its own packaging | judge | 2 | 2 |
| staccato x9 | judge | 1 | 1 |
| SPOKEN, judge: letters 'ABS' (keep only if people say it as letters; otherwise the words) | judge | 1 | 1 |
| SPOKEN, judge: 'wound' can be said two ways; reword if both fit | judge | 1 | 1 |

All staccato variants together: 75 findings in 13 scripts.

## Quoted examples

- **NICHE/PERSONA BAN: template stock line: channel promise** (#1): ...I am Werner Finkbeiner. This channel is for people in America living in houses and ...
- **NICHE/PERSONA BAN: template stock line: channel promise** (#4): ...I am Werner Finkbeiner. This channel is for the American homeowner and the American...
- **HARD BAN: tease: keep watching** (#7): ...e American house is a thing you want to keep watching, subscribe to Werner Finkbeiner and tel...
- **REPEATED SENTENCE** (#2): "Number three." said twice in a row
- **SPOKEN: percent sign (write 'percent')** (#1): ...lar. What is inside is acetic acid at 25%....
- **SPOKEN: percent sign (write 'percent')** (#1): ...ite vinegar on your own shelf. That is 5%. Five times weaker. And that one number...
- **SPOKEN: 'psi' (say 'pounds of pressure' or 'pounds per square inch')** (#5): ...In psi, that is 45 to 60. Many American houses...
- **staccato x9** (#2): "It is written down." | "Twelve chapters." | "The problem." | "The old way."
- **staccato x5** (#1): "The Problem." | "The Old Way." | "What You Need." | "When to Stop."
- **staccato x5** (#14): "It is not stronger." | "Warm, fat pours easily." | "A solid." | "Rice."
- **trailing 'Not Y.' beat** (#1): ...t your hand under the rim of your toilet. Not in the water. Just up under the lip, where the small ...
- **trailing 'Not Y.' beat** (#1): ...up of the essence straight into the bowl. Not diluted. You want it at full strength against th...
- **not-X-period beat** (#1): ... of the essence straight into the bowl. Not diluted. You want it at full strength against the ...
- **not-X-period beat** (#4): ...r, the night. None of them fights heat. Not one. Every one of them either keeps heat from ...
- **talks about its own packaging** (#8): ...dred and One Free Repairs, and the free in that title is the repairs, not the download. A hun...
- **talks about its own packaging** (#13): ...rely gets handed down anymore, and free in that title describes the repairs you do yourself, ...
- **SPOKEN, judge: letters 'EPA' (keep only if people say it as letters; otherwise the words)** (#6): ...t 125 to 130 liters of water a day. The EPA puts an American at 82 gallons a day at...
- **SPOKEN, judge: letters 'EPA' (keep only if people say it as letters; otherwise the words)** (#6): ...For a family of four, the EPA's number is more than 300 gallons a day...
- **SPOKEN, judge: letters 'PVC' (keep only if people say it as letters; otherwise the words)** (#3): ...Most drain lines in American houses are PVC, the white plastic, or ABS, the black. ...
- **SPOKEN, judge: letters 'PVC' (keep only if people say it as letters; otherwise the words)** (#3): ..., the white plastic, or ABS, the black. PVC begins to soften somewhere above 140 de...
- **SPOKEN, judge: 'wound' can be said two ways; reword if both fit** (#5): ... tape. Germans use a wisp of hemp fiber wound into the thread and a smear of sealing ...

Note on #2's REPEATED SENTENCE: the mid CTA ends "So. Number three." and the next item opens "Number three. Coffee grounds." The two sentences are separated only by the `===END CTA===` line, which the scanner also skips in an unstripped file, so this finding is not caused by the stripping.

Note on #7's HARD BAN: it is in the end CTA, "if the German house against the American house is a thing you want to keep watching, subscribe to Werner Finkbeiner". This is a subscribe line, not a retention tease, but the scanner's "keep watching" ban does not tell them apart.

Note on "channel promise": the plumbing pack bans `this channel (is for|exists|is all about)`. It fires on the intro line of every script that says "this channel is for" (9 of 14). #2, #3, #5 and #8 say "This is for ..." instead, and #13 says "here the American house gets ...", so none of them trigger it.

## Echo phrases (H18), as listed by the scanner

- #1: number x4: "101" (mentions past the second must add something new)
- #2: phrase x6: "goes in the trash"; phrase x4: "that is the whole"; phrase x3: "one hundred and one"; phrase x3: "moves while it is"
- #3: phrase x3: "one hundred and one"; number x4: "10" (mentions past the second must add something new)
- #4: phrase x3: "of the house and"; phrase x3: "one hundred and one"
- #5: phrase x4: "one hundred and one"; phrase x3: "that is the whole"; number x4: "120" (mentions past the second must add something new)
- #6: none
- #7: phrase x3: "the floor of it"
- #8: number x6: "10" (mentions past the second must add something new); number x4: "72" (mentions past the second must add something new)
- #9: none
- #10: phrase x3: "on a hook inside"; phrase x3: "a hook inside the"; phrase x3: "hook inside the shower"
- #11: phrase x4: "the bottom of the"; phrase x3: "at the bottom of"; phrase x3: "bottom of the bowl"
- #12: none
- #13: phrase x6: "of the overflow tube"; phrase x4: "top of the overflow"
- #14: none
