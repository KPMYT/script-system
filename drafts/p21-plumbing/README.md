# DRAFT: P21, the plumbing rebuild (Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter, Werner Finkbeiner)

Not part of the library yet. Built 2026-11-06 (session 16) from `drafts/lite-roger-the-pipe-guy-DRAFT.md` (the iter-09 winner: 8.0 against the account skills' 6.2, `tests/iterations/iter-09/RESULTS.md`) and the plumbing skills on the account, for the operator to see before anything replaces the library or goes to the account. Laid out exactly as the five skills would be uploaded, on the shape of `drafts/p21-style/`.

## The files

| File | What it is | Replaces |
|---|---|---|
| `plumbing-scripts/SKILL.md` | The steps: inputs, NOT READY, the video type and its model, write, read aloud, check, the output by script type (about 1,000 words) | the account's `plumbing-scripts` (11,394 words, plus `excerpts.md` 11,289, `voice-samples.md` 1,212, `unit-plan-template.md` 884 and 39 model files), and, for these four channels only, `core/workflow.md` sections 2 to 6 and every other core file |
| `plumbing-scripts/check.py` | The hard-rules check, one `CHANNELS` entry per channel (no counts to meet) | the core scanner, the pack's scanner block and the full audit, for these four channels |
| `plumbing-scripts/references/models/` | Seven real on-camera transcripts (R04, R06, R13, R14, R15, R16, R18), one per file, with what to take, what not to take and his signature phrases quoted exactly | the 39 beat maps and labelled scripts, `excerpts.md`, `voice-samples.md` |
| `plumbing-scripts/references/price-guide.md` | The price guide, copied unchanged from the account (identical to the library's) | the same file |
| `roger-the-pipe-guy-persona/SKILL.md` | Roger's one page | the account's profile (1,444 words) and the lite draft |
| `mark-silverbridge-persona/SKILL.md` | Mark's one page | the account's profile (1,366 words) |
| `vintage-pipefitter-persona/SKILL.md` | The Vintage Pipefitter's one page | the account's profile (886 words) |
| `werner-finkbeiner-persona/SKILL.md` | Werner's one page, with "the German way" | the account's profile (3,815 words) |
| `*/personas/books/*-book.md` | Roger's, Mark's and Werner's book files, copied unchanged from the account (identical to `personas/books/`) | the same files |
| `tests/iterations/iter-16/brief-*.txt` | Four TEST briefs (below) | nothing |

**What does not change:** `script-writer` (START, the channel question) and every other niche's skills.

**Page lengths** (body words, frontmatter and table rules left out): pack 998; Roger 1,663; Mark 1,694; Vintage 1,514; Werner 1,875. The brief asked about 900 to 1,300 for a page; these run longer, close to the style pages (Scarlett 1,764, Diane 1,947, counted the same way), because each carries its channel's safety lines, book facts and ending. Werner's carries "the German way". The operator may want them cut further.

## The models picked (real people only, operator's rule)

From the account pack's `references/models/INDEX.md` and `studies/plumbing/data/competitors/`. Only presenters on camera (`meta.md` format line "FACE"). Got2Learn (R01-R03, R08-R12) is left out: `meta.md` logs it FACELESS (voice-over over hands). Arrow Pest Service (R07, R19, R20) is left out: a two-person on-site dialogue that leans on the footage, and pest control. R17 (Silver Cymbal, generator) is left out: its transcript has no punctuation (0 full stops). R21 has no transcript on disk. S files (our channels, TheCheapFix) are AI channels and never used. Roger Wakefield's other uploads on disk are trade-career talks, a reaction video (two voices mixed) and an insurance video at 0.61x his normal.

| Video type | Model | Why (reading) |
|---|---|---|
| How-to, correct way; seasonal or emergency (closest) | R13 Roger Wakefield, flushing a water heater (2,271 words, 47.41x) | the iter-09 winner's model; the honest limit first, the job in its order, the escalation when it fails |
| The correct way; mistakes (second) | R14 Roger Wakefield, soldering (2,295 words, 37.52x) | a rule line at the top of each step; the number-one mistake named at its own step |
| Head-to-head verdict | R04 Roger Wakefield, tank vs tankless (1,575 words, 39.66x) | the painful part first, the payback, the verdict split by household |
| Product swap | R18 Silver Cymbal, compression valves (1,570 words, 15.00x) | the popular shortcut judged fairly before it's beaten |
| Hidden cause; banned or code explainer (closest) | R06 Silver Cymbal, LED bulbs (747 words, 18.77x) | the hidden cause by 0:38, then the viewer checking their own house |
| Never-do, mistakes and "N things" lists | R16 Silver Cymbal, string trimmer hacks (747 words, 25.22x) | each item opens on a moment lived, then the cause, the fix, the result |
| Single-product fix | R15 Silver Cymbal, windshield (912 words, 151.07x) | the failed attempt, the product early, every dose with its reason |

Figures are from each `meta.md` (views as of 2026-10-20), read 2026-11-06. Every signature phrase was checked by script as an exact match against its transcript (timestamps removed, lines joined). **The gap:** no real on-camera plumbing list video is on disk, so the three list types share R16, a short lawn video. On-camera list videos do exist in the HVAC study (for example `studies/hvac/data/hvac-guide-for-homeowners/Unx9Ze10N98/`, "5 BIGGEST Winter HVAC Mistakes Homeowners Don't Know!", 190.77x, and `the-diy-hvac-guy/SkLMRM9NnBY/`, "3 Things HVAC Contractors Don't Want You To Know About.", 68.32x). Not used: the task named the plumbing study only. The operator's call.

## What changed from the tested one-page draft (iter-09's findings)

| iter-09 finding (run B, the winner) | Fix on the page |
|---|---|
| Level three said "start with levels one and two", then "before you touch a thing": on a blocked main line the viewer would plunge into the backup | Every page: "When nothing goes down, the test for the main line comes first: if it's the main, stop running water and call. Never send them back to the plunger first." The check fails a main-line backup with no stop-water line |
| "Here's what you do" three times | "never say a stock phrase twice"; the check fails a second use |
| The book break ran long and read a six-part list aloud | "One benefit, never a list"; lists of three at most; "back into the video with a real line, not 'back to the drain'" |
| The opening's price line led nowhere | "Prices belong to the steps; the opening needs one at most, often none" |
| Few reward beats | "End each step on the win" |
| Run A: the chemical warning after the plunger and snake | "the chemical check comes before any plunger or snake"; the check fails the order |
| Run A: swipes at plumbers' motives | the villain as two facts side by side, never a motive; the check fails the motive words |

## What changed from the account skills (the newest operator decisions)

Carried, as plain guidance or as a hard rule in the check:
- **The persona facts:** names, the voices and their words a minute (Roger 170, Mark 181, Vintage 190, Werner 181, 2026-10-29), tenures (45, 40, 45, 30; the title's number wins), Mark's and Werner's no contractions, Roger's first-Saturday habit, Werner's three soft details (one per script) and the fixed mentor line, the Vintage Pipefitter's no name, no mentor, no book.
- **Script type:** Roger, Mark, Vintage Classic (no markers; the check fails any); Werner Talking Head (two blocks; the start marker `Werner's 101 Free Repairs`). VO copy for all four (all ElevenLabs).
- **The books and CTAs:** the spoken titles, the true facts, "the book", never "e-book", the link in the description and the QR code every time, the book match claimed only as far as it goes, the mid-video line about a third of the way in and never before the end of item 3 in the shape their hits used (Roger, Mark), Werner's basic 40 to 55 words, the Vintage Pipefitter's one-line subscribe ask at the end.
- **The ending (P5):** the end reminder, then the comment ask with a question about their house and "I read every one." as the last line; no sign-off, recap, subscribe (except Vintage) or next video.
- **The opening:** the point in the first sentence, the product named outright; no tool list and each tool named once; at most one promise and only one the end pays (P18); no time on a promise; no "today we're going to"; no "no plumber needed" when a step ends in a call; the count line naming no single item (P10); the escalation line as an option (P17); the first real step by about 45 seconds.
- **The villain:** the trade's price and silence and the store shelf, two facts side by side, never a motive; disgust at a big price as his opinion (Werner flat).
- **Money (P7):** the brief, then the price guide; always estimates, rounded, never cents except a cost per use; say what moves a range; no guaranteed saving; payback arithmetic holds.
- **Safety:** the five defaults where the brief is silent, every gas-leak step, one line inside the step, every call naming its trigger; the main-line stop.
- **Length:** at least 12 minutes at the real speed; 12 to 20 the sweet spot; never pad; NOT READY only when the brief can't reach it.
- **Bans:** intros, teases, recaps, homework lists, "I tested", "watch me", pointing at the screen, customer stories, named companies run down, hype, the template's stock lines, swearing, jokes, edit notes; Werner's whole list (relatives, the book's stories, arrival, hometown, credentials, German law, comedy German, euros, umlauts).
- **The German way:** every German claim from the brief and hedged, the fix in the American house, up to three German words glossed.

**Dropped (counts and templates only):**
1. The rotation log as an input, and its model, money, promise and comment fields; the "no model twice in the last five scripts" and "name three differences" rules. Replaced by: don't reuse an earlier script's comment question or opening line in this chat.
2. The unit plan template and the planning step.
3. The 39 beat maps, `excerpts.md`, `voice-samples.md`, and the per-type opening orders and first-tip seconds in the video-types table.
4. The number cap: one dollar figure per item, figures on about half the items. Kept in words: "not every step needs a price"; the opening "one at most, often none" (the check reports it, never fails it).
5. "Two or three" promise devices per video, forward lines paid within five minutes, no five minutes without one, no more than two items without a bridge.
6. The item shape (scene, pipe, cost, turn, fix, win) and 100 to 130 words an item.
7. The rates: "but" in every item, a question every two items, an "I" line in most items, the insistence line once, the title's feeling and the villain "every few items". Now "now and then".
8. The words-before-the-first-step figures (130, 135, 140) and the scanner mark at 45 seconds: the check reports the timing only.
9. The money-device menu and its rotation; the benefit-pair rotation in the CTAs.
10. The named list of ten trade terms to explain (the rule stays: explain a trade word the first time), and the standard-kit list.
11. "Most people" once and "not X, it's Y" once (humanizer counts); the persona device "at most twice, under 40 words".
12. The full audit, the originality score and the core scanner.

**Not checked, on the operator's word:** boiling water and dry washing soda ("dont even flag them", 2026-10-21). The pages carry them as defaults; the brief wins.

## The check

`python3 check.py SCRIPT --channel roger|mark|vintage|werner --title "..." --brief BRIEF` (models and the price guide are found next to it). It fails: length under 12 minutes at the channel's speed; markers in a Classic script, or Werner's blocks wrong (two, the printed title, the mentor line word for word, the spoken title, link and QR, 30 to 65 words in the mid block, the comment ask after the end marker); a missing mid book line or end reminder (Roger, Mark) or subscribe line (Vintage); the last line not closing the comment ask with "I read every one"; the bans and the never-twice phrases; contractions (Mark, Werner); the tenure figure, or said twice; Werner's German words over three and personal details over one; the safety requirements (chemical check before the first plunger or snake, the main-line stop, every gas-leak step, never mixing bleach or peroxide, power or gas off before a water-heater job, "no plumber needed" with a call); prices not in the brief or the price guide, with a range required to come from one line of either; cents; figures in a statistic not in the brief; voice symbols, dashes, curly quotes, short units, two numbers side by side, umlauts; sentences over 35 words; lists of more than three in the opening; eight words in a row from a model or a model's signature phrase. INFO lines (never fails): the opening's words and seconds, dollar figures in the opening, the mid book line's place and size, numbers in neither source, the first sentence against the title.

**Runs (2026-11-06):**

| Script | Channel | Result | What it found |
|---|---|---|---|
| `tests/iterations/iter-09/run-B/script.txt` (the winner) | roger | FAIL (2) | no "I read every one" at the end (the operator's P5 ending); "here's what you do" three times (the judge's finding) |
| `tests/iterations/iter-09/run-A/script.txt` | roger | FAIL (2) | "If you take one thing from this whole video"; the chemical check after the plunger step (the judge's safety finding) |
| Mark's `eT-n10P6RsU` captions, paragraphs added | mark | FAIL (7) | the stock priority line; the toilet, showerhead and tally prices outside the price guide (the audit's findings); caption artifacts (`%`, "Q&R") |
| Vintage's `o_4qckQjeYE` captions, paragraphs added | vintage | FAIL (12) | 10.7 minutes; the three item-naming promises; the $2,000 to $5,000 and $13,000 figures (the audit's findings); the snake offered before any chemical warning; caption artifacts |
| Werner's `XQ_VHuIc2eQ` captions, markers added | werner | FAIL (3) | the stock priority line; "doesn't" and "[clears throat]" (the audit calls both caption slips) |

Captions are YouTube's text of the voice, not the scripts, so their symbol and sentence-length fails are the caption system's. Small made-up fixtures also confirmed the gas, mixing, main-line, water-heater, scope, marker, mentor, German-word and personal-detail checks fire.

**False alarms fixed while testing:** (1) the comment ask required a "?", but the pack allows "Tell me..." (run A's "Leave me a comment and tell me what you found... I read every one." failed): now a "?" or "tell me"; (2) the chemical-order check fired on the word "plunger" inside the book line: book paragraphs are now skipped; (3) Werner's "So, four reasons the stopper seizes, then the repair for both kinds, the lift rod and the push button." read as a four-item list: a list now needs four short parts, after a leading "So,"; (4) Mark's book title as captioned with "$10,000" didn't match the spoken title: digits or words now both match; (5) my own Mark and Vintage briefs quoted the published video's wrong figures in their boundary lines, which let those figures pass the price check: the boundaries now describe them in words.

## The test briefs (`tests/iterations/iter-16/`)

| File | Video | Type and model |
|---|---|---|
| `brief-roger.txt` | `AGp_vAn5hqI` "How to Unclog a Drain For Beginners": a copy of `iter-09/brief.txt`, header changed | how-to, R13 |
| `brief-mark.txt` | `eT-n10P6RsU` "These 3 Powders Will Save You HOURS of Scrubbing Toilets, Tubs and Sinks" | single product (three), R15 |
| `brief-vintage.txt` | `o_4qckQjeYE` "8 Things You Should NEVER Pour Down Your Drains" | never-do list, R16 |
| `brief-werner.txt` | `XQ_VHuIc2eQ` "Why Your Sink Stopper Gets Stuck — The $5 Grease Every German Plumber Carries" | hidden cause, R06 |

Each is talking points from the published video's items, with the 2026-11-05 audit's flagged facts corrected, prices only where the video and the price guide agree (or the title gives one), a safety line and, where the channel has a book, the book match checked against the book file.

## Open questions for the operator (not settled here)

1. **"I read every one."** The operator's ending (P5, 2026-10-21; "saying the narrator reads every comment is allowed") is carried and checked. The iter-09 judge called it "an unverifiable claim for a text-to-speech persona", and the style rebuild bans it. Keep it for plumbing?
2. **The mid-video book line on a short list.** "About a third of the way in" and "never before the end of item 3" can't both hold on a four-item list (Mark's audit, 2026-11-05: after item 3 is about 74 percent in). Which wins?
3. **Werner's end block.** Read here as: the one-line book reminder inside the end markers, the comment ask after `===END CTA===` as the last line (the pack's "comment line, last line of the script" with `core/workflow.md` §4's markers). Right?
4. **"Nobody who gets paid for the visit"** is banned as a motive in the check, from the 2026-11-05 audit's reading of the no-motive rule, not from a separate operator decision.
5. **An audit error found:** Werner's audit says "a small water damage job in one room runs about $150 to $500" is "Not in the price guide (measured)". It is: section 7, first row ("about $150 to $500", confirmed). The Werner brief uses it.

## On the operator's yes (not done yet)

1. Archive the current library copy: `plumbing-scripts/`, the four `personas/*.md` profiles and the account's 2026-10-29 copies into `archive/plumbing-pack-2026-10/` (moved, never deleted).
2. Put the new files in their library places; update `tools/build_skills.py`, `tests/run_checks.py` (the plumbing and Werner checks test the old pack), `README.md`, `HANDOFF.md`, `CHANGELOG.md`.
3. Run iter-16: one writer per brief on these pages, one blind judge against the published videos.
4. Build and send five skills: `plumbing-scripts` and the four persona skills (delete the old, upload the new).
