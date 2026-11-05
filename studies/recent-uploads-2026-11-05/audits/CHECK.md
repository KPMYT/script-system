# Check of the upload audits (2026-11-05)

A second helper's re-check of the five channel audits in this folder (Mark, Vintage, Werner, Scarlett, Diane) against the caption transcripts, the CSV tables and the rules they cite. The audits themselves were not edited. Roger's audit is checked separately (last heading).

**How it was checked (all on 2026-11-05, no web search):**
- **Quotes.** A script searched the transcript for every quoted line in each audit that carries a timestamp (Mark 147, Vintage 148, Werner 137, Scarlett 83, Diane 95), ignoring punctuation and line breaks, and compared the audit's time with the transcript line it sits in. Every hit that looked late or missing was then read by hand. The tables below show a hand-picked sample per channel, mostly the lines a rule break rests on.
- **Counts.** Caption words recomputed for every video in every CSV: timestamps stripped, whitespace-separated tokens counted. Words a minute = words / video length. Minutes at profile speed = words / (Mark 181, Vintage 190, Werner 181, Scarlett 169, Diane 172); the speeds were confirmed in each persona file and in `plumbing-scripts/SKILL.md` "Length".
- **First item and opening promises.** For every video, the first-item time was worked out from the transcript (the line's start time plus its share of the line's words) and the opening was read for promises.
- **Rules.** Each sampled rule break was checked against the text it cites: `plumbing-scripts/SKILL.md`, `style-scripts/SKILL.md` (and `references/hooks.md`), the persona files, `HANDOFF.md` §3 (2026-10-29 blocks), `PROPOSALS.md` P18, `core/retention-mechanics.md` §14, `core/greenlight-audit.md` B9, `core/humanizer.md` H21, `core/cta-and-endings.md` §3, the price guide and the book files.
- "Measured" means counted or read from a file here. "Reading" means my judgment.

**Across all five audits (measured):**
- **Quotes:** every timestamped quote was found in its transcript, and every timestamp sits within about 30 seconds of where the words are. The few apparent misses were quotes running across a line break, ranges ("[9:51]-[11:25]"), quotes from a sister video cited in another video's section (all found in that video), or the audit quoting a caption spelling differently ("I read every one" where the captions have "I read everyone"). **No misquote found.**
- **Counts:** no difference over 2% on any of the 24 videos. The only differences at all are Vintage `oJYnV-RePuU` (CSV 1,855, raw tokens 1,862), `ewBOEjJEzyY` (2,803 vs 2,804) and `o_4qckQjeYE` (2,023 vs 2,024). In `oJYnV-RePuU` the gap is exactly the caption sound labels (">> [sighs and gasps] >>" and "[clears throat]", 7 tokens), which the helper left out. Every 12-minute verdict is right.
- **First items:** every CSV first-item time is within 3 seconds of the transcript.

---

## Mark Silverbridge (`audits/mark.md`, `mark-table.csv`)

### Quotes (sample of 10; 147 checked in all)

| Item checked | Audit says | Source says | Result |
|---|---|---|---|
| Mid CTA after item 1 (eT) | "One aside before the faucets. If that soak just kept a toilet off your shopping list…" [4:11] | In the 4:11 line; my estimate 4:21 | OK |
| Kit named twice (uq3) | "A cup plunger for a sink. A flange plunger for a toilet. A plastic zip tool…" [12:01] | In the 12:01 line | OK |
| Priority flag (eT) | "If you take one thing from this video, take this. Get the water out first." [2:37] | In the 2:37 line; same flag found in 8y, uq3, qHBP, c4wk (fcwY has none) | OK |
| Bare myth flag (c4wk) | "Number two is the one people get backwards." [2:37] | In the 2:37 line | OK |
| Tool list in opening (qHBP) | "You can clear that yourself tonight with a plunger, a bucket, and a cheap plastic strip…" [0:00] | 0:00 line, second sentence | OK |
| "Crime" line (qHBP) | "…a plumber charges $150 to $300 to fit one. I think that is a crime for a part that size" [8:53] | In the 8:53 line | OK |
| Contraction (qHBP) | "If the water drops away with a gulp, you're done." [6:47] | Starts at the end of the 6:16 line, "you're done" in the 6:47 line | OK |
| Three promises (8y) | "The weekly dose has one step you cannot skip…" [0:30]; "An empty plastic bottle is the rescue…" [1:00]; "And the last piece is a 1-minute job…" [1:00] | All three in those lines | OK |
| Villain line (8y) | "nobody who gets paid for that visit is going to bring up a box of laundry soap." [0:00] | 0:00 line | OK |
| Promise block (fcwY) | "Number four takes about a minute… Number two is the one people get backwards… And the last two are the machines…" [0:31] | In the 0:33 line | OK |

