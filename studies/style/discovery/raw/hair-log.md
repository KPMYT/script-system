# Discovery log: HAIR lane (women 50+/60/70, English)

Date: 2026-10-28. Discovery helper, lane B (hair). Tools: NexLev only (search_niche_finder_channels, youtube_search, get_similar_channels + get_similar_channels_status, youtube_channel_videos, check_faceless_channel, youtube_channel_about). No web search. No git.

Output: `studies/style/discovery/raw/hair.csv` (one row per kept channel, sorted by subscribers).

## Totals

- Unique channels found across all searches: **710** (stored in a scratch candidate file).
- Shortlisted as possibly hair + mature-women relevant (from title/description/video titles): **93**.
- **Screened** (keep rule checked against channel data): **64**, made up of **50 kept** and **14 screened out**.
- Own channels found and excluded (not counted): 2 (Scarlet Starling, Diane de Chambray).
- Shortlisted but not screened (out of budget): 31, listed below.
- Kept by type: real_on_camera 28, faceless_narrated 9, unclear 5, ai_avatar 5, mixed 3. Real on camera 28 vs faceless/AI/unclear/mixed 22.
- Kept by lane: hair 27, fashion+hair 14, makeup-adj 6, lifestyle-mixed 2, fashion 1.
- Kept by audience_fit: core-50plus 35, partly 15.

## Rules applied (from study-brief Phase 2)

- Candidate: English channel where women 50+ are the main audience or a major share of videos. Broad channels count only when mature-women videos are a large share of their winners.
- Keep: uploaded in the last 12 months AND (10K+ subs OR any video since 2022 with 100K+ views). Faceless/AI channel under one year old: kept with any video at 50K+.

## Searches

Counts: `returned` = results the call gave back; `new` = channels not already in the candidate set. Niche Finder (NF) queries were semantic with no sortBy; `hasMore=True` means more results existed.

| # | Tool | Query / seed and filters | Returned | New | Notes |
|---|---|---|---|---|---|
| 1 | search_niche_finder_channels | haircuts for women over 60 (p1, limit 20) | 20 | 20 | hasMore=True |
| 2 | search_niche_finder_channels | haircuts for women over 60 (p2) | 20 | 20 | hasMore=True |
| 3 | search_niche_finder_channels | gray hair transition going gray naturally (limit 40) | 40 | 20 | hasMore=True |
| 4 | search_niche_finder_channels | silver hair styling for women over 50 (limit 40) | 40 | 5 | hasMore=True |
| 5 | search_niche_finder_channels | hairstyles that make older women look younger (limit 40) | 40 | 3 | hasMore=True |
| 6 | search_niche_finder_channels | short haircuts for mature women (limit 40) | 40 | 4 | hasMore=True |
| 7 | search_niche_finder_channels | thin fine hair over 50 best haircut (limit 40) | 40 | 8 | hasMore=True |
| 8 | search_niche_finder_channels | pixie cut older women (limit 40) | 40 | 2 | hasMore=True |
| 9 | search_niche_finder_channels | bob haircut over 60 (limit 40) | 40 | 5 | hasMore=True |
| 10 | search_niche_finder_channels | hairdresser makeovers for older women (limit 40) | 40 | 2 | hasMore=True |
| 11 | search_niche_finder_channels | hair color for women over 50 (limit 40) | 40 | 2 | hasMore=True |
| 12 | search_niche_finder_channels | hair mistakes that age you (limit 40) | 40 | 3 | hasMore=True |
| 13 | search_niche_finder_channels | hair stylist tips for mature clients (limit 40) | 40 | 3 | hasMore=True |
| 14 | search_niche_finder_channels | short hairstyles for women over 70 (limit 40) | 40 | 0 | hasMore=True |
| 15 | search_niche_finder_channels | gray hair blending highlights instead of dye (limit 40) | 40 | 10 | hasMore=True |
| 16 | search_niche_finder_channels | thinning hair menopause women hair loss (limit 40) | 40 | 11 | hasMore=True |
| 17 | search_niche_finder_channels | layered shag haircut women over 50 (limit 40) | 40 | 1 | hasMore=True |
| 18 | search_niche_finder_channels | wigs and toppers for women over 60 with thinning hair (limit 40) | 40 | 1 | hasMore=True |
| 19 | search_niche_finder_channels | hairstyles for women over 50 tips from a hairdresser (isFaceless=false, limit 40) | 40 | 17 | hasMore=True |
| 20 | youtube_search | haircuts that make women over 60 look younger (type=video) | 19 | 14 |  |
| 21 | youtube_search | hairstyles that age you over 50 (type=video) | 7 | 5 |  |
| 22 | youtube_search | best haircut for thin hair over 50 hairstylist (type=video) | 9 | 5 |  |
| 23 | youtube_search | going gray gracefully transition journey (type=video) | 11 | 10 |  |
| 24 | youtube_search | short hairstyles for women over 70 (type=video) | 8 | 6 |  |
| 25 | youtube_search | haircut transformation older woman makeover salon (type=video) | 7 | 5 |  |
| 26 | youtube_search | silver hair care toning purple shampoo gray hair tips (type=video) | 11 | 7 |  |
| 27 | youtube_search | best hair color for women over 50 to look younger colorist (type=video) | 15 | 12 |  |
| 28 | youtube_search | pixie haircut tutorial woman over 60 (type=video) | 12 | 5 |  |
| 29 | youtube_search | my gray hair routine over 60 styling tips (type=video) | 9 | 4 |  |
| 30 | youtube_search | bob haircuts for women over 60 that take years off (type=video) | 12 | 7 |  |
| 31 | youtube_search | gray hair transformation silver hair color salon older woman (type=video) | 7 | 4 |  |
| 32 | youtube_search | hair tips for women over 50 from a hairdresser (type=video) | 4 | 3 |  |
| 33 | get_similar_channels (+ _status) | level 2 seed Justin Hickox | 94 | 63 |  |
| 34 | get_similar_channels (+ _status) | level 2 seed Glam Girl Gabi | 106 | 85 |  |
| 35 | get_similar_channels (+ _status) | level 2 seed Boys And Girls Hairstyles (RaDona) | 60 | 28 |  |
| 36 | get_similar_channels (+ _status) | level 2 seed Woman in midlife | 95 | 71 |  |
| 37 | get_similar_channels (+ _status) | level 2 seed Summer Beauty | 88 | 71 |  |
| 38 | get_similar_channels (+ _status) | level 2 seed Elegant After 60 (UC1eIO) | 122 | 71 |  |
| 39 | get_similar_channels (+ _status) | level 2 seed Rami Jabali Hair Salon | 79 | 52 |  |
| 40 | get_similar_channels (+ _status) | level 2 seed Katie Goes Platinum | 94 | 45 |  |

Per-channel calls on top of the searches: `youtube_channel_videos` (sort_by=popular, first page of 30) for most screened channels, `check_faceless_channel` for every kept channel, and `youtube_channel_about` / similar-channels "about" data for country, joined date, total views, video count and last upload.

## Failures

- No NexLev call failed outright, so no retry-then-skip was needed.
- `get_similar_channels_status` sometimes returned `in_progress`; it was polled again until complete.
- Large Niche Finder outputs were saved to scratch files and parsed there. An early parser bug (wrong JSON key) was fixed and the files were re-parsed; no data was lost.

## Method notes (read before using the numbers)

- **Views are rounded** by the channel-videos tool (for example 1.1M, 601K). Some exact counts come from search results or the Niche Finder.
- **Dates are approximate.** The videos tool gives relative dates ("1 year ago"), mapped back from 2026-10-28, so "1 year ago" becomes 2025-10 and "3 years ago" becomes 2023-10. A video dated "4 years ago" might be from before 2022, so it was not counted toward the 100K-since-2022 rule and was left out of the top 3 (top-3 columns only list videos counted as 2022 or later).
- **Top 3** = the three most-viewed long-form videos since 2022 in the first page of the popular sort (30 videos). For channels found through the Niche Finder, the NF "top videos" list (sorted by views) was used where it covered this. A few channels show only one top video because only one video from 2022 or later appeared in their popular top 30; the notes column explains each.
- **uploads_last_90d:** the newest sort was skipped for most channels to save calls. Where it was not fetched, the column says "n/a (newest not fetched)" or gives a minimum counted from the popular list. A "3 months ago" date was treated as outside 90 days.
- **last_upload** comes from the newest sort when fetched, otherwise from the "last video X ago" field in similar-channels data (marked with ~ when it is approximate).
- **est_monthly_revenue / rpm_est** come from the Niche Finder and are only filled for channels it returned; they are blank elsewhere. They are NexLev estimates of AdSense only.
- **Country** is blank where NexLev had none.
- **Type disputes:** NexLev `check_faceless_channel` is recorded as given (nexlev_faceless, nexlev_confidence). `type` is the reading of title, description and format:
  - Niche Finder edit tag = ai_avatar but faceless check = not faceless → `ai_avatar` (the check counts an avatar presenter as a face).
  - Brand-voice "women over 60" channels with faceless check = not faceless but no named human host → `unclear` (noted "likely AI presenter").
  - Salon haircut-transformation compilations with no host → `mixed` (Her Hair, Mind blowing Hair, Haircut for Women Over 45).
  - Tarantula (its own salon footage, stylist voice, no presenter) → `real_on_camera`, though NexLev says faceless. Disputed; see its notes.
  - Trendy Short Hairstyles LookBook is a photo-slideshow compilation with no host. `faceless_narrated` was the nearest allowed value, though it may have no narration.
- **Commenter usernames:** none were collected or stored.

## Kept channels (summary; full data in hair.csv)

