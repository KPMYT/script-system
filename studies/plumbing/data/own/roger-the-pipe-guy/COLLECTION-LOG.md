# Collection log — Roger the Pipe Guy (own)

Collected 2026-10-20 by a helper agent following `studies/plumbing/study-brief.md`. NexLev MCP tools only. Collect and describe only.

## Channel

- Channel ID: UCR2C--KENITllxSo1aAbWWA (handle @RogerthePipeGuy)
- URL: https://www.youtube.com/channel/UCR2C--KENITllxSo1aAbWWA
- About (youtube_channel_about): "Sharing DIY plumbing Advice So Your Drains Never Clog Again". 76.2K subscribers, 9,509,350 total views, joined 2023-12-27, 221 videos (about page). One link: "100 Old House Fixes" (rogerthepipeguybooks.com).
- Slug / group: roger-the-pipe-guy / own

## Method

1. `youtube_channel_videos` sorted newest and sorted popular (first page each, 30 videos). All needed videos were on the first pages: Group A, the 15-video normal window plus one spare, and the popular top 5, all dated after 2024-10-20. No continuation pages needed.
2. Long-form = 3:00 or longer and not a Short. Every listed video is 15:00–30:32, so none were excluded for length.
3. Exact dates, views, likes and durations from `youtube_video_details` for all 10 study videos, the skipped video, and all 16 window videos (15 plus a spare).
4. Transcripts: `get_bulk_video_transcripts` (one call for the original 10, one retry for 3GMK8QAmagA plus its replacement). All are English auto-generated. Written as `[m:ss] text`, one line per segment.
5. Comments: `youtube_video_comments`, sort "top" and sort "newest". Top-level only; text and like counts only; usernames dropped; obvious spam skipped.
6. Format: `check_faceless_channel`, the about text, the video descriptions, the transcripts and the comments (see below).

## Group A — 5 most recent long-form uploads

| # | Video ID | Title | Upload (exact) | Duration | Views | Likes | Views / normal |
|---|---|---|---|---|---|---|---|
| 1 | E3p1V2wiQDc | 10 Secrets To a Clog-Free Drain ALL Winter (EASY DIY) | 2026-10-19 07:45 -07:00 | 17:57 | 801 | 15 | 0.30 |
| 2 | nxb3nS21zgg | $1 Homemade Drain Cleaner That Actually Unclogs Every Drain! | 2026-10-17 03:00 -07:00 | 18:58 | 1881 | 30 | 0.70 |
| 3 | 8BZZwj93dkQ | I Tried Everything to Unclog My Drains — This Finally Worked! | 2026-10-16 07:00 -07:00 | 16:31 | 6599 | 46 | 2.45 |
| 4 | ihZc3VGeG6c | How To Use Hydrogen Peroxide To Get Rid Of Smells, Rings and Clogs! | 2026-10-14 04:00 -07:00 | 18:24 | 2103 | 39 | 0.78 |
| 5 | n-2hjVGsu-Q | 9 Cheap Toilet Tricks That Make Every Plumber Visit Look Like a Scam | 2026-10-13 08:30 -07:00 | 24:50 | 2101 | 36 | 0.78 |

**Skipped:** 3GMK8QAmagA, "12 Signs Your Plumber Is Doing A LAZY Job (Costing You THOUSANDS)" (2026-10-15 08:42 -07:00, 19:13, 2881 views, 19 likes). Bulk transcripts returned `{"msg": "Not Available"}` on the first call and again on a retry. Replaced by the next most recent long-form upload, n-2hjVGsu-Q.

## Group B — 5 most-viewed long-form uploads published on/after 2024-10-20

None of these is in Group A, so no popular-order skips were needed.

| Popular rank | Video ID | Title | Upload (exact) | Duration | Views | Likes | Views / normal |
|---|---|---|---|---|---|---|---|
| 1 | WfAwg1l0xCE | 5 Things You Should NEVER Pour Down Your Drain | 2026-02-14 09:44 -08:00 | 18:24 | 1217431 | 29403 | 452.91 |
| 2 | YjPAVZAffh0 | Why Plumbers' Own Drains Never Clog — The $2 Monthly Habit They Don't Advertise | 2026-06-20 12:00 -07:00 | 18:44 | 977201 | 27067 | 363.54 |
| 3 | Rkm2BnFL9FA | Pour Hydrogen Peroxide Into Your Toilet Tank Tonight and Watch What Happens | 2026-07-01 12:00 -07:00 | 23:09 | 492833 | 9591 | 183.35 |
| 4 | hebGJ43lQ6s | In 45 Years of Plumbing, I've Never Had a Clogged Drain — Here's Exactly What I Do | 2026-04-30 12:00 -07:00 | 19:04 | 456616 | 7757 | 169.87 |
| 5 | kHT6ZL8At0w | 1 Cup of This Destroys Every Drain Clog — But Never Touches Your Pipes | 2026-07-23 12:00 -07:00 | 21:37 | 451172 | 10100 | 167.85 |

