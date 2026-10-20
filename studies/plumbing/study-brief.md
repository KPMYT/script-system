# Plumbing Script Study

A study of YouTube scripts in the plumbing niche: the operator's three plumbing channels and five competitors. The method is the woodworking study's (`studies/woodworking/study-brief.md`), at a larger scale. Keep it separate from everything else.

## Isolation rules

- Read and write only inside this repository.
- Never change user-level or global settings. Do not install anything without asking.
- **Collect and describe only.** Do not write scripts, edit skill or library files, or draw conclusions about what is "good." Judging is the operator's job, and comes later as a separate comparison step.
- Never edit `data/` or `notes/` to fit a conclusion.

## Structure

```
inputs/channels.md
data/own/<channel>/<video-id>/          transcript.txt, comments.md, meta.md
data/competitors/<channel>/<video-id>/  same files
data/<own|competitors>/<channel>/COLLECTION-LOG.md   per-channel log written by its helper
notes/own/  and  notes/competitors/     one notes file per video: <channel>__<video-id>.md
notes/INDEX.md                          one line per video
transcripts-combined/                   transcripts merged per channel, with header blocks, for pasting into a chat
log.md                                  every action, failure and skipped video, and why
```

## Transcript source

NexLev MCP tools only (bulk transcripts take up to 10 videos per call). If NexLev fails, stop and report; don't switch methods without the operator's approval.

## Selection (every channel, own and competitor; operator, 2026-10-20)

- **Group A:** the 5 most recent long-form uploads.
- **Group B:** the 5 most-viewed long-form uploads published on or after 2024-10-20 (last 24 months), skipping any already in Group A and taking the next one down.
- Long-form means 3:00 or longer and not a Short.
- Exact dates, views and durations come from `youtube_video_details` (list dates for older videos are approximate).

## For every video

- `meta.md`: title, channel (own or competitor), format, selection group (with its rank in popular order for Group B), video ID, URL, upload date, duration, views (as of the collection date), likes, the channel's normal, views divided by normal, age at collection, transcript source and segment count, comment counts.
  - **Normal:** the median of exact views of the channel's 15 most recent long-form uploads that are at least 7 days old.
  - **Format:** FACE (a real or AI-avatar presenter on camera, or filming a real job) or FACELESS (narration over footage), with the basis recorded (NexLev `check_faceless_channel`, the about text, the transcript, comments).
- `transcript.txt`: the full transcript, one line per segment, `[m:ss] text`. If none exists, log it and skip the video (take the next one in that group).
- `comments.md`: the top ~50 comments by relevance plus the ~25 newest. Comment text and like counts only, never usernames. Skip obvious spam.

## Notes (one per video, about 250-350 words, describing only)

Same sections as the woodworking notes (`studies/woodworking/notes/competitors/*.md` show the layout):
- **Basics:** title, views divided by normal, duration, format, selection.
- **Structure map:** hook length (words and seconds); when the first real value lands; each segment with its approximate start time and word count.
- **Pacing:** how segments connect; how long each point or item runs (shortest, longest, typical).
- **Content habits:** how often prices or costs are mentioned; whether it names where to buy parts or tools; how much it describes what's on screen (show and tell); safety warnings and "call a plumber" moments.
- **Voice:** personal experience or stories (yes/no, how often); personality versus pure information; any group or industry cast as the adversary.
- **CTAs:** where they fall (timestamp), what they ask for, how they're worded.
- **Standout lines:** up to 3 short excerpts, at most 2 sentences each.
- **Comments:** recurring questions, complaints, praise, and any "sounds like AI" remarks, with rough counts.

After the notes, `notes/INDEX.md` (one line per video), then the combined transcripts. No trend summaries or conclusions in this phase.
