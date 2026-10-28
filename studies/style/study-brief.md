# Style niche study (women over 50): brief

For Scarlet Sterling (the affluent American) and Diane de Chambray ("the French way"). Plan: `drafts/style-study-plan-DRAFT.md`. Operator decisions: `HANDOFF.md` §3, "the style niche study" (2026-10-28).

**Scope:** hair and fashion for women over 50 first. Makeup and skincare for mature women are scanned too, labelled `adjacent`; they get their own pack later.

## Isolation rules (every helper)

- Write only inside `studies/style/`, and only in your own files.
- **Collect and describe only.** Don't judge what's "good", don't write scripts, don't edit library or skill files.
- Never edit collected data to fit a conclusion.
- Never store commenters' usernames.
- NexLev tools only (no web search). If a call fails, retry once, then log it and move on.

## Phase 1: own baseline (`own-baseline-2026-10/`)

Every upload on both channels: views, likes, date, length, views divided by the channel's normal. Transcripts and comments for every video (the channels are small). Notes on the top and bottom videos.

## Phase 2: the scoping scrape (`discovery/`)

Four discovery helpers, each with its own lane and its own raw file in `discovery/raw/`. Overlap between lanes is expected; the main session de-duplicates.

**What counts as a candidate:** an English-language YouTube channel where women over 50 are the main audience or a major share of the videos (titles with "over 50 / 60 / 70", "mature women", "older women", "after 50", gray hair, or presenters over 50 talking to their peers). Broad style channels count only if mature-women videos are a large share of their winners.

**Keep a channel when:** it has uploaded in the last 12 months, **and** it has 10K+ subscribers or any video since 2022 with 100K+ views. A faceless or AI channel under a year old is kept with any video at 50K+ (these new entrants are the closest format peers to our channels). Channels that fail are listed in a short "screened out" section with the reason, so they aren't searched again.

**Raw file columns** (`discovery/raw/<lane>.csv`, one row per channel):

```
channel_name,handle,channel_id,url,country,subscribers,total_views,video_count,channel_created,last_upload,uploads_last_90d,type,type_basis,nexlev_faceless,nexlev_confidence,lane,audience_fit,top1_title,top1_views,top1_date,top2_title,top2_views,top2_date,top3_title,top3_views,top3_date,est_monthly_revenue,rpm_est,found_via,notes
```

- `type`: `real_on_camera` · `faceless_narrated` (voice over stock or slides) · `ai_avatar` (generated presenter) · `ai_clone` (copies a real presenter's format with a generated one) · `mixed` · `unclear`
- `type_basis`: what the type rests on (the NexLev faceless check, thumbnails, titles, the description). Mark your own reading as `reading`.
- `lane`: `fashion` · `hair` · `fashion+hair` · `makeup-adj` · `skincare-adj` · `french-lens` · `lifestyle-mixed`
- `audience_fit`: `core-50plus` · `partly` · `broad`
- top videos: the channel's top three long-form videos (5:00 or longer) **since 2022**, by views, with exact views and dates
- revenue and RPM: NexLev's estimates, as given
- `found_via`: the search or tool that found it

Each helper also writes `discovery/raw/<lane>-log.md`: every search run (tool, query, filters), the count found, failures, and the screened-out list.

## Phase 3 onward

Outliers against each kept channel's normal, the video-type map, then the script and comment study (the HVAC method, `studies/hvac/study-brief.md`). Briefs for those follow once the master channel list is approved.

**Normal (for later phases):** the median of exact views of a channel's 15 most recent long-form uploads (5:00 or longer, not Shorts) that are at least 7 days old.

## Round 2 (2026-10-28, after the NexLev top-up): finish the screen and collect the outliers

Every channel in `round2/worklist-N.csv` gets the same treatment: the 198 kept channels (`status` kept) and the 159 found but not screened (`status` to-screen, from the lane logs and the operator's list). Six helpers, one worklist each.

**Calls per channel (NexLev is now paid, $0.02 a call: stay at or under 180 calls per helper):**
1. `youtube_channel_outliers` (`max_videos` 100, `min_outlier_threshold` 2): the channel's about data (subscribers, total views, joined date, video count, NexLev's average views) and its outlier videos.
2. `youtube_channel_videos`, sort `newest`: last upload, uploads in the last 90 days, and the **normal** (the median views of the 15 most recent uploads of 5:00 or longer that are at least 7 days old; if fewer qualify, use all that do and say so). Also record how many of the newest 30 are under 5:00 (the Shorts share).
3. `check_faceless_channel` only for to-screen channels. **NexLev reads a generated presenter as "not faceless"**, so its answer can't tell real women from AI.
4. Then the **thumbnail reading** (free, no NexLev call). Download two outlier thumbnails (`https://i.ytimg.com/vi/<id>/hqdefault.jpg`) with curl into a new folder under the scratchpad, and look at them with the Read tool. Set `type` from what is visible:
   - `real_on_camera`: the same photographic woman, consistent across videos, plus a named presenter in the about text or title
   - `ai_avatar`: a generated-looking presenter
   - `faceless_narrated`: no presenter (outfit collages, models, stock)
   - `mixed` or `unclear` otherwise

   Always give the basis.

**Output** (append a row after each channel, so nothing is lost if the run is cut short):
- `round2/channels-N.csv`:
  ```
  channel_id,channel_name,handle,status_in,subscribers,total_views,joined,video_count,nexlev_avg_views,normal,normal_basis,last_upload,uploads_last_90d,shorts_in_newest30,type,type_basis,nexlev_faceless,presenter_note,lane,audience_fit,keep,keep_reason,notes
  ```
  `keep` applies the Phase 2 rule (active in the last 12 months; 10K+ subscribers or a 100K+ video since 2022; a faceless or AI channel under a year old with a 50K+ video). Kept rows are re-checked by the same rule.
- `round2/outliers-N.csv`: every outlier video the tool returns, one row each:
  ```
  channel_id,channel_name,video_id,title,views,publish_date,length,nexlev_ratio,ratio_vs_normal,since_2022,on_topic,topic_note
  ```
  - `on_topic` is `core` (hair, fashion, accessories or color for women 50+), `adjacent` (makeup or skincare for mature women), or `off` (anything else, such as health, fitness or lifestyle).
  - `ratio_vs_normal` is views divided by the normal from call 2. `nexlev_ratio` is the tool's own figure (views against the channel's mean).
