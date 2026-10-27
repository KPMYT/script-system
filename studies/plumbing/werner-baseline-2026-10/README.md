# Werner Finkbeiner: baseline of the 14 pre-library scripts (2026-10)

This folder is research data. It holds the 14 scripts written for the Werner Finkbeiner channel before the script library existed, as they stand in Google Drive, along with descriptive counts and the library scanner's findings on each. It collects and describes only. Nothing here is a rule, a target or a conclusion, and none of it is edited to fit one.

**The channel.** Werner Finkbeiner, YouTube channel id `UCreWf0tHuPS82aG596yD5nA`, handle `@WernerFinkbeiner-c8z`. It had 11 subscribers on 2026-10-27. Its description begins: "I'm Werner Finkbeiner. I grew up in Germany, where water and heating cost real money and you fix things before you replace them." The operator stopped the channel on 2026-10-22 and is now relaunching it. These 14 videos are everything published before the stop, and this folder is the "before" picture for the relaunch.

## Where each piece came from

- **Script text:** one Google Doc per video, read on 2026-10-27 with the Google Drive connector (`read_file_content`). Each doc is the script as written for that video, with voice tags such as `[warm]` (from #9 onward) and `===START CTA(...)===` / `===END CTA===` markers. All 14 docs were fetched; none failed. Every doc's Drive title is "Untitled document", so the titles below come from YouTube.
- **Video facts** (title, YouTube id, published date, length, views): YouTube via NexLev, as of 2026-10-27, supplied with the task.
- **Counts** (`counts.md`) and **scanner results** (`scanner.md`): computed on 2026-10-27 from the saved scripts, by a throwaway script run outside the repo. Each file says exactly how.

## Caveat: the doc may differ from what was voiced

Each doc is the script as written. The voiceover may have been edited, cut, re-recorded or ad-libbed, and the published video may add or drop lines. Nothing in this folder was checked against the audio or the YouTube transcript. Word counts and words-per-minute figures describe the doc against the video's length, which also includes any non-narrated time, so treat WPM as an estimate.

## How the scripts are saved

`scripts/NN-short-slug.md`, numbered in publication order (the NEW # below). Each file starts with a 4-line header (title; Drive doc id; YouTube video id; published date, length and views on 2026-10-27), then a blank line, then the doc text **verbatim, exactly as the Drive connector returned it**. The text was copied by a script straight from the connector's response, not retyped. Nothing was unescaped or tidied:

- The connector returns the docs as Markdown with escapes, and these are **kept as returned**: voice tags appear as `\[warm\]` and markers as `\===START CTA(Werner's 101 Free Repairs)===`. Read `\[`, `\]` and `\=` as `[`, `]` and `=`. These are the only escapes in the 14 files.
- Trailing double spaces (Markdown hard line breaks), blank spacer lines and leading spaces are as returned.
- For counting and scanning, the escapes were undone in scratch copies only (see `counts.md` and `scanner.md`). The saved files were not changed.

Format differences between the docs, as they come:

- **#1–#3** mark only the mid-video CTA. Their closing book-and-subscribe paragraph is unmarked.
- **#4–#14** mark both CTAs.
- **#1–#8** have no voice tags. **#9–#14** have 25 to 30 each.

## The 14 videos

| NEW # | Title | Drive doc id | YouTube id | Published | Length | Views (2026-10-27) | File |
|---|---|---|---|---|---|---|---|
| 1 | Pour this $1 German Liquid in Your Toilet Bowl and Watch What Happens (6 Genius Uses) | 1ZF3F-_SNWBJorNlUouzmysrb3jpu8WKR3UMHoX_ARek | hVJH8vnppmc | 2026-09-27 | 17:44 | 171 | `scripts/01-essigessenz-toilet-6-uses.md` |
| 2 | 10 Things German Households NEVER Pour Down the Drain (Americans Do Most of Them Weekly) | 1j8JmPCAZifQLVKKSHw1j9wtEId2qZASHbVMeXomKnUo | Xs_ZJgAdluQ | 2026-09-27 | 12:58 | 40 | `scripts/02-10-never-down-drain.md` |
| 3 | In 30 Years as a German Plumber, I've Never Had a Clogged Drain — Here's Exactly What I Do | 1lF8H_6dzKbz4-PsWq9l7J1DE1xj6oBMWH0tr1Pqs7W0 | pgk-dAod0Hc | 2026-09-27 | 21:24 | 154 | `scripts/03-30-years-never-clogged-drain.md` |
| 4 | This Is How We Cool Our House Without AC (The German Way) | 1szLPzIDdRrUBnzUrSiSNUE196HrURD8ZfTa1YDlZo94 | o8ZfFH7x-20 | 2026-09-27 | 15:51 | 178 | `scripts/04-cool-house-without-ac.md` |
| 5 | 20 German Plumbing RULES That Will Save You THOUSANDS (Americans Break Most of Them) | 161OXnGpLwxXxXzWqplVvR37POPHh30fLQnvtk8OYtdY | YsfRE_O0M-c | 2026-09-27 | 19:35 | 92 | `scripts/05-20-plumbing-rules.md` |
| 6 | Germans Use Less Than HALF the Water Americans Do — 12 Habits That Cut Your Bill | 1KA0Co_JsorwLSLsH6VCdfEo7Knl9QvXsPgwG9nrLqs8 | 38ACMLTg3es | 2026-09-29 | 24:32 | 40 | `scripts/06-12-water-habits.md` |
| 7 | How Germans Remove Limescale From EVERYTHING — The $3 Powder in Every German Kitchen | 1Sqifj_-V_xaAAgUqP0-Zq-DJQFfKMsxZODkwikls9Fk | osldv09jkeY | 2026-10-06 | 23:00 | 102 | `scripts/07-limescale-citric-acid.md` |
| 8 | 10 German Heating RULES Americans Break — That Cost You Hundreds Every Winter | 1c10rwcs7mpKmBpG4AqJAgrMISl7tbd-MVSkYoYzfqKc | dkNbxjwFoRg | 2026-10-06 | 25:36 | 241 | `scripts/08-10-heating-rules.md` |
| 9 | How Germans Keep Mold Out of the House FOREVER — The 5-Minute Habit Americans Never Learned | 10N_gnlUQ1lS-dOKw0Xolxe-arQ-bght8xn98K2BbNtY | pP5W9mrKg6Y | 2026-10-06 | 14:36 | 52 | `scripts/09-mold-5-minute-habit.md` |
| 10 | The Best Way to Clean Your Shower & Tub (The German Way) | 19N2_etOCwNiInYKsTU4XOjtKszkdN0hy-BEy3yiJuKE | qPzoEpqUhaQ | 2026-10-13 | 14:21 | 224 | `scripts/10-clean-shower-and-tub.md` |
| 11 | How to Unclog ANY Toilet Without a Plunger — The German Kitchen Trick That Works Every Time | 1X_Bft2KIwmoxJwj1WSW9H2A8Zsjs3j_yF8VyFzj6mpM | 339UAeV-1LU | 2026-10-13 | 15:55 | 1000 | `scripts/11-unclog-toilet-no-plunger.md` |
| 12 | Why Your Shower Drain KEEPS Clogging — It's Missing the $6 Part Every German Drain Has | 1WMUK7XZsD_dgC_p1GxlUY2P_yg8qyrWPIo1SvgG5ooY | RO3DF20poGk | 2026-10-13 | 15:15 | 185 | `scripts/12-shower-drain-6-dollar-part.md` |
| 13 | Running Toilet? The 10-Minute German Fix (NO New Parts, NO Plumber) | 1Uu6fUvE8wn2lTpm6xzA5gMZoFDXZnHQQzp8ahT_V03I | 5ILY4KofoY4 | 2026-10-13 | 15:58 | 256 | `scripts/13-running-toilet-10-minute-fix.md` |
| 14 | 9 Things German Households NEVER Flush — Americans Flush Most of Them Every Week | 1RLe2X1py4IpqMu9evwmPtpWTUD_Pv4oSgHyOkhIa_qk | DGv12bqyfJM | 2026-10-15 | 15:33 | 10 | `scripts/14-9-never-flush.md` |

## Files

| File | What it is |
|---|---|
| `README.md` | This file: what the folder is, sources, the table, caveats. |
| `scripts/` | The 14 scripts, verbatim from Drive, each with a 4-line header. |
| `counts.md` | Per-script measures (spoken words, estimated WPM, CTA lengths, "but", "you", questions, contractions, German words, "So." openers, dollar figures, tenure figures, and structural features such as name intro, teases, halfway checkpoint, recap, three-things assignment, sign-off, subscribe and comment asks), with medians, ranges and quoted evidence. |
| `scanner.md` | `core/script-scanner.py` run on each script with `--rules plumbing-scripts/SKILL.md` and the title: the verdict, counts per finding label, and quoted examples. |
