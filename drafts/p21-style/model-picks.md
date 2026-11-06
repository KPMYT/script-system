# P21 style: model transcript picks (DRAFT, research only)

Picked 2026-11-06 for the new style skill design: one page of rules plus ONE real model transcript chosen for the video type, read for flow only (how she opens, moves point to point, sounds like a person), never for words.

**Sources and rules followed.** Only M-rows of `studies/style/models/approved-models.csv` (real presenters). No F-rows (faceless or AI). No men (Justin Hickox, M06, M08, M10, M12, left out). Video types and the models already filed under each come from the style pack (`/root/.claude/skills/synced/*/style-scripts/SKILL.md`, "The video types", and `references/models/INDEX.md`). Each pick was confirmed as a woman presenting on camera in the first person from its `meta.md` ("Type (round 2): real_on_camera" and "Presenter as heard in the transcript") and from reading the transcript itself. No video folder has a `notes.md` (each holds only `meta.md`, `comments.md` and `transcript.txt`), so `meta.md` and the transcript were the checks.

**How the figures were got.**
- **Words:** spoken words, counted by this helper on 2026-11-06 from `transcript.txt` with the `[m:ss]` timestamps, bracket tags (`[music]`) and `>>` removed. Each count matches the "Transcript words" figure in that video's `meta.md`. (Note: the iter-10 `models.md` counts, e.g. M19 "3,235" and M21 "1,062", come out the same as a plain `wc -w`, which counts the timestamps too, so they run about 15% high.)
- **Punctuated:** full stops counted in `transcript.txt` on 2026-11-06 (M08, M12, M25, M26 and M27 have 0 to 2 and were avoided).
- **Date, duration, views, views against normal:** copied from each `meta.md`, read on 2026-11-06. The views were counted on 2026-10-28 (the collection date `meta.md` gives).
- **Where the list starts:** the timestamp in `transcript.txt` where item one begins.
- **Quotes:** every quoted line under "don't take" was copied from the transcript and checked by script on 2026-11-06 as an exact match against the transcript text with the timestamps removed and the line breaks joined. They are marked **[copied]**. Caption mis-hearings are kept as captioned.
- "Why", "weaker on" and "suits" are this helper's reading, not measured.

Our scripts run 2,100 to 2,700 words. A pick between 1,500 and 4,000 words is treated as fine; anything outside that is flagged.

---

## Summary

| Type | Chosen | Second | For whom |
|---|---|---|---|
| Mistakes that age you | **M18** Capsule Closet Stylist, "10 Fashion Mistakes That Make You Look Years Older" (fashion) | **M04** Chery, "Your Fine Hair Doesn't Have to Look Older" (hair) | Both. M18 is a British stylist, the closest voice to Scarlett. For Diane's French titles, M21 (type 7) is the French-voiced option |
| Never these, wear these instead | **M13** Adore Your Wardrobe, "Ditch the Shorts: 7 Things to Wear Instead" | **M28** Aliceinparis, "10 Things French Women Never Buy" | M13 both (Scarlett first); M28 Diane |
| The best N | **M07** Glam Girl Gabi, "Best Bangs for your Face Shape" (hair) | **M13** (fashion: the seven alternatives as a best-N list) | Both |
| Styling it wrong: N secrets | **M09** Summer Beauty, "STOP Styling Your Hair WRONG For Your Face & Head Shape!" (hair) | **M24** Diana GOSS, "6 Styling Mistakes That Are Making You Look SHORTER" (fashion) | Both (a thin type, see doubts) |
| How to wear X | **M19** Beth Djalali, "Why Linen Looks Frumpy After 50 (And How to Fix It)" | **M30** Kay Harms, "How to Tie a Scarf this Winter" (4,063 words, a little long) | Both |
| Body-shape fixes | **M24** Diana GOSS, "6 Styling Mistakes That Are Making You Look SHORTER" | **M23** Marie-Anne Lecoeur, "How To Look Slimmer" | M24 both; M23 Diane (weight-framed, see "don't take") |
| The rules she never breaks (incl. the French rules) | **M28** Aliceinparis, "10 Things French Women Never Buy" | **M21** Marie-Anne Lecoeur, "7 Things That Scream 'Old Lady'" (923 words, short) | Diane. Scarlett has no real-presenter model of this type (see doubts) |
| The why explainer | **M01** Summer Beauty, "Why Your Haircut Never Looks Right (It's Not You)" (hair) | **M19** (fashion) | Both |
| One mistake, then N swaps | **M13** (the capris-and-maxis mistake, then seven swaps) | **M19** (the linen mistake, then ten pieces) | Both |

