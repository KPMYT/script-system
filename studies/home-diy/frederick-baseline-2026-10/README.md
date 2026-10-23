# Frederick Barnes: baseline of the scripts made before the library (2026-10-22)

Study data: collect and describe only. Nothing here is a rule, and nothing here was edited to fit a conclusion.

**Why it exists.** Frederick Barnes (the retired-fireman persona) is moving from home security and fire prevention towards home DIY, with the firefighter framing kept. Before his scripts change, this records what the channel's scripts were like and how the videos did, so later scripts can be compared against it.

## What's here

| File | What it is |
|---|---|
| `scripts/NEW-01.txt` … `NEW-23.txt` | The 23 scripts as they sit in the team's Drive (folders "[NEW 1]" to "[NEW 23]", one Google Doc each, fetched 2026-10-22). Copied verbatim by helper agents, typed out from the fetch results (not byte-diffed against Drive). Kept as returned: the `\===START CTA(...)===` markers, `\[voice tags\]`, curly quotes, em dashes and spacer lines. Written with the old system (the FacelessOS-style master prompt plus the Notion profile), not this library. |
| `views.md` | Which script became which video, the public view counts on 2026-10-22, durations, and words a minute. |
| `measurements.md` | Counts per script (words, "you", "I", questions, "but", sentence length, CTA length and position, voice tags, name intro) and what the library's scanner flagged. |
| `measure.py` | The counting script behind `measurements.md` (run: `python3 measure.py scripts`). Regex counts: approximate. |
| `scanner-output.txt` | `core/script-scanner.py` run on each script (with the backslashes before `===` and `[` removed first), using a TEST-only rules block: name Frederick Barnes, book Prevent The Burning, tenure none, "e-book" banned, the sign-off allowed. CTA-label lines left out. |
| `analysis.md` | The main session's reading of the 23 scripts against the library and the plumbing findings (as given to the operator on 2026-10-22). |

## Sources

- Scripts: Google Drive, team folder `1_UPLOADED` (and the folder above it for NEW 22 and 23).
- Briefs and titles: the "FREDERICK BARNES" ideation sheet (Drive).
- Persona and CTA rules at the time: Notion, "FIREFIGHTING - Frederick Barnes" (Channel List, TEAM ACCESS).
- Views: the channel's public videos tab (`UCSf0X7Rt96r7sx0uCiDgDcA`) read with `yt-dlp --flat-playlist` on 2026-10-22. NexLev was down (connection error). Per-video pages were blocked ("confirm you're not a bot"), so there are no exact upload dates, likes or comments; the flat list rounds large counts (434,000).

## Limits

- Views are one day's snapshot with no upload dates, impressions, click-through or retention, so they can't separate the script from the title, thumbnail or how much YouTube showed the video.
- NEW 21, 22 and 23 weren't published on 2026-10-22.
- Two titles changed at upload (NEW 6, NEW 7), and NEW 5's "(25 Years of Storm Calls)" became "(The Firefighter Way)".
