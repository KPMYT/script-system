# Collection log: helper H2 (round 3, script and comment study)

Collected 2026-10-28. Videos: the 11 rows of `inputs/videos.csv` with helper = 2 (rows 1, 2, 6, 12, 16, 18, 20, 23, 26, 32, 37), on 8 channels: mm-personal-styling, diana-goss (3), chic-over-60, alice-luxe (2), woman-in-midlife, vivian-sinclair, anniepicks, trends-spotted-fashion-timeless-and-agel.

Files written: `data/<channel_slug>/<video_id>/meta.md`, `transcript.txt`, `comments.md` for all 11; `notes/<channel_slug>__<video_id>.md` for all 11; this log. Helper scripts and raw page captures are in the scratchpad (`round3-h2/`), outside the repository.

## Calls used: 40 of 60

| # | Tool | Target | Result |
|---|---|---|---|
| 1-11 | youtube_video_details | each of the 11 videos | ok |
| 12 | get_bulk_video_transcripts | 10 IDs (all but HG2OJ0O3lxg) | ok, 10 of 10 successful |
| 13 | get_video_transcript | HG2OJ0O3lxg (the 11th; bulk takes 10) | ok, 378 segments |
| 14 | youtube_video_comments top | gfbWOw00Y-M | ok, 20 |
| 15 | youtube_video_comments top + token | gfbWOw00Y-M | returned the same 20 comments (20 of 20 repeats) |
| 16 | youtube_video_comments newest | gfbWOw00Y-M | ok, 20 |
| 17-18 | comments top, newest | eKCl-bRx8wg | ok, 20 + 20 |
| 19 | comments top + token | eKCl-bRx8wg | 19 of 20 already on page 1 (reordered), 1 new |
| 20-37 | comments top, newest | the other 9 videos | ok, 20 + 20 each |
| 38-40 | youtube_video_details (self-check) | YLiz8tlx9g4, 2q_6Qf69Ywc, CkVrghocoPs | ok |

No `youtube_channel_videos` call was needed: all 8 channels have a normal in `round2/channels-all.csv`.

## Failures, swaps and deviations
- Failures: none. No limit or credit errors.
- Missing transcripts: none. No swaps needed.
- Deviation: the brief asks for one more page of top comments when a continuation token comes back. Every video returned a token, but on the first two videos the token gave the same page (20/20, then 19/20 repeats; the HVAC study saw the same). The extra top page was therefore dropped for the remaining 9 videos (9 calls saved). Each `comments.md` says which case applies.
- Comment counts collected: gfbWOw00Y-M 39 unique (20+20), eKCl-bRx8wg 40 (21+20), 2IkhtemG-MM 32, CkVrghocoPs 32, 2e50uMLaCtE 39 (1 spam skipped), aaDZuD5jIfs 25 of 37 shown (1 off-topic political comment skipped), 9ZNV79Uva3g 38, NMvN5bjcwks 39, 2q_6Qf69Ywc 40, YLiz8tlx9g4 36 (1 product-spam skipped), HG2OJ0O3lxg 37.
- No usernames stored. Channel-owner comments are marked [OWNER] (4 videos have one pinned owner comment). Where comment authors' display names read like other channels (CkVrghocoPs, aaDZuD5jIfs, YLiz8tlx9g4), the comments are kept and this is described without the names.
- Notes run about 900-1,150 words including headings and quotations, above the brief's "about 500-800"; the extra is mostly quoted text.

## Self-check
1. Three fresh details calls (calls 38-40) against the first pull: titles, durations and upload dates identical; no AI disclosure in any of the three descriptions.
   - YLiz8tlx9g4: views 1,013,945 then 1,013,950 (+5); likes 22,280 both.
   - 2q_6Qf69Ywc: views 910,914 then 910,946 (+32); likes 13,147 then 13,148.
   - CkVrghocoPs: views 490,793 then 490,830 (+37); likes 3,704 then 3,703.
   meta.md keeps the first-pull figures.
2. Quote check (`python3 -I check_quotes.py`): every double-quoted string in the 11 notes files searched (case and whitespace normalised) in that video's transcript, comments file or title. 573 quotes, 573 found, 0 missing.
3. Timestamp check (`check_ts.py`): every "[m:ss] "quote"" line in the notes compared with the segment where the quote starts; after fixes, all within 10 seconds.

## Things that look odd (described, not judged)
- Vivian Sinclair (2q_6Qf69Ywc): the narrator says "My name is Vivian Sinclair" and claims "40 years beside a fitting room mirror". Six comments call the presenter AI or fake ("Is this lady AI? Uh, yes!", 302 likes; one asks for transparency in the description) and about eight point to a lawn-product logo appearing in the visuals, even on the glasses (top comment, 514 likes). Round 2 typed this channel faceless_narrated from thumbnails; the comments describe an on-screen presenter. No AI disclosure in the description.
- Alice Luxe (both videos): no AI disclosure in the descriptions; round 2 found the about text states AI voiceovers. Both scripts share the same closing line ("if you enjoyed watching this video you will definitely love this next one") and the same problem/solution beats.
- MM Personal Styling: captions spell the presenter "Melissa Morel"; the title says Melissa Murrell. A second woman (Amy) appears in one item.
- Diana GOSS: no name said in any of the three transcripts; viewers address her as Diana. The jeans video (9ZNV79Uva3g, Body shape group) says no viewer age and no over-50 wording; its tags say "Style over 40". The captions render "voilà" as "Ebola" in two endings.
- Woman in midlife (2e50uMLaCtE): the title says she coloured her gray hair; the video shows one test strand, and she asks viewers whether to go further. No name or age is said.
- TRENDS SPOTTED FASHION (HG2OJ0O3lxg): the video is about a real woman, Inès de la Fressange, named in speech and the description. Comments mention "your French accent" and two complain about the translated audio ("Very bad French interprétation").
- AnniePicks (YLiz8tlx9g4): names Meryl Streep, Carolina Herrera and the Princess of Wales as examples. A commenter praises "the dove gray and blush pairing", which is not in the video.
- Chic Over 60 (2IkhtemG-MM): one commenter says she followed the channel's glasses video and "that was a disaster".
- Group fit: all 11 match their groups by topic.
