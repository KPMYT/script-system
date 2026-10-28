# 02 Openings and numbers: the style scripts measured

Part 2 of the style comparison (women over 50: hair and fashion), written 2026-10-28 for Scarlet Sterling and Diane de Chambray. It measures the 45 study transcripts in `data/` (Elegántica `X9mj5fEPfVk` and Camino de los Ancianos `SdbAfqmUwJ0` are DROPPED in `inputs/videos.csv` and left out) and our own 38 transcripts in `own-baseline-2026-10/data/`, and sets the groups side by side. It describes and counts; it doesn't recommend. Nothing in `data/`, `notes/`, `comparison/00-measures.md`, `measures.csv` or the library was changed. Helper scripts are in the scratchpad (`analysis02/`), not in the repository.

## How to read this

- **Groups.** *Real* = the 21 videos with a real presenter or real client footage (type `real` in `videos.csv`; this includes Marie-Anne Lecoeur's `ixlexruRC6c`, the original of pair D). *Faceless/AI* = the other 24: faceless narration, AI presenters, the "faceless/AI" pair videos, Ageless Confidence ("not checked") and Ageless Style 50s & 60s ("unclear"). This matches `tools/measure.py` except that `measure.py` files pairs A to C under "pair-winner" and "pair-copy"; here they sit in Faceless/AI and get their own table in section 8. *Scarlet* = 25 videos, *Diane* = 13. Own "top" and "bottom" are the videos the baseline notes cover (top 4 and bottom 3 by views among uploads at least 7 days old, `own-baseline-2026-10/SUMMARY.md`).
- **Multiples (× normal)** are each video against its own channel's normal. Study normals run from about 1 thousand to over 100 thousand views and our normals are 532 (Scarlet) and 607 (Diane), so multiples are compared within a channel or a pair, never as a ranking across groups.
- **Measured vs reading.** Word counts, rates, times and phrase counts are measured by script. Where each hook ends, where each item starts, what counts as a "move", a "story", a "tease" or a "recap" is my reading (one coder), checked against the notes' structure maps and the transcripts. Those cells are marked as reading.
- **Small samples.** 21, 24, 25 and 13 videos; the top/bottom sets are 4 and 3. A difference of one or two videos is noise.

**How things were counted**
- *Words:* tokens holding a letter or digit, with the `[m:ss]` stamp, bracket tags (`[Music]`) and `>>` removed (the round-3 rule). *Minutes:* the `meta.md` duration. *WPM* = words ÷ minutes. These are `measure.py`'s figures and match `measures.csv`.
- *you, I, but:* as `measure.py` (you/your/yours/yourself and contractions; I/me/my/mine/myself and contractions; the word "but"), per 1,000 words.
- *Questions:* in the 73 punctuated transcripts, every "?" (as `measure.py`). The 10 unpunctuated ones (Diana GOSS ×3, Justin Hickox ×2, Alice Luxe ×2, Elegance At 60 `vATkBSPjQmc`, Adore Your Wardrobe, AnniePicks) were hand-counted: a pattern listed every question frame (auxiliary before a pronoun, wh-word before a verb, "what if", "did you know", "have you ever", "what's"), and I kept only questions put to the viewer or voiced for her. Questions to an on-camera client are left out. These counts are marked **h** and are floors. In the punctuated set "?" also counts salon dialogue (the two Rami Jabali consultations hold 28 and 22) and questions inside CTAs.
- *Hook:* every spoken word before the first real item: the first item of the title's list, or for the five non-list videos (two salon consultations, a makeover, a personal story, Summer Beauty's head-shape lesson) the first substantive point. Item one starts at the first line that belongs to it (its heading, or a scene that is clearly item one's own), not at a generic "let's get started". Hook words are counted up to the exact first word of item one; hook seconds are the start of the caption line holding that word. Where a real teaching section (a rule, a test, a mechanism) comes before item one, its start is given separately as "first teaching".
- *Items:* start times set by hand for all 78 list videos, from the notes' segment maps (59 noted videos) and from item headings found in the transcript (the 24 own videos without notes), each checked against the transcript. An item runs to the next item, an interlude (mid-roll CTA, plug, aside) or the close; interludes are cut out and an item interrupted by a mid-roll CTA is joined back up. Boundaries are at caption-line starts, so each item's word count can be off by a line (about 6 words). Units outside the title's list (Chic After 60's five rules and five mistakes around its seven outfits, Justin Hickox's two "special sauces", Diane's three "avoid" frames after her seven, the "granny" retire blocks) are counted as extras and left out of item lengths.
- *Age said:* `measure.py`'s count, then a wider hand-checked count (section 4).
- *Money figures:* each "$", "£", "€" amount, each number followed by dollars, bucks, pounds or euros, and number ranges after a price verb ("runs 50 to 90", "between 120 and 250"); each end of a range counts (as the HVAC and plumbing files). *Brands and stores:* a list of about 125 name patterns built from every notes file's products section plus common US, UK and French chains, matched as whole words and read in context. *Store-type words:* department store, drugstore, pharmacy, consignment, thrift, secondhand, the mall, outlet, high street, online. *Percentages:* a number with % or "percent". *Measurements:* a number with in, inch, mm, cm or feet.
- *Title keywords:* the title's words minus a stop list (articles, pronouns, "women", "look", "make", numbers, "instantly", and similar). Reported: how many are said at least once, all title keywords said per 1,000 words, and the longest run of title words said in order.

**Hand checks**
- *measure.py re-checked on 5 videos* (Marie-Anne Lecoeur `ixlexruRC6c`, Diana GOSS `eKCl-bRx8wg`, Age with Style `6byOPawCepI`, Scarlet `w6w_ktMBHXM`, Diane `ISAL4NBlshQ`), with an independent `sed`/`wc -w`/`grep -o -w` count. Words match exactly on all five (923, 1,483, 2,658, 4,078, 2,082; Diane's meta says 2,087 because it counted tags). "you" (52, 74, 136, 138, 67), "I" (25, 53, 19, 24, 21) and "but" (9, 6, 18, 2, 2) give `measure.py`'s per-1,000 figures to the decimal. "?" counts match (12, unpunctuated, 4, 3, 2). Read in context: six of Marie-Anne Lecoeur's 12 questions are the same item pivot, "So, what can you do instead?"; Age with Style's 4 are one hook question and three item pivots ("So, what's the solution?"); Scarlet's 3 are one CTA line and two self-test questions ("Does it brighten the skin under your chin? Or does it put a shadow there?"); Diane's 2 are pivots ("What does a French woman do instead?"). `measure.py`'s figures stand. One thing it can't do: it leaves the 10 unpunctuated transcripts without a question figure, so its real-side median (3.6) is over 15 videos; with the hand counts added the real median is 2.6.
- *Hooks against the notes:* of the 55 noted videos where the notes give a first-item time for the same item, 54 are within 3 s of the line found here (Rami Jabali `RuyOhWfU-RI`: notes 3:52, the line is 3:57). Of 53 notes' "about N words in" figures, 49 are within 5% of the recount. The four outside: Diana GOSS `eKCl-bRx8wg` 50 → 54; Summer Beauty `UUS1R9oWx4o` 110 → 130; Marie-Anne Lecoeur `n9ICHZq3_tY` 90 → 116 (the notes stop at 0:36, before two "stay to the end" lines; item one starts at 0:45); Age with Style `6byOPawCepI` 230 → 244. Glam Girl Gabi, Chic After 60 `h6Y1RZzOlzg` and two own videos use a different anchor here (the title's first item, not the first teaching) and are compared on the "first teaching" figure instead.
- *Age, money and brands:* every match was read in context; corrections are listed in sections 4 and 5.

---

## 1. Length, pace and voice

Rows by side, highest multiple first. Q = "?" count (h = hand count, a floor).

| Side | Channel | Video | × normal | Words | Min | WPM | you /1k | I /1k | but /1k | Q | Q /1k |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Real | Woman in midlife | `2e50uMLaCtE` | 118.7 | 1,360 | 7.4 | 184 | 16.9 | 92.7 | 2.9 | 9 | 6.6 |
| Real | MAKEOVERGUY | `WgkP3h4QWpg` | 70.4 | 1,292 | 9.4 | 137 | 21.7 | 64.2 | 3.9 | 7 | 5.4 |
| Real | Justin Hickox | `vFul5tvg1Cw` | 63.2 | 2,476 | 10.1 | 245 | 49.3 | 30.7 | 6.9 | 1h | 0.4 |
| Real | Diana GOSS | `eKCl-bRx8wg` | 31.4 | 1,483 | 9.0 | 165 | 49.9 | 35.7 | 4.0 | 2h | 1.4 |
| Real | Justin Hickox | `rU56_ly6l2s` | 29.3 | 3,339 | 14.6 | 228 | 42.8 | 34.7 | 4.2 | 3h | 0.9 |
| Real | MM Personal Styling | `gfbWOw00Y-M` | 28.5 | 5,325 | 30.9 | 173 | 37.8 | 30.6 | 10.1 | 5 | 0.9 |
| Real | Summer Beauty | `UUS1R9oWx4o` | 27.2 | 2,547 | 15.2 | 167 | 60.9 | 15.3 | 3.9 | 0 | 0.0 |
| Real | Diana GOSS | `NMvN5bjcwks` | 23.6 | 1,841 | 11.2 | 164 | 50.0 | 23.4 | 6.5 | 1h | 0.5 |
| Real | Adore Your Wardrobe | `vBsFMkGDbhA` | 16.5 | 1,881 | 11.4 | 165 | 48.9 | 21.8 | 6.4 | 3h | 1.6 |
| Real | Rami Jabali | `qwM0s0Q3Rjw` | 15.6 | 1,759 | 10.0 | 176 | 42.6 | 38.1 | 8.5 | 28 | 15.9 |
| Real | Rami Jabali | `RuyOhWfU-RI` | 14.9 | 1,939 | 11.0 | 176 | 56.7 | 61.9 | 9.3 | 22 | 11.3 |
| Real | Diana GOSS | `9ZNV79Uva3g` | 14.8 | 2,179 | 12.7 | 172 | 39.9 | 10.6 | 8.3 | 1h | 0.5 |
| Real | chery 🍒 | `XCf4o0ZOOiw` | 14.0 | 2,022 | 11.9 | 170 | 55.9 | 18.3 | 7.9 | 1 | 0.5 |
| Real | Glam Girl Gabi | `9LvzTBzXL5k` | 12.4 | 2,067 | 11.3 | 183 | 55.1 | 15.5 | 4.8 | 9 | 4.3 |
| Real | Marie-Anne Lecoeur | `ixlexruRC6c` | 12.4 | 923 | 8.0 | 115 | 56.3 | 27.1 | 9.8 | 12 | 13.0 |
| Real | Tracy Campoli | `NT1mEOX-p7Y` | 10.6 | 5,226 | 25.9 | 202 | 42.1 | 57.4 | 12.4 | 29 | 5.5 |
| Real | Marie-Anne Lecoeur | `MWQ6T1wURJU` | 7.5 | 2,031 | 13.0 | 156 | 27.6 | 22.2 | 9.8 | 6 | 3.0 |
| Real | Marie-Anne Lecoeur | `G-RW7ih19Y4` | 6.5 | 2,195 | 16.5 | 133 | 57.9 | 14.1 | 5.9 | 8 | 3.6 |
| Real | Summer Beauty | `xNuoMiG2kVw` | 5.8 | 2,279 | 13.3 | 171 | 57.9 | 9.2 | 6.6 | 6 | 2.6 |
| Real | Aliceinparis | `fLIVwKa-y3U` | 4.5 | 1,966 | 15.1 | 130 | 11.7 | 8.1 | 5.1 | 0 | 0.0 |
| Real | Marie-Anne Lecoeur | `n9ICHZq3_tY` | 1.6 | 2,170 | 14.3 | 152 | 35.0 | 22.6 | 5.1 | 7 | 3.2 |
| Faceless/AI | AnniePicks | `YLiz8tlx9g4` | 1,325.4 | 1,046 | 6.8 | 155 | 24.9 | 2.9 | 2.9 | 2h | 1.9 |
| Faceless/AI | Alice Luxe | `CkVrghocoPs` | 818.0 | 3,900 | 24.6 | 159 | 62.3 | 1.8 | 5.1 | 2h | 0.5 |
| Faceless/AI | Golden Melanin Lifestyle | `dn3mNRtYTY4` | 518.8 | 2,274 | 15.2 | 149 | 60.2 | 17.1 | 5.7 | 11 | 4.8 |
| Faceless/AI | Glow After 60 | `G5y1gFHWPIA` | 498.5 | 4,768 | 30.5 | 156 | 22.4 | 10.1 | 1.3 | 8 | 1.7 |
| Faceless/AI | Ageless Melanin | `qFLenue5BBI` | 337.6 | 2,241 | 15.9 | 141 | 65.2 | 12.5 | 6.2 | 6 | 2.7 |
| Faceless/AI | Age with Style | `6byOPawCepI` | 291.6 | 2,658 | 16.0 | 166 | 51.2 | 7.2 | 6.8 | 4 | 1.5 |
| Faceless/AI | Elegant After 60 | `XR3IwlcIcCY` | 240.7 | 2,067 | 11.4 | 181 | 46.9 | 10.6 | 5.3 | 9 | 4.3 |
| Faceless/AI | Alice Luxe | `aaDZuD5jIfs` | 216.2 | 3,568 | 22.6 | 158 | 52.7 | 2.8 | 7.6 | 7h | 2.0 |
| Faceless/AI | ChicAfterSixty | `_OQsPYjIfsQ` | 205.6 | 4,424 | 26.6 | 166 | 40.5 | 24.4 | 2.5 | 8 | 1.8 |
| Faceless/AI | Chic Over 60 | `2IkhtemG-MM` | 164.2 | 3,060 | 17.4 | 176 | 46.1 | 3.9 | 5.9 | 16 | 5.2 |
| Faceless/AI | Vivian Sinclair | `2q_6Qf69Ywc` | 140.1 | 2,849 | 17.0 | 168 | 38.6 | 15.1 | 1.1 | 7 | 2.5 |
| Faceless/AI | Ever Chic At 50 | `kKjLX7Q6wc8` | 101.2 | 3,446 | 24.0 | 144 | 55.1 | 1.7 | 5.5 | 15 | 4.3 |
| Faceless/AI | Elegance At 60 | `XByilJlme5Y` | 64.6 | 2,041 | 12.7 | 160 | 50.0 | 14.2 | 5.9 | 6 | 2.9 |
| Faceless/AI | Ageless Style 50s & 60s | `Fs17Qc6l8Ug` | 55.7 | 2,024 | 12.1 | 168 | 76.6 | 22.2 | 9.4 | 3 | 1.5 |
| Faceless/AI | Elegance At 60 | `vATkBSPjQmc` | 53.9 | 1,452 | 10.0 | 146 | 61.3 | 9.6 | 4.1 | 2h | 1.4 |
| Faceless/AI | Rock Your Fashion | `KNwk391XyIY` | 49.0 | 1,995 | 13.2 | 151 | 54.6 | 2.5 | 3.5 | 3 | 1.5 |
| Faceless/AI | French Fashion | `-eTr9aVSWlM` | 32.2 | 2,298 | 14.7 | 156 | 44.8 | 6.5 | 4.8 | 13 | 5.7 |
| Faceless/AI | Chic After 60 | `YeKT0zkdIrw` | 25.9 | 4,084 | 29.8 | 137 | 20.3 | 3.2 | 7.8 | 2 | 0.5 |
| Faceless/AI | Stylish60plus | `8p2y_Yk0pNQ` | 25.5 | 3,738 | 23.4 | 160 | 49.0 | 6.2 | 2.1 | 11 | 2.9 |
| Faceless/AI | Chic After 60 | `h6Y1RZzOlzg` | 14.9 | 2,078 | 13.5 | 154 | 39.5 | 20.2 | 2.4 | 7 | 3.4 |
| Faceless/AI | Trends Spotted | `HG2OJ0O3lxg` | 12.4 | 2,221 | 16.0 | 139 | 31.5 | 2.2 | 1.8 | 2 | 0.9 |
| Faceless/AI | Ageless Confidence | `UTpC6n7KKi0` | 2.6 | 2,481 | 14.6 | 170 | 44.3 | 13.3 | 2.4 | 2 | 0.8 |
| Faceless/AI | Age with Style | `K6N1EFo7oec` | 1.9 | 2,852 | 18.8 | 152 | 31.9 | 4.9 | 1.4 | 6 | 2.1 |
| Faceless/AI | Elegant After 60 | `ZFx3yIrJqO0` | 0.8 | 2,484 | 14.2 | 175 | 45.9 | 5.6 | 4.8 | 9 | 3.6 |

