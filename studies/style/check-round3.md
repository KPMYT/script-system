# Style study: round 3 check (2026-10-28)

An independent checker re-checked two videos per collector against fresh NexLev pulls made on 2026-10-28, about 07:00-07:15 UTC, roughly half an hour to an hour after collection. Every existing file was only read; this is the only file written. Tools: `youtube_video_details`, `get_video_transcript`, `youtube_video_comments`, `youtube_channel_videos`. No web search. **NexLev calls: 37 of the 45 allowed:**
- 8 details
- 8 transcripts
- 17 comment pages (15 first pages plus 2 continuation pages)
- 2 channel lists
- 2 details for the exact view counts of the median videos

Scratch work (compare scripts, comment picks, the handle list used for the privacy search) is in `/tmp/claude-0/-home-user-script-system/a46e4e64-c9ae-55b0-aafb-8c468f9ffa04/scratchpad/check-r3/`.

**Sample** (four real, four faceless or AI; three are copycat-pair videos):

| Collector | Real | Faceless / AI |
|---|---|---|
| H1 | `ixlexruRC6c` Marie-Anne Lecoeur | `UTpC6n7KKi0` Ageless Confidence (Pair B, the copy) |
| H2 | `2e50uMLaCtE` Woman in midlife | `YLiz8tlx9g4` AnniePicks |
| H3 | `WgkP3h4QWpg` MAKEOVERGUY | `YeKT0zkdIrw` Chic After 60 (Pair C, the winner) |
| H4 | `vFul5tvg1Cw` Justin Hickox | `K6N1EFo7oec` Age with Style (Pair A, the re-upload) |

## Summary

| Video (collector) | 1 meta vs fresh details | 2 transcript (10 lines) | 3 comments (5 picked) | 4 notes (6 claims) | 5 no usernames |
|---|---|---|---|---|---|
| ixlexruRC6c (H1) | pass | pass | pass (5/5) | pass (3 timestamps 3-4 s early, within tolerance) | pass |
| UTpC6n7KKi0 (H1) | pass | pass (full file, 389/389) | pass (1/1, the only comment) | **fail** (3 timestamps 6-9 s early) | pass |
| 2e50uMLaCtE (H2) | pass | pass | pass (5/5) | pass | pass |
| YLiz8tlx9g4 (H2) | pass | pass | pass (4/5, 1 not returned) | **fail** (hook word count) | pass |
| WgkP3h4QWpg (H3) | pass | pass | pass (5/5) | pass (1 flag: CTA timestamp) | pass |
| YeKT0zkdIrw (H3) | pass | pass (full file, 675/675) | pass (5/5; 1 found only on top page 2) | pass | pass |
| vFul5tvg1Cw (H4) | pass | pass | pass (5/5) | **fail** ("about 600 words in" is ~910) | pass |
| K6N1EFo7oec (H4) | pass | pass (full file, 465/465) | pass (5/5) | pass | pass |

| Channel normal | `round2/channels-all.csv` | Recomputed (list values) | Exact median video | Result |
|---|---|---|---|---|
| Woman in midlife | 5,300 | 5,300 (JlWXM85ehtQ) | 5,367 | pass |
| Age with Style | 3,800 | 3,800 (9Q7c1ZwSZgY) | 3,846 | pass |

**Counts by check:**
- Meta: 8 pass.
- Transcripts: 8 pass. 80 sampled lines all identical, and the 3 files compared by script match in full.
- Comments: 8 pass. 36 picks: 35 found with identical like counts, 1 not returned by paging, 0 wrong.
- Notes: 5 pass, 3 fail. 48 claims checked: 43 pass, 3 fail, 2 pass with a flag.
- Privacy: 8 pass.
- Normals: 2 pass.

All failures sit in the notes, and all are small: one wrong word count, one hook figure about 11% high, and one note with three timestamps 6-9 s early. Meta, transcripts and comments are faithful to fresh pulls, and no data looks invented.

## 1. meta.md against fresh `youtube_video_details`

Titles, upload dates and durations match exactly on all 8. Likes are identical or +1/+2. Views moved only by normal growth. Age at collection and views ÷ normal were recomputed from the meta figures, and all 8 match.

