# Collection log — WINNI (Helper C)

Collected 2026-10-27 by collector helper C following `studies/hvac/study-brief.md` and `inputs/videos.md`. Describe-only; no judgements.

## Channel

- Name: WINNI
- Handle: @WINNI.Designs
- Channel ID: UC1pbNAyLnP_OIaEBFBl3xaw
- Subscribers: 1.29M (youtube_channel_videos meta, 2026-10-27)
- About: "Hey my name is Misha and I love construction, and making videos."

## Videos collected (selection rows from inputs/videos.md)

| Row | Video ID | Type | Views (2026-10-27) | Duration | Normal | Views / normal | Transcript segments | Comments (unique) |
|---|---|---|---|---|---|---|---|---|
| 25 | 6CE72U92R-I | cheap fixes vs the quote | 9,166,449 | 8:44 | 37,888 | 241.94 | none | 52 |

All rows assigned to Helper C for this channel were collected. 6CE72U92R-I has no transcript and is skipped from script analysis (see Failures).

## Format

ON CAMERA, filmed doing the work; the video has no transcript, so whether anyone speaks is not known (a reading; not checked visually). Basis: comments describe the people seen working ("I love it when the wife comes out to help!", 16 likes; "Really nice to see you working as a couple team", 8 likes; "Love how the guy started with the router", 2 likes) and the soundtrack ("fast forward, hammering & sound", 8 likes); channel About: "Hey my name is Misha and I love construction, and making videos."; description in first person ("Today I will show you our process"); NexLev `check_faceless_channel` isFaceless=false, confidence 0.96, format "tutorial" (fresh call, 2026-10-27).

## Method (NexLev MCP tools only, no web search)

