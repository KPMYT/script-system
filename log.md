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

### Dale Oakfield's Workshop (UCfAbfnf_riu2GaZHsY_QVmQ) — 31 uploads, 10 collected
- Skipped (user instruction, repeated titles): `a2MSePy9VXw`, `P_iJd8eutB8` ("Do THIS Every Sunday…"); `eNCc5E40-EQ`, `97gygC6SkqU` ("25 'ILLEGAL' Woodworking Money Tricks…").
- Skipped (under 3 minutes): `fRRiu2HMq3c` (0:28).
- Collected: Pdm4mNFDh8M, jhWrUiGVLrk, IrcJeDBBpUU, bvc9i5jmkqw, ZxZfGN4u7zE, JGHTrw1EIW8, PbK8YeMSqWM, bSrj9KXJiLs, jLrejHeAEjM, k4U6Vhv7Luo.
- Normal = 2412. Window views (sorted): 560 ZxZfGN4u7zE, 681 jLrejHeAEjM, 780 m9U74aA0jho, 984 uTckHxaRp5c, 1002 uYqcpaFdjVg, 1007 bvc9i5jmkqw, 1270 bSrj9KXJiLs, **2412 PbK8YeMSqWM**, 3843 tJGZMIwqdTI, 5112 DZF1Gj4ClMI, 7701 s84kicne7ug, 8554 JGHTrw1EIW8, 12544 k4U6Vhv7Luo, 14203 QmjS_XHqxK0, 23374 _9LE-RzHNz8.
- Under 7 days old at collection (views still accumulating): Pdm4mNFDh8M, jhWrUiGVLrk, IrcJeDBBpUU.
- Comments: 14 in total across the 10 videos; 4 videos returned 0 comments (jhWrUiGVLrk, IrcJeDBBpUU, bvc9i5jmkqw, bSrj9KXJiLs). On every video the newest set equals the top set. Target of ~50 top + ~25 newest not reachable. 0 spam skipped.
- Pdm4mNFDh8M transcript re-fetched; identical to the Phase 1 file.

### Hank Hardwood (UCSbHMOqtAX2DvSJl4djytsQ) — 31 uploads, 10 collected
- Upload count: 31, all long-form (no Shorts tab), so the full 10 were available.
- Collected: z1xeeyXsWpU, ZOqZ9E4sFIM, mA0fzSGGN2w, pkb2Ljhg-Mc, F79FvsuExqk, qnn7mRENJ5Q, fqGmsXJR6f0, 5wkjmXYGEZs, ZJE8XMH3s3g, c5Okb4u5ENo.
- Normal = 4305. Window views (sorted): 982 Ui7jSc6lc_I, 1043 ZJE8XMH3s3g, 1518 fqGmsXJR6f0, 1880 9TXV19M0Er8, 2335 c5Okb4u5ENo, 2377 4wJn7sfiAJ4, 2775 oXywmmTIIIU, **4305 8iiFFAL4bvk**, 4373 cGszUvYe1kY, 4440 5wkjmXYGEZs, 4633 G8ePsmj-8ec, 7066 3oUT0Na_X2g, 7376 b3t6MmqfI3c, 7397 se6nDVFmyHk, 7443 PFuT9MlnOSc.
- Under 7 days old at collection: z1xeeyXsWpU, ZOqZ9E4sFIM, mA0fzSGGN2w, pkb2Ljhg-Mc, F79FvsuExqk.
- Comments: 0–7 per video; ZJE8XMH3s3g returned none. NexLev's reported comment totals are sometimes higher than what it returned (e.g. qnn7mRENJ5Q: total 10, returned 6 top / 7 newest), probably replies, which are excluded. One identical comment ("This BOGUS channel…") appears on 9 of 10 videos; kept (not spam by the rule). 0 spam skipped.
- Title of c5Okb4u5ENo ends in " 1" exactly as returned by the API.

### Both channels
- NexLev often returns a comment's like count as a blank string; recorded as 0 likes.
- No comments flagged as from the channel owner.
