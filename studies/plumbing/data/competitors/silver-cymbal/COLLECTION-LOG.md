# Collection log — Silver Cymbal (competitor)

Collected 2026-10-20 by a helper agent following `studies/plumbing/study-brief.md`. Describe-only; no judgements.

## Channel

- Name: Silver Cymbal
- Channel ID: UC67dKTEwpAhKv2oYDATwR8g
- Handle: @SilverCymbal
- About (youtube_channel_about): 1.09M subscribers, 539 videos, 465,370,479 views, joined 2012-06-27, United States. Description: "Do more yourself - Do it Yourself / Home Improvement - Plumbing / Heating / Generators / Landscaping & Gardening - Lawn Care / Everything you see is how I take care of my home and I hope that you can use some of my videos to help you do more yourself at your home."
- Topic spread of the 10 selected videos (descriptive): plumbing 1 (compression fittings, YRow6eS6AHw); sealing pipe and wire penetrations 1 (sHL4lBAhklA); battery power stations 2; generator/panel 1; LED bulbs 1; lawn care 2; air duster/blower 1; car windshield cleaning 1.

## Format: FACE

Basis:
- NexLev `check_faceless_channel` (regular videos, cached 2026-10-20): isFaceless=false, confidence 0.97, primary category "do it yourself", format "reviews", tags do it yourself / tech gadgets / home improvement / autos.
- About text: "Everything you see is how I take care of my home".
- Transcripts: first-person presenter who introduces himself on camera ("Hey guys, I'm Chris from the Silver Cymbal channel", XJdrUmHkjIs [0:00], fseq9NvO_zw [0:00], VW_bhZt3IpM [0:04], K8F2R1gDSkg [0:05]) and films his own installs and live tests (e.g. live reactions in W-iM-xNJj9E, on-camera removal of a 4-year-old seal in sHL4lBAhklA).
- Comments refer to his on-camera appearance ("That camera quality is insane. I can see his pores." and weight-loss remarks on K8F2R1gDSkg and VW_bhZt3IpM; "You got some infant hands on that bad boy" on W-iM-xNJj9E).

## Method (NexLev MCP tools only)

1. `youtube_channel_about`, `check_faceless_channel`.
2. `youtube_channel_videos` sort=newest, pages 1–3 (90 uploads, back to items labelled "2 years ago"); sort=popular, pages 1–4 (ranks 1–120).
3. `youtube_video_details` for every Group A/B candidate, every popular-list candidate labelled "2 years ago" or newer, and all 15 normal-window videos plus the 16th (exact dates, views, likes, durations).
4. `get_bulk_video_transcripts` in two calls of 5 IDs (all 10 succeeded). Outputs were saved by the tool to local JSON files and converted with a script to `[m:ss] text`, one line per segment, start times taken from `startMs`.
5. `youtube_video_comments` sort=top and sort=newest, one page each per video (see API oddities). Comment text and like counts copied into scratch lists and assembled into `comments.md` by script; usernames never copied; @handles inside comment text replaced with "@[handle removed]".
6. Long-form = 3:00 or longer and not a Short. All candidates were checked: every selected video is ≥ 3:25 and has `isShortsEligible=false`.

## Group A — 5 most recent long-form uploads

| # | Video ID | Title | Published | Views | Views / normal |
|---|---|---|---|---|---|
| 1 | XJdrUmHkjIs | EcoFlow Just Made Whole House Backup WAY More Affordable! ALL NEW TITAN | 2026-10-13 | 72,567 | 1.02 |
| 2 | K8F2R1gDSkg | Hands On with the MOST Powerful Portable Solar Generator Anker Has Made - S5000 | 2026-10-09 | 45,438 | 0.64 |
| 3 | W-iM-xNJj9E | Not Sure You Can Still Call this an Air Duster - BIG Wolfbox First Look | 2026-10-07 | 56,870 | 0.80 |
| 4 | VW_bhZt3IpM | Lawn Care is Expensive. Try THIS Instead! | 2026-09-13 | 329,878 | 4.65 |
| 5 | sHL4lBAhklA | Spray Foam is Expensive. Use THIS Instead! | 2026-08-30 | 1,512,707 | 21.31 |

