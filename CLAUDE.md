# Woodworking-for-Profit Script Study

A self-contained research project: a study of YouTube scripts in the woodworking-for-profit lane. Keep it completely separate from anything else.

## Isolation rules

- Read and write only inside this repository. Never touch other repositories or anything outside this one.
- Never change user-level or global settings. Any configuration needed goes in this repository only.
- Do not install anything without asking the user first.
- Do not write scripts, edit skill files, or draw conclusions about what is "good." This project collects and describes. Judging is the user's job, later.
  - This rule still applies in full to `data/` and `notes/`: collect and describe only, never edit them to judge, and never edit skill files from there.
  - Exception (script-library phase, from 2026-10-18): files inside `script-library/` may be edited, as the user's task for that phase describes. Edit nothing outside `script-library/` during that work (except log entries and this file). Log every change in `script-library/iterations/refs-NN/CHANGES.md` (file | what changed | why), commit after each task, and never delete previous versions.

## Structure

```
inputs/channels.md
data/own/<channel-name>/<video-id>/          transcript.txt, comments.md, meta.md
data/competitors/<channel-name>/<video-id>/  same files
notes/own/  and  notes/competitors/          one notes file per video
transcripts-combined/                        all transcripts merged per channel (and all-in-one), with header blocks, for pasting into a chat
script-library/                              script rules (core/, woodworking-scripts/, tests/); editable only in the script-library phase
log.md                                       every action, every failure, every skipped video and why
```

## Transcript source

Use the NexLev MCP tools (bulk transcripts take up to 10 videos per call). If NexLev is not available in the session or fails, stop and tell the user. Do not switch to another method until the user approves it.

## Phases

Stop after each phase, report briefly, and wait for the user's go-ahead. Commit and push at the end of every phase.

### Phase 1, setup and test
- Save the channel links to `inputs/channels.md`.
- Confirm NexLev works by pulling the transcript of the most recent long-form video on the first own channel. Report whether it worked.

### Phase 2, own channels
- For each of the two own channels: the 10 most recent long-form uploads. Long-form means 3 minutes or longer and not in the Shorts tab.
- "Dale Oakfield's Workshop" pivoted to woodworking-for-profit on 2026-09-09. Tag any upload before that date as PRE-PIVOT in meta.md. Collect it, but mark it excluded from analysis.
- "Hank Hardwood" may have fewer than 10 uploads. Take what exists and log the count.

### Phase 3, competitors
- For each competitor: the 5 most recent long-form uploads, plus the 5 most-viewed long-form uploads from the last 24 months. If a video falls in both groups, take the next one down.
- In meta.md, tag the channel FACE (a presenter on camera or filming a real build) or FACELESS (narration over footage).

### For every video (Phases 2 and 3)
- `meta.md`: title, URL, upload date, duration, views, and the channel's normal. The normal is the median views of its last 10-15 long-form uploads, ignoring anything under 7 days old. Also record views divided by the normal.
- `transcript.txt`: the full transcript. If none exists, log it and skip the video.
- `comments.md`: the top ~50 comments by relevance plus the ~25 newest. Comment text and like counts only, no usernames. Skip obvious spam.

### Phase 4, notes
For each collected video (excluding PRE-PIVOT ones), write `notes/<own or competitors>/<channel>__<video-id>.md`, about 250-350 words, describing only, never judging:
- Basics: title, views divided by normal, duration, face or faceless.
- Structure map: hook length (words and seconds); when the first real value is delivered; each segment with its approximate start time and word count.
- Pacing: how segments connect, and how long each point or item runs (shortest, longest, typical).
- Content habits: how often prices or earnings are mentioned; whether it says where to buy materials; how much it describes what is on screen (show and tell).
- Voice: personal experience or stories (yes/no, how often); personality versus pure information; any group or industry cast as the adversary.
- CTAs: where they fall (timestamp), what they ask for, how they are worded.
- Standout lines: up to 3 short excerpts, at most 2 sentences each.
- Comments: recurring questions, complaints, praise, and any "sounds like AI" remarks, with rough counts.

After Phase 4, write `notes/INDEX.md`: one line per video (channel, title, views/normal, notes file). Then stop. Do not summarize trends or write conclusions.
