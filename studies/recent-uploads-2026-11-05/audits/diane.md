# Audit: Diane de Chambray, three newest uploads (2026-11-05)

**Channel:** Diane de Chambray (`UC2z5yffdjwr3xpr-iDp9Yvw`). **Persona:** `personas/diane-de-chambray.md`. **Pack:** `style-scripts/SKILL.md`. **Words a minute in the profile:** 172. **Book:** *The French Way* (`personas/books/diane-de-chambray-book.md`).

**Sources.** Captions pulled with NexLev `get_bulk_video_transcripts` on 2026-11-05 (all three came back; none empty). Titles, publish dates, lengths and views as collected the same day (views are public counts at collection, 1 to 4 days after upload, and say nothing yet). Transcripts: `../transcripts/diane-<videoId>.txt`.

**Caution.** These are YouTube's automatic captions of the voiceover: **what the voice said, not the script the VA pasted in** (the scripts and briefs aren't in this repo). Caption punctuation is the caption system's guess, so sentence and question counts are approximate. Timestamps quoted below are the start of the caption segment where the quote begins; in the transcript files each line holds about 30 seconds, so a quote sits in the line whose timestamp is at or just before the one given. No channel of the operator's is connected to NexLev, so there is no retention data.

**Scanner.** `core/script-scanner.py` was run on a timestamp-stripped copy of each transcript (kept outside the repo) with `--rules style-scripts/SKILL.md personas/diane-de-chambray.md`, `--refs` on the profile, the pack, `excerpts.md`, `voice-samples.md`, `hooks.md` and every model file, and `--title`. It found **nothing to fix on sight on all three**: no ban hits, no copy-guard runs, no sign-off, no name, no subscribe ask. Its shape-test flags (short "staccato" sentences) are left out as judged lines, not breaks. On #3 it found "no spoken signposts" because the captions put item one mid-sentence ("Well, number one, ..."): a caption effect, so item counts for #3 were done by hand.

| # | Video | Title | Published | Length | Views at collection | Caption words | Words a minute (real) | Minutes at 172 |
|---|---|---|---|---|---|---|---|---|
| 1 | `2IYXD6OaV8I` | Stop Trying to Dress Young After 50 (The French Way) | 2026-11-04 | 14:24 | 196 | 2,363 | 164 | 13.7 |
| 2 | `YCdL6Zbxfps` | 7 Hair Colors That Make Women Over 60 Look INSTANTLY Younger (The French Way) | 2026-11-02 | 12:47 | 984 | 2,158 | 169 | 12.5 |
| 3 | `aJlpJC2qB2w` | 9 Things Elegant Women Over 60 Are NOT Wearing This Winter | 2026-11-01 | 15:28 | 786 | 2,630 | 170 | 15.3 |

Diane's normal was 607 views on 2026-10-28 (`studies/style/own-baseline-2026-10/SUMMARY.md`); #2 is already above it at 3 days and #3 at 4 days. Too early to read anything into.

---

## 0. Were these made with the library? Yes, all three (reading, from the evidence)

We don't know for sure that the VAs used the style pack. The captions say they did: every packaging habit the study found in all 13 old scripts is gone, and the three scripts use things that exist **only** in the new profile (drafted 2026-10-29): the exact heritage line, and one each of the three personal details Claude drafted for her, a different one in each video.

| Check | Old scripts (13, `studies/style/pack-diagnosis-2026-10-28/persona-sweep.md`, `comparison/06-own-vs-winners.md`) | #1 | #2 | #3 |
|---|---|---|---|---|
| Self-introduction ("I'm Diane...") | 13 of 13 | none | none | none |
| Sign-off "À bientôt" | 12 of 13 | none | none | none |
| Book pitched | twice, "389 pages" in all 13 | once at 4:32 + one line at 14:05 | once at 3:33 + one line at 12:29 | once at 3:46 + one line at 15:10 |
| Last line | "which of the five rules you're taking to the mirror tonight" shape, 12 of 13 | comment ask about her | comment ask about her | comment ask about her |
| Comment question | which one first | the style rule she was handed at 50 | the hair color she's worn longest | her age and where she's watching from |
| Heritage line "the way I was raised in Paris" | never ("the women I know in Paris" instead) | not used | 4:35 | 1:46 |
| Approved personal detail (one per script) | none | one in, one out (12:35) | the changed mind (1:15) | the scarf knot without a mirror (8:34) |
| French claims hedged | 12% (21 of 180) | 7 of 7 (one borderline) | 2 of 2 | 8 of 8 |
| Seconds / words to item one | median 71 s / 206 words | 26 s / 73 words | 31 s / 82 words | 25 s / 70 words |
| "but" per 1,000 words | 1.0 | 5.9 | 5.6 | 5.3 |
| Prices | in 13 of 13 | 0 | 0 | 0 |
| "Picture...", "quietly", "reads as", "small gold hoops", "voila", "cherie" | in every script | 0 | 0 | 0 |
| Subscribe ask | 13 of 13 | 0 | 0 | 0 |

