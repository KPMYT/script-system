# Recent uploads, 2026-11-05: every plumbing channel, Scarlett and Diane

The operator asked: "kindly audit each of our latest scripts across all plumbing channels and transcribe for me please. same goes for the style scripts so diane and scarlett".

**Scope:** every upload since the last review (`recent-uploads-2026-10-29/`, the day the session 13 plumbing rules went on the account) on Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter and Werner Finkbeiner, and on Scarlett Starling and Diane de Chambray. That is 33 videos. **Left out:**
- two long compilations: Mark's `Ey5HCL2lCqk` (2:20:48) and the Vintage Pipefitter's `yVwCoTug6d4` (2:50:14)
- Werner's `kZ09VQIqAS4`, already reviewed on 2026-10-29

**Method:** as in the two earlier upload reviews.
- Upload lists from NexLev `youtube_channel_videos` (newest first) on 2026-11-05.
- Captions from `get_bulk_video_transcripts` / `get_video_transcript`.
- The scanner was run on timestamp-stripped copies, and every transcript was read against the pack, the persona profile, the core rules and the operator's decisions in `HANDOFF.md` §3 (plumbing 2026-10-29; style 2026-10-29, session 14).
- One helper per channel. A second helper then re-checked a sample of each audit's quotes and counts against the transcripts (`audits/CHECK.md`).

**Cautions:**
- **The transcripts are YouTube's automatic captions of the voiceover,** so they record what the voice said, in the caption system's own spelling and punctuation. They are not the scripts the VAs pasted in, which aren't in this repo. Sentence and question counts taken from caption punctuation are approximate.
- **No channel of the operator's is connected to NexLev,** so there is no retention data. Views are public counts at collection time, and the newest videos are hours old.
- **Publish dates are NexLev's,** worked out from YouTube's "x days ago", so they can be a day off.

Findings only: nothing in the library changed because of this folder. Proposed fixes wait for the operator's yes.

## Files

| File | What it is |
|---|---|
| `transcripts/<channel>-<videoId>.txt` | The caption text, joined into lines of about 30 seconds, each starting with its timestamp. Words exactly as captioned. |
| `audits/<channel>.md` | The audit of each video on that channel, then the channel's patterns and top fixes. |
| `audits/<channel>-table.csv` | One row per video: length, words, words a minute, the 12-minute check, first item, opening promises, rule breaks, verdict. |
| `audits/CHECK.md` | The second helper's re-check of a sample of quotes and counts. |
| `SUMMARY.md` | The main session's summary across all six channels. |