| Video | Title | Date | Duration | Views (meta → fresh, diff) | Likes (meta → fresh) | Age / ratio recomputed |
|---|---|---|---|---|---|---|
| ixlexruRC6c | ✓ | 2025-08-17 ✓ | 482 s ✓ | 1,038,117 → 1,038,164 (+47) | 16,665 → 16,665 | 436.5 d ✓ / 12.36 ✓ |
| UTpC6n7KKi0 | ✓ | 2026-07-16 ✓ | 877 s ✓ | 1,048 → 1,049 (+1) | 13 → 13 | 103.5 d ✓ / 2.56 ✓ |
| 2e50uMLaCtE | ✓ | 2025-06-18 ✓ | 443 s ✓ (7:23; videos.csv says 7:24) | 629,078 → 629,109 (+31) | 5,747 → 5,748 | 497 d ✓ / 118.7 ✓ |
| YLiz8tlx9g4 | ✓ | 2024-10-19 ✓ | 406 s ✓ | 1,013,945 → 1,013,945 (0) | 22,280 → 22,280 | 739 d ✓ / 1,325.4 ✓ |
| WgkP3h4QWpg | ✓ | 2026-08-28 ✓ | 566 s ✓ | 2,395,153 → 2,395,270 (+117) | 26,462 → 26,464 | 60.4 d ✓ / 70.4 ✓ |
| YeKT0zkdIrw | ✓ | 2025-09-15 ✓ | 1789 s ✓ | 960,045 → 960,072 (+27) | 11,622 → 11,622 | 407.6 d ✓ / 25.9 ✓ |
| vFul5tvg1Cw | ✓ | 2024-07-09 ✓ | 607 s ✓ | 3,222,185 → 3,222,226 (+41) | 45,699 → 45,699 | 841 d ✓ / 63.18 ✓ |
| K6N1EFo7oec | ✓ | 2025-11-22 ✓ | 1127 s ✓ | 7,133 → 7,133 (0) | 132 → 132 | 340 d ✓ / 1.88 ✓ |

The other meta lines checked against the fresh records also hold:
- Channel IDs.
- No AI disclosure in any of the 8 descriptions.
- K6N1EFo7oec's unfilled "[Insert Channel Link Here]".
- UTpC6n7KKi0's description, which opens with the literal word "DESCRIPTION".
- The Justin Hickox sponsor line.

## 2. Transcripts

There was one fresh `get_video_transcript` pull per video.
- **Compared by script in full (3 videos):** UTpC6n7KKi0, YeKT0zkdIrw and K6N1EFo7oec. The pulls were large enough to be saved to disk. Using the collectors' format (`[m:ss]` from `startMs`, whitespace collapsed), segment counts match (389, 675, 465) with 0 differing lines.
- **Compared by eye (5 videos):** the other five pulls were shown inline, so 10 lines were checked by eye. These were lines 1-3, five lines spread at 1/7 steps, and the last 2.

| Video | Lines checked | Result |
|---|---|---|
| ixlexruRC6c | 1-3, 20, 40, 60, 80, 100, 120, 137-138 | all identical (e.g. 60 "[3:28] wearing. Instant pop. Without the"; 138 "[8:00] video on screen") |
| UTpC6n7KKi0 | full file | 389/389 identical |
| 2e50uMLaCtE | 1-3, 26, 52, 78, 104, 130, 181-182 | all identical (e.g. 78 "[2:52] you're stuck with it. In the back, we"; 182 "[7:16] [Music]") |
| YLiz8tlx9g4 | 1-3, 24, 49, 74, 98, 123, 172-173 | all identical (e.g. 74 "[2:55] reminiscent of a fine glass of red wine") |
| WgkP3h4QWpg | 1-3, 33, 67, 101, 135, 169, 236-237 | all identical (e.g. 67 "[2:35] [music] my forehead is high. My weight") |
| YeKT0zkdIrw | full file | 675/675 identical |
| vFul5tvg1Cw | 1-3, 45, 90, 135, 180, 225, 314-315 | all identical (e.g. 180 "[5:28] is also the reason that I didn't want to") |
| K6N1EFo7oec | full file | 465/465 identical |

## 3. Comments