## Channel normal

**Normal = 2688**: the median of exact views of the 15 most recent long-form uploads at least 7 days old on 2026-10-20 (published on or before 2026-10-13). Exact views from `youtube_video_details`:

| # | Video ID | Upload (exact, -07:00) | Views |
|---|---|---|---|
| 1 | n-2hjVGsu-Q | 2026-10-13 08:30 | 2101 |
| 2 | oh_jTNw1sjs | 2026-10-10 13:00 | 6790 |
| 3 | R-hbXQFUrzQ | 2026-10-09 12:00 | 2688 |
| 4 | eeM7RjlKbA0 | 2026-10-09 03:30 | 2816 |
| 5 | qyvLwKZuUAk | 2026-10-07 22:30 | 1928 |
| 6 | zO-vXxXafdQ | 2026-10-07 07:00 | 8042 |
| 7 | 1i8TevJix6g | 2026-10-05 06:45 | 2110 |
| 8 | L7QAYvm1_M8 | 2026-10-03 12:00 | 25414 |
| 9 | 8eiXxw4uPV4 | 2026-10-02 15:00 | 3724 |
| 10 | WWjzsYKWEV0 | 2026-10-01 08:30 | 1602 |
| 11 | h3pwIHvb2UQ | 2026-09-30 03:45 | 4080 |
| 12 | 1yHlNYHxeS4 | 2026-09-28 22:30 | 2134 |
| 13 | zYpiPIgktRM | 2026-09-28 11:45 | 2336 |
| 14 | GPxlrjpARPY | 2026-09-28 06:15 | 1997 |
| 15 | NvGBqCyPA1Q | 2026-09-27 08:45 | 4709 |

Sorted: 1602, 1928, 1997, 2101, 2110, 2134, 2336, **2688**, 2816, 3724, 4080, 4709, 6790, 8042, 25414 → median 2688.

Boundary note: n-2hjVGsu-Q is exactly 7 days old by calendar date and was counted, as ages are counted in days. If it were excluded on time of day, the window would take the next upload, TcEDI8WibS4 (2026-09-26, 3968 views), and the median would be 2816. n-2hjVGsu-Q is also a Group A video. That is allowed: the window and the groups are separate.

## Format: FACELESS (recorded basis)

- **NexLev `check_faceless_channel`** (cached, analysed 2026-10-20T07:53Z): isFaceless = **false**, confidence 0.96, format "tutorial", tags DIY / home improvement / how-to / education. **This result does not match the other evidence and the operator's expectation. It is recorded here, not overridden silently.**
- **Video descriptions:** 7 of the 10 study videos (E3p1V2wiQDc, 8BZZwj93dkQ, ihZc3VGeG6c, YjPAVZAffh0, Rkm2BnFL9FA, hebGJ43lQ6s, kHT6ZL8At0w) end with a "Credits:" or "Credits to the footage:" list of 20–70 other YouTube channels, e.g. @thisoldhouse, @rogerwakefield, @got2learn, @homerepairtutor. This points to compiled third-party b-roll. WfAwg1l0xCE, nxb3nS21zgg and n-2hjVGsu-Q have no credits list.
- **Transcripts:** a single first-person narrator ("I'm Roger", "In 45 years of plumbing…"; WfAwg1l0xCE says "three decades"). The narration never says where he is or that he is on camera. On-screen references are limited to the book QR code and, in n-2hjVGsu-Q, a before/after toilet image ("Look at the toilet on the left…"). Bracketed auto-caption marks ("[clears throat]", "[snorts]", "[gasps]") appear in several videos. WfAwg1l0xCE contains the spoken line "Continuing with the final sections now".
- **Comments:** "I'm not buying any of this as you never see Roger the pipe guy in his videos. You never see him actually working on a clogged pipe." (WfAwg1l0xCE); "'Roger' sure sounds like a text to speech lol" (YjPAVZAffh0, 129 likes); "This artificial voice is so dehumanizing" (kHT6ZL8At0w); "Is this a human speaking?" (WfAwg1l0xCE); "thanks morgan freeman voice lol" (hebGJ43lQ6s).
- **Conclusion recorded:** FACELESS, a veteran-plumber persona voiceover over compiled b-roll, as the operator expected. NexLev's classifier disagrees.