### Counts (all six videos)

| Video | Words (CSV / recount) | Words a minute | Minutes at 181 | 12 min? | Result |
|---|---|---|---|---|---|
| eT-n10P6RsU | 2,301 / 2,301 | 180 / 179.8 | 12.7 / 12.71 | yes | OK |
| uq3Y59kTMRM | 2,492 / 2,492 | 184 / 183.9 | 13.8 / 13.77 | yes | OK |
| c4wkMyTOfUY | 1,918 / 1,918 | 185 / 185.0 | 10.6 / 10.60 | no | OK |
| qHBPo1Ct9Eg | 2,074 / 2,074 | 184 / 184.1 | 11.5 / 11.46 | no | OK |
| 8y-LYtHsvEI | 1,942 / 1,942 | 186 / 186.4 | 10.7 / 10.73 | no | OK |
| fcwYC9OKlCE | 2,674 / 2,674 | 182 / 181.7 | 14.8 / 14.77 | yes | OK |

### First item and opening promises (all six videos)

| Video | Audit: first item / promises | Transcript | Result |
|---|---|---|---|
| eT-n10P6RsU | 0:44 / 0 | "Number one, citric acid" at about 0:43. No promise. But the opening says "One for the ring in the crust, one for the scum, one for the stains", which tells what each powder does: borderline against "the count line never says what any single item holds" (reading) | partly |
| uq3Y59kTMRM | 0:45 / 0 | "Number one, the kitchen sink" at about 0:44; no promise | OK |
| c4wkMyTOfUY | 0:45 / 0 | "Number one, the toe touch" at about 0:45; no promise | OK |
| qHBPo1Ct9Eg | 1:53 / 1 borderline | "Step one, the slow sink" at about 1:53; "all three are in this video" is the one borderline line | OK |
| 8y-LYtHsvEI | 3:07 (dose) / 3 | "Here is the weekly dose" at about 3:07; three promises confirmed. But the fix itself (laundry powder in hot tap water, once a week) is named in the first sentence at 0:00, so "first item 187 s" is the helper's reading that the dose with amounts is the first real tip | partly |
| fcwYC9OKlCE | 0:58 / 3 | "Number one. The toilet" at about 0:59; three promises confirmed | OK |

### Rule breaks (sample of 6)

| Item checked | Audit says | Rule says | Result |
|---|---|---|---|
| Mid CTA before end of item 3 (eT) | breaks "never before the end of item 3" | Pack "CTAs" and Mark's profile "Style and length" both say "about a third of the way in, never before the end of item 3". The audit is also right that the two can't both hold on a 4-5 item list | OK |
| Kit named twice (uq3, qHBP) | breaks "the kit is named once in the whole video" | Pack "The opening": "No tool list in the opening, and the kit is named once in the whole video… never both and never twice"; HANDOFF 2026-10-29 | OK |
| Priority flag in the same words | breaks "in fresh words each time" | Pack "Point then promise": "A priority flag at the first answer, in fresh words each time" | OK |
| Bare myth flag (c4wk) | breaks the myth-flag rule | Pack "Ways to promise more value": "Never a bare 'the one everybody gets backwards'" | OK |
| Villain "nobody who gets paid for that visit / by the visit" (8y, fcwY) | joins pay to silence, a motive | The written test is "Never 'so', 'since' or 'because' between what the trade earns and what it doesn't say" and "not at motives". The line has no joining word and states no motive; reading it as an implied motive is fair, but it is the helper's reading, not the rule's words. The audit half-admits this ("No 'because', but…") yet counts it as a break | partly |
| Contraction (qHBP, 8y) | breaks the profile | Mark's profile: "no contractions anywhere in the script"; scanner ban | OK |

### Facts (2 flagged, 1 called fine)

| Item checked | Audit says | Source says | Result |
|---|---|---|---|
| "Scum is wax, so acid barely touches it" (eT) vs video 6 | video 6 uses vinegar on soap scum ("The vinegar loosens the minerals" [8:29]) | fcwY 8:29-9:00: "Warm some white vinegar… The vinegar loosens the minerals". The contradiction is measured; that acid does break soap scum is the helper's reading (general chemistry, not checked here) | OK |
| "15 to 20 firm strokes" vs the cited book page | book p. 42 says "Repeat 10-15 times" | `mark-silverbridge-book.md` line 1007, page 42: "Repeat 10–15" | OK |
| Called fine: book match "on page 36" (eT) | Fix #13, "The Weak Flush", page 36 | Book contents: "13. The Weak Flush | 36" | OK |

