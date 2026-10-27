# 02 Openings and numbers: the HVAC scripts measured

Part 2 of the HVAC comparison, written 2026-10-27 for the Roger the HVAC Guy pack (`hvac-scripts`, to be built from `plumbing-scripts`). It measures the 36 transcribed videos in `data/` (WINNI `6CE72U92R-I` has no transcript and is left out) and sets each figure next to the plumbing study's figure for the same measure. It describes; it doesn't recommend. Nothing in `data/`, `notes/` or the library was changed.

## How to read this

- **Measured by script:** `tools/measure.py` (run `python3 tools/measure.py` from `studies/hvac/`; `--open 30` prints every first 30 s). Views, multiples, durations and types come from each `meta.md`; hook lengths and first-value times come from the notes and were re-checked against the transcripts (below).
- **Groups:** *real people* = 25 videos (on camera, hands only, or a human voice-over: Everyday Home Repairs, grayfurnaceman and Project Farm count here); *faceless / persona* = 10 videos (Ray Dutton ×6, HVAC Exposed ×2, Vent Exposed, Lost Survival Knowledge); *Roger* = Roger the Pipe Guy's own HVAC video (n = 1, so its "median" is just the video).
- **Multiples (× normal)** compare a video with its own channel's normal. Normals run from 548 views (HVAC Exposed) to 1,927,750 (Technology Connections), so multiples are compared **within a channel**, never across. grayfurnaceman's 781× and 193× are against an off-topic baseline (`log.md`).
- **Measured vs reading.** Counts, times and word counts are measured. Which job a line does (point, villain, reassurance), what counts as the "first real value" and which videos are "lists" are my reading, one coder, marked where it matters.

**How things were counted**
- *Words:* transcript tokens with the `[m:ss]` stamp and tags like `[Music]` removed. *Minutes:* the meta duration. *Words per minute* = words ÷ minutes (as `studies/plumbing/comparison/stats.md`).
- *"you/your"* = you, your, yours, yourself (and you're, you'll, you've, you'd); *"I/me/my"* = I (and I'm, I've, I'll, I'd), me, my, mine, myself; *"but"* = the word. All per 1,000 words. These match the plumbing study's counts (`03-own-vs-competitors.md`, "How I counted") closely enough to compare.
- *Viewer questions:* 20 transcripts have punctuated captions (20+ full stops per 1,000 words); there every "?" is counted ("Attic? Utility closet?" is two). The other 16 have no punctuation at all, so no sentence or question can be cut by machine. For those, a broad pattern listed every possible question frame (an auxiliary before a pronoun, a wh-word before an auxiliary, "what if", "guess how"; 244 candidates); I read each in context and kept only questions put to the viewer or voiced for him ("so you might be asking why have two brands…"). A presenter talking to himself mid-job, reported speech and "would you please hit the like button" are left out. Statement-shaped questions ("You want better air quality?") can't be found this way, so these 16 counts (marked **h**) are floors. Sentences were not counted anywhere; the "first sentence" in section 2 is cut by hand, by sense.
- *Dollar figures:* every "$" amount; a number followed by dollars, bucks, cents or grand; "a couple bucks", "a couple thousand dollars"; each end of a range counts ("$250 to $400" = 2, as in plumbing `03`). "Hundreds of dollars" is counted apart as vague (it changes no median). Amounts said with no money word ("billed at 300") are missed: the hand check found 7 of these in one Ray Dutton script, so the faceless counts are floors.
- *Numbers per minute:* runs of digits or number words (two to billion; "one" and ordinals left out), each run once.
- *Items:* start and end times for the 15 list videos are set in `measure.py` from the notes' segment maps and checked line by line in the transcript; an item ends where the next item, an interlude, a plug or the recap starts. Ray Dutton's two book plugs inside an item are cut out.

**Hand checks (3 videos, against the transcripts):** The Funny Carpenter `_g8gQ1gg1FM`, Deanin' It Yourself `dRL13JlclhM`, Ray Dutton `fHAlfm21vYw`.
- Words (1,102 / 1,065 / 2,521) match `wc -w`; "you" (75 / 90 / 89), "I" (14 / 44 / 18) and "but" (6 / 3 / 2) match a separate `grep -w` count.
- Questions: Funny Carpenter's 5 "?" are all real questions (two in the hook, [0:00]-[0:07]). Deanin's whole transcript was read: one question, at [0:00]. Ray's `fHAlfm21vYw` has no "?" and no question-shaped sentence either, so its 0 stands.
- Dollar figures: Deanin 2 ("a couple bucks" ×2) and Funny Carpenter 0 are right. Ray's 16 are all real, but the script misses 7 unmarked amounts ("runs 150 to 300" [1:57], "you pay 150, sometimes 300", "A $15 flame sensor billed at 300. A $40 igniter billed at 400"), so the true count is about 23.
- First value and item one: Funny Carpenter item five at [0:21], first tip [0:28] ("If you have a set of pliers at home, use those."); Deanin first step [0:57]; Ray item one at [0:52], first value [1:08] ("You reset it instead of reading it.").
- **Across all 36:** 30 of the notes' first-value times stand (most within 3 s of the line they quote). 6 were moved, by 2-15 s, where the line the notes describe starts elsewhere: Ray `K2jCz3D5z_0` 1:04 → 1:13, `_ZgVjFpBnQA` 1:42 → 1:49, `dOZ-8__G4uU` 0:53 → 0:58, `fHAlfm21vYw` 0:53 → 1:08, `UdyqMC1GVxQ` 1:44 → 1:42, Word of Advice `1bRsFAMgZRQ` 0:11 → 0:08 (`FV_RECHECK` in the script). Hook word counts re-counted from the transcript match the notes within 4 words on every video.

---

## 1. Measured per video

"Q" is the viewer-question count ("h" = hand count from unpunctuated captions, a floor). "Hook" = the notes' hook words (re-counted from the transcript) / seconds. "$ before first value" = dollar figures said before the first real value. "Item 1" = when item one starts, list videos only.

