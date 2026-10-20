# Log

Every action, every failure, every skipped video and why. Newest at the bottom.

## 2026-10-20 — Setup

- Operator supplied five competitors (Silver Cymbal, Roger Wakefield, Got2Learn, Arrow Pest Service as a parallel niche, TheCheapFix as an AI channel) and asked for the woodworking exercise at a larger scale on their three plumbing channels (Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter): 5 most popular (last 2 years) and 5 most recent per channel, reviewed by subagents, with a comparison afterwards.
- NexLev `channel_resolver` resolved all five competitor links (IDs in `inputs/channels.md`). Own channels found by NexLev channel search, exact title match.
- Created `study-brief.md`, `inputs/channels.md` and the folders.
- Collection and notes: one helper agent per channel (8 in parallel), each writing only inside its own channel folders and a `COLLECTION-LOG.md`.

## 2026-10-20 — Collection and notes (8 helper agents)

Method: as `study-brief.md`. One helper per channel, NexLev only, each writing only its own channel folders, with its full record in `data/<group>/<channel>/COLLECTION-LOG.md` (selection, skips, the 15 normal-window views, format basis, comment totals, API oddities). Exact dates and views from `youtube_video_details`.

| Channel | Group | Videos | Normal | Format |
|---|---|---|---|---|
| Roger the Pipe Guy | own | 10 | 2,688 | FACELESS (NexLev's check says not faceless, 0.96; recorded FACELESS on credits lists of other channels' footage, voiceover-only transcripts and comments) |
| Mark Silverbridge Plumbing | own | 10 | 549 | FACELESS (same conflict: NexLev says not faceless, 0.98) |
| The Vintage Pipefitter | own | 10 | 609 | FACELESS (NexLev agrees, 0.98) |
| Silver Cymbal | competitor | 10 | 70,989 | FACE |
| Roger Wakefield Plumbing Education | competitor | 10 | 5,210 | FACE |
| Got2Learn | competitor | 5 | 121,799 | FACELESS (one recent video, a channel update, is FACE) |
| Arrow Pest Service | competitor (pest control, parallel niche) | 10 | 270,890 | FACE |
| TheCheapFix | competitor ("AI channel") | 10 | 7,670 | FACELESS |

Skips and gaps:
- **Got2Learn has no most-viewed group.** Its only long-form upload since 2024-10-20 (a 2025-07-01 channel update) is already in the recent group; the one before is from 2023. Nothing substituted; the operator decides. One video (2DQq4wa0ar0) had no transcript and was replaced by the next one down.
- **Roger the Pipe Guy:** 3GMK8QAmagA had no transcript (two tries); the next recent video took its place.
- **Popular lists dominated by old uploads:** Roger Wakefield's window picks are popular ranks 23-106, Silver Cymbal's 5-110 (older videos skipped by exact date, listed in each log).
- **Comments:** NexLev's comment paging returns the first page again on every channel, so each video has at most about 20-29 top and 20 newest comments, not ~50 + ~25. Many own-channel recent videos have 0-1 comments.
- **Boundary cases:** some channels' newest window video is exactly 7 days old and was counted; each log gives the normal without it (unchanged for Mark, TheCheapFix and Silver Cymbal; Roger the Pipe Guy would be 2,816).
- **Topic mix:** the selection rule doesn't filter by topic. Silver Cymbal is broad home DIY (1 of 10 is a plumbing video); TheCheapFix has 4 car/pet videos and 1 HVAC.
- **Notes length:** the notes run about 400-550 words with headings, over the brief's 250-350 but in line with the woodworking notes they copy.

Checks by the main session:
- All 8 channels: every video folder has meta.md, transcript.txt and comments.md, and every video has a notes file (75).
- Every normal recomputed from the 15 views in its log: all 8 match. Every meta.md's views / normal matches its views and normal.
- No usernames or handles in any comments.md (the only "@" matches are in the header lines describing the rule).

Recorded as found (described, not judged): the own channels' narrators give different tenures (Mark 25/35/45 years; Vintage Pipefitter's narrator says 30 while titles say 45); two Vintage Pipefitter videos read script cues aloud ("And subscribe CTA.", "Mid-roll subscribe CTA."); a French comment on Got2Learn's channel update says its content is reused by "AI channels like Roger the Pipe guy".

## 2026-10-20 — Index and combined transcripts

- `notes/INDEX.md`: one line per video (75), own channels first.
- `transcripts-combined/`: one file per channel, plus `own-3-channels.txt` and `competitors-5-channels.txt`, with header blocks; see its README. Built with a scratch script outside the repo. Verified 204,760 transcript words in the originals and in the combined files.

## 2026-10-20 — Operator decisions after collection

- Own channels confirmed (the three found by name search are the right ones).
- Got2Learn: add its 5 all-time most-viewed long-form uploads as its Group B (one helper agent; channel normal kept at 121,799).
- Comparison approved: written to `comparison/`, separate from the data and notes. `comparison/stats.md` holds the measured numbers per video (length, spoken words, words per minute, hook length, first-value time), computed by the main session from the meta, transcript and notes files.

## 2026-10-20 — Got2Learn all-time group added

