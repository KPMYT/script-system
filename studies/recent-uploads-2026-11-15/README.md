# Recent uploads, 2026-11-15: Roger the Pipe Guy, script review before the retention graphs

The operator asked for a review of Roger's last five uploads in two stages: "first do a script analysis without looking at the retention curves, based on our improvements last time ... compare hooks, CTAs, body's, overall structure, and other necessary variables. then we look into detail at the retention graphs."

**Stage 1 (this folder's `analysis-scripts.md`)** was written before any retention file was opened. **Stage 2** (the retention exports from YouTube Studio) comes after, in its own file, so the script read can't be bent to fit the curves.

**The five videos** (NexLev `youtube_channel_videos`, newest first, 2026-11-15; the operator's Studio exports name the same five):

| # | Video | Title | Published (NexLev) | Length |
|---|---|---|---|---|
| 1 | `DH2pymJ_25Y` | DO NOT Plunge Your Sink Until You Watch This Video | 11-07 | 15:12 |
| 2 | `mv7sECwbEQo` | Put a Dishwasher Tablet in Your Kitchen Sink and Watch What Happens (7 Genius Uses) | 11-10 | 12:54 |
| 3 | `L0gXnrUhubQ` | You're Cleaning Your Toilet Bowl WRONG — Learn the RIGHT Way | 11-11 | 13:33 |
| 4 | `6hRdKcuEFJs` | You've Been Using Hydrogen Peroxide WRONG (It Stopped Working) | 11-12 | 13:13 |
| 5 | `nOvk7uwz06s` | How To Remove Years Of DISGUSTING Sludge From Your Washing Machine Drum (GUARANTEED!!!) | 11-13 | 14:23 |

Not in the operator's five: `8t_8SDbzmc4` ("Pouring Drain Cleaner Is NOT Saving You Money", 11-07) and `bzYjAKdRIe0` (11-06).

**Method:** as in `recent-uploads-2026-11-05/`. Captions from `get_bulk_video_transcripts`, joined into lines of about 30 seconds (`transcripts/roger-<id>.txt`, words exactly as captioned). Read in full against the rules in force since 2026-11-06 (P21: `personas/roger-the-pipe-guy.md`, `plumbing-scripts/SKILL.md`), and compared with the 11-05 review of Roger's nine uploads before them. `plumbing-scripts/check.py` was run on timestamp-stripped copies with no brief; book page claims checked against `personas/books/roger-the-pipe-guy-book.md`; prices against `plumbing-scripts/references/price-guide.md`.

**Cautions:**
- Captions are what the voice said, in the caption system's spelling ("$150", "3%", "100 Old House Fixes"). The VA's scripts and briefs aren't in the repo, so the checker's money, number and symbol lines are mostly caption artefacts or brief-sourced and are not counted as breaks here unless the words themselves break a rule.
- Question counts come from caption punctuation (approximate).
- Whether these five were written on the P21 skills isn't recorded; the dates (all after the 11-06 build) and the book-line shape suggest they were.

Findings only: nothing in the library changed because of this folder.

## Files

| File | What it is |
|---|---|
| `transcripts/roger-<id>.txt` | Caption text in lines of about 30 seconds, each starting with its timestamp |
| `analysis-scripts.md` | Stage 1: the script read, hooks, structure, body, book line, ending, voice and facts, against the rules and the 11-05 review |
| `retention/<videoId>/*.csv` | Stage 2 data: the operator's YouTube Studio audience-retention exports, unchanged (all viewers, organic, and the subscriber, new and returning, and casual and regular splits; the ad files are empty) |
| `analysis-retention.md` | Stage 2: the curves matched to the captions, where viewers leave, who stays, and stage 1's seven predictions checked |
| `winners-check.md` | Problems 2 (the limit line at 0:30 to 0:45) and 3 (the book line) looked for in our 15 study hits and Roger's two recent hits: the openings and every book or subscribe passage |
