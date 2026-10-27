# Collection log — Technology Connections (Helper C)

Collected 2026-10-27 by collector helper C following `studies/hvac/study-brief.md` and `inputs/videos.md`. Describe-only; no judgements.

## Channel

- Name: Technology Connections
- Handle: @TechnologyConnections
- Channel ID: UCy0tKL1T7wFoYcxCe0xjN6Q
- Subscribers: 3.22M (youtube_channel_videos meta, 2026-10-27)
- No Shorts tab on the channel. Description of HnMuNCl7tZ8 says the channel has "never done a brand deal"; Patreon-funded.

## Videos collected (selection rows from inputs/videos.md)

| Row | Video ID | Type | Views (2026-10-27) | Duration | Normal | Views / normal | Transcript segments | Comments (unique) |
|---|---|---|---|---|---|---|---|---|
| 21 | HnMuNCl7tZ8 | never-do / safety | 2,951,229 | 28:55 | 1,927,750 | 1.53 | 687 | 43 |
| 22 | 7J52mDjZzto | decision versus (an explainer) | 4,846,403 | 35:15 | 1,927,750 | 2.51 | 583 | 38 |

All rows assigned to Helper C for this channel were collected.

## Format

ON CAMERA. Basis: NexLev `check_faceless_channel` isFaceless=false, confidence 0.95, format "educational" (cached, 2026-10-27); presenter narrates his own bench tests in first person and closes with a blooper reel; comments address the presenter directly.

## Method (NexLev MCP tools only, no web search)

1. `youtube_video_details` for each selected video (exact views, likes, publish time, length, hasCaption) and for the median video of the normal window plus any videos tied with it on the list.
2. `get_bulk_video_transcripts` once for all Helper C videos. The output was saved by the tool to a local file; a script turned each `transcript` array into `[m:ss] text`, one line per segment (h:mm:ss past one hour), start time from `startMs`.
3. `youtube_video_comments` sort=top: page 1, then 2 more pages, each with the newest continuation token (per the main session's tip); sort=newest: 1 page. Comment text and like counts were copied into scratch files (no usernames, no channel IDs) and assembled into `comments.md` by script; duplicates across pages were removed by matching the comment text; @handles inside comment text replaced with "@[handle removed]"; owner comments (API `authorIsChannelOwner=true`) marked [OWNER].
4. `youtube_channel_videos` sort=newest, page 1 (30 uploads) for the normal window; `check_faceless_channel` for the format.
5. **How the normal was taken.** The list gives display view counts that are truncated (for example "37K" for an exact 37,888) and relative dates. The 15-video window was ranked on the list values; exact views were then fetched with `youtube_video_details` for the median video and for any video whose display value ties with it. Because the display values are truncated, not rounded, a video showing a higher display value always has more exact views, so the order holds except inside a tie, and ties were resolved with exact counts. The other window videos were not fetched one by one (their exact counts are not needed for the median).

## Normal: 1,927,750

Median of the exact views of the 15 most recent long-form uploads (5:00+, Videos tab so not Shorts) at least 7 days old on 2026-10-27, from `youtube_channel_videos` sort=newest on 2026-10-27. "List date" is the approximate date from the relative time ("3 months ago"); "list views" is the truncated display value.

| # | Video ID | Duration | List date (approx.) | List views | Exact views | Status |
|---|---|---|---|---|---|---|
| 1 | 0KoeY54M5VA | 50:37 | 2026-09-27 (1 month ago) | 2,300,000 |  | in |
| 2 | F_7B2shTPPU | 58:45 | 2026-08-27 (2 months ago) | 1,800,000 |  | in |
| 3 | _KWdCqpXB7A | 1:11:11 | 2026-06-27 (4 months ago) | 3,600,000 |  | in |
| 4 | KnUFH5GX_fI | 55:51 | 2026-05-27 (5 months ago) | 3,000,000 |  | in |
| 5 | nXdVG45wveo | 24:11 | 2026-04-27 (6 months ago) | 1,100,000 |  | in |
| 6 | mmCfOazZCNQ | 54:46 | 2026-03-27 (7 months ago) | 1,900,000 | **1,927,750** (median) | in |
| 7 | KtQ9nt2ZeGM | 1:32:00 | 2026-02-27 (8 months ago) | 4,900,000 |  | in |
| 8 | tCVsyY5TRQI | 34:39 | 2025-12-27 (10 months ago) | 891,000 |  | in |
| 9 | oy7BrKNmZAQ | 33:48 | 2025-12-27 (10 months ago) | 1,100,000 |  | in |
| 10 | INZybkX8tLI | 23:16 | 2025-12-27 (10 months ago) | 1,100,000 |  | in |
| 11 | 8I4Jc-WLsrs | 27:28 | 2025-11-27 (11 months ago) | 844,000 |  | in |
| 12 | DAX2_mPr9W8 | 41:27 | 2025-11-27 (11 months ago) | 3,500,000 |  | in |
| 13 | ms8uu0zeU88 | 34:40 | 2025-10-27 (1 year ago) | 2,500,000 |  | in |
| 14 | Aytf6ARcs8s | 41:47 | 2025-10-27 (1 year ago) | 1,900,000 | 1,924,417 | in |
| 15 | JzClLWL-Eys | 29:20 | 2025-10-27 (1 year ago) | 1,900,000 | 1,942,271 | in(15th) |
| – | HFYWHeBhYbM | 32:37 | 2025-10-27 (1 year ago) | 1,200,000 |  | beyond window |

Source note: exact (details 2026-10-27): mmCfOazZCNQ 1927750 (2026-03-21T08:39:02-07:00, 3285 s); Aytf6ARcs8s 1924417 (2025-10-01T08:23:12-07:00, 2506 s); JzClLWL-Eys 1942271 (2025-08-31T08:30:47-07:00, 1760 s). Positions 7-9 = 1924417, 1927750, 1942271 -> median mmCfOazZCNQ 1927750. Neighbour 1.8M (F_7B2shTPPU) below, 2.3M above.

Three uploads show "1.9M" on the list (a tie in the truncated display), so all three were fetched exactly: Aytf6ARcs8s 1,924,417; mmCfOazZCNQ 1,927,750; JzClLWL-Eys 1,942,271. Positions 7 to 9 in sorted order, so the median (8th) is mmCfOazZCNQ. Nothing under 5:00 or under 7 days old in the window.

## Transcripts

| Video ID | Segments | Words | Track |
|---|---|---|---|
| HnMuNCl7tZ8 | 687 | 4,690 | auto-generated |
| 7J52mDjZzto | 583 | 5,923 | English (not auto-generated) |

No transcript gaps over 20 s.

## Comments

| Video ID | API commentsCount | Pages fetched | Top | Newest | In both | Unique | [OWNER] | Spam skipped |
|---|---|---|---|---|---|---|---|---|
| HnMuNCl7tZ8 | 6K | top: page 1 (20) + page 2 (+3 new) + page 3 (no new); newest: 1 page | 23 | 20 | 0 | 43 | 0 | 0 |
| 7J52mDjZzto | 10K | top: page 1 (20) + page 2 (no new) + page 3 (no new); newest: 1 page | 20 | 20 | 2 | 38 | 1 | 0 |

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

