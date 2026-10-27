# Collection log — HVAC Exposed (faceless persona, structure only)

Collected 2026-10-27 by collector helper D, following `studies/hvac/study-brief.md`. NexLev MCP tools only. Rows 34–35 of `inputs/videos.md`.

## Channel

- Channel ID UCZ1IwSV46bb09fMvqHn6_2A · @HVACExposed
- `youtube_channel_videos` meta: 9.59K subscribers; listing videosCount "31". The `youtube_channel_outliers` channel block (called once while looking for a cheaper source of exact views; it found no outliers): "80 videos", 2,020,215 total views, joined 2026-02-27, country United States, one link "E-book" → askfrankhvac.com, avgViews 25,253. About text: "Your HVAC system is the most expensive thing in your home you know nothing about. We're here to change that. Real research. No contractor kickbacks. No brand deals. Just the facts."
- `check_faceless_channel` (cached 2026-10-27): isFaceless=false, confidence 0.97, format "educational", tags business / home improvement / how to / education. The selection marks it F. Descriptions use a first-person persona with an e-book: "📘 THE HVAC OWNER'S BIBLE - everything I check on a system, and on a quote before you sign it: askfrankhvac.com" and "After 20 years in the field" (l2yy). The narration never names the persona. The videos were not viewed.

## Videos

| Row | Video ID | Type | Upload | Duration | Views | Likes | Normal | × normal | Segments | Comments (top + newest) |
|---|---|---|---|---|---|---|---|---|---|---|
| 34 | l2yyfYpcwpQ | product villain / myth-bust | 2026-03-30 | 13:37 | 351,191 | 4,617 | 548 | 640.86 | 358 | 20 + 20 (175 shown) |
| 35 | QKPPm6M0__o | brand verdict | 2026-02-28 | 12:07 | 578,457 | 8,606 | 548 | 1055.58 | 332 | 38 + 20 (1K shown) |

## Normal = 548

The median of the exact views of the 15 most recent long-form uploads published on or before 2026-10-20, from `youtube_channel_videos` sort=newest, page 1. Excluded as under 7 days old: 65SBaxQH5PY (1 day), fAMl98_0Qwc (4 days). x4M4j_vZvFc was checked with `youtube_video_details`: published 2026-10-19 08:45 -07:00, 8 days old, so it is included (415 views, exact). The listing gives exact counts under 1,000. The median, cMEGznAyMYM at 548, is below 1,000, and so are its neighbours (488 and 643), so the median is exact.

Window, with listing views: x4M4j_vZvFc 415 · myti1Fy69Mg 300 · mJesg2iENcA 330 · CCOusOwvBIU 643 · uwciEmrw7z4 386 · Q76pw2qLfXQ 488 · PaoR-sLb4S4 345 · fgaNhEU-A2s 927 · K4D0x9yMR4Y 4.7K · _7Gq3aGFs5A 865 · wtSOeT1ROYk 3.4K · 94RlbdgEt30 6.6K · oiBYLY2fOVI 340 · **cMEGznAyMYM 548 (median)** · 92DaQEp83QY 2.1K. All between 11:23 and 14:59. 16th: -3WIudw2rKE (3.3K).

The two study videos (Feb and Mar 2026) are far outside the recent window, which explains the very large multiples (641× and 1,056×). The listing also shows titles that closely track Ray Dutton's Garage titles, for example "5 Winter Thermostat Habits That Wear Out Your Furnace Years Early" (x4M4j_vZvFc) and "Before You Turn the Heat On This Fall, Check These 5 Things" (cMEGznAyMYM).

## Method

- `youtube_video_details` for both videos; `get_bulk_video_transcripts` (one call with Vent Exposed and Lost Survival Knowledge), both succeeded, English auto-generated, `[m:ss] text`.
- Earlier pull: `niche-research/.../ray-sources-2026-10-26/transcripts/tx_hvacexposed_filter.txt` = l2yyfYpcwpQ. It is plain text with no timestamps. After normalising case and punctuation, the word sequence is identical to the fresh pull (2,045 words, 0 differences). The only difference is the format.
- Comments, top sort: l2yy p1 20, p2 an exact repeat (0 new), p3 not fetched; QKPP p1 20, p2 +11, p3 +7. Newest: one page of 20 each. No owner replies. QKPP's top list includes one comment that names "ARS/Rescue Rooter" as a quote option (29 likes). It is kept and marked, and the same wording pattern appears twice on Vent Exposed.

## Failures and gaps

None of the calls failed. The top lists are shorter than ~60 because of the paging. The notes run ~620–640 words.

## Check of my own work (2026-10-27)

- **Meta re-check:** a fresh `youtube_video_details` for QKPPm6M0__o returns duration 727 s and upload date 2026-02-28 15:16 -08:00, both matching meta.md. Views are 578,495 against 578,457 in meta.md (+38 in the interval); likes 8,606 match.
- **Quote re-check against transcript.txt:**
  - l2yyfYpcwpQ [12:46] "It's a marketing story dressed up as a health product." Transcript: "[12:46] exchanger. It's a marketing story" / "[12:48] dressed up as a health product." Matches.
  - QKPPm6M0__o [10:21] "Bosch broke the lock." Transcript: "[10:21] Bosch broke the lock." Matches.
  - l2yyfYpcwpQ [8:04] "Your HVAC system is not a medical device." Transcript: "[8:04] Your HVAC system is not a medical" / "[8:07] device." Matches.
- All transcript quotes and quoted comments in both notes were also checked by script, with 0 misses.