**Group medians** (own channels included for comparison; their per-video rows are in section 7)

| Group | n | Words | Min | WPM | you /1k | I /1k | but /1k | Q /1k | Videos 12 min or longer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Real | 21 | 2,031 | 11.9 | 170 | 48.9 | 23.4 | 6.5 | 2.6 | 10 of 21 |
| Faceless/AI | 24 | 2,482.5 | 16 | 157 | 46.5 | 6.8 | 4.8 | 2 | 21 of 24 |
| Scarlet | 25 | 2,804 | 16.4 | 171 | 33.8 | 4.1 | 1.1 | 0.4 | 25 of 25 |
| Diane | 13 | 2,852 | 16.9 | 170 | 39.9 | 5.6 | 1 | 1.4 | 13 of 13 |

**Measured:**
- **Length.** The real side is the shortest (median 11.9 min, 2,031 words; 10 of 21 run 12 minutes or more). Faceless/AI runs 16.0 min (21 of 24 at 12+). Our two channels sit at 16.4 and 16.9 min, and all 38 are 12:30 or longer; the study's range is 6:46 to 30:51.
- **Pace.** Real and our channels share a median of 170-171 wpm; faceless/AI is slower at 157. The study spread is wide (115 to 245: Marie-Anne Lecoeur's 115 against Justin Hickox's 245 and 228); ours is narrow (149 to 186).
- **"you".** Real 48.9 and faceless/AI 46.5 per 1,000 words; Scarlet 33.8, Diane 39.9. 32 of the 45 study videos are above Diane's median.
- **"I".** Real 23.4 (8.1 to 92.7; the personal story and the makeover are the top two), faceless/AI 6.8, Scarlet 4.1, Diane 5.6. 37 of our 38 are under 10 per 1,000; 2 of the 21 real videos are.
- **"but".** Real 6.5, faceless/AI 4.8, Scarlet 1.1, Diane 1.0. The lowest real video has 2.9 per 1,000; 36 of our 38 are below that, and 34 of 38 are at 2.0 or under (4 of the 24 faceless/AI videos and none of the real ones are).
- **Questions.** Real 2.6 per 1,000 (median, with hand counts), faceless/AI 2.0, Scarlet 0.4, Diane 1.4. 10 of our 38 videos contain no "?" at all; 23 of 38 are under 1 per 1,000, against 8 of 21 real and 4 of 24 faceless/AI.

---

## 2. The hook

### 2.1 Every study hook, measured

Hook w and s = words and seconds before item one (recounted). "First teaching" is given only where a rule, test or mechanism starts before item one. "Notes figure" = the notes' "words in" and first-item time, for the check above. Moves (my reading over a pattern search, see 2.3): **Q** question to the viewer, **F** the feared result, **N** a promise of N items, **A** an authority line (name, channel or credential), **S** a story or scene, **T** a "stay to the end" tease, **C** a comment ask, **G** an age line, **K** a task to do now, **U** a subscribe or like ask.

| Side | Channel | Video | × normal | Hook w | Hook s | % of video | First teaching (w / s) | Moves | Notes figure |
|---|---|---|---:|---:|---:|---:|---|---|---|
| Real | Woman in midlife | `2e50uMLaCtE` | 118.7 | 475 | 2:20 | 32% | – | S | 480 w / 2:20 |
| Real | MAKEOVERGUY | `WgkP3h4QWpg` | 70.4 | 445 | 2:45 | 29% | – | S | 455 w / 2:45 |
| Real | Justin Hickox | `vFul5tvg1Cw` | 63.2 | 908 | 3:28 | 34% | 216 / 0:49 | FN | 910 w / 3:26 |
| Real | Diana GOSS | `eKCl-bRx8wg` | 31.4 | 54 | 0:31 | 6% | – | FN | 50 w / 0:31 |
| Real | Justin Hickox | `rU56_ly6l2s` | 29.3 | 266 | 1:13 | 8% | – | FN | 280 w / 1:13 |
| Real | MM Personal Styling | `gfbWOw00Y-M` | 28.5 | 172 | 0:57 | 3% | – | FNACU | 175 w / 0:59 |
| Real | Summer Beauty | `UUS1R9oWx4o` | 27.2 | 130 | 0:45 | 5% | – | A | 110 w / 0:45 |
| Real | Diana GOSS | `NMvN5bjcwks` | 23.6 | 294 | 1:50 | 16% | – | G | 296 w / 1:50 |
| Real | Adore Your Wardrobe | `vBsFMkGDbhA` | 16.5 | 250 | 1:43 | 15% | – | QA | 250 w / 1:43 |
| Real | Rami Jabali | `qwM0s0Q3Rjw` | 15.6 | 66 | 0:42 | 7% | – | S | – w / 0:41 |
| Real | Rami Jabali | `RuyOhWfU-RI` | 14.9 | 790 | 3:57 | 36% | – | S | 780 w / 3:52 |
| Real | Diana GOSS | `9ZNV79Uva3g` | 14.8 | 298 | 1:44 | 14% | – | QFN | 300 w / 1:44 |
| Real | chery 🍒 | `XCf4o0ZOOiw` | 14.0 | 65 | 0:26 | 4% | – | FNA | 65 w / 0:26 |
| Real | Glam Girl Gabi | `9LvzTBzXL5k` | 12.4 | 749 | 4:16 | 38% | 114 / 0:34 | QFA | 100 w / 0:33 |
| Real | Marie-Anne Lecoeur | `ixlexruRC6c` | 12.4 | 29 | 0:13 | 3% | – | QFN | 29 w / 0:13 |
| Real | Tracy Campoli | `NT1mEOX-p7Y` | 10.6 | 401 | 1:55 | 7% | – | QNAGU | 400 w / 1:55 |
| Real | Marie-Anne Lecoeur | `MWQ6T1wURJU` | 7.5 | 57 | 0:22 | 3% | – | G | 56 w / 0:22 |
| Real | Marie-Anne Lecoeur | `G-RW7ih19Y4` | 6.5 | 78 | 0:36 | 4% | – | A | 78 w / 0:36 |
| Real | Summer Beauty | `xNuoMiG2kVw` | 5.8 | 146 | 0:50 | 6% | – | QFNA | 145 w / 0:50 |
| Real | Aliceinparis | `fLIVwKa-y3U` | 4.5 | 67 | 0:23 | 3% | – |  | 65 w / 0:23 |
| Real | Marie-Anne Lecoeur | `n9ICHZq3_tY` | 1.6 | 116 | 0:45 | 5% | – | NAT | 90 w / 0:44 |
| Faceless/AI | AnniePicks | `YLiz8tlx9g4` | 1,325.4 | 121 | 0:46 | 11% | – | QFNG | 122 w / 0:46 |
| Faceless/AI | Alice Luxe | `CkVrghocoPs` | 818.0 | 350 | 2:08 | 9% | – | QNG | 345 w / 2:08 |
| Faceless/AI | Golden Melanin Lifestyle | `dn3mNRtYTY4` | 518.8 | 169 | 0:59 | 6% | – | QFNSTG | 165 w / 0:59 |
| Faceless/AI | Glow After 60 | `G5y1gFHWPIA` | 498.5 | 323 | 2:02 | 7% | – | FNSTG | 330 w / 2:02 |
| Faceless/AI | Ageless Melanin | `qFLenue5BBI` | 337.6 | 435 | 2:47 | 17% | 262 / 1:34 | FNACGU | 430 w / 1:34 |
| Faceless/AI | Age with Style | `6byOPawCepI` | 291.6 | 244 | 1:24 | 9% | – | QFNASTGU | 230 w / 1:24 |
| Faceless/AI | Elegant After 60 | `XR3IwlcIcCY` | 240.7 | 300 | 1:40 | 15% | – | QFNSTG | 300 w / 1:40 |
| Faceless/AI | Alice Luxe | `aaDZuD5jIfs` | 216.2 | 201 | 1:19 | 6% | – | QTG | 207 w / 1:19 |
| Faceless/AI | ChicAfterSixty | `_OQsPYjIfsQ` | 205.6 | 327 | 1:48 | 7% | – | FNASG | 320 w / 1:48 |
| Faceless/AI | Chic Over 60 | `2IkhtemG-MM` | 164.2 | 222 | 1:16 | 7% | – | QNATG | 220 w / 1:16 |
| Faceless/AI | Vivian Sinclair | `2q_6Qf69Ywc` | 140.1 | 546 | 3:02 | 18% | 371 / 2:03 | FNAGU | 540 w / 3:02 |
| Faceless/AI | Ever Chic At 50 | `kKjLX7Q6wc8` | 101.2 | 668 | 4:35 | 19% | 331 / 2:12 | QFASGU | 660 w / 4:35 |
| Faceless/AI | Elegance At 60 | `XByilJlme5Y` | 64.6 | 258 | 1:37 | 13% | – | QS | 250 w / 1:37 |
| Faceless/AI | Ageless Style 50s & 60s | `Fs17Qc6l8Ug` | 55.7 | 310 | 1:43 | 14% | – | QFNATCGU | 300 w / 1:43 |
| Faceless/AI | Elegance At 60 | `vATkBSPjQmc` | 53.9 | 33 | 0:22 | 4% | – | Q | – w / 0:22 |
| Faceless/AI | Rock Your Fashion | `KNwk391XyIY` | 49.0 | 116 | 0:43 | 5% | – | QNATG | 115 w / 0:43 |
| Faceless/AI | French Fashion | `-eTr9aVSWlM` | 32.2 | 31 | 0:13 | 1% | – | N | – w / 0:11 |
| Faceless/AI | Chic After 60 | `YeKT0zkdIrw` | 25.9 | 469 | 3:07 | 10% | 226 / 1:22 | FNTG | 470 w / 3:07 |
| Faceless/AI | Stylish60plus | `8p2y_Yk0pNQ` | 25.5 | 270 | 1:42 | 7% | – | FNASTGU | 280 w / 1:42 |
| Faceless/AI | Chic After 60 | `h6Y1RZzOlzg` | 14.9 | 459 | 2:54 | 22% | 178 / 1:05 | QFNAG | 165 w / 1:05 |
| Faceless/AI | Trends Spotted | `HG2OJ0O3lxg` | 12.4 | 352 | 2:27 | 15% | – | QNST | 360 w / 2:29 |
| Faceless/AI | Ageless Confidence | `UTpC6n7KKi0` | 2.6 | 364 | 2:08 | 15% | – | FNASTG | 360 w / 2:08 |
| Faceless/AI | Age with Style | `K6N1EFo7oec` | 1.9 | 141 | 0:50 | 4% | – | QFNACG | 140 w / 0:50 |
| Faceless/AI | Elegant After 60 | `ZFx3yIrJqO0` | 0.8 | 187 | 1:05 | 8% | – | QFNAG | 180 w / 1:05 |

