# 08: Hair against fashion: are the feelings the same?

Style study (women over 50), 2026-10-28. The operator's question, verbatim: "hair fashion makeup seperate packs but for now hair and fashion will be one pack. the emotions are the same right? compare scripts". This file describes, counts and quotes. It writes no rules and recommends nothing.

## The short answer

**Mostly the same.** The same feelings run through both: in comments, 29% of hair comments and 29% of fashion comments voice a feeling about the viewer herself, and the leading feelings in both are permission ("I wear what I want"), relief at an explanation, unhappiness with a body part and "nobody shows women like me". Presenters in both name a feeling in about the same share of hooks (7 of 15 hair, 14 of 23 fashion) and speak in their own person in about a third of videos. The differences that are large and steady:

1. **Who gets the blame (the practical pain).** Hair: the stylist. Stylist complaints are on 12 of 15 hair videos and 0 of 23 fashion videos (Fisher p < 0.001); "not listened to" 9 of 15 against 2 of 23 (p = 0.001). Fashion: clothes that don't fit or aren't made for her, on 12 of 23 fashion videos and 0 of 15 hair (p = 0.001).
2. **Which feeling the script names.** Hair scripts name fear of change and frustration with the process (nervous about bangs, scared of a short cut, "petrified", the patience of going gray): 10 of 21 hair feeling items against 3 of 47 fashion (p = 0.0002), in 8 of 15 hair videos against 3 of 23 (p = 0.01). Fashion scripts name body self-consciousness, comfort and confidence: 37 of 47 fashion feeling items against 5 of 21 hair (p < 0.001). The faceless scripts show the same split (11 of 16 hair feeling items are fear of change or the process, 3 of 43 fashion; p < 0.001).
3. **The hard words live in fashion.** "Frumpy", "old lady", "mumsy" or "dowdy" are spoken in 13 of 23 fashion scripts and 1 of 15 hair scripts (p = 0.002). Hair scripts say "aging" and "older" instead; "granny" belongs to the faceless hair videos.
4. **Topics only one side has.** Hair: the gray grow-out (hiding it, being judged for it) and styling it yourself at home. Fashion: feet, shoes and health; petite sizing; heat. These are topic-bound and carry their own feelings, but each sits on a handful of videos.

Permission is twice as common per comment on fashion videos (9.9% against 4.1%), but three fashion videos carry half of it; at the level of videos the gap is not beyond chance (p = 0.25).

---

## 1. Sample and method

**Sample (appendix):**
- **Real presenters, the main comparison: 38 videos.** The 30 models (M01-M30) plus the 8 real rows of `inputs/videos.csv` that are not models. **Hair 15, fashion 23.**
  - The makeover `WgkP3h4QWpg` changes body shape, clothes, hair, makeup and colour; the body and clothes read-out is its longest part, so it is counted as fashion. Every comment test was re-run with it counted as hair. One reading moves: unhappiness about a body part reaches p = 0.047 by video (0.17 with the makeover as fashion), because its body read-out draws body comments. Nothing else changes.
  - The Rami Jabali makeover `RuyOhWfU-RI` changes only the haircut: hair.
  - French angle: fashion (M28, `n9ICHZq3_tY`, `fLIVwKa-y3U`).
  - M27 `NMvN5bjcwks` is a colour video with one hair-colour item: fashion.
- **Faceless or AI, secondary: 20 videos** (hair 4, fashion 15, one other). The faceless, AI-presenter and "unclear" rows of `inputs/videos.csv` that are not copycat pairs, plus F02 and F06. F07 skipped (music). F06 (hygiene) is neither hair nor fashion and is left out of the comparisons. Faceless hair is only 4 videos.
- **Comments:** every viewer comment in the 57 `comments.md` files, parsed by script and read and coded one by one by hand. Owner comments, accounts marked as named like a style channel and repeats are left out. Base: real hair 586, real fashion 887 (42 of them on the makeover); faceless hair 124, faceless fashion 541. Comments that read as generated (the signs in `01-viewers.md` §6) were coded GEN and left out of the shares: 4 real fashion, 15 faceless hair, 14 faceless fashion.

**Definitions reused from `07-emotions-and-age.md`:**
- The comment codebook, unchanged: invisible; unheard by the stylist or shop staff; not catered for or not shown (makers, videos, models); frumpy or given up; losing her spark or feeling old; comparison with her past self or younger women; judged; permission and rebellion; relief at being understood; recognising her own mistake; pride; young inside; being seen; unhappy about a body part; hope; hiding during a grow-out or after illness.
- The item rule: an item counts when it names an inner feeling (feel, comfortable, confident, nervous, scared, shame, regret and the like), not a look word ("dated", "older", "flattering"). List videos only; non-list videos (salon cut-alongs, vlogs, consultations) are coded for feeling lines but not for item shares.
- Before or after the fix, first person or about the viewer, as in 07.

**Codes I had to add:**
- Comments: **fear of change** (hesitant or afraid to go gray, cut, try); **can't do it at home** (the technique needs a second pair of hands); and topic tags (thin hair, gray, curly, face and neck, body and weight, petite, feet and shoes, heat or climate, cost). The three practical problems of `01-viewers.md` (no stylist who can cut, no clothes that fit, health or mobility) were re-coded here per comment.
- Scripts, to sort the feeling items by kind: fear of change; frustration with the process; body self-consciousness; self-image (feeling like herself, feeling off); comfort; confidence or feeling good; confusion; permission; frumpy or past self.

