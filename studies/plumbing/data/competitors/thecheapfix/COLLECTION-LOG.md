# Collection log — TheCheapFix (competitor)

Collected 2026-10-20 by a helper agent following `studies/plumbing/study-brief.md`. NexLev MCP tools only.

## Channel

- Channel ID: UC7xrSTuKm8YPd2l6WPgMt-g · handle @TheCheapFix · https://www.youtube.com/channel/UC7xrSTuKm8YPd2l6WPgMt-g
- Operator note: AI channel
- `youtube_channel_about`: 65.3K subscribers; "75 videos"; 10,474,220 total views; joined 2007-11-23; country blank; description blank; one link, "SECRET EBOOKS BELOW👇" → thecheapfix.netlify.app.
- `check_faceless_channel` (cached 2026-10-20): isFaceless=true, confidence 0.98, format "tutorial", tags "do it yourself, crafts, home, life stories", Google Trends keyword "hydrogen peroxide hacks".
- Every upload seen in either listing is a "Hydrogen peroxide" (one "White vinegar") list video of 11–23 minutes. Topics range well beyond plumbing: cars, pets, HVAC, gardening, beauty and dental.

## Method

1. `youtube_channel_videos` sorted newest (page 1, 30 videos) and sorted popular (page 1, 30 videos). Every listed item was ≥3:00 and none was a Short (shortest 11:45). Group A, Group B and the 15-video normal window all fall within page 1 of each sort, so no continuation pages were needed.
2. `youtube_video_details` was called for all 10 selected videos, the 15 window videos and the 16th (outside-window) video, to confirm exact dates, views, likes and durations.
3. `get_bulk_video_transcripts`: one call for cljD9InmFzk, then one call for the other 9. All 10 succeeded, each on an English auto-generated track. Written as `[m:ss] text`, one line per segment.
4. `youtube_video_comments`, sorted top and sorted newest, for each video (top-level only, text and likes only).
5. Notes written from the transcripts and comments, one file per video in `notes/competitors/thecheapfix__<id>.md`.

## Group A — 5 most recent long-form

| # | Video ID | Title | Upload (exact) | Views | Views/normal |
|---|---|---|---|---|---|
| 1 | cljD9InmFzk | Pour Hydrogen Peroxide Down Your Drains Tonight & Watch What Happens! | 2026-10-19 09:00 -07:00 | 448 | 0.06 |
| 2 | TOurn07rVVQ | Pour Hydrogen Peroxide Down Your Garbage Disposal Tonight & Watch What Happens #1 Kills Rotten Smell | 2026-10-18 07:22 -07:00 | 853 | 0.11 |
| 3 | uJVc7zmq7vs | Pour Hydrogen Peroxide in Your Toilet Tank Tonight and Watch What Happens -#1 Fixes a Running Toilet | 2026-10-16 11:00 -07:00 | 5266 | 0.69 |
| 4 | nbBsxB8rFwU | 9 Hydrogen Peroxide Car Carpet Tricks That Make Professional Detailers Look Overpriced! | 2026-10-15 06:25 -07:00 | 1714 | 0.22 |
| 5 | YYLUiZEB_pE | Put Hydrogen Peroxide on Dog Pee Stains and Watch What Happens (11 Secrets Cleaners Won’t Tell You) | 2026-10-14 09:00 -07:00 | 1661 | 0.22 |

## Group B — 5 most-viewed long-form published on/after 2024-10-20

