# French-lens + makeup/skincare discovery log (Phase 2)

Helper lane: **french-makeup** (Part 1 `french-lens`; Part 2 `makeup-adj` / `skincare-adj`). Run 2026-10-28. NexLev tools only. Output: `french-makeup.csv` (65 kept channels, one row each).

## How the data was gathered (read before using the CSV)

The brief's method (youtube_channel_about + youtube_channel_videos popular/newest per channel) returns 10-20K tokens per call, too much for ~100 channels in one session. So the per-channel checks were done with smaller NexLev calls. The source of each figure is stated in the row:

- **Channel stats** (subs, views, video count, created, country, last upload): `get_channel_analytics`, or the `about` block NexLev returns inside `get_similar_channels` results, or `search_niche_finder_channels` stats. Last upload is often NexLev's relative text ("2 days ago" as of 2026-10-28).
- **Top three long-form videos since 2022**: `search_videos` (NexLev video index, channelId filter, startDate 2022-01-01, minLength 5:00, sort viewCount); `youtube_channel_videos` popular for Elegant After 60, Nikol Johnson and French Fashion; niche-finder top-video lists (marked "day approx."); or titles seen in `youtube_search` (marked with the relative age). Caveats: the NexLev video index is incomplete (it missed Nikol Johnson's 5.8M video and Ana Vogue's 251K video), its view counts lag live counts, and its dates for older videos are often rounded to an import date (e.g. many "2025-10-24"). Dates from `youtube_channel_videos` are derived from relative ages ("3 years ago").
- **uploads_last_90d**: `search_videos` count of indexed uploads since 2026-07-30 (all lengths) where run; blank where not pulled. Index counts may undercount (Camille Cowher: 0 indexed, but last upload "1 month ago").
- **nexlev_faceless / confidence**: `get_batch_channel_metrics_v2` (same NexLev classifier, 10 channels per call; also gives RPM) for most rows; `check_faceless_channel` for Elegant After 60, Nikol Johnson, Dominique Sachse. Where niche-finder's isFaceless/isAiChannel flags disagree with the classifier, `type` = `unclear` and both are quoted in `type_basis`.
- **est_monthly_revenue**: niche-finder estimate where the channel is in the niche-finder index; **rpm_est**: batch-metrics RPM (niche-finder RPM where marked).
- For ~25 real channels kept on subscribers + recent upload, top videos were **not pulled**; the row says so. These are worth a `search_videos`/`youtube_channel_videos` pass by the main session if they make the master list.

## Searches run

