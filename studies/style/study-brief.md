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
