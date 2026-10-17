# Log

Every action, every failure, every skipped video and why. Newest at the bottom.

## 2026-10-17 — Phase 1, setup and test

- Created `CLAUDE.md` with the isolation rules and the phase plan.
- Created `inputs/channels.md` with the 2 own channels and 2 competitor links.
- Created folders `data/own/`, `data/competitors/`, `notes/own/`, `notes/competitors/` (empty ones hold a `.gitkeep`).
- NexLev `channel_resolver` on @DaleOakfieldWoodworking → channel ID `UCfAbfnf_riu2GaZHsY_QVmQ`, title "Dale Oakfield's Workshop". OK.
- NexLev `youtube_channel_videos` (newest) → first page returned 30 of 31 uploads (2026-09-17 to 2026-10-15). OK.
  - Channel tabs reported by NexLev: "Videos" only.
  - Most recent long-form: `Pdm4mNFDh8M` "The One Wood Gift That Sells to EVERYONE Even People Who Have Everything", 15:56, 2026-10-15.
  - Noted for Phase 2: `fRRiu2HMq3c` (0:28) is listed in the Videos tab but is under 3 minutes, so it is not long-form.
  - Noted for Phase 2: two titles appear twice with different IDs — "Do THIS Every Sunday and Your Woodwork Sells All Week" (`a2MSePy9VXw` 2026-10-12, `P_iJd8eutB8` 2026-10-03) and "25 'ILLEGAL' Woodworking Money Tricks…" (`eNCc5E40-EQ` 2026-10-11, `97gygC6SkqU` 2026-10-03).
- NexLev `get_bulk_video_transcripts` on `Pdm4mNFDh8M` → success, 375 timed segments, 0:00 to 15:53. Saved to `data/own/dale-oakfields-workshop/Pdm4mNFDh8M/transcript.txt` (one line per segment, `[m:ss] text`). meta.md and comments.md for this video are left for Phase 2.

## 2026-10-17 — Phase 2, own channels

User instructions for this phase: skip the repeated-title videos, ignore the Shorts tab (use the 3-minute rule), no PRE-PIVOT tagging needed (nothing is pre-pivot).

Method (both channels):
- Video lists from NexLev `youtube_channel_videos` (newest). Exact title, upload date/time, duration, views and likes from `youtube_video_details`. Upload dates there are channel-local (-07:00) and are often one day earlier than the dates on the channel list; meta.md uses the `youtube_video_details` date.
- Transcripts: one `get_bulk_video_transcripts` call per channel (10 IDs each). 20 of 20 succeeded, 0 failed.
- Comments: `youtube_video_comments`, sort "top" and sort "newest", top-level only, no usernames. NexLev never returned a second page for any of these videos.
- Normal: median of exact views of the channel's 15 most recent long-form uploads that were at least 7 days old on 2026-10-17 (same exclusions as below).
- Collection was split across two parallel helper agents, one per channel. They briefly shared one scratch file outside the repo; both rebuilt their data from the raw NexLev responses, and I cross-checked all 20 meta.md files afterwards (correct channel, views match the channel lists).

### Dale Oakfield's Workshop (UCfAbfnf_riu2GaZHsY_QVmQ) — 10 collected (channel metadata says 31 uploads; see correction below)
- Skipped (user instruction, repeated titles): `a2MSePy9VXw`, `P_iJd8eutB8` ("Do THIS Every Sunday…"); `eNCc5E40-EQ`, `97gygC6SkqU` ("25 'ILLEGAL' Woodworking Money Tricks…").
- Skipped (under 3 minutes): `fRRiu2HMq3c` (0:28).
- Collected: Pdm4mNFDh8M, jhWrUiGVLrk, IrcJeDBBpUU, bvc9i5jmkqw, ZxZfGN4u7zE, JGHTrw1EIW8, PbK8YeMSqWM, bSrj9KXJiLs, jLrejHeAEjM, k4U6Vhv7Luo.
- Normal = 2412. Window views (sorted): 560 ZxZfGN4u7zE, 681 jLrejHeAEjM, 780 m9U74aA0jho, 984 uTckHxaRp5c, 1002 uYqcpaFdjVg, 1007 bvc9i5jmkqw, 1270 bSrj9KXJiLs, **2412 PbK8YeMSqWM**, 3843 tJGZMIwqdTI, 5112 DZF1Gj4ClMI, 7701 s84kicne7ug, 8554 JGHTrw1EIW8, 12544 k4U6Vhv7Luo, 14203 QmjS_XHqxK0, 23374 _9LE-RzHNz8.
- Under 7 days old at collection (views still accumulating): Pdm4mNFDh8M, jhWrUiGVLrk, IrcJeDBBpUU.
- Comments: 14 in total across the 10 videos; 4 videos returned 0 comments (jhWrUiGVLrk, IrcJeDBBpUU, bvc9i5jmkqw, bSrj9KXJiLs). On every video the newest set equals the top set. Target of ~50 top + ~25 newest not reachable. 0 spam skipped.
- Pdm4mNFDh8M transcript re-fetched; identical to the Phase 1 file.