| Channel | Video | Type | ×normal | Words | Min | WPM | you /1k | I /1k | but /1k | Q | Q /1k | $ figs | $ /min | nums /min | Hook w (recount) / s | $ before first value | First value | Item 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Atlas AC | `r_uP9itJ0HQ` | brand verdict | 88.6 | 2,745 | 15:23 | 178 | 13.5 | 27.0 | 4.0 | 4h | 1.5 | 0 | 0.00 | 2.3 | 100 (100) / 31 | 0 | 1:17 | – |
| Deanin' | `dRL13JlclhM` | substance / drain fix | 818.5 | 1,065 | 5:51 | 182 | 84.5 | 41.3 | 2.8 | 1h | 0.9 | 2 | 0.34 | 1.0 | 57 (57) / 15 | 0 | 0:57 | – |
| Everyday HR | `sRvH-io-ZtA` | symptom diagnostic | 9.2 | 1,530 | 8:25 | 182 | 47.1 | 19.6 | 6.5 | 2h | 1.3 | 2 | 0.24 | 4.8 | 134 (134) / 35 | 1 | 0:37 | – |
| Everyday HR | `--A2I2s7aNw` | seasonal checklist | 7.2 | 1,562 | 8:56 | 175 | 39.7 | 14.1 | 3.2 | 0h | 0.0 | 3 | 0.34 | 1.2 | 90 (90) / 25 | 2 | 0:28 | 1:13 |
| grayfurnaceman | `yJxDc90hs4g` | symptom diagnostic | 781.4 | 1,400 | 10:10 | 138 | 16.4 | 30.0 | 3.6 | 2 | 1.4 | 0 | 0.00 | 1.5 | 48 (48) / 19 | 0 | 0:26 | – |
| grayfurnaceman | `X3Y-yA42UBk` | upsell exposé | 192.6 | 744 | 5:19 | 140 | 60.5 | 12.1 | 2.7 | 0h | 0.0 | 0 | 0.00 | 1.7 | 81 (81) / 37 | 0 | 0:55 | – |
| RenoVision | `J95l9Ue4224` | hidden cause: the bill and drafts | 24.9 | 3,791 | 18:20 | 207 | 45.6 | 19.3 | 3.4 | 2h | 0.5 | 4 | 0.22 | 3.6 | 60 (60) / 13 | 0 | 0:22 | – |
| How To Home | `AQQH9QwC46A` | N things / insider | 11.1 | 2,846 | 12:40 | 225 | 25.3 | 28.5 | 8.1 | 0h | 0.0 | 5 | 0.39 | 2.4 | 42 (42) / 10 | 0 | 0:23 | 0:10 |
| How To Home | `i8nDBZo6XyE` | cheap-part repair | 8.1 | 2,568 | 11:40 | 220 | 32.3 | 30.0 | 5.5 | 0h | 0.0 | 1 | 0.09 | 3.3 | 53 (53) / 14 | 0 | 0:14 | – |
| HVAC Guide | `Unx9Ze10N98` | mistakes list | 190.8 | 1,391 | 6:43 | 207 | 35.2 | 24.4 | 5.8 | 2h | 1.4 | 0 | 0.00 | 1.3 | 63 (63) / 17 | 0 | 0:19 | 0:17 |
| Project Farm | `RkjRKIRva58` | ranked verdict | 2.5 | 2,514 | 12:54 | 195 | 5.2 | 3.6 | 5.6 | 3 | 1.2 | 14 | 1.09 | 17.1 | 123 (123) / 33 | 0 | 1:21 | – |
| Silver Cymbal | `_b6p0fkWhCY` | symptom diagnostic | 52.5 | 2,015 | 8:52 | 227 | 59.1 | 24.8 | 4.0 | 1h | 0.5 | 1 | 0.11 | 1.8 | 69 (69) / 15 | 0 | 0:17 | 1:03 |
| Silver Cymbal | `qAxJb0J1HH0` | substance / drain fix | 46.0 | 1,993 | 8:09 | 245 | 45.2 | 20.6 | 12.0 | 1h | 0.5 | 1 | 0.12 | 0.5 | 118 (118) / 29 | 0 | 0:30 | – |
| Tech Connections | `7J52mDjZzto` | decision versus | 2.5 | 5,891 | 35:15 | 167 | 8.3 | 10.5 | 11.0 | 21 | 3.6 | 0 | 0.00 | 1.6 | 190 (190) / 63 | 0 | 0:37 | – |
| Tech Connections | `HnMuNCl7tZ8` | never-do / safety | 1.5 | 4,684 | 28:55 | 162 | 15.8 | 14.7 | 10.2 | 2h | 0.4 | 2 | 0.07 | 1.6 | 97 (97) / 38 | 1 | 1:36 | – |
| DIY HVAC Guy | `y07w1hiKIrI` | outage / cheap part | 106.0 | 2,250 | 11:46 | 191 | 40.9 | 11.1 | 4.9 | 0h | 0.0 | 0 | 0.00 | 1.2 | 140 (140) / 41 | 0 | 0:48 | – |
| DIY HVAC Guy | `SkLMRM9NnBY` | N things / insider | 68.3 | 2,170 | 13:17 | 163 | 65.9 | 14.7 | 6.9 | 0h | 0.0 | 2 | 0.15 | 2.5 | 171 (171) / 60 | 0 | 1:00 | 1:00 |
| DIY HVAC Guy | `Qx3cC1y23JY` | outage how-to | 60.4 | 1,390 | 7:08 | 195 | 44.6 | 4.3 | 7.9 | 3 | 2.2 | 12 | 1.68 | 3.4 | 63 (63) / 21 | 3 | 0:23 | – |
| DIY HVAC Guy | `Is0pv2Qnza0` | cheap-part repair | 60.4 | 2,336 | 11:25 | 205 | 46.7 | 10.3 | 5.6 | 2h | 0.9 | 7 | 0.61 | 4.6 | 143 (143) / 46 | 4 | 0:48 | – |
| DIY HVAC Guy | `x2BK-zr4raE` | brand verdict | 32.0 | 1,750 | 9:30 | 184 | 51.4 | 16.6 | 6.3 | 1 | 0.6 | 7 | 0.74 | 1.3 | 77 (77) / 21 | 0 | 0:21 | – |
| DIY HVAC Guy | `mP0IjyvQtxw` | seasonal checklist | 30.2 | 3,187 | 14:55 | 214 | 41.7 | 10.0 | 3.5 | 1 | 0.3 | 2 | 0.13 | 2.2 | 137 (137) / 36 | 0 | 0:44 | 0:44 |
| Funny Carpenter | `_g8gQ1gg1FM` | mistakes list | 5.8 | 1,102 | 5:33 | 199 | 68.1 | 12.7 | 5.4 | 5 | 4.5 | 0 | 0.00 | 4.5 | 66 (66) / 21 | 0 | 0:28 | 0:21 |
| Provident Prepper | `erq-QuCN0G0` | outage list | 73.4 | 2,804 | 15:09 | 185 | 51.0 | 12.5 | 7.8 | 4h | 1.4 | 0 | 0.00 | 1.9 | 140 (140) / 57 | 0 | 1:06 | 0:57 |
| Word of Advice | `3Jonl_TLkpE` | symptom diagnostic | 140.7 | 1,557 | 8:57 | 174 | 35.3 | 14.8 | 7.1 | 1 | 0.6 | 3 | 0.34 | 2.9 | 37 (37) / 11 | 0 | 0:11 | – |
| Word of Advice | `1bRsFAMgZRQ` | cheap-part repair | 74.9 | 2,455 | 13:08 | 187 | 48.1 | 33.4 | 8.6 | 1 | 0.4 | 0 | 0.00 | 1.9 | 28 (28) / 8 | 0 | 0:08 | – |
| HVAC Exposed | `QKPPm6M0__o` | brand verdict | 1055.6 | 1,754 | 12:07 | 145 | 43.9 | 4.0 | 2.9 | 2 | 1.1 | 15 | 1.24 | 5.0 | 260 (262) / 100 | 1 | 1:51 | 6:58 |
| HVAC Exposed | `l2yyfYpcwpQ` | product villain / myth-bust | 640.9 | 2,027 | 13:37 | 149 | 54.8 | 7.9 | 5.9 | 10 | 4.9 | 27 | 1.98 | 7.7 | 120 (116) / 50 | 5 | 1:40 | – |
| Lost Survival | `rX4eyZaHAjw` | outage list | 55.6 | 4,061 | 22:21 | 182 | 32.0 | 1.0 | 2.0 | 2 | 0.5 | 6 | 0.27 | 2.0 | 150 (149) / 49 | 1 | 1:50 | 1:49 |
| Ray Dutton | `dOZ-8__G4uU` | seasonal checklist | 147.9 | 2,334 | 11:49 | 198 | 42.0 | 8.1 | 1.3 | 3 | 1.3 | 10 | 0.85 | 2.1 | 172 (172) / 50 | 1 | 0:58 | 0:51 |
| Ray Dutton | `K2jCz3D5z_0` | habit list | 135.5 | 2,245 | 14:27 | 155 | 53.9 | 9.4 | 3.1 | 2 | 0.9 | 6 | 0.42 | 4.4 | 164 (164) / 63 | 0 | 1:13 | 1:07 |
| Ray Dutton | `fHAlfm21vYw` | seasonal checklist | 113.7 | 2,521 | 14:42 | 171 | 35.3 | 7.1 | 0.8 | 0 | 0.0 | 16 | 1.09 | 4.8 | 160 (162) / 50 | 1 | 1:08 | 0:52 |
| Ray Dutton | `_ZgVjFpBnQA` | product villain / myth-bust | 93.1 | 2,292 | 15:10 | 151 | 48.9 | 11.8 | 3.5 | 3 | 1.3 | 16 | 1.05 | 2.5 | 260 (260) / 100 | 5 | 1:49 | – |
| Ray Dutton | `qbWN3OViWxQ` | mistakes list | 70.7 | 2,318 | 14:05 | 165 | 55.7 | 9.9 | 1.7 | 2 | 0.9 | 8 | 0.57 | 2.7 | 165 (169) / 57 | 2 | 1:00 | 0:59 |
| Ray Dutton | `UdyqMC1GVxQ` | doing it wrong | 16.9 | 2,195 | 13:30 | 163 | 42.4 | 11.8 | 3.2 | 1 | 0.5 | 12 | 0.89 | 1.9 | 215 (215) / 74 | 2 | 1:42 | – |
| Vent Exposed | `86S3ITbfzQY` | brand verdict | 601.5 | 1,258 | 8:12 | 153 | 35.0 | 6.4 | 3.2 | 1 | 0.8 | 18 | 2.20 | 6.6 | 185 (181) / 66 | 3 | 1:09 | 1:07 |
| Roger (own) | `cFYptbCvNjI` | single-product fix | 13.6 | 3,387 | 23:29 | 144 | 39.9 | 7.7 | 0.9 | 9 | 2.7 | 15 | 0.64 | 1.8 | 134 (134) / 55 | 0 | 1:01 | – |

