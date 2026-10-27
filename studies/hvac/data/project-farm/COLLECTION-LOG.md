# Collection log — Project Farm (Helper C)

Collected 2026-10-27 by collector helper C following `studies/hvac/study-brief.md` and `inputs/videos.md`. Describe-only; no judgements.

## Channel

- Name: Project Farm
- Handle: @ProjectFarm
- Channel ID: UC2rzsm1Qi6N1X-wuOg_p0Ng
- Subscribers: 3.95M (youtube_channel_videos meta, 2026-10-27)
- Description of RkjRKIRva58: "I always buy all of the products to ensure fair and unbiased results"; Amazon links for each filter.

## Videos collected (selection rows from inputs/videos.md)

| Row | Video ID | Type | Views (2026-10-27) | Duration | Normal | Views / normal | Transcript segments | Comments (unique) |
|---|---|---|---|---|---|---|---|---|
| 23 | RkjRKIRva58 | ranked verdict (filmed tests: structure only) | 2,574,586 | 12:54 | 1,025,022 | 2.51 | 366 | 48 |

All rows assigned to Helper C for this channel were collected.

## Format

HANDS ONLY (a reading; not checked visually). Basis: first-person narration of his own bench work ("I built this air filter test stand." [0:33]; "I'll tape the perimeter"); no collected comment mentions his face or appearance; NexLev `check_faceless_channel` isFaceless=false, confidence 0.98, format "reviews" (cached, 2026-10-27), which says a real person, not whether the face is shown; the description lists his test equipment.

## Method (NexLev MCP tools only, no web search)

