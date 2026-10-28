# Collection log, helper 3 (round 3, 2026-10-28)

Videos: the 11 rows of `inputs/videos.csv` with helper = 3 (8 channels). All 11 collected; every video has a transcript. **Swaps needed: none.**

## NexLev calls: 49 of 60

| # | Tool | Calls | Notes |
|---|---|---|---|
| 1-11 | youtube_video_details | 11 | one per video |
| 12-13 | get_bulk_video_transcripts | 2 | 10 IDs, then YeKT0zkdIrw; 11 of 11 returned. Both results were too large to display and were saved by the harness to files, which were read from disk (no data lost) |
| 14-24 | youtube_video_comments, top | 11 | 20 comments each, all returned a continuation token |
| 25-35 | youtube_video_comments, top page 2 | 11 | mostly the same comments as page 1 (vATkBSPjQmc: identical 20); 0-4 new per video |
| 36-46 | youtube_video_comments, newest | 11 | 20 each |
| 47-49 | youtube_video_details (self-check) | 3 | see below |

Failures: none. No retries. No limit or credit errors. Normals all taken from `round2/channels-all.csv` (no `youtube_channel_videos` call needed; Ageless Confidence is not one of my channels).

## Per video

| Video | Channel | Transcript (segments) | Comments shown | Collected (viewer + owner) | Spam skipped |
|---|---|---|---|---|---|
| vATkBSPjQmc | Elegance At 60 | auto, 231 | 183 | 36 (36 + 0) | 0 |
| XByilJlme5Y | Elegance At 60 | auto, 316 | 528 | 39 (38 + 1) | 0 |
| UUS1R9oWx4o | Summer Beauty | auto, 351 | 1.4K | 42 (41 + 1) | 0 |
| xNuoMiG2kVw | Summer Beauty | auto, 321 | 367 | 42 (41 + 1) | 0 |
| 9LvzTBzXL5k | Glam Girl Gabi | English (non-auto track), 431 | 628 | 43 (42 + 1) | 1 (hair-loss "recipes" promo) |
| G5y1gFHWPIA | Glow After 60 | auto, 781 | 288 | 38 (37 + 1) | 1 (another channel's self-promotion) |
| dn3mNRtYTY4 | Golden Melanin Lifestyle | auto, 385 | 713 | 36 (36 + 0) | 0 |
| h6Y1RZzOlzg | Chic After 60 | auto, 326 | 217 | 41 (41 + 0) | 0 |
| qFLenue5BBI | Ageless Melanin | auto, 355 | 1.1K | 44 (44 + 0) | 0 |
| WgkP3h4QWpg | MAKEOVERGUY | auto, 237 | 1K | 43 (43 + 0) | 0 |
| YeKT0zkdIrw | Chic After 60 | auto, 675 | 261 | 43 (43 + 0) | 0 |

Comments are top-level only (the tool returns no replies). Owner comments are marked `[OWNER]`. Comments from accounts whose names read like style or over-50 channel names are marked `[account named like a style channel]`; the names themselves are not stored. 31 such comments across my 11 videos, 11 of them on YeKT0zkdIrw. No usernames are stored anywhere.

## Self-check

1. **Three fresh details calls** (about 07:3x UTC, an hour after the first pull):
   - h6Y1RZzOlzg: views 552,974 → 553,988 (+1,014), likes 6,163 → 6,172. Title, duration and date unchanged. (The video is 7.5 days old, so still climbing.)
   - WgkP3h4QWpg: views 2,395,153 → 2,395,204 (+51), likes 26,462 → 26,463. Unchanged otherwise.
   - vATkBSPjQmc: views 754,127 and likes 9,474, unchanged.
   The meta files keep the first pull's figures.
2. **Quote check** (`python3 -I` script, scratchpad `round3-h3/check_quotes.py`): every double-quoted string in my 11 notes searched in that video's `transcript.txt` or `comments.md`, case- and punctuation-insensitive, also with non-speech tags such as `[music]` and `>>` removed. **544 quotes, 0 not found.**

## Method notes

- Transcript lines are `[m:ss] text`, from the tool's startMs. Word counts in meta.md include bracketed tags; word counts and wpm in the notes are spoken words only, and segment word counts are approximate (sums of segments between the start times given).
- The notes run about 950-1,150 words, over the brief's 500-800, because of the number of sections asked for.
- Scripts and raw tool outputs: scratchpad `round3-h3/` (`raw/`, `build1.py`, `build_meta.py`, `ana.py`, `check_quotes.py`). Raw outputs were taken from this session's own tool results.

## Anything odd

- **No AI disclosure** in any of the 11 descriptions. Golden Melanin Lifestyle carries only a general "educational and entertainment purposes" disclaimer.
- **Presenters' names:** Gaby (Glam Girl Gabi, says her name and "hairstylist and makeup artist for 20 years"). Summer Beauty says "As a hair stylist of 18 years" in both videos but no name. MAKEOVERGUY: the client names herself (Susan, 69); the narrator says "my book, Staging Your Comeback" but not his name; the description credits Christopher Hopkins. Several top comments speak of missing Christopher ("I know he is missed", "Thank you all of the team for carrying on"); worth a check before he is used as a model.
- **Voice and image remarks:** Glow After 60 drew 6 AI remarks (voice and images, for example a mirror reflection that "doesn't match"). Elegance At 60 (vATkBSPjQmc): one viewer calls the narrator "This man".
- **Group fit:** neither Summer Beauty video nor the Glam Girl Gabi video says an age in speech; their commenters include women in their 30s and under 50. Elegance At 60's two videos and the leggings video's titles say 50/60, but Elegance At 60's narration never says an age.
- **Promises not paid:** Glow After 60 twice points to a shopping list and affiliate links "in the description"; the description has neither (a top comment asks where they are, 42 likes). Elegance At 60 (XByilJlme5Y) says "We'll talk more about that later" about pants said to look outdated and does not return to it.
- **A cut in YeKT0zkdIrw:** the olive-and-ivory item (22:05) jumps from its name straight to accessories; it is about half the length of the other seven items.
- **Advice that differs between channels in this set:** Ageless Melanin calls navy "heavy and dated on mature skin" and black, beige and gray "aging colors"; Chic After 60's winner leads with navy and white and recommends beige and black.
- **Ratios:** YeKT0zkdIrw has no ratio in videos.csv; against Chic After 60's normal (37,000) it is 25.9×. h6Y1RZzOlzg is 14.9×.
