# Collection log — Vent Exposed (faceless, structure only)

Collected 2026-10-27 by collector helper D, following `studies/hvac/study-brief.md`. NexLev MCP tools only. Row 36 of `inputs/videos.md`.

## Channel

- Channel ID UCTDbUAjE9Ab_wwvuV7cgtvQ · @VentExposed
- `youtube_channel_videos` meta: 1.93K subscribers; 12 videos; empty continuation (the whole channel is on one page). About text starts: "Your contractor charged you $400 for an $8 part. Your 'premium' AC brand is made by the same company as the budget one. And that $30 filter? It's destroying ..."
- `check_faceless_channel` (fresh analysis 2026-10-27): isFaceless=false, confidence 0.91, format "reviews", tags home repair / engineering / science / "youtube faceless / tiktok pages". The selection marks it F. No named narrator. Descriptions list "Sources" and "No sponsorships. No affiliate links.", and carry the hashtag #HVACExposed and the keyword "hvac exposed" (HVAC Exposed is a different channel). The channel's topics also include pest control and water heaters. The video was not viewed.

## Video

| Row | Video ID | Type | Upload | Duration | Views | Likes | Normal | × normal | Segments | Comments (top + newest) |
|---|---|---|---|---|---|---|---|---|---|---|
| 36 | 86S3ITbfzQY | brand verdict | 2026-05-25 | 8:12 | 673,134 | 9,411 | 1,119 | 601.55 | 225 | 30 + 20 (732 shown) |

## Normal = 1,119

The channel has only 11 long-form uploads, all published more than 7 days ago (12 listed; MyxET4o45eg "17 2" is 3:48 and is excluded). With fewer than 15, the normal is the median of all 11. The median is TOnB8XmW6Cs, exact 1,119 from `youtube_video_details` (listing "1.1K"; its neighbours are 922 and 1.6K, so the rounding cannot reorder them).

Views from the listing: lPx46BZt0o0 83 · ZQ-4sAhwLYg 169 · laG6_n5G0mM 438 · TTtvxG2_PeY 705 · 8-FLSekacro 922 · **TOnB8XmW6Cs 1,119** · Sp-tauLyf48 1.6K · 9pW2TigPDzQ 3.4K · RSd0zscPMDs 5.4K · uTHHV98zlpw 13K · 86S3ITbfzQY 673,134. The study video is the channel's only upload above 13K.

## Method

- `youtube_video_details`; `get_bulk_video_transcripts` (225 segments, English auto-generated, `[m:ss] text`; contains "[music]" caption tags).
- Comments, top sort: p1 20, p2 +10, p3 0 new. Newest: one page of 20. No owner replies. Two top comments (29 and 34 likes) recommend "ARS" / "American Residential Services" for quotes in near-identical structure and wording. They are kept and marked in comments.md, and the same pattern appears once on HVAC Exposed QKPPm6M0__o.

## Failures and gaps

None of the calls failed. The top list stops at 30 unique comments. The note runs ~640 words.

## Check of my own work (2026-10-27)

- **Meta re-check:** a fresh `youtube_video_details` for 86S3ITbfzQY returns views 673,134, likes 9,411, duration 492 s and upload 2026-05-25 10:20 -07:00. All match meta.md exactly.
- **Quote re-check against transcript.txt:**
  - [3:39] "Nine brand names, one parts bin." Transcript: "[3:39] Nine brand names, one parts bin. So, why". Matches.
  - [2:48] "you're paying for a font on a metal box." Transcript: "[2:48] an American Standard, you're paying for" / "[2:50] a font on a metal box." Matches.
  - [4:34] "If that number makes your chest tight, keep listening". Transcript: "[4:34] depending on your market. If that number" / "[4:36] makes your chest tight, keep listening". Matches.
- One standout line, "a pricing structure, not a quality structure" [0:44], has a "[music]" caption tag inside it in the transcript ("a pricing [music] structure"). It is quoted without the tag.
