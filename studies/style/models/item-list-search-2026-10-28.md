# Item-list model search: real presenters (helper H7, 2026-10-28)

**Goal:** find item-list videos (glasses, jewelry, earrings, necklaces, handbags, scarves, shoes, accessories) aimed at women 40+/50+/60+ and presented by a **real person on camera**, as model-script candidates. The channels make videos like "5 Glasses That Make Women Over 60 Look Instantly Younger".

**Short answer:** nothing qualifies for **glasses, earrings, necklaces or jewelry**. Every video in the window with real views on those topics comes from a faceless or AI-avatar channel. The closest real-presenter jewelry videos are weak (about 1x their channel's normal) or several years old. Real presenters do have strong item-list videos on **shoes** and **scarves**. The best one, Style With Serena's shoes video (640K, 13.3x), was already in `round2/outliers-all.csv`. One new fit turned up: Kay Harms on scarves (78K, 3.1x).

NexLev calls used: **29 of 30**.

## Queries run

| # | Tool | Query / filters | Useful result |
|---|---|---|---|
| 1 | youtube_search | "jewelry mistakes women over 50" | all faceless/AI (Stylish60plus 214K, Chic After 60 133K, Fashion & Elegance 50 69K) |
| 2 | youtube_search | "glasses frames women over 60 look younger stylist" | all faceless/AI (Vivian Sinclair 911K, Chic After 60 227K, ChicAfterSixty 85K) |
| 3 | youtube_search | "earrings that age you over 50" | all faceless/AI; Beth Djalali (real) jewelry trends 23.7K |
| 4 | search_videos (DB) | "jewelry", 2024-10-28+, 5:00+, 20K+ views | worldwide noise (wholesale markets, ASMR); nothing aimed at 50+ |
| 5 | search_videos (DB) | exact "over 50", 2024-10-28+, 5:00+, 10K+ (500 rows) | Style With Serena shoes, Kay Harms travel shoes, Tina's Best Midlife shoes |
| 6 | youtube_search | "Makeoverguy glasses frames mature women" | no glasses video from Makeoverguy (hair makeovers only) |
| 7 | youtube_search | "handbags women over 60 stylist" | all faceless/AI; Catherine Campbell 22K (later found to be an AI presenter) |
| 8 | youtube_search | "accessories mistakes over 50 personal stylist" | real presenters, but general style mistakes (MM 1.57M, Beth Djalali 138K), not item lists |
| 9-11 | search_videos (DB) | fuzzy "jewelry earrings necklace…", "glasses eyeglasses frames…", "handbags bags scarf shoes accessories…" + women over 50/60, 2024-10-28+, 5:00+ (500 rows each) | filtered to real/unknown channels: only shoe videos from real presenters |
| 12-15 | search_videos (DB) | exact "earring", "glasses", "jewelry", "necklace", 2024-10-28+, 5:00+, 10K+, sorted by views (500 rows each) | no real 50+ presenter (top results are worldwide noise; one unknown channel: Belleza Serena glasses 355K) |
| 16 | youtube_search | "how to choose eyeglass frames women over 50 tips" | real presenters only in old videos (Timeless Beauties by Jacqueline 269K, 7y; SusanAfter60 70K, 6y) |
| 17 | youtube_search | "how to wear necklaces neckline over 50 style" | all faceless/AI (Ana Vogue is AI; Vivian Sinclair necklaces 113K is AI) |
| 18 | youtube_search | "jewelry styling tips over 60 how I wear my jewelry" | real presenters only in old/low videos (UnBlah statement jewelry 29.5K, 3y) |
| 19 | youtube_search | "eyewear trends 2026 glasses women over 40 what to wear instead" | faceless/AI, or men's channels, or optician channels not aimed at 50+ |
| 20 | youtube_search | "jewelry trends 2026 women over 40 what's in what's out" | The Style Insider (real) 63.6K = 0.8x; others are younger creators not aimed at 40+ |
| 21 | youtube_search | "glasses over 50 my best tips new frames try on women over 60 real" (past year) | all faceless/AI, or try-on/sponsored glasses |
| 22 | youtube_search | "earrings necklace mistakes older women stylist talks" (past year, by views) | all faceless/AI |
| 23-26 | youtube_video_details | Vy1yYqc001c, i3VhtCE3d_U, dFAGM7iBWRI, qhIyVZDEdP0 | exact views and dates; Catherine Campbell's description says "Catherine Campbell is an AI presenter." |
| 27 | youtube_search | "how to wear a scarf women over 50 ways to tie" (past year, by views) | **Kay Harms scarf tutorial 78K** (real); the rest faceless/AI |
| 28 | youtube_search | "handbag mistakes over 50 what to carry instead stylist" (past year, by views) | all faceless/AI |
| 29 | youtube_video_details | uBqNLIiLnv4 | exact views and date for Kay Harms |

No channel-normal calls were needed: every real channel below is already in `round2/channels-all.csv`.

## Candidates

Exact views are from youtube_video_details where marked "(exact)". All other figures are as search showed them. Channel normal comes from `round2/channels-all.csv`.

| Channel | Title | Video ID | Link | Views | Uploaded | Length | Normal | Ratio | Presenter (how judged) | Format | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Style With Serena | Wear THIS, Not THAT: 5 Outdated Fall Shoes to Ditch in 2026 | dFAGM7iBWRI | https://youtu.be/dFAGM7iBWRI | 640,045 (exact) | 2026-09-20 | 26:49 | 48,000 | **13.3x** | real woman (channels-all real_on_camera; description signed "XO, Serena", her own sizes listed) | 5-item list, "wear this, not that" | **fits.** Best real item-list model found. Already in outliers-all (13.29x), but not on the known-item list in the brief. |
| Dressed for My Day with Kay Harms | How to Tie a Scarf this Winter - Feel Confident & Look Stylish in Scarves | uBqNLIiLnv4 | https://youtu.be/uBqNLIiLnv4 | 78,090 (exact) | 2025-12-18 | 20:28 | 25,000 | **3.1x** | real woman (channels-all real_on_camera; description in first person, signed "~ Kay") | how-to: 5 scarf types, ways to tie each | **fits.** New: not in outliers-all. Channel is aimed at 50+ (tags "fashion over 50", e-book "for women over 40"); the title itself carries no age. A how-to/demo, not a "mistakes" list. |
| Style With Serena | Top 10 Most Comfortable Shoes! / Must Have Shoes for Women Over 50 | Vy1yYqc001c | https://youtu.be/Vy1yYqc001c | 202,977 (exact) | 2024-04-17 | 33:06 | 48,000 | 4.2x | real woman (as above; mentions her own bunions) | top-10 list with outfits | **weak.** Uploaded before 2024-10-28 and under 1M. Also leans toward product picks (affiliate list). NexLev's database date (2025-02-25) is wrong. |
| Beth Djalali | Spring 2026 Jewelry Trends Every Woman Over 50 Should Try | qhIyVZDEdP0 | https://youtu.be/qhIyVZDEdP0 | 23,678 (exact) | 2026-03-19 | 12:32 | 20,000 | 1.2x | real woman (channels-all real_on_camera; describes shopping and wearing the pieces herself) | 5-trend list with styling advice | **weak.** The only real-presenter jewelry list for 50+ in the window, but no outlier and far under 70K. |
| The Style Insider | The Only Jewelry Trends That Actually Matter in 2026 | N0SCl6Eh6FE | https://youtu.be/N0SCl6Eh6FE | 63,591 | ~8 months ago (~2026-02) | 15:15 | 80,000 | 0.8x | real woman (channels-all real_on_camera) | trend list | **weak/no.** Below the channel's normal; title not age-aimed. |
| Dressed for My Day with Kay Harms | Best Travel Shoes for Stylish Women \|\| Comfortable Shoes for Women Over 50 | n0FVHKL7CtY | https://youtu.be/n0FVHKL7CtY | 42,000 | ~2025-10 (database date, approximate) | 23:00 | 25,000 | 1.7x | real woman (channels-all) | shoe picks | **weak.** Under 2.5x and 70K; product picks. |
| Tina's Best Midlife | Cute, Comfortable & Affordable Fall Shoes for Women Over 50 \| Honest Reviews | yuOlMPrRG74 | https://youtu.be/yuOlMPrRG74 | 23,000 | 2026-10 (~2 weeks) | 15:42 | 2,700 | 8.5x | real woman (channels-all) | product review roundup | **no.** A review/haul-style format, and only 23K. Already in outliers-all. |
| Capsule Closet Stylist | The Ultimate Guide to Accessories for Women Over 60: Timeless Elegance | -OfNT2xw4B8 | https://youtu.be/-OfNT2xw4B8 | 4,400 | ~2026-09 (database date) | 11:37 | 3,500 | 1.3x | real woman (channels-all) | accessories guide | **no.** Right topic, but no traction. |
| Catherine Campbell | 7 Bags You Shouldn't Be Carrying After 60 (And What to Carry Instead) | i3VhtCE3d_U | https://youtu.be/i3VhtCE3d_U | 22,369 (exact) | 2026-10-17 | 15:58 | not in csv | n/a | **AI**: the description says "Catherine Campbell is an AI presenter." | 7-item list + instead | **no** (not real). |
| Timeless Beauties by Jacqueline | TIPS FOR PICKING EYEGLASS FRAMES FOR WOMEN OVER AGE 50+ | 6KauoTS7KjY | https://youtu.be/6KauoTS7KjY | 269,002 | ~7 years ago (~2019) | 18:26 | not in csv, not fetched | n/a | probably a real woman (named channel, first-person description; **not verified**) | glasses how-to tips | **old, separate list.** The only sizeable real-presenter glasses video found, but outside the window and under 1M. |
| SusanAfter60 | Tips On Selecting Eyeglass Frames | oG3ahAnLMX0 | https://youtu.be/oG3ahAnLMX0 | 70,274 | ~6 years ago | 5:11 | not fetched | n/a | probably a real woman (first-person description; not verified) | glasses tips | **old.** Outside the window, under 1M. |
| Beth Djalali | Making A Statement: The Classic Jewelry Every Woman Should Own \| Style Over 50 | SmbbcwrTCRg | https://youtu.be/SmbbcwrTCRg | 56,879 | ~3 years ago | 9:14 | 20,000 | (2.8x vs today's normal) | real woman (channels-all) | jewelry essentials list | **old.** Outside the window, under 1M; sponsored by Native. |
| UnBlah Yourself | Dos and Donts of Statement Jewelry \| How to choose, style and wear it without looking cheap | dFVnI4LtEbw | https://youtu.be/dFVnI4LtEbw | 29,502 | ~3 years ago | 23:24 | 22,000 | 1.3x | real woman (channels-all) | dos and don'ts | **old/weak.** |

Other real-presenter item outliers **already in `round2/outliers-all.csv`** (not re-checked; that file's dates are rounded from relative ages): MM Personal Styling "Do's and don'ts of shoes with jeans" (KVlrLcdaJ8w, 176K, 3.2x); Adore Your Wardrobe "What Shoes to Wear with Wide-Leg Pants" (kCy2p4Yijns, 95K, 3.96x); Bridget Fisher "This Year's Sneaker Trends REVEALED" (O3dyfJ5oCR8, 147K, 8.2x); Julie Catherine "How to Wear Sneakers Stylishly Over 50" (GpN1FweBEAE, 80K, 9.6x, channel typed "mixed"); The Style Insider "Top Shoe Trends For 2025" (xRrjoVADdrA, 182K, 2.3x); Diana GOSS "Dresses Shoes And Bags Pairing Mistakes" (CVir8z2ULBY, 116K, 2.7x).

**Not candidates, listed for context.** These are the big item-list videos on the exact topics, and all are from faceless/AI channels (type from channels-all):
- Vivian Sinclair glasses (2q_6Qf69Ywc, 911K) and necklaces (AbrbifrM9mI, 113K): ai_avatar
- Chic After 60: glasses (I5ksu0xZTcA, 227K), jewelry rules (G4ao9SYVrDw, 134K), earrings (ESjFJQPlc4w, 50K): ai_avatar
- Stylish60plus earrings (V2jDlroQV3g, 215K): faceless
- Age with Style bags (XLDRv1nV_xo, 320K): faceless
- TIMELESS PEARL crossbody (cgbsZZ2xwIY, 222K): faceless
- Belleza Serena "7 Stylish Glasses…60+" (wAjgJoth8Nk, 355K): **not checked**. The channel is not in the csv. A Spanish-named channel with a translated-style title, so probably faceless, but unverified.

## Top picks (in order)

1. **Style With Serena: "Wear THIS, Not THAT: 5 Outdated Fall Shoes to Ditch in 2026"** (dFAGM7iBWRI). Real woman, 640K, 13.3x, Sept 2026, 26:49. The strongest real item-list model in the window, already in outliers-all.
2. **Kay Harms: "How to Tie a Scarf this Winter"** (uBqNLIiLnv4). Real woman, 78K, 3.1x, Dec 2025, 20:28. New find. A how-to rather than a mistakes list.
3. **Beth Djalali: "Spring 2026 Jewelry Trends Every Woman Over 50 Should Try"** (qhIyVZDEdP0). Real woman, 23.7K, 1.2x, Mar 2026. The only real 50+ jewelry list in the window. Weak, kept only because nothing better exists for jewelry.
4. **Style With Serena: "Top 10 Most Comfortable Shoes / Must Have Shoes for Women Over 50"** (Vy1yYqc001c). Real woman, 203K, 4.2x, Apr 2024. Strong but before the window.
5. **Timeless Beauties by Jacqueline: "Tips for Picking Eyeglass Frames for Women Over Age 50+"** (6KauoTS7KjY). 269K, ~2019. The only sizeable real-presenter glasses video found. Old, and presenter not verified.

## Doubts and limits

- **Glasses, earrings, necklaces and jewelry:** no real-presenter video that meets the brief (2024-10-28+, about 70K+, 2.5x+) turned up in 29 calls. For the last two years, these topics on YouTube appear to be almost entirely faceless/AI. This is a finding, not proof of absence: search covers only top-ranked results, and NexLev's database is thin for this niche.
- NexLev's database dates for older videos are often import dates (many show 2025-02-25/26). Only dates marked exact come from youtube_video_details.
- Presenters were judged by channel type in `round2/channels-all.csv` (earlier thumbnail reading), plus the video descriptions fetched here. No check_faceless call was used. Jacqueline and SusanAfter60 were judged by name and description only.
- Serena's and Kay Harms's videos carry affiliate links, as most real style channels do. They are advice videos, not single-product sponsored reviews.