**Distinct transcripts picked: 12.** These are the files that would go in the skill:

| # | ID | Presenter, channel | Path | Words | Types |
|---|---|---|---|---|---|
| 1 | M01 | Summer, Summer Beauty | `studies/style/data/summer-beauty/i5jFYNeCHGM/transcript.txt` | 2,617 | why explainer |
| 2 | M04 | Chery Gibson, chery | `studies/style/data/chery/XCf4o0ZOOiw/transcript.txt` | 2,022 | mistakes (hair) |
| 3 | M07 | Gabi, Glam Girl Gabi | `studies/style/data/glam-girl-gabi/9LvzTBzXL5k/transcript.txt` | 2,067 | best N |
| 4 | M09 | Summer, Summer Beauty | `studies/style/data/summer-beauty/UUS1R9oWx4o/transcript.txt` | 2,547 | styling it wrong |
| 5 | M13 | Kelly Snyder, Adore Your Wardrobe | `studies/style/data/adore-your-wardrobe/7ecJWmEQ3Ks/transcript.txt` | 2,397 | never these; best N (2nd); one mistake then N swaps |
| 6 | M18 | Michelle Barrow, Capsule Closet Stylist | `studies/style/data/capsule-closet-stylist/Rg_YiVy40fk/transcript.txt` | 2,536 | mistakes (fashion) |
| 7 | M19 | Beth Djalali | `studies/style/data/beth-djalali/Hionkf3pHJc/transcript.txt` | 2,716 | how to wear X; why (2nd); one mistake (2nd) |
| 8 | M21 | Marie-Anne Lecoeur | `studies/style/data/marie-anne-lecoeur-the-french-chic-exper/ixlexruRC6c/transcript.txt` | 923 | rules (2nd); Diane's mistakes |
| 9 | M23 | Marie-Anne Lecoeur | `studies/style/data/marie-anne-lecoeur-the-french-chic-exper/G-RW7ih19Y4/transcript.txt` | 2,195 | body-shape (2nd, Diane) |
| 10 | M24 | Diana GOSS | `studies/style/data/diana-goss/6Yz0BKoKG-M/transcript.txt` | 3,168 | body-shape; styling it wrong (2nd) |
| 11 | M28 | Alice, Aliceinparis | `studies/style/data/aliceinparis/saDURZc-pno/transcript.txt` | 1,903 | rules; never these (2nd) |
| 12 | M30 | Kay Harms, Dressed for My Day | `studies/style/data/dressed-for-my-day-with-kay-harms/uBqNLIiLnv4/transcript.txt` | 4,063 | how to wear X (2nd) |

Four of the twelve suit Diane's French voice (M21, M23 and M28 are French women on camera; M22 was considered too, see type 5). Eight are American or British presenters for Scarlett and for either channel's flow.

---

## 1. Mistakes that age you

