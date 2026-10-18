# Combined transcripts (paste-ready)

All 45 collected transcripts, combined into plain-text files for pasting or uploading into a Claude chat.

| File | Videos | Approx. size |
|---|---|---|
| `1-dale-oakfields-workshop.txt` | 10 (own) | ~30K words / ~40K tokens |
| `2-hank-hardwood.txt` | 15 (own: 10 recent avatar + 5 most-viewed faceless) | ~45K words / ~60K tokens |
| `3-bearded-viking-woodworks.txt` | 10 (competitor: 5 recent + 5 most-viewed) | ~19K words / ~25K tokens |
| `4-whosthevoss.txt` | 10 (competitor: 5 recent + 5 most-viewed) | ~24K words / ~31K tokens |
| `all-45-videos.txt` | all 45 | ~118K words / ~156K tokens |

Each video starts with a header block:

```
================================================================
VIDEO: <title>
Channel: <channel> (own|competitor) | Format: FACE/FACELESS (...)
Selection: <10 most recent / 5 most recent / 5 most-viewed ...>
Uploaded: <date> | Duration: <m:ss> | Views: <n> | Views/normal: <ratio> (channel normal <n>)
URL: <youtube url> | Video ID: <id>
----------------------------------------------------------------
```

followed by the full transcript as paragraphs, with a `[m:ss]` timestamp about every 30 seconds. Within each file, videos run recent-first (newest to oldest), then most-viewed.

The text is identical to the per-line originals in `data/<own|competitors>/<channel>/<video-id>/transcript.txt` (verified: 115,003 transcript words in both); only the line breaks and per-line timestamps were merged. Views are as of 2026-10-17.

`all-45-videos.txt` is close to the size limit of a single chat, so the per-channel files are the safer choice.