**Method:**
- 5 comments per file were drawn with `random.seed(20261028)` from the parsed entries of each `comments.md`. Duplicates marked "[also in top]" were excluded so that no comment was drawn twice.
- Each pick was looked for in fresh `top` and `newest` first pages.
- Where a pick was missing, one continuation page of `top` was tried.
- "Not returned" means the comment was absent from every page NexLev gave. That shows nothing against the collector, because the top ranking reshuffles between calls.

| Video | Found, likes match | Not returned | Notes |
|---|---|---|---|
| ixlexruRC6c | 5: 415, 420 (top); 0, 1, 0 (newest) | 0 | |
| UTpC6n7KKi0 | 1 of 1: "Thank you 🙏 / I just turn 67..." (1) | 0 | fresh `commentsCount` 1, no continuation token, as the log says. Only 1 call made |
| 2e50uMLaCtE | 5: 177, 17, 29 (top); 1, 1 (newest) | 0 | |
| YLiz8tlx9g4 | 4: 9 [OWNER], 352, 110 (top); 1 (newest) | 1: "(0 likes) Recommending this to everyone I know." | absent from top pages 1 and 2. Page 2 returned 15 of page 1's comments again |
| WgkP3h4QWpg | 5: 144, 86, 9 (top); 0, 0 (newest) | 0 | |
| YeKT0zkdIrw | 5: 27, 7, 2 (top p1); 40 (top p2: "All beautiful and classic colours; however I do miss seeing a belt..."); 1 (newest) | 0 | |
| vFul5tvg1Cw | 5: 1K, 171 (top); 0, 0, 0 (newest) | 0 | the comment the file skips as spam ("free 3rd tuff tuff 4th 55xx.xx 5") is in the fresh newest page, so the skip is confirmed |
| K6N1EFo7oec | 5: 0, 0 (top); 0, 0, 0 (newest) | 0 | all five are answers to the "where are you watching from" ask |

Totals: 36 picks, 35 found with identical like counts, 1 not returned, 0 wrong. Owner flags match: [OWNER] on the AnniePicks pinned link and the Marie-Anne Lecoeur and Justin Hickox pinned comments, and `authorIsChannelOwner` is false on every other pick.

## 4. Notes: six claims per video

Quotes were searched for by script in the transcript, ignoring case and punctuation and skipping `[music]`-type tags. Word counts were recounted as spoken words with tags excluded, so they run a few words under the collectors' totals, which count tags.

**Timestamp tolerance used:** a quote counts as correctly placed if its time is within 5 s of the line where the quote starts. Being later than that line is allowed, as in the HVAC check. In this round the H1 notes run the other way: they cite the line *before* the quote. Up to 5 s early passes; 6 s or more fails.

### ixlexruRC6c (H1): pass

| # | Claim | Check | Result |
|---|---|---|---|
| 1 | Hook "0:00-0:13, about 30 words" | 29 words to "fabulous, and chic." | pass |
| 2 | First item "lands at 0:13" | "The first thing that" is on the [0:13] line | pass. The line also says "about 26 words in", where the count is 29 (26 is the word count before the [0:13] line), so the note's two hook figures disagree slightly |
| 3 | "7 items" | baggy, closed necklines, beige, clumpy shoes, twee prints, untucked tops, hairstyles | pass |
| 4 | Feeling "[2:48] you disappear faster than a macaron at a Parisian cafe" | at [2:48] | pass. Three other feeling lines cite the line before: [2:22] is at 2:26, [3:35] at 3:39, [4:30] at 4:33 (3-4 s, within tolerance) |
| 5 | CTA "No like, subscribe or comment request is spoken anywhere"; end-card pointer 7:51 | "subscribe" 0, "comment" 0, "like" as a request 0; "watch the video on screen" at [7:59] closes the 7:51 block | pass |
| 6 | Comments "Disagreement with tucking, 4" | file entries 12, 15, 17, 23 | pass. Also "old lady" said 10 times: 10 in the transcript |

### UTpC6n7KKi0 (H1): fail (3 timestamps)

