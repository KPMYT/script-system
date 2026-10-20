# Collection log: Roger Wakefield Plumbing Education

Collected 2026-10-20 by a helper agent, following `studies/plumbing/study-brief.md`.

## Channel

- Name: Roger Wakefield Plumbing Education (@RogerWakefield)
- Channel ID: UCGIMKh92vaL0_Yc0u4GYhHA
- Group: competitor
- About (youtube_channel_about): 732K subscribers, 158,571,387 views, "2,302 videos", joined 2014-10-24, United States. The description is first person: "I'm Roger Wakefield, a Texas Master Plumber and LEED AP with over 40 years of experience".

## Method (NexLev MCP only)

1. `youtube_channel_about` and `check_faceless_channel` for the channel.
2. `youtube_channel_videos` sorted newest (page 1, 30 videos) and sorted popular (pages 1–4, 120 videos, using the continuation token).
3. `youtube_video_details` to confirm exact date, duration and views: the 15 newest long-form uploads, plus every popular-list candidate in or near the 24-month window (ranks 12, 23, 26, 37, 40, 48, 60, 65, 78, 85, 90, 100, 106).
4. `get_bulk_video_transcripts`: one call for VxkL-T0U-r0, one call for the other 9. All 10 returned transcripts.
5. `youtube_video_comments`: top and newest for each video (see the comments section).
6. Long-form = 3:00 or longer and not a Short. Every video on the newest page was 7:11 or longer; no Shorts appeared in the Videos tab.

## Format: FACE

Basis:
- `check_faceless_channel`: isFaceless=false, confidence 0.98, format "commentary", tags business / education / news / life stories (fresh analysis, 2026-10-20).
- About text: first person from Roger Wakefield.
- Transcripts: first-person talk to camera (Group A), a sit-down interview (VxkL-T0U-r0), a reaction over another creator's video (OEbAeVn6DHg), and hands-on shop or bench demos (zfrqkteUPAI, 1kWd9HidNJk).
- Comments react to his on-camera presence (red shirt and green gloves, camera angles "talking off into space").
- Also recorded: three comments on 2026 uploads mention AI. RGH2k2G8oaQ: "this is AI for much of the acting you see on screen". f8-sd5Zw0E4: "smothered in AI slop". Wav7A7YhduY: "why did YouTube give him an ai tag". The presenter is still Roger, so the format stays FACE.

## Normal

The 15 most recent long-form uploads at least 7 days old as of 2026-10-20, with exact views from `youtube_video_details`:

| # | Video ID | Published | Views |
|---|---|---|---|
| 1 | VxkL-T0U-r0 | 2026-10-12 | 6308 |
| 2 | RGH2k2G8oaQ | 2026-07-09 | 2683 |
| 3 | Wav7A7YhduY | 2026-07-06 | 3180 |
| 4 | f8-sd5Zw0E4 | 2026-07-02 | 97050 |
| 5 | TVi8z3unRlM | 2026-06-29 | 3678 |
| 6 | -TWW5o5DVos | 2026-06-25 | 4460 |
| 7 | NXYOn28vpbs | 2026-06-22 | 1323 |
| 8 | u1i8U7ugJZE | 2026-06-18 | 10136 |
| 9 | 2HoEPWRTQ9w | 2026-06-15 | 3018 |
| 10 | F3wluqIM7ng | 2026-06-11 | 16688 |
| 11 | kF7xIBzlQmI | 2026-06-08 | 11916 |
| 12 | hUXlIjWC7qU | 2026-06-04 | 5210 |
| 13 | 8FPwN9MS64c | 2026-06-01 | 7841 |
| 14 | 4hW1CzKCz5s | 2026-05-28 | 3944 |
| 15 | x_qV-LF7NS4 | 2026-05-25 | 16920 |

Sorted: 1323, 2683, 3018, 3180, 3678, 3944, 4460, **5210**, 6308, 7841, 10136, 11916, 16688, 16920, 97050.

**Normal = 5210** (the 8th of 15).

VxkL-T0U-r0 (published 2026-10-12 14:00 -07:00) is 8 days old, so it counts.

## Group A: 5 most recent long-form

