# Round 3 collection log: helper H6 (model scripts)

Date: 2026-10-28. Videos: the 10 rows of `models/approved-models.csv` with helper = 6 (M16, M17, M18, M19, M24, M25, M28 real presenters; F02, F06, F07 faceless or AI channels, collected as structure-only models). Method: `study-brief.md`, "Round 3" and "Rules added after the round 3 check". Written only to `data/<slug>/<video_id>/`, `notes/<slug>__<video_id>.md` and this file. Scripts kept in the session scratchpad (`h6/`), run with `python3 -I`. No git commands run.

## NexLev calls: 45 of 55

| Tool | Calls | Notes |
|---|---|---|
| youtube_video_details | 10 + 3 self-check = 13 | all succeeded |
| get_bulk_video_transcripts | 1 | 10 IDs, 10 of 10 returned (all "English (auto-generated)"). The result was too large to show and was saved by the harness to a file, then parsed with `python3 -I`; not a failure |
| get_video_transcript | 0 | not needed |
| youtube_video_comments | 31 | top + newest for all 10 (20); top page 2 for the 9 videos with a normal top token (9); r58VDhcsdYo: 1 retry of sort=top and 1 continuation call (2), see below |
| **Total** | **45** | no errors, no limit or credit messages |

Data files were built from the tool results as logged in this session's transcript (exact text, no hand copying); comments were de-duplicated by comment ID.

## Videos collected (10 of 10, all with transcripts)

| Model | Channel | Video | Upload date | Views | ÷ normal | Duration | Transcript | Comments shown / collected |
|---|---|---|---|---|---|---|---|---|
| M16 | Angela Masson - Fashion Over 50 | creI37QkUMs | 2026-01-22 | 253,628 | 3.96 (64,000) | 17:59 | yes, 413 seg | 1.4K / 39 |
| M17 | Darlene Obiyan | iJZEsuGk3sA | 2026-05-17 | 266,707 | 9.88 (27,000) | 22:43 | yes, 529 seg | 515 / 45 |
| M18 | Capsule Closet Stylist | Rg_YiVy40fk | 2025-12-07 | 98,658 | 28.19 (3,500) | 13:21 | yes, 363 seg | 211 / 43 |
| M19 | Beth Djalali | Hionkf3pHJc | 2026-05-17 | 158,326 | 7.92 (20,000) | 16:01 | yes, 442 seg | 321 / 36 |
| M24 | Diana GOSS | 6Yz0BKoKG-M | 2025-06-26 | 541,064 | 12.58 (43,000) | 18:11 | yes, 487 seg | 441 / 45 |
| M25 | Marnie Goldberg | r58VDhcsdYo | 2022-10-04 | 2,838,735 | 34.62 (82,000) | 17:44 | yes, 461 seg | 7.9K / 20 |
| M28 | Aliceinparis | saDURZc-pno | 2025-12-10 | 118,369 | 4.23 (28,000) | 14:51 | yes, 296 seg | 390 / 30 |
| F02 | Vivian Sinclair | tSfgNEUXh8U | 2026-08-08 | 321,228 | 49.42 (6,500) | 26:58 | yes, 629 seg | 499 / 39 |
| F06 | Emiko Sato | 5lCfaBWShOE | 2026-10-13 | 2,413,996 | 16.31 (148,000) | 16:08 | yes, 374 seg | 1K / 45 |
| F07 | Ageless Glamour | 060ynhA72T8 | 2025-04-21 | 1,097,485 | 9,627 (114) | 7:07 | yes, 83 seg | 169 / 34 |

Normals are from `models/approved-models.csv` (taken from `round2/channels-all.csv`); views ÷ normal uses the exact views from the first details call. Missing transcripts: none. Swaps needed for missing transcripts: none.

## Things the main session may want to decide

- **F07, 060ynhA72T8 (Ageless Glamour) is mostly not narrated talking advice.** Narration runs only 0:00-2:38 (about 438 words of generic hacks, no age said); the rest of the 7:07 is music with "[Music]" and "Heat." captions, reading as a music-only slideshow. Comments cite timestamps in the silent part about "the model", and about half the newest comments are in Portuguese, Spanish, German or French. Meta, comments and a short note were written; the note carries a format flag.
- **All seven M rows have real presenters on camera** as far as the transcripts and comments show (first-person speech, personal stories, comments addressing them by name; no AI remarks on any M video).
- **F02 and F06 are AI personas by the comments' account**: Vivian Sinclair 7 AI or lip-sync remarks (top one 104 likes); Emiko Sato 4 (top one 423 likes, "I thought they had to disclose AI."). Neither description has an AI disclosure line.
- **M25, r58VDhcsdYo comments**: NexLev's sort=top returned the newest-first page (its continuation token reads get_newest_first). One retry and the continuation call returned the same 20 comments. So this video has only 20 comments, in newest order, and no relevance-ranked list; `comments.md` and `meta.md` say so.
- **M28, saDURZc-pno**: 11 spam comments for two replica-goods sellers were skipped (they were 11 of the 20 newest), so only 9 newest remain.
- **F06 topic**: hygiene and body odour after 40, not hair or fashion (consistent with "a topic the real models don't cover"). Its channel normal rests on 8 uploads.
- **M24 has no age in speech** (petite or average height is the audience); M17 and M28 also say no age number; M18 says "over 50" once though its description says over 60.