| Channel | Subs | Type | Lane | Fit | Top video views |
|---|---|---|---|---|---|
| HotandFlashy | 1230000 | real_on_camera | makeup-adj | core-50plus | 263000 |
| Nikol Johnson | 1180000 | real_on_camera | makeup-adj | core-50plus | 5800000 |
| Glam Girl Gabi | 782000 | real_on_camera | hair | core-50plus | 3100000 |
| Justin Hickox | 694000 | real_on_camera | hair | core-50plus | 3200000 |
| Boys And Girls Hairstyles (RaDona) | 234000 | real_on_camera | hair | core-50plus | 1173420 |
| Tarantula | 204000 | real_on_camera | hair | partly | 1400000 |
| Kerry-Lou | 182000 | real_on_camera | makeup-adj | core-50plus | 333000 |
| Chic After 60 | 115000 | unclear | fashion+hair | core-50plus | 956000 |
| Rami Jabali Hair Salon | 113000 | real_on_camera | hair | partly | 1625510 |
| Summer Beauty | 108000 | real_on_camera | hair | partly | 1200000 |
| Karen of Curl House | 106000 | real_on_camera | hair | partly | 425000 |
| Mindful Midlife | 103000 | real_on_camera | lifestyle-mixed | core-50plus | 890000 |
| Age with Style | 89600 | ai_avatar | fashion+hair | core-50plus | 1100000 |
| UnBlah Yourself | 88400 | real_on_camera | fashion | partly | 658000 |
| The World Of Craig | 70000 | real_on_camera | hair | partly | 294000 |
| Trendy Short Hairstyles LookBook | 55300 | faceless_narrated | hair | partly | 1100000 |
| Stylish60plus | 52300 | faceless_narrated | fashion+hair | core-50plus | 418000 |
| Style over 60 | 52200 | faceless_narrated | fashion+hair | core-50plus | 392000 |
| Deepa Berar | 44400 | real_on_camera | hair | partly | 49000 |
| Wellness 360 | 44200 | faceless_narrated | fashion+hair | core-50plus | 649000 |
| SimplySharon | 42400 | real_on_camera | hair | core-50plus | 41000 |
| Elegant Older Women | 27900 | faceless_narrated | fashion+hair | core-50plus | 406000 |
| Locks by Lauryn | Grey Blending Specialist | 27600 | real_on_camera | hair | partly | 93000 |
| Ageless Style 50s & 60s | 27100 | unclear | fashion+hair | core-50plus | 495000 |
| The Beauty Debut | 25700 | real_on_camera | makeup-adj | core-50plus | 170000 |
| Mind blowing Hair | 25400 | mixed | hair | partly | 854000 |
| Ebony lifestyle | 25100 | unclear | fashion+hair | core-50plus | 451000 |
| Kathleen Benjamin | 23100 | real_on_camera | makeup-adj | core-50plus | 656000 |
| The New Knew | 22000 | real_on_camera | hair | partly | 32000 |
| Her Hair | 20400 | mixed | hair | partly | 1000000 |
| Tanja | 20000 | real_on_camera | hair | core-50plus | 754000 |
| Go Gray Be CHIC | 19800 | real_on_camera | hair | core-50plus | 226000 |
| Katie Goes Platinum | 19400 | real_on_camera | hair | core-50plus | 530000 |
| Woman in midlife | 18900 | real_on_camera | hair | core-50plus | 628904 |
| Silver Foxy | 18700 | real_on_camera | hair | partly | 127000 |
| Kim Sullins | 17900 | real_on_camera | makeup-adj | core-50plus | 334000 |
| Style In Her Prime | 16700 | unclear | fashion+hair | core-50plus | 601000 |
| Grayawhile | 16000 | real_on_camera | hair | core-50plus | 267913 |
| Glow After 60 | 16000 | faceless_narrated | fashion+hair | core-50plus | 363000 |
| Elegant After 60 | 13000 | faceless_narrated | fashion+hair | core-50plus | 698000 |
| ChicAfterSixty | 12500 | ai_avatar | fashion+hair | core-50plus | 492000 |
| SparklingSilvers | 12100 | real_on_camera | hair | partly | 125000 |
| chery 🍒 | 10500 | real_on_camera | hair | partly | 103000 |
| Alice Luxe | 9370 | unclear | hair | core-50plus | 490000 |
| Lisa beauty | 7230 | ai_avatar | lifestyle-mixed | core-50plus | 324000 |
| Rosalind Gray | 7070 | ai_avatar | fashion+hair | core-50plus | 158000 |
| AgelessStyleTips | 6950 | ai_avatar | fashion+hair | core-50plus | 136000 |
| Elder Insights | 6550 | faceless_narrated | hair | core-50plus | 222000 |
| Golden Elder Days | 4960 | faceless_narrated | hair | core-50plus | 156000 |
| Haircut for Women Over 45 | 987 | mixed | hair | core-50plus | 348000 |

## Screened out (with reasons)

| Channel | Channel ID | Reason |
|---|---|---|
| 10 Years Younger (Jay) | UCVf4gEACUWpQEv0DiGNoxMw | 47.8K subs; real (UK male presenter); anti-ageing/biohacking (earthing, hydrogen water, men hair transplant). Not a women-50+ channel; gray-hair video 127K is one-off. Fails candidate definition. |
| Beauty Palace New | UCZUnnt32yurPuepH--IiS2g | 469K subs; salon-transformation compilations (all ages, 15-in-1 makeovers) + old SFX makeup; one mature winner (The Haircut That Took 20 Years Off Her Face 1.3M, 2026-05) but mature-client videos are not a large share of winners -> broad, not a candidate. Likely compilation/reupload format. |
| Evelyn Hart | UC35beahevoTdl2bGIBW7S3A | AI-avatar, created 2026-09-07, 235 subs, best video 23K (<50K needed for under-1-year faceless rule). |
| Style After Sixty | UCTSYeyREkFQQYvtazAIeESQ | AI-avatar, created 2026-07-26, 1.21K subs, best video 23K (<50K). |
| Latest Trendy Hairstyles | UCPZ9n4OllCrIbHkW5mc4NMw | 590 subs; last upload 1 year ago (outside 12 months); Türkiye-based hairstyle slideshow channel. |
| Her Glory Gray Hair | UCZ_-ybMqmETX6kFQT8L-y6w | 145 subs; 36.6K total views across 63 videos (no 100K video possible); gray-hair tips in 60 seconds (Shorts-style). |
| Graceful & Glowing 60+ | UCV_ZJuDD_rXcHZ22DF-K7mg | Created 2026-09-14; 5 videos, 21 total views. |
| Hair with Darlene | UCX5haM5j_LQ7GUuqntD2-8w | Created 2026-09-20; 14 subs, 5K total views (stylist for women 60+; too new). |
| Golden Aura Fashion | UCgVEle2Vc_sRmk-VHY-6MCQ | Created 2026-02-25; 511 subs, 36.4K total views (no 50K video possible). |
| TimelessTresses | UCP6SgMd_gnHcqf26Iios72w | 1.68K subs; 159.6K total views across 64 videos; created 2021 so needs a 100K+ video - not verified video-by-video (total views make it unlikely). |
| Hair Explore | UCqwuF0EhPt5V-tVQ2azw81g | Italian-language channel (description in Italian), 10 videos, 17.9K total views - not English, no qualifying video. |
| Have A Good Hair Day | UCd2FGxSAChWUjP01st1ieAw | Real hairstylist (Laura), 12.4K subs, active; winners are all-age DIY/colour tutorials (BIXIE haircut 789K, DIY dye 310K) - mature-women videos not a large share of winners -> broad, not a candidate. |
| Free Salon Education | UCeasbjVyx227l2ETO-xAssw | Broad stylist-education channel (1.09M); none of its top 30 videos are aimed at mature women |
| All About Hair with Danise | UCRnK2oqHpFlujagG0osFYFg | Stylist-education channel (7.8K); top videos are about thinning shears and technique; no mature-women videos among its winners |

## Own channels excluded

- Scarlet Starling (UCTMwV-uy20eaRwFfc4Sx13g): operator's own channel; found in searches and excluded.
- Diane de Chambray (UC2z5yffdjwr3xpr-iDp9Yvw): operator's own channel; found in searches and excluded.

## Shortlisted, found but not screened

These looked possibly relevant but their keep rule was not checked. Figures are from similar-channels "about" data where it existed; "no data" means only the ID and name were captured.

