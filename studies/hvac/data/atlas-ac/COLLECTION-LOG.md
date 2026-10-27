# Collection log — Atlas AC (Helper A)

Collected 2026-10-27 by collector helper A following `studies/hvac/study-brief.md` and `inputs/videos.md`. Describe-only; no judgements.

## Channel

- Name: Atlas AC
- Handle: @atlasacrepair
- Channel ID: UCWtuOnlW7BeXLgr6M1_Z49g
- Subscribers: 32.7K (channel_videos meta, 2026-10-27)
- About (from `youtube_channel_videos` meta): "Atlas AC Repair is a residential air conditioning and heating company serving San Antonio, Austin, Arlington/Dallas-Fort Worth and Houston, Texas. This chann..." (truncated by the API)

## Videos collected (selection rows from inputs/videos.md)

| Row | Video ID | Type | Views (2026-10-27) | Duration | Views / normal |
|---|---|---|---|---|---|
| 9 | r_uP9itJ0HQ | brand verdict | 1,873,990 | 15:23 | 88.63 |

All rows assigned to Helper A for this channel were collected; none skipped.

## Format: ON CAMERA

NexLev `check_faceless_channel` (regular videos, cached 2026-10-27T03:36Z): isFaceless=false, confidence 0.95, primary category "do it yourself", format "tutorial". Channel description: a Texas AC repair company. Video description: "Regulated by The Texas Department of Licensing and Regulation". Transcript: presenter introduces himself, "hi this is Kenneth with Atlas AC" [0:18], company voice ("our primary brand that we sell"). One comment addresses his delivery ("you present with a very fast speech"). Whether he is on screen throughout cannot be confirmed from transcript and comments; recorded as ON CAMERA on NexLev's classification plus the named presenter.

## Method (NexLev MCP tools only, no web search)

1. `youtube_video_details` for each selected video (exact views, likes, publish time, length, isShortsEligible) and for every video in the normal window plus the 16th upload (boundary check).
2. `get_bulk_video_transcripts` once for all 9 Helper A videos (9/9 successful). The tool output was too large to show inline and was saved by the tool to a local file; a script converted each `transcript` array to `[m:ss] text`, one line per segment, start time from `startMs` (HTML entities unescaped, whitespace collapsed). Every track is "English (auto-generated)".
3. `youtube_video_comments` sort=top and sort=newest, one page each per video (see API oddities). Comment text and like counts were copied by hand into scratch files (no usernames, no channel IDs) and assembled into `comments.md` by script; @handles inside comment text are replaced with "@[handle removed]" (none occurred); owner comments identified by the API field `authorIsChannelOwner=true` and marked [OWNER].
4. `youtube_channel_videos` sort=newest, page 1 (30 uploads) for the normal window; `check_faceless_channel` for the format.
5. Long-form for the normal = 5:00 or longer and not a Short (Videos tab only; every video checked has `isShortsEligible=false`).

## Normal: 21,145

Median of exact views (`youtube_video_details`, 2026-10-27) of the 15 most recent long-form uploads (5:00+, not Shorts) at least 7 days old on 2026-10-27, taken in upload order from `youtube_channel_videos` sort=newest.

| # | Video ID | Published | Duration | Views |
|---|---|---|---|---|
| 1 | 661ea-MrdfY | 2026-09-15 | 10:25 | 10,810 |
| 2 | MJjX6QASDYw | 2026-08-18 | 10:03 | 59,578 |
| 3 | ikFvdsNKaMQ | 2026-07-27 | 10:17 | 10,044 |
| 4 | itDfycFTLfw | 2026-07-13 | 10:09 | 62,077 |
| 5 | 8u2810Yk5OA | 2026-06-23 | 14:37 | 1,464 |
| 6 | j0AP_PNCi7s | 2026-04-08 | 17:34 | 103,660 |
| 7 | hXQpvHN-cnE | 2026-03-16 | 19:11 | 3,880 |
| 8 | jQk0hNktOag | 2026-01-28 | 7:10 | 2,711 |
| 9 | JOmmbClpya0 | 2026-01-23 | 19:37 | 29,113 |
| 10 | zxwSG7ICWpY | 2025-12-01 | 14:42 | 21,145 |
| 11 | PxjklIvU7o0 | 2025-12-01 | 19:12 | 19,244 |
| 12 | DxOMhHEeUUs | 2025-09-04 | 17:36 | 445,429 |
| 13 | ntQ-OaE_A2M | 2025-08-15 | 33:08 | 120,682 |
| 14 | x3khwp4NiCQ | 2025-06-26 | 22:12 | 137,942 |
| 15 | rOzuB-PeAvg | 2025-06-05 | 14:51 | 15,088 |