**Verdict:** reliable. Every quote and count checks out; the one soft spot is that two "breaks" (the "nobody who gets paid" line, and the dose as first item in 8y) are readings counted as rule breaks.

---

## The Vintage Pipefitter (`audits/vintage.md`, `vintage-table.csv`)

### Quotes (sample of 10; 148 checked in all)

| Item checked | Audit says | Source says | Result |
|---|---|---|---|
| Recap (8vTW) | "So here's the whole bill. Washing soda in the kitchen, borax in the bathroom…" [11:39] | In the 11:24 line | OK |
| Bare myth flag (8vTW) | "…the cheapest, and the one everybody gets backwards. Number four, baking soda." [10:10] | In the 9:51 line | OK |
| Anatomy before tip (ewBO) | "First, what you're dealing with under that sink." [0:53]; "The first reason it sticks is the gunk." [2:01] | 0:30 line; 1:33 line (my estimate 2:03) | OK |
| End promise (ewBO) | "So, both get fixed here." [0:33] | 0:30 line; push-button section starts in the 11:25 line | OK |
| No-plumber line (Ee36) | "None of this needs a plumber and it's all a weekend's work." [0:45] | 0:30 line | OK |
| Call point (Ee36) | "…shut the water off at the main and make the call." [8:52] | 8:23 line | OK |
| "Because" motive (7SnN) | "Nobody in the trade is going to explain how simple some of this is because every one of these jobs is a visit they get to bill for." [0:18] | 0:00 line | OK |
| Three promises (7SnN) | "Number three can get you a faucet part for free…" [0:48] | 0:32 line | OK |
| Two promises (oJYn) | "Step three is the soak… and step five comes with a check…" [0:35] | 0:30 line | OK |
| $13,000 total (o_4q) | "Now, add up the low end of every bill on this list, and it comes to more than $13,000." [10:38] | 10:22 line | OK |

### Counts (all seven videos)

| Video | Words (CSV / recount) | Words a minute | Minutes at 190 | 12 min? | Result |
|---|---|---|---|---|---|
| 8vTWjM60GRM | 2,544 / 2,544 | 202 / 201.9 | 13.4 / 13.39 | yes | OK |
| ewBOEjJEzyY | 2,803 / 2,804 | 195 / 195.2 | 14.8 / 14.76 | yes | OK |
| 7oNBRxJmjxE | 2,638 / 2,638 | 188 / 188.4 | 13.9 / 13.88 | yes | OK |
| Ee36yVgRJtY | 1,861 / 1,861 | 178 / 178.1 | 9.8 / 9.79 | no | OK |
| 7SnNq7RXa88 | 2,952 / 2,952 | 196 / 196.4 | 15.5 / 15.54 | yes | OK |
| oJYnV-RePuU | 1,855 / 1,862 (sound labels) | 183 / 184.1 | 9.8 / 9.80 | no | OK (0.4%) |
| o_4qckQjeYE | 2,023 / 2,024 | 182 / 181.8 | 10.6 / 10.65 | no | OK |

### First item and opening promises (all seven videos)

| Video | Audit: first item / promises | Transcript | Result |
|---|---|---|---|
| 8vTWjM60GRM | 0:44 / 0 | "Number one, washing soda" at about 0:45; count line only | OK |
| ewBOEjJEzyY | 2:01 / 1 (end-paid) | "The first reason it sticks" at about 2:03; one promise, paid in the last section | OK |
| 7oNBRxJmjxE | 0:45 / 0 | "Before any of that, find the shutoff" at about 0:46; escalation line only | OK |
| Ee36yVgRJtY | 1:01 / 3 | "Number one, how a pipe really bursts" at about 1:02; three promises | OK |
| 7SnNq7RXa88 | 1:03 / 3 | "Number one" at about 1:03; three promises | OK |
| oJYnV-RePuU | 0:45 / 2 | "Step one, dust it dry" at about 0:47; two promises | OK |
| o_4qckQjeYE | 0:55 / 3 | "Number one, grease" at about 0:57; three promises | OK |

### Rule breaks (sample of 6)

