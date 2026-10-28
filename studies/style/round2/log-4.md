# Round 2, helper 4: log

Worklist: `round2/worklist-4.csv` (59 channels: 33 kept, 26 to-screen). Run date 2026-10-28.

## NexLev calls (running count)

- 01 Justin Hickox: outliers + videos = 2 calls (total 2)
- 02 Style with Cathy: 2 calls (total 4)
- 03 Boys And Girls Hairstyles: 2 calls (total 6)
- 04 Risa Does Makeup: 2 calls (total 8)
- 05 Dominique Sachse: 2 calls (total 10); outlier tool returned 0 outliers
- 06 Jodi Mannes: 2 calls (total 12)
- 07 Kim Sullins: 2 calls (total 14)
- 08 Mature Makeup Masterclass: 2 calls (total 16)
- 09 Camille Cowher: 2 calls (total 18); outlier tool returned 0 outliers
- 10 Julie Catherine: 2 calls (total 20)
- 11 SimplySharon: 2 calls (total 22)
- 12 Tamara's Timeless Beauty: 2 calls (total 24)
- 13 Beauty and the Boutique: 2 calls (total 26); outlier tool returned 0 outliers
- 14 Stung by Samantha: 2 calls (total 28)
- 15 Claudia Glows: 2 calls (total 30)
- 16 Elegántica: 2 calls (total 32)
- 17 The Beauty Armor: 2 calls (total 34)
- 18 TRENDS SPOTTED FASHION: 2 calls (total 36). Note: 2 earlier attempts used the wrong parameter name and were rejected by the tool schema before reaching NexLev; not counted. proc.py now excludes 0-view uploads from normal and says so in normal_basis (from row 18 on).
- 19 Glow At Any Age: 2 calls (total 38)
- 20 Sachiko Mori: 2 calls (total 40)
- 21 Belleza Sin Edad 60+: 2 calls (total 42)
- 22 Over 60 Lifestyle: 2 calls (total 44)
- 23 The Style Edit: 2 calls (total 46)
- 24 Ageless Glow: 2 calls (total 48)
- 25 Stil Mit 50+: 2 calls (total 50)
- 26 ELEGANCE AFTER 60.: 2 calls (total 52)
- 27 Second Bloom: 2 calls (total 54)
- 28 Chic & Timeless: 2 calls (total 56)
- 29 Age with Style: 2 calls (total 58)
- 30 Ageless Style 50s & 60s: 2 calls (total 60)
- 31 Haircut for Women Over 45: 2 calls (total 62)
- 32 Elegancia Atemporal: 2 calls (total 64)
- 33 Older Line Podcast With Penelope: 2 calls (total 66)
- 34 Casual Comfort: 3 calls (total 69)
- 35 Stylish Beyond 60: 3 calls (total 72)
- 36 Stylish haircuts: 3 calls (total 75)
- 37 Chic60Plus: 3 calls (total 78)
- 38 Mature Women's Style: 3 calls (total 81)
- 39 Stylish Over 60 Plus: 3 calls (total 84)
- 40 Traci Jeske: 3 calls (total 87)
- 41 After 60 wardrobe: 3 calls (total 90)
- 42 ziliottodesign: 3 calls (total 93); outliers result was saved to a tool-results file by the harness and parsed from there
- 43 Timeless Style After 60: 3 calls (total 96)
- 44 Ageless Chic: 3 calls (total 99)
- 45 Michelle Shelly / Fashion over 60: 3 calls (total 102)
- 46 The Style Insider: 3 calls (total 105)
- 47 Glow at Every Age: 3 calls (total 108)
- 48 Chic Over 60: 3 calls (total 111)
- 49 Melanin Majesty: 3 calls (total 114)
- 50 Feminine Over 50 With Mia: 3 calls (total 117); faceless check was a fresh analysis (not cached)
- 51 Wraparound Plus: 3 calls (total 120); faceless check was a fresh analysis
- 52 Daily Black Glow: 3 calls (total 123)
- 53 Erica Taylor Beauty: 3 calls (total 126); faceless check was a fresh analysis
- 54 Gray Hair Transition and Beyond: 3 calls (total 129); faceless check was a fresh analysis; keep set to no by hand (last upload '1 year ago', on the 12-month line)
- 55 Timeless After 50 (now 'The Receipts And Reality'): 3 calls (total 132); 0 outliers returned
- 56 The Life Of Hair: 3 calls (total 135); faceless check was a fresh analysis
- 57 Styles By Summer: 3 calls (total 138); faceless check was a fresh analysis
- 58 Pampered Wolf: 3 calls (total 141); faceless check was a fresh analysis
- 59 Stylish Curves: 3 calls (total 144); faceless check was a fresh analysis

## Summary