| # | Claim | Check | Result |
|---|---|---|---|
| 1 | Hook "0:00-2:08, about 360 words" | 364 words before "Secret number five" | pass |
| 2 | First item "at 2:08 ('Secret number five')" | "Secret number" ends the [2:08] line | pass |
| 3 | "5 items" | secrets five to one, counted down | pass. Also "60 is said 8 times (over 60: 3, after 60: 5)": 8 = 3 + 5 |
| 4 | Feeling "[0:54] My hair used to be so full..." | at [0:54] | pass |
| 5 | CTA "3:13: 'If that just made you rethink your part, hit subscribe now'" and "6:19: 'Quick pause...'" | "If that just made you" starts at [3:19]; "Quick pause." is its own line at [6:28] | **fail**, 6 s and 9 s early. The structure map uses the same wrong boundaries ("subscribe and comment request 3:13", "'Quick pause' ... 6:19") |
| 6 | Comments "1 collected; YouTube shows 1" | fresh `commentsCount` 1, the same comment, 1 like | pass |

**FAIL: the timestamps.**
- The feeling "[0:21] 'she looks tired before she's even left the house'" starts at [0:28] ("and she looks tired before she's even"), 7 s early.
- The 3:13 CTA is at 3:19, 6 s early.
- The 6:19 CTA is at 6:28, 9 s early.

H1's own self-check accepted offsets up to 12 s, which is why these passed there.

### 2e50uMLaCtE (H2): pass

| # | Claim | Check | Result |
|---|---|---|---|
| 1 | Hook "0:00-0:21, about 65 words" | 66 words to "I don't feel great" ([0:16]-[0:18]) | pass |
| 2 | First concrete step "lands at 2:20, about 480 words in" | "So, let's address the not wanting to ruin..." at [2:20], 480 words | pass |
| 3 | Not a list; the colorist speaks "2:20-3:37" | the colorist's turn runs [2:20] to [3:40] ("just going to look a little"), then her voice-over "When she was doing this test strand" | pass |
| 4 | Feeling "[3:46] you know the fear of I am never going back" | starts at the end of [3:47] | pass |
| 5 | CTA "No subscribe or like ask in speech. The ending is the open question." | "subscribe" 0; no like request; "should I put color around my face?" at [7:07]-[7:09] | pass |
| 6 | Comments "keep the white, do nothing, about 24 of 39" | about 17 of 19 top plus about 6 of 20 newest, so 22-23 by my reading | pass (rough count) |

### YLiz8tlx9g4 (H2): fail (hook word count)

| # | Claim | Check | Result |
|---|---|---|---|
| 1 | Hook "0:00-0:47, about 135 words"; first item "about 135 words in" | 121 spoken words to "let's jump right [Music] in"; "in our first combination" starts at [0:46], 122 words in | **fail**: about 11% high |
| 2 | First item "at 0:47" | [0:46] | pass |
| 3 | "7 items" | first to seventh combination; matches the description chapters | pass |
| 4 | Feeling "[0:39] great style has no age limit" | "great" ends the [0:36] line, the rest is [0:39] | pass |
| 5 | CTA "One CTA, at 6:25" plus the last 40 words | "subscribe" 1 (at [6:32]); the CTA block begins [6:23]-[6:28]; the last 40 words match the transcript | pass |
| 6 | Comments: "Six newest comments come from accounts whose names read like other over-50/60, senior or story channels" | six such display names in the fresh newest page | pass. Also "over 50" once: 1; "youthful" 3 times: 3 |

**FAIL:** the hook figure. The note's own segment counts add up to the transcript total (1,047), so about 13 words of item one are filed under the hook. Item one, "~129", runs to about 139 when counted from 0:46. Either the hook is "about 120 words (0:00-0:46)" or the boundary needs to be stated.

### WgkP3h4QWpg (H3): pass (1 flag)

| # | Claim | Check | Result |
|---|---|---|---|
| 1 | Cold open "0:00-0:37, about 95 words" | 100 words to "this next phase." (tags excluded) | pass |
| 2 | First analysis "at 2:45, about 455 words in" | "If you really [music] want to know" at [2:45], about 463 words in | pass |
| 3 | Six elements "paid in order" (body, head, hair, face, color, style) | body [3:11], head [4:39], hair [4:53], face [5:15], color [6:19], style [6:29] | pass |
| 4 | Feeling "[7:49] I feel like I was back 20 years at least how I used to look." | "I feel" ends the [7:49] line | pass |
| 5 | CTA "6:35: 'Please help us continue offering this free content...'" | the CTA block starts at [6:35] ("Creating and sharing this experience"); the quoted sentence is at [6:47] | pass with a **flag** (the time is the block start, 12 s before the quoted words) |
| 6 | Comments "The husband, about 9"; "Missing Christopher, about 6" | husband: exactly 9 (408, 295, 90, 86, 75, 18, 12, 0, 0); missing Christopher or the channel: 4 explicit plus 3 "where have you been" type, so 6 is fair | pass. Also "69" three times, all by the client: 3 |

