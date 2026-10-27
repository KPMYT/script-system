# HVAC study: round 1 check (2026-10-27)

A second helper re-checked two videos per collector against fresh NexLev pulls made on 2026-10-27 (about 04:05-04:10 UTC). Every existing file was only read; this is the only file written. Tools: `youtube_video_details`, `get_video_transcript`, `youtube_video_comments`, `youtube_channel_videos` (no web search). Scratch work (fresh transcript pulls, the quote-finder script, the comment picks) is in `/tmp/claude-0/-home-user/f63a7813-66f7-513b-a288-eabac2c20b9a/scratchpad/check-r1/`.

**Sample:** A `mP0IjyvQtxw`, `r_uP9itJ0HQ` · B `sRvH-io-ZtA`, `X3Y-yA42UBk` · C `J95l9Ue4224`, `cFYptbCvNjI` · D `qbWN3OViWxQ`, `86S3ITbfzQY`.

## Summary

| Video (collector) | 1 meta vs fresh details | 2 transcript | 3 comments (5 picked) | 3b no names / handles / IDs | 4 notes: 6+ claims | 4b no quality judgments |
|---|---|---|---|---|---|---|
| mP0IjyvQtxw (A) | pass | pass | pass (5/5) | pass | pass | **flag** (1 phrase) |
| r_uP9itJ0HQ (A) | pass | pass | pass (5/5) | pass | **fail** (1 count) | **flag** (1 word) |
| sRvH-io-ZtA (B) | **fail** (owner-comment line) | pass | pass (5/5) | pass | pass | pass |
| X3Y-yA42UBk (B) | pass | pass | pass (4/5, 1 not findable) | pass | pass | **flag** (2 phrases) |
| J95l9Ue4224 (C) | pass | pass | pass (4/5, 1 not findable) | pass | **fail** (hook figure) | pass |
| cFYptbCvNjI (C) | pass | pass | pass (5/5) | pass | pass | pass |
| qbWN3OViWxQ (D) | pass | pass | pass (4/5, 1 not findable) | pass | pass | pass |
| 86S3ITbfzQY (D) | pass | pass | pass (4/4 unique, 1 not findable) | pass | **fail** (2 timestamps) | pass |

| Channel normal (check 5) | Meta / COLLECTION-LOG | Recomputed | Result |
|---|---|---|---|
| The DIY HVAC Guy | 40,551 (hrw0LA9XOZc) | 40,551 (hrw0LA9XOZc) | pass |
| grayfurnaceman | 1,555 (ywDGEZ2IvkY) | 1,555 (ywDGEZ2IvkY) | pass |
| Ray Dutton's Garage | 8,345 (Wn7lGvsvpfY) | 8,345 (Wn7lGvsvpfY) | pass |

**Counts by check:**
- Meta: 7 pass, 1 fail.
- Transcripts: 8 pass.
- Comments: 8 pass. 36 of the sampled comments were found with identical like counts; 4 could not be found because NexLev paging returns the same page again, so none was disproved.
- Privacy: 8 pass.
- Notes facts: 5 pass, 3 fail.
- Quality wording: 5 clean, 3 flagged.
- Normals: 3 pass.

All failures are small: one wrong meta line, one wrong count, one self-contradicting hook figure and two wrong timestamps. No data was found invented. Every quote in all 8 notes was found in its transcript or comments file.

## 1. meta.md against fresh `youtube_video_details`

Upload dates and durations match exactly on all 8. Views moved only by normal growth. Likes are identical on all except mP0IjyvQtxw (+2). Age at collection and views/normal were recomputed and all match.