- Channels done: 59 of 59 (rows 1-59 in `channels-4.csv`, same order as the worklist; no duplicates). Outlier rows: 373 in `outliers-4.csv` (core 253, adjacent 89, off 31).
- NexLev calls used: 144 of 180 (33 kept rows x 2, 26 to-screen rows x 3). No call failed and no limit or credit error came back. Two calls at row 18 were rejected by the tool schema before reaching NexLev (wrong parameter name) and are not counted.
- Keep result: 41 kept, 18 not kept. Of the 33 worklist 'kept' rows, 31 stayed kept; of the 26 'to-screen' rows, 10 were kept.
- Type split (all 59): faceless_narrated 29, real_on_camera 25, ai_avatar 3, mixed 2. Kept only: faceless_narrated 19, real_on_camera 18, ai_avatar 3, mixed 1.

### Not kept, with reasons

| # | Channel | Reason |
|---|---|---|
| 23 | The Style Edit | 3,710 subs, top 28K |
| 31 | Haircut for Women Over 45 | 989 subs, top 8.5K |
| 37 | Chic60Plus | 685 subs, top 33K (young faceless, needs 50K) |
| 38 | Mature Women's Style | 60 subs, top 1.4K |
| 39 | Stylish Over 60 Plus | 191 subs, top 8K |
| 40 | Traci Jeske | 468 subs, top since 2022 1.2K |
| 41 | After 60 wardrobe | 8 subs, top 284 |
| 42 | ziliottodesign | 3,090 subs, top 14K |
| 43 | Timeless Style After 60 | 625 subs, top 6.1K |
| 44 | Ageless Chic | 12 subs, top 1.1K |
| 45 | Michelle Shelly / Fashion over 60 | 6,490 subs, top since 2022 41K |
| 49 | Melanin Majesty | 9,740 subs (just under 10K), top 64K; joined 2025-02, so the young rule does not apply |
| 51 | Wraparound Plus | 5,980 subs, top 39K |
| 52 | Daily Black Glow | 31 subs, top 729 |
| 53 | Erica Taylor Beauty | no upload in 12 months (last about 2024-10) |
| 54 | Gray Hair Transition and Beyond | newest upload shows '1 year ago' (on the 12-month line); keep set to no by hand, flagged borderline |
| 55 | Timeless After 50 (now 'The Receipts And Reality') | 5,530 subs, single video 97K (just under 100K) |
| 56 | The Life Of Hair | 119K subs but no upload in 12 months (last about 2024-10) |

### Odd items

- All dates come from NexLev relative times ('1 month ago' and so on), so they are approximate. Many uploads share the same date, and the since-2022 test is approximate for '4 years ago' videos.
- Videos-tab metadata often reports '31' videos whatever the real count. Some channels put Shorts-length uploads on the videos tab (row 53 is entirely 1-3 min videos, so normal could not be computed). The Shorts tab was not checked.
- Outlier scans cover only the 100 most recent videos. Four channels returned 0 outliers (rows 5, 9, 13, 55).
- Some uploads returned 0 views and are left out of normal (noted in normal_basis).
- Row 42's outlier result was too large for the tool output and was read from the saved result file.
- A cluster of new over-60 faceless channels share titles word for word and use generated women in their thumbnails: rows 19, 24, 29, 30, 35, 37, 38, 39, 41, 43, 44, 47, 48, 49 and the single video on 55. Examples: 'How To Style Wide-Leg Pants and look Elegant', 'Stop Buying More Clothes: 7 Elegant Wardrobe Essentials for Women Over 60', '10 Elegant Shoes For Women Who HATE Heels', '9 Swaps to Make Your Fall Outfits Look Modern in 2026', 'DON'T Get a Granny Cut'. Row 43 uploads the same title several times under different ids.
- NexLev's faceless check often reads generated faces as 'not faceless' (rows 35, 37, 38, 39, 43, 48, 49, 55). It reads row 56 (a hairdresser filming clients) as faceless.
- Rows 33 and 50 rest on posed photos of women in stockings and short dresses framed as '50+ fashion'. All their outliers are marked off on an audience reading. Row 50 is kept on the 100K rule (129K). Both are flagged for main-session review.
- Row 55's channel id now carries another name and topic (cost-of-living commentary) with one haircut video left.
- Row 53 may be an older account of kept row UCTxMakpAk-pNwySUepxS3SQ (worklist note; not cross-checked).
- Row 27 (Second Bloom) is kept only on the young-AI rule, so the keep depends on the ai_avatar reading.
- Row 54's keep was set by hand against the script's 365-day arithmetic.
- Several channels build thumbnails from other people's photos (rows 28, 36, 42, 46, 59, reading).
- Thumbnail text does not match the title on rows 41, 52 and 58.