### Hank Hardwood (UCSbHMOqtAX2DvSJl4djytsQ) — 10 most recent collected (+5 most-viewed, see below)
- Upload count: NexLev channel metadata says 31; the 30 newest are all long-form, so the full 10 were available. (Corrected below: the true count is higher.)
- Collected: z1xeeyXsWpU, ZOqZ9E4sFIM, mA0fzSGGN2w, pkb2Ljhg-Mc, F79FvsuExqk, qnn7mRENJ5Q, fqGmsXJR6f0, 5wkjmXYGEZs, ZJE8XMH3s3g, c5Okb4u5ENo.
- Normal = 4305. Window views (sorted): 982 Ui7jSc6lc_I, 1043 ZJE8XMH3s3g, 1518 fqGmsXJR6f0, 1880 9TXV19M0Er8, 2335 c5Okb4u5ENo, 2377 4wJn7sfiAJ4, 2775 oXywmmTIIIU, **4305 8iiFFAL4bvk**, 4373 cGszUvYe1kY, 4440 5wkjmXYGEZs, 4633 G8ePsmj-8ec, 7066 3oUT0Na_X2g, 7376 b3t6MmqfI3c, 7397 se6nDVFmyHk, 7443 PFuT9MlnOSc.
- Under 7 days old at collection: z1xeeyXsWpU, ZOqZ9E4sFIM, mA0fzSGGN2w, pkb2Ljhg-Mc, F79FvsuExqk.
- Comments: 0–7 per video; ZJE8XMH3s3g returned none. NexLev's reported comment totals are sometimes higher than what it returned (e.g. qnn7mRENJ5Q: total 10, returned 6 top / 7 newest), probably replies, which are excluded. One identical comment ("This BOGUS channel…") appears on 9 of 10 videos; kept (not spam by the rule). 0 spam skipped.
- Title of c5Okb4u5ENo ends in " 1" exactly as returned by the API.

### Both channels
- NexLev often returns a comment's like count as a blank string; recorded as 0 likes.
- No comments flagged as from the channel owner.

## 2026-10-17 — Phase 2 addendum (user request)

- User: Dale and Hank are talking-head AI avatars → all 20 Phase 2 meta.md files tagged `Format: FACE (AI-avatar talking head)` plus `Selection: 10 most recent long-form uploads`.
- User: also take Hank's top 5 most-viewed, which were a different format (classic faceless) → tagged `Format: FACELESS (classic faceless format)`.
- **Correction:** NexLev `youtube_channel_videos` (sort popular) on Hank lists uploads from July–August 2026 that were not on the first page of the newest-sorted list. NexLev's "31 uploads" channel metadata is therefore wrong; the channel has more uploads. The same may apply to Dale (first page also ended with a continuation token). The 10-most-recent selections and the normals are unaffected (both use the newest-sorted order).
- Note: dates on NexLev channel lists for older videos are approximate ("1 month ago" → 2026-09-17, "2 months ago" → 2026-08-17). meta.md always uses the exact date from `youtube_video_details`.
- Top 5 most-viewed long-form (none overlap the 10 most recent; all ≥ 12 min):
  - `KLit5xVATG4` "7 Tiny Wood Projects I CAN'T Make Fast Enough — They SELL OUT!" — 2026-07-14, 13:35, 87,929 views, 20.42× normal
  - `zPS80HAofPs` "Stores THROW OUT Pallets — Here's How I Sell Them for THOUSANDS" — 2026-08-22, 15:30, 51,954 views, 12.07× normal
  - `Hv7e4kwUNgk` "7 Ways to Turn FREE Pallet Wood Into Big Money" — 2026-07-18, 14:31, 46,354 views, 10.77× normal
  - `DJGPsg-N670` "25 FREE Pallet Projects That Can Build You a REAL Business" — 2026-08-02, 14:04, 29,239 views, 6.79× normal
  - `FBSLO4DO-bQ` "10 Woodworking Side Hustles That Can Make You $5,000 a Month" — 2026-07-12, 12:40, 28,669 views, 6.66× normal