| Channel | Channel ID | Subs | Last upload | Country | Note |
|---|---|---|---|---|---|
| Infinite Garden by Beth K | UCDO9emSTIB01KhWk7lCB3XQ | 10500 | 6 months ago | United States | style & beauty, 10.5K subs; last upload 6 months ago |
| MAKEOVERGUY | UCPbPMpLLXu45J_K1mWyXXCQ | no data |  |  |  |
| Joli Campbell ~ QuickSilverHair | UC2TlUxfpRWHZ1XEGJ8BqnKA | 8800 | 1 month ago | United States | silver-hair creator since 2015; 8.8K subs; needs a 100K-since-2022 check |
| Gray Hair Transition and Beyond | UCb0nbyCEC6XCZr3caEOUsoQ | 4180 | 10 months ago | United States | gray-hair transition; 4.2K subs, 1.29M total views; last upload 10 months ago; needs a 100K-since-2022 check |
| Living Your Best Life | UCxzXdTKlMueaJFGGm2nB0QQ | no data |  |  |  |
| Megan Graham | UCuTEzIC9y2GgROcTZCIfFyg | no data |  |  |  |
| The New Narrative | UCF15aSqFpJeBc9lf27_BnKw | 8110 | 53 minutes ago | Canada | midlife lifestyle, Canada |
| Loving Our Age | UC9qvp__gu8s1B4OCM5O9YRQ | no data |  |  |  |
| Only Hairstyles | UCv41YRs8uNfTVCwlkUi9RHA | 3200 | 3 hours ago | Türkiye | Türkiye; created 2025-06; hairstyle ideas |
| Stylish Beyond 60 | UCIG0YdmteAJBkqOFTyAPgdg | no data |  |  |  |
| Bloom After 60 | UCIV9PRIncsJkwkfs_OZ_2Dw | no data |  |  |  |
| Timeless After 50 | UCCxTLaiWCys3lVCuIZ8Yq7g | no data |  |  |  |
| Crowned in Elegance | UC0GOZj66XJyl8fb3Zk9K5_g | 3230 | 1 day ago |  | style for women over 50/60; 3.2K subs, 149K total views (a 100K video is unlikely) |
| Casual Comfort | UC1Ev-v3_A-yqIOVmTQEmn0g | no data |  |  |  |
| Hairstyleslife | UChXfKuZiQZaulUbU49dAdZg | 30900 | 2 months ago | Türkiye | Türkiye; men+women hairstyles per description |
| Glam Guide | UC6zvRQP_BiTcR8dxQ7QfIJQ | 2120 | 1 month ago | India | India; 2.1K subs |
| Solo After Sixty | UCbLBebIpWT7IUEWz0k6l4xg | no data |  |  |  |
| Good Dreams Only | UCxJh-6IG_Eka3P9R7z3KVfg | 38000 | 2 weeks ago | United States | colour psychology/style for women 40+ |
| Hairstyles cutting fashion | UCLj7XnpsXScuwDUPCpeCbpQ | 28300 | 5 hours ago |  | hairstyle compilations; audience not checked |
| The Life Of Hair | UCFicQVyEhEhC7kM9-0hcLNA | 119000 | 11 months ago | United Kingdom | UK hair tutorials; last upload 11 months ago (just inside 12 months) |
| Hair Cut | UCMt07WXo9DRKuUnMEIP7yFA | 134000 | 2 days ago | Vietnam | Vietnam-based hair compilations; language/audience not checked |
| Fashionistas | UCWIwBH_wgzRYJx7k7cjdexA | 420000 | 1 month ago | United States | broad beauty per description |
| Ana Vogue | UCcai-ND1haM-bJtkOz_7oPA | 51100 | 17 hours ago | United States | fashion for mature women per description (fashion lane) |
| 10 Years Younger | UCViorfQaEoD32u0gWqmhwLA | 27300 | 33 minutes ago | United Kingdom | UK makeover brand channel (TV format), created 2026-01 |
| Prime of your life | UCxNI-S9TXSUjR2JS1Se9krQ | 14900 | 1 month ago | New Zealand | women after 40, NZ |
| Life Styled After 50 | UCIwwxZcVs_0GIftK9soi0bA | 7510 | 1 day ago | United States | over-50 variety show (beauty, style, home) |
| Styles By Summer | UCTFVVLBy2xGQ3ThRgcSbMZQ | 374000 | 2 weeks ago | United States | broad hair/product reviews per description |
| Blowout Professor | UCX_gtN8XsErdLPOUkEPaqiA | 1050000 | 1 month ago | United States | broad hair channel per description; mature share unknown |
| Turmeric Me Crazy | UC0KlJOYsf7eDRchMQKd2rrg | no data |  |  |  |
| Confident Beauty 50+ | UChunxvx8KLvtBfg2h346cjg | no data |  |  |  |
| Little Miss Fashion | UCgNM2WAawiUYGz4reoUrDgg | no data |  |  |  |

## Not shortlisted (found, judged non-candidates on sight)

617 channels, by source: similar-channels 461, niche finder 121, youtube search 35. These were set aside from their name, description and video titles without a keep-rule check. The main groups:
- 50+/60+ **fashion-only** channels with no hair winners (for example Ageless Style Over 50, Stylish Over 60, Refined After 60, Mature Vogue). These belong to the fashion and faceless/AI lanes and were left to those helpers.
- **General / younger-audience** hair and beauty creators (for example Brad Mondo, Valeria Lipovetsky, Hannah Hall makeup).
- **Men's** style/grooming (for example Mr. Gent Style Over 50).
- **Non-English** channels (German "Stilvoll ab 60", Spanish "Belleza Serena", Japanese, Hindi and others).
- **Off-topic** similar-channel noise (Bible audio, mindset academies, entertainment compilations).
Full list (name | channel ID) follows so other lanes can check for duplicates.

<details><summary>Not-shortlisted channels</summary>