| # | Video ID | Title | Published | Duration | Views | Views/normal |
|---|---|---|---|---|---|---|
| 1 | VxkL-T0U-r0 | How Much Do Plumbers Make Here? $104,000 at the Bottom | 2026-10-12 | 10:41 | 6308 | 1.21 |
| 2 | RGH2k2G8oaQ | Why college kids quit for the trades | 2026-07-09 | 16:54 | 2683 | 0.51 |
| 3 | Wav7A7YhduY | 🚨 The #1 reason water damage insurance claims get denied isn't the leak it's ONE word buried in | 2026-07-06 | 16:33 | 3180 | 0.61 |
| 4 | f8-sd5Zw0E4 | 🚨 The Trade School Bubble Is About to Burst — And Nobody Is Talking About It 🚨 | 2026-07-02 | 13:04 | 97050 | 18.63 |
| 5 | TVi8z3unRlM | What no one tells you about starting Plumbing business | 2026-06-29 | 17:31 | 3678 | 0.71 |

The next two uploads (-TWW5o5DVos, NXYOn28vpbs) were kept as backups. They were not needed.

## Group B: 5 most-viewed long-form published on or after 2024-10-20

I paged the popular list 4 times (ranks 1–120). Ranks 1–22 are all dated before the window (list dates of 3–8 years ago). I checked every candidate with `youtube_video_details`:

| Popular rank | Video ID | Exact publish date | Views | Result |
|---|---|---|---|---|
| 12 | -8zDDMPyp1Q | 2024-01-30 | 1122750 | before window, skipped |
| **23** | **OEbAeVn6DHg** | 2025-05-07 | 742479 | **Group B #1** |
| 26 | WgRI042MLFg | 2024-04-30 | 726580 | before window, skipped |
| 37 | 0IT9pEAyM04 | 2024-08-08 | 578079 | before window, skipped |
| 40 | C_5dlaW37YM | 2024-04-25 | 541461 | before window, skipped |
| 48 | pO9In9CP7IY | 2024-09-03 | 436837 | before window, skipped |
| 60 | p7ZP2RVUm2Q | 2024-07-09 | 338169 | before window, skipped |
| 65 | GZORiYBa-6U | 2024-01-16 | 318083 | before window, skipped |
| **78** | **ooWoKmqrooU** | 2024-12-19 | 259436 | **Group B #2** |
| **85** | **zfrqkteUPAI** | 2026-03-30 | 247030 | **Group B #3** |
| 90 | 0bFGXtXvZsc | 2024-03-14 | 238289 | before window, skipped |
| **100** | **WXJGaGtXrgY** | 2025-12-04 | 206645 | **Group B #4** |
| **106** | **1kWd9HidNJk** | 2025-11-20 | 195478 | **Group B #5** |

None of the Group A videos ranked above rank 106 (the highest, f8-sd5Zw0E4, has 97,050 views), so no Group B pick had to be skipped for overlap. The next in-window candidate, which was not needed, is K5O01f6Br2E (rank 117, list date "1 year ago", 168K views).

Group B with titles:

| Rank | Video ID | Title | Published | Duration | Views | Views/normal |
|---|---|---|---|---|---|---|
| 23 | OEbAeVn6DHg | Real Plumber Breaks Down DIY Toilet Install | 2025-05-07 | 17:23 | 742479 | 142.51 |
| 78 | ooWoKmqrooU | Top Paying Trades Jobs of 2025 | 2024-12-19 | 11:39 | 259436 | 49.80 |
| 85 | zfrqkteUPAI | FLUSHING A Water Heater The RIGHT WAY Step by Step | 2026-03-30 | 10:04 | 247030 | 47.41 |
| 100 | WXJGaGtXrgY | 🔥 Don’t Buy a New Water Heater Until You Watch This! Tank vs Tankless – The TRUTH | 2025-12-04 | 9:13 | 206645 | 39.66 |
| 106 | 1kWd9HidNJk | How to Solder Copper Pipe Like a PRO in 5 Minutes | 2025-11-20 | 13:12 | 195478 | 37.52 |

## Skipped videos

- Group B: the eight popular-list videos marked "before window" above.
- No video was skipped for a missing transcript. All 10 returned full transcripts, even though `youtube_video_details` reports `hasCaption: false` for every one of them.

## Transcripts

| Video ID | Segments | Span | Words |
|---|---|---|---|
| VxkL-T0U-r0 | 327 | 0:00–10:19 | 2325 |
| RGH2k2G8oaQ | 404 | 0:00–16:52 | 2830 |
| Wav7A7YhduY | 421 | 0:00–16:30 | 2887 |
| f8-sd5Zw0E4 | 346 | 0:00–13:02 | 2283 |
| TVi8z3unRlM | 463 | 0:00–17:28 | 2922 |
| OEbAeVn6DHg | 430 | 0:00–17:20 | 2898 |
| ooWoKmqrooU | 290 | 0:00–11:38 | 2021 |
| zfrqkteUPAI | 298 | 0:00–10:01 | 2271 |
| WXJGaGtXrgY | 219 | 0:00–9:08 | 1575 |
| 1kWd9HidNJk | 340 | 0:00–13:10 | 2295 |

