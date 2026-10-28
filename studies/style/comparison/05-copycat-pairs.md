# The copycat pairs: same title, different results

Round 4 analysis, 2026-10-28. Four pairs of videos with the same (or near-identical) title and very different view counts, side by side. This file describes and quotes. It doesn't recommend anything.

**Sources:** `data/<slug>/<id>/` (meta, transcript, comments), `notes/<slug>__<id>.md`, `round2/channels-all.csv`, `round2/outliers-all.csv` and `inputs/operator-list-resolved.csv`. No NexLev calls were made for this file.

**How things are counted here:**
- **Words** are spoken words only, so bracket tags such as "[sighs and gasps]" and ">>" are left out. The totals match `comparison/measures.csv`.
- **Timestamps** are the start of the transcript segment where a quote begins.
- **Item word counts** run from the line that names the item to the line that names the next one. Each count includes that item's bridge into the next item.
- **Words before item 1** is everything spoken before the first item is named, including channel intros and early asks.
- **Age phrases** are "over / after / at / in their" plus 50, 60 or 70, and "50s / 60s / 70s" when they refer to a person's age. Decades such as "the 1960s and 70s" and the channel name "Elegant After 60" are left out.
- **Views per day** is total views divided by age at collection. It's a lifetime average and says nothing about the shape of the view curve.

**Limits of the data:**
- Descriptions were not stored in full. Only the collectors' description notes in `meta.md` are available, so the description rows below compare those notes.
- No thumbnail of these eight videos was read in this study. Round 2 read two outlier thumbnails per channel, and of these eight only `ixlexruRC6c` was among them.
- Subscriber counts are as of 2026-10, not at upload time.
- The study can't see impressions, click-through, retention or traffic sources.

---

## 1. The four pairs at a glance

| | A winner | A copy | B winner | B copy | C winner | C copy | D original | D copy |
|---|---|---|---|---|---|---|---|---|
| Channel | Age with Style | Age with Style | ChicAfterSixty | Ageless Confidence | Chic After 60 | Elegant After 60 | Marie-Anne Lecoeur | Ageless Style 50s & 60s |
| Video | `6byOPawCepI` | `K6N1EFo7oec` | `_OQsPYjIfsQ` | `UTpC6n7KKi0` | `YeKT0zkdIrw` | `ZFx3yIrJqO0` | `ixlexruRC6c` | `Fs17Qc6l8Ug` |
| Type (round 2) | faceless | faceless | AI presenter | not checked | AI presenter | faceless | real | faceless |
| Uploaded | 2025-08-23 | 2025-11-22 | 2026-07-23 | 2026-07-16 | 2025-09-15 | 2026-05-04 | 2025-08-17 | 2026-04-25 |
| Age at collection (days) | 431 | 340 | 97 | 103 | 408 | 177 | 436 | 185 |
| Views | 1,107,951 | 7,133 | 493,468 | 1,048 | 960,045 | 2,229 | 1,038,117 | 267,196 |
| Channel normal | 3,800 | 3,800 | 2,400 | 409 | 37,000 | 2,900 | 84,000 | 4,800 |
| Views ÷ normal | 291.6 | 1.9 | 205.6 | 2.6 | 25.9 | 0.77 | 12.4 | 55.7 |
| Views per day | 2,571 | 21 | 5,087 | 10 | 2,353 | 13 | 2,381 | 1,444 |
| Likes (per view) | 19,359 (1.75%) | 132 (1.85%) | 10,177 (2.06%) | 13 (1.24%) | 11,622 (1.21%) | 105 (4.71%) | 16,665 (1.61%) | 6,009 (2.25%) |
| Comments shown | 823 | 53 | 869 | 1 | 261 | 13 | about 3K | 882 |
| Length | 16:00 | 18:47 | 26:35 | 14:37 | 29:49 | 14:14 | 8:02 | 12:05 |
| Words | 2,658 | 2,852 | 4,424 | 2,481 | 4,084 | 2,484 | 923 | 2,024 |
| Words per minute | 166 | 152 | 166 | 170 | 137 | 175 | 115 | 168 |
| Words before item 1 | 244 | 141 | 294 | 364 | 482 | 177 | 29 | 310 |
| First item named | 1:24 | 0:50 | 1:37 | 2:08 | 3:10 | 1:05 | 0:13 | 1:43 |
| Items | 7 | 7 | 5 | 5 | 8 | 8 | 7 | 7 |
| Words per item | 265-328 | 330-392 | 416-946 | 199-271 | 210-449 | 242-294 | 83-152 | 166-272 |
| Age phrases | 11 | 1 | 8 | 8 | 6 | 4 | 2 | 8 |
| First spoken ask | 1:04 (subscribe) | 0:39 (location) | 10:40 (books) | 3:19 (subscribe) | 29:29 (like) | 13:27 (comment) | none | 1:34 (comment, subscribe) |

**Pair D isn't a flop pair.** The faceless copy has a quarter of the original's views but 55.7× its own channel's normal, against the original's 12.4×. Measured against their own channels, the copy did better. In the other three pairs the copy sits at or under 3× its normal.

**Same channel only in pair A.** In B, C and D the winner's channel has the higher normal: 2,400 against 409 (5.9×), 37,000 against 2,900 (12.8×), and 84,000 against 4,800 (17.5×). Subscribers now: B 12,500 against 219; C 115,000 against 13,000; D 294,000 against 27,100.

---

## 2. How many copies of each title the study can see

