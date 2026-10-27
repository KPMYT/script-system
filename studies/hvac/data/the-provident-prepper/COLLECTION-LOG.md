# Collection log — The Provident Prepper (Helper C)

Collected 2026-10-27 by collector helper C following `studies/hvac/study-brief.md` and `inputs/videos.md`. Describe-only; no judgements.

## Channel

- Name: The Provident Prepper
- Handle: @TheProvidentPrepper
- Channel ID: UCsehkdEMPHIy_PIBZZs3VRg
- Subscribers: 290K (youtube_channel_videos meta, 2026-10-27)
- About: "We're Kylene and Jonathan Jones".

## Videos collected (selection rows from inputs/videos.md)

| Row | Video ID | Type | Views (2026-10-27) | Duration | Normal | Views / normal | Transcript segments | Comments (unique) |
|---|---|---|---|---|---|---|---|---|
| 26 | erq-QuCN0G0 | outage list | 1,216,737 | 15:09 | 16,570 | 73.43 | 463 | 44 |

All rows assigned to Helper C for this channel were collected.

## Format

ON CAMERA (a married couple presenting). Basis: NexLev `check_faceless_channel` isFaceless=false, confidence 0.96, format "educational" (cached, 2026-10-27); channel About "We're Kylene and Jonathan Jones"; two voices introduce themselves ("we are the provident preppers" [0:16]) and show family photos from their own outage test; comments address the family ("What a great, useful video by such a cute family!").

## Method (NexLev MCP tools only, no web search)

1. `youtube_video_details` for each selected video (exact views, likes, publish time, length, hasCaption) and for the median video of the normal window plus any videos tied with it on the list.
2. `get_bulk_video_transcripts` once for all Helper C videos. The output was saved by the tool to a local file; a script turned each `transcript` array into `[m:ss] text`, one line per segment (h:mm:ss past one hour), start time from `startMs`.
3. `youtube_video_comments` sort=top: page 1, then 2 more pages, each with the newest continuation token (per the main session's tip); sort=newest: 1 page. Comment text and like counts were copied into scratch files (no usernames, no channel IDs) and assembled into `comments.md` by script; duplicates across pages were removed by matching the comment text; @handles inside comment text replaced with "@[handle removed]"; owner comments (API `authorIsChannelOwner=true`) marked [OWNER].
4. `youtube_channel_videos` sort=newest, page 1 (30 uploads) for the normal window; `check_faceless_channel` for the format.
5. **How the normal was taken.** The list gives display view counts that are truncated (for example "37K" for an exact 37,888) and relative dates. The 15-video window was ranked on the list values; exact views were then fetched with `youtube_video_details` for the median video and for any video whose display value ties with it. Because the display values are truncated, not rounded, a video showing a higher display value always has more exact views, so the order holds except inside a tie, and ties were resolved with exact counts. The other window videos were not fetched one by one (their exact counts are not needed for the median).

## Normal: 16,570

Median of the exact views of the 15 most recent long-form uploads (5:00+, Videos tab so not Shorts) at least 7 days old on 2026-10-27, from `youtube_channel_videos` sort=newest on 2026-10-27. "List date" is the approximate date from the relative time ("3 months ago"); "list views" is the truncated display value.

| # | Video ID | Duration | List date (approx.) | List views | Exact views | Status |
|---|---|---|---|---|---|---|
| – | Eld0QLDbWxk | 24:35 | 2026-10-24 (3 days ago) | 14,000 |  | out<7 days |
| 1 | Fh9wLDxcGf0 | 13:23 | 2026-10-17 (10 days ago) | 14,000 |  | in |
| 2 | Y9po1YvNV_g | 25:30 | 2026-10-13 (2 weeks ago) | 16,000 | **16,570** (median) | in |
| 3 | 3Nt4u4V2YIU | 6:40 | 2026-10-06 (3 weeks ago) | 13,000 |  | in |
| 4 | FudXHxlr_Ic | 13:05 | 2026-09-27 (1 month ago) | 47,000 |  | in |
| 5 | BDrTXR2NuPg | 14:16 | 2026-09-27 (1 month ago) | 44,000 |  | in |
| 6 | vkYLdhE0_4k | 13:18 | 2026-09-27 (1 month ago) | 26,000 |  | in |
| 7 | rsG6sb5kQFA | 42:33 | 2026-09-27 (1 month ago) | 8,800 |  | in |
| 8 | ZiC0Yp8Dmp0 | 13:35 | 2026-09-27 (1 month ago) | 211,000 |  | in |
| 9 | 95DViR71Ta8 | 25:24 | 2026-08-27 (2 months ago) | 67,000 |  | in |
| 10 | LwslHadkjtM | 42:10 | 2026-08-27 (2 months ago) | 3,200 |  | in |
| 11 | hVamvDLX5T0 | 18:34 | 2026-08-27 (2 months ago) | 9,800 |  | in |
| 12 | nUW2DsHHuHI | 13:13 | 2026-08-27 (2 months ago) | 2,900 |  | in |
| 13 | W9DOKIYDJqQ | 16:26 | 2026-07-27 (3 months ago) | 217,000 |  | in |
| 14 | Kg4b-GDCebQ | 25:54 | 2026-07-27 (3 months ago) | 10,000 |  | in |
| 15 | mZlvUJWrWU4 | 28:25 | 2026-07-27 (3 months ago) | 22,000 |  | in(15th) |
| – | EXrRKgPaGAs | 22:48 | 2026-07-27 (3 months ago) | 22,000 |  | beyond window |

Source note: median exact: Y9po1YvNV_g 16570 views (details 2026-10-27; published 2026-10-09T11:07:57-07:00; 1529 s; list neighbours 14K and 22K, order not affected)

Excluded as under 7 days old: Eld0QLDbWxk (list "3 days ago"). The list shows the median video as "2 weeks ago"; its exact publish time is 2026-10-09.

## Transcripts

| Video ID | Segments | Words | Track |
|---|---|---|---|
| erq-QuCN0G0 | 463 | 2,805 | auto-generated |

No transcript gaps over 20 s.

## Comments

| Video ID | API commentsCount | Pages fetched | Top | Newest | In both | Unique | [OWNER] | Spam skipped |
|---|---|---|---|---|---|---|---|---|
| erq-QuCN0G0 | 2.2K | top: page 1 (20) + page 2 (+5 new) + page 3 (no new); newest: 1 page | 25 | 20 | 1 | 44 | 1 | 0 |

Username/handle check: comments.md holds comment text and like counts only; no usernames or channel IDs.

## Failures and API oddities

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

