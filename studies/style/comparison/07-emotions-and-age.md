# 07: The feelings that drive the niche, and the age brackets

Style study (women over 50: hair and fashion), 2026-10-28, for Scarlet Sterling and Diane de Chambray. It describes, counts and quotes. It writes no rules or scripts and recommends nothing.

**The frame being tested (the operator's words):** "they feel unheard, they feel frumpy, they feel like they are losing their spark as they age and we are giving them practical solutions to solve emotional problems … we turn their emotional problem and pain into a heard and easy to solve solution with our practical tricks." The test is whether the comments and scripts show this, how strongly, and what else they show. Real women presenters are treated as the source of technique, as the operator asked.

**Sources:**
- Comments: every `comments.md` for the 45 study videos (the two DROPPED rows left out) and our 38 (`own-baseline-2026-10/`).
- Scripts: the 45 transcripts and notes, and our 38 transcripts.
- Titles: `round2/outliers-all.csv`, core topic only, on channels where `round2/channels-all.csv` has `final_keep` = yes and `audience_check` starting "pass". That gives **1,182 titles** (de-duplicated by video ID). This filter keeps every core outlier on those channels, so it differs from the 1,118 "breakout" videos in `BREAKOUT-MAP.md`.
- Ages: the age-giving comments of `01-viewers.md`, found again and read one by one.

No NexLev calls. Nothing in `data/`, `notes/`, `round2/` or `own-baseline-2026-10/` was changed.

**Reading it:**
- **Sides:**
  - **R** = the 21 real-presenter videos.
  - **F** = the 24 faceless or AI-presenter videos, the copycat pairs included.
  - **O** = our 38.
- **Comment base:** my own parse gives R 804, F 792, O 42 viewer comments. Owner comments, comments marked `[account named like a style channel]` and "[also in top]" repeats are left out. `01-viewers.md` counted R as 811; the difference comes from how duplicates were merged.
- **Count types:**
  - **(hand)** = I read every comment, or every item, and coded it myself.
  - **(pattern)** = a regex count by script. It over-counts words used about objects ("a confident red mouth") and misses paraphrase.
  - **(reading)** = my interpretation.
- **Tags:** quotes are verbatim, auto-caption spellings kept. A transcript tag is the video ID and the start of the segment where the quote begins. A comment tag gives the likes in brackets, then the video ID. No usernames.
- **Generated-looking comments:** 28 comments that read as generated (the "reads as generated" signs in `01-viewers.md` §6, almost all on F videos) were coded GEN and left out of the feeling counts.

---

## The short version

1. **The operator's three feelings are present in the comments but rare.** Per 1,600 study comments (hand):
   - frumpy, dowdy or "given up" about herself: 25
   - losing her spark or confidence, or feeling old: 17, and about a third of these come with an illness
   - feeling invisible or unseen: 6, and only 1 is a complaint; 2 welcome it
   - the word "unheard" never appears

   **Being unheard does appear in a practical form:**
   - stylists or shop staff who don't listen: 7
   - makers and videos that don't cater for her: 14
   - the model complaints in `01-viewers.md`: 78
2. **The commonest feeling about herself is the opposite of the frame.** Permission and rebellion ("I wear what I want", "proud to be old") make 113 comments, 7% of the study comments, with 10,346 likes. Relief at being understood makes 46, and 33 of those are on real videos. Most of the relief is relief at an explanation ("ohhh THAT’S why…"), not at being comforted.
3. **Real presenters attach a feeling to only about a quarter of their items.** By hand, 31 of 115 items in the 17 list videos name an inner feeling. The rest are told in look words ("dated", "older", "flattering"), which are in two-thirds of real items (pattern).
4. **Where the real presenter puts the feeling:**
   - before the fix (24 items) a little more often than after it (15)
   - usually in one sentence of about 12 words (4-29)
   - in plain words: feel, comfortable, confident, nervous, scared, shame, regret
   - in her own person in 10 of 21 videos, with 2 more told through the client's words: "every time I get bangs, I regret it" (Gabi), "I do myself" (chery), PCOS chin hair (Melissa Murrell)
   - often with a reframe step that moves the blame off the woman: "that's usually a sign that the proportions are off"
5. **Faceless scripts use more feeling words than real ones, but mostly as labels.** Strict pattern: 2.3 per 1,000 words, against 1.4 for real. "Confidence" is often said about colours ("whispers confidence and quiet luxury"). First-person feeling lines are 3 in 24 F videos, against 18 in 7 of 21 real.
6. **Ours name a feeling in about 1 item in 11** (reading of the pattern hits; the pattern alone says 15%):
   - first-person feeling lines: 1 in 38
   - hooks with a feeling word: 5 of 38 (real 8 of 21)
   - our own device is to name what the habit feels like ("It feels like kindness. It feels like hiding.") and then give the look verdict ("reads tired")
7. **Title age brackets differ mainly because the channel type differs.**
   - "Over 60" titles are 96% faceless.
   - Titles with no age are 67% real.
   - Within faceless titles, "over 60" leans to hair, mistakes and "instantly"; "over 50" leans to "expensive" and "elegant". These gaps are clear in the counts; the "younger" gap (21% against 14%) is not.
   - Feeling words in titles are near zero in every bracket: "confident" 3 of 1,182, "invisible / turn heads" 3.
8. **Comments by the viewer's own age (132 found):** median 70.
   - 50s: 11, 10 of them on real videos, mostly about going gray.
   - 60s: 41, led by comfort and permission (13).
   - 70+: 73. Loss of ability or of her past self is a little more common here (9, against 2 in the 60s).
   - Neither gap is beyond chance at these sizes.
9. **The script data can't show brackets.**
   - The 3 real "over 50" scripts are all Marie-Anne Lecoeur.
   - 36 of our 38 titles say "over 60".
   - F has 6 "over 50" against 12 "over 60".

---

## Part A. The driving emotions

### A1. What viewers say they feel about themselves (comments, hand)

Every comment was read. A comment counts only when it voices a feeling about the viewer herself, not an opinion of the video. One comment can carry two codes.

| Feeling about herself | R (804) | F (792) | O (42) | Likes, study | Per 1,000 study comments |
|---|---:|---:|---:|---:|---:|
| **The operator's frame** | | | | | |
| Invisible, unseen, unnoticed | 2 | 4 | 0 | 468 | 3.8 |
| Unheard by stylists or shop staff (not listened to) | 3 | 4 | 0 | 220 | 4.4 |
| Not catered for or not shown: makers, videos | 5 | 7 | 2 | 730 | 7.5 |
| Frumpy, dowdy, "given up", "look rubbish" | 15 | 10 | 0 | 1,343 | 15.7 |
| Losing her spark or confidence, feeling old | 9 | 8 | 0 | 599 | 10.7 |
| **What else shows up** | | | | | |
| Comparison with her past self or younger women | 20 | 4 | 0 | 3,124 | 15.0 |
| Judged (family, society, stylists, colleagues, the video) | 12 | 12 | 1 | 2,494 | 15.0 |
| Permission and rebellion | 37 | 73 | 3 | 10,346 | 68.9 |
| Relief, being understood | 33 | 13 | 0 | 4,574 | 28.8 |
| Recognising her own mistake ("guilty of…") | 2 | 7 | 0 | 249 | 5.6 |
| Pride (in her hair, her age, her style) | 8 | 13 | 0 | 1,123 | 13.2 |
| Feeling young inside, better than ever | 0 | 4 | 0 | 108 | 2.5 |
| Being seen: compliments received | 10 | 10 | 0 | 736 | 12.5 |
| Unhappy about a body part | 17 | 12 | 1 | 4,099 | 18.2 |
| Hope, a fresh start ("ready for rebooting") | 3 | 2 | 0 | 87 | 3.1 |
| Hiding during a grow-out or after illness | 2 | 1 | 0 | 34 | 1.9 |

**Literal word checks (pattern, viewer comments, study):**
- "frump": 7
- "invisib": 3
- "spark": 4, none of them about the viewer herself (one is about the makeover client: "had then lost her sparkle along the way" [9] `WgkP3h4QWpg`)
- "unheard", "no one listens" or "listen to me / us": 3
- "dowdy", "let myself go" or "given up": 4
- "confiden": 24, of which 17 are on F, many in comments that read as generated

The practical problems in `01-viewers.md` (no stylist who can cut 28, no clothes that fit 28, health or mobility 22) are not re-counted here.

#### Invisible, unseen (6)
- "I've been waiting my entire life to be invisible, so I'm leaning into it now." [148] `Fs17Qc6l8Ug`
- "I like being older and don't mind being invisible." [92] `Fs17Qc6l8Ug`
- "I do feel invisible and would love to grow it out." [10] `_OQsPYjIfsQ`. This is the only complaint.
- As a general observation, not about herself: "When older women stop caring about their appearance, other people stop caring about the older women" [217] `ixlexruRC6c`
- As a joke: "I lost 85 pounds and no one noticed!" [1] `G-RW7ih19Y4`

#### Unheard: by the stylist or the shop (7), and by makers and videos (14)
- "So true I am tired of hair dressers telling me I need curtain bangs" [157] `9LvzTBzXL5k`
- "I tell hairstylists point black, NO GRANNY CUT, and what do they give me? A granny cut." [22] `XR3IwlcIcCY`
- "How do you get stylists to listen to what you want and not just do their thing?" [3] `CkVrghocoPs`
- "salespeople always try to convince me that black looks good on me and everyone" [11] `NMvN5bjcwks`
- "part of the problem is the lack of dresses designed and tailored for the mature woman" [296] `MWQ6T1wURJU`
- "Why on earth do they make dresses for older woman with so many bows and ruffles and big puffy sleeves?" [184] `G5y1gFHWPIA`
- "I virtually never see any hairstyle examples for this combo." [126] `UUS1R9oWx4o`
- Ours: "They never give input for women like me who are tall and have long legs." [0] `yl-Vq9WyLzY`

#### Frumpy, dowdy, given up (25)
- "Me sitting here in my leggings and baggy old t-shirt wondering why I'm even watching this." [436] `gfbWOw00Y-M`
- "I look and feel heavier and frumpier when I tuck in my top." [324] `ixlexruRC6c`
- "I just look like a pregnant Old Lady" [137] `vBsFMkGDbhA`
- "I’m at that stage where I think I should just throw on a burka and forget about it." [41] `XByilJlme5Y`
- "I felt so exposed and ugly." [28] `CkVrghocoPs`. This is about a pixie cut that went wrong.

Reading: in about half of the 25 the feeling is tied to one garment or one cut, not to how she sees herself overall.

#### Losing her spark or confidence, feeling old (17)
- "I am struggling with not being able to do the things I did when I was younger." [392] `eKCl-bRx8wg`. The viewer is 71.
- "This old age stuff is hard!" [11] `vATkBSPjQmc`
- "I feel like I look old and haggard all the time." [0] `rU56_ly6l2s`. This one is about thinning hair.
- "I lost my confidence 10 years ago when I was diagnosed with Multiple Sclerosis." [0] `NT1mEOX-p7Y`
- "Time to 'get pretty again'. I have missed myself." [0] `_OQsPYjIfsQ`. The viewer is 77 and writing after a broken back.

Six of the 17 come with an illness: chemotherapy (2), MS, a stroke, the broken back, a thyroid condition. Two are from viewers under 50. Four comments say the opposite, that they feel young inside or better than ever: "still has the heart and mind of a youthful person" [106] `XByilJlme5Y`; "I'm 71 and feel better than I have since i was 30." [1] `Fs17Qc6l8Ug`.

#### Comparison with her past self or with younger women (24)
- "I no longer have a waistline. Am I alone?" [798] `ixlexruRC6c`
- "Gravity sucks, but it is what it is" [471] `WgkP3h4QWpg`
- "I never want to look like I’m trying to look like my daughter" [363] `gfbWOw00Y-M`
- "I'm 63 and the last thing I want to look like is a baby doll." [333] `MWQ6T1wURJU`
- "I've started getting insecure and guilty over bright colors thinking that such brilliance belongs to the youger ones" [28] `qFLenue5BBI`. The viewer is 44.

20 of the 24 are on real videos. Most compare her body with her own past body. When younger women come up (5), the fear is looking too young ("baby doll", "my daughter"), not too old.

#### Judged (25)
- "all of the ways in which I was told I wasn’t good enough by society, by peers, by advertising and tv" [1.7K] `UUS1R9oWx4o`
- "Waiting for the day when being old isn't an insult." [390] `ixlexruRC6c`
- "husband argued that I looked like an old hag and I needed to try to look like I was when we met." [228] `_OQsPYjIfsQ`
- "My former stylist told me women to go gray looked 10 years older" [0] `xNuoMiG2kVw`
- "I have people say it's too wild, and stylists thin it out to be more respectable." [0] `_OQsPYjIfsQ`

By who judges (hand):

| Who judges | Comments |
|---|---:|
| Society, "people", being old as an insult | 9 |
| The video or channel itself | 5 |
| Stylists | 4 |
| Family (a husband, a son, children) | 3, or 4 counting the mother in the 1.7K comment |
| Colleagues | 2 |
| Others' opinions | 1 |
| Teased | 1 |
| Shop staff | 0 |
| Daughters | 0 |

Daughters appear only as the age the viewer doesn't want to copy.

#### Permission and rebellion (113)
- "I do not mind looking older because I am older" [502] `eKCl-bRx8wg`
- "I'm just so proud to have made it this far!" [368] `Fs17Qc6l8Ug`
- "I wear what I want, when I want, where I want, why I want, and how I want." [343] `6byOPawCepI`
- "I’m 73. I was in nursing 40 yrs. I love my comfortable clothes" [341] `Fs17Qc6l8Ug`
- "I am 71. I am an old lady. I don't care if my clothes say that I am an old lady. Celebrate my age!" [244] `ixlexruRC6c`

This is wider than the 55 "wear what I want" comments in `01-viewers.md`, because it also counts pride in age and comfort first. 30 of the 113 are on the two "Scream 'Old Lady'" videos.

#### Relief, being understood (46)
- "ohhh THAT’S why i think i look better with height on my hair." [924] `UUS1R9oWx4o`
- "This is the first realistic make over I've ever seen." [471] `WgkP3h4QWpg`
- "Seeing others with bodies like mine was so encouraging!" [248] `XByilJlme5Y`
- "This is the first time in my life that I have understood what is going on with my hair when I blow dry." [95] `vFul5tvg1Cw`
- "Thank you for caring about us older women ❤" [27] `6byOPawCepI`

Reading: 7 of the 46 are on Summer Beauty's cranial-top video. That video's script names almost no feeling at all (A2); the relief comes from an explanation. Next come Justin Hickox's two videos (5 each) and Diana GOSS's colour video (4).

#### Which of the operator's three feelings the evidence supports

| The operator's feeling | Evidence | Strength |
|---|---|---|
| **Unheard** | As a feeling about herself, no: the word is never used, and 1 complaint of feeling invisible. As a practical complaint, yes: stylists who don't listen (7), makers and videos that don't cater for her (14), the 78 model complaints | **Weak** as an inner feeling; **moderate** as "the salon and the shops don't listen" |
| **Frumpy** | 25 self-descriptions (1.6% of study comments), most of them about one garment; the word itself 7 times | **Weak to moderate** |
| **Losing her spark** | 17 (1.1%), a third tied to illness; the word "spark" is never used about herself; outnumbered about 8 to 1 by permission and pride lines (134) | **Weak** |
| **What else, and stronger** | Permission and rebellion 113; relief at understanding 46 (cognitive more than emotional); body and past-self comparisons 54; judged 25 | |

Reading: the feeling most present in her own words is "I've earned the right to wear what I like". The pain she names is mostly practical, and her thanks are mostly for an explanation.

---

### A2. How real presenters tie a feeling to a fix

#### Counts

| Measure | Real | F/AI | Ours | Basis |
|---|---:|---:|---:|---|
| Items naming an inner feeling, list videos only | **31 of 115 (27%)** in 17 videos | | | hand, item by item |
| Items with a strict feeling pattern | 28 of 115 (24%) | 38 of 91 (42%) | 32 of 209 (15%) | pattern. Real items use hand boundaries from the notes' structure maps; F and ours use the spoken item numbers ("number three", "the second cut"), so 14 F and 36 of ours qualify |
| …the feeling in the first third of the item | 10% | 25% | 4% | pattern |
| …the feeling in the last third | 11% | 20% | 7% | pattern |
| Items with a look word (older, dated, modern, flattering, elegant, expensive…) | 64% | 90% | 68% | pattern |
| Strict feeling words per 1,000 words, in items | 1.4 | 2.3 | 0.4 | pattern |
| Hooks (first 60 s) with a feeling word | 8 of 21 | 9 of 24 | 5 of 38 | pattern |
| First-person feeling lines ("I feel", "I felt", "I regret", "I'm petrified") | **18, in 7 videos** | 3, in 3 | 1, in 1 | pattern, each read |
| "You'll feel / make you feel" lines | 19, in 10 | 42, in 16 | 13, in 12 | pattern |

**Hand coding, the 17 real list videos (items naming a feeling / items):**

| Video | Feeling items / items | Notes |
|---|---:|---|
| Melissa Murrell `gfbWOw00Y-M` | 4/10 | all before the fix |
| Diana GOSS `eKCl-bRx8wg` | 3/5 | |
| Marie-Anne Lecoeur `ixlexruRC6c` | 3/7 | |
| Justin Hickox `vFul5tvg1Cw` | 0/5 | |
| Summer Beauty `UUS1R9oWx4o` | 0/4 | hook only |
| Glam Girl Gabi `9LvzTBzXL5k` | 2/5 | plus her own feeling in the intro |
| Justin Hickox `rU56_ly6l2s` | 2/7 | |
| chery `XCf4o0ZOOiw` | 4/7 | |
| Summer Beauty `xNuoMiG2kVw` | 3/3 | patience and commitment more than pain |
| Marie-Anne Lecoeur `G-RW7ih19Y4` | 2/8 | |
| Diana GOSS `9ZNV79Uva3g` | 0/5 | hook only |
| Diana GOSS `NMvN5bjcwks` | 0/5 | hook only |
| Marie-Anne Lecoeur `MWQ6T1wURJU` | 2/7 | |
| Adore Your Wardrobe `vBsFMkGDbhA` | 1/6 | plus intro and outro |
| Tracy Campoli `NT1mEOX-p7Y` | 5/11 | all her own feelings |
| Marie-Anne Lecoeur `n9ICHZq3_tY` | 0/10 | |
| Aliceinparis `fLIVwKa-y3U` | 0/10 | |

Before the fix: 24 items. After it: 15. The four makeover or consultation videos (Rami Jabali ×2, Woman in midlife, MAKEOVERGUY) are a single story each and are counted separately below.

#### Twenty chains: pain, then the trick, then the result felt or seen

| # | Presenter, video | Pain named | The trick | Result, felt or seen | Her own experience |
|---|---|---|---|---|---|
| 1 | Marie-Anne, `ixlexruRC6c` | "hiding behind tons of fabric because they have lost their self-confidence" [0:35] | "I encourage you to choose clothes that follow your natural lines" [0:51] | "Show off your shape. This is youthful. Celebrate your shape or the woman you are" [1:06] | no |
| 2 | Marie-Anne, `ixlexruRC6c` | "the vibe is square, oldfashioned, stuck in the past. This tight also means uptight" [1:55] | "May I suggest you try a V-neck?" [2:11] | "open up your neckline, open up your self-confidence" [2:26] | no |
| 3 | Marie-Anne, `ixlexruRC6c` | "Comfort is non-negotiable. I agree with you. You don't have to suffer to be stylish." [4:04] (the viewer's objection, granted) | "Look for elegant flats, smart sneakers, or low heeail boots" [4:37] | "can have comfort and style and look youthful by doing so" [5:00] | "Here in France, we women…" |
| 4 | Marie-Anne, `G-RW7ih19Y4` | "everybody else knows that your knickers are too small" [2:06] | size up | "There is no shame whatsoever in upping the size of your underwear, but you will feel more comfortable. The outline of your clothing will look so much more flattering." [2:08] | no |
| 5 | Marie-Anne, `MWQ6T1wURJU` | "Many women tell me that they are ashamed of their bodies. Maybe because they are older bodies, no longer as stoned as they used to be and also overweight." [3:35] | "But we all have womanly feminine figures that we need to embrace. Why not put a belt on?" [3:45] | "to create and show off an hourglass silhouette" [4:06] | reported from clients |
| 6 | Diana GOSS, `eKCl-bRx8wg` | "instead of concealing some areas we feel less confident about under some loose shapeless clothes and make ourselves look heavier and older than we are" [2:10] | a fitted silhouette | "accentuate the areas we really feel confident about" [2:24] | "we"; shown on her own body |
| 7 | Diana GOSS, `eKCl-bRx8wg` | "so I simply look dull and older because of the wrong color framing my face" [4:01] | "if I only switch to cool light and clear Hue" [4:06] | "brightens up my features makes my skin look more clear eyes pop up and mostly important make me feel more confident" [4:13] | yes: the "before" is on her |
| 8 | Diana GOSS, `9ZNV79Uva3g` (hook) | "if you tried five pair of jeans and none of them fit it doesn't mean there is something wrong with your figure" [0:07] | five fit rules | "we want to look and feel confident in jeans" [0:26] | "we" |
| 9 | Gabi, `9LvzTBzXL5k` | "every time I get bangs, I regret it" [3:45]; "I instantly just feel off, like the balance of my face feels immediately off" [3:53] | read your proportions | "if you've ever tried to style and something just felt wrong, that's usually a sign that the proportions are off" [4:00] (the reframe) | yes, her own |
| 10 | Gabi, `9LvzTBzXL5k` | "if you've been scarred by a bad bang experience in the past" [7:55] | side bangs | "If you're really nervous about trying bangs, but you really, really want to, this is also one of the easier and safer places to start" [8:57] | no |
| 11 | Gabi, `9LvzTBzXL5k` | "Do you feel cuter with a bit of forehead covered" [10:23] (the feeling is the test) | the hat test | "choose the style that you feel the most confident in" [10:53] | "one of my favorite tricks that I came up with in the salon" |
| 12 | Justin Hickox, `rU56_ly6l2s` | "if you're really like insecure and you've got some pieces that you can see the scalp through" [13:49] | "you use fibers your hair looks 10 times thicker" [13:53] | "it just feels much more youthful much more flattering" [14:00] | no |
| 13 | chery, `XCf4o0ZOOiw` | "Most women have a slight receding hairline. I do myself, which is why I wear my hair a little bit closer to the center." [10:19] | move the part | "be open-minded when you're switching your part because you are so used to seeing yourself a certain way" [11:10]; "you probably get lots of compliments and no one will even know what was different" [11:20] | yes |
| 14 | Summer Beauty, `xNuoMiG2kVw` (hook) | "you either picture yourself looking washed out or 20 years older overnight. I get it. We have been conditioned to believe that gray hair equals giving up." [0:12] | three ways to go gray | "so you can feel amazing every step of the way" [0:45] | "We"; her mother and mother-in-law |
| 15 | Summer Beauty, `xNuoMiG2kVw` | "You're kind of curious or even tempted, but you're also not ready to commit 100%." [9:35] | blending, foils | "It's all just really dependent again with what you're comfortable with and what works for you." [12:32] | "I was so proud of this work and a bit nervous as she is my mother-in-law" [8:23] |
| 16 | Woman in midlife, `2e50uMLaCtE` | "when I have my hair back like this and I'm not wearing makeup and and it's frizzy, I don't feel great" [0:11] | a test strand; "I'm petrified, but I'm trusting you." [3:17] | "Beauty can't be defined for us from the outside." [6:25] | the whole video; "If you've ever grown out your hair, you know the fear of I am never going back." [3:46] |
| 17 | Tracy Campoli, `NT1mEOX-p7Y` | "I'm not going to feel like a stuffed sausage" [15:34] | wide-leg jeans and a black blazer | "I feel comfy, I feel put together." [15:56]; "I got stopped on the street by these young girls that were like" [17:09], then "By the way, you look great." [17:13] | yes, all of it |
| 18 | MAKEOVERGUY, `WgkP3h4QWpg` (the client) | "I don't think I look particularly wonderful with long hair. I think my forehead is high. My weight is one thing I'm still working on." [2:31] | the makeover | "I feel like I was back 20 years at least how I used to look" [7:49]; "I feel fine and I'm 69" [9:00] | the client's own words |
| 19 | Rami Jabali, `qwM0s0Q3Rjw` (the client) | "your hair might feel a bit thinner, but it's actually it's got a good thickness on the roots. But, maybe you're just feeling the middle and the ends" [3:01] | a shorter cut | "And that's the main target that it looks full. Like you don't feel like there's something wrong." [8:06]; "Don't be scared. Put your hand through." [8:38] | no |
| 20 | Melissa Murrell, `gfbWOw00Y-M` | "I have polycystic ovaries, which means I'm plagued by excess hair" [27:11] | the hair-removal device | "don't be afraid to do these extra little things" [27:51] | yes |

#### Patterns in the real chains

- **The usual shape is a look, a swap, then a look.** Most real items are told in look words: "I look heavy and older"; "more balanced… flirty and younger". A felt line is added in about a quarter of them. Two-thirds of real items use a look word (pattern). Diana GOSS's notes describe her items as ending "in age words" (`notes/diana-goss__NMvN5bjcwks.md`).
- **Where the feeling sits:**
  - before the fix in 24 items and after it in 15 (hand)
  - the pattern finds it about equally in the first and last thirds (10% and 11%)
  - in hooks it is usually both: the fear named, then a promised feeling (chains 8 and 14)
  - in single items it is either the pain that opens the item (chains 1, 5, 6) or a closing "pro tip" that turns the fix into a feeling (chain 2)
- **How long:** one sentence, about 12 words (4-29) over the feeling lines in these chains. The longest are hook lines (chain 14, about 30 words). No real item spends more than two sentences on the feeling before the fix arrives; the gap between pain and fix is 10-20 seconds in chains 1-3 and 5-7.
- **The words:**

  | Word or family | Times in real items (pattern) |
  |---|---:|
  | feel, feels, felt, feeling | 45 |
  | comfortable | 10 |
  | confident, self-confidence | 8 |
  | nervous, scared, afraid, insecure | 5 |
  | shame, ashamed | 3 |
  | stress, stressful | 6 |

  The words of the operator's frame are near absent from real scripts: "frumpy" is said in 4 real videos (`03-body-feelings-ctas.md` §2.2), and "invisible" / "disappear" in 2.
- **How she shows she has felt it:**
  - **In her own person, 10 of 21 videos:**
    - Gabi's bangs
    - chery's hairline
    - Melissa Murrell's PCOS and broken toe
    - Tracy's "I feel" lines
    - Diana GOSS wearing the "before" herself
    - Summer Beauty's nerves over her mother-in-law and her own hair type
    - Woman in midlife throughout
    - Marie-Anne's "my hair problem"
  - **Through a client's words: 2 more** (MAKEOVERGUY, Rami Jabali).
  - **None at all: 9.** These include both Justin Hickox videos, Aliceinparis and Marie-Anne's French-pieces video.
- **The reframe:** before the fix, several presenters move the fault off the woman:
  - "that's usually a sign that the proportions are off" (chain 9)
  - "it doesn't mean there is something wrong with your figure" (chain 8)
  - "We have been conditioned to believe" (chain 14)

  `03-body-feelings-ctas.md` §2.1 counts the explicit not-your-fault line in 4 real videos against 12 F.
- **The result is more often seen than felt.** Chains 13 and 17 end on a compliment from someone else. Chains 4, 7, 12 and 17 end on how she will feel ("feel more comfortable", "feel more confident").

#### For contrast: faceless and AI scripts

- **Feeling as a label on the clothes:** "a combination that whispers confidence and quiet luxury" (`YeKT0zkdIrw` [13:18]). That one video has 12 "confidence" hits in its items.
- **The pain named before the fix, as in the real scripts:**
  - "it feels like it's helping us hide the parts of our body we no longer feel confident about" (`kKjLX7Q6wc8` [4:56])
  - "when you're over 50 and feeling self-conscious about your body" (`Fs17Qc6l8Ug` [1:54])
- **The promised feeling after the fix:** "Clothes should never make you feel trapped. They should make you feel comfortable, confident, and graceful." (`6byOPawCepI` [4:32])
- **Invented first-person feeling lines (3 videos):**
  - "Some made me feel fabulous. Some made me look like I'd given up." (`h6Y1RZzOlzg` [0:32])
  - "every year I felt a little more erased and I blamed my age" (`_OQsPYjIfsQ` [6:55])
  - "I nearly cried in the bathroom" (`_OQsPYjIfsQ` [10:29])
- **The nervous-start move, shared with real presenters (chain 10):** "If you're nervous about leggings, start here." (`h6Y1RZzOlzg` [2:59])

---

### A3. Our 38 scripts

| Measure | Ours | Real | F/AI |
|---|---:|---:|---:|
| Items with a strict feeling pattern | 32 of 209 (15%) | 24% | 42% |
| …of which about a woman's feeling, on reading | **about 19 items (9%)** | hand 27% | |
| Hooks (first 60 s) with a feeling word | 5 of 38 | 8 of 21 | 9 of 24 |
| First-person feeling lines | 1 | 18 | 3 |
| "It feels like… / feels safe" lines (what the habit feels like) | 17, in 11 videos | 3 | 9 |
| Videos with no feeling item at all (pattern) | 9 of 36 | 4 of 17 | 0 of 14 |

**What the other pattern hits in our items are:**
- "confident" said about an object, about 10: "one confident red mouth" (`Rba36JLtcYY`), "One clean, confident, heavy line" (`EB4Vwf5G0QE`), "the most confident combinations of the season" (`3JBVSs9ETu4`)
- a physical sensation, about 9: "you can feel the band pressing" (`bMlBJn27PEU`)
- "Fine hair fears heaviness", 2 (`EB4Vwf5G0QE`)

**Where our feeling lines sit (reading the 20 lines):**
- 5 early in the item, naming the fear: "The fear, of course, is that it's too young, a bow for a girl of 20, and that fear is exactly backwards." (`bMlBJn27PEU` [12:43])
- 6 in the middle
- 9 near the end (20 lines in 19 items), mostly reassurance or a bridge: "there's no shame in skipping it" (`w6w_ktMBHXM`); "the deep cool shades so many women are afraid of" (`3JBVSs9ETu4` [13:51])

**Our closest matches to the real chains:**
- "If you've been nervous about going shorter, start here" (`XGBMW0cEggI` [9:48])
- "Nervous about bright color? Start small with a scarf" (`oH6XV-weIGs` [14:41])
- "if people have started asking whether you're tired on days you feel perfectly fine, the problem is usually shape" (`pgMgC2aGPUw` [7:31])
- "It looks tidy and tidy feels safe. So why does it make you look older than you feel?" (`qmYPg0L3qZU` [6:37])

**Our own device:**
- **Name what the habit feels like, then give the look verdict:** "It feels like kindness. It feels like hiding." (`EVFmbo51Ou0` [2:01]), then "A size six in a shapeless sweater reads tired. A size 16 in a fitted blazer reads polished." (`EVFmbo51Ou0` [1:13])
- **The result is a picture, not a feeling:** "what's left in the mirror is simply a well-dressed woman at any size" (`EVFmbo51Ou0` [15:45])
- **The presenter forewarns rather than confides:** "I know this one is going to sting a little" (`EVFmbo51Ou0` [10:37])
- **The one first-person line is given to a woman in a scene:** "That is not how I feel." (`e2v7TDK3SW0` [0:38])

Reading: ours sit nearer the real presenters than the faceless channels on how few feeling words they use, but below both on items with a feeling. None of ours shows the presenter herself having felt it.

---

## Part B. Age brackets

### B4. Titles (1,182 core outliers)

A title counts in a bracket when it says the age as an age ("over 60", "after 50", "60+", "in your 60s", "#over50"). "Multi" means two or more ages ("Over 50, 60 & 70"). "Older words" means "older women", "mature" or "grandmother" with no number.

| Bracket | Titles | Median views | 500K+ | Median views ÷ channel normal | Real / faceless / unclear | Median views, real / faceless |
|---|---:|---:|---:|---:|---|---|
| over 50 | 200 | 79,500 | 10 | 5.2 | 87 / 96 / 17 | 69,000 / 85,000 |
| over 60 | 251 | 52,000 | 5 | 28.7 | 10 / 241 / 0 | 36,500 / 55,000 |
| over 70 | **8** | 98,000 | 0 | 24.2 | 4 / 3 / 1 | 201,000 / 23,000 |
| multi (50 & 60, 50-60-70) | 47 | 52,000 | 3 | 4.8 | 8 / 39 / 0 | 71,500 / 52,000 |
| older words, no number | 15 | 34,000 | 1 | 7.7 | 5 / 9 / 1 | |
| **no age** | 629 | 76,000 | 63 | 5.7 | 419 / 119 / 91 | 83,000 / 51,000 |
| over 40 (for reference) | 31 | 46,000 | 5 | 2.2 | 17 / 1 / 13 | |

**Lead words by bracket (pattern, share of titles):**

| Word family | over 50 | over 60 | over 70 (8) | multi | no age |
|---|---:|---:|---:|---:|---:|
| mistakes, avoid, never, stop, don't | 23% | **31%** | 0 | 13% | 17% |
| elegant, classy, chic, timeless | 21% | 20% | 1 title | **49%** | 8% |
| younger, youthful | 9% | **21%** | 1 | 0 | 3% |
| expensive, rich, luxury | **12%** | 6% | 0 | 2% | 3% |
| instantly | 7% | **16%** | 0 | 0 | 3% |
| hair (cut, bob, pixie, bangs, gray) | 13% | 26% | 3 | 11% | **38%** |
| gray or silver | 3% | 1% | 0 | 0 | **16%** |
| body (slim, tummy, petite, plus, arms…) | 12% | 12% | 1 | 11% | 10% |
| older, "ages you" | 9% | 10% | 2 | 9% | 6% |
| frumpy, dowdy, dated | 8% | 3% | 0 | 4% | 3% |
| old lady, granny | 2% | 5% | 0 | 0 | 0.2% |
| comfort | 0.5% | 1% | 0 | **13%** | 0.3% |
| confident | 0 | 1 title | 0 | 0 | 1 title |
| invisible, turn heads, compliments | 1 title | 1 title | 0 | 0 | 0 |

**Examples:**
- **over 50:**
  - "7 Things That Scream 'Old Lady' (Harsh But True): Style Over 50" (1.0M, real)
  - "7 Colour Combinations That Make You Look Expensive & Elegant | Women's Fashion Over 50" (1.0M, faceless)
  - "How To Look Slimmer: The MOST EFFECTIVE Style Tips For Women Over 50" (547K, real)
- **over 60:**
  - "5 Glasses That Make Women Over 60 Look Instantly Younger" (910K)
  - "DON’T Get a "Granny" Cut! 3 Haircuts That Actually Make You Look 10 Years Younger At 60" (698K)
  - "5 Real-Body Tricks to Wear Sleeveless Dresses at 60+ (No Perfect Arms Needed)" (325K). All three are faceless.
- **over 70:**
  - "The Most Requested Haircut for Women Over 70 | She Drove All the Way From Idaho for This Haircut!" (352K, real)
  - "Cutting My 77-Year-Old Mom’s Hair | For Women Over 70 Years Old" (259K, real)
  - "7 Dresses That Make Women Over 70 Look 10 Years Younger" (130K, faceless)
- **multi:** "5 Ways to Avoid Looking Heavy and Outdated After 50 and 60!" (754K); "Everyday Summer Fashion for Women Over 50, 60 & 70 | Classy & Comfortable Looks" (348K)
- **no age:**
  - "You're Styling Your Bob Haircut WRONG! Do THIS Instead- 5 SECRETS" (3.2M)
  - "How To INSTANTLY Look Slimmer! 10 Style Tricks" (2.9M)
  - "Double Chin or Sagging Neck? NEVER WEAR These Hairstyles! DO THIS INSTEAD…" (1.2M), all real

**The confound, and the comparison inside faceless titles.** The bracket mostly stands in for the channel type: "over 60" is 96% faceless and "no age" is 67% real. Faceless titles alone, over 50 (96 titles, 43 channels) against over 60 (241 titles, 61 channels):

| Word family, faceless titles only | over 50 | over 60 | Fisher exact p |
|---|---:|---:|---:|
| expensive, rich, luxury | 21% | 6% | 0.0002 |
| mistakes, avoid, never, stop | 16% | 31% | 0.004 |
| hair | 15% | 27% | 0.016 |
| elegant, classy, chic | 32% | 20% | 0.02 |
| instantly | 8% | 17% | 0.04 |
| younger | 14% | 21% | 0.12 |
| old lady, granny | 2% | 5% | 0.25 |
| body | 12% | 12% | 1.0 |
| median views | 85,000 | 55,000 | |

Reading: within faceless titles, "over 50" leans to looking expensive and elegant, and "over 60" to hair, avoiding mistakes and looking younger instantly. Feeling words are almost absent from titles in every bracket: "confident" 3 of 1,182, "invisible / turn heads / compliments" 3, "frumpy / dated" 45. In "over 70" the real titles are hair services for a named older client.

### B5. Comments by the age the viewer gives (hand, 132)

I found 132 of the 149 age-giving comments in `01-viewers.md` again by pattern and read each one; the rest use forms my pattern missed. Median 70, as in `01-viewers.md`.

| Viewer's age | Comments | Real / faceless | Permission, comfort | Pride, young inside | Loss of past self or spark | Frumpy, given up | Judged | Relief | Stylist let-down | Body, health, limits | Hair topic / clothes topic |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| under 50 | 7 | 5 / 2 | 1 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 3 / 1 |
| 50s | 11 | **10 / 1** | 3 | 1 | 2 | 0 | 0 | 0 | 1 | 1 | **8** / 5 |
| 60s | 41 | 15 / 26 | **13 (32%)** | 6 | 2 (5%) | 0 | 0 | 6 | 1 | 3 | 16 / **30** |
| 70+ (70s 55, 80+ 18) | 73 | 21 / 52 | 16 (22%) | 5 | **9 (12%)** | 2 | 4 | 3 | 3 | 4 | 35 / 41 |

**50s (11):** going gray and thinning hair lead, and 7 of the 11 are on Summer Beauty's gray video or other hair videos. There is no "frumpy" and no "invisible".
- "I’m 52 and tired of covering the grays so I’m going to start with option #3!" [18] `xNuoMiG2kVw`
- "At nearly 53, I have NEVER had a stylist tell me my" [31] `UUS1R9oWx4o`
- "I'm still working on accepting my new weight." [55] `G-RW7ih19Y4`

**60s (41):** comfort and permission, heels against flats (6 comments aged 61-64 on the shoe video), pride and feeling better than before. There are two directions on age: refusing "old lady" clothes and gray hair, and refusing to look too young.
- "I'm 62, I wear whatever I feel comfortable!" [363] `6byOPawCepI`
- "I’m 62 and I feel more beautiful now then I did when I was younger." [151] `NMvN5bjcwks`
- "I'm 63 and no longer give a toss how people view me." [109] `ixlexruRC6c`
- "I am 65 years old and I refuse to use old lady clothes." [51] `WgkP3h4QWpg`
- The one "invisible" complaint is 67 (`_OQsPYjIfsQ`).

**70+ (73):** comfort and convenience, pride in age, staying current rather than younger, and more lines about lost abilities, the changed body, illness and widowhood. Fine or thin hair and stylists come up most on the ChicAfterSixty fine-hair video, where about 20 viewers answered its age-and-place question.
- "I am struggling with not being able to do the things I did when I was younger." [392] `eKCl-bRx8wg` (71)
- "I don’t mind looking my age, but want to look my age in the 21 century." [227] `Fs17Qc6l8Ug` (almost 73)
- "I'm 72 and you're keeping me current." [191] `gfbWOw00Y-M`
- "I want wash and go hair. I want convenience." [143] `XR3IwlcIcCY` (80 in 9 days)
- "I just discovered this and I am 80 and I KNOW I can look much better now." [85] `WgkP3h4QWpg`
- "I'm almost 80 & lost my husband last year. But I still try & dress for him" [0] `6byOPawCepI`

**Size of the differences:**
- Loss of past self or spark: 60s 2 of 41 against 70+ 9 of 73. Fisher exact p = 0.32.
- Permission: 13 of 41 against 16 of 73. p = 0.27.
- Neither gap is beyond chance.
- The 50s group sits almost wholly on real hair videos, so its topics follow the videos it was found on.

### B6. Scripts by the title's bracket

| Side | over 50 | over 60 | no age | other |
|---|---:|---:|---:|---:|
| Real | 3 (all Marie-Anne Lecoeur) | 0 | 17 | 1 (over 40, Tracy Campoli) |
| F/AI | 6 | 12 | 5 | 1 multi |
| Ours | 1 | **36** | 1 | |

**Medians per 1,000 words (pattern):**

| | strict feeling | look words | age said | "younger" |
|---|---:|---:|---:|---:|
| Real, over 50 (3) | 1.8 | 20.7 | 2.2 | 1.5 |
| Real, no age (17) | 1.6 | 2.3 | 0 | 0 |
| F, over 50 (6) | 2.3 | 17.3 | 2.9 | 0.5 |
| F, over 60 (12) | 1.3 | 7.4 | 2.3 | 0.4 |
| Ours, over 60 (36 of 38) | 0.4 | 5.2 | 1.1 | 0 |

Reading:
- On the real side the "over 50" group is one presenter's refrain ("old lady" said 10 times), so the bracket can't be told apart from Marie-Anne Lecoeur.
- On the faceless side the "over 50" scripts carry more look words and somewhat more feeling words than the "over 60" ones. The "over 50" six include the copied "Scream 'Old Lady'" script and the two Black-women videos, so the difference again follows the video, not the age.
- Ours are all one bracket.
- The data can't show how a script changes its feeling lines by bracket.

### B7. What differs by bracket, and how strong the evidence is

| Bracket | Titles | Comments (viewer's own age) | Scripts | What differs | Strength |
|---|---|---|---|---|---|
| **over 50** | 200; median 79.5K; half real | 50s: 11, mostly real hair videos | real 3 (one presenter), F 6 | faceless titles lean to expensive and elegant (21%, 32% of faceless titles); viewers in their 50s talk about going gray and hair | titles: **moderate** (n = 96 faceless, clear word gaps); comments: **very weak** (11); scripts: **none** |
| **over 60** | 251; median 52K; 96% faceless | 60s: 41 | F 12, ours 36 | faceless titles lean to hair, mistakes, "instantly" (27%, 31%, 17%; "younger" 21%, not a clear gap); viewers in their 60s lead on comfort and permission (32%) | titles: **moderate**, but the same thing as "faceless"; comments: **weak**; scripts: **none** usable |
| **over 70** | 8 | 70+: 73 (the largest group) | 0 | titles: hair services (4 real); comments: somewhat more lost ability, illness, widowhood (12% against 5%), staying current | titles: **too few**; comments: **weak** (p 0.32) |
| **no age** | 629; median 76K; 67% real; 63 of the 500K+ | (viewers of every age) | real 17, F 5 | hair 38% and gray 16%; "younger" 3%; feeling words near zero | titles: **strong** as a description, but it is the real-presenter side |

**Are the differences big enough to matter?**
- In titles, the word mix differs by bracket, and inside faceless titles some of the gaps are large: "expensive" 21% against 6%.
- In comments and scripts, the differences between brackets are small, rest on 11-73 comments and 3-12 scripts, and are not beyond chance.
- Across every bracket the larger and steadier difference is between real and faceless channels, and between the practical pain viewers name and the emotional labels faceless titles use.
- On this evidence the bracket differences are not large enough to read as separate emotional profiles. Viewers in their 70s show a modest and uncertain tilt towards loss.

---

## What this can't show

- **Who stays silent.** Commenters are about 1 in 1,000 viewers, self-selected, often older and more opinionated. A viewer who feels unheard or invisible may simply not comment, so low counts are not proof the feeling is absent.
- **Feelings behind practical words.** "No stylist can cut my hair" may carry frustration or feeling unheard. I coded what was said, not what may lie under it.
- **Cause.** Nothing here shows that a feeling line, or its place in the item, made a video win. Real and faceless videos differ in presenter, channel size, topic and length at once.
- **Item boundaries.** Real items use the notes' structure maps, read by hand. F and ours use spoken item numbers by script, which cut some items wrongly and left out 10 F videos and 2 of ours. The item counts on the three sides were not made the same way; the 27% (real, hand) and about 9% (ours, reading) are the like-for-like pair.
- **One coder.** The comment codes, the hand item codes and the "reading" lines are one reader's calls. The 28 comments read as generated were excluded by judgement.
- **Brackets.** The title age is the channel's choice of label, not the audience's age, and it moves with the channel type. Only 8 "over 70" titles exist, and our scripts cover one bracket. YouTube's own audience ages are not in the study.
- **Ages in comments** are what 132 viewers chose to say. Several videos asked for the viewer's age, which inflates some bands.

## Check

The comments were parsed from all 83 `comments.md` files with `python3 -I`, scratchpad only, and coded by hand over a full read of all 1,638 viewer comments. Every quoted transcript line in A2 and A3 was matched by script to its transcript (case, punctuation and caption tags ignored). Each tag is the start of the segment where the quote begins. Every quoted comment was matched to its comment file with its likes and video ID. Title counts come from a script over `round2/outliers-all.csv` and `round2/channels-all.csv`, with the age patterns checked by eye on every "over 70", "over 40" and "multi" title and on the no-age titles that contain a number. Fisher exact tests are two-sided.