**Medians**

| Group | n | Hook words | Hook seconds | Hook as % of runtime | Words to first teaching | Seconds to first teaching | Item one by 30 s | by 60 s | after 2:00 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Real | 21 | 172 | 57 | 7 | 146 | 49 | 4 | 11 | 5 |
| Faceless/AI | 24 | 285 | 101 | 8.7 | 251 | 89 | 2 | 6 | 9 |
| Scarlet | 25 | 275 | 99 | 9.9 | 197 | 69 | 0 | 3 | 6 |
| Diane | 13 | 209 | 71 | 7.7 | 184 | 64 | 0 | 5 | 3 |

**Measured:**
- **Words and time to item one.** Real median 172 words / 57 s; faceless/AI 285 / 1:41; Scarlet 275 / 1:39; Diane 209 / 1:11. Scarlet's hooks sit at the faceless/AI figure; Diane's fall between the two study sides.
- **Item one inside the first minute:** 11 of 21 real, 6 of 24 faceless/AI, 3 of 25 Scarlet, 5 of 13 Diane. Inside 30 s: 4 real (Marie-Anne Lecoeur ×2 at 0:13 and 0:22, chery 0:26, Aliceinparis 0:23), 2 faceless/AI (Elegance At 60 `vATkBSPjQmc` 0:22, French Fashion 0:13), none of ours. Fastest of ours: Scarlet `pgMgC2aGPUw` and Diane `kWzjIzbdB00`, both 0:45-0:46.
- **Longest:** Justin Hickox's bob video (908 words, 3:28: product prep and rough-drying with the sponsored dryer before "step number one"), Rami Jabali `RuyOhWfU-RI` (790 words of client history), Glam Girl Gabi (749 to the first bang type, but teaching from 0:34), Ever Chic At 50 (668 words, 4:35; its comment "5 minutes to get to the actual point? Really?!!" has 34 likes), and Scarlet's concealer video `Z9cXNiZtV8w` (911 words, 5:08: the diagnosis, then the mid-roll book CTA, then rule one).
- **First teaching before item one** appears in 2 real, 5 faceless/AI, 13 Scarlet and 5 Diane videos. Counting to whichever comes first, the medians are real 146 words / 49 s, faceless/AI 251 / 1:29, Scarlet 197 / 1:09, Diane 184 / 1:04.

### 2.2 The hooks quoted in full

