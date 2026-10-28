# Our channels vs the study winners: side by side

Style study, written 2026-10-28. This file sets the scripts of our two channels, Scarlet Sterling (25 uploads) and Diane de Chambray (13 uploads), next to the 45 study videos, one dimension at a time. Where a study video covers the same topic or type as one of ours, the two are matched and shown together. It describes and quotes only. It makes no rules and no script suggestions. Our 38 scripts were written before the library had any style rules.

Sources: `../own-baseline-2026-10/` (SUMMARY, data, 14 notes), `../data/` and `../notes/` (the study videos), `00-measures.md` and `measures.csv` (built by `../tools/measure.py`). The extra counts in this file come from my own read-only scripts, kept in `/tmp/claude-0/-home-user-script-system/a46e4e64-c9ae-55b0-aafb-8c468f9ffa04/scratchpad/own-vs-winners/` (`lex2.py`, `ngrams.py`, `stock.py`, `own_table.py`, `study_first.py`, `promise.py`, `find.py`).

---

## How far the numbers go (read this first)

- **The sample.** The study set has 45 videos. 42 are winners: 21 real presenters on camera, 18 faceless or AI channels, and 3 pair winners. The other 3 are pair copies: the same title on another channel, or a re-upload, that flopped (Age with Style K6N1EFo7oec at 1.88×, Ageless Confidence UTpC6n7KKi0 with 1,048 views, Elegant After 60 ZFx3yIrJqO0 at 0.77×). "Winners" below means the 42. The copies are shown on their own where they help.
- **The format.** Our channels use an AI face and an AI voice (NexLev reads them as "not faceless", 96% and 98%). The faceless/AI winners are the like-for-like group. The real winners film try-ons, live styling or clients. Where a difference could just come from the camera, I say so.
- **Views.** Our channels are 5 to 6 weeks old, with normals of 532 (Scarlet) and 607 (Diane). Study normals run from 600 to 84,000. Views are compared only within a channel, as views ÷ normal.
- **Age.** Our videos were 1.3 to 37 days old at collection. Five Scarlet uploads were under 7 days old. Most winners are months or years old.
- **Transcripts.** Every transcript on both sides is a YouTube auto-caption. Question marks are counted only on punctuated tracks; several real channels (Justin Hickox, Diana GOSS, Adore Your Wardrobe) have none. Caption errors are quoted as they appear.
- **Time to the first item.** Study times come from the notes (checked in round 3, with its corrections, such as Justin Hickox's 910 words). For our videos, I read each opening and timed it at the start of the transcript segment where the first item begins. For the 14 videos that have notes, my times match the notes.
- **Pattern counts** (scenes, prices, stock phrases, "but") are word-pattern counts over the full transcripts. They are approximate, and each pattern is given where it is used.

### At a glance (medians; measured)

| Side | Videos | Words | Minutes | Words/min | "you" /1k | "I" /1k | "but" /1k | "?" /1k | Age said | CTA words | Seconds to first item | Words before first item | Presenter or channel named in the opening |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Real winners | 21 | 2,031 | 11.9 | 170 | 48.9 | 23.4 | 6.5 | 3.6 | 0 | 3 | 50 | 145 | 4 of 21 |
| Faceless/AI winners | 18 | 2,258 | 15.6 | 156 | 49.5 | 8.1 | 4.9 | 2.9 | 5.5 | 3.5 | 98.5 | 264 | 6 of 18 |
| Pair winners | 3 | 4,084 | 26.6 | 166 | 40.5 | 7.1 | 6.8 | 1.5 | 7 | 4 | 108 | 326 | 1 of 3 |
| Pair copies | 3 | 2,484 | 14.6 | 170 | 44.3 | 5.6 | 2.4 | 2.1 | 6 | 4 | 65 | 185 | 2 of 3 |
| **Scarlet Sterling** | 25 | 2,804 | 16.4 | 171 | 33.8 | 4.1 | 1.1 | 0.4 | 2 | 7 | 93 | 269 | 25 of 25 |
| **Diane de Chambray** | 13 | 2,852 | 16.9 | 170 | 39.9 | 5.6 | 1.0 | 1.4 | 4 | 7 | 71 | 206 | 13 of 13 |

All 42 winners together: 81.5 s and 243.5 words to the first item, and 17 of 42 reach it within 60 s. Ours: 91 s and 268.5 words, and 9 of 38 within 60 s. "CTA words" is the measure script's count of subscribe, comment, link, description, bell and share.

### Pattern counts (mean per 1,000 words, and how many videos have at least one; measured)

| Pattern | Winners (42) | Real (21) | Faceless/AI (18) | Scarlet (25) | Diane (13) |
|---|---|---|---|---|---|
| "Picture" / "Imagine" (an imagined scene) | 0.35 (15) | 0.25 (7) | 0.28 (7) | 1.17 (23) | 1.06 (13) |
| Pointing at what is shown ("you can see", "as you see", "see how", "look at this", "like this", "I'm wearing") | 1.47 (35) | 2.34 (20) | 0.65 (13) | 0.25 (13) | 0.28 (6) |
| The QR code or "on your screen" | 0.10 (8) | 0.16 (6) | 0.03 (1) | 1.23 (25) | 1.16 (13) |
| A price ($, "dollars", "bucks") | 0.15 (7) | 0.17 (5) | 0.14 (2) | 1.00 (21) | 1.37 (13) |
| Own book, guide, course or checklist | 0.46 (23) | 0.66 (11) | 0.24 (9) | 1.72 (25) | 1.44 (13) |
| "Stay to the end" style tease | 0.20 (14) | 0.05 (2) | 0.38 (10) | 0.21 (12) | 0.39 (9) |
| "Subscribe" | 0.43 (25) | 0.24 (6) | 0.66 (16) | 0.36 (25) | 0.34 (13) |

---

## 1. Which of our videos match which study videos

| Our video (views, × normal, age in days) | Study video on the same topic or type (views, × normal) | How close |
|---|---|---|
| Scarlet `h9MsF44shdQ` "You're Styling Your Bob WRONG After 60 — 5 Secrets To Turn Heads Instantly" (514, 0.97×, 10) | Justin Hickox `vFul5tvg1Cw` "You're Styling Your Bob Haircut WRONG! Do THIS Instead- 5 SECRETS" (3,222,185, 63.2×) | Same title shape, same count, same topic |
| Scarlet `XGBMW0cEggI` "5 Bob Haircuts Women Over 60 Should NEVER Get — And the 3 That Take 10 Years Off" (2,787, 5.24×, 11); Diane `qmYPg0L3qZU` "The French Bob After 60…" (607, 1.00×, 24) | Justin Hickox `vFul5tvg1Cw` | Same topic (bobs); ours are about cuts, his is about styling |
| Scarlet `pgMgC2aGPUw` "10 Glasses That Make Women Over 60 Look INSTANTLY Younger" (1,650, 3.10×, 34); `Z13YRFrGF2w` "Wealthy Women Over 60 NEVER Wear These 3 Glasses…" (3,924, 7.38×, 22); Diane `kWzjIzbdB00` "Parisian Women Over 60 NEVER Wear These 3 Glasses…" (1,093, 1.80×, 33); `Ky2QiqNLd5I` "7 Glasses… (The French Way)" (684, 1.13×, 31) | Vivian Sinclair `2q_6Qf69Ywc` "5 Glasses That Make Women Over 60 Look Instantly Younger" (910,914, 140.1×) | pgMgC2aGPUw is the same title with 10 frames instead of 5 |
| Scarlet `w6w_ktMBHXM` "5 Necklaces That Make Women Over 60 Look EXPENSIVE (And 3 That Age You Instantly)" (39,935, 75.07×, 30); Diane `41ezk-kRd7Y` "The Only 3 Necklaces…" (529, 0.87×, 22) | No study video is about necklaces. Nearest items: MM Personal Styling's accessories item (`gfbWOw00Y-M` 0:59, ~296 words); Marie-Anne Lecoeur's closed necklines (`ixlexruRC6c` 1:29, ~117); Aliceinparis's pearls (`fLIVwKa-y3U` 2:33, ~70 words plus a ~417-word sponsored pearl block); Trends Spotted's "accent ceiling" (`HG2OJ0O3lxg` 6:13, ~214) | Item level only |
| Scarlet `XgQ5NgHQ3JQ` "How to Wear a Scarf After 60 — 7 Ways…" (911, 1.71×, 28); Diane `bMlBJn27PEU` "How to Tie a Scarf After 60 the French Way — 7 Knots…" (167, 0.28×, 12) | No study video is about scarves. Nearest items: French Fashion's "big scarf" (`-eTr9aVSWlM` 11:43, ~204 words); Aliceinparis's tie, "Think of it as a silk scarf in a long stray form" (0:24, ~123) | Item level only |
| Diane `egJ5B6d879c` "5 French Haircuts That Flatter ANY Face Shape…" (2,911, 4.80×, 16); `kIjkdHM3a68` "5 French Haircuts That Make Women Over 60 Look INSTANTLY Younger (Salons Won't Suggest Them)" (153, 0.25×, 27) | Marie-Anne Lecoeur, the French lens: `ixlexruRC6c` (its hair item at 7:17) and `n9ICHZq3_tY` "AI Gets French Style WRONG!". On haircuts: Elegant After 60 `XR3IwlcIcCY` "DON'T Get a 'Granny' Cut!" (240.7×) and Stylish60plus `8p2y_Yk0pNQ` (25.5×) | French lens from Marie-Anne; cuts from the faceless winners |
| Diane `ISAL4NBlshQ` "Why French Women Over 60 NEVER Look Frumpy — It's Not Their Weight, It's These 5 Rules" (3,826, 6.30×, 13); Scarlet `EVFmbo51Ou0` "Why You Look Frumpy After 60 — It's NOT Your Weight…" (537, 1.01×, 3) | Marie-Anne Lecoeur `ixlexruRC6c` "7 Things That Scream 'Old Lady' (Harsh But True)" (1,038,117, 12.4×); Adore Your Wardrobe `vBsFMkGDbhA` "STOP Feeling Frumpy in Wide Leg Jeans!" (16.5×) | Same problem (frumpy or "old lady") |
| Scarlet `yl-Vq9WyLzY` "The Jeans Mistake Making Women Over 60 Look OLDER — and the 3 Pairs That Take 10 Years Off" (12,620, 23.72×, 21) | Diana GOSS `9ZNV79Uva3g` "How To Find Jeans For Your Figure" (14.8×); Adore Your Wardrobe `vBsFMkGDbhA` | Same item |
| Others, in the tables only: Scarlet's pixie `3t_q9UrMctk` (0.58×), thinning hair `85nTTAPzBeM` (0.22×), colour combinations `M6HEuRQzwKw` (0.87×) and Diane's `jPoeJlLO2_w` (0.31×), apple shape `pnBhMamGvhE` and Diane's `L6-ASPZTz1s` (2.17×), "look expensive" `UXXfCp_HS6g` (0.44×) | Alice Luxe pixie `CkVrghocoPs` (818×); ChicAfterSixty fine hair `_OQsPYjIfsQ` (205.6×); Chic After 60 colour combinations `YeKT0zkdIrw` (Pair C winner) and AnniePicks `YLiz8tlx9g4` (1,325×); Elegance At 60 pants `XByilJlme5Y` (64.6×); Tracy Campoli `NT1mEOX-p7Y` (10.6×) | Same topic |

Makeup, lipstick, concealer and earrings (8 of our 38) have no study match; the study scanned makeup only as `adjacent`.

**Copied wording.** I searched for any run of 7 or more words shared by one of our scripts and a study script. Only stock phrases turned up: "tell me in the comments which of", "point your phone's camera at the code", "catch your reflection in a shop window", "a trim every 4 to 6 weeks". One line is close in idea, though not in words: Vivian Sinclair, "A frame either lifts the eye or drags it down. There is no neutral." (`2q_6Qf69Ywc` [1:04], uploaded 2026-08-22), and Diane, "Which means it's doing a lot of work for you, or a lot of work against you. There's no neutral setting." (`Ky2QiqNLd5I` [0:45], 2026-09-26).

---

## 2. The hook

### Matched pairs (measured)

| Video | Hook to the end of the promise | First item | Words before the first item | Self-introduction |
|---|---|---|---|---|
| Justin Hickox, bob | 136 words, 0:00-0:31 | Product prep at 0:48; numbered step 1 at 3:26 | ~910 (to step 1) | none spoken |
| Scarlet `h9MsF44shdQ`, bob styling | 151 words to 0:51, then a ~291-word "why" | Secret 1 at 2:30 | 442 | 0:34 |
| Scarlet `XGBMW0cEggI`, bobs to avoid | 193 words | 1:04 | 193 | 0:50 |
| Diane `qmYPg0L3qZU`, French bob | 148 words | 0:49 | 148 | 0:30 |
| Vivian Sinclair, glasses | ~207 words, 0:00-1:07 | 3:02 (cat eye) | ~540 | 1:07, "My name is Vivian Sinclair." |
| Scarlet `pgMgC2aGPUw`, 10 glasses | 142 words | 0:45 | 142 | 0:32 |
| Scarlet `Z13YRFrGF2w`, wealthy women's glasses | 153 words to 0:52 | Frame 1 at 2:39 | 458 | 0:32 |
| Diane `kWzjIzbdB00`, Parisian glasses | 142 words | 0:46 | 142 | 0:34 |
| Diane `Ky2QiqNLd5I`, French glasses | ~300 words | Rule 1 at 1:47; frame 1 at 3:41 | 307 / 570 | 1:16 |
| Marie-Anne Lecoeur, "old lady" | ~30 words, 0:00-0:13 | 0:13 | ~29 | none |
| Adore Your Wardrobe, frumpy jeans | ~140 words, 0:00-1:01 | 1:43 | ~250 | 1:05 |
| Diane `ISAL4NBlshQ`, frumpy | 175 words | 0:58 | 175 | 0:33 |
| Scarlet `EVFmbo51Ou0`, frumpy | ~268 words | "Thing one" at 1:41 | 268 | 0:40 |
| Diana GOSS, jeans | 112 words, 0:00-0:39, then a free-guide CTA to 1:44 | 1:44 | ~300 | none in this video |
| Scarlet `yl-Vq9WyLzY`, jeans | 138 words | The mistake pair at 0:49; pair 1 at 5:32 | 138 | 0:33 |
| Elegant After 60, granny cut | 291 words | 1:40 | ~300 | none |
| Diane `egJ5B6d879c`, French haircuts (top) | 149 words to 0:47, then about 190 more | 1:52 | 339 | 0:26 |
| Diane `kIjkdHM3a68`, French haircuts (bottom) | 106 words to 0:34, then two contrast scenes | 1:35 | 291 | 0:55 |
| Scarlet `w6w_ktMBHXM`, necklaces | 193 words | 0:58 | 193 | 0:25 |
| Diane `41ezk-kRd7Y`, necklaces | 183 words, then a 174-word "French rule" | 2:00 | 357 | 0:49 |
| Scarlet `XgQ5NgHQ3JQ`, scarves | ~110 words, then a fabric section | 1:39 | 300 | ~0:25 |
| Diane `bMlBJn27PEU`, scarves | 157 words, then the why and the prices | 2:13 | 366 | 0:40 |

### The hooks in full (matched pairs)

**Bob.** Justin Hickox (`vFul5tvg1Cw` [0:00], 136 words, unpunctuated captions): "if you don't know these five styling hacks you're probably styling your Bob totally wrong if your Bob has too much volume on the sides it can make your face look full and drippy and kind of make the top feel like it's flat to your head or if there's too much volume in the nape it can bring your eye down and make your profile feel frumpy as well now if the line is too parallel to the floor it can make it seem like the back is too long and it'll bring your eye down also now I'm going to show you five styling techniques it will fix all of these problems no worries and make any Bob look 10 times more flattering on you oh and by the way this works on everyone"

Scarlet (`h9MsF44shdQ` [0:00], 151 words to the promise): "There's a round brush in your bathroom drawer that may be quietly adding years to a perfectly good bob. Every morning it rolls the ends under into that smooth rounded shape. A firm hairspray sets it stiff and by the time you're out the door, the crown is flat and the whole cut sits like a helmet. It looks tidy. It also looks like a portrait from another decade. You can keep the cut and you can even keep the brush. What changes is about 10 minutes of drying and finishing. And the last secret takes 2 seconds and costs nothing. I'm Scarlet Sterling and this channel is for women over 60 who want to look polished and quietly expensive. Mostly with what's already in the closet and on the bathroom shelf. Today it's five secrets for the bob. From a trick that starts with your head upside down to a little roller that works while you do your makeup." Next comes "Let's be fair to that round brush for a moment" (0:51), about 291 words on why the routine flattens the crown, before "The first secret" at [2:30].

**Glasses.** Vivian Sinclair (`2q_6Qf69Ywc` [0:00], ~207 words): "For a fortnight now, everything we have done has been about color. 2 weeks ago, I handed you eight shades one at a time, and last week we put them in pairs and played the chord. Today, all of it arrives where it has been heading the whole while. At the one thing on you that never comes off, sitting permanently against your skin, closer to your eyes than any garment will ever be. Your glasses. So, let me say something a little boldly, and then let me be very gentle about it. A pair of glasses can put 10 years on a face faster than any line ever did, and it has nothing to do with how old you are. It comes down to three things: shape, color, and a small handful of design details nobody thinks to explain to a woman over 60, though every one of them is visible in 4 seconds once somebody points at it. We are doing all three today, and the details get a section of their own because that is where I have watched the biggest change happen in a mirror. Here it is in one sentence. A frame either lifts the eye or drags it down. There is no neutral."

Scarlet (`Z13YRFrGF2w` [0:00], 153 words): "Picture two women sharing a table at Sunday brunch. They have the same silver hair, the same navy sweater, even the same little gold earrings, and they're both wearing glasses. One of them looks rested and quietly expensive, the kind of woman you'd assume has a tailor on speed dial. The other looks tired and a little older than she really is. Neither one spent a penny more than the other. So, why do they look so different from across the room? The answer is sitting on the bridge of each nose. I'm Scarlet Sterling, and this channel is for women over 60 who want to look polished and expensive without spending like it. Today, we're retiring three frames you'll rarely see on a woman who looks wealthy, whether or not she is, and I'll show you what she wears instead, along with the small rules that make choosing your next pair almost…"

Diane (`kWzjIzbdB00` [0:00], 142 words): "Go and find the last photograph anybody took of you. The one from the restaurant table or the one your daughter put up from the garden. Look at your eyes in it. If you see two little white discs where your eyes should be or a hard black bar running across the middle of your face, that's not the camera. That's your glasses. A Parisian woman over 60 will change nearly anything else she owns before she lets that happen. Three kinds of glasses she stays away from. Three she puts on instead. And number three is the pair almost nobody suspects. I'm Diane. This is for women over 60 who want to look expensive without spending like it. By the end you'll know which pair to take off your face tonight and exactly what to ask for at the optician's counter."

**Frumpy and "old lady".** Marie-Anne Lecoeur (`ixlexruRC6c` [0:00], ~30 words): "Are you ready for little tough love? Today I'm revealing seven things that instantly scream old lady. And what to wear instead to look instantly modern, fabulous, and chic."

Diane (`ISAL4NBlshQ` [0:00], 175 words): "Lay the outfit on the bed before you put it on. The gray cardigan, the comfortable black trousers, the soft top that goes with everything. Now step back and look at it. Nobody is wearing it. No hips, no arms, no age, no number on a scale, just cloth on a quilt. And it already looks tired. That's the whole case, closed. If an outfit can look frumpy with no one in it, your body was never the suspect. Frumpy is a set of decisions, five of them. And French women over 60 simply make the opposite five every day without thinking. I'm Diane, and I show women over 60 how French women get dressed so we can borrow it. Today you're getting all five rules, and at the end, a 10-minute mirror test that tells you exactly which one your closet has been breaking. Keep that cardigan outfit in your head because we're going to rebuild it together, rule by rule. And stay for rule five because it costs nothing and changes the most."

**Jeans.** Diana GOSS (`9ZNV79Uva3g` [0:00], 112 words, unpunctuated): "if you tried five pair of jeans and none of them fit it doesn't mean there is something wrong with your figure all the jeans are not for you it simply means you picked the wrong model wrong jeans can make your hips look wider your bottom look heavier can create love handles or make your Bump look saggy we don't want all this unpleasant surprises do we we want to look and feel confident in jeans so in this video I'm breaking down five really important things about jeans you probably never heard of and showing you how to find the right fit for your height and shape so bear with"

Scarlet (`yl-Vq9WyLzY` [0:00], 138 words): "You get dressed for a family birthday lunch and you feel good about it. A soft ivory sweater, your favorite gold earrings, your hair behaving for once. Then, someone takes a full-length photo beside the cake and the woman in that picture looks shorter, wider, and older than the one who smiled back from the mirror that morning. So, what changed between the mirror and the camera? Very often, it's the jeans. One particular pair in one particular cut that so many of us own without suspecting a thing. I'm Scarlet Sterling and this channel is for women over 60 who want to look polished and quietly expensive. Mostly with what's already in the closet. Today, I'll show you the jeans mistake that adds years, why it does what it does, and the three pairs that can take…"

**Necklaces** (no study match). Scarlet (`w6w_ktMBHXM` [0:00], 193 words): "There's about an inch of skin at your collar bone that decides whether a necklace is flattering you or working against you. Land on it and a plain sweater starts reading like money. Land 2 in lower and that same necklace drags your chin and your jawline down with it. We're taught to shop for the pendant and the stones, but the pendant is almost never the problem. It's the length and how much light the metal hands back to your face. I'm Scarlet Sterling and this channel is for women over 60 who want to look polished and expensive without a bigger budget. Five necklaces today that read expensive on a woman over 60 and three that are aging you. Two of the three that age you are in nearly every jewelry box in the country and one of them you probably wore last week. We'll get to those. The good ones come first because once you know what right looks like, the wrong ones are easy to spot. From a few feet away, the first one does something none of the others quite manage. It softens the line of the jaw…"

**French haircuts.** Diane (`egJ5B6d879c` [0:00], 149 words to 0:47): "Somewhere along the way, someone looked at you and told you your face shape. Round, square, long, or heart. And every haircut since has been built to correct it. A stacked back here, a wedge there, and a round brush and a can of spray holding the whole repair job together. You did everything the chart asked. So, how does a French woman with the very same face shape walk out of the salon with less done to her hair and somehow look 10 years lighter? I'm Diana Shambre [caption spelling] and this is where women over 60 come to borrow the French way of getting dressed from the shoes right up to the haircut. Today you're getting five French cuts that flatter any face shape. The exact words to hand your stylist for each one. And somewhere in the middle, the one cut that works on every face shape with…"

Two other winners give the faceless form. French Fashion (`-eTr9aVSWlM` [0:00], 29 words, first item at 0:11): "Bonjour. My winter wardrobe fits in one small closet and I'm never cold. 10 types of clothes, not 10 items. So, two sweaters is fine. Get these right and winter's solved." Stylish60plus (`8p2y_Yk0pNQ` [0:00]) opens "Please do not get the granny cut."

### How the openings are built (measured over all videos)

- **First line.** All 38 of ours open on a second-person scene, a physical detail or an instruction: "Picture two women…" or "Two women…" (5 videos: Z13YRFrGF2w, SZnf4UJCNDk, Rba36JLtcYY, XGBMW0cEggI, EVFmbo51Ou0), a salon chair (kIjkdHM3a68, _rIka9NRGH0), a mirror, drawer or dish (85nTTAPzBeM, XAwQqpN3wQo, z6Ngr5oSjlw, h9MsF44shdQ), a lunch or brunch (yl-Vq9WyLzY, M6HEuRQzwKw, 41ezk-kRd7Y). The winners' first lines more often state the problem or the list outright. Examples: Justin, "if you don't know these five styling hacks"; Marie-Anne, "Today I'm revealing seven things"; Chic Over 60 reads its title, "10 things women over 60 should remove from their wardrobe right now"; Chic After 60, "Leggings after 60, yes or no?"; Ageless Style, "If you want to look older, tired, and invisible, please keep doing these seven things." Others open with a question or a greeting.
- **Naming the list early.** The number in the title is said within the first 20 seconds in 12 of the 28 winners whose titles carry a count (other than an age). Ours: 5 of 38. "Today", "this video" or "I'm going to" comes in the first 20 seconds in 13 of 42 winners and 3 of 38 of ours.
- **The self-introduction block.** All 38 of ours carry it, between 0:25 and 1:16 (median about 0:33), in near-fixed wording. Scarlet's form is "I'm Scarlet Sterling and this channel is for women over 60 who want to look polished and…" (the 9-word core "for women over 60 who want to look polished" appears in 19 videos). Among the winners, 11 of 42 name a presenter or the channel in the opening: Melissa Murrell, Gaby, Kelly Snider, Tracy, Vivian Sinclair, and the channel welcomes of Chic Over 60, Rock Your Fashion, Ever Chic At 50, Ageless Melanin, Stylish60plus and Age with Style. The other 31 never introduce anyone.
- **Teases.** Ours: 21 of 38 have a hold or tease ("a reason I'm saving for the very end", `XGBMW0cEggI` [0:48]; "stay for rule five", `ISAL4NBlshQ`). Faceless/AI winners: 10 of 18. Real winners: 2 of 21.

---

## 3. The authority line

| Video | Who she says she is (quoted) |
|---|---|
| Justin Hickox (bob) | Nothing spoken as a credential. The description carries "over 30 years as a professional hairstylist". He styles a live model on camera. |
| Vivian Sinclair (glasses) | "My name is Vivian Sinclair." (1:07); "What I know is what 40 years beside a fitting room mirror teaches you, and I sold and fitted the things that sit on a face for every one of those years." (1:29); a limit: "I am not an optician and shall not pretend to be one." (1:18). Named clients (Clarice, Ursula) and "an optician called Winifred Bracken". |
| Marie-Anne Lecoeur | `n9ICHZq3_tY`: "from a French woman living in France to show you the 10 essential pieces that we French women wear" (0:18). `ixlexruRC6c`: no credential, only place: "Here in France, we women even in our 70s and over, wear lovely shoes." (4:14). `G-RW7ih19Y4`: "as a professionally trained stylist". |
| Diana GOSS (jeans) | Authority by system: "when it comes to jeans there are nine key Silhouettes"; "I keep on repeating that fabric is the king" (7:09). |
| Adore Your Wardrobe | "for the past 8 years I've been running an online fashion education program" (1:12). |
| French Fashion (AI) | No credential. A persona's life instead: "I still wear a pair I bought when Chirac was president." (11:33); a husband and a granddaughter. |
| **Scarlet** (all 25) | "I'm Scarlet Sterling and this channel is for women over 60 who want to look polished and expensive without a bigger budget." (`w6w_ktMBHXM` [0:25]). Authority is credited to the trade or to a model group: "These length rules aren't mine originally." (`w6w_ktMBHXM` [5:05]); "those line rules belong to generations of tailors" (`yl-Vq9WyLzY` [4:37]); "The women in my circle follow three small rules" (`Z13YRFrGF2w` [10:58]). |
| **Diane** (all 13) | "I'm Diane, and I show women over 60 how French women get dressed so we can borrow it." (`ISAL4NBlshQ` [0:33]); "In Paris, among most of the women I know, the alterations tailor is a neighborhood habit." (`ISAL4NBlshQ` [1:40]); "none of this is my invention" (`kIjkdHM3a68` [5:22]). |

**Measured.** None of our 38 scripts claims a job, a number of years, a client or a past ("I've worked", "my clients", "as a stylist", "when I was" find nothing). "For generations" appears in 12 of ours and in none of the 45 study scripts. Among the winners, a stated credential or tenure appears in speech in about 12 of 42. Real: MM, Diana GOSS, Glam Girl Gabi ("hairstylist and makeup artist for 20 years"), Summer Beauty ("As a hair stylist of 18 years"), chery ("my salon"), Marie-Anne, Adore, Rami Jabali. Faceless/AI: Vivian ("40 years"), Ageless Style ("I've worked with hundreds of women over 50"), Glow After 60 ("after years of looking at what actually works"), Chic After 60 leggings ("I'm over 60 myself"). ChicAfterSixty's authority is lived experience: "I followed those same rules for almost 30 years" (0:32).

---

## 4. The feelings voiced (quotes with timestamps)

| Pair | Study video | Ours |
|---|---|---|
| Bob | Justin: [0:06] "make your face look full and drippy" (looking older); [0:13] "make your profile feel frumpy" (frumpy); [6:41] "I'm saving you money right now" (money); [0:28] "this works on everyone" (permission) | Scarlet `h9MsF44shdQ`: [0:00] "may be quietly adding years to a perfectly good bob" (looking older); [0:20] "It also looks like a portrait from another decade." (dated); [2:01] "you can look more tired than you feel" (older than she feels); [2:11] "Nothing is wrong with your hair or with your face." (reassurance) |
| Glasses | Vivian: [0:31] "it has nothing to do with how old you are" (older than she feels); [2:48] "the face reads as tired on a morning when you slept beautifully"; [10:34] "It had never gone anywhere. It had simply been behind something." (invisible); [16:38] "this is where beauty does not expire, it evolves" (permission) | Scarlet `Z13YRFrGF2w`: [0:15] "The other looks tired and a little older than she really is."; [7:47] "it's the closest thing to a good night's sleep you can put on in the morning"; [15:25] "it makes people assume you have a whole drawer of beautiful things" (status). Diane `kWzjIzbdB00`: [2:02] "Your eyes are in a cave." (being seen); [14:20] "the conclusion a stranger draws in that half second is that you have taste" (status) |
| Frumpy / old lady | Marie-Anne `ixlexruRC6c`: [0:35] "hiding behind tons of fabric because they have lost their self-confidence"; [2:48] "you disappear faster than a macaron at a Parisian cafe" (invisible); [3:39] "beige equal invisible plus old lady"; [4:33] "You can have comfort and style." (permission) | Diane `ISAL4NBlshQ`: [0:20] "your body was never the suspect"; [2:14] "The first person who sees you asks if it's new." (being seen); [6:51] "The woman at the next table quietly decides you must have help at home." (status); [10:43] "This was never about chasing younger. It's about looking decided." |
| Jeans | Diana GOSS: [0:10] "it doesn't mean there is something wrong with your figure"; [0:26] "we want to look and feel confident in jeans"; [9:08] "they look quite cheap most of the time" (money) | Scarlet `yl-Vq9WyLzY`: [0:14] "looks shorter, wider, and older than the one who smiled back from the mirror"; [1:21] "If you own that pair, you're in very good company." (belonging); [6:38] "looking chosen is a very big part of looking expensive" (status) |

**What differs (described).** The winners' feelings are mostly about the viewer's own body and age, stated head-on ("droopy", "frumpy", "lost their self-confidence", "invisible"; ChicAfterSixty [6:55], "every year I felt a little more erased"). Ours turn on being judged by onlookers: a stranger, a friend or "the woman at the next table" notices, assumes or decides something ("quietly decides you must have help at home", "nobody could tell you why", "the gate agent assuming you organized the entire trip", `3JBVSs9ETu4` [10:15]). Status words ("expensive", "wealth", "money", "rich", "luxury") come 2.98 times per 1,000 words in Scarlet's scripts (25 of 25), against 1.64 for the faceless/AI winners and 0.28 for the real ones. Viewer pushback on that frame appears in our top video's comments: "To come across as wealthy, is nowadays a security risk" (4 likes) and "Wear what you can afford" (2) (`w6w_ktMBHXM`).

---

## 5. "You", "I", "but" and questions per 1,000 words (measured)

| Video | you | I | but | ? |
|---|---:|---:|---:|---:|
| Justin, bob | 49.3 | 30.7 | 6.9 | unpunct. |
| Scarlet `h9MsF44shdQ` / `XGBMW0cEggI` / Diane `qmYPg0L3qZU` | 44.7 / 32.3 / 41.8 | 2.9 / 5.5 / 3.9 | 1.1 / 0.0 / 0.6 | 0.0 / 1.0 / 2.1 |
| Vivian, glasses | 38.6 | 15.1 | 1.1 | 2.5 |
| Scarlet `pgMgC2aGPUw` / `Z13YRFrGF2w` / Diane `kWzjIzbdB00` / `Ky2QiqNLd5I` | 51.8 / 34.8 / 44.9 / 41.2 | 4.1 / 3.6 / 3.8 / 8.5 | 1.7 / 2.3 / 0.5 / 1.8 | 1.4 / 2.0 / 1.5 / 0.0 |
| Marie-Anne `ixlexruRC6c` / `n9ICHZq3_tY` | 56.3 / 35.0 | 27.1 / 22.6 | 9.8 / 5.1 | 13.0 / 3.2 |
| Adore, frumpy jeans | 48.9 | 21.8 | 6.4 | unpunct. |
| Diane `ISAL4NBlshQ` / Scarlet `EVFmbo51Ou0` | 32.2 / 21.8 | 10.1 / 6.8 | 1.0 / 0.8 | 1.0 / 0.8 |
| Diana GOSS, jeans | 39.9 | 10.6 | 8.3 | unpunct. |
| Scarlet `yl-Vq9WyLzY` | 39.3 | 3.9 | 1.6 | 1.6 |
| Diane `egJ5B6d879c` / `kIjkdHM3a68` | 47.6 / 47.5 | 9.2 / 7.1 | 1.5 / 1.1 | 2.2 / 0.7 |

- **"I".** Scarlet's median is 4.1 and Diane's 5.6, below every winner group (real 23.4, faceless/AI 8.1, pair winners 7.1). The real winners' "I" comes from showing and telling ("I'm wearing", "I see it in my salon", Tracy's 188 "I" forms). Story markers ("I remember", "I once", "I used to", "my mother", "my client") occur in 11 of our 38 and in 12 of the 21 real winners.
- **"But".** About 1.0 per 1,000 words on both our channels, against 4.9 to 6.8 for the winner groups and 2.4 for the copies. "Though", "however", "yet" and "still" do not make up the gap: 1.5 and 1.2 for ours, 1.6 and 1.2 for the winners. Our scripts state their contrasts without "but", as in "It looks tidy. It also looks like a portrait from another decade." (`h9MsF44shdQ` [0:20]).
- **"You".** 33.8 and 39.9, against about 49 for both winner groups.
- **Questions.** Scarlet 0.4 and Diane 1.4 on punctuated tracks, against 3.6 (real) and 2.9 (faceless/AI).

---

## 6. Items: count, words each, how each opens and ends

| Video | Items | Words each | How an item opens | How it ends |
|---|---|---|---|---|
| Justin, bob | 5 steps, plus texture notes | 171-384 | "step number two two is to keep the nape tight" | On the shown result: "now you can see the difference between before and now" |
| Scarlet `h9MsF44shdQ` | 5 secrets, plus a "retire" block (~283) | 285-410 | "The first secret, and the one everything else is built on, is…" | A three-part wrap, then a tease: "Lifted, light, and entirely your own." ([4:43]); "Graceful, unforced, and completely on purpose." ([10:06]) |
| Scarlet `XGBMW0cEggI` | 5 to avoid, 3 to ask for | Avoid 192-269; ask 273-530 | "The second lives right at the front where everyone looks first." | A short wrap ("Softer at the back and far kinder to the face.") or a salon script ("In the chair, ask for…") |
| Vivian, glasses | 5 shapes, plus details and colour (~1,085) | 212-261 | "Number two, the soft rectangle with rounded corners." | "Who it suits?", "What to avoid?", and two items end on a named client: "Why has nobody shown me this?" |
| Scarlet `pgMgC2aGPUw` | 10 frames | about 190-310 | "Number one is for almost anyone, and especially for the woman whose…" | A "Picture…" scene, then a verdict: "on you it reads as good taste" ([2:18]) |
| Scarlet `Z13YRFrGF2w` | 3 frames, 3 rules, 2 habits | Frames 361-498; rules 141-168 | The frame named, then a swap | A mirror test |
| Diane `kWzjIzbdB00` | 3 to avoid, 3 to wear, 4 fitting rules | Avoid 512-552; wear 272-324 | "Number one, the heavy black rectangle." | A mechanism, a scene, then a phone or mirror test |
| Marie-Anne `ixlexruRC6c` | 7 | 80-170 | "The next thing that scream old lady is…" | "So, what can you do instead?" then "My pro tip is…" |
| Adore, frumpy jeans | 6 do's and don'ts, plus "do" subscribe | 130-300 | "my first due is to know…" | A rule |
| Diane `ISAL4NBlshQ` | 5 rules | 237-303 | "Rule number one, fit. Here's what I see" | "The French answer", "Picture it", "Your test today" |
| Scarlet `EVFmbo51Ou0` | 5 things | ~330-400 | "Thing one, fit." | A payoff line: "…and it will do more than any new purchase this month." (thing one, before 4:26) |
| Diana GOSS, jeans | 5 things (the first split into 4 body-shape blocks) | 85-380, typically ~200 | A rule ("fabric is the king") | A shown try-on |
| Scarlet `yl-Vq9WyLzY` | 1 mistake (~445), 3 pairs, fit and wash blocks | Pairs 354-400 | A scene: "picture a farmer's market on a bright autumn morning" | The birthday-photo scene returns at 3:03, 13:19 and 16:56 |
| Stylish60plus, haircuts | 7 | 302-493 | The old version, then "watch these two side by side" | A tease for the next cut |
| Diane `egJ5B6d879c` / `kIjkdHM3a68` | 5 cuts each | 330-496 / 255-329 | "Number one, the French bob." / "Number one is for the woman who's worn it short forever" | A stylist script / a one-line wrap ("A bob doesn't need rollers. It needs a good edge.") |
| Scarlet `w6w_ktMBHXM` | 8 (5 good, 3 mistakes) | 270-470 | A distance teaser: "From a few feet away, the first one does something…" | A one-line wrap: "Simple, warm, and impossible to argue with." ([3:04]) |
| Diane `41ezk-kRd7Y` | 3 necklaces | 583-655, then a ~1,600-word tail | "Necklace number one is a fine gold chain…" | "Tonight, take the set out of its box and lay it on the bed." |
| Nearest study items | MM accessories (~296); Marie-Anne necklines (~117); French Fashion scarf (~204) | | "The next thing that scream old lady is closed neck lines." | "My pro tip is open up your neckline, open up your self-confidence." |

**Measured across all videos.** The notes list our items at 205-655 words, typically 250-400. The winners' run 70-850 words: Marie-Anne's are 80-170 each and ChicAfterSixty's up to 851. The faceless/AI winners' items have the same fixed shape as ours: Chic Over 60 ends each on a keep-or-go line, Ageless Style uses "The swap" 7 times, and Glow After 60 adds shops by budget. A "Picture…" or "Imagine…" scene inside the items appears in 36 of our 38 and in 15 of the 42 winners.

---

## 7. The age said, and the title's promise in speech

- **Age phrases** (measure script: "over/after/at" + 40-80, "women our age", "older women" and similar): Scarlet median 2, Diane 4, faceless/AI winners 5.5, real winners 0. The real winners say no age at all (Justin, Diana GOSS, Adore, Tracy's "over 40" aside). Several faceless winners repeat it: Rock Your Fashion 21, Ever Chic 19, Age with Style 11. "Women over 60" appears in 36 of our 38, mostly in the self-introduction.
- **The title's promise, spoken.** Measured over titles and transcripts:
  - Of our 8 titles with "Younger", 3 say "younger" in speech (median 0 uses). All 5 winner titles with "Younger" say it (median 2).
  - Of our 3 "Slimmer" titles, 1 says "slimmer" or "thinner". Marie-Anne's slimmer video says it 12 times, as a refrain: "With a monochrome outfit, 10 lb thinner for sure."
  - "10 years" or "years off" is in 11 of our titles and spoken in 6 of those videos.
  - "Expensive" titles say "expensive" 5-10 times in ours and 2-7 times in the winners.
  - "Old lady" or "granny" titles: Marie-Anne says "old lady" 10 times; our two 'Granny' lipstick titles (Scarlet and Diane) say it once each.

---

## 8. Reassurance and shame

- **Measured word lists** (shame: old lady, granny, grandma, frumpy, dowdy, invisible; reassurance: "nothing wrong with you", "you deserve" and similar): the median is 0 on every side. The high counts are all winners: Marie-Anne `ixlexruRC6c` 11 shame words, Ageless Style 11, Elegant After 60 granny cut 10.
- **Ours (quoted).**
  - Reassurance: "Nothing is wrong with your hair or with your face." (`h9MsF44shdQ` [2:11]); "A great many women wore a version of it, and there's no shame in that at all." (`XGBMW0cEggI` [1:29]); "That's a habit, not a failing." (`kIjkdHM3a68` [1:21]); "never your weight and never your age" (`EVFmbo51Ou0` [0:57]); "Your face shape was never the problem." (`egJ5B6d879c` [1:12]).
  - Lines that could read as shaming, from the notes: "Dullness reads as neglect every time" (`w6w_ktMBHXM` [16:16]); "What I see breaks my heart a little. A beautifully put together woman and then a chunky white gym sneaker underneath or the clog." (`ISAL4NBlshQ` [7:14]); "Hair that doesn't move looks like it belongs to another decade and unfairly so does the woman under it." (`kIjkdHM3a68`); "thin jersey has the manners of cling film" (`L6-ASPZTz1s`).
- **The winners (quoted, from the notes).**
  - Marie-Anne: "I told you I was going to be harsh. Not on you, but your clothes. Cruel to be kind and all that."
  - Elegant After 60: "Ladies, that isn't a haircut. That's a cry for help" (5:53).
  - Ageless Style: "This video wasn't meant to shame you. It was meant to wake you up. You are not invisible."
  - Vivian: "Aging is not the problem. The wrong frame is".
  - Justin: "no worries".
- **How each side handles it (described).** The winners that shame do it openly and then name it ("tough love", "harsh", "brutally honest"). Their comments push back hard: "Waiting for the day when being old isn't an insult." (390 likes, `ixlexruRC6c`). Ours rarely use the shame words (3 of 38 say "frumpy"). The judgement comes as a verdict on the object ("reads tired", "reads as neglect", "looks prescribed").

---

## 9. The French lens (Diane only)

| Video | French/Paris words per 1k | Claim sentences about French or Parisian women | Hedged ("most", "many", "usually", "often", "tend", "plenty", "rarely", "I know"…) |
|---|---:|---:|---:|
| Diane, all 13 | 3.5-7.7 (median about 6.5) | 180 | 21 (12%) |
| Marie-Anne `n9ICHZq3_tY` | 11.1 | 18 | 4 (22%) |
| French Fashion `-eTr9aVSWlM` (AI) | 6.5 | 10 | 1 (10%) |
| Aliceinparis `fLIVwKa-y3U` | 20.9 | 30 | 4 (13%) |
| Trends Spotted `HG2OJ0O3lxg` | 0.9 | 1 | 0 |

Diane's videos range from 0% hedged (`Rba36JLtcYY`, `akYILT648sU`, `jPoeJlLO2_w`, `qmYPg0L3qZU`, `Ky2QiqNLd5I`) to 41% (`z6Ngr5oSjlw`).

**Claims and hedges, quoted (Diane):**
- Unhedged: "Half of them skip black in daylight altogether and wear navy." (`akYILT648sU` [1:35]); "A Parisian woman over 60 will change nearly anything else she owns before she lets that happen." (`kWzjIzbdB00` [0:19]); "French women over 60 have a four-second trick that lifts the whole face" (`bMlBJn27PEU` [0:00]).
- Hedged: "French women tend to build around quiet colors" (`41ezk-kRd7Y` [1:35]); "French women are known for going longer between cuts, often 10 or 12 weeks." (`egJ5B6d879c` [10:52]); "Plenty of the women I know in Paris wear gold against silver hair anyway" (`z6Ngr5oSjlw` [15:54]).
- History given as fact: "the French bob has been cut in Paris for over a century" (`qmYPg0L3qZU` [0:15]), with "is usually credited with starting the fashion for it in 1909" ([1:02]).

**Where Diane stands, in her own words.** She never says she is French or lives in France. She puts herself among the borrowers ("so we can borrow it", `ISAL4NBlshQ` [0:33]) and in America ("which is not remotely how we buy it here", `Ky2QiqNLd5I` [1:05]; "A good haircut in America runs somewhere between $60 and $150", `egJ5B6d879c` [10:54]). Her link to Paris is acquaintance: "the women I know in Paris" (`z6Ngr5oSjlw` [13:44] and [15:54]) and "among most of the women I know" (`ISAL4NBlshQ` [1:40]). Her habit is to watch: "What I see" in 7 of 13 videos, 14 uses. French words: "voilà" in 11, "à bientôt" (any caption spelling) in 12, "chérie" in 5. No study script uses "chérie"; 2 use "voilà" and 1 "à bientôt" (French Fashion: "À bientôt, mes chers amis.").

**The winners.** Marie-Anne speaks as one of them: "We French women, we like little detailing." Her hedges are "usually", "most" and "at least one". The AI channel French Fashion speaks as a French woman with a home life ("Her husband keeps the heating at 19° to save money. Mine does, too."), mostly unhedged: "That's why in France, this is where the money goes." ([0:24]). Aliceinparis presents from Paris, also mostly unhedged: "Skinny jean have never been popular here in France or in Paris" (6:46). Marie-Anne's AI video sets real French women against AI channels: "I see so many AI videos who show you what French women wear. Invariably, they get it wrong." Five of its comments are against AI ("I can spot an AI video immediately and scroll by").

---

## 10. Visuals in words

| | Study video | Ours |
|---|---|---|
| Bob | Justin points at the live demonstration: "you see how she's pointing the air down" (3:52); "do you see how strong that line Looks" (7:37) | Scarlet describes hand steps and an imagined morning: "we'll start where the morning starts, with damp hair, a towel around your shoulders" (`h9MsF44shdQ` [2:20]) |
| Glasses | Vivian describes frames exactly and has no as-you-see lines: "a modern frame with the softest upward sweep at the outer corners, not a wing" | Scarlet sets a scene: "Picture a long lunch with friends and you catch your reflection in the restaurant window on the way out." (`pgMgC2aGPUw` [2:06]) |
| Frumpy | Marie-Anne's slimmer video points at pictures: "And in our example here, you can see by wearing one color from top to bottom" | Diane rebuilds one imagined outfit rule by rule ("Keep that cardigan outfit in your head", `ISAL4NBlshQ`) |

**Measured.** Pointing at what is shown: 1.47 per 1,000 words in the winners (real 2.34, in 20 of 21; faceless/AI 0.65, in 13 of 18), against 0.25 and 0.28 for ours. Imagined scenes ("Picture…", "Imagine…"): 0.35 in the winners (15 of 42), against 1.17 and 1.06 for ours (36 of 38). The one thing on screen our scripts always name is the QR code ("the code on your screen" or "on the screen", 25 of 25 and 13 of 13; winners 8 of 42). Scene settings recur: "gallery" in 20 Scarlet videos (study 3), "book club" in 17 Scarlet videos (study 1), "brunch" in 10, "cafe" in 10 Diane videos, "shop window" or "restaurant window" in 11 Diane videos.

Comments on the faceless winners name a mismatch between words and pictures. Vivian: "the visuals of Scott's lawn products all while listening to a discussion about choosing eyeglasses??" (514 likes). Stylish60plus: "You used a lot of the same photos to illustrate all kinds of different cuts". Glow After 60: "I think the dress being talked about should ALWAYS be the one that is shown." (42). On ours: "All of those pics of women were really cute. You are completely incorrect." and "It can be improved by models who are not a perfect size" (2 likes) (`yl-Vq9WyLzY`).

---

## 11. CTAs and the ending

**Ours (measured, all 38).** Every script has the same three parts:
- the self-introduction block (0:25-1:16)
- a mid-roll pitch for the channel's book, 2:18 to 7:28 in, about a third of the way through. Scarlet's book is "300 budget-friendly ways to look expensive"; Diane's is "The French Way, 389 pages". The 14 notes measure the pitch at 148-234 words.
- an end block of 84-215 words: the book again, then "subscribe", then usually "tell me in the comments which…" (27 of 38).

Scarlet ends every one of her 25 videos on "Until next time, stay polished and stay sterling." Diane ends 12 of 13 on "à bientôt" (caption spellings vary: "A bientôt", "Abento", "Abian too", "Abian 2"); the 13th, `kWzjIzbdB00`, ends on "Keep it simple and let them wonder how you do." The packaging totals about 230-450 words a video. A QR code is explained in every video, often as a little lesson ("point the camera at that square the way you would at a grandchild", `w6w_ktMBHXM`).

**Endings quoted (last words):**
- Justin (bob): "but if you're curious there is a link in the description where you can learn more and Prime day 2024 you can save up to 30% so make sure you check that out now I'll see you over here"
- Scarlet `h9MsF44shdQ`: "And tell me in the comments which of these five secrets you'll try first. Until next time, stay polished and stay sterling."
- Vivian (glasses): "The shades that quietly add years after 60 and the ones that take them straight off again. Until then, keep your chin up, take up all the room you like, and I will see you next week."
- Diane `kWzjIzbdB00`, the one Diane video without the farewell: "Whatever you end up in, the line on your face should point up. That's the whole lesson. Another French habit soon. Keep it simple and let them wonder how you do."
- Marie-Anne `ixlexruRC6c`: "A shorter cut is youthful, my lovely ladies. I hope you enjoy these things that scream old lady. But if you want to find out the fashion mistake that make you look older, watch the video on screen"
- Diane `ISAL4NBlshQ`: "Subscribe to Diane de Chambray, so the next French habit finds you, and tell me in the comments which of the five rules you're taking to the mirror tonight. À bientôt."
- Diana GOSS (jeans): "let me know in the comments which jeans fit you feel most comfortable in thank you for watching see you on Sunday bye"
- Scarlet `yl-Vq9WyLzY`: "subscribe to Scarlet Sterling, and tell me in the comments which of the three pairs you'll try first. Until next time, stay polished and stay sterling."
- French Fashion: "Winter is long. Dress warm, dress well, and let the cold be jealous of you. À bientôt, mes chers amis."

**The winners.** "Subscribe" is spoken in 25 of 42; Marie-Anne's four videos never ask, and Justin never asks in speech. A comment ask comes in 27 of 42. Sales blocks are as long as ours or longer in some winners: Diana GOSS's course ad (~270 words) and free guides (~185 words, before the first item), Tracy Campoli's sponsor read (~324), and ChicAfterSixty's books, then a paid membership. Others have almost none: Chic After 60 colour (`YeKT0zkdIrw`) has one 40-word CTA at 29:32 and no mid-roll. Vivian asks for a comment halfway: "We are halfway so tell me in the comments what you are wearing right now and which of these you would try next. I read every one and they genuinely decide what I make." (7:30). What sets ours apart is the identical layout in 38 of 38, not the size of the pitch.

---

## 12. Products, brands, prices and books

| Side | Brands named in speech | Prices in speech | Own product |
|---|---|---|---|
| Real winners | Most of them: MM (Boden, Uniqlo, M&S, H&M "$29.99"), Tracy (Uniqlo "$15", H&M "$50", Zara, Levi's), Justin (Laifen, sponsored), Marie-Anne (Birkenstocks and Crocs as the "no"; her own shirt line), Summer Beauty (Redken, K18) | 5 of 21 | Courses, guides, sponsors, affiliate links |
| Faceless/AI winners | Few: Glow After 60 (~27 stores with "under $50"-style prices), Chic After 60 (Max Mara, Ralph Lauren), Trends Spotted (Burberry, Hermès), Golden Melanin (Ugg) | 2 of 18 | Books, checklists, memberships; Vivian: "Not one of them costs anything to notice." |
| **Ours** | None in 38 videos (the 14 notes record "No brands" each time; Diane describes one without naming it: "A silk house in Paris introduced a printed square back in the 1930s") | 34 of 38: "Good freshwater pearls run somewhere around 40 to $120 for a strand." (`w6w_ktMBHXM` [12:51]); "A good dark straight jean usually runs somewhere around 40 to 80 dollars at the mall" (`yl-Vq9WyLzY`); "A good haircut in America runs somewhere between $60 and $150" (`egJ5B6d879c`) | The book, twice in every video |

Comments on the winners ask for shops and links: "I can't belive you said, 'the brands that get it right,' without mentioning the brands" (87 likes, Elegance At 60 `XByilJlme5Y`). The question on our top video is the same kind: "Where can I buy the natural stone pendant on a leather cord please?" (`w6w_ktMBHXM`).

---

## 13. Length and words per minute

| Video | Length | Words | Words/min |
|---|---:|---:|---:|
| Justin, bob | 10:07 | 2,476 | 245 (two voices) |
| Scarlet `h9MsF44shdQ` / `XGBMW0cEggI` / Diane `qmYPg0L3qZU` | 15:58 / 16:55 / 18:37 | 2,773 / 2,913 / 3,352 | 174 / 172 / 180 |
| Vivian, glasses | 16:59 | 2,849 | 168 |
| Scarlet `pgMgC2aGPUw` / `Z13YRFrGF2w` / Diane `kWzjIzbdB00` / `Ky2QiqNLd5I` | 16:28 / 17:58 / 23:40 / 22:00 | 2,954 / 3,075 / 3,944 / 3,396 | 179 / 171 / 167 / 154 |
| Marie-Anne `ixlexruRC6c` / `n9ICHZq3_tY` | 8:02 / 14:18 | 923 / 2,170 | 115 / 152 |
| Diane `ISAL4NBlshQ` / Scarlet `EVFmbo51Ou0` | 12:30 / 16:37 | 2,082 / 2,663 | 167 / 160 |
| Diana GOSS, jeans / Adore | 12:41 / 11:26 | 2,179 / 1,881 | 172 / 165 |
| Scarlet `yl-Vq9WyLzY` | 18:00 | 3,106 | 173 |
| Scarlet `w6w_ktMBHXM` / Diane `41ezk-kRd7Y` | 22:07 / 18:16 | 4,078 / 3,334 | 184 / 183 |

Every one of our 38 videos is between 12:30 and 23:40 long, and the median is 16:27 (Scarlet) and 16:56 (Diane). The winners run from 6:46 to 30:51: the real ones at a median of 11.9 minutes, the faceless/AI ones at 15.6, and the pair winners at 26.6. Pace is about the same: ours 170-171 words/min, real 170, faceless/AI 156. The words in the first 30 seconds are also similar (ours 89-92, winners 83-86).

---

## 14. Our top videos against our bottom ones

| Video | Views (× normal, days) | Words | Words/min | you /1k | I /1k | First item (s / words before) | Prices | "Picture/Imagine" | Avoid or negative wording in the title |
|---|---|---:|---:|---:|---:|---|---:|---:|---|
| S `w6w_ktMBHXM` necklaces | 39,935 (75.07, 30) | 4,078 | 184 | 33.8 | 5.9 | 58 / 193 | 1 | 4 | "And 3 That Age You" |
| S `yl-Vq9WyLzY` jeans | 12,620 (23.72, 21) | 3,106 | 173 | 39.3 | 3.9 | 49 / 138 | 5 | 3 | "Mistake… OLDER" |
| S `Z13YRFrGF2w` wealthy glasses | 3,924 (7.38, 22) | 3,075 | 171 | 34.8 | 3.6 | 159 / 458 | 2 | 3 | "NEVER Wear" |
| D `ISAL4NBlshQ` frumpy | 3,826 (6.30, 13) | 2,082 | 167 | 32.2 | 10.1 | 58 / 175 | 4 | 2 | "NEVER Look Frumpy" |
| D `egJ5B6d879c` French haircuts | 2,911 (4.80, 16) | 2,729 | 185 | 47.6 | 9.2 | 112 / 339 | 2 | 2 | none |
| S `3t_q9UrMctk` pixie | 311 (0.58, 9) | 2,696 | 169 | 34.5 | 3.7 | 105 / 322 | 0 | 2 | none |
| S `UXXfCp_HS6g` expensive, no spend | 236 (0.44, 37) | 2,888 | 182 | 48.1 | 3.8 | 188 / 595 | 4 | 6 | none |
| S `3JBVSs9ETu4` fall colours | 157 (0.30, 14) | 2,440 | 163 | 29.1 | 4.9 | 117 / 317 | 3 | 2 | none |
| D `jPoeJlLO2_w` colour combinations | 189 (0.31, 29) | 2,831 | 163 | 39.6 | 5.3 | 64 / 175 | 1 | 5 | none |
| D `bMlBJn27PEU` scarf knots | 167 (0.28, 12) | 2,707 | 170 | 39.9 | 5.5 | 133 / 366 | 1 | 2 | none |
| D `kIjkdHM3a68` French haircuts | 153 (0.25, 27) | 2,672 | 169 | 47.5 | 7.1 | 95 / 291 | 4 | 3 | none ("Salons Won't Suggest Them") |
| **Median, top 5** | | 3,075 | 173 | 34.8 | 5.9 | 58 / 193 | 2 | 3 | 4 of 5 |
| **Median, bottom 6** | | 2,702 | 169 | 39.8 | 5.1 | 111 / 320 | 2 | 2.5 | 0 of 6 |

**Same-topic pairs inside our channels (measured).**

| Topic | Higher-viewed | Lower-viewed | First item (higher vs lower) |
|---|---|---|---|
| French haircuts (Diane, 11 days apart) | `egJ5B6d879c` 2,911, "Flatter ANY Face Shape" | `kIjkdHM3a68` 153, "Look INSTANTLY Younger (Salons Won't Suggest Them)" | 112 s vs 95 s |
| Bob (Scarlet, both 2026-10-17) | `XGBMW0cEggI` 2,787, "Should NEVER Get" | `h9MsF44shdQ` 514, "Styling Your Bob WRONG" (Justin's form) | 64 s vs 150 s |
| Necklaces | Scarlet `w6w_ktMBHXM` 39,935, 8 items | Diane `41ezk-kRd7Y` 529, 3 items | 58 s vs 120 s |
| Glasses | Scarlet `Z13YRFrGF2w` 3,924 | Scarlet `pgMgC2aGPUw` 1,650; Diane `kWzjIzbdB00` 1,093, `Ky2QiqNLd5I` 684 | 159 s vs 45 s, 46 s and 221 s |
| Face-shape haircuts (same title) | Diane `egJ5B6d879c` 2,911 | Scarlet `se0NK3SdI0I` 802 | 112 s vs 93 s |
| Frumpy | Diane `ISAL4NBlshQ` 3,826 | Scarlet `EVFmbo51Ou0` 537 (3.4 days old) | 58 s vs 101 s |

**What differs (described).**
- **Speed to the first item.** The medians favour the tops (58 s against 111 s). Within same-topic pairs, the higher-viewed video got there sooner in 3 of 6 and later in 3.
- **Length.** The tops are longer (median 3,075 words against 2,702); the top video is the longest Scarlet script (4,078).
- **Wording rates.** "You", "I", prices and scenes overlap between the two groups.
- **Packaging.** It is the same in all 11: the self-introduction, the book pitch at 2:18-7:28, and the same sign-offs.
- **Titles.** The clearest difference is outside the script. 4 of the 5 tops put an avoid or negative element in the title; none of the 6 bottoms does. Over the 33 videos at least 7 days old, the 16 titles with "NEVER", "STOP", "Mistake", "Age You", "OLDER", "WRONG", "Avoid", "Frumpy" or "Granny" have a median of 1.98× normal; the 17 without have 0.87×. The four "Turn Heads" titles all sit at 0.31-0.97×.
- **Avoid items inside the scripts.** The tops voice their avoid list early: "three that are aging you" (`w6w_ktMBHXM` [0:34]); "the jeans mistake that adds years" (`yl-Vq9WyLzY`); "we're retiring three frames" (`Z13YRFrGF2w`); "What I see" in `ISAL4NBlshQ`. Several bottoms carry mistakes inside the items too (`bMlBJn27PEU` opens each knot on the mistake; `kIjkdHM3a68` has "five things to retire"), but not in the title.
- **Comments.** On the top video, 3 of 14 viewer comments push back on the "expensive" or "wealthy" frame and 2 are about AI.

---

## 15. Lines that read as AI-written, and lines repeated across our 38 scripts

**Repeated phrases** (counted as word runs over all 38 transcripts, longest form kept; "study" = how many of the 45 study scripts contain the same run):

| Phrase | Our videos (Scarlet / Diane) | Study videos |
|---|---|---:|
| "until next time stay polished and stay sterling" | 25 (25/0) | 0 |
| "book 300 budget friendly ways to look expensive" | 25 (25/0) | 0 |
| "subscribe to scarlet sterling" | 24 (24/0) | 0 |
| "is for women over 60 who want to look polished" | 17 (15/2) | 0 |
| "i'm scarlet sterling and this channel is for women over 60" | 13 (13/0) | 0 |
| "tell me in the comments which" | 27 (16/11) | 3 |
| "it's a digital download" | 20 (16/4) | 0 |
| "code on your screen" / "code on the screen" | 20 / 14 | 0 |
| "the mistake, the swap and the payoff" (the book pitch) | 10 (10/0) | 0 |
| "laid out the same way, the dated habit, the French secret, then how to do it" (the book pitch) | 8 (0/8) | 0 |
| "of numbered secrets" | 8 (0/8) | 0 |
| "whenever (it) suits you (is the right time)" | 10 (7/3) | 0 |
| "from across the room" / "from across a room" | 18 (11/7), 23 uses | 0 |
| "small gold hoops" | 22 (13/9) | 0 |
| "camel coat / cardigan / sweater / trousers" | 21 (17/4), 46 uses | 3 |
| "for generations" | 12 (9/3) | 0 |
| "so many of us" / "nearly all of us" | 15 (13/2) | 0 |
| "somewhere along the way" | 6 (5/1) | 1 |
| "on an ordinary Tuesday" | 6 (5/1) | 1 |
| "in (very) good company" / "plenty of company" | 5 (4/1) | 0 |
| "picture a gallery afternoon" | 7 (7/0) | 0 |
| "what I see" (Diane) | 7 of 13, 14 uses | — |
| "keep it simple and let them wonder how you do (it)" (Diane's closing line) | 3 (0/3) | 0 |

**Words that recur far more in ours than in the study set:**
- "reads as" or "reads [tired, polished, expensive, dated…]": 33 of 38, 112 uses (study: 11 of 45, 31 uses)
- "quietly": 32 of 38, 74 uses (study: 6 of 45, 20)
- "Picture a / it / yourself / the": 30 of 38, 67 uses (study: 6 of 45, 13)
- "quiet luxury": 9 Scarlet videos, 20 uses (study: 6, 9)
- "on purpose", "chosen" or "decided": 31 of 38 (study: 8 of 42 winners)

**Line shapes the notes flag in our scripts:**
- Three-part or two-word wraps that close an item: "Simple, warm, and impossible to argue with." (`w6w_ktMBHXM` [3:04]); "Fresh and finished." (`3t_q9UrMctk` [3:03]); "Verdict on both. Simple, warm, finished." (`M6HEuRQzwKw` [2:36]); "And quietly, well done." ([2:25]).
- Aphorisms: "A brooch is bought, a rosette is made" (`bMlBJn27PEU` [5:10]); "She reads polished, full stop." (`ISAL4NBlshQ` [10:23]).
- The unseen onlooker: "You look rested and nobody could tell you why." (`pgMgC2aGPUw` [2:12]); "the woman at the next table" (4 Diane videos).
- The same staged opening, "Two women…" with matching details ("the same silver hair", "the same navy sweater"), in 5 videos. `Z13YRFrGF2w` and `SZnf4UJCNDk` both open at "Sunday brunch".

Stock phrases also show up in the faceless winners ("It's not you, it's the blouse" in Ever Chic, "it's usually not you, it's the blouse" in Age with Style; "Here's the problem" and "The swap" in Ageless Style). Ours repeat the same ones across many more videos.

**What viewers say.**
- AI remarks: 9 of the 42 viewer comments on our videos (Scarlet 8 of 38, Diane 1 of 4), for example "Are you Scarlet Sterling, Vivienne Morgan or A.I.?" (5 likes, the most-liked comment on `w6w_ktMBHXM`), "AI.  What a stupid video." (`3JBVSs9ETu4`), "I know this is AI but this video contains GREAT info!" (`h9MsF44shdQ`). On the faceless/AI winners: 18 AI remarks in about 790 collected comments (about 2%; Vivian 6, Glow 6). On the real winners: none. The samples differ: ours are every comment on small videos, theirs the top and newest pages.
- The voice: two Scarlet comments say her accent changed between videos: "I just watched another Scarlet Starling and she had a middle American accent. / Now she's got a fake British accent." (`Z13YRFrGF2w`), and "What gives with the silly British accent?" (`SZnf4UJCNDk`).
- Length: "can you commuicate the message more briefly?" (`Z13YRFrGF2w`).

---

## The biggest measured gaps between ours and the winners

Each item gives the gap and its evidence. Nothing here is a rule or a recommendation.

1. **Almost no first person, and no credential.** "I" is 4.1 (Scarlet) and 5.6 (Diane) per 1,000 words, against 23.4 (real), 8.1 (faceless/AI) and 7.1 (pair winners). None of our 38 states a job, years, a client or a past. About 12 of 42 winners do: Vivian, "40 years beside a fitting room mirror"; Ageless Style, "I've worked with hundreds of women over 50". Story markers come in 11 of our 38 and 12 of 21 real winners. Our authority is credited elsewhere: "for generations" in 12 of ours, 0 study scripts.
2. **Almost no "but", fewer questions and less "you".** "But" is 1.0-1.1 against 4.9-6.8 (copies 2.4). Questions: 0.4 and 1.4 against 2.9-3.6. "You": 33.8 and 39.9 against about 49.
3. **The same packaging in every video.** All 38 have a self-introduction block at 0:25-1:16, a book pitch of 148-234 words at 2:18-7:28, and a book, subscribe and comment ending; 25 of 25 Scarlet videos end on the same line. Only 11 of 42 winners introduce anyone at all, and the winners' CTAs vary in size and place. The measure script counts a median of 7 CTA words in ours against 3-4.
4. **The promise is named later and less often.** The title's count is said in the first 20 seconds in 5 of 38 of ours against 12 of 28 winners; "today" or "this video" in 3 of 38 against 13 of 42. 3 of our 8 "Younger" titles say "younger" in speech (all 5 winners do). The time to the first item (median 91 s) is close to the faceless/AI winners' (98.5 s) and longer than the real winners' (50 s).
5. **Imagined scenes instead of pointing at the screen.** "Picture…" or "Imagine…" comes in 36 of 38 of ours against 15 of 42 winners. Pointing at what is shown: 0.25-0.28 per 1,000 against 1.47 (real 2.34). The only on-screen thing ours always name is the QR code (38 of 38; winners 8 of 42).
6. **A recurring house vocabulary.** "Reads as" (33 of 38, 112 uses; study 31 uses in 11), "quietly" (32 of 38; study 6), "from across the room" (18; study 0), "small gold hoops" (22; study 0), "gallery" (20 Scarlet videos; study 3), "book club" (17; study 1). AI remarks are 9 of 42 viewer comments on ours, against about 2% on the faceless/AI winners (different samples).
7. **Prices without brands.** Ours name prices in 34 of 38 and brands in none. Winners name prices in 7 of 42. Real winners name brands and stores freely; faceless winners mostly name neither.
8. **Status and onlookers, more than the body.** Status words come 2.98 times per 1,000 in Scarlet (faceless/AI 1.64, real 0.28). The judgement in ours comes from an imagined stranger ("The woman at the next table quietly decides…"); the winners' comes from the viewer's own mirror, body or age ("make your face look full and drippy").
9. **Longer, at the same pace.** Ours run 12:30-23:40 (median about 16:30) and 2,082-4,078 words, against medians of 11.9 minutes (real) and 15.6 (faceless/AI). The pace is about the same (170 against 156-170 words/min).
10. **Diane's French lens is borrowed.** Marie-Anne speaks as "a French woman living in France" and the AI channel French Fashion as a French woman with a home life. Diane speaks as an American who watches ("so we can borrow it"; "how we buy it here"; "What I see" in 7 of 13), with "the women I know in Paris" as her only tie. She hedges 12% of her 180 claim sentences, close to the winners (10-22%).

---

## What this can't show

- **Why a video won.** There is no retention, click-through, impression or traffic data for either side, and no thumbnails were compared. The winners were picked because they won, so the set holds only 3 flops (the pair copies).
- **Script against format.** I can't separate the script from the AI face, the AI voice or the pictures. The real winners film try-ons and live styling; the faceless winners' pictures are known only from comments. I didn't watch any video, ours included, so what our visuals show is unknown.
- **Age and channel history.** Our channels are 5-6 weeks old with 531 and 62 subscribers; most winners are months or years old on channels with large normals. Our tops against bottoms are mixed up with upload order, topic and title.
- **Topic against script.** Within our channels, the titles (avoid and "NEVER" wording) separate the tops from the bottoms more clearly than any script measure. That is a pattern in 33 videos, not a cause.
- **Comments.** Ours are tiny (42 viewer comments over 38 videos; 9 of 13 Diane videos have none), so every comment-based figure on our side rests on a handful of remarks.
- **Accuracy of the counts.** They are pattern counts on auto-captions. Questions can't be counted on unpunctuated tracks. "Pointing" and "scene" patterns catch some lines that don't do either. Caption errors ("Diana Shambre", "Abento", "bixie") stay as they are. Item word counts come from transcript segments, so their edges are approximate (±20 words).
- **No study match** for 8 of our 38 (makeup, lipstick, concealer, earrings), or for whole necklace and scarf videos; those comparisons use single items from other videos.
