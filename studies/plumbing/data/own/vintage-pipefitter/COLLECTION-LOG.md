# Collection log — The Vintage Pipefitter (own)

Collected 2026-10-20 by a helper agent following `studies/plumbing/study-brief.md`. NexLev MCP tools only.

## Channel

- Channel ID: UCyImxEdbXY3x0w51WQtOG9Q (handle @Thevintagepipefitter)
- About (youtube_channel_about): 10.1K subscribers; 1,655,698 total views; joined 2008-07-10; country United States; link "101 Ways to Unclog Any Drain" (vintagepipefitter.com). Description: "the most valuable plumbing knowledge in America is sitting in old trade manuals, forgotten patents, and the memories of men who've been dead for fifty years… Get the Ebook here".
- The popular-sorted list also contains two non-plumbing uploads from 2011 ("12 gauge Bolt Action shotgun.", 2:18, 96,034 views; "L4d2 poster easter eggs", 1:00). The channel predates the plumbing uploads; recorded as found.

## Method

1. `youtube_channel_videos` sort=newest (page 1, 30 items, back to 2026-09-20) and sort=popular (page 1, 30 items). Page 1 of each was enough: Group A, Group B and the normal window all fall inside it. Continuation tokens were not needed for the video lists.
2. `youtube_video_details` for the 10 selected videos, for every video in the normal window, for the window boundary (xOLfkfnOZho) and for the skipped popular rank 4 (0L4OqBg_mTU). Exact dates, views, likes and durations below come from these calls. List dates are approximate and were not used.
3. `check_faceless_channel` and `youtube_channel_about` for the format basis.
4. `get_bulk_video_transcripts` for all 10 in one call: 10/10 succeeded, all "English (auto-generated)". The result was too large for the tool window and was saved to a local file by the harness; transcript.txt files were written from that file with a script (start time from startMs, `[m:ss] text`, one line per segment, no edits to text beyond HTML-entity decoding).
5. `youtube_video_comments` sort=top and sort=newest for each video (see oddities: pagination). Usernames, handles and channel IDs were dropped; text and like counts only.
6. meta.md built from the details calls; notes written from the transcripts and comments.

## Group A — 5 most recent long-form uploads

| # | Video ID | Title | Upload (PDT) | Duration | Views | Views / normal |
|---|---|---|---|---|---|---|
| 1 | 7oem6cSCg-g | Your Toilet DOESN'T Need Bleach — 9 Things You Didn't Know About Toilets | 2026-10-17 11:30 | 16:12 | 251 | 0.41 |
| 2 | WxRQIn76yRo | Why Plumbers' Showers Never Run Cold — The 1 Valve They Add to Every Water Heater | 2026-10-17 03:17 | 15:52 | 372 | 0.61 |
| 3 | bSrEWmK0g5E | Explode 20 Years of Grease by Unclogging This Kitchen Drain | 2026-10-15 10:26 | 16:57 | 327 | 0.54 |
| 4 | dIe837GgLDs | Bleach vs Vinegar vs CLR vs Pumice Stone — A 45-Year Plumber Ranks All 4 for Toilet Rings | 2026-10-14 09:47 | 15:06 | 1016 | 1.67 |
| 5 | AiUUNM24kCo | Pour This Down Every Drain to Unclog Them While You Sleep | 2026-10-12 12:25 | 16:29 | 603 | 0.99 |

Group A #1–#4 were 3–6 days old at collection, younger than the 7-day floor used for the normal; their ratios are recorded but are not on the same footing as the window.

## Group B — 5 most-viewed long-form uploads published on/after 2024-10-20

| Popular rank | Video ID | Title | Upload (PDT) | Duration | Views | Views / normal |
|---|---|---|---|---|---|---|
| 1 | rGEFZrtOJOI | 9 Things Plumbers Don't Want You to Know About Hydrogen Peroxide and Your Drains | 2026-07-15 11:00 | 19:52 | 753316 | 1236.97 |
| 2 | uWXIUmWdPeY | Half a Cup of This Dissolves Years of Limescale Overnight — And It's NOT Vinegar | 2026-08-20 11:00 | 21:52 | 240315 | 394.61 |
| 3 | hOz49worQJg | 1 Cup of This Removes Every Toilet Bowl Ring Forever — And It's NOT Bleach | 2026-07-31 12:09 | 21:27 | 167260 | 274.65 |
| 5 | rDLzNLUZnhw | 1 Cup of This Dissolves ANY Drain Clog Overnight — Without Touching Your Pipes | 2026-07-29 11:38 | 22:01 | 51304 | 84.24 |
| 6 | 9_11vx_L6oM | DO NOT Install a Toilet Until You Watch This - 12 Mistakes That Guarantee a Leak | 2026-05-24 12:00 | 14:25 | 37217 | 61.11 |

No Group A video appeared in the popular top 6, so no Group B overlap skip was needed.

## Skipped videos and why

- 0L4OqBg_mTU (popular rank 4, "12 gauge Bolt Action shotgun.") — 2:17 by details (137 s), under 3:00, and published 2011-10-30, before the 24-month window. Not long-form; skipped, next one down taken.
- Oj8TuPz5g4c (popular rank 7, 1:00, 2011) — not reached; would also fail both tests.
- No video was skipped for a missing transcript.

## Normal

Median of exact views of the 15 most recent long-form uploads at least 7 days old as of 2026-10-20 (published on or before 2026-10-13). AiUUNM24kCo (2026-10-12 12:25 PDT) is the newest qualifying upload; the four newer ones are under 7 days old. Window, newest first (views from youtube_video_details, 2026-10-20):

