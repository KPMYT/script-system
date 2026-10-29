# TEST: judge report, iter-07 run 01

**Channel and title:** Scarlett Starling, "5 Necklaces That Make Women Over 60 Look EXPENSIVE (And 3 That Age You Instantly)"
**Judged:** `test-run-01/output.md` and `script.txt` (2,172 spoken words, about 12.9 minutes at 169), `chat.md`, `scanner-main-session.txt` and the `verify_output.py` findings (counts taken as facts), `brief-01.txt` (its REFERENCE line ignored).
**References (judge only):** our old script on the same title, `refs/w6w_ktMBHXM-ours-transcript.txt` (39,935 views, 75x; 4,079 words with the timestamps stripped, about 22 minutes), and the winner F01, `refs/2q_6Qf69Ywc-F01-transcript.txt` (Vivian Sinclair's glasses list, 910K; 2,849 words; faceless, judged for structure only).
**Rules:** `style-scripts/SKILL.md`, `style-scripts/references/hooks.md`, `style-scripts/references/voice-samples.md`, `personas/scarlett-starling.md`, `personas/books/scarlett-starling-book.md`, core `workflow.md` §1 and §4-5.

**Facts from the main session, as given:**
1. The scanner's one FIX ON SIGHT ("three hundred budget friendly ways to look expensive", copied from `scarlett-starling.md`) is the book's spoken title, which the profile requires in the CTA and has no `allow:` line for. It is a library gap, not a writer slip. The same goes for the "300" in NUMBERS NOT FOUND, which is the book title's number.
2. The `verify_output.py` "QUOTE NOT IN THE SCRIPT" ("Fine hair doesn't have to age you, but a few small habits make it feel like it does.") is the writer quoting M04's hook in its Hook evidence. It is a tool false positive, not an audit error.
3. The channel gate. The VA said "the rich lady one", then "Scarlett, the rich American one", and got the full list back both times. `core/workflow.md` §1 says: "Accept the number or the exact name. Anything else gets the list again." The chat followed the rule exactly. **Does it matter? A little.** It cost the VA two extra turns, and the third reply ("Please reply with just the number or the channel's exact name, written as it appears in the list.") reads a little stern to someone in a hurry. Nothing went wrong, and refusing "the rich lady one" is right: a description shouldn't be guessed. But "Scarlett" matches one channel out of eleven, and turning it away is friction with no safety gain. See library fix L3.

The rest of the gate is right. It asked for the three inputs, noticed the missing rotation log after the paste, asked for that alone, and wrote on "none, it's new".

---

## 1. Verdict

**Yes, this is up to the operator's bar, and I would upload it after one short fix round (FIX-THEN-PASS: about ten lines).**

The hook is short, clear and carried move for move from a real model: M29's question, feared look, count, permission, in 65 words, with item one at about 23 seconds. Our old script took about a minute and had a name intro and a tease. The body is "practical solutions to emotional problems" done properly:
- every item gives a length, a metal or a shape, the why (light, line, shadow, proportion), a check in her own mirror or photo, and a result in look words;
- four of eight items name a feeling in one plain sentence, before the fix;
- the blame moves off her once, in fresh words ("The beads did that.");
- all three "age you" items give a plain way to keep the piece.

It drops everything that hurt the old script: the intro, the tease, the prices, the house vocabulary, the long QR walkthrough, the twice-pitched book, the subscribe ask and the sign-off. It is clearly better than our old script.

What holds it back from the top marks:
- **The hook's second move is vague.** "Put the wrong necklace with it." The model names a concrete dated look; ours doesn't.
- **The feeling sits on the outfit, not on her.** "look less expensive, and older, than it really is".
- **The title's feeling fades in the body.** Items 1, 2, 6 and 7 never say "expensive", "age", "older" or "years".
- **The questions are mostly turn devices,** not questions about her own closet.
- **The template shows in places:** a check announced the same way in four items, and "I understand" twice.

None of these is a rule break that a viewer would complain about. They are the difference between good and the operator's "we need to do better".

## 2. Scores (1-10; the hook counts double)

| Category | New script | Our old script (w6w_ktMBHXM) | Winner (F01, structure only) | Why, in one line |
|---|---|---|---|---|
| **The hook (x2)** | 8 (16) | 4 (8) | 3 (6) | New: M29's four moves in order, 65 words (model 72), item one at about 23 s, "expensive" in sentence 1, permission plain; the feared look is generic and "older" lands on the outfit, not on her. Old: a strong concrete first line ("about an inch of skin at your collar bone"), then a name and channel intro, a tease ("We'll get to those.") and item one at about 1:00. F01: a strong feared-look line, but a recap, an intro, a subscribe ask and an invented career, with 475 words and 3:02 to item one. |
| Keeping the title's promise | 8 | 7 | 7 | New: five that look expensive and three that age you, each "age" item swapped and kept; TITLE WORDS expensive 7 (first at about 4 s), instant 2 (first at about 15 s); "age you" is said only twice and items 6-7 never name aging. Old: 5+3 paid, but in 22 minutes. F01: five shapes paid, plus the details section. |
| Clarity on one listen | 8 | 6 | 7 | New: mean sentence 14.4 words, terms explained (princess length, vermeil, undertone, lobster clasp, collar, costume jewelry); the hook question is knotty, and "said ver-may" is awkward. Old: long picture-led sentences ("it reads as gallery, as travel, as a woman who buys things..."). F01: clear mechanisms, but ornate and long. |
| Emotion | 7 | 5 | 6 | New: a feeling in 4 of 8 items, all before the fix; her mirror, her photo, her drawer; the why in every item; permission specific; one fresh reframe; the body named once ("a fuller bust or a softer middle"); "but" 5.5 per 1,000. Weak spots: the title's feeling fades, and 1 of 6 questions is about her. Old: "but" 0.5 per 1,000 and "for a lot of us". F01: a strong blame-move ("Aging is not the problem. The wrong frame is"), but client stories and a slogan close. |
| Voice and persona | 8 | 3 | 2 | New: "I" as opinion; the approved hall-mirror detail once; the credential line once; no name, no house vocabulary ("quietly" 0, "reads" 0). But both persona touches sit in item 5, and the credential line is clunky. Old: "I'm Scarlet Sterling", "any single piece of jewelry I own", "my own jewelry box included", "reads" throughout, "gallery", "on an ordinary Tuesday". F01: an invented 40-year career and named clients. |
| Claims and proof | 9 | 4 | 2 | New: no try-on, clients, "studies show" or pointing; the undertone tests are hedged as the brief asks ("Neither test is perfect, so take them as a hint and let your mirror decide."); the neck is a styling note only. Old: experience claims and prices from nowhere. F01: "40 years beside a fitting room mirror", Clarice, Ursula, a named optician. |
| Money | 10 | 3 | 9 | New: no price (the brief's $50-150 is left as background, as the pack says); "expensive" comes from metal, length, finish and one-at-a-time. Old: a whole price section ("40 to $120", "30 to 80", "150 to 400") plus consignment shops. F01: no prices. |
| Safety | 9 | 8 | 10 | New: no default applies; the comfort note on heavy beads is apt and short ("They're heavy to wear all day, too, and you feel it by the afternoon."). Old: a good weight caution for long chains. F01: the glasses default done well ("I am not an optician"; "Fit first, always"). |
| Written for the voice | 8 | 7 | 7 | New: inches in words, no symbols, no brackets in the script; the VO copy matches the script word for word (23 tags); "So does vermeil, said ver-may, ..." is a spoken pronunciation aside. The refs are auto-captions, so they are judged lightly. |
| CTA and ending | 9 | 2 | 2 | New: the mid CTA at word 612 of 2,172 (28%), after item two's result, 86 words, all six parts, a true fact ("every one of its Ways gives you the swap and the payoff") and the matched chapter (The Jewelry Rules); a one-line reminder; a comment ask about her, last; no subscribe or sign-off. Against it: "That one is next." is said and then held across the CTA. Old: "I gathered", a long QR walkthrough, "Whenever you get to it is fine", the book twice, "most of them free", subscribe, a which-one ask and a sign-off. F01: subscribe twice, "I read every one", a next-week tease and a sign-off. |
| Length and pacing | 8 | 4 | 5 | New: 12.9 min; items 178-318 words, all in band; nothing padded, but the check is announced by formula. Old: about 22 min, with "Picture" scenes, a price section and a two-rule summary. F01: about 3 min before item one, plus a recap at the end. |
| Originality vs the models | 8 | 6 | 5 | New: no lifted wording (the one copy-guard hit is the book title, fact 1); it differs from F02 and M29 in at least three ways (keepers first; 5+3 instead of 5+5; keep routes in every "age" item; an item shape with a check). Its opening question is a close frame of M29's ("What's the fastest way to ruin a good fall outfit?"): allowed by "format carried", but at the edge of "fresh words". Old: original, but house vocabulary shared across 38 scripts. F01: the faceless formula (recap, persona, slogan). |
| Audit honesty | 9 | n/a | n/a | The evidence matches the script and the tools. The only stretch is "I-verdicts: 8 of 8", which counts two empathy lines as verdicts (see 4, W9). |
| **Total** | **117 / 140** | **63 / 130 (68 / 140 scaled)** | **68 / 130 (73 / 140 scaled)** | The refs have no audit block, so they are scored out of 130 and scaled. The scores measure our rules. The winner's 910K came from its title, its thumbnail and its strong "why" lines, not from rule-keeping. |

**My counts** (`python3 -I`, the same word pattern as the scanner, which gives 2,172 for the script; the refs with timestamps and the TEST header stripped):

| Per 1,000 words | New script (2,172) | Our old script (4,079) | F01 (2,849) | Pack aim |
|---|---|---|---|---|
| "you" (the word, with you're/you'd/you'll/you've) | 20.7 (45) | 21.8 (89) | 21.8 (62) | "about 45" (the pack doesn't say whether "your" counts) |
| "you" + "your/yours/yourself" | 43.3 (94) | 33.8 (138) | 38.6 (110) | |
| "but" | 5.5 (12) | 0.5 (2) | 1.1 (3) | about 5 or more |
| "I" (with I'd/I'm/I'll/I've) | 6.0 (13) | 4.4 (18) | 9.8 (28) | about 10 (reported, never a fail) |
| questions | 2.8 (6) | 0.7 (3) | 2.5 (7) | 4 to 8 a script |

The auto-captions drop question marks, so the refs undercount.

- **Items naming a feeling: 4 of 8** (target about a quarter), each before the fix: 3 "Maybe pearls have always felt too formal for everyday, or like something you'd save for a wedding."; 5 "If a bold necklace makes you feel a little exposed, start with the single pendant."; 6 "Maybe you've looked at a photo of yourself wearing one and thought your face looked tired, and you couldn't say why."; 8 "It can feel like the safe, finished choice, and I understand why."
- **"but" by item:** 1, 1, 2, 1, 1, 2, 1, 3 (8 of 8 items).
- **Questions:** hook 1, item 1 1, the end of item 2 1, item 3 1, item 6 1, item 8 1. Only one is about her own things: "Do you have one of those tucked away in a drawer, still in its box?"
- **The title's feeling:** expensive 7 + instant 2 + "age you" 2 + "older" 1 + "adds years" 1 + "dated" 1 = about 14, or **about 6 per 1,000**. The pack's figures are 14 to 17 for real winners and about 8 for our old scripts.

## 3. The hook, side by side

**The model: M29**, "Wear THIS, Not THAT: 5 Outdated Fall Shoes to Ditch in 2026". A real presenter, never these / wear these instead (the right type), Usable: Yes. 72 words kept; item one at 0:36 (24 s once the omitted tease and intro are taken out).

| # | M29's move | M29 (from `hooks.md`) | Words | The new hook | Words |
|---|---|---|---|---|---|
| 1 | question to her | "What's the fastest way to ruin a good fall outfit?" | 10 | "What's the quickest way to make a good outfit look less expensive, and older, than it really is?" | 18 |
| 2 | feared look named | "Wear a shoe style that died 3 years ago." | 9 | "Put the wrong necklace with it." | 6 |
| 3 | count line | five styles, "starting with the flats sitting in your closet" | 25 | "So here are five necklaces that make women over 60 look expensive, and three that age you instantly, each with what to wear instead, starting with the simplest." | 28 |
| 4 | permission | keep what you like | 28 | "And if you love one on the second list, you can keep it." | 13 |
| 5 | item one | at 0:36 (24 s net) | | "Number one is a fine gold chain, ..." at word 65, about 23 s | |
| | **Total** | | **72** | | **65** |

**The new hook in full (65 words):**

> What's the quickest way to make a good outfit look less expensive, and older, than it really is?
> Put the wrong necklace with it.
> So here are five necklaces that make women over 60 look expensive, and three that age you instantly, each with what to wear instead, starting with the simplest.
> And if you love one on the second list, you can keep it.

**Against the rubric:**
- **The model, named and carried:** yes. The audit names M29 and its four moves, and ours keeps the same moves in the same order.
- **Length:** shorter than the model and well under 110 words; item one at about 23 s.
- **Clear:** one idea a sentence, no scene, no "Picture".
- **The title's promise word:** "expensive" is in sentence 1, and "instantly" in sentence 3.
- **Nothing banned:** no intro, slogan, tease, task or recap. The age is said only where the title says it.

**Where it falls short:**
- **Move 2 is generic.** M29's feared look is a concrete, recognisable thing ("a shoe style that died 3 years ago"). "The wrong necklace" names nothing she can picture in her own drawer, so the hook's emotional hit rests on the question alone.
- **The feeling lands on the outfit.** "look less expensive, and older, than it really is" says the outfit looks older. The pack's fashion note asks for "looking older ... than she feels", in her words. "Older ... than it really is" about clothing is also a slightly knotty phrase on one listen.
- **The count line's tail is weaker than the model's.** "starting with the simplest" loses M29's "in your closet" anchor, and "each with what to wear instead" sounds as if it covers all eight.
- **Very close to the model's frame.** Sentence 1 follows M29's frame almost exactly. The copy guard passes, and the operator asked for the format to be carried, but the next M29 hook should carry the move (a question about what spoils an outfit), not the sentence frame.

## 4. Failures

### Library fixes (a rule is missing, unclear or wrong)

| # | What happened (quoted) | Where | The fix |
|---|---|---|---|
| L1 | The scanner's FIX ON SIGHT: "three hundred budget friendly ways to look expensive" (8 words in a row), and "300" in NUMBERS NOT FOUND. The profile requires this spoken title in the CTA (fact 1). Both Scarlett writers hit it. | `personas/scarlett-starling.md`, the scanner block; the scanner's numbers check | Add `allow: Three Hundred Budget-Friendly Ways to Look Expensive` to the profile's scanner block (as Dale's and Hank's profiles do for their book lines), and check `diane-de-chambray.md` for the same gap. Have the numbers check accept a number that appears in the profile's `book:` line. |
| L2 | The `verify_output.py` "QUOTE NOT IN THE SCRIPT": "Fine hair doesn't have to age you, but a few small habits make it feel like it does." This is M04's line, quoted in the Hook evidence (fact 2). | `tools/verify_output.py`; `core/greenlight-audit.md`, the Hook line | Either skip quotes that follow "modelled on" or "graded against" a model ID, or (better) have the Hook line name a model's moves without quoting its wording. That also keeps model lines out of delivered output. |
| L3 | The gate turned down "Scarlett, the rich American one" twice in all (fact 3). | `core/workflow.md` §1 | Accept a reply that names exactly one channel unambiguously (any word of its name, case-insensitive, e.g. "Scarlett"), and say which one it took ("Scarlett Starling it is."). Keep sending the list back for descriptions ("the rich lady one") and for names that match more than one channel ("Roger"). If §1 is a locked decision, file this in `PROPOSALS.md`. |
| L4 | "you" is 20.7 per 1,000 as a word, but 43.3 counting "your". The pack's "'you' about 45 per 1,000 words" doesn't say which, so neither the writer nor the judge can check it. | `style-scripts/SKILL.md`, "Voice" and "Before handing over" | Define the count (I'd say "you" and "your" together, which is what makes ~45 reachable), and have the scanner print it. |
| L5 | The title's feeling fades: about 6 per 1,000 against the pack's 14 to 17. The scanner's title-words list doesn't include "age", so "age you", the title's own phrase, was never counted. The only check is "twice, once in the first minute". | `style-scripts/SKILL.md`, the scanner block's `title-words` line; Emotion rule 8 | Add `age you\|ages\|aging\|adds years` to `title-words`. Have the TITLE WORDS line also print a per-1,000 rate and flag a rate under about 8, as a report, not a fail. |
| L6 | The check is announced by formula: "Here's the check." (item 2), "The check is easy." (item 3), "Now the check." (item 4), "Here's an easy test." (item 6). | `style-scripts/SKILL.md`, "The item shape" step 5 | Add: "The check needs no announcement. Give it as an instruction, and rotate any lead-in; never the same lead-in twice." |
| L7 | "So does vermeil, said ver-may, which is a thick layer of gold over sterling silver." | `style-scripts/SKILL.md`, "Voice" (covers French words only) | Add a line for trade words with a non-English sound (vermeil, toque, cloche): name the term once with what it is, never a spoken pronunciation guide; a pronunciation hint, if needed, goes in the VO copy only. |

### Writer slips (the rule was there and wasn't followed)

| # | The line | The rule | The fix |
|---|---|---|---|
| W1 | "Put the wrong necklace with it." | `SKILL.md`, "The opening" 2 and 5 (carry the move: M29's move 2 names a concrete feared look) | Name it: "Hang the wrong necklace on it: too high, too heavy or too dark." (13 words; drop "starting with the simplest" to stay under 72.) |
| W2 | "What's the quickest way to make a good outfit look less expensive, and older, than it really is?" | `SKILL.md`, "The opening" 5 (the worry in her words; fashion: older than she feels) | "What's the quickest way to make a good outfit look less expensive, and make you look older?" (17 words; the promise word stays in sentence 1). |
| W3 | Items 6 and 7 never say the title's feeling. Item 6 ends on "your face looks brighter and more lifted"; item 7 on "You'll look taller through the neck and shoulders, and more at ease." | `SKILL.md`, "Emotion" 8 (say the title's feeling again every few items, in the title's words) | One plain line each, e.g. item 6 after "The beads did that.": "That shadow is what makes a necklace age you." Item 7: "That shorter neck is the reason a choker adds years so fast." Also one "expensive" in items 1 or 2. |
| W4 | Six questions, but five are turn devices ("Gold or silver, then?", "So what makes a strand good?", "So what goes there instead?"). Only one is about her: "Do you have one of those tucked away in a drawer, still in its box?" | `SKILL.md`, "Emotion" 7 (ask about her own hair, closet or mirror) | Turn two into questions about her: item 3, "Is there a strand of pearls in your drawer that only comes out for weddings?"; item 7, "Do you have a necklace that sits right up under your chin?" |
| W5 | "So which necklace sends the most light up onto your face? That one is next." followed at once by "One aside first, since we're talking about lengths." | `SKILL.md`, "CTAs" (at the end of an item's result) and "Point then promise" (bridges point at the very next thing) | Cut "That one is next." and carry the question in the return line: "Now, back to your neckline, and the necklace that sends the most light up onto your face." |
| W6 | In item 5: "Before I go out, I take one last look in the mirror by my front door, ..." and six lines later "After a lifetime of dressing well, my verdict on statement pieces is simple, and it's one at a time." | The profile, the credential line ("only where it does a job"); `SKILL.md`, "Voice" (plain over clever) | Keep the hall mirror in item 5. Move the credential line to item 3's verdict, where it does a job: "After a lifetime of dressing well, if I could hand you only one necklace from this whole list, it would be this one." |
| W7 | "I understand that." (item 3) and "It can feel like the safe, finished choice, and I understand why." (item 8), plus the four check lead-ins in L6. | `core/humanizer.md` (echo and formula); `SKILL.md`, "Voice" | Keep one "I understand". Drop the check lead-ins or vary them (see L6). |
| W8 | "And if you love one on the second list, you can keep it." This is paid in items 6-8, but "each with what to wear instead" in the count line sounds as if it covers all eight. | `SKILL.md`, "The opening" 6 (the count line: the whole list in one clean line) | "...and three that age you instantly, with what to wear instead." |
| W9 | The audit's "I-verdicts: 8 of 8" lists for item 6 "I can see why they're so popular, because they look bold and cheerful in the shop." and for item 8 "It can feel like the safe, finished choice, and I understand why." Both are empathy lines, not verdicts. | `core/greenlight-audit.md`, the evidence lines must match the script | Report "6 of 8 verdicts; items 6 and 8 carry empathy instead". Or add a plain opinion line to each, from what the brief already supports (e.g. item 6: "I'd keep anything dark and heavy well below the collarbone."). |

No hard-rule failures: no intro, tease, slogan, price, client, try-on, pointing, house vocabulary, subscribe ask or sign-off. The scanner's limits, echo, filler and reframe lines are all 0.

## 5. What the new script does better

**Than our old script (w6w_ktMBHXM):**
- **Item one in 23 seconds, not about 60, with no intro or tease.** The old script: "I'm Scarlet Sterling and this channel is for women over 60 ... We'll get to those." The new one: "Put the wrong necklace with it." Then the count, then item one.
- **Permission with a way to keep the piece, in every "age you" item.** "If you love your dark beads, you can keep them, but change how you wear them." / "If you love your choker, I'd move it down a couple of inches before I'd give it up." / "You don't have to get rid of the set." The old script had one ("If you can't part with the dark piece, at least stop wearing it on a dark top.").
- **A check in her own mirror in every item, in plain steps.** "Hold the strand up to the light and look at the gaps between the pearls. You should see a small knot in every one." / "Before you leave the house, count how many pieces you're wearing that came in the same box. If it's more than one, take one off."
- **The quality tells from the brief, explained,** where the old script had prices. "A good chain has some weight for its size. It closes with a lobster clasp, which is the little claw-shaped clasp you pinch open with your thumbnail."
- **A clean CTA.** It runs 86 words with the right chapter, against the old one's long walkthrough ("point the camera at that square the way you would at a grandchild"), "I gathered" and "Whenever you get to it is fine".
- **The ending asks about her and stops:** "Tell me your age and where you're watching from." The old ending: "tell me which of those three turned up in your drawer ... Until next time, stay polished and stay Sterling."
- **About ten times the "but" turns** (5.5 against 0.5 per 1,000), and no house vocabulary. The old script used "reads" 11 times, plus "gallery" and "on an ordinary Tuesday".

**Than the winner (F01):**
- **Item one at about 23 s, against 3:02.** No recap of past videos, no invented 40-year career, no named clients.
- **The blame moves off her in three words.** F01 takes a paragraph ("Aging is not the problem. The wrong frame is"); ours says "The beads did that."
- **The "age you" half pays a swap and a way to keep the piece every time.** F01's "What to avoid?" lines give no out for a woman who loves the piece.
- **No slogan close.** F01 ends: "this is where beauty does not expire, it evolves".

**What both references do that this script could borrow (structure, not wording):**
- **The old script's one concrete mechanism line in the hook.** "There's about an inch of skin at your collar bone that decides whether a necklace is flattering you or working against you." That is the kind of specific feared look W1 asks for.
- **F01's "who it suits" beat.** It names her body in most items (round face, silver hair). The new script names her body once ("a fuller bust or a softer middle"). A short neck or a softer jawline would fit items 3, 5 and 7.

## 6. The top five changes, ranked

1. **Sharpen the hook's middle (W1, W2).** Make the feared look concrete and put "older" on her: "What's the quickest way to make a good outfit look less expensive, and make you look older? Hang the wrong necklace on it: too high, too heavy or too dark." Drop "starting with the simplest". That makes about 67 words, still under M29's 72.
2. **Keep the title's feeling alive in the second list (W3, L5).** One plain line in each of items 6 and 7 in the title's own words ("age you", "adds years"), and one "expensive" in item 1 or 2. Add "age you" to the pack's `title-words`.
3. **Ask her about her own drawer and mirror (W4).** Turn two of the turn questions into questions about her pearls and her choker.
4. **Fix the CTA lead-in (W5).** Cut "That one is next." and carry the light question in the return line.
5. **Clean up item 5 and the formula lines (W6, W7, L6, L7).** Move the credential line to item 3's verdict, drop the check lead-ins and the second "I understand", and replace "said ver-may".

**Library fixes, in order:** L1 (an `allow:` line for the book title, and book-title numbers), L5 (add "age you" to title-words, plus a per-1,000 report), L3 (accept an unambiguous channel name and confirm it), L4 (define the "you" count), L2 (no model quotes in the Hook line, or have verify skip them), L6 (no check formula), L7 (no spoken pronunciation guides).