## Comments collected

| Video ID | API commentsCount | Top kept | Newest kept | Unique total | Spam skipped |
|---|---|---|---|---|---|
| E3p1V2wiQDc | 2 | 1 | 1 | 1 | 1 (book promo, same comment in both lists) |
| nxb3nS21zgg | 1 | 0 | 0 | 0 | 1 (book promo; only comment) |
| 8BZZwj93dkQ | 1 | 0 | 0 | 0 | 1 (book promo; only comment) |
| ihZc3VGeG6c | 2 | 1 | 1 | 1 | 1 (book promo) |
| n-2hjVGsu-Q | 2 | 0 | 0 | 0 | 1 (book promo; API returned only 1 of 2) |
| WfAwg1l0xCE | 1.1K | 28 | 20 | 47 | 0 |
| YjPAVZAffh0 | 1.1K | 20 | 20 | 40 | 0 |
| Rkm2BnFL9FA | 208 | 20 | 19 | 35 | 1 (off-topic political) |
| hebGJ43lQ6s | 190 | 20 | 19 | 33 | 1 (off-topic political) |
| kHT6ZL8At0w | 431 | 20 | 19 | 37 | 1 (off-topic political) |

Totals: 110 top + 99 newest kept = 209 entries, 194 unique comments; 8 spam skipped. "Newest" lists mark any comment also in the top list with "[also in top]".

Short of the brief's ~50 top / ~25 newest because of the pagination fault below. Group A videos have almost no comments (1–2 each).

Spam pattern: the same "book Rogue Remedies by Ruth Vance" promotion appears, in near-identical wording, as the only or top comment on all five Group A videos. Kept but noted: three comments recommending a named service company ("ars/rescue rooter" ×2 in YjPAVZAffh0 and kHT6ZL8At0w; "American Residential Services" ×1 in hebGJ43lQ6s). They read as possible promotion but are on-topic.

## Failures and API oddities

- **Transcript unavailable:** 3GMK8QAmagA returned "Not Available" twice (see Group A).
- **Comment pagination is unreliable:** continuation tokens mostly return the same comments. WfAwg1l0xCE top pages 2 and 3 added 7 and then 1 new comment. YjPAVZAffh0 top page 2 was identical to page 1. WfAwg1l0xCE newest page 2 was identical to page 1. Paging was stopped after that, and the other videos got one page per sort (up to 20 each).
- **Like counts:** the top sort gives YouTube-rounded values (e.g. "1.5K", "2K"). Most newest-sort entries have a blank like count, recorded as 0 per the brief.
- **List dates are approximate and bunched:** the newest listing shows 11 videos as 2026-09-29 ("3 weeks ago"); exact dates run 2026-09-26 to 2026-09-30. Several list dates are a day off the exact date (e.g. nxb3nS21zgg listed 2026-10-18, exact 2026-10-17). The popular list shows "2026-07-20" for videos whose exact dates are 2026-06-20 and 2026-07-01.
- **List durations** differ from `lengthSeconds` by about a second (e.g. WfAwg1l0xCE "18:25" listed, 1104 s = 18:24). Durations in this study use `lengthSeconds`.
- **Video counts disagree:** the about page says 221 videos; the newest-list metadata says "31"; the popular-list metadata says "0".
- **Repeated titles in the newest list:** "I BET Your Toilet Is Leaking RIGHT NOW…" (DxPENg2w_po, H91eD8U7r7E), "Pour Hydrogen Peroxide Into These 7 Drains Tonight…" (pio9TQl-JZU, u64p2RtdNlc) and "One Cup of This Clears ANY Slow Drain Overnight…" (aL8tzFjpfow, uqGiwiN1Xig) each appear twice, with different IDs and lengths. None is in the study set.
- `youtube_video_details` reports `hasCaption: false` and category "Entertainment" for every video, yet auto-generated English transcripts were returned for all but one.
- **ihZc3VGeG6c:** the narration jumps mid-sentence at [4:36] ("Week four, it's gone and that water evaporates and the plug is gone") with no gap in the timestamps. A later line refers to "that P trap I showed you", which never appears in the transcript.
- Comment publish dates from the API are derived from relative text ("3 months ago") and are not exact. They are not used.

## Files written

- `data/own/roger-the-pipe-guy/<video-id>/meta.md`, `transcript.txt`, `comments.md` for the 10 videos above
- `notes/own/roger-the-pipe-guy__<video-id>.md` for the 10 videos
- This log
