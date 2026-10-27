# Collection log: Word of Advice TV

Helper B, 2026-10-27. Channel Word of Advice TV (@WordofAdviceTV, channel ID UCekKmUEJxBRx5tI1tUyHOqA, about 662K subscribers per NexLev `youtube_channel_about`).

## Videos collected

| # | Video ID | Title | Type | Views | Duration | Views / normal | Segments | Comments collected |
|---|---|---|---|---|---|---|---|---|
| 12 | 3Jonl_TLkpE | Furnace Not Working - The Most Common Fix | symptom diagnostic | 2,567,895 | 8:57 | 140.71 | 222 | 38 unique |
| 13 | 1bRsFAMgZRQ | Furnace Not Igniting - How to Check and Replace Ignitor | cheap-part repair | 1,367,552 | 13:08 | 74.93 | 343 | 37 unique |

## Format
ON CAMERA. NexLev `check_faceless_channel`: isFaceless=false, confidence 0.97, format "tutorial". Both transcripts open "Hey guys, Jay here with Word of Advice TV".

## Method
- Sources: NexLev only. `youtube_video_details` (views, likes, date, duration), `get_bulk_video_transcripts` (one call for all 9 Helper B videos), `youtube_video_comments` (sort top and sort newest), `youtube_channel_videos` (channel upload list), `check_faceless_channel`, `youtube_channel_about`. No web search.
- `youtube_channel_videos` list dates are relative placeholders, so every candidate upload's exact date, length and views came from `youtube_video_details`.
- Normal: the median of exact views of the 15 most recent long-form uploads (5:00+, not Shorts) at least 7 days old on 2026-10-27.

## Channel normal: 18,250

| # | Video ID | Upload date | Length (s) | Views | Title |
|---|---|---|---|---|---|
| 1 | gTkHUMmmDIY | 2026-09-27 | 332 | 11,604 | What Gauges Should You Have? |
| 2 | 3FAiVQk9-ws | 2026-08-30 | 732 | 21,594 | Must-Have Tools Every Tool Bag Should Have! |
| 3 | 6pSvKvGp1QE | 2026-08-15 | 365 | 11,009 | Most Common Question About The Most Commonly Replaced AC Part |
| 4 | YiHObsjSHwY | 2026-07-25 | 865 | 10,562 | $30,000 for a New Air Conditioner? |
| 5 | -TcZiVkTlNA | 2026-07-04 | 339 | 23,187 | How to Wire 521 Start Capacitor and Potential Relay in Air Conditioner |
| 6 | 1_K6A6ZKthU | 2026-06-09 | 557 | 53,521 | How to Wire Central Air Conditioner - Basic A/C Wiring |
| 7 | yZwil5Nt9r8 | 2026-03-07 | 743 | 15,254 | How to Flush and Rinse an On Demand Tankless Water Heater |
| 8 | NUOL77juChE | 2026-02-08 | 852 | 129,991 | How to Unlock a Locked Car Door Without a Key (Keys Locked Inside) |
| 9 | sWSYvOSyEb0 | 2026-01-10 | 588 | 5,321 | All You Will Ever Need to Know When Peeling a Pomegranate |
| 10 | YXGMbPU_6Ak | 2025-12-20 | 330 | 13,246 | High Efficiency Heat Pump vs Standard Heat Pump, Which is Better to Get? |
| 11 | Ek48NTMR9RM | 2025-10-31 | 381 | 12,090 | How Does a Solar Water Heater Work? |
| 12 | XOT4_BYzVJw | 2025-09-14 | 587 | 39,517 | How to install a Midea Window Air Conditioner |
| 13 | xgZSgXepxJk | 2025-08-17 | 421 | 160,501 | How to Take Apart and Clean Portable Air Conditioner |
| 14 | bR6mdGC0Jbw | 2025-07-26 | 535 | 18,250 | How to Replace Screen on a Window and Slide Door Easy! |
| 15 | MqiqyWc_mzg | 2025-06-28 | 345 | 83,744 | Window AC Not Cooling Properly - Easy Fix |

Sorted views: 5,321, 10,562, 11,009, 11,604, 12,090, 13,246, 15,254, 18,250, 21,594, 23,187, 39,517, 53,521, 83,744, 129,991, 160,501. Median (8th of 15): 18,250.

Next upload back (16th, not counted, recorded as a spare): -GHaMPfrLt0 2025-05-24 86,991.
Excluded for length (under 5:00): SscqOFuKxmQ (2:35), _LvTCQ0xtek (4:32), clj_drlzOdY (3:13).

## Transcripts
- 3Jonl_TLkpE: track "English (auto-generated)", 222 segments, 1,558 words. youtube_video_details reports hasCaption=false.
- 1bRsFAMgZRQ: track "English (auto-generated)", 343 segments, 2,456 words. youtube_video_details reports hasCaption=false.

## Comments
- Text and like counts only; no usernames or channel IDs. @handles inside comment text are replaced with "@[handle removed]" (none were needed in this channel's files). Channel-owner comments marked [OWNER].
- Pagination: continuation tokens on `youtube_video_comments` returned pages that largely repeated the first page (tested on --A2I2s7aNw and sRvH-io-ZtA, Everyday Home Repairs). One page per sort was then used: about 20 top + 20 newest per video, short of the brief's ~60 top. A later tip from the main session (continuation pages may add 5-8 new each) arrived after all 9 comment files were finished; the videos were not re-pulled, in line with that tip ("Don't redo videos you've already finished unless it's quick").
- 3Jonl_TLkpE: API commentsCount 1.9K; collected 20 top + 20 newest = 38 unique (2 in both lists); owner: 1 pinned owner comment (video links), in both lists; spam skipped: 0. The newest list's most recent comment is dated "7 months ago".
- 1bRsFAMgZRQ: API commentsCount 925; collected 20 top + 20 newest = 37 unique (3 in both lists); owner: 1 pinned owner comment (video links), in both lists; spam skipped: 0.

## Failures
- None. Every NexLev call returned data on the first try.

## Verification
Fresh `youtube_video_details` call for 3Jonl_TLkpE (2026-10-27, after meta.md was written): views 2,567,895, lengthSeconds 537 (8:57), publishDate 2018-10-20T13:16:39-07:00. All three match meta.md exactly.
Whole-set check (all 9 Helper B notes): every quoted string in the notes was matched by script against its transcript.txt (sections above Comments) or comments.md (Comments section), with case and punctuation ignored and "..." treated as a gap. Three paraphrases that had been put in quotation marks were unquoted. Quote timestamps were also compared with segment times, and three were corrected by 2-7 s (X3Y-yA42UBk [1:53]->[1:48] and [2:15]->[2:10]; yJxDc90hs4g [5:30]->[5:28]).
