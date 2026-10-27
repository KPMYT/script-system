# HVAC script and comment study

A study of the scripts and comments of proven HVAC videos, for the Roger the HVAC Guy pack (`hvac-scripts`, to be built from `plumbing-scripts`). Asked for by the operator on 2026-10-27 ("9 - yes please very imp", answering `drafts/hvac-pack-diagnosis-DRAFT.md` §9). It feeds four parts of the pack:
- the model library (beat maps and labelled scripts by video type)
- the excerpts (real lines grouped by job)
- the voice samples (real human narration only)
- the viewer section (what HVAC viewers bring, from their comments)

The method is the plumbing study's (`studies/plumbing/study-brief.md`). The selection is different: the videos are picked by **video type** from the HVAC research (`niche-research/studies/hvac/`), not five recent and five popular per channel, because the pack needs models for each type.

## Isolation rules

- Read and write only inside `studies/hvac/` (each helper only in its own channels' folders and notes).
- **Collect and describe only.** Don't write scripts, edit skill or library files, or judge what's "good". The comparison comes later as a separate step.
- Never edit `data/` or `notes/` to fit a conclusion.

## Structure

```
inputs/videos.md                       the selection, with why each video is in it and which helper collects it
data/<channel-slug>/<video-id>/        transcript.txt, comments.md, meta.md
data/<channel-slug>/COLLECTION-LOG.md  per-channel log written by its helper
notes/<channel-slug>__<video-id>.md    one notes file per video
notes/INDEX.md                         one line per video
transcripts-combined/                  transcripts merged per channel, with header blocks
log.md                                 every round: what ran, failures, skipped videos and why
```

## Sources

NexLev tools only: `youtube_video_details` (exact views, date, duration, likes), `get_video_transcript` or `get_bulk_video_transcripts` (up to 10 a call), `youtube_video_comments` (top and newest), `youtube_channel_videos` (for the channel's normal), `check_faceless_channel` (type). None of these count against the web-search cap. If NexLev fails for a video, log it and move on; don't switch to another method without the main session's yes.

## For every video

- `meta.md`:
  - title, channel and handle, video ID and URL
  - the video type (from `inputs/videos.md`)
  - upload date, duration, views and likes (as of the collection date), and the collection date
  - the channel's normal, and views divided by normal
  - age at collection
  - format: on camera / faceless / faceless persona / AI avatar, with the basis
  - transcript source and segment count
  - comment counts (total shown, and how many collected)
  - **Normal:** the median of exact views of the channel's 15 most recent long-form uploads (5:00 or longer, not Shorts) that are at least 7 days old.
- `transcript.txt`: the full transcript, one line per segment, `[m:ss] text`. If none exists, log it and skip the video.
- `comments.md`: the top ~60 comments by relevance plus the ~20 newest. Text and like counts only, **never usernames**. Skip obvious spam. Mark replies from the channel owner as `[OWNER]`.

## Notes (one per video, about 300-400 words, describing only)

The plumbing notes' sections, plus four HVAC ones:
- **Basics:** title, views divided by normal, duration, format, type.
- **Structure map:**
  - the hook's length (words and seconds)
  - when the first real value lands
  - each segment with its approximate start time and word count
- **Pacing:** how segments connect; how long each point or item runs (shortest, longest, typical).
- **Content habits:**
  - prices and costs: how often, and how said
  - where to buy parts or tools
  - how much it describes what's on screen
- **Voice:**
  - personal experience or stories (yes/no, how often)
  - personality against pure information
  - any group or company cast as the adversary, quoted
- **CTAs:** where they fall (timestamp), what they ask for, how they're worded.
- **HVAC: safety.** Every safety line, quoted with its timestamp: power off, gas, carbon monoxide, capacitors, refrigerant, "call a tech" moments and what triggers them.
- **HVAC: the emotions voiced.** Up to five short quotes showing the feeling the script works on (the cold night, the bill, the upsell, pride, comfort, distrust), each with its timestamp. Quote; don't label beyond a word or two.
- **HVAC: the season and the clock.** Any season, weather or time-pressure lines, quoted.
- **Standout lines:** up to 3 short excerpts, at most 2 sentences each.
- **Comments:**
  - recurring questions, complaints and praise, with rough counts
  - safety corrections from viewers, quoted with likes
  - what viewers say they saved or avoided (money, a visit, a cold night), quoted with likes
  - any "sounds like AI" remarks, with a rough count