| Popular rank | Video ID | Title | Upload (exact) | Views | Views/normal |
|---|---|---|---|---|---|
| 1 | ls7BwoRhM9Q | 9 Things Plumbers Don't Want You to Know About Hydrogen Peroxide (#4 Saves $300) | 2026-05-23 02:15 -07:00 | 2183304 | 284.66 |
| 2 | RA1-fogcslM | 11 Things Auto Detailers Don't Want You to Know About Hydrogen Peroxide (#7 Saves $500) | 2026-08-24 04:57 -07:00 | 1676523 | 218.58 |
| 3 | SUqzcj5udsk | 12 Things Plumbers Don't want You to Know About Hydrogen Peroxide! | 2026-08-04 15:47 -07:00 | 1513057 | 197.27 |
| 4 | yIh1HAlbhc0 | 11 Things HVAC Technicians Don't Want You to Know About Hydrogen Peroxide! (#8 Saves $900) | 2026-08-07 15:55 -07:00 | 1089664 | 142.07 |
| 5 | Ins--8a65ZI | 11 Things Mechanics Don't Want You To Know About Hydrogen Peroxide! | 2026-07-05 07:04 -07:00 | 989059 | 128.95 |

None of the top 5 popular videos was in Group A, so no skip-down was needed. All five are well inside the 24-month window.

## Skipped videos

- None. All 10 selected videos had transcripts.
- The selection rule was applied regardless of topic. As a result, Group A includes car carpet (nbBsxB8rFwU) and dog stains (YYLUiZEB_pE), and Group B includes car interiors (RA1-fogcslM), car care (Ins--8a65ZI) and HVAC (yIh1HAlbhc0).

## Normal

**Normal = 7670** (median of the 15 most recent long-form uploads at least 7 days old as of 2026-10-20, exact views from `youtube_video_details`).

| # | Video ID | Upload (exact) | Views |
|---|---|---|---|
| 1 | xjD_02aQcRc | 2026-10-13 07:45 -07:00 | 1415 |
| 2 | aq472DAKmuw | 2026-10-11 07:45 -07:00 | 11838 |
| 3 | _SzUE4m9UWA | 2026-10-10 09:00 -07:00 | 2878 |
| 4 | 2w5W-RJxeu4 | 2026-10-09 12:41 -07:00 | 2719 |
| 5 | KpYUcF9mqXA | 2026-10-08 06:00 -07:00 | 3396 |
| 6 | k8ntn53i-l4 | 2026-10-06 11:07 -07:00 | 10384 |
| 7 | lAB4cFTQIxM | 2026-10-05 06:40 -07:00 | 1483 |
| 8 | XXcdoopJQsE | 2026-10-03 16:17 -07:00 | 1309 |
| 9 | pickXFED8B8 | 2026-10-02 10:24 -07:00 | 228548 |
| 10 | 8f_8A_I0uQs | 2026-10-01 12:25 -07:00 | 7670 |
| 11 | Zef4LQvEMe4 | 2026-09-30 09:38 -07:00 | 7866 |
| 12 | _6DsA7qHSro | 2026-09-29 12:10 -07:00 | 64064 |
| 13 | 9vyvOUVr7RA | 2026-09-28 07:33 -07:00 | 5543 |
| 14 | -q-LJnSgJh8 | 2026-09-26 20:22 -07:00 | 153817 |
| 15 | Il3TkvVja1s | 2026-09-22 09:06 -07:00 | 253420 |

- Sorted: 1309, 1415, 1483, 2719, 2878, 3396, 5543, **7670**, 7866, 10384, 11838, 64064, 153817, 228548, 253420.
- Boundary: xjD_02aQcRc is exactly 7 calendar days old on 2026-10-20 and was included. YYLUiZEB_pE (2026-10-14, 6 days) and newer were excluded.
- The 16th video, h1sv9OU6Okc (2026-09-21, 1905 views), is outside the window.
- The window is skewed: 4 of the 15 have 64K–253K views and the rest 1.3K–12K.

## Format basis

FACELESS. Basis:
- NexLev `check_faceless_channel` isFaceless=true (0.98).
- The about text is blank.
- All 10 transcripts are unattributed voice-over ("we", sometimes "I") with no named presenter, no references to anyone on camera and no sign of an AI-avatar presenter.
- Comments on the popular uploads describe "AI narration"/"AI voice" and footage that does not match the narration (cloth seat shown, then a leather one; baking soda shown when peroxide is described; 35% jugs on screen).
- Not visually verified: no video was viewed.

## Comment totals (top-level, after de-duplication within each sort)

