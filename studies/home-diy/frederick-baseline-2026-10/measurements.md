# Measurements (2026-10-22)

Regex counts from `measure.py`, approximate; voice tags and CTA markers removed before counting. "I-anecdotes" and "words_before_#1" are rough (the first catches only some phrasings; the second is the first "number …" phrase, which can sit in the hook). The hand-checked versions are in `analysis.md`.

Columns: voice tags = bracketed delivery tags ([quietly], [warm]…); min@165 = minutes at 165 words a minute; you/1k, I/1k, but/1k = per 1,000 words; ? = question marks; sent = mean sentence length in words; <=6w% = share of sentences of six words or fewer; digits = numbers written as digits; intro = "I'm Frederick Barnes," near the top; CTA words = mid / end; midCTA@% = where the mid CTA starts, as a share of the script; dread/1k = death, kill, trapped, smoke, flames, burn down, fatal, deadly; firefighter refs = "firefighter", "fire department", "fire marshal".

| script | voice tags | words | min@165 | you/1k | I/1k | I-anecdotes | ? | but/1k | sent | <=6w% | digits | intro | words_before_#1 | CTA words | midCTA@% | dread/1k | firefighter refs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NEW-01 | 0 | 3225 | 19.5 | 27.9 | 5.6 | 4 | 1 | 0.6 | 16.9 | 14 | 0 | True | 90 | 154/140 | 19 | 1.6 | 5 |
| NEW-02 | 0 | 3161 | 19.2 | 37.3 | 5.4 | 4 | 2 | 1.3 | 18.0 | 11 | 0 | True | 431 | 163/115 | 27 | 6.3 | 5 |
| NEW-03 | 0 | 2745 | 16.6 | 26.6 | 4.0 | 1 | 0 | 2.2 | 10.4 | 43 | 14 | True | None | 156/145 | 34 | 2.2 | 0 |
| NEW-04 | 0 | 3190 | 19.3 | 26.3 | 5.3 | 1 | 0 | 0.6 | 14.4 | 22 | 26 | True | None | 171/170 | 28 | 7.8 | 0 |
| NEW-05 | 0 | 3053 | 18.5 | 28.2 | 4.3 | 1 | 0 | 1.6 | 12.3 | 27 | 0 | True | None | 177/134 | 25 | 1.6 | 3 |
| NEW-06 | 0 | 4254 | 25.8 | 25.4 | 4.2 | 2 | 0 | 0.5 | 15.6 | 14 | 0 | True | 308 | 193/89 | 22 | 2.8 | 11 |
| NEW-07 | 31 | 3255 | 19.7 | 21.5 | 3.7 | 2 | 0 | 0.6 | 20.5 | 6 | 0 | True | 146 | 160/98 | 35 | 2.2 | 5 |
| NEW-08 | 28 | 3278 | 19.9 | 34.2 | 4.0 | 1 | 0 | 0.0 | 17.0 | 10 | 0 | True | 173 | 164/106 | 25 | 1.5 | 5 |
| NEW-09 | 0 | 3191 | 19.3 | 31.7 | 3.8 | 1 | 1 | 1.9 | 18.2 | 9 | 0 | True | None | 156/113 | 21 | 4.4 | 1 |
| NEW-10 | 29 | 3008 | 18.2 | 13.6 | 3.0 | 1 | 0 | 1.7 | 17.0 | 11 | 0 | True | 150 | 155/97 | 31 | 3.7 | 1 |
| NEW-11 | 29 | 3122 | 18.9 | 38.8 | 3.2 | 1 | 5 | 0.6 | 17.6 | 18 | 0 | True | 162 | 160/89 | 32 | 0.6 | 1 |
| NEW-12 | 29 | 2704 | 16.4 | 32.5 | 4.4 | 2 | 3 | 0.4 | 18.6 | 6 | 0 | True | 88 | 159/107 | 24 | 1.8 | 2 |
| NEW-13 | 18 | 2806 | 17.0 | 27.1 | 7.8 | 1 | 1 | 1.4 | 16.5 | 18 | 0 | True | 267 | 168/126 | 32 | 0.7 | 0 |
| NEW-14 | 22 | 2603 | 15.8 | 19.6 | 3.8 | 1 | 1 | 2.3 | 15.7 | 22 | 0 | True | 224 | 164/96 | 26 | 3.1 | 2 |
| NEW-15 | 24 | 2847 | 17.3 | 20.0 | 4.9 | 2 | 0 | 1.4 | 14.8 | 23 | 0 | True | 171 | 161/124 | 23 | 3.9 | 1 |
| NEW-16 | 25 | 2652 | 16.1 | 19.6 | 3.4 | 0 | 0 | 0.8 | 14.7 | 25 | 46 | True | 333 | 173/91 | 33 | 0.8 | 1 |
| NEW-17 | 26 | 2740 | 16.6 | 29.2 | 3.6 | 0 | 1 | 1.5 | 15.9 | 23 | 0 | True | 151 | 165/120 | 32 | 8.0 | 0 |
| NEW-18 | 27 | 2953 | 17.9 | 25.4 | 6.4 | 1 | 0 | 2.7 | 17.4 | 8 | 0 | True | None | 154/96 | 23 | 4.4 | 0 |
| NEW-19 | 31 | 2964 | 18.0 | 30.4 | 4.0 | 2 | 2 | 2.4 | 16.3 | 15 | 0 | True | 151 | 156/94 | 20 | 0.7 | 0 |
| NEW-20 | 35 | 3131 | 19.0 | 28.1 | 7.3 | 2 | 3 | 0.0 | 17.2 | 21 | 0 | True | 184 | 163/117 | 38 | 2.2 | 1 |
| NEW-21 | 29 | 3151 | 19.1 | 20.6 | 6.0 | 0 | 1 | 1.0 | 17.4 | 28 | 0 | True | 172 | 161/104 | 34 | 3.2 | 3 |
| NEW-22 | 30 | 3067 | 18.6 | 22.8 | 4.6 | 2 | 0 | 0.3 | 15.8 | 25 | 0 | True | 194 | 173/138 | 37 | 3.6 | 3 |
| NEW-23 | 30 | 3095 | 18.8 | 19.7 | 3.2 | 1 | 0 | 1.0 | 12.8 | 24 | 0 | True | 154 | 148/106 | 24 | 1.6 | 3 |

## Scanner (`scanner-output.txt`)

Fix on sight across the 23: curly quotes 906 and em dashes 65 (all in NEW 13 to NEW 23); hard-ban teases 5 ("by the end, you'll" in NEW 5, 6, 9; "by the end of this video" in NEW 10; "stay with me to the end" in NEW 17); "right here" once (NEW 12); "e-book" twice (NEW 12, 13). Judge-level: staccato runs 67, trailing "Not Y." beats 8.

Not caught by the scanner, found by reading: the name intro in all 23; bracketed voice tags in 16; "By the end of this one" (NEW 2) and "By the end of this you'll know" (NEW 4); the CTA "no rush" family (`core/cta-and-endings.md` §5) in 18 of 23.