| # | part | tool | query / target | filters | result (count, new candidates) |
|---|---|---|---|---|---|
| 1 | part1 | search_niche_finder_channels | "French women style over 50" | limit 50, sortBy unset, page 1 | 50 results; 50 new (pool start) |
| 2 | part2 | search_niche_finder_channels | "makeup for women over 50" | limit 50, page 1 | 50 results; 19 new |
| 3 | part1 | search_niche_finder_channels | "Parisian chic style for older women" | limit 50, page 1 | 50 results; 7 new |
| 4 | part1 | search_niche_finder_channels | "how French women age gracefully" | limit 50, page 1 | 50 results; 10 new |
| 5 | part1 | search_niche_finder_channels | "French pharmacy skincare" | limit 50, page 1 | 50 results; 35 new (mostly general skincare/brand-avoid, few 50+) |
| 6 | part2 | search_niche_finder_channels | "makeup for mature skin" | limit 50, page 1 | 50 results; 10 new (mostly young general makeup) |
| 7 | part2 | search_niche_finder_channels | "hooded eyes makeup tutorial for older women" | limit 40, page 1 | 40 results; 5 new (young general makeup) |
| 8 | part2 | search_niche_finder_channels | "skincare routine over 50 anti-aging" | limit 40, page 1 | 40 results; 11 new (mostly 50+ health/fitness, off-scope) |
| 9 | part1 | search_niche_finder_channels | "European style for women over 60" | limit 40, page 1 | 40 results; 0 new |
| 10 | part1 | search_niche_finder_channels | "French woman in Paris sharing style and beauty secrets in English" | limit 40, page 1 | 40 results; 25 new (mostly Paris travel/French-language learning, off-scope) |
| 11 | part2 | channel_resolver | @DominiqueSachse | - | resolved to UCaGDszQCToHQHeG1XO2JiIw |
| 12 | part2 | channel_resolver | @NikolJohnson | - | UCuhS2wb4EgcjdwPG-g6z3dg |
| 13 | part2 | channel_resolver | @Fabulous50s | - | UCiWPU83VmOXjQ6xY0gIrhIQ |
| 14 | part2 | get_similar_channels | Dominique Sachse (UCaGDszQCToHQHeG1XO2JiIw) level 3 | async | FAILED; retried level 2: FAILED. Similar-channels list for Nikol Johnson showed Dominique Sachse's main channel is UCXrsVPFsk-66NTaoGMXoPFQ (the resolved ID appears to be a different/secondary channel); re-run on that ID |
| 15 | part2 | get_similar_channels | Nikol Johnson level 3 | async | 72 results; 67 new (rich seam of real mature-makeup channels) |
| 16 | part2 | get_similar_channels | Fabulous50s level 3 | async | 89 results; 88 new, but all fitness/yoga/tai chi/health: Fabulous50s is a fitness-over-50 channel, so its peers are out of the style scope; not screened individually |
| 17 | part1 | youtube_search | "French women over 60 never wear" | type video | 20 results; channels: Elegant After 60 (17 of 20), Stylish60plus, Classic Beauty & Style (new) |
| 18 | part1 | youtube_search | "how French women dress after 50" | type video | 20 results; 8 new channels: Marie-Anne Lecoeur, Aliceinparis, French Fashion, Fashion Mantika, Whispers Fashion & Styles, Loya the Fashion Queen, Ana Vogue, Rock Your Fashion |
| 19 | part1 | youtube_search | "Parisian chic over 60" | type video | 20 results; 7 new channels: Elegant Looks After Sixty, Ella Grace, Confident Closet, Over 60 Lifestyle, Bridget Fisher, Curiosity Street Style, Miranda Priestly |
| 20 | part2 | youtube_search | "makeup mistakes that age you" | type video | 20 results; 8 new channels: Risa Does Makeup, Tammy's Ageless Beauty, Simply Diane, Jeannie Giannone, Sue Blackhurst Beauty, Ageless Style Co., Ali Andreea, Chalene Johnson (also Dominique Sachse main ID UCXrsVPFsk-66NTaoGMXoPFQ, Nina Ubhi, Smitha Deepak, Makeup By Nikki La Rose already in pool). One result channel shown as "Second Bloom and 5 more" (collab/multi-channel listing, links dianehollis.com) - no channel ID given |
| 21 | part2 | youtube_search | "eyeliner trick for mature women hooded eyes" | type video | 20 results; 5 new channels: Stephanie Marie, Erin Parsons Makeup, Erica Taylor Beauty, Prime Melanin, Soojin Park (rest already in pool: Glam Girl Gabi, Nikol Johnson, HotandFlashy, Risa Does Makeup, Graceful Beauty, Kerry-Lou, Jodi Mannes, Wayne Goss, TheMakeupChair, Sephora) |
| 22 | part2 | get_similar_channels | Dominique Sachse main channel UCXrsVPFsk-66NTaoGMXoPFQ level 3 | async | 110 results; 98 new; mostly broad beauty/derm/fashion; 50+ relevant: Melissa55, rxstrmom, Pretty Over Fifty, Claudia Glows, Rena Hedeman, UnBlah Yourself, The Honest Channel, Dr. Susan Hardwick-Smith, What To Wear, Christie Kramer, Shepherds Fashions, Infinite Garden by Beth K; French-lens: ParisianVibe, Justine Leconte officiel |
| 23 | part1 | search_niche_finder_channels | "Italian style elegance for women over 60" | limit 30, page 1 | 30 results; 1 new (same faceless 50+ fashion cluster) |
| 24 | part1 | search_niche_finder_channels | "French skincare and beauty secrets for women over 60" | limit 30, page 1 | 30 results; 0 new |
| 25 | part2 | search_niche_finder_channels | "makeup over 60 to look younger" | limit 30, page 1 | 30 results; 1 new |
| 26 | part2 | search_niche_finder_channels | "drugstore makeup and foundation for mature women" | limit 30, page 1 | 30 results; 0 new |
| 27 | part2 | search_niche_finder_channels | "mature beauty vlogger makeup tutorials for women over 50" | limit 30, isFaceless=false, page 1 | 30 results; 9 new (mostly young beauty creators; Stylish & Grateful relevant) |
| 28 | part2 | search_niche_finder_channels | "skincare for mature skin over 60 wrinkles retinol" | limit 30, isFaceless=false, page 1 | 30 results; 11 new (mostly 50+ health/fitness; Tammy Weatherhead relevant) |
| 29 | part1 | search_niche_finder_channels | "French chic style older woman Paris" | limit 30, isFaceless=false, page 1 | 30 results; 8 new (Diana GOSS, Slow Down In Style relevant; rest broad/Paris lifestyle) |
| 30 | part1 | search_niche_finder_channels | "British style and elegance for mature women" | limit 30, page 1 | 30 results; 1 new (Spanish-language) |
| 31 | part2 | youtube_search | "makeup to look 10 years younger over 60" | type video | 20 results; 5 new channels: Zabrena, Jackie Alves, Bev Soutar Beauty, KiKi Carr, Beverly Hills MD (brand). Also surfaced Diane de Chambray (UC2z5yffdjwr3xpr-iDp9Yvw) = the operator's own channel, excluded (covered by Phase 1 baseline) |
| 32 | part1 | youtube_search | "French pharmacy skincare products women over 50" | type video | 20 results; 4 new channels: Finding Sofia (15 of 20 results), thelidiaedit, Care with Kate, Dr. Shereene Idriss |
| 33 | part1 | get_similar_channels | Elegant After 60 (UCn4q5n4EbawoOKOL_FK2tPg) level 3 | async | 60 results; 39 new; nearly all faceless/AI 50+/60+ fashion & hair (fashion/hair lanes). Also surfaced Diane de Chambray (operator's own) and Scarlet Starling (UCTMwV-uy20eaRwFfc4Sx13g, created 2026-09-15 same day as Diane; appears to be the operator's own Scarlet Sterling channel) - both excluded |
| 34 | part1 | get_similar_channels | Marie-Anne Lecoeur (UC3iINwXX6oQ0DqfE1SQ-S-w) level 3 | async | 84 results; 61 new; mostly real & faceless 50+ fashion (other lanes) plus men's 50+ style; Italian lens: Dolce Vita Fashion&Lifestyle |
| 35 | part2 | search_niche_finder_channels | "makeup tutorials for mature women over 50 by a mature beauty creator" | limit 50, isFaceless=false, minSubscribers 10000 | 50 results; 15 new (mostly young beauty/nails/hair creators); enriched Sally Atkins |
| 36 | part2 | search_niche_finder_channels | "anti-aging skincare reviews for women over 50" | limit 50, isFaceless=false, minSubscribers 10000 | 50 results; 15 new (mostly 50+ health/fitness and young skincare) |
| 37 | part2 | search_niche_finder_channels | "hooded eyes eyeliner and foundation tips for aging skin" | limit 50, minSubscribers 10000 | 50 results; 7 new (young beauty) |
| 38 | part2 | search_niche_finder_channels | "beauty and makeup over 60 and 70 silver hair" | limit 50, minSubscribers 10000 | 50 results; 7 new (ChicAfterSixty hair; rest 60+ wisdom/health) |
| 39 | both | get_batch_channel_metrics_v2 | 7 batches of 10 candidate channels | async | 70 channels: RPM, NexLev faceless flag + confidence, top country |

