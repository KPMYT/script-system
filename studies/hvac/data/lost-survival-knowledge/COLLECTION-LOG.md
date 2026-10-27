# Collection log — Lost Survival Knowledge (faceless, structure only)

Collected 2026-10-27 by collector helper D, following `studies/hvac/study-brief.md`. NexLev MCP tools only. Row 37 of `inputs/videos.md`.

## Channel

- Channel ID UC-JjgZLelrq83F4vIfmD3Jw · @LostSurvivalKnowledge
- `youtube_channel_videos` meta: 15.4K subscribers; listing videosCount 31. About text starts: "Lost Survival Knowledge documents the self-reliance skills of early American homesteads, trail camps, and backcountry farms…"
- `check_faceless_channel` (cached 2026-10-27): isFaceless=true, confidence 0.98, format "documentary", tags prepping / home improvement / lifestyle / history, Trends keyword "survival prepping".
- The description carries a "Creative Process Disclosure": "Every episode is narrated by Joe, recorded for this channel. No synthetic, cloned, or AI-generated voices are used anywhere on Lost Survival Knowledge". That is the channel's own claim and was not verified. The selection marks the channel F. There is no product link and no keywords on the video.

## Video

| Row | Video ID | Type | Upload | Duration | Views | Likes | Normal | × normal | Segments | Comments (top + newest) |
|---|---|---|---|---|---|---|---|---|---|---|
| 37 | rX4eyZaHAjw | outage list | 2026-10-14 | 22:21 | 1,330,901 | 9,748 | 23,954 | 55.56 | 656 | 20 + 20 (414 shown) |

The video was 13 days old at collection, so its view count was still climbing fast (1,331,002 at the re-check a few minutes later).

## Normal = 23,954

The 15 most recent long-form uploads at least 7 days old, from `youtube_channel_videos` sort=newest, page 1. Excluded as under 7 days old: E2dneabQiE8 (3 days), zwrVqEHTNxY (5 days). The median is 0D07QPeiSA0, exact 23,954 from `youtube_video_details` (listing "23K"; neighbours 17K and 34K).

Window: pGHumnhmV4A 10K · rX4eyZaHAjw 1,330,901 (the study video, which is itself in the window) · m97VxEfuUbw 34K · lm1kEiEnlPQ 521K · b70IVJDybhg 3.0K · aqNCjVdyKK8 17K · C2N33sGzkx4 77K · jbLXP7rlaJc 3.8K · THCHA2KfrQU 8.3K · **0D07QPeiSA0 23,954** · Q0jfwAdO71o 321K · M8C3B4JWAso 112K · QdtPArYSHso 370K · zN14FWnSVc0 5.5K · Hscc6EdIyts 9.7K. All between 18:07 and 25:53. 16th: v_V_3-gufv8 (119K). The study video is in its own normal's window. Leaving it out and adding the 16th (119K) would not move the median.

The channel's titles repeat one frame: "15 Dollar Tree Items That Become WORTH GOLD When Your Furnace Stops Working" (521K), "25 Walmart Items That Become Priceless When the Power Goes Out" (321K), "20 Cheap Items That Can Keep Any Room Warm Without Electricity" (370K).

## Method

- `youtube_video_details`; `get_bulk_video_transcripts` (656 segments, English auto-generated, `[m:ss] text`, many "[music]" tags).
- Comments, top sort: p1 20, p2 an exact repeat (0 new), p3 not fetched. Newest: one page of 20. No owner replies, even though the description invites stories ("the best ones end up in future episodes").

## Failures and gaps

None of the calls failed. The top list stops at 20 unique comments. The note runs ~760 words, the longest of my ten, because of the 15-item count-down and the many safety lines.

## Check of my own work (2026-10-27)

- **Meta re-check:** a fresh `youtube_video_details` for rX4eyZaHAjw returns duration 1,341 s and upload 2026-10-14 11:00 -07:00, both matching meta.md. Views are 1,331,002 against 1,330,901 (+101 in the interval); likes are 9,749 against 9,748.
- **Quote re-check against transcript.txt:**
  - [18:23] "Save your money and your eyebrows." Transcript: "[18:23] Save your money and your eyebrows. A few". Matches.
  - [20:00] "People get cold, and cold people get desperate." Transcript: "[20:00] >> People get cold, and cold people get" / "[20:02] desperate." Matches.
  - [21:36] "The same tricks that keep the warmth in also keep the danger in." Transcript: "[21:36] The same tricks that keep the warmth in" / "[21:38] also keep the danger in." Matches.
- "Most of them under $10" [0:38] has a "[music]" caption tag in the transcript ("Most of them [music] under $10"). It is quoted without the tag.
