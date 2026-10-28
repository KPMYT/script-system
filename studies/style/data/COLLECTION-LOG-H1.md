# Round 3 collection log: helper H1

Date: 2026-10-28. Videos: the 12 rows of `inputs/videos.csv` with helper = 1. Method: `study-brief.md`, "Round 3". Written only to `data/<my channel slugs>/`, `notes/<my slug>__<id>.md` and this file. Scripts kept in the session scratchpad (`round3-h1/`).

## NexLev calls: 58 of 60 (53 in the first pass, 5 for the swap)

| Tool | Calls | Notes |
|---|---|---|
| youtube_video_details | 12 + 3 self-check + 1 swap = 16 | all succeeded |
| get_bulk_video_transcripts | 3 | 10 IDs + 2 IDs + 1 ID (swap); 13 of 13 returned. Both results were too large to show inline and were saved by the harness to a file, then parsed with `python3 -I`; not a failure |
| get_video_transcript | 0 | not needed |
| youtube_video_comments | 38 | top + newest for all 13; top page 2 for the 12 videos that returned a continuation token (UTpC6n7KKi0 returned none) |
| youtube_channel_videos | 1 | Ageless Confidence normal (not in round 2) |
| **Total** | **58** | no failures, no retries, no limit or credit errors |

## Videos collected (12 of 12, all with transcripts)

| # | Channel | Video | Views | ÷ normal | Transcript | Comments shown / collected |
|---|---|---|---|---|---|---|
| 3 | Marie-Anne Lecoeur | ixlexruRC6c | 1,038,117 | 12.36 (84,000) | en auto, 138 seg | 3K / 42 |
| 4 | Elegántica | X9mj5fEPfVk | 1,193,524 | 702.07 (1,700) | **es** auto, 490 seg | 1.5K / 44 |
| 14 | Rami Jabali Hair Salon | qwM0s0Q3Rjw | 748,617 | 15.60 (48,000) | en auto, 320 seg | 1.3K / 41 |
| 15 | chery 🍒 | XCf4o0ZOOiw | 103,785 | 14.03 (7,400) | en auto, 291 seg | 105 / 31 |
| 19 | Marie-Anne Lecoeur | G-RW7ih19Y4 | 547,210 | 6.51 (84,000) | en auto, 315 seg | 769 / 39 |
| 24 | Marie-Anne Lecoeur | MWQ6T1wURJU | 628,761 | 7.49 (84,000) | en auto, 278 seg | 1.7K / 39 |
| 25 | Adore Your Wardrobe | vBsFMkGDbhA | 396,929 | 16.54 (24,000) | en auto, 255 seg | 499 / 40 |
| 31 | Tracy Campoli | NT1mEOX-p7Y | 506,694 | 10.56 (48,000) | en auto, 716 seg | 482 / 40 |
| 34 | Marie-Anne Lecoeur | n9ICHZq3_tY | 138,649 | 1.65 (84,000) | en auto, 296 seg | 552 / 39 |
| 36 | French Fashion | -eTr9aVSWlM | 451,523 | 32.25 (14,000) | en auto, 377 seg | 171 / 39 |
| 39 | Rami Jabali Hair Salon | RuyOhWfU-RI | 714,306 | 14.88 (48,000) | en auto, 324 seg | 872 / 41 |
| 43 | Ageless Confidence | UTpC6n7KKi0 | 1,048 | 2.56 (409, fresh) | en auto, 389 seg | 1 / 1 |
| 47 | Ageless Style 50s & 60s | Fs17Qc6l8Ug | 267,196 | 55.67 (4,800) | en auto, 303 seg | 882 / 39 |

Normals are from `round2/channels-all.csv` except Ageless Confidence (UCxw2jFWBftkpRkFE4EC9W-Q, @AgelessConfidence-j2m, 219 subscribers, 16 videos): one `youtube_channel_videos` newest call listed all 16 uploads; all are 5:00 or longer (0 under 5:00); the newest (10 hours old) was excluded; the median of the other 15 (views as NexLev rounds them: 53 to 21,000) is 409. Older upload dates in that listing are relative ("3 months ago"), so the 7-day rule only bit on the newest.

