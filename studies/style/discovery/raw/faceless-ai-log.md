# Discovery log: faceless and AI channels (lane D)

Helper: faceless-ai discovery helper. Date: 2026-10-28. Tools: NexLev MCP only (no web search). Output: `faceless-ai.csv` (same folder).

## Result in one paragraph

70 channels kept (rows in the CSV). 70 screened out with NexLev channel data (reasons below), plus 89 screened out from similar-channel listing stats or their own descriptions. 45 found but NOT screened because NexLev's weekly call limit (2000 calls, shared account) ran out mid-run; they are listed in their own section so the main session can pick them up after the reset (2026-10-31 06:56 UTC). The two operator channels (Scarlet Sterling UCTMwV-uy20eaRwFfc4Sx13g and Diane de Chambray UC2z5yffdjwr3xpr-iDp9Yvw) came up in their own similar-channel results and are not listed anywhere as candidates.

## Method

- Discovery: NexLev semantic niche finder (faceless filter, AI filter and unfiltered), faceless outlier-video search, viral small-channel search, latest discovered faceless niches, YouTube search on the operator's own titles, and similar-channels (level 3) on both operator channels.
- Screening per candidate:
  - **Live outlier scan** (`youtube_channel_outliers`, up to 100-500 videos, threshold tuned so the top videos come back). Gives channel about data (subs, total views, video count, joined date, country, handle, links) plus the best videos ranked by views/average, which is view order.
  - **Faceless check** (`check_faceless_channel`).
  - For channels NexLev already holds, the stored **niche-finder record** (editing style, AI flag, uploads per week, revenue, RPM, recent popular videos).
- Keep rule applied as written in the brief:
  - uploaded in the last 12 months, and
  - 10K+ subscribers or a 100K+ video since 2022.
  - Faceless/AI channels under a year old are kept with any 50K+ video.
- `type` rules:
  - NexLev isAiChannel true while check_faceless sees a face → `ai_avatar` (always when there is a named persona or a book).
  - NexLev editing style ai_images / stock_footage_voiceover, or a faceless check of true → `faceless_narrated`.
  - Conflicting signals → `unclear`.
  - `type_basis` names the signal and says `reading` where it is my interpretation.

### Deviations from the requested method (and why)

- **Top 3 videos.** Taken from the live outlier scan instead of the "popular" sort of `youtube_channel_videos`. The popular listing cost ~20K tokens per channel. The outlier scan returns the same top videos in view order for far less. Where the scan returned fewer than three videos above the threshold, the remaining top-video cells are blank.
- **Exact view counts.** The tools return views in rounded form for most channels (e.g. 536000 = "536K"). Values are stored as given.
- **Dates are approximate.** NexLev returns relative dates ("1 year ago", "3 months ago"), converted to calendar dates counted back from 2026-10-28. Many videos therefore show the same day-of-month (e.g. 2025-10-28 = "1 year ago"). Treat dates as month-level at best.
- **uploads_last_90d.** Where a number is marked "(NexLev index count)", it is a count of indexed uploads. Otherwise it is NexLev's uploads-per-week figure × 13, marked "~". Blank means neither was available; the newest-videos listing was too costly to pull per channel. NexLev's per-week figure lags: a few channels show ~0 while their last upload is recent.
- **last_upload.** Comes from the NexLev record, the similar-channel listing, or the newest top video (written as "on or after ...") when nothing better was available.
- **Not done (NexLev limit):**
  - similar-channel searches on 4-6 of the strongest faceless/AI channels;
  - `search_youtube_suggested_videos` on the operator's videos;
  - the full screen of the remaining finds.
- **Seven channels were screened from their stored NexLev niche-finder record only,** without a live outlier scan or faceless check: Emiko Sato, Brand Smart Buy, Sé Tu Mejor Versión, Elegance At 60, Style over 60, Mature Vogue and BeautybyJaiy. Their top videos come from NexLev's stored video list, which may miss older winners. Their notes say so.
- **Real on-camera channels were not given CSV rows.** They came up in the similar-channel results and are out of this lane (fashion, hair and French+makeup lanes cover them). They are listed below so they are not lost.

## Searches run

Counts are new candidates (channels with a women-50+ angle not already in the pool) unless noted.

### NexLev niche finder (`search_niche_finder_channels`, limit 50, language en unless noted)

| # | Query | Filters | Results / new candidates |
|---|---|---|---|
| 1 | fashion tips for women over 60 narrated | isFaceless=true | 50 results / 50 new (first query; includes some off-topic) |
| 2 | style advice older women AI presenter | isFaceless=true | 6 new |
| 3 | hairstyles for women over 60 | isFaceless=true | 7 new |
| 4 | look younger after 60 | isFaceless=true | 14 new |
| 5 | what women over 70 should wear | isFaceless=true | 4 new |
| 6 | French women over 60 style | isFaceless=true | 4 new |
| 7 | elegant women over 50 | isFaceless=true | 3 new |
| 8 | old money style older women | isFaceless=true | 22 results, mostly off-topic (history/old-money) |
| 9 | makeup over 60 | isFaceless=true | 6 new |
| 10 | skincare for mature skin women over 60 | isFaceless=true | 10 new |
| 11 | fashion tips for women over 60 narrated (page 2) | isFaceless=true, offset 50 | 22 new |
| 12 | gray silver hair transition women over 50 | isFaceless=true | 0 new |
| 13 | style mistakes that age you after 60 what not to wear | isFaceless=true | 0 new |
| 14 | fashion and hair for women over 60 | isAiChannel=true | 4 new |
| 15 | fashion tips for women over 60 | no faceless filter | 3 new |
| 16 | jewelry glasses and accessories for women over 60 | isFaceless=true | 0 new |
| 17 | Parisian chic French style secrets | isFaceless=true | 35 results, mostly off-topic (French nostalgia, cooking) |
| 18 | street style outfit ideas lookbook women over 50 60 70 | isFaceless=true | 0 new |
| 19 | short haircuts thin hair older women look younger | no faceless filter | 5 new |
| 20 | `*` (filter browse) | categoryId 81 (beauty), en, lastUploadAfter 2025-10-28, sortBy subscribers | 65 results, 61 general/young beauty; dropped as off-topic |

### NexLev faceless outlier videos (`faceless_outliers_videos`, minUploadDate 2025-06-01, limit 50)

| Query | New candidates |
|---|---|
| fashion and style tips for women over 60 | 24 |
| haircuts and hairstyles that make women over 60 look younger | 4 |
| French women over 60 never wear these, Parisian style after 50 | 8 |
| makeup and skincare mistakes for mature women over 60 | 14 |
| jewelry, glasses, shoes and jeans that make older women look expensive | 7 |
| category browse: beauty for elderly women (english, long-form) | 14 videos, 0 new |
| category browse: beauty for middle age women | 11 videos, 0 relevant new |

