# Collection log — How To Home (Helper A)

Collected 2026-10-27 by collector helper A following `studies/hvac/study-brief.md` and `inputs/videos.md`. Describe-only; no judgements.

## Channel

- Name: How To Home
- Handle: @HowToHomeDIY
- Channel ID: UCpb-xu6Oun_d41RjztUgFWA
- Subscribers: 855K (channel_videos meta, 2026-10-27)
- About (from `youtube_channel_videos` meta): "Hey, I'm Adam! I am not a professional electrician, plumber, or HVAC tech, I am a fellow DIYer who loves to install, and make repairs on my own home and prop..." (truncated by the API)

## Videos collected (selection rows from inputs/videos.md)

| Row | Video ID | Type | Views (2026-10-27) | Duration | Views / normal |
|---|---|---|---|---|---|
| 7 | i8nDBZo6XyE | cheap-part repair | 2,195,875 | 11:40 | 8.14 |
| 8 | AQQH9QwC46A | N things / insider | 2,980,456 | 12:40 | 11.05 |

All rows assigned to Helper A for this channel were collected; none skipped.

## Format: ON CAMERA

NexLev `check_faceless_channel` (regular videos, cached 2026-10-27T03:36Z): isFaceless=false, confidence 0.95, primary category "do it yourself", format "tutorial", tags do it yourself / home repair / engineering / tech. Channel description "Hey, I'm Adam! I am not a professional ... HVAC tech, I am a fellow DIYer". Descriptions signed "Blessings, Adam" and mention "shirts I use and wear in my videos". Transcripts are first-person narration of his own repairs. Comments address him directly ("You handsome SOB, it worked"). The channel owner's comments carry isVerified=true.

## Method (NexLev MCP tools only, no web search)

1. `youtube_video_details` for each selected video (exact views, likes, publish time, length, isShortsEligible) and for every video in the normal window plus the 16th upload (boundary check).
2. `get_bulk_video_transcripts` once for all 9 Helper A videos (9/9 successful). The tool output was too large to show inline and was saved by the tool to a local file; a script converted each `transcript` array to `[m:ss] text`, one line per segment, start time from `startMs` (HTML entities unescaped, whitespace collapsed). Every track is "English (auto-generated)".
3. `youtube_video_comments` sort=top and sort=newest, one page each per video (see API oddities). Comment text and like counts were copied by hand into scratch files (no usernames, no channel IDs) and assembled into `comments.md` by script; @handles inside comment text are replaced with "@[handle removed]" (none occurred); owner comments identified by the API field `authorIsChannelOwner=true` and marked [OWNER].
4. `youtube_channel_videos` sort=newest, page 1 (30 uploads) for the normal window; `check_faceless_channel` for the format.
5. Long-form for the normal = 5:00 or longer and not a Short (Videos tab only; every video checked has `isShortsEligible=false`).

## Normal: 269,689

Median of exact views (`youtube_video_details`, 2026-10-27) of the 15 most recent long-form uploads (5:00+, not Shorts) at least 7 days old on 2026-10-27, taken in upload order from `youtube_channel_videos` sort=newest.

| # | Video ID | Published | Duration | Views |
|---|---|---|---|---|
| 1 | YlPhqsMeegs | 2026-10-10 | 13:32 | 141,002 |
| 2 | eagOP0bRePM | 2026-09-26 | 15:53 | 269,689 |
| 3 | 1XYHUBFwMo0 | 2026-08-22 | 15:54 | 256,351 |
| 4 | NXBtYTZNBzw | 2026-07-18 | 13:49 | 366,945 |
| 5 | 934fwlPwG5M | 2026-07-03 | 14:55 | 169,208 |
| 6 | Q8EwxVM4uaM | 2026-06-13 | 14:40 | 113,445 |
| 7 | gQjotD-B0OU | 2026-05-16 | 13:07 | 1,770,100 |
| 8 | 4p6tGOlsLbM | 2026-05-02 | 14:57 | 464,220 |
| 9 | wMHIfUIVuJA | 2026-04-18 | 14:14 | 601,319 |
| 10 | psieFs6qG3I | 2026-03-28 | 14:23 | 522,826 |
| 11 | XYbEjHKFp08 | 2026-03-07 | 26:28 | 60,128 |
| 12 | sCZ9aac_7nI | 2026-02-21 | 18:57 | 32,753 |
| 13 | kDVvn6NCYO8 | 2026-02-07 | 19:39 | 45,836 |
| 14 | K-whqrbfQ-o | 2026-01-24 | 21:44 | 841,667 |
| 15 | k1ckcgTPmrM | 2026-01-10 | 21:08 | 375,045 |