| # | Video ID | Upload (PDT) | Views |
|---|---|---|---|
| 1 | AiUUNM24kCo | 2026-10-12 | 603 |
| 2 | Lb92wK35RiQ | 2026-10-11 | 876 |
| 3 | spYPVQxsMvc | 2026-10-10 | 1716 |
| 4 | zOaTwlXVE1U | 2026-10-08 | 519 |
| 5 | awCEiez-RN8 | 2026-10-07 | 277 |
| 6 | 9VfMsV8D2ng | 2026-10-06 | 767 |
| 7 | eVwz-PZ0SCs | 2026-10-05 | 302 |
| 8 | DG91p8vsUXA | 2026-10-04 | 1062 |
| 9 | I9dh2vBWJRY | 2026-09-28 | 429 |
| 10 | 2zVCuhQ6oFs | 2026-09-27 | 1524 |
| 11 | za0w77vagiE | 2026-09-26 | 609 |
| 12 | Q0PCzGlcNP4 | 2026-09-25 | 621 |
| 13 | 9IKZ_OXoPHE | 2026-09-24 | 2001 |
| 14 | xBVJIJYVaDs | 2026-09-23 | 492 |
| 15 | qaTMdy0q1no | 2026-09-22 | 355 |

Sorted: 277, 302, 355, 429, 492, 519, 603, **609**, 621, 767, 876, 1062, 1524, 1716, 2001. **Normal = 609.** Boundary check: the 16th upload, xOLfkfnOZho, is dated 2026-09-21 (656 views), so it is outside the window. All 15 are long-form (13:13 to 25:22 on the list; none are Shorts).

## Format basis

**FACELESS.** Evidence: `check_faceless_channel` isFaceless=true, confidence 0.98, primary category "do it yourself", format "tutorial" (cached 2026-10-20); the about text describes a research/lost-knowledge channel with an e-book and names no presenter; all 10 transcripts are first-person voiceover addressed to the viewer, with no reference to a presenter on screen (references are to a QR code or "the pattern on your screen"); 4 of the 5 Group B descriptions end with a "Credits to" list of other YouTube channels and brands (compiled third-party footage); comments on Group B videos refer to an "ai voice", to "the narration", to images "copied … from other sources" and to visuals "made with AI". The narrator presents as a veteran plumber ("30 years", Uncle Ray) while several titles say "45 years"; recorded as found.

## Comment totals

| Video ID | API commentsCount | Top collected | Newest collected | Unique | Spam/off-topic skipped |
|---|---|---|---|---|---|
| 7oem6cSCg-g | 0 | 0 | 0 | 0 | 0 |
| WxRQIn76yRo | 0 | 0 | 0 | 0 | 0 |
| bSrEWmK0g5E | 0 | 0 | 0 | 0 | 0 |
| dIe837GgLDs | 0 | 0 | 0 | 0 | 0 |
| AiUUNM24kCo | 1 | 1 | 1 | 1 | 0 |
| rGEFZrtOJOI | 94 | 20 | 19 | 32 | 1 (off-topic political rant) |
| uWXIUmWdPeY | 54 | 19 | 20 | 25 | 1 (book promotion) |
| hOz49worQJg | 127 | 20 | 20 | 33 | 0 |
| rDLzNLUZnhw | 23 | 11 | 11 | 11 | 2 (book promotion; off-topic rant) |
| 9_11vx_L6oM | 16 | 12 | 13 | 13 | 0 |

Total unique comments kept: 115. The ~50 top + ~25 newest targets could not be met (see pagination below, and the recent uploads have 0–1 comments). The brief-wide "skip obvious spam" rule was applied to two copies of the same book-promotion pattern and to two rants unrelated to the video. Checked after writing: no comments.md contains usernames or @handles (the only "@" is a viewer's timestamp "@11:50").

## Failures and API oddities

- **Comment pagination does not advance.** For rGEFZrtOJOI, passing the continuation token for sort=top returned the identical first 20 comments twice (two attempts), and sort=newest page 2 returned the identical first 20 again. Each sort order therefore yields at most 20 comments per video. Not retried further on the other videos; page 1 only was used for all.
- API commentsCount is higher than what the endpoint returns when there is no continuation (rDLzNLUZnhw 23 vs 13; 9_11vx_L6oM 16 vs 13); the count probably includes replies.
- Blank like counts come back as a single space (" "); recorded as 0.
- Comment publishDate values are computed from relative text ("2 months ago") at fetch time, not real timestamps; not used.
- List dates and views are approximate: the newest list showed 2026-09-29 for uploads that are actually 2026-09-22 to 2026-09-28, and 2026-07-20 for rGEFZrtOJOI (actual 2026-07-15); list views differ slightly from details (WxRQIn76yRo 366 vs 372).
- Channel video counts disagree: list meta says 31 videos (newest sort) or 0 (popular sort); about says 605.
- Every plumbing upload checked reports category "Music" and hasCaption=false, yet auto-generated transcripts were available for all 10.
- Bulk transcript output (861,910 characters) exceeded the tool window and was saved to a local file, which was then parsed; no transcript text was lost.
- Spoken script labels appear in two transcripts: "And subscribe CTA." at [18:43] in hOz49worQJg and "Mid-roll subscribe CTA." at [8:54] in rDLzNLUZnhw ("Bonus tip stinger" at [20:58] in uWXIUmWdPeY). hOz49worQJg also says "the Vintage Plumber" at [18:53]. bSrEWmK0g5E's tool list starts mid-sentence at [4:54]. Recorded as found.