**Comparability with 07.** On the 17 list videos both files coded, 07 found 31 feeling items in 115; I found 32 in 128 (my item splits are finer on Tracy Campoli's capsule video). The two counts agree exactly on 11 of the 17 videos. The largest gaps: chery `XCf4o0ZOOiw` (07: 4 of 7, mine: 2 of 7) and Justin Hickox `rU56_ly6l2s` (07: 2 of 7, mine: 4 of 6, because I counted "scared to use too much product" and "drives you crazy" as feelings about the process). This is one coder's reading in both files.

**Machine counts:** the counting rules of `tools/measure.py` (spoken words only, bracket tags and ">>" removed; "you", "I", "but" per 1,000 words; questions only where the track is punctuated), copied into a scratchpad script rather than imported because `measure.py` writes files when it runs. Salon and makeover videos include clients' voices in the counts.

---

## 2. Machine counts per 1,000 spoken words

| Measure | Real hair (15) | Real fashion (23) | Mann-Whitney p | Faceless hair (4) | Faceless fashion (15) |
|---|---|---|---|---|---|
| Spoken words | 2,279 (1,360-3,376) | 2,397 (923-5,325) | 0.41 | 3,653 (2,067-3,900) | 2,241 (1,046-4,768) |
| "but" | 6.6 (2.9-9.3) | 8.3 (3.9-12.4) | 0.04 | 5.2 (2.1-7.6) | 4.1 (1.1-9.4) |
| "you / your" | 49.3 (16.9-69.5) | 39.9 (11.7-58.4) | 0.16 | 50.9 (46.9-62.3) | 46.1 (22.4-76.6) |
| "I / me / my" | 33.2 (9.2-92.6) | 27.1 (8.1-80.6) | 0.64 | 4.5 (1.8-10.6) | 10.1 (1.7-22.2) |
| Questions (punctuated tracks) | 4.4 (0-15.9), n = 13 | 3.7 (0-13.0), n = 18 | 0.89 | 3.7, n = 2 | 2.7 (0.9-5.7), n = 13 |
| Items naming a feeling (hand, list videos) | 21 of 53 (40%); per-video median 50% (0-100%), n = 10 | 47 of 191 (25%); per-video median 26% (0-60%), n = 22 | 0.10 (per video) | 16 of 26 (62%), n = 4 | 43 of 127 (34%), n = 15 |

Medians with ranges. The Mann-Whitney test compares the per-video values. Real fashion presenters say "but" a little more often; the other machine counts do not differ.

The item shares lean to hair, but they are not a clean like-for-like: hair has fewer list videos (10, three of them teaching videos with few items each), and the per-video gap is not beyond chance. What differs more clearly is the *kind* of feeling (§3.2).

---

## 3. Scripts by hand (real presenters)

Every real transcript was read in full. Per-video codes are in the scratchpad file listed under "Check".

### 3.1 Where and how the feeling is voiced

| Measure | Hair (15) | Fashion (23) |
|---|---|---|
| Feeling items before the fix / after it | 12 / 9 | 21 / 26 |
| Hooks (first 60 s) that name a feeling | 7 of 15 | 14 of 23 (Fisher p = 0.51) |
| Videos where the presenter voices her own feeling | 5 of 15 | 8 of 23 (p = 1.0) |
| …plus a client's own feeling lines | 2 (`R7g-CrH4m2A`, `RuyOhWfU-RI`) | 1 (the makeover) |
| List videos with no feeling item | 2 of 10 | 6 of 22 |

The placement is the same as in 07: one short sentence, either opening the item (the pain) or closing it (the promised feeling). Fashion leans slightly to the feeling after the fix; hair slightly before. Neither lean is large.

### 3.2 Which feeling is named, item by item (hand)

| Kind of feeling (feeling items only) | Hair (21 items) | Fashion (47 items) |
|---|---:|---:|
| Fear of change (nervous, scared, on the fence, regret) | 5 | 2 |
| Frustration or fear about the process (product, styling, patience) | 5 | 1 |
| Self-image (feeling off, not like herself, feeling cuter) | 4 | 2 |
| Body self-consciousness (legs, arms, tummy, face) | 3 | 13 |
| Confidence, feeling good | 2 | 14 |
| Comfort | 0 | 10 |
| Others' judgement / confusion / permission / frumpy or past self | 1 / 1 / 0 / 0 | 0 / 0 / 2 / 3 |

Fear of change and the process together: hair 10 of 21, fashion 3 of 47 (Fisher p = 0.0002). Body, comfort and confidence together: hair 5 of 21, fashion 37 of 47 (p < 0.001). By video, fear-of-change lines (items or not) appear in 8 of 15 hair videos and 3 of 23 fashion videos (p = 0.01).

Reading: a haircut or colour change cannot be taken off at night, and the hair scripts talk about the step itself ("if you're nervous, start here"). A fashion item can be tried and returned, and the fashion scripts talk about the body inside the clothes and how it will feel.

**Hair: fear of change and the process**
- "If you're really nervous about trying bangs, but you really, really want to, this is also one of the easier and safer places to start." (`9LvzTBzXL5k` [8:57])
- "If you have been on the fence about cutting your length, this is your sign." (`XCf4o0ZOOiw` [1:06])
- "I'm petrified, but I'm trusting you." (`2e50uMLaCtE` [3:17])
- "You're kind of curious or even tempted, but you're also not ready to commit 100%." (`xNuoMiG2kVw` [9:35])

**Hair: the feeling in the presenter's own person**
- "every time I get bangs, I regret it" (`9LvzTBzXL5k` [3:45])
- "It's a process where you feel ugly a lot. It's really, really hard." (`pC4YjCxSalg` [6:55])

**Fashion: body self-consciousness**
- "Most women over the age of 50, well, we hate this season. Not because we don't like summer, but because of our legs." (`7ecJWmEQ3Ks` [0:03])
- "Many women tell me that they are ashamed of their bodies." (`MWQ6T1wURJU` [3:35])
- "our crepey skin, our arms aren't as toned" (`Hionkf3pHJc` [13:08])
- "we are more self-aware of certain parts of our body that don't look the same as they did back in the day specifically on me it's my stomach" (`r58VDhcsdYo` [4:43])

**Fashion: comfort and confidence**
- "I'm not going to feel like a stuffed sausage" (`NT1mEOX-p7Y` [15:34])
- "I feel comfy, I feel put together." (`NT1mEOX-p7Y` [15:56])
- "open up your neckline, open up your self-confidence" (`ixlexruRC6c` [2:26])

### 3.3 The adversary cast

| Adversary (presenter's own words) | Hair videos (15) | Fashion videos (23) |
|---|---:|---:|
| The stylist or salon (the cut that went wrong, the stylist who should notice) | 5 | 0 |
| Stores, makers, catalogues, designers | 0 | 7 |
| Trends or trend lists | 1 | 5 |
| Beauty standards, companies, "conditioning" | 3 | 0 |
| Commenters ("armchair warrior") | 2 | 0 |
| Inspiration photos, models, "the rules" | 2 | 1 |
| An ex-partner; AI channels; a 1980s colour analyst | 0 | 1 each |
| Nobody named | 6 | 11 (incl. the makeover) |

Fashion's stores-and-makers count includes bra fitters, blends of linen and "the jeans" themselves (`9ZNV79Uva3g`). In hair the stylist is often half-excused: Summer Beauty names the stylist and then says the fault is "never been told".

**Hair**
- "You get angry, blame the stylist, or worse, you blame yourself and start questioning your own beauty." (`i5jFYNeCHGM` [0:12])
- "this is something that your hair stylist should be paying attention to" (`W8Hg-J6HbUo` [13:05])
- "Companies selling us things were telling us what is beautiful. And I was brainwashed." (`pC4YjCxSalg` [5:47])

**Fashion**
- "Chico's does hold on to stuff that their older clientele really love let's make that stop" (`r58VDhcsdYo` [3:16])
- "they're often sold in these magazines and places that are aimed at over 50 age group" (`Rg_YiVy40fk` [2:52])
- "If I was that designer, I would put somebody else's name on it." (`MWQ6T1wURJU` [8:15])

### 3.4 Reassurance and hard words

| Measure | Hair (15) | Fashion (23) | Fisher p |
|---|---:|---:|---:|
| Videos with an explicit "not your fault / nothing wrong with you" reframe (hand) | 4 | 8 | 0.73 |
| Videos saying "frumpy", "old lady", "mumsy" or "dowdy" (pattern, each read) | 1 | 13 | 0.002 |
| …times said | frumpy 1 | frumpy 28, old lady 11, mumsy 4, dowdy 1 | |
| Videos saying "dated / outdated" | 2 | 7 | |
| Videos saying "aging", "ages you" | 4 | 11 | |

The one hair use of "frumpy" is Justin Hickox describing a bob's profile ("make your profile feel frumpy"). "Granny" or "grandma" in the real scripts is never an insult: "only grandmothers had gray hair" (`pC4YjCxSalg`), a grandmother's summers (`Hionkf3pHJc`).

**Hair reframes**
- "the problem isn't always your stylist, and it's certainly not your own looks" (`i5jFYNeCHGM` [0:19])
- "if you've ever tried to style and something just felt wrong, that's usually a sign that the proportions are off" (`9LvzTBzXL5k` [3:59])
- "We have been conditioned to believe that gray hair equals giving up." (`xNuoMiG2kVw` [0:17])

**Fashion reframes and hard words**
- "if you tried five pair of jeans and none of them fit it doesn't mean there is something wrong with your figure" (`9ZNV79Uva3g` [0:07])
- "You are not too old, you are not too big, you are not behind." (`iJZEsuGk3sA` [22:29])
- "there are other options besides clunky, frumpy, kind of like, I'm going to say it, old lady shoe" (`m7pfd4OxPzs` [16:15])

---

## 4. Comments by hand (real presenters)

### 4.1 Feelings, hair against fashion

Shares are of all viewer comments, generated-looking ones left out (hair 586, fashion 883). "Videos" is the number of videos with at least one such comment (hair 15, fashion 23). The first p tests comments (it ignores that comments cluster on videos); the second tests videos.

| Code (07) | Hair n (%) | Hair likes | Hair videos | Fashion n (%) | Fashion likes | Fashion videos | p, comments | p, videos |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Any feeling about herself | 171 (29.2) | | | 256 (29.0) | | | | |
| Permission and rebellion | 24 (4.1) | 4,236 | 8 | 87 (9.9) | 11,671 | 15 | < 0.001 | 0.51 |
| Relief, being understood | 27 (4.6) | 3,121 | 10 | 29 (3.3) | 1,805 | 12 | 0.21 | 0.51 |
| Pride | 24 (4.1) | 898 | 10 | 15 (1.7) | 803 | 9 | 0.007 | 0.18 |
| Not catered for or not shown | 23 (3.9) | 1,925 | 7 | 35 (4.0) | 5,012 | 16 | 1.0 | 0.19 |
| Unhappy about a body part | 21 (3.6) | 4,757 | 7 | 53 (6.0) | 4,966 | 17 | 0.04 | 0.17 |
| Unheard by the stylist or shop staff | 18 (3.1) | 2,210 | 9 | 2 (0.2) | 15 | 2 | < 0.001 | 0.001 |
| Judged | 17 (2.9) | 2,849 | 7 | 13 (1.5) | 406 | 8 | 0.06 | 0.51 |
| Being seen, compliments | 13 (2.2) | 1,067 | 6 | 9 (1.0) | 207 | 8 | 0.08 | 1.0 |
| Hope, a fresh start | 12 (2.0) | 446 | 6 | 13 (1.5) | 247 | 6 | 0.42 | 0.48 |
| Comparison with her past self | 10 (1.7) | 592 | 6 | 17 (1.9) | 3,109 | 11 | 0.84 | 0.74 |
| Losing her spark, feeling old | 8 (1.4) | 71 | 5 | 6 (0.7) | 419 | 4 | 0.27 | 0.44 |
| Hiding during a grow-out or after illness | 6 (1.0) | 99 | 4 | 0 | | 0 | 0.004 | 0.02 |
| Frumpy, given up | 2 (0.3) | 558 | 2 | 18 (2.0) | 1,842 | 8 | 0.005 | 0.26 |
| Recognising her own mistake | 2 | | 2 | 2 | | 2 | 0.65 | |
| Fear of change (added) | 2 | | 1 | 0 | | 0 | 0.16 | |
| Invisible | 0 | | 0 | 3 | | 3 | 0.28 | |
| Young inside | 1 | | 1 | 3 | | 3 | 1.0 | |

**The steady differences** (beyond chance by video as well as by comment): unheard by the stylist (hair) and hiding during the gray grow-out (hair). **The ones that sit on a few videos** (beyond chance by comment, not by video): permission and frumpy (fashion), pride (hair). Permission on fashion: 18 on the Serena shoe video, 17 on the "Old Lady" video, 15 on the shorts video; on hair, 9 of the 24 are on the gray grow-out story `pC4YjCxSalg`. Pride on hair is mostly pride in gray hair.

**Hair**
- "I keep asking for layers and all I get is shorter hair and crapy layers!" [442] `W8Hg-J6HbUo`
- "the stylist never gets them right. It's very frustrating" [238] `W8Hg-J6HbUo`
- "Everyone said I look older, I don't care. People do grow old you see." [210] `pC4YjCxSalg`
- "Fortunately I transitioned during the pandemic. It was the best time to stay hidden." [31] `xNuoMiG2kVw`
- "ohhh THAT'S why i think i look better with height on my hair." [924] `UUS1R9oWx4o`

**Fashion**
- "Turning 70 this year...so I'm old enough to wear whatever I want!!" [1.5K] `7ecJWmEQ3Ks`
- "Showing real middle aged women in these clothes would be helpful. Not young, skinny fashion models." [1.2K] `7ecJWmEQ3Ks`
- "I no longer have a waistline. Am I alone?" [798] `ixlexruRC6c`
- "Me sitting here in my leggings and baggy old t-shirt wondering why I'm even watching this." [436] `gfbWOw00Y-M`
- "Not all of us have the arms for sleeveless dresses." [264] `MWQ6T1wURJU`

### 4.2 The top themes

| Rank | Hair | Fashion |
|---|---|---|
| 1 | Relief at an explanation (27) | Permission and rebellion (87) |
| 2 | Permission, mostly about gray (24) and pride, mostly in gray (24) | Unhappy about a body part (53) |
| 3 | Not catered for: thin, curly or double-chin hair never shown (23) | Not catered for: models too young, too slim, too tall (35) |
| 4 | Body part: jowls, flat crown, forehead (21) | Relief (29) |
| 5 | Unheard by the stylist (18), judged when going gray (17) | Frumpy (18), past self (17) |

The same five feelings fill both lists; what they are about differs. Hair's "not catered for" is about hair texture and the model's chin; fashion's is about the model's size and age.

- "You need to have a model that actually has a double chin." [314] `GOuDkBf6CmA`
- "part of the problem is the lack of dresses designed and tailored for the mature woman" [296] `MWQ6T1wURJU`

### 4.3 The practical problems

| Problem | Hair comments (videos) | Fashion comments (videos) | p, videos |
|---|---|---|---|
| No stylist who can cut or listen | 32 (12 of 15) | 0 | < 0.001 |
| Can't do it at home (added) | 9 (2) | 0 | 0.15 |
| No clothes that fit, nothing made for her | 0 | 32 (12 of 23) | 0.001 |
| Health or mobility | 11 (6) | 31 (14) | 0.32 |

Hair's health comments are mostly hair loss or changed hair after illness, surgery or medication, plus two about no longer being able to drive to a good stylist or style it oneself; fashion's are feet, knees, backs, walking aids and incontinence, usually tied to shoes.

- "Unfortunately it's nearly impossible to find stylists that can actually cut a bob." [1K] `vFul5tvg1Cw`
- "Us at home need to know how to achieve the same results without removing our head to fix our hair." [1.1K] `rU56_ly6l2s`
- "Why is it every one of you telling us petite women what to wear thin?" [278] `6Yz0BKoKG-M`
- "Flat shoes with no support are painful for a lot of us!" [200] `dFAGM7iBWRI`

---

## 5. Pain points

### In the scripts (hand, videos naming it as a problem)

| Hair (15 videos) | n | Fashion (23 videos) | n |
|---|---:|---|---:|
| Thin, fine, flat, breaking or falling hair | 10 | The body changing: weight, tummy, arms, legs, hips | 14 |
| Going gray, colour washing out | 5 | Frumpy, dated or outdated pieces | 10 |
| The wrong cut, the stylist | 4 | Shoes and feet, comfort against style | 5 |
| Face shape and proportions | 3 | Nothing to wear, nothing fits | 4 |
| The face changing: sagging, jowls, receding hairline | 3 | Heat or warmth | 3 |
| Styling it at home, hold | 2 | Looking older through colour or skin; petite height; budget | 2 each |

### In the comments (topic tags, comments and videos)

| Hair | Comments (videos) | Fashion | Comments (videos) |
|---|---|---|---|
| Gray hair | 57 (10) | Body and weight | 58 (16) |
| Thin or fine hair | 54 (12) | Petite sizing | 32 (15) |
| Face and neck (jowls, chin) | 23 (4) | Feet and shoes | 31 (10) |
| Curly or changed texture | 14 (7) | Heat or climate | 12 (7) |
| Cost | 4 (3) | Cost | 7 (5) |

Almost no topic crosses over: no hair comment is about body size, shoes or petite sizing, and no fashion comment is about thin hair or curls. Gray hair appears in 5 fashion comments: one viewer has just stopped dyeing, one says a pink cardigan makes her white hair look old, three are about which colours suit gray hair.

---

## 6. Size of the differences

| Difference | Carried by | Test | Reading |
|---|---|---|---|
| Hair comments blame the stylist; fashion comments blame fit and makers | Stylist: 12 of 15 hair videos, 0 of 23 fashion. Fit: 12 of 23 fashion, 0 of 15 hair | Fisher, videos: p < 0.001 and 0.001 | Real and large |
| Hair scripts voice fear of change and the process | 10 of 21 hair feeling items, 3 of 47 fashion; 8 of 15 hair videos, 3 of 23 fashion | Fisher: p = 0.0002 (items), 0.01 (videos) | Real; one coder; faceless scripts agree (11 of 16 against 3 of 43, p < 0.001) |
| Fashion scripts voice body, comfort, confidence | 37 of 47 fashion items, 5 of 21 hair | Fisher: p < 0.001 | Real; one coder |
| Shame words in fashion scripts | 13 of 23 fashion videos, 1 of 15 hair | Fisher: p = 0.002 | Real; partly the titles (six fashion titles say "frumpy", none of the hair titles) |
| Hiding during the gray grow-out (comments) | 6 comments on 4 hair videos, 0 fashion | Fisher, videos: p = 0.02 | Small numbers; topic-bound |
| More permission on fashion | 87 against 24 comments; 15 of 23 against 8 of 15 videos | Comments p < 0.001; videos p = 0.51; per-video share p = 0.25 | Clustered on three fashion videos; not a steady difference |
| More frumpy self-description on fashion | 18 against 2 comments; 8 against 2 videos | Comments p = 0.005; videos p = 0.26 | Small; follows the fashion titles that say "frumpy" |
| More pride on hair | 24 against 15 comments | Comments p = 0.007; videos p = 0.18 | Mostly pride in gray hair; topic-bound |
| More body-part unhappiness on fashion | 53 against 21 comments; 17 of 23 against 7 of 15 videos | Comments p = 0.04; videos p = 0.17 (0.047 if the makeover counts as hair) | Borderline; both sides voice it about their own topic (body against face and head) |
| Items naming a feeling (share) | 40% hair, 25% fashion | Per-video Mann-Whitney p = 0.10 | Not beyond chance |
| "but" per 1,000 words | 6.6 hair, 8.3 fashion | Mann-Whitney p = 0.04 | Small |

Samples are small: 15 hair and 23 fashion real videos, about 40 comments each. Fisher tests are two-sided. With twenty-odd comparisons, one or two p values under 0.05 would turn up by chance; the first four rows stand well clear of that.

---

## 7. Faceless and AI (secondary)

### Scripts (19 transcripts read; items and feelings coded by hand)

| Measure | Faceless hair (4) | Faceless fashion (15) |
|---|---|---|
| Items naming a feeling | 16 of 26 | 43 of 127 |
| …fear of change or the process | 11 | 3 |
| …body, comfort, confidence | 4 | 21 |
| …self-image, often in invented stories ("Clarice", "Marguerite") | 0 | 11 |
| …other | 1 (giving up femininity with a short cut) | 8 (guilt 2, permission 3, frumpy, invisible, a ring's memories) |
| Adversary | the stylist ("granny cutter") 1; the "granny cut" 1; none 2 | makers 4; "the industry" 2; trends or influencers 2; "nobody explains" 2; none 5 |
| Explicit "not your fault" reframe | 2 | 8 |

The split repeats: faceless hair scripts talk about the step ("I know cutting your hair this short can feel intimidating"), faceless fashion scripts about the body and comfort.

- "Three questions you must ask your stylist that will instantly tell you if they are a granny cutter or a true artist." (`XR3IwlcIcCY` [1:27])
- "It is not your age. It is the cut." (`8p2y_Yk0pNQ` [0:14])
- "I know cutting your hair this short can feel intimidating" (`aaDZuD5jIfs` [8:51])
- "Most dresses on the market are still designed around a body that stopped being the majority sometime around age 35." (`G5y1gFHWPIA` [1:08])
- "it's probably not your body. It's just bad engineering." (`XByilJlme5Y` [5:31])

### Comments (faceless hair 109, faceless fashion 527, after GEN)

| Code | Faceless hair n (%) | Faceless fashion n (%) |
|---|---|---|
| Any feeling | 34 (31%) | 180 (34%) |
| No stylist who can cut or listen | 18 (17%), 2 videos | 0 |
| Not catered for or not shown | 6 (6%) | 71 (13%), 12 videos |
| Permission | 10 (9%) | 67 (13%) |
| Unhappy about a body part | 0 | 27 (5%) |
| No clothes that fit | 0 | 14 (3%) |

The same practical split as the real side: the hair complaint is the stylist, the fashion complaint is fit and the models.

- "I tell hairstylists point black, NO GRANNY CUT, and what do they give me? A granny cut." [22] `XR3IwlcIcCY`
- "Why on earth do they make dresses for older woman with so many bows and ruffles and big puffy sleeves?" [184] `G5y1gFHWPIA`

---

## What this can't show

- **One coder.** The script items, the kinds of feeling and every comment code are my reading. On the 17 videos 07 also coded, our item counts agree exactly on 11; the disagreements are about whether a feeling about the process (product, styling) counts.
- **Small and uneven samples.** 15 real hair against 23 real fashion videos; 10 against 22 list videos; faceless hair only 4. Comments cluster on videos, so per-comment tests overstate certainty; both are shown.
- **Topic and format travel with the group.** Hair has salon cut-alongs, consultations and two gray-hair vlogs; fashion has none of those (one makeover aside). Hair teaching videos (face shape, cranial tops) have few items. Some differences may belong to the format, not to hair. The makeover could go either way; counting it as hair moves only the body-part reading (p = 0.047 by video).
- **Titles drive comments.** Fashion titles that say "frumpy" draw frumpy comments; the gray-hair videos draw judged-and-proud comments. The comment differences partly follow the topics the channels chose.
- **Commenters are a small, self-selected group**, and what a woman leaves unsaid can't be counted.
- **Makeup** is not in this sample (one makeover aside), so nothing here speaks to a makeup pack.
- **Cause.** Nothing here shows which feeling line makes a video perform.

## Check

- Every transcript quote in this file (marked `"…" (ID [m:ss])`) was matched by a `python3 -I` script against its `transcript.txt`, with case, punctuation and caption tags ignored, and its timestamp checked to lie within 3 seconds of the start of the segment where the quote begins. Every comment quote (marked `"…" [likes] ID`) was matched against its `comments.md` with its like count and video ID. Result of the last run: see the line below.
- Machine counts, comment tallies, video-level tests and Fisher and Mann-Whitney tests were run by scripts in `/tmp/claude-0/-home-user-script-system/1606fe5d-4351-58e1-8e5d-ec273208b30e/scratchpad/h8/` (`measures.py`, `tally.py`, `ftally.py`, `videolevel.py`, `scripts_real.py`, `stats.py`, `verify.py`). The hand codes are in the same folder: `script_codes.md` (real transcripts), `faceless_codes.md`, `ccodes.txt` (real comments), `fcodes.txt` (faceless comments).
- No NexLev or web calls. No file other than this one was changed.

Last run of `verify.py` on this file: 30 transcript quotes and 18 comment quotes checked, 0 problems.

---

## Appendix: the classified sample

| Code | Video ID | Channel | Title (short) | Side | Group | Note |
|---|---|---|---|---|---|---|
| M01 | `i5jFYNeCHGM` | Summer Beauty | Why Your Haircut Never Looks Right (It's Not You) | real | hair |  |
| M02 | `pC4YjCxSalg` | Woman in midlife | I Stopped Dyeing My Hair at 49 — Here’s What Really Happened | real | hair | gray grow-out story |
| M03 | `A8llK8GsSD0` | Karen of Curl House | I WIsh I Knew This BEFORE Washing My Gray Natural Hair! | real | hair | the transcript is a pre-shampoo oil tutorial |
| M04 | `XCf4o0ZOOiw` | chery 🍒 | Your Fine Hair Doesn't Have to Look Older (Do This Instead) | real | hair |  |
| M05 | `R7g-CrH4m2A` | Boys And Girls Hairstyles (RaDona) | The Most Requested Haircut for Women Over 70 / She Drove All the Wa... | real | hair | salon cut-along |
| M06 | `W8Hg-J6HbUo` | Justin Hickox | Women That LOOK 10 YEARS YOUNGER Know THIS About Their Hair! | real | hair |  |
| M07 | `9LvzTBzXL5k` | Glam Girl Gabi | Best Bangs for your Face Shape (At Any Age!) | real | hair |  |
| M08 | `rU56_ly6l2s` | Justin Hickox | You're Styling Your THIN/FINE Hair WRONG! Do THIS Instead- 5 SECRETS | real | hair |  |
| M09 | `UUS1R9oWx4o` | Summer Beauty | STOP Styling Your Hair WRONG For Your Face & Head Shape! | real | hair |  |
| M10 | `GOuDkBf6CmA` | Justin Hickox | Double Chin or Sagging Neck? NEVER WEAR These Hairstyles! DO THIS I... | real | hair |  |
| M11 | `2e50uMLaCtE` | Woman in midlife | I colored my Gray Hair after 18 months of no dye | real | hair | gray grow-out vlog |
| M12 | `vFul5tvg1Cw` | Justin Hickox | You're Styling Your Bob Haircut WRONG! Do THIS Instead- 5 SECRETS | real | hair |  |
| V14 | `qwM0s0Q3Rjw` | Rami Jabali Hair Salon | ✂️ Stop Saving Damaged Ends …. Start Building Real Hair Thickness | real | hair | salon consultation and cut |
| V17 | `xNuoMiG2kVw` | Summer Beauty | Are You Going GRAY? Don't Pick The WRONG Method | real | hair |  |
| V39 | `RuyOhWfU-RI` | Rami Jabali Hair Salon | ✨ The Hair Effect: The Fastest Way to Transform Your Face ✨ | real | hair | makeover by haircut only: hair |
| V38 | `WgkP3h4QWpg` | MAKEOVERGUY | “Fine at 69.” Her Husband Was Almost Speechless / MAKEOVERGUY | real | fashion | makeover; the body and clothes read-out is the longest part, plus hair, makeup and colour: fashion (comment tests re-run with it as hair) |
| M13 | `7ecJWmEQ3Ks` | Adore Your Wardrobe | Ditch the Shorts: 7 Things to Wear Instead / Fashion Over 50 | real | fashion |  |
| M14 | `NT1mEOX-p7Y` | Tracy Campoli | The Over 40 Capsule Wardrobe That Makes You Look EXPENSIVE (without... | real | fashion |  |
| M15 | `m7pfd4OxPzs` | Tracy Campoli | 7 Items That Make You Look FRUMPY After 50 (Stop Wearing These!) | real | fashion |  |
| M16 | `creI37QkUMs` | Angela Masson - Fashion Over 50 | Get Out Of YOUR Frumpy Style RUT! 10 Things to Change After 50 | real | fashion |  |
| M17 | `iJZEsuGk3sA` | Darlene Obiyan | Stop Dressing Frumpy/ Curvy Style Tips Over 50 | real | fashion |  |
| M18 | `Rg_YiVy40fk` | Capsule Closet Stylist | 10 Fashion Mistakes That Make You Look Years Older | real | fashion |  |
| M19 | `Hionkf3pHJc` | Beth Djalali | Why Linen Looks Frumpy After 50 (And How to Fix It) | real | fashion |  |
| M20 | `gfbWOw00Y-M` | MM Personal Styling | 10 Style Mistakes That Instantly Make You Look Older with Personal ... | real | fashion |  |
| M21 | `ixlexruRC6c` | Marie-Anne Lecoeur - The French Chic Expert | 7 Things That Scream 'Old Lady' (Harsh But True): Style Over 50 | real | fashion |  |
| M22 | `MWQ6T1wURJU` | Marie-Anne Lecoeur - The French Chic Expert | How Not To Wear Summer Dresses Over 50: Fashion Mistakes Women Over... | real | fashion |  |
| M23 | `G-RW7ih19Y4` | Marie-Anne Lecoeur - The French Chic Expert | How To Look Slimmer: The MOST EFFECTIVE Style Tips For Women Over 50 | real | fashion |  |
| M24 | `6Yz0BKoKG-M` | Diana GOSS | 6 Styling Mistakes That Are Making You Look SHORTER (Fix These!) | real | fashion |  |
| M25 | `r58VDhcsdYo` | Marnie Goldberg | How To Not Look Frumpy & Older Than You Are-Get Out of That Rut!! | real | fashion |  |
| M26 | `eKCl-bRx8wg` | Diana GOSS | 5 Style Mistakes That Make You Look Older Than You Are | real | fashion |  |
| M27 | `NMvN5bjcwks` | Diana GOSS | How To Look Instantly Younger / 5 Colour Hacks You Need To See | real | fashion | colour video; one of five items is hair colour |
| M28 | `saDURZc-pno` | Aliceinparis | 10 Things French Women Never Buy (But Everyone Else Does) | real | fashion | French angle (listed as "french"): fashion |
| M29 | `dFAGM7iBWRI` | Style With Serena | Wear THIS, Not THAT: 5 Outdated Fall Shoes to Ditch in 2026 | real | fashion |  |
| M30 | `uBqNLIiLnv4` | Dressed for My Day with Kay Harms | How to Tie a Scarf this Winter - Feel Confident & Look Stylish in S... | real | fashion |  |
| V20 | `9ZNV79Uva3g` | Diana GOSS | How To Find Jeans For Your Figure / Jeans For Your Body Type | real | fashion |  |
| V25 | `vBsFMkGDbhA` | Adore Your Wardrobe | STOP Feeling Frumpy in Wide Leg Jeans! | real | fashion |  |
| V34 | `n9ICHZq3_tY` | Marie-Anne Lecoeur - The French Chic Expert | AI Gets French Style WRONG! Here's What Real French Women Actually ... | real | fashion | French angle: fashion |
| V35 | `fLIVwKa-y3U` | Aliceinparis | 10 Fashion Trends You’ll See Everywhere in Paris in 2026 | real | fashion | French angle: fashion |
| V05 | `vATkBSPjQmc` | Elegance At 60 | 5 Ways to Avoid Looking Heavy and Outdated After 50 and 60! - Fashi... | faceless/AI | fashion |  |
| V06 | `2IkhtemG-MM` | Chic Over 60 | 10 Things Women Over 60 Should REMOVE From Their WARDROBE Right Now! | faceless/AI | fashion |  |
| V10 | `XR3IwlcIcCY` | Elegant After 60 | DON’T Get a "Granny" Cut! 3 Haircuts That Actually Make You Look 10... | faceless/AI | hair |  |
| V12 | `CkVrghocoPs` | Alice Luxe | 7 Pixie Cut Mistakes Women Over 60 Should AVOID | faceless/AI | hair |  |
| V18 | `aaDZuD5jIfs` | Alice Luxe | GRAY Hair Styles That Make You Look Expensive | faceless/AI | hair |  |
| V21 | `G5y1gFHWPIA` | Glow After 60 | 7 Dresses That Hide a Tummy After 60 (No Shapewear, No Guessing) | faceless/AI | fashion |  |
| V22 | `KNwk391XyIY` | Rock Your Fashion | 10 PETITE Style SECRETS That’ll Change Everything - 50+ Women's Fas... | faceless/AI | fashion |  |
| V26/F01 | `2q_6Qf69Ywc` | Vivian Sinclair | 5 Glasses That Make Women Over 60 Look Instantly Younger | faceless/AI | fashion | glasses: accessory, fashion |
| V27 | `XByilJlme5Y` | Elegance At 60 | Pants to Avoid with a Large Tummy & Lower Belly Pooch - Apple Shape... | faceless/AI | fashion |  |
| V28/F03 | `dn3mNRtYTY4` | Golden Melanin Lifestyle | 10 SHOE Mistakes That Are Aging Black Women Over 50 (And The Beauti... | faceless/AI | fashion |  |
| V29 | `h6Y1RZzOlzg` | Chic After 60 | How to Wear LEGGINGS Over 60 Without Looking Sloppy / Plus 7 Easy O... | faceless/AI | fashion | AI presenter |
| V30/F08 | `kKjLX7Q6wc8` | Ever Chic At 50 | 7 Blouse Mistakes Quietly Aging Women Over 60 (And How to Fix Them) | faceless/AI | fashion |  |
| V32/F04 | `YLiz8tlx9g4` | AnniePicks | 7 Colour Combinations That Make You Look Expensive & Elegant / Wome... | faceless/AI | fashion |  |
| V33 | `qFLenue5BBI` | Ageless Melanin | 8 COLORS THAT MAKE BLACK WOMEN OVER 50 LOOK YOUNG, RADIANT, AND TUR... | faceless/AI | fashion | AI presenter |
| V36/F05 | `-eTr9aVSWlM` | French Fashion | The Only 10 Clothes You Need All Winter (The French Way, 50+) | faceless/AI | fashion | French angle: fashion |
| V37 | `HG2OJ0O3lxg` | TRENDS SPOTTED FASHION Timeless and Ageless | She's 68 in Paris — 5 Style Rules She Never Breaks | faceless/AI | fashion | French angle: fashion |
| V46 | `8p2y_Yk0pNQ` | Stylish60plus | 7 Modern Haircuts That Instantly Make You Look Younger 60+ | faceless/AI | hair |  |
| V47 | `Fs17Qc6l8Ug` | Ageless Style 50s & 60s | 7 Things That Scream 'Old Lady' (Harsh But True): Style Over 50 | faceless/AI | fashion | type "unclear" in videos.csv; uses the M21 title |
| F02 | `tSfgNEUXh8U` | Vivian Sinclair | STOP Wearing These 5 Earrings After 60! WEAR These INSTEAD | faceless/AI | fashion | earrings: accessory, fashion |
| F06 | `5lCfaBWShOE` | Emiko Sato | 11 Hygiene Rules Japanese Women Follow After 40 to Avoid “Old Perso... | faceless/AI | other | hygiene: neither group; left out of the hair-fashion comparisons |

Codes: M = approved model; V = row number in `inputs/videos.csv`; F = faceless reference list in `models/approved-models.csv`. Real: hair 15, fashion 23. Faceless/AI: hair 4, fashion 15, other 1.
