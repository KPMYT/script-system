# Model file spec (electrical references)

How every file in `references/models/` was built (2026-10-27), adapted from `plumbing-scripts/model-file-spec.md`. Kept for adding models later; not part of the installed skill.

**The library:** 37 videos (E01 to E38, no E06) from real, on-camera channels with 1M+ views, mostly posted 2022 or later (operator, 2026-10-27: "model scripts for sure please from the winners in recent months/years from the real channels that have over 1m views"). Picks, with views and dates from NexLev on 2026-10-27: `studies/electrical/model-picks-2026-10-27.csv` (E06 dropped: a working electrician's panel job, not homeowner work). E33 to E38 were added after review R3 (`studies/electrical/pack-review-2026-10-27/R3.md`, M9 and M10) to cover the generator, outlet-mistake, plug-hole and LED-glow titles; E38 is a pre-2022 idea reference only (no real 1M+ video on its topic exists from 2022 on). All are real channels, so every file is tagged [real]: structure and voice may be borrowed, wording never.

Every model is ONE markdown file in `electrical-scripts/references/models/`, named `<ID>-<channel-slug>-<short-topic-slug>.md`, e.g. `E01-everyday-home-repairs-outlet-finished-wall.md`.

## File layout (exactly these sections, in this order)

```
# <ID>. <Video title, exactly as on YouTube, curly quotes straightened>

- **Channel:** <name> · **Video:** <id> · https://www.youtube.com/watch?v=<id>
- **Tag:** [real] (structure and voice; never wording)
- **Views / normal:** <N.NNx> (<views> on 2026-10-27 / channel normal <normal>, from the study's videos-with-multiples.csv)
- **Posted:** <YYYY-MM-DD> · **Length:** <m:ss> · <N> spoken words · **Video type:** <one of the types below>
- **US or UK:** <US | UK (sockets, earth, Part P: wording and code never transfer)>

## Beat map

| Time | Beat | What it does (no quoted wording) | Emotion | Words |
|---|---|---|---|---|
| 0:00-0:12 | POINT | names the problem the viewer has and the fix | nuisance → pride | 28 |

- **Items or steps:** how many, how long each runs (shortest, longest, typical), in what order and why.
- **Promise devices:** which ones (step count, numbered item + stake, escalation ladder, the rule that protects everything, check at home, problem you didn't know, myth flag, priority flag, question the next item answers), where each is promised and where paid.
- **Forward lines:** how many; the longest gap between a forward line or payoff.
- **Stakes:** how the danger is said (fire, shock, damage, the dead circuit, the inspector): where it first lands, how often it comes back, how strong; whether it's in proportion.
- **Safety lines:** where power-off / verify-dead / call-an-electrician lines sit, and how long they are.
- **CTA placement:** where, how long (sponsor reads: say so).
- **Ending:** what the last 30 seconds do.
- **What sets it apart from other models of its type:** 2-3 bullets.

## Emotion voicing

The study labelled emotions from titles only; the operator wants "how the script makes them sound" (2026-10-26). For each emotion the video uses (pride / capability, safety fear (fire, shock), "you've been doing it wrong", myth-busting, how-it-works curiosity, nuisance ("make it stop"), relief, others you find), give: where it first comes in (timestamp), how often it returns, and 2-4 verbatim lines with timestamps showing the words that carry it. One line on what the emotional arc of the whole video is (e.g. "nuisance → why → capability → relief").

## Why it works

One paragraph: what the comments thank and complain about (pull the top comments with NexLev `youtube_video_comments`; quote 3-6 with like counts), the pace, the opening, what viewers did after.

## Script (verbatim, labelled)

The full transcript, each paragraph starting with its [m:ss] timestamp, labels in square brackets at the start of the passage they cover.
Labels: [POINT] [QUESTION] [VILLAIN] [SCOPE] [PROMISE] [ITEM] (1), (2)... [STEP] (1), (2)... [MECHANISM] [CHECK] [STAKES] [SAFETY] [CALL AN ELECTRICIAN] [CODE] [MYTH] [FORWARD] [ASIDE] [CTA] [END] [COMMENT] [CLOSE]
Banned (label wherever they occur): [INTRO: banned] [TEASE: banned] [RECAP: banned] [POINTING: banned] [FIRST-PERSON DEMO: banned] (also covers first-person tests, measurements shown on camera, history and customer stories) [TRADE BASHING: banned] (electricians, inspectors, firefighters as villains) [MONEY: banned for this channel] [UNSAFE: banned] [ELECTRICIAN'S JOB: explain, never the viewer's step] (work only a licensed electrician does: anything inside the panel or behind the dead front, new breakers, interlock plates, service conductors, a new circuit; the script explains what the electrician does and why, and never instructs the viewer to do it) [PRODUCTION NOTE: banned] [SPONSOR]
Conventions: two labels on one line = the passage does both, in order; "(2, cont.)" = an item picked up again. Keep the transcript text verbatim (auto-caption mistakes kept); drop only noise tags like [Music]; straighten curly quotes. Replace any email address or phone number with [contact removed]. A sponsor read over ~150 words may be shortened to "[SPONSOR] (sponsor read, N words, omitted)".

## Doesn't transfer

Bullets, each quoting the line with its [m:ss]: everything Frederick Barnes (an AI talking-head presenter, retired electrician, 35 years, knowledge only, no book) can't or mustn't use: on-camera demonstrations, meter readings and tests shown, pointing at the screen, first-person tests and job stories, customer stories, greetings and name intros, teases, recaps, work inside the panel or fitting an interlock (the electrician's job: explained, never instructed), electrician or inspector bashing, money and prices (no money framing on this channel), sponsor reads, UK wording and code, unsafe methods (working live, skipping verify-dead), tenure figures other than 35, and any factual slip you notice (mark your own as "check against the brief").
```

## The video types (use these names)

how-to / correct way; fix this problem (the real reason, why does X keep doing Y); explainer (what X actually does, test topics explained); X vs Y; mistakes list; single big mistake; know-this list (N things every homeowner should know). Use "other: <short description>" if none fits.

## Rules for the builders

- Transcripts: NexLev `get_video_transcript` (fallback `get_video_subtitle`); comments: `youtube_video_comments`. Save raw transcripts under `studies/electrical/transcripts/<video_id>.txt` (study data, never edited after saving).
- Write ONLY your assigned files. Don't commit or push. Scratch work goes in your own subfolder of the session scratchpad.
- Verify by script that the labelled script text (labels removed) matches the saved transcript word for word, and that every quote in "Emotion voicing", "Why it works" and "Doesn't transfer" is verbatim with the right timestamp.
- Plain, clear English in your own text; no em dashes, no curly quotes, no ellipsis characters.
- When done, reply with: each file name, its video type, spoken words, item count, its emotional arc, and anything you couldn't do or flagged.