### Chosen: M18, Capsule Closet Stylist, "10 Fashion Mistakes That Make You Look Years Older"
- **Presenter:** Michelle Barrow, a woman on camera, first person ("Hi, my name's Michelle Barrow. I've been a personal stylist for 26 years"; British usage such as "trousers" and "pop socks", per `meta.md` and the transcript).
- **Path:** `studies/style/data/capsule-closet-stylist/Rg_YiVy40fk/transcript.txt`
- **Words:** 2,536 (in range). **Punctuated:** yes (148 full stops).
- **Published** 2025-12-07 · 13:21 · **98,658 views** (as of 2026-10-28) · 28.19x the channel's normal (`meta.md`, read 2026-11-06). Item one starts at 1:15.
- **Suits:** both; Scarlett first (a British stylist's voice, the nearest to a former London designer).
- **Why:** ten things she owns, each one named plainly, then why it ages her, then an exemption for comfort or medical need, then the swap. It's spoken, not read: she turns to the viewer's likely objection before every verdict, which gives the natural point-to-point flow we want. It's at our length, and the items are wardrobe pieces (cardigans, rain jackets, shoes, trousers, leggings), which is our main engine.
- **Weaker on:** the opening runs into a subscribe ask before item one, and the last two items (underwear, a handbag full of rubbish) wander. Its tone is blunt in places ("No, just no").
- **Don't take:**
  - Plugs: the free "discovery call" and the free capsule wardrobe planner; the like/subscribe/share ask before item one.
  - Catchphrases and signature turns **[copied]**:
    - "please like, subscribe, share my content with anybody"
    - "Those long cardigans are a big no-no for me"
    - "Okay, to me, that just looks like it's an old person's jacket."
    - "No, just no in any kind of shape nor form."
    - "I bet that a lot of you watching this will recognize it straight away."
    - "Let me know in the comments how you get on."

### Second: M04, chery, "Your Fine Hair Doesn't Have to Look Older (Do This Instead)"
- **Presenter:** Chery Gibson, a woman hairstylist and salon owner on camera, first person ("I see it in my salon all the time"; named in the description, not the speech, per `meta.md`).
- **Path:** `studies/style/data/chery/XCf4o0ZOOiw/transcript.txt`
- **Words:** 2,022 (in range). **Punctuated:** yes (124 full stops).
- **Published** 2026-04-28 · 11:53 · **103,785 views** (as of 2026-10-28) · 14.03x normal (`meta.md`, read 2026-11-06). Item one starts at 0:26.
- **Suits:** both, for hair titles.
- **Why:** the tightest hair-mistakes flow in the set: about 40 words of hook, then straight into item one, and each bridge makes the next mistake sound bigger. Each item names the mistake, explains it through light, contrast or structure, and gives what to ask the stylist instead. It worked as the model for a Diane hair list in iter-10.
- **Weaker on:** the third item turns into a three-product run. Most items are about cut and styling, not colour.
- **Don't take:**
  - Plugs: the Virtue volumizing primer, a volumizing powder, the R+Co Balloon Dry Volume Spray, her website and the like/subscribe close.
  - Catchphrases and signature turns **[copied]**:
    - "I see it in my salon all the time."
    - "I guarantee you there's something on this list that you're probably doing right now."
    - "If you have been on the fence about cutting your length, this is your sign."
    - "I hear this one all of the time." (an iter-10 writer echoed this one)
    - "which brings me to the next mistake"
    - "we're not going for a 1987"

*For Diane's French "mistakes" titles:* M21 (see type 7) is the French-voiced option of this type.

## 2. Never these, wear these instead

### Chosen: M13, Adore Your Wardrobe, "Ditch the Shorts: 7 Things to Wear Instead | Fashion Over 50"
- **Presenter:** Kelly Snyder, a woman on camera, first person ("Hey everybody, it's Kelly Snyder from Adore Your Wardrobe"); she counts herself among women over 50 (`meta.md` and the transcript).
- **Path:** `studies/style/data/adore-your-wardrobe/7ecJWmEQ3Ks/transcript.txt`
- **Words:** 2,397 (in range). **Punctuated:** yes (142 full stops).
- **Published** 2026-04-05 · 13:18 · **814,141 views** (as of 2026-10-28) · 33.92x normal (`meta.md`, read 2026-11-06). Item one starts at 3:37.
- **Suits:** both; Scarlett first.
- **Why:** the "never" (capris and maxi dresses) is said once, clearly, with the reason (they cut the leg at the widest point and add weight), and then every item is a "wear this" with the same three parts: what to look for on the label, the length, and how to style it. Warm, chatty and direct; it moves item to item with a clear signpost ("Number two is", "Option number three"). It's the best-performing real model against its channel's normal among the fashion lists.
- **Weaker on:** the never-list is two things, not one per item, so for a title with one "never" per item the writer has to pair them. It leans on body jokes we wouldn't use.
- **Don't take:**
  - Plugs: the free "summer ready guide" (said three times) and the presenter's programme intro.
  - Body words: "cankles", "Frumpsville", "spider veins".
  - Catchphrases and signature turns **[copied]**:
    - "they look like you got off the fashion train at Frumpsville"
    - "because they are the devil. They are the devil."
    - "Real Housewives of Beverly Hills hot girl summer"
    - "I always think of her like the ugly duckling from high school who had a serious glow up in adulthood."
    - "Yeah, yeah, yeah, I know, I said no shorts, but here's the truth."
    - "That's where I want us to live. We are going to live there."

### Second: M28, Aliceinparis, "10 Things French Women Never Buy (But Everyone Else Does)"
- See type 7 (the same file). Suits Diane: each "never" has an "instead" ("Instead of spending money on ... French women prefer ..."). Weaker here because most of its items are about shopping and gadgets, not clothes.

## 3. The best N

### Chosen: M07, Glam Girl Gabi, "Best Bangs for your Face Shape (At Any Age!)"
- **Presenter:** Gabi, a woman on camera, first person ("my name is Gaby, and I've been a hairstylist and makeup artist for 20 years"; she uses her own face as an example). `meta.md` notes she reads as younger than 50 (round-2 reading).
- **Path:** `studies/style/data/glam-girl-gabi/9LvzTBzXL5k/transcript.txt`
- **Words:** 2,067 (in range). **Punctuated:** yes (98 full stops; a non-auto "English" caption track per `meta.md`).
- **Published** 2025-07-20 · 11:19 · **1,902,659 views** (as of 2026-10-28) · 12.4x normal (`meta.md`, read 2026-11-06). The list starts at 4:16.
- **Suits:** both, for hair titles.
- **Why:** a true best-N: four options (curtain, air, side, blunt), each with what it is, why it flatters and for whom, and who should skip it. The voice is warm and permission-giving, and the flow between items is natural. It ends on a simple self-test rather than a recap.
- **Weaker on:** about four minutes of method before item one (longer than we'd open), celebrity comparisons, and no over-50 framing (the title says "At Any Age").
- **Don't take:**
  - Plugs: her "2025 Haircut Trends" video and the bang-cutting tutorial; the celebrity examples (Sarah Jessica Parker, Liv Tyler).
  - Catchphrases and signature turns **[copied]**:
    - "draw arrows to absolutely everything that you hate about your face"
    - "What's it going to be?"
    - "Here's the truth. Flattering bangs aren't just about face shape, they are about balance."
    - "One woman isn't more beautiful than the other"
    - "It's called the hat test."
    - "Now I know you're going to ask this, so I'm going to answer it preemptively."

### Second: M13 (see type 2)
- For fashion best-N titles: the seven alternatives each have the why and the for whom (fabric, length, styling, "if you're petite", "if you're fuller through the hip"). The video was built as an "instead" list, so the writer reads it for its item rhythm, not its "never" opening.
- *Not picked:* M14 (Tracy Campoli, the "best N" model in INDEX) is 5,226 words with a sponsor read and heavy try-on, too long to read for flow.

## 4. Styling it wrong: N secrets

### Chosen: M09, Summer Beauty, "STOP Styling Your Hair WRONG For Your Face & Head Shape!"
- **Presenter:** Summer, a hairstylist, on camera, first person ("As a hair stylist of 18 years"; "fine thick straight hair like myself"); `meta.md` notes she reads as under 50 (round-2 reading).
- **Path:** `studies/style/data/summer-beauty/UUS1R9oWx4o/transcript.txt`
- **Words:** 2,547 (in range). **Punctuated:** yes (128 full stops).
- **Published** 2025-04-11 · 15:15 · **1,224,258 views** (as of 2026-10-28) · 27.2x normal (`meta.md`, read 2026-11-06).
- **Suits:** both, for hair titles.
- **Why:** the only real woman's "styling it wrong" video with punctuation: the thing she's been told (the rules), why it doesn't fit her own head, then the better way at home, step by step (product, lift, tool, a bonus tip). The voice explains and reassures ("this is not to say that low cranial tops look bad").
- **Weaker on:** it leans on celebrity photos (Laura Dern, Kerry Washington and others) for whole stretches, it isn't numbered, and its technical terms (cranial top, facial thirds) aren't our viewer's words.
- **Don't take:**
  - Plugs: the "Volu" hot tool, the products linked below, her earlier videos; the celebrity examples.
  - Catchphrases and signature turns **[copied]**:
    - "Hello beauties."
    - "So, ask and you shall receive."
    - "Hopefully, this is making sense to you guys."
    - "I am excited for this part."
    - "will have everyone fooled into thinking you have that high cranial top"
    - "Be sure to leave a heart emoji in the comments"

### Second: M24, Diana GOSS (see type 6)
- For fashion titles: each "mistake" is a common outfit formula she shows wrong, explains through proportion, then fixes piece by piece ("Let's fix it."). Weaker here because it's built on try-ons (she wears both versions).
- *Not picked:* M08 and M12 (Justin Hickox: a man, and unpunctuated), M27 (Diana GOSS, colour hacks: unpunctuated).

## 5. How to wear X

### Chosen: M19, Beth Djalali, "Why Linen Looks Frumpy After 50 (And How to Fix It)"
- **Presenter:** a woman on camera, first person, speaking to women 50 plus ("welcome back to Style at a Certain Age where I bring you the trusted edit for women 50 plus"; "I'm 5'8""); her name isn't said in the speech (`meta.md`).
- **Path:** `studies/style/data/beth-djalali/Hionkf3pHJc/transcript.txt`
- **Words:** 2,716 (just above our 2,700). **Punctuated:** yes (219 full stops).
- **Published** 2026-05-17 · 16:01 · **158,326 views** (as of 2026-10-28) · 7.92x normal (`meta.md`, read 2026-11-06).
- **Suits:** both; worked as the model for a Scarlett "how to wear" title in iter-10.
- **Why:** one piece, the fear named first (it wrinkles, it adds weight), a lived scene, then the why (three buying rules, three pitfalls), then the pieces, each with the occasion ("a garden lunch", "a Saturday in town"). The fear she names is our viewer's fear, and the voice is a friend talking.
- **Weaker on:** from 7:20 to the end the ten pieces are a one-brand haul with prices, so the second half is product-led.
- **Don't take:**
  - Plugs: Quince (all ten pieces, prices, "links in three places"), the affiliate note; her show name and sign-off.
  - Catchphrases and signature turns **[copied]**:
    - "Half the women I know over 50 have quietly given up on linen."
    - "Stay with me"
    - "and I bet it happens at your house, too." (an earlier writer echoed this one)
    - "women I love, women I respect"
    - "Lived-in is American classic."
    - "style has no expiration date, and neither do you."
    - also her sign-off name for viewers: "Grits and Glamours"

### Second: M30, Dressed for My Day with Kay Harms, "How to Tie a Scarf this Winter - Feel Confident & Look Stylish in Scarves"
- **Presenter:** Kay Harms, a woman on camera, first person ("My name is Kay and this is Dress for My Day. My goal really is just to help women over 50"; `meta.md`).
- **Path:** `studies/style/data/dressed-for-my-day-with-kay-harms/uBqNLIiLnv4/transcript.txt`
- **Words:** 4,063 (**longer than 4,000**, about 1.5 times our length). **Punctuated:** yes (286 full stops).
- **Published** 2025-12-18 · 20:28 · **78,099 views** (as of 2026-10-28) · 3.12x normal (`meta.md`, read 2026-11-06). The first tie starts at 2:35.
- **Suits:** both.
- **Why:** the only real model filed under this type in INDEX. It names the real reason she won't wear the piece (it overwhelms her, "I just look like here comes the scarf"), answers it with every tie, and puts numbered tips between the ties as breathers. Gentle, permission-heavy voice for women over 50.
- **Weaker on:** long, and much of it is knot-by-knot tying steps the viewer has to watch; the end is channel housekeeping.
- **Don't take:**
  - Plugs: the channel memberships and Bible study; the brands (Lily Silk, Sarah Flint, Anthropologie, Nordstrom); "I'll link it".
  - Catchphrases and signature turns **[copied]**:
    - "Am I right?"
    - "You know what I mean?"
    - "Things don't have to be perfect."
    - "She's got more to do than just doodah in front of the mirror all day, right?"
    - "Then just jush it into place a little bit."
    - "We still have so much to contribute, ladies."

*Also considered for Diane:* M22, Marie-Anne Lecoeur, "How Not To Wear Summer Dresses Over 50" (`studies/style/data/marie-anne-lecoeur-the-french-chic-exper/MWQ6T1wURJU/transcript.txt`, 2,031 words, punctuated, 2025-04-13, 628,761 views as of 2026-10-28). A French woman on camera at our length, but it's built on on-screen example photos ("You can see in this orange example"), and Diane's profile bans pointing at the screen, so it wasn't picked. If it's used, don't take "Bonjour friendship ladies", "Good florals good. Bad florals bad.", "Oh my gosh, you will look a million dollars in it." or "Think of them as smile lines for clothes." **[copied]**.

## 6. Body-shape fixes

### Chosen: M24, Diana GOSS, "6 Styling Mistakes That Are Making You Look SHORTER (Fix These!)"
- **Presenter:** a woman on camera, first person (named only in her Instagram handle; mentions "my son"; no age said; `meta.md`).
- **Path:** `studies/style/data/diana-goss/6Yz0BKoKG-M/transcript.txt`
- **Words:** 3,168 (in range, a little long). **Punctuated:** yes (231 full stops).
- **Published** 2025-06-26 · 18:11 · **541,064 views** (as of 2026-10-28) · 12.58x normal (`meta.md`, read 2026-11-06). Item one starts at 1:17.
- **Suits:** both.
- **Why:** the body-shape thesis our type wants, said early: the problem is the styling, not her body ("you'll never blame your body or height again"). Every fix keeps the comfort and changes only proportion and where the eye goes (one-third and two-thirds, vertical flow, the narrowest part of the leg). Never about weight.
- **Weaker on:** it's built on try-ons (she wears the wrong and the right version, "I'm wearing ..."), with a sponsor, a quiz plug and a tease. Read it for the idea order inside each fix, not the opening.
- **Don't take:**
  - Plugs: Petite Studio (the sponsor, with a sale code), the free style personality quiz, her Instagram, the "little surprise" tease.
  - Catchphrases and signature turns **[copied]**:
    - "Tricky question, isn't it?"
    - "you'll never blame your body or height again"
    - "Okay, I know what you're thinking."
    - "Let's fix it."
    - "Same jumpsuit, just styled smarter."
    - "Voila."

### Second: M23, Marie-Anne Lecoeur, "How To Look Slimmer: The MOST EFFECTIVE Style Tips For Women Over 50"
- **Presenter:** Marie-Anne Lecoeur, a French stylist on camera, first person ("as a professionally trained stylist"; captioned "Marian"/"Mariana"; `meta.md`).
- **Path:** `studies/style/data/marie-anne-lecoeur-the-french-chic-exper/G-RW7ih19Y4/transcript.txt`
- **Words:** 2,195 (in range). **Punctuated:** yes (161 full stops).
- **Published** 2025-06-15 · 16:28 · **547,210 views** (as of 2026-10-28) · 6.51x normal (`meta.md`, read 2026-11-06).
- **Suits:** Diane (the only French woman's body-shape video).
- **Why:** it opens on body acceptance before any technique ("The most important thing is for you to accept and love your body"), and every technique is told in optical terms: where the eye goes, where the body is cut, why a seam or a V narrows. The voice is a French stylist's.
- **Weaker on:** **it is framed on weight** ("10 lbs thinner", "one to two sizes"), which our type forbids, and much of it points at example dresses on screen. Read it for the order (accept first, then technique by technique), never for its promise.
- **Don't take:**
  - The weight framing entirely; the "yes dress" links in the description; pointing at the screen.
  - Catchphrases and signature turns **[copied]**:
    - "If you want to look 10 lbs thinner, you're in the right place."
    - "size up, slim down"
    - "10 lb thinner for sure."
    - "What's not to like?"
    - "I found you a yes dress."
    - "This is a vaoom dress indeed."

*Not picked:* M17 (Darlene Obiyan, 3,844 words): its opening is a long personal weight story, it's built on try-ons, and its voice is heavy with "girl", which would pull a writer off our persona.

## 7. The rules she never breaks (incl. the French rules)

### Chosen: M28, Aliceinparis, "10 Things French Women Never Buy (But Everyone Else Does)"
- **Presenter:** Alice, a woman on camera, first person, French-accented English ("Bonjour, I am French"; "here in Paris"; `meta.md`).
- **Path:** `studies/style/data/aliceinparis/saDURZc-pno/transcript.txt`
- **Words:** 1,903 (in range, a little short). **Punctuated:** yes (123 full stops).
- **Published** 2025-12-10 · 14:51 · **118,369 views** (as of 2026-10-28) · 4.23x normal (`meta.md`, read 2026-11-06). Item one starts at 0:27.
- **Suits:** Diane.
- **Why:** the national-lens rules shape from a real French woman: each item is a practice ("French women never ..."), the cultural reason she can check against her own life, then what French women do instead. It goes straight into item one with almost no intro, and the "instead" is the same move every time, which is the French-rules engine.
- **Weaker on:** the topic is shopping and gadgets (Stanley cups, smart watches, skin-care fridges), not dressing; item three becomes a long sponsor read. Its audience isn't over 50 (INDEX).
- **Don't take:**
  - Plugs: the Omnia pillow (Sleep and Glow) sponsor read and holiday offer; the brands (Stanley, Cafe Kitsune, Bodum, Daniel Wellington, Tissot, Cartier, Jacquemus).
  - Catchphrases and signature turns **[copied]**:
    - "Bonjour, I am French"
    - "It's simply not in our culture."
    - "At least, it's not really in our culture."
    - "Much more popular, especially here in Paris."
    - "Something I personally experienced."
    - "Let me know what you think about this video."

### Second: M21, Marie-Anne Lecoeur, "7 Things That Scream 'Old Lady' (Harsh But True): Style Over 50"
- **Presenter:** Marie-Anne Lecoeur, a French stylist on camera, first person ("Here in France, we women"; `meta.md`).
- **Path:** `studies/style/data/marie-anne-lecoeur-the-french-chic-exper/ixlexruRC6c/transcript.txt`
- **Words:** 923 (**shorter than 1,500**, under half our length). **Punctuated:** yes (82 full stops).
- **Published** 2025-08-17 · 8:02 · **1,038,117 views** (as of 2026-10-28) · 12.36x normal (`meta.md`, read 2026-11-06).
- **Suits:** Diane (both for rhythm). Also Diane's option for "Mistakes that age you".
- **Why:** a fixed four-beat item (the thing, why it ages, "So, what can you do instead?", a one-line pro tip) in a French woman's voice, with France as the standard ("Here in France, we women even in our 70s and over, wear lovely shoes"). It worked as the model for a Diane list in iter-10.
- **Weaker on:** short, so it shows the item rhythm, not long-form pacing. It's a mistakes list with a French lens rather than a rules list.
- **Don't take:**
  - "scream" (banned in Diane's profile) and "instantly"; the end-screen video tease.
  - Catchphrases and signature turns **[copied]**:
    - "Are you ready for little tough love?"
    - "scream old lady"
    - "My pro tip is"
    - "you disappear faster than a macaron at a Parisian cafe"
    - "no Crocs, no stocks"
    - "Cruel to be kind and all that."

*For Scarlett:* no real-presenter video of "the woman who gets it right" exists in the approved M-rows (INDEX files only F06 here, and F-rows are out). The nearest are M28's shape (the practice, the reason, the instead) told through Scarlett's own lens, or M18's item rhythm.

## 8. The why explainer

### Chosen: M01, Summer Beauty, "Why Your Haircut Never Looks Right (It's Not You)"
- **Presenter:** Summer, a female hairstylist and image consultant on camera, first person ("after 19 years as a hair stylist"; she uses her own heart-shaped face, a wig and photos; no age given; `meta.md`).
- **Path:** `studies/style/data/summer-beauty/i5jFYNeCHGM/transcript.txt`
- **Words:** 2,617 (in range). **Punctuated:** yes (125 full stops).
- **Published** 2026-06-19 · 15:03 · **665,238 views** (as of 2026-10-28) · 14.78x normal (`meta.md`, read 2026-11-06).
- **Suits:** both, for hair titles. It was the model in iter-08 run B, which the judge scored best ("the only one that sounds like one woman talking all the way through", `tests/iterations/iter-08/RESULTS.md`).
- **Why:** the explainer shape: the cut that feels off and the feeling (blaming the stylist or herself), the relief ("you've never been told"), a diagnosis before any advice, then the fixes by length, layers and part, with the part saved for last.
- **Weaker on:** the middle (face shapes and length-to-width ratios) is technical and runs long, and the presenter isn't aimed at women over 50.
- **Don't take:**
  - Plugs: the paid digital face shape analysis and her website; her own face and wig as proof.
  - Catchphrases and signature turns **[copied]**:
    - "Do you ever wonder why some people can pull off almost any haircut?"
    - "something most of us were never really taught how to identify"
    - "Are you ready? Let's go."
    - "which I'm very jealous of"
    - "If you're still confused, don't stress."
    - "Drop a heart emoji in the comments if you did."

### Second: M19 (see type 5)
- For fashion titles: "why linen looks frumpy" names the fear, turns it with the why ("they've been buying it the wrong way"), then gives the rules and pitfalls before any product.

## 9. One mistake, then N swaps

### Chosen: M13 (see type 2)
- **Why for this type:** the one mistake (capris and maxi dresses) is set up in the hook and explained in one unit (what they do to the leg, why they age her), done by 3:37 of 13:18 (about a quarter of the way in), and then each swap is a full item with its own signpost ("Number two is the skort", "Option number three"), the fabric, the length and the styling. That's the type's shape almost exactly.
- **Weaker on:** the mistake is two garments, not one; the swaps run about 250 words each, shorter than our 300 to 450.

### Second: M19 (see type 5)
- **Why:** the one mistake (buying linen the wrong way) explained through rules and pitfalls, then ten pieces. **Weaker on:** the mistake part runs to 7:20 of 16:01 (about 45%), past the type's one-third, and the swaps are a one-brand haul.
- *Not picked:* M14, which the pack files for the swaps (5,226 words, a sponsor read and try-ons).

---

## Doubts for the operator

1. **Word counts:** iter-10's counts include the timestamps (about 15% high). The figures here are spoken words and match `meta.md`.
2. **Short or long:** M21 is 923 words (short); M30 is 4,063 (just over 4,000). The other ten are between 1,903 and 3,168.
3. **M23 is weight-framed** ("10 lbs thinner"). It's picked only as Diane's French body-shape second, for its order; the writer must skip its promise. If that's too risky, M24 alone covers the type.
4. **Thin types:** "Styling it wrong" has no ideal real woman's model: M09 leans on celebrity photos, and M24 on try-ons and a sponsor. "The rules she never breaks" has nothing for Scarlett among the M-rows.
5. **Not aimed at over 50:** M01, M07 and M09 (younger hairstylists, no age framing) and M28 (a general audience). Their flow transfers; the over-50 framing has to come from the brief.
6. **Screen-pointing:** M22, M23 and M24 point at what's on screen, and Diane's profile bans that. A writer reading them could pick up the habit.
