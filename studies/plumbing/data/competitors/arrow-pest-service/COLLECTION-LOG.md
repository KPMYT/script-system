# Collection log — Arrow Pest Service (competitor, parallel niche)

Collected 2026-10-20 by a helper session. Method: `studies/plumbing/study-brief.md`. Collect and describe only.

## Channel

- Name: Arrow Pest Service · handle @ArrowPestService
- Channel ID: UCsTn0U92ikWtriwoGLjWEAw
- Niche: pest control (parallel niche; included "to understand", per the operator)
- youtube_channel_about: 315K subscribers, "220 videos", 44,654,774 total views, joined 2015-04-14, country United States. Links: arrowps.com and an Amazon storefront ("Shop My Pest Control Products"). The about text describes the business as blending pest control with "real estate insights".
- Category on every collected video: Howto & Style. Uploads in the newest list come every week, usually on a Friday at 15:00 -07:00.

## Method (NexLev MCP only)

1. `youtube_channel_videos` sort=newest, page 1 (30 items, list dates 2026-10-10 back to 2025-12-20), and sort=popular, page 1 (30 items). No more pages were needed: Group A and all 15 normal-window videos are on newest page 1, and popular ranks 1–5 all fall inside the 24-month window. List dates are approximate (most show the 20th of a month), so every candidate was checked with `youtube_video_details`.
2. `youtube_video_details` for 22 videos: the 17 most recent long-form uploads in list order (to order the window exactly) plus the Group B candidates. All dates, views, likes and durations below come from these calls.
3. `check_faceless_channel` (cached result, 2026-10-20T07:53Z) and `youtube_channel_about`.
4. `get_bulk_video_transcripts`: two calls (1 + 9 videos). All 10 succeeded.
5. `youtube_video_comments`: sort=top and sort=newest, 34 calls in total (see the pagination note below). Comment pages were turned into `comments.md` by a script that read the NexLev JSON responses, so nothing was retyped by hand.

## Group A — 5 most recent long-form uploads

| # | Video ID | Title | Upload date | Duration | Views | Views / normal |
|---|---|---|---|---|---|---|
| 1 | Sg17BA6M3EI | Homemade Stink Bug Trap That Actually Works! | 2026-10-09 | 16:35 | 449072 | 1.66 |
| 2 | zuiwdNiVylQ | I Tested 6 Household Pest Killers! | 2026-10-02 | 1:55:07 | 28405 | 0.10 |
| 3 | cMhqzhuIH2g | Why Your Lawn Is Full Of Weeds (And How To Fix It) | 2026-09-25 | 15:27 | 29212 | 0.11 |
| 4 | ZBfgXMnhK_g | 5,000 Yellow Jackets vs WD 40! | 2026-09-18 | 22:15 | 270890 | 1.00 |
| 5 | 4pG5LWiwfaU | Get Rid of Spiders! (Easy DIY) | 2026-09-11 | 16:02 | 444754 | 1.64 |

zuiwdNiVylQ is a 1:55:07 compilation of six earlier jobs (isLiveContent=false). It meets the long-form rule (3:00 or longer, not a Short), so it was kept. Three of its segments use the same footage as the Group B videos 2XTSgRtcwh0, Wg9-yFIXlx0 and DgMVZB814YI.

## Group B — 5 most-viewed long-form uploads published on or after 2024-10-20

| Popular rank | Video ID | Title | Upload date | Duration | Views | Views / normal |
|---|---|---|---|---|---|---|
| 1 | 2XTSgRtcwh0 | KILL ALL Yellowjackets And Wasps For 1/2 Mile. Safe For Honey Bees! | 2025-10-17 | 16:53 | 6822568 | 25.19 |
| 2 | Wg9-yFIXlx0 | KILL ALL Rats And Mice Around Your Home. Safe For Pets! | 2025-10-31 | 20:13 | 4674195 | 17.25 |
| 3 | DgMVZB814YI | ROACHES EVERYWHERE-Simple Hack Kills Them All! | 2025-11-21 | 22:36 | 2595835 | 9.58 |
| 4 | d3QKP9kRwd8 | Homemade Bed Bug Trap That Actually Works! | 2025-12-30 | 16:22 | 2357474 | 8.70 |
| 5 | FaKOqJcsg4A | KILL EVERY Mosquito. SAFE For Honey Bees & Pets! | 2026-05-08 | 20:58 | 2330282 | 8.60 |