Per-channel verification calls (not discovery): `get_channel_analytics` x18 (Nikol Johnson, Fabulous50s, Marie-Anne Lecoeur, Aliceinparis, French Fashion, Ana Vogue, Elegant Looks After Sixty, Finding Sofia, thelidiaedit, Risa Does Makeup, Tammy's Ageless Beauty, Jeannie Giannone, Jackie Alves, Bev Soutar Beauty, KiKi Carr, Stephanie Marie, Zabrena, Sue Blackhurst Beauty); `search_videos` top-3 / last-90-day for 16 channels; `youtube_channel_videos` popular x3; `youtube_channel_about` x2 (both Dominique Sachse IDs); `check_faceless_channel` x3; `get_batch_channel_metrics_v2` x8 (80 channels).

## Failures and oddities

- `get_similar_channels` on Dominique Sachse `UCaGDszQCToHQHeG1XO2JiIw` (what `channel_resolver` returned for @DominiqueSachse) failed at level 3, retried at level 2, failed again. That ID is an empty 450-sub, 0-video channel. Her real channel is `UCXrsVPFsk-66NTaoGMXoPFQ` (@dominiquesachsetv, 1.89M); the similar-channel search on it succeeded.
- `search_videos` with `limit: 0` is rejected (minimum 1); used limit 1 and read `total`.
- The niche-finder index barely covers the real mature-makeup creators (Nikol Johnson's peers came almost entirely from `get_similar_channels`). Semantic queries mostly return the new faceless 50+ fashion cluster.
- Seed note: **Fabulous50s is a fitness/health channel** for women over 50 (workouts, menopause belly fat), not makeup/skincare. Kept as a 50+ peer (lane `lifestyle-mixed`). Its 89 similar channels are all fitness/yoga/tai chi and were not screened (out of the style scope).
- The shared scratchpad folder is also used by other helpers; this helper worked in its own subfolder.

## Excluded on sight (the operator's own channels)

- Diane de Chambray `UC2z5yffdjwr3xpr-iDp9Yvw` (62 subs, created 2026-09-15; seen via youtube_search and Elegant After 60 similars). Covered by the Phase 1 baseline.
- Scarlet Starling `UCTMwV-uy20eaRwFfc4Sx13g` (531 subs, created 2026-09-15, same day as Diane; seen in Elegant After 60 similars). Looks like the operator's Scarlet Sterling channel; please confirm.

## Screened out (reason; so they aren't searched again)

**Part 1 (French / European lens)**
- Mademoiselle Spends `UCp2NEe9VThU1qvPDavlVQGw`: real French presenter, 199K, active. Broad audience: winners not age-targeted ("French Dressing Rules EVERYONE Should Learn Once And For ALL" 1.8M, "10 Things Elegant Ladies NEVER Wear!" 1.4M, "French Table Manners..." 687K). A strong French-lens format reference even though it fails the audience test.
- Justine Leconte officiel `UChxkFSjTE7nLCHsDk8_pRhg` (1.02M, French designer): broad fashion audience.
- ParisianVibe `UC-KUF3oGTSSuix72gBqamWg` (617K): broad Paris fashion/lifestyle, not 50+.
- Les Frenchies `UC5m1fPLNTZCgLjIzO5iy-Ng` (482K), Paris Top Tips `UC7OYOafHE2YME_Bpq9lXPuw`, Visiting POV `UCRO_bRfOrkmCGZlaKCD3lVQ`, FrenchTastic Explorations, French Countryside Diary, My French Manor Tales, The Beau Chateau, Chef Vivien: France travel/food/home, not 50+ style.
- Lucile `UCJdLzKzBQIsY3IIsCxGS7EA`, Français avec Nelly, French Talks, ella entwistle, Eloise O'Connor: French language/culture, not 50+ style.
- The Mirror Edit `UCLTXZUZ7Sme8zekDHihbd2g`: faceless/AI, created 2026-08, top video 8.2K (under 50K).
- Finding Sofia `UCbkmE5D9C8BEtvCn0QkLOBg`: French pharmacy for 50+, but 580 subs, top 14,685; created 2025-04 (over a year).
- thelidiaedit `UCOYx03krfdD5OMlu1yHfkew`: 3.1K subs, NexLev avg 2,136 views, over-30/40 audience.
- Elegant Academy `UCKW9TVF2cM1CbJoGo4MjstQ`: last upload ~2025-10 (NexLev, at or past the 12-month line), 1.2K subs, top 64K.
- Classic Beauty & Style `UCe26BQcRdzk5EZ5IM0P1D8Q`: NexLev avg 29 views.
- Ageless Queens `UCgC-uVXN5nb6jw-uvNDTyzA`: last upload ~2025-10; star-photo compilations under 5 min.
- Dolce Vita Fashion&Lifestyle `UC1J9qwQqyZbEvwWccy4-nHA` (26.3K, Italy): Milan street-style compilations, not 50+-targeted by tags. Italian-lens reference.
- Eleganza-Stile Over 50 `UC591CBZ7NSvvJlwVnU3Jhjw` (21.1K, Italy): Italian-language.
- French-language (not English): L'Art de Bien Vieillir, Élégance Après 60, Hana et toi, Les Veillées de Mémé Odile, Secrets de France, Histoires de France, L'Autre France, Colette Dubois, Marie Dubois, Éclat Melanin, Défends Ton Assiette FR, Mieux Choisir, Dans ton assiette, Lá France D Autrefois, LaBelleClassique, Secrets de Cuisine d'Antan, Tendances du Jour.
- German-language: Mode und Stil 50+, Stil Mit 50+, Stille Eleganz, Stil kennt kein Alter, Elegant Sein, KlarerBlick, Stilvoll ab 60, Yumikos japanische Pflege.
- Spanish-language: Estilo Después de los 50, Elegancia Atemporal, Camino de los Ancianos, Belleza Sin Edad 60+, Elegancia Madura, Belleza Serena, Elegántica, Belleza de la Edad de Oro, Sachiko Mori, Yuna Han, Salud Dorada 70, Etiqueta Rosa, NARELVA, DR. EMILIO NAVARRO, Federer Archivos, Pura Vida Salud.

**Part 2 (makeup / skincare)**
- Zabrena `UCwQ48S6LdJVdGUM27M0oy4w` (587K): broad drugstore-makeup audience; mature share of winners not established ("7 Makeup Tricks That Make You Look 10 YEARS Younger" 44K).
- Broad beauty / derm, not 50+-led: Marlena Stell, Wayne Goss, Lisa Eldridge, Smitha Deepak, Nina Ubhi, Christen Dominique, Ali Andreea, Makeup By Nikki La Rose, Tina Yong, Charlotte Tilbury Beauty, Sephora, TheMakeupChair, Shonagh Scott, Erin Parsons, Hindash, Milabu, Kaur Tips, Jessy Hartel, Madddnot, Laura Lee, Tati, Abbey Yung, James Welsh, Dr. Sam Ellis, Dr. Shereene Idriss, Doctorly, Dr. Daniel Sugai, DrAmirKaram, Chalene Johnson.
- Young / general beauty creators from niche-finder: Freya Tidy, coco, linag0ldi, vevina chu, Beauty With Brain, Beauty Theory, Edens Glam, Makeupbyash, Glambysophi, Rokael Lizama, Jammy G, Mansi Palav, peachushi, Chloewaterz, Candi, LeleGalliano, Sam Chapman, ugly elle, leeskin, Station Jaya, and the nail/wig/hair tutorial channels in those results.
- Beverly Hills MD `UCb8P5vUFd1Pr82cN41dLXGg`: brand channel; the mature-makeup video is 6 years old.
- Rena Hedeman `UC9SGmSLSQAlxl6cPU_-NH1w` (17.1K): last upload "1 year ago" (outside 12 months).
- makeupcoach `UCAhH9smF6wYrsdeH0l5p9rw` (39.3K): German-language.
- Tammy Weatherhead `UCfObiIAS1BNzqiIjW2XsSPQ` (133K): mostly short-form Korean skincare; no 50+ focus in winners.
- Aging Queens `UC0uabQ9Zs6bDpr1n-gqR3MQ`: faceless, created 2025-10-14 (just over a year), 3.3K subs, top 67K (under 100K).
- Beauty Mina `UCZBoYIhVz0NHI4b0J1q4TlA`: account created 2019, 4.39K subs, top 81K (under 100K).
- Style After 60 `UCCac3e7jjjwD4SZdprJRmxA`: under a year, top 38K (under 50K).
- Skin Truth Index `UCikLsy4ZJsvaJnP7_ykAkJg`: under a year, top 49K, 279 subs.
- Vien Tran (705 subs, 28K), dangcongthan (462 subs), Diana Cole (140 subs), Novokumar Ghosh (280 subs, 17K), Skin Sense (218 subs), The Beauty Markup (363 subs), Black Skin Science (228 subs; 348K video but not 50+), THEALOELIXIR (2.5K, 47K): too small or no qualifying video.
- Simply Diane `UCnhKWr1sauQU4G1qsMaNnKQ`, Ageless Style Co. `UC0-ioRByvtgk4BNAGJCsgbw`, Soojin Park `UCeM_U686us-NxFOeEx3RIxA`: new persona channels with 25 / 268 / 8 views on recent uploads; no evidence of a 50K video. A youtube_search result titled "7 Makeup Mistakes That Age You After 60 (I Made Every One)" was listed under "Second Bloom and 5 more" (a multi-channel collab) linking dianehollis.com, the same "Diane" persona as Simply Diane.
- Healthy Over 40 (last upload 2024-10), Healthy Aging Secrets (2023-10), Ms. BoBo (~2025-10), Edens Glam, peachushi, Candi, Jammy G (2023-24): inactive.
- 50+ health/fitness (out of style scope): Fabulous50s' 88 similar fitness channels, Live Healthy Over 50, Fit Over 50, Age Over 50s, Senior Smarts, Holistic Health Over 50, Fitness journey, Better Health While Aging, Body Fix Exercises, Prosper Over 50, WISE AGING, Healthy Long Life, Life To Your Years, Wisdom After 60, Golden Elders, SoulSync, Staying Ageless.

## Leads met but not screened to a decision

Too little data in hand to apply the keep rule; worth one `get_channel_analytics` + `search_videos` call each.
- Fashion Mantika `UCCyXqRy2wU-TAs2PzZIXr3Q`: "How to Dress Like a Parisian Woman After 50" 67,992 (1mo); faceless; not monetized; channel age unknown (keep if under a year).
- Curiosity Street Style `UCToGf14fYoWXnUI6R_fuk7w`: Paris street style over 50, 15,195; faceless; NexLev avg 40K/video.
- Bridget Fisher `UCyp6bHEwRL03WvELlZWUVlA`: "How French Women Stay Stylish Over 40: 6 Caroline de Maigret Rules" 44,943; real; UK.
- Ella Grace `UCdPhN0_2Yy56K_Wj5Lw9iTw`: Linda Wright French style over 60, 18,665; faceless.
- Confident Closet `UCG-I7C4SKvJv1XLyv6EFnqw`, Miranda Priestly `UCbs1izzqoeLUfXmKmEJ-t7Q`, Over 60 Lifestyle `UCF69VL7T5lj_YaXJC3IwX0w`, Rock Your Fashion `UCeW6gtrT1ojeODaFyATlx_Q`, Whispers Fashion & Styles `UCsLv1bB6G20BpVt4P5_aLmQ`, Loya the Fashion Queen `UCBeEI6IogaHOvlVB47GKrcA`: small French/Parisian-over-50/60 uploads, each seen with under 10K views.
- Prime Melanin `UCgOIMljjMuq6NIORaFKEBsg`: "10 Eyeliner Secrets to Instantly Lift Mature Eyes" 33,818 (4mo).
- Erica Taylor Beauty `UCwUG82Z94P_kuiq0e5pSxBg` ("EYELINER OVER 40", 36,543, 3y), possibly an older account of Erica Taylor (kept row `UCTxMakpAk-pNwySUepxS3SQ`).
- Kristi Allure `UCy-GIxvF11R7_2fKOWg5pug` (16.4K): beauty/lifestyle; 50+ share unknown.
- Care with Kate `UCc3sGUgG2fexaCAZY6qKa2w`: French pharmacy haul 7,073.

## Met in my searches, other lanes (not added here; for the fashion / hair / faceless helpers)

Niche-finder data suggests these pass the keep rule: Age with Style `UCsiBzifgu6vwRubtmdIcOzA` (89.6K), Elegance At 60 `UCGhT9pJVlUY0SwhDRkQoyKg` (74.2K), Dress like a Queen `UCVPjIX_7LnoHfkYrk9QiEZQ` (70.4K), TRENDS SPOTTED FASHION `UCQ7Nd8tNX_xPGRhtjx4VivQ` (70.1K), Shopping On Champagne `UCV7lS0SIBTYd-m4fG_x_GoA` (66.1K), Vivian Sinclair `UCfDezkF4P9FNxrD6PFGCoPw` (35.9K, created 2026-08, 906K video), Her Classy Femininity, CougarFashion (over 40), Elegant Older Women, Personality and style, Golden Chic Life, Elegant Style After 50, Senior Fashion Styles, Styled Beyond 60, Rosalind Gray (created 2026-07, 158K), ChicAfterSixty (hair, 492K), Second Bloom (created 2026-10, 72K, etiquette), EverGrace Style, All About Fashion, Fashion4U, Style In Her Prime, Ageless Style 50s & 60s, Elegant Beyond Age, Glow After 60, EverWise Older Women, Lux Gray, Fashion & Elegance 50, Midlife Posh Closet, What To Wear, Your Guide To Style, Christie Kramer, Shepherd's Fashions, Infinite Garden by Beth K (grey hair), Beth Djalali, The Style Insider, Annemarie My Fashion Life, MY FRIEND DEIRDRE, Heather Anderson, Style with Cathy, Loving Our Age, Ageless Melanin, Golden Melanin Lifestyle, Beauté de l'Âge d'Or and Bienvenue sur Élégance 60+ (French-tagged channels with English hair titles, under a year, 68K / 93K). Inactive in that cluster: Ethereal Elegance and Wellness 360 (last ~2025-11, still inside 12 months), Elegant Fashion And Style Over 60 (last 2024-10, inactive).

## Counts

- Screened: about 230 channels named above or in the CSV (65 kept, ~130 screened out by name, ~15 leads), plus ~90 fitness similars set aside as a group and ~60 other-lane channels passed on.
- Kept: Part 1 = 15 (9 `french-lens`, 6 fashion / fashion+hair channels met through the French searches); Part 2 = 50 (34 `makeup-adj`, 11 `skincare-adj`, 5 `lifestyle-mixed`).
- Type split of kept rows: Part 1 = 3 real, 6 faceless_narrated, 1 ai_avatar, 5 unclear; Part 2 = 41 real, 6 faceless_narrated, 3 unclear.