- Helper collected Got2Learn's 5 all-time most-viewed long-form uploads (popular ranks 1-5, 2017-2021: pmN88UvZfDI, 8IV7oG43DZ0, DHk94YoC95k, JyVbjDsric4, xpsLXmntINE), with transcripts, comments and notes; details appended to its COLLECTION-LOG.md. Normal kept at 121,799. No skips; one transient 504 on a transcript (retried, identical text); the video-watch tool was rate-limited, so the five are FACELESS by the channel check, transcripts and comments, not visually checked.
- Rebuilt `notes/INDEX.md` (80 lines), `transcripts-combined/` (211,449 transcript words in originals and combined files) and `comparison/stats.md`.

## 2026-10-20 — Comparison

- Three analyst agents, each writing one file in `comparison/` and reading only the study data: `01-own-channels.md` (own hits vs recent), `02-competitors.md` (competitor profiles, TheCheapFix in depth), `03-own-vs-competitors.md` (12 dimensions, top-10 differences). The main session wrote `comparison/README.md` (summary, limits, consolidated suggestions).
- Spot-checks by the main session against the transcripts and meta files: "Peroxide does not dissolve rock" (uWXIUmWdPeY [1:31]) present; the spoken cues "And subscribe CTA." (hOz49worQJg [18:43]), "Mid-roll subscribe CTA." (rDLzNLUZnhw [8:54]), "Bonus tip stinger." (uWXIUmWdPeY [20:58]) and "Continuing with the final sections now" (WfAwg1l0xCE [12:46]) present; "Where is the footage of him doing the tests?" present (sXlzedri_Hg comments); a name or channel intro in the first minute in 15 of 15 own recent uploads and 0 of 15 own hits (confirmed by search; the hits' first-minute "I'm" lines are all "I'm going to…"); the shared-title dates (TheCheapFix 2026-05-23 then Vintage 2026-07-15; Roger 2026-07-01 then TheCheapFix 2026-10-16). One count differs by method: "stay till the end" teases in own hooks, 22 of 30 by part 3's hand count, 18 of 30 by a strict phrase search; the summary gives both.

## 2026-10-20 — Operator decisions on the comparison; readable page

- Operator decisions recorded in `comparison/README.md` and `HANDOFF.md` section 3: Vintage Pipefitter CTA only at the end (two-line free e-book, email capture); Roger and Mark CTAs shortened; no name intros on any channel (core already bans them; woodworking profiles say "Greeting: none"); Mark's tenure 45; faster to the point; TheCheapFix not the main source.
- Production-notes count (operator's question): a pattern search of all 80 transcripts found 4 spoken labels in 4 own hit videos (3 Vintage, 1 Roger), listed in `comparison/README.md`. "a cut to a colony of bacteria" (ihZc3VGeG6c [1:52]) matched the search but is narration, not a cue.
- Readable summary page published as a private artifact for the operator: https://claude.ai/artifact/SGRPBBUCWdG8YUFWkuW6Fd (source kept outside the repo).

## 2026-10-20 — Second, deeper comparison pass

- The operator found the first comparison not detailed enough and asked for examples for every medium and weaker suggestion, more hook structures and more on the emotions used. Five analyst agents, each writing one file: `04-hooks.md`, `05-emotions.md`, `06-titles-and-promises.md`, `07-body-craft.md`, `08-suggestions-with-examples.md`. Each reports that its quotes were matched to the transcripts by script and that no illustrative line shares 8+ consecutive words with any transcript.
- Main-session spot-checks: "Look at the toilet on the left" (n-2hjVGsu-Q [0:00]) and "That picture you clicked on" (bSrEWmK0g5E) present; "Nine times out of 10" in 11 of 30 own transcripts (01 had said "at least 9"); washing soda "Pour it dry. Do not mix it into a slurry" (rDLzNLUZnhw [8:13]) against "dissolve one cup … in a bucket" (Rb0aS97YnSA [11:28]); "This is the one that makes the word forever in that title honest" (hOz49worQJg) and "pure reflex for anyone who clears drains" (fq7bWC_bRqQ) present; the 428-like comment on kHT6ZL8At0w present. The scanner's tease bans were tested against the phrasings `04-hooks.md` lists: "stay till the end", "stick with me", "do not go clicking away", "bonus tip at the end", "at the very end" and "stay for number 10" are not caught; "stick around" is.
- Readable page rebuilt from the five deep-dive reports and republished to the same link (version 2): 19 hook structures, 18 emotions, 25 title formulas, 12 item shapes, suggestions (a)-(j) with examples and rewrites, the proposed scanner checks. The page builder reports all 603 quoted strings match the report files. One rendering fix by the main session: comment tags now wrap, which removed a 78px sideways scroll at phone width.
- `comparison/09-differences.md` (operator's request: "list to me all differences between scripts in these variables"): 24 variables × 11 groups, built from files 01-08 with gaps filled from notes and transcripts; a table of the counts the files give differently, with both figures; the ranked 15.
- Readable page version 3: "Every difference" section added from 09 (24 variable boxes, the ranked 15), and the scanner section now shows the core checks as built.
- `comparison/11-reasons-to-stay.md`: what happens after the point in all 40 hits (first answer, every value promise, when it's paid), 19 devices, templates. Its verification: 259 script and 50 comment quotes found verbatim; no illustrative passage shares 8+ words with a transcript; passages pass the scanner. Three tease forms it found unbanned were added to the scanner.