- `round2/log-N.md`: calls used, failures, anything odd.

The helpers never edit `discovery/`, `inputs/` or another helper's files.

## Round 3 (2026-10-28): the script and comment study

The 45 approved videos are in `inputs/study-videos.md` and `inputs/videos.csv`. The `helper` column assigns each video; every channel belongs to one helper. The method is the HVAC study's (`../hvac/study-brief.md`), with style's own note sections.

**Tools (NexLev, paid; at most 60 calls per helper):**
- `youtube_video_details`: exact views, likes, date, duration, description
- `get_bulk_video_transcripts`: up to 10 IDs per call; `get_video_transcript` if one is missing
- `youtube_video_comments`: sort top and sort newest, one page each, plus one more page of top when it returns a continuation token

The channel's **normal** comes from `round2/channels-all.csv` (look up the channel ID). Compute it fresh only if the channel isn't there (Ageless Confidence): use one `youtube_channel_videos` newest call and the rule above.

If a video has **no transcript**, keep its meta and comments, write no notes, and say so in your log. The main session swaps in a reserve.

**For every video, in `data/<channel_slug>/<video_id>/`:**
- `meta.md`:
  - title, channel, handle, video ID and URL
  - the study group and why it was picked (from `videos.csv`)
  - upload date, duration, exact views and likes, and the collection date
  - the channel's normal, and views ÷ normal
  - age at collection
  - type (from round 2) and the presenter, as heard in the transcript (first-person name, gender)
  - transcript source and segment count
  - comments shown and collected
  - the AI disclosure line in the description, if there is one, quoted
- `transcript.txt`: one line per segment, `[m:ss] text`
- `comments.md`: text and like counts only, **never usernames**. Mark the owner's replies `[OWNER]` and skip spam.

**Notes (`notes/<channel_slug>__<video_id>.md`, about 500-800 words, describing only):**
- **Basics:** title, views ÷ normal, duration, words, words per minute, type, group.
- **Structure map:**
  - the hook: its words and seconds, quoted in full if under 80 words
  - when the first real item lands
  - every segment with its start time and approximate word count
  - the number of items and their typical length in words
- **Voice:**
  - the authority line (who she says she is), quoted
  - "you" against "I"
  - personal stories
  - any group cast as the adversary, quoted (salons, stylists, "the fashion industry", "Americans", younger women, the viewer's past self)
- **The feelings voiced:** up to six short quotes with timestamps, each labelled in a word or two (invisible, older than she feels, frumpy, confidence, being seen, money, belonging, rebellion, permission).
- **Reassurance and shame:** "nothing is wrong with you" lines, and any lines that could read as shaming the viewer or other women. Quote both.
- **The age in speech:** how often an age or "over 60" is said, quoted with examples.
- **Visuals in words:** does the narration name what should be on screen? Two examples.
- **Products, brands, stores and prices** named.
- **Promises and payoffs:** what the opening promises, and where (or whether) each promise is paid.
- **CTAs and the ending:** timestamps and wording quoted; the last 40 words quoted.
- **The French or national lens**, where there is one: the claims made about French (or other) women, quoted, and how they are hedged.
- **Standout lines:** up to three, two sentences each at most.
- **Comments:**
  - recurring themes with rough counts, and the questions viewers ask
  - the ages viewers give
  - what they say they'll change or have changed
  - pushback or corrections, quoted with likes
  - any "AI" or "fake" remarks, quoted with likes and counted

**Each helper also writes `data/COLLECTION-LOG-H<n>.md`:** calls used, failures, swaps needed. Before finishing, run a self-check:
- three fresh details calls
- a script (`python3 -I`) that finds every quoted string in the notes in its transcript or comments file