Next in popular order, not needed: symDHme88ks (rank 6, about 2.0M, list date "1 year ago"). The highest-ranked Group A video in the popular list is O_0ZCwXjKEM at rank 7, but it is not in Group A, so no Group B pick had to be skipped.

## Skipped videos and why

- None skipped for missing transcripts (all 10 had transcripts).
- No Group A / Group B overlap, so no Group B substitutions.
- KdzNk3jM6kw "Exterminator Panama City, FL" (0:28, list date 2023-10-20) appears at popular rank 21. Excluded: under 3:00 and outside the window.

## Normal (median of exact views, 15 most recent long-form uploads at least 7 days old on 2026-10-20)

Window: uploads on or before 2026-10-13. In date order:

| Video ID | Upload date | Views |
|---|---|---|
| Sg17BA6M3EI | 2026-10-09 | 449072 |
| zuiwdNiVylQ | 2026-10-02 | 28405 |
| cMhqzhuIH2g | 2026-09-25 | 29212 |
| ZBfgXMnhK_g | 2026-09-18 | 270890 |
| 4pG5LWiwfaU | 2026-09-11 | 444754 |
| MONzpDX9a7c | 2026-09-04 | 371545 |
| mTsrR72bTT8 | 2026-08-21 | 175176 |
| O_0ZCwXjKEM | 2026-08-14 | 1940264 |
| XXizhg1_cRU | 2026-08-07 | 881444 |
| jI_pO4I3xYk | 2026-07-31 | 183863 |
| kVUqvi-U4qI | 2026-07-24 | 234167 |
| pTWEdIzC8D4 | 2026-07-17 | 1568478 |
| 8fQrHjY6L4I | 2026-07-05 | 33449 |
| 0NfaPV6WxzA | 2026-06-26 | 767854 |
| e9ubjAwwahI | 2026-06-19 | 118645 |

Sorted: 28405, 29212, 33449, 118645, 175176, 183863, 234167, **270890**, 371545, 444754, 449072, 767854, 881444, 1568478, 1940264.
**Normal = 270890** (8th of 15, ZBfgXMnhK_g).

The next upload down, ESSKMhEWP14 (2026-06-09, 57164 views), was checked to confirm the order. The newest list shows no upload on 2026-08-28 or 2026-07-10, so the weekly rhythm has gaps there. This is recorded as listed, not investigated further.

## Format

FACE. Basis:
- check_faceless_channel: isFaceless=false, confidence 0.95, format "tutorial", primary category "do it yourself".
- About text: a named pest control business (Arrow Pest Service, arrowps.com).
- Transcripts: on-site dialogue between the owner, Mack (nicknamed "Honey Bear"), and his daughter McKenzie ("Cornbread"), filming real customer jobs and home demonstrations.
- Comments react to the two on camera (e.g. "That blue eyed baby girl looks just like you dad"; "camo looks best on these 2").

## Transcripts

All are NexLev, English (auto-generated). youtube_video_details reports hasCaption=false for every video, but NexLev still returned auto-generated transcripts. Segments overlap in time (startMs/endMs); timestamps use startMs. For zuiwdNiVylQ, which runs past an hour, timestamps keep the [m:ss] form with minutes above 59 (e.g. [115:01]).