Verbatim from the transcripts, tags removed, caption spelling kept ("foreign" is the captions' tag for music).

**Real (5)**
- **Marie-Anne Lecoeur `ixlexruRC6c`** (1,038,117 views, 12.4×; 29 words, 0:13): "Are you ready for little tough love? Today I'm revealing seven things that instantly scream old lady. And what to wear instead to look instantly modern, fabulous, and chic."
- **Diana GOSS `eKCl-bRx8wg`** (1,349,801, 31.4×; 54 words, 0:31): "foreign how old you are 30 40 50 or older the last thing you want to achieve when you get dressed is to look older than you are so today we're talking about five most common mistakes that make you look older and most important how to fix them in just a few seconds"
- **chery `XCf4o0ZOOiw`** (103,785, 14.0×; 65 words, 0:26): "Fine hair doesn't have to age you, but a few small habits make it feel like it does. I see it in my salon all the time. The same mistakes, the same results, and most women have no idea that they're making them. We're covering the seven most common mistakes, and I guarantee you there's something on this list that you're probably doing right now."
- **Summer Beauty `xNuoMiG2kVw`** (263,054, 5.8×; 146 words, 0:50): "Hello beauties. You know gray hair means business when it sets up camp right on your part line in full HD. If you clicked on this video, you're probably thinking about going gray. But every time you imagine it, you either picture yourself looking washed out or 20 years older overnight. I get it. We have been conditioned to believe that gray hair equals giving up. That it means we've stopped trying, stopped caring, or worse, started aging. But what if I told you that going gray can actually be freeing, empowering, and absolutely gorgeous when done the right way? As a hair stylist of 18 years, I am here to show you three smart ways to transition to gray, how to set realistic expectations, and how to avoid the biggest mistakes so you can feel amazing every step of the way. Ready? Let's talk gray."
- **Aliceinparis `fLIVwKa-y3U`** (125,357, 4.5×; 67 words, 0:23): "2026 is already there. And if you are wondering which are the biggest fashion trends, this video is for you. As you may know, French women absolutely love fashion trends that are wearable, timeless, and that give the effortless chic vibe. So, in this video, I'm going to break down the biggest fashion trend for 2026, the ones you are going to see everywhere in Paris."

**Faceless/AI (5)**
- **French Fashion `-eTr9aVSWlM`** (451,523, 32.2×; 31 words, 0:13): "Bonjour. My winter wardrobe fits in one small closet and I'm never cold. 10 types of clothes, not 10 items. So, two sweaters is fine. Get these right and winter's solved."
- **AnniePicks `YLiz8tlx9g4`** (1,013,945, 1,325×; 121 words, 0:46, unpunctuated): "have you ever wondered what makes some women stand out the secret to effortlessly elegant without looking old the secret often lies in the right color combinations in today's video we're going to explore the latest seven stunning color combinations to break out of your wardrobes black white and gray color palette this doesn't mean a top to bottom change just the right combination of colors to transform simple take your outfits to a whole new level of Elegance making you look more classy and expensive ensive without spending too much money inspired by stylish women over 50 these combinations are not only trendy but Timeless proving that great style has no age limit without further Ado let's jump right in"
- **Rock Your Fashion `KNwk391XyIY`** (372,217, 49.0×; 116 words, 0:43): "Are you ready for the 10 petite style secrets that'll change everything for women over 50? Hi and welcome to Rock Your Fashion. If you're 5'4 in or under, this video is going to be a total gamecher. Here's the secret. Being petite after 50 is actually an advantage when you know how to dress for your proportions. Once you understand these 10 secrets, getting dressed becomes effortless and you'll look incredibly sophisticated. In this video, I'm sharing the exact styling techniques that petite women over 50 need to look taller, more polished, and absolutely fabulous. And petite style secret number six, that's the one that uses accessories in a very clever way. Let's get started."
- **Golden Melanin Lifestyle `dn3mNRtYTY4`** (882,034, 519×; 169 words, 0:59): "Let me ask you something, and I want you to be really honest with yourself. How many times have you stood in front of the mirror, put together what you thought was a beautiful outfit, and felt like something was just off? The top was perfect. The pants were tailored to fit your curves just right. But something was pulling the whole look down, and for the life of you, you could not figure out what it was. Well, I am going to tell you exactly what that mystery culprit was. It was your shoes, sis. Today, we are covering 10 shoe mistakes that are quietly aging your look. And more importantly, I am going to tell you exactly what to replace them with, so you can step out with confidence and grace. Now, I need you to stay with me until the very end, because the last mistake on this list is the one almost every woman over 50 is making right now. Let us get into it."
- **Age with Style `6byOPawCepI`** (1,107,951, 292×; 244 words, 1:24): "Have you ever stood in front of the mirror wearing a blouse you thought was flattering, but something just felt off? You couldn't quite put your finger on it, but the outfit didn't feel as polished or youthful as you imagined. My friends, it's usually not you, it's the blouse. And the truth is, many women over 60 are still making the same blouse mistakes that secretly drag down their style. But here's the good news. Once you know what to avoid and what to do instead, blouses can become one of the most flattering, confidence boosting pieces in your wardrobe. Welcome, my beautiful friends, to Age with Style. The place where we celebrate fashion that doesn't just cover you, but truly honors you at every stage of life. This is your space to find clothes that work with you, highlight your best features, and make you feel excited to get dressed again. If you're new here, I am so thrilled you found us. And if you're part of this gorgeous community already, welcome back. It always feels like catching up with stylish friends. Before we dive in, make sure you hit that subscribe button and tap the little bell because I share practical, uplifting style tips that make dressing over 60 fun, inspiring, and confidence boosting. And trust me, you don't want to miss what's coming next. All right, let's get into the seven blouse mistakes women over 60 should stop making."

**Ours: the top 3 and bottom 3** (both channels pooled, by views ÷ own channel normal, uploads at least 7 days old)
- **Top 1, Scarlet `w6w_ktMBHXM`** (39,935 views, 75.1×; 197 words, 0:58): "There's about an inch of skin at your collar bone that decides whether a necklace is flattering you or working against you. Land on it and a plain sweater starts reading like money. Land 2 in lower and that same necklace drags your chin and your jawline down with it. We're taught to shop for the pendant and the stones, but the pendant is almost never the problem. It's the length and how much light the metal hands back to your face. I'm Scarlet Sterling and this channel is for women over 60 who want to look polished and expensive without a bigger budget. Five necklaces today that read expensive on a woman over 60 and three that are aging you. Two of the three that age you are in nearly every jewelry box in the country and one of them you probably wore last week. We'll get to those. The good ones come first because once you know what right looks like, the wrong ones are easy to spot. From a few feet away, the first one does something none of the others quite manage. It softens the line of the jaw without covering anything up."
- **Top 2, Scarlet `yl-Vq9WyLzY`** (12,620, 23.7×; 143 words, 0:49): "You get dressed for a family birthday lunch and you feel good about it. A soft ivory sweater, your favorite gold earrings, your hair behaving for once. Then, someone takes a full-length photo beside the cake and the woman in that picture looks shorter, wider, and older than the one who smiled back from the mirror that morning. So, what changed between the mirror and the camera? Very often, it's the jeans. One particular pair in one particular cut that so many of us own without suspecting a thing. I'm Scarlet Sterling and this channel is for women over 60 who want to look polished and quietly expensive. Mostly with what's already in the closet. Today, I'll show you the jeans mistake that adds years, why it does what it does, and the three pairs that can take those years right back off."
- **Top 3, Scarlet `Z13YRFrGF2w`** (3,924, 7.4×; 463 words, 2:39): "Picture two women sharing a table at Sunday brunch. They have the same silver hair, the same navy sweater, even the same little gold earrings, and they're both wearing glasses. One of them looks rested and quietly expensive, the kind of woman you'd assume has a tailor on speed dial. The other looks tired and a little older than she really is. Neither one spent a penny more than the other. So, why do they look so different from across the room? The answer is sitting on the bridge of each nose. I'm Scarlet Sterling, and this channel is for women over 60 who want to look polished and expensive without spending like it. Today, we're retiring three frames you'll rarely see on a woman who looks wealthy, whether or not she is, and I'll show you what she wears instead, along with the small rules that make choosing your next pair almost easy. Glasses are the one accessory you wear from breakfast to bedtime. They go with you to brunch and to the pharmacy, into every family photo, and onto every video call. They sit right in the middle of your face, closer to your eyes than any earring or necklace will ever get. So, whatever the frame is doing, it's doing it all day long. A necklace that isn't quite working can come off before lunch, but your glasses stay right where they are. After 60, the face changes in soft, quiet ways. Brows grow thinner and lighter. Hair turns silver, or white, or salt and pepper, and skin keeps its beauty while losing a little of the contrast it had at 40. Eyelids lose a bit of their definition, too. A frame that looked crisp on the face you had years ago can start working against the face you have now. Then, there's the way we buy them. Frames tend to get chosen in a hurry, at the end of an appointment, under bright shop lights, while you squint into a little mirror without your own lenses in. So, you reach for the pair that feels safe, and safe usually means black. If there's a drawer in your house holding four pairs of drugstore readers, every one of them black, you're in very good company. The women who always look expensive treat glasses differently. To them, the frame is jewelry, the piece that sits closest to the eyes, and they choose it with the same care they'd give a pair of earrings. There are three small rules behind every frame they pick, and once you know them, the wall of frames at the optician's stops looking like a guessing game. We'll come to those rules a little later, but first, the frames they've let go. So, which one goes first?"
- **Bottom 3, Scarlet `3JBVSs9ETu4`** (157, 0.30×; 320 words, 1:57): "Autumn hands you the most forgiving light of the whole year. It sits low, it goes gold by late afternoon, and it is kind to every face it touches. And every October, I watch women over 60 zip themselves into head-to-toe black and give all of that kindness right back. Black doesn't glow in autumn light. It swallows it, then presses shadows up under the chin and into every hollow it can find. The right colors do the opposite. They catch that low golden light and return it to your skin. Today, I have seven of them for you. I'm Scarlet Sterling, and this channel is for women over 60 who want to look polished, elegant, and quietly expensive, mostly with what's already hanging in the closet. My promise for the next few minutes is simple. By the seventh color, you'll know exactly which shades belong near your face this season, and which ones have been adding years without your permission. Seven colors, then. Among them, the coat shade that will outdress everything else you wear this fall. The one color that can retire black from your wardrobe for good. And a seventh you may have quietly talked yourself out of. Nothing on this list needs a boutique or a bigger budget, and most of it is a rearrangement of hangers you already own. One rule before the first color, because it governs all seven. Color earns its keep near the face. The coat, the scarf, and the knit closest to your jawline do the talking, while the trousers stay dark and quiet underneath. And all seven of today's shades are mid-tones with a soft low-glare finish. That is deliberate. Mid-tones flatter silver and gray hair. They are gentle on mature skin, and they photograph beautifully in dim autumn light, which matters in the season of the family photo. Get the placement right, and simple pieces start doing expensive work."
- **Bottom 2, Diane `bMlBJn27PEU`** (167, 0.28×; 368 words, 2:13): "French women over 60 have a four-second trick that lifts the whole face, and it has nothing to do with skin care. It happens in the hallway, coat on, keys in hand. A square of silk folded twice, tied low and loose. Suddenly, the jaw has a frame, the eyes have light, the whole woman looks finished. Here's the part that stings a little. You probably own that square already, lying flat in a drawer, folded the day you bought it. What you don't own is the knot. Today, I'm handing you seven, and knot number seven, chérie, never touches your neck at all. I'm Diane de Chambray, and this channel is for women over 60 who want to look polished, current, and quietly expensive without spending much. The French way, in other words. So, go get a scarf, any scarf from the drawer, because we're doing every one of these together in front of the mirror. First, the why. Because the why is the piece American women skip. A scarf worn loose at the base of the neck builds a soft frame just under the jawline, and a framed jaw reads as a defined jaw. The eye finishes the line for you. Tie that same scarf high and tight, though, and it does the opposite. The fabric pushes up, the neck shortens, everything bunches toward the chin. Same scarf, opposite face. Low and loose lifts, high and tight squeezes, and every knot today obeys that one law. Now, the scarf itself. The classic is a silk twill square, 90 by 90 cm, about 35 in a side, big enough to fold into almost anything. A silk house in Paris introduced a printed square back in the 1930s, and it has been a Parisian signature ever since. On grandmothers, on bankers, on girls who borrowed it from both. For fall, you want a wool or cashmere length, and for summer, cotton. And the budget news is good. A new silk twill square runs 30 to 80 dollars, but consignment shops and flea markets are full of them for 10 to 25, because somebody's daughter didn't want hers. A cashmere blend? 40 to 80. Less than one forgettable sweater."
- **Bottom 1, Diane `kIjkdHM3a68`** (153, 0.25×; 292 words, 1:35): "You sit down in the chair. The cape snaps shut at your neck. The stylist catches your eye in the mirror and asks what we're doing today. And before you've really thought about it, you hear yourself say the usual, just a trim. Keep it short. An hour later, you walk out with the same neat rounded sprayed shape you walked in with. It's tidy. It's fine. You pay. You thank her. And on the way to the car, you pet the back of your head the way you always do, just to check it's all still there. And that shape is quietly adding years that nobody asked for. Now picture a little salon on a side street in Paris. Same chair, same cape, same mirror. But the first question is different. The stylist wants to know how you wear your hair on a lazy Sunday when nobody's looking and how much time you'd like to spend on it in the morning. The answer she's hoping for is almost known. I'm Diane and this channel is for women over 60 who'd like to borrow the way French women get dressed. Today, five French haircuts that look current grow out gracefully and dry on their own. And at the very end, the four phrases to say in the chair so you actually walk out with one. I'll be honest with you for a second first. A lot of American salons have a default for women past 60 and it's short and set. That's a habit, not a failing. The stylist is cutting what the women before you ask for. So that's what she offers you. The Paris salons I know start from the opposite end with movement and they work backward from there."

(Diane's own top video, `ISAL4NBlshQ`, 6.3×, is fourth on the pooled list; its hook opens "Lay the outfit on the bed before you put it on." and reaches "Rule number one, fit." at 0:58 after 175 words.)

What the six own hooks share, measured: all six give the name and the channel's line ("this channel is for women over 60 who want to look polished…") between 0:20 and 0:55; all six say "over 60" at least once; none asks for a comment or a subscription; five of the six open on a scene or an image in the second or third person. The three top hooks are 143-463 words and the three bottom 292-368; the top three reach item one at 0:49, 0:58 and 2:39, the bottom three at 1:35, 1:57 and 2:13.

### 2.3 The moves, counted per side

Each hook (all words before item one) was searched for each move with a pattern, and every match was read in context; false matches were dropped and missed ones added by reading (examples: "in about 2 seconds flat" is not a feared result; "If you want to look 10 lbs thinner" is a wish, not a fear; Rami Jabali's and MAKEOVERGUY's questions are dialogue with the client, not questions to the viewer; MAKEOVERGUY's "My name is Susan" is the client). "Story or scene" = a narrated moment in two or more sentences (a first-person story, client footage, or a second- or third-person scene such as "Two women sit down at the same cafe table"). "Tease" = an explicit hold or a named later payoff ("stay with me until the very end", "knot number seven, chérie, never touches your neck at all"); a plain "by the end of this video you'll know…" is a promise, not a tease. "Credential" = a job, years, a salon, clients or lived standing ("As a hair stylist of 18 years", "I'm over 60 myself", "most women I know in Paris").

| Move | Real (21) | Faceless/AI (24) | Scarlet (25) | Diane (13) |
|---|---:|---:|---:|---:|
| question | 6 | 16 | 7 | 3 |
| feared result | 9 | 16 | 19 | 7 |
| promise of N items | 10 | 20 | 23 | 12 |
| authority line (name, channel or credential) | 9 | 13 | 25 | 13 |
| …of which a credential | 8 | 5 | 0 | 1 |
| story or scene | 4 | 10 | 15 | 11 |
| "stay to the end" tease | 1 | 12 | 17 | 11 |
| comment ask | 1 | 3 | 0 | 0 |
| age line | 3 | 20 | 25 | 13 |
| a task to do now (extra) | 0 | 0 | 3 | 4 |
| subscribe or like ask (extra) | 2 | 6 | 0 | 0 |
| reassurance line (extra) | 2 | 11 | 2 | 2 |
| median moves per hook (the 8 asked) | 2 | 5 | 5 | 6 |

**Measured:**
- **The age line** is in 3 of 21 real hooks, 20 of 24 faceless/AI and all 38 of ours.
- **Authority:** every one of our 38 hooks names the presenter and the channel; 1 of the 38 carries a credential (Diane `z6Ngr5oSjlw`, "most women I know in Paris"). Real hooks: 9 of 21 carry an authority line, 8 of them a credential ("I see it in my salon all the time"; "As a hair stylist of 18 years"; "as a professionally trained stylist"). Faceless/AI: 13 of 24, 5 with a credential ("40 years beside a fitting room mirror", "I've worked with hundreds of women over 50").
- **The tease:** 1 of 21 real hooks (Marie-Anne Lecoeur `n9ICHZq3_tY`, "Stay to the end for the French staple that everybody gets wrong"), 12 of 24 faceless/AI, 17 of 25 Scarlet, 11 of 13 Diane.
- **Story or scene:** real 4 of 21, and all four are client footage or a personal story with no list (the two consultations, the makeover, "I can't believe I did it"). Faceless/AI 10 of 24, mostly the mirror moment ("Have you ever stood in front of the mirror wearing a blouse…"). Scarlet 15 of 25, Diane 11 of 13.
- **Question to the viewer:** real 6 of 21, faceless/AI 16 of 24, Scarlet 7 of 25, Diane 3 of 13.
- **Comment and subscribe asks before item one:** comment asks in 1 real (MM Personal Styling) and 3 faceless/AI hooks (Ageless Melanin, Age with Style's copy `K6N1EFo7oec` "Where in the world are you watching from today? Drop a quick comment below.", Ageless Style); subscribe or like asks in 2 real and 6 faceless/AI. None in our 38: both channels hold the first CTA to the mid-roll book block.
- **A task to do now** (not in the asked list, counted because it only appears on our side): 3 Scarlet ("Go and get the pair you wear most"; "Before anything else, try something with me"; "Tomorrow morning… stand by a window") and 4 Diane ("Lay the outfit on the bed"; "Go and find the last photograph anybody took of you"; "go get a scarf"; "try a little experiment"). None in the study.
- **How many moves per hook** (of the eight asked): median 2 real, 5 faceless/AI, 5 Scarlet, 6 Diane. The three most-viewed real videos carry one to three: Justin Hickox's bob (3.2M views) F N, MAKEOVERGUY (2.4M) S, Glam Girl Gabi (1.9M) Q F A. Ageless Style, pair D's copy, carries all eight.

---

## 3. Items

### 3.1 Per list video

Words per item in spoken order are in the scratchpad (`rows.json`); here shortest / median / longest. "Median s" = the median item's words at the video's pace. Heading (my reading of how items are introduced): **N** numbered ("Mistake number one", "Secret number five", "Number one, …"), **O** ordinal or "next" sentence ("The first thing that scream old lady…", "The next styling mistake that I see a lot of is…", "The second shade is for lunch with friends"), **T** topic or name only ("Wearing your hair too long.", "Curtain bangs."). "Explicit swap label" = items holding a swap word or frame (instead, swap, the fix, the solution, alternative, "what can you do", "the French answer", choose, try, opt for, replace, look for, ask for, pro tip).

| Side | Channel | Video | Items | Words per item: shortest / median / longest | Median s | Heading | Explicit swap label | Extras |
|---|---|---|---:|---|---:|---|---|---:|
| Real | Woman in midlife | `2e50uMLaCtE` | not a list | – | – | – | – | – |
| Real | MAKEOVERGUY | `WgkP3h4QWpg` | not a list | – | – | – | – | – |
| Real | Justin Hickox | `vFul5tvg1Cw` | 5 | 171 / 225 / 368 | 55 | N | 2 of 5 | 0 |
| Real | Diana GOSS | `eKCl-bRx8wg` | 5 | 195 / 221 / 267 | 80 | O | 4 of 5 (mistake list) | 0 |
| Real | Justin Hickox | `rU56_ly6l2s` | 5 | 306 / 419 / 633 | 110 | N | 1 of 5 | 2 |
| Real | MM Personal Styling | `gfbWOw00Y-M` | 10 | 297 / 466 / 819 | 161 | O | 6 of 10 (mistake list) | 0 |
| Real | Summer Beauty | `UUS1R9oWx4o` | not a list | – | – | – | – | – |
| Real | Diana GOSS | `NMvN5bjcwks` | 5 | 171 / 322 / 411 | 118 | T | 4 of 5 | 0 |
| Real | Adore Your Wardrobe | `vBsFMkGDbhA` | 6 | 128 / 255 / 294 | 93 | O | 5 of 6 | 0 |
| Real | Rami Jabali | `qwM0s0Q3Rjw` | not a list | – | – | – | – | – |
| Real | Rami Jabali | `RuyOhWfU-RI` | not a list | – | – | – | – | – |
| Real | Diana GOSS | `9ZNV79Uva3g` | 5 | 170 / 248 / 833 | 87 | O | 3 of 5 | 0 |
| Real | chery 🍒 | `XCf4o0ZOOiw` | 7 | 122 / 270 / 497 | 95 | T | 3 of 7 (mistake list) | 0 |
| Real | Glam Girl Gabi | `9LvzTBzXL5k` | 4 | 190 / 228 / 255 | 75 | T | 0 of 4 | 0 |
| Real | Marie-Anne Lecoeur | `ixlexruRC6c` | 7 | 80 / 127 / 167 | 66 | O | 6 of 7 (mistake list) | 0 |
| Real | Tracy Campoli | `NT1mEOX-p7Y` | 10 | 168 / 238 / 393 | 71 | N | 2 of 10 | 0 |
| Real | Marie-Anne Lecoeur | `MWQ6T1wURJU` | 7 | 71 / 294 / 468 | 113 | O | 4 of 7 (mistake list) | 0 |
| Real | Marie-Anne Lecoeur | `G-RW7ih19Y4` | 8 | 155 / 265 / 399 | 120 | O | 6 of 8 | 0 |
| Real | Summer Beauty | `xNuoMiG2kVw` | 3 | 285 / 577 / 1145 | 202 | N | 2 of 3 | 0 |
| Real | Aliceinparis | `fLIVwKa-y3U` | 10 | 77 / 136 / 170 | 63 | O | 3 of 10 | 0 |
| Real | Marie-Anne Lecoeur | `n9ICHZq3_tY` | 10 | 86 / 154 / 495 | 61 | O | 4 of 10 | 0 |
| Faceless/AI | AnniePicks | `YLiz8tlx9g4` | 7 | 113 / 120 / 149 | 46 | O | 3 of 7 | 0 |
| Faceless/AI | Alice Luxe | `CkVrghocoPs` | 7 | 378 / 469 / 724 | 177 | O | 7 of 7 (mistake list) | 0 |
| Faceless/AI | Golden Melanin Lifestyle | `dn3mNRtYTY4` | 10 | 144 / 179 / 252 | 72 | N | 9 of 10 (mistake list) | 0 |
| Faceless/AI | Glow After 60 | `G5y1gFHWPIA` | 7 | 430 / 542 / 693 | 208 | T | 6 of 7 | 0 |
| Faceless/AI | Ageless Melanin | `qFLenue5BBI` | 8 | 99 / 138 / 202 | 59 | N | 2 of 8 | 0 |
| Faceless/AI | Age with Style | `6byOPawCepI` | 7 | 267 / 291 / 337 | 105 | N | 7 of 7 (mistake list) | 0 |
| Faceless/AI | Elegant After 60 | `XR3IwlcIcCY` | 3 | 255 / 422 / 434 | 140 | N | 2 of 3 | 0 |
| Faceless/AI | Alice Luxe | `aaDZuD5jIfs` | 8 | 370 / 406 / 496 | 154 | T | 2 of 8 | 0 |
| Faceless/AI | ChicAfterSixty | `_OQsPYjIfsQ` | 5 | 394 / 493 / 851 | 178 | O | 4 of 5 (mistake list) | 0 |
| Faceless/AI | Chic Over 60 | `2IkhtemG-MM` | 10 | 225 / 250 / 306 | 85 | N | 8 of 10 (mistake list) | 0 |
| Faceless/AI | Vivian Sinclair | `2q_6Qf69Ywc` | 5 | 212 / 230 / 261 | 82 | N | 3 of 5 | 0 |
| Faceless/AI | Ever Chic At 50 | `kKjLX7Q6wc8` | 7 | 241 / 333 / 454 | 139 | N | 7 of 7 (mistake list) | 0 |
| Faceless/AI | Elegance At 60 | `XByilJlme5Y` | 5 | 115 / 248 / 375 | 93 | T | 5 of 5 (mistake list) | 0 |
| Faceless/AI | Ageless Style 50s & 60s | `Fs17Qc6l8Ug` | 7 | 166 / 187 / 272 | 67 | O | 7 of 7 (mistake list) | 0 |
| Faceless/AI | Elegance At 60 | `vATkBSPjQmc` | 4 | 224 / 314 / 432 | 129 | T | 2 of 4 (mistake list) | 0 |
| Faceless/AI | Rock Your Fashion | `KNwk391XyIY` | 10 | 147 / 174 / 199 | 69 | N | 5 of 10 | 0 |
| Faceless/AI | French Fashion | `-eTr9aVSWlM` | 10 | 193 / 222 / 260 | 85 | T | 8 of 10 | 0 |
| Faceless/AI | Chic After 60 | `YeKT0zkdIrw` | 8 | 214 / 436 / 450 | 191 | O | 2 of 8 | 0 |
| Faceless/AI | Stylish60plus | `8p2y_Yk0pNQ` | 7 | 297 / 368 / 477 | 138 | N | 5 of 7 | 0 |
| Faceless/AI | Chic After 60 | `h6Y1RZzOlzg` | 7 | 121 / 147 / 166 | 57 | N | 6 of 7 | 10 |
| Faceless/AI | Trends Spotted | `HG2OJ0O3lxg` | 5 | 214 / 307 / 355 | 133 | N | 1 of 5 | 0 |
| Faceless/AI | Ageless Confidence | `UTpC6n7KKi0` | 5 | 202 / 238 / 250 | 84 | N | 4 of 5 | 0 |
| Faceless/AI | Age with Style | `K6N1EFo7oec` | 7 | 329 / 349 / 393 | 138 | N | 7 of 7 (mistake list) | 0 |
| Faceless/AI | Elegant After 60 | `ZFx3yIrJqO0` | 8 | 220 / 272 / 280 | 93 | N | 6 of 8 | 0 |

### 3.2 Medians and shapes

| Group | List videos | Items per video (median, range) | Median of video medians (words) | All items pooled: median (n) | Items under 150 words | over 400 | Heading N / O / T | Explicit swap label, all items | …mistake/avoid lists |
|---|---:|---|---:|---|---:|---:|---|---|---|
| Real | 16 | 6.5 (3-10) | 251.5 | 241 (107) | 22 | 18 | 4 / 9 / 3 | 55 of 107 | 23 of 36 |
| Faceless/AI | 24 | 7 (3-10) | 281.2 | 258 (167) | 20 | 35 | 14 / 5 / 5 | 118 of 167 | 63 of 69 |
| Scarlet | 25 | 7 (3-10) | 269.5 | 266 (169) | 7 | 15 | 8 / 16 / 1 | 125 of 169 | 29 of 32 |
| Diane | 13 | 6 (3-10) | 283 | 285 (83) | 0 | 18 | 13 / 0 / 0 | 60 of 83 | 11 of 17 |

**Measured:**
- **Items per video:** median 6.5 real, 7 faceless/AI, 7 Scarlet, 6 Diane; every group runs 3 to 10.
- **Words per item:** pooled medians 241 (real), 258 (faceless/AI), 266 (Scarlet), 285 (Diane). Short items are a real-side feature: 22 of 107 real items are under 150 words (Marie-Anne Lecoeur's seven "old lady" items run 80-167; Aliceinparis's trends 77-170), against 20 of 167 faceless/AI, 7 of 169 Scarlet and none of Diane's 83. Diane's shortest item is 150 words; 18 of her 83 are over 400.
- **Even vs uneven:** faceless/AI lists are the most even (Age with Style's winner 267-337, AnniePicks 113-149, Rock Your Fashion 147-199, Elegant After 60's copy 220-280). Real lists balloon on one item (Diana GOSS's fit item 833 against 170-280; Summer Beauty's chemical transition 1,145 against 285 and 577; Marie-Anne Lecoeur's own shirt line 495 against 86-284). Ours: Diane's `41ezk-kRd7Y` (three necklaces, median 705) and `jPoeJlLO2_w` (489) and Scarlet's `Z9cXNiZtV8w` (three rules, median 506) carry the longest units.
- **Share of the transcript inside the items:** median 81% real, 79% faceless/AI, 70% Scarlet, 69% Diane (ranges 44-96, 41-96, 41-83, 52-85). The rest is hook, interludes, extras and close; on our side the mid-roll book block (about 150-235 words in each noted video) is one of the interludes.
- **Headings:** real lists lean on ordinal and "next" sentences (9 of 16); faceless/AI lean on numbers (14 of 24); Diane numbers every item in all 13 ("Number one, …", "Knot number one", "French bob number one"); Scarlet mostly uses ordinal sentences (16 of 25: "The first cut is…", "The second shade is…") and numbers in 8.
- **"Do this instead":** in the mistake or avoid lists (21 study and own videos marked in the tables), an explicit swap label appears in 23 of 36 real items, 63 of 69 faceless/AI, 29 of 32 Scarlet and 11 of 17 Diane. Read in full, the items without a label nearly all still name a replacement in plain words: "put a belt on or buy or wear a style that has a nipped in waistline" (Marie-Anne Lecoeur `MWQ6T1wURJU`, item 2), "Trade the lacquer for a flexible hold spray" (Scarlet `EB4Vwf5G0QE`, item 5), "Usually a shorter cut, just a few inches off, is all you need" (Marie-Anne Lecoeur `ixlexruRC6c`, the hair item). Of 28 unlabelled mistake or avoid items read in full (study and own), all but one name a replacement or a rule to follow (Golden Melanin's worn-out shoes: "Invest in quality, and then take care of what you have."); the exception is Diane's bob-to-avoid number four in `qmYPg0L3qZU`, whose matched lines are a photo test ("Pull up a recent photo of yourself and ask what you notice first."). In the positive lists (colours, cuts, pieces) the item is the "do", and the label rate is lower everywhere (real 32 of 71, faceless/AI 55 of 98).

### 3.3 How items open and close

**Recurring formulas, counted** (uses per 1,000 words, each group pooled; videos using the phrase at least once)

| Phrase | Real | Faceless/AI | Scarlet | Diane |
|---|---|---|---|---|
| instead | 0.68 (14 of 21) | 1.76 (20 of 24) | 1.11 (23 of 25) | 1.44 (13 of 13) |
| swap | 0.21 (3 of 21) | 0.21 (7 of 24) | 0.83 (18 of 25) | 0.03 (1 of 13) |
| "solution" | 0.06 (2 of 21) | 0.24 (7 of 24) | 0.00 (0 of 25) | 0.00 (0 of 13) |
| "what can you do (instead)" | 0.12 (1 of 21) | 0.00 (0 of 24) | 0.00 (0 of 25) | 0.00 (0 of 13) |
| "(here's) what I see" | 0.00 (0 of 21) | 0.00 (0 of 24) | 0.00 (0 of 25) | 0.36 (7 of 13) |
| "the French answer / fix / way / version" | 0.02 (1 of 21) | 0.02 (1 of 24) | 0.00 (0 of 25) | 1.38 (13 of 13) |
| "picture" / "imagine" | 0.10 (3 of 21) | 0.42 (6 of 24) | 0.91 (23 of 25) | 0.69 (10 of 13) |
| "try this" / "test" | 0.21 (5 of 21) | 0.30 (12 of 24) | 0.27 (11 of 25) | 1.44 (13 of 13) |
| "the next" | 0.70 (11 of 21) | 0.53 (19 of 24) | 0.30 (14 of 25) | 0.62 (10 of 13) |
| "pro tip" | 0.19 (3 of 21) | 0.00 (0 of 24) | 0.00 (0 of 25) | 0.00 (0 of 13) |
| "the good news" | 0.02 (1 of 21) | 0.11 (5 of 24) | 0.01 (1 of 25) | 0.05 (2 of 13) |

**Patterns, verbatim (quotes from the transcripts):**
- *Real, the stylist's turn:* Marie-Anne Lecoeur opens each item "The next thing that screams old lady is…" and pivots on a question, "So, what can you do instead?" (six times in `ixlexruRC6c`; she is the only one in the study to use that phrase), then "My pro tip is…". In `MWQ6T1wURJU`: "Our next fashion mistake that many women over 50 make with their dresses is to wear the wrong shoes or unflattering shoes." MM Personal Styling: "So the next styling mistake that I see a lot of is…". Justin Hickox: "this leads us into step number one", "which takes us into number four". Aliceinparis repeats one formula ten times: "And the next best fashion trends 2026 you will see everywhere in Paris is…". chery heads each item with the mistake alone ("Wearing your hair too long.") and closes on a bridge ("which brings me to the next mistake").
- *Faceless/AI, numbered and labelled:* "Now, mistake one, choosing blouses that are too baggy." then "So, what's the solution?" and a one-line rule, "Your blouse should frame you, not drown you." (Age with Style's winner). The same channel's re-upload: "Mistake number one, the too boxy blouse." with "The elegant alternative". Golden Melanin: "Mistake number one, clear plastic heels." and "What you wear instead". Ageless Style: "The first thing, the oversized dress." then "Here's the problem" and "The swap". Several close on a question or line that sells the next item: "But what if you want to look like you just walked out of a high-end jewelry vault?" (Elegant After 60 `ZFx3yIrJqO0`); "the next piece solves a problem every woman over 50 knows well" (French Fashion); "But, the next cut is the one most women get wrong and the reason is a single word" (Stylish60plus).
- *Diane, one fixed shape:* "Number one, …" → "Here's what I see" (in 7 of 13) → "The French answer" (the French answer/fix/way/version in all 13, 1.38 per 1,000 words against 0.02 in the study) → "Picture it" → a test ("Try this tomorrow morning", "Your test today"; "try this" or "test" in all 13, 1.44 per 1,000 against 0.21-0.30 in the study) → an aphorism ("A brooch is bought, a rosette is made"; "A bob doesn't need rollers. It needs a good edge.").
- *Scarlet, scene and verdict:* items often open on a scene and only then name the unit ("So, picture the first properly cold Saturday of the season… That coat is the first color, camel"; "From a few feet away, the first one does something none of the others quite manage."), carry "picture"/"imagine" in 23 of 25 videos (0.91 per 1,000 against 0.10 real), use "swap" in 18 of 25 (0.83 per 1,000; real 0.21), and close on a short verdict ("Simple, warm, and impossible to argue with."; "Verdict on both. Simple, warm, finished.") or a forward line ("Pressed clothes look cared for. The next habit makes your whole closet look like one person chose it on purpose.").
- *"The next"* as a bridge: real 0.70, faceless/AI 0.53, Diane 0.62, Scarlet 0.30 per 1,000.

---

## 4. Age said in speech

`measure.py` counts "over/after/at/past/in your" + 40-80 and four peer phrases. The hand check widened it (numbers after beyond, turning, "60 plus", "our 60s", "in their 60s"; peer phrases "at our age", "at my age", "as we age", "as we get older", "mature skin/face/lips") and read every number match and all 73 peer matches in context. Kept: real ages in other frames ("the shades that worked at 40 can start arguing with you at 65"). Dropped: 9 fashion decades ("retro 50s looking silhouette", "'70s patchwork", "'70s boots"). Left in but flagged: 11 spoken channel names that carry an age ("welcome to Ever Chic at 50", "This is Elegant After 60").

| Group | measure.py age (median per video) | Hand-check count: age numbers + peer phrases (median) | per 1,000 words (median) | Videos with none | First age line (median s, where said) | Videos with an "our age" / "my age" phrase |
|---|---:|---:|---:|---:|---:|---:|
| Real | 0 | 0 | 0 | 11 | 44 | 2 |
| Faceless/AI | 6 | 7 | 2.40 | 2 | 18.5 | 3 |
| Scarlet | 2 | 3 | 1.20 | 0 | 35 | 1 |
| Diane | 4 | 4 | 1.40 | 0 | 31 | 0 |

**Measured:**
- **Real:** median 0 per video; 11 of 21 say no age at all. The exception is Marie-Anne Lecoeur's summer-dress video, 14 (title "…Over 50: Fashion Mistakes Women Over 50 Make…"); next are chery and Tracy Campoli with 3 each ("over 40" ×3 in Tracy's).
- **Faceless/AI:** median 7 per video (2.4 per 1,000 words); 2 of 24 say none (both Elegance At 60). Top: Ever Chic At 50 22 ("over 60" ×12), Rock Your Fashion 21 ("over 50" ×15, "women our age" ×3), Chic After 60's colour video 15, Age with Style's winner 11 against 3 in its re-upload.
- **Ours:** every video says it; median 3 (Scarlet, 1.2 per 1,000) and 4 (Diane, 1.4). Range 1-7 and 2-8.
- **Which phrases:** across all 83 videos, "over 60" 126, "after 60" 63, "over 50" 44, then "mature skin" 22, "as we age" 17, "as we get older" 10. "Women our age" is said 3 times in the whole corpus, all in Rock Your Fashion; "at our age" and "at my age" twice each.
- **When:** median first age line at 0:44 in the real videos that say one, 0:18 faceless/AI, 0:35 Scarlet, 0:31 Diane.

---

## 5. Numbers and money

| Group | Money figures /1k | Videos with any money figure | Brand or store names /1k | Videos naming any brand | Distinct brands per video (median, max) | Store-type words /1k | Percentages /1k | Measurements /1k |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| Real | 0.14 | 3 of 21 | 1.74 | 13 of 21 | 1, 18 | 0.04 | 0.37 (7) | 0.23 (6) |
| Faceless/AI | 0.15 | 2 of 24 | 0.82 | 6 of 24 | 0, 15 | 0.15 | 0.12 (5) | 0.29 (8) |
| Scarlet | 1.30 | 21 of 25 | 0.00 | 0 of 25 | 0, 0 | 0.31 | 0.07 (2) | 0.50 (11) |
| Diane | 1.59 | 13 of 13 | 0.03 | 1 of 13 | 0, 1 | 0.31 | 0.13 (1) | 0.33 (8) |

**Measured:**
- **Prices are an own-channel feature.** Our channels say money figures in 34 of 38 videos (1.30 and 1.59 per 1,000 words, pooled); the study does in 5 of 45 (0.14 real, 0.15 faceless/AI): MM Personal Styling ("$29.99" H&M boots, a device "about £105"), Justin Hickox (a "$13 off" code), Tracy Campoli ("I think this thing costs $15", jeans "usually about $50 a pair", "$5 off"), Glow After 60 (six "under $X" prices by budget) and Trends Spotted ("a €15 top and a €500 top"). Ours are mostly ranges: "A ponte blazer runs 50 to 90 dollars" (Diane `ISAL4NBlshQ`), "independent optician… between 150 and 400 dollars" (Scarlet `Z13YRFrGF2w`).
- **Brands are the other way round.** 13 of 21 real videos name a brand or store (1.74 per 1,000): Tracy Campoli names 18 (Uniqlo, H&M, Quince, Zara, Aritzia, J.Crew, The RealReal, Chanel and more), MM Personal Styling 9, Marie-Anne Lecoeur's French-wardrobe video 9 (several as captioned, "Bato", "V West", "armor looks"). Faceless/AI: 6 of 24 (0.82), of which Glow After 60 alone names 15 chains (ASOS, Chico's, Eileen Fisher, Talbots, J. Jill, Marks & Spencer…) and the rest one to three as comparisons ("like you walked right out of a Ralph Lauren catalog"). Ours: one brand in 38 videos (Warby Parker, Diane `Ky2QiqNLd5I`); otherwise store types ("at the drugstore", "consignment shops", "the mall"), 0.31 per 1,000 against 0.04 and 0.15.
- **Sponsors** are spoken only on the real side: the Laifen dryer in both Justin Hickox videos (captioned "lifean", "liyen", "life and Swift"), Lumineux in Tracy Campoli, Ginger Berry pearls in Aliceinparis.
- **Percentages and measurements** are rare everywhere (percentages in 7 real, 5 faceless/AI, 2 Scarlet, 1 Diane video; measurements in 6, 8, 11 and 8). Examples: "at least 50% wool and 70 to 90% is even better" (French Fashion); "Wet hair can stretch up to 50% beyond its normal length before it snaps." (Ageless Confidence); "Number one is pearls worn at 16 to 18 in" (Scarlet).
- **Corrections from reading:** "£10 thinner for sure" in Marie-Anne Lecoeur's slimming video is the captions' rendering of "10 lbs" (dropped); "any old navy bag" in MM Personal Styling is a colour, not the store (dropped); MAKEOVERGUY's "for 37 and 1" (the captions' rendering of a 37-and-a-half-year marriage) is not money (dropped). The money count is a floor on our side: a hand read of six own videos against their notes found one missed figure in three of them (Scarlet `w6w_ktMBHXM` "30 to 80" for a gold-filled chain; `bkUBVNvN4NY` "eight to $14" counted as one; `yl-Vq9WyLzY` premium denim "start around 150"), so our true rate is about 10-20% higher. The study counts held on the four checked (MM, Tracy Campoli, Glow After 60, Trends Spotted).

---

## 6. Repetition: title words and the recap

| Group | Title keywords (median) | Share said at least once (median) | Title keywords said per 1,000 words (median) | Longest run of the title said in order, first 60 s (median words) | …anywhere (median) | Videos saying 4+ title words in a row in the first 60 s | Recap that names items back |
|---|---:|---:|---:|---:|---:|---:|---:|
| Real | 5 | 80% | 16.7 | 2 | 3 | 5 of 21 | 2 of 21 |
| Faceless/AI | 5.5 | 100% | 13.9 | 3 | 3.5 | 10 of 24 | 12 of 24 |
| Scarlet | 5 | 83.3% | 8.2 | 3 | 3 | 2 of 25 | 9 of 25 |
| Diane | 6 | 88.9% | 13.3 | 3 | 3 | 2 of 13 | 4 of 13 |

**Measured:**
- **Title keywords said back.** Real videos repeat their title keywords most (median 16.7 per 1,000 words), mostly the subject noun said over and over ("bangs" 43 times in Glam Girl Gabi, "hair" 53 in chery, "jeans" 27 in Diana GOSS). Faceless/AI 13.9 (Alice Luxe's pixie video says "pixie" 88 times). Diane 13.3 ("French" is 4.9 per 1,000 across her 13). Scarlet 8.2, the lowest group; 6 of her 25 are under 3 per 1,000 (`w6w_ktMBHXM` 2.7, her top video; `pgMgC2aGPUw` 2.7, `pnBhMamGvhE` 2.6, `EVFmbo51Ou0` 1.9, `oBTVhnqkV04` 1.4, `_rIka9NRGH0` 1.2).
- **The title's promise word.** "Instantly" is in 10 Scarlet titles and 4 Diane titles and is said in none of those 14 videos; it is in 4 faceless/AI titles and said once. "Younger" is in 3 Diane titles and said 0 times in all three; in 5 Scarlet titles it is said 0, 1, 2, 2 and 0 times; in 5 faceless/AI titles 1 to 3 times each. "Expensive" is said 8-9 times in each of the three Scarlet videos that carry it.
- **The title read out.** 4 or more title words in a row are said in the first minute in 5 of 21 real, 10 of 24 faceless/AI, 2 of 25 Scarlet and 2 of 13 Diane videos. Chic Over 60 reads its whole 12-word title as its first sentence; Diana GOSS says six title words in a row ("five most common mistakes that make you look older").
- **Recap that names the items back** (reading; for the study, a recap or wrap-up segment in the notes' structure maps; for ours, the close read in full): real 2 of 21 (Justin Hickox's thin-hair video, Summer Beauty's gray video); faceless/AI 12 of 24 (both Age with Style videos, Ageless Melanin, Ageless Style, Chic After 60's leggings, Chic Over 60, ChicAfterSixty, Elegant After 60's copy, Ever Chic, Glow After 60, Trends Spotted, Vivian Sinclair); Scarlet 9 of 25; Diane 4 of 13. Three of ours close on a test that re-runs the rules instead of naming them (Diane `ISAL4NBlshQ` "Five checks. Check one, the shoulder seam."; Scarlet `EVFmbo51Ou0` "The mirror audit."; Scarlet `bkUBVNvN4NY`). The real side's typical close is a sign-off or an end-card pointer after the last item (Marie-Anne Lecoeur: no spoken like, subscribe or comment ask in `ixlexruRC6c`).

---

## 7. Our channels against the study

### 7.1 Every own video

Sorted by multiple within each channel. Hook moves use the letters in 2.1. Recap: yes (names items or fixes back), test (closes on a test that re-runs the rules), no.

| Channel | Video | Title | × normal | Words | Min | WPM | you /1k | I /1k | but /1k | Q /1k | Hook w | Hook s | Items | Median item w | Age /1k | Money /1k | Title words /1k | Hook moves | Recap |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Scarlet | `w6w_ktMBHXM` (top) | 5 Necklaces That Make Women Over 60 Look EXPENSIVE (And 3 Th | 75.07 | 4,078 | 22.1 | 184 | 33.8 | 5.9 | 0.5 | 0.7 | 197 | 0:58 | 8 | 354 | 1.7 | 1.0 | 2.7 | FNATG | yes |
| Scarlet | `yl-Vq9WyLzY` (top) | The Jeans Mistake Making Women Over 60 Look OLDER — and the  | 23.72 | 3,106 | 18.0 | 173 | 39.3 | 3.9 | 1.6 | 1.6 | 143 | 0:49 | 4 | 395 | 0.6 | 1.9 | 11.3 | QFNASG | no |
| Scarlet | `Z13YRFrGF2w` (top) | Wealthy Women Over 60 NEVER Wear These 3 Glasses — Here's Wh | 7.38 | 3,075 | 18.0 | 171 | 34.8 | 3.6 | 2.3 | 1.9 | 463 | 2:39 | 3 | 408 | 2.0 | 2.0 | 5.2 | QFNASG | no |
| Scarlet | `bkUBVNvN4NY` (top) | The 10 Makeup Rules That Make Women Over 60 Look 10 YEARS Yo | 6.49 | 3,354 | 19.2 | 175 | 36.1 | 3.9 | 3.0 | 0.0 | 220 | 1:13 | 10 | 270 | 0.9 | 0.9 | 5.7 | FNATG | test |
| Scarlet | `XGBMW0cEggI` | 5 Bob Haircuts Women Over 60 Should NEVER Get — And the 3 Th | 5.24 | 2,913 | 16.9 | 172 | 32.3 | 5.5 | 0.0 | 1.0 | 195 | 1:04 | 8 | 230 | 0.7 | 0.0 | 8.6 | QNASTG | yes |
| Scarlet | `pgMgC2aGPUw` | 10 Glasses That Make Women Over 60 Look INSTANTLY Younger | 3.10 | 2,954 | 16.5 | 179 | 51.8 | 4.1 | 1.7 | 1.4 | 142 | 0:45 | 10 | 226 | 1.0 | 2.0 | 2.7 | FASTG | no |
| Scarlet | `XAwQqpN3wQo` | STOP Wearing These 10 Earrings After 60 — They Age You Insta | 2.59 | 2,466 | 15.0 | 164 | 40.5 | 6.5 | 1.2 | 0.4 | 232 | 1:22 | 10 | 167 | 1.2 | 2.0 | 8.5 | NATGK | yes |
| Scarlet | `SZnf4UJCNDk` | The 5 Lipstick Shades That Take 10 YEARS Off After 60 (And t | 2.32 | 2,817 | 16.7 | 169 | 34.8 | 5.0 | 0.7 | 0.3 | 291 | 1:46 | 5 | 321 | 2.1 | 2.1 | 17.4 | FNASG | no |
| Scarlet | `XgQ5NgHQ3JQ` | How to Wear a Scarf After 60 — 7 Ways That INSTANTLY Lift Yo | 1.71 | 2,687 | 15.4 | 175 | 35.4 | 3.4 | 0.0 | 0.0 | 304 | 1:39 | 7 | 267 | 0.4 | 0.0 | 20.8 | NATG | no |
| Scarlet | `se0NK3SdI0I` | The 5 Haircuts That Flatter ANY Face Shape After 60 (And Tak | 1.51 | 2,903 | 16.6 | 175 | 33.1 | 4.8 | 1.0 | 0.0 | 224 | 1:12 | 5 | 362 | 0.7 | 0.7 | 23.4 | FNATGK | yes |
| Scarlet | `EB4Vwf5G0QE` | 7 Hair Mistakes That Age Women Over 60 by 10 YEARS (Fix Them | 1.08 | 2,403 | 15.6 | 154 | 25.8 | 5.8 | 1.7 | 4.2 | 189 | 1:09 | 7 | 257 | 1.7 | 2.5 | 21.6 | FNASTG | yes |
| Scarlet | `EVFmbo51Ou0` | Why You Look Frumpy After 60 — It's NOT Your Weight, It's Th | 1.01 | 2,663 | 16.6 | 160 | 21.8 | 6.8 | 0.8 | 0.8 | 275 | 1:44 | 5 | 357 | 0.8 | 1.5 | 1.9 | FNASG | test |
| Scarlet | `oH6XV-weIGs` | 8 Colors That Make Women Over 60 Look EXPENSIVE and CHIC | 1.00 | 2,872 | 17.5 | 164 | 43.2 | 3.5 | 1.4 | 0.7 | 292 | 1:39 | 8 | 266 | 0.7 | 0.7 | 6.6 | FNATGK | yes |
| Scarlet | `h9MsF44shdQ` | You're Styling Your Bob WRONG After 60 — 5 Secrets To Turn H | 0.97 | 2,773 | 16.0 | 174 | 44.7 | 2.9 | 1.1 | 0.0 | 442 | 2:30 | 5 | 410 | 0.7 | 0.0 | 10.8 | FNASTG | no |
| Scarlet | `M6HEuRQzwKw` | 5 Color Combinations That Make Women Over 60 Turn Heads Agai | 0.87 | 2,157 | 14.3 | 151 | 19.5 | 4.6 | 0.0 | 1.4 | 278 | 1:47 | 5 | 242 | 2.3 | 0.5 | 8.3 | NASTG | no |
| Scarlet | `_rIka9NRGH0` | 5 Haircuts That Make Women Over 60 Look INSTANTLY Younger (H | 0.74 | 2,409 | 15.1 | 159 | 25.3 | 8.3 | 1.2 | 1.2 | 358 | 2:15 | 5 | 225 | 2.1 | 1.7 | 1.2 | QFASTG | yes |
| Scarlet | `Z9cXNiZtV8w` | Over 60? STOP Applying Concealer Like This — 3 Rules for NO  | 0.69 | 2,804 | 16.0 | 175 | 46.4 | 3.6 | 0.7 | 0.4 | 911 | 5:08 | 3 | 506 | 1.4 | 1.4 | 16.4 | QNATG | no |
| Scarlet | `VrT07KxdgNo` | How Women Over 50 Turn Heads AGAIN — 7 Style Secrets That Ha | 0.59 | 2,402 | 16.1 | 149 | 26.2 | 3.3 | 2.1 | 0.4 | 175 | 1:10 | 7 | 270 | 2.9 | 0.8 | 8.3 | FNASTG | yes |
| Scarlet | `3t_q9UrMctk` (bottom) | 5 Pixie Cuts That Make Women Over 60 Look 10 Years YOUNGER | 0.58 | 2,696 | 15.9 | 169 | 34.5 | 3.7 | 1.1 | 0.4 | 322 | 1:45 | 5 | 365 | 1.1 | 0.0 | 8.2 | FNAG | no |
| Scarlet | `pnBhMamGvhE` | Apple-Shaped Woman? 7 Outfits That INSTANTLY Look Slimmer (A | 0.45 | 2,696 | 16.4 | 164 | 15.6 | 3.0 | 0.4 | 0.0 | 361 | 2:13 | 10 | 211 | 0.4 | 1.5 | 2.6 | FNAG | no |
| Scarlet | `UXXfCp_HS6g` (bottom) | How to Look EXPENSIVE After 60 Without Spending a Dime (7 Tr | 0.44 | 2,888 | 15.8 | 182 | 48.1 | 3.8 | 0.7 | 0.7 | 595 | 3:08 | 7 | 292 | 1.4 | 1.4 | 4.8 | QFNATG | no |
| Scarlet | `e2v7TDK3SW0` | 10 Outfit Mistakes That Make Women Over 60 Look 10 Years OLD | 0.32 | 2,894 | 16.8 | 172 | 19.0 | 5.5 | 1.4 | 0.0 | 204 | 1:02 | 10 | 231 | 1.0 | 2.1 | 6.2 | FNASG | no |
| Scarlet | `3JBVSs9ETu4` (bottom) | The 7 Fall Colors That Make Women Over 60 Look INSTANTLY You | 0.30 | 2,440 | 15.0 | 163 | 29.1 | 4.9 | 1.2 | 0.0 | 320 | 1:57 | 7 | 250 | 2.5 | 2.5 | 3.3 | FNASTG | no |
| Scarlet | `oBTVhnqkV04` | 10 Style Tricks That Make Women Over 60 Look INSTANTLY Slimm | 0.28 | 2,928 | 18.2 | 161 | 31.1 | 3.8 | 1.0 | 0.0 | 227 | 1:22 | 10 | 248 | 1.7 | 1.4 | 1.4 | NASG | no |
| Scarlet | `85nTTAPzBeM` | Thinning Hair After 60? 5 Cuts That INSTANTLY Look Twice as  | 0.22 | 2,619 | 15.0 | 175 | 26.0 | 4.6 | 1.1 | 1.1 | 270 | 1:29 | 5 | 359 | 1.5 | 2.3 | 22.1 | QFNASTG | yes |
| Diane | `ISAL4NBlshQ` (top) | Why French Women Over 60 NEVER Look Frumpy — It's Not Their  | 6.30 | 2,082 | 12.5 | 167 | 32.2 | 10.1 | 1.0 | 1.0 | 175 | 0:58 | 5 | 262 | 1.0 | 2.4 | 10.1 | FNASTGK | test |
| Diane | `egJ5B6d879c` (top) | 5 French Haircuts That Flatter ANY Face Shape After 60 (And  | 4.80 | 2,729 | 14.8 | 185 | 47.6 | 9.2 | 1.5 | 2.2 | 339 | 1:52 | 5 | 413 | 1.5 | 0.7 | 29.3 | QFNASTG | no |
| Diane | `L6-ASPZTz1s` (top) | Apple-Shaped After 60? 7 Outfits French Women Wear to Look I | 2.17 | 3,395 | 18.3 | 186 | 36.8 | 6.2 | 0.6 | 0.6 | 493 | 2:36 | 10 | 278 | 0.6 | 0.9 | 7.7 | QNASTG | no |
| Diane | `kWzjIzbdB00` (top) | Parisian Women Over 60 NEVER Wear These 3 Glasses — Here's W | 1.80 | 3,944 | 23.7 | 167 | 44.9 | 3.8 | 0.5 | 1.5 | 142 | 0:46 | 6 | 420 | 2.0 | 1.3 | 8.1 | NATGK | yes |
| Diane | `Rba36JLtcYY` | 5 Lipstick Shades French Women Wear After 60 to Look 10 YEAR | 1.73 | 2,765 | 16.8 | 165 | 39.1 | 4.3 | 4.0 | 1.4 | 209 | 1:11 | 5 | 283 | 2.2 | 1.8 | 14.8 | FNASTG | yes |
| Diane | `Ky2QiqNLd5I` | 7 Glasses That Make Women Over 60 Look INSTANTLY Younger (Th | 1.13 | 3,396 | 22.0 | 154 | 41.2 | 8.5 | 1.8 | 0.0 | 570 | 3:41 | 7 | 278 | 1.5 | 2.1 | 5.6 | FNASTG | no |
| Diane | `qmYPg0L3qZU` | The French Bob After 60 — 3 Versions That Take 10 YEARS Off  | 1.00 | 3,352 | 18.6 | 180 | 41.8 | 3.9 | 0.6 | 2.1 | 148 | 0:49 | 8 | 272 | 0.9 | 0.6 | 26.3 | NAG | no |
| Diane | `akYILT648sU` | 10 Outfit Mistakes American Women Over 60 Make — That French | 0.95 | 2,852 | 16.3 | 175 | 20.3 | 5.6 | 0.3 | 0.0 | 161 | 0:57 | 10 | 214 | 1.4 | 2.5 | 14.0 | FNASTG | yes |
| Diane | `41ezk-kRd7Y` | The Only 3 Necklaces a Woman Over 60 Needs to Look EXPENSIVE | 0.87 | 3,334 | 18.3 | 183 | 32.1 | 4.5 | 0.3 | 0.6 | 357 | 2:00 | 3 | 705 | 1.5 | 3.0 | 7.8 | NASTG | yes |
| Diane | `z6Ngr5oSjlw` | French Women Over 60 NEVER Wear These 7 Earrings — Here's Wh | 0.46 | 2,939 | 16.9 | 174 | 43.9 | 7.8 | 0.7 | 2.0 | 176 | 0:56 | 7 | 287 | 1.0 | 2.4 | 13.3 | NASG | no |
| Diane | `jPoeJlLO2_w` (bottom) | 5 Color Combinations French Women Over 60 Wear to Turn Heads | 0.31 | 2,831 | 17.4 | 163 | 39.6 | 5.3 | 1.1 | 1.8 | 175 | 1:04 | 5 | 489 | 0.7 | 0.4 | 13.8 | NASTGK | no |
| Diane | `bMlBJn27PEU` (bottom) | How to Tie a Scarf After 60 the French Way — 7 Knots That IN | 0.28 | 2,707 | 15.9 | 170 | 39.9 | 5.5 | 1.9 | 1.9 | 368 | 2:13 | 7 | 263 | 1.5 | 1.5 | 22.5 | QFASTGK | no |
| Diane | `kIjkdHM3a68` (bottom) | 5 French Haircuts That Make Women Over 60 Look INSTANTLY You | 0.25 | 2,672 | 15.8 | 169 | 47.5 | 7.1 | 1.1 | 0.8 | 292 | 1:35 | 5 | 299 | 1.1 | 1.5 | 8.2 | FNASTG | no |

### 7.2 Top against bottom, and against the study

| Set | n | × normal | Words | Min | WPM | you /1k | I /1k | but /1k | Q /1k | Hook w | Hook s | Items | Median item w | Age /1k | Money /1k | Title words /1k |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Scarlet top | 4 | 15.50 | 3,230 | 18.6 | 174 | 35.4 | 3.9 | 1.9 | 1.2 | 208.5 | 65.5 | 6 | 374.5 | 1.3 | 1.5 | 5.4 |
| Scarlet bottom | 3 | 0.40 | 2,696 | 15.8 | 169 | 34.5 | 3.8 | 1.1 | 0.4 | 322 | 117 | 7 | 292 | 1.4 | 1.4 | 4.8 |
| Scarlet all | 25 | 1 | 2,804 | 16.4 | 171 | 33.8 | 4.1 | 1.1 | 0.4 | 275 | 99 | 7 | 270 | 1.2 | 1.4 | 8.2 |
| Diane top | 4 | 3.50 | 3,062 | 16.5 | 176 | 40.9 | 7.7 | 0.8 | 1.2 | 257 | 85 | 5.5 | 345.5 | 1.2 | 1.1 | 9.1 |
| Diane bottom | 3 | 0.30 | 2,707 | 15.9 | 169 | 39.9 | 5.5 | 1.1 | 1.8 | 292 | 95 | 5 | 299 | 1.1 | 1.5 | 13.8 |
| Diane all | 13 | 1 | 2,852 | 16.9 | 170 | 39.9 | 5.6 | 1 | 1.4 | 209 | 71 | 6 | 283 | 1.4 | 1.5 | 13.3 |
| Study real | 21 | – | 2,031 | 11.9 | 170 | 48.9 | 23.4 | 6.5 | 2.6 | 172 | 57 | 5 | 251.5 | 0 | 0 | 16.7 |
| Study faceless/AI | 24 | – | 2,482.5 | 16 | 157 | 46.5 | 6.8 | 4.8 | 2 | 285 | 101 | 7 | 281.5 | 2.4 | 0 | 13.9 |

**Measured:**
- **Where both channels differ from both study sides** (not just from one): "but" (1.0-1.1 per 1,000 against 4.8-6.5), "I" (4.1-5.6 against 6.8 and 23.4), "you" (33.8-39.9 against 46.5-48.9), questions (0.4-1.4 against 2.0-2.6), money figures (34 of 38 videos against 5 of 45), brand names (1 of 38 against 19 of 45), the age line in every hook (against 3 of 21 real and 20 of 24 faceless/AI), the name-and-channel line in every hook, and no comment or subscribe ask before item one (the study has one or both in 9 of 45). Item length is not one of them: our medians (266 and 285 words) sit next to faceless/AI (258) and real (241).
- **Where Scarlet sits with faceless/AI and Diane doesn't:** hook length (Scarlet 275 words / 1:39, faceless/AI 285 / 1:41; Diane 209 / 1:11) and item one inside the first minute (Scarlet 3 of 25, faceless/AI 6 of 24, Diane 5 of 13, real 11 of 21).
- **Scarlet top 4 against bottom 3:** the top four have shorter hooks (median 208.5 words / 1:06 against 322 / 1:57), are longer overall (3,230 words, 18.6 min against 2,696, 15.8), and have longer items (median 374.5 words against 292). Two of the top four reach item one by 0:58 (`w6w_ktMBHXM`, `yl-Vq9WyLzY`); none of the bottom three does before 1:45. "but", "you", "I" and age rates barely differ.
- **Diane top 4 against bottom 3:** the same direction, smaller: hooks 257 / 1:25 against 292 / 1:35; 3,062 words against 2,707; items 345.5 against 299. Diane's top four say fewer title keywords (9.1 per 1,000 against 13.8).
- **What else differs between top and bottom, unmeasured here:** topic (Scarlet's top four are necklaces, jeans, glasses and makeup, her bottom three pixie cuts, "look expensive" habits and fall colours; Diane's top four are the frumpy rules, haircuts, apple-shape outfits and glasses, her bottom three colour pairs, scarf knots and haircuts), age at collection (top 13-33 days, bottom 9-37 days, so they overlap), and the thumbnail. The top-bottom gaps above are 4 against 3 videos and should be read with that.

---

## 8. The copycat pairs

Four pairs, each a winner and a same-title copy. A and C are faceless/AI against faceless/AI; B is ChicAfterSixty against Ageless Confidence ("not checked" in round 2); D is Marie-Anne Lecoeur's own video against Ageless Style 50s & 60s, a faceless channel using her exact title, whose copy is itself a hit on its channel (267,196 views, 55.7×).

| Pair | Role | Channel | Video | Views | × normal | Words | Min | WPM | you /1k | I /1k | but /1k | Q /1k | Hook w | Hook s | Items | Median item w | Age /1k | Money /1k | Title words /1k | Hook moves | Recap |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A | winner | Age with Style | `6byOPawCepI` | 1,107,951 | 291.57 | 2,658 | 16.0 | 166 | 51.2 | 7.2 | 6.8 | 1.5 | 244 | 1:24 | 7 | 291 | 4.1 | 0.0 | 17.3 | QFNASTGU | yes |
| A | copy | Age with Style | `K6N1EFo7oec` | 7,133 | 1.88 | 2,852 | 18.8 | 152 | 31.9 | 4.9 | 1.4 | 2.1 | 141 | 0:50 | 7 | 349 | 1.1 | 0.0 | 13.0 | QFNACG | yes |
| B | winner | ChicAfterSixty | `_OQsPYjIfsQ` | 493,468 | 205.61 | 4,424 | 26.6 | 166 | 40.5 | 24.4 | 2.5 | 1.8 | 327 | 1:48 | 5 | 493 | 2.3 | 0.0 | 34.1 | FNASG | yes |
| B | copy | Ageless Confidence | `UTpC6n7KKi0` | 1,048 | 2.56 | 2,481 | 14.6 | 170 | 44.3 | 13.3 | 2.4 | 0.8 | 364 | 2:08 | 5 | 238 | 3.6 | 0.0 | 24.6 | FNASTG | no |
| C | winner | Chic After 60 | `YeKT0zkdIrw` | 960,045 | 25.90 | 4,084 | 29.8 | 137 | 20.3 | 3.2 | 7.8 | 0.5 | 469 | 3:07 | 8 | 436 | 3.7 | 0.0 | 12.7 | FNTG | no |
| C | copy | Elegant After 60 | `ZFx3yIrJqO0` | 2,229 | 0.77 | 2,484 | 14.2 | 175 | 45.9 | 5.6 | 4.8 | 3.6 | 187 | 1:05 | 8 | 272 | 4.0 | 0.0 | 14.9 | QFNAG | yes |
| D | winner | Marie-Anne Lecoeur | `ixlexruRC6c` | 1,038,117 | 12.36 | 923 | 8.0 | 115 | 56.3 | 27.1 | 9.8 | 13.0 | 29 | 0:13 | 7 | 127 | 2.2 | 0.0 | 8.7 | QFN | no |
| D | copy | Ageless Style 50s & 60s | `Fs17Qc6l8Ug` | 267,196 | 55.67 | 2,024 | 12.1 | 168 | 76.6 | 22.2 | 9.4 | 1.5 | 310 | 1:43 | 7 | 187 | 4.4 | 0.0 | 2.5 | QFNATCGU | yes |

**Measured, pair by pair:**
- **A, Age with Style (same channel, same title; 291.6× against 1.9×).** The winner is shorter (16:00 against 18:47) with a longer hook (244 words / 1:24 against 141 / 0:50) that holds a mirror-scene question, the subscribe ask and a vague tease ("you don't want to miss what's coming next"); the copy's hook asks for a comment ("Where in the world are you watching from today?") and has no scene or tease. The winner's items are shorter and very even (267-337, median 291, against 329-393, median 349). The winner has more "you" (51.2 against 31.9 per 1,000), more "but" (6.8 against 1.4) and more age lines (11 against 3). Both recap.
- **B, fine hair after 60 (205.6× against 2.6×).** The winner is nearly twice as long (26:35, 4,424 words against 14:37, 2,481) with items twice the length (median 493 against 238) and much more first person (24.4 against 13.3 per 1,000; "I followed those same rules for almost 30 years", "my mother's old bathroom"). Hooks are similar (327 / 1:48 against 364 / 2:08); the copy adds a held payoff (the "Susan" story) and two CTA interludes inside the list. The winner recaps all five rules; the copy does not.
- **C, 8 colour combinations (25.9× against 0.77×).** The winner is twice as long (29:49 against 14:14) and the slowest faceless/AI video (137 wpm against 175), with a hook of 469 words / 3:07 against 187 / 1:05, the lowest "you" rate in the faceless/AI group (20.3 against 45.9), almost no questions (2 against 9) and no recap; the copy has a question, a recap and items of 220-280 words against the winner's 214-450.
- **D, "7 Things That Scream 'Old Lady'" (12.4× on Marie-Anne Lecoeur's channel; 55.7× on the copy's).** The original is the shortest list in the study by words and the slowest video: 8:02, 923 words, 115 wpm, a 29-word hook that reaches item one at 0:13 with three moves (question, feared result, count), and items of 80-167 words. The copy is 12:05 and 2,024 words with a 310-word / 1:43 hook carrying all eight moves ("If you want to look older, tired, and invisible, please keep doing these seven things."; "I've saved it for last, so you have to stay until the end."; "comment style in the comments"), items of 166-272 words, "The swap" said seven times, and a recap. The copy says the title's keywords far less (2.5 against 8.7 per 1,000).
- **Across the four:** no measure points the same way in every pair. The winner is longer in B and C and shorter in A and D; its hook is longer in A and C and shorter in B and D; its items are longer in B and C and shorter in A and D. The winner has more "but" in A and C, about the same in B and D.

---

## Methods notes

- Scripts (scratchpad, `/tmp/claude-0/-home-user-script-system/a46e4e64-c9ae-55b0-aafb-8c468f9ffa04/scratchpad/analysis02/`): `lib.py` (loader), `spec.py` (the hand-set first-item anchors and item segment maps for all 83 videos, with a docstring on the marks), `analyze.py` (per-video measures, `rows.json`), `moves.py` (hook move patterns; the per-video calls are in `build.py`), `items2.py` (heading windows and swap labels), `build.py` (tables, hand corrections and the reading sets: questions, feared results, counts, authority, teases, comment asks, headings, recaps), `notecmp.py` (the notes check). All read-only on `studies/style/`; run with `python3 -I`.
- The reading calls (which lines are a hook's moves, where items start, heading style, recap) were made by one coder in one pass, with the pattern matches as a prompt and every match read in context. Another coder would move a few videos on "story or scene", "tease" and "recap" in particular; the side-level gaps reported above are large enough that a few moves would not reverse them, but the smaller ones (a difference of 1-3 videos) could.
- Hook times are caption-line starts (±3 s). Item word counts are at line boundaries (about ±6 words per boundary). The rounding in notes' "about N words" figures (round-3 check) is why the recount differs by 1-5% on most noted videos.
- Our 24 un-noted videos had item starts set from their headings; their mid-roll book CTA and close were set by reading the transcript around each "my book" mention.
- Question, money and brand counts are floors where marked; question counts for the 10 unpunctuated study transcripts are hand counts of viewer questions only.
- The pair-D copy (Ageless Style) is counted in Faceless/AI and the pair-D original in Real, so section 8 overlaps sections 1-6 for those two videos; the pairs A-C videos are inside Faceless/AI too.

## What the numbers can't show

- **Cause.** Every gap here sits alongside differences in topic, upload date, channel age, thumbnail, title wording, presenter and the platform's distribution; none of these was held fixed. The pairs hold the title fixed and still point in different directions (section 8).
- **Delivery.** These are caption transcripts. Voice, pace changes, pauses, music, what is on screen (try-ons, before/afters, AI images) and the presenter's face are not in them; the real side's try-on videos carry much of their content visually.
- **Retention.** Nothing here measures where viewers leave. A long hook that holds viewers and one that loses them look the same in a transcript.
- **Truth and quality.** The counts don't say whether a price, a claim ("Studies in color psychology show…") or a fix is right, or whether a scene is well written. They count that something was said, not how well.
- **Reading calls.** Moves, item boundaries, heading style and recap are one coder's reading; the definitions are given so they can be re-coded.
- **Small groups.** Top and bottom are 4 and 3 videos; the pairs are one each. Differences of one or two videos within these sets are not findings.