| Video ID | Top | Newest | Also in top | Spam skipped | API commentsCount |
|---|---|---|---|---|---|
| cljD9InmFzk | 0 | 0 | 0 | 0 | 0 |
| TOurn07rVVQ | 0 | 0 | 0 | 0 | 0 |
| uJVc7zmq7vs | 4 | 4 | 4 | 0 | 5 |
| nbBsxB8rFwU | 0 | 0 | 0 | 0 | 0 |
| YYLUiZEB_pE | 0 | 0 | 0 | 0 | 0 |
| ls7BwoRhM9Q | 24 | 20 | 1 | 0 | 745 |
| RA1-fogcslM | 19 | 19 | 0 | 0 | 365 |
| SUqzcj5udsk | 20 | 20 | 6 | 0 | 169 |
| yIh1HAlbhc0 | 17 | 18 | 4 | 2 | 100 |
| Ins--8a65ZI | 20 | 19 | 6 | 1 | 234 |

- Total: 104 top + 100 newest entries, 183 unique comments.
- Owner pinned comments are included and tagged `[channel owner]`.
- Spam skipped (3): one off-topic bot-style comment ("metal-refining setup… flow battery build"), and two word-for-word copies of other top comments posted by a second account with a timestamp added. The same copying pattern appeared on two videos.
- Username check: done after writing. No commenter usernames or handles appear in any comments.md. The only "@" hits are a timestamp ("@3:32") and "@ corrections"; the only channel-name hits are the owner's own link URL.

## Failures and API oddities

- **Comment pagination did not work.** On ls7BwoRhM9Q, top pages 2–4 returned the same ~20 comments reshuffled (about 2 new per page), and newest page 2 returned exactly page 1. On RA1-fogcslM, top page 2 was identical to page 1. Further paging was stopped, and every video got one page per sort (~20 each). That is below the brief's ~50 top + ~25 newest target for the Group B videos.
- **Zero comments:** four Group A videos (cljD9InmFzk, TOurn07rVVQ, nbBsxB8rFwU, YYLUiZEB_pE) returned commentsCount 0 for both sorts. It is not possible to tell from the API whether comments are off or simply not posted yet (the videos are 1–6 days old).
- **Comment dates:** the API's comment publishDate values are rebuilt from relative text ("2 months ago"), so they are approximate. They are not recorded in the files.
- **List dates are approximate.** Example: ls7BwoRhM9Q is listed as 2026-06-20, but details give 2026-05-23. Exact dates come from `youtube_video_details`.
- **Inconsistent video counts:** videosCount was "31" in the newest listing, "0" in the popular listing and "75 videos" from `youtube_channel_about`.
- **Captions:** `youtube_video_details` reports hasCaption=false for all checked videos, yet NexLev returned English auto-generated transcripts for all 10. The transcript language menus also list other auto-generated tracks (Spanish, Portuguese-Brazil, Italian).
- **Metadata:** nbBsxB8rFwU's description promises "13 things" about car seats and child seats; the text is copied from RA1-fogcslM's description and doesn't match the video's 9 carpet tricks. RA1-fogcslM's title says 11, but its script counts 13.
- **Pinned links:** the owner comment on Ins--8a65ZI links to a different e-book store (aminomedia.gumroad.com) from the one on ls7BwoRhM9Q and SUqzcj5udsk (thecheapfix.netlify.app).
- **Shared text across videos (described only, see notes):** large passages repeat nearly word for word between cljD9InmFzk and TOurn07rVVQ, between nbBsxB8rFwU and RA1-fogcslM, and between ls7BwoRhM9Q and Ins--8a65ZI.
- **Other transcript signs:** doubled number calls ("Number eight. Number eight.") and caption glitches ("Eighty a mi- dangerous", "you you", "a a").
- No NexLev tool call failed.

## Files written

- `data/competitors/thecheapfix/<id>/meta.md`, `transcript.txt`, `comments.md` for the 10 videos above
- `notes/competitors/thecheapfix__<id>.md` for the 10 videos above
- this log