Sorted: 32,753 · 45,836 · 60,128 · 113,445 · 141,002 · 169,208 · 256,351 · **269,689** · 366,945 · 375,045 · 464,220 · 522,826 · 601,319 · 841,667 · 1,770,100.

Not in the window: MH8Lo6fuWyc (list "2 days ago"), under 7 days old. All 30 listed uploads are 10:08 or longer.

16th upload: ks1LWjWpiDU, 2025-12-13, 35:11, 227,527 views. Neither selected video falls in the window (both 2023).

## Transcripts

| Video ID | Segments | Words | Track |
|---|---|---|---|
| i8nDBZo6XyE | 339 | 2,568 | English (auto-generated) |
| AQQH9QwC46A | 370 | 2,846 | English (auto-generated) |

No video was skipped for a missing transcript.

## Comment totals

| Video ID | API commentsCount | Top | Newest | Unique | In both | [OWNER] comments |
|---|---|---|---|---|---|---|
| i8nDBZo6XyE | 3.3K | 20 | 20 | 34 | 6 | 1 |
| AQQH9QwC46A | 2.7K | 20 | 20 | 38 | 2 | 1 |

Unique comments collected for this channel: 72. Spam skipped: 0 (nothing obvious; one Spanish-language comment about the dubbed audio track on i8nDBZo6XyE was kept). Username/handle check run on every comments.md: no usernames, channel IDs or @handles remain.

## Failures and API oddities

- **Comment pagination did not advance** (same as the plumbing study). On mP0IjyvQtxw sort=top, the continuation token was passed twice (the first token, then the token returned with the second page); both calls returned the same first 20 comments as the first call. So every list holds 20 comments, not the brief's ~60 top + ~20 newest. No other comment method was used. Per the helper instructions (retry, then log and move on), the other videos were collected with one page per sort.
- In sort=newest, an older comment is listed first on several videos (the owner's pinned comment where one exists; on others a high-like viewer comment, likely pinned; the API does not flag pins). Marked in `comments.md`.
- Comment like counts of 1,000+ come rounded ("1.2K"); blank like counts (" ") recorded as 0. Comment dates are relative and approximate.
- `youtube_channel_videos` list dates are placeholders (e.g. "1 month ago" shown as 2026-09-27) and view counts are rounded; exact dates and views come from `youtube_video_details`.
- `youtube_video_details` returns `hasCaption: false` for every video, yet transcripts came back for all.
- `channel_videos` meta reports videosCount 31 for each channel (page size), not the channel total.
- No call failed; no retries were needed except the pagination test above.

## Checks (helper self-check, 2026-10-27)

- meta.md vs fresh `youtube_video_details` (2026-10-27, after the notes): **AQQH9QwC46A** meta 2,980,456 views / 82,708 likes / 12:40 (760 s) / 2023-04-29; fresh 2,980,460 views (+4) / 82,707 likes (-1) / 760 s / 2023-04-29T09:30:02-07:00. Duration and date match; views and likes moved slightly over the session. Meta values left as first collected.
- Quoted lines vs transcript: [6:54] "the bug or Whatever Gets inside of there can actually serve as an insulator" (AQQH9QwC46A) found; the note first had [6:56] and a capital "The", corrected to the transcript's [6:54] and lower case. The all-quotes script (see the DIY HVAC Guy log) found every quote in both notes; one timestamp corrected ([7:24] "I'm not super good at math", i8nDBZo6XyE, first written [7:28]). Two segment labels that paraphrased in quote marks were rewritten without quote marks.

## Notes written

- notes/how-to-home__i8nDBZo6XyE.md
- notes/how-to-home__AQQH9QwC46A.md

Note length: the brief asks for about 300-400 words per note. With every required section (including the four HVAC ones) the notes run about 530-700 words by `wc -w`, which also counts headings, timestamps, URLs and like counts. The plumbing study's notes (250-350 asked) run about 510-540 by the same count.
