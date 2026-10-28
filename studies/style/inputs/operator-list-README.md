# The operator's list (2026-10-28)

The operator pasted 151 lines on 2026-10-28: section 1, "some of the top videos in the niche real people", and section 2, "some old faceless outliers and channels". They are kept as sent in `operator-list-2026-10-28.txt`. With repeats removed there are 121 entries; 120 were matched to a video and one was left unresolved.

## How the videos were found

NexLev was blocked (the weekly limit), so the main session read YouTube's public search pages directly (`../tools/ytlib.py`, `../tools/resolve_titles.py`), about 1.5 seconds apart.

- **Views are exact,** as YouTube showed them on 2026-10-28.
- **Dates are YouTube's own rough ages,** such as "3y ago" or "10mo ago". Video pages were refused ("too many requests"), so there are no exact dates yet. NexLev fills them in after the reset.
- **Copycats.** For many titles YouTube returns several near-identical titles on other channels. The match keeps:
  1. the channel named in the pasted line, if there is one;
  2. otherwise an exact title;
  3. otherwise the most-viewed near-identical title.
- **Runs differ a little,** because YouTube's results vary. The resolver ran three times and the final file combines the runs.
  - The main session fixed nine rows by hand (`match` = `manual`, or the reason is in `note`).
  - "makeup mistakes to avoid" is too general to match one video and is left unresolved.
- **The copy counts are a floor.** They count only the first 20 search results.

`operator-list-resolved.csv` has one row per entry: section, pasted line, video ID, title, channel and ID, views, age, length, and notes, including copies found on other channels.

## Results

119 distinct videos on 38 channels. 15 channels were not in `../discovery/master.csv` yet. 61 of the videos are five or more years old, so they predate the study's 2022 floor for models. They stay in as topic and title evidence.

### Real people (section 1)

| Channel | Videos in the list | Best video | Views | Posted | In master.csv |
|---|---:|---|---:|---|---|
| Dominique Sachse | 18 | The BEST Makeup To Look 10 YEARS YOUNGER! 10 Youthful Tips & Tricks / Domin | 12,698,331 | 8y ago | yes (real) |
| Nina Ubhi | 5 | HOW TO STOP CONCEALER FROM CREASING UNDER YOUR EYES / NINA UBHI | 6,961,730 | 5y ago | **new** |
| Hindash | 1 | HOW I DO MAKEUP ON MATURE SKIN / Hindash | 6,922,619 | 7y ago | **new** |
| Graceful Beauty | 4 | HOW TO Cover GRAY HAIR - IN SECONDS! **without coloring your hair** | 6,600,244 | 8y ago | yes (real) |
| Stay Fabulous with Nisha | 2 | HOODED, DROOPY EYES  - TIPS AND TRICKS (updated) | 6,201,951 | 10y ago | **new** |
| Nikol Johnson | 8 | THE SNEAKY EYELINER TRICK FOR MATURE WOMEN / Nikol Johnson | 5,852,962 | 3y ago | yes (real) |
| fabulous50s | 4 | 5 Biggest Makeup Mistakes On Mature Eyes Tutorial Over 50 / Fabulous50s | 5,404,374 | 7y ago | yes (real) |
| Glam Girl Gabi | 5 | Women with THIN FINE Hair LOVE this Hair Style (I can see why!) | 5,376,668 | 4y ago | yes (real) |
| Mathias4Makeup | 1 | How to do Makeup on Women over 60 Makeup Tutorial - mathias4makeup | 5,305,998 | 11y ago | **new** |
| Lisa Eldridge | 1 | Glowing,Youthful Day MakeUp Tutorial For Mature Skin | 4,902,744 | 13y ago | **new** |
| Busbee Style | 5 | 5 Style Tips To Look 10 Years *YOUNGER*! (Over 40) | 4,328,426 | 6y ago | **new** |
| rxstrmom | 6 | Chatty GetReadyWithMe ~ DID I HAVE A FACELIFT? ~ OVER 70~ SHOUTOUT | 4,217,484 | 6y ago | yes (real) |
| HotandFlashy | 9 | How I "Fixed" My Droopy Hooded Eyelids | 3,973,627 | 9y ago | yes (real) |
| Brittanybearmakeup | 2 | MAKEUP ON MATURE SKIN...Transforming My Mom! / BrittanyBearMakeup | 3,777,910 | 6y ago | **new** |
| Justin Hickox | 14 | You're Styling Your Bob Haircut WRONG! Do THIS Instead- 5 SECRETS | 3,221,942 | 2y ago | yes (real) |
| Marnie Goldberg | 2 | How To Not Look Frumpy & Older Than You Are-Get Out of That Rut!! | 2,838,725 | 4y ago | yes (real) |
| Tricia Cusden - Look Fabulous Forever | 1 | Define Your Eyes and Lips Over 60 - Makeup for Older Women | 2,641,505 | 13y ago | yes (real) |
| Risa Does Makeup | 3 | MASTERCLASS FOR HOODED AGING EYES / Game Changing NEW Technique! | 2,620,816 | 3y ago | yes (real) |
| Pretty Over Fifty | 1 | 5 Things That Happened When I Started Shaving My Face | 2,199,116 | 6y ago | yes (real) |
| Pampered Wolf | 2 | Over 35? Stop applying under-eye concealer like a Youtuber! | 2,022,869 | 8y ago | **new** |
| Style With Serena | 1 | How To Not Look Older! Fashion Mistakes Making You Look Old #lookyounger#ov | 1,927,513 | 3y ago | **new** |
| Loving Our Age | 1 | Do's and Don'ts for Hooded, Downturn or Mature Eye Makeup | 1,856,872 | 9y ago | **new** |
| Stylish Curves | 1 | Do's & Don'ts To Hide A Large Tummy & Flattering Ways To Dress A Belly | 1,718,400 | 3y ago | **new** |
| Style with Cathy | 1 | Summer Style Tips for Plus Size Apple Shape Women: How to Transform Your Lo | 1,699,545 | 4y ago | yes (real) |
| Angela Masson - Fashion Over 50 | 1 | Avoid These STYLE MISTAKES When Traveling To Europe This Summer | 1,514,752 | 3y ago | yes (real) |
| Tina Yong | 1 | How To Look Good On Video Calls - Zoom, FaceTime, Skype 👩‍💻 | 1,267,425 | 6y ago | **new** |
| Marie-Anne Lecoeur - The French Chic Expert | 1 | How Not To Look Older: Fashion Mistakes That Make You Look Older | 1,254,415 | 2y ago | yes (real) |
| Shepherd's Fashions | 1 | 10 Ways To Tie A Scarf | 933,535 | 4y ago | **new** |
| Audrey Coyne | 1 | How To Look EXPENSIVE Even On a BUDGET | 259,861 | 2y ago | **new** |
| Smitha Deepak | 1 | NO FOUNDATION Makeup with just 5 Items | 240,717 | 10mo ago | **new** |
| Aliceinparis | 1 | How NOT to Look Like A Tourist While Traveling To Europe This Summer | 109,364 | 2y ago | yes (real) |