Timestamps are written as `[m:ss]` from each segment's startMs. HTML entities are decoded. The text is otherwise as returned.

## Comments

All comments are top-level. Text and like counts only; no usernames. A blank like count is written as 0, and "1.1K" is written as returned. Handles inside comment text were checked for: none found. One self-identified personal name inside a comment was replaced with "[name removed]" (VxkL-T0U-r0). Comments by the channel itself are marked [channel owner].

| Video ID | API commentsCount (incl. replies) | Top | Newest | In both | Unique | Spam skipped |
|---|---|---|---|---|---|---|
| VxkL-T0U-r0 | 14 | 12 | 13 | 12 | 13 | 0 |
| RGH2k2G8oaQ | 32 | 20 | 20 | 17 | 23 | 0 |
| Wav7A7YhduY | 17 | 13 | 13 | 13 | 13 | 0 |
| f8-sd5Zw0E4 | 775 | 25 | 20 | 0 | 45 | 0 |
| TVi8z3unRlM | 18 | 13 | 13 | 13 | 13 | 0 |
| OEbAeVn6DHg | 1.8K | 20 | 20 | 3 | 37 | 0 |
| ooWoKmqrooU | 842 | 20 | 19 | 0 | 39 | 1 |
| zfrqkteUPAI | 204 | 19 | 20 | 4 | 35 | 1 |
| WXJGaGtXrgY | 416 | 20 | 20 | 3 | 37 | 0 |
| 1kWd9HidNJk | 160 | 20 | 20 | 3 | 37 | 0 |
| **Total** | | **182** | **178** | **68** | **292** | **2** |

Spam skipped:
- zfrqkteUPAI: a top comment (100 likes) that works in a national service company's name without discussing the video's method. Treated as a promotional plant.
- ooWoKmqrooU: a newest comment from another creator promoting their own faceless channel.

**Shortfall against the ~50 top / ~25 newest target.** Continuation tokens did not page forward. Each follow-up call returned the same first page, or the same page with 1–4 new items:
- RGH2k2G8oaQ: top page 2 and newest page 2 were identical to page 1.
- OEbAeVn6DHg: top page 2 and newest page 2 were identical to page 1.
- f8-sd5Zw0E4: top pages 2 and 3 added 1 and 4 new comments; newest page 2 was identical to page 1.

After those tries I stopped paging. The other large videos have one top call and one newest call each (about 20 + 20). The five small videos (13–23 top-level comments) are complete.

## API oddities and notes

- **Approximate list dates.** `youtube_channel_videos` gives rounded dates (for example, every "3 months ago" video is listed as 2026-07-20). Exact dates come from `youtube_video_details`. On the popular list, "N years ago" behaves as a floor: every "2 years ago" video checked was before 2024-10-20.
- **Upload gap.** The Videos tab shows no upload between 2026-07-09 and 2026-10-12. The newest-page order matched the exact dates throughout.
- **Inconsistent video counts.** The `meta.videosCount` on list pages varies ("31", then "0", then "31"), while the about page reports 2,302 videos.
- **Durations.** List durations are 1 s longer than details for two videos (RGH2k2G8oaQ 16:55 vs 1014 s; f8-sd5Zw0E4 13:05 vs 784 s). Meta files use the details value.
- **Truncated title.** Wav7A7YhduY's title comes back cut off ("…it's ONE word buried in") in both list and details. It is recorded as returned.
- **zfrqkteUPAI looks older than its date.** It has an exact publish date of 2026-03-30, but the description carries an older link block (Trade Talks channel, subreddit, Trades Academy mini-course) and the sign-off "LEED AP, the expert plumber", unlike the other 2026 uploads. Recorded only; it was not checked further.
- **Transcript quirks.** ooWoKmqrooU's transcript is unpunctuated auto-caption style. OEbAeVn6DHg's transcript interleaves Roger and the other creator's clip audio with no speaker labels.
- **Approximate comment dates.** Comment publish dates from the API are approximate (relative). They are not used.

## Files written

- `data/competitors/roger-wakefield/<id>/meta.md`, `transcript.txt`, `comments.md` for the 10 videos.
- `notes/competitors/roger-wakefield__<id>.md` for the 10 videos.
- This log.

No other files were touched, and nothing was committed.