### NexLev viral videos from small channels (`search_viral_videos_small_channels`, last 90 days)

| Query | Filters | Result |
|---|---|---|
| over 60 | duration 300s+ | 8 videos, 0 new in lane |
| women over 50 | - | 0 |
| after 60 | - | 15 videos, health only, 0 new |
| older women | - | 0 |
| French | - | 3 videos, 0 new |

### NexLev latest discovered faceless niches (`latest_discovered_faceless_niches`)

| Call | Result |
|---|---|
| limit 1000 | in lane: Skin Truth Index (279 subs, ~30 days old, best 49K: screened out, under 50K) and Timeless Style Living (kept); Life After 70 and Royal Dress Code off-lane |
| limit 1000, outlierScore 1 | 242 overlap with the first call; only Emiko Sato new in lane |

### YouTube search via NexLev (`youtube_search`, type video) on the operator's own titles

| Query | New candidates |
|---|---|
| 5 Necklaces That Make Women Over 60 Look EXPENSIVE | 10 (incl. ELEGANCE AFTER 60., Stylish After 60, Diane Hartwell, The Golden Years Archive, Classy Academy); also Val Rose Style Over 60, channel ID not returned (N/A) |
| The Jeans Mistake Making Women Over 60 Look OLDER | 12 |
| Wealthy Women Over 60 NEVER Wear These Glasses | 7 |
| Why French Women Over 60 NEVER Look Frumpy | 5 (incl. real channels Marie-Anne Lecoeur, Aliceinparis, Sandra Sallin) |
| 5 French Haircuts That Flatter ANY Face Shape After 60 | 10 (incl. Elder Insights, Justin Hickox) |
| women over 60 look younger style tips (upload date: month, sort: views) | 10 |

Observation, recorded as data: two small channels publish titles identical or near-identical to the operator's:

- Stylish After 60 (UC8rf2u19rY2EIx0-2vvvh5w, 22 views): copied the necklaces title two days after it.
- Val Rose Style Over 60: channel ID not returned.

### Similar channels (`get_similar_channels`, level 3, async)

| Seed | Result |
|---|---|
| Scarlet Sterling (UCTMwV-uy20eaRwFfc4Sx13g) | 125 channels |
| Diane de Chambray (UC2z5yffdjwr3xpr-iDp9Yvw) | 67 channels |
| Union | 166 distinct, of which ~111 were not already in the pool. Each one is placed in a section below. |

The listing returned Scarlet's channel as "Scarlet Starling", joined 2026-09-15, 531 subs.

## Failures

- **NexLev weekly limit.** After about 2000 calls in the 7-day window (shared across all tools and, as far as I can tell, all helpers on this account), `youtube_channel_outliers` for Ageless Beauty Queen (UCdXtokc69BLX7vikPsauHRQ) returned WEEKLY LIMIT EXCEEDED. The limit resets 2026-10-31 06:56 UTC. I did not retry, because a retry would fail the same way. Every NexLev tool is blocked until the reset, for the other discovery helpers too.
- **Oversized results.** The similar-channel results (287K and 155K characters) and several niche-finder results went over the size limit. They were read from the saved result files with python. No data was lost.
- **Stale index.** `search_videos` (NexLev video index) had empty or stale views for many small channels (e.g. Journey After 60 index top 4.9K vs about 6.5K seen live). It was dropped as a source for top videos.
- **Missing channel ID.** `youtube_search` returned "N/A" as the channel ID for Val Rose Style Over 60, so it could not be screened.

## Screened out (with NexLev channel data)

