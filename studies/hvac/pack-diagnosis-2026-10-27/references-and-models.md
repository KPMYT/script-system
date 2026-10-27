# HVAC pack diagnosis: reference material and models (2026-10-27)

Read-only diagnosis for the Roger the HVAC Guy pack, to be built by copying `plumbing-scripts`. It says, file by file, what in plumbing's `references/` transfers as-is, what must be adapted, and what HVAC needs instead. Nothing in either repository was changed except this file.

**Sources.** Plumbing pack as installed: `/root/.claude/skills/synced/82c74450-.../plumbing-scripts/` (`SKILL.md`, `references/`), shortened below to `PS/`. HVAC research: `/home/user/niche-research/studies/hvac/` (`HV/`). Views, dates and lengths for HVAC videos come from `HV/data/raw/topvideos-exact-2026-10-26.json` (the same exact pull as `HV/top-100.csv` and `HV/recent-winners.md`, innertube `/next`, 2026-10-26); a `~` marks a census tab-rounded figure (`HV/data/raw/census-videos-2026-10-26.csv`), whose date is also approximate; `P3` marks a figure from `HV/data/raw/top-real-person-3y-2026-10-26.csv`. Channel types are the study's readings (`HV/data/raw/census-types-{A,B,C}-2026-10-26.csv`, `HV/channels.csv`); "not found" means the study has no type for that channel.

**Short answer.**
1. The plumbing pack's *structure* references mostly transfer: about 30 of its 39 model files have a beat map that fits an HVAC title of the same type. Its *content* references (voice samples, excerpts, price guide) are plumbing through and through and must be rebuilt, not copied.
2. Only 4 plumbing models are HVAC or next to it already: S18 (HVAC peroxide), S13 (furnace condensate), R05 (spray foam, a drafts video) and R17 (generator in an outage).
3. HVAC has strong real-person candidates for most types, but proven faceless HVAC models are thin outside Ray Dutton's 6 videos and the two brand verdicts. Ranked verdict, decision versus, "doing it wrong" and cheap-fixes-vs-quote have **no** proven faceless candidate.
4. Only 4 HVAC transcripts are on disk, all AI-voiced (Ray Dutton x2, HVAC Exposed x2). No real-person HVAC transcript has been pulled, so the voice samples cannot be written yet.

---

## 1. Model library

### 1a. Plumbing's 39 model files: does the structure serve HVAC?

Types and tags from `PS/references/models/INDEX.md`. R = real channel (structure and voice), S = AI-voiced (structure only). "HVAC use" names the batch-1 title (number from `HV/ideation/greenlit-log.md`) the structure fits.

