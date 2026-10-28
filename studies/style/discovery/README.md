# Discovery: the scoping scrape (round 1, 2026-10-28)

**Status:** round 1 is collected, but it stopped early when NexLev's weekly limit (2,000 calls across the account) ran out. The list is a working draft, not the final channel map.

## Files

- `raw/<lane>.csv` and `raw/<lane>-log.md`: one per helper (fashion, hair, French plus makeup and skincare, faceless and AI). Each log lists every search, the screened-out channels with reasons, and the channels found but not yet screened. The raw files are never edited.
- `master.csv`: the four lanes merged by channel ID, built by `../tools/merge_discovery.py` (`python3 -I tools/merge_discovery.py discovery/raw discovery/master.csv`, run from `studies/style/`). It holds 198 unique channels; 61 were found by more than one helper.

## How the merge works

- **Base row:** where several lanes found the same channel, the row with the most filled cells.
- **Type:** if the lanes agree, their type is kept. Where one lane said `unclear` or `mixed` and another gave a specific type, the specific one is kept. Two specific types that disagree become `disputed`. Every lane's reading and its basis are kept in `type_readings`.
- **Groups:**
  - `real` is `real_on_camera`.
  - `faceless-ai` is `faceless_narrated`, `ai_avatar` or `ai_clone`.
  - `unclear` is unclear, mixed or disputed.
- **Top videos:** the three highest-viewed long-form videos found by any lane, with duplicates removed by title.
- **Tier** comes from the best video: A 1M+, B 300K-1M, C 100K-300K, D under 100K, or unknown.
- **`data_gaps`** names what is still missing.

## Counts (198 channels)

| Group | A 1M+ | B 300K-1M | C 100K-300K | D under 100K | unknown | All |
|---|---:|---:|---:|---:|---:|---:|
| real | 17 | 24 | 17 | 9 | 22 | 89 |
| faceless-ai | 7 | 26 | 34 | 10 | 5 | 82 |
| unclear | 2 | 12 | 9 | 1 | 3 | 27 |

## Known limits (fixed in round 2, after the reset)

- **Approximate views and dates on 122 rows.** Some helpers worked from rounded view counts, relative dates such as "2 years ago", or NexLev's cached index, which covers only part of each channel.
- **Missing upload counts:** `uploads_last_90d` is missing on 102 rows.
- **Missing top videos:** 30 rows have no top videos, and 27 have only one or two.
- **Off-topic top videos.** Some "top videos" are off-topic, so a channel's tier is not yet a niche verdict: castor oil, a menopause belly-fat video, a home tour. Phase 3 judges only on-topic outliers against each channel's normal.
- **Not yet screened:** about 170 channels were found but not screened:
  - faceless and AI: 45
  - hair: 31
  - fashion: 97
- **Not yet run:** the similar-channel and suggested-video searches on the strongest faceless channels and on the operator's own videos.
