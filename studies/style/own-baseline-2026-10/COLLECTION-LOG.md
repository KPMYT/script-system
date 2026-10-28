# Collection log: own-channel baseline, October 2026

Collector: research helper (Phase 1 of `studies/style/study-brief.md`). Date: 2026-10-28, about 03:25-04:30 UTC. Tools: NexLev only. No web search, no git. Files were written only inside `studies/style/own-baseline-2026-10/`.

## What ran

| Step | Tool | Calls | Result |
|---|---|---:|---|
| Video lists | `youtube_channel_videos` (sort newest) | 2 | Scarlet 25 videos, Diane 13. No continuation token, so each list was complete in one page. Both channels show only a "Videos" tab (no Shorts). |
| Faceless check | `check_faceless_channel` | 2 | Both `isFaceless: false` (Scarlet 0.96 from cache, Diane 0.98 fresh). Full result in `SUMMARY.md`. |
| Video details | `youtube_video_details` | 38 + 3 re-pulls | All 38 returned. Exact views, likes, `lengthSeconds` and `publishDate` were taken from here. |
| Transcripts | `get_bulk_video_transcripts` | 5 (2 + 10 + 10 + 10 + 6 IDs) | 38 of 38 successful, all on the "English (auto-generated)" track. Each response was too large to return inline, so the session saved it to a local tool-results file. The transcripts were written from those files by a script. `get_video_transcript` was not needed. |
| Comments | `youtube_video_comments` | 76 (38 × top, 38 × newest) | No call returned a continuation token, so every video's comments fit in one page per sort. 57 top-level comments in total (Scarlet 47, Diane 10), of which 15 are the channels' own link comments. |

## Failures and retries

- No tool call failed and none needed a retry.

## Data quirks recorded as found (data not altered)

- **Listing vs details.** `youtube_channel_videos` gives rounded views ("2.7K") and dates estimated from relative text. Every listed date was 1-8 days later than the details `publishDate`. Only details values are used.
- **Upload dates before the stated start.** Four Scarlet and three Diane uploads have publish dates before 2026-09-28 (earliest 2026-09-20 and 2026-09-22). They are recorded as returned.
- **Channel title.** YouTube's channel title for @ScarletSterlingYT is "Scarlet Starling". The narration and descriptions say "Scarlet Sterling".
- **Comment counts.** The shown `commentsCount` includes replies. On w6w_ktMBHXM, 16 are shown and 15 top-level comments were returned; the 16th is a reply. The tool returns `replyCount` but cannot fetch reply text, so that reply is logged as not retrievable in `comments.md`. On EVFmbo51Ou0, the top call reported a count of 0 while returning 1 comment, and the newest call reported 1. On qmYPg0L3qZU, the top sort returned 1 comment and the newest sort returned 2 (the owner's link appeared only under newest). Pulling both sorts on every video covered this.
- **Comment dates** are the tool's conversion of YouTube's relative text ("2 weeks ago"), so they are approximate. A blank `likesCount` (" ") is recorded as 0.
- **`hasCaption` is false** on all 38 videos, yet auto-generated transcripts were returned for all of them.
- **Auto-caption errors** are kept as transcribed. Examples: Diane's name as "Diana Shambre", "Deand Chambre", "Deian Chambre" and "Diane Dechambre"; "À bientôt" as "Abento" and "Abian too"; "the liquor's on" in ISAL4NBlshQ at 9:40; "The The rule" in bkUBVNvN4NY.
- **Descriptions.** 22 uploads (the newer ones) include a line stating the presenter is "a fictional character with an AI-generated name, face, and voice". 20 of those say "He is not a real person" and 2 say "She". 16 older uploads have no such line. Each `meta.md` records which applies.

## Processing

- `transcript.txt`: one line per caption segment as `[m:ss] text`. The time is `startMs` floored to whole seconds; whitespace inside a segment is collapsed. Segments overlap in time (rolling captions), but their text does not repeat: only 4 of 15,889 segments open with three words found in the previous segment. Segment counts are in each `meta.md`.
- Word counts are whitespace-separated tokens across all segments. Words per minute = words ÷ (`lengthSeconds` ÷ 60).
- `comments.md`: comment text and likes only, with no usernames or channel IDs. The channel's own comments are tagged [OWNER]. Line breaks inside a comment are shown as " / ". No comments were removed as spam: none looked like spam, though some commenters' account names resemble other style channels (names not stored).
- The age in days runs from the details `publishDate` to 2026-10-28 03:30 UTC.
- **Normal.** Scarlet: the 15 most recent of 20 qualifying uploads (5:00+, at least 7 days old), from 3t_q9UrMctk (2026-10-19) back to se0NK3SdI0I (2026-10-01), median 532. 85nTTAPzBeM, at 6.9 days old, falls just short of 7 days. Diane: all 13 uploads qualify, so fewer than 15 are available and the median of all 13 is used: 607.
- **Notes.** The top 4 and bottom 3 by views among uploads at least 7 days old, per channel. Segment start times and word counts come from a script that sums words between anchor lines in `transcript.txt`; the hook is everything before the first item. "you / I / we" figures count pronoun forms (you, your, you're...; I, me, my, I'm...; we, us, our...).
- **Note length.** The notes run about 780-910 words each (counted with headings), above the ~400-600 target. The extra length comes from the required quoted items: six emotion quotes, reassurance and shaming quotes, CTA wording and the last ~40 words.

## Self-checks

1. **Re-pulled details** for ISAL4NBlshQ, 3JBVSs9ETu4 and kWzjIzbdB00. Publish dates, durations, views and likes all matched the first pull exactly (3,826/9; 157/9; 1,093/7).
2. **Quote verification.** A `python3 -I` script extracted every double-quoted string in the 14 notes and searched for it, after lowercasing, collapsing whitespace and normalizing curly quotes, in that video's transcript text (timestamps stripped, segments joined), then in `comments.md`, then in the title and `meta.md`. It also checked that every `[m:ss]` or `(m:ss)` attached to a quote lies within 12 seconds of where the quote starts in the transcript.
   - First run: 11 quoted strings were not found. They were my own section labels put in quotes, or two quotes that I had joined with "...". There were also 3 timestamps off by 14-17 seconds.
   - All were fixed by removing the quote marks from the labels, splitting the joined quotes, and correcting the timestamps.
   - Final run: 614 quoted strings checked, 0 not found, 0 timestamp offsets over 12 s.
3. **Username check.** A search for "@" and for the commenter handles seen in the raw responses found nothing in any written file.

## Not done or out of scope

- Reply text (the tool can't fetch it), retention, CTR and other analytics: no NexLev tool covering them was called for these channels.
- No judgments, scripts or library edits.