| File | Video type | R/S | HVAC? | Why (one line) |
|---|---|---|---|---|
| R01 | banned / code explainer | R | partly | "why it's not allowed" fits refrigerant or venting rules; no batch-1 title needs it |
| R02 | other (tips list) | R | partly | list pacing only; no villain or money |
| R03 | how-to | R | partly | "why it failed before the fix" fits #14 (flame sensor) |
| R04 | head-to-head | R | yes | verdict split by household = heat pump vs gas furnace |
| R05 | product swap | R | yes | already a drafts video (1,529,886 in `HV/recent-winners.md`); fits #11, #12 |
| R06 | hidden cause | R | yes | cause printed on the product = the MERV rating on the filter (#3) |
| R07 | single-product fix | R | partly | stake before the product; pest content |
| R08 | how-to | R | partly | short step pacing; solder content |
| R09 | mistakes list | R | partly | pass/fail stake, no money; HVAC mistakes run on money |
| R10 | other (facts) | R | partly | facts list, no saving |
| R11 | seasonal / emergency | R | partly | preparedness shape fits an outage kit; 0.55x, weak |
| R12 | seasonal / emergency | R | no | built on news footage; 0.16x |
| R13 | how-to | R | yes | "who should not do this" first fits #5, #6, #14 (80% furnaces, gas smell) |
| R14 | how-to | R | partly | rule line per step |
| R15 | single-product fix | R | yes | amounts-and-steps recipe fits #7 (soap mix); 3:57 is too short for runtime |
| R16 | never-do (pacing) | R | partly | lived moment before each hack |
| R17 | seasonal / hidden cause | R | yes | an outage procedure in order fits #16; 4:06, under 5 minutes |
| R18 | product swap | R | partly | popular option judged fairly fits washable filters (#9) |
| R19 | single-product fix | R | partly | whole promise in 14 seconds |
| R20 | single-product fix | R | yes | honest escalation ladder fits #14 ("if it still shuts off") |
| R21 | how-to (drywall) | R | yes | the two opening moves are topic-free |
| S01 | N things | S | yes | cross-reference chain fits #7 |
| S02 | head-to-head | S | yes | one scale before the contenders = the MERV scale for #9 |
| S03 | never-do | S | yes | fits #13 |
| S04 | mistakes list | S | yes | fits #4 |
| S05 | N things | S | yes | price per item fits #7 |
| S06 | single-product fix | S | yes | it is #5's format source |
| S07 | hidden cause | S | yes | #10's format source |
| S08 | single-product fix | S | yes | #6's format source |
| S09 | how-to (routine) | S | yes | first-person routine fits #8 |
| S10 | banned / code | S | partly | as R01 |
| S11 | head-to-head | S | partly | evidence units fit #9; "tested to destruction" can't be said |
| S12 | head-to-head | S | yes | topic rounds fit heat pump vs furnace |
| S13 | how-to / seasonal | S | yes | same topic as #5, #6, #8; 1.36x at 7 days, unproven |
| S14 | single-product fix | S | yes | "And It's NOT Vinegar" shape = #5 |
| S15 | single-product fix | S | yes | "And It's NOT Bleach" = #5's exact tail |
| S16 | mistakes list | S | partly | mistakes in job order fit a how-to like #14 |
| S17 | N things | S | yes | correction item fits #7 |
| S18 | N things (HVAC) | S | yes | already HVAC; keep its `[UNSAFE: banned]` labels (coil misting) |

**Verdict:** structure yes for 25, partly for 13, no for 1 (R12). But every file's content, script and "Doesn't transfer" notes are plumbing, so the HVAC pack should keep only the ones it uses and add HVAC models beside them (see 1c and risk 3).

### 1b. The 16 batch-1 titles mapped to types

| # | Title (short) | Type |
|---|---|---|
| 1 | 9 Thermostat Habits | warning / habit list |
| 2 | Do These 9 Things Before the First Cold Snap | seasonal checklist |
| 3 | The $5 Filter ... Better Than the $30 One | **new: product myth-bust** (cheap beats premium; closest R06 hidden cause) |
| 4 | 11 Furnace Mistakes HVAC Companies Hope... | warning list (mistakes) |
| 5 | 1 Cup of This ... NOT Bleach | substance mystery (single-product fix) |
| 6 | Pour Vinegar ... Watch What Comes Out | substance mystery |
| 7 | 11 Things HVAC Techs Don't Want You to Know About Dawn | **N things about one product** |
| 8 | I Pour Vinegar ... Every Month ... THOUSANDS | substance mystery, first-person routine |
| 9 | Pleated vs Fiberglass vs Washable vs HEPA ... Ranks All 4 | ranked verdict |
| 10 | Why HVAC Techs' Own Furnaces Never Break Down | **hidden cause / own-house routine** (S07) |
| 11 | THIS Is Why Your Heating Bill Is So High | **hidden cause: the bill and drafts** |
| 12 | 7 Cold-House Fixes ... $5,000 Insulation Quote | **new: cheap fixes vs the quote** |
| 13 | NEVER Plug Your Space Heater Into These 5 Things | warning list (never-do, safety) |
| 14 | Furnace Keeps Shutting Off? The $12 Part | symptom diagnostic + cheap-part repair |
| 15 | Ceiling Fan WRONG All Winter | **new: "you've been doing it wrong" one-setting fix** |
| 16 | Your Car Can Keep Your Furnace Running | **outage / emergency how-to** |

Brand verdict and decision versus are needed by no batch-1 title (CONCLUSIONS §4.1 puts a brand verdict in batch 2).

### 1c. HVAC model candidates by type

Who: **R** = real person on camera (voice and structure); **FV** = faceless, narrator not checked (could be a human voice-over like Got2Learn; listen before using for voice); **F** = faceless AI or persona (structure only); **?** = type not found. Proven = 300K+ faceless or 1M+ real (operator's rule). Transcript paths: `RT/` = `HV/data/raw/ray-sources-2026-10-26/transcripts/`; `SP/` = `/home/user/script-system/studies/plumbing/data/`. All are English, US, 5:00+.

**Warning / habit list (#1, #4, #13)**

| ID | Title | Channel | Views | Uploaded | Length | Who | Proven | Transcript |
|---|---|---|---|---|---|---|---|---|
| K2jCz3D5z_0 | The 5 Thermostat Habits That Wear Out Your AC Years Early | Ray Dutton's Garage | 1,129,891 | 2026-08-18 | 14:28 | F | yes | no |
| qbWN3OViWxQ | 5 AC Mistakes HVAC Companies Hope You Keep Making | Ray Dutton's Garage | 589,530 | 2026-07-31 | 14:06 | F | yes | `RT/tx_ray2.txt` |
| wZk06FJWMlM | 5 Energy Bill Mistakes Utility Companies Hope You Keep Making | Ray Dutton's Garage | 405,898 | 2026-08-29 | 14:20 | F | yes | no |
| _g8gQ1gg1FM | 5 Furnace Filter Mistakes That Will Cost You Money! | The Funny Carpenter | 2,898,729 | 2024-02-15 | 5:34 | R | yes | no |
| V-jmSjy2ArM | Space Heater Nonsense | Technology Connections | 5,388,888 | 2019-02-13 | 17:43 | R | yes | no |
| HnMuNCl7tZ8 | The clever feature that makes cheap heaters safe — and why they're actually dangerous | Technology Connections | 2,950,693 | 2025-02-01 | 28:56 | R | yes | no |

Near miss: "5 BIGGEST Winter HVAC Mistakes Homeowners Don't Know!" (`Unx9Ze10N98`, HVAC Guide for Homeowners, 982,052, 6:44, R), just under 1M. Plumbing S03/S04 cover the item shape.

**Seasonal checklist (#2)**

| ID | Title | Channel | Views | Uploaded | Length | Who | Proven | Transcript |
|---|---|---|---|---|---|---|---|---|
| dOZ-8__G4uU | Before You Shut Your AC Down This Fall, Do This (Or Pay for It Next Spring) | Ray Dutton's Garage | 1,229,174 | 2026-09-11 | 11:49 | F | yes | no |
| fHAlfm21vYw | Before You Turn On Your Heat This Fall, Do This (Or Pay for It the First Cold Night) | Ray Dutton's Garage | 943,315 | 2026-09-14 | 14:42 | F | yes | no |
| mP0IjyvQtxw | Before You Turn On Your Heat This Fall, Watch This (Or Pay For It All Winter) | The DIY HVAC Guy | 1,220,217 | 2026-09-26 | 14:56 | R | yes | no |
| --A2I2s7aNw | Yearly Furnace Cleaning And Maintenance Pro Tips | Everyday Home Repairs | 2,169,980 | 2022-11-07 | 8:56 | FV | yes | no |
| pBBnXHse-T0 | 15 Air Conditioner Maintenance Tips | Word of Advice TV | 1,969,301 | 2019-05-11 | 32:00 | R | yes (cooling) | no |

This fixes plumbing's weakest type: its four seasonal models are 0.55x, 0.16x, 4:06 long, and 7 days old.

**Substance mystery / "pour X and watch" (#5, #6, #8)** — **too few HVAC candidates.**

| ID | Title | Channel | Views | Uploaded | Length | Who | Proven | Transcript |
|---|---|---|---|---|---|---|---|---|
| yIh1HAlbhc0 | 11 Things HVAC Technicians Don't Want You to Know About Hydrogen Peroxide! (#8 Saves $900) | TheCheapFix | 1,094,534 | 2026-08-07 | 14:58 | F | yes | `SP/competitors/thecheapfix/yIh1HAlbhc0/` (= S18) |
| qAxJb0J1HH0 | How to UNCLOG your AC DRAIN Condensate line FAST - Water stains on Ceiling? or in the Pan | Silver Cymbal | 3,773,264 | 2019-07-31 | 8:10 | R | yes | no |
| Kny-VwwzTn8 | How to Unclog AC Drain Line Fast (3 Seconds), Avoid Repairman | jeffostroff | 1,676,241 | 2019-03-22 | 8:47 | ? | yes if real | no |
| dRL13JlclhM | BEST AC Drain Line Cleaning Tool \| 92 % DON'T Know This | Deanin' It Yourself | 1,595,451 | 2023-01-25 | 5:51 | R | yes | no |

The only faceless HVAC substance video over 300K is TheCheapFix's (already S18). The real ones are condensate how-tos, not substance videos. The operator's own HVAC data point, "Pour One Cup of Vinegar Down Your AC's Drain Line Today (Before It Floods Your Ceiling)" (`cFYptbCvNjI`, Roger the Pipe Guy, 37,000, 23:30, 9.04x; `HV/data/raw/plumbing-own-channels-2026-10-26/videos_roger.csv`), isn't proven by the rule and has no transcript on disk. Keep plumbing's S06, S08, S14, S15 and S13 as this type's models.

**Ranked verdict, "Ranks All 4" (#9)**. **No faceless candidate.**

| ID | Title | Channel | Views | Uploaded | Length | Who | Proven | Transcript |
|---|---|---|---|---|---|---|---|---|
| RkjRKIRva58 | Best Furnace Filter Brand? 3M Filtrete vs HoneyWell BestAir, Nordic Pure, Flanders EZ Flow | Project Farm | 2,574,233 | 2021-02-14 | 12:55 | ? | yes if real | no |
| RdbFAG5xbyY | The ULTIMATE Air Filter Test [Engineer Tested] | Brand Ranks | 1,351,786 | 2024-10-31 | 13:20 | ? | ? | no |
| sQGfO4hNb60 | We Tested Every Air Purifier! One Clear Winner! | Project Farm | 1,147,219 | 2026-03-08 | 21:15 | ? | yes if real | no |

All three are filmed tests, which our scripts can't claim (`PS/SKILL.md`, "A title that promises tests"). The faceless 3-way "Window AC vs Mini-Split vs Central: The Math Nobody Shows You (The Real Cost Over 10 Years)" (`auUvh-k5ja4`, Coil Exposed, 212,736, 8:12, F) is under 300K. Use plumbing S02 (857.86x) and S11 for structure.

**Brand verdict, "The Only N Brands Worth Buying" (batch 2)**

| ID | Title | Channel | Views | Uploaded | Length | Who | Proven | Transcript |
|---|---|---|---|---|---|---|---|---|
| 86S3ITbfzQY | The Only 4 AC Brands Worth Buying in 2026 (Everyone Else Is Overcharging You) | Vent Exposed | 672,609 | 2026-05-25 | 8:12 | F | yes | no |
| QKPPm6M0__o | The Only 5 HVAC Brands Worth Buying (The Lifetime List) | HVAC Exposed | 578,285 | 2026-02-28 | 12:08 | F | yes | no |
| r_uP9itJ0HQ | STOP Buying the WRONG Air Conditioner Brands | Atlas AC | 1,873,961 | 2022-11-28 | 15:24 | R | yes | no |
| x2BK-zr4raE | STOP Buying This HVAC Brand | The DIY HVAC Guy | 1,295,963 | 2024-04-13 | 9:30 | R | yes | no |

Plumbing has no model of this type at all. Every proven one is about AC or HVAC in general. No furnace-brand video is proven: the biggest found is "The Only 4 Furnace Brands Worth Buying in 2026 (The 20-Year List)" (`m85JmJWFt7U`, HVAC Mike, 7,240).

**Symptom diagnostic, "Why your furnace keeps..." (#14)**

| ID | Title | Channel | Views | Uploaded | Length | Who | Proven | Transcript |
|---|---|---|---|---|---|---|---|---|
| sRvH-io-ZtA | The Most Common Reason Why A Gas Furnace Won't Turn On | Everyday Home Repairs | 2,777,727 | 2022-09-15 | 8:25 | FV | yes | no |
| 3Jonl_TLkpE | Furnace Not Working - The Most Common Fix | Word of Advice TV | 2,567,766 | 2018-10-20 | 8:57 | R | yes | no |
| _b6p0fkWhCY | #1 Problem & Quick Fix with Central Air Conditioning Not Cooling | Silver Cymbal | 4,307,792 | 2018-07-20 | 8:53 | R | yes | no |
| stZs8Co80vk | 8 Reasons Why Your AC is Freezing Up | Word of Advice TV | 2,034,948 | 2018-08-12 | 8:54 | R | yes | no |
| yJxDc90hs4g | Furnace wont start.  What to do before calling the repair man. | grayfurnaceman | 1,215,132 | 2012-09-12 | 10:11 | FV | yes | no |

No faceless persona video passes: Ray's "Why 70 Degrees Feels Cold in Your House Every Winter (It's Not the Furnace)" (`GKizclJLSq0`, ~155,000, 13:15) is the best. Symptom-fix is a weak persona format (0.98x, `HV/formats.md`).

**Cheap-part repair (#14)**

| ID | Title | Channel | Views | Uploaded | Length | Who | Proven | Transcript |
|---|---|---|---|---|---|---|---|---|
| Is0pv2Qnza0 | HVAC Contractors Practically Make Their Living On These | The DIY HVAC Guy | 2,449,985 | 2024-05-25 | 11:26 | R | yes | no |
| i8nDBZo6XyE | Was Quoted $400. I Fixed It For $11.72! AC Capacitor Testing and Replacement | How To Home | 2,195,593 | 2023-04-22 | 11:41 | R | yes | no |
| 1bRsFAMgZRQ | Furnace Not Igniting - How to Check and Replace Ignitor | Word of Advice TV | 1,366,846 | 2018-11-29 | 13:08 | R | yes | no |
| R7AKPgBB_R4 | How To Clean Your Furnace Flame Sensor | HouseImprovements | ~1,000,000 | ~2014 | 9:46 | ? | yes if real | no |
| y07w1hiKIrI | Keep Your Family Warm During A Power Outage By Installing This $5 Part | The DIY HVAC Guy | 4,291,080 | 2023-10-15 | 11:47 | R | yes | no |

No faceless candidate: Ray's "$X part" reruns all stayed under 50K (`HV/ray-dutton-sources.md` §4).

**Decision versus, heat pump vs gas furnace (later batch)**. **Too few: no head-to-head is proven.**

| ID | Title | Channel | Views | Uploaded | Length | Who | Proven | Transcript |
|---|---|---|---|---|---|---|---|---|
| 7J52mDjZzto | Heat Pumps: the Future of Home Heating | Technology Connections | 4,845,958 | 2021-02-28 | 35:15 | R | yes (explainer, not a versus) | no |
| GhAKMAcmJFg | This is Why Heat Pumps May NOT Be The Future | Skill Builder | 2,541,987 | 2021-07-19 | 13:12 | R | yes (UK) | no |
| wbY3n5ofevU | Heat Pump vs Gas Furnace - Which is the Best Choice For You? | HVACDirect | ~248,000 | ~2023 | 6:16 | ? | no | no |
| OAok8omYqSY | Heat Pump Vs. Furnace - Which is BETTER? | Atlas AC | ~212,000 | ~2025 | 14:00 | R | no | no |

Use plumbing R04 and S12 (tank vs tankless) for the shape.

**N things about one product (#7)**: plumbing S01, S05, S17, S18 already fit. The HVAC real-person "N things they don't want you to know" lists: "Top 5 Things AC Companies Don't Want You To Know How To Do!" (`AQQH9QwC46A`, How To Home, 2,980,312, 2023-04-29, 12:40, R, no transcript) and "3 Things HVAC Contractors Don't Want You To Know About." (`SkLMRM9NnBY`, The DIY HVAC Guy, 2,770,350, 2022-08-05, 13:17, R, no transcript). Both are task lists, not one product, so they help with structure only in part.

**Hidden cause / product myth-bust (#3, #10, #11)**

| ID | Title | Channel | Views | Uploaded | Length | Who | Proven | Transcript |
|---|---|---|---|---|---|---|---|---|
| _ZgVjFpBnQA | The $30 AC Filter Is Destroying Your HVAC System (Here's Why) | Ray Dutton's Garage | 773,572 | 2026-08-02 | 15:10 | F | yes | `RT/tx_ray3.txt` |
| l2yyfYpcwpQ | Why the $30 Filter Is Destroying Your HVAC System (The Airflow Lie) | HVAC Exposed | 351,124 | 2026-03-30 | 13:38 | F | yes | `RT/tx_hvacexposed_filter.txt` |
| J95l9Ue4224 | THIS is Why Your Heat Bill is So High! Rim Joist Insulation Technique! | Home RenoVision DIY | 5,842,373 | 2024-12-07 | 18:21 | R | yes | no |
| MFGRsWoSf4w | The Most Common Furnace Filter Issue And How To Fix It | Everyday Home Repairs | 1,351,765 | 2021-12-27 | 10:07 | FV | yes | no |

For #10, plumbing S07 is the format source and stays the main model.

**Cheap fixes vs the quote (#12)**. **Thin.** "You Won't Believe This Insulation Solution for COLD Walls!" (`6CE72U92R-I`, WINNI, 9,166,055, 2024-09-04, 8:45, type not found, no transcript) is the topic source, but it's an on-camera build. "Spray Foam is Expensive. Use THIS Instead!" (`sHL4lBAhklA`, Silver Cymbal, 1,529,886, 2026-08-30, 5:34, R; transcript `SP/competitors/silver-cymbal/sHL4lBAhklA/`, = R05) is the closest proven structure. The title format's source (204k) isn't HVAC.

**"You've been doing it wrong" one-setting fix (#15)**. **Thin.** The topic source, "Ceiling fans: the simple idea we keep screwing up" (`_KWdCqpXB7A`, Technology Connections, 3,632,065 P3, 2026-06-17, 71:11, R), is a 71-minute essay, so it's no use for structure. Ray's "You're Cleaning Your AC Wrong (And It's Costing You)" (`UdyqMC1GVxQ`, ~140,000, 13:31, F) is under 300K. Use R06 and R15 (short, one-setting reveals).

**Outage / emergency how-to (#16)**

| ID | Title | Channel | Views | Uploaded | Length | Who | Proven | Transcript |
|---|---|---|---|---|---|---|---|---|
| Qx3cC1y23JY | Why Buy A Generator? You Have One Parked In Your Driveway. | The DIY HVAC Guy | 2,450,035 P3 | 2025-10-25 | 7:08 | R | yes | no |
| y07w1hiKIrI | (as above, the $5 part) | The DIY HVAC Guy | 4,291,080 | 2023-10-15 | 11:47 | R | yes | no |
| rX4eyZaHAjw | 15 Cheap Walmart Items That Become WORTH GOLD When Your Furnace Dies | Lost Survival Knowledge | 1,327,280 | 2026-10-14 | 22:21 | F | yes | no |
| erq-QuCN0G0 | 6 Lifesaving Tips to Keep Warm During a Winter Power Outage | The Provident Prepper | 1,216,524 | 2020-10-23 | 15:10 | R | yes | no |

Plumbing R17 (generator) also transfers, though it runs only 4:06.

**Pattern from the electrical pack** (`origin/claude/intelligent-ride-v1at70`): one CSV of picks (`studies/electrical/model-picks-2026-10-27.csv`, 32 rows with id, video_id, views, posted, length, video_type, why, transcript_ok), real 1M+ channels only, and an adapted spec (`electrical-scripts/model-file-spec.md`) that adds "Stakes", "Safety lines", a "US or UK" line and an "Emotion voicing" section. HVAC should copy the CSV and the transcript_ok check. Its stakes and safety-lines fields suit HVAC (CO, gas, the cold night) better than plumbing's spec does.

---

## 2. Voice samples

**Plumbing's voices** (`PS/references/voice-samples.md`): three verbatim stretches from Got2Learn (faceless voice-over over diagrams, `pmN88UvZfDI`), Silver Cymbal (on camera, a windshield video, `fseq9NvO_zw`) and Roger Wakefield (on camera, an older master plumber, `WXJGaGtXrgY`). The "Borrow / Don't borrow" block (pointing at the picture, own demos, the trade's motives, hype, single prices, banned phrases, personal life) is topic-free and transfers as-is. The three samples are plumbing (and one is windshields) and get replaced.

**HVAC candidates for 2-3 verbatim clips** (register to match: plain, practical, older tradesman; none has been listened to, so the age and register are readings from thumbnails and About pages):

| Channel | Video to clip | Why | Watch for |
|---|---|---|---|
| **Everyday Home Repairs** (FV, 2.78M top) | `sRvH-io-ZtA` (2,777,727) or `--A2I2s7aNw` (2,169,980) | voice over hands, the format closest to ours, like Got2Learn in plumbing | confirm it's a human voice |
| **grayfurnaceman** (FV, 167K subs) | `yJxDc90hs4g` (1,215,132) | furnace-only, plain "before you call the repair man" framing; also has "The your heat exchanger is cracked so your furnace must be replaced scam" (`X3Y-yA42UBk`, ~299,000), Roger's upsell villain | 2012 audio quality; confirm the voice and age |
| **Word of Advice TV** (R, 661K subs, appliance repairman per About) | `3Jonl_TLkpE` (2,567,766) | step-by-step, plain, "most common fix" | points at the camera a lot |
| **Silver Cymbal** (R) | `_b6p0fkWhCY` (4,307,792) or `qAxJb0J1HH0` (3,773,264) | already plumbing's sample 2 voice, so the house sound stays the same across trades | has a transcript on disk only for non-HVAC videos |
| Atlas AC (R, Kenneth Carpenter, co-owner) | `r_uP9itJ0HQ` (1,873,961) | the only real brand-verdict voice | contractor sales register |

Not for voice: **The DIY HVAC Guy** (the biggest real HVAC channel, but "real young man in red cap" by the thumbnail reading, `HV/channels.csv`; use for structure), **How To Home** (high energy), **Technology Connections** (distinctive essay voice; CONCLUSIONS §6.6 says "structure more than tone"), and every Ray Dutton, HVAC Exposed or John The HVAC Guy video (AI-voiced).

**On disk:** no transcript of any real HVAC voice. The four HVAC transcripts (`RT/`) are all AI-voiced. Pull 3-4 of the videos above through NexLev's transcript tool (it doesn't count against the search cap, per the niche-research CLAUDE.md) before writing `voice-samples.md`.

---

## 3. Excerpts file

**What's there** (`PS/references/excerpts.md`, about 11,300 words): 16 groups of verbatim lines by job (the point in the first sentence, opening questions, villain lines, scope, promises, priority flags, item lines, mechanism, home checks, money, honest limits, safety, call-a-pro, forward lines, CTAs, comment questions), about 200 quotes in all, with 11 marked **Problem:**. Sources: 60 plumbing-study transcripts (Silver Cymbal 32 lines, TheCheapFix 30, Got2Learn 29, The Vintage Pipefitter 28, Mark Silverbridge 23, Roger Wakefield 23, Roger the Pipe Guy 21, Arrow Pest Service 18).

**Plumbing-only:** almost every quote's content (p-traps, flappers, sediment, solder, sewer gas, the main line). Group 8 (mechanism), group 9 (home checks), group 13 (call-a-pro: "two drains at once is the main line") and the money lines in group 10 are all plumbing facts. Only 3 lines are HVAC already (group 13 #7, group 15 #2, group 10 #9, all from S18).

**Topic-free, can carry:** the intro text (tags, how to use it, what to leave behind), each group's "Shape:" notes, and the CTA and comment-question groups (15, 16), whose wording is about the viewer, not the pipe.

**What an HVAC version needs:** the same 16 groups filled from HVAC transcripts. That means pulling roughly 20-30 HVAC transcripts first (the real channels in 1c and 2, plus Ray's top 5 and the brand verdicts as structure only). Add two groups plumbing doesn't need: **season and clock lines** (the first cold night, the after-hours call) and **CO and gas safety lines said in proportion**, since CONCLUSIONS §2 finds safety fear a weak lead (0.94x). The pack can ship without it at first (the electrical branch's `electrical-scripts/references/` has no excerpts file), but then the writer has no HVAC lines to shape from.

---

## 4. Price guide

**Plumbing's sections** (`PS/references/price-guide.md`, 136 rows: 83 confirmed, 29 adjusted, 10 thin, 14 in words):

| Section | Rows | Carries to HVAC as-is |
|---|---|---|
| 1. Calling a plumber | 6 | none: the HVAC service call differs ($75-$200 vs plumber $50-$250); "checking a license" can be adapted in words |
| 2. Drains and sewer | 17 | none |
| 3. Toilets | 9 | none |
| 4. Water heaters | 14 | none |
| 5. Gas | 3 | "gas leak repaired" (in words) partly |
| 6. Pipes, valves and leaks | 33 | frozen pipe, burst pipe (#1 item 9, #16), leak alarm (under a furnace or AC pan) |
| 7. Damage | 11 | all 11 as-is (condensate overflow, #5, #6, #8; "THOUSANDS" in #8 rests on them), incl. the $15,000 average claim (can cite) |
| 8. DIY shelf | 25 | white vinegar, 3% peroxide, baking soda, small wet-dry vac, silicone caulk |
| 9. Facts | 18 | the **gas-leak row** as-is (mandatory every-step rule, `PS/SKILL.md` "Safety"); the rest are water-heater and water facts |

So about 21 of 136 rows carry. Note one clash: the brief's caulk is "$5-$10 a tube" (#12), and the guide's silicone caulk is "$9-$12". The brief wins.

**Seed list: every price and safety fact in the 16 briefs** (`HV/ideation/batch1-briefs-2026-10-26.tsv`) **and CONCLUSIONS §6.7/§6.8.** These were checked once by the batch-1 fact-checker (`HV/log.md` line 92), not yet two-source.

| Item | Figure as written | From |
|---|---|---|
| Service call / no-heat visit | $75-$200 | #2, #4, #10; §6.7 |
| Emergency / night or weekend visit | $250-$400 or more | #2, #10; §6.7 |
| Yearly inspection / tune-up | $80-$250 | #2, #10; §6.7 |
| 1-inch filter, plain | $5-$15 | #2, #4 |
| Pleated MERV 8 | about $5-$8 each in a multipack | #3, #9, #10 |
| Dense 1-inch MERV 11-13 / "allergen" | $20-$35 | #3 |
| Fiberglass filter | about $1-$3 (MERV 1-4) | #3, #9 |
| Washable / electrostatic | $20-$50 once | #9 |
| 4-5 inch media filter | about $25-$60, lasts 6-12 months | #3 |
| HEPA room purifier | $100-$250 | #3, #9 |
| Dense filter airflow loss | roughly 7-11% on PSC blowers (studies) | #3 |
| EPA filter advice | MERV 13 or as high as the system can handle | #3, #9 |
| Filter change | 1-inch every 1-3 months, monthly with pets | #3, #9 |
| Blower motor | $300-$1,100 installed; ECM $600-$1,500+ | #1, #3, #9; §6.7 |
| Flame sensor part | $10-$25 | #4, #14 |
| Flame sensor job | $100-$250; $300 or more after hours | #4, #14; §6.7 |
| Hot-surface igniter | part $20-$60; $120-$350 installed | #4; §6.7 |
| Pressure switch | $175-$350 installed | #8; §6.7 |
| Clogged-condensate call | $150-$300 | #5, #6, #8 |
| Condensate pump | $150-$400 installed | #5, #6, #8; §6.7 |
| Condensing furnace output | a few gallons a day in cold weather; 90%+ AFUE, white PVC vents | #5, #6, #8 |
| Pro coil cleaning | $100-$200+ | #7 |
| Thermostat batteries | $5, every fall | #1 |
| C-wire adapter | $20-$30 | #1 |
| Supply vents open | at least 80-90% | #1 |
| DOE setback | 7-10°F for 8 hours a day saves as much as 10% a year; "working harder to recover" is a misconception | #1 |
| Ceiling fan | winter clockwise on low (DOE); about 1% a year per degree for 8 hours (keep soft) | #15 |
| Canned spray foam | about $5-$10 a can | #11, #12 |
| Rigid foam board | $20-$60 for a typical section | #11 |
| ENERGY STAR air sealing | average 15% on heating and cooling (about 11% of total) for the whole package | #11 |
| Door weatherstrip and sweep | $10-$25 a door | #12 |
| Outlet foam gaskets | $5 a pack | #12 |
| Caulk | $5-$10 a tube | #12 |
| Window film kit | $15-$25 for several windows | #12 |
| Attic hatch | $20-$50 DIY; stair cover $50-$150 | #12 |
| Chimney plug | $30-$80 | #12 |
| Whole-house insulation | "several thousand dollars" (in words) | #12 |
| Space heater draw | 1,500 W = about 12.5 A; a 15-amp circuit carries 12 A continuous (80% rule) | #13 |
| Light-duty cords | 16- and 18-gauge rated only 10-13 A | #13 |
| Space heater deaths | about one-third of home heating fires, 88% of heating fire deaths (NFPA, 2016-2020) | #13 |
| Furnace power need | about 300-800 W | #16 |
| Pure sine inverter | $100-$250 (1,000-1,500 W) | #16; §6.7 |
| Idling car fuel | roughly a quarter to half a gallon an hour | #16 |
| Furnace inlet / transfer switch | $200-$500 | #16; §6.7 |
| Portable / standby generator | $500-$1,500; $7,000-$15,000+ installed | #16 |
| **Safety (§6.8 and briefs)** | smell gas: leave, call the gas company from outside; CO alarm on every level and outside each sleeping area (CPSC), alarms last 5-10 years; never run a red-tagged furnace; refrigerant is licensed work; power off at the switch or disconnect, gas valve off for burner work; never bypass a limit or pressure switch; refill the trap, never pour into pressure-switch hoses or the inducer; never mix bleach and vinegar; combustion safety test before sealing near natural-draft appliances; damper only when cold, never on gas logs; space heater straight into the wall, 3 feet clear, UL/ETL/CSA; car or generator 20 feet from openings, never in a garage, never backfeed; 3 feet clear around the furnace; PVC vent ends 12 inches above the snow line | #2, #4-#8, #11-#14, #16; §6.8 |

**Still missing** for the 16 titles and the main lanes. All are **not found** in the research; no figures are given here:
- **Title figures without a row:** the "$5,000 insulation quote" (#12; the brief says only "several thousand"). The "$12 part" and "$300" (#14) and the "$20 leak" (#11) sit inside brief ranges but need their own rows.
- **Calling a tech:** HVAC hourly rate; the after-hours multiplier; HVAC permit; checking an HVAC license.
- **Parts and jobs:** capacitor (part and installed), contactor, inducer motor, control board, thermostat installed, a pro C-wire, heat exchanger replacement, refrigerant recharge per pound, duct cleaning, duct sealing, combustion safety test, energy audit.
- **Replacement quotes:** new furnace, new central AC, heat pump, mini-split installed (needed for the decision-versus and brand lanes and for "replacement quote" stakes).
- **Shelf:** dish soap, leak-check solution, fin comb, Scotch-Brite pad, CO alarm, foil tape.
- **Facts:** CO deaths a year (CPSC), AFUE and SEER2 basics, refrigerant phase-down (R-22, R-410A), and brand warranty and reliability sources for brand verdicts.

**How plumbing's guide was checked (copy this):** researched 2026-10-21 by four researchers, two or more independent publishers or retailers per figure, then re-checked job by job by four *other* researchers against publishers the first ones didn't use. Every row carries **confirmed / adjusted / thin / in words**, and "can cite" only where a named source may be said aloud. Rounded ranges, never cents. The full research is kept in `/home/user/script-system/studies/plumbing/price-research-2026-10/` (A-D jobs, research and verify files). Re-checked yearly. Electrical swapped this file for a no-money `facts-guide.md` with Source and Status columns. HVAC needs money (the plumbing model), with a facts section like electrical's for the safety rows.

---

## 5. Unit plan template

From `PS/references/unit-plan-template.md`:

| Field | Plumbing-specific? | HVAC needs |
|---|---|---|
| Video type "[one of the ten in SKILL.md]" | yes | the HVAC type list (1b), incl. brand verdict, product myth-bust, cheap fixes vs quote, doing-it-wrong, outage |
| Item shape "what's really happening in the pipe" (SKILL item shape step 2) | yes | "in the system" |
| EMOTION "disgust words on: [grease, gunk, hair, roots, tank items]" | yes | HVAC leads on distrust and self-reliance (E3 1.83x, E13 1.53x, CONCLUSIONS §2); swap for "distrust / self-reliance beats" and keep disgust for trap slime and dust-caked blowers only |
| Villain line "the trade's price or silence" | partly | add "the honest out: a tech you trust" (CONCLUSIONS §6.2) |
| MONEY | partly | add "title figure -> price-guide row" (the $5, $12, $300, $5,000) |
| SAFETY "defaults used where the brief is silent" | yes | the plumbing defaults (boiling water, dry washing soda) become the §6.8 list |
| CTAs "(Roger, Mark; none on Vintage)" | yes | Roger the HVAC Guy's profile; the book is not decided (CONCLUSIONS §7.4) and the collab credit is open (§7.2) |
| **new: SEASON** | n/a | heating or cooling, upload month, the cold-night or hot-day stake |
| **new: SYSTEM SCOPE** | n/a | who it applies to (condensing 90%+ vs 80% furnace, heat pump vs gas, single-stage vs variable-speed, natural-draft appliances) |
| **new: FIRST-PERSON ROUTINE** | n/a | #8 and #10 are Roger's own routine; say how the claims policy allows it ("persona narrative only", brief #8) |

---

## 6. Top risks in carrying the reference material over

1. **Plumbing facts leaking in.** The copy guard catches only 8-word runs. It won't stop a writer reusing a plumbing *fact or price* ("a drain call starts around $150", the main-line call-a-pro trigger) seen in SKILL.md, the excerpts or the models. Worse, if the plumbing price guide is copied, the scanner's D4 check ("every number traces to the brief + price guide") will pass plumbing numbers, and the two service-call figures conflict.
2. **The copy guard set.** The HVAC pack's `--refs` list must name its own files. If it keeps the plumbing excerpts in the guard but not in the pack (or the reverse), the guard either misses lines or flags harmless ones. If Ray Dutton's transcripts are added as models, they must be in the guard. Ray's own method was near-copying (`HV/ray-dutton-sources.md` §3), and Roger must stand apart from him (CONCLUSIONS §5).
3. **Models are nearly all plumbing.** Only 4 of 39 are HVAC or next to it. The no-repeat rule (no model reused within the last five scripts) will run dry fast on types with 1-2 HVAC models (brand verdict, decision versus, doing-it-wrong) unless the plumbing structure models stay in the library.
4. **Thin, unpulled HVAC voice.** No real HVAC voice transcript is on disk. The biggest real channel reads as a young man, and the older-tradesman register is unconfirmed for every candidate.
5. **Structure only, but AI-voiced.** All four HVAC transcripts on disk are AI-voiced (Ray, HVAC Exposed). S18 carries `[UNSAFE: banned]` passages (coil misting, disputed by technicians in the comments) that must keep their labels.
6. **Safety rules are plumbing.** The SKILL.md defaults and the voice-samples' "never claims a house" clash with HVAC needs: CO, gas, refrigerant and limit switches (§6.8), and the first-person routine titles (#8, #10).
7. **Footage-bound sources.** The real-person giants (WINNI 9.2M, Home RenoVision 5.8M, Technology Connections 71:11) are on-camera builds or essays. Their structure needs footage a faceless channel doesn't have, so their beat maps must mark what doesn't transfer.
8. **Title numbers without a row.** The $5,000 insulation quote has no figure, so the script must say it in words or the title changes.

---

## Self-check (5 rows re-opened against the source files)

| Row | Checked against | Result |
|---|---|---|
| `_g8gQ1gg1FM` 2,898,729 / 2024-02-15 / 5:34 | `HV/top-100.csv` row 89 | matches |
| `86S3ITbfzQY` 672,609 / 2026-05-25 / 8:12 (492 s) | `HV/data/raw/topvideos-exact-2026-10-26.json`; census row | matches |
| `Qx3cC1y23JY` 2,450,035 / 2025-10-25 / 7:08 (428 s) | `top-real-person-3y-2026-10-26.csv`; sweep length 428 | matches |
| `fHAlfm21vYw` 943,315 / 2026-09-14 / 14:42 | `HV/recent-winners.md` 90-day row 16 | matches |
| `sRvH-io-ZtA` 2,777,727 / 2022-09-15 / 8:25 | `topvideos-exact-2026-10-26.json` | matches |
