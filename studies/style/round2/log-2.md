# Round 2, helper 2: log

Worklist: `round2/worklist-2.csv` (60 channels: 33 kept, 27 to-screen). Run date 2026-10-28.
Budget: at most 180 NexLev calls. Planned: 2 per kept channel, 3 per to-screen channel (147).

## Calls (running count)

- 01 Stylish & Grateful: outliers + videos = 2 calls (total 2)
- 02 MM Personal Styling: 2 calls (total 4)
- 03 Marie-Anne Lecoeur: 2 calls (total 6); outliers result too large for inline, read from saved tool-result file
- 04 Mindful Midlife: 2 calls (total 8)
- 05 Woman in midlife: 2 calls (total 10)
- 06 My Friend Deirdre: 2 calls (total 12)
- 07 Tracy Campoli: 2 calls (total 14)
- 08 Grayawhile: 2 calls (total 16)
- 09 KiKi Carr: 2 calls (total 18)
- 10 SparklingSilvers: 2 calls (total 20)
- 11 Deepa Berar: 2 calls (total 22)
- 12 50plusdaily: 2 calls (total 24); 0 outliers; Videos tab only 8 short uploads
- 13 Maria Crocker: 2 calls (total 26)
- 14 Mel C's Makeup & Style: 2 calls (total 28)
- 15 The Honest Channel: 2 calls (total 30)
- 16 All About Fashion: 2 calls (total 32)
  - note: All About Fashion uploads run 4:20-7:00; 18 of newest 30 are under 5:00 (these are not Shorts, just short slideshows). Normal (895) uses only the 5:00+ uploads, so ratio_vs_normal is extreme (1.1M video = 1229x).
- 17 Vivian Sinclair: 2 calls (total 34)
- 18 Ethereal Elegance: 2 calls (total 36)
- 19 French Fashion: 2 calls (total 38)
- 20 Timeless Style Living: 2 calls (total 40)
- 21 Lisa beauty: 2 calls (total 42)
- 22 Classic Style 60+: 2 calls (total 44)
- 23 Beauty is Tested: 2 calls (total 46)
- 24 Timeless Black Fashion: 2 calls (total 48)
- 25 Ella Grace: 2 calls (total 50)
- 26 Beauty of Black Queens: 2 calls (total 52)
- 27 Brand Smart Buy: 2 calls (total 54)
- 28 L'Age du Style: 2 calls (total 56)
- 29 Elegant Always: 2 calls (total 58)
- 30 Ever Chic At 50: 2 calls (total 60)
- 31 EverWise Older Women: 2 calls (total 62)
- 32 Ageless Melanin: 2 calls (total 64)
- 33 Stilvoll ab 60: 2 calls (total 66)
  - note: lanes for rows 20-33 (except 28) first written with ad-hoc labels (general-50plus, black-women-50plus, beauty-dupes, lookbook-slideshow, brand-review-50plus); relabelled to the brief's lane set, original description moved to notes as 'lane detail'. No numbers changed.
- 34 WISE ELDER'S INSIGHT: 3 calls (total 69)
- 35 Confident Closet: 3 calls (total 72)
- 36 Dazzling hair style: 3 calls (total 75)
- 37 Ageless Style Secrets: 3 calls (total 78)
- 38 Golden Age Fashion: 3 calls (total 81)
- 39 Chicbagstyle: 3 calls (total 84)
- 40 Jo - Shines Bright: 3 calls (total 87)
- 41 Fabulous After 50: 3 calls (total 90)
- 42 Ageless elegance (dN7): 3 calls (total 93)
- 43 Fashion Over 60 (The Mature Muse): 3 calls (total 96)
- 44 Historias de Adobe: 3 calls (total 99)
- 45 Melanin Elegance: 3 calls (total 102)
- 46 Adore Your Wardrobe: 3 calls (total 105)
- 47 TIMELESS PEARL: 3 calls (total 108)
- 48 Style After 50: 3 calls (total 111)
- 49 Fashion in Maturity: 3 calls (total 114)
- 50 Gigi Your Stylist: 3 calls (total 117)
- 51 Refined After 50: 3 calls (total 120)
- 52 Evergreen Styles: 3 calls (total 123)
- 53 Loya the Fashion Queen (worklist name garbled): 3 calls (total 126)
- 54 MAKEOVERGUY: 3 calls (total 129)
- 55 Loving Our Age: 3 calls (total 132)
- 56 Good Dreams Only: 3 calls (total 135)
- 57 Prime of your life: 3 calls (total 138)
- 58 Little Miss Fashion: 3 calls (total 141)
- 59 Busbee Style: 3 calls (total 144)
- 60 Brittanybearmakeup: 3 calls (total 147)

