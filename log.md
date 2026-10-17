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