1. `youtube_video_details` for each selected video (exact views, likes, publish time, length, hasCaption) and for the median video of the normal window plus any videos tied with it on the list.
2. `get_bulk_video_transcripts` once for all Helper C videos. The output was saved by the tool to a local file; a script turned each `transcript` array into `[m:ss] text`, one line per segment (h:mm:ss past one hour), start time from `startMs`.
3. `youtube_video_comments` sort=top: page 1, then 2 more pages, each with the newest continuation token (per the main session's tip); sort=newest: 1 page. Comment text and like counts were copied into scratch files (no usernames, no channel IDs) and assembled into `comments.md` by script; duplicates across pages were removed by matching the comment text; @handles inside comment text replaced with "@[handle removed]"; owner comments (API `authorIsChannelOwner=true`) marked [OWNER].
4. `youtube_channel_videos` sort=newest, page 1 (30 uploads) for the normal window; `check_faceless_channel` for the format.
5. **How the normal was taken.** The list gives display view counts that are truncated (for example "37K" for an exact 37,888) and relative dates. The 15-video window was ranked on the list values; exact views were then fetched with `youtube_video_details` for the median video and for any video whose display value ties with it. Because the display values are truncated, not rounded, a video showing a higher display value always has more exact views, so the order holds except inside a tie, and ties were resolved with exact counts. The other window videos were not fetched one by one (their exact counts are not needed for the median).

## Normal: 1,025,022

Median of the exact views of the 15 most recent long-form uploads (5:00+, Videos tab so not Shorts) at least 7 days old on 2026-10-27, from `youtube_channel_videos` sort=newest on 2026-10-27. "List date" is the approximate date from the relative time ("3 months ago"); "list views" is the truncated display value.

| # | Video ID | Duration | List date (approx.) | List views | Exact views | Status |
|---|---|---|---|---|---|---|
| – | HQhq2SHko9I | 19:20 | 2026-10-26 (1 day ago) | 1,100,000 |  | out<7 days |
| 1 | kIjMCDHW9Ec | 20:33 | 2026-10-19 (8 days ago) | 1,000,000 | 1,060,901 | in |
| 2 | vtSO1wrAqU0 | 18:55 | 2026-10-13 (2 weeks ago) | 1,600,000 |  | in |
| 3 | 4ievxm-8P7E | 24:28 | 2026-10-06 (3 weeks ago) | 686,000 |  | in |
| 4 | rk5a6DLCgcQ | 21:15 | 2026-09-29 (4 weeks ago) | 959,000 |  | in |
| 5 | xTFbdQ5J39c | 18:21 | 2026-09-27 (1 month ago) | 771,000 |  | in |
| 6 | 4EHO9S2-e7A | 17:58 | 2026-09-27 (1 month ago) | 1,400,000 |  | in |
| 7 | U6Au81P6yHk | 22:19 | 2026-09-27 (1 month ago) | 1,000,000 | **1,025,022** (median) | in |
| 8 | 4UU-oNXjcEE | 20:24 | 2026-09-27 (1 month ago) | 2,800,000 |  | in |
| 9 | 1PA8AHGJMPQ | 18:31 | 2026-08-27 (2 months ago) | 1,900,000 |  | in |
| 10 | My1J_97gt40 | 17:46 | 2026-08-27 (2 months ago) | 527,000 |  | in |
| 11 | we1GYoSb95I | 23:08 | 2026-08-27 (2 months ago) | 948,000 |  | in |
| 12 | awe7kY5nvdU | 21:09 | 2026-08-27 (2 months ago) | 2,600,000 |  | in |
| 13 | T_Nb-fpPkJA | 18:23 | 2026-07-27 (3 months ago) | 352,000 |  | in |
| 14 | 1ZsOdRHv_uQ | 17:09 | 2026-07-27 (3 months ago) | 1,000,000 | 1,035,146 | in |
| 15 | 4PZuPLvh-7k | 18:34 | 2026-07-27 (3 months ago) | 992,000 |  | in(15th) |
| – | ZvpB6cyp0PI | 22:27 | 2026-07-27 (3 months ago) | 935,000 |  | beyond window |

Source note: exact (details 2026-10-27): kIjMCDHW9Ec 1060901 (2026-10-18T09:50:30-07:00, 1233 s, 9 days old); U6Au81P6yHk 1025022 (2026-09-06T09:50:26-07:00, 1339 s); 1ZsOdRHv_uQ 1035146 (2026-07-19T09:50:23-07:00, 1029 s). Position 7 = 992K (4PZuPLvh-7k), positions 8-10 = 1025022, 1035146, 1060901 -> median U6Au81P6yHk 1025022.

Excluded as under 7 days old: HQhq2SHko9I (list "1 day ago"). Three uploads show "1M" (a tie), so all three were fetched exactly: U6Au81P6yHk 1,025,022; 1ZsOdRHv_uQ 1,035,146; kIjMCDHW9Ec 1,060,901 (published 2026-10-18, 9 days old, so in). 4PZuPLvh-7k shows 992K, below all three. Sorted positions 8 to 10, so the median is U6Au81P6yHk.

## Transcripts

| Video ID | Segments | Words | Track |
|---|---|---|---|
| RkjRKIRva58 | 366 | 2,514 | auto-generated |

No transcript gaps over 20 s.

## Comments

| Video ID | API commentsCount | Pages fetched | Top | Newest | In both | Unique | [OWNER] | Spam skipped |
|---|---|---|---|---|---|---|---|---|
| RkjRKIRva58 | 10K | top: page 1 (20) + page 2 (+8 new) + page 3 (+2 new); newest: 1 page | 30 | 20 | 2 | 48 | 1 | 0 |

Username/handle check: comments.md holds comment text and like counts only; no usernames or channel IDs.

## Failures and API oddities

- Format is a reading: the brief asks for on camera / hands only / faceless; the transcript, description and comments give no sign of his face and NexLev does not test that. Not checked visually.
- Comment continuation pages mostly repeat page 1 and add 0 to 10 new comments each, so the top list holds 20 to 35, not the brief's ~60. Pages that returned nothing new are listed above. No other comment method was used.
- In sort=newest, the pinned comment (the owner's, where there is one) is listed first even though it is old; marked in comments.md.

## Spam skipped

0.

## Verification (2026-10-27, helper C, for all its channels)

1. **meta.md against a fresh `youtube_video_details` call** (2 videos re-opened):

| Video | Field | meta.md | Fresh call | Result |
|---|---|---|---|---|
| _g8gQ1gg1FM | views | 2,910,014 | 2,910,325 | +311 since the first pull the same day (live count); not changed in meta.md |
| _g8gQ1gg1FM | duration | 5:33 (333 s) | 333 s | match |
| _g8gQ1gg1FM | upload date | 2024-02-15 (12:24:45-08:00) | 2024-02-15T12:24:45-08:00 | match |
| cFYptbCvNjI | views | 37,083 | 37,083 | match |
| cFYptbCvNjI | duration | 23:29 (1409 s) | 1409 s | match |
| cFYptbCvNjI | upload date | 2026-08-27 (08:30:24-07:00) | 2026-08-27T08:30:24-07:00 | match |

2. **Quoted lines against the transcript text** (3 re-checked by hand in `transcript.txt`):
   - HnMuNCl7tZ8 [0:46] "the written warnings on a space heater or really any product should never be ignored they were written in blood": lines [0:46] to [0:51]; match.
   - RkjRKIRva58 [7:53] "I'll then spread 1 cup of flour across the filter and wait until the particle count stops climbing.": lines [7:53] to [7:55]; match.
   - cFYptbCvNjI [11:30] "Never combine bleach and vinegar.": line [11:30]; match.
   - In addition, a script checked every timestamped quote in all 8 notes against the data-folder transcripts (quote must start in a segment within 3 s of its timestamp) and every comment quote against comments.md: 259 transcript quotes and 61 comment quotes, 0 misses. Earlier misses found by the same check (wrong timestamps by 2 to 9 s, a few words off the auto-caption text) were corrected in the notes before this run.