### YeKT0zkdIrw (H3): pass

| # | Claim | Check | Result |
|---|---|---|---|
| 1 | Hook "0:00-1:22, about 220 words" | 222 words before [1:22] | pass |
| 2 | First pairing "at 3:07, about 470 words in" | "first combination" at [3:07], 469 words before | pass |
| 3 | "Eight items"; olive and ivory short, going "straight to 'Gold jewelry works beautifully with this pairing'" | 8 pairings; the gold line at [22:13], 8 s into the 22:05 item | pass |
| 4 | Feeling "[1:15] age doesn't limit beauty. In fact, it gives it a new kind of power." | the quote starts at [1:17] | pass |
| 5 | CTA "No CTA until 29:32: 'don't forget to like it, share it with a friend, and subscribe...'" | at [29:32]; "subscribe" said once in the whole video; "comment" 0 | pass |
| 6 | Comments "Eleven of the 43 come from accounts named like style or over-60 channels" | 11 entries tagged `[account named like a style channel]` | pass. Also "after 60 / over 60 / at 60 six times": 2 + 3 + 1 = 6 |

### vFul5tvg1Cw (H4): fail (1 word count)

| # | Claim | Check | Result |
|---|---|---|---|
| 1 | Hook "0:00-0:31, 136 words" | 136 words to "this works on everyone" | pass |
| 2 | "First numbered step lands at 3:26 (about 600 words in)" | "step number one" at [3:28]; 908 words before [3:26], about 911 before the phrase | **fail** (word count) |
| 3 | "5 items" | step numbers one to five at 3:28, 4:59, 5:50, 6:48, 8:22 | pass |
| 4 | Feeling "[6:37] almost get you two three maybe even a month worth of growout" then "[6:41] I'm saving you money right now" | at [6:37] and [6:41] | pass |
| 5 | CTA "9:43 'want to say a big thank you to lifean for sponsoring this video ... there is a link in the description'. No subscribe or comment ask in speech." | at [9:43]; "subscribe" 0; "comment" once, as "one of the comments that I'm going to get" | pass |
| 6 | Comments "the crown and final styling not shown (3, e.g. 113 likes 'Felt like a cliff-hanger.')" | 113, 48, 12 (plus one garbled 0-like comment that may mean the same) | pass |

**FAIL:** the note's own segment list gives hook 136 + sponsor 79 + prep 407 + rough-drying 286 = 908 words before step one. "About 600 words in" contradicts it.

### K6N1EFo7oec (H4): pass

| # | Claim | Check | Result |
|---|---|---|---|
| 1 | Hook "0:00-0:39, 103 words" | 103 words before [0:39] | pass |
| 2 | First mistake "at 0:50, 'Mistake number one, the too boxy blouse', about 140 words in" | at [0:50], 141 words in | pass |
| 3 | "7 items" | seven "Mistake number" items | pass |
| 4 | Feeling "[1:33] more like you've simply pulled on a sack" | at [1:35] | pass |
| 5 | CTA "0:43 and 18:38: the location question"; "18:07: 'which mistake are you going to stop making first? ... Let me know in the comments below.'" | [0:43], [18:38], [18:07] and [18:18] | pass |
| 6 | Comments "the answer to the location question (24 of 29)"; "AI or fake remarks: 1" | 17 top plus 7 unique newest = 24; one "we are not AI perfect older people" (0) | pass. Also "One number: 'women over 60'": "60" occurs once. The note's "three months after" the 1.1M upload checks out: 6byOPawCepI was uploaded 2025-08-23 |

## 5. No commenter usernames

