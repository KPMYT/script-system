# Fashion lane discovery log (Phase 2)

Lane: fashion and style for women over 50/60/70, English. Helper: fashion-lane discovery agent. Date of all data: 2026-10-28.
Output: `fashion.csv` (101 kept channels). This log covers every search, the method, approximations, failures and the screened-out list.

## 1. Summary

- Kept: **101** channels (all rows in `fashion.csv`).
- Individually screened out: **210** (section 6), including 13 channels that qualify but are already kept in another lane's CSV and 1 own channel.
- Found but not fully screened (NexLev limit): **97** (section 8, with IDs and stats for pickup after the reset).
- Similar-channel results dismissed on name/description as not candidates (men's style, music, kids, news, travel, fitness, non-English, etc.): **314** (section 7).
- Type split of kept rows: real_on_camera 27, faceless_narrated 46, ai_avatar 1, unclear 27.
- Lane split of kept rows: fashion 62, lifestyle-mixed 15, fashion+hair 10, makeup-adj 6, skincare-adj 3, hair 3, french-lens 2.
- Audience fit: core-50plus 82, partly 19.

## 2. Own channel (excluded)

"Scarlet Starling" (UCTMwV-uy20eaRwFfc4Sx13g, About reads "Welcome to Scarlett Sterling") is the operator's own channel. It came up in similar-channel results (531 subs). It is not listed as a competitor.

## 3. Searches

### 3a. Niche finder (search_niche_finder_channels; channelLanguage=en, limit 50, no sortBy unless noted). New candidates = channels not seen in an earlier query.

| # | Query | Filters | New candidates |
|---|---|---|---|
| 1 | fashion for women over 50 | en, limit 50 | 50 |
| 2 | fashion for women over 50 (page 2) | en, limit 50, page 2 | 23 |
| 3 | fashion for women over 50 | en, isFaceless=false | 21 |
| 4 | style tips for women over 60 | en | 7 |
| 5 | how to look younger after 60 clothes outfits | en | 6 |
| 6 | elegant classy older women style | en | 10 |
| 7 | old money quiet luxury style for mature women | en | 20 (mostly off-topic old-money channels) |
| 8 | capsule wardrobe over 50 | en | 10 |
| 9 | what not to wear after 60 style mistakes that age you | en | 3 |
| 10 | dressing for apple shape body over 50 tummy | en | 10 (mostly fitness) |
| 11 | accessories jewelry glasses scarves for older women | en | 1 |
| 12 | personal stylist for women over 50 on camera | en | 2 |
| 13 | lookbook outfits women over 60 try on haul | en | 3 |
| 14 | grandmother style fashion over 70 | en | 0 |
| 15 | how to look expensive on a budget mature women | en | 2 |
| 16 | avoid looking frumpy midlife women style | en | 2 |
| 17 | midlife fashion blogger over 60 shares her outfits and style advice | en | 0 |
| 18 | plus size petite fashion over 50 | en | 5 |
| 19 | colors that make older women look younger wardrobe color analysis | en | 2 |

Total unique niche-finder candidates: 177.

### 3b. youtube_search (type video unless noted). New = channels not already met.

| # | Query | Filters | New channels |
|---|---|---|---|
| 1 | things women over 60 should stop wearing | video | 12 |
| 2 | style over 60 outfits that make you look older | video, sort views | 10 |
| 3 | how to look expensive over 50 | video | 6 |
| 4 | what to wear over 70 women | video | 12 |
| 5 | style mistakes over 60 women | video, duration medium | 5 |
| 6 | fashion over 50 capsule wardrobe stylist | video | 5 |
| 7 | fashion over 50 | type channel | 11 |
| 8 | frumpy over 50 how to stop looking frumpy | video | 7 |
| 9 | fashion over 60 | type channel | 10 |
| 10 | old money style women over 60 | video | 7 |
| 11 | jewelry mistakes women over 60 accessories that age you | video | 11 |
| 12 | over 50 try on haul outfits midlife | video | 5 |
| 13 | how to dress apple shape over 50 hide tummy | video | 4 |
| 14 | shoes that make women over 60 look younger | video | 10 |

Total unique youtube_search channels not in the niche finder: 115.

### 3c. get_similar_channels (level 1) on 7 strong channels

| Seed | Results | First seen in this run |
|---|---|---|
| Chic After 60 | 90 | 90 |
| Shopping On Champagne | 126 | 114 |
| Vivian Sinclair | 111 | 79 |
| MM Personal Styling | 121 | 102 |
| Marie-Anne Lecoeur | 83 | 42 |
| TRENDS SPOTTED FASHION | 95 | 0 (all already seen from earlier seeds) |
| Elegance At 60 | 74 | 37 |

523 unique channels in total; 66 were already met in 3a/3b. Of the rest, 124 matched age and style words in name or About and were screened one by one (sections 6 and 8); 314 did not and are listed in section 7.

### 3d. Per-channel calls (not searches)

youtube_channel_about, youtube_channel_videos (popular), youtube_video_details, check_faceless_channel, get_channel_analytics (about-level data: subs, views, videos, joined, country, last upload), search_videos (NexLev video index, filtered by channelId, 5:00+, since 2022-01-01, sorted by views), get_batch_channel_metrics_v2 (14 jobs: average views, faceless flag and confidence, RPM, monetization, top country).

## 4. Method, approximations and data sources

- **Keep rule** applied as written: uploaded in the last 12 months AND (10K+ subscribers OR any video since 2022 with 100K+ views). A faceless/AI channel under one year old is kept with any video at 50K+. "1 year ago" last upload was treated as inactive, "11 months ago" as active.
- **Candidate test:** English channel where women over 50 are the main audience or a major share of videos. Broad style channels were kept only when an age-specific winner was seen; otherwise screened out with the reason "not age-specific / not verified".
- **Top 3 videos** are long-form (5:00+) since 2022. Sources, by row (stated in each row's notes):
  - Early rows: popular sort with top-1 exact from youtube_video_details.
  - Many rows: popular sort only (views rounded by YouTube, e.g. 1.8M; dates derived from relative text such as "4 years ago", so `~2022 (approx)`).
  - Some rows: NexLev `search_videos` index for the channel. Views are cached (the row says when) and the index often covers only part of a channel's catalogue (the row gives "N of M indexed"). Dates are approximate.
  - Some rows: NexLev niche-finder cached top-5 videos (approximate dates).
  - Last 30 rows added after the limit: only videos I had already seen in my own youtube_search results ("partial"); some rows have no top videos at all (said in notes).
- **Last upload / uploads in 90 days:** from get_channel_analytics or similar-channel about data ("N days ago" as of 2026-10-28), or NexLev niche-finder lastVideoDate and uploadsPerWeek x 13 (marked approx). The newest sort was not called for most channels; uploads_last_90d is "n/a" where not collected.
- **Type labels:**
  - check_faceless or batch-metrics isFaceless=true gives faceless_narrated.
  - Not faceless plus a named real presenter in About gives real_on_camera.
  - Rows are marked **unclear** when NexLev says not faceless but its niche data flags faceless/AI, or when the channel was created 2024+ and its About names no real presenter (persona-style). That last part is my own reading and is marked "reading".
  - Chic After 60 was marked ai_avatar (reading).
- **Revenue/RPM:** niche-finder monthlyRevenue and rpm (base / total) where available; otherwise the batch-metrics RPM; otherwise blank.
- **Cross-lane overlap:** 13 channels I met are already kept in `french-makeup.csv` or `hair.csv`. They are not duplicated in `fashion.csv` (section 6, "already kept in"). About 30 of my kept rows also appear in those files (other lanes recorded them independently). I did not remove them.
- **Shared scratchpad:** other helpers share the scratchpad. My `nf.py` was overwritten by another helper (their note says so), and `pool.json` in the root belongs to them. My own data files (records, screened, batch, analytics) were not affected. For one row (Stylish outfits) the creation date came from another lane's NexLev niche-finder pool. This is noted in the row.
- No commenter usernames were collected.

## 5. Failures

- **NexLev weekly limit:** reached at about 04:07 UTC on 2026-10-28: "WEEKLY LIMIT EXCEEDED, 2000/2000 MCP tool calls ... resets 2026-10-31 06:56 UTC".
  - The first refused call was get_channel_analytics for SuppleChicTV (UCjnim4l9ObyJFO6Cn6mJUjw).
  - Retried once with search_videos (Angela Masson); it was refused the same way.
  - Batch-metrics status polls for jobs created before the limit still returned results. No other NexLev calls were made after that, as the main session instructed.
- Consequence: 97 candidates could not be fully checked. They are listed in section 8 with IDs and the stats seen, for pickup after the reset.
- No other tool failures.

## 6. Screened out (decided)

210 channels. Reason given per row.

| Channel | Channel ID | Reason | Found via |
|---|---|---|---|
| Elegant Fashion And Style Over 60 | UC8rJqI3YGdgUcZVHILLSqvw | Inactive: NexLev last video about 2 years ago (2024), uploadsPerWeek 0; 85.2K subs, 1.1M top video | nf:fashion for women over 50 |
| HouseOfElegance | UCa9KQyun6e1uB6iJl2fCgYg | Inactive: last upload about 1 year ago per NexLev (outside 12 months); 1.6K subs; one 139K video | nf:fashion for women over 50 |
| Ageless Style Icons | UC4iMSCYpbu6kG8Lia46j77Q | Inactive: last upload about 1 year ago per NexLev; 1.9K subs; top 81K | nf:fashion for women over 50 |
| Smart Fashion | UCYcmyDtGnrFi9gBP4Pixciw | Not a candidate as found: top titles have no over-50 framing (brands robbing you blind); broad women's fashion. 6.3K subs, 272K top | nf:capsule wardrobe over 50 |
| Vintage Woman Secrets | UCLYagTtUz5Rp7QK4t9jAH8A | Not a candidate: 1950s lingerie nostalgia, titles framed for men; 1.1K subs, 107K top | nf:fashion for women over 50 (p2) |
| Lisa Fashion Style | UC1GQRbBQM1eLg4FPgtPglOw | Inactive per NexLev (last video about 1 year ago, uploadsPerWeek 0); all top videos are Shorts (Natural Older Women Over 60); 37.7K subs | nf:fashion for women over 50 (p2) |
| Street Style Hunt | UCsajS9S8q5be7v1tLWKCstg | Inactive: last video about 2 years ago (2024); 5.2K subs; 138K top | nf:fashion for women over 50 (p2) |
| Senior Fashion Class | UCfqm-owzftN8K4KxeTF5trA | Size: AI/faceless, under a year old (2026-04), best video 41K (<50K), 1.9K subs | nf:fashion for women over 50 |
| Elegant Academy | UCKW9TVF2cM1CbJoGo4MjstQ | Inactive/size: last video about 1 year ago, 1.2K subs, top 64K | nf:elegant classy older women style |
| Elegance in Every Detail | UCBaMaBRu4XwCHalwR50bLfA | Not a candidate as found: top titles have no over-50 framing (sneaker/jean trends); broad. 10.2K subs, NG | nf:elegant classy older women style |
| The Elegance Society | UC82ZtUPn4PduSPadGzHpEiA | Not a candidate as found: top titles have no age framing (colour combos look expensive); 2.2K subs, 132K top, created 2026-07 | nf:elegant classy older women style |
| Ageless Queens | UCgC-uVXN5nb6jw-uvNDTyzA | Inactive: last video about 1 year ago; celebrity-over-60 Shorts lists; 3.9K subs | nf:elegant classy older women style |
| Natalie Paterson | UCKKDzoxS74kkcxHtA_ByKOA | Off-topic for style: home decor after 60 (living room/bathroom looks old), cookbook funnel; 3.8K subs, 84K top, created 2026-08 (would pass the new-faceless size rule) | nf:what not to wear after 60 style mistakes that age you |
| Aging Queens | UC0uabQ9Zs6bDpr1n-gqR3MQ | Size: 3.3K subs, best video 67K (<100K); created 2025-10-14 so not under a year | nf:what not to wear after 60 style mistakes that age you |
| Style After 60 | UCCac3e7jjjwD4SZdprJRmxA | Size: under a year old (2026-03) faceless, best video 38K (<50K); 2.5K subs | nf:fashion for women over 50 |
| Style After Sixty | UCTSYeyREkFQQYvtazAIeESQ | Size: under a year old (2026-07) faceless, best video 23K; 1.2K subs | nf:fashion for women over 50 |
| LIFE AFTER SIXTY | UCw3rDeePRfGB-wpv2_bAVeg | Off-topic for style: senior women relationship/family advice (Im 78...); 5.8K subs, 154K top | nf:how to look younger after 60 clothes outfits |
| Classy Academy | UCJUn02MVnahA9My9-DUkTBQ | Broad elegance channel: top winners carry no over-50 framing (8 things elegant ladies never wear 1.2M); 135K subs | nf searches (see log) |
| The Essence Of Elegance | UCP5F10B1IF3uJjHtJx2WgRg | Broad elegance channel, no over-50 framing in top winners; 99.6K subs | nf searches (see log) |
| Lucrative Elegance | UC7ja09zyYoG7LZ0rzwZzIdg | Broad elegance/classical-lady channel, no over-50 framing in top winners; 191K subs | nf searches (see log) |
| Ellena Hue | UC3TYncYbgM7hvrib4bj9f9w | Broad pro-stylist channel; top winners not age-framed (one mature-women apple-shape video 95K); 137K subs | nf searches (see log) |
| Her Classy Femininity | UCSNqYRW5oGef0gaVquCUfFA | Broad classy/feminine channel, no age framing; 36.1K subs | nf searches (see log) |
| Slow Down In Style | UCcx8uX1WqAoOQxe2y-5A-tg | Broad minimal/capsule style, no age framing in winners; 40.3K subs | nf searches (see log) |
| Refining Style | UCmpbERxzvAtB_fmvVT-dr1w | Broad colour/glasses analysis, no age framing; 80.2K subs | nf searches (see log) |
| Style with Danielle | UC54kQeK3NYItVyvKy6TOksQ | Broad plus-size/body-shape; one over-40 video (122K) only; 63.2K subs | nf searches (see log) |
| Summer Beauty | UCl4iYvuUhw3DIRyYtV1Twig | Broad hair (face shape), no age framing in winners; 108K subs (hair lane may judge differently) | nf searches (see log) |
| Healthy Over 40 | UCzKSuXXH9QNAIK0fn913mRQ | Inactive: last video about 2 years ago (2024) | nf searches (see log) |
| Ms. BoBo | UCHkz976V7OzqZtu8aZ2xPdw | Inactive: last video about 1 year ago; mature-model bios | nf searches (see log) |
| Big on Style | UCUKb7TP60fQRKghGSsvFDHw | Broad plus-size dress hauls, no age framing; 21.8K subs | nf searches (see log) |
| Shonda Style Official | UC2atwVPOdHL962xVGWDX17w | Inactive: last video about 1 year ago; plus-size hauls | nf searches (see log) |
| Femme Fatale | UC3VUvxSWWpPQVRN1L9YliJQ | Broad pretty/polished tips, no age framing; 32K subs | nf searches (see log) |
| The Elegant Edition | UC1XeD4J11bJIu7cdPc-dnmA | Broad rich-mom style, no over-50 framing; 27.2K subs | nf searches (see log) |
| Fiona Nathaniel | UCAicQjGwGcQtZjVyQb3uREg | Broad capsule wardrobe, ID, partly Indonesian-language | nf searches (see log) |
| Freya Tidy | UC2qDS2ggZ46y1Z5z8Reo9qQ | Broad lifestyle/makeup vlogs, no age framing | nf searches (see log) |
| Lavishing with Sandali | UCNUo23E9CSMiQ9beKbfpwkQ | Not English (Sinhala); 147K subs | nf searches (see log) |
| The Miranda Holder | UCxLItPy-5COqesvVAwUPRGg | Inactive: last video about 2 years ago (2024) | nf searches (see log) |
| Pretty Over Fifty | UCH9m-hQ86lby7pU6ausvAJQ | Qualifies (325K subs, active) - already kept in french-makeup.csv as skincare-adj; not duplicated here | yt-channel:fashion over 50 |
| Mature Muse Studio | UCP4PXi1X0f7UBSl4wZPtEMg | Faceless, created 2026-07 (<1 yr) but best video 48K (NexLev index cached 2026-10-25) - just under the 50K bar; 443 subs | yt:style over 60 outfits that make you look older |
| 50 + Women's Fashion | UCZ0yCMWQFnnFwXNQCNm7abw | 263 subs, 44,971 total views, 4 videos, created 2025-10 (over 1 year): no video can reach 100K (analytics) | yt-channel:fashion over 50 |
| Elegant Looks After Sixty | UCauMLf6DMetMzkCQv309FRA | Qualifies (4.2K subs but 218,930-view video per lane C) - already kept in french-makeup.csv; not duplicated here | yt:old money style women over 60 |
| Awesome outfits | UCgSch4cA2N7EnT7TRb9drTA | Faceless, created 2026-06-22 (<1 yr), 151 subs; best long-form 21K (popular sort) - under the 50K bar | yt:what to wear over 70 women |
| Stilvoll ab 60 | UCvwwzMIBXsmTjrR-QsHdKyg | Not English (German-language channel, Stilvoll ab 60); 1.4K subs | yt:style over 60 (German-named channel, English title) |
| Mademoiselle Spends | UCp2NEe9VThU1qvPDavlVQGw | Broad French-elegance channel (200K subs), not age-specific in About; French-lens lane territory | similar-channels / yt search |
| Lovely Angela | UCU79xHcniAuNH__P4RPVyOw | Short compilations (avg 1.5 min), 8.6K subs, no qualifying long-form seen; last upload 3 months ago | similar-channels / yt search |
| Morah Style Lab | UC2DYqiyhOt_bnixQhKQT0Dg | Broad body-shape channel (not age-specific); last upload 3 months ago | similar-channels / yt search |
| Curvy Claire UK | UC8EFGqdzh5pY8aKM0u5rjVg | Not style advice for women 50+: personal outfit vlogs (stilettos, mini skirts), About not age-specific | similar-channels / yt search |
| Classy Woman | UCQ-utJft-svYijXcgndichg | Etiquette / quiet-luxury habits, not age-specific (About) | similar-channels / yt search |
| Giedre Kavaliunaite | UCR28x4kMV_tHjQuMIiup5rw | Broad body-shape style guide (Lithuania), not age-specific | similar-channels / yt search |
| RZ Infinite Fashion | UCUxVYG91rM_EGtRi6o8-1nQ | 5.98K subs; avg video 1:59; best seen 24.7K (2:01); no 100K long-form seen | similar-channels / yt search |
| HalfofCarla | UCbKiDX7w3CsFiGjE8CqN1bg | Weight-loss / mindset channel, not style for women 50+ | similar-channels / yt search |
| Lori Lundquist | UCjdNY4n7VZ5fEgfutRELpNQ | Petite style, not age-specific in About (37K subs) | similar-channels / yt search |
| Attractive Women | UC9H-r9dXUUFqttd8xDRjSLA | Broad: fashion for women of all ages (About); avg video 4.2 min | similar-channels / yt search |
| fabulous50s | UCiWPU83VmOXjQ6xY0gIrhIQ | Met in this lane; already kept in french-makeup.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| HotandFlashy | UCU9rHRAeSzi--j1jkXQ47RA | Met in this lane; already kept in french-makeup.csv/hair.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Tracy Campoli | UC2sXkXBWd51cpk_5nyUha2w | Met in this lane; already kept in french-makeup.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Darlene Obiyan | UCcvRTuhJHnMMCHB1Q4MmIaQ | Met in this lane; already kept in french-makeup.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Ana Vogue | UCcai-ND1haM-bJtkOz_7oPA | Met in this lane; already kept in french-makeup.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Ebony lifestyle | UCzcEPpZRCK1aklhuUnNznzQ | Met in this lane; already kept in hair.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Woman in midlife | UC1exmI_KJ-zXoKQAdhhzc3Q | Met in this lane; already kept in hair.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Style In Her Prime | UC35JHXEfvrb62DZpbmSs-Ww | Met in this lane; already kept in hair.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Elegant After 60 (13K) | UC1eIOMYX7jZveQT3ezH59rw | Met in this lane; already kept in hair.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Sandra Sallin | UCdcl4w0uOvJhryVuUL3Vwuw | Met in this lane; already kept in french-makeup.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| rxstrmom | UCeY_QgW8iYhcv8GiZoDQ-Bw | Met in this lane; already kept in french-makeup.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Nikol Johnson | UCuhS2wb4EgcjdwPG-g6z3dg | Met in this lane; already kept in french-makeup.csv/hair.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Marie-Anne Lecoeur | UC3iINwXX6oQ0DqfE1SQ-S-w | Met in this lane; already kept in french-makeup.csv - not duplicated here (not re-screened) | yt search / similar-channels |
| Ageless Style Over 60 | UC8mRh_qJrGqR-izFtK4PAJw | Cannot meet keep rule: 3 subs, 1390 total views (needs a video of 50K+), created 2026-08-14 | similar:Chic After 60 |
| Classic Gent | UCFbEJORScJ2K2E_NjQVfBAA | Men's style, not women 50+ | similar:Chic After 60 |
| Diane Hartwell | UCXMFQXW2KDG61Gb1ZrcvNDA | Cannot meet keep rule: 66 subs, 22636 total views (needs a video of 50K+), created 2026-09-20 | similar:Chic After 60 |
| Elegant looks After 50 | UCV4cS9Wmraht0C1YEDecjPA | Cannot meet keep rule: 11 subs, 1800 total views (needs a video of 50K+), created 2026-08-20 | similar:Chic After 60 |
| Style without age | UCtabZ91H_V1fE5lfOs2yeyA | Cannot meet keep rule: 178 subs, 34739 total views (needs a video of 50K+), created 2026-08-02 | similar:Chic After 60 |
| Gentleman 40+ | UCvvn0thUkPz-Rm-thaKzgzw | Men's style, not women 50+ | similar:Chic After 60 |
| Scarlet Starling | UCTMwV-uy20eaRwFfc4Sx13g | Operator's own channel (Scarlett Sterling) - excluded, not a competitor | similar:Chic After 60 |
| 60 & Fabulous | UCjqiqlfmQtVcK8zxKrhD9Sw | Cannot meet keep rule: 437 subs, 28217 total views (needs a video of 50K+), created 2026-08-27 | similar:Chic After 60 |
| Prime Style 50+ | UCjdROdaLh381SpcNnlUhdzw | Men's style, not women 50+ | similar:Chic After 60 |
| Radiant at Every Age | UCCgzpIjLXkigZ1FliZ1NLag | Cannot meet keep rule: 569 subs, 41837 total views (needs a video of 50K+), created 2026-06-12 | similar:Chic After 60 |
| Trendy & Timeless | UCvApE6ZJqT19jwAcFyuZ3IQ | Cannot meet keep rule: 119 subs, 32369 total views (needs a video of 50K+), created 2026-08-28 | similar:Shopping On Champagne |
| christina amanita | UCf8vWBnTgffE8r994jGOBlg | Not a style channel (slow-living vlog) | similar:Shopping On Champagne |
| TomKat Stitchery | UCyze3rUDxYJSQigBwigZGwQ | Not a style channel (sewing) | similar:Shopping On Champagne |
| Eleganza-Stile Over 50 | UC591CBZ7NSvvJlwVnU3Jhjw | Not English (Italian) | similar:Vivian Sinclair |
| Stylish Over 60 | UCB6rbkmfVdmzqvrFfy9wkUA | Cannot meet keep rule: 110 subs, 11025 total views (needs a video of 50K+), created 2026-08-11 | similar:Vivian Sinclair |
| Best After 60 | UCZgkapU4VP6h0HoDbiT0Hkg | Cannot meet keep rule: 4 subs, 256 total views (needs a video of 50K+), created 2026-08-15 | similar:Vivian Sinclair |
| Graceful & Glowing 60+ | UCV_ZJuDD_rXcHZ22DF-K7mg | Cannot meet keep rule: 0 subs, 21 total views (needs a video of 50K+), created 2026-09-14 | similar:Vivian Sinclair |
| Ageless Allure | UCxE8p-eBaPRbE4HZb81blAQ | Cannot meet keep rule: 347 subs, 42031 total views (needs a video of 50K+), created 2026-07-11 | similar:Vivian Sinclair |
| Ageless Radiance | UCB_7WIbsrumw7hKVc8E-xdQ | Cannot meet keep rule: 100 subs, 5941 total views (needs a video of 50K+), created 2026-06-07 | similar:Vivian Sinclair |
| Ageless Beauty 60 | UCOPwN8VbdYNt_M0kgMeN_-A | Cannot meet keep rule: 552 subs, 44588 total views (needs a video of 50K+), created 2026-09-25 | similar:Vivian Sinclair |
| The Ageless Crown | UCcF7kQ-OWhdLHUM-DIiwebA | Cannot meet keep rule: 863 subs, 34584 total views (needs a video of 50K+), created 2026-06-26 | similar:Vivian Sinclair |
| Healthwise For Seniors | UCG2g-cTUJMWBNmMzkqB9i-Q | Not a style channel (health) | similar:Vivian Sinclair |
| Kim Sullins | UCvFBxvgf-zLTgmRHVe75x5g | Off-lane (makeup); 17800 subs - left to the makeup lane, not screened here | similar:Vivian Sinclair |
| Alice Luxe | UC4l04C6A_dog3pHfxoHggBg | Off-lane (hair); 9370 subs - left to the hair lane, not screened here | similar:Vivian Sinclair |
| Timeless Style 40+ | UC-TGG-M30FyF9qFjkGTOizw | Men's style, not women 50+ | similar:Vivian Sinclair |
| Camille Cowher🔸️Makeup Over 50 | UCo_cQhVAhCdp7S9RTcPFwtA | Off-lane (makeup); 232000 subs - left to the makeup lane, not screened here | similar:Vivian Sinclair |
| Refined After 60 | UCsKI8NjFFYR8A-sAC7eV8nw | Cannot meet keep rule: 62 subs, 6538 total views (needs a video of 50K+), created 2026-09-03 | similar:Vivian Sinclair |
| The Hair Fix | UCwloE1X8tiijwWESyV8eD7Q | Off-lane (hair); 2210 subs - left to the hair lane, not screened here | similar:Vivian Sinclair |
| HerNewChapter60 | UCQgy2_0_GWRm9qDeGCL3t5A | Cannot meet keep rule: 0 subs, 20 total views (needs a video of 50K+), created 2026-08-18 | similar:Vivian Sinclair |
| HerNewChapter60 | UC1N6oOPB2iUEHmul24D4vXA | Cannot meet keep rule: 2 subs, 118 total views (needs a video of 50K+), created 2026-08-18 | similar:Vivian Sinclair |
| Timeless Melanin Aura | UC4ihZWl6OT28sF-Y2A1spLw | Cannot meet keep rule: 697 subs, 35074 total views (needs a video of 50K+), created 2026-01-17 | similar:Vivian Sinclair |
| ForeverChicOver40 | UCMjtAVOT4NL4lI8rXREDUGA | Cannot meet keep rule: 406 subs, 37307 total views (needs a video of 50K+), created 2026-05-05 | similar:Vivian Sinclair |
| Tricia Cusden - Look Fabulous Forever | UCuflfWUNugwPkZOQUEyAowQ | Off-lane (makeup); 73100 subs - left to the makeup lane, not screened here | similar:Vivian Sinclair |
| Elegant Essence Over 50 | UCYX76nK3S6mKT9zBOkrIHdg | Cannot meet keep rule: 313 subs, 24363 total views (needs a video of 100K+), created 2022-04-09 | similar:Vivian Sinclair |
| Vital Aging | UCumi_hLfGyoJCNull6Ozcvw | Not a style channel (health) | similar:Vivian Sinclair |
| Golden Mile Travel | UCfV82sfrC9MPTfV4mZbRGtw | Not a style channel (travel) | similar:Vivian Sinclair |
| Tip Hack 60s | UCWaHmKqBXsoWmBgCezWIQrA | Not a style channel (general tips) | similar:Vivian Sinclair |
| Healthy Aging Daily | UCKdOEph0mZpnWV3eBKnNPwA | Not a style channel (health) | similar:Vivian Sinclair |
| 60 and Stylish | UCILZsdYkovsBC3nWB_BhJ-w | Cannot meet keep rule: 0 subs, 9 total views (needs a video of 50K+), created 2026-08-31 | similar:Vivian Sinclair |
| Ageless Confidence | UCxw2jFWBftkpRkFE4EC9W-Q | Cannot meet keep rule: 219 subs, 27099 total views (needs a video of 50K+), created 2026-07-14 | similar:Vivian Sinclair |
| Mature Elegance | UCa0oVGz5EA8Ufwz6SRJI46w | Men's style, not women 50+ | similar:MM Personal Styling |
| Curlyair Chic | UCR54MZ5pspyvcgJhIJv1eAg | Cannot meet keep rule: 518 subs, 70282 total views (needs a video of 100K+), created 2025-03-27 | similar:MM Personal Styling |
| 40+ Men's Fashion | UC-eazqFVXRzzyFymCJNuC2A | Men's style, not women 50+ | similar:MM Personal Styling |
| Timeless Chic 40+ | UCEkYsB33mDB4dDJLWrpAE1g | Cannot meet keep rule: 274 subs, 40913 total views (needs a video of 50K+), created 2026-08-28 | similar:MM Personal Styling |
| Dapper Dads | UCahyKEIYF9o2WsUzbFtytxQ | Men's style, not women 50+ | similar:MM Personal Styling |
| Beyond50Skin | UCX73yv8VXHQoygoYc51LnBQ | Off-lane (skincare); 32000 subs - left to the skincare lane, not screened here | similar:MM Personal Styling |
| Always In Vogue | UC-KKYkHbb0oa-5MZmI9mgKg | Men's style, not women 50+ | similar:Marie-Anne Lecoeur |
| Beyond Classic Style | UC7AwTxa5YqvFkgiND-DwtCw | Cannot meet keep rule: 12 subs, 868 total views (needs a video of 50K+), created 2026-07-26 | similar:Marie-Anne Lecoeur |
| Senior Secrets Book | UCyg9lCTVFfnyZ_GLi3799bA | Not a style channel (books/wisdom; last upload 7 months ago) | similar:Marie-Anne Lecoeur |
| EVERYDAY ELEGANCE | UCDsWel08uozMVkb-2F694oQ | Cannot meet keep rule: 10 subs, 403 total views (needs a video of 50K+), created 2026-09-13 | similar:TRENDS SPOTTED |
| Avas Beauty | UCqJZ_NHRFUbrFKMBkZ38S4w | Cannot meet keep rule: 169 subs, 29447 total views (needs a video of 100K+), created 2025-01-23 | similar:Elegance At 60 |
| TIMELESS CHARM & STYLES | UC9H-C6uJVKCRfE4zslwoHGQ | Cannot meet keep rule: 280 subs, 29687 total views (needs a video of 100K+), created 2023-04-05 | similar:Elegance At 60 |
| Style with Beth | UChmqzcHhCH8-hg6bDNVBIXQ | Cannot meet keep rule: 4 subs, 453 total views (needs a video of 50K+), created 2026-09-14 | similar:Elegance At 60 |
| Diane de Chambray | UC2z5yffdjwr3xpr-iDp9Yvw | Cannot meet keep rule: 62 subs, 13207 total views (needs a video of 50K+), created 2026-09-15 | similar:Elegance At 60 |
| Ageless Beauty Journal | UC3AM396rgaXNKhmYK4rb19Q | Cannot meet keep rule: 7 subs, 307 total views (needs a video of 50K+), created 2026-10-05 | similar:Elegance At 60 |
| Rachel Felber, MD | UCehnCQUUcpW34HgmeP_DgtA | Not a style channel (fitness/health (ER doctor, strength coach)) | similar:Elegance At 60 |
| Outfits for Women's | UCyJbyl5UYAMg7c7V2IGBFqw | Tiny: 400 subs, 220742 total views, best video 33000 (NexLev cache), created 2026-09-18 - below keep rule | nf searches (see log) |
| 50+ Men's Style | UC-_zbheM4YPHE4E8Vqux2eg | Men's style / men over 40-60 (2120 subs, last 2026-09-26) | nf searches (see log) |
| Gentleman Post | UC5vfB78wka0I_CAdHeql7Xw | Men's style / men over 40-60 (12700 subs, last 2026-10-26) | nf searches (see log) |
| Jenny Style Audit | UCpt2DV6j33Sf8c2F5VRDW-w | Tiny: 212 subs, 20484 total views, best video 4400 (NexLev cache), created 2026-09-04 - below keep rule | nf searches (see log) |
| The Mirror Edit | UCLTXZUZ7Sme8zekDHihbd2g | Tiny: 393 subs, 48379 total views, best video 8200 (NexLev cache), created 2026-08-16 - below keep rule | nf searches (see log) |
| Novokumar Ghosh | UC7lD1HImfYEbMZSAih1ibkQ | Tiny: 280 subs, 42681 total views, best video 17000 (NexLev cache), created 2023-07-13 - below keep rule | nf searches (see log) |
| Shifted Mind Academy 50+ | UC1QQoJrY2q9lbMFAWHFSfFA | Tiny: 189 subs, 70000 total views, best video 30000 (NexLev cache), created 2025-11-22 - below keep rule | nf searches (see log) |
| Evelyn Hart | UC35beahevoTdl2bGIBW7S3A | Tiny: 235 subs, 30893 total views, best video 23000 (NexLev cache), created 2026-09-07 - below keep rule | nf searches (see log) |
| Mr. Gent Style Over 50 | UCVTShoJ7vBF4awDMcZK3aXA | Men's style / men over 40-60 (2029 subs, last 2026-05-27) | nf searches (see log) |
| Eleanor Winslow | UCbwn6l34lEWhOIAjmPe4jzA | Tiny: 115 subs, 18083 total views, best video 10000 (NexLev cache), created 2026-09-08 - below keep rule | nf searches (see log) |
| Bold & Styled | UCtdx6KngcAGi4XKlVkQHcoA | Broad style (not 50+ focused), or inactive (2210 subs, last 2025-12-26) | nf searches (see log) |
| Ashley Grant | UCgXvIOk7meBAmy-dxQ4M2Dg | Tiny: 234 subs, 33648 total views, best video 11000 (NexLev cache), created 2019-02-09 - below keep rule | nf searches (see log) |
| Gentleman After 40 | UC4uF9yUiplXLJh9UDuKm3tg | Men's style / men over 40-60 (3150 subs, last 2026-07-26) | nf searches (see log) |
| Healthy Aging Secrets | UCuF-68zpaTQD9yVmoU2rI_w | Fitness / health / wellness, not style (4460 subs, last 2023-10-26) | nf searches (see log) |
| dangcongthan dangcobgthan | UCQXAU70bWa4BXzxbaHbqZhA | Tiny: 462 subs, 11953 total views, best video 2500 (NexLev cache), created 2019-01-26 - below keep rule | nf searches (see log) |
| Old Money Gentleman | UChyJ53n11vvyy_T0FxiUWMA | Men's style / men over 40-60 (451 subs, last 2026-05-27) | nf searches (see log) |
| Old Money Opulence | UCYn5-gd7AUq8DYIYj4cQxzQ | Old-money / luxury lifestyle stories, not women 50+ style (16600 subs, last 2026-10-17) | nf searches (see log) |
| Old Money Section | UCGMVt_ZfmG10SvxtGKImg8w | Old-money / luxury lifestyle stories, not women 50+ style (2680 subs, last 2026-10-26) | nf searches (see log) |
| Old Money Allure | UCVMHhPlUyHpgkzJWtfZ5j5g | Old-money / luxury lifestyle stories, not women 50+ style (73700 subs, last 2026-10-25) | nf searches (see log) |
| Gild Grove / Old Money Aesthetic | UC5UKPuji3fV6lWKb0CF2yhg | Old-money / luxury lifestyle stories, not women 50+ style (10300 subs, last 2024-10-26) | nf searches (see log) |
| Old Money Lovers | UCrrPCWBc0cEo_gGrIM7OgjQ | Old-money / luxury lifestyle stories, not women 50+ style (6570 subs, last 2024-10-26) | nf searches (see log) |
| Old Money Films | UCF1yfQkJTarDKb0K1mCsX_Q | Old-money / luxury lifestyle stories, not women 50+ style (1500 subs, last 2026-10-23) | nf searches (see log) |
| Refined Style Studio | UCMei1XtpepC0UBth8F9Hl2w | Tiny: 434 subs, 47223 total views, best video 17000 (NexLev cache), created 2026-04-16 - below keep rule | nf searches (see log) |
| Dressi | UCDQd2oNmc1O090rMFD9ETKA | Men's style / men over 40-60 (37100 subs, last 2026-10-25) | nf searches (see log) |
| The Luxury Lane | UCuLZpbu5_Yuw5sfB8vWWqYg | Old-money / luxury lifestyle stories, not women 50+ style (54300 subs, last 2026-10-25) | nf searches (see log) |
| Old Money Throne | UCY4wgwwf4Wq1-nD5XIkPFoA | Old-money / luxury lifestyle stories, not women 50+ style (4110 subs, last 2026-09-26) | nf searches (see log) |
| Old Money Mansions | UCb7-IKPS4DHQd2DBbwD39pA | Old-money / luxury lifestyle stories, not women 50+ style (87000 subs, last 2026-10-25) | nf searches (see log) |
| Quiet Money Stories | UCNjyn0Q1L2Mx0O4nXnXvfAA | Old-money / luxury lifestyle stories, not women 50+ style (1340 subs, last 2026-10-26) | nf searches (see log) |
| Old Money Empires | UCuwva7-m9V3IithchidKiTQ | Old-money / luxury lifestyle stories, not women 50+ style (14300 subs, last 2026-10-25) | nf searches (see log) |
| Oldmoney Explorer | UCEtPgo99rGEJUIAnObaBYwA | Old-money / luxury lifestyle stories, not women 50+ style (3790 subs, last 2026-10-26) | nf searches (see log) |
| Classy Man Academy | UCUOcqSzhVLaBf1gfxDk8R6g | Men's style / men over 40-60 (10800 subs, last 2026-07-26) | nf searches (see log) |
| Charles Ashworth Hosting | UCtTK69TxSbeDM4YCI5PG6zg | Men's style / men over 40-60 (560 subs, last 2026-10-26) | nf searches (see log) |
| True Gentlemen Club | UCR2qzS4F0Tbsk6p1wDNDnMg | Men's style / men over 40-60 (7250 subs, last 2025-11-26) | nf searches (see log) |
| Opulent Living | UCSqlhptneND0435u6TSQuNQ | Old-money / luxury lifestyle stories, not women 50+ style (2250 subs, last 2024-10-26) | nf searches (see log) |
| The Luxury Meltdown | UCf8pPw_UcIrRfVVpSTt5WiQ | Old-money / luxury lifestyle stories, not women 50+ style (13600 subs, last 2026-10-25) | nf searches (see log) |
| Duncan Marsh Style | UC_1ULk_xm8iW1ADone3RBQg | Men's style / men over 40-60 (2340 subs, last 2026-10-26) | nf searches (see log) |
| TheMatureGentleman | UCJEOLYrF4omhA2BxeYgd1ww | Men's style / men over 40-60 (818 subs, last 2025-10-26) | nf searches (see log) |
| Gentleman's Edit | UCUM0SHTKiI-kBE8QkhKfqIA | Men's style / men over 40-60 (810 subs, last 2025-10-27) | nf searches (see log) |
| Clara's Forgotten Wardrobe | UCeghtrf546YiyyokP9pw2gA | Tiny: 396 subs, 13571 total views, best video 1800 (NexLev cache), created 2016-05-07 - below keep rule | nf searches (see log) |
| Wisdom After 60 | UC5MkHMM9vnjSb0MFp4AmKgQ | Fitness / health / wellness, not style (14100 subs, last 2026-10-19) | nf searches (see log) |
| A FASHION | UCIq58g_1_vGIUQaRqmFT35A | Runway / swimwear shows, not women 50+ style (208000 subs, last 2026-10-24) | nf searches (see log) |
| jada | UC8QGhMCpngw0c9FcnGxYSIg | Broad style (not 50+ focused), or inactive (38400 subs, last 2026-10-22) | nf searches (see log) |
| Women Fashion | UCfLl_m81n2RMZivWtq3zhdQ | Broad style (not 50+ focused), or inactive (86900 subs, last 2024-10-26) | nf searches (see log) |
| NAOFISH STREET STYLE | UCC8HTUqnaCrHS9XiINM5k_g | Broad style (not 50+ focused), or inactive (53400 subs, last 2026-10-22) | nf searches (see log) |
| American Fashion, Beauty & Grooming | UCCvBfAbudEYZHPBxx9HwDHg | Tiny: 266 subs, 78358 total views, best video 39000 (NexLev cache), created 2026-08-05 - below keep rule | nf searches (see log) |
| Fit Over 50 | UCTKJUH1BEYRTzEOz8gsCg2g | Fitness / health / wellness, not style (5520 subs, last 2024-10-26) | nf searches (see log) |
| Under the Cover Podcast | UCUu9x-gupt__nk-qje7IxTw | Broad style (not 50+ focused), or inactive (2620 subs, last 2025-10-26) | nf searches (see log) |
| Vien Tran | UCbhdAaeCUpADCaAKvK9Jc-g | Tiny: 705 subs, 69715 total views, best video 28000 (NexLev cache), created 2022-01-09 - below keep rule | nf searches (see log) |
| Loya the Fashion Queen | UCBeEI6IogaHOvlVB47GKrcA | Broad style (not 50+ focused), or inactive (22200 subs, last 2026-10-14) | nf searches (see log) |
| JulieNne's Choice | UC3DZ6OlP8BmFw9Sz_TsQyCg | Broad style (not 50+ focused), or inactive (6840 subs, last 2026-10-25) | nf searches (see log) |
| FASHION FANATIC TV | UCEZNKbZ8VQHizm2eQb5rVBA | Runway / swimwear shows, not women 50+ style (10900 subs, last 2026-10-05) | nf searches (see log) |
| Iconic Runway | UCVUzjCw5VyOtbYuXnixvUoA | Runway / swimwear shows, not women 50+ style (3470 subs, last 2025-10-26) | nf searches (see log) |
| Diana Cole | UCajJYEIjY1hHNCKGGlF9e0A | Tiny: 140 subs, 18075 total views, best video 4600 (NexLev cache), created 2022-06-28 - below keep rule | nf searches (see log) |
| Hollywood couture | UCsHmvZ3g5A9tAwYO2o1mPMw | Celebrity / model-bio / red-carpet compilations (4550 subs, last 2026-10-25) | nf searches (see log) |
| Outfit Society | UC_48t_pgayuUzp35VkuQhyg | Tiny: 544 subs, 192138 total views, best video 23000 (NexLev cache), created 2026-07-06 - below keep rule | nf searches (see log) |
| Hollywood Observer | UC80qQDj1aAHNV-wudapTuIw | Celebrity / model-bio / red-carpet compilations (14400 subs, last 2026-10-26) | nf searches (see log) |
| Fit After 50 | UChBmQWO2Vf9Y5qkua0MMDPw | Fitness / health / wellness, not style (94700 subs, last 2026-10-24) | nf searches (see log) |
| Petra Genco | UCr2QF3zsAwLID2Z582FYiyA | Fitness / health / wellness, not style (977000 subs, last 2026-10-20) | nf searches (see log) |
| Body Fix Exercises—for over 50s | UC9QgDBvyfbflM9zCBqp2GNA | Fitness / health / wellness, not style (733000 subs, last 2026-10-05) | nf searches (see log) |
| Live Healthy Over 50 | UCctKiULeD3WEnrsSoM_xOzw | Fitness / health / wellness, not style (247000 subs, last 2026-10-25) | nf searches (see log) |
| AGE OVER FIFTY | UC6eXei8hHnRQ3V0smMgCsew | Fitness / health / wellness, not style (1910 subs, last 2026-10-24) | nf searches (see log) |
| Wellness Strong | UCbQtc2egEox2QL_8X_y6Jmw | Fitness / health / wellness, not style (9790 subs, last 2026-10-24) | nf searches (see log) |
| Selina Peachy | UCffpKuermbVBuluknCvt_yQ | Broad style (not 50+ focused), or inactive (70300 subs, last 2024-10-26) | nf searches (see log) |
| Fitness journey | UCJNG5KDGVzQwNYbJiySoBvw | Fitness / health / wellness, not style (40900 subs, last 2026-09-26) | nf searches (see log) |
| Queen Fitness | UCpF5DZx08oxpJvLhBNeVihg | Fitness / health / wellness, not style (5070 subs, last 2026-10-22) | nf searches (see log) |
| Truly Isabelle | UC6qAO-KodxFMIjssweXg5iA | Broad style (not 50+ focused), or inactive (59500 subs, last 2026-07-26) | nf searches (see log) |
| Booty & Beast | UC4SZUjGRLmvjvKKAJ155I2w | Fitness / health / wellness, not style (31900 subs, last 2023-10-26) | nf searches (see log) |
| Feminine Retreat | UCc_WwBWJGs7q3ZCXQ5L2bFQ | Broad style (not 50+ focused), or inactive (5610 subs, last 2024-10-26) | nf searches (see log) |
| Edel Belar | UCvXlKBsrexbtXBSgosxz0ZA | Broad style (not 50+ focused), or inactive (11600 subs, last 2025-10-26) | nf searches (see log) |
| Layla Fashion | UCxL5Q1badukzLkDOF7hIuaA | Not a style channel for women 50+ (pantyhose / sewing patterns / hair braids / hair channel) (72300 subs, last 2026-10-24) | nf searches (see log) |
| ChicWears | UCAM_h6tD5tyumfNGd-izU0A | Broad style (not 50+ focused), or inactive (5420 subs, last 2025-10-26) | nf searches (see log) |
| Tanya Swizzz | UC4wMHKXG45lC5Q1zVTtQILw | Broad style (not 50+ focused), or inactive (37800 subs, last 2025-10-26) | nf searches (see log) |
| Fashion Show | UC6pOIwoFyOmS1bwRaGvxdkQ | Runway / swimwear shows, not women 50+ style (128000 subs, last 2026-10-05) | nf searches (see log) |
| rockstarcheveux | UC00MBBC-JH7zM0yz02vvWrw | Not a style channel for women 50+ (pantyhose / sewing patterns / hair braids / hair channel) (67400 subs, last 2025-10-26) | nf searches (see log) |
| That Girl Journey | UCqLJ8CabhqM3CSZXCJuB3tw | Broad style (not 50+ focused), or inactive (18900 subs, last 2026-09-26) | nf searches (see log) |
| ModernWoman Apparel | UCeTXqeLXmz5OR09DN5Xoi4w | Not a style channel for women 50+ (pantyhose / sewing patterns / hair braids / hair channel) (42000 subs, last 2026-09-26) | nf searches (see log) |
| Erica Joy | UCbjGxE4fzyPAoHAoY4LLdhA | Broad style (not 50+ focused), or inactive (7520 subs, last 2025-10-26) | nf searches (see log) |
| Hamel | UCCJ57t-PkZnH8mqUk6GOl-g | Broad style (not 50+ focused), or inactive (96900 subs, last 2026-10-21) | nf searches (see log) |
| Percia Verlin | UC4bYC7O9yRVYuxC4NP2w2ag | Broad style (not 50+ focused), or inactive (105000 subs, last 2026-10-12) | nf searches (see log) |
| Enduring Attire | UCB_pgOzMdSPSGMA2PRfnKxg | Broad style (not 50+ focused), or inactive (14800 subs, last 2025-10-26) | nf searches (see log) |
| Glamour Waves | UCGC1zPjp0qrwLDULqlYzpEg | Broad style (not 50+ focused), or inactive (7640 subs, last 2025-10-26) | nf searches (see log) |
| Toofierce 1 | UCaf24tOYsvqHHqGsuUGi9bA | Broad style (not 50+ focused), or inactive (3790 subs, last 2025-10-26) | nf searches (see log) |
| TimurLand | UCuMVzMlqHQzXRdERL_8tEFA | Broad style (not 50+ focused), or inactive (8060 subs, last 2026-01-26) | nf searches (see log) |
| Beautybyemily | UCRZZQL0jQ0aipT6pWKPNDng | Not a style channel for women 50+ (pantyhose / sewing patterns / hair braids / hair channel) (53000 subs, last 2026-10-24) | nf searches (see log) |
| Pose perfect | UCvYZcvLch4hrr-f7sHB54OQ | Celebrity / model-bio / red-carpet compilations (13100 subs, last 2026-04-26) | nf searches (see log) |
| Curvy Model Moment | UCxCsGeZ_E83jwaKoYO_Uc8A | Celebrity / model-bio / red-carpet compilations (5860 subs, last 2025-12-26) | nf searches (see log) |
| Apex Beauty | UC0YbI_DgYgj5iIWFjIMbxrg | Celebrity / model-bio / red-carpet compilations (8910 subs, last 2026-10-25) | nf searches (see log) |
| Mr Curvy | UCPE8IFhcl35PFt-iZPwUnTA | Men's style / men over 40-60 (43600 subs, last 2025-10-26) | nf searches (see log) |
| Today Is A Plus Day | UCzk6wMw266PTuTMvrw9TrIw | Celebrity / model-bio / red-carpet compilations (13700 subs, last 2025-10-26) | nf searches (see log) |

## 7. Similar-channel results dismissed as not candidates (314)

Name, description and stats from the similar-channel about data showed no women-50+ style angle (examples: news, celebrity, kids, music, men's style, travel, fitness, non-English). Listed as name (subs, ID):

Belleza Serena (213000, UCtMRZDhdzhGeCnWQb4IXBrw); Elegancka Kobieta (4880, UCC6_5drFrCuH8tZ8Nq0Kkmg); Camino de los Ancianos (61900, UCy0Y3ykT36UiCZBEDpXmUnw); 시니어패션tv (7920, UCq519bGSR2FP4KRAj-AsA7Q); Stil mit Reife (11100, UCSEMXisj1-DDM3-xC2XEwOQ); Élégance Après 60 (3520, UCfToK4QQsiisVFwmpUmZbYA); L’Âge du Style (5370, UCXVKNeABG8f5shd_aNc0GCw); Elegant ab 50 (1100, UCk9XNYRzz_l38cPl_6y2byw); Donna Matura (3990, UCLcnFdxIXNuLdAsEy8PRZuQ); Styled by Marie - Anne (78, UCLa8_D5YgVZYzSRkJn-B5aw); Outfits for Women's (403, UCyJbyl5UYAMg7c7V2IGBFqw); Novokumar Ghosh (285, UC7lD1HImfYEbMZSAih1ibkQ); Hae Mi Jane / Outfit Ideas (14500, UCg56mWoCfkNuXd7v_rJ0B2g); VisileModern (36700, UCT9aY_JY8yG_-dyaq368dhg); Airport NOW (38200, UC-GisSy1AobuPqxU1AafuJA); Jewel Verdict (146000000, UClSNP4s-_ZqcWR70uXDac0g); Style 60 Plus (1570, UC5FXoHc8OOGlrKzqTvVaCJA); BlickPunkt (3880, UCpeqZf4fMfKE6b5vYM4LpLw); Romantic French Music (29900, UCFZDgXljncRAVw8CMMzpDHg); AtelierChanson (15700, UC2mbzMre4pRTEw2BacPOaxg); Honest Voices (33800, UCymOM3aTF-7qSsI6aZJuj-A); Lisa  Life and Style (70900, UCKHO2e2sy2wqu1Ch8j7zfrA); Anna Rova (41900, UCiaFjH3AgBXoKiJjZDrEUKA); Miss Louie (534000, UCLhdpWK0herl_LAY3gySqLQ); Gemary Ermus (245000, UCtHwyuBMGZwxQAgNpvVe-FQ); Alyssa Beltempo (307000, UCU8ssMY0rZQtCgWVwQNpmUA); Valentina Schick (139, UCan9cpXy_LxiKySPRSFi_2w); Desi Rich (255000, UCDq9gkJSg2mYFtbpGyJ4kAg); Julianna Lee (86200, UCvYiqA54CuIW2ETJJnFLY4Q); by CHLOE WEN (185000, UCm7YDmFAzoVolBri3OiFkjg); Timeless  Elegance  Style (91300, UCOkJSedGdibbqg1ucO7W5Bw); Trend & Eleganz ab 50 (16100, UCAPujE1qTP414OtXGJtBHVg); Petite Dressing (462000, UCgHwP4zLihxk-teJXTFmNTg); Annie (24100, UCKuVB_5H_MnnvxpXAIYAbhg); Brooke Anderson (14700, UCaJvZMVXxYpVfs-HmV9op3Q); Patricia Mycyk (99500, UCnofNUJuSu42XfiI9cI0JTQ); Violetta Genova (16000, UCdm1SDjcqs3jdoCrCugxvEg); 센스쟁이 언니네 (14200, UCY6VT9RFRkW9WGUHioqa26w); Parker York Smith (1170000, UCDHnXzXMy11cWm95J-Lw-bQ); seenbyluna (1780, UCYi7DfxLdJEmElLWzxooL5Q); Gemma McLean - Grounded in Style (11300, UC6yCi5I9R5Mz7FdW8WUxf7A); ♡ Mirella (38700, UC9akBE3w9lIftCVZ2ai92QQ); Emma Hill (409000, UCYUE4U_lp7YPIB0iXxnTjbw); おふみチャンネル / ミニマリストライフは楽し。 (68500, UCrhw-2rnDD6TmyeSMdMQQAg); fashion logic channel Kotaro Doi (65100, UC8BaUjB4zYkOeNS-MArmeZA); Chincha Rabiña (1080000, UC-oZptQjNysb-MsikqQJs0w); Certifiably Jenny (6010, UCbSzSpPOL3rMiVXXSX_H85g); Bridge of Life studio (1430, UCPiVj1n7hsOWqQLstl7IPYQ); Genx Gypsy (60800, UClmv4uNKPg9hLXcTHBDvVjg); by Tashira (122000, UCc95c_6uMb1VyFEJjgydHRA); Rebecca Rowe (350, UCrLU_wL3TiUbzai1BOevOtQ); Alex (258000, UCG8Ek6j9-NW15qrCgJZdErA); Lynda @ NewAgeBeauty (78800, UC-3dCfj2kP0s5lB_Wg-H-7A); Ellie-Jean Royden / Body & Style (393000, UCp9uGwRfXSFVlYg6qRA5ERQ); Liubov fashion (33100, UCyWqvMS3sFGUy9M3RNo0Ryg); Your Guide To Style (96200, UConcXdLCLexF_9RKlQUf0ug); Elana Kinda (81700, UCH7Smk5Oev0lR6Pn5sWgMJA); Dana Berez (167000, UCAHNAm34YmE_4k6iq9Ig0vg); Stylecure (1480, UCm3P9a0lML27MAGQLzJWoiQ); Outfit Repeater (25600, UC1Pe2_qht4jlw6bG7zNLUPg); Maria Teresa Lopez (44500, UCxT_up6KTpYGBUWHbDUdOPw); Audrey Coyne (824000, UCdF5QXMUx1tT7odhtBdDyEA); Victoria (1060000, UCyxZB7SqkRFqij18X1rDYHQ); Carrie in Peri (4840, UC2k5ydvB6D9qPQ3hz_0extg); ParisianVibe (617000, UC-KUF3oGTSSuix72gBqamWg); Gemini Stitches (6760, UCbrKHDsYiuYSKmmpsoI0pow); Dearly Bethany (1160000, UC4HsumPi975_XPqpsU2tAqQ); Madeline Hegedus (79100, UCNVB6_eY4h2Xj54dQFxjJ8A); Simply Cerisa (7200, UCY8dGEhs8pi_B6wflOmGwaA); Allison Baek (487000, UCEzPt33mdyhRs3aQPhiN_pA); Tisha H (10200, UCDOIouNfZJ_qk6SH-M347Yg); Monroe Steele (147000, UC2y1XeYiRRXKKBCadTe0v7Q); Dolce Vita Fashion&Lifestyle (26300, UC1J9qwQqyZbEvwWccy4-nHA); Digital Pattern Library (34300, UCjY4F0YdIRlY7nXaOxRiQJA); Miss Wow (68600, UCNPYiyEQrZtGpYnNyrlLDqQ); BeYourBest (920000, UCiuFO2oly5EjOxMfuJbhFhA); Rebecca / Sew Pomona (5080, UClzhV2badgx3HHhdG1uWHDA); Tim Dessaint (1580000, UCfJrdVVcWZMHLC--a4ovLLQ); Glam Girl Gabi (781000, UCYoiYowIowF7tYYel9NHpKQ); Meghan Livingstone (303000, UCSRynFqyrqF3IqVcwmu0Hrw); Daily reflections with Anshra (2690, UComTQFJSEupqR5lbHTFBAYg); Justin Hickox (694000, UCTfRM6bqWXYyCcs_78ywftQ); Justina (82100, UCQ8SRxehWl_cbboVCI3MDpQ); Jillz Guerin (995000, UCzR9e4gHwY1kOM0nFMcWe0A); 10 Years Younger (27300, UCViorfQaEoD32u0gWqmhwLA); Style With Refa, 6.4K views . 2 hours ago (122000, UCF_p08Z3e9t66XMzRMKfYPw); monica fashion google (2670, UCfiw6eHMAazLKWVpuBCQq4g); Shilpa Raidas (85300, UCNzMzNswnQzdrUWgEIyB1Qw); The Measured Life (19200, UC1Zme5QCTgydoSpxYfwwSPg); Face Yoga Studio (183000, UChbC-8zb43SbJp2f6JxK-Fw); 활력하우스 (4440, UCg-63ozgRqF9A_73m0c6BtA); Dr. Anil Rajani (1110000, UCEtV88L58Bnb9er_PP-oWQQ); MypersonaltrainerTv (489000, UCtKXnFU2lu0pOdipAnQyBzg); Aly Smalls (292000, UCjHBvutnv4fE6EoBjbBZHKg); Boldnessby4 (53000, UCNK8Nx3jjulsjEnilEWVcZw); DIZHA HOUSE OF FASHION (46100, UC7HnNwP5yQicSMEFKCbjA1Q); Sewing Passion (11700, UC3611V-p7GQADv4veuiJGGQ); 123 GO! Planet (290000, UCvKFtvWVdGQtVEKFhG6PxPQ); Pierre Dalati (2950000, UC8Av1tO-ha143nNYzxmf1Fg); Hey Jawaria (5410, UCimiZ4qOlVpKYROn4rIVFOg); Kushi Maqbool (1400000, UCKiLwmDpKLZldOelUcpKydw); A Lighter Life with Charlotte (12400, UCV9EUcWeLDB4IJScwE_1XIg); Good Morning America (5510000, UCH1oRy1dINbMVp3UFWrKP0w); The Update (163000, UCe-9r2bMxhayJI-VjNFePgw); Lara Sewing (450000, UCVBzetMCiMvMBUSgADolCtg); MsMojo (5770000, UC3rLoj87ctEHCcS7BuvIzkQ); Razor & Style (7570, UCn5nfkbo6og57wE5_OcF4ow); Ivy Nicole (576, UC4gpPUvoq-xxMdsFMHs9Bwg); DoctorOz (2000000, UCc8cHxAZ3jwWkrrDyaLwDUw); Doctor Youn (5570000, UC9HQXWbt14wTdr_Tzc8ZE0A); KlarerBlick (8480, UCkb483SvyY4lmP8YQ9FB70A); Stil kennt kein Alter (4980, UCdsbpdB0GuhrT3Ruw2LhnAQ); Fame X stars 60 (133, UCSe1k-QNaHcCdSE3bmdteDA); Phong Cách sống (7980, UC3Vhm5ZOumYZJLkda6jH04g); Sylvie Roch Fashion (, UCWXAqytZ8OqsVUI1hEudUHw); Timeless Gentleman (4930, UCrO1nbyCtTH-fIW7Z9Z20Lw); Sue Porter (None, UCXimVMkKOdXqpptWFIWeGRw); Real Men Real Style (3720000, UCmRfQHc3U4fV1-i8Ry1HmtA); Nancy Harlow (None, UCDXHbM3rszafW-vJg3Nxq2Q); Health & Science (2180, UC_bhb099SyHITzMpy3bTgJw); TrustyShoeGuides (8950, UCN3nXbSFqiEmjx9U4z5_GAg); Stylish haircuts (206, UCMvXFDgAyhr-KZrY0iUQdug); Dazzling hair style (302, UC-r2D4SmNHIz7YL8X--WrKg); Trendy Short Hairstyles LookBook (55200, UCQW-RcqcD7WD0PU-PMqIkyw); NewBeauty Magazine (314000, UC47_xW02caxPoJxZVuzbhDw); Infinite Garden by Beth K (10500, UCDO9emSTIB01KhWk7lCB3XQ); Her Glory Gray Hair (145, UCZ_-ybMqmETX6kFQT8L-y6w); BobPixie HairStyles (3320, UCY50cJcqWO8AE_dDzrthgWQ); Cosmetic Tattoos by Rach (1070, UCHqRFvnwaMFVvWLOQfdk_xg); Timeless Femme (14, UC-45I0qBHVOwUAc712cDVJg); Teeth Talk Girl (844000, UCoWqwg_7NXuvoJZIgzHf8Dw); Trendy Haircut (203, UCVXYrsQPbEkjh_zwJgtcSuQ); SRV (1890, UC4vSJFORn0vOdgvT021374Q); Huberman Lab Clips (1500000, UCkZjTZNvuxq1CYMS3cwZa1Q); Baseline Dental (81000, UCrayGf-fUZPru_cagtvI_ng); Fashion and Style Edit (199000, UCeKN1FCLQbW_CFzrRXlv1iA); KANAKOおしゃれ迷子のオシャレ探し (216000, UCFjJt3fFi-diIJ53OpA9NKA); A N N A R E I D (214000, UC0DsQklZE7kyWTx98QPapwA); Bridget Fisher (18600, UCyp6bHEwRL03WvELlZWUVlA); Find Your Fashion with Neha (175000, UCwrYckPz1R1-FEzqL60evuA); Vilma Martins (57400, UCEOYDg5tIg7cHbWjZLjYCMg); Harry Has (358000, UCOSB1BAWREqnFHWI1A4n6ow); Ellie Richards (35500, UCe_wxUe-s32EEuEJyG00U2g); Fashion Tips (23800, UCDdtmklCWlTwoklUCE7XQPw); Dstyle - outfit ideas & outfit inspirations (28400, UCxmpyg5qMnSua2lgZ4bLvXg); MAIAZINE (154000, UCuvIgsu-bRmJtrooNgfGACQ); MILAN ON TREND Live (117000, UC_nlGK-4qqkxxH14JVwaSYw); Laini Ozark (338000, UC7QdhHIZ7TUJYjnZXRkRaaA); Sarah Ryan (23100, UC-Mv5IaDuufnCDeJ1DZ-ycA); 45+ Men’s Casual (24000, UC1YvgrBhWfMuwrimi4Jw0NQ); beepworld (158000, UCDFaGHrYtg_U72sTTU5XDcg); Lauren Messiah (88500, UC-B4Ec_YqNreCpmmpARAUXQ); Vaibhav Keswani (754000, UCnd5xZAWXs0soICzuxGNtFw); Asia Jackson (710000, UC6ZCeXD14B7WAJO5nsjGryw); Ciara O Doherty (256000, UCxZZCfJohaloPldKKwVObeg); Aliceinparis (142000, UC4MBo52ZvRib_GZav-ZpOcg); Fae Jagdon (1180, UC9AwSbmvhZnDY35mjqr160g); REVOLVE (53100, UCcVjy3JzHHzIWZp3ND3lqvA); That Trending Girl (12500, UCpB9K0RrHs7Ud_QQ6XdtyFA); Walking Together (236000, UCbVDxpi3ZeCay6y4PmwDsmQ); FWRD (19000, UCQ85u4fHO7Ng1jh3d3R8pKw); Stoic Wave (57500, UCkg52KfuD8Evhr8LgTE3ujg); Duncan Marsh Style (2350, UC_1ULk_xm8iW1ADone3RBQg); Olivia Kindle (21500, UCAtOvm9aRskDYrViiZnp85w); Peshkov shoes / Оригинальные кроссовки из США (33100, UC4uiPRVoiWxtR65K_aYUgSg); The Mode Report (2310, UCDtxeI2a7mGaB2hKI02hlXg); Erin Nicole TV (132000, UC-SMshzkuetzs4mNHZmJwUg); Allison Bornstein (59700, UCMYv2v0LdaWxv4HqKVHL3cg); Claire's Monologue (171000, UCf_eWKhIcGbF4TFrfYZ9ZZw); Kate Deluxe (1790, UCMwn2WwtEr9rp78BKfqlznQ); Christina Mychas (499000, UCzC9E3yXJoBSBfUKpDQKw2g); GSC Journal (770, UCuoGbO3VdU3QyEsi97c4Jbw); The Business of Fashion (197000, UCe1qICvWRDbdH7-Fixvj7Bg); Tamara Kalinic (531000, UCwLnjNtJw8Tsa2tAJW7-nnQ); by bella (134, UCZC5e6Exz2j6oguDB6gcwog); Bliss Foster (451000, UC1OR9yjgsvoFK3xxhCs-19Q); Nina Ubhi (736000, UCHUJ5ydbxEDm0uZ27sw3R9g); 목단MOKDAN (51600, UCO89GdC-Yxc4dPym5lE21VQ); Gentleman's Gazette (1820000, UCEgoThiTZG6wbTVA6B1Ksaw); Robin Rae (3800, UCrKvYzxNqjv893dGzuY476w); One Pack Wanderers (110000, UC2jOcQnwJDw5D25dMFrIUJQ); Sana Ansari's Handbook (63900, UCNrptAc_0Rr4cS4ORwR6fPw); ASMR Beauty Treatments (190000, UC7gq8OJjwl0wFX-JCw0fr6g); PiQtour Japan (82900, UCoC6YquSPNoXwJ9dZzL7_Ag); Christie Ressel (128000, UC0dcCISmgepE1dDdKBErx1Q); Sew Show with Shae (101000, UCA5YAzEaLaaHHJuEnbAicJA); Notches Sewing (526000, UCPVOzJHrFW13AbxgM6msi0Q); Fashion Mentor (7340, UCuHgDlcrvj2UAkVMiA-re4w); MANORA (1010, UCsugureEY_Nd3q5vDbBV61w); NAOFISH STREET STYLE (53400, UCC8HTUqnaCrHS9XiINM5k_g); kelly (553000, UC4Od06BfmUtZ6yb_Wb0uU3g); Funto's Flair (1990, UCNI_C4o8BzkXewb1nQCb1Fw); Real Person ASMR by August (363000, UC_RnbA7Hxr-KNPj8D3ussNw); Kensho Quest (128000, UCGcTPkD7J5SHdxURhWIdiqA); Natalie Zacek (426000, UCdaxSc8XWgjRJ1saDlr7JNQ); Mel Robbins (6360000, UCk2U-Oqn7RXf-ydPqfSxG5g); tara lynn (172000, UCWm1wbBu-Tf1VPSC8EakHDA); Kaur Tips (1430000, UCjw7M5WI3ZYO-j4DDjS5evw); Happy to Wander (Travel Tips & Inspo) (203000, UCu_ddDIgIZREFg_N_1-z4nQ); Alexandra Gater (993000, UCrh9tOpAY2-Ev5pRssXq2Wg); Pack Hacker (347000, UC_rI3y1DzDULTr-UIvshiwg); Her Women Life (20500, UCFymz4ExX3I8YAob_3w_Y7A); Fashiways (945, UCgi8Iay5S1-dv23yL5ak-UQ); Repair & Rewear (153000, UCnebvDXGqMhsaomITkVtwng); Downtown Tailoring (192000, UCfFpsIL7N44Lj5GZhfoPrdw); HGTV (1110000, UCBiuljj5uaUVHbnTAzfvutg); Professor Pincushion (607000, UC2QSX1z7lvF3bWXv6sK0UXw); Not Enough Nelsons (5600000, UC-_KiH_Z2yerhAD_cAjAMOA); Lydia Naomi (150000, UCo6c0lfyl-qAZlB_JaIklWw); Tale Handmade (806000, UC5gFBJJue2Y95WR7IDJGwHQ); Aplins in the Alps (106000, UCi1Xq_gjK1LxT-AQ1Wdsrrg); Hello Sewing (107000, UCTrsNvwHducP2zQFi1MS0ow); Ronald Reagan Presidential Foundation & Institute (1360000, UCEJi23qnygQHE5UeLXoV_JQ); Retire With Style (5090, UCkOSdTtgxpAUCnCLC6MEFyQ); Paris on Trend (1990, UC4WjgDfO4CDS0kRKH62gR4w); Shine Poe Zune (29800, UCVXvjHvzuESziJtzn_fKxag); Face Yoga Expert (473000, UC4xcFhl2nMbseJO9nEl_kog); Titi Toys and Dolls (6380000, UCXodGGoCUuMgLFoTf42OgIw); TODAY (5120000, UChDKyKQ59fYz3JO2fl0Z6sg); Miarti - Sewing Tips (1450000, UC2oQEVuGx3OSsyhwWCJHoSA); World Fashion Channel (259000, UCtkq2EwnU6tLra6BRoalz9A); The Stylish Gentlemen (76900, UC2UEqxXiCVFIuTx8yXb3_pA); Natasha Gibson Germany (207000, UCSkK-qENLho-q-6x1PKu7Vg); Daily Helen (140000, UC68UNOyKiIkuHLZlrVTN9PQ); Decore Sem Pressa (173000, UCBuSt9QvL0VjmpvhQ3vz-vQ); Colourful Noir (75900, UCtbdd75kTp7auUhrO--yd4g); Women fashion (11700, UC5yvV3rgIvvQR0q4-j4Eaxg); The Simply Posh Style (3670, UCkVoaGTiaiLwbg4DKc-zNzg); Gentleman's Edit (808, UCUM0SHTKiI-kBE8QkhKfqIA); Everyday Fashion (1710, UCUBTtXWynzBLF5TeY1QtieQ); Deni Kiro Personal Stylist London (1120, UCsgm3ln14tCd2W0up7J_0Mg); The Style Consultant (75000, UCzdScm9am2TzHM7G15i-FwA); kasper norgaard (3240, UC_YK09Y6MqhTcLE0ph6wwMg); Outfit Society (543, UC_48t_pgayuUzp35VkuQhyg); My Chic Style by Hailey Feldman (1480, UC5lfbmquR4q7a-C3rRj1WHQ); Joshua Becker (350000, UCBMKymQczkDxCpE1R2vvA4Q); WELCOME TO MY CURLS (174000, UC40WCzb-Uc1jNcxPBg2emxA); Anita : Sequins and Sand (54200, UCBSjYYBWlgbrZLhu94YK-Ug); Velvet Haul 4k (3530, UCvQo-TyigkCr6mxGUnfRuJA); Neeraja Ammus (156000, UCuw5VpFLiFL4duzErnJ4EDA); Curvy Swimwear - Curvy by Capriosca Swimwear (72700, UCh64Zj3U5boUvn9oWE5Jb2Q); Creator Insider (931000, UCGg-UqjRgzhYDPJMr-9HXCg); Nadine Sykora (6960, UCxV_eEPgGfKirgy6BpsCYWw); Adam Ivy (63400, UCNFEngs9Na5nf9iIlYQDB9Q); Goddess of Salads (125000, UCT71o-RYm3AgNDp_-rxexfw); Luke Hodges (28000, UCQrY-y8BaUt5xqWqnYDiJpg); Esencia Femenina (47900, UCUfq5Zy-FXU2Oi0EOAq1zLw); Return to Elegance / with Elisa (52000, UCtI9dGg8bFD1d7mO1mX7QiA); Grace And Style (3860, UCwfLJMhm1nhujPeV7EkvS7A); Classy Vibe Fashion (6400, UCPEpSEpPlFdwLoWCUqsJMDg); IKAMODA (60800, UCDoqy-lWHe8W0lcvSRhZe8w); Girl Talk With Ju (20900, UC4kqDNfR5A0no-sG4zkMXFw); The Gentle Wardrobe (41200, UCxYa6mbW-_htXfixim4QPFg); The United Colors of Style (19300, UCkYm-XJGXpuv44m-UASajaQ); Simply Styled Up (2230, UC8KZCELLgqBQ6Y5_QOlIyDQ); Nick Alexander (83900, UCp-lIhAMXFfvHTwB5Xh73Xw); Italian street fashion🇮🇹  Rome, Italy (62800, UCQh7Qf5BMKlUigdyF7kEmHA); Parisian Outfits (2120, UCGCB1LKOKyRa2JID3rJ2ulw); Như Nguyễn (15, UCF_6MQY2NzLhvFsLOuaPLZw); Billie Newland (154000, UCTqgYnpEv0QaWhOwSBsRLRQ); GOTHAM GALLERIA (37200, UC6n2VZtq4pDtfEAluIWZFQw); Amanda Siedler (3590, UCsOXYhBgpvldsvguWJU9Kpg); Milea Fashion (951, UCLKC71UHD1RymAjnkWjsADw); Florence Fashion Insider (1100, UC9kSaetd7ITjpHVj3-miTsQ); Drew Joiner (393000, UCc0-cA0mThWPk7_PGjT8oFA); InStylePhD: Fashioned to Lead (6340, UCvQaBhzCUwI-I17qqHQ-wOQ); My Clothes' Diary (718, UCcSM8qBKO7YsxKpTKFNs6-Q); Genevieve Daily Beauty (6960, UCp6FL3ogFiu6H6hHJ8NU4mg); MILAN ON TREND (321000, UCpKgjGCyZ-gvNdLxh-nPpjQ); Zoë Bergman (335, UC9pefoOI3ySpqutvwenOcYA); IslandChic77 (4470, UC2lX7tl8gr3rShzA_M4wtzA); FOMO No More (166, UCsbzI8Ya1gLX9L9HR2yZFsw); Trendvest Fashion (282, UCJhg33egm-JbfLlVuaYGwiA); Stylemebetter (13800, UCQ2JHpnqy9HroPZyJLxYWnw); Clare Walch (15000, UCldytZeIniyeoUzL4JB4WgQ); Mar Gallardo (113000, UCoZF91JUgIGcQI4y0jP6hCA); FASHIONPHILE Collective (362000, UCUGPEKFkv_FeT8UF9NgtM-Q); Silvina Gaiero (9700, UC4e-s5WIhqxPgwv0O21dX2A); Natalia Chicago (7450, UCRK8TDBPCiPfOx_qBgAvtZw); Fashion Trend Updates (8080, UCYl1C6NUpvbUntHz0Soms_Q); Jennifer Lynn (43500, UClAzCC2a99df61TQiuYNdvQ); ThriftyMaureen (9110, UCB5_x_TLdkd5dDcfj3sKhsA); The Iron Snail (777000, UC-0kjvCj9Z_pL_yH648Uq7w); Katie Nicole Goddess (13600, UC3gT8HF7SXAQs7WIAfSZpsA); CHANEL (2940000, UCclHSnngVTZK7LEOQAzcg1w); Taylor Morello (42100, UCfjujgVWyA6uS0owCea28kg); FF Channel (2540000, UC3T5fmgL4Kvk3kG1kF6JFeA); Fashion Insider (344, UCcOUK8FwYbeyN012QzDCGKw); Falabella Chile (134000, UCMLH0vqjhCblKOjFVBG6IQw); Sarv (7080, UChw4GH9IB-il80PpCfKVB7A); YayYayBoom (238000, UC5z5H1uiZBbft11lFUFiz-A); Simply Sasha Noel (9340, UCqhImwO-C0j1IKhUDjj1sOw); MATCHES (11600, UCcY_dnHqMukFmCiDydY0btQ); Kay Mollah (89700, UC4hLMzedbxOYZiIoxdqDT7w); Stylish Curves (131000, UCuQzPtoVu5EUHVJ4hGt-CXw); Libby (142000, UCqXL13aYkzltvtTta95kIFg); Simply Maggie (7740, UCRRXz5_hGCQbfOj2Cmx5DXw); Isabella Moretti EN (383, UCu9wUF4wrOeZ-ie-2up-quA); Janiece Styles (4260, UC7eE-WKMFYNd1dNAUrjK6wg); Sylwester Isley (, UC83ZVF1MUSZ0BgM2895GCzg); Erica Ball Style (17700, UCD5_DIfFTgDsGhj5Aey7qcg); NasrinS Artenest (1290, UCG-aDTjEQD4k02A6OWPauYA); Donna - Petit Dressing (253, UCsJNFIuYvVaWtzqxkLseMAQ); Lina · Elegant Style, Never Boring (1580, UC8ZKP2QEFlP7GOfAzjIBQ8w); Fashion Mantika (686, UCCyXqRy2wU-TAs2PzZIXr3Q); PALOMA FASHION TIPS / BEAUTY / LIFESTYLE (15, UCzWX0DQJaUYMplIK5R9PYDw); Own Your Style (2, UCMLWyEG-WZSVNgcqNCnzxlA); Fashion Streams (4320, UCrMdhq5jX3SI9F-ic4kvXaw); Mahhima Suneja (344, UCLZ_8Fl9VX7cyu1YJce8nqw); mehakaura (250000, UCE4Ty0MKNXtzw4bxO70UKeA); Arabic Engale (5480, UC1BGCyJhjo66-ORRdfyMTiA); Linz (174000, UCf1afJO8KD2zBZ5bGtO1HCw); Modeling Show (1030, UCwWumTIzjVlzy2OiucjdOeQ); Pose (284000, UCHPaTqSUEAzvPgDDttGAO6g).

## 8. Found but not fully screened - pick up after the NexLev reset (2026-10-31 06:56 UTC)

97 channels. Stats are what I saw before the limit. Most need a popular-sort check (a 100K+ long-form video since 2022, or 50K+ for faceless channels under a year old); a few need an audience check.

| Channel | Channel ID | Stats seen / what is missing | Found via |
|---|---|---|---|
| Chicbagstyle | UCHS-8nkje-_xYLa63dRIUug | Light check: NexLev batch avg 228 views/video, faceless=T, monetized=no; best YouTube-search hit 10 views; not popular-checked | yt:things women over 60 should stop wearing |
| Classic style after 60 | UCIZm3YxEe3pP5JBPoeuc6qw | Light check: NexLev batch avg 752 views/video, faceless=F, monetized=no; best YouTube-search hit 0 views; not popular-checked | yt-channel:fashion over 60 |
| Stylish Over 60 Plus | UCIb0bKXdytbd4tnUEaODCTw | Light check: NexLev batch avg 1291 views/video, faceless=F, monetized=no; best YouTube-search hit 88 views; not popular-checked | yt:things women over 60 should stop wearing |
| Fashion ideas | UCIhYhh3HSKWGp8LTWlpba9Q | 6,750 subs, created 2023; best indexed long-form 16K (15 indexed; light check) | yt-channel:fashion over 50 |
| Ageless Refinement | UCIlbLUTwky_SYOUiOEaKyUQ | Light check: NexLev batch avg 520 views/video, faceless=F, monetized=no; best YouTube-search hit 204 views; not popular-checked | yt:shoes that make women over 60 look younger |
| The Grace Edit | UCJkjoFGgru77AimLwCqn4gQ | Light check: NexLev batch avg 528 views/video, faceless=T, monetized=no; best YouTube-search hit 389 views; not popular-checked | yt:jewelry mistakes women over 60 |
| Fashion Style Over 60 | UCKkmMy0OeDRaV6zitxu2U5w | Light check: NexLev batch avg 35 views/video, faceless=F, monetized=no; best YouTube-search hit 0 views; not popular-checked | yt-channel:fashion over 60 |
| Jo - Shines Bright | UCKtShAef5sNw6jLdiGylCgA | 4,050 subs, created 2025-03; batch avg 3,178 views/video; 100K video not seen (light check, popular sort not called) | yt:over 50 try on haul outfits midlife |
| Soft Chic 60+ | UCMF7Kl9MuntN-SbpmmWePtg | Light check: NexLev batch avg 2602 views/video, faceless=F, monetized=yes; best YouTube-search hit 1340 views; not popular-checked | yt:jewelry mistakes women over 60 |
| Traci Jeske | UCMPT-x9ElzrwmMtC9aeO9jg | Light check: NexLev batch avg 492 views/video, faceless=F, monetized=no; best YouTube-search hit 0 views; not popular-checked | yt:how to look expensive over 50 |
| Timeless Melanin | UCOeAfRoTrbgL3zcNEBtqV7w | Light check: NexLev batch avg 714 views/video, faceless=F, monetized=no; best YouTube-search hit 61 views; not popular-checked | yt:frumpy over 50 how to stop looking frumpy |
| Grace After 60 | UCSaXBU4cwbCJ_7ZKd5xLp0w | Light check: NexLev batch avg 777 views/video, faceless=F, monetized=no; best YouTube-search hit 191 views; not popular-checked | yt:things women over 60 should stop wearing |
| Elegant At 60 | UCUtEh9xGbLY_AMw7aduu8Lg | Light check: NexLev batch avg 254 views/video, faceless=F, monetized=no; best YouTube-search hit 90 views; not popular-checked | yt:shoes that make women over 60 look younger |
| Fabulous After 50 | UCVWezJzRk7Z-6_J5h67Sijg | Light check: NexLev batch avg 791 views/video, faceless=F, monetized=no; best YouTube-search hit 45 views; not popular-checked | yt:old money style women over 60 |
| Ada Solly Styling | UCWxmH_YX43dNwiLdloY_gUA | Light check: NexLev batch avg 1461 views/video, faceless=F, monetized=yes; best YouTube-search hit 2087 views; not popular-checked | yt:frumpy over 50 how to stop looking frumpy |
| After 60 wardrobe | UCYTDB4vbsivPBM5XuWr_sOA | Light check: NexLev batch avg 100 views/video, faceless=T, monetized=no; best YouTube-search hit 175 views; not popular-checked | yt:jewelry mistakes women over 60 |
| Melanin Fashion Secrets | UCZGxoWm0-0UiesAPQarb01Q | Light check: NexLev batch avg 271 views/video, faceless=F, monetized=no; best YouTube-search hit 413 views; not popular-checked | yt:jewelry mistakes women over 60 |
| Ageless Elegance | UC_6p4XX4pDD1bk9XxKcjdOQ | Light check: NexLev batch avg 1721 views/video, faceless=T, monetized=yes; best YouTube-search hit 4349 views; not popular-checked | yt:style over 60 outfits that make you look older |
| Ageless Elegance (bucIT) | UCbucIT5zNlg6netqi72Sj7g | Light check: NexLev batch avg 470 views/video, faceless=T, monetized=no; best YouTube-search hit 41 views; not popular-checked | yt:style mistakes over 60 women (medium) |
| Ageless elegance (dN7) | UCdeN7QLLQWyqECN3YvwiIJA | Light check: NexLev batch avg 1565 views/video, faceless=F, monetized=no; best YouTube-search hit 563 views; not popular-checked | yt:style mistakes over 60 women (medium) |
| Honestly Plus Size | UCeK0lb8TvVj_3ZiqExVJiHA | Light check: NexLev batch avg 2973 views/video, faceless=F, monetized=no; best YouTube-search hit 960 views; not popular-checked | yt:over 50 try on haul outfits midlife |
| ziliottodesign | UCeR3studWUHzv8YpKQ28BTg | Light check: NexLev batch avg 736 views/video, faceless=F, monetized=yes; best YouTube-search hit 4660 views; not popular-checked | yt:fashion over 50 capsule wardrobe stylist |
| Graceful Glow Fashion | UCfSnn7dl4uf_dJk79gZo3vA | Light check: NexLev batch avg 1279 views/video, faceless=T, monetized=no; best YouTube-search hit 218 views; not popular-checked | yt:shoes that make women over 60 look younger |
| Golden Age Fashion | UCfkD2j55k90xhXk21In0LgQ | Light check: NexLev batch avg 1636 views/video, faceless=T, monetized=no; best YouTube-search hit 1334 views; not popular-checked | yt:things women over 60 should stop wearing |
| Timeless Glow Club | UCg9Xo514G1GiNlnMyWMTN1A | Light check: NexLev batch avg 413 views/video, faceless=F, monetized=no; best YouTube-search hit 1145 views; not popular-checked | yt:jewelry mistakes women over 60 |
| Style Aura | UCiMRoND7j58HOp1fUNWBzHQ | Light check: NexLev batch avg 1234 views/video, faceless=T, monetized=no; best YouTube-search hit 89 views; not popular-checked | yt:frumpy over 50 how to stop looking frumpy |
| Fashion Over 60 (Mature Muse) | UCk5XnyMPvVreVHwzDa8U8KQ | Light check: NexLev batch avg 1187 views/video, faceless=F, monetized=no; best YouTube-search hit 0 views; not popular-checked | yt-channel:fashion over 60 |
| Ageless60 | UCkKACvzhTRwD7X-DpIosk3Q | Light check: NexLev batch avg 423 views/video, faceless=F, monetized=no; best YouTube-search hit 0 views; not popular-checked | yt-channel:fashion over 60 |
| Timeless Style After 60 | UCl50lEo8OKMH0ZRfEmzn_YA | Light check: NexLev batch avg 796 views/video, faceless=F, monetized=no; best YouTube-search hit 0 views; not popular-checked | yt-channel:fashion over 60 |
| Wise Women Over 60 | UCmuyxmX1GbuYAgUfAgMcApw | Light check: NexLev batch avg 518 views/video, faceless=T, monetized=no; best YouTube-search hit 403 views; not popular-checked | yt:old money style women over 60 |
| Timeless Elegant Fashion | UCnr4FcEntzBnqKfEC8anE-g | Light check: NexLev batch avg 397 views/video, faceless=F, monetized=no; best YouTube-search hit 1238 views; not popular-checked | yt:things women over 60 should stop wearing |
| Fashion over 60 (o2RN) | UCo2RNWVZHJBZmPouDxcBllQ | Light check: NexLev batch avg 288 views/video, faceless=F, monetized=no; best YouTube-search hit 0 views; not popular-checked | yt-channel:fashion over 60 |
| Historias de Adobe | UCr44MLEXDNiCjnxgseipnGg | Not a style channel (NexLev category stories). Light check: NexLev batch avg 4562 views/video, faceless=T, monetized=no; best YouTube-search hit 276 views; not popular-checked | yt:jewelry mistakes women over 60 |
| Modern Muse 60Plus | UCri-oeaEQTX9X9MhKdIYBew | Light check: NexLev batch avg 1778 views/video, faceless=F, monetized=no; best YouTube-search hit 623 views; not popular-checked | yt:shoes that make women over 60 look younger |
| Whispers Fashion & Styles | UCsLv1bB6G20BpVt4P5_aLmQ | Not a style channel (NexLev category stories). Light check: NexLev batch avg 2035 views/video, faceless=T, monetized=yes; best YouTube-search hit 183 views; not popular-checked | yt:how to look expensive over 50 |
| Ageless Chic | UCwAVQFqwPHBoTbzgxJv0Ymw | Light check: NexLev batch avg 344 views/video, faceless=T, monetized=no; best YouTube-search hit 1148 views; not popular-checked | yt:old money style women over 60 |
| Ageless 360 | UCwpuNriBe5e7TdxMu5y-IrQ | Light check: NexLev batch avg 900 views/video, faceless=T, monetized=no; best YouTube-search hit 110 views; not popular-checked | yt:jewelry mistakes women over 60 |
| Simply Stylish Over 60 | UCx09KKEp9ecol5Qf9cqOKaA | Light check: NexLev batch avg 720 views/video, faceless=T, monetized=no; best YouTube-search hit 0 views; not popular-checked | yt-channel:fashion over 60 |
| Stylish Seniors | UCy1ypSyi_qISk2vpNHdtWHQ | Light check: NexLev batch avg 1297 views/video, faceless=T, monetized=yes; best YouTube-search hit 2023 views; not popular-checked | yt:style mistakes over 60 women (medium) |
| BCsells - Casual Over 60 | UCykV8ufox96KsunV-aSLmqA | 8,350 subs; best indexed long-form since 2022 10,454 views (NexLev index covers 27 of 265 videos; light check) | yt-channel:fashion over 60 |
| Melanin Elegance | UCzHKOwDo2m7ydjO2Mc7Zcsw | Light check: NexLev batch avg 71 views/video, faceless=T, monetized=no; best YouTube-search hit 82 views; not popular-checked | yt:shoes that make women over 60 look younger |
| Lily styles 50 plus | UCGuY6GOg3Zt3q8jQ0wk37eg | Light check: NexLev batch avg 1836 views/video, faceless=F, monetized=no; best YouTube-search hit 7876 views; not popular-checked | yt:over 50 try on haul outfits midlife |
| Michelle Shelly / Fashion over 60 | UCBdrqYtmYxQh0L1HAZZBUGA | Light check: NexLev batch avg 1897 views/video, faceless=F, monetized=no; best YouTube-search hit 0 views; not popular-checked | yt-channel:fashion over 60 |
| Clara Kensington: Golden Aura Fashion | UCEtAs4Bse3dJN5M8VoQKOQw | Light check: NexLev batch avg 2582 views/video, faceless=F, monetized=no; best YouTube-search hit 17949 views; not popular-checked | yt:how to look expensive over 50 |
| All Fashion Milano | UCOSXUqY20f8iJtY1OYj19Rg | Broad: Milan street-style compilations (father-son team); About not age-specific; NexLev weekly call limit reached before its videos could be checked | similar-channels / yt search |
| Style & Sophisticate | UCkgXXs_Tt5BeT63vedZLunQ | Audience age not shown (About: modern women who value sophistication); 19.7K subs, faceless, NexLev top country Italy; NexLev weekly call limit reached before its videos could be checked | similar-channels / yt search |
| Adore Your Wardrobe | UCiCk9YOdjY8zZMUvMCGurCQ | Broad: wardrobe formulas, About not age-specific (52.4K subs); NexLev weekly call limit reached before its videos could be checked | similar-channels / yt search |
| Lux Gray | UCkhNFDBRUU8K82ZAosvHFmA | Audience not verifiable: empty About, faceless, Kenya, 40.2K subs; NexLev weekly call limit reached before its videos could be checked | similar-channels / yt search |
| Im just me - Marleen | UCGYx0XACuSPTTR8HUj3tZsg | Plus-size apple-shape fashion; age focus not shown in About (49.1K subs; 584K tummy video); possible fit, not verified | similar-channels / yt search |
| The Style Insider | UCcjVGHwHYVOkuvNEX2UH11Q | Broad (NZ ex-magazine editor, 291K subs); age focus not shown in About; NexLev weekly call limit reached before its videos could be checked | similar-channels / yt search |
| SuppleChicTV | UCjnim4l9ObyJFO6Cn6mJUjw | No About data (limit reached); its seen 2.23M tummy video is ~5 years old (before 2022); broad | similar-channels / yt search |
| Style With Serena | UCpsZd3lQayBjdFHEu2rPbvA | Broad (234K subs, women who refuse to disappear); age not stated; seen winner is a travel capsule; NexLev weekly call limit reached before its videos could be checked | similar-channels / yt search |
| Madre | UCyJBo3ddTNTbLmXuOpWRtNg | Luxury-buyer persona (Isabelle Vargas), 46.7K subs; audience age not stated in About; NexLev weekly call limit reached before its videos could be checked | similar-channels / yt search |
| Senior Wellness Elevate | UCCRyYSezD6xrHlD3OhD0XaA | Not verified: 2220 subs (<10K), 516828 total views, created 2025-09-28; best video seen 169; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| TIMELESS PEARL | UCBFU2lgwyTr1dr2XDGusa4A | Not verified: 886 subs (<10K), 224216 total views, created 2026-06-20; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| The Chic Over 50 | UCi0HmKGNSBe5vS6bzt63D-w | Not verified: 989 subs (<10K), 89903 total views, created 2026-08-21; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Glow At Any Age | UCq7vy7QW7_S53Mb9CkfFhow | Not verified: 9300 subs (<10K), 755893 total views, created 2025-12-29; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Fashion For Seniors | UC-ONxF2qMV73jqEsyrCQh7w | Not verified: 6930 subs (<10K), 424023 total views, created 2025-08-30; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| French Fashion | UCCDxeYvF9t_XkLIawoSlmXQ | Not verified: 4860 subs (<10K), 565205 total views, created 2026-10-10; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Glow at Every Age | UCHMR9dxvz4_jH2fcnr49eGQ | Not verified: 4160 subs (<10K), 293084 total views, created 2026-02-02; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Melanin & Style After 60 | UC11SeASFFKw-2vQ22RSFcMA | Not verified: 1860 subs (<10K), 77101 total views, created 2026-04-13; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Trendy Outfit Vibes | UCnJHurJdw1MJLvpIKsK6cIA | Not verified: 1730 subs (<10K), 3630977 total views, created 2025-09-09; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Chic Fashion Over 50 | UC4BrfgCf7jLS53P0WIULysw | Not verified: 906 subs (<10K), 130830 total views, created 2024-05-22; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Style & Elegance | UCaGVgtIAmJJCCSN8HTL1TSw | Not verified: 206 subs (<10K), 97513 total views, created 2026-07-28; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Style After 50 | UCPhMszWwUHDpAcrCdVhMJow | Not verified: 132 subs (<10K), 93997 total views, created 2026-09-09; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Style & Grace Over 60 | UCSc6E36Yn54tJS033JqHKbg | Not verified: 733 subs (<10K), 125802 total views, created 2026-09-10; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Crowned in Elegance | UC0GOZj66XJyl8fb3Zk9K5_g | Not verified: 3230 subs (<10K), 149142 total views, created 2025-05-28; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Chic60Plus | UCDwKxV6wu25sohB-Rsx-raQ | Not verified: 672 subs (<10K), 54873 total views, created 2026-08-21; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Ageless Beauty Queen | UCdXtokc69BLX7vikPsauHRQ | Not verified: 1350 subs (<10K), 80818 total views, created 2026-08-03; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Chic Over 60 | UCkbGQ6Snk83E-dKt9aG_vVw | Not verified: 1380 subs (<10K), 213408 total views, created 2026-06-29; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Chic After 60 |
| Refined After 60 | UCHnphEBp4q2GGfpQRaT5Byw | Not verified: 3650 subs (<10K), 293961 total views, created 2026-04-25; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Shopping On Champagne |
| Susan's Sweet Life | UCq3KsYbDXujenB6oEoQqiNw | Not verified: 7880 subs (<10K), 1853687 total views, created 2012-08-28; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Shopping On Champagne |
| Hey! It's Heather | UCP0wo4nRpEzT6CB-qfjZWTQ | Not verified: 6690 subs (<10K), 1465292 total views, created 2018-10-16; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Shopping On Champagne |
| Timeless Wisdom Path | UCU5pdr0Y3PZyOFltpetrxJQ | Not verified: 1910 subs (<10K), 372427 total views, created 2025-09-21; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Shopping On Champagne |
| Fashion in Maturity | UC4wZo_yW_lqgDPEs-TbDzog | Not verified: 8460 subs (<10K), 717150 total views, created 2024-10-16; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Vivian Sinclair |
| Style After 60 | UCbYE70VeEYdG22asS8H_hDw | Not verified: 818 subs (<10K), 52822 total views, created 2026-01-31; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Vivian Sinclair |
| Elegant  After 60 | UCOpu6m8l0hf4qoViWdWip1Q | Not verified: 2170 subs (<10K), 254098 total views, created 2026-05-24; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Vivian Sinclair |
| Melanin Majesty | UC6BQai1lazBSCRlv6AAho1Q | Not verified: 9730 subs (<10K), 490309 total views, created 2025-02-03; best video seen 64271; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Vivian Sinclair |
| Gracefully Dressed | UCSL-QkE2wBO7cmwY1V7jrMA | Not verified: 1050 subs (<10K), 193788 total views, created 2024-09-21; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Vivian Sinclair |
| Graceful Over 60 | UCvy7fElgsQRHa1wFqc-kacg | Not verified: 719 subs (<10K), 117942 total views, created 2010-05-07; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Vivian Sinclair |
| Bloom After 60 | UCIV9PRIncsJkwkfs_OZ_2Dw | Not verified: 1090 subs (<10K), 115931 total views, created 2025-06-24; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Vivian Sinclair |
| Gigi Your Stylist | UCamuyqN1rtMEeWsfQUj6hbA | Not verified: 325 subs (<10K), 219594 total views, created 2025-06-24; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Vivian Sinclair |
| Style Over 40 | UCORx4MlralwR0kcph1aFZ7w | Not verified: 570 subs (<10K), 296619 total views, created 2025-06-10; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:MM Personal Styling |
| Feminine Over 50 With Mia | UCblEH1XOSZ3ep95FHUNjPhw | Not verified: 4100 subs (<10K), 4011058 total views, created 2026-05-18; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Marie-Anne Lecoeur |
| BIG WOW | UCAsvbBGceKl1Y-ytJW--hFg | Not verified: 222 subs (<10K), 98147 total views, created 2026-09-22; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Marie-Anne Lecoeur |
| Minimalism Over 50 | UCSYcXMinnxP_5uTS8jpSNyA | Not verified: 4540 subs (<10K), 462363 total views, created 2024-10-02; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Marie-Anne Lecoeur |
| Only Fame | UCS6xlNX8RUefhhxQy4xjOuw | Not verified: 8480 subs (<10K), 7433617 total views, created 2025-10-19; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:TRENDS SPOTTED |
| Refined After 50 | UCKbzlKtqb5KlitumXEAn6aQ | Not verified: 2130 subs (<10K), 123661 total views, created 2026-05-23; best video seen 0; no 50K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Elegance At 60 |
| Golden Ebony lifestyle | UCMNsf3dJlJdd0mAhxJIIc2g | Not verified: 1970 subs (<10K), 121301 total views, created 2023-12-03; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Elegance At 60 |
| Wraparound Plus | UCRcB5ORiLfPAAtol8QZMgng | Not verified: 5900 subs (<10K), 408622 total views, created 2023-05-28; best video seen 0; no 100K+ video confirmed (NexLev weekly call limit reached before popular check) | similar:Elegance At 60 |
| Ageless Elegance 60+ | UC-3WS-nyfXFoM3CGTTO0-hQ | Light check: NexLev batch avg 199 views/video; not popular-checked | yt search |
| Style beyond 60 | UC13_ide7vSj8PL8XEoSJ8ew | Light check: NexLev batch avg 245 views/video; not popular-checked | yt search |
| Glow After 60 | UC2u8sjLECpdV5IWTZrheusA | Light check: NexLev batch avg 7074 views/video; not popular-checked (monetized; would need popular check - NexLev limit reached) | yt search |
| Aging With Elegance | UC5THY_nQ7U8ETbW_nCqk0Jg | Light check: NexLev batch avg 1172 views/video; not popular-checked | yt search |
| Evergreen Styles | UC8JUKcfAoWlrCnqYDY7jAqQ | Light check: NexLev batch avg 1065 views/video; not popular-checked | yt search |
| Pretty Over 60 | UCCGlbWAmCIBJ5NV4WlZnqGw | Light check: NexLev batch avg 29 views/video; not popular-checked | yt search |
| Daily Black Glow | UCEMDkSpIbSDiTwcErwT9sJQ | Light check: NexLev batch avg 232 views/video; not popular-checked | yt search |

Also pending: the 27 rows marked `unclear` and the 46 faceless rows have no check_faceless confirmation beyond batch metrics; the 30 rows added after the limit need popular-sort top-3 videos and exact last-upload and 90-day counts.