The hooks also follow named models from `style-scripts/references/hooks.md` move for move (reading; the VA's plan isn't here to confirm which model it named):

- **#3 is M29's hook almost exactly.** M29 (Style with Serena, fall shoes): question to her, feared look named, count line "starting with the flats in her closet", permission "keep what you like". #3: "What makes a woman look older the moment she steps outside this winter?" / "The coat she bought for warmth and nothing else." / "So, here are nine things elegant women over 60 have stopped wearing this winter and the swap for each one. Starting with the coat hanging by your door." / "Some of these you'll keep anyway. That's fine. If you love it, I'll tell you how to wear it." [0:00-0:25]. 70 words (M29: 72).
- **#2 follows M27** (Diana GOSS, colour hacks): the feeling named, then "color is the quick tool", then the promise. #2: "If you've been putting off the color appointment because you're afraid of what a new shade will do to your face, I understand." / "But color is also the fastest tool you have. Faster than any haircut." / the count line [0:00-0:31]. 82 words.
- **#1 fits M20** (promise word, contrast, count line), with M28's French contrast: "Stop trying to dress young after 50, because it does the opposite of what you want." / "This isn't about dressing old or giving up. Women in France mostly don't chase young." / "So, here are nine things that say trying too hard with a French swap for each one." [0:00-0:26]. 73 words.

Three different hook models across three videos, as the rotation rule asks.

---

## 1. "Stop Trying to Dress Young After 50 (The French Way)" (`2IYXD6OaV8I`)

**In one line:** a clean library script and the best of the three: short hook, item one at 26 seconds, every item explains why, hedged French claims, checks given plainly, book once in the right place; its one clear break is a makeup item (lashes and liner) in a pack that doesn't cover makeup.

### What works

- **The title in the first sentence, and the promise straight after:** "Stop trying to dress young after 50, because it does the opposite of what you want. The outfit meant to take years off puts them back on." [0:00]. "Young" is said 9 times (scanner).
- **The feeling named in plain words, before the fix,** as the pack asks: "But, the worst part is the feeling underneath. The tug at the back, the glance in every shop window, the whole dinner spent managing a hem." [1:03]; "The feeling here is the one that comes up most. The body changed and the jeans didn't and somewhere in there you start dressing around the jeans." [5:30].
- **The blame moved off her, in fresh words:** "But the jean was cut for a hip that hasn't arrived yet and no amount of dressing around it will change the cut." [5:40].
- **The why in every item:** "A very short skirt sends every bit of attention to the leg, so the leg has to carry the whole outfit." [0:47]; "What do people read first when there's a sentence on your chest? The sentence." [3:33].
- **Checks given plainly, never announced** (the only one of the three that does this throughout): "Hold yours up to the window before you buy it. If you can see your hand through it, it's too thin" [4:18]; "Set the bag on the floor. If it stands up on its own, it's structured." [7:52]; "Lay your hand flat on a white sheet of paper." [9:02].
- **Permission with the out:** "And if you love a shorter top, keep it with high-rise pants underneath so the two meet with nothing in between." [3:16]; "If you love trends, keep loving them. Buy the one and let it be the thing that makes the classic pieces look current." [12:20].
- **Over-70 lean and safety:** "It also lifts you off the ground on a sole that doesn't bend, and I'd rather you were steady." [10:45]; "have the cobbler stretch it rather than going up a size." [11:27].
- **The book CTA is right:** after item three's result, 81 words, true facts only: "my book, The French Way, has a secret on that. Refuse the trend inside your own foundation in the chapter five pieces that do the work of 50. There are 101 secrets, each with a how to do it and a skip if" [4:37]. Secret 11 is "Refuse the Trend Inside Your Own Foundation" in "Five Pieces That Do the Work of Fifty" (book index). Return line: "Now, the one so many women are wearing now." [5:01].
- **The ending:** one book line, then "Leave me a comment with the style rule you were handed at 50 and tell me whether you still follow it or broke it years ago." [14:15], the last words. That question is on the pack's list.
- **One personal detail, from the profile:** "My own rule is one in, one out." [12:35].