**Group medians**

| Group | n | ×normal | Words | Min | WPM | you /1k | I /1k | but /1k | Q /1k | $ figs | $ /min | nums /min | Hook w | Hook s | First value s | Item 1 s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Real people | 25 | 52.5 | 2,170 | 11:25 | 187 | 44.6 | 14.8 | 5.6 | 0.6 | 2.0 | 0.1 | 1.9 | 81 | 25 | 30 | 50 |
| Faceless / persona | 10 | 124.6 | 2,268 | 13:51 | 159 | 43.1 | 8.0 | 3.0 | 0.9 | 13.5 | 1.0 | 3.5 | 168 | 60 | 86 | 67 |
| Roger the Pipe Guy (own) | 1 | 13.6 | 3,387 | 23:29 | 144 | 39.9 | 7.7 | 0.9 | 2.7 | 15.0 | 0.6 | 1.8 | 134 | 55 | 61 | – |

| Group | $ figures /1k words (median) | $ figures + vague money phrases /1k (median) | Videos 12 min or longer |
|---|---|---|---|
| Real people | 0.5 | 0.5 | 10 of 25 |
| Faceless / persona | 5.9 | 5.9 | 8 of 10 |
| Roger (own) | 4.4 | 4.4 | 1 of 1 |

**Against the plumbing study (same measures)**

| Measure | HVAC real people (25) | HVAC faceless / persona (10) | Roger's HVAC video | Plumbing figure (file) |
|---|---|---|---|---|
| Length | 11:25 | 13:51 | 23:29 | own 30 videos 18:30, competitors 13:06 (`03-own-vs-competitors.md`, pooled); Roger's hits 18:24-23:09 (`stats.md`) |
| Words per minute | 187 | 159 | 144 | own 156, competitors 174.5 (`03`); Roger's hits 138 (`stats.md`) |
| "you/your" /1k | 44.6 | 43.1 | 39.9 | own 28.2-32.4, TheCheapFix 32.3, Silver Cymbal 49.5, Wakefield 51.6 (`03`); Roger hits WfAwg1l0xCE 41.0, YjPAVZAffh0 42.9 (`tests/iterations/iter-04/test-run-02/comparison/roger-hit.md`) |
| "I/me/my" /1k | 14.8 | 8.0 | 7.7 | own 5.3-8.8, TheCheapFix 0.5, face channels 15.2-25.1 (`03`) |
| "but" /1k | 5.6 | 3.0 | 0.9 | Silver Cymbal's LED video 20.0, Wakefield 7.0, Got2Learn 2.4, Arrow 1.1, test run 02 1.0 (`tests/iterations/iter-04/test-run-02/comparison/real-creators.md`) |
| Viewer questions /1k | 0.6 (the 9 punctuated: 1.2) | 0.9 | 2.7 | Silver Cymbal 6.7, Wakefield 5.7, Arrow 11.5 (`real-creators.md`); Roger hits 2.0 and 0.7 (5 and 2 questions, `roger-hit.md`) |
| Dollar figures /1k | 0.5 | 5.9 | 4.4 | TheCheapFix 5.6, Roger 3.6, Mark 3.0, Wakefield 2.7, Vintage 2.6, Got2Learn 1.4, Silver 0.3, Arrow 0.2 (`03`, "Prices") |
| Dollar figures /min | 0.1 | 1.0 | 0.6 | not measured; my conversion of `03`'s rates at each channel's pace: TheCheapFix about 1.0, Roger about 0.55 |
| Numbers /min | 1.9 | 3.5 | 1.8 | not measured as such; measurements per 1,000 words 1.6-5.4 (`07-body-craft.md` §4) |
| Hook | 81 w / 25 s | 168 w / 60 s | 134 w / 55 s | own 62.5 s, competitors 30 s (`03`); Roger hits 180 w / 65 s (`stats.md`) |
| First real value | 0:30 | 1:26 | 1:01 | own 1:14, competitors 0:38 (`03`); Roger hits 1:34 (`stats.md`) |
| Item one (lists) | 0:50 (8 lists) | 1:07 (7 lists) | – | plumbing pack "first tip by": never-do 30-45 s, mistakes 15-30 s (`SKILL.md`, "The video types") |

What the side by side shows (measured): the HVAC faceless winners sit where the plumbing own channels sat on pace (159 against 156 wpm) and first person (8.0 against 5.3-8.8), well above them on "you" (43 against 28-32), and next to TheCheapFix on money (5.9 dollar figures per 1,000 against 5.6). They are slower to the first value than the plumbing own channels (1:26 against 1:14) and far slower than the HVAC real people (0:30). Nobody in the HVAC set reaches Silver Cymbal's 20 "but"s per 1,000 from the plumbing LED video: Silver's own two HVAC videos run 4.0 and 12.0, and 12.0 is the HVAC maximum. Roger's HVAC video is longer than all five Roger plumbing hits (18:24-23:09), close to their pace (144 against 138 wpm), and has the second-lowest "but" rate in the set (0.9; Ray `fHAlfm21vYw` 0.8).

---

## 2. Openings

### 2.1 Every opening, first 30 seconds

Quotes are verbatim from the transcript, trimmed with "…" (auto-caption spelling kept: "hbac", "which on"). "What it does" lists the jobs in the order they come, my reading. Times are the start of the caption line. Rows run by type, highest multiple first within a type.