Next most recent (not used): crWFk9Da9_4 (2026-08-20).

## Group B — 5 most-viewed long-form uploads published on/after 2024-10-20

"Popular rank" = position in NexLev `youtube_channel_videos` sort=popular (all upload dates, 30 per page; ties in rounded view counts keep the API's order).

| # | Video ID | Title | Published | Views | Popular rank | Views / normal |
|---|---|---|---|---|---|---|
| 1 | fseq9NvO_zw | A Ridiculously Easy Way to Clean the INSIDE of Your Windshield (NO Haze or Streaks) | 2025-11-23 | 10,723,985 | 5 | 151.07 |
| 2 | cfGgCbQAjwM | 4 String Trimmer Hacks You’ll Wish You Knew Sooner - Clean Edges | 2025-05-21 | 1,790,187 | 60 | 25.22 |
| 3 | sX442FodiT4 | Homeowners are Destroying Generators Skipping 1 Step During a Power Outage | 2025-01-28 | 1,689,323 | 63 | 23.80 |
| 4 | dVjg_BK3G3s | Sneaky Reason LED Bulbs are Dying Faster than Advertised | 2024-11-11 | 1,332,137 | 84 | 18.77 |
| 5 | YRow6eS6AHw | Move Over Sharkbites...Solder-Free Plumbing just got Easier with Compression Valves | 2025-10-12 | 1,065,097 | 110 | 15.00 |

## Skipped videos and why

- sHL4lBAhklA (popular rank 73, 1,512,707 views, 2026-08-30): already in Group A; Group B took the next eligible video down.
- Popular-list videos labelled "2 years ago" that `youtube_video_details` dated before 2024-10-20 (outside the 24-month window):
  - EkuLHpYz02Y, rank 10, 2024-05-12, 8,030,497 views
  - U9ZQ96hbmIY, rank 24, 2024-03-09, 4,294,515
  - gzC7IpqKo2M, rank 25, 2024-06-23, 4,035,803
  - uToDTP99WEo, rank 36, 2023-10-31, 2,888,699
  - PZFJkXfThUg, rank 40, 2024-03-31, 2,714,327
  - 9d9TL02idO4, rank 79, 2023-11-26, 1,392,228
  - Tdn_IAm1e0g, rank 86, 2023-12-13, 1,315,576
  - pPMm0reEBPM, rank 96, 2023-12-21, 1,200,175
  - P6lwyRmOk30, rank 98, 2024-05-26, 1,176,462
- All other videos in popular ranks 1–109 carry list labels of "3 years ago" or older.
- No video was skipped for a missing transcript.

## Normal

Median of exact views of the 15 most recent long-form uploads at least 7 days old (as of 2026-10-20): **70,989** (rIMsBWXS7UE).

| # | Video ID | Published | Duration | Views |
|---|---|---|---|---|
| 1 | XJdrUmHkjIs | 2026-10-13 | 9:32 | 72,567 |
| 2 | K8F2R1gDSkg | 2026-10-09 | 7:11 | 45,438 |
| 3 | W-iM-xNJj9E | 2026-10-07 | 5:29 | 56,870 |
| 4 | VW_bhZt3IpM | 2026-09-13 | 5:24 | 329,878 |
| 5 | sHL4lBAhklA | 2026-08-30 | 5:33 | 1,512,707 |
| 6 | crWFk9Da9_4 | 2026-08-20 | 4:56 | 27,934 |
| 7 | p6zvBXU8V0M | 2026-08-18 | 4:47 | 19,389 |
| 8 | zMSWKLvDFTc | 2026-08-16 | 12:28 | 232,606 |
| 9 | OGVXmIZtEG8 | 2026-08-06 | 5:39 | 64,786 |
| 10 | VuQwtq7v0pk | 2026-08-03 | 11:01 | 78,033 |
| 11 | geHew6AY57Q | 2026-07-12 | 4:57 | 67,247 |
| 12 | hd6tJMsJ1ac | 2026-06-24 | 6:15 | 46,655 |
| 13 | ggxTdCjKBjI | 2026-06-15 | 10:52 | 106,472 |
| 14 | rIMsBWXS7UE | 2026-05-31 | 5:04 | 70,989 |
| 15 | iyQk6K8ABlw | 2026-05-26 | 6:26 | 80,561 |

Sorted: 19,389 · 27,934 · 45,438 · 46,655 · 56,870 · 64,786 · 67,247 · **70,989** · 72,567 · 78,033 · 80,561 · 106,472 · 232,606 · 329,878 · 1,512,707.

Boundary note: XJdrUmHkjIs was published 2026-10-13 07:43 -07:00, exactly 7 days before the collection date, and is counted as "at least 7 days old". If it were left out, the 16th upload, e2vsJxyGJtQ (2026-05-24, 637,498 views), would enter the window; the median would still be 70,989.

## Transcripts

All 10 from `get_bulk_video_transcripts` (2 calls, 10/10 successful). Segment counts: XJdrUmHkjIs 279, K8F2R1gDSkg 187, W-iM-xNJj9E 111, VW_bhZt3IpM 173, sHL4lBAhklA 178, fseq9NvO_zw 128, cfGgCbQAjwM 102, sX442FodiT4 131, dVjg_BK3G3s 107, YRow6eS6AHw 223.

## Comment totals

- Top: 199 kept (20 per video, 19 on XJdrUmHkjIs after spam). Newest: 198 kept (20 per video, 19 on XJdrUmHkjIs and cfGgCbQAjwM after spam).
- Unique after de-duplicating top/newest overlap: 369 (XJdrUmHkjIs 36, K8F2R1gDSkg 31, W-iM-xNJj9E 35, VW_bhZt3IpM 37, sHL4lBAhklA 39, fseq9NvO_zw 39, cfGgCbQAjwM 35, sX442FodiT4 39, dVjg_BK3G3s 39, YRow6eS6AHw 39). Comments in both lists are marked "[also in top]".
- Spam skipped: 2 (XJdrUmHkjIs: generic praise from a promotional channel account; cfGgCbQAjwM: off-topic, bot-like prayer comment).
- The channel owner's pinned comment (affiliate or offer links) is kept on 9 of 10 videos and marked "(channel owner)"; VW_bhZt3IpM had none in either list.
- Handles redacted inside comment text: 1 comment (on K8F2R1gDSkg, appearing in both lists).
- Username/handle check: run on all 10 `comments.md` files before finishing; no usernames or @handles remain.
- API commentsCount per video: XJdrUmHkjIs 137, K8F2R1gDSkg 74, W-iM-xNJj9E 107, VW_bhZt3IpM 200, sHL4lBAhklA 791, fseq9NvO_zw 8.2K, cfGgCbQAjwM 573, sX442FodiT4 1K, dVjg_BK3G3s 4.2K, YRow6eS6AHw 1.2K.

## Failures and API oddities

- **Comment pagination did not advance.** For `youtube_video_comments`, passing the returned continuation token gave back the same first 20 comments, for both sort=top and sort=newest (tested 3 times on YRow6eS6AHw and once on dVjg_BK3G3s). So each list holds at most 20 comments instead of the brief's ~50 top + ~25 newest. No other comment method was used.
- In sort=newest, the pinned owner comment is always returned first, whatever its date.
- Comment like counts of 1,000+ come rounded ("1.1K", "2.9K"); recorded as given. Blank like counts (" ") recorded as 0.
- `youtube_channel_videos` list dates are placeholders on the 20th of a month ("1 month ago" → 2026-09-20, etc.); exact dates came from `youtube_video_details`. Relative labels can be loose (uToDTP99WEo listed "2 years ago", published 2023-10-31).
- `youtube_channel_videos` meta reports videosCount 31 or 0 per page, while `youtube_channel_about` reports 539 videos.
- `youtube_video_details` returns `hasCaption: false` for every video checked, yet transcripts were returned for all 10.
- Captions spell the channel name "Silver Symbol" in most videos.
- Bulk transcript outputs exceeded the tool's inline size limit and were saved by the tool to local files, then read by script; no content was lost (all segments converted).