| Item checked | Audit says | Rule says | Result |
|---|---|---|---|
| No-plumber scope line (Ee36) | breaks job 4 and HANDOFF 2026-10-29 | Pack "The opening" job 4: "Never a blanket 'nothing here needs a plumber'… when the video has a point where the viewer stops and calls"; HANDOFF says the same | OK |
| "Because" motive (7SnN) | breaks the villain rule | Pack "The villain": "Never 'so', 'since' or 'because' between what the trade earns and what it doesn't say" | OK |
| Promise runs (Ee36, 7SnN, oJYn, o_4q) | break P18 | P18: "at most one promise beyond the count or escalation line, and only of what the end of the video pays… never two" | OK |
| Bare myth flag (8vTW) | breaks the myth-flag rule | Pack: "Never a bare 'the one everybody gets backwards'"; the script uses those very words | OK |
| Recap before the close (8vTW) | breaks "No recaps" | B9 and §14 do count a run-down anywhere. But the Mark audit left the very similar money run-backs in Mark's fcwY ("So, add it up. A toilet call, a greasy kitchen line…") and 8y "not counted". Same kind of line, two standards | partly |
| $13,000 total (o_4q) | breaks "Never: a total stated as certain when it depends on the viewer's house" | That rule is about savings that depend on the viewer's house. The real fault the helper found is arithmetic: the low ends said aloud are $150 + $300 + $2,000 + $10,000 = $12,450 (measured, confirmed). The fitting rules are "Proof": "Check the arithmetic", and D4 (every number traces). Right finding, wrong rule cited | partly |

### Facts (2 flagged, 1 called fine)

| Item checked | Audit says | Source says | Result |
|---|---|---|---|
| $13,000 total (o_4q) | low ends add to $12,450 | Dollar figures in the transcript: $150; $300 to over $1,000; $2,000 to $5,000; $10,000 and up. Low ends: $12,450 | OK |
| Flapper "$5 to $25" (7SnN) | guide says $4 to $10 | Price guide line 57: "Flapper | $4 to $10" | OK |
| Called fine: toilet-clog prices (7oNB) | "$100 to $275" with an auger and "$250 to $550" if the toilet comes off match the guide | Price guide line 34: "$100 to $275 with an auger; $250 to $550 if the toilet comes off" | OK |

**Verdict:** the most reliable of the five. Quotes, counts, times and promise counts are all right; the only weak points are one rule mis-cited for the $13,000 total and a recap standard that differs from the Mark audit.

---

## Werner Finkbeiner (`audits/werner.md`, `werner-table.csv`)

### Quotes (sample of 9; 137 checked in all)

| Item checked | Audit says | Source says | Result |
|---|---|---|---|
| Contraction (QLNO) | "If you use something that's strong, wear gloves…" [7:25] | In that line | OK |
| Installer claim (0r9) | "10 flushes is the check the installer bills for and rarely does…" [11:12] | In that line | OK |
| Step order (0r9) | step 11 "One end to the shutoff, one end to the tank." [9:20]; "Step 12. If yours is a two-piece toilet, the tank goes on now." [9:54] | 9:20 line and 9:51 line, in that order | OK |
| Item one late (u8g) | "Number one, the toe touch." [2:04] | About 2:04 | OK |
| Two personal details (u8g) | "In Germany, we call this Wartung…" [3:22]; "I keep a tin on the shelf for screws like these…" [7:27] | Both found; no other video has two | OK |
| Two figures in opening (XQ) | "about $5" [0:00]; "The visit runs about $100" [0:25] | 0:00 line | OK |
| Book chapter (XQ) | "Chapter 3 covers the things that stick." [6:20] | 6:09 line | OK |
| Dose three ways (U-a) | "half a cup" [3:58]; "a spoonful of powder" [4:22]; "a cup of the powder" [4:26] | All three found in order | OK |
| Same comment question (U-a vs 10-28) | "Tell me which level your toilet was at…" (10-28) | `recent-uploads-2026-10-29/transcripts/werner-kZ09VQIqAS4.txt` 10:57 line | OK |

### Counts (all five videos)

| Video | Words (CSV / recount) | Words a minute | Minutes at 181 | 12 min? | Result |
|---|---|---|---|---|---|
| QLNO-HgIcHo | 2,213 / 2,213 | 169 / 168.7 | 12.2 / 12.23 | yes | OK |
| 0r9P7Wd5FWk | 2,295 / 2,295 | 170 / 170.0 | 12.7 / 12.68 | yes | OK |
| u8gZHowqGnk | 2,279 / 2,279 | 165 / 165.1 | 12.6 / 12.59 | yes | OK |
| XQ_VHuIc2eQ | 2,549 / 2,549 | 166 / 165.5 | 14.1 / 14.08 | yes | OK |
| U-a-ygRV4Fo | 2,030 / 2,030 | 185 / 185.1 | 11.2 / 11.22 | no | OK |

### First item and opening promises (all five videos)

