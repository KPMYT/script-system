# Combined transcripts (paste-ready)

All 80 collected transcripts, combined into plain-text files for pasting or uploading into a Claude chat.

| File | Videos | Approx. size |
|---|---|---|
| `1-roger-the-pipe-guy.txt` | 10 (own) | ~30K words / ~40K tokens |
| `2-mark-silverbridge.txt` | 10 (own) | ~29K words / ~39K tokens |
| `3-vintage-pipefitter.txt` | 10 (own) | ~31K words / ~41K tokens |
| `4-silver-cymbal.txt` | 10 (competitor) | ~12K words / ~16K tokens |
| `5-roger-wakefield.txt` | 10 (competitor) | ~25K words / ~33K tokens |
| `6-got2learn.txt` | 10 (competitor: 5 recent + 5 all-time most-viewed, 2017-2021) | ~14K words / ~18K tokens |
| `7-arrow-pest-service.txt` | 10 (competitor, pest-control parallel niche; one recent video is a 1:55:07 compilation) | ~49K words / ~65K tokens |
| `8-thecheapfix.txt` | 10 (competitor, "AI channel") | ~28K words / ~38K tokens |
| `own-3-channels.txt` | 30 (files 1-3) | ~90K words / ~120K tokens |
| `competitors-5-channels.txt` | 50 (files 4-8) | ~128K words / ~170K tokens |

Each video starts with a header block:

```
================================================================
VIDEO: <title>
Channel: <channel> (own|competitor) | Format: FACE/FACELESS [| niche or operator note]
Selection: <5 most recent long-form uploads / 5 most-viewed long-form uploads, last 24 months / 5 all-time most-viewed long-form uploads>
Uploaded: <date> | Duration: <m:ss> | Views: <n> | Views/normal: <ratio> (channel normal <n>)
URL: <youtube url> | Video ID: <id>
----------------------------------------------------------------
```

followed by the full transcript as paragraphs, with a `[m:ss]` timestamp about every 30 seconds. Within each file, videos run recent first (newest to oldest), then most-viewed or all-time most-viewed (most views first).

The text is identical to the per-line originals in `data/<own|competitors>/<channel>/<video-id>/transcript.txt` (verified: 211,449 transcript words in both); only the line breaks and per-line timestamps were merged. Views are as of 2026-10-20. The two group files are close to or over the size of a single chat, so the per-channel files are the safer choice.