| Channel | Channel ID | Reason |
|---|---|---|
| Novokumar Ghosh | UC7lD1HImfYEbMZSAih1ibkQ | 280 subs, 42681 total views: no video can reach 50K (NexLev stats) |
| The Mirror Edit | UCLTXZUZ7Sme8zekDHihbd2g | 393 subs, 48379 total views: no video can reach 50K (NexLev stats) |
| Evelyn Hart | UC35beahevoTdl2bGIBW7S3A | 235 subs, 30893 total views: no video can reach 50K (NexLev stats) |
| Jenny Style Audit | UCpt2DV6j33Sf8c2F5VRDW-w | 212 subs, 20484 total views: no video can reach 50K (NexLev stats) |
| Ageless Style Icons | UC4iMSCYpbu6kG8Lia46j77Q | no upload in last 12 months (last 2025-10-26, NexLev) |
| Eleanor Winslow | UCbwn6l34lEWhOIAjmPe4jzA | 115 subs, 18083 total views: no video can reach 50K (NexLev stats) |
| HouseOfElegance | UCa9KQyun6e1uB6iJl2fCgYg | no upload in last 12 months (last 2025-10-26, NexLev) |
| Ashley Grant | UCgXvIOk7meBAmy-dxQ4M2Dg | 234 subs, 33648 total views: no video can reach 50K (NexLev stats) |
| Elegant Academy | UCKW9TVF2cM1CbJoGo4MjstQ | no upload in last 12 months (last 2025-10-26, NexLev) |
| Diana Cole | UCajJYEIjY1hHNCKGGlF9e0A | 140 subs, 18075 total views: no video can reach 50K (NexLev stats) |
| Ageless Queens | UCgC-uVXN5nb6jw-uvNDTyzA | no upload in last 12 months (last 2025-10-26, NexLev) |
| dangcongthan dangcobgthan | UCQXAU70bWa4BXzxbaHbqZhA | 462 subs, 11953 total views: no video can reach 50K (NexLev stats) |
| Vien Tran | UCbhdAaeCUpADCaAKvK9Jc-g | 705 subs, 69715 total views, channel over 1 year old: no video can reach 100K |
| Aging Smarter | UCu67IiiiS2m0ibjfIV8sXww | 295 subs, 15742 total views: no video can reach 50K (NexLev stats) |
| Elegant Fashion And Style Over 60 | UC8rJqI3YGdgUcZVHILLSqvw | no upload in last 12 months (last 2024-10-26, NexLev) |
| Refined Style Studio | UCMei1XtpepC0UBth8F9Hl2w | 434 subs, 47223 total views: no video can reach 50K (NexLev stats) |
| Journey After 60 | UCBnPTmijWKU8xbIv-jMArkw | 1.76K subs (index), top video seen ~6.5K views (YouTube search); index top 4.9K: no qualifying video |
| Style After 60 | UCCac3e7jjjwD4SZdprJRmxA | faceless/AI, created 2026-03-24 (under 1 year): best video 38K (5 Makeup MISTAKES Women Over 60 Do), under the 50K bar; 2.49K subs |
| Elegant Sein | UCZzfcxL6u0LZGHOZbS9MkTg | not English: German channel (NexLev lang de, former handle NatürlichimGleichgewicht-de); top video is a German psychology video (188K); one English style video at 92K |
| Fashion Tips | UCDdtmklCWlTwoklUCE7XQPw | broad general outfit-ideas channel (white shirt, boho, beige pants); mature-women titles are not a large share of its winners |
| Elegance in Every Detail | UCBaMaBRu4XwCHalwR50bLfA | broad trend channel (sneaker/jean trends, spring essentials); mature-women titles not a large share of winners |
| THEALOELIXIR | UCNYHf0DPH-piQ9IVSjihNog | broad skincare-brand rankings (The Ordinary ranked, luxury moisturizers); best video in NexLev recent list 47K, under the 50K bar for a channel under 1 year (created 2026-07-03) |
| Beauté de l’Âge d’Or | UCqRgAobmV_WzcZIFERKiTsA | 1950s nostalgia (forgotten hair tips, hygiene rules, kitchen habits), not over-50 style; French-labelled channel |
| ICONIC - WOMEN OVER 50 | UCXfUl8O2X6OKVvm4TvKlJug | lookbook/biography clips of named attractive older models (MRS ANDI NICOLE, CURIOUS CARLY); not style advice, audience unclear |
| Everyday Fashion | UCUBTtXWynzBLF5TeY1QtieQ | 3-minute lookbook clips (Natural & Attractive Older Women Over 50 #78, #89, #93); no long-form 5:00+ videos seen; audience unclear |
| Mode und Stil 50+ | UCSarPoUqrV5fNvufTXgTvdg | not English: mostly German titles (13 Modefehler, die kleine Frauen ueber 50 vermeiden) with some English |
| Stille Eleganz | UCBjbbT1ijYTEszeqyVvUotA | not English: German titles (Diese 7 Herbstjacken machen ab 60 alt!) |
| Élégance Après 60 | UCfToK4QQsiisVFwmpUmZbYA | not English: mostly French titles (ARRETEZ! Ces 7 Erreurs...); top 202K |
| Bienvenue sur Élégance 60+ | UCFGU_g0-AwFEu_XHS1kbhkQ | not English: mostly French titles (Erreurs de Bijoux Qui Vous Vieillissent) |
| Hana et toi | UCxio3MI6RSj9verf9Sf4-FQ | not English: mostly French titles (Melangez CECI a Votre Shampoing) |
| Senior Fashion Class | UCfqm-owzftN8K4KxeTF5trA | faceless/AI, created 2026-04-30: best video 41K (3 Trending Glasses... Women Over 60), under the 50K bar; 1.91K subs |
| Style After Sixty | UCTSYeyREkFQQYvtazAIeESQ | faceless/AI, created 2026-07-26: best video 23K (7 Pixie Cuts for Women Over 60...), under the 50K bar; 1.22K subs |
| Stilvoll ab 60 | UChWRWvHXc81-jrzofzHAjag | created 2026-07-26 (AI/faceless reading; German description, English titles): best video 44K (The Bob After 60...), under the 50K bar; 782 subs |
| Estilo Después de los 50 | UCLBgPjRjCOwvjRzs6bMCoJA | created 2026-05-13 (Turkey-registered, Spanish name, English titles): best video 47K (7 Jackets That Look Dated After 50), under the 50K bar; 252 subs |
| Shifted Mind Academy 50+ | UC1QQoJrY2q9lbMFAWHFSfFA | created 2025-11-22 (under 1 year): best video 31K and it is a 3-minute short-form clip; 192 subs, 12 videos |
| Outfits for Women's | UCyJbyl5UYAMg7c7V2IGBFqw | created 2026-09-18: best video 33K (Elegant & Stylish Outfits for Women Over 50), under the 50K bar; 408 subs |
| Mina's Lab | UCZzKg5asSfIvUVQklI3VOhQ | broad: royal/celebrity makeup and home tours (Diana, Kate, Jackie Kennedy); 1 of 7 top videos aimed at over-50 (111K). Repurposed 2007 channel, 7.1K subs |
| Style Legends | UCDmhYIY6igVaCVW7jv8PBRA | off-topic: fashion-icon history documentaries (3 videos, 839K total), not a women-over-50 channel |
| Graceful Style Guide | UC45XK1uXg45MkUwkl6DWLfw | off-topic: senior health and wisdom (1,068 videos, Elders Lantern), not style |
| Serena Aure | UC6Bwn2MhfwF7ok_XtMEN_kQ | broad: belly-fat and glow-up videos (947K, 475K), no over-50 framing; 17K subs, created 2026-02 |
| Luxe Audit | UC-VA2oyVDkysxNHAStMM3CA | broad: skincare brand audits with no age framing (top 461K); found via mature-skin outliers search |
| Luxe Branded | UCiIFcGXDNzcKJw-kmNCkUEA | broad: cosmetic brand investigations with no age framing (top 1.1M, 10 videos) |
| Her Style Audit | UCo6uFyf_KvnqA9X3PrnQquQ | broad: women's clothing brand audits with no age framing in winners (top 328K); 19.8K subs |
| Smart Fashion | UCYcmyDtGnrFi9gBP4Pixciw | broad: clothing brand audits with no age framing (top 273K); created 2026-05 |
| Fashion For Women Over 60 | UCDMv6pf3v7cXoG6N4HSx8ww | 26 subs, 9.9K total views, top video 311 views |
| The Grace Edit | UCJkjoFGgru77AimLwCqn4gQ | 215 subs, 27K total views, top 4.6K (persona Grace, gumroad ebook) |
| Classy Academy | UCJUn02MVnahA9My9-DUkTBQ | broad: general elegance channel (135K subs, top 1.2M) with no age framing in winners; 8-minute videos |
| Ageless Refinement | UCIlbLUTwky_SYOUiOEaKyUQ | 2.58K subs, 55K total views, top 2.8K |
| Evergreen Styles | UC8JUKcfAoWlrCnqYDY7jAqQ | 427 subs, 54K total, created 2025-07 (over a year), top 21K |
| Ageless elegance | UCdeN7QLLQWyqECN3YvwiIJA | 662 subs, 77K total, created 2026-06, top 22K (under the 50K bar) |
| Melanin at 50 | UCM7SbWU79ah7UtV6peq-Bmw | 74 subs, 5.7K total, top 1.2K |
| Ageless Beauty | UCuj5v6pVAUBuMqhexJbv5YQ | 366 subs, 26.6K total, top 8.7K |
| Timeless at Sixty | UCnaif8YKLzS8a0Jt92a484A | 1 subscriber, 39 views, created 2026-09 |
| Radiant After 60 | UCT0MCvJeQYk5pKCt4n0zuzg | 6.45K subs, 50K total, created 2025-07, top 12K (persona Clara Whitmore) |
| Fashion in Maturity | UC4wZo_yW_lqgDPEs-TbDzog | 8.46K subs, created 2024-10 (over a year), top 63K: under 10K subs and no 100K video |
| Golden After 60 | UCrrV68TQf2raW-t0_x7mMMg | 150 subs, 17K total, top 4.7K |
| Ebony Aura | UCM03KjKUiNG7fEih3NbReTg | 1.03K subs, created 2023-12 (over a year), top 35K |
| timeless queens | UC1j2faZgHoeQIf0YSMqEgRg | 107 subs, 8K total, top 2.5K |
| TIMELESS CHARM & STYLES | UC9H-C6uJVKCRfE4zslwoHGQ | 280 subs, 30K total, created 2023, top 19K |
| The Elegant Edition | UC1XeD4J11bJIu7cdPc-dnmA | broad: rich-mom / minimalist elegance channel (27.2K subs, top 278K) with no age framing in winners |
| Crowned in Elegance | UC0GOZj66XJyl8fb3Zk9K5_g | 3.24K subs, created 2025-05 (over a year), top 83K: under 10K subs and no 100K video |
| Timelessly Chic | UCXuSoiQm-E9jQEU7imOrxsA | 317 subs, 34K total, top 8.1K |
| Classic Fashion 60+ | UCsxP-G5n_1e03oiu8w4ihTg | 757 subs, 35K total, top 19K |
| Only Hairstyles | UCv41YRs8uNfTVCwlkUi9RHA | no qualifying video: 3.26K subs, created 2025-06 (over a year), top 64K; almost all videos are 3-minute hairstyle photo lookbooks (TR) |
| Éclat Melanin | UCdfQxG929RKxiWxppRDj0JA | French-language channel (NexLev lang fr, FR) with translated titles; best 28K, under the 50K bar |
| Aging Queens | UC0uabQ9Zs6bDpr1n-gqR3MQ | created 2025-10-14 (just over a year), best 67K, 3.3K subs; last upload ~2026-08-27 (NexLev record) |
| Beauty Mina | UCZBoYIhVz0NHI4b0J1q4TlA | registered 2019 (repurposed, Korean makeup persona Mina), best 81K: no 100K video and under 10K subs (NexLev record) |
| CougarFashion | UCmdXZnICr_pgtqwOgcAKYIQ | no long-form: 2-minute model lookbooks (top 1.6M at 2:03); audience framed over 40 (NexLev record) |
| The Elegance Society | UC82ZtUPn4PduSPadGzHpEiA | broad: color-combination videos with no age framing (132K at 3 months old, reused footage); NexLev record |
| Mind blowing Hair | UCX68HYZ3j7R1mgy1kV0GHVA | out of lane: real salon makeover footage (NexLev faceless false), left to the hair lane; 25.4K subs, top 854K |

## Screened out from listing stats or descriptions (similar-channel and search finds)

| Channel | Channel ID | Reason | Listing stats |
|---|---|---|---|
| Elegancka Kobieta | UCC6_5drFrCuH8tZ8Nq0Kkmg | not English; Polish | 4,880 subs, 888,742 total views, joined 2026-06-19, last upload 1 day ago, avg length 00:20:35 |
| Elegancia Magnética | UC_gPuaHhnXXm12hrs8H-rCA | not English; Spanish | 6,600 subs, 1,278,605 total views, joined 2024-10-22, last upload n/a, avg length 00:16:03 |
| Luce Como Reina | UCqUEjsLMkC1nnTo6g7jD5FA | not English; Spanish (2.6M views, created 2026-07) | 7,230 subs, 2,639,427 total views, joined 2026-07-18, last upload 2 days ago, avg length 00:16:14 |
| Donna Matura | UCLcnFdxIXNuLdAsEy8PRZuQ | not English; Italian name and IT registration, empty description (reading; not checked) | 3,990 subs, 909,762 total views, joined 2026-06-03, last upload 11 hours ago, avg length 00:20:26 |
| Stilvoll 60 Plus | UCBPV22GKhIfBwYTMWkskNGw | not English; German (created 2026-08, 877K views) | 3,440 subs, 876,517 total views, joined 2026-08-05, last upload 15 hours ago, avg length 00:14:59 |
| Phong Cách sống | UC3Vhm5ZOumYZJLkda6jH04g | not English; Vietnamese | 7,980 subs, 1,868,623 total views, joined 2026-02-09, last upload 12 hours ago, avg length 00:12:42 |
| 황혼지혜TV | UC29xC-EzaG5Ttasv5NS6r5g | not English; Korean; strong (72.5K subs, 31.9M views) but not English | 72,500 subs, 31,881,573 total views, joined 2025-05-02, last upload 3 days ago, avg length 00:23:15 |
| オシャレで人生が変わる〜大人スタイル | UC0TZz2u7wBbApHKd3WVgGlg | not English; Japanese stylist | 6,370 subs, 2,510,162 total views, joined 2016-03-01, last upload 1 hour ago, avg length 00:27:26 |
| Radiante & Natural | UCj2tiZOVwkLlqYDjueZ2RyA | not English; Spanish hair channel (12.2M views) | 8,530 subs, 12,155,078 total views, joined 2025-03-16, last upload 9 hours ago, avg length 00:15:45 |
| Eleganza-Stile Over 50 | UC591CBZ7NSvvJlwVnU3Jhjw | not English; Italian (21.1K subs) | 21,100 subs, 3,744,431 total views, joined 2025-01-01, last upload 5 days ago, avg length 00:14:34 |
| BlickPunkt | UCpeqZf4fMfKE6b5vYM4LpLw | not English; German psychology channel | 3,880 subs, 504,603 total views, joined 2026-01-05, last upload 5 hours ago, avg length 00:20:29 |
| Timeless Gentleman | UCrO1nbyCtTH-fIW7Z9Z20Lw | men's style, not a women-50+ channel | 4,930 subs, 1,033,976 total views, joined 2026-06-03, last upload 4 hours ago, avg length 00:12:16 |
| Prime Gentleman | UC5jz7ZwI-RVP2iBHWF9KHkg | men's style, not a women-50+ channel | 1,360 subs, 208,583 total views, joined 2026-06-15, last upload 7 hours ago, avg length 13:06 |
| Gentleman 40+ | UCvvn0thUkPz-Rm-thaKzgzw | men's style, not a women-50+ channel | 5,500 subs, 656,983 total views, joined 2021-01-15, last upload 2 weeks ago, avg length 00:16:35 |
| Dapper Dads | UCahyKEIYF9o2WsUzbFtytxQ | men's style, not a women-50+ channel | 23,100 subs, 3,251,358 total views, joined 2025-02-23, last upload 18 hours ago, avg length 00:17:58 |
| Classic Gent | UCFbEJORScJ2K2E_NjQVfBAA | men's style, not a women-50+ channel | 23,000 subs, 3,393,120 total views, joined 2024-04-24, last upload 16 hours ago, avg length 19:38 |
| Timeless Style 40+ | UC-TGG-M30FyF9qFjkGTOizw | men's style, not a women-50+ channel | 1,890 subs, 199,442 total views, joined 2025-09-30, last upload 6 days ago, avg length 00:13:13 |
| Gentleman Post | UC5vfB78wka0I_CAdHeql7Xw | men's style, not a women-50+ channel | 12,700 subs, 2,278,218 total views, joined 2025-07-07, last upload 8 hours ago, avg length 00:09:57 |
| Real Men Real Style | UCmRfQHc3U4fV1-i8Ry1HmtA | men's style, not a women-50+ channel | 3,720,000 subs, 536,812,092 total views, joined 2010-12-07, last upload 1 day ago, avg length 00:13:51 |
| Feynman Explore | UCL2MQGIZFv-OV0m-4DgP9Og | off-topic; science/psychology | 7,410 subs, 902,538 total views, joined 2026-06-21, last upload 1 hour ago, avg length 00:23:41 |
| Hamza Imtiaz | UCfRkzkhZR92odUNXa4PWNHg | off-topic; graphic designer | 3,770 subs, 325,577 total views, joined 2026-05-28, last upload 11 days ago, avg length 00:12:29 |
| Natalie Paterson | UCKKDzoxS74kkcxHtA_ByKOA | off-topic; home decor | 3,870 subs, 442,820 total views, joined 2026-08-23, last upload 1 day ago, avg length 00:18:38 |
| Colette Dubois | UC0mKF2tEF9XLoC_Z9KxkdQg | off-topic; room decor | 761 subs, 153,275 total views, joined 2026-09-13, last upload 20 hours ago, avg length 00:14:46 |
| Golden Fame | UCleH0KyMDt3p1hUDfc4atDQ | off-topic; Hollywood nostalgia | 125 subs, 68,823 total views, joined 2025-05-04, last upload 15 hours ago, avg length 00:30:36 |
| Classic Beauty Channel | UC4OLHUSbFgmMf8MJHGan1og | off-topic; religious content | 262 subs, 164,493 total views, joined 2025-12-14, last upload 1 day ago, avg length 00:05:04 |
| The Curious Why | UCnhKWr1sauQU4G1qsMaNnKQ | off-topic; no description, 17 views | None subs, 17 total views, joined 2026-09-26, last upload 1 day ago, avg length 00:11:17 |
| RBL Wellness & Beauty Tv | UC0X1-pDlni6YSEStvZhNuiQ | off-topic; yoga and wellness, 41K total views | 431 subs, 41,117 total views, joined 2020-06-29, last upload 16 hours ago, avg length 00:15:27 |
| Healthwise For Seniors | UCG2g-cTUJMWBNmMzkqB9i-Q | off-topic; senior health, by name (no stats) | no listing stats |
| BobPixie HairStyles | UCY50cJcqWO8AE_dDzrthgWQ | off-topic; 3.6-minute hairstyle lookbooks; description is about men's style | 3,320 subs, 819,133 total views, joined 2022-06-18, last upload 7 days ago, avg length 00:03:36 |
| Forever Chic After 60 | UCpPgC4sOEENZbG1QDNvtRcw | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 17 subs, 4,731 total views, joined 2026-09-18, last upload 2 days ago, avg length 00:13:23 |
| Margaret Winslow | UC0d-318_15KshbZgkPIvljw | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 60 subs, 12,690 total views, joined 2026-10-08, last upload 11 hours ago, avg length 23:18 |
| Ageless Beauty 60 | UCOPwN8VbdYNt_M0kgMeN_-A | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 552 subs, 44,588 total views, joined 2026-09-25, last upload 12 hours ago, avg length 00:17:39 |
| Style After 60 | UCD4-zunnA4VqYdPfoZ5YhuA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 45 subs, 16,021 total views, joined 2026-07-08, last upload 17 hours ago, avg length 00:10:26 |
| Style beyond 60 | UC13_ide7vSj8PL8XEoSJ8ew | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 71 subs, 5,212 total views, joined 2026-08-23, last upload 2 days ago, avg length 00:14:19 |
| Graceful & Glowing 60+ | UCV_ZJuDD_rXcHZ22DF-K7mg | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, 21 total views, joined 2026-09-14, last upload 1 day ago, avg length 00:17:22 |
| After 60 wardrobe | UCYTDB4vbsivPBM5XuWr_sOA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 8 subs, 669 total views, joined 2026-09-23, last upload 13 hours ago, avg length 00:17:08 |
| Ageless elegant wardrobe | UCSYCtuNMFlSPPLuhoc6HUag | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 14 subs, 1,167 total views, joined 2026-10-21, last upload 2 hours ago, avg length 13:33 |
| Elegance over 60 | UCyA0F0p4a6nNGdVV5yS-9xA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 45 subs, 5,098 total views, joined 2026-08-19, last upload 2 days ago, avg length 00:13:33 |
| Look Beautiful After 60 | UCFxa-kR0PMw4Hhvi6U84SPA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, None total views, joined 2026-10-03, last upload 7 hours ago, avg length 00:08:33 |
| Classy Look After 60 | UCO7Irjxr0aS3hr1KJeuq3OA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 10 subs, 802 total views, joined 2026-08-03, last upload 4 days ago, avg length 00:07:41 |
| Barbara Fashion | UCmvT5Gl7Blc603Im_Zvkccg | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 2 subs, 173 total views, joined 2024-06-28, last upload 1 hour ago, avg length 00:13:43 |
| Melanin Fashion Secrets | UCZGxoWm0-0UiesAPQarb01Q | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 56 subs, 4,893 total views, joined 2026-03-29, last upload 7 days ago, avg length 00:13:20 |
| Senior Wisdom Shared | UCL54HelJiHX8RhSaCMgHeBQ | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 311 subs, 92,953 total views, joined 2025-06-09, last upload 8 months ago, avg length 00:22:52 |
| Timeless Melanin Queen | UCB1qAMpK5j1hT8ovNG4HahA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 270 subs, 15,073 total views, joined 2026-06-04, last upload 23 hours ago, avg length 00:22:41 |
| MASTERING 60 | UCGlmvvF1HaRLVmhld7Zwmww | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 14 subs, 1,159 total views, joined 2026-06-30, last upload 20 hours ago, avg length 00:09:22 |
| Ageless Silver Chic | UCgcDqGnrlH7Okj_x8c0ARkQ | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 2 subs, 290 total views, joined 2026-09-04, last upload 22 hours ago, avg length 00:16:14 |
| Melanin Care | UCHY5J9WqFsbZdyagk3cfzqQ | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 117 subs, 8,057 total views, joined 2026-06-25, last upload 1 day ago, avg length 00:14:19 |
| Style elder | UCiYiKVLLCMCKBJSslFZtN4g | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 31 subs, 4,713 total views, joined 2026-05-30, last upload 4 weeks ago, avg length 00:14:32 |
| Classic Beauty Channel | UC9PedZLpvcAhtwR5ltxdw3A | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 300 subs, 4,505 total views, joined 2022-08-22, last upload 1 day ago, avg length 00:10:27 |
| Style without age | UCtabZ91H_V1fE5lfOs2yeyA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 178 subs, 34,739 total views, joined 2026-08-02, last upload 1 day ago, avg length 00:10:28 |
| Ageless Elegance | UCNW5YDAKTap17I3YF7aG-Lg | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 15 subs, 1,644 total views, joined 2026-09-22, last upload 10 days ago, avg length 00:15:47 |
| Golden Grace | UCX_2ZWYwZ1HWbXhRyKyuvkA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, 58 total views, joined 2026-09-03, last upload 1 day ago, avg length 00:15:03 |
| Gorgeous After 60 | UCuAg5iVoHvgEW_J-xJ5DVRQ | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 9 subs, 828 total views, joined 2026-08-25, last upload 21 hours ago, avg length 00:16:40 |
| Timeless Femme | UC-45I0qBHVOwUAc712cDVJg | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 14 subs, 2,307 total views, joined 2026-07-29, last upload 3 hours ago, avg length 00:13:35 |
| Stylish Over 60 | UCB6rbkmfVdmzqvrFfy9wkUA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 110 subs, 11,025 total views, joined 2026-08-11, last upload 1 hour ago, avg length 00:23:15 |
| Stylish after 60 | UCYHFtsxn2o43b-Ui3o8jQ8Q | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 199 subs, 21,598 total views, joined 2026-06-16, last upload 3 days ago, avg length 00:09:21 |
| Style Without Age | UChIhNB7QJwf7CMpx-qkfwOg | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, 91 total views, joined 2026-10-04, last upload 1 hour ago, avg length 00:20:15 |
| Ageless Chic | UCwAVQFqwPHBoTbzgxJv0Ymw | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, None total views, joined 2026-09-28, last upload 5 hours ago, avg length 00:15:03 |
| Anna Bella - Beauty | UCyrJAgi32YmYq8_KPlMnfwg | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 338 subs, 2,123 total views, joined 2026-10-14, last upload 1 day ago, avg length 00:17:47 |
| Classic Beauty & Style | UCe26BQcRdzk5EZ5IM0P1D8Q | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, 1 total views, joined 2026-10-23, last upload 3 hours ago, avg length 00:16:57 |
| Pretty Over 60 | UCCGlbWAmCIBJ5NV4WlZnqGw | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, 57 total views, joined 2026-09-03, last upload 4 hours ago, avg length 00:16:04 |
| Magnolia Mature Studio | UCp6C3Agl-s1C5WBeL-fu8cw | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 13 subs, 1,344 total views, joined 2026-10-16, last upload 2 days ago, avg length 00:13:06 |
| Mary Malkin | UCRF4XexegpAnRLqsCJBQoKw | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, 69 total views, joined 2026-09-19, last upload 3 minutes ago, avg length 00:07:01 |
| 60 and Stylish | UCILZsdYkovsBC3nWB_BhJ-w | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, 9 total views, joined 2026-08-31, last upload 2 days ago, avg length 00:10:32 |
| Dress Code Daily | UCpAGthWXIkAoa_fhtdTfakg | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 27 subs, 5,432 total views, joined 2026-05-11, last upload 10 days ago, avg length 00:14:48 |
| Stylish After 60 | UC8rf2u19rY2EIx0-2vvvh5w | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, 22 total views, joined 2026-08-24, last upload 4 hours ago, avg length 00:20:56 |
| Diane Hartwell | UCXMFQXW2KDG61Gb1ZrcvNDA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 66 subs, 22,636 total views, joined 2026-09-20, last upload 19 hours ago, avg length 00:10:31 |
| GlamAt60Plus | UCSiacLZ-fXk-GDye8OMeQqA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 35 subs, 3,272 total views, joined 2024-02-16, last upload 21 hours ago, avg length 00:15:25 |
| Van Luat Pham | UCt3hU5Tz7vrXSjcmBHoi4-A | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 21 subs, 2,577 total views, joined 2018-04-05, last upload 4 hours ago, avg length 00:13:13 |
| Ageless Elegance (2) | UCKih8sJ7Qlk98_ik01oppNA | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | None subs, 2,227 total views, joined 2026-10-10, last upload 8 hours ago, avg length 00:11:15 |
| Grace After 60 | UCSaXBU4cwbCJ_7ZKd5xLp0w | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 129 subs, 27,987 total views, joined 2024-12-31, last upload 3 days ago, avg length 00:10:54 |
| 60 & Fabulous | UCjqiqlfmQtVcK8zxKrhD9Sw | total views too low for any qualifying video (under 50K for a channel under a year old, under 100K otherwise) | 437 subs, 28,217 total views, joined 2026-08-27, last upload 1 day ago, avg length 00:18:45 |

## Real on-camera channels seen (out of this lane, not given rows)

These are for the fashion, hair and French+makeup lanes; several already appear in `french-makeup.csv`.

| Channel | Channel ID | Note | Listing stats |
|---|---|---|---|
| Nina Ubhi | UCHUJ5ydbxEDm0uZ27sw3R9g | real presenter | 736,000 subs, 68,726,049 total views, joined 2013-08-25, last upload n/a, avg length 00:17:06 |
| Glam Girl Gabi | UCYoiYowIowF7tYYel9NHpKQ | real presenter | 781,000 subs, 156,381,801 total views, joined 2018-09-23, last upload 1 day ago, avg length 00:15:01 |
| Darlene Obiyan | UCcvRTuhJHnMMCHB1Q4MmIaQ | real presenter | 111,000 subs, 11,231,777 total views, joined 2017-09-12, last upload 3 days ago, avg length 00:26:59 |
| Melissa55 | UCPVxz3ekxV8xW7HP-X2hiaw | real presenter | 161,000 subs, 18,688,530 total views, joined 2011-02-08, last upload 6 days ago, avg length 00:17:01 |
| Kim Sullins | UCvFBxvgf-zLTgmRHVe75x5g | real presenter | 17,800 subs, 1,949,855 total views, joined 2026-01-13, last upload 2 days ago, avg length 00:10:19 |
| Tamara’s Timeless Beauty | UCTHb57pkZsg0SFI-rsXHGaQ | real presenter | 127,000 subs, 11,002,002 total views, joined 2014-04-21, last upload 7 days ago, avg length 00:21:02 |
| Sixty and Me | UC3_-zY3XwUvsNT3ofJAw4cA | real presenter | 270,000 subs, 41,564,896 total views, joined 2013-01-16, last upload 1 day ago, avg length 00:11:13 |
| Dez Scott | UCba1EG8B4f_4wumI4724vRg | real presenter | 31,700 subs, 2,925,477 total views, joined 2021-04-02, last upload 3 days ago, avg length 00:25:30 |
| Makeup By Nikki La Rose | UCCydBRF6RjrT58FV6KO-wwg | real presenter | 579,000 subs, 167,236,293 total views, joined 2013-09-14, last upload 2 days ago, avg length 01:07:32 |
| Giedre Kavaliunaite | UCR28x4kMV_tHjQuMIiup5rw | real presenter | 165,000 subs, 26,362,790 total views, joined 2015-11-02, last upload 3 months ago, avg length 00:20:04 |
| Boys And Girls Hairstyles | UCwWEsSuYKPmqGwIlQSww-gg | real salon, all ages | 234,000 subs, 97,614,106 total views, joined 2012-03-04, last upload 7 hours ago, avg length 00:12:49 |
| Carissa Simenti | UCZH4ixqp9Cyx8EsUjorrmlA | presenter is 38 (description); real on camera | 2,540 subs, 466,073 total views, joined 2026-07-17, last upload 22 hours ago, avg length 00:23:56 |
| Marie-Anne Lecoeur - The French Chic Expert | UC3iINwXX6oQ0DqfE1SQ-S-w | real presenter | no listing stats |
| Aliceinparis | UC4MBo52ZvRib_GZav-ZpOcg | real presenter | 142,000 subs, 23,300,156 total views, joined 2020-08-11, last upload 20 hours ago, avg length 00:18:42 |
| Sandra Sallin | UCdcl4w0uOvJhryVuUL3Vwuw | real presenter | no listing stats |
| Justin Hickox | UCTfRM6bqWXYyCcs_78ywftQ | real presenter | 694,000 subs, 90,671,667 total views, joined 2007-11-12, last upload 2 days ago, avg length 00:55:44 |
| Beverly Hills MD | UCb8P5vUFd1Pr82cN41dLXGg | skincare brand channel (Beverly Hills MD) | 53,100 subs, 2,624,717 total views, joined 2014-09-10, last upload 6 days ago, avg length 00:08:02 |

## Found but NOT screened (NexLev limit reached): for the main session after the reset

Nothing below has been checked for type, audience share or top videos. The stats come from the similar-channel listing (2026-10-28).

**A. Pass the 10K-subscriber and recent-upload parts of the keep rule on listing stats; audience share, type and top videos still to check**

| Channel | Channel ID | Listing stats | Also in another lane file |
|---|---|---|---|
| Timeless  Elegance  Style | UCOkJSedGdibbqg1ucO7W5Bw | 91,300 subs, 15,663,323 total views, joined 2024-10-13, last upload 1 day ago, avg length 00:08:57 |  |
| WISE ELDER'S INSIGHT | UCQcMAWpNsth46OnO2u8TCkg | 97,200 subs, 10,362,206 total views, joined 2025-02-08, last upload 9 months ago, avg length 00:25:03 |  |
| Fashion & Elegance 50 | UCY4FtLwuNTvUzmsa9VbiCZw | 93,900 subs, 7,120,327 total views, joined 2025-01-16, last upload 9 days ago, avg length 00:11:58 |  |
| Ella Grace | UCdPhN0_2Yy56K_Wj5Lw9iTw | 60,100 subs, 3,617,508 total views, joined 2020-02-18, last upload 6 hours ago, avg length 10:48 |  |
| Trendy Short Hairstyles LookBook | UCQW-RcqcD7WD0PU-PMqIkyw | 55,200 subs, 12,330,221 total views, joined 2023-03-17, last upload 5 hours ago, avg length 00:11:44 |  |
| Ana Vogue | UCcai-ND1haM-bJtkOz_7oPA | 51,100 subs, 9,404,433 total views, joined 2024-05-21, last upload 17 hours ago, avg length 00:11:37 | french-makeup.csv (faceless_narrated) |
| Lux Gray | UCkhNFDBRUU8K82ZAosvHFmA | 40,200 subs, 3,298,274 total views, joined 2013-06-03, last upload 1 day ago, avg length 00:11:06 |  |
| Casual Comfort | UC1Ev-v3_A-yqIOVmTQEmn0g | 27,600 subs, 4,887,866 total views, joined 2022-04-17, last upload 23 hours ago, avg length 00:12:49 |  |
| Ebony lifestyle | UCzcEPpZRCK1aklhuUnNznzQ | 25,100 subs, 1,141,234 total views, joined 2025-10-08, last upload 19 hours ago, avg length 00:10:58 |  |
| Elegant Beyond Age | UCW5swRUkHClHj-4XE9YvwDw | 25,000 subs, 1,398,409 total views, joined 2026-05-26, last upload 2 days ago, avg length 00:21:48 |  |
| Glow After 60 | UC2u8sjLECpdV5IWTZrheusA | 16,000 subs, 1,421,860 total views, joined 2025-04-17, last upload 7 days ago, avg length 00:17:02 |  |
| Elegant After 60 | UC1eIOMYX7jZveQT3ezH59rw | 13,000 subs, 1,451,415 total views, joined 2025-06-22, last upload 3 weeks ago, avg length 00:14:06 |  |
| Classic Style 60+ | UCMhgcynY760cgpMH5TfSRtw | 12,000 subs, 1,329,166 total views, joined 2016-04-14, last upload 1 month ago, avg length 00:14:02 |  |

**B. Under 10K subs but total views high enough that a qualifying video is possible**

| Channel | Channel ID | Listing stats | Also in another lane file |
|---|---|---|---|
| Alice Luxe | UC4l04C6A_dog3pHfxoHggBg | 9,370 subs, 2,603,646 total views, joined 2024-07-25, last upload 7 days ago, avg length 00:14:07 |  |
| Fashion ideas | UCIhYhh3HSKWGp8LTWlpba9Q | 6,750 subs, 1,262,419 total views, joined 2023-09-01, last upload 1 hour ago, avg length 00:04:39 |  |
| Stylish Seniors | UCy1ypSyi_qISk2vpNHdtWHQ | 7,950 subs, 572,900 total views, joined 2024-12-09, last upload 11 hours ago, avg length 00:18:32 |  |
| French Fashion | UCCDxeYvF9t_XkLIawoSlmXQ | 4,660 subs, 565,205 total views, joined 2026-10-10, last upload 16 hours ago, avg length 00:12:24 | french-makeup.csv (ai_avatar) |
| Elegant Looks After Sixty | UCauMLf6DMetMzkCQv309FRA | 4,240 subs, 582,474 total views, joined 2015-12-08, last upload 3 days ago, avg length 00:18:48 | french-makeup.csv (faceless_narrated) |
| Senior Wellness Elevate | UCCRyYSezD6xrHlD3OhD0XaA | 2,220 subs, 516,828 total views, joined 2025-09-28, last upload 2 weeks ago, avg length 00:17:50 |  |
| Confident Closet | UCG-I7C4SKvJv1XLyv6EFnqw | 2,350 subs, 309,958 total views, joined 2024-12-28, last upload 1 day ago, avg length 00:20:14 |  |
| Fashion Awareness | UCdKGQ_KFJScNWnsBh1gBC9A | 1,350 subs, 409,733 total views, joined 2025-05-14, last upload 2 weeks ago, avg length 00:05:52 |  |
| Stylish Beyond 60 | UCIG0YdmteAJBkqOFTyAPgdg | 4,040 subs, 277,333 total views, joined 2026-07-09, last upload 1 day ago, avg length 00:16:35 |  |
| Fashion society | UCBqI405pZ3Pj3cgC0nSaMLg | 1,070 subs, 276,576 total views, joined 2026-07-31, last upload 22 hours ago, avg length 00:13:07 |  |
| Stylish outfits | UCWn1L2Rw2wBBhHwTbPLjfVw | 294 subs, 236,448 total views, joined 2026-09-27, last upload 21 hours ago, avg length 00:12:50 |  |
| Diana Iconic 50+. | UCzwdO_-92CQay_YDd9iluxQ | 1,110 subs, 194,303 total views, joined 2026-04-06, last upload 9 hours ago, avg length 00:08:57 |  |
| Modern Elegant 60 | UCCoTIkqSQ707Z_mjo-rgw4w | 2,460 subs, 186,248 total views, joined 2026-08-04, last upload 2 days ago, avg length 00:12:30 |  |
| Dazzling hair style | UC-r2D4SmNHIz7YL8X--WrKg | 302 subs, 181,218 total views, joined 2026-06-22, last upload 1 day ago, avg length 00:09:52 |  |
| Style & Grace Over 60 | UCSc6E36Yn54tJS033JqHKbg | 733 subs, 125,802 total views, joined 2026-09-10, last upload 1 day ago, avg length 00:14:20 |  |
| ELEGANCE AFTER 60. | UCZYB8pvmPEfCO3h0vDxh1kA | 1,250 subs, 123,700 total views, joined 2026-08-26, last upload 23 hours ago, avg length 00:14:36 |  |
| Stylish haircuts | UCMvXFDgAyhr-KZrY0iUQdug | 206 subs, 116,044 total views, joined 2026-06-28, last upload 17 hours ago, avg length 00:11:11 |  |
| Stylish Haircuts | UCua90VcQFsb7d_1BPcu1deg | 125 subs, 93,395 total views, joined 2026-06-22, last upload 1 day ago, avg length 00:10:06 |  |

**C. Probably below the bar (a qualifying video would need almost all of the channel's views), not verified**

| Channel | Channel ID | Listing stats |
|---|---|---|
| Chic Fashion Over 50 | UC4BrfgCf7jLS53P0WIULysw | 906 subs, 130,830 total views, joined 2024-05-22, last upload 3 hours ago, avg length 00:24:46 |
| The Timeless Wardrobe | UCIFNxLRdijyBQoMzhA5k97g | 763 subs, 120,632 total views, joined 2022-08-10, last upload 1 day ago, avg length 00:14:16 |
| Ageless Style Secrets | UC7BCs3Kc2FtB6KDdJjP6Oww | 902 subs, 52,943 total views, joined 2026-06-28, last upload 23 hours ago, avg length 00:13:28 |
| Style After 60 | UCbYE70VeEYdG22asS8H_hDw | 818 subs, 52,822 total views, joined 2026-01-31, last upload 3 hours ago, avg length 00:14:17 |
| Chic60Plus | UCDwKxV6wu25sohB-Rsx-raQ | 672 subs, 54,873 total views, joined 2026-08-21, last upload 3 days ago, avg length 00:11:21 |
| Ageless Women | UCs597gAcT1IaZzxmTGy1xgg | 695 subs, 55,173 total views, joined 2026-04-29, last upload 2 days ago, avg length 00:15:09 |
| Trendy Haircut | UCVXYrsQPbEkjh_zwJgtcSuQ | 203 subs, 54,032 total views, joined 2026-06-24, last upload 16 hours ago, avg length 00:11:11 |
| Modern Muse 60Plus | UCri-oeaEQTX9X9MhKdIYBew | 432 subs, 58,871 total views, joined 2026-07-21, last upload 9 hours ago, avg length 00:19:13 |
| Golden Age Fashion | UCfkD2j55k90xhXk21In0LgQ | 658 subs, 63,155 total views, joined 2025-10-30, last upload 3 months ago, avg length 00:11:50 |
| Ageless Beauty Queen | UCdXtokc69BLX7vikPsauHRQ | 1,350 subs, 80,818 total views, joined 2026-08-03, last upload 6 days ago, avg length 00:15:51 |

**D. Search finds with no stats collected**

| Channel | Channel ID | Found via |
|---|---|---|
| Mature Women's Style | UCHiE9iiarxu4KxzITECSABw | YT search: women over 60 look younger style tips (month, by views) |
| Refined After 60 | UCHnphEBp4q2GGfpQRaT5Byw | YT search: women over 60 look younger style tips (month, by views) |
| Stylish Chic women | UCxr1Nw2Ad4O2SBOVzWhwECg | YT search: women over 60 look younger style tips (month, by views) |
| Ever chic women | UCbXP8zDdqkcwWLxdZBtvr4A | YT search: women over 60 look younger style tips (month, by views) |

## Seen in search results, not candidates (summary)

- 141 pool entries from the searches above were off-topic for this study, by group:
  - men's style (e.g. Gentleman Post);
  - senior health, wellness and life-lessons channels (Life After Sixty, Wisdom After 60, Healthy After 60, Golden Age Wisdom and similar);
  - old-money and royal history;
  - French nostalgia and cooking;
  - celebrity biography;
  - general psychology.
- The category-81 filter browse (query 20) returned 61 general and young-audience beauty channels, dropped without screening.

## Housekeeping note (shared scratchpad)

At the start of the run I wrote to the shared scratchpad root by mistake:

- I overwrote another helper's `scratchpad/nf.py`.
- I appended 12 rows to their `scratchpad/pool.json`.

What I did about it:

- I removed my 12 rows, so their pool is back to its 50 entries.
- I replaced `nf.py` with a reconstruction that writes their schema. Its first lines say it was reconstructed by this helper.
- All my working files then moved to `scratchpad/faceless-ai/`.
- No file under `studies/` other than my two output files was touched.