| Video | Date | Duration | Views (meta → fresh, diff) | Likes (meta → fresh) |
|---|---|---|---|---|
| mP0IjyvQtxw | 2026-09-26 ✓ | 895 s ✓ | 1,226,257 → 1,226,425 (+168) | 9,677 → 9,679 |
| r_uP9itJ0HQ | 2022-11-28 ✓ | 923 s ✓ | 1,873,990 → 1,873,987 (−3) | 40,459 → 40,459 |
| sRvH-io-ZtA | 2022-09-15 ✓ | 505 s ✓ | 2,779,706 → 2,779,783 (+77) | 28,881 → 28,881 |
| X3Y-yA42UBk | 2015-08-31 ✓ | 319 s ✓ | 299,519 → 299,519 (0) | 3,905 → 3,905 |
| J95l9Ue4224 | 2024-12-07 ✓ | 1100 s ✓ | 5,848,497 → 5,848,743 (+246) | 60,524 → 60,524 |
| cFYptbCvNjI | 2026-08-27 ✓ | 1409 s ✓ | 37,083 → 37,083 (0) | 178 → 178 |
| qbWN3OViWxQ | 2026-07-31 ✓ | 845 s ✓ | 589,617 → 589,606 (−11) | 14,609 → 14,609 |
| 86S3ITbfzQY | 2026-05-25 ✓ | 492 s ✓ | 673,134 → 673,134 (0) | 9,411 → 9,411 |

**FAIL: sRvH-io-ZtA meta.md, Comments line.**
- meta.md says: "channel-owner comments: 1 unique (pinned; appears in both lists, marked [OWNER])".
- Its own `comments.md` header says: "No owner comment appeared in either list". The file has no `[OWNER]` tag.
- `data/everyday-home-repairs/COLLECTION-LOG.md` says: "sRvH-io-ZtA: ... owner: none".
- Fresh top and newest pulls show no comment with `authorIsChannelOwner=true`.
- The meta line matches the --A2I2s7aNw entry in the same log ("1 pinned owner comment ... in both lists"), so it looks copied from that video.

## 2. Transcripts

Each fresh `get_video_transcript` pull was compared line by line with `transcript.txt` by script for 7 videos. X3Y-yA42UBk (112 lines) was compared by eye. All 8 match the file **in full**: same segment count, same text, same timestamps, on every line (0 mismatches). That covers the brief's first 3, middle 3 and last 3 lines on each.

| Video | Segments (file = fresh) | Words in file | Words stated in meta |
|---|---|---|---|
| mP0IjyvQtxw | 439 | 3,187 | 3,187 ✓ |
| r_uP9itJ0HQ | 380 | 2,746 | 2,746 ✓ |
| sRvH-io-ZtA | 214 | 1,531 | 1,531 ✓ |
| X3Y-yA42UBk | 112 | 744 | 744 ✓ |
| J95l9Ue4224 | 509 | 3,792 | 3,792 ✓ |
| cFYptbCvNjI | 581 | 3,388 | 3,388 ✓ |
| qbWN3OViWxQ | 351 | 2,318 (whitespace split) | 2,328 |
| 86S3ITbfzQY | 225 | 1,297 | not stated |

The qbWN3OViWxQ difference (2,328 vs 2,318) is a counting method, not an error. Splitting on punctuation as well as spaces gives exactly 2,328, and the earlier niche-research pull `tx_ray2.txt` also counts 2,318 by spaces.

## 3. Comments

**Method:**
- 5 comments per file were picked with a seeded random draw (`random.seed(20261027)`) from the numbered entries of each `comments.md`.
- Each was then looked for in fresh `top` and `newest` pulls. Where it wasn't on page 1, up to 2 more continuation pages were tried.
- "Not findable" means it was absent from every page NexLev returned. On those videos the continuation token returns the same 20 comments again (the known paging fault in `log.md`), so absence does not show the comment is wrong.