### Rule breaks

1. **A makeup item.** "Number seven, the eyes, the caterpillar false lashes and the hard black liner." [9:23], then "Brown mascara, top lashes only, and a soft brown or gray liner along the roots of the top lashes, smudged." [9:47]. 172 words, a whole numbered item. The pack covers hair and fashion, "Not makeup or skincare (a later pack)" (`style-scripts/SKILL.md`, description and "Inputs": "A whole-look title may keep one short face paragraph from the brief ... with no products and no results"). This item has products (mascara, liner, a cotton swab) and a result ("Your eyes look open"). *Fix:* a clothes or hair item in its place, or one sentence on a soft lash line inside another item.
2. **"Most" on a specific shoe (borderline).** "Ballet flats and loafers are the two you'll find most often on French women" [11:08]. The profile's French-way rule 1: "'Most' only for the broad habits ... a specific piece, shoe or color takes 'plenty of', 'many' or 'you'll often see'", written after "In France, most women wear ballet flats" went too far. This is softer than that line (it ranks shoes rather than counting women), but it's the same piece and the same word. *Fix:* "you'll often see ballet flats and loafers on French women".

### Readings, not rules

- **The tenth section.** After item nine, "Now, the other side." [12:58] runs 155 words: "The shapeless tunic, the elastic waist on everything, the giving up. That doesn't look older exactly. It looks like you stopped." [13:08], then a new list ("Neutrals with one accent ... One meaningful jewel ... A silk scarf. A modern haircut ... And a red lip"). Mostly new material, so not a recap, but it's a wind-down the count line didn't promise, and "It looks like you stopped" points at her rather than the garment. "The elastic waist on everything" may sting a 70+ viewer for whom elastic is comfort.
- **"After 50, I think that's a lot to ask of two knees."** [0:54]: the dry humor lands on her body, not the clothes (the profile: humor "aimed at the clothes, never at the woman").
- **Who the items are for.** The micro mini, the crop top, the backpack purse, the trucker cap and caterpillar lashes are mostly a younger woman's mistakes; the viewer is about 65-75 (pack, "The viewer"). The title (After 50) allows it.
- **The book match.** The CTA follows the white-shirt item but names Secret 11 (refusing trends). Secret 3, "Invest in the One Blouse That Replaces Ten", is the closer match for a white shirt; Secret 11 fits item nine.
- **"I"** at about 4.2 per 1,000 words, against the pack's guide of about 10 (reported, never a fail).

### Facts worth checking

None look wrong. All are general styling knowledge the pack allows (a hem at the ankle bone, a wide boat neck balancing the hip, the cobbler stretching leather). "A bag you can't see is a bag someone else can open. And in a crowd that happens faster than you think." [7:13] is a fear line with no number; fine as written (reading).

### Voice and caption oddities

- "with the step in the skip spelled out" [14:09]: surely "the step and the skip"; caption, not voice (worth a listen).
- "and old one goes to the donation bag" [12:35]: a dropped "an", probably caption.
- Otherwise clean. No French words were used at all.

### Numbers (caption-based, approximate)

14:24; 2,363 words; 164 words a minute; 13.7 minutes at 172 (meets 12); item one at 0:26 (word 73); one opening promise (the count line); book CTA at 4:32 (31% in, after item 3 of 9; 81 words), end book line 14:05, comment ask 14:15 (last); "you" and "your" 43.6 per 1,000 (all you-forms 47.8); "but" 5.9; "I" 4.2; 6 question marks; 7 French claim sentences, all hedged; item words 172 to 296 (item nine 410 with the close); 16.8% of sentences six words or fewer.

---