| Video | Audit: first item / promises | Transcript | Result |
|---|---|---|---|
| QLNO-HgIcHo | 0:49 / 0 | "Step one. Dust the toilet" at about 0:50; count line only | OK |
| 0r9P7Wd5FWk | 0:46 / 1 (end-paid) | "Step one. The water goes off" at about 0:46; one promise ("the four signs… come at the end"), paid at 12:32 | OK |
| u8gZHowqGnk | 2:04 (type check 0:51) / 1 (end-paid) | "So, which stopper" at about 0:52; "Number one" at about 2:04; one end promise at about 0:46 | OK |
| XQ_VHuIc2eQ | 0:46 / 0 | "Number one, hair" at about 0:45; count line only | OK |
| U-a-ygRV4Fo | 1:02 / 0 | "Level one" at about 1:02. Counted 0, but "And you will know yours by the water." is in the opening; the audit discusses it as a judged borderline (the scanner flags it); the CSV shows a plain 0 | partly |

### Rule breaks (sample of 6)

| Item checked | Audit says | Rule says | Result |
|---|---|---|---|
| Contraction (QLNO, U-a) | breaks the profile | Werner's profile: "Contractions: none"; scanner ban | OK |
| Two personal details (u8g) | at most one per script | Profile: "at most one per script outside the CTA"; the German background is listed as one ("the way we do it in Germany") and the screw tin as another | OK |
| Two dollar figures in the opening; four in one item (XQ) | break the number cap | Pack: "One dollar figure at most in the opening"; "at most one dollar figure per item", three side by side as the exception | OK |
| Book chapter (XQ) | chapter 3 has no stoppers; a false offer claim | Book file: chapter 3 is repairs 12-19 (hinges, doors, windows, drawers, locks…); plumbing match table sends drains to chapter 6. `cta-and-endings.md` §3: "A page that doesn't cover what the script says it covers is a false claim". The sentence is literally true of chapter 3 but points the viewer at the wrong chapter | OK |
| Installer claims (0r9) | break the villain rule | Pack's villain rule is about price, silence and motives; "bills for and rarely does" is a claim about practice, not a motive. The closest written rule is "Proof: Never… Sweeping claims nobody can check", which the audit also cites. Fair, but a judgment | partly |
| Same comment question (u8g after XQ) | "never the same question two videos running" | The questions differ (a tub's six stoppers and baths sat in, against a sink's lift rod or push button and years sticking). Same shape, not the same question. U-a's repeat of 10-28 ("which level…, and whether…") is closer to the same question | partly |

### Facts (2 flagged, 1 called fine)

| Item checked | Audit says | Source says | Result |
|---|---|---|---|
| Supply line before the tank (0r9) | step-order mistake | Step 11 connects "one end to the tank"; step 12 then fits the tank on a two-piece toilet | OK |
| Washing-soda dose (U-a) | half a cup, a spoonful and a cup | All three in 3:58-4:26 | OK |
| Called fine: book match repair 49 (u8g) | "repair 49 in chapter 6" is right | Book: "49 | Break Up a Bathtub Drain Clogged With Soap Scum and Hair | 6" | OK |