| Type | Video | × normal | First ~30 s (verbatim, trimmed) | What it does, in order | Hook w / s | First value | Tease / name |
|---|---|---|---|---|---|---|---|
| Seasonal | Ray `dOZ-8__G4uU` | 147.9 | "…in a few weeks when you finally go to shut it down for the season, you have got a choice to make and it is worth about a couple thousand dollars. Do it the way most folks do, throw a cover over it, cut the power to it, walk away feeling responsible…" | season clock and stake (sentence 1) → the usual way ends with "the compressor" → reassurance ("wakes up next season like nothing ever happened") → name and tenure [0:37] → villain ("the same companies that mail out that spring repair quote") → "Cheapest fix first." (no count) | 172 / 50 | 0:58 | name [0:37] |
| Seasonal | Ray `fHAlfm21vYw` | 113.7 | "Sometime in the next few weeks, on the first cold night, you're going to walk to the thermostat, slide it from cool to heat… You'll just trust it. That trust is the most profitable week in the heating business." | season scene → villain [0:18] → tenure [0:29] → count line [0:36] ("five furnace mistakes") → "Two are 10-minute fixes" → numbered tease with $8,000 | 160 / 50 | 1:08 | last item teased [0:42] |
| Seasonal | DIY HVAC Guy `mP0IjyvQtxw` | 30.2 | "Every single fall, millions of people make the same exact HVAC mistakes, and the worst part is they don't realize it until it's too late. Maybe your furnace doesn't turn on… the first cold day of the year… pay a professional thousands of dollars…" | subject (not the fix) → two symptoms → cost in words, the pro → count line [0:20] → reassurance "can be avoided very easily" | 137 / 36 | 0:44 | "stay tuned for all five" [0:31] |
| Seasonal | Everyday HR `--A2I2s7aNw` | 7.2 | "how's it going you guys it's Scott with everyday home repairs and today I want to run you through how to do a furnace tune-up now you should be doing this yearly whether you're doing yourself trying to save 75 to 125 dollars or you're calling in a professional…" | name → subject → money range → a pro will show you | 90 / 25 | 0:28 | name [0:00] |
| Mistakes | HVAC Guide `Unx9Ze10N98` | 190.8 | "what is the biggest HVAC mistake we see made in the winter time in today's video we're going to talk about some of those mistakes… and the last one will be the thing I think that affects your safety and your pocketbook the most so let's dive into this six big mistakes…" | question (answered at the last item) → numbered tease → count line ("six"; the title says 5) → item one [0:17] | 63 / 17 | 0:19 | last item [0:08] |
| Habits | Ray `K2jCz3D5z_0` | 135.5 | "It's a 100° outside… it still reads 77. Not 72 where you set it, 77. So, you do what anybody would do. You reach for the phone… Before you make that call, let me save you the money. There are five things people do at that little box on the wall…" | scene → stop before the call → count line [0:27] → bill, wear and villain ("the easiest paycheck they'll write all summer") → "Two of them are probably happening in your house right now" → tenure | 164 / 63 | 1:13 | none |
| Mistakes | Ray `qbWN3OViWxQ` | 70.7 | "Right now, on the hottest afternoon of the year, you're doing at least two things to your air conditioner that the company who services it is quietly hoping you never stop." | point and villain in sentence 1 → name and tenure [0:20] → sequel line → count line → numbered tease with "eight to twelve thousand dollars" | 165 / 57 | 1:00 | "saved the biggest for last" [0:48]; name |
| Doing it wrong | Ray `UdyqMC1GVxQ` | 16.9 | "It's a Saturday morning… go at the side of that unit like you're washing mud off a truck… The homeowners who wreck their air conditioners aren't the ones who ignore them. It's the responsible ones…" | scene → blame turned onto the careful → "turns a free chore into a $900 one" → tenure → three-part promise → $6 tool tease | 215 / 74 | 1:42 | "stick around… $6 tool" [1:14] |
| Mistakes | Funny Carpenter `_g8gQ1gg1FM` | 5.8 | "There are a million furnace filter out there. Cheap ones versus expensive ones. Which ones are better for the air quality in your home? And are the expensive ones actually costing you more electricity than you thought?" | subject → two questions → tenure (30 years) → count line [0:12] → item five [0:21] | 66 / 21 | 0:28 | none |
| Symptom | grayfurnaceman `yJxDc90hs4g` | 781.4 | "Okay, wake up in the morning. It's cold. Of course, first thing I'm going to do is go to the thermostat… it's all blank. There's nothing going on. Okay. One of two issues." | the symptom as a first-person scene → first check | 48 / 19 | 0:26 | none |
| Symptom | Word of Advice `3Jonl_TLkpE` | 140.7 | "Hey guys, Jay here with Word of Advice TV. Today I want to go over the most common furnace problem. So on average… every six furnace calls, one of them is guaranteed to be this problem. So to begin with, take off the top door on your furnace." | name → subject → how common it is → first step (the part, a flame sensor, named at [1:52]) | 37 / 11 | 0:11 | name [0:00] |
| Symptom | Silver Cymbal `_b6p0fkWhCY` | 52.5 | "if your air conditioning system isn't working the way it used to I'm gonna give you three tips that you can do at home yourself you don't need any special tools…" | symptom and count in sentence 1 → reassurance → tease → before-reading | 69 / 15 | 0:17 | "stay tuned" [0:13] |
| Symptom | Everyday HR `sRvH-io-ZtA` | 9.2 | "it's Scott with everyday home repairs I'm going to show you quickly how to troubleshoot and solve a problem where your furnace is turning on and then quickly off… out of the last five failures I've had in my rental properties two of those failures have been this exact issue…" | name → symptom → "you're going to be able to troubleshoot this yourself" → own story, "ten dollars in parts" | 134 / 35 | 0:37 | name [0:00] |
| Outage / cheap part | DIY HVAC Guy `y07w1hiKIrI` | 106.0 | "hey guys and welcome back to the channel… a much more simplified way of getting power to your furnace in the event of an emergency now most of you homeowners who have gas furnaces if you look by your furnace you more than likely will just see a little switch like this…" | greeting and sequel → subject → look at your own furnace → "100% the easiest and cheapest method" → parts | 140 / 41 | 0:48 | channel greeting |
| Cheap part | Word of Advice `1bRsFAMgZRQ` | 74.9 | "Hey guys, Jay here with Word of Advice TV. And today I want to go over the furnace igniter… On gas furnaces, there's pretty much just four types of igniters." | name → subject → first fact | 28 / 8 | 0:08 | name [0:00] |
| Cheap part | DIY HVAC Guy `Is0pv2Qnza0` | 60.4 | "…possibly the biggest scam that happens in the hbac industry every single summer… this is a capacitor… I've heard of people being charged $2,000 to replace this piece and guess how much it is $10…" | villain (sentence 1) → part named [0:11] → price gap as a question → "I don't know how these guys sleep at night" → "how to do it safely" | 143 / 46 | 0:48 | none |
| Cheap part | How To Home `i8nDBZo6XyE` | 8.1 | "in this video I'm going to show you how I go about diagnosing and repairing what is most definitely one of the most common service calls… so let's go ahead and Jump Right In let's go" | plain announcement (the part unnamed until [0:59]; the title's $400 and $11.72 not said) → first step | 53 / 14 | 0:14 | none |
| Brand verdict | HVAC Exposed `QKPPm6M0__o` | 1,055.6 | "In 2015, Lennox Industries settled a class action lawsuit for selling air conditioners with coils that were chemically designed to rot from the inside out… while you paid $2,000 to refill a system…" | a named maker as villain, as a dated fact → a commenter's story → "That is an illusion." → count and promise [1:20] → "We spent 3 months cross-referencing…" | 260 / 100 | 1:51 (brand 1 at 6:58) | none |
| Brand verdict | Vent Exposed `86S3ITbfzQY` | 601.5 | "A $14,000 Trane air conditioning system and an $11,000 American Standard air conditioning system roll off the same production line… The only difference is the sticker on the cabinet. That's not an opinion." | verdict fact (sentence 1) → source → "54 brand names… eight actual manufacturers" → contractor as villain → three-part promise | 185 / 66 | 1:09 | "By the end of this video" [0:50] |
| Brand verdict | Atlas AC `r_uP9itJ0HQ` | 88.6 | "buying a new AC system could be a headache… contractors telling you which brand is the best… but which on should you go with and which one should you stay away from hi this is Kenneth with Atlas AC…" | problem → question → name [0:18] → like ask [0:31] → climate disclaimer → own-brand disclosure | 100 / 31 | 1:17 (verdict 12:01) | name; "watch this to the end" [2:28] |
| Brand verdict | DIY HVAC Guy `x2BK-zr4raE` | 32.0 | "If you're thinking about replacing your HVAC system in the near future, I want to share some critical information… brands that I dislike and that I like… ways that you can save money…" | who it's for → two-part promise → first fact (two ways to buy) | 77 / 21 | 0:21 (verdict 3:36) | none |
| Outage | Provident Prepper `erq-QuCN0G0` | 73.4 | "do you know how to stay warm during a winter power outage hi i'm jonathan and i'm ben… the grid has become increasingly unreliable… we turned off our power in the middle of winter just to see if we could survive" | question → names → the threat → own test → count "six secrets" [0:31] | 140 / 57 | 1:06 | names [0:16]; "stay with us" [0:41] |
| Outage | DIY HVAC Guy `Qx3cC1y23JY` | 60.4 | "Did you know that you can turn your car into a generator? A lot of folks don't want to spend $500 or $1,000 on a power station or a generator, but for less than $200…" | question that is the point → price gap → scope ("any vehicle") | 63 / 21 | 0:23 | none |
| Outage | Lost Survival `rX4eyZaHAjw` | 55.6 | "When the furnace quits on a January night, the house doesn't go cold all at once. It goes room by room. You feel it at the windows first… Your grandparents knew that feeling well." | scene → grandparents → "a cheap cousin sitting on a Walmart shelf… under $10" → open loop on item 1 → 1936 story (~150 w) → count line [1:39] | 150 / 49 | 1:49 | top item [0:41] |
| N things | DIY HVAC Guy `SkLMRM9NnBY` | 68.3 | "what's up guys welcome back to the handyman for hire YouTube channel I have recently noticed that many of you viewers like my heating uh furnace replacement videos…" | channel news (~40 s) → "save thousands and thousands of dollars" → count line → "very easy" | 171 / 60 | 1:00 | channel greeting |
| N things | How To Home `AQQH9QwC46A` | 11.1 | "so in this video I'm going to go over some of the top things that AC companies do not want you knowing how to do or that you're even allowed to do them so let's go ahead and Jump Right In…" | villain (sentence 1) → item one [0:10] (no count; 4 of the title's 5 delivered) | 42 / 10 | 0:23 | none |
| Drain fix | Deanin' `dRL13JlclhM` | 818.5 | "hey do you guys have a clogged AC drain and you need to get it flushed you don't want to call a professional this little tool can save you hundreds let me show you exactly how to use it…" | question (yes or no, about the viewer's drain) → the pro → the tool, unnamed, and "hundreds" → greeting → symptoms → tease | 57 / 15 | 0:57 | "stay tuned to the end" [0:43] |
| Drain fix | Silver Cymbal `qAxJb0J1HH0` | 46.0 | "if you want a central air-conditioning system this could be one of the most important videos you'll ever watch because at one point or another you're gonna get a clogged drain line… water stains and your ceiling…" | stakes → symptom on screen → cause → "a couple quick fixes" | 118 / 29 | 0:30 | none |
| Upsell exposé | grayfurnaceman `X3Y-yA42UBk` | 192.6 | "this series of videos is about hbac scams I was a service tech for 35 years I worked with a lot of people that did good work… that's not what this is about this is about those few that take advantage…" | subject → tenure → fairness to the trade → villain scoped to "those few" → the scam named [0:46] | 81 / 37 | 0:55 | none |
| Myth-bust | HVAC Exposed `l2yyfYpcwpQ` | 640.9 | "You're standing in Home Depot, filter aisle, dozens of options. On the left, the cheap ones, five bucks… On the right… Filtrete, 25, $30… What's another 20 bucks for cleaner air?" | scene → question → "a mistake that could cost you $2,000" → point "It's strangling it." [0:44] → "a homeowner I'll call David" | 120 / 50 | 1:40 | none |
| Myth-bust | Ray `_ZgVjFpBnQA` | 93.1 | "You're standing in the filter aisle… Down low sit the cheap ones, five or six dollars… sit the expensive ones, $30 in purple and black packaging…" | the same scene → name and tenure [0:43] → villain → held-back "two ratings" → "Stick with me to the end" → point [1:49] | 260 / 100 | 1:49 | name; end tease [1:15]-[1:35] |
| Hidden cause | RenoVision `J95l9Ue4224` | 24.9 | "hey guys Jeff here and welcome to my 1974 home… today's project we are actually insulating our Rim joist… we're going to show you the good the better and the best option" | name → subject → three-rung ladder → first fact | 60 / 13 | 0:22 | name [0:00] |
| Ranked verdict | Project Farm `RkjRKIRva58` | 2.5 | "Replacing that furnace filter every 30 days can get very expensive. So, the question is, are cheap filters just as good as the more expensive ones?… We've got about 14 different filters to test today…" | cost → two questions → count (14) → the four tests listed | 123 / 33 | 1:21 | none |
| Decision | Tech Connections `7J52mDjZzto` | 2.5 | "Well, I'm pumped. What if I were to tell you that all of the energy you need to heat your home on a cold winter day could be found… outside?… Sounds impossible at first, doesn't it?" | pun → question with the answer inside → disbelief named and answered → first fact | 190 / 63 | 0:37 | none |
| Never-do | Tech Connections `HnMuNCl7tZ8` | 1.5 | "you've probably heard from all sorts of people that electric space heaters are dangerous things… and it is true… however likely not in the ways you imagine… this cheap plastic heater which cost less than 20 bucks has multiple safety devices…" | belief → conceded → flipped (the point) → "very stupid things which nobody should ever repeat" [0:38] | 97 / 38 | 1:36 | none |
| Single-product fix (own) | Roger `cFYptbCvNjI` | 13.6 | "Go stand in the middle of your house and count the things that make water… Now, here is the one you missed. Right now, on a muggy August afternoon, the appliance moving the most water in your house is your air conditioner." | go-look → the reveal [0:21]-[0:30] → stakes ("that is exactly why ceilings come down in August") → name [0:55] → three promises, one held back | 134 / 55 | 1:01 (vinegar named 5:04, dose 8:46) | name; held-back part [1:22] |

### 2.2 What the openings share (measured counts, reading of jobs)

| Job in the opening | Real people (25) | Faceless / persona (10) | Roger |
|---|---|---|---|
| Title's subject named in the first sentence (after any greeting) | 22 (not How To Home `i8nDBZo6XyE`, part unnamed until [0:59]; DIY HVAC Guy `SkLMRM9NnBY`, 40 s of channel news; DIY HVAC Guy `Is0pv2Qnza0`, "this right here" until [0:11]) | 10 | no (the AC at [0:30], vinegar at [5:04]) |
| The fix, answer or verdict fact itself in the first sentence | 3 (`Qx3cC1y23JY`, `7J52mDjZzto`, `HnMuNCl7tZ8`) | 2 (Vent Exposed, HVAC Exposed `QKPPm6M0__o`) | no |
| Opens on a second-person scene ("You're standing in…", "It's a Saturday morning…") | 0 (grayfurnaceman `yJxDc90hs4g` opens on a first-person one) | 7 | a go-look line |
| A question in the first 30 s | 9 | 1 (HVAC Exposed `l2yyfYpcwpQ`) | 0 |
| The trade or a company as villain in the first 60 s | 3 plain (`Is0pv2Qnza0`, `AQQH9QwC46A`, grayfurnaceman `X3Y-yA42UBk` scoped to "those few"), 3 soft (Atlas, Deanin', `mP0IjyvQtxw`) | 7 | 0 |
| Reassurance or honest scope | about 10 | 3 (`dOZ-8__G4uU`, `fHAlfm21vYw`, `UdyqMC1GVxQ`) | 0 |
| Count line, list videos | 6 of 8 (not How To Home `AQQH9QwC46A`, Everyday HR's steps) | 6 of 7 (not Ray `dOZ-8__G4uU`) | – |
| Dollar figures before the first value: none / one / two or more | 20 / 2 / 3 | 1 / 4 / 5 | none |
| Name intro in the first minute | 7 (Atlas, Everyday HR ×2, RenoVision, Word of Advice ×2, Provident Prepper), plus 3 channel greetings | 3 (Ray `_ZgVjFpBnQA` [0:43], `dOZ-8__G4uU` [0:37], `qbWN3OViWxQ` [0:20]) | yes, [0:55] |
| Tenure number in the first minute | 2 (grayfurnaceman 35, Funny Carpenter 30) | 6 (Ray, "25 years", all six) | no |
| Forward tease in the first ~2.5 min | 6 | 6 | 1 |
| First real value by 45 s | 16 | 0 (fastest [0:58], Ray `dOZ-8__G4uU`) | no ([1:01]) |

**Teases (all 13, verbatim).** *Vague:* Deanin' [0:43] "I need you to stay tuned to the end because I got another tip for you"; Silver Cymbal `_b6p0fkWhCY` [0:13] "stay tuned and I'll show you more"; DIY HVAC Guy `mP0IjyvQtxw` [0:31] "make sure and stay tuned for all five of these reminders"; Provident Prepper [0:41] "stay with us"; Atlas AC [2:28] "closer to the end of the video I'm going to give you my top picks so you are going to want to watch this to the end"; Ray `_ZgVjFpBnQA` [1:15]-[1:35] "There's one more piece I've saved for the end… Stick with me to the end". *With a concrete payoff:* HVAC Guide [0:08] "the last one will be the thing I think that affects your safety and your pocketbook the most"; Ray `qbWN3OViWxQ` [0:48] "I saved the biggest for last because it's the one that costs eight to twelve thousand dollars"; Ray `fHAlfm21vYw` [0:42] "The last one is why a furnace that should last 20 years dies at 12"; Ray `UdyqMC1GVxQ` [1:14] "stick around because there's a $6 tool that undoes most of it"; Lost Survival [0:41] "the item at the very top of this list won't make your house 1° warmer. And it's still the one I'd buy first."; Vent Exposed [0:50] "By the end of this video, you'll know the only four brands worth buying in 2026"; Roger [1:22] "before we are done, I am going to tell you about a small part". No tease at all in grayfurnaceman `yJxDc90hs4g` (781×), Word of Advice `3Jonl_TLkpE` (141×), HVAC Exposed's brand video (1,056×) or Ray's two highest multiples (`dOZ-8__G4uU` 148×, `K2jCz3D5z_0` 135×); Deanin' (818×) has a vague one.

### 2.3 Patterns by video type (best examples by multiple)

**Seasonal checklist (4).** Three open on the season's clock in the second person: "in a few weeks when you finally go to shut it down for the season" (Ray `dOZ-8__G4uU`, 148×, his highest), "on the first cold night" (Ray `fHAlfm21vYw`, 114×), "Every single fall" (DIY HVAC Guy `mP0IjyvQtxw`, 30×). Ray's two put the stake into the first 20 s ("it is worth about a couple thousand dollars" [0:00]; "That trust is the most profitable week in the heating business" [0:18]) and reach the first tip at [0:58] and [1:08]. `dOZ-8__G4uU` is the only Ray video with no count line ("Cheapest fix first." [0:49]). Everyday HR's tune-up opens on a name and a money range and is fast to value ([0:28]) but sits at 7.2× on its channel.

**Mistakes, habits, doing it wrong (5).** All four lists say a count by [0:36]; Ray's "doing it wrong" is an argument with no count. HVAC Guide (191×) opens on a question it answers at the last item, teases that item at [0:08] and is into mistake one at [0:17]. Ray's two lists (`K2jCz3D5z_0` 135×, `qbWN3OViWxQ` 71×) both say how many of the mistakes are going on in the viewer's house now ("Two of them are probably happening in your house right now" [0:45]; "Two of them you're doing this very second" [0:47]). The Funny Carpenter (5.8×) asks two questions in the first 7 s and starts item five at [0:21]. Ray's lowest multiple (`UdyqMC1GVxQ`, 16.9×) has his longest hook of the six apart from the filter video (215 w / 74 s).

**Symptom diagnostic (4).** The shortest openings in the set: 11-35 s, 37-134 words, first step at [0:11]-[0:37], no villain in any, a tease in one. The two highest multiples open on the symptom itself: "Okay, wake up in the morning. It's cold." (grayfurnaceman `yJxDc90hs4g`, 781×) and "the most common furnace problem… every six furnace calls, one of them is guaranteed to be this problem" (Word of Advice `3Jonl_TLkpE`, 141×; first step [0:11], though the part, the flame sensor, is named only at [1:52]).

**Cheap part (4, with the outage part).** Only DIY HVAC Guy `Is0pv2Qnza0` (60×) opens on the price gap and the villain: "I've heard of people being charged $2,000 to replace this piece and guess how much it is $10" [0:23]. His bigger multiple, `y07w1hiKIrI` (106×), has no villain and no price in the hook and opens on a channel greeting; it sends the viewer to his own furnace ("if you look by your furnace you more than likely will just see a little switch like this"). How To Home's "Was Quoted $400. I Fixed It For $11.72!" says neither price in its spoken hook.

**Brand verdict (4).** The two faceless winners open on a fact that is already half the verdict: a dated lawsuit against a named maker (HVAC Exposed, 1,056×) and "roll off the same production line… The only difference is the sticker on the cabinet" (Vent Exposed, 602×). Both then hold the list: brand one at [1:09] (Vent) and at [6:58], 57% in (HVAC Exposed). The two human ones open on the buyer's confusion and hold the verdict to [3:36] (DIY HVAC Guy, 32×) and [12:01] (Atlas, 89×, after a name intro, a like ask and two disclaimers in the first minute).

**Outage (4).** Questions open two: "Did you know that you can turn your car into a generator?" (DIY HVAC Guy `Qx3cC1y23JY`, 60×; the point and the question in one sentence, then "$500 or $1,000… for less than $200") and "do you know how to stay warm during a winter power outage" (Provident Prepper, 73×). Lost Survival (56×) opens on a scene ("the house doesn't go cold all at once. It goes room by room.") and spends about 150 more words on a 1936 cold wave before item 15 at [1:49].

**N things / insider (2).** How To Home `AQQH9QwC46A` (11×) puts the villain in its first sentence ("things that AC companies do not want you knowing how to do") and is into item one at [0:10]; it says no count and delivers four of the title's five. DIY HVAC Guy `SkLMRM9NnBY` (68×) spends 40 s on channel news first.

**Drain fix (2).** Deanin' (818×) opens on a yes-or-no question about the viewer's own drain, plus the pro and money in words ("you don't want to call a professional this little tool can save you hundreds"), then spends 40 s on a greeting, symptoms and a tease before the first step at [0:57]. Silver Cymbal (46×) opens on stakes and the symptom on screen (ceiling stains); first fix at [0:30].

**The rest (one each)** are in the table above; the one shape not seen elsewhere is grayfurnaceman's fairness line before the villain ("I worked with a lot of people that did good work… this is about those few that take advantage" [0:06], 193×).

---

## 3. Item lengths in list videos

| Channel | Video | Items | Words per item (each, in spoken order) | Shortest | Median | Longest | Median s | $ figures per item | Items with a $ figure | Most in one item |
|---|---|---|---|---|---|---|---|---|---|---|
| Everyday HR | `--A2I2s7aNw` | 4 | 71, 281, 534, 325 | 71 | 303 | 534 | 104 | 0, 0, 1, 0 | 1 of 4 | 1 |
| How To Home | `AQQH9QwC46A` | 4 | 436, 567, 1133, 502 | 436 | 534 | 1133 | 142 | 3, 0, 0, 2 | 2 of 4 | 3 |
| HVAC Exposed | `QKPPm6M0__o` | 5 | 62, 99, 78, 85, 160 | 62 | 85 | 160 | 41 | 0, 0, 0, 0, 1 | 1 of 5 | 1 |
| HVAC Guide | `Unx9Ze10N98` | 6 | 139, 164, 112, 124, 112, 589 | 112 | 132 | 589 | 37 | 0, 0, 0, 0, 0, 0 | 0 of 6 | 0 |
| Lost Survival | `rX4eyZaHAjw` | 15 | 232, 250, 233, 217, 225, 251, 246, 233, 279, 245, 199, 214, 224, 213, 244 | 199 | 233 | 279 | 76 | 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0 | 4 of 15 | 1 |
| Ray Dutton | `K2jCz3D5z_0` | 5 | 494, 206, 305, 356, 374 | 206 | 356 | 494 | 138 | 3, 0, 2, 1, 0 | 3 of 5 | 3 |
| Ray Dutton | `dOZ-8__G4uU` | 3 | 320, 518, 704 | 320 | 518 | 704 | 161 | 0, 0, 4 | 1 of 3 | 4 |
| Ray Dutton | `fHAlfm21vYw` | 5 | 358, 224, 387, 348, 295 | 224 | 348 | 387 | 121 | 2, 4, 2, 0, 0 | 3 of 5 | 4 |
| Ray Dutton | `qbWN3OViWxQ` | 5 | 266, 279, 340, 373, 435 | 266 | 340 | 435 | 131 | 0, 1, 0, 4, 1 | 3 of 5 | 4 |
| Silver Cymbal | `_b6p0fkWhCY` | 3 | 151, 237, 1163 | 151 | 237 | 1163 | 74 | 0, 0, 1 | 1 of 3 | 1 |
| DIY HVAC Guy | `SkLMRM9NnBY` | 3 | 408, 465, 1008 | 408 | 465 | 1008 | 160 | 0, 0, 2 | 1 of 3 | 2 |
| DIY HVAC Guy | `mP0IjyvQtxw` | 5 | 533, 751, 413, 702, 561 | 413 | 561 | 751 | 164 | 0, 0, 0, 1, 0 | 1 of 5 | 1 |
| Funny Carpenter | `_g8gQ1gg1FM` | 5 | 76, 245, 161, 148, 244 | 76 | 161 | 245 | 50 | 0, 0, 0, 0, 0 | 0 of 5 | 0 |
| Provident Prepper | `erq-QuCN0G0` | 6 | 333, 344, 280, 90, 133, 201 | 90 | 240 | 344 | 74 | 0, 0, 0, 0, 0, 0 | 0 of 6 | 0 |
| Vent Exposed | `86S3ITbfzQY` | 3 | 259, 267, 208 | 208 | 259 | 267 | 103 | 5, 3, 3 | 3 of 3 | 5 |

Not counted as lists: the argued videos (Ray `UdyqMC1GVxQ` and `_ZgVjFpBnQA`, HVAC Exposed `l2yyfYpcwpQ`; sections of about 200-300 words in the notes), the brand videos built as company blocks (Atlas, DIY HVAC Guy `x2BK-zr4raE`), Project Farm (14 filters at about 24 s each in round one and 12 s in round two, per its notes) and the step-by-step repairs. Ray `fHAlfm21vYw` item 5 runs on into its own check ([11:01] the thermometer test, [12:12] "the one sentence"); with those it is about 590 words.

**Measured:**
- **Items are long everywhere.** Of 77 items, 3 fall in 100-130 words, 7 under 100 and 67 over 130. Medians per video: real people 132-561 words, faceless 85-518. The shortest items are HVAC Exposed's brands (62-160, median 85 words, about 41 s; the first 57% of that video is the case against the industry) and HVAC Guide's (112-164 words, about 37 s each for items 1-5, then 589 for the held-back item 6).
- **Shape across the list.** Ray's items grow as the money grows: `qbWN3OViWxQ` 266 → 279 → 340 → 373 → 435; `dOZ-8__G4uU` 320 → 518 → 704 ("Cheapest fix first."). Lost Survival keeps all 15 within 199-279 words. The real people's last or biggest item balloons: Silver Cymbal tip 3 is 1,163 words against 151 and 237; DIY HVAC Guy `SkLMRM9NnBY` #3 1,008 against 408 and 465; HVAC Guide #6 589 against 112-164.
- **Money per item.** Faceless items: 23 of 41 carry no dollar figure, 8 carry one, 10 carry two or more (a floor; see the hand check). Vent Exposed puts 3-5 figures on every item. Real people: 30 of 36 items carry none.

**How items are joined (verbatim).**
- *Ray Dutton: a forward line that names the next item's stake, every item.* "That first one's a switch. This next one is a belief" (`K2jCz3D5z_0` [4:44]); "That's the mistake they bill the most. The next one is the mistake they bill the highest because of when it happens." (`fHAlfm21vYw` [3:01]); "The dollar figures only climb from here and the last one clears 10,000." (`qbWN3OViWxQ` [4:32]); "And the last one, the one I saved for the end, is where that number goes from a couple hundred dollars to the single most expensive part you own." (`dOZ-8__G4uU` [5:53]). Three of his four lists also have a mid-list interlude, and one bridge credits the viewer: "If you just caught yourself, good." (`qbWN3OViWxQ` [2:25]).
- *Lost Survival: forward lines every few items, tied to later items.* "Pay attention to this next one because it changes how the rest of the list works." [9:29]; "we'll come back to why when we get to number one" [10:50]; "the next item is the one people really argue about" [12:07].
- *HVAC Exposed and Vent Exposed: a punch line, then the number.* "Number five. And this is the one they really do not want you to know about." (`QKPPm6M0__o` [9:28]); "I don't say that lightly, but the spec sheet doesn't lie. Number three, Carrier." (Vent [2:50]).
- *Real people: plain numbering,* mostly with no forward line: "Mistake number three, putting the filter in backward." (Funny Carpenter [1:47]); "number two is an interesting one" (HVAC Guide [0:54]); "tip number four is to drink warm liquids" (Provident [6:07]); "step number three is going to be cleaning the furnace" (Everyday HR [3:09]); "Now, while we're out here, I want to talk about mistake number two" (DIY HVAC Guy [3:10]). How To Home repeats the title's villain as its bridge: "the next repair that AC companies don't want you to know how to fix" [2:03].

---

## 4. Length and runtime

| Type | Videos, shortest to longest (length, × normal) |
|---|---|
| Seasonal checklist | Everyday HR 8:56 7.2×; Ray 11:49 147.9×; Ray 14:42 113.7×; DIY HVAC Guy 14:55 30.2× |
| Mistakes / habit / doing it wrong | Funny Carpenter 5:33 5.8×; HVAC Guide 6:43 190.8×; Ray 13:30 16.9×; Ray 14:05 70.7×; Ray 14:27 135.5× |
| Symptom diagnostic | Everyday HR 8:25 9.2×; Silver Cymbal 8:52 52.5×; Word of Advice 8:57 140.7×; grayfurnaceman 10:10 781.4× |
| Cheap part (with the outage part) | DIY HVAC Guy 11:25 60.4×; How To Home 11:40 8.1×; DIY HVAC Guy 11:46 106.0×; Word of Advice 13:08 74.9× |
| Brand / ranked verdict | Vent Exposed 8:12 601.5×; DIY HVAC Guy 9:30 32.0×; HVAC Exposed 12:07 1,055.6×; Project Farm 12:54 2.5×; Atlas 15:23 88.6× |
| Outage | DIY HVAC Guy 7:08 60.4×; Provident 15:09 73.4×; Lost Survival 22:21 55.6× |
| N things / insider | How To Home 12:40 11.1×; DIY HVAC Guy 13:17 68.3× |
| Drain fix | Deanin' 5:51 818.5×; Silver Cymbal 8:09 46.0× |
| Myth-bust / product villain | HVAC Exposed 13:37 640.9×; Ray 15:10 93.1× |
| One each | grayfurnaceman upsell exposé 5:19 192.6×; RenoVision hidden cause 18:20 24.9×; Roger single-product fix 23:29 13.6×; Tech Connections never-do 28:55 1.5×, decision 35:15 2.5× |

**Measured:**
- **Spread:** 5:19 to 35:15. Real people median 11:25 (10 of 25 at 12 minutes or more); faceless median 13:51 (8 of 10); Roger 23:29, longer than every video in the set except Technology Connections' two.
- **Within a channel** (the only fair comparison): Ray's six run 11:49-15:10. His shortest is his highest multiple (`dOZ-8__G4uU`, 11:49, 148×), but his lowest (`UdyqMC1GVxQ`, 16.9×) is 13:30, mid-range. DIY HVAC Guy's longest (`mP0IjyvQtxw`, 14:55) is his lowest (30×) and his highest (`y07w1hiKIrI`, 106×) is 11:46. Of the seven channels with two videos, the longer one is the higher multiple in four and the lower in three; in Ray's six and DIY HVAC Guy's six there is no steady direction. Length and multiple don't line up in this sample.
- **The persona winners cluster at 12-15 minutes** (7 of 10: 12:07-15:10), with two shorter (Vent 8:12, Ray 11:49) and one long (Lost Survival 22:21). Among the real people, the best video of 8 of the 14 channels is under 12 minutes (grayfurnaceman 10:10, Deanin' 5:51, HVAC Guide 6:43, Word of Advice 8:57, DIY HVAC Guy 11:46, Silver Cymbal 8:52, Everyday HR 8:25, Funny Carpenter 5:33).

---

## 5. What the numbers say against the plumbing rules

Where the HVAC winners sit against each rule in the plumbing pack (`plumbing-scripts/SKILL.md`). Description only.

**"The point in the first sentence… by about 15 seconds."** The subject is in the first sentence in 32 of 36 videos, including all 10 faceless ones. The fix, answer or verdict fact is in the first sentence in 5 (`Qx3cC1y23JY`, `7J52mDjZzto`, `HnMuNCl7tZ8`, Vent Exposed, HVAC Exposed `QKPPm6M0__o`). Seven of the 10 faceless winners open on a second-person scene and state the point at [0:41]-[1:49]; the scene openers include Ray's two highest multiples. Roger's own video names its product at [5:04].

**"The first real tip by about 45 seconds; in a list, item one by about 30."** Real people: 16 of 25 by 45 s (median 0:30); in lists, 3 of 8 by 30 s (How To Home [0:10], HVAC Guide [0:17], Funny Carpenter [0:21]). Faceless: 0 of 10 by 45 s (median 1:26; fastest Ray `dOZ-8__G4uU` [0:58], his highest multiple); in lists, 0 of 7 by 30 s (fastest [0:51]). Roger [1:01]. No faceless winner meets this rule; their hooks run 120-260 words.

**"About 100-130 words per item."** 3 of 77 items fall in that band. The median item is 303 words for real people and 250 for the faceless. Only HVAC Exposed's brand list (median 85) and HVAC Guide's first five (112-164) sit near or under it. The highest multiples on their channels run long items: Ray `dOZ-8__G4uU` 320-704, `K2jCz3D5z_0` 206-494; HVAC Guide's held-back item 589.

**"At most one dollar figure per item… figures on no more than about half the items; the opening has one figure at most."** Faceless items: 10 of 41 carry two or more figures (a floor), and Ray's three lists with figures put them on 3 of 5 items each; Vent Exposed puts 3-5 on all 3. Lost Survival (4 of 15 items, never more than one) and HVAC Exposed's brands (1 of 5) sit inside the cap. In the opening, 5 of 10 faceless videos say two or more figures before the first value (HVAC Exposed `l2yyfYpcwpQ` 5, Ray `_ZgVjFpBnQA` 5, Vent 3, Ray `UdyqMC1GVxQ` 2, Ray `qbWN3OViWxQ` 2 as one range); counting a range as one, 4 do. Real people mostly say no figures at all (median 0.5 per 1,000 words; 20 of 25 openings carry none).

**"At least 12 minutes."** Faceless: 8 of 10 meet it; the two that don't (Vent 8:12, Ray `dOZ-8__G4uU` 11:49) are Vent's only measured video and Ray's highest multiple. Real people: 10 of 25. Roger's HVAC video (23:29) is past the plumbing sweet spot of 12-20.

**Also, against "Emotion, all the way through":** the rule asks for much more "but" (it cites Silver Cymbal at about 20 per 1,000) and a viewer question about every two items. The HVAC faceless winners run 0.8-5.9 "but" per 1,000 (median 3.0; Ray 0.8-3.5) and 0-10 questions a video (median 0.9 per 1,000; Ray 0-3). The real people run 2.7-12.0 "but" (median 5.6). "You" is high everywhere (faceless median 43 per 1,000), well above the plumbing own channels' 28-32.

## Limits

- One coder for every reading (the jobs in an opening, the first value, what counts as a list or an item); hook lengths are the helpers' figures, re-counted for words only.
- Question and dollar counts are floors where noted; samples by type are small (often 1-4 videos); multiples compare only within a channel; nothing here measures retention.