**Pass on all 8 videos**, in all 32 files (meta, transcript, comments and notes).
- **Handle search:** 65 commenter handles taken from the fresh pulls (at least 5 per video; none are reproduced here) were searched across the 32 files, with 0 hits.
- **"@" search:** the only "@" hits are:
  - the channel's own handle in each `meta.md`
  - the sponsor handle quoted from the Justin Hickox description
  - the "@[handle removed]" placeholder text
- **Other identifiers:** the only `UC…` IDs are the channels' own, in `meta.md`. There are no author fields.
- **Names marked, not stored:** comments from accounts named like style channels are marked `[account named like a style channel]` (H3) or described (H2) without the names. The six such accounts in the AnniePicks newest page, and the 11 on YeKT0zkdIrw, are not named anywhere.

Observation: in the Justin Hickox pinned owner comment, the two business e-mail addresses (`info@…`, `dionna@…`) were turned into "info@[handle removed]" by the handle filter. This is over-redaction of the channel owner's public contact details. It is harmless and not a commenter name.

## 6. Channel normals

**Method:**
- Make a fresh `youtube_channel_videos` call (sort newest, page 1).
- Take the 15 most recent uploads that are 5:00 or longer and at least 7 days old on 2026-10-28.
- Sort them by list views, then pull the median video's exact views.

**Woman in midlife (UC1exmI_KJ-zXoKQAdhhzc3Q): 5,300, pass.**
- Excluded:
  - gFTq3n-d7-g (6 days old)
  - pxz-KIcgNBc (4:37)
  - 9l3xpadSWMY (3:39)
  - gu73sQ5m5CE (3:24)
- The window runs SSLACoXEOgE … Y5pldXprA4o (list positions 2-19).
- Sorted list values: 855, 1.2K, 2.4K, 2.6K, 2.7K, 4.3K, 4.7K, **5.3K**, 6.1K, 7.1K, 7.6K, 8.2K, 16K, 16K, 16K.
- The median is JlWXM85ehtQ, exact **5,367**. Its neighbours, 4.7K and 6.1K, cannot cross it.

**Age with Style (UCsiBzifgu6vwRubtmdIcOzA): 3,800, pass.**
- Excluded as under 7 days old:
  - M3EjfOhCnX0 (1 day)
  - jldm9wZF-kc (3 days)
  - QR1EO8Vzcnk (5 days)
- The window runs gHxLJ7cGn3U (8 days) … 0WOnKVJtrH0. All are 13:16 or longer.
- Sorted: 947, 1.0K, 1.3K, 1.9K, 2.4K, 3.0K, 3.6K, **3.8K**, 3.9K, 3.9K, 5.3K, 5.8K, 6.6K, 6.7K, 6.8K.
- The median is 9Q7c1ZwSZgY, exact **3,846**. The neighbours (3.6K and 3.9K) cannot cross: list values are cut off, not rounded, so 3.9K is at least 3,900.

Both recomputed medians equal the round-2 figures. The exact pulls show something the round-2 notes miss: NexLev's list counts are **truncated, not rounded** (5,367 is shown as "5.3K" and 3,846 as "3.8K"). Round-2 normals therefore run up to about 2% low against the brief's "median of exact views". On the two sampled videos the effect is small:
- 2e50uMLaCtE: 118.7× becomes 117.2×.
- K6N1EFo7oec: 1.88× becomes 1.85×.

This is not a collector error; the brief told collectors to take normals from `round2/channels-all.csv`.

## Summary of failures

1. **vFul5tvg1Cw notes (H4), Structure map line 11:** "First numbered step lands at 3:26 (about 600 words in)". It is about 910 words in: 908 words before [3:26], which is also what the note's own segment counts add up to.
2. **YLiz8tlx9g4 notes (H2), Structure map lines 7-9:** the hook is given as "about 135 words" and the first item as "about 135 words in". The count is 121 words before "in our first combination" at [0:46], and item one is about 139 words, not ~129.
3. **UTpC6n7KKi0 notes (H1):** three timestamps are 6-9 s early.
   - Feelings, line 20: "[0:21] 'she looks tired before...'" should be [0:28].
   - CTAs, line 47: "3:13" should be 3:19.
   - CTAs, line 48: "6:19" should be 6:28.
   - The same 3:13 and 6:19 boundaries appear in the Segments line (line 10).