## Presenter types as heard

- M16: female, unnamed in speech, "Finally, in my 50s", lives in The Villages. M17: "I am Darlene", "I am by no means a stylist". M18: "my name's Michelle Barrow. I've been a personal stylist for 26 years" (description hashtag spells Barrett). M19: unnamed in speech, "Style at a Certain Age", 5 foot 8. M24: unnamed in speech except her Instagram handle, a son mentioned. M25: "my name is Marnie", "just under six months away from turning 50", Chico's brand ambassador. M28: unnamed in speech, "Bonjour, I am French", lives in Paris.
- F02: "My name is Vivian Sinclair", "I ran a boutique for 40 years" (her other studied video says "40 years beside a fitting room mirror"); several formula lines recur across the two videos ("There is no neutral.", "this is where beauty does not expire, it evolves"). F06: "I'm Emiko. I'm Japanese. I'm 48, and for 22 years, I worked behind a beauty counter in a department store in Tokyo." Twice says "In America, we". F07: unnamed "we" channel, no gender or background stated.

## Oddities

- Sponsorships: M24 Petite Studio (spoken "4th of July sale" vs August sale dates in the description); M28 Sleep and Glow pillow (description says "this video is sponsored"); M19 is all Quince with affiliate links and "I put my own name on", no sponsorship statement; M16, M17 and M25 carry affiliate links.
- M19's description says "Eleven pieces"; the speech shows ten. M17's description contains a leftover drafting line ("You can put this right under a section in your description like:"). M28's description says "© 2024" on a 2025 upload. F06's speech dates the Shiseido study 1999, the description 2001.
- F02's transcript ends mid-sentence at 26:56. F06's details title has no closing quote mark.
- M25 uses the older caption style (no punctuation or capitals); quoted as is. Several transcripts carry "[music]" tags inside sentences (M17, M19); quotes avoid the tags or split around them.
- Comment pagination quirk as in other helpers: top page 2 added 0 new comments on 4 videos (creI37QkUMs, Hionkf3pHJc, tSfgNEUXh8U, 060ynhA72T8) and 2-11 on the others.
- One comment on tSfgNEUXh8U was signed with an initial and surname; the signature was replaced with "[name removed]" (no other text changed).
- One 1-like Marnie comment wishes harm ("I hope ya hair falls out!"); kept as pushback, not spam.
- Note length: the notes run about 960 to 1,570 words by `wc -w` (including headings and quotes), above the brief's 500-800 guide, similar to H1's; nothing was cut so the quoted evidence stays complete.

## Self-checks

1. **Three fresh details calls** (after all comment pulls):
   - 5lCfaBWShOE: date, duration (968 s) and title matched; views 2,413,996 then 2,414,076 (+80); likes 22,419 then 22,420.
   - r58VDhcsdYo: everything matched exactly (2,838,735 views, 53,505 likes, 1,064 s, 2022-10-04).
   - 060ynhA72T8: everything matched exactly (1,097,485 views, 9,432 likes, 427 s, 2025-04-21).
   - The first-pull figures are the ones recorded in meta.md and the notes.
2. **Quote verification.** A `python3 -I` script extracted every double-quoted string in the 10 notes and searched for it (lowercased, whitespace collapsed, curly quotes, dashes and ellipses normalised) in the video's transcript (segments joined, timestamps stripped), then `comments.md`, then `meta.md`. For each quote with a timestamp written next to it (`[m:ss] "..."` or `"..." (m:ss`), it checked that the timestamp is within 3 seconds of the start of the segment where the quote begins.
   - First runs, note by note: 8 strings not found (three of my own labels in quote marks, such as over 50 and Americans do wash there; three quotes that crossed a music tag, including a last-40-words quote; one quote with a height mark inside it, which split into two strings) and 11 timestamp offsets over 3 seconds (mostly from reading a pasted transcript view one segment late; three were ambiguous price strings such as "$32" matched at their first occurrence). All were fixed by re-quoting clean parts, removing quote marks from labels or prices, or correcting the timestamp.
   - Final run: 710 quoted strings checked, 0 not found, 0 timestamp offsets over 3 s.
3. **Username check.** A script compared all 373 commenter handles seen in the raw responses against every file I wrote: 0 matches. A search for "@" found only the channels' own handles in `meta.md`, Diana Goss's contact address in her description notes, and the header word "@handles" in each `comments.md`.