- Stil kennt kein Alter | UCdsbpdB0GuhrT3Ruw2LhnAQ
- Style After 60 | UCCac3e7jjjwD4SZdprJRmxA
- Stilvoll ab 60 | UChWRWvHXc81-jrzofzHAjag
- Novokumar Ghosh | UC7lD1HImfYEbMZSAih1ibkQ
- Styled Beyond 60 | UCr55Tkbou2vwDw01fzGOdtQ
- Ashley Grant | UCgXvIOk7meBAmy-dxQ4M2Dg
- Senior Fashion Styles | UCtVEmEvt7KPIzhtmRNCojlQ
- KlarerBlick | UCkb483SvyY4lmP8YQ9FB70A
- Belleza Sin Edad 60+ | UCiEy8lbUxoKiPKB3ZFjsQSQ
- Shifted Mind Academy 50+ | UC1QQoJrY2q9lbMFAWHFSfFA
- The Mirror Edit | UCLTXZUZ7Sme8zekDHihbd2g
- L’Âge du Style | UCXVKNeABG8f5shd_aNc0GCw
- Golden Chic Life | UCB34i2i0LGm9oC7jKGGg62A
- Elegant Sein | UCZzfcxL6u0LZGHOZbS9MkTg
- Senior Fashion Class | UCfqm-owzftN8K4KxeTF5trA
- Elegant After 60 | UCn4q5n4EbawoOKOL_FK2tPg
- Camino de los Ancianos | UCy0Y3ykT36UiCZBEDpXmUnw
- Timeless Style Living | UCMloBTH0nDTwGkN4DMnqHKQ
- Stil Mit 50+ | UCfOKRSLxASH9WFWHQR36XGg
- BeautybyJaiy | UCrTEih9idLuwzi31sBOP_-A
- Grace Sydney | UCp3eZ4nK0WMS0UlR4Yc23KA
- Vivian Sinclair | UCfDezkF4P9FNxrD6PFGCoPw
- All About Fashion | UC_Qai9ySieOdLhWc8nKWaeQ
- Elegant Fashion And Style Over 60 | UC8rJqI3YGdgUcZVHILLSqvw
- Elegant Style After 50 | UCvkFS5ZG8smI8VfKVYb3AbA
- Bienvenue sur Élégance 60+ | UCFGU_g0-AwFEu_XHS1kbhkQ
- Mature Vogue | UCOZXt7lvi4moRYUIllvS0ug
- Aging Smarter | UCu67IiiiS2m0ibjfIV8sXww
- dangcongthan dangcobgthan | UCQXAU70bWa4BXzxbaHbqZhA
- Marina Burrage | UCTfURjPtausbrP71gyKg4lQ
- Ageless Glow | UCaXJaaiglTONpkU7mKBlY6g
- Aging Queens | UC0uabQ9Zs6bDpr1n-gqR3MQ
- Hana et toi | UCxio3MI6RSj9verf9Sf4-FQ
- El Hogar de Graciela Vega | UC14VCA72xkah53_7Bbsr9qg
- 50plusdaily | UCOnqnvlRmWaSlwt51QpYQ8A
- Gentleman Post | UC5vfB78wka0I_CAdHeql7Xw
- me_heavenli | UCeV7CR3bp3EsVTLSFDuWHNg
- Sarah Troyer | UCnVNWhvlg2GvGo3SibMS8rQ
- Fade Guide | UCMUrva07PktxsP1Pyz3auNQ
- Golden Age Wisdom | UChH9waS1-DppeJ2fhC5Adzg
- Glowup Guy | UC9_qPrbrgECt71ipqZkkl0Q
- Shivan Kay | UC_2TSCz99saIbP52aUhDY8w
- Bloom With Alex | UCeF8bpMh3RNXEEUdQPnnJmA
- Bobbie.grl_ | UC8GRZYI3SngrPGdB_fh3S6Q
- Melanin Beauty Over 50+ | UChVU3135PhjH6UTRmoEpgaQ
- Ethereal Elegance | UCcrzDxoyhz_GQHQzzkN4acw
- Estilo Después de los 50 | UCLBgPjRjCOwvjRzs6bMCoJA
- Mode und Stil 50+ | UCSarPoUqrV5fNvufTXgTvdg
- Ageless Style Icons | UC4iMSCYpbu6kG8Lia46j77Q
- HouseOfElegance | UCa9KQyun6e1uB6iJl2fCgYg
- Clemons Hays | UCjPCcws3t6EZxptwmZgYDNQ
- Vien Tran | UCbhdAaeCUpADCaAKvK9Jc-g
- Ageless Queens | UCgC-uVXN5nb6jw-uvNDTyzA
- CougarFashion | UCmdXZnICr_pgtqwOgcAKYIQ
- The Style Edit | UChUXkf73JXhf9EHMChpB7EA
- Beautybyemily | UCRZZQL0jQ0aipT6pWKPNDng
- rockstarcheveux | UC00MBBC-JH7zM0yz02vvWrw
- FATAMORGANA_1289 | UCjZv_VWbXoqt77Hn23SMT_A
- CODIGO ALFA 40+ | UCO00FFziduq8Cnb4x3TUlNg
- Tomb45 | UCpui-V36iJcXBffKmxlHYKw
- 50+ Men's Style | UC-_zbheM4YPHE4E8Vqux2eg
- Gentleman's Edit | UCUM0SHTKiI-kBE8QkhKfqIA
- Healthy Over 40 | UCzKSuXXH9QNAIK0fn913mRQ
- Bold & Styled | UCtdx6KngcAGi4XKlVkQHcoA
- Mr. Gent Style Over 50 | UCVTShoJ7vBF4awDMcZK3aXA
- Ms. BoBo | UCHkz976V7OzqZtu8aZ2xPdw
- ICONIC - WOMEN OVER 50 | UCXfUl8O2X6OKVvm4TvKlJug
- Hass Barber | UC1eLO9x2mRrzZfjzHiaKNYw
- Loscuts | UCvuh4MICg6swIC2KYmQt9Lg
- Gentleman After 40 | UC4uF9yUiplXLJh9UDuKm3tg
- UBarber Academy | UCLqixpNgq0BgBRsfawWi9WA
- Caballero Clásico | UCJwT0QkOPQ2D7IedFiZg2uw
- Aicha professional hair | UCQDdOqj0P5zYzHDxAQSW0qQ
- Éclat Melanin | UCdfQxG929RKxiWxppRDj0JA
- Elegance At 60 | UCGhT9pJVlUY0SwhDRkQoyKg
- Natalie Paterson | UCKKDzoxS74kkcxHtA_ByKOA
- Yuna Han | UCUCOJO5MxvVeFzDaSm-c6rA
- Build-A-Girl | UC9boCO6tQ-92IOcv8Qs3vrw
- hoorain salon | UCeJUHt6GhuxXO3AK7w4LyaQ
- Beautyatwill | UC1bjNgihlwzqAJFvRLhri-A
- Rachel McKeown | UCTs0s3oFjPPkpPzO61yK6Pw
- harry blends | UCc5MSmIx-pROLCviehbvlLw
- George.Colorist | UC6uSvyoNvBzVXrroorjL0XA
- blueblends | UCpu4w5nVVJwkYJkRPFHzrJA
- The Blend Factors | UCY3s8SpKxHypyD2LtbH4xAw
- Mix of colorss | UCC9nkjB_DnIrEkR6dJXQuFw
- BETA | UCmTy7N-rw_WAzNxQONLdHLQ
- Nino | UCRLRnA-CCnwRm2Jz77tanaQ
- prettyyctrllx | UCyXLP75eHh8ig7YCN9trcig
- Blendrix | UCUNpWM5cs1o6LklQyYmqv2w
- Liz Kidder Studio | UCnP1muG2UYa4c-gRiRGw9dg
- Dr. Jumana Al-Deek / Menopause & Weight Loss | UCGFhXFHkgpQAhYANshLywmg
- AL GARRIDO | UChgpjygTZc9WXuBxivgnV1g
- Ciencia Capilar | UCButO4pHuTyJZzTifebTGvg
- Fernando Wi Channell | UC4lzYhcdDCTfR0-QRm_eiIQ
- mila | UCHwqT0YAc0lqqoQCQtEtloQ
- Helga Vital | UCQEO9IDljcnPjApLXXBziUQ
- Mansi Palav | UCIV0g_dm-T4ffb-ejt5l9eA
- Mens Health Over 50 | UCMJFched4vg8vNZ0EqP8iWQ
- Janet Mercer | UCocgHVL-3NS6ksplvLRFz0g
- DR. NORA HAYES | UChsZgTme1dZNl7Uo5f0yx1A
- Moda para Hombres 40+ | UCGShPxX4dr2bAJWVNVTRxnQ
- Shopping On Champagne | UCV7lS0SIBTYd-m4fG_x_GoA
- Eleanor Winslow | UCbwn6l34lEWhOIAjmPe4jzA
- Sally Atkins | UCc4zDq1uWOHFA_JesTne6fw
- sophiemariecurly | UCigZIj83t_6JddWhoJI5dZg
- Anastasiya Zolotaya | UC1Y5sxWC8e--fP3XG19CDpg
- Healthy Aging Secrets | UCuF-68zpaTQD9yVmoU2rI_w
- Stylish & Grateful | UCnA2AvPXZuRPE5JQ6tgfHGQ
- Diana GOSS | UCsCMk96I9GtBAS1TXjXCEAA
- Candi | UCyEDygB5eRvyO_S5zjCGn0w
- Shell Talks Hair | UCqw8ZG1c0sIV3kh6gk9cUyQ
- Styleswithfaith | UCHYQGFO0n94h3d2L1e2l8hA
- Ellena Hue | UC3TYncYbgM7hvrib4bj9f9w
- Heather Fletcher | UCorG6AURQ8Awk5SW55vIxFg
- AdoreAbria | UCYRFTA3d6MkxSL0fQraKUUw
- Fit After 50 | UChBmQWO2Vf9Y5qkua0MMDPw
- Glambysophi | UCyZ4b1A_wltKHzFzsHvqUtg
- Sophie Marie | UCSpEqToPcVIZuO4zoULJQIA
- Body Fix Exercises—for over 50s | UC9QgDBvyfbflM9zCBqp2GNA
- Style with Danielle | UC54kQeK3NYItVyvKy6TOksQ
- Aging Gracefully | UCAyZyz-Og2wOIzV_w9vALHQ
- Dress like a Queen 👑 | UCVPjIX_7LnoHfkYrk9QiEZQ
- Justin Hickox | UCTfRM6bqWXYyCcs_78ywftQ
- Ella Grace | UCdPhN0_2Yy56K_Wj5Lw9iTw
- Classic Fashion 60+ | UCsxP-G5n_1e03oiu8w4ihTg
- Grace After 60 | UCSaXBU4cwbCJ_7ZKd5xLp0w
- Glam Girl Gabi | UCYoiYowIowF7tYYel9NHpKQ
- Ageless 360 | UCwpuNriBe5e7TdxMu5y-IrQ
- Timeless Wise | UCsZgej5-hmi_2MtR9-UPxGQ
- Fashion Blast | UCDPNxO9QANlE68yZQIpbS5A
- Amandasilversister | UChQl_LzeJ1IJo9vYRh5c-bg
- Naturally Grayceful | UCd5F7N6awd2jOsVKDEWK66A
- Fashion Flair | UC3tWPQ-g4p9zwzalEi6k_NA
- Beauty and Fashion | UCqR4pMaDze0x5LS9I6SaXgw
- What A Hairstyle | UCmSJdBNOcrzlDrOv-ppE9Vg
- Hair Renewal | UCnKcJ6huGyeYntZdrjhy1Hg
- Style By Hair Magic | UCYK3syLx4c6bo8vLpGdoTJQ
- Naturally Graysful | UCRR1Vf0qI5Ibz8iqzjHhv4Q
- Coconut Farms | UCs9OATScNBFX0fga5BLdpjw
- Ageless elegance | UCdeN7QLLQWyqECN3YvwiIJA
- The Ageless Crown | UCcF7kQ-OWhdLHUM-DIiwebA
- Ever Chic At 50 | UCBCCodrcrSRDgF0GrEuAMbg
- Elegance over 60 | UCyA0F0p4a6nNGdVV5yS-9xA
- Timeless Wisdom Path | UCU5pdr0Y3PZyOFltpetrxJQ
- Ageless Glow (UCHxB7) | UCHxB7IxEJWDzB86w481XoFQ
- EverWise Older Women | UCeG4b6RGGOIB9cCys1OzmOg
- Age Inappropriate | UCXmrHEHdl8pW_hPcZGRZV_Q
- Classic Chic Styles | UCfjjociHTILmDGtOO7bCxcQ
- Ageless Elegance | UCKih8sJ7Qlk98_ik01oppNA
- Healthwise For Seniors | UCG2g-cTUJMWBNmMzkqB9i-Q
- women style plus 60 | UCRVfXVDf3359Wj1939BizIg
- Ageless Allure | UCxE8p-eBaPRbE4HZb81blAQ
- Radiant at Every Age | UCCgzpIjLXkigZ1FliZ1NLag
- WELLNESS FOR OLDER WOMEN | UCw93pu3O_UM4zcb1x95C3cA
- Guy Tang | UCjzof44RG883SW61XlkP-Pg
- Timeless Beauty | UCrq1g9Wp6Zi6KeSJr_Jk7sQ
- Ageless Confidence | UCxw2jFWBftkpRkFE4EC9W-Q
- Peinadas | UCAJysel-xcsT6NmWzFKqSuw
- Paul Watts HAIR | UCYL1Kn00HYDP0gOZKHBC84w
- Epifania Feminina | UCgfNEYFY--AbughOjT4wQhw
- TheSalonGuy | UCmi9wFeEZCV9gMDO-Sw_F-w
- Pri Flor | UCG9p01XxrFNdblvnu7iLImw
- Мода за 50 | UCLuwg0ab8DbiG4DHnA3ggsQ
- ellebangs | UCNCVZv2H9BXoA9UNI6TUSVw
- DIY Hairschool | UCMZB3K8oRJLL2xJXLcgRVWg
- Kaur Tips | UCjw7M5WI3ZYO-j4DDjS5evw
- Jas Anahis | UCBDIuYogcalOfy5g4o2hnLA
- Glow Without Age | UC7hyNTKirISMphkZisHi_-w
- The Essence Of Elegance | UCP5F10B1IF3uJjHtJx2WgRg
- Timeless Fashion Guide | UCOu0UNvSgYtc_w6DEak3W1g
- SHADOW TALKS | UCpR0xImBx_FGiFL57OjIZ0Q
- Elegance at any Age | UC70e5nNrGR-94Iplgm-ZRSA
- Dahiana | UCTfIhOFOG08p9VPrtfEVsYg
- TheHairGuru Carla | UC5j1n97VJ1EPFPRPr0zY8vg
- Glow At Any Age | UCq7vy7QW7_S53Mb9CkfFhow
- Avas Beauty | UCqJZ_NHRFUbrFKMBkZ38S4w
- Shea Whitney | UCU0k21RR-k7Zxil6KMs5nsw
- Chlöe Swift Stylist | UCFQAK8lVjY0daQ1MBHm9BXg
- Fashion in Maturity | UC4wZo_yW_lqgDPEs-TbDzog
- SassyShuchi | UCRcLCfocVxMYDhhnWlR8vKA
- Beauty With Brain | UCgmEBmk6yMS7e5HCGlDfyFA
- Tori Hunter | UCu6wyAefmxa74HZ13bReqcg
- Daniela Liepert | UCOcbsVf8Zt7N_YmBoCOLzYg
- Stylish haircuts | UCMvXFDgAyhr-KZrY0iUQdug
- Black & timeless | UC0DMHvFx3gaz94PCyARcRgw
- Mykah Jackman | UCRbRR9Wz8wDChGwIr7pRitQ
- Fun Daily | UCB0zrAl16Iq1oPLcP_-ZxAg
- fabulous50s | UCiWPU83VmOXjQ6xY0gIrhIQ
- Clara Kensington: Golden Aura Fashion | UCEtAs4Bse3dJN5M8VoQKOQw
- Style & Hair Glow | UCFCngivoKVu4xWGADmwqTiQ
- Maxora | UCDYsOqny5pZKhCIbMtN9U9g
- mraesthetics | UCGAbhGVTsWEr7wCNa9q_TRQ
- Elegant Beyond Age | UCW5swRUkHClHj-4XE9YvwDw
- Ben Azadi | UCUh_MOM621MvpW_HLtfkLyQ
- Jonathan Van Ness | UCf5LdDDOm1hYgDcSP3KimNA
- Real Men Real Style | UCmRfQHc3U4fV1-i8Ry1HmtA
- Chadtag | UCS3VEKQ3zcFdLhr-gieQ24g
- AlwaysAmeera | UCzgqWTlKiQACMCxB4UUC8nQ
- kayli boyle | UCfINcpvFORbgOZTpIaWxmbw
- DailyDose | UCFMAEVqwaeSc3P2Zxrvu7JQ
- Christine Le | UCvaslozYkHmrCU-vUaXZ9SQ
- PaisLee and PresLee | UCTy22G-rmPqJE_Ce7Mwo6mQ
- Allure | UCb0tMboxhHE8Jx6-nhJmRPw
- Zolven | UCyd0Yzg3F9nB3ig4UT0x66Q
- Amber Scholl | UCrlcqlqYJV28LvH1iYgw4DA
- Alex Costa | UCZyCposXwcyopaACep44maQ
- Jania Aaliyah | UC_SxLdlfh9Usd-vJHuEM8bQ
- BuzzFeedVideo | UCpko_-a4wgz2u_DgDgd9fqA
- The Social CTV | UComtk_zGLBSakLpZ3LmyfAg
- Golden Melanin Luxuries | UCp1KA5V-echMzqJcwNOnTbA
- JANE HUSH | UCNTgovMhpu3cbvVs_hWPjog
- MahaloStyleAndBeauty | UCcb05RFCOBeDgYNuN0pfFWQ
- GoldenGirlsHD | UCXIy8qcZ-97cuZGwPjNrnSg
- Beauty and the Boutique | UC_bc4xV-LjKlrkUlmMDQiaQ
- Kinni Beauty | UCesCE4xLnspN17kLtT2Qyiw
- Nina Ubhi | UCHUJ5ydbxEDm0uZ27sw3R9g
- Jodi Mannes | UCmwVYrrkCidc9BkUH-3EFZw
- Tati | UC4qk9TtGhBKCkoWz5qGJcGg
- Wayne Goss | UCCvoAe__WFYMNAEN-C-CtYA
- Risa Does Makeup | UCVtgrv6KHBNcRxDTys9TCcQ
- Sue Blackhurst Beauty | UCO4RFZZJ5pshOh_u7oSaoLw
- Erica Taylor | UCTxMakpAk-pNwySUepxS3SQ
- Elena Rachitskaya | UC9m3H8GjKrhu7098exLYc7w
- Pampered Wolf | UC8Nq-SrQLyc0DYuPrj0Y9uw
- Marlena Stell | UCE1BqH-72EBs-siTbDAjOGQ
- Abbey Yung | UCGCJF-m6ewM0TNJRwwsvi8w
- Stephanie Marie | UCb4iUMjpHZCiATCCwPaO47Q
- Mel C's Makeup & Style | UCRdnm4SuREcckrII-7BJRNg
- Ali Andreea | UCcng5aBy0ZmX7g2PfHf4gJA
- MrsMelissaM | UC8gaiQHu6uEfWa87kZ0_FkQ
- JustDoingMyBest | UC9QxOf1etehIyGTb_4yBzEg
- Laura Rae Beauty | UCk8zS1FjuJesK4HvMoLWCnA
- Graceful Beauty | UCTRUB2otFFPY0C1xpWJJJmg
- Carmel Nicole | UCGzvgMV4DHVQqBtTUnuUQGA
- Makeup By Nikki La Rose | UCCydBRF6RjrT58FV6KO-wwg
- Glow Up Over 50 with Kim | UCDBka6AisJPi7WU83ZLnP8Q
- Younique by Melissa ( Over 50 Beauty) | UCOV_dS_w6wgISp_Lyn-pwTQ
- Hannah Hall makeup | UCD4gn63ANRVCe78gz-CrvuA
- Maritroter | UCdDf5__qbVdf88NULXhneWg
- Blondiewoodbeauty | UCyp3vTLUAajrhqJtc8xhzRA
- Mature Makeup Masterclass | UCJXkeTS8KCNgrkty6QxpQ8Q
- CYoung | UCFdi3igjh6--YqjX17M1lhA
- Tricia Cusden - Look Fabulous Forever | UCuflfWUNugwPkZOQUEyAowQ
- Doctorly | UCHCZnC9akNA9pBP7aJGNKdg
- MandyLea | UCnL5ZQAj4WRPelrWt_v_P_Q
- Chris Gibson | UC4UmKCcnP0JbGPGrVxn8IPA
- Charlotte Holdcroft | UChK6kpyOTrMOJ391JUYBfSw
- Laura Fagelman | UCTMh6wXhe6SF3ci1Ikj9X0g
- Tina Yong | UC0ng0jJflTuJBBH5DGvr1Pw
- Suzan Taci | UCykydt-oes-0ii0nZFGUqEQ
- Ageless Style Secrets | UC7BCs3Kc2FtB6KDdJjP6Oww
- Zabrena | UCwQ48S6LdJVdGUM27M0oy4w
- Foteini Armstrong | UCFsYq4Iv75jAzpd4QibRPbg
- The Beauty Armor | UCbtdnMDoDqBunhDGangl11Q
- Lisa Eldridge | UCFghPtzFcmyDiID1ASMA4Dg
- Dr. Sam Ellis | UCRi13TUqA_SawPlPOG6jz1Q
- Mathilde Heather | UCFEjeAOxT2WRqxublmwKpSg
- Sahar's glam gallery | UCtzX684Hwr1pAtm4NdLsXkQ
- Julia Guesmia | UCjqD7lX1pBsxdWZgIbApkBw
- Anurag Shares | UC3dnN9m7YYtdFljrGEB_TVQ
- Cat's Eye Beauty | UC49Au4aUXqAnVusdyA7eiLA
- Sareena Karim | UCcVyd6HhRgn4aokCf9yz-eQ
- Jessica Morrobel | UCFK54Q2DC-pTPMXGJFQxLvg
- Cynthia Dhimdis | UCy2a2uHwOsOFemdVbIYRZMw
- Mixed Makeup | UC28FD2v19VZFryIjpvGIFLw
- Emily Heal | UClm9D6Std5EnJruG4XtoS7g
- Colby Troy | UCrm1k8eYCGQheJS86hL26og
- Julianna Lee | UCvYiqA54CuIW2ETJJnFLY4Q
- Prime Melanin | UCgOIMljjMuq6NIORaFKEBsg
- Doctor Eye Health | UCSs2CvlyOKLYY4SbfehnKNQ
- Stylish 50 Plus | UC22dYrWdVe747fePSU1L4xg
- Refined After 60 | UCHnphEBp4q2GGfpQRaT5Byw
- Crystal Coisne | UC_kSdTbRKLrxUTbiVsNVcNg
- Masumi  Channel | UCHp-Kd44q3Al-luQaoMr2SA
- Chloe Darling | UCTBvx8ESAlRg_ed0Z2YE5PA
- Sabrina Bailey | UC9lnL1p06V6S0-7M5coJDtg
- Renecreativity | UCcGxQv6VbDjR6zrZCK5Nytg
- DIY Pattern | UC0zPeFD5tCZrfjPD-unAeAw
- Sukaina | UCNMTH-Chhtywl-cDQ9FYOgA
- Mama Tenny | UCdr58hnhNbqaxBnng7R65sw
- Missba world | UC-MBKRzXrGKn1Y0n_J7XgcA
- Plakshi Jain / Crochet | UCUpAnKhFhQFsT6cjAb4Vjew
- Cutting and sewing Sarah | UCt_H1dBy5o5TOBrp9yKhvww
- Shalini Bells | UC8UhKsJ658HWG_jHYjgwRXA
- Real Vintage Dolls House | UCqRGR-9fqYzhDAzccsoVjBA
- AMS Beauty Glow2 | UCqb06tOCejarkTjF5LnexDQ
- sallykim7 | UCv-nP6YzWKo1QEJRJYuPXzQ
- Caters Clips | UCcR4cyQyAF-guvk7Wm5Lbqg
- ElyseCrochets 💌 | UCx0hrzDBdrduAHZHw7LjMDA
- Kamille Alcantara | UCagYGlKnTAMD6dYUa8Yk6Ig
- Easy Sewing | UCb4-J4_lmBfnLq4BL0g8R5w
- Sabina Hannan | UCRxHAGIRcF6qswaibWwyKjQ
- Petite Hook | UCMkpzeMALfSscMRFMYdL-dQ
- 황경인경인 | UC5QPH-9aMHQeVa61T72PTfg
- Cut & Chic | UCAIKyouFUNKBcoqUD2ZOZaQ
- SOBUE-似合わせの教科書 | UCP8Gr2rZ8IJdJtademQ-h0g
- Trendy Haircut | UCVXYrsQPbEkjh_zwJgtcSuQ
- ALI THE STYLISH | UChwF53Dbn2msL_r_2vvDACw
- Imtiyaz Ali | UCW4AaC28DCs5kcOX0JWN6CA
- Hair Bloom | UCzy9K6dUkFEf7fGszUxhgqA
- Look Young | UCOG3bmModR_RNSYG2SQ0Fcw
- Hairstyle Trends | UCpva8n-pfLAiEHHZRSHLF5Q
- Ageless Elegance | UC_6p4XX4pDD1bk9XxKcjdOQ
- BobPixie HairStyles | UCY50cJcqWO8AE_dDzrthgWQ
- Ali hair Academy | UCYbc21caiyr6v7vzhSJhB2g
- Fashion Trend Seeker | UCvz7o9PdPuu0hBAFIf8B9Dg
- Stilvoll 60 Plus | UCBPV22GKhIfBwYTMWkskNGw
- Elegant and Ageless | UCIEoiq-n25LZAK3EIpmC5sA
- Macklan Robert Clendenin | UCeDAjAKZGnVXpQYNdSQ4kzA
- Kelvin Siso | UCCS1Hpwzdjvy2Gl3oQ6zXUg
- Morgan Roy | UCnoyXKcb2dG8CwN70jvj_Ng
- Fame X stars 60 | UCSe1k-QNaHcCdSE3bmdteDA
- Glow & Grace Women Over 50 | UCdtsX_r47FygSY6tusIz-5g
- MypersonaltrainerTv | UCtKXnFU2lu0pOdipAnQyBzg
- Desi Makeovers | UCyxIgscUAeonLzrnMIcVV0A
- Nma luxe | UCcX1jn-wpwxOw3ghfbOQcMw
- Life With Spirit Over 50! | UChjn67gX8wWlsXMWF3WtDRA
- Be Genuine by Dr Athira | UChbJ4k5M6xTHu1BeBn-605A
- Kristi Carlson / Perimenopause Wellness | UCDoCvdYI4V2erEhbjxPSrJA
- Dr Ruth Machin | UCrF3NApg8D7iTd-sSDogeaQ
- Signature by Maria Farhan | UCSsEUoyxn8_a0cSftHGNIqg
- Annemarie My Fashion Life | UCstgRTy7c1W69lkMlc53-Nw
- The Elegant Gentleman | UCCpkvRy8exBV19_iQdH0aig
- Dr. Mary Claire Haver, MD | UCHFffg5HmfoId6E8WTVOc5Q
- FusionHub | UCJu_9SBxqMZqCbA802x5oAw
- Angel Cornelius | UCp8a3fzeThLY3XbKgVVUOEw
- Guilherme Samuel  | UCWC9ziBscDfAah2q7moRO8Q
- Golden Melanin Lifestyle | UCR1GuiIaEiaqaWp20PT5K8w
- Flipping50 | UCsrH0iucem3JoZdHQ2yvWPA
- Tuma sanga | UCYBTFMd07BUQkFO8dE08Ztw
- Capsule Closet Stylist | UCgNkiUqEi0HfHrDN-5h6EPg
- Stacey Nicole Smith | UCxF1NSJDuzwkcCpsfzdRK6w
- Aleksandra Lipa | UCw_NcvfK1QMtzDeZ94QTnhw
- Color Wow Hair | UCe-LF9yOuwUBzsiRYN5VWnQ
- The Everyday Sage | UCPwhohfBUP4-zJTI3P7ps1A
- Dr Dray | UCnxmUrGMtpQT844Yd_l7Zyg
- Tried natural recipe tv | UCkLI65mHh24HdLjWMPWQklQ
- Élégance Après 60 | UCfToK4QQsiisVFwmpUmZbYA
- Coach Elan / Women’s Health & Fitness After 40 | UCCogDjzs_DhK4_kpImMKzLw
- Curly Chemistry | UC9NYUv_5p-s3IKTEHTGaMgA
- Ageless Style for Women Over 60 | UC_iF9gYOYsNAeqJGAYU3H8Q
- Mahogany James | UCzgJFmhTOvFKgqM-6Ex2pbw
- Dr. Stacy Sims Official | UCPD55VPa1ZWx1a_nzWC2VJA
- High Performance Health | UC7ygt0Kro_Mqax2nLtz-yqQ
- SHARP AFTER 50 | UC40meuc1wkH8N3JJ5JGwHxQ
- Dana Ripperton | UCFRAs9CaMB5UNNklP4EY9NA
- Vital Well | UCzIpj-kCwFgK1ylqi_v8GpA
- Elite Hair Care USA™️ | UCyWSr-zf2REcLn7DQg0J07w
- Not In Your Head | UCarzT5NzfIq9e-7BkXDdlTg
- Fit Tuber | UCYC6Vcczj8v-Y5OgpEJTFBw
- 【縮毛矯正専門サロンsinsia】sinsストレート髪質で人生は変わる | UCw2dOPIVKLYuJOukv_hvvPQ
- Lady N | UCKLDqkMLeoXptUUDzfRJkpQ
- Brad Mondo | UCoc_XJPj6YLMQDWtPDQcDtA
- Dr David Jockers | UCIAZtlZSFlnBp_hAlvB6QSw
- GlowHub By Anum | UCVD9lXdQDp_2QFxRu3NSI9A
- Rosanna Smith - Health | UCSRfhuYJMyvL7RFIumOUEmg
- Natural Cures | UC_gcEbkXOt8j7NUoxulEaTA
- Florafauna_tor | UCJGzIIAKNOscTQLvf_UPwUA
- Melissa Denise | UCk4tzUlk1KeCs0xS6tT4YoA
- dimples on my WHAT? | UCPnVwn-uVJJUsoIhXQ8nkfw
- The Drew Barrymore Show | UCWIj8e2_-uK1m886ADSYO6g
- Michelle Roots Fitness & Nutrition Coach | UCHSxl5c1nobpsKtBIyvjKvQ
- Doctor Alex | UCGLAPJjQh7ege-N08u_GZrg
- Maa, yeh kaise karun? | UCBxfj0-E6_OyU7Zvu0F-zKg
- RazorEmporium | UCbZNav_HIPuMxn9n-jaayLQ
- Mayo Clinic | UC8fQzKHIhSoZeSq3bwQx4mw
- Galpen-chan | UCYBgGycDMg71VtOo043ECLw
- Pink Jardin | UCsxJwhOU15x-jvnl1O-chaQ
- Closer Lives: Jenn and Leon | UCD-wx9lLiFeulexN0Y00DMQ
- This Morning | UChFsYLqPUyLiZnfRog6wiZA
- Senior Wellness | UCslmaJaMSw8F8BId4CxByJw
- Good Morning America | UCH1oRy1dINbMVp3UFWrKP0w
- Dr Danish Salim's Dr D Better Life | UCShOERdmAnqqizmgm6LN10g
- TEDx Talks | UCsT0YIqwnpJCM-mx7-gSA4Q
- TODAY | UChDKyKQ59fYz3JO2fl0Z6sg
- The Diary Of A CEO Clips | UCnjgxChqYYnyoqO4k_Q1d6Q
- SciShow | UCZYTClx2T1of7BRZ86-8fow
- Digital Dukandaar | UCnFI8gk5BE075mr6FCb20cg
- Human Garage Experience | UCx5EZl3eZGzNrYyRFZuha-g
- The Art of Being A Man | UC-HeiDc9DPTOUE_OcHDe-1w
- Ellie-Jean Royden / Body & Style | UCp9uGwRfXSFVlYg6qRA5ERQ
- Erica Ball Style | UCD5_DIfFTgDsGhj5Aey7qcg
- Justine Leconte officiel | UChxkFSjTE7nLCHsDk8_pRhg
- Ellie Richards | UCe_wxUe-s32EEuEJyG00U2g
- Libby | UCqXL13aYkzltvtTta95kIFg
- Color Class | UCLpLz8pKnsH01-Uqnh4juRw
- Aria Vale | UCHQMcSbHKDS6c-e97wmX_Ug
- Desi Rich | UCDq9gkJSg2mYFtbpGyJ4kAg
- MM Personal Styling | UCgmaIAMFvJunsgcHOBUM25g
- What you Wearing? | UCtlVMzLyDxrAavW13IXKIvg
- Mae Alice Suzuki | UCHQ0GPGhqjinKm-Y9DLC3hw
- Stella Cini | UCGIaiz5OLxlfuH9gkqbejnQ
- Kelly's Life | UCBTSOI3W7qWKSASqrlY6rqA
- Bridget Fisher | UCyp6bHEwRL03WvELlZWUVlA
- ASMR Jonie | UCo7kA3XcXrqS8_cbz5GboCg
- lloganand | UCbHRsOLUWfx6HB9LSQFko1Q
- brittnee alexus hair | UCCdKf4EWpxdh6yKrY6ERopQ
- Bethany Brenneman | UCADwKwyloLWSwI3ac_3-1fg
- Mikaela Carrizo | UCsOTGPlk9S4YLieBmEccHjA
- Schwarzkopf Professional USA | UCG3aI1XxsildMwEd801s1Tw
- Isabella Zamuner | UCwA8EGolZWi-lxJT85QVmnA
- Khu / Kolors & Kurves ♡ | UCaEQlhFthF9El7wz4OBwZpw
- Kackie Reviews Beauty | UC0IwZAQyW6Z2E-Amqa3cNhg
- One Dapper Street | UCoxWvJUqQWuWY6kkx1CBHZw
- Colour Analysis Studio | UCIlFJcVe4mK-rJc2kOE_s4A
- The Lifestyle Cog | UC8GRLDtr12b91BhGq-x92Zg
- Sumansi Sahgal | UC1SjI6gr88-kiIwZuWIj-nw
- Deepika Arya | UC21FluxmvDsPXkEycq8oD-g
- Mystylebox | UCNEc9lkhgWUjt-cDdeFGp0g
- jess caelyn | UClVv87UUpArH-lLATvSAKsQ
- Obakie | UCt6mLXCHeFyhujK6r42vIyQ
- jasmine le | UCKJrvj5wrlQMlri_QT8zdSQ
- Julia Dobkine / Agile Styling Color Analysis | UC14K6bfynka4kWCHTfAdtMg
- NIKKO | UCXnywexyHnh6o6dgZlQ54oQ
- Ageless Style Co. | UC0-ioRByvtgk4BNAGJCsgbw
- 5-Minute Crafts DIY | UC2etEuPIfohP4P53wM0KImA
- Style With Faizy | UCDQRWCTopSedLle7MTYDH7A
- Hair Angels | UCYTKG7kU-VQJBoLRz11pmxw
- Your Style Hue · Color Seasons | UCPoo58e6kuC4XqxmfUpg-iw
- MIGRA | UCwV45J6RqRpfnqC3fAV6Ctw
- QOVES | UCnlvhYDQLq4d_C3JYEVnWAQ
- Easy makeup by Karishma | UCad1SXB8yaXtRmJEEHaN6hA
- Feel Good With Ali | UCy_N1G9SAXCE3CBWMNdcNDQ
- Alex Gaboury | UCdtRI1LNu7RjIDqXWwUBlDA
- Thrift Junkie Fred ☆ | UCMBlHVHW3ZpBwJ2IOcZ_IKQ
- Golden Age Glow | UC_T9GtYU4nyv8UJePteRmVQ
- UnflapAura | UCMdrzESMoqNux7WQJtnDaww
- Allison Baek | UCEzPt33mdyhRs3aQPhiN_pA
- dear peachie | UC_z-ddsQOcGupaINaXOh54g
- Level Up Traits | UCKsAAQED1oPWmlqS-siZQbA
- Glow Mode | UCH-vmMvxou0GZOTzJD5_7gg
- Valeria Lipovetsky | UCWkDFq1pO7YNzifE3A4UsMA
- ASMR Beauty Treatments | UC7gq8OJjwl0wFX-JCw0fr6g
- Facebasis | UCQNEzfBRnWibmN093Kmi2Mw
- The Style Theorists | UCd4t3EEUy0LUOM4MTdjpNHA
- Jules Lynn Beauty | UCJABwLTxzA1Qo-pidvT9EKg
- Oceans ASMR | UCC2xZiqsdhsTd9AaC0achGQ
- Alexandria ASMR | UCvp9ypbbOQ2-vtuO-J3k-lw
- Ayush ZenFit | UCZ1FtH8YN1VsqQf6LE4TnsA
- Ishan Sharma | UCY6N8zZhs2V7gNTUxPuKWoQ
- Veena Sridhar's Kitchen | UC1TlqQMOwKalDFDmFIrkmqg
- Bromaxxing | UCqZU4-bgPPZR4tDKXPGptVw
- SweetHearts Hair | UCbKAjRFsR7WE04kdMXL5gVA
- Tingting ASMR | UClqNSqnWeOOUVkzcJFj4rBw
- ExpHub - Prashant Kirad | UCgoyBmLOMNWmsiVkj-MezyQ
- Pierre Dalati | UC8Av1tO-ha143nNYzxmf1Fg
- GQ | UCsEukrAd64fqA7FjwkmZ_Dw
- Ben Azelart Top Videos | UCpFC1R_aZOH3AfCuEMZrJUQ
- charli d'amelio | UCi3OE-aN09WOcN9d2stCvPg
- LINEONE Hair | UCtl1KyRUgG2Yrc8GDIT5W7g
- Fashion For Seniors | UC-ONxF2qMV73jqEsyrCQh7w
- Ageless Black Queens | UCYrVMFXU5tO3NtaaQDxGK8Q
- Glow at Every Age | UCHMR9dxvz4_jH2fcnr49eGQ
- Golden Age Fashion | UCfkD2j55k90xhXk21In0LgQ
- Luce Como Reina | UCqUEjsLMkC1nnTo6g7jD5FA
- Belleza Serena | UCtMRZDhdzhGeCnWQb4IXBrw
- sadi4718 | UCS3-h0XEwU225gYKOz-oY1w
- Refined After 50 | UCKbzlKtqb5KlitumXEAn6aQ
- Rock Your Fashion | UCeW6gtrT1ojeODaFyATlx_Q
- Ageless Style Over 50 | UCtNoKsrDFISnbjHK-m8vzvA
- Style Never Ages | UCgYUYUFXih1DsD5ACXBMWlg
- Ageless Melanin | UCxvKeo4XCACuU6Zd1aQzhmA
- Classic Style 60+ | UCMhgcynY760cgpMH5TfSRtw
- The Golden Years Archive | UCVZ2uoMXHpb83eLwesu9PdA
- Fashion & Elegance 50 | UCY4FtLwuNTvUzmsa9VbiCZw
- EverElegant style | UCDZP2dWoNA6MeOxmMQaY6zw
- Modern Elegant 60 | UCCoTIkqSQ707Z_mjo-rgw4w
- Journey After 60 | UCBnPTmijWKU8xbIv-jMArkw
- Timeless Glow | UC8jydU55NBQGigZjz36HzVQ
- Grace & Glow Lifestyle | UCYg5ozPxNaDTGOImC9gq8Fg
- Phong Cách sống | UC3Vhm5ZOumYZJLkda6jH04g
- Livora | UCk5IwNa-38p--ote1WqfxVQ
- Classic 60 Look | UCkixxXXpBERjt_krLoYilfA
- 優雅な日々ファッション 60+ | UCbH-Y0sm8H5pOnUom0ry6kg
- Timeless Style After 60 | UCl50lEo8OKMH0ZRfEmzn_YA
- Graceful Style Guide | UC45XK1uXg45MkUwkl6DWLfw
- Beauty Beyound 50 | UCl-tfuLYb3lzEAAiOuQFDOg
- Senior Spark Life | UCkRgoW_-IPxAMhGjNyAPbFQ
- Gracefully Dressed | UCSL-QkE2wBO7cmwY1V7jrMA
- Graceful Aging with Ruby | UCLEjotn8qHtJzywdBfcBnuA
- Scarlet Starling | UCTMwV-uy20eaRwFfc4Sx13g
- After 60 wardrobe | UCYTDB4vbsivPBM5XuWr_sOA
- Stylish Over 60 | UCB6rbkmfVdmzqvrFfy9wkUA
- EverGrace Style | UCcgDZKiLyJG4wpvNLoFCcYg
- Style without age | UCtabZ91H_V1fE5lfOs2yeyA
- 60s Best | UCZ_VczZdm6UF00vjJvVTs0g
- Attractive Women | UC9H-r9dXUUFqttd8xDRjSLA
- Tracy Campoli | UC2sXkXBWd51cpk_5nyUha2w
- Elegant Beyond 60 | UCa9xJmc-1f9FZErv_KFi4jA
- Fashion For Women Over 60 | UCDMv6pf3v7cXoG6N4HSx8ww
- Classic Gent | UCFbEJORScJ2K2E_NjQVfBAA
- Mayitos Beauty | UC86dEhYaxa3WdshVHQvVJbA
- Adore Your Wardrobe | UCiCk9YOdjY8zZMUvMCGurCQ
- Gracefully Styled 60+ | UC_ctSZAf5JIctxUaFuzAVSQ
- Timeless Elegance Style | UCM3EH9yVijLM_Fo0Bmyzylg
- Best After 60 | UCZgkapU4VP6h0HoDbiT0Hkg
- Timeless Elegant Fashion | UCnr4FcEntzBnqKfEC8anE-g
- Timeless, with Diane | UCFThaKGjhY7sctiWBMPE9uQ
- Styled by Marie - Anne | UCLa8_D5YgVZYzSRkJn-B5aw
- Fame Frame | UCm_bZZfXWYPBkZF9M51aycw
- Regal Gentleman | UCx_Couu5K05uXzUOTw3hLIg
- 60 and Stylish | UCILZsdYkovsBC3nWB_BhJ-w
- Vogue After 60 | UCBvuZ4bLtfcvMMyvbNd--rw
- Loretta Banks | UCcoEeeivwKoILXsTnZ-rw1g
- 60 & Fabulous | UCjqiqlfmQtVcK8zxKrhD9Sw
- Kirei at Sixty | UCrnkQyJoTbKFLwtc19JSorQ
- BlickPunkt | UCpeqZf4fMfKE6b5vYM4LpLw
- Stylin at 60+ | UCifTa7HcBKOjPzQ-XekpP9g
- EverAfter | UCtl2ctZb95K_yz87uNXMRow
- Chioma Vibes | UCGmr-g0h4UCz4cBACO0jWJA
- Margaret being Margaret | UC-4Xt9BEMoyO3e3tDyrF_vA
- Chic Over 60 | UCkbGQ6Snk83E-dKt9aG_vVw
- เส้นทางสู่ร้อยปี | UCFzL-pZZQQRd4BxufOPT9fQ
- Everyday Fashion | UCUBTtXWynzBLF5TeY1QtieQ
- Dress Code Daily | UCpAGthWXIkAoa_fhtdTfakg
- Elegant Fashion Over 60 | UCuvx5ECwGVkFZ-CZ3ErOoRw
- Elegant and ageless | UC1nRW40HBnX2dbJT2USTvRA
- La Mente Ancestral | UCN79nVGNNw1FRU5Jx5-32xA
- Golden women journal | UCR4fFm6g7_4v4J_SUfgc1EQ
- Samraat Choudhary | UCTXxR--_ubDMgp_hdkMFadg
- Mirella Manelli | UCRGlMBCo3QZFW9gJdseWirA
- SUNNY HAIRPORT | UCiHnLH0aFt_7xmM0G33kHiA
- AmandaLand TV | UCqOvln4ybkexlDgf-F_0cKA
- Shanelle Beauty  | UCa9nfAeJivFt1S2aInkzj5Q
- ss lifestyle oman | UCqSIQTS0Shu6FT3c4gB56xg
- Hair Buddha | UCDxhyRS1wRQ5lAzlmG6G7qQ
- Swavy Curly Courtney | UCbIzL-of1Mz_wY9GuNTexQw
- Best Haircuts | UCE0MWJvhCNwlp3BYXhPptUw
- Cocaknotz | UCatS8cb7vojZ1lQbrvhghmg
- DieHardBarbiie | UCUtQRERtwt5g7YIuidhn3BA
- Ditching Diets & Dye | UCkkiXUPlezVhUrqBDuy7_Bw
- hair by Kristi Jennings | UCtATO56ZrFIaL6sDec-g7QQ
- UniWigs | UCjgjB4hnTmONnGdatqtlUwQ
- BLEACH DADDY | UCAMb3mj7Kz6Bon_WdZNUykw
- Zoya Salon | UCj6jlEi4X0ScBFoegxGmWxg
- The Hair Loss Show | UC6Z6GxYsW9EdvnUjqpGIbQA
- Dr. Mamina | UCa8U11JrxgFAQP63bR9AAZA
- Hairmani | UCxN9vn3ue7vvLYlGMAl1ZAA
- The Grey Indian | UC99wklX8ERY1QKd4NsjwXRA
- Naturally_Nica | UC4zR_mcYO2rk9vqccL1cZLA
- xsamhair | UCNbx6yTu6FvokGh75xRL1wg
- HairEveryday | UCQpOCfso2p9BCeQ9x81aMmg
- Simply Subrena | UCQpvy5BKoJoYyAh4tQM0EMw
- Julia and Hunter | UC4Unj6XzNqvCUvmoFhafALg
- Everything Homemade | UC3Hpme4Q41AbeKpxaBldgfQ
- Newtimes Hair | UC_Aizh93NX3eKvoNMH12tgw
- DrkNlvely | UCjGTvWo7IoKmdjEyFB-HGCQ
- Hair For Humans | UCpt1_bOOKBfmDzaPN87J-VQ
- Natalya | UCm1WrC-YaZUWTDgK0PS9INg
- Cosmo Health | UCh45Tc0arWplMHTKGUA3k5A
- Luxy Hair | UCJqcphJAnsD5YDXcRFzTsOw
- Cosmetic World | UCtNvVUy7ari0SSry79lLcrA
- Refining Style | UCmpbERxzvAtB_fmvVT-dr1w
- Fit Tuber Hindi | UCDWVNwQce16D16tPc5NBYlQ
- Tina Hart Beautiful Journey | UCWzhndr_RoZw8Tj2MFOQe5g
- RECIPES FOR YOU | UCq6akguHzmPR6dqIqhuUIAA
- Skinvestigation | UCOu_KBklBYqpb0MchOd86ng
- ehowbeauty | UClVCIrKwwi36uYe2V6vRkJg
- Sam Villa Hair Tutorials | UCUUOUXV5xmEqGWGf9eUyjdQ
- Stranded Hair Extensions | UCk4qZI8ddsGz0A3dCiJ3vmQ
- The Yoga Institute | UCihUiDJzjyo2ov_qGtW33lw
- Stay Fabulous with Nisha | UCUSV0-kNMyQGIDol_468KpA
- Taylor Morello | UCfjujgVWyA6uS0owCea28kg
- Andrew Huberman | UC2D2CMWXMOVWx7giW1n3LIg
- ThreadsObsessed | UCGNPyrcUGdphh-G1MCjP44g
- Daily Bible Audio | UCL5xC4sFNGH-u-iBftrPSYA
- Southern Living | UCtYty94mQ6on0Q2oqD2erhg
- Sesa Ayurveda | UCbsJzF0UmVvS5cuNTlDDnUw
- Amanda Nighbert - Registered Dietitian | UC8KpxyBBxv1YlEsjAdyGrXA
- Helping Foundation | UCetF1zwuRlZpLg74WWsqOBw
- Erica G Designs | UCnYV90LC264qd3OQbh6A_eA
- 白髪ぼかし専門美容師カイ【シングレイハイライトチーム】 | UCeMhKlxAEqn64X6vUeQTxhw
- Maryam Remias | UCE43Llr2FByjS2ZjUvf_p0Q
- Glow With Katie | UCul6Xy5KxSyzWo5ooomOXBQ
- Irene Claire | UCHbV0CDwil6XdOKuneyCcvQ
- Kristina Angelina | UCx7M4wbcKkbHoymqhiyCJSA
- Jeannie | UCsV1nF-KPgSK-A3xwcwjMpA
- Bleaching and coloring by Jacky Teacher | UC2AaH5dwlHsB1QE6VTQyl6w
- Suzan Barnes | UCYtuugsWYKy8i6YtUSmL-0A
- La Pasión de Ana | UCPTALg5unMcYgwccU0boLXg
- Ju POPPIN | UCxlDh2nd6aQjBqsoWvw3gdA
- Herbishh | UCQ2GY3d7W9X7Uqh57BJ7tvQ
- Beth's Best Hair | UCy0BLqbzCBCPFvVrhpfw2nA
- Amna Hair Zone | UCPTOt2arb9T1idryca3HXng
- Elise Marquam Jahns | UCGADiKwkR5WSwvLfCFUrDig
- Camille Cowher🔸️Makeup Over 50 | UCo_cQhVAhCdp7S9RTcPFwtA
- Philipp Karner | UCXitUIxYw_U-foxbSXSh04Q
- You Beauty | UCId3fcjIozVt9dsWTnOSmtw
- Sixty & Radiant | UCNZpezk-lmkfXGRp4NZbNHA
- Styled by Whitney | UCZF9EDObD0cp-RtgJnK149w
- SimplyRVing Homebase | UCBq3rHmB_4GpOCOPhgofzCQ
- charlierewilding | UCJIlQ8T836wBB7LxUTT4b-g
- Evolva Official | UCaoPiQ1debiKXGg9SpHN7bg
- Simon Squibb | UCGznz4NfW5iymkvn1l40qyA
- MJ The Gray | UCH76iINwrNP0kOI96Exy2Cw
- Big City Girl Small City Living | UC9hLS3MeM0zZXiGpVzAzG5w
- Lorraine | UCM0cwESe107DHyGpEUx1n4Q
- TODAY with Jenna & Sheinelle | UCwukDJWDHn4JW2aHps1ZCvA
- Brooke Roberts | UClTWZYvFecdBhkHYrYGDyNQ
- JumpButton Studio | UCLWl_R2zfy94mQjY-Ctqs2g
- Baylor College of Medicine | UCLMEy29-dHF9dVCZ_ekOR1A
- Bhargavi beauty world | UCRIMs5MlCZLVzSt68gGxQzw
- Midlife Dream Miles | UCtvUR6coMmIw6Sk5aMwDpIA
- RawBeautyKristi | UCOtoxvHLKrIlWbt4MRBWfbQ
- ch cosmetics | UCALH_sFANbeoPkvSMV6LDeQ
- Taichi Zidong | UCcfbXvyfxnDW7xlgpNvMgOQ
- Dr. Brooks’ Longevity Clinic | UCtAHQOrmL2TV2xT6f4az7ew
- Matt Gray | UChYHKRass0kZvBkVKQuZElQ
- Sephora | UC9YX5x_VU8gfe0Oui0TaLJg
- House of Caro. | UCXW8mlXMK1rYboFHUmHAlUg
- From Vinos Diary | UCKYcfwIUDfVooez2xt1j0iQ
- GYRUS SULCUS | UCpBRZ6j0oAkjyd3FLr4yPtA
- Beauty & Style for Mature Women | UCMsVCgNPyhbMkw1K9foD8ew
- Dr. Eric Berg DC | UC3w193M5tYPJqF0Hi-7U-2g
- Biohealthy | UCOhE6Cq6tT9Jh6BcCxcPM4g
- KPRC 2 Click2Houston | UCKQECjul8nw1KW_JzfBTP1A

</details>