1. `youtube_video_details` for each selected video (exact views, likes, publish time, length, hasCaption) and for the median video of the normal window plus any videos tied with it on the list.
2. `get_bulk_video_transcripts` once for all Helper C videos. The output was saved by the tool to a local file; a script turned each `transcript` array into `[m:ss] text`, one line per segment (h:mm:ss past one hour), start time from `startMs`.
3. `youtube_video_comments` sort=top: page 1, then 2 more pages, each with the newest continuation token (per the main session's tip); sort=newest: 1 page. Comment text and like counts were copied into scratch files (no usernames, no channel IDs) and assembled into `comments.md` by script; duplicates across pages were removed by matching the comment text; @handles inside comment text replaced with "@[handle removed]"; owner comments (API `authorIsChannelOwner=true`) marked [OWNER].
4. `youtube_channel_videos` sort=newest, page 1 (30 uploads) for the normal window; `check_faceless_channel` for the format.
5. **How the normal was taken.** The list gives display view counts that are truncated (for example "37K" for an exact 37,888) and relative dates. The 15-video window was ranked on the list values; exact views were then fetched with `youtube_video_details` for the median video and for any video whose display value ties with it. Because the display values are truncated, not rounded, a video showing a higher display value always has more exact views, so the order holds except inside a tie, and ties were resolved with exact counts. The other window videos were not fetched one by one (their exact counts are not needed for the median).

## Normal: 37,888

Median of the exact views of the 15 most recent long-form uploads (5:00+, Videos tab so not Shorts) at least 7 days old on 2026-10-27, from `youtube_channel_videos` sort=newest on 2026-10-27. "List date" is the approximate date from the relative time ("3 months ago"); "list views" is the truncated display value.

| # | Video ID | Duration | List date (approx.) | List views | Exact views | Status |
|---|---|---|---|---|---|---|
| 1 | 4GBQ_7IUru0 | 8:35 | 2026-10-06 (3 weeks ago) | 15,000 |  | in |
| 2 | 4fzoJVK_SlQ | 26:25 | 2026-09-27 (1 month ago) | 622,000 |  | in |
| 3 | s2sqIuEEyEI | 8:31 | 2026-09-27 (1 month ago) | 42,000 |  | in |
| 4 | UE6G_7GE0AA | 53:14 | 2026-07-27 (3 months ago) | 37,000 | **37,888** (median) | in |
| 5 | 5m1Kxt_IY08 | 45:06 | 2026-06-27 (4 months ago) | 10,000 |  | in |
| – | t8MfSUDpmYQ | 4:10 | 2026-05-27 (5 months ago) | 4,700 |  | out<5:00 |
| 6 | r9W9SCGKZac | 8:07 | 2026-05-27 (5 months ago) | 5,200 |  | in |
| 7 | EcjAkJueRno | 25:47 | 2026-05-27 (5 months ago) | 2,700 |  | in |
| 8 | FH5ZG6n6uv0 | 27:22 | 2026-04-27 (6 months ago) | 137,000 |  | in |
| 9 | ezzmdPPGqjk | 1:58:33 | 2026-04-27 (6 months ago) | 38,000 |  | in |
| 10 | w3OvP3fHLhs | 11:06 | 2026-04-27 (6 months ago) | 3,700 |  | in |
| 11 | c39U5o9jMeM | 23:39 | 2026-04-27 (6 months ago) | 381,000 |  | in |
| – | IM20ByrFbTc | 3:52 | 2026-03-27 (7 months ago) | 5,700 |  | out<5:00 |
| 12 | DES2NciPBLw | 11:59 | 2026-02-27 (8 months ago) | 3,100 |  | in |
| 13 | WZni8bpynyw | 10:40 | 2025-12-27 (10 months ago) | 272,000 |  | in |
| 14 | sBM9Y3Wag3M | 8:01 | 2025-12-27 (10 months ago) | 5,900 |  | in |
| 15 | RAwd_J8OR2w | 17:12 | 2025-12-27 (10 months ago) | 353,000 |  | in(15th) |
| – | HmdQBEo5aTw | 6:58 | 2025-10-27 (1 year ago) | 23,000 |  | beyond window |

Source note: median exact: UE6G_7GE0AA 37888 views (details 2026-10-27; published 2026-07-06T11:52:53-07:00; 3193 s; list shows 37K for 37888, so list counts are truncated; neighbour ezzmdPPGqjk 38K >= 38000 stays above, 15K below)

Excluded as under 5:00: t8MfSUDpmYQ (4:10), IM20ByrFbTc (3:52). ezzmdPPGqjk (1:58:33) is in the window as long-form. The list shows the median video as "37K" for an exact 37,888, which shows the list counts are truncated, not rounded; its neighbour ezzmdPPGqjk shows "38K" (at least 38,000), so the order holds.

## Transcripts

| Video ID | Segments | Words | Track |
|---|---|---|---|
| 6CE72U92R-I | none | none | "Not Available" (bulk call and single-video retry) |



## Comments

| Video ID | API commentsCount | Pages fetched | Top | Newest | In both | Unique | [OWNER] | Spam skipped |
|---|---|---|---|---|---|---|---|---|
| 6CE72U92R-I | 1.2K | top: page 1 (20) + page 2 (+8 new) + page 3 (+7 new); newest: 1 page (1 spam skipped) | 35 | 19 | 2 | 52 | 0 | 1 |

Username/handle check: comments.md holds comment text and like counts only; no usernames or channel IDs.

## Failures and API oddities

- **No transcript** for 6CE72U92R-I: `get_bulk_video_transcripts` returned "Not Available"; retried once with `get_video_transcript`, same result. Logged and skipped from script analysis, per the brief; no notes file was written for it. youtube_video_details reports hasCaption=false. Description chapters (for reference only): 00:00 demo; 00:54 Sheathing; 03:03 Flashing; 05:15 Helo Extera Install.
- Spam skipped: 1 (gibberish: keyboard characters and an emoji). One top comment (#29, 0 likes) promotes the writer's own coating product; kept as a real comment and noted here.
- Comment continuation pages mostly repeat page 1 and add 0 to 10 new comments each, so the top list holds 20 to 35, not the brief's ~60. Pages that returned nothing new are listed above. No other comment method was used.
- In sort=newest, the pinned comment (the owner's, where there is one) is listed first even though it is old; marked in comments.md.

## Spam skipped

1 (6CE72U92R-I).

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