| Video | Found, likes match | Not findable | Notes |
|---|---|---|---|
| mP0IjyvQtxw | 5 (3, 8, 8, 37, 0) | 0 | all on page 1 |
| r_uP9itJ0HQ | 5 (13, 0, 335, 1, 77) | 0 | the 77 and the 1 appeared only on the third top page |
| sRvH-io-ZtA | 5 (144, 0, 0, 0, 322) | 0 | |
| X3Y-yA42UBk | 4 (0, 10, 0, 2) | 1: "(1 likes) I usually see cracked exchangers on very old equipment..." | the 2nd top page and the 2nd newest page repeated page 1 |
| J95l9Ue4224 | 4 (227, 13, 12, 0) | 1: "(0 likes) Great tips, definitely a summer project here in the PNW..." | 3 top pages and 1 newest page; the first fresh top page held almost none of the file's top list, so ranking shifts between calls |
| cFYptbCvNjI | 5 unique (32, 2, 0, 0, 0) | 0 | the video has 5 top-level comments; the draw hit 2 duplicates (top/newest), so all 5 unique were checked |
| qbWN3OViWxQ | 4 (80, 44, 86, 0) | 1: "(214 likes) I keep mine at 72 during the day and 68 at night. I live in Arizona..." | the 2nd top page repeated page 1. It is odd that a 214-like comment is missing from a top page that lists 1-like comments; the collector says it came from page 2 or 3. Unverified, not disproved. |
| 86S3ITbfzQY | 4 unique (6, 0, 0, 0) | 1: "(0 likes) FANTASTIC VIDEO" | the draw picked "I have 2 units made by Rudd" twice (top #20 and newest #7, the same comment), so a 5th pick was drawn; the 2nd newest page repeated page 1 |

**Privacy:** pass on all 8 files. There are no @handles, channel IDs (UC…) or author fields in any comment text. The only "@" hit is "@2months" inside a comment in qbWN3OViWxQ, which is ordinary text. The fresh pulls do carry usernames; none of them appears in any file.

Observation, not a failure: three comments end with or address a first name typed by the commenter: "... keep up the good work.   Ken" (mP0IjyvQtxw top #9), "... sense the flame. John" (sRvH-io-ZtA top #5) and "Ditto Chris." (r_uP9itJ0HQ top #17, addressing another commenter). These are not usernames, but the main session may want to strip trailing signatures.

## 4. Notes

Each quoted line was searched for in the transcript by script, across line breaks and with punctuation ignored. Hook word counts were recounted from the transcript. Every transcript quote in all 8 notes was found.

**Timestamps:** the notes cite the line holding most of a quote, so many sit 2-4 s after where the quote starts. For example, mP0 "[9:55] click my favorite HVAC tools" starts at 9:57, and X3Y "[3:16] you want to see the crack" starts at 3:12. These count as pass here. The two below are outside that range.

### mP0IjyvQtxw: pass
1. Hook "~137 w, 36 s, ends [0:36] 'let's hop outside'": 137 words up to "hop", which ends at 0:36. ✓
2. First value "[0:44] mistake number one is covering your air conditioner every fall": at 0:44. ✓
3. CTA "[9:55] click my favorite HVAC tools": starts at 9:57. ✓
4. Safety "[3:52] pulling our disconnect and making sure that there's no power": at 3:50. ✓
5. Emotion "[0:12] your energy bill has skyrocketed for no reason": at 0:12. ✓
6. Comment "Turn power off to the furnace too!! ..." (2 likes): file and fresh both 2. ✓
7. Also: "'Mistake number four' is never said aloud" is confirmed; neither "mistake number four" nor "number four" occurs in the transcript.

**Flag (judgment):** line 23 "tool and detector pitches run long". "Run long" is an evaluation; give the plug lengths instead.

### r_uP9itJ0HQ: fail (1)
1. Hook "~100 w, 31 s": exactly 100 words to "stay away from" at 0:29-0:31. ✓
2. First value "[1:17] there are six major companies...": at 1:17. ✓
3. CTA "[0:35] would you please hit the like button...": at 0:35. ✓
4. Verdict "held to [12:01] (78% in)": 721 s of 923 s is 78.1%. ✓
5. Emotion "[12:41] the homeowner is just done with it": at 12:41. ✓
6. Standout "[3:43] the difference in between carrier and Bryant...": starts at 3:41. ✓

**FAIL:** Pacing says `"So you might be asking" ×4 as bridges`. The transcript has the phrase **3** times: [3:52], [4:30], [5:16]. "you may be asking" and "you might be wondering" occur 0 times.

**Flag (judgment):** line 23 "Hedged, candid". "Candid" is an evaluation; "Hedged" plus the quotes already describe it.

(The transcript's auto-captions write "Lennox" as "Linux" at [12:15]; the notes write Lennox. That is fine for a label, but no quote contains the word, so nothing is misquoted.)

### sRvH-io-ZtA: pass
1. Hook "~134 w, 35 s (ends [0:35] 'how to troubleshoot them')": 134 words in 0:00-0:35. ✓
2. First value "[0:37] a key to troubleshooting is getting a baseline...": starts on the [0:35] line. ✓
3. Prices "just ten dollars in parts" [0:27] and "three or four packs for about 15 on Amazon" [6:28]: both at those times. ✓
4. Safety "[1:19] ... should be off if you're poking around inside your furnace": at 1:19. ✓ "[3:47] ... as a safety protocol": at 3:44. ✓
5. CTA "[8:13] check out this video right here": at 8:10. ✓
6. Comment "2:00AM, two days after Christmas ... You kept my family warm" (322): fresh 322. ✓

### X3Y-yA42UBk: pass
1. Hook "~81 w, ~37 s (first segment [0:06]; ends [0:43])": 81 words in 0:00-0:43. ✓
2. First value "[0:55] now there's some truth in this...": starts at 0:52. ✓
3. Safety "[3:31] carbon monoxide not carbon dioxide monoxide is a poisonous gas": at 3:31. ✓
4. Emotion "[0:38] sometimes scare them to death": at 0:38. ✓
5. CTA "[5:00] if you have questions or comments...": at 5:00. ✓
6. Comment "I recommend having co detectors in any home..." (19): fresh 19. ✓
7. Also: "744 words in 5:19" matches the transcript (744).

**Flag (judgment):**
- Line 14 "Claim, then the honest version, then the test to ask for": "the honest version" judges truthfulness.
- Line 23 "Plain, fair to the trade": "fair" is an evaluation. Quoting "a lot of people that did good work" alone would describe it.

### J95l9Ue4224: fail (1)
1. First value "[0:22] one piece of insulation that filled the space": at 0:22. ✓
2. Prices "[17:10] it's $1,200 and it guarantees me an air seal": at 17:10. ✓
3. Safety "[5:24] foam must be applied in layers to avoid overheating or combustion": at 5:24. ✓ The claim "No respirator ... lines" is confirmed: "respirator" and "mask" do not occur.
4. Emotion "[13:39] you can pay for it for the rest of your life with energy bills...": at 13:39. ✓
5. CTA "None spoken beyond the sign-off 'cheers till next time' [18:17]": at 18:17. ✓
6. Comments "Isocyanates and their catalysts are toxic, carcinogenic" (2K) and "Love those safety contact lenses" (13): fresh 2K and 13. ✓

**FAIL:** the hook line "Hook: 75 w, 16 s (ends [0:11] 'we're going to show you the good the better and the best option')" contradicts itself. That phrase ends on the [0:11] line at about 0:13, after **60** words. 75 words / 16 s runs on to "[0:13] been a lot of things that have uh / [0:15] changed over the years so let's just". Either the figure or the end-point is wrong.

### cFYptbCvNjI: pass
1. Hook "134 w, 55 s (ends [0:51] 'that is exactly why ceilings come down in August.')": 134 words in 0:00-0:55; "August." is at 0:54. ✓
2. First value "[1:01] takes 90 seconds, costs about $4 for the whole cooling season": at 1:01. ✓
3. CTA "[23:08] 'subscribe to Roger the plumber guy'": at 23:08. ✓ Book title "100 Old House Fixes That Save You Thousands": at 6:46 and 22:24. ✓
4. Safety "[11:30] Never combine bleach and vinegar." and "[11:39] Bleach mixed with an acid gives off chlorine gas.": at 11:30 and 11:38. ✓
5. Emotion "[15:50] it is deeply satisfying": at 15:50. ✓
6. Comments "5 unique of 6": API commentsCount 6, 5 returned. ✓ The top comment (32 likes) is quoted correctly.

### qbWN3OViWxQ: pass
1. Hook "~165 words, ~57 s; ends 'they'll smile the whole way there' [0:53]": 169 words up to "there." at 0:55. ✓
2. First value "[1:00] #1 cranking the thermostat to 60": "Number one, cranking the thermostat way down" on [0:59]-[1:01]. ✓
3. CTA "[13:13] comments ... because I read every one": the phrase is at 13:18 inside the [13:13] block. ✓ "[13:31] hit subscribe" and "[14:00] Keep your cool": both exact. ✓
4. Safety "Refrigerant is licensed work..." [8:19] and "This is a call a professional, full stop." [8:29]: both exact. ✓
5. Emotion "never, ever sign under a countdown clock" [12:28]: exact. ✓
6. "No book line in the narration": confirmed; "raydutton", "book" and "guide" occur 0 times.
7. "Sounds like AI: 4" quotes: 80, 63 and 4 likes match fresh top; 0 matches fresh newest. ✓

### 86S3ITbfzQY: fail (2 timestamps)
1. Hook "~185 words, ~66 s ... ending 'selling you engineering or selling you a logo' [1:05]": 186 words in 0:00-1:07. ✓
2. First value "[1:09] #1 and #2, Trane and American Standard": at 1:09-1:14. ✓
3. CTA "[4:41] If you've made it this far, hit subscribe." and "[7:08] Drop the brand you'd never buy again...": both exact. ✓
4. Emotion "If that number makes your chest tight, keep listening" [4:34]: exact. ✓
5. Prices "$200 service call and a $1,600 part swap" [2:37] and "12 to $15,000" [4:31]: both exact. ✓
6. Comments "Good information, but AI fucking slop. stop it." (0) and the two ARS comments (29, 34): fresh 0, 29 and 34. ✓
7. Also: "8:12, the shortest of the ten" holds for collector D's ten videos.

**FAIL:**
- "Season and clock" cites `"in 2026" [0:42]`. The transcript has "[0:55] worth buying in 2026". At [0:42] is "pushes Carrier over Goodman or Trane".
- "Prices" cites `"$3.7 billion" purchase [4:56]`. It is said at [5:03] ("Global for $3.7 billion."). At [4:56] is "the comment section is loading, but".

(The standout "a pricing structure, not a quality structure." [0:44] drops an auto-caption "[music]" tag that sits mid-phrase. The words are all there, so this passes.)

## 5. Channel normals

Method: a fresh `youtube_channel_videos` (sort newest, page 1). The 15 most recent uploads of 5:00+ that are at least 7 days old on 2026-10-27 were taken, then sorted by list count. List counts are rounded (for example "40K"), so exact `youtube_video_details` pulls were made wherever a neighbour of the median came within rounding range.

**The DIY HVAC Guy: 40,551, pass.**
- Excluded as under 7 days: SMJoRo02SX4 (2 days) and AWHQ9OPv9tk (5 days).
- The window holds the same 15 IDs as COLLECTION-LOG.md, in the same order: -MywUZ-ZNOg … Ah6CFpyEqN4. All are 5:00+, and osi9KTbj8nM is the 16th.
- Rounded sorted list: 18K, 20K, 22K, 24K, 31K, 36K, 39K, **40K**, 54K, 59K, 60K, 71K, 88K, 94K, 1.2M.
- 39K and 40K are within rounding of each other, so both were pulled exactly: hrw0LA9XOZc **40,551** (unchanged from the meta) and 4GL_X-dIn2Q 39,902. The 9th is 54K. The median is 40,551.

**grayfurnaceman: 1,555, pass.**
- Excluded:
  - 62XtfsJVeOA (2 days old)
  - DMz6DRxOXWg (3:00)
  - 16O_v2DSzB4 (4:02)
  - QtQ7IFA0BDo (3:58)
  - sTSQi-IlAhg (4:04)
- The window holds the same 15 IDs as the log, with matching durations (ywDGEZ2IvkY 5:44 … AGAwwcmf8o0 11:09). The 16th is vKTjUgjsA7s.
- Rounded sorted list: 752, 935, 957, 1.0K, 1.1K, 1.1K, 1.2K, **1.5K**, 2.2K, 2.8K, 2.9K, 3.3K, 3.5K, 3.6K, 11K.
- The neighbours (1.2K and 2.2K) can't cross 1.5K whatever the rounding. The exact pull of ywDGEZ2IvkY gives **1,555**.

**Ray Dutton's Garage: 8,345, pass.**
- Excluded as under 7 days: AglSKzOY2E8, j2OYzAHipok, vHVITBbPcQI.
- The window holds the same 15 IDs as the log (LhrgMgcHw_A … 9MbOdR2x0N8). The 16th is aspLlFv3Ij0. fHAlfm21vYw and dOZ-8__G4uU are list positions 22 and 23, as the log says.
- Rounded sorted list: 1.9K, 2.3K, 4.5K, 5.1K, 5.5K, 5.5K, 6.5K, **8.3K**, 11K, 17K, 19K, 48K, 127K, 156K, 264K.
- The neighbours (at most 6,599 below, at least 11,000 above) can't cross. The exact pull of Wn7lGvsvpfY gives **8,345**.

The collectors' views-divided-by-normal figures were recomputed for all 8 sampled videos and match to 2 decimals.

## Other findings (not in the 5 checks)

1. **The same promotional comment appears on four channels.** A comment recommending "American Residential Services" / "ARS" for a written estimate appears in near-identical wording on 4 study videos from 4 different channels:
   - `cFYptbCvNjI` (Roger the Pipe Guy; top comment, 32 likes)
   - `86S3ITbfzQY` (Vent Exposed; two comments, 29 and 34)
   - `QKPPm6M0__o` (HVAC Exposed)
   - `dOZ-8__G4uU` (Ray Dutton's Garage)

   The notes record these as viewer comments ("recorded as written"; "near-identical wording"). Collector D's note on 86S3ITbfzQY spotted the pattern within one video, but no file links it across channels. It looks like a coordinated promotional placement rather than viewer opinion (a reading, not a measurement). If it counts as spam under the brief's "skip obvious spam", it would come out of the viewer counts.
2. **Paging:** in 4 of 8 videos, a sampled comment could not be re-found because the continuation token returns the same page. This limits how far any checker can verify the lower-ranked comments. It is the fault already logged in `log.md`, not a collector error.
3. **Timestamp convention:** the notes put a quote at the line holding most of it, sometimes 2-4 s after the quote starts. Nothing says which convention to use. A line in the brief (start of quote, within ±3 s) would make later checks mechanical.

## Fixes to make (for the main session; nothing was changed here)

1. `data/everyday-home-repairs/sRvH-io-ZtA/meta.md`, Comments line: change "channel-owner comments: 1 unique (pinned; appears in both lists, marked [OWNER])" to "channel-owner comments: 0". That matches comments.md, COLLECTION-LOG.md and the fresh pull.
2. `notes/atlas-ac__r_uP9itJ0HQ.md`, Pacing: change `"So you might be asking" ×4` to `×3 ([3:52], [4:30], [5:16])`.
3. `notes/home-renovision-diy__J95l9Ue4224.md`, Hook: make the figure agree with its end-point. Either "60 w, 13 s (ends [0:11] '...the good the better and the best option')" or "75 w, 16 s (ends [0:15] 'so let's just')".
4. `notes/vent-exposed__86S3ITbfzQY.md`: change `"in 2026" [0:42]` to `[0:55]`, and `"$3.7 billion" purchase [4:56]` to `[5:03]`.
5. Reword the four evaluative phrases as description:
   - mP0IjyvQtxw: "tool and detector pitches run long"
   - r_uP9itJ0HQ: "candid"
   - X3Y-yA42UBk: "the honest version"
   - X3Y-yA42UBk: "fair to the trade"
6. Decide how to treat the ARS comments on cFYptbCvNjI, 86S3ITbfzQY, QKPPm6M0__o and dOZ-8__G4uU: tag them (for example `[likely promo]`) and leave them out of viewer counts, or keep them as written and note the cross-channel pattern in `log.md`.
7. Optional: strip the trailing first-name signatures ("Ken", "John") and "Ditto Chris" from the three comments listed in section 3; add a timestamp convention to the brief.