## 2. "7 Hair Colors That Make Women Over 60 Look INSTANTLY Younger (The French Way)" (`YCdL6Zbxfps`)

**In one line:** a warm, well-explained hair script that finally says "instantly" (none of the 14 old "instantly" titles did) and carries the dye safety line, but it adds a second count to the hook, announces its checks four times, runs the book CTA long, and two of its "seven colors" aren't colors.

### What works

- **The fear of the change named first, as the pack's hair note asks:** "If you've been putting off the color appointment because you're afraid of what a new shade will do to your face, I understand. The wrong color can add years in an afternoon." [0:00].
- **The title's words said, early and again:** "instantly" 4 times (first at about 0:26, scanner: "look instantly younger"), "younger" 3. The study found "instantly" in 14 of our old titles and said in none of those videos.
- **The blame moved off her, in fresh words:** "And you'll blame your face when the color is doing it. The shade changed that week and your face took the blame for it." [1:03].
- **The profile's changed-mind detail, used as designed:** "I used to think a deep chocolate was the elegant choice once the gray came and I changed my mind." [1:15].
- **The safety default, in proportion:** "If you color at home, do the patch test on the box every single time. And if your scalp itches or burns, stop and see a doctor." [1:57].
- **The salon as help, never the enemy,** with words to use in the chair: "Ask your colorist for the same family, brown, but two levels lighter than you'd pick on your own." [1:24]; "If your colorist reaches for the whole head of foils, say no, thank you, and say the sentence again." [3:08].
- **The heritage line doing a job:** "The way I was raised in Paris, gray was a color you decided on, and then you kept it the way you'd keep a good coat." [4:35] (gray worn on purpose is on the profile's documented ground).
- **Terms explained the first time:** a level [1:15], face-framing [2:53], violet shampoo [4:52], lowlights [6:43], demarcation line [7:16], toner [8:32].
- **Permission:** "If you've worn one solid shade for decades and you love it, keep it but have the roots softened with a few lowlights so the edge disappears." [7:22].
- **The book match is exact:** "The one called hair, skin, and the details no one talks about but everyone notices has a secret on choosing a hair color that lights your eyes." [3:39] (Secret 63 in that chapter); the Color Compass "five to seven colors" is the book's own figure. No "younger" in the CTA, as the book file requires.
- **The ending:** "Leave me a comment with the hair color you've worn the longest and whether it's the one you had at 40 or one you chose since." [12:37], last.

### Rule breaks

1. **A second promise in the hook.** "Here are seven hair colors that make a woman over 60 look instantly younger and three that do the opposite." [0:23]. The pack's opening: "Never in the hook: ... a second promise" and "Don't add moves" (M27, the model it follows, has one promise). The "three that do the opposite" are never counted out: the box black [0:53], the flat ash rinse ("One warning while we're on silver" [5:16]) and the cold platinum [8:54] sit inside other items with no numbers, so a viewer can't tell when the three have been paid. *Fix:* drop "and three that do the opposite", or make them a counted part.
2. **Checks announced, four times.** "Your check is a photo at the window in daylight with your hair down." [2:05]; "Then the check, which is the easiest one in this video." [3:14]; "Your check is the window again." [5:53]; "And your check is a photo from the side in daylight" [10:40]. The pack's item shape, step 5: "Give it plainly; never announce it ('Here's the check')", and the operator's fix 7 (HANDOFF §3, 2026-10-29: "checks given plainly, item endings varied"). The same "your check is" frame four times also makes the items end alike. *Fix:* "Take a photo at the window in daylight with your hair down."
3. **The book CTA runs 104 words** [3:33-4:09], against "about 60 to 90 words" (`style-scripts/SKILL.md`, "CTAs"). *Fix:* cut either the opening sentence ("Let me stop for a moment here because those face pieces are the first thing I'd send you to my book for.") or the Color Compass sentence.

### Readings, not rules

