# Round 3 collection log: helper H5 (model scripts)

Date: 2026-10-28. Videos: the 8 rows of `models/approved-models.csv` with helper = 5 (M01, M02, M03, M05, M06, M10, M13, M15). Method: `study-brief.md`, "Round 3" and "Rules added after the round 3 check". Written only to `data/<channel_slug>/<video_id>/`, `notes/<channel_slug>__<video_id>.md` and this file. Scripts kept in the session scratchpad (`h5/`), all run with `python3 -I`. No git commands run.

## NexLev calls: 36 of 45

| Tool | Calls | Notes |
|---|---|---|
| youtube_video_details | 8 + 3 self-check = 11 | all succeeded |
| get_bulk_video_transcripts | 1 | 8 IDs, 8 of 8 returned. The result was too large to show inline and was saved by the harness to a file, then parsed with `python3 -I`; not a failure |
| get_video_transcript | 0 | not needed |
| youtube_video_comments | 24 | top + newest for all 8; top page 2 for all 8 (every top call returned a continuation token) |
| **Total** | **36** | no failures, no retries, no limit or credit errors |

## Videos collected (8 of 8, all with transcripts)

| Model | Channel | Video | Upload date | Views | ÷ normal | Duration | Transcript | Comments shown / collected |
|---|---|---|---|---:|---:|---|---|---|
| M01 hair | Summer Beauty | i5jFYNeCHGM | 2026-06-19 | 665,238 | 14.78 (45,000) | 15:03 | en auto, 374 seg | 576 / 39 |
| M02 hair | Woman in midlife | pC4YjCxSalg | 2025-12-04 | 322,520 | 60.85 (5,300) | 9:04 | en auto, 225 seg | 1K / 41 |
| M03 hair | Karen of Curl House | A8llK8GsSD0 | 2026-10-10 | 297,760 | 32.02 (9,300) | 10:08 | en auto, 222 seg | 290 / 41 |
| M05 hair | Boys And Girls Hairstyles (RaDona) | R7g-CrH4m2A | 2026-06-25 | 353,040 | 42.53 (8,300) | 24:23 | en auto, 556 seg | 190 / 35 |
| M06 hair | Justin Hickox | W8Hg-J6HbUo | 2026-05-12 | 1,292,732 | 25.35 (51,000) | 16:14 | en auto, 456 seg | 2.2K / 53 |
| M10 hair | Justin Hickox | GOuDkBf6CmA | 2025-05-06 | 1,261,132 | 24.73 (51,000) | 16:18 | en auto, 456 seg | 1.4K / 43 |
| M13 fashion | Adore Your Wardrobe | 7ecJWmEQ3Ks | 2026-04-05 | 814,141 | 33.92 (24,000) | 13:18 | en auto, 342 seg | 1.6K / 39 |
| M15 fashion | Tracy Campoli | m7pfd4OxPzs | 2026-04-16 | 170,229 | 3.55 (48,000) | 17:25 | en auto, 463 seg | 490 / 43 |

Normals are from `approved-models.csv` (taken from `round2/channels-all.csv`); views ÷ normal uses the exact views from the first details call. Missing transcripts: none. Swaps needed: none.

## Things the main session may want to decide

- **R7g-CrH4m2A (RaDona, M05) is a salon cut-along, not a narrated advice script.** A real stylist cuts and styles a real client (Sharon) and explains as she goes: no hook, no list, no spoken CTA, long quiet cutting stretches, 133 wpm. It is talking, and the presenter is real, but its structure is unlike the other seven. The title's "Women Over 70" and the client's age (76) are only in the title and description, never in speech.
- **No video is a silent try-on or haul, and every presenter is a real person** (as heard and as typed in round 2). GOuDkBf6CmA (Justin Hickox, M10) is a real presenter talking over edited photos of one model; he says "I don't think I did the best job photoshopping this". Commenters object that the model has no double chin, but none call the video fake or AI.
- **Ages are rarely spoken.** Only M06 ("women over 50", once), M13 ("over the age of 50" and "over 50") and M02 (her own "49") say an age. M01, M03, M10 and M15 say no age at all; the titles of M03 ("Gray") and M15 ("After 50") are not echoed in speech, and M03 never says the word gray.
- **M15 (Tracy Campoli) is 3.55 × normal**, the lowest of the eight; the candidates list had 170,000 views (about 3.5 ×). One of its seven items is the paid Negative sponsor read.
- **M03 (Karen of Curl House) was 18 days old** at collection (uploaded 2026-10-10), so its views are still moving (+31 in the self-check).
- **M10 (GOuDkBf6CmA) is 540 days old** (uploaded 2025-05-06), from the 12-to-24-month block of the candidates list.

## Oddities