## Totals

- Channels done: 60 of 60 (33 kept, 27 to-screen). Rows: channels-2.csv 60, outliers-2.csv 407.
- NexLev calls used: 147 of 180 (2 per kept channel, 3 per to-screen channel). No failed calls, no retries, no limit or credit errors.
- Keep result: 44 yes, 16 no. All 33 kept channels still pass; 11 of 27 to-screen channels pass.
  - To-screen passes: WISE ELDER'S INSIGHT, Historias de Adobe, Adore Your Wardrobe, TIMELESS PEARL, Refined After 50, Loya the Fashion Queen, MAKEOVERGUY, Loving Our Age, Good Dreams Only, Prime of your life, Busbee Style.
  - Four of these are off the 50+ style niche (WISE ELDER'S INSIGHT, Historias de Adobe, Loya the Fashion Queen, Prime of your life). The rule is metrics only, so they stay "yes" with the topic noted in keep_reason.
  - TIMELESS PEARL and Refined After 50 pass only through the faceless-under-1-year-50K rule, and NexLev reads both as not faceless. The faceless call comes from the thumbnail reading.
- Type split (reading): faceless_narrated 32, real_on_camera 21, ai_avatar 5, mixed 2, unclear 0.

## Odd findings (descriptive)

- Shared titles across channels on this list:
  - 'The ONLY 5 Handbag Rules Women Over 60 Should Follow'
  - '5 Glasses That Make Women Over 60 Look Instantly Younger'
  - 'French Women Get More Beautiful With Age'
  - '7 Dresses That Hide a Tummy After/Over 60'
  - 'DON'T Cut Your Hair Short UNLESS...'
  - 'How to Wear Leggings Like a Mature Woman Over 60'
  - '5 Affordable Women's Brand(s) Everyone Ignores'
  - 'Old Person Smell'
  - 'Granny' glasses/lipstick
  - 'STOP Wearing These 5 Earrings After 60'
- The thumbnail wording 'Makes You 10x Younger!' appears on EverWise Older Women, Ageless Style Secrets, Fabulous After 50 and Evergreen Styles.
- Repurposed or switched channels:
  - Lisa beauty (joined 2019).
  - French Fashion (chess upload).
  - Melanin Elegance: joined 2015; all 25 uploads date from 2026.
  - Historias de Adobe: the handle and about text are still a 60+ style channel ('Timeless Grace 60+'), but since ~2026-10-14 it posts Spanish/English drama stories. Its 59K keep-qualifying video is a story.
- Videos tab nearly empty: Fashion Over 60 (1 of 12) and Gigi Your Stylist (2 of 86). The rest are presumably Shorts, which were not fetched.
- Members-only uploads have no view count and are excluded from the normal (Prime of your life, and earlier rows).
- Activity unclear:
  - Little Miss Fashion: all newest 30 uploads read '1 year ago'.
  - Brittanybearmakeup: newest Videos-tab upload is ~4 years old (Shorts not checked).
- Worklist row UCBeEI6IogaHOvlVB47GKrcA had a garbled name field; NexLev returns 'Loya the Fashion Queen'.
- Celebrity press photos are used as thumbnails (Little Miss Fashion; Loya the Fashion Queen uses runway/celebrity collages).
- Extreme ratio_vs_normal values where the normal is low or built from collapsed recent uploads:
  - All About Fashion 1229x
  - Prime of your life 1202x (a 2023 video against a members-heavy recent feed)
  - Classic Style 60+, Timeless Black Fashion, TIMELESS PEARL 443x
- MAKEOVERGUY's outliers call returned only one 2x video because NexLev's average is 292K; several other 2026 uploads were 86K-114K.
