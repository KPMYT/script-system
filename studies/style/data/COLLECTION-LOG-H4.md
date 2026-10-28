# Collection log: helper H4 (round 3, script and comment study)

Collected 2026-10-28 by collector H4, following `study-brief.md` ("Isolation rules" and "Round 3"). Describe-only. Videos: the 11 rows of `inputs/videos.csv` with helper = 4. Files written only in `data/<my channel slugs>/`, `notes/<slug>__<id>.md` and this log. Working scripts are in the session scratchpad (`round3-h4/`), not in the repo.

## Summary

| n | Video | Channel (slug) | Group | Views (10-28) | Normal | ÷ normal | Transcript | Comments kept | Notes |
|---:|---|---|---|---:|---:|---:|---|---:|---|
| 7 | vFul5tvg1Cw | justin-hickox | Hair mistakes and haircuts | 3,222,185 | 51,000 | 63.18 | English auto, 315 seg | 36 | yes |
| 10 | XR3IwlcIcCY | elegant-after-60 | Hair mistakes and haircuts | 698,146 | 2,900 | 240.74 | English auto, 307 seg | 42 | yes |
| 11 | SdbAfqmUwJ0 | camino-de-los-ancianos | Hair mistakes and haircuts | 670,236 | 18,000 | 37.24 | **Arabic auto only**, 608 seg | 37 | **no (dropped; replaced by row 46)** |
| 13 | rU56_ly6l2s | justin-hickox | Thin or fine hair | 1,493,819 | 51,000 | 29.29 | English auto, 438 seg | 38 | yes |
| 22 | KNwk391XyIY | rock-your-fashion | Body shape | 372,217 | 7,600 | 48.98 | English auto, 320 seg | 41 | yes |
| 30 | kKjLX7Q6wc8 | ever-chic-at-50 | Single items | 536,110 | 5,300 | 101.15 | English auto, 556 seg | 37 | yes |
| 35 | fLIVwKa-y3U | aliceinparis | French angle | 125,357 | 28,000 | 4.48 | English auto, 298 seg | 31 | yes |
| 40 | 6byOPawCepI | age-with-style | Pair A (winner) | 1,107,951 | 3,800 | 291.57 | English auto, 396 seg | 42 | yes |
| 41 | K6N1EFo7oec | age-with-style | Pair A (re-upload) | 7,133 | 3,800 | 1.88 | English auto, 465 seg | 29 | yes |
| 42 | _OQsPYjIfsQ | chicaftersixty | Pair B (winner) | 493,468 | 2,400 | 205.61 | English auto, 640 seg | 46 | yes |
| 45 | ZFx3yIrJqO0 | elegant-after-60 | Pair C (copy) | 2,229 | 2,900 | 0.77 | single-video call, 375 seg | 8 | yes |
| 46 | 8p2y_Yk0pNQ | stylish60plus | Hair mistakes and haircuts (replaces row 11) | 216,520 | 8,500 | 25.47 | single-video call, 583 seg | 26 | yes |

Videos collected: 12 (meta, transcript, comments for all), the 11 assigned plus the swap. Notes written: 11. Transcripts missing in English: 1 (SdbAfqmUwJ0, dropped and replaced, see below).

Normals all come from `round2/channels-all.csv` (no `youtube_channel_videos` call was needed; Ageless Confidence is not an H4 channel). There are two channels named "Elegant After 60" in that file; both H4 videos (XR3IwlcIcCY and ZFx3yIrJqO0) return channel ID `UC1eIOMYX7jZveQT3ezH59rw` (@ElegantAfter60, normal 2,900), so the Pair C copy is on the same channel as the 698K "Granny" cut video, as the selection says.

## NexLev calls: 52 (48 in the first run, of 60; 4 for the swap, of the 8 allowed)

1. `youtube_video_details` × 11 (one per video).
2. `get_bulk_video_transcripts` × 1 (10 IDs; 10/10 successful). The output was saved by the tool to a file and converted by script to `[m:ss] text` lines (start from `startMs`, HTML entities unescaped, whitespace collapsed).
3. `get_video_transcript` × 2: ZFx3yIrJqO0 (the 11th ID); SdbAfqmUwJ0 again, because the bulk call returned an Arabic track (it returned the same Arabic text).
4. `youtube_video_comments` × 31: top page 1, newest page 1, and top page 2 via the continuation token for 9 videos; 2 calls for ZFx3yIrJqO0 (no continuation token; only 8 of 13 comments returned); 2 calls for SdbAfqmUwJ0 (page 2 of top not requested: its comments and audio are not English and no notes are written for it).
5. `youtube_video_details` × 3 for the self-check.
6. Swap (8p2y_Yk0pNQ): `youtube_video_details` × 1, `get_video_transcript` × 1 (track name not returned; 583 segments, 3,864 words), `youtube_video_comments` × 2 (top page 1, newest page 1) + 1 (top page 2 via the token; it repeated page 1 and added none).

Failures: none. No call errored, no limit or credit message.

## Swaps