Two limits apply to these counts:
- The operator-list counts come from the first 20 YouTube search results, so they are a floor, and the stored note names only the first six copies.
- `round2/outliers-all.csv` lists only videos that are outliers on their own channel (2× or more NexLev's channel mean), so copies that did poorly on their channel are missing from it. Its views are rounded and its dates are approximate.

**A: "7 Blouse Mistakes Women Over 60 Should STOP Making NOW!"**
- Operator list: "16 near-identical titles on other channels".
- The six named: Chic After 60 490,786; Golden Chic Life 3,225; Chic After 60 19,176; Chic After 60 7,764; Elegant Style After 50 46,732; Sylvie Roch Fashion (the view figure is cut off in the stored note).
- Chic After 60 posted the title three times, as Age with Style posted it twice (`log.md`).
- Outliers file, same wording with another number: Beauty of Black Queens "6 BLOUSE MISTAKES BLACK WOMEN OVER 60 SHOULD STOP MAKING NOW!" 14,000; Ageless 360 "9 Blouse Mistakes…" 2,200; Camino de los Ancianos "12 Blouse Mistakes… Need to Stop Making NOW!" 142,000 (a Spanish channel that fails the audience check).
- Age with Style also re-posted a second blouse title, "7 Blouse Mistakes Aging You After 60 And What to Wear Instead": 98,712 and 6,470 on Age with Style, against EverWise Older Women's 105,772.

**B: "Stop Styling Your Fine Hair Like This After 60! 5 Secrets for Instantly Fuller Volume"**
- `videos.csv`: the title "is on about 20 channels".
- Outliers file:
  - ChicAfterSixty 493K (26:35)
  - Stylish60plus 160K (20:45)
  - Senior Fashion Styles 108K (14:45; 173.9× its normal of 621)
  - Vivian Sinclair 101K (18:29)
  - EverWise Older Women 86K ("7 Secrets for Instant Volume", 18:14)
  - KlarerBlick 42K (short title; channel not kept)
- Among the copies the study can see, Ageless Confidence's 1,048 is the low end. Four other copies passed 85K.
- The title's shape ("Styling Your … Hair … 5 Secrets") is also the shape of Justin Hickox's real-stylist "You're Styling Your THIN/FINE Hair WRONG! Do THIS Instead- 5 SECRETS" (1.49M, 14:38, study row 13). The operator list finds 6 near-identical copies of that title, at 3 to 445 views.

**C: "8 COLOR COMBINATIONS That Make Older WOMEN Look EXPENSIVE, Younger and Turn Heads!"**
- Operator list: "19 near-identical titles on other channels".
- The six named: Ageless Glamour 569; Grace & Glow Lifestyle and Timeless Melanin Aura 388; Grace & Glow Lifestyle 2,482; Elegant After 60 2,228 (this copy); Vivian Sinclair 89,092; Glow at Every Age 548.
- Outliers file: Elegant Beyond Age "8 COLOR COMBINATIONS That Make Older Women Look More Expensive, Younger and Turn Heads" 148K (15:10); Graceful Glow Fashion "10 COLOR COMBINATIONS…" 8,300.

**D: "7 Things That Scream 'Old Lady' (Harsh But True): Style Over 50"**
- Outliers file, exact title: Marie-Anne Lecoeur 1.0M; Ageless Style 50s & 60s 267K; EverGrace Style 14K (20:31); Ageless 360 2,400 (25:02).
- Variants:
  - Golden Melanin Lifestyle "…(Harsh But True): Black Women Over 50" 210K
  - Lisa beauty "10 Things That SCREAM "Old Lady" After 60" 132K
  - Marie-Anne Lecoeur's own follow-up "7 Things That Scream 'Frumpy Old Lady'" 106K
  - ELEGANCE AFTER 60. "7 Fashion Mistakes That Scream "Old Lady" After 60 (Harsh But True)" 8,100

---

## 3. Pair A: Age with Style against itself

Same channel, same title, same description template (signed "Sarah"), uploaded 91 days apart. The copy is **a different script**, not a re-cut: different hook, different order, and partly different mistakes.

### Basics
| | Winner `6byOPawCepI` | Copy `K6N1EFo7oec` |
|---|---|---|
| Uploaded / age | 2025-08-23 (channel about 2 months old; joined 2025-06-23) / 431 days | 2025-11-22 (channel about 5 months old) / 340 days |
| Length / words / wpm | 16:00 / 2,658 / 166 | 18:47 / 2,852 / 152 |
| After the list (recap + CTA) | 308 words (14:14 on) | 208 words (17:26 on) |

### Hook (full text)
**Winner, 0:00-0:33, 101 words:**
> "Have you ever stood in front of the mirror wearing a blouse you thought was flattering, but something just felt off? You couldn't quite put your finger on it, but the outfit didn't feel as polished or youthful as you imagined. My friends, it's usually not you, it's the blouse. And the truth is, many women over 60 are still making the same blouse mistakes that secretly drag down their style. But here's the good news. Once you know what to avoid and what to do instead, blouses can become one of the most flattering, confidence boosting pieces in your wardrobe."

It's followed by a 127-word welcome (0:33) that ends in a subscribe ask: "make sure you hit that subscribe button" (1:04) and "trust me, you don't want to miss what's coming next" (1:17).

**Copy, 0:00-0:39, 103 words:**
> "Ladies, have you ever felt like your top is working against you instead of for you? Like no matter what you pair it with, your favorite blouse just makes you feel a little frumpy? Today, we are changing that. Welcome back to Age with Style. Your blouse is the first thing people notice, and honestly, an outdated cut or ill-fitting fabric can instantly add years to your look. But don't worry, in this video, I'm tackling the seven most common blouse mistakes women over 60 make. More importantly, I'm giving you the easy chic alternatives that will have you looking and feeling fabulous."

It's followed by a 38-word location ask: "Where in the world are you watching from" (0:43).

Both hooks open on a mirror or wardrobe question and say "over 60" once. Only the winner has a "not you" reframe.

### First item
- Winner: "mistake one, choosing blouses that are too baggy", 1:24, 244 words in.
- Copy: "Mistake number one, the too boxy blouse" (0:50), 141 words in.

### Items in order, with words
| # | Winner | Words | Copy | Words |
|---|---|---:|---|---:|
| 1 | too baggy (1:24) | 265 | too boxy (0:50) | 392 |
| 2 | too tight or stiff (3:00) | 295 | high-water sleeve (3:25) | 392 |
| 3 | outdated collars and necklines (4:50) | 276 | overly busy small print (5:59) | 347 |
| 4 | loud prints (6:32) | 305 | frumpy fabric (8:21) | 368 |
| 5 | too long (8:32) | 315 | too-high neckline (10:44) | 336 |
| 6 | sleeve styles (10:25) | 328 | over-embellished (12:56) | 330 |
| 7 | fabric quality (12:17) | 322 | mismatched length (15:14) | 338 |

**What the two lists share:**
- Six of the seven topics: fit, sleeves, prints, fabric, neckline and length, in a different order.
- Only in the winner: "too tight or stiff". Only in the copy: "over-embellished".
- The same fixes: the French tuck, the 3/4 sleeve, and the same jewel-tone triple ("sapphire blue, emerald green, or ruby red", winner 7:58; "sapphire blue, emerald green, ruby red", copy 7:47).
- The copy's items run about 60 words longer each.

### Item shape
**Winner:**
- Opens "Mistake [n], [name]".
- Then why women do it ("So many women over 60 fall into this trap", 1:29; "we've been told for years", 1:32).
- Then a turn ("So, what's the solution?", 3:59; "The good news is"; "So, what works beautifully?").
- Closes on a one-line rule ("So, remember this. Your blouse should frame you, not drown you.", 2:51).

**Copy:**
- Opens "Mistake number [n], the [name]", then restates it ("Mistake number two is a small detail…").
- Then the failure, then "The elegant alternative" (1:50), "The sophisticated alternative" or "The fashionable alternative".
- Closes on an instruction ("Make it a habit", 5:54; "If it stops right at your widest point, put it back", 17:14).
- It cross-refers to earlier items ("the French tuck we just discussed", 5:41).

### Feelings voiced
| Winner | Copy |
|---|---|
| "something just felt off" (0:04), frumpy | "your favorite blouse just makes you feel a little frumpy" (0:07), frumpy |
| "baggy just looks like the blouse belongs to someone else" (2:03), frumpy | "add years to your look" (0:24), older |
| "looking closed off and a little frumpy" (5:32), frumpy | "more like you've simply pulled on a sack" (1:33), frumpy |
| "unfortunately age you instead of enhancing you" (7:01), older | "where we are often least comfortable drawing attention" (11:29), self-consciousness |
| "Clothes should never make you feel trapped" (4:32), comfort | "I know what I'm doing" (5:13), confidence |
| "You've earned the right to dress in a way that makes you shine" (14:47), permission | "honor your beautiful, experienced body" (17:55), permission |

"Frumpy" is said once in the winner and 5 times in the copy.

### Age said
- Winner: 11 age phrases. "over 60" 10 times ("So many women over 60 fall into this trap", 1:29), plus "at 60,70 and beyond".
- Copy: 1 ("blouse mistakes women over 60 make", 0:29). Otherwise "at any age" twice and "as we age".

### Reassurance and shame
**Winner:**
- Reassurance: "My friends, it's usually not you, it's the blouse" (0:11); "don't panic. You can make it work" (2:26); "every single one of these mistakes has an easy fix" (14:22); "You are not too old and it is never too late to look amazing" (15:49).
- Could read as shaming: "frankly unkind to you" (3:56); "stop punishing yourself with stiff, tight blouses" (4:38); "One of the most common mistakes I see women over 60 make" (5:02).

**Copy:**
- Reassurance: "But don't worry" (0:24); "none of these seven changes are complicated" (17:26).
- Could read as shaming: "Donate them or save them strictly for messy chores" (2:45); "Stop letting your clothes wear you" (3:18); "creating a visual disaster zone" (15:26); "look juvenile" (13:23).

### Held finale or teases
- Winner: no held item, only "trust me, you don't want to miss what's coming next" (1:17). No next-video tease.
- Copy: none of these.

### CTAs and the ending
**Winner:**
- Subscribe and bell before the list (1:04).
- At 15:20: like, subscribe, and "let me know in the comments which blouse mistake you've been guilty of" (15:37).
- Last words: "Until next time, remember this. You are not too old and it is never too late to look amazing. Age with style, my loves, because you deserve nothing less."

**Copy:**
- The location ask before the list (0:43).
- At 18:07: "which mistake are you going to stop making first?", then like and subscribe.
- The location ask again: "Tell me again, where in the world are you watching from?" (18:38).
- Last words: "I'll be reading through those comments. I'll see you next time."

### Description (from the meta notes)
- **Same template.**
- **Winner:** "SUBSCRIBE for new videos everyday"; "Let me know which mistake you’re saying goodbye to—I read every single comment!"
- **Copy:**
  - says "every week" and leaves a placeholder unfilled: "SUBSCRIBE for new videos every week ► [Insert Channel Link Here]"
  - lists its seven mistakes
  - repeats the location ask: "tell me where in the world you are watching from!"

### Comments about thumbnails or pictures
No comment on either video says "thumbnail".

**Winner, 11 of 42 comments are about the women or images shown:**
- "How many women in their 60 -  70’s etc have lovely slim body shape that are always shown in these videos." (1.1K likes, the top comment)
- "I think if a plus size model was used side by side with the slim model it would give a more visual example" (403)
- "I love how these videos use women who look like professional models." (134)
- "That baggy blouse on the first shot look fine to me!" (109)

**Copy, 2 of 29:** "The model has no stomach and can wear her shirts tucked in" (0); "we are not AI perfect older people" (0).

### Comment reactions
**Winner:**
- Wear-what-I-like replies, about 7: "I wear what I want, when I want, where I want, why I want, and how I want." (343); "I'm 62, I wear whatever I feel comfortable!" (363).
- Bras, 2: "a good bra that fits and supports properly" (233).
- Pushback: "I HATE that just tucked in the front look" (226).
- Ages given: 62, 65, 80, almost 80, 84.

**Copy:**
- 24 of 29 answer the location question.
- Bellies, 2.
- Pushback: "I am tired of so called experts telling us what we should wear." (0).
- No ages given.

### Script and not-script differences
**Script:** a different text under the same title; a "not you" reframe only in the winner; "over 60" 11 times against once; subscribe-first against location-first; shorter items in the winner; a longer close in the winner.

**Not script:**
- the upload date (August against November)
- the copy being the channel's second use of a title that already had about 1M views, so its audience may already have seen it
- the thumbnails (not read)

---

## 4. Pair B: ChicAfterSixty against Ageless Confidence

Near-identical titles. The winner has "Fine Hair … in 2026", the copy "FINE HAIR" with no year. **The copy was uploaded first, seven days earlier.** The winner's channel had 12,500 subscribers and a normal of 2,400; the copy's had 219 subscribers, 16 videos and a normal of 409.

### Basics
| | Winner `_OQsPYjIfsQ` | Copy `UTpC6n7KKi0` |
|---|---|---|
| Uploaded / age | 2026-07-23 / 97 days | 2026-07-16 / 103 days |
| Length / words / wpm | 26:35 / 4,424 / 166 | 14:37 / 2,481 / 170 |
| Presenter as heard | a woman over 60 in the first person, no name, own stories | a hairstylist in the first person ("in my chair"), no name or gender, client stories |

### Hook (full text)
**Winner, 0:00-1:37, 294 words:**
> "You just caught your reflection in the hallway mirror, and your hair looked flat again. Pressed to your scalp, thinner on top than you remember it being. You patted it, smoothed it down, and let out that little sigh you've been letting out for years now. Stop. Put your hand down. Because the way you have been styling your fine hair is the exact thing making it look thinner. Not your age, not your genes, the styling. The rules you were handed decades ago and never once questioned. I know this because I followed those same rules for almost 30 years, and every single one of them was quietly working against me. Here is what I finally learned. Fine hair is not the problem. Fine hair worn the way a 1980s magazine told you to wear it is the problem. And once I found the buried salon techniques from the 1960s, the ones stylists used before the product companies rewrote everything, my hair looked fuller in one afternoon than it had in a decade. I still remember standing in my mother's old bathroom using her can of stiff hair spray because that is what you were supposed to do, and wondering why my hair looked like a helmet with the scalp showing through anyway. It took me years to understand I had been taught backwards. None of what I am about to show you costs much. Most of it costs nothing. It works with the hair on your head right now, today, exactly the length it is. You do not need extensions. You do not need a keratin treatment. You do not need to be brave enough to chop it all off. You just need to stop obeying five rules that were never true."

(The track's "[sighs and gasps]" tag after "and" is left out.)

**Copy, 0:00-2:08, 364 words** (the captions open on a stray "Top."):
> "If you're over 60 and you have fine hair, don't touch a brush, a dryer, or a single product this morning until you hear this. Your hair likely isn't thinning the way you think it is. It's being styled in a way that makes it look thinner than it actually is. And here's the proof. Two photos. Same woman, same warning, same amount of hair on her head. In one, her scalp shows straight down the center and she looks tired before she's even left the house. In the other, her crown has real lift. Her part looks half as narrow and she looks years younger. Nothing changed between those two photos except technique. Not a haircut, not a supplement, not a single new strand. I've worked with fine hair on women over 60 for a long time and I hear some version of the same sentence almost every week in my chair. My hair used to be so full. I don't recognize myself in photos anymore. I think I'm going bald. One client, I'll call her Susan, told me almost exactly that the first time she sat down, she'd already started looking at wigs and spending her evenings searching thickening treatments online. Keep her in mind because I'll tell you what changed for her by the end of this video. More often than not, when we actually look at the scalp, the hair is still there. It's just been trained morning after morning to lie in exactly the wrong direction and nobody ever explained why. Today, I'm giving you five secrets that instantly add volume to fine hair after 60, counting down from five to one because the first secret only works once you understand the last. Skip it and you'll be doing everything else right next month and still wondering why nothing changed. And every one of these five is a habit, which means every single morning you keep doing it the old way. The gap gets a little wider than it was yesterday, a little more visible than it was last week. That's the part nobody tells you. And it's also exactly why fixing it now matters more than waiting."

**How the two hooks differ:**
- The winner opens on a second-person mirror scene and a command, then gives her own 30 years.
- The copy opens on a command and an on-screen two-photo "proof", then a quoted client.
- The copy has three hooks that the winner lacks: a countdown device, a story held to the end (Susan), and a cost-of-waiting line.

### First item
- Winner: "Let me start with the biggest one" (1:37), with the rule stated at 1:48 ("The rule goes like this").
- Copy: "Secret number five" (2:08).

### Items in order, with words
| # | Winner (as five "rules" to break) | Words | Copy (counted down) | Words |
|---|---|---:|---|---:|
| 1 | from 1:37, the rule "When your hair gets thin, cut it short" (1:48); keep length, blunt edge | 518 + 428 on where the rule came from (salons, magazines) = 946 | 5. move your part (2:08) | 201 |
| | | | subscribe and comment ask (3:19) | 64 |
| 2 | heavy conditioner (7:28); condition ends only, protein, clarify | 515 | 4. don't brush straight back (3:42) | 239 |
| | book plug (10:40) | 81 | 3. no regular brush on wet hair (5:11) | 217 |
| 3 | from 11:08, the rule "Dry your hair the way it falls" (11:50); upside-down drying, move the part, cool shot | 589 | "Quick pause" subscribe ask and hold (6:28) | 98 |
| 4 | from 14:29, the rule "Shiny hair is healthy hair" (14:50); dry-shampoo texture | 416 | 2. dry the roots upward (6:56) | 199 |
| 5 | overdirection, the held last rule (17:09) | 845 | 1. products on mid-lengths and ends only (8:06) | 271 |
| after | recap 248 (22:04), close 175, CTAs 315 | 738 | why it happens 285 (9:45), consistency 78, Diane story 265, Susan payoff 42, CTAs 158 | 828 |

**What the two lists share:** three ideas, placed differently.
- Moving the part: inside the winner's rule 3; the copy's secret 5.
- Drying with the roots lifted: winner's rule 3; copy's secret 2.
- Keeping conditioner and product off the roots: winner's rule 2; copy's secrets 3 and 1.

**Only in the winner:** keep length with a blunt cut, matte texture over shine, overdirection, the cool shot, and the history of who made the rules.

**Only in the copy:** tension from brushing straight back, and wet-brush breakage.

### Item shape
**Winner:**
- Opens on the received rule in quotes ("The rule goes like this", 1:48; "Here is the rule").
- Then the truth or "the science" ("Fine hair is a measurement, not a curse", 2:34), the fix, and a personal result ("I nearly cried in the bathroom").
- Closes on a bridge to the next rule: "But cutting length was only the first way we were led astray." (7:28); "that is where the third rule lives" (11:10); "there's a fourth rule" (14:34).

**Copy:**
- Opens "Secret number [n]" plus a claim ("ages the face more than almost anything else on this list, and most women have no idea they're doing it", 3:47).
- Then a "Stop…" or "Never…" command, the mechanism with a figure, and the fix ("The fix costs nothing", 3:00; "Try this instead", 4:34).
- Closes on a time-to-result line ("within a couple of weeks, you'll notice less hair left behind on your comb", 6:21) or a size claim ("It's genuinely one of the smallest habit changes", 5:03).

### Feelings voiced
| Winner | Copy |
|---|---|
| "You just caught your reflection in the hallway mirror" (0:00), older | "she looks tired before she's even left the house" (0:28), older |
| "the short, tidy, invisible style of a woman who had accepted she was no longer being looked at" (6:10), invisible | "My hair used to be so full. I don't recognize myself in photos anymore. I think I'm going bald." (0:54), loss, fear |
| "every year I felt a little more erased" (6:55), invisible | "This should give you hope instead of dread." (11:11), hope |
| "I was furious" (5:01), rebellion | "she believed this was simply what happened to her at her age" (12:29), resignation |
| "This is fine for women with money" (11:21), money | "more compliments in those 2 weeks than in the previous 10 years combined" (13:23), being seen |
| "You did not lose your fullness. It was taken from you one rule at a time" (24:13), rebellion, permission | |

### Age said
- Winner, 8: "over 60" 3, "after 60" 2, "in their 60s and 70s" (two), "my 50s". "barely 70 years old" is said of the rule and isn't counted. Menopause is named once.
- Copy, 8: "over 60" 3, "after 60" 5; menopause once.

### Reassurance and shame
**Winner:**
- Reassurance: "Not your age, not your genes, the styling" (0:21); "Fine hair is a measurement, not a curse" (2:34); "it was never you. It was never your hair. It was the instructions" (24:08); "None of this requires money" (23:40).
- Shame-adjacent lines point at habits: "That instruction is why your hair is flat" (11:58); "I promise you are doing it right now tonight" (7:33).
- The blame goes to salons, magazines, "the beauty industry" and product companies.

**Copy:**
- Reassurance: "Your hair likely isn't thinning the way you think it is" (0:09); "You likely have close to the same number of strands you had two decades ago" (10:32); "None of this requires an expensive treatment, a supplement, or a procedure" (11:14).
- Could read as shaming: "most women have no idea they're doing it" (3:47); "every single morning you keep doing it the old way" (1:54); "I can usually tell just from someone's hairline whether she wore tight buns" (4:27).
- The foil is "nobody ever explained why".

### Held finale or teases
**Winner, three devices:**
- the last rule held: "the one I saved for the end" (17:16)
- a spoken bridge between every pair of rules
- a next-video tease: "Because next I am going to show you the one thing about hair color after 60 that every salon gets wrong" (25:13)

**Copy, five devices:**
- the countdown ("the first secret only works once you understand the last", in the hook)
- Susan held to the end ("Keep her in mind", 1:15; paid at 13:30)
- "Two secrets left and I need you to stay for both of them" (6:40)
- "Four down, one to go. And this is the mistake I promised you at the very start." (8:06)
- a next-week tease ("next week I'm covering the one product ingredient silently aging fine hair", 14:04)

### CTAs and the ending
**Winner:**
- Books mid-video: "I have put it all together in my books, Style Reset, Style Deeper, and Styled Complete" (10:50).
- At 24:34: "So, tell me, which of these rules did you follow the longest?", plus the location ask and subscribe.
- The next-video tease (25:13).
- A paid circle: "Inside the Timeless Elegant Circle" (25:54), "you can cancel anytime".
- Last words: "If this helped you, do subscribe and stay with me here. I have many more simple hair tips just like these, um, made especially for you, and I would love to keep helping."

**Copy:**
- "If that just made you rethink your part, hit subscribe now" (3:19).
- "Quick pause. If this is helping already, subscribing means…" (6:28).
- At 13:55: "Come back and tell me how it goes", comment, subscribe, share.
- Last words: "this is just what happens to hair after 60. It isn't. And now you both know it. Thank you for watching all the way through and I'll see you in the next one."

### Description (from the meta notes)
**Winner:**
- opens on a book link ("📘 This book helps you build a timeless, elegant wardrobe with confidence.") and "Join The Timeless Elegance Circle"
- "This is for every woman over sixty who has been told her best hair days are behind her. They're not."

**Copy:**
- "begins with the literal word 'DESCRIPTION' then hashtags"
- "A longtime hairstylist breaks down the five daily habits secretly flattening fine hair after 60"
- a six-point list including "Two real client transformations"
- a dermatologist disclaimer

### Comments about thumbnails or pictures
None on either video. The winner has one remark on the voice: "To those who don’t like the AI voice, get over it." (49).

### Comment reactions
**Winner, 46 collected:**
- About 20 give an age and place in answer to the end question.
- Ages given run from 61 to 84 (18 ages).
- Agreement includes "I qualified as a hairdresser in 1977 … I agree with everything this lady has said." (87).
- A viewer posted a timestamped summary (86).
- Too slow: "Well, I'll listen to this next time I have insomnia!" (58).
- A husband story: "husband argued that I looked like an old hag" (228).
- Pushback: "I have a hair dresser who knows what is best for my hair!" (44).

**Copy:** one comment in total: "I just turn 67 and I have to cut my hair short bc of arthritis in my left shoulder." (1).

### Script and not-script differences
**Script:**
- 26:35 and 4,424 words against 14:37 and 2,481
- a myth-busting frame ("five rules that were never true") against a countdown of secrets
- a named adversary (the industry) against none
- the narrator's own stories against client stories
- the copy's earlier subscribe asks (3:19, 6:28) and more retention devices

**Not script:**
- the channels: 219 subscribers against 12,500, and a normal of 409 against 2,400
- the copy was posted first
- the title's casing and the year "in 2026"
- the presenter: the winner's channel shows a recurring generated woman; the copy's type was never checked
- the thumbnails (not read)

Four other copies of this title passed 85K, including a 14:45 one (Senior Fashion Styles), so the copy's 14:37 length isn't unique to the flop.

---

## 5. Pair C: Chic After 60 against Elegant After 60

Identical titles. The winner's channel has a normal of 37,000; the copy's has 2,900. The copy went up on 2026-05-04, six days after the copy's channel posted its own 698,146-view hit, "DON’T Get a "Granny" Cut!" (`XR3IwlcIcCY`, 2026-04-28), a hair title.

### Basics
| | Winner `YeKT0zkdIrw` | Copy `ZFx3yIrJqO0` |
|---|---|---|
| Uploaded / age | 2025-09-15 / 408 days | 2026-05-04 / 177 days |
| Length / words / wpm | 29:49 / 4,084 / 137 | 14:14 / 2,484 / 175 |
| Narrator as heard | first person, no name, "our style" | the channel, not a person ("This is Elegant After 60"), no name |

### Hook (full text)
**Winner, 0:00-1:22, 226 words:**
> "The richest women in the world don't always wear diamonds or designer logos. Their secret, they know how to use color. Because color speaks before you do, it whispers luxury. It radiates youth and it has the power to turn heads without a single word. Now after 60, our style needs to work harder for us. The wrong shade can drain the life from your skin, but the right combination can light up your face, smooth your lines, and make you look like the most confident woman in the room. In this video, I'll share eight powerful color combinations that every elegant woman should know. These are not passing trends. They're timeless palettes worn by the world's most sophisticated women. And here's the best part. You don't need a designer wardrobe. These colors work in everyday outfits with pieces you likely already own. Imagine the quiet confidence of navy and white. The glow of blush, pink, and gray, the richness of burgundy, and cream. These combinations don't just make you look younger. They make you look expensive without saying a single word. So, if you're ready to dress not just your body, but your confidence, stay with me. By the end of this video, you'll see that age doesn't limit beauty. In fact, it gives it a new kind of power. Let's step into it together."

It's followed by a 256-word "why color matters" section (1:22), including "Studies in color psychology show that certain pairings communicate qualities like authority, trust, vitality, or calmness" (2:36).

**Copy, 0:00-1:05, 177 words** (channel intro included):
> "Most women over 60 are told to blend in, to wear safe neutrals, and disappear. But look at her. That's not just an outfit. That's a navy and champagne power play that says CEO and icon in the same breath. Today, I'm showing you the eight color secrets that act like an instant facelift and make you the most expensive looking woman in any room. Ready to turn some heads? Welcome back, lovely. This is Elegant After 60, and if you're new here, we believe that style doesn't have an expiration date. It only gets more refined. We've all felt it, that day you look in the mirror and feel a bit washed out. It's not you, it's your palette. As we move into our 60s and beyond, our skin undertones shift and our hair transforms into a crown of silver or white. The safe colors you wore in your 40s, they're actually aging you. Today, we're using color theory to cheat the clock. We're talking about eight specific pairings that scream luxury without saying a word. Let's dive back into our first showstopper, navy and champagne."

**How the two hooks differ:**
- The winner opens on a status line about "the richest women", then names three of its pairings.
- The copy opens on being told to "blend in", then points at the screen ("But look at her", 0:06) and adds a "not you" reframe ("It's not you, it's your palette", 0:37).

### First item
- Winner: "Our first color combination" (3:10), 482 words in.
- Copy: "One, navy and champagne" (1:05), 177 words in.

### Items in order, with words
| # | Winner | Words | Copy | Words |
|---|---|---:|---|---:|
| 1 | navy and white (3:10) | 384 | navy and champagne (1:05), nicknamed "the old money classic" | 251 |
| 2 | beige and black (5:55) | 432 | charcoal gray and soft blush (2:32) | 263 |
| 3 | soft gray and blush pink (9:06) | 449 | emerald green and gold (3:59) | 256 |
| 4 | white and camel (12:28) | 449 | espresso and sky blue (5:31), nicknamed "the crisp morning" | 263 |
| 5 | burgundy and cream (15:42) | 408 | winter white and camel (7:02) | 266 |
| 6 | soft teal and charcoal gray (18:50) | 446 | plum and burnt orange (8:32) | 257 |
| 7 | olive green and ivory (22:05) | 210 | silver and lavender (10:02), nicknamed "the luminous queen" | 294 |
| 8 | chocolate brown and powder blue (23:38) | 444 | red and stone (11:44), nicknamed "the power player" | 242 |
| after | "how do I know which ones are right for me?" 337 (27:07), CTA 43 | 380 | recap 62 (13:08), CTA 143 | 205 |

**What the two lists share:** four pairings, near-identical.
- navy with white or champagne
- gray or charcoal with blush
- white or winter white with camel
- chocolate or espresso with powder or sky blue

**Only in the winner:** beige and black, burgundy and cream, teal and charcoal, olive and ivory.

**Only in the copy:** emerald and gold, plum and burnt orange, silver and lavender, red and stone.

The winner's item 7 is short (210 words). After its name it goes straight to "Gold jewelry works beautifully with this pairing" (22:13), with no symbolism or outfit list.

### Item shape
**Winner:**
- Opens "Our [nth] color combination is one of the most…" plus the name.
- Then what each color symbolizes, "As we age…", four labelled outfit formulas ("Everyday chic.", "Cold weather classic."), accessories, imagined scenes ("Imagine stepping onto a cruise ship in a navy linen dress with a white sun hat.", 5:13) and a luxury-house line.
- Closes on a summary claim ("It's the color pairing that never goes out of style", 5:46; "This combination says, "I am refined. I am timeless. and I don't need to shout to be noticed.", 18:42).

**Copy:**
- Opens "Combo [n], [name]" with a nickname.
- Then a skin or hair reason, a texture tip, and a jewelry, shoe or makeup tip.
- Closes on a lead-in that teases the next item, in seven of the eight items. Two are questions ("But what if you want to look like you just walked out of a high-end jewelry vault?", 3:50).
- It points at the screen: "And notice the jewelry" (1:59); "Notice what happens the moment we add the blue" (5:50).

### Feelings voiced
| Winner | Copy |
|---|---|
| "The wrong shade can drain the life from your skin" (0:19), older | "Most women over 60 are told to blend in" (0:00), invisible |
| "make you look like the most confident woman in the room" (0:29), being seen | "that day you look in the mirror and feel a bit washed out" (0:35), older |
| "They make you look expensive without saying a single word." (1:05), money | "the difference between looking like you're heading to a board meeting and looking like you own the company" (1:42), status |
| "age doesn't limit beauty. In fact, it gives it a new kind of power." (1:17), permission | "Who is she?" (3:59), being seen |
| "Too much black on its own can exaggerate that, creating shadows and making us look tired." (6:53), older | "the energy of a woman half your age" (12:00), younger |
| "let your choices tell the story of a woman who knows her worth" (29:27), worth | "You've spent decades building your life" (13:23), permission |

"Expensive" is said 7 times in the winner and 13 times in the copy.

### Age said
- Winner, 6: "after 60" 2, "at 60" 1, "over 60" 3. "As we age" or "as we get older" is said 8 more times.
- Copy, 4: "over 60" 2 ("Most women over 60", 0:00; "what it means to be a woman over 60", 13:58), "after 60" 1, "our 60s" 1. It also says "your 40s" once, and the channel name "Elegant After 60" twice.

### Reassurance and shame
**Winner:**
- Reassurance: "You don't need a designer wardrobe." (0:45); "The best color combination is the one that makes you feel authentic, confident, and aligned with your lifestyle." (28:15).
- Could read as shaming: "the neon red that looked exciting at the 30th of May now overwhelm your complexion at 60" (1:53, as captioned); "Bright pinks can sometimes look juvenile" (12:10).

**Copy:**
- Reassurance: "It's not you, it's your palette" (0:37); "turns the sign of aging into your most expensive accessory" (10:20); "You've earned every bit of that attention" (14:06).
- Could read as shaming: "The safe colors you wore in your 40s, they're actually aging you" (0:48); "Most women reach for black" (1:08); "While others are playing it safe in beige" (8:43).

### Held finale or teases
- Winner: "stay with me. By the end of this video, you'll see that age doesn't limit beauty" (1:12); "And now, let's look at the first combination, one that's as fresh today as it was a century ago" (3:05); "Our eighth and final combination" (23:38). No held item.
- Copy: a teasing lead-in at the end of 7 of 8 items. No held item.

### CTAs and the ending
**Winner:**
- Nothing is asked until 29:29: "If you found this video inspiring, don't forget to like it, share it with a friend, and subscribe" (43 words).
- Last words: "Because elegance is not about age, it's about attitude. And it's never too late to shine."
- The description's ebook is not mentioned in speech.

**Copy:**
- Nothing is asked until 13:27: "I want to hear from you. Which of these eight combinations made your heart skip a beat?", then like, subscribe and bell.
- Last words: "Go out there, wear your colors with pride, and keep turning those heads. You've earned every bit of that attention. This is Elegant After 60, and I'll see you in the next video."

### Description (from the meta notes)
**Winner:**
- first line: "Discover the 8 best clothing color combinations that make women over 60 look instantly younger, more radiant, and effortlessly stylish."
- an ebook link
- promised "bonus tips" on finding your shades, paid in speech at 27:07

**Copy:**
- "From the "Old Money" elegance of Navy & Champagne to the "Luminous Queen" glow of Silver & Lavender"
- "reclaim your visibility"
- hashtags including #SilverEconomy and #ClassicChicLab

### Comments about thumbnails or pictures
**Winner, 2 of 43:** "Would be nice to see everyday women used instead of models." (12); "These women have no weight problems." (27).

**Copy:** none of 8.

### Comment reactions
**Winner, 43 collected:**
- Lists and timestamps, 3: "Navy and White, Beige and Black, Soft Grey and Blush Pink, White and Camel" (238).
- Favourites, about 8.
- Skin-tone objections, about 6: "How can you say that these colours suit every type of person?" (0).
- Belts: "I do miss seeing  a belt on the pants." (40).
- Too long: "So much unnecessary talking…just get to the point…geez" (0).
- Eleven of the 43 come from accounts named like style channels.
- Ages given: 60+, 68, 69, 71, 73.

**Copy, 8 collected:**
- Favourites, 5: navy and champagne 3 ("Navy and champagne for me too!🥂", 0).
- Thanks, 3.
- One objection: "These are lovely suggestions, but also very continental. Not going to work in South Africa." (2).

### Script and not-script differences
**Script:**
- 29:49 and 4,084 words at 137 wpm, against 14:14 and 2,484 at 175 wpm
- a 482-word lead-in with a "psychology" section, against 177 words
- symbolism, outfit formulas and scenes, against nicknames and teasers
- four different pairings
- a channel voice against a first-person voice

**Not script:**
- the channel's normal (37,000 against 2,900)
- the copy came eight months after the winner and six days after its own channel's hit on another topic
- the thumbnails (not read)
- the presenter (round 2 reads the winner's channel as generated women in staged settings)

---

## 6. Pair D: Marie-Anne Lecoeur (real) against Ageless Style 50s & 60s (faceless)

The exact title, word for word, eight months later. Here the copy is also a breakout on its own channel (55.7×), so this pair is an original against a successful copy, not a winner against a flop. The pair is also set out in `notes/ageless-style-50s-60s__Fs17Qc6l8Ug.md` ("Against the original").

### Basics
| | Original `ixlexruRC6c` | Copy `Fs17Qc6l8Ug` |
|---|---|---|
| Uploaded / age | 2025-08-17 / 436 days | 2026-04-25 / 185 days |
| Length / words / wpm | 8:02 / 923 / 115 (pauses and sound effects) | 12:05 / 2,024 / 168 |
| Presenter | herself on camera, French, in France; credentials only in the description | unnamed first person, "I've worked with hundreds of women over 50" (0:50); gender not stated |

### Hook (full text)
**Original, 0:00-0:13, 29 words:**
> "Are you ready for little tough love? Today I'm revealing seven things that instantly scream old lady. And what to wear instead to look instantly modern, fabulous, and chic."

**Copy, 0:00-1:43, 284 words, then a 26-word comment ask:**
> "If you want to look older, tired, and invisible, please keep doing these seven things. Seriously, keep doing them because they work incredibly well at making you disappear. But, if you actually want to feel like yourself again, if you want people to actually see you when you walk in a room, then the next 5 minutes are going to feel like a cheat code because I'm about to tell you the exact seven things that are aging you without you even realizing it. No products, no surgery, no dressing younger. Just seven specific things to stop doing today. Now, here's the thing, and I need you to really hear this. You've probably been told that aging gracefully means accepting where you're at or embracing the process. And yes, that's true. But, nobody told you that embracing yourself doesn't mean accepting things that are actively making you feel invisible. I've worked with hundreds of women over 50, and every single one who felt stuck, frumpy, or like they'd lost their identity, they were doing at least four of these seven things. Four, without even knowing it. So, here's my promise to you. By the end of this video, you'll know exactly what's holding you back. And more importantly, you'll know what to do instead. But, I'm not just going to list them. I'm going to show you why each one ages you, and the simple swap that changes everything. The very last thing on this list, it's the one women fight me on the most, but it's also the one that makes the biggest difference. I've saved it for last, so you have to stay until the end. Let's start with number one. Ready? Before we begin, comment style in the comments if you're ready to break free from these old patterns, and subscribe so you don't miss the transformation."

### First item
- Original: "The first thing that scream old lady look is baggy, shapeless clothes" (0:13), 29 words in.
- Copy: "The first thing, the oversized dress" (1:43), 310 words in.

### Items in order, with words
| # | Original | Words | Copy | Words |
|---|---|---:|---|---:|
| 1 | baggy, shapeless clothes (0:13) | 123 | the oversized dress (1:43) | 272 |
| 2 | closed necklines (1:25) | 118 | the hair that stopped trying (3:25) | 189 |
| 3 | head-to-toe beige (2:32) | 130, plus a 37-word "harsh" aside (3:44) | the shoe that says "I've given up" (4:33) | 166 |
| 4 | clumpy shoes (3:59) | 131 | the pattern that traps you (5:33) | 174 |
| 5 | twee prints (5:03) | 90 | the lipstick you've worn since 1985 (6:39) | 186 |
| 6 | untucked tops (5:58) | 152 | the handbag (7:48) | 195 |
| 7 | aging hairstyles (7:17) | 83 | the way you carry yourself, held (9:05) | 227 |
| after | end card (7:51) | 30 | recap and reassurance 149 (10:23), four-step CTA 156 (11:09) | 305 |

**What the two lists share:** shapeless clothes, shoes, prints and hair (hair moved from last to second).

**Dropped by the copy:** necklines, beige, tucking.

**Added by the copy:** lipstick, handbag, posture (the held finale).

### Item shape
**Original:**
- Opens "The next thing that scream(s) old lady is…".
- Then the problem and "So, what can you do instead?" (0:51).
- Closes on "My pro tip is…" ("My pro tip is tailored, not baggy", 1:25; "My pro tip is over is over", 7:07). Six of the seven items have it; hair has none.

**Copy:**
- Opens "The [nth] thing, [title phrase]".
- Then "Here's the problem" (4:49) or "Here's the thing".
- Then "The swap, …" (3:07), in all seven items.
- Closes on a promised result: "Your whole outfit will thank you" (5:30); "I promise you people will treat you differently" (10:19).

### Feelings voiced
| Original | Copy |
|---|---|
| "hiding behind tons of fabric because they have lost their self-confidence" (0:35), confidence | "If you want to look older, tired, and invisible" (0:00), invisible, older |
| "square, oldfashioned, stuck in the past" (1:59), older | "if you want people to actually see you when you walk in a room" (0:13), being seen |
| "you disappear faster than a macaron at a Parisian cafe" (2:48), invisible | "felt stuck, frumpy, or like they'd lost their identity" (0:55), frumpy, identity |
| "beige equal invisible plus old lady" (3:39), invisible | "And when you're over 50 and feeling self-conscious about your body" (1:54), body |
| "You can have comfort and style." (4:33), permission | "like you're trying too hard to look like you used to" (7:10), older |
| "open up your neckline, open up your self-confidence" (2:26), confidence | "It's about deciding that you deserve to be seen." (10:06), permission, being seen |

"Old lady" is said 10 times in the original and 3 in the copy. "Invisible" is said once in the original and 6 times in the copy; "disappear" once against 5 times.

### Age said
- Original, 2: "neck areas we women over 60 want to elongate" (1:47) and "even in our 70s and over". The title says 50.
- Copy, 8: "over 50" 8 times, plus dates used as age markers ("since 1995", "since 1985").

### Reassurance and shame
**Original:**
- Reassurance: "I told you I was going to be harsh. Not on you, but your clothes." (3:44); "Comfort is non-negotiable. I agree with you." (4:04).
- Could read as shaming: "hide what little self-confidence they may have left" (0:44); "But those clunky, sensible shoes, no mercy." (4:10); "Say no to gladiator sandals or hobbit feet styles." (4:49); "this highlights your tummy or you love handles" (6:32).

**Copy:**
- Reassurance: "This video wasn't meant to shame you. It was meant to wake you up. You are not invisible." (10:32); "You don't need a complete wardrobe overhaul" (10:55); "I'm not saying you need to suffer" (4:56).
- Could read as shaming: "you look like you're wearing your mother's nightgown" (2:21); "I've stopped caring about how I look" (2:36, the narrator's reading of comfort dressing); "starts being the old lady helmet" (3:43); "the world has been giving you feedback you didn't deserve" (10:48).

### Held finale or teases
- Original: none.
- Copy:
  - "I've saved it for last, so you have to stay until the end" (1:28), paid with "It's the way you carry yourself" (9:17)
  - "the next 5 minutes" (0:16), though the list runs about 8.5 minutes

### CTAs and the ending
**Original:**
- No like, subscribe or comment request anywhere.
- Last words: "A shorter cut is youthful, my lovely ladies. I hope you enjoy these things that scream old lady. But if you want to find out the fashion mistake that make you look older, watch the video on screen" (from 7:47).

**Copy:**
- "Before we begin, comment style in the comments…" and subscribe (1:34).
- At 11:09, "Here's what I want you to do next": pick one thing, comment, subscribe, share.
- Last words: "Because the truth is none of us have to do this alone. You are not invisible. You never were. Now go change that one thing. I'll see you in the comments."

### Description (from the meta notes)
**Original:**
- "Bonjour, I am Marie-Anne Lecoeur a fully trained personal stylist and member of The Federation of Image Professionals. I have written two best-selling Amazon books on style"
- a free ecourse, 15 affiliate "LINKS TO YES PIECES", a masterclass, journals, an Amazon storefront and a not-sponsored disclaimer
- A pinned owner comment sells an "Instant Youth System".

**Copy:**
- "we" voice: "we’re breaking down the 7 common style mistakes that unintentionally scream "old lady""
- its "What We’re Covering" list ("Matching" trap, fabrics) doesn't match the seven items spoken
- a closing quote attributed to Rachel Zoe

### Comments about thumbnails or pictures
**Original, 2 of 42:**
- "all your lovely examples are slim ladies with waists!" (440)
- "the images of your head transposed on models wearing questionable outfits never fails to crack me up" (139)

**Copy, about 6 of 39, on the comparison and handbag pictures:**
- "I didn’t like the comparison pictures" (227)
- "This is like the before and after weight loss ad photos." (132)
- "NOOO the difference was the lady on the left is not smiling, does look unhappy." (106)
- "I don’t see women with stomachs" (149)
- two on the bags (1 like each)

### Comment reactions
**Original:**
- Pushback on the "old lady" frame, about 11: "Waiting for the day when being old isn't an insult." (390); "I am 71. I am an old lady. I don't care if my clothes say that I am an old lady. Celebrate my age!" (244); "News flash.  Old ladies are cool." (227).
- Tucking: "I disagree with tucking in blouses." (1.1K, the top comment).
- Short hair: "All the sweet little old ladies at my church have short hair." (654).
- Waistline: "I no longer have a waistline.  Am I alone?" (798).
- Ages given: 63, "70 soon", 70, 71, 74, "almost 79", 80, 83.

**Copy:**
- Pride and comfort, about 12: "I'm just so proud to have made it this far!" (368); "I love my comfortable clothes" (341); "Be yourself!! Dress how you want and what you're comfortable wearing." (244).
- Invisibility welcomed: "I've been waiting my entire life to be invisible" (148).
- Shoes: "Those orthopedic shoes are worn for a reason." (243).
- An answer to the posture item: "One of the reasons older women look down is because we are more prone to tripping" (115).
- Ages given: 66, 67, 71, almost 73, 73, over seventy, 75.

### Script and not-script differences
**Script:**
- 923 words against 2,024
- a 29-word hook against 284 words with a reversed pitch, an authority line and a held finale
- three items swapped
- no spoken ask against a pre-list ask and a four-step close
- "old lady" against "invisible" as the repeated word

**Not script:**
- a real, credentialed stylist with 294K subscribers against a 27K faceless channel
- the copy came eight months later, when the title had already reached 1M
- the delivery (a real voice with pauses at 115 wpm, against narration at 168)
- the pictures (her head on models, against before/after stock images)
- the thumbnails (only the original's was read in round 2)

---

## 7. Across the pairs

### What every winner has that its copy lacks, counted
| Feature | A | B | C | D | Count (winner has, copy lacks) | Script? |
|---|---|---|---|---|---:|---|
| Asks for nothing until later in the video (first ask as a share of runtime: winner against copy) | 6.7% / 3.5% | 40% / 23% | 99% / 94.5% | none / 13% | **4 of 4** | script |
| Higher channel normal | same channel | 2,400 / 409 | 37,000 / 2,900 | 84,000 / 4,800 | **3 of 3** (A not applicable) | not script |
| Uploaded first | yes | **no** (the copy was 7 days earlier) | yes | yes | 3 of 4 | not script |
| No slip recorded in the description notes (copy: placeholder, literal "DESCRIPTION", mismatched list) | yes | yes | no slip on either side | yes | 3 of 4 | description, not script |
| More words | no | yes | yes | no | 2 of 4 | script |
| Longer runtime | no | yes | yes | no | 2 of 4 | script and delivery |
| Slower speech | no | yes | yes | yes | 3 of 4 | delivery (voice settings or a real speaker) |
| More words before item 1 | yes | no | yes | no | 2 of 4 | script |
| More age phrases | yes (11 / 1) | tie (8 / 8) | yes (6 / 4) | no (2 / 8) | 2 of 4 | script |
| A "not you" reframe line | yes | yes, but the copy has one too | no, only the copy | no, only the copy | 1 of 4 | script |
| The narrator's own stories | none either side | yes (about 8 / 0; the copy has client stories) | none either side | slight (her blouse, her hair) / none | 2 of 4 | script |
| A named outside adversary (industry, salons, magazines) | soft ("we've been told for years") | yes | no | no | 1 of 4 | script |
| A spoken product or offer | no | yes (books, circle) | no | no (the description only) | 1 of 4 | script |

**Nothing script-side runs 4 of 4 except the ask timing.** In every pair the winner's first spoken ask comes later in the video, as a share of runtime, than the copy's. In D the original asks for nothing at all. The margins are thin in A (both ask before item 1) and in C (both ask only at the end).

### What every copy has that its winner lacks, counted
| Feature | A | B | C | D | Count |
|---|---|---|---|---|---:|
| An earlier first ask (the same fact as above) | yes | yes | yes | yes | 4 of 4 |
| Faster speech | no | yes | yes | yes | 3 of 4 |
| A different script under the same title (not a re-cut) | yes | yes | yes | yes | 4 of 4 (true of both sides by definition) |
| More retention devices (holds, countdowns, teasers between items; copy / winner) | no (0 / 1) | yes (5 / 3) | yes (7 / 1) | yes (2 / 0) | 3 of 4 |
| A description slip (placeholder, header, mismatch) | yes | yes | no | yes | 3 of 4 |
| A shorter close after the list | yes (208 / 308) | no | yes (205 / 380) | no (305 / 30) | 2 of 4 |
| More of one emotion word ("frumpy" 5 / 1; "expensive" 13 / 7; "invisible" 6 / 1) | yes | no | yes | yes | 3 of 4, a different word each time |

### Things that are the same on both sides of every pair
- **The item count promised by the title** (7, 5, 8, 7). All eight deliver every item.
- **A fixed item formula.** All eight repeat the same phrase at each item's turn or close: "So, what's the solution?", "The elegant alternative", "Here is the rule", "Secret number", "Our [nth] color combination", "Combo [n]", "So, what can you do instead? … My pro tip is", "The swap".
- **Reassurance.** All eight have at least one line saying the viewer is fine and the clothes or the rules are the problem. All eight also have at least one line that points at the viewer's habits or could read as shaming.
- **No AI disclosure** in any of the eight descriptions.
- **Age and body pushback in the comments**, wherever there are enough comments to see it (A winner, C winner, both of D).
- **Comments per view don't favour the winners.** Per 1,000 views, three copies drew more comments than their winners (A 7.43 against 0.74; C 5.83 against 0.27; D 3.30 against 2.89). Most of A copy's comments answer its location question. Likes per view are higher on the copy in A, C and D.

### The pair winners and copies in `00-measures.md`
That file's "pair-winner" and "pair-copy" medians cover pairs A to C only. D sits in the other study groups. Over A to C the winners' median is 4,084 words against 2,484. Adding D, as the tables here do, splits word count 2 against 2.

### The caveat
Views also depend on things this study can't see or separate:
- **The thumbnail.** None of the eight was read for this round.
- **The channel.** Its size, its normal, and its audience's history: the copy in A is the same channel's second use of a title.
- **Timing.** The upload date, the season, and what the channel posted just before. C's copy followed a 698K hit on another topic by six days.
- **Title differences.** B's casing and "in 2026".
- **The algorithm.** Impressions, click-through, retention and traffic sources.

Four pairs are too few to tell any of these apart. A feature that splits at random would come out 4 of 4 in one direction or the other about one time in eight. And in B, the same title (or a near-identical one) passed 85K on at least four other channels, one of them at 14:45.

### Which differences are script differences
**Script:**
- the hook, including its length, its reframe and its holds
- the item list, its order and the words per item
- the item formula
- the age phrases
- the feelings named
- the adversary
- stories
- spoken offers
- the place and number of asks, and the ending

**Delivery, not script:** words per minute and runtime at a fixed word count (voice speed, a real speaker's pauses).

**Packaging, not script:** the title's small differences, the description (its template slips, links and hashtags) and the thumbnail.

**Neither (context):**
- the channel's normal and subscribers
- upload order and date
- the channel's recent hits
- the presenter type (real, generated or faceless) and the pictures used in the video, which drew the most picture comments (A winner, D copy)