(Also checked: the rocker-arm reading. Item four lengthens the rod for a plunger set too high [7:49]; item five says "Only this time a stopper that sits too high gets the rod lengthened" [9:08]. The quote is right; that the direction is backwards is correctly marked as the helper's reading.)

**Verdict:** reliable. Quotes, counts and facts all check out; two of its breaks (the installer lines and the u8g comment question) are judgments presented a little more firmly than the rule text supports.

---

## Scarlett Starling (`audits/scarlett.md`, `scarlett-table.csv`)

### Quotes (sample of 9; 83 checked in all)

| Item checked | Audit says | Source says | Result |
|---|---|---|---|
| Hook (Jgp7) | "Forgive me, but the granny cut adds years to a face." … "Number one, the textured pixie." 40 words [0:00-0:18] | 40 words before "Number one", which falls at about 0:18 | OK |
| Mid CTA (Jgp7) | "…And one chapter holds 10 nocost quick wins…" [4:28-5:05], 97 words | 97 words from "While those words" to "on screen." | OK |
| Closing run-back (Jgp7) | "So the words for the chair come down to the same few… soft movement, face framing, no blunt perimeter, and point cut ends." [14:49] | In the 14:3x-15:07 lines | OK |
| Reframe (Jgp7) | "That cut wasn't wrong for you. It was wrong for hair that has gone finer…" [3:16] | Found | OK |
| Leggings ending (XaSc) | "Four pairs cover everything in this video…" [14:46-15:35] | Found | OK |
| Poster line (XaSc) | "Comfort you can see is frumpy. Comfort you can't see is polished." [9:29] | Found | OK |
| Mid CTA (4kVa) | "It opens with one rule worth the whole book, the fit-first rule…" [4:04-4:41], 108 words | 108 words from "A quick word" to "on the screen." | OK |
| Item seven tail (4kVa) | "Two last habits go with this… A full-length mirror in daylight tells you the truth." [12:26] | Found | OK |
| Captions stop (Jgp7) | "Is it the one you've worn the longest, or did you change it at" [15:38] | Last line of the transcript | OK |

### Counts (all three videos)

| Video | Words (CSV / recount) | Words a minute | Minutes at 169 | 12 min? | Result |
|---|---|---|---|---|---|
| Jgp7nzZpN9k | 2,394 / 2,394 | 153 / 152.6 | 14.2 / 14.17 | yes | OK |
| XaSctY7Qeyc | 2,752 / 2,752 | 173 / 172.7 | 16.3 / 16.28 | yes | OK |
| 4kVamjO4Y4U | 2,218 / 2,218 | 166 / 165.7 | 13.1 / 13.12 | yes | OK |

### First item and opening promises (all three videos)

| Video | Audit: first item / promises | Transcript | Result |
|---|---|---|---|
| Jgp7nzZpN9k | 0:18 / 0 | "Number one" at about 0:18 (word 40); count line only | OK |
| XaSctY7Qeyc | 0:33 / 1 | "Rule one" at about 0:32 (word 100). The 1 is "I'll build seven outfits you can copy piece by piece"; the audit's text says this "reads as part of the count line", so the CSV's 1 and the text disagree. Reading: M30's own hook has a two-part count ("five different types of scarves with at least two or three ways to wear each one"), so counting it as part of the count line is defensible | partly |
| 4kVamjO4Y4U | 0:37 / 1 | "Number one" at about 0:37 (word 104); the 1 is "This video is about why, and it's fixable." | OK |

### Rule breaks (sample of 6)

| Item checked | Audit says | Rule says | Result |
|---|---|---|---|
| Mid CTA too long (Jgp7 97, 4kVa 108) | 60-90 words | Pack "CTAs": "in about 60 to 90 words"; the profile says the same. Note: the audit's word counts leave out the return line, which the pack lists as part 6 of the CTA. With it: Jgp7 104, 4kVa 111, and the leggings CTA (called fine at 82) is 94 | OK (method note) |
| Closing run-back (Jgp7) | §14, B9, "No recaps" | §14: a closing list "that runs back over what earlier sections already said is a recap, however it is phrased"; B9 the same | OK |
| More than one reframe | H21, at most one | `core/humanizer.md` H21: "At most one per script"; pack Emotion rule 5: the blame move "counts as the script's one reframe" | OK |
| Poster line (XaSc) | pack "Voice" | Pack "Voice": "Plain over clever. No poster lines" | OK |
| "It opens with… the fit-first rule" (4kVa) | the book claim isn't supported | Book file: the frameworks are "introduced on p. 13" (the introduction); "The Tailor's Secret" is chapter 2, pp. 50-82, starting at Way 11, "Hem Your Trousers to Break Once, Softly" | OK |
| **Missed: checks announced (XaSc, 4kVa)** | the audit lists the checks under "What works" as "given plainly" | Pack item shape, step 5: "Give it plainly; never announce it ('Here's the check')". The transcripts announce them: leggings "The check is simple." (about 1:16), "Now, the bend test." (about 2:27, quoted by the audit itself as good), "The check is a photo." (about 5:42); elegant women "The check is easy." (about 1:53), "The check is a phone photo." (about 3:41), "Then, the check is on the bed." (about 5:56). The Diane audit counts exactly these lines as a break | **wrong** |

### Facts (2 flagged, 1 called fine)

| Item checked | Audit says | Source says | Result |
|---|---|---|---|
| "Every cut in this video… are in" the book (Jgp7) | the index has the bob, pixie and length only | Book chapter 19, Ways 197-207: layered bob, textured pixie, length with movement, face shape, color, dimension, gray, roots, blow-dry, trims, products. No shag, stacked bob, lob or side-swept bang | OK |
| Fit-First rule placement (4kVa) | introduced on p. 13, not the chapter's opening | Book file line 55 and the chapter table | OK |
| Called fine: leggings checks "given plainly" | fine | Announced three times (see above) | **wrong** |
| Called fine (second): Way 105 match "word for word" (XaSc) | exact | Book: "105 | Fit the Waistband to Sit Without a Gap or a Dig | 372 | 10" (chapter 10, The Pants Vocabulary) | OK |

**Verdict:** quotes, counts and book checks are accurate, but the audit missed a rule the Diane audit applies: announced checks in two of three videos (three each), and praised one of them. Its rule-break counts for those two videos are one short each.

---

## Diane de Chambray (`audits/diane.md`, `diane-table.csv`)

### Quotes (sample of 9; 95 checked in all)

| Item checked | Audit says | Source says | Result |
|---|---|---|---|
| Makeup item (2IYX) | "Number seven, the eyes, the caterpillar false lashes and the hard black liner." [9:23] | Found | OK |
| "Most" on a shoe (2IYX) | "Ballet flats and loafers are the two you'll find most often on French women" [11:08] | Found | OK |
| Second count (YCdL) | "…look instantly younger and three that do the opposite." [0:23] | End of the 0:00 line | OK |
| Checks announced (YCdL) | "Your check is a photo at the window…" [2:05]; "Then the check, which is the easiest one…" [3:14]; "Your check is the window again." [5:53]; "And your check is a photo from the side…" [10:40] | All four found | OK |
| CTA (YCdL) | 104 words [3:33-4:09] | 104 words from "Let me stop" to "on the screen." | OK |
| Makeup item (aJlp) | "Number eight, heavy full coverage makeup and the frosted lid." [12:05] | Found | OK |
| Checks announced (aJlp) | "Here's what to check before you buy." [1:22]; "The check is easy." [5:08]; "The check before you leave the house is to count one accent." [10:12] | All found | OK |
| Run-down (aJlp) | "Everything on this list comes down to one habit…" [14:36] | Found | OK |
| Repeats #1 (aJlp) | "Structured just means it holds its shape when it's empty" (#1 [7:13]) | In #1 at about 7:28 (15 s off, within tolerance) | OK |

### Counts (all three videos)

| Video | Words (CSV / recount) | Words a minute | Minutes at 172 | 12 min? | Result |
|---|---|---|---|---|---|
| 2IYXD6OaV8I | 2,363 / 2,363 | 164 / 164.1 | 13.7 / 13.74 | yes | OK |
| YCdL6Zbxfps | 2,158 / 2,158 | 169 / 168.8 | 12.5 / 12.55 | yes | OK |
| aJlpJC2qB2w | 2,630 / 2,630 | 170 / 170.0 | 15.3 / 15.29 | yes | OK |

### First item and opening promises (all three videos)

| Video | Audit: first item / promises | Transcript | Result |
|---|---|---|---|
| 2IYXD6OaV8I | 0:26 / 1 | "Number one" at about 0:26 (word 73). The 1 is the count line itself | OK, but see note |
| YCdL6Zbxfps | 0:31 / 2 | "Color number one" at about 0:31 (word 82). The 2 is the count line plus "three that do the opposite" | OK, but see note |
| aJlpJC2qB2w | 0:25 / 1 | "Well, number one" at about 0:27 (word 70). The 1 is the count line | OK, but see note |

Note: this CSV counts the count line as a promise. The other five CSVs (and Scarlett's) count promises **beyond** the count line. On their basis Diane's column would read 0, 1, 0. The CSVs can't be compared as they stand.

### Rule breaks (sample of 6)

| Item checked | Audit says | Rule says | Result |
|---|---|---|---|
| Makeup item (2IYX, aJlp) | the pack is hair and fashion | Pack description: "Not makeup or skincare (a later pack)"; "Inputs": a whole-look title "may keep one short face paragraph… with no products and no results". A whole numbered item (172 and 211 words) is more than one short paragraph. ("No products" more likely means no named products; mascara and liner are generic, but the item still breaks the "short paragraph" limit) | OK |
| "Most" on a specific shoe (2IYX) | borderline | Diane's profile, French-way rule 1: "a specific piece, shoe or color takes 'plenty of', 'many' or 'you'll often see'" (written after "most women wear ballet flats"). Correctly marked borderline | OK |
| Checks announced (YCdL, aJlp) | item shape step 5 | Pack: "Give it plainly; never announce it ('Here's the check')"; HANDOFF 2026-10-29 fix 7 | OK |
| CTA 104 words (YCdL) | over 60-90 | Pack "CTAs": about 60 to 90 words | OK |
| Run-down before the book line (aJlp) | §14, B9, no recaps | B9: "recaps anywhere in the script (a run-down of what was just built counts…)" | OK |
| Second promise in the hook (YCdL) | "Never in the hook: … a second promise"; "Don't add moves" | Both rules exist. But the extra is inside the one count sentence, and M27, the hook model the audit names, has a single promise move that itself lists several outcomes. The firm fault is that the "three that do the opposite" are never counted out, so the viewer can't tell when they're paid. Scarlett's leggings hook ("five rules… seven outfits") was not counted as a second promise; the two audits treat the same move differently | partly |

### Facts (2 flagged, 1 called fine)

| Item checked | Audit says | Source says | Result |
|---|---|---|---|
| CTA book match (YCdL) | Secret 63 in "Hair, Skin, and the Details…"; the Color Compass "five to seven colors" | Book: chapter 7, "Hair, Skin, and the Details No One Talks About But Everyone Notices" holds Secrets 62-71; "63 | Choose a Hair Color That Lights Your Eyes…"; the Color Compass "five to seven colors" on p. 8; "ten teaching chapters" | OK |
| CTA facts (aJlp) | climate chapter, Capsule Rule five to eight | Book: chapter 9, "Dressing for the Life You Have Now: Occasion, Climate, and Context"; Capsule Rule "no more than five to eight" | OK |
| Called fine: #1 checks "given plainly, never announced" | fine | No "the check is / your check is / here's the check" in 2IYX | OK |

(Also checked: "instantly" said 4 times in YCdL. The transcript has "instantly" three times and "instant" once, which the scanner's "instant" stem counts: right.)

**Verdict:** reliable. Quotes, counts, book facts and first-item times are right; fix the promise column's definition and soften one break (the second count in YCdL) to match how the Scarlett audit treats the same move.

---

## Corrections needed

1. **Scarlett audit: add a missed rule break in two videos.** The leggings video (`XaSctY7Qeyc`) and the elegant-women video (`4kVamjO4Y4U`) each announce the check three times ("The check is simple", "Now, the bend test", "The check is a photo"; "The check is easy", "The check is a phone photo", "the check is on the bed"). The pack says never announce it. The audit praises these lines as "given plainly"; that should go. CSV rule_breaks_count: 2 to 3 and 3 to 4. The channel pattern then matches Diane's ("checks announced").
2. **Diane CSV: the opening_promises column counts the count line;** the other CSVs count promises beyond it. Change it to 0, 1, 0, or say in the header what is counted.
3. **Diane `YCdL6Zbxfps`, break 1:** reword it as "the 'three that do the opposite' are promised but never counted out". It is one count sentence, as in the hook model M27. Treat Scarlett's leggings "five rules… seven outfits" the same way, whichever way that goes.
4. **Scarlett CSV, leggings:** opening_promises says 1, but the audit's text says the line is part of the count line. Make them agree.
5. **Vintage `o_4qckQjeYE`, the $13,000 total:** the finding is right ($12,450 measured), but cite "Proof: check the arithmetic" and D4, not "a total stated as certain when it depends on the viewer's house".
6. **Recaps: one standard across audits.** Vintage counts 8vTW's "So here's the whole bill…" as a break. The Mark audit leaves the similar closing run-backs in fcwY ("So, add it up…") and 8y ("A strainer at $2 to $10, a zip tool…") "not counted". B9 counts recaps anywhere. Either count all three or none.
7. **Mark, the "nobody who gets paid for that visit / by the visit" lines (8y, fcwY):** label them as a reading. The written rule bans "so/since/because" joins and motives, and neither is in the line.
8. **Mark `8y-LYtHsvEI`, first item 187 s:** note that the fix itself is named at 0:00, and 3:07 is the first dose with amounts (the helper's reading of "first real tip").
9. **Mark `eT-n10P6RsU` opening:** "One for the ring in the crust, one for the scum, one for the stains" says what each item does. It is borderline against the count-line rule and isn't mentioned; add it as a borderline.
10. **Werner `0r9P7Wd5FWk`, installer lines:** rest the break on "Proof: sweeping claims nobody can check", not on the villain/motive rule, and mark it as a judgment.
11. **Werner `u8gZHowqGnk`, comment question:** it is the same shape as the video before, not the same question. Downgrade it to a reading, or say "same shape".
12. **Werner `U-a-ygRV4Fo` CSV:** opening_promises 0 should note the judged borderline "And you will know yours by the water" (the scanner flags it).
13. **Style CTA word counts leave out the return line,** which the pack counts as part of the CTA. Say so in the audits. With the return line, the Scarlett leggings CTA is 94 words, just over "about 60 to 90".
14. **Method note only, no change:** Vintage `oJYnV-RePuU`'s 1,855 words leaves out caption sound labels (raw tokens 1,862, 0.4%). Every other count matches within 0.1%.

## Roger the Pipe Guy

Checked separately: see `CHECK-roger.md`.
