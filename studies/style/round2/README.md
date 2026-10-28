# Round 2: the finished channel screen and the outliers (2026-10-28)

Six helpers, one work list each (`worklist-1.csv` to `-6.csv`, 357 channels), method in `../study-brief.md` "Round 2". NexLev calls: 887 in all (144-151 per helper), no limit or credit errors.

## Files

- `channels-N.csv`, `outliers-N.csv`, `log-N.md`: each helper's raw output. These are never edited.
- `channels-all.csv` and `outliers-all.csv`: merged by `../tools/merge_round2.py`. The merge adds:
  - `audience_check`: the main session's calls on channels that pass the numbers but aren't 50+ style (the list is at the top of the script)
  - `group`: real, faceless-ai or unclear
  - `final_keep`
  - for each outlier: `long_form`, `angle` and `object` (keyword rules on the title)
- `BREAKOUT-MAP.md`: the tables, built by `../tools/breakout_map.py`.

## Counts

- **Channels:** 357 checked, **249 kept**.
  - By group: 106 real on camera; 126 faceless or AI (102 faceless narrated, 24 AI presenter); 17 unclear or mixed.
  - Seven of the kept channels are only partly 50+ (Blowout Professor, Lisa Eldridge, two street-style channels and others). They are left out of the map.
- **Audience fails** (pass the numbers, not this niche): WISE ELDER'S INSIGHT, Historias de Adobe, Loya the Fashion Queen, Prime of your life, Whispers Fashion & Styles, Only Fame, 10 Years Younger, Tina Yong. Two more channels fail for suggestive framing, against the style hard rule: Older Line Podcast With Penelope and Feminine Over 50 With Mia.
- **Outliers:** 2,478 unique videos. The map uses **1,182 core** and **345 adjacent**: long-form, 2022 on, kept channels that pass the audience check.

## Limits

- **The data is rough:**
  - views are NexLev's rounded counts
  - dates come from relative text, so they are approximate and "4 years ago" can't be placed against the 2022 floor
  - outliers are only found among each channel's 100 most recent uploads
  - Shorts were never checked
- **The labels are judgements:**
  - The type rests on two thumbnails per channel. NexLev's faceless check reads generated presenters as "not faceless", so it can't separate real from AI.
  - Angle and object are keyword rules on titles, so a few are misfiled and about 9% are "other". They sort the map; they are not a reading of the videos.
- **Ratios against the normal can be huge** (hundreds or thousands of times) where a channel's recent uploads collapsed or its normal rests on a handful of videos.
- **The faceless side is full of near-identical titles across channels.** A big outlier there may owe as much to the channel, the thumbnail or timing as to the topic.