**Flags (pass, but worth a touch):**
- WgkP3h4QWpg notes, line 45: "6:35:" is the CTA block's start. The quoted "Please help us continue offering..." is at [6:47].
- ixlexruRC6c notes, lines 21-23: three feeling times cite the line before the quote, 3-4 s early ([3:35] should be 3:39, [4:30] should be 4:33, [2:22] should be 2:26). Line 7, "about 26 words in", disagrees with the hook's "about 30 words" (29 counted).

## Other findings (not in the checks)

1. **A high-liked comment missing from a fresh top page.** ixlexruRC6c `comments.md` top #15 is "I disagree with tucking in blouses..." at 1.1K likes, which would be the video's most-liked comment. It is not on the fresh top page 1, whose highest-liked comment has 798 likes. It was not one of the five picks, so it was not chased further. It is the same pattern as the 214-like comment in the HVAC check: unverified, not disproved. The note cites it as "the most-liked comment".
2. **The AnniePicks `comments.md` header (line 9)** says "5 of the newest come from accounts whose display names read like other over-50/60, senior or story channels ... (6 counting the last)". The note says six. The fresh newest page shows six such accounts, and one of them praises "the dove gray and blush pairing", which is not in the video. The header should simply say 6.
3. **Timestamp habits differ by collector.** H1 tends to cite the line before a quote, up to 9 s early; H3 and H4 cite the quote's own line or the block start. H1's self-check allowed 12 s, H2's 10 s. A single rule in the brief (for example, the start of the quote, within ±3 s) would make checks mechanical. The HVAC check made the same recommendation.
4. **Word-count method differs.** Some collectors count bracketed tags and ">>" as words, others do not. For example, for WgkP3h4QWpg the meta says 1,392 words including tags, the note says about 1,340, and I count 1,292 spoken words. Notes should say which method they use, as H3's log does.
5. **Paging.** Continuation pages mostly repeat page 1: AnniePicks page 2 repeated 15 of its 20. One pick was found only on YeKT0zkdIrw top page 2. This is the fault already logged, not a collector error.

## Fixes recommended (for the main session; nothing was changed here)

1. `notes/justin-hickox__vFul5tvg1Cw.md` line 11: change "(about 600 words in)" to "(about 910 words in)".
2. `notes/anniepicks__YLiz8tlx9g4.md`, lines 7-9:
   - "Hook: 0:00-0:47, about 135 words" becomes "Hook: 0:00-0:46, about 120 words".
   - "First item at 0:47 ..., about 135 words in" becomes "First item at 0:46 ..., about 122 words in".
   - In Segments, "hook 0:00 (~135); blue with white or gray 0:47 (~129)" becomes "hook 0:00 (~122); blue with white or gray 0:46 (~139)".
3. `notes/ageless-confidence__UTpC6n7KKi0.md`:
   - Line 20, [0:21]: change to [0:28].
   - Line 47, "3:13:": change to "3:19:".
   - Line 48, "6:19:": change to "6:28:".
   - Line 10, Segments: "subscribe and comment request 3:13" becomes 3:19, and "'Quick pause' ... 6:19" becomes 6:28.
4. Optional touch-ups:
   - `notes/makeoverguy__WgkP3h4QWpg.md` line 45: change "6:35:" to "6:47:", or write "6:35 (block start; the ask at 6:47)".
   - `notes/marie-anne-lecoeur-the-french-chic-exper__ixlexruRC6c.md` lines 21-23: [3:35] becomes [3:39], [4:30] becomes [4:33], [2:22] becomes [2:26]. Line 7: "about 26 words in" becomes "about 29 words in".
5. `data/anniepicks/YLiz8tlx9g4/comments.md` line 9: change "5 of the newest ... (6 counting the last)" to "6 of the newest ...".
6. Brief, for later rounds:
   - Set one timestamp rule (the start of the quote, ±3 s).
   - Set one word-count rule (spoken words; tags excluded).
   - Note that NexLev list views are truncated, so normals should either use exact pulls for the median video or say "list values".
7. Optional: check whether the 1.1K "I disagree with tucking in blouses" comment on ixlexruRC6c can be re-found. If not, soften "the most-liked comment" in its note to "1.1K at collection".
