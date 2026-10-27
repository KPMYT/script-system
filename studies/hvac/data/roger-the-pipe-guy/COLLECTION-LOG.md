# Collection log — Roger the Pipe Guy (the operator's own channel) (Helper C)

Collected 2026-10-27 by collector helper C following `studies/hvac/study-brief.md` and `inputs/videos.md`. Describe-only; no judgements.

## Channel

- Name: Roger the Pipe Guy
- Handle: @RogerthePipeGuy
- Channel ID: UCR2C--KENITllxSo1aAbWWA
- Subscribers: 77K (youtube_channel_videos meta, 2026-10-27)
- No Shorts tab. Normal recomputed fresh for this study (the plumbing study's normal, pulled 2026-10-20, was 2,688).

## Videos collected (selection rows from inputs/videos.md)

| Row | Video ID | Type | Views (2026-10-27) | Duration | Normal | Views / normal | Transcript segments | Comments (unique) |
|---|---|---|---|---|---|---|---|---|
| 27 | cFYptbCvNjI | single-product fix (own HVAC data point) | 37,083 | 23:29 | 2,719 | 13.64 | 581 | 5 |

All rows assigned to Helper C for this channel were collected.

## Format

FACELESS persona (narration over third-party footage). Basis: the description carries a "Credits:" list of about 30 other channels whose footage is used; the transcript is one first-person voice ("I am Roger." [0:55]) with no presenter cues; the plumbing study recorded the channel the same way. NexLev `check_faceless_channel` says isFaceless=false, confidence 0.96, format "tutorial" (cached, 2026-10-27), which disagrees.

## Method (NexLev MCP tools only, no web search)

1. `youtube_video_details` for each selected video (exact views, likes, publish time, length, hasCaption) and for the median video of the normal window plus any videos tied with it on the list.
2. `get_bulk_video_transcripts` once for all Helper C videos. The output was saved by the tool to a local file; a script turned each `transcript` array into `[m:ss] text`, one line per segment (h:mm:ss past one hour), start time from `startMs`.
3. `youtube_video_comments` sort=top: page 1, then 2 more pages, each with the newest continuation token (per the main session's tip); sort=newest: 1 page. Comment text and like counts were copied into scratch files (no usernames, no channel IDs) and assembled into `comments.md` by script; duplicates across pages were removed by matching the comment text; @handles inside comment text replaced with "@[handle removed]"; owner comments (API `authorIsChannelOwner=true`) marked [OWNER].
4. `youtube_channel_videos` sort=newest, page 1 (30 uploads) for the normal window; `check_faceless_channel` for the format.
5. **How the normal was taken.** The list gives display view counts that are truncated (for example "37K" for an exact 37,888) and relative dates. The 15-video window was ranked on the list values; exact views were then fetched with `youtube_video_details` for the median video and for any video whose display value ties with it. Because the display values are truncated, not rounded, a video showing a higher display value always has more exact views, so the order holds except inside a tie, and ties were resolved with exact counts. The other window videos were not fetched one by one (their exact counts are not needed for the median).

## Normal: 2,719

Median of the exact views of the 15 most recent long-form uploads (5:00+, Videos tab so not Shorts) at least 7 days old on 2026-10-27, from `youtube_channel_videos` sort=newest on 2026-10-27. "List date" is the approximate date from the relative time ("3 months ago"); "list views" is the truncated display value.

| # | Video ID | Duration | List date (approx.) | List views | Exact views | Status |
|---|---|---|---|---|---|---|
| – | qDzI9pvP9GE | 13:23 | 2026-10-26 (16 hours ago) | 2,300 |  | out<7 days |
| – | DB81QvLW4lQ | 14:42 | 2026-10-25 (2 days ago) | 2,800 |  | out<7 days |
| – | q0MrIYDkPmM | 13:04 | 2026-10-24 (3 days ago) | 3,200 |  | out<7 days |
| – | urqk4J93K0Y | 24:14 | 2026-10-22 (5 days ago) | 1,800 |  | out<7 days |
| – | HANFZaK1yJ4 | 19:12 | 2026-10-21 (6 days ago) | 1,400 |  | out<7 days (same title as E3p1V2wiQDc) |
| – | 3tsYa7aOprw | 21:12 | 2026-10-21 (6 days ago) | 1,800 |  | out<7 days |
| 1 | E3p1V2wiQDc | 17:58 | 2026-10-20 (7 days ago) | 2,200 |  | in (exact upload 2026-10-19 07:45 -07:00 per plumbing study log, 8 days old) |
| 2 | nxb3nS21zgg | 18:58 | 2026-10-18 (9 days ago) | 2,200 |  | in |
| 3 | 8BZZwj93dkQ | 16:31 | 2026-10-17 (10 days ago) | 7,900 |  | in |
| 4 | 3GMK8QAmagA | 19:14 | 2026-10-16 (11 days ago) | 2,900 |  | in |
| 5 | ihZc3VGeG6c | 18:25 | 2026-10-15 (12 days ago) | 2,200 |  | in |
| 6 | n-2hjVGsu-Q | 24:50 | 2026-10-14 (13 days ago) | 2,300 |  | in |
| 7 | oh_jTNw1sjs | 25:54 | 2026-10-13 (2 weeks ago) | 6,800 |  | in |
| 8 | R-hbXQFUrzQ | 29:08 | 2026-10-13 (2 weeks ago) | 2,700 | **2,719** (median) | in |
| 9 | eeM7RjlKbA0 | 22:54 | 2026-10-13 (2 weeks ago) | 2,800 |  | in |
| 10 | qyvLwKZuUAk | 21:45 | 2026-10-13 (2 weeks ago) | 1,900 |  | in |
| 11 | zO-vXxXafdQ | 21:18 | 2026-10-13 (2 weeks ago) | 8,000 |  | in |
| 12 | 1i8TevJix6g | 20:27 | 2026-10-06 (3 weeks ago) | 2,100 |  | in |
| 13 | L7QAYvm1_M8 | 24:42 | 2026-10-06 (3 weeks ago) | 27,000 |  | in |
| 14 | 8eiXxw4uPV4 | 28:46 | 2026-10-06 (3 weeks ago) | 3,700 |  | in |
| 15 | WWjzsYKWEV0 | 23:44 | 2026-10-06 (3 weeks ago) | 1,600 |  | in(15th) |
| – | h3pwIHvb2UQ | 19:38 | 2026-10-06 (3 weeks ago) | 4,100 |  | beyond window |

Source note: median exact: R-hbXQFUrzQ 2719 views (details 2026-10-27; published 2026-10-09T12:00:24-07:00; 1748 s; list neighbours n-2hjVGsu-Q 2.3K below and eeM7RjlKbA0 2.8K above; list counts are truncated so order holds)

Excluded as under 7 days old: qDzI9pvP9GE, DB81QvLW4lQ, q0MrIYDkPmM, urqk4J93K0Y, HANFZaK1yJ4 (same title as E3p1V2wiQDc), 3tsYa7aOprw (list "16 hours" to "6 days ago"). E3p1V2wiQDc shows "7 days ago"; its exact upload is 2026-10-19 07:45 -07:00 (plumbing study log), 8 days old, so it is in. The selected video cFYptbCvNjI (2026-08-27) is older than the window, which reaches back to 2026-10-06 only, because the channel uploads almost daily.

## Transcripts

| Video ID | Segments | Words | Track |
|---|---|---|---|
| cFYptbCvNjI | 581 | 3,388 | auto-generated |

No transcript gaps over 20 s.

## Comments

| Video ID | API commentsCount | Pages fetched | Top | Newest | In both | Unique | [OWNER] | Spam skipped |
|---|---|---|---|---|---|---|---|---|
| cFYptbCvNjI | 6 | top: 1 page (5 comments, no continuation token returned); newest: 1 page (same 5) | 5 | 5 | 5 | 5 | 0 | 0 |

Username/handle check: comments.md holds comment text and like counts only; no usernames or channel IDs.

## Failures and API oddities

- The top comment (32 likes) names a service company ("american residential services is one option for that kind of visit"); recorded as written and noted here.
- The spoken CTA in the transcript reads "subscribe to Roger the plumber guy" [23:08] (caption text as returned).
- Normal comparison: plumbing study (2026-10-20) 2,688; this study 2,719. `inputs/videos.md` lists the video at 9.0x; with the fresh normal and views it is 13.64x.
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