- **Presenters as heard:** Summer Beauty's stylist never says her name ("after 19 years as a hair stylist"). Woman in midlife never says her name (49 when she stopped dyeing, two years on, a senior Wall Street job); a short clip at 0:54 is an earlier recording ("I have not yet told my husband"). Karen names herself and her credentials. RaDona is not named in speech; the client Sharon is. Justin Hickox is not named in his own speech in either video; in W8Hg-J6HbUo he speaks to his editor "Joseph". Kelly Snyder names herself (the description spells Snyder). Tracy does not say her name; she gives "only 5'2", Miami, a husband, a daughter and "we're Gen X".
- **Chapters that do not match speech:** W8Hg-J6HbUo's description has a stray "13:20 Mistake #6 / 15:23 Closing Thoughts" after its five mistakes; the speech has five. GOuDkBf6CmA's chapters list three features; the speech covers four.
- **A8llK8GsSD0:** the details/transcript `languageMenu` field reads "Ukrainian (auto-generated)", but the selected track is "English (auto-generated)" and the speech is English. About 70 seconds (7:02-8:11) have no speech.
- **W8Hg-J6HbUo** carries a sung on-screen overlay of critics' comments (6:52-7:27, "[singing]") and an outtake after the sign-off (16:00-16:12), which is the transcript's last 40 words.
- **AI disclosure:** none of the 8 descriptions has an AI disclosure line.
- **AI remarks in comments:** one, approving, on i5jFYNeCHGM: "I love that you do the measurements manually and not AI." (0 likes). None elsewhere.
- **Comment pagination:** every top call returned a continuation token. Page 2 added 0 new comments on R7g-CrH4m2A and 7ecJWmEQ3Ks, 2 on three videos, 4 on two, and 15 on W8Hg-J6HbUo. Duplicates were removed by text; each `comments.md` says what page 2 added. A8llK8GsSD0, R7g-CrH4m2A and 7ecJWmEQ3Ks have no owner comment in the lists; 7ecJWmEQ3Ks's newest list begins with the top viewer comment (pinned-style), counted as "in both".
- **Spam:** none skipped. Two comments by other channel accounts on R7g-CrH4m2A ("What a beautiful transformation!...", "Very nice! She looks so beautiful.") read as generic praise, have no links and are kept. One meaningless comment ("auwatte") is kept.
- **Non-English comments kept:** one Spanish (pC4YjCxSalg), one Russian (W8Hg-J6HbUo).
- **Note length:** the notes run about 990 to 1,320 words by `wc -w` (including headings and quotes), above the brief's 500-800 guide, as with H1's notes. Nothing was cut so that the quoted evidence stays complete.
- **File writing:** transcripts, comments and meta were written by `python3 -I` scripts. The details results and all 24 comment pages came back inline (not saved to files), so the comment texts, like counts and owner flags were copied from the inline results into per-page JSON files in the scratchpad and assembled by script; usernames were never copied. The notes were written directly.

## Self-checks

1. **Three fresh details calls** (2026-10-28, after all comment pulls):
   - A8llK8GsSD0: date and duration (608 s) matched; views 297,760 then 297,791 (+31), likes 3,708 then 3,711.
   - W8Hg-J6HbUo: date, duration (974 s) and likes (42,217) matched; views 1,292,732 then 1,292,763 (+31).
   - m7pfd4OxPzs: everything matched exactly (170,229 views, 5,698 likes, 1,045 s).
   - The first-pull figures are the ones recorded in meta.md, the notes and the table above.
2. **Quote verification.** A `python3 -I` script extracted every double-quoted string in my 8 notes and searched for it, after lowercasing, collapsing whitespace and normalising curly quotes, dashes and ellipses, in the video's transcript (timestamps stripped, segments joined), then `comments.md`, then only the title line and the quoted description line of `meta.md`. For every quote with an `[m:ss]` before it or `(m:ss)` after it, it checked that the time is within 3 seconds of the start of the segment where the quote begins.
   - First runs, note by note (several before meta.md was written): 35 strings not found and 3 timestamps off. Most misses were titles, title fragments and description text, found once meta.md existed; the rest were my own labels in quote marks (over 50, over 60, women over 50, controversial, fake, wish I had known, do this instead and similar) and one misquote (a line given as starting "And this is a scenario" where the transcript says "And again, this is a scenario"). The timestamp misses were 6:10 for 6:06, 5:58 for 6:12 and 0:34 for 0:39. All were fixed by removing quote marks from labels, re-quoting the exact words, or correcting the time. Two comment quotes with inner quote marks were re-quoted before their notes were first checked.
   - Final run: 487 quoted strings checked, 0 not found, 0 timestamps more than 3 seconds off.
   - A second script checked that like counts written next to comment quotes match `comments.md`: 49 checked, all matched (one apparent mismatch was the script reading across two quotes).
3. **Username check:** a search of my 8 `comments.md` files for "@" finds only the "@[handle removed]" replacements (owner-comment email addresses in the two Justin Hickox files) and the header text; a search of all my written files for ten commenter and channel handles seen in the raw responses found none.