| Video ID | Segments | Words | Last timestamp |
|---|---|---|---|
| Sg17BA6M3EI | 480 | 3144 | 16:29 |
| zuiwdNiVylQ | 2932 | 18838 | 115:01 |
| cMhqzhuIH2g | 448 | 2967 | 15:20 |
| ZBfgXMnhK_g | 634 | 3575 | 22:06 |
| 4pG5LWiwfaU | 470 | 3070 | 15:56 |
| 2XTSgRtcwh0 | 445 | 2882 | 16:50 |
| Wg9-yFIXlx0 | 517 | 3311 | 20:11 |
| DgMVZB814YI | 484 | 2907 | 22:35 |
| d3QKP9kRwd8 | 438 | 2908 | 16:19 |
| FaKOqJcsg4A | 604 | 4116 | 20:51 |

## Comments

| Video ID | Top | Newest | In both | Unique | Spam skipped | API commentsCount |
|---|---|---|---|---|---|---|
| Sg17BA6M3EI | 20 | 20 | 2 | 38 | 0 | 332 |
| zuiwdNiVylQ | 24 | 20 | 6 | 38 | 0 | 154 |
| cMhqzhuIH2g | 20 | 20 | 3 | 37 | 0 | 158 |
| ZBfgXMnhK_g | 26 | 20 | 4 | 42 | 0 | 471 |
| 4pG5LWiwfaU | 22 | 20 | 2 | 40 | 0 | 540 |
| 2XTSgRtcwh0 | 29 | 20 | 1 | 48 | 0 | 9.9K |
| Wg9-yFIXlx0 | 20 | 20 | 1 | 39 | 0 | 9.6K |
| DgMVZB814YI | 22 | 20 | 2 | 40 | 0 | 9.3K |
| d3QKP9kRwd8 | 20 | 20 | 2 | 38 | 0 | 2.4K |
| FaKOqJcsg4A | 20 | 20 | 1 | 39 | 0 | 2.9K |
| **Total** | **223** | **200** | **24** | **399** | **0** | |

- Top-level comments only, text and like counts only. Any @handle inside comment text was replaced with "@[handle removed]". The channel's own comments (pinned product links, one note) are kept and tagged "[channel owner]". Blank like counts are recorded as 0. Counts of 1,000 or more are kept as the API's abbreviations (e.g. "3.9K").
- Spam rule: links or crypto/messaging promotion from non-owner accounts. None found. Hostile, political and off-topic comments were kept as data.
- Check before finishing: none of the collected author handles appears in any comments.md (scripted check), and every "@" in the files is either "@[handle removed]" or a timestamp like "@ 7:49".

## Failures and API oddities

- **Comment pagination does not advance.** Continuation tokens from youtube_video_comments returned page 1 again, for both sorts:
  - sort=top page 2 was identical to page 1 for Sg17BA6M3EI, cMhqzhuIH2g, d3QKP9kRwd8 and FaKOqJcsg4A. For the others it overlapped heavily, adding 0–9 new comments.
  - A third top page was tried for 2XTSgRtcwh0 and came back identical to page 2.
  - sort=newest page 2 was identical to page 1 for Sg17BA6M3EI and zuiwdNiVylQ, so newest paging stopped there.
  - Result: about 20–29 top and 20 newest comments per video, not the brief's ~50 + ~25. No other method was used.
- youtube_video_details returns about 250 country codes per call (very large responses). No effect on the data.
- get_bulk_video_transcripts results were too large to show inline and were saved by the client to tool-result files, then converted by script.
- Popular-list view counts are rounded (e.g. "2.3M" for both d3QKP9kRwd8 and FaKOqJcsg4A). Exact counts from details confirm the order: 2357474 > 2330282.
- Notes files run about 410–465 words by `wc -w`, counting headings, timestamps and the Basics block. That is above the brief's 250–350 target and below the woodworking template notes this was modelled on (about 470–500).

## Files

- `data/competitors/arrow-pest-service/<video-id>/` — meta.md, transcript.txt, comments.md (10 folders)
- `notes/competitors/arrow-pest-service__<video-id>.md` (10 files)
- Scratch (not part of the study): /tmp/claude-0/-home-user-script-system/c72a3e80-0208-5a73-aa3c-d8cb68cb0601/scratchpad/arrow-pest-service/