Sorted: 1,464 · 2,711 · 3,880 · 10,044 · 10,810 · 15,088 · 19,244 · **21,145** · 29,113 · 59,578 · 62,077 · 103,660 · 120,682 · 137,942 · 445,429.

Excluded as under 5:00 (list lengthText; not detail-checked): Bdju5w1MRGM "Variable Speed - Post Install Thoughts.mp4" 3:29 (sits between PxjklIvU7o0 and DxOMhHEeUUs in upload order) and W6QXjNYEv_k 4:42 (later than the window anyway). Nothing in the list was under 7 days old (newest 661ea-MrdfY, 2026-09-15).

16th long-form upload: 8UYhXhTmFDc, 2025-05-19, 11:42, 139,510 views. Note jQk0hNktOag is 7:10 (430 s) and counts as long-form. The window reaches back to 2025-06-05; the selected video (2022) is outside it. The channel posts irregularly, so the window spans about 16 months.

## Transcripts

| Video ID | Segments | Words | Track |
|---|---|---|---|
| r_uP9itJ0HQ | 380 | 2,746 | English (auto-generated) |

No video was skipped for a missing transcript.

## Comment totals

| Video ID | API commentsCount | Top | Newest | Unique | In both | [OWNER] comments |
|---|---|---|---|---|---|---|
| r_uP9itJ0HQ | 3.4K | 20 | 20 | 40 | 0 | 0 |

Unique comments collected for this channel: 40. Spam skipped: 0. Username/handle check run on comments.md: no usernames, channel IDs or @handles remain.

## Failures and API oddities

- **Comment pagination did not advance** (same as the plumbing study). On mP0IjyvQtxw sort=top, the continuation token was passed twice (the first token, then the token returned with the second page); both calls returned the same first 20 comments as the first call. So every list holds 20 comments, not the brief's ~60 top + ~20 newest. No other comment method was used. Per the helper instructions (retry, then log and move on), the other videos were collected with one page per sort.
- In sort=newest, an older comment is listed first on several videos (the owner's pinned comment where one exists; on others a high-like viewer comment, likely pinned; the API does not flag pins). Marked in `comments.md`.
- Comment like counts of 1,000+ come rounded ("1.2K"); blank like counts (" ") recorded as 0. Comment dates are relative and approximate.
- `youtube_channel_videos` list dates are placeholders (e.g. "1 month ago" shown as 2026-09-27) and view counts are rounded; exact dates and views come from `youtube_video_details`.
- `youtube_video_details` returns `hasCaption: false` for every video, yet transcripts came back for all.
- `channel_videos` meta reports videosCount 31 for each channel (page size), not the channel total.
- No call failed; no retries were needed except the pagination test above.

## Checks (helper self-check, 2026-10-27)

- meta.md vs fresh `youtube_video_details` (2026-10-27, after the notes): **r_uP9itJ0HQ** meta 1,873,990 views / 40,459 likes / 15:23 (923 s) / 2022-11-28; fresh 1,873,990 / 40,459 / 923 s / 2022-11-28T13:11:01-08:00. All match.
- Quoted lines vs transcript: [8:49] "it looks and smells like a builder grade system to me" found; the note first had [8:52] (the line containing "smells"), corrected to [8:49]. The all-quotes script found every quote; one more timestamp corrected ([0:35] like-button ask, first written [0:31]); one paraphrase in quote marks rewritten.

## Notes written

- notes/atlas-ac__r_uP9itJ0HQ.md

Note length: the brief asks for about 300-400 words per note. With every required section (including the four HVAC ones) the notes run about 530-700 words by `wc -w`, which also counts headings, timestamps, URLs and like counts. The plumbing study's notes (250-350 asked) run about 510-540 by the same count.