### Faceless (section 2)

| Channel | Videos in the list | Best video | Views | Posted | In master.csv |
|---|---:|---|---:|---|---|
| Age with Style | 4 | 7 Blouse Mistakes Women Over 60 Should STOP Making NOW! | 1,107,946 | 1y ago | yes (unclear) |
| Chic After 60 | 4 | 8 COLOR COMBINATIONS That Make Older WOMEN Look EXPENSIVE, Younger and Turn | 959,790 | 1y ago | yes (faceless-ai) |
| Elegance At 60 | 1 | Pants to Avoid with a Large Tummy & Lower Belly Pooch - Apple Shapes, Short | 903,752 | 1y ago | yes (faceless-ai) |
| Ana Vogue | 1 | Makeup Tips for Women Over 50+ | 236,736 | 2y ago | yes (faceless-ai) |
| EverWise Older Women | 1 | 7 Blouse Mistakes Aging You After 60 And What to Wear Instead | 105,772 | 1y ago | yes (unclear) |
| Golden Chic Life | 2 | The ONLY 5 JEANS That Make You Look Amazing at 60+ | 50,157 | 1y ago | yes (faceless-ai) |
| Dress like a Queen 👑 | 1 | 7 Haircuts That Instantly Make You Look Younger 60+ | 24,044 | 9mo ago | yes (unclear) |

### Copies of the faceless titles

| Title | Kept as | Views | Near-identical titles on other channels |
|---|---|---:|---:|
| 3 Haircuts That Will Make You Look 10 Years YOUNGER & 3 You Should Avo | Chic After 60 | 855,081 | 16 |
| 5 Chic HAIRCUTS That Make Women Over 60 Look Stunning! | Chic After 60 | 50,771 | 12 |
| Makeup Tips for Women Over 50+ | Ana Vogue | 236,736 | 0 |
| These Are the 7 Bags You Shouldn't Be Using After 60 (and What to Use  | Age with Style | 319,936 | 12 |
| These Are The 7 Worst SHOES for Women Over 60 & Best Chic Alternatives | Age with Style | 457,890 | 15 |
| 7 DRESSES Black Women Should Stop Wearing After 60 | Age with Style | 280,133 | 9 |
| The ONLY 5 JEANS That Make You Look Amazing at 60+ | Golden Chic Life  | 50,157 | 15 |
| 8 COLOR COMBINATIONS That Make Older WOMEN Look EXPENSIVE, Younger and | Chic After 60 | 959,790 | 19 |
| 7 Blouse Mistakes Women Over 60 Should STOP Making NOW! | Age with Style | 1,107,946 | 16 |
| 7 Style Tips for Petite Women 60 and Over | Chic After 60 | 469,974 | 5 |
| 7 Haircuts That Instantly Make You Look Younger 60+ | Dress like a Queen 👑 | 24,044 | 15 |
| 10 DRESSES That Hide Belly Fat and Flatter Your Shape | Golden Chic Life  | 22,859 | 5 |
| Pants to Avoid with a Large Tummy & Lower Belly Pooch - Apple Shapes,  | Elegance At 60 | 903,752 | 13 |
| 7 Blouse Mistakes Aging You After 60 And What to Wear Instead | EverWise Older Women | 105,772 | 11 |
