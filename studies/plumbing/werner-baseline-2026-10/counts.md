# Werner Finkbeiner baseline: counts

Computed 2026-10-27 by a throwaway Python script run with `python3 -I` from a scratch directory outside the repo (not kept in the repo). The input was the 14 saved scripts in `scripts/`, which are verbatim Drive text with the header removed. Descriptive only: no target or rule is implied.

## How each measure was taken

- **Spoken text:** the markdown escapes were undone (`\[`→`[`, `\]`→`]`, `\===`→`===`), then every `===START CTA(...)===` / `===END CTA===` line and every `[voice tag]` were removed. The CTA text itself stays in. **Words** = whitespace-separated tokens containing at least one letter or digit (so `$15`, `1,000` and `25%` are one word each, and a lone dash is not a word).
- **WPM** = spoken words ÷ the video's length in minutes. The length includes any non-narrated time (intro, B-roll pauses, end screen), so this is an estimate and a lower bound on the voice's real pace. The doc may also differ from what was voiced (see README).
- **Mid CTA / End CTA words** = words inside the first and the last marked CTA block. Scripts 1–3 mark only the mid CTA, so their **end CTA** is unmarked; there it is the last paragraph naming the book ("Free Repairs"), counted on its own (marked `*`). **Mid CTA at** = the share of spoken words that come before the mid CTA's START marker.
- **but / you per 1,000:** whole-word, case-insensitive. "you" counts only `you` (not your, yours).
- **?** = count of question marks in the spoken text.
- **Contractions per 1,000:** any word ending n't, 're, 've, 'll, 'd or 'm, plus it's, that's, there's, here's, what's and let's (straight or curly apostrophe). Possessives such as "Werner's" are not counted.
- **"So." openers** = `So.` followed by a space or line end (with a capital S it can only open a sentence). "So," openers are given too, for comparison.
- **Dollar figures:** `$`+digit tokens and the words "dollar"/"dollars" are counted separately, because the scripts use both styles ("$15 to $20", "150 and 350 dollars"). A range written in words is one "dollars" hit. Euro mentions are noted separately.
- **German words:** case-sensitive whole-word counts for Feierabend, Ordnung, Werkstatt, Handarbeit, Sparsamkeit, Wartung, Vorsorge, Pfusch, Werkzeug, Hausmittel, Essigessenz, Zitronensäure, Stoßlüften, Meister and Natron, plus the German words I spotted reading every script: Kalk, Rollladen, Wartungsfuge, Haarsieb and Soda (only where it is given as the German name; lower-case "soda" in "baking soda" is not counted). No script has an umlaut or ß anywhere. Werkstatt, Handarbeit, Werkzeug, Zitronensäure, Stoßlüften and Meister appear in none. #9 describes Stoßlüften ("in English it comes out as shock ventilation") without saying the word. Place names (Freiburg in #4) are not counted.
- **Years-of-experience figure:** searched for "N years as / in the / of" and for every "N years" phrase, then read each hit. **None of the 14 scripts states a tenure figure.** #3's title says "In 30 Years as a German Plumber", but the script never repeats it (it says "I have never had a clogged drain. Not in any kitchen, not in any bathroom, not once.").
- **Yes/no features:** a regex pass found candidates, and every one was then checked by reading. The regex missed several clear cases (for example the halfway checkpoints in #6, #8 and #13), so the flags below are set by hand, and each has a quoted line in the evidence section.

## Per-script numbers

| # | Spoken words | Length | WPM (est.) | Mid CTA words | Mid CTA at | End CTA words | but /1k | you /1k | ? | Contractions /1k | "So." | "So," | `$`+digit | "dollar(s)" | Voice tags | CTA marker lines |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3124 | 17:44 | 176 | 158 | 39% | 157* | 0.3 | 24.3 | 0 | 0.0 | 4 | 1 | 6 | 3 | 0 | 2 |
| 2 | 3237 | 12:58 | 250 | 151 | 27% | 146* | 0.6 | 17.9 | 1 | 0.0 | 5 | 0 | 0 | 3 | 0 | 2 |
| 3 | 4374 | 21:24 | 204 | 160 | 26% | 157* | 0.5 | 19.4 | 0 | 0.0 | 8 | 1 | 0 | 8 | 0 | 2 |
| 4 | 2876 | 15:51 | 181 | 170 | 22% | 123 | 1.0 | 15.6 | 2 | 0.0 | 4 | 1 | 0 | 6 | 0 | 4 |
| 5 | 3539 | 19:35 | 181 | 208 | 20% | 135 | 0.0 | 11.6 | 2 | 0.0 | 3 | 0 | 12 | 4 | 0 | 4 |
| 6 | 3439 | 24:32 | 140 | 155 | 22% | 133 | 1.5 | 14.2 | 0 | 0.0 | 3 | 0 | 10 | 0 | 0 | 4 |
| 7 | 3224 | 23:00 | 140 | 237 | 32% | 149 | 1.6 | 17.4 | 0 | 0.0 | 6 | 0 | 0 | 11 | 0 | 4 |
| 8 | 3534 | 25:36 | 138 | 197 | 22% | 157 | 0.6 | 16.7 | 0 | 0.0 | 8 | 0 | 0 | 14 | 0 | 4 |
| 9 | 2770 | 14:36 | 190 | 160 | 22% | 110 | 2.2 | 23.8 | 2 | 0.0 | 3 | 1 | 0 | 8 | 25 | 4 |
| 10 | 2688 | 14:21 | 187 | 150 | 26% | 113 | 0.7 | 13.8 | 1 | 0.0 | 2 | 0 | 0 | 5 | 26 | 4 |
| 11 | 2959 | 15:55 | 186 | 155 | 19% | 113 | 1.7 | 11.8 | 0 | 0.0 | 4 | 1 | 0 | 3 | 30 | 4 |
| 12 | 2893 | 15:15 | 190 | 160 | 44% | 118 | 2.1 | 13.8 | 2 | 0.0 | 4 | 0 | 0 | 6 | 28 | 4 |
| 13 | 2991 | 15:58 | 187 | 156 | 32% | 115 | 1.3 | 13.0 | 1 | 0.0 | 2 | 2 | 0 | 6 | 28 | 4 |
| 14 | 2816 | 15:33 | 181 | 167 | 25% | 108 | 2.5 | 7.8 | 0 | 0.0 | 4 | 0 | 0 | 6 | 27 | 4 |

`*` = unmarked end CTA (scripts 1–3), counted as the last paragraph that names the book.

Euro mentions: #1 (2: "about one euro", "about a euro"), #7 (1: "two to three euros"). All other scripts: 0.

### Median and range across the 14

| Measure | Median | Range |
|---|---|---|
| Spoken words | 3057.5 | 2688–4374 |
| WPM (est.) | 183.5 | 138–250 |
| Mid CTA words | 160 | 150–237 |
| End CTA words | 128 | 108–157 |
| but per 1,000 | 1.15 | 0–2.5 |
| you per 1,000 | 14.9 | 7.8–24.3 |
| Questions (?) | 0.5 | 0–2 |
| Contractions per 1,000 | 0 | 0–0 |
| "So." openers | 4 | 2–8 |
| "So," openers | 0 | 0–2 |
| `$`+digit figures | 0 | 0–12 |
| "dollar(s)" words | 6 | 0–14 |
| Mid CTA at (% of spoken words) | 25.5% | 19–44% |
| Voice tags | 0 | 0–30 |

Video length is the YouTube length; WPM medians are against that length.

## German words

| # | German words (count) |
|---|---|
| 1 | Feierabend 1, Wartung 1, Essigessenz 1 |
| 2 | Feierabend 1, Ordnung 1, Vorsorge 1 |
| 3 | Feierabend 1, Vorsorge 1, Natron 1, Soda 3 |
| 4 | Feierabend 1, Vorsorge 1, Rollladen 1 |
| 5 | Feierabend 1, Wartung 1, Wartungsfuge 1, Vorsorge 1 |
| 6 | Feierabend 1, Sparsamkeit 1 |
| 7 | Feierabend 1, Wartung 1, Kalk 9 |
| 8 | Feierabend 1, Wartung 1, Vorsorge 1 |
| 9 | Feierabend 1, Vorsorge 1 |
| 10 | Feierabend 1, Ordnung 1, Wartungsfuge 1 |
| 11 | Feierabend 1, Pfusch 1, Hausmittel 1 |
| 12 | Feierabend 2, Vorsorge 1, Haarsieb 1 |
| 13 | Feierabend 1, Ordnung 1, Wartung 1 |
| 14 | Feierabend 1, Ordnung 1, Vorsorge 1 |

Totals across the 14: Feierabend 15 (in 14 scripts), Kalk 9 (in 1 scripts), Vorsorge 8 (in 8 scripts), Wartung 5 (in 5 scripts), Ordnung 4 (in 4 scripts), Soda 3 (in 1 scripts), Wartungsfuge 2 (in 2 scripts), Essigessenz 1 (in 1 scripts), Natron 1 (in 1 scripts), Rollladen 1 (in 1 scripts), Sparsamkeit 1 (in 1 scripts), Pfusch 1 (in 1 scripts), Hausmittel 1 (in 1 scripts), Haarsieb 1 (in 1 scripts).

German words per script (excluding the closing Feierabend): median 2, range 1–10. The usual pattern is one to three distinct German words besides the closing Feierabend, each said once and glossed in English straight away ("This is Ordnung, which does not mean tidiness."). #7 is the exception ("Kalk" said 9 times), and #3 says "Soda" 3 times while explaining the Soda/Natron naming trap. #12 also uses Feierabend mid-script ("Make it the last small job before Feierabend, which is the German word for the hour when the day's work is done.").

## Features present

| # | Name intro | "this channel is for" | Tease of a later item | Tease of "the end" | Halfway checkpoint | End recap ("never N things") | Three things this week | Feierabend last line | Subscribe ask | Comment ask | Years figure | Closing order |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | yes | yes | yes | no | yes | yes | yes | yes | yes | yes | no | end CTA > three-things > Feierabend |
| 2 | yes | no | yes | no | yes | yes | yes | yes | yes | yes | no | end CTA > three-things > Feierabend |
| 3 | yes | no | yes | no | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 4 | yes | yes | yes | no | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 5 | yes | no | yes | yes | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 6 | yes | yes | yes | no | yes | yes | yes (not called "three") | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 7 | yes | yes | yes | no | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 8 | yes | no | yes | no | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 9 | yes | yes | yes | no | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 10 | yes | yes | yes | no | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 11 | yes | yes | yes | yes | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 12 | yes | yes | yes | no | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 13 | yes | no | yes | no | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |
| 14 | yes | yes | yes | no | yes | yes | yes | yes | yes | yes | no | three-things > end CTA > Feierabend |

Totals: name intro 14/14 ("I am Werner Finkbeiner" 12, "My name is Werner Finkbeiner" 1 (#8), a bare "Werner Finkbeiner." 1 (#3)); "this channel is for" 9/14 (the rest say "This is for ...", and #13 says "here the American house gets the German answer"); a tease of a later item 14/14; a tease of "the end" 2/14; halfway checkpoint 14/14; end recap 14/14; a three-task assignment for the week 14/14 (13 call it "three things" or "three small jobs"); Feierabend as the last line 14/14; subscribe ask 14/14; comment ask 14/14; years figure 0/14.

Closing order: in #1–#2 the end CTA comes before the three-things assignment. In #3–#14 the three things come first and the end CTA after them (for #3, the unmarked closing book paragraph follows the three things). #6 adds an end-screen line before the sign-off: "There is another video on your screen now, if the evening has room for it." #3 adds "So. Go and find the valve." before it.

Last lines as written (tags removed): #1 "Enough for today. Feierabend."; #2 "Enough for today. Feierabend."; #3 "Enough for today. Feierabend."; #4 "Feierabend."; #5 "Enough for today, Feierabend."; #6 "Enough for today. Feierabend."; #7 "Feierabend."; #8 "Enough for today, Feierabend."; #9 "Feierabend."; #10 "Feierabend."; #11 "Feierabend."; #12 "Feierabend."; #13 "Feierabend."; #14 "Feierabend.".

## Evidence (quoted from the spoken text)

### 1. Pour this $1 German Liquid in Your Toilet Bowl and Watch What Happens (6 Genius Uses)

- Name intro: "I am Werner Finkbeiner."
- Tease: "Number four is coming, and number four is the one I would bet on you not seeing, because it does not clean anything at all."
- Halfway: "Stop with me a moment, because those first three were one job wearing three costumes."
- Recap: "So. Six uses, and now I have to tell you that they were never six things."
- Week: "Three things this week, and not one of them takes an afternoon."
- Subscribe: "Subscribe if this is how you like to be told things, and in the comments, tell me the one thing your house does that you have quietly arranged your whole life around."
- Comment ask: "Subscribe if this is how you like to be told things, and in the comments, tell me the one thing your house does that you have quietly arranged your whole life around."

### 2. 10 Things German Households NEVER Pour Down the Drain (Americans Do Most of Them Weekly)

- Name intro: "I am Werner Finkbeiner."
- Tease: "Number three is the one that will annoy some of you, because the person who told you to do it meant well, and they were not trying to cost you money."
- Halfway: "So. Five of them. Stop here for a second and look at what they have in common"
- Recap: "So. Ten things. And I will tell you now that they were never ten things."
- Week: "Three things this week, and none of them take an hour."
- Subscribe: "And subscribe to Werner Finkbeiner, and say something in the comments while you are here, because what this channel promises is the German habit set beside the American one and the service call that never had to happen."
- Comment ask: "Then, in the comments, what does your house do that you stopped noticing years ago and simply worked around?"

### 3. In 30 Years as a German Plumber, I've Never Had a Clogged Drain — Here's Exactly What I Do

- Name intro: "Werner Finkbeiner."
- Tease: "Number three is the one people resist hardest, because it means getting on the floor and taking a piece of your own plumbing apart with your hands"
- Halfway: "So. Five of the nine. Stop here for a moment, because the first five have something in common"
- Recap: "And now the thing I actually wanted to tell you, which is that they were never nine."
- Week: "So. Three things this week, not nine."
- Subscribe: "Subscribe to Werner Finkbeiner for the rest of them, the small repair done early and the call that never had to happen, and in the comments name the one thing your house does that you have quietly started living with."
- Comment ask: "Subscribe to Werner Finkbeiner for the rest of them, the small repair done early and the call that never had to happen, and in the comments name the one thing your house does that you have quietly started living with."

### 4. This Is How We Cool Our House Without AC (The German Way)

- Name intro: "I am Werner Finkbeiner."
- Tease: "Thing two costs nothing. It is a time of day, and if you get it wrong, thing one stops working."
- Halfway: "Now stop for a moment, because there is a pattern in the first three"
- Recap: "it was one idea standing in eleven places"
- Week: "So, this week, three things, no more."
- Subscribe: "If a small repair done early sounds like your kind of thrift, subscribe to Werner Finkbeiner, and tell me in the comments which room in your house never cools."
- Comment ask: "If a small repair done early sounds like your kind of thrift, subscribe to Werner Finkbeiner, and tell me in the comments which room in your house never cools."

### 5. 20 German Plumbing RULES That Will Save You THOUSANDS (Americans Break Most of Them)

- Name intro: "I am Werner Finkbeiner."
- Tease: "That one I keep for the end." (tease of the end)
- Halfway: "So. Halfway. Stop a moment and look at the first ten together."
- Recap: "So. Twenty rules, and I said there was one thing underneath them."
- Week: "Three things this week, and no more than three."
- Subscribe: "If your house has started speaking in drips and knocks and you would rather answer it yourself than pay someone to translate, subscribe to Werner Finkbeiner and tell me in the comments which noise in your house you have learned to sleep through."
- Comment ask: "If your house has started speaking in drips and knocks and you would rather answer it yourself than pay someone to translate, subscribe to Werner Finkbeiner and tell me in the comments which noise in your house you have learned to sleep through."

### 6. Germans Use Less Than HALF the Water Americans Do — 12 Habits That Cut Your Bill

- Name intro: "I am Werner Finkbeiner, and this channel is for people in American houses who would rather understand a thing than pay someone to look at it."
- Tease: "It can run all day and all night with nobody home, and we come back for it before we leave the bathroom."
- Halfway: "So. Six habits, and every one of them happened in the bathroom."
- Recap: "every habit on this list was that same rule, carried into a different room."
- Week: "So the week looks like this."
- Subscribe: "Subscribe to Werner Finkbeiner for more German habits set beside American ones and small repairs caught early, and after the meter test, tell me in the comments what the dial did."
- Comment ask: "Subscribe to Werner Finkbeiner for more German habits set beside American ones and small repairs caught early, and after the meter test, tell me in the comments what the dial did."

### 7. How Germans Remove Limescale From EVERYTHING — The $3 Powder in Every German Kitchen

- Name intro: "I am Werner Finkbeiner."
- Tease: "And the water heater, which is the one where I will tell you to stop."
- Halfway: "Halfway. Stop a moment and see what the five have in common"
- Recap: "you will see that there were never ten things here."
- Week: "Three things for this week, no more than three."
- Subscribe: "And if the German house against the American house is a thing you want to keep watching, subscribe to Werner Finkbeiner and tell me in the comments what your house has been saying."
- Comment ask: "And if the German house against the American house is a thing you want to keep watching, subscribe to Werner Finkbeiner and tell me in the comments what your house has been saying."

### 8. 10 German Heating RULES Americans Break — That Cost You Hundreds Every Winter

- Name intro: "My name is Werner Finkbeiner, and this is for anyone in the United States paying somewhere between 600 and 1,200 dollars to heat a house through a cold winter and wondering where it all goes."
- Tease: "rule three is the one where I ask you to make the bedroom colder on purpose, which is also where a small numbered knob costs less than you think."
- Halfway: "So. Five rules, and I want you to notice what they have in common"
- Recap: "And they are not ten things. It is one thing standing in ten rooms."
- Week: "This week, three things, no more."
- Subscribe: "Subscribe to Werner Finkbeiner for the German habit set against the American one and the service call that never had to happen, and tell me in the comments which window in your house has been tilted since October."
- Comment ask: "Subscribe to Werner Finkbeiner for the German habit set against the American one and the service call that never had to happen, and tell me in the comments which window in your house has been tilted since October."

### 9. How Germans Keep Mold Out of the House FOREVER — The 5-Minute Habit Americans Never Learned

- Name intro: "I am Werner Finkbeiner, and this channel is for people in American houses and apartments who would rather understand a problem than keep paying to have it scrubbed away."
- Tease: "which I will show you in a minute, along with what a German household does instead."
- Halfway: "Stop here a moment and look at what we have so far."
- Recap: "were never eight separate things. They are one rule, showing up in eight different corners of the house"
- Week: "So, three things for this week."
- Subscribe: "Subscribe to Werner Finkbeiner for the old German habit set next to the American one, and tell me in the comments which corner of your house goes dark first every winter."
- Comment ask: "Subscribe to Werner Finkbeiner for the old German habit set next to the American one, and tell me in the comments which corner of your house goes dark first every winter."

### 10. The Best Way to Clean Your Shower & Tub (The German Way)

- Name intro: "I am Werner Finkbeiner, and this channel is for anyone who owns or rents a home and would rather understand why a thing happens than keep paying to have it cleaned up."
- Tease: "including the sponge that must never touch an acrylic tub."
- Halfway: "That is four of the eight, and it is worth stopping here to notice what the four have in common."
- Recap: "Six places, and the same idea standing in every one of them."
- Week: "This week, three things."
- Subscribe: "Subscribe to Werner Finkbeiner for the old German habits that keep a small repair small and the service call unnecessary, and tell me in the comments which corner of your bathroom you have learned to stop looking at."
- Comment ask: "Subscribe to Werner Finkbeiner for the old German habits that keep a small repair small and the service call unnecessary, and tell me in the comments which corner of your bathroom you have learned to stop looking at."

### 11. How to Unclog ANY Toilet Without a Plunger — The German Kitchen Trick That Works Every Time

- Name intro: "I am Werner Finkbeiner, and this channel is for anyone in an American house who would rather understand a thing than pay to have it done."
- Tease: "And at the very end, this same idea turns up in rooms that have nothing to do with a toilet." (tease of the end)
- Halfway: "So. Halfway, and worth one look back."
- Recap: "they were never separate tricks."
- Week: "Three small things for this week, then."
- Subscribe: "Subscribe to Werner Finkbeiner for the old German house habit set next to the American one, and tell me in the comments what your toilet does that you have simply learned to live with."
- Comment ask: "Subscribe to Werner Finkbeiner for the old German house habit set next to the American one, and tell me in the comments what your toilet does that you have simply learned to live with."

### 12. Why Your Shower Drain KEEPS Clogging — It's Missing the $6 Part Every German Drain Has

- Name intro: "I am Werner Finkbeiner, and this channel is for American homeowners and renters who would rather know the cause of a thing than keep paying for it."
- Tease: "Still ahead are the bottle that should never go near this drain, and the part the German drain already has"
- Halfway: "Stop here a moment, because the first three have something in common."
- Recap: "Seven things, and laid side by side, they turn out to be one thing said seven ways."
- Week: "So. This week, three things and no more."
- Subscribe: "Subscribe to Werner Finkbeiner for the German habit set beside the American one and the small repair done early, and in the comments, tell me how long that shower has been draining slow."
- Comment ask: "Subscribe to Werner Finkbeiner for the German habit set beside the American one and the small repair done early, and in the comments, tell me how long that shower has been draining slow."

### 13. Running Toilet? The 10-Minute German Fix (NO New Parts, NO Plumber)

- Name intro: "I am Werner Finkbeiner, and here the American house gets the German answer to its everyday troubles."
- Tease: "Why that tablet never goes back, you will hear later."
- Halfway: "So. Eight minutes left, and time to put the first two side by side."
- Recap: "Now look at the three together."
- Week: "Three small jobs for the coming week, then."
- Subscribe: "Subscribe to Werner Finkbeiner for the older, plainer German way with the same troubles your house has, and tell me in the comments which it was in your tank, the stone, the screw, or the chain."
- Comment ask: "Subscribe to Werner Finkbeiner for the older, plainer German way with the same troubles your house has, and tell me in the comments which it was in your tank, the stone, the screw, or the chain."

### 14. 9 Things German Households NEVER Flush — Americans Flush Most of Them Every Week

- Name intro: "I am Werner Finkbeiner."
- Tease: "Still ahead is the package with that one word printed on it, and what it turns into under the street has a name of its own."
- Halfway: "So. Five down, four to go, and we are standing at the edge of your property."
- Recap: "It looks like nine rules for nine different things. It is one rule."
- Week: "Three small jobs for this week."
- Subscribe: "Subscribe to Werner Finkbeiner for the next German habit set beside the American one, and tell me in the comments the one sound or smell your house makes that you have simply learned to live with."
- Comment ask: "Subscribe to Werner Finkbeiner for the next German habit set beside the American one, and tell me in the comments the one sound or smell your house makes that you have simply learned to live with."