Missing transcripts: none. Swaps needed for missing transcripts: none.

## Swap (2026-10-28, on the main session's instruction)

- **Row 4, X9mj5fEPfVk (Elegántica), dropped for being Spanish.** Its files are kept as they were: `data/eleg-ntica/X9mj5fEPfVk/` and `notes/eleg-ntica__X9mj5fEPfVk.md`.
- **Replacement: row 47, Fs17Qc6l8Ug (Ageless Style 50s & 60s, UCiZC8_8E5MJ5_8aymXClr-w, @AgelessStyle50s60s).** It uses Marie-Anne Lecoeur's exact title. Language checked first: the title, description and transcript track ("English (auto-generated)") are English. Normal 4,800 from `round2/channels-all.csv`; 267,196 views, 55.67 × normal; uploaded 2026-04-25, 185 days old; type faceless_narrated (round 2). It was collected by the same method, and its note has an extra "Against the original" section comparing it with ixlexruRC6c.
- Replacement oddities: the narrator is unnamed and never states a gender, but claims "I've worked with hundreds of women over 50". The description's "What We’re Covering" list (a "Matching" trap, fabrics) does not match the seven items spoken. The hook promises "the next 5 minutes", but the list runs about 8.5 minutes. There is no AI disclosure line. About 5 comments criticise the before/after and handbag pictures. Top page 2 returned the same 20 comments as page 1.
- The replacement note runs about 1,720 words because of the comparison section.

## Things the main session may want to decide (possible swaps)

- **X9mj5fEPfVk (Elegántica) is a Spanish-language video** (now dropped and replaced; see above). Title, description, narration (Spanish auto-generated track) and comments are all Spanish. `videos.csv` shows an English title, which reads as YouTube's translated title. Collected and noted in full (quotes in Spanish, glosses in English), but it does not meet the English-language rule in Phase 2.
- **vBsFMkGDbhA (Adore Your Wardrobe) has no age anywhere**: not in the title, description, keywords or speech. Commenters give ages 45 to 70.
- **UTpC6n7KKi0 (Ageless Confidence)** has 1 comment in total, so the comment half of the study is thin for it (expected for the flopped copy in Pair B).

## Oddities