- **Two of the seven "colors" aren't colors.** "Color two, brightening pieces around the face only." [2:18] is a placement; "Color seven, and this is the rule under all the others. Two or three tones, never one." [10:47] is a rule. Colors four and six are both lowlights through going-gray hair. The title promises seven hair colors; five are paid as colors.
- **"Color four, blend the gray in."** [9:34], inside item six, sounds like a new signpost (probably "Color four blends the gray in"). Worth a listen.
- **The French way is thin here:** 6 French or Paris mentions (2.8 per 1,000 words, against a median of about 6.5 in her old scripts), two hedged claims ("In France, you'll often see women in their 60s and 70s in this kind of soft brown" [1:47]; "Plenty of French brunettes in their 60s go this way" [10:16]) and the heritage line. That is the honest result: the profile's documented ground for hair is "air-dried, low-fuss hair; gray worn on purpose and kept glossy", and the profile says not to invent where there is no documented practice. For a "(The French Way)" title it's light; the fix is a brief with more French material, not invented claims.
- **"Darker is the move almost every woman makes the week the gray shows up."** [0:40]: an unhedged claim about women (not French women, so outside the profile's rule).

### Facts worth checking (none checked against the brief, which isn't here)

- **"Iron in the water tints blonde orange, and a simple filter on the shower head takes most of it out."** [8:57]. Mineral water and brassy blonde is a common salon claim, but "takes most of it out" is a strong claim for a shower filter, and the pack bars "a health, scalp or dye-chemistry fact beyond the brief and the safety defaults". A break only if the brief didn't give it.
- **"Then a cool rinse at the end of every wash which closes the surface of the hair so it shines."** [11:53]. Widely repeated; the evidence for cold water "closing" the cuticle is thin (reading).
- **"a smoothing treatment if your hair is frizzy"** [11:46]: some salon smoothing treatments carry formaldehyde warnings; no safety line given (reading; the pack's safety defaults don't name it).
- **"It's about 40 minutes in the chair"** [2:53] and **"about 20 minutes in the chair"** [5:16]: plausible, but numbers the pack wants traced to the brief or marked general knowledge.
- Correct as said: violet opposite yellow, blue opposite orange [4:52], [8:32]; a level as one step from black to the palest blonde [1:15].

### Voice and caption oddities

- "five to seven colors you find ones from your undertone" [3:56]: "once"; caption.
- "The result is a cam one." [7:33]: probably "a calm one"; worth a listen.
- "the same way the ash rinsed did" [9:13]: "ash rinse did"; caption.
- "the light travels across it in a bend as you turn" [12:09]: probably "band".

### Numbers (caption-based, approximate)

12:47; 2,158 words; 169 words a minute; 12.5 minutes at 172 (meets 12, the closest of the three); item one at 0:31 (word 82); two opening promises (seven colors, and three that do the opposite); book CTA at 3:33 (28% in, after item 2 of 7; 104 words), end book line 12:29, comment ask 12:37 (last); "you" and "your" 46.3 per 1,000 (all you-forms 54.7); "but" 5.6; "I" 5.6; 6 question marks; item words 222 to 358; 20.6% of sentences six words or fewer.

---

## 3. "9 Things Elegant Women Over 60 Are NOT Wearing This Winter" (`aJlpJC2qB2w`)

**In one line:** a well-built winter list on an exact M29 hook, with the French lens carried all the way through although the title doesn't ask for it; it has the channel's second makeup item, three announced checks, and a closing run-down of the wardrobe before the book line.

### What works

- **The hook is a winning model's, applied** (see section 0), 70 words, item one at 0:25, with M29's permission move: "Some of these you'll keep anyway. That's fine. If you love it, I'll tell you how to wear it." [0:16], and the body pays it: "Can you still keep a perfer? Yes, for walking the dog and shoveling the step." [1:57]; "if you love the quilted jacket, wear it open over a long cardigan" [3:25]; "Keep the color if you love it, but choose it in a matte finish" [13:13].
- **Her climate, as the profile asks:** "I understand it. It's warm. It's light and in a lot of the US January is no joke." [0:32]; "And if your feet need the soft boot for warmth, keep it for the house and the car." [7:13].
- **Safety on falls, plainly:** "Now the steady part because I'd never put you on an icy sidewalk for the sake of a boot. Turn it over in the shop. You want a sole with real grip and a low wide heel" [6:44].
- **The blame moved off her:** "So much of this is simply where a hem falls, and that hem was decided by whoever cut the jacket, never by you." [3:36].
- **The heritage line and the scarf detail, once each:** "The way I was raised in Paris, a coat is bought once and then it's worn every cold day for years." [1:46]; "I have one knot I can tie in a doorway without a mirror, and that's the only one worth learning." [8:34].
- **The villains are habits, as allowed:** logos ("now it says you paid for an advertisement and then wore it" [4:27]), the advice she was handed ("Somewhere along the way, a lot of women were taught that matching is what put together looks like" [9:09]).
- **The book CTA:** after item two's result, 86 words, true facts: "It has 101 secrets, and everyone tells you how to do it and when to skip it, with a chapter on dressing for the climate you actually have. The system behind it is the capsule rule. Five to eight pieces chosen once that all work together." [3:53] (the climate chapter and the Capsule Rule's five to eight are in the book index).
- **The ending:** "Leave me a comment with your age and where you're watching from, so I know how cold a winter you're dressing" [15:20]: the question the study found gets the most answers, tied to the topic.

