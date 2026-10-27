# Collection log — The Funny Carpenter (Helper C)

Collected 2026-10-27 by collector helper C following `studies/hvac/study-brief.md` and `inputs/videos.md`. Describe-only; no judgements.

## Channel

- Name: The Funny Carpenter
- Handle: @TheFunnyCarpenter
- Channel ID: UCgx_ERh6IE-Td3FLJstu1iQ
- Subscribers: 785K (youtube_channel_videos meta, 2026-10-27)
- Channel description not pulled; the video description advertises the presenter's HVAC service business in the Fraser Valley (wagnerheating.com).

## Videos collected (selection rows from inputs/videos.md)

| Row | Video ID | Type | Views (2026-10-27) | Duration | Normal | Views / normal | Transcript segments | Comments (unique) |
|---|---|---|---|---|---|---|---|---|
| 19 | _g8gQ1gg1FM | mistakes list | 2,910,014 | 5:33 | 500,610 | 5.81 | 166 | 44 |

All rows assigned to Helper C for this channel were collected.

## Format

ON CAMERA. Basis: NexLev `check_faceless_channel` isFaceless=false, confidence 0.98, format "tutorial" (fresh call, 2026-10-27); first-person demonstrations in the transcript; a blooper reel at the end; the description sends viewers to the presenter's HVAC service business ("If you need any H-Vac service work in the Fraser Valley please check out: wagnerheating.com").

## Method (NexLev MCP tools only, no web search)

1. `youtube_video_details` for each selected video (exact views, likes, publish time, length, hasCaption) and for the median video of the normal window plus any videos tied with it on the list.
2. `get_bulk_video_transcripts` once for all Helper C videos. The output was saved by the tool to a local file; a script turned each `transcript` array into `[m:ss] text`, one line per segment (h:mm:ss past one hour), start time from `startMs`.
3. `youtube_video_comments` sort=top: page 1, then 2 more pages, each with the newest continuation token (per the main session's tip); sort=newest: 1 page. Comment text and like counts were copied into scratch files (no usernames, no channel IDs) and assembled into `comments.md` by script; duplicates across pages were removed by matching the comment text; @handles inside comment text replaced with "@[handle removed]"; owner comments (API `authorIsChannelOwner=true`) marked [OWNER].
4. `youtube_channel_videos` sort=newest, page 1 (30 uploads) for the normal window; `check_faceless_channel` for the format.
5. **How the normal was taken.** The list gives display view counts that are truncated (for example "37K" for an exact 37,888) and relative dates. The 15-video window was ranked on the list values; exact views were then fetched with `youtube_video_details` for the median video and for any video whose display value ties with it. Because the display values are truncated, not rounded, a video showing a higher display value always has more exact views, so the order holds except inside a tie, and ties were resolved with exact counts. The other window videos were not fetched one by one (their exact counts are not needed for the median).

## Normal: 500,610

Median of the exact views of the 15 most recent long-form uploads (5:00+, Videos tab so not Shorts) at least 7 days old on 2026-10-27, from `youtube_channel_videos` sort=newest on 2026-10-27. "List date" is the approximate date from the relative time ("3 months ago"); "list views" is the truncated display value.

| # | Video ID | Duration | List date (approx.) | List views | Exact views | Status |
|---|---|---|---|---|---|---|
| 1 | 80X_8gh4XmI | 11:09 | 2026-10-19 (8 days ago) | 862,000 |  | in |
| 2 | bC2cdhMHdNM | 7:49 | 2026-09-27 (1 month ago) | 290,000 |  | in |
| 3 | yeVK4EtdBso | 9:13 | 2026-09-27 (1 month ago) | 987,000 |  | in |
| – | 59EAzYwBrHU | 4:26 | 2026-09-27 (1 month ago) | 283,000 |  | out<5:00 |
| 4 | sZ7Xt9rcaKE | 11:41 | 2026-08-27 (2 months ago) | 47,000 |  | in |
| 5 | qkb_4umxvuA | 7:36 | 2026-07-27 (3 months ago) | 500,000 | **500,610** (median) | in |
| 6 | YOYxWpWa-fA | 8:54 | 2026-06-27 (4 months ago) | 856,000 |  | in |
| 7 | _mnlj8LxtGc | 11:44 | 2026-06-27 (4 months ago) | 163,000 |  | in |
| 8 | cjlgh8XW0wg | 6:56 | 2026-05-27 (5 months ago) | 887,000 |  | in |
| – | 6hkeFTzsyFM | 4:09 | 2026-05-27 (5 months ago) | 1,500,000 |  | out<5:00 |
| 9 | 7fFQvAeEHxE | 11:08 | 2026-05-27 (5 months ago) | 157,000 |  | in |
| 10 | gP2nPWvxtxA | 10:03 | 2026-04-27 (6 months ago) | 339,000 |  | in |
| – | HCaUgUEqkjM | 3:52 | 2026-03-27 (7 months ago) | 187,000 |  | out<5:00 |
| 11 | EFFMnB2IE20 | 8:04 | 2026-03-27 (7 months ago) | 406,000 |  | in |
| 12 | keEwBkKOH7o | 11:19 | 2026-03-27 (7 months ago) | 672,000 |  | in |
| 13 | D01GZX1QuoQ | 20:51 | 2026-02-27 (8 months ago) | 358,000 |  | in |
| 14 | ha6DDZICyw0 | 7:30 | 2026-01-27 (9 months ago) | 530,000 |  | in |
| 15 | pCKCAFGr1To | 12:22 | 2025-12-27 (10 months ago) | 2,400,000 |  | in(15th) |
| – | qUXOzhwgYCA | 9:12 | 2025-12-27 (10 months ago) | 3,200,000 |  | beyond window |

Source note: median exact: qkb_4umxvuA 500610 views (details 2026-10-27; published 2026-07-01T12:25:31-07:00; 456 s; neighbours 406000 and 530000 on the list, order not affected by rounding)

Excluded as under 5:00: 59EAzYwBrHU (4:26), 6hkeFTzsyFM (4:09), HCaUgUEqkjM (3:52). Nothing in the list was under 7 days old (newest 80X_8gh4XmI, list "8 days ago").

## Transcripts

| Video ID | Segments | Words | Track |
|---|---|---|---|
| _g8gQ1gg1FM | 166 | 1,102 | auto-generated |

No transcript gaps over 20 s.

## Comments

| Video ID | API commentsCount | Pages fetched | Top | Newest | In both | Unique | [OWNER] | Spam skipped |
|---|---|---|---|---|---|---|---|---|
| _g8gQ1gg1FM | 1.2K | top: page 1 (20) + page 2 (+5 new) + page 3 (no new); newest: 1 page | 25 | 20 | 1 | 44 | 0 | 0 |

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