- **Presenter names heard:** Kelly Snider (Adore Your Wardrobe; the description spells Snyder); Tracy, "I'm 51 years old" (Tracy Campoli); Marie-Anne, captioned "Marian"/"Mariana" (her greeting is captioned "Virtual French fic ladies" and "Bonjour friendship ladies"). Rami Jabali and Chery are not named in their own speech. French Fashion's narrator never says a name (round 2 reads the about text as the persona Valérie) but gives herself a husband, a granddaughter and boots "I bought when Chirac was president". Ageless Confidence's narrator is a nameless first-person hairstylist; one of its two client stories is about a client called **"Diane"** (the same first name as our French channel's persona, likely coincidence).
- **AI disclosure:** none of the 12 descriptions carries an AI disclosure line, including French Fashion (round 2 type ai_avatar) and Elegántica (faceless, generated-looking thumbnails per round 2).
- **AI remarks in comments:** only on n9ICHZq3_tY (Marie-Anne's video about AI channels): 5 viewer comments against AI channels, none calling this video AI. French Fashion has 0 explicit AI remarks; two comments say the pictures do not match the narration ("gardening gloves", 29 likes), and two compliment the presenter's hair as if she were real.
- **Rami RuyOhWfU-RI:** a Russian comment complains about the voice-over ("Озвучка просто из преисподней...лучше бы субтитры."), which suggests a dubbed Russian audio track on the video.
- **chery XCf4o0ZOOiw:** the description's chapter times for mistakes 3 and 4 (3:35, 5:30) do not match where they start in the transcript (2:14, 3:32).
- **French Fashion -eTr9aVSWlM was 8.6 days old** at collection (uploaded 2026-10-19) with 451K views; views rose by 460 between the first pull and the self-check pull later in the same session.
- **Elegántica ratio:** 702 × against the round-2 normal of 1,700 (videos.csv says 647 ×; the views have grown).
- **Elegántica comments:** 8 of the 19 newest comments are versions of the phrase the video asks viewers to type ("Deseo cultivar mi elegancia").
- **Group fit:** n9ICHZq3_tY is in "French angle" as an answer to AI channels, but the AI point is made only in the first 13 seconds; the rest is a 10-essentials list with a long plug for her own shirt line. qwM0s0Q3Rjw and RuyOhWfU-RI are salon consultations with clients, not narrated scripts (no hook, no list, no spoken CTA).
- **Comment pagination quirk:** the "top" continuation token mostly returns the same comments again. Page 2 added 0 new comments on 3 videos (G-RW7ih19Y4, MWQ6T1wURJU, n9ICHZq3_tY) and 1 to 5 on the others. Duplicates were removed by text; each `comments.md` says how many each page added.
- **Captions:** vBsFMkGDbhA has an older caption style with no punctuation or capitals; the notes quote it as is. Several transcripts carry tags ("[music]", "[clears throat]"); word counts in the notes exclude them where stated.
- **Note length:** the notes run about 980 to 1,320 words by `wc -w` (including headings and quotes), above the brief's 500-800 guide; the own-baseline notes run about 850. Nothing was cut so that the quoted evidence stays complete.
- **File writing:** data files (transcripts, comments, meta) were written by `python3 -I` scripts; the 12 notes files were written with shell heredocs, not `python3 -I`.

## Self-checks

1. **Three fresh details calls** (2026-10-28, later in the same session, after all comment pulls):
   - ixlexruRC6c: date, duration (482 s) and likes (16,665) matched; views 1,038,117 then 1,038,157 (+40).
   - -eTr9aVSWlM: date and duration (882 s) matched; views 451,523 then 451,983 (+460), likes 3,581 then 3,583.
   - UTpC6n7KKi0: everything matched exactly (1,048 views, 13 likes, 877 s).
   - The first-pull figures are the ones recorded in meta.md and the notes.
2. **Quote verification.** A `python3 -I` script extracted every double-quoted string in my 12 notes and searched for it, after lowercasing, collapsing whitespace and normalising curly quotes and ellipses, in the video's transcript (timestamps stripped, segments joined), then `comments.md`, then the title, `videos.csv` row, the details record and `meta.md`. It also checked that each `[m:ss]` given before a quote is within 12 seconds of where the quote starts in the transcript.
   - First runs, note by note: 14 strings not found in total. Nine were my own labels in quote marks ("transmits", "over 50/60", "over 50", "older", "most helpful", "same cut", "Paris/Parisian", "Valérie", and "women over 50" from the keywords, which the script does not search); five came from three quotes broken by inner quote marks or a backslash (two comments and one transcript line). All were fixed by removing the quote marks from labels or re-quoting a clean part. No timestamp was off.
   - Final run: 778 quoted strings checked, 0 not found, 0 timestamp offsets over 12 s.
   - Replacement note (Fs17Qc6l8Ug): the same script, extended so that quotes not found in this video's sources are also searched in ixlexruRC6c's transcript (timestamps are checked only against Fs17Qc6l8Ug's own transcript). The first run found 8 strings that failed, from four places where quotes were nested inside quotes; I fixed them by re-quoting clean parts. Final run: 101 quoted strings, 0 not found, 0 timestamp offsets over 12 s.
3. **Username check** (repeated on the replacement's files: only the channel's own handle appears, in meta.md). A search of all my written files for "@" found only channel handles in `meta.md` and one viewer's "@ 10:25" timestamp; a search for 20 commenter handles seen in the raw responses found none (one false match from a regex-like handle).