- **SdbAfqmUwJ0 (Camino de los Ancianos, row 11).** NexLev details return a Spanish title ("Evita Estos Cortes de Pelo de “Señora Mayor” que te Hacen Ver Más Mayor — ¡El #5 es Muy Común!") and a Spanish description; videos.csv carries an English title. The transcript track NexLev selects is "Arabic (auto-generated)" (its languageMenu says "Spanish (auto-generated)"); both the bulk and the single call return the same Arabic text. All 37 collected comments are in Spanish, many of them the one word "Lista" (ready). Round 2 had already flagged the channel ("about text and thumbnail text are Spanish ... check language before using as an English peer"). Meta, transcript (Arabic, as returned) and comments are kept; no notes are written. The main session dropped it (2026-10-28); its files are kept as they are.
- **Swap done (2026-10-28, on the main session's request):** row 46, Stylish60plus, "7 Modern Haircuts That Instantly Make You Look Younger 60+", `8p2y_Yk0pNQ`, collected the same way into `data/stylish60plus/8p2y_Yk0pNQ/` with notes in `notes/stylish60plus__8p2y_Yk0pNQ.md`. Normal 8,500 from `round2/channels-all.csv` (channel ID UCf9O3MaUZAXbUeb5LllhekA). 35 days old at collection; 26 unique comments of 70 shown.

## Comments

- Kept per video: see the table. Top lists hold 20 to 27 (page 1 plus any new comments on page 2), newest lists 19 or 20 (8 for ZFx3yIrJqO0).
- Top page 2: NexLev returned a re-ranked copy of page 1, adding 0 to 7 new comments (vFul5tvg1Cw 0, rU56_ly6l2s 0, K6N1EFo7oec 0, XR3IwlcIcCY 3, KNwk391XyIY 4, kKjLX7Q6wc8 1, fLIVwKa-y3U 1, 6byOPawCepI 2, _OQsPYjIfsQ 7). The HVAC study saw the same behaviour.
- Comment text and likes were extracted by script from the tool results; username and channel-ID fields were dropped before anything was written. @handles inside text are replaced with "@[handle removed]". Owner comments marked [OWNER]: 3 (both Justin Hickox videos, pinned product lists; Ever Chic At 50, a pinned question).
- Spam skipped: 2 ("332" on rU56_ly6l2s; a garbled string on vFul5tvg1Cw).
- Several of the short praise comments on the faceless channels' videos come from accounts whose display names read like other over-50 style channels. The names are not stored; the comments are kept as ordinary comments.

## Self-check

1. Three fresh `youtube_video_details` calls (end of run):
   - _OQsPYjIfsQ: 493,474 views (stored 493,468, +6); likes 10,177 (same); date, length and channel ID match.
   - K6N1EFo7oec: 7,133 views and 132 likes (both the same); date, length and channel ID match.
   - kKjLX7Q6wc8: 536,108 views (stored 536,110, −2); likes 4,697 (same); date, length and channel ID match.
2. Quote check (`python3 -I` script): every double-quoted string in the 10 notes files was searched for in that video's `transcript.txt`, `comments.md` or `meta.md` (title and quoted description lines), case, punctuation and quote marks normalized, quotes with "..." checked part by part. First run: 5 not found, all my own paraphrases placed in quote marks; reworded. Final run: **582 quotes, 0 not found** (transcript 452, comments 113, meta 17).
3. Swap notes (8p2y_Yk0pNQ), same script: first run 3 not found, all because the transcript puts a "[music]" tag inside the quoted sentence; the quotes now include the tag as the transcript shows it. Final: **64 quotes, 0 not found** (transcript 54, comments 9, meta 1). No fresh details re-check was run for the swap (its details call is from the same session, minutes earlier).

## Anything odd

- **Presenters.** Justin Hickox: a man; his own name is not spoken in either transcript (only in the code "Justin 13"); he calls the bob model "Di" (Dionna in the description, "My Wife's Beauty Favorites" in his pinned comment). Aliceinparis: a woman on camera; her name is not spoken. Age with Style: no name spoken, but both descriptions are signed "Sarah". ChicAfterSixty (round 2: AI presenter): an unnamed first-person woman over 60 with a family backstory, who says of her paid circle "I answer you myself, never a robot". No other presenter gives a name.
- **AI disclosure lines:** none in any of the 11 descriptions. AI remarks in comments: XR3IwlcIcCY 2, kKjLX7Q6wc8 2, 6byOPawCepI 1, K6N1EFo7oec 1, _OQsPYjIfsQ 1 (defending "the AI voice"); none on the real-presenter videos.
- **Group fit.** fLIVwKa-y3U (French angle) never addresses age: no age is said, none in the title. The video is a general Paris trends list with a sponsored pearl segment. SdbAfqmUwJ0 is not English (above).
- **Pair A.** K6N1EFo7oec is not a re-cut of 6byOPawCepI: same title and description template, but a different script (different hook, partly different mistakes, longer items, and only one "over 60" against about 12). Its early "Where in the world are you watching from" ask is answered by 24 of its 29 comments.
- **Placeholders left in descriptions:** XR3IwlcIcCY ("[Link to Volumizing Mousse]" and two more); K6N1EFo7oec ("[Insert Channel Link Here]").
- **Promise not paid:** kKjLX7Q6wc8's recap says "we've also talked about how to shop with intention" and the description promises "a smart-shopping guide"; no such segment exists.
- **Speech rate.** The Justin Hickox transcripts run 228-245 wpm because two people talk and the auto-captions merge them; the Aliceinparis captions garble many accented words (quotes follow the captions).
- **Swap video (8p2y_Yk0pNQ).** It opens "Please do not get the granny cut." (the theme of XR3IwlcIcCY). Its transcript carries many "[music]" tags. About 12 of its 26 comments are short praise, several from accounts named like other over-50 style channels. One viewer says the same photos were used for different cuts. No AI disclosure in the description, no AI remarks in comments.
- **Notes length.** The notes run about 850-1,250 words, over the brief's "about 500-800", because every required section is filled; the ChicAfterSixty notes are the longest (26:35 video, five long rules).