- Ratios use the same channel normal (4305), which is computed from the recent avatar-format uploads.
- Transcripts: one bulk call, 5 of 5 succeeded (405 / 423 / 433 / 387 / 351 segments, each running to within ~3 s of the video's end).
- Video descriptions on these five carry a "NEW BOOK" link (hankhardwood.com) and a long "Credits" list naming other channels (e.g. KLit5xVATG4's list includes BeardedVikingWoodWorks).
- Comments (20 per NexLev page): kept top/newest = KLit5xVATG4 26/20 (API count 72), zPS80HAofPs 14/15 (24), Hv7e4kwUNgk 13/13 (16), DJGPsg-N670 6/6 (7), FBSLO4DO-bQ 15/15 (24). 0 spam skipped.
  - Only KLit5xVATG4 returned continuation tokens, and paging was unreliable: top pages 2–4 added 3, 3 and 0 new comments; newest pages 2–3 repeated page 1. Stopped there. API counts likely include replies (excluded).
  - The channel owner's pinned book-promo comment is kept with a `[channel owner]` prefix on KLit5xVATG4, Hv7e4kwUNgk, FBSLO4DO-bQ.
  - Kept as not spam (judgement calls): a viewer linking their own YouTube Short (Hv7e4kwUNgk); an off-topic rant and a timestamped summary comment (FBSLO4DO-bQ); two near-identical comments with different IDs (Hv7e4kwUNgk).

## 2026-10-17 — Phase 3, competitors

User confirmed full transcripts must be collected and stored for future use. Check of all 25 own-channel transcripts: each runs to within 1–5 s of the video's end (2,335–3,817 words each).

Method: same as Phase 2 (NexLev only). One helper agent per competitor, each with its own scratch folder outside the repo. Selection: Group A = 5 most recent long-form (Videos tab, ≥ 3:00); Group B = 5 most-viewed long-form published on/after 2024-10-17, skipping any already in Group A. Exact dates from `youtube_video_details` (NexLev list dates for older videos are approximate). Normal = median of exact views of the 15 most recent long-form uploads at least 7 days old. FACE/FACELESS by the user's definitions; basis recorded in each meta.md. I re-checked both medians and that no author handles or channel IDs appear in any comments.md.

### BeardedVikingWoodWorks (UCsWLcxLC1B-MLCeIpYtPiMw) — 10 collected, folder `bearded-viking-woodworks`
- Format: FACE. Basis: NexLev `check_faceless_channel` isFaceless=false (0.98, "tutorial"); about text describes his own build videos; transcripts narrate his own builds in first person; comments react to his appearance.
- Group A (recent): `_L70uEXtGfc` (2026-10-11, 6 days old), `l_mOoZNuuDg`, `TwM0Wtfhako`, `AopDfSQj2FI`, `_vzgcQ-1hhQ`.
- Group B (most-viewed, last 24 months): `aOh10QByJp0` (rank 2), `oDZB7UsqMHo` (4), `7r2281_Jin8` (5), `5wxFNCfgcPQ` (6), `C-oLqfdSsRM` (7). Skipped as already in Group A: rank 1 `_vzgcQ-1hhQ`, rank 3 `AopDfSQj2FI`.
- Normal = 73,108 (15 uploads up to 2026-10-04; 16th `RVOOoPNkPMk` 2026-05-05 outside). Window views: 18485, 24935, 52681, 54747, 55158, 67345, 72723, **73108** (`_yP3R04q5N0`), 103597, 223359, 248823, 406585, 669365, 924656, 2877107.
- Transcripts: 10/10, English auto-captions, each ends within 5 s of the video's end. The bulk call's output was too large to display inline; it was saved to a file and read in full.
- Comments: 20–39 top, 19–20 newest per video. Paging: page 2 usually repeated page 1 exactly; stopped per rule. API comment counts 97 to "1K". 1 spam skipped (contact-me opener on `aOh10QByJp0`).
- No videos under 3:00 encountered.

### WhosTheVoss (UCejaHizj8RLiP7bPDv6v0tg) — 10 collected, folder `whosthevoss`
- Format: FACE. Basis: `check_faceless_channel` isFaceless=false (0.97, "tutorial"); about text describes tutorials with free plans; transcripts film his own builds ("look how close my face is", "cut all of these out on camera"); comments mention his on-camera presence.
- Group A (recent): `0lk5SY97KnI` (2026-10-10, exactly 7 days), `aaQRt6CAFik`, `z9gYuMQyHbo`, `ZIUYmkpHgP8`, `Tyrb9pNre6w`.
- Group B (most-viewed, last 24 months): `6gmjCVaRfjY` (rank 1), `64alAPtMfFw` (2), `mCZZDfP7s2o` (3, 2024-10-27 — inside the window), `arNIvR7AXVE` (4), `i-mjhZz7OZU` (5). No overlap with Group A (first Group A video is popular rank 6), so no replacements.
- Normal = 232,499 (15 uploads 2026-07-04 to 2026-10-10; 16th `gBbATzrGB9g` 2026-06-27 outside). Window views: 95484, 101592, 134713, 174515, 177333, 183215, 208586, **232499** (`Tyrb9pNre6w`), 263843, 355687, 401159, 759717, 931227, 1933143, 2314838.
- Transcripts: 10/10, English auto-captions. Three end more than 10 s before the video ends: `Tyrb9pNre6w` (16 s), `mCZZDfP7s2o` (16 s), `64alAPtMfFw` (24 s). Each ends on a sign-off line ("See you later.", "…go build one", "…it works."), so the gap is probably outro without speech; noted in their meta.md.
- Comments: 20–35 top, 19–20 newest per video; same paging behaviour. 1 spam skipped (video-editing services pitch on `z9gYuMQyHbo`). Kept as not spam (judgement calls): offers of a design app, a quote tool and machine-shop work; a religious comment. One `[channel owner]` comment on `mCZZDfP7s2o`. On `6gmjCVaRfjY` NexLev gave the comment total and one like count as "1K"; recorded as given.

### Both competitors
- Comment totals reached: well under the ~50 top target on every video (NexLev paging returns repeated pages). Newest ~20 per video (target ~25).