### The French angle without "French Way" in the title

The title has no "(The French Way)", but the script carries the lens all the way through: 11 French or Paris mentions (4.2 per 1,000 words; #1 5.9, #2 2.8), 8 claim sentences about French women, all hedged, plus the heritage line. For example: "So, what do plenty of French women reach for instead? A long wool coat." [1:08]; "What many French women wear instead is a sleek leather ankle boot" [6:20]; "Most French women you'd call elegant have a small wardrobe built on neutrals" [11:05] ("most" on a broad habit, as allowed); "Plenty of women in Paris wear the same coat from November to March" [14:52]. "American women" appears once, in the third person, as a habit ("Plenty of American women love these because they're soft and they're easy." [5:56]); the profile allows twice.

**Does it fit the persona?** Yes (reading). The profile makes the French lens Diane's, not the title's: "a chic, candid friend who shows women over 60 how French women get dressed, and how to borrow it with an American closet", and every swap here is on the profile's documented ground (the long wool coat, a structured bag without logos, dark leather boots, the silk or wool scarf, one accent, the small wardrobe on neutrals, the Breton, dark straight jeans, the near-bare face with a berry lip, short nails). It also follows rule 3 (the American climate caution). The script never says "the French way" outside the book's name, so it doesn't promise a series it isn't in. Whether a non-French title belongs on this channel is an ideation question, not a script one.

### Rule breaks

1. **A makeup item (the channel's second in three videos).** "Number eight, heavy full coverage makeup and the frosted lid." [12:05] ... "a tinted moisturizer instead of foundation. So skin looks like skin, mascara, groomed brows, and then one thing that is deliberate, a red or a berry lip." [12:38]. 211 words, a whole numbered item with products. The script knows it: "This is a clothes video, so I'll keep this one short, but it belongs on the list because the face finishes the coat." [12:09]. Same rule as #1's break 1 (`style-scripts/SKILL.md`, "Inputs": one short face paragraph, "no products and no results"). *Fix:* the berry lip as one sentence inside item six (it is already "the one accent"), and a winter clothes item (gloves, tights, a hat) as number eight.
2. **Checks announced, three times.** "Here's what to check before you buy." [1:22]; "The check is easy." [5:08]; "The check before you leave the house is to count one accent." [10:12]. Same rule as #2's break 2 (item shape step 5; HANDOFF §3, 2026-10-29, fix 7).
3. **A run-down before the book line.** "Everything on this list comes down to one habit. A small edited winter wardrobe worn all season without apology. One good coat, a few cashmere knits, a scarf, maybe two, the same dark boots, and the same plain bag everyday until spring." [14:36] (91 words in all). `core/retention-mechanics.md` §14: "No recap, no wind-down"; `core/greenlight-audit.md` B9 ("a run-down of what was just built counts"); the pack's "No recaps". *Fix:* end on item nine's result ("It also means your gloves go on and off without a thought."), then the book line.

### Readings, not rules

- **Repeats #1, published three days later on the same channel.** Both have the head-to-toe trend item (#3 [10:32], #1 [11:40]), long acrylic nails (#3 [13:18], #1 [8:13]), the structured bag without logos, the Breton and dark straight jeans, and near-identical lines: "Structured just means it holds its shape when it's empty" (#1 [7:13]) and "Structure just means it holds its own shape when you set it down" (#3 [4:42]); "File to follow the curve of your fingertip and one color" (#1 [8:46]) and "file to follow the shape of your fingertip in one color" (#3 [14:02]). The operator ruled repeated topics "not your problem" for the script library (HANDOFF §3, 2026-10-29); noted for the ideation side.
- **"Your neck is already shorter in winter because your shoulders come up against the cold."** [7:41] and **"Midhip is the widest point on most women."** [2:23]: stated as fact; fine as styling talk, unsourced.
- **"here's my rule. Wait a season."** [11:58]: "my rule" is allowed as opinion (pack, emotion rule 12), but next to the scarf detail it edges toward a second personal detail.

### Voice and caption oddities

- **"the coat is doing the perfect job in bed fabric"** [1:34]: garbled; probably "the puffer's job in better fabric". Worth a listen, since it's the item's key line.
- "Can you still keep a perfer?" [1:57]: "puffer"; caption.
- "Sheerling style" [5:46]: "shearling"; caption.
- "a silk square tied at the color of the coat" [7:57]: "collar"; and "The season's collar on the coat" [10:32] may be "color". Worth a listen.
- "the rest of the winters worked out the same way" [3:46] and "everyone tells you how to do it" [3:56]: "winter's" and "every one"; caption.
- **The captions end mid-sentence:** "so I know how cold a winter you're dressing" [15:26], with no "for". Either the voice dropped the word or the edit clipped the last second. Worth a listen.

### Numbers (caption-based, approximate)

15:28; 2,630 words; 170 words a minute; 15.3 minutes at 172 (meets 12); item one at 0:25 (word 70); one opening promise (the count line; the permission line is M29's move and is paid); book CTA at 3:46 (24% in, after item 2 of 9; 86 words), end book line 15:10, comment ask 15:20 (last); "you" and "your" 38.4 per 1,000 (all you-forms 45.6); "but" 5.3; "I" 6.8; 5 question marks; item words (by hand) 247 to 300, item two 383 with the CTA, item nine 361 with the close; 18.5% of sentences six words or fewer.

---

## 4. The channel

**Patterns (3 of 3 videos):**

- **Library-made, and the old packaging is gone:** no name, no channel intro, no sign-off, no subscribe ask, no prices, no house vocabulary, the book once mid-video plus one line, the last line a comment question about her, rotated. Every gap in finding 15 of `studies/style/comparison/README.md` (the self-introduction, the book twice, the fixed sign-off) is closed.
- **The slow start is fixed:** item one at 25 to 31 seconds (old median 71 s and 206 words; real winners 50 s). Finding 16.
- **The title's promise is said:** "instantly" 4 times in #2, "young" 9 in #1, "elegant" 11 in #3 (scanner). Finding 17.
- **The emotion gap is mostly closed:** "but" 5.3 to 5.9 per 1,000 (old 1.0; the pack asks about 5); 5 or 6 questions (pack 4-8); a feeling line and the blame moved off her in each. Finding 18.
- **Hedged French claims:** 17 of 17 claim sentences hedged (old 12%), one borderline. No "women I know in Paris".
- **"I" stays low:** 4.2, 5.6 and 6.8 per 1,000 against the pack's guide of about 10 (old 5.6). Reported, never a fail; the "I" that is there is all opinion.
- **The voice ran a little under the profile:** 164, 169 and 170 words a minute against 172. The 12-minute floor errs on the safe side; nothing broke.

**In 2 of 3 (below the pattern bar, worth watching):** a makeup item (#1, #3); checks announced (#2 four times, #3 three; #1 none).

**Against the previous review (2026-10-29, Werner and Frederick):** none of that review's failures repeat here. Lengths pass at the real voice speed, the hooks are short and modelled, there's one count line (except #2's extra), and no recap list at the very end (#3's run-down sits before the book line).

**Top 3 fixes for the next scripts:**

1. **Keep makeup out of the numbered items.** The pack is hair and fashion; a whole-look title may carry one short face line (a lip color, groomed brows), with no products, inside another item.
2. **Give the check plainly.** "Take a photo at the window" rather than "Your check is a photo at the window"; vary how items end.
3. **One promise in the hook, and end on the last item.** No second count ("and three that do the opposite"), no run-down of the wardrobe before the book line; and keep the book CTA inside 60-90 words.
