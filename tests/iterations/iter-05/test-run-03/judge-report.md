# TEST: judge report, electrical test run 03 (Frederick Barnes)

The script under judgement is `script.txt`, the script part of `output.md`. It runs 3,361 spoken words, about 17.2 minutes at 195 words a minute. The title is "The REAL Reason Your Plug Won't Stay In The Outlet", the brief is A12 (`../brief-A12.txt`) and the rotation log is "none".

Run 03 is the confirmation run on the final library:
- 31 models, all from 2022 on. E08 (the reference video) and E12 are gone; they sit in `studies/electrical/models-removed-2026-10-27/`.
- Run 01's fixes L1-L8 and run 02's fixes N1-N5 are applied (`CHANGELOG.md`, 2026-10-27, "Run 02 judged…").
- The writer modelled it on E11 and E09.

The reference is the same as in runs 01 and 02: Everyday Home Repairs, "Plug Won't Stay In Outlet" (`../refs/0h_r2bD5bMs-transcript.txt`, 11:13, 1,928 caption words). I judged it on 2026-10-27 against `../judge-rubric.md`, reading every "test-run-01/" in it as "test-run-03/". I changed no file except this one.

**How the counts were made** (the same method as runs 01 and 02, so the three runs compare):
- **Word counts** split on whitespace, the scanner's method. I get 3,361, the same as the scanner and the verifier.
- **Rates per 1,000 words** come from regex counts on the spoken text, CTA and comment included:
  - "you" counts you, your, yours, yourself and their contractions.
  - Fire words are fire, burn, melt and ignite in any form.
  - Death words are kill, die, death, deadly, fatal and electrocute in any form.
  - "I" counts I, I'd, I'm, I've, I'll, me and my.
  - Questions are sentences ending in "?".
- **Times** are word positions divided by 195.
- **"L12"** means line 12 of `script.txt`. Run 03 puts one sentence on each line.
- **Facts:** the scanner (`scanner-main-session.txt`) and verifier (`verify-output.txt`) counts are taken as fact. Both agree: 3,361 words, 7 items, SENTENCES 223, mean 15.1, 15.7% at six words or fewer, 25 over 25 words, longest 35, 0 fix-on-sight, 0 discrepancies in 36 quoted lines.
- **Copy check:** I compared every 6-word run in the script against the reference transcript, E08, E09, E11, the voice samples and the persona profile, and found none shared. The only runs shared with `SKILL.md` and `excerpts.md` are the allowed value-promise frame and the pack's required safety wording ("a tester that won't seat proves nothing", "so nobody flips it back on", "don't touch the panel").

**The count table:**

| Measure | Run 03 | Run 02 | Run 01 | Reference | Pack target |
|---|---|---|---|---|---|
| "you" per 1,000 | 42.2 (142) | 47.1 (159) | 35.9 (113) | 49.3 (95) | at least 35 (fix) |
| "but" per 1,000 | 5.4 (18) | 5.3 (18) | 5.4 (17) | 4.1 (8) | at least 5 |
| Questions | 7 (L4, L13, L32, L63, L142, L165, L233) | 8 | 7 | about 1 | 4 to 8 |
| "I/me/my" per 1,000 | 6.2 (21) | 6.2 (21) | 6.0 (19) | 23.3 | 6 to 12 |
| Fire words | 4 (1.2 per 1,000): "fires" L6 (the CPSC line), "melted" L78, L85, L147 | 5 (1.5) | 4 (1.3) | 0 | about 2 per 1,000 at most |
| Death words | 0 | 0 | 0 | 0 | at most 2 |
| Sentences | mean 15.1; 15.7% at 6 words or fewer; 25 over 25; longest 35 (L51) | mean 12.5; 20.0%; 7 over 25; longest 30 | mean 16.5; 8.4%; 22 over 25; longest 33 | no punctuation | at least 12% short; none over 35 |
| Steps with no short sentence | 0 | 0 | 3 | n/a | 0 |
| Highest step mean | 17.8 words (the opening); 16.2 (step six) | 14.2 | 20.6 | n/a | 18 at most |
| Money words | 0 | 0 | 0 | "about 50 cents", "about two dollars" | 0 |

**Per step** (word counts from the scanner; means, short sentences, questions and "but" counted by me):

| Step | Starts | Words | Mean words | Short | Questions | "but" |
|---|---|---|---|---|---|---|
| Opening | 0:00 | 142 | 17.8 | 2 | 1 | 1 |
| 1. Plug or outlet | 0:44 | 288 | 15.2 | 3 | 1 | 2 |
| 2. The hardest-working outlets (the real reason) | 2:12 | 460 | 15.3 | 3 | 1 | 3 |
| 3. Is it getting hot (the signs) | 4:34 | 489 | 13.6 | 9 | 1 | 3 |
| 4. Power off, prove it, look inside | 7:04 | 548 | 15.7 | 4 | 0 | 3 |
| 5. What's in the box (the stop signs) | 9:53 | 317 | 15.1 | 2 | 1 | 2 |
| 6. Buy the right outlet | 11:30 | 502 | 16.2 | 2 | 1 | 2 |
| 7. Re-check, swap, power back, the test | 14:05 | 615 + ending | 14.3 | 10 | 1 | 2 |

## 1. Verdict

**Run 03 is the best of the three runs, and every one of run 02's four blocking items is fixed.**
- **The re-check:** step seven now runs the full order before any hand goes near a wire (14:05):
  > "Plug-in tester in, and lit in both halves. Pen beeping on a working outlet. Breaker off and taped. The plug-in tester goes dark top and bottom, and still lights in an outlet you know works. Cover off, pen near the screws, outlet eased out by its strap, every wire tested. Pen back on that good outlet, still beeping. Only then do your hands go near the wires."
- **The plug-in tester** is seen lit in each half: "Push your plug-in tester into the top half of the worn outlet and watch it light up, then do the bottom half." It goes dark in both halves, then lights again on a working outlet.
- **The two-probe tester** gets its own live check: "it gets its own check on the working outlet before and after."
- **The new two-prong outlet** has a check: "If you put in a two-prong outlet, check it with the two-probe tester across the slots, which should show power, then plug in a lamp."
- **The heat overstatement is gone:** "Run your vacuum or a space heater off that outlet, and those few small spots heat up under the load."
- **The title comes home:** "That's the real reason your plug won't stay in." (3:09)
- **Facts:** every fact traces to the brief or the facts guide, with two wording slips (B3, W4).

It feels right for the operator's bar most of the way through:
- "It still works, so it's easy to shrug that off. But a worn spring does more than drop plugs. That loose fit is a warning."
- "The screwdriver's right there in your hand, but this order is what keeps you safe."
- "Let go of the cord. It stays."

**Would I upload run 03 as delivered? No, but it's three short line edits from upload, and only one of them is a library gap.**

| # | What blocks it | Kind | Fix |
|---|---|---|---|
| B1 | **No prove-dead path for a two-slot outlet, or for a worn half the tester won't seat in.** Step four tells every viewer to "Push your plug-in tester into the top half of the worn outlet". An older house with a two-slot outlet can't do that, and the script itself offers two-prong outlets (L181, L218). In a plastic box, that viewer is left with the pen alone, which the script itself says not to trust ("I wouldn't trust a quiet pen on its own anywhere."). The same gap hits a worn half the tester won't stay seated in: "a tester that won't seat proves nothing" (L106), but the script never says what to use instead. Run 02 covered the two-slot case half way; run 03 dropped it. | **Library gap (would recur).** `SKILL.md` Safety rule 1 says how to test a two-slot outlet, but nothing makes the line required, and neither the plan nor "Before handing over" asks for it. | Library: N7 below. Script, after L106: "If your outlet has only two slots, or a half won't hold the tester even when you press it, use the two-probe tester across the slots instead. Check it on a working outlet first. It should show power here now, and nothing once the breaker's off." |
| B2 | **"a GFCI will make the tester show an open ground" (L217, 16:13) is wrong as said.** The missing ground wire causes that reading, not the GFCI. "Open ground" is still never explained (runs 01, 02 and 03). | Wording: writer slip. The unexplained term: **library gap** (would recur). Safety rule 7 uses "open ground" itself, and the term isn't on the always-explain list. | "Where the box has no ground wire, the tester will show an open ground, the light pattern that means no ground wire is connected. That's expected there, so on a GFCI, the test button is your test." Library: N8. |
| B3 | **The GFCI is wired by "the same spot" (L197).** "Move the wires one at a time, so each one goes to the same spot on your new outlet that it had on the old one." That's right for a plain outlet. It's wrong when a plain outlet becomes a GFCI, where the incoming wires must go on the line screws (L174 says what line is, but step seven never uses it). | **Writer slip** (facts guide 6.10 and 14.22 were there). | After L197: "On a GFCI, the wires that bring the power in go on the screws marked line. If there's only one cable in your box, that's the only pair you use." |

**Is this channel's script skill ready to deploy?** Yes, once N7 (one sentence in Safety rule 1 plus one "Before handing over" line) and N8 (one term on the list) are in. I would not run a fourth full test for them. A spot check of step four on the next real script is enough, because everything else run 02 asked for landed.

The other findings (3c) are polish and don't block upload. Some of them have now recurred across runs, and I mark those:
- the open-box "I" lines, against Emotion rule 9 (runs 02 and 03);
- "electrician" three times in seven lines (runs 01, 02 and 03);
- three "I'd rather you" lines;
- longer sentences than run 02;
- the AFCI line half answered.

## 2. Score table

| Category | Run 03 | Reference | Why, in one line (run 03) |
|---|---|---|---|
| Opening (first 45 s) | **9** | 5 | The exact fix-video order: the problem and the answer in sentence one ("your outlet is usually worn out inside"), the wrong guess, the cause with "But", "Is that dangerous? It can be." with the CPSC line, the scope, and the value promise naming steps five and six. Step one at 0:44. Its sentences are long (17.8 mean; L8 is 30 words). |
| Keeping promises | **9** | 7 | The value promise is paid at 9:53 and 11:30; "step three covers exactly what to do" (1:53) at 6:01; "the one people skip" (6:59) at 7:04; "the part you came for" (14:00) at 16:37. The real reason is at 0:12 and named at 3:09. Only the AFCI rooms get "call the inspector" instead of "which outlet to buy". |
| Clarity on one listen | **7** | 6 | Worse than run 02: mean 15.1 (run 02: 12.5), 15.7% short (run 02: 20%), 25 sentences over 25 words (run 02: 7). Step six packs twelve buying rules into 502 words. Unclear: "open ground" (unexplained), "checking each pair", "the kind with two probes on wires", and "You'll want two testers" before a third arrives. |
| Number load | 9 | 6 | No figure in the opening. At most two real figures per step (step five: 1965 and the mid-1970s; step six: twenty-amp, six feet), every one traced. |
| Stakes (no money) | **9** | 4 | No money. Fire at 1.2 per 1,000, once in the opening (the CPSC line, allowed by the fix order) and once where it's real. The overstatement is fixed ("under the load"). Every fear line is answered within a line. A "space heater" is named twice (a Frederick tic; the brief names it once). |
| Safety | **8** | 4 | Step four and the step-seven re-check follow "The order at a device" line by line; rule 2 is complete, including the two-prong check; every stop sign leaves the breaker off. Missing: the two-slot or won't-seat case (B1); the GFCI line screws (B3); the open-ground wording (B2). |
| Voice and persona | 9 | 6 | Calm, warm and plain, with no stories, no tenure (allowed), no name and no tests claimed. "That alone is reason enough for me." "Now that's an outlet I'd trust." "I'd rather you" three times is a tic. |
| Written for the voice | 9 | n/a | Units in words, "A L" spaced, the letter sets explained, button labels in lower case, no "live". |
| CTA and ending | 9 | 3 | A 22-word subscribe line alone in the markers with no result promise; "Which outlet in your house drops plugs the most, and what usually gets plugged into it? Leave it in the comments, because I read every one." |
| Length and pacing | 8 | 6 | 17.2 minutes, in the sweet spot. Some padding: "electrician" three times in L85-91, three "I'd rather you", and a long plug branch in step one. Hands-on starts at 7:04 (run 02: 6:40). |
| Originality vs the models | 9 | n/a | No 6-word run shared with the reference, E08, E09, E11, the voice samples or the profile. At least five structural differences from E08 (below). |
| Emotion | 8 | 5 | Every floor is met, with 7 of 7 wins, 7 of 7 "but" turns, 7 questions and the title phrase back at 3:09. But steps four and six open on a procedure, "you" fell from 47.1 to 42.2, and the sentences got longer. |
| Audit honesty | 8 | n/a | 0 discrepancies in 36 quotes. "Rules (F): clean" again sits over open-box "I" lines (rule 9) and the missing two-slot case. "That loose fit is a warning." is listed as a title-word return. |
| **Total (of 130)** | **111** | | Run 02: 110; run 01: 101 |

## 3. Failures

### 3a. The rules, checked one by one

**Safety, line by line against `electrical-scripts/SKILL.md` "Safety" rule 1 ("The order at a device", "Any later re-check") and rule 2:**

| Rule | The script | Result |
|---|---|---|
| Power off and proven, inside the first step that needs it, before any cover plate comes off | Step four (7:04) L99 "Before you buy anything, turn the power off, prove it's off, and look inside the box." The plate comes off at L118, after the plug-in tester's dark check (L111) and the pen's live check (L114). | Met |
| The plug-in tester goes into the outlet you'll work on **before** the breaker goes off; it's seen lit in each half, then dark in each half; held in | L104 "Start with the power still on." L105 "Push your plug-in tester into the top half of the worn outlet and watch it light up, then do the bottom half." L106 "hold it in while you check the lights, because a tester that won't seat proves nothing." L111 "Back at the outlet, your plug-in tester should stay dark in both halves." | **Met** (run 02's W3 fixed) |
| Every tester the proof relies on gets the live check, before and after | Plug-in tester: lit at the worn outlet (L105), then L112 "plug it into a working outlet on another circuit and make sure it still lights." Pen: L114 "Hold it to that working outlet first and make sure it beeps." L126 "go back to the working outlet and make sure your pen still beeps." Two-probe: L125 "it gets its own check on the working outlet before and after." | **Met** (run 02's W2 two-probe half fixed). On one listen, the two-probe tester's live check is said after the instruction to use it. Better: "check it on the working outlet first, then on the wires, then on the working outlet again." |
| A two-slot outlet: no plug-in tester; the non-contact tester at each slot, then the two-probe tester across the slots, power on first, then off | Not in the script. Step four assumes three slots for every viewer (L105). The plan has no two-slot line either. | **Not met (B1).** Run 02 had it half done; run 03 dropped it. The same gap covers a worn half that won't hold the tester: L106 says it "proves nothing" and offers nothing else. |
| At the box: plate off; the tester on the terminals you can reach; screws out; device eased forward by the strap without touching the wires; then every wire and cable in view; only then hands | L118 "Take the cover plate off and hold the pen near the screws on each side of the outlet." L119 "Then take out the two mounting screws, ease the outlet forward by its metal strap, and keep your fingers off the wires." L120 "Hold the pen to every wire and every cable you can see now, not just the ones on the outlet." L121 the snapped tab, "test every wire on both sides". | **Met**, in exactly the rule's order |
| A non-contact tester's silence is never proof; a two-probe tester in a metal box or on armored cable | L122-124 "A quiet pen feels like the answer. But a pen can stay quiet next to a wire that still has power, especially inside a metal box. If your box is metal, or the cable has a metal jacket, use a two-probe tester on the wires instead, checking each pair." | Met (8.3, 8.4). "checking each pair" is vague on one listen. 8.4 gives the pairs as hot to neutral, hot to ground, neutral to ground: "black to white, black to bare, white to bare". |
| If any wire still shows power: stop, hands off, find the breaker, test again, else a call | L127 "If anything still shows power, take your hands away, track down which breaker powers it, then test once more." L128 "If you can't find it, that's where an electrician takes over." | Met |
| Tape over the breaker; labels can be wrong | L109 "the labels in a panel can be wrong, so let the tester decide." L110 "Put a piece of tape over that breaker and a note on the panel door". | Met (8.13, 8.14) |
| A plug-in tester is a check, never permission | L193-196 the plug-in tester is one check among several; "Only then do your hands go near the wires." | Met in practice. The rule's sentence (8.11) isn't said outright; run 02's "never permission to go back in the box" was clearer. Minor. |
| **Any later re-check** runs the same order, said briefly: tester live, plug-in tester dark in both halves, plate off, terminals, device out, every wire, tester live again | L189 "Back from the store, run the whole check again before you touch a wire." L190 "Plug-in tester in, and lit in both halves." L191 "Pen beeping on a working outlet." L192 "Breaker off and taped." L193 "The plug-in tester goes dark top and bottom, and still lights in an outlet you know works." L194 "Cover off, pen near the screws, outlet eased out by its strap, every wire tested." L195 "Pen back on that good outlet, still beeping." L196 "Only then do your hands go near the wires." | **Met** (run 02's W1 and N2 fixed). Two small additions would make it exact: "every wire tested, with the two-probe tester if your box is metal", and "without touching the wires" after "by its strap". |
| Power back on between visits | L151-152 "If it all looks clean, fold the outlet back in, screw it in, and put the plate on. Then take the tape off and turn that breaker on again so the rest of the circuit works, and leave that one outlet empty until your new one goes in." | Acceptable. It's a choice run 02 didn't make, and it's why step seven can start from "lit in both halves". Step seven's L190 serves as the check on that restore. |
| 2. How the power comes back, and the test after | L212 "Now take the tape off and flip the breaker on." L213 "You'll want to rush this last part, but the test after is what tells you it's right." L214 "check its lights against the pattern the label calls correct." L215-216 the GFCI's test and reset. L218 the two-prong outlet. L219 "If the tester shows anything you didn't expect, turn the breaker off again, prove it dead the same way, and check each wire against its screw." L220-223 the plug that kept falling out: "It stays." L224-226 the win. | **Met** (run 02's W4 and N4 fixed). L219 is a good addition. |
| 2. After a stop sign the breaker stays off | L148 "put the outlet back with the breaker still off, leave the tape on, and call a licensed electrician before that circuit comes back on." L85 and L86-88 (the emergency sequences). | Met |
| 3. The call-an-electrician line names its trigger, in order | L144-146 aluminum: "that's aluminum wiring. That's a stop… a licensed electrician's job." L147-148 the other signs. L175 "If your box has two or more cables and you can't tell which one brings the power in, that's where you stop and call an electrician." | Met. L175 has no "why" clause; L176's maker line partly gives it. |
| 6. Old wiring | L142-146 "Was your house built between 1965 and the mid-1970s?… dull silver rather than copper-colored, or the cable jacket is printed with the letters A L or the word aluminum… An ordinary outlet never goes on aluminum". L147 "insulation that's brittle, cracked or cloth-covered". | Met (7.5, 7.7, 7.9, 13.7) |
| 7. No ground: no plain three-prong; open ground expected; the GFCI's test button is the test | L180-182 the three choices from 4.15 and "it doesn't add a ground" (4.17). L217 "Where the box has no ground wire, a GFCI will make the tester show an open ground, and that's expected, so the test button is your test there." | **Partly (B2).** The choices and the test are right, but the cause is said wrong, and "open ground" is unexplained. |
| GFCI line and load in the swap | L173-176 line and load explained, the two-cable stop, the maker's sheet. L197 "Move the wires one at a time, so each one goes to the same spot on your new outlet that it had on the old one." | **Gap (B3).** "The same spot" doesn't hold when a plain outlet becomes a GFCI. |
| Emergency 12.13 (hot or discolored) | L85 "If the plate feels warm, or you see brown or melted marks, stop using that outlet now, unplug whatever's in it, and get a licensed electrician to look at it soon." | Complete |
| Emergency 12.14 (smell, crackle, buzz) and the panel (9.5) | L86 "unplug what's in it or quit using it." L87 "if you can safely get to your panel, the breaker box, switch off the breaker for that outlet". L88 "call a licensed electrician." L89-90 "And if that smell is coming from the panel itself, don't touch the panel. Just call." | Complete |
| What the visuals will draw | L51 "that metal still has power on it, right where a child's fingers can reach." L70 "Run your vacuum or a space heater off that outlet". | **Minor.** L51 invites a picture of a child's fingers at a blade that has power, and the pack says "A line that says a wire is still live has no hand, finger or tool in it". Fix: "and that metal still has power on it, at a child's height." L70 reads as an instruction to load a worn outlet. Fix: "When a vacuum runs off that outlet, those few small spots heat up under the load." |
| Emotion rule 9 / "How safety sounds": no "I" line while the box is open | Step four, with the outlet eased out: L129 "I wouldn't trust a quiet pen on its own anywhere." L130 "I'd rather you spend the extra minute here than anywhere else in this job." Step five, with the outlet out: L141 "Before I'd pick up a new outlet, I'd want to know all of it." Step seven, mid-wiring: L204 "I'd use the screws every time, even on a brand-new outlet that has the holes." L150 follows a stop sign and is allowed. | **Not met** (W1 in 3c). Rule 9 now says "never while the box is open" (N3). None of these lines is unsafe; they break the rule, and the audit says "Rules (F): clean". |
| Nothing removed from the brief's safety | Breaker off and verified with a tester, the same rating, GFCI where the spot now needs it, tamper-resistant where required, scorched wires or a melted box to an electrician, the exposed blade, no spreading the blades | Met |

**Fact check, line by line** (brief, and the facts-guide rows named):

| Line | Source | Result |
|---|---|---|
| L1 "your outlet is usually worn out inside"; L3 the brass spring that grips the blade | brief | Correct |
| L6 CPSC "loose-fitting plugs can cause overheating and fires" | brief; 4.28 | Correct, and named in full first |
| L11-15 the plug in another outlet first | brief | Correct |
| L17-18 bent or thin blades, cheap phone chargers | brief | Correct |
| L22 "a bent blade only touches the springs at a couple of points" | none | Unsourced mechanism (the brief's smaller-contact-area line applied to a bent blade). Low risk; the CPSC half of the sentence is 4.28. |
| L24 listed, "a lab such as UL has tested and certified it" | 14.48 | Correct |
| L25 a lamp or appliance with a bad plug: stop using it until repaired or the cord replaced | none | General knowledge, safe; not marked as such in the plan |
| L26 brown marks on the blades, or a warm plug: "step three covers exactly what to do" | brief (signs) | **Partly paid.** Step three's actions (L85) are for the outlet and plate, not a plug with brown blades. Fix: "…that's more than wear: stop using that plug, and step three covers the outlet." |
| L31-42 the hardest-working outlets; thousands of insertions; the yank; high-draw heat | brief | Correct |
| L43 "That's the real reason your plug won't stay in." | brief | Correct |
| L46-48 two-prong plugs first; the ground pin as a brace; "gives stray current a way back" | brief; 14.3 | Correct |
| L49 hotels, kitchens and bathrooms | brief | Correct |
| L51 the exposed blade | brief ("energized metal exposed to fingers") | Correct; see the visuals row above |
| L67-69 smaller contact, resistance, heat; the CPSC line | brief | Correct; "resistance" explained |
| L70 "heat up under the load" | brief ("heats under load") | **Correct** (run 02's W5 fixed) |
| L72-73 the softening loop; arcing explained | brief; 14.18 | Correct |
| L75-80 the six signs | brief | Correct ("A smell like hot plastic" for "burning smell") |
| L81-84 the first two mean worn springs, the last four mean heat | the brief's list, sorted by the writer | Reasonable. The flicker could also be a loose terminal, but step five's look inside catches that before any part is bought. |
| L85-90 emergency steps | 12.13, 12.14, 9.5 | Correct |
| L102-103 the plug-in tester "with three lights that shows whether an outlet is wired right"; the pen | 8.11, 14.46 | Correct |
| L108 "A breaker is the switch that shuts off one circuit, which is everything that one breaker feeds." | 14.9, 14.13 | Correct |
| L121 the snapped tab, two breakers | 4.27 | Correct |
| L123-125 pen silence; metal box; two-probe tester "reads the actual voltage" | 8.3, 8.4, 14.47 | Correct |
| L137 the ground wire, "the path that lets stray current trip the breaker" | 14.3 | Correct |
| L139 "what the trade calls backstabbing" | 14.27 | Correct; the term is explained |
| L142-146 aluminum, 1965 to the mid-1970s, A L | 7.5, 7.7, 7.9 | Correct |
| L147 brittle, cracked or cloth-covered insulation; scorched wires; a melted box | 13.7; brief | Correct |
| L159 "a little sideways T shape, it's a twenty-amp outlet, and your new one needs that T too"; L161 plain slots, the plain kind | 4.18; brief ("same rating") | Correct; avoids 4.18's disputed clause |
| L160 "An amp is just how much current is flowing." | 14.7 | Correct |
| L163-164 tamper-resistant, shutters; "in a home that's most places" | 4.1, 4.2, 4.14 | Correct |
| L165-169 GFCI places, within six feet of a sink; "the rule follows the replacement" | 4.5, 4.11 | Correct |
| L167 the GFCI explained | 14.19 | Correct |
| L170-171 protected further up the line; the sticker | 4.11, 6.13 | Correct |
| L173-174 "two pairs of screws"; line and load | 6.10, 14.22 | Correct |
| L176 "The maker's own sheet says to install one only if you understand basic wiring and can read a wiring diagram." | 13.6 (Leviton's GFCI sheet) | Close. 13.6 is one maker's sheet; "One maker's sheet" or "The instructions on many GFCIs" is exact. |
| L177-179 AFCI: "In bedrooms, living rooms and a lot of other rooms, newer code may also want AFCI protection… Your local inspector can tell you what applies in your house. I'd make that phone call before you buy." | 4.13, 6.15, 6.18, 14.20; guide "Code is local" | Correct and hedged right, but **half answered**: 4.13 gives what to buy (an AFCI outlet, or a dual-function outlet, 14.21), and the value promise was "which outlet to buy for your spot". |
| L180-182 no ground: the three choices; "it doesn't add a ground" | 4.15, 4.17 | Correct (all three of 4.15's options) |
| L183 weather-resistant outdoors, "built to stand up to outdoor damp and cold" | 4.3, 14.24 | Correct |
| L198-200 hot to brass, neutral to silver, ground to green; hot and neutral explained | 4.19, 14.1, 14.2 | Correct |
| L201-204 push-in holes loosen as the outlet heats and cools; the screw grips better | 3.7 | Correct |
| L205 "the strip gauge molded on the back of your outlet shows how much" | 3.1 | **Correct** (run 02's "gauge in a second sense" fixed) |
| L206 clockwise, three-quarters around | 3.2 | Correct |
| L207-208 one wire per screw; a pigtail with a listed connector | 3.4, 14.26 | Correct |
| L209 break the tab the same way | 4.27 | Correct |
| L210 "to the figure in the instructions if they give one" | 3.9 | Correct |
| L215-216 test: the tester goes dark; reset: it lights again | 6.5 (the same check with a tester for the lamp) | Correct |
| L217 "a GFCI will make the tester show an open ground" | 4.17, rule 7 | **Wrong as said (B2).** The missing ground causes the reading. |
| L218 the two-probe tester across the slots, then a lamp | rule 2 | Correct |

Apart from B2 and the unsourced L22 mechanism, nothing in the script is wrong as a fact.

**Emotion, against the pack's eleven rules:**

| Rule | Result | Evidence |
|---|---|---|
| 1. The viewer in the scene; each rung opens on a sense or a scene line (N5) | **Partly (5 of 7)** | Scene or sense openers: step one ("Before you blame your outlet, take that same plug to another outlet"), step two ("Find the outlets in your house that work the hardest… Which outlet does your vacuum always go into?"), step three ("Has the cover plate ever felt warm when you went to unplug something?"), step five ("Take a good look, without pulling on anything.") and step seven ("Back from the store…"). Procedure openers: step four ("Before you buy anything, turn the power off, prove it's off, and look inside the box.") and step six ("Buy a new outlet of the same rating, and make sure it's the kind your spot needs today."). |
| 2. One spine feeling (fix: nuisance, then relief) | Met | The nuisance: "drops out every time the cord gets bumped" (L1), "even if only one of them is bugging you today" (L57), "It still works, so it's easy to shrug that off" (L64). The relief: "It takes a firm push now. Let go of the cord. It stays." (L221-223) |
| 3. Strong, plain words; a short line in every step; 12% across | Met on the floors, weaker than run 02 | "worn out inside", "spread wide open", "the metal gets tired", "yanked out at an angle", "scorch", "feeds on itself", "Those are your suspects." 15.7% short and none missing, but a mean of 15.1 and 25 sentences over 25 words (run 02: 7). |
| 4. A "but" turn inside every step | Met (7 of 7) | L19 "It feels like an outlet problem, but it's the charger."; L45 "But notice which plugs fall out first"; L65 "But a worn spring does more than drop plugs."; L123 "But a pen can stay quiet…"; L149 "It's not the news you wanted, but you found it at the right time."; L169 "But the rule follows the replacement"; L202 "But those push-in holes hold the wire with a small spring". |
| 5. A question about every two steps; 4 to 8 | Met (7) | One in every step except four; the longest gap is L63 (4:41) to L142 (10:22), about 5.7 minutes, covering steps three to five. |
| 6. Sensory warning signs | Met | L75-80: droop, the flicker, the warm plate, "Brown or melted marks", "Crackling or buzzing.", "a smell like hot plastic". |
| 7. Every step ends on a win | **Met (7 of 7)** | L27 "you haven't opened a thing"; L58 "Now you've got a short list instead of a mystery."; L95 "you know exactly what your loose outlet has been telling you"; L131 "Now the box is dead, and you've proved it more than one way."; L153 "you haven't bought a thing yet"; L185 "the outlet you bring home fits your spot the first time"; L224-226 "You did that yourself, and you did it in the right order." |
| 8. The title's feeling and key word come back | **Met** (run 02's W9 fixed) | "won't stay in" L1; "the real reason your plug won't stay in" L43 (3:09); "getting your plug to stay put" L186; "It stays." L223. The hotel moment is still an explanation, not a lived scene (L49). |
| 9. "I" verdicts in most steps; one insistence line; none while the box is open | Partly | 7 of 7 steps have an "I" line; the insistence line is L115 "Please, don't skip that check, before and after." Four "I" lines sit inside open-box stretches (L129, L130, L141, L204). |
| 10. Capability straight after fear | Met | L51, then L52 "A new outlet grips your plug all the way in, so those blades stay covered."; L84, then L94 "But if all you found was a plug that droops… that's the job the rest of this video walks you through."; L148, then L149. |
| 11. Finish on relief | Met | L220-226 the plug holds, "Now that's an outlet I'd trust." |

**The chat** (`chat.md`): turn 1 lists the seven channels and turn 2 asks for exactly the title, the brief and the rotation log. The VA took the normal path, and the gate was tested in run 01, so no mistakes were tried this run.

**Originality: structure against E08** (the reference). The script differs in at least these ways:
1. It checks the plug before blaming the outlet (step one). E08 never does.
2. It finds the hardest-working outlets with a lamp-plug test (step two). E08 explains the wear only after the outlet is broken open.
3. It has a warning-signs step with the emergency sequences (step three). E08 has none.
4. It looks inside before shopping, with the stop signs (steps four and five). E08 confirms the rating only mid-install.
5. It buys by code and location (rating, tamper-resistant, GFCI, AFCI, no ground). E08 buys by price and "commercial grade".
6. It re-checks after the store.
7. It tests the GFCI and the two-prong outlet after power-up, and ends on a comment question.

### 3b. Library fixes (the rule is missing, unclear or wrong)

Run 02's N1-N5 are all in `SKILL.md`. Each one that the writer followed worked; see "Runs 01 -> 02 -> 03". Two narrow gaps remain, and both would recur.

**N7. The two-slot case (and a worn half that won't seat) is described but not required** (B1). File: `electrical-scripts/SKILL.md` "Safety" rule 1, "The order at a device", and "Before handing over".
- The rule says how to test a two-slot outlet, but not that an outlet script must say it. Run 02 covered it half way; run 03 dropped it, and the plan never raised it.
- Proposed, added to "The order at a device":
  > "Any script that opens an existing outlet says the two-slot case in one or two lines at the prove-dead step, and the same fallback for a half that won't hold the plug-in tester: the two-probe tester across the slots, checked on a working outlet first, showing power before the breaker goes off and none after, then checked again."
- Proposed, added to "Before handing over", safety line:
  > "the two-slot and won't-seat fallback said, in any outlet script"
- Optional scanner flag (judge): a script that says "plug-in tester" and never "two slots" or "two-slot".

**N8. "Open ground" isn't on the always-explain list** (B2; unexplained in runs 01, 02 and 03). File: `SKILL.md` "The viewer", the term list, and "Safety" rule 7.
- Rule 7 itself says "open ground is expected there", so the writer copies the term.
- Proposed: add "open ground" to the list.
- Proposed: add a row to facts guide §14:
  > "Open ground (on a plug-in tester): the light pattern that means no ground wire is connected at that outlet."
- Proposed, rule 7's line to read:
  > "the tester will show an open ground (no ground wire connected), which is expected there".

**Smaller, optional:**
- **N9. Make the open-box "I" rule checkable** (runs 02 and 03 both broke it; see W1). Have the evidence block's "I-verdicts" line mark any verdict between "plate off" and "breaker on" ("open-box: none"), so the audit can't call the rules clean over them.
  - Or, if the operator prefers, allow one short testing verdict inside the prove-dead sequence ("I wouldn't trust a quiet pen on its own"). Those lines reinforce safety rather than detour from it.
  - This is the operator's call; I'd take the first option.
- **N10. "Before handing over" could ask** that the buying step answers every rule it raises with what to buy (the AFCI line, W5), and that step seven names where a GFCI's incoming wires go whenever the script offers a GFCI (B3). B3 is a writer slip, but a GFCI swap will come up again in this niche.

### 3c. Writer slips (the rule was there)

**W1. "I" lines while the box is open** (rule: `SKILL.md` "Emotion" rule 9; "Safety", "How safety sounds"). Recurring: run 02's W7 was the same slip.
- The lines:
  - L129 "I wouldn't trust a quiet pen on its own anywhere."
  - L130 "I'd rather you spend the extra minute here than anywhere else in this job."
  - L141 "Before I'd pick up a new outlet, I'd want to know all of it."
  - L204 "I'd use the screws every time, even on a brand-new outlet that has the holes."
- Fixes:
  - Move L129-130 before the plate comes off, after L116: "I wouldn't trust a quiet pen on its own anywhere. I'd spend the extra minute here."
  - Cut L141.
  - Move L204 after the test: "A screw grips better, and I'd use one every time." can follow L224.

**W2. Restated points and tics** (rules: "Length", "Never pad"; "Voice", "A phrase is voice once"; `humanizer.md` H18).
- **"electrician" three times in seven lines:**
  - L85 "get a licensed electrician to look at it soon."
  - L88 "After that, call a licensed electrician."
  - L91 "that repair belongs to an electrician."
  - The first two are the required emergency sequences. L91 becomes "Heat damage like that can reach past the outlet into the wires and the box behind it." This was flagged in runs 01 and 02 too.
- **"I'd rather you" three times:**
  - L130 "I'd rather you spend the extra minute here"
  - L150 "I'd much rather you find that with the breaker off"
  - L172 "I'd rather you buy the GFCI outlet than guess."
  - Run 02 had two. Keep L150 and reword the others; L172 could be "In those spots, I'd buy the GFCI outlet and stop guessing."
- **"space heater" twice** (L41, L70). The brief names it once in its list, and it's Frederick's old tic (17 of his 23 scripts). In L70, use "a hair dryer".

**W3. Clarity on one listen** (rules: "Emotion" rule 3, "Short sentences mostly"; "The viewer", terms; core C2). The floors are met, but run 03 slid back from run 02. Fixes:
- **Split the longest sentences:**
  - L51 (35 words): "A plug hanging halfway out leaves bare metal showing. That metal still has power on it, at a child's height."
  - L177 (33 words)
  - L26 (32 words)
  - L121 (32 words)
- **Step six's load:** move the photo line (L184) to step five, where the box is open, and answer the AFCI line in one sentence (W5).
- **"You'll want two testers" (L101):** a third arrives at L124. Say "two testers, and for some boxes a third".
- **"That's the kind with two probes on wires that reads the actual voltage" (L125):** say "the kind with two metal probes on short leads, that reads the actual voltage."
- **"checking each pair" (L124):** say "black to white, black to bare, and white to bare."

**W4. The GFCI and open ground wording, and the GFCI line screws** (B2, B3; facts guide 4.17, 6.10, 14.22). See the verdict table for the lines and fixes.

**W5. The AFCI line is half answered** (rules: "Point then promise", every forward line paid; the value promise "which outlet to buy for your spot"; facts guide 4.13, 14.21). L177-179 sends the viewer to the inspector without saying what to buy. Fix, after L178: "If you need it, an AFCI outlet, or a dual-function one that does both jobs, goes in the same way." Or cut the AFCI line: the brief gives no AFCI rule, and run 02 judged fine without it.

**W6. Two of the seven rungs open on a procedure** (rule: "The rung shape in fix videos" item 1, N5). Fixes:
- Step four: "Your hand's on the screwdriver and the cover plate's right there. Before you buy anything, turn the power off, prove it's off, and look inside."
- Step six: "You're standing in the aisle with a wall of outlets in front of you. Buy one of the same rating…"

**W7. Small forward-line and scene slips:**
- **L26 promises that step three covers a plug with brown blades,** but step three covers the outlet. Fix: "…that's more than wear: stop using that plug, and step three covers the outlet."
- **The hotel moment is still an explanation** (L49). Run 02 asked for the moment; one line would do it: "the hotel outlet where your phone charger slid out every night".
- **"Run your vacuum or a space heater off that outlet" (L70)** reads as an instruction. Fix: "When a vacuum or a hair dryer runs off that outlet…"

**W8. The evidence overclaims** (rules: `core/greenlight-audit.md`, the evidence block).

| The evidence says | The script |
|---|---|
| "Rules (F): clean" | The open-box "I" lines (W1), the missing two-slot case (B1), the GFCI line screws (B3) and the open-ground wording (B2). |
| "I-verdicts: 7 of 7 items… none in: none" | True as counted, but four of them are open-box (W1). |
| Title word: "That loose fit is a warning." and "Heat softens the spring metal…" | Neither carries the title's key word. The real returns are L43, L186 and L223, and those are enough. |

`verify-output.txt` found 0 discrepancies in 36 quoted lines, and its re-counts (3,361 words, ITEMS, SENTENCES) match. The Numbers line is honest: it marks the small counts as general knowledge and names a row for every figure.

## 4. What the script does better than the reference

| What | Reference | Run 03 |
|---|---|---|
| The point | "hey guys how's it going it's scott with everyday home repairs and i want to talk a little bit about a very common problem…" | "If your plug won't stay in the outlet, or drops out every time the cord gets bumped, your outlet is usually worn out inside." |
| Plug or outlet | Never checks the plug | "Before you blame your outlet, take that same plug to another outlet, one that holds your other plugs just fine, and push it in… It feels like an outlet problem, but it's the charger." |
| The why | "from heat and just use over time it's really opened up and that is why it's not holding" | "After thousands of plugs going in and out, the metal gets tired. A cord yanked out at an angle bends the springs further than they were ever meant to go… That's the real reason your plug won't stay in." |
| Which outlets | "that's probably the outlet that is where the vacuum's being plugged in every day" | "Which outlet does your vacuum always go into? Then there's the one by your bathroom sink that takes the hair dryer every morning. Those are your suspects." Then the lamp-plug test: "Push it all the way in and let go. If it sags or slides out, that outlet's springs are done." |
| The stake | "this can obviously be a safety hazard because you start to expose a connected hot side piece of metal" | Heat first, sourced and explained ("CPSC puts it plainly: a loose connection can't carry much current without getting hot."), then the six signs with what each one means and the emergency steps, then "But if all you found was a plug that droops… that's the job the rest of this video walks you through." |
| Proving it dead | "i have two amber color lights on… now we can see that all lights are off" | Lit in each half, dark in each half, the tester checked on a working outlet, the pen live-dead-live, the terminals, the outlet eased out by its strap, every wire, the metal-box rule, and what to do if a wire still shows power. Then all of it again after the store. |
| The right part | Prices and "commercial grade" | Rating by the sideways T, tamper-resistant, GFCI by location and "the rule follows the replacement", the no-ground choices, weather-resistant, screws over push-in holes. No money. |
| Stop signs | none | Aluminum, brittle or cloth-covered insulation, scorched wires, a melted box, the two-cable GFCI: "put the outlet back with the breaker still off, leave the tape on, and call a licensed electrician before that circuit comes back on." |
| The finish | "we won't have any issues for years to come hopefully that helped you out" | "Then take that plug that kept falling out and push it in. It takes a firm push now. Let go of the cord. It stays." |

**Where the reference is still better:**
- **Its hotel moment is lived:** "you try to plug in your phone and the outlet just literally will not hold the plug at all". Run 03 still explains it ("the loose outlets you remember are in hotels…").
- **Its sentences are shorter in spirit.** Its talk is loose but light; run 03's middle (steps four and six) is heavier than run 02's.

## 5. The top five changes, ranked

1. **Add the two-slot and won't-seat fallback to step four (B1; library fix N7).** After L106: "If your outlet has only two slots, or a half won't hold the tester even when you press it, use the two-probe tester across the slots instead. Check it on a working outlet first. It should show power here now, and nothing once the breaker's off." Put the same clause in step seven's re-check.
2. **Fix the GFCI lines (B2, B3; library fix N8).**
   - L217: "the tester will show an open ground, the light pattern that means no ground wire is connected. That's expected there".
   - After L197: "On a GFCI, the wires that bring the power in go on the screws marked line. If there's only one cable in your box, that's the only pair you use."
3. **Take the "I" lines out of the open box (W1).** Move L129-130 before the plate comes off, cut L141, and move L204 after the win.
4. **Make it simpler again (W3, W2).**
   - Split L51, L177, L26 and L121.
   - Cut L91's third "electrician" and two of the three "I'd rather you".
   - Use a hair dryer instead of the second space heater.
   - Explain "each pair" and say "a third tester for some boxes".
5. **Close the loose ends (W5-W8).**
   - Answer the AFCI line with what to buy, or cut it.
   - Open steps four and six on a scene.
   - Fix L26's forward line.
   - Add the hotel moment.
   - Correct the evidence's "Rules (F): clean".

## Runs 01 -> 02 -> 03

### Scores side by side

| Category | Run 01 | Run 02 | Run 03 | Change 02 -> 03 |
|---|---|---|---|---|
| Opening (first 45 s) | 8 | 9 | 9 | 0 |
| Keeping promises | 8 | 9 | 9 | 0 |
| Clarity on one listen | 6 | 8 | 7 | -1 (mean 12.5 -> 15.1; over 25 words: 7 -> 25) |
| Number load | 9 | 9 | 9 | 0 |
| Stakes (no money) | 8 | 8 | 9 | +1 (the heat overstatement fixed) |
| Safety | 6 | 7 | 8 | +1 (the re-check, each half, the two-probe live check, the two-prong test) |
| Voice and persona | 8 | 9 | 9 | 0 |
| Written for the voice | 9 | 9 | 9 | 0 |
| CTA and ending | 9 | 9 | 9 | 0 |
| Length and pacing | 7 | 8 | 8 | 0 |
| Originality vs the models | 8 | 9 | 9 | 0 |
| Emotion | 7 | 8 | 8 | 0 (title phrase and scene openers up; "you" and short sentences down) |
| Audit honesty | 8 | 8 | 8 | 0 |
| **Total (of 130)** | **101** | **110** | **111** | **+1** |
| Verdict | FIX-THEN-PASS: the middle reads as a manual; three prove-dead gaps; the store before the look | FIX-THEN-PASS: four small line edits; one safety-order slip | FIX-THEN-PASS: three short line edits; one library gap (two-slot) | |

### Run 02's four blocking items

| # | Run 02 blocker | Run 03 | Evidence |
|---|---|---|---|
| 1 | The step-six re-check pulled the outlet before testing it | **Fixed** | L190-196: "Plug-in tester in, and lit in both halves… Breaker off and taped. The plug-in tester goes dark top and bottom… Cover off, pen near the screws, outlet eased out by its strap, every wire tested. Pen back on that good outlet, still beeping. Only then do your hands go near the wires." |
| 2 | The two-probe tester never checked live; no two-slot dark check | **Partly** | Two-probe: **fixed**, L125 "it gets its own check on the working outlet before and after." Two-slot: **not fixed**. The case is gone entirely (B1). |
| 3 | No check for a new two-prong outlet | **Fixed** | L218 "If you put in a two-prong outlet, check it with the two-probe tester across the slots, which should show power, then plug in a lamp." |
| 4 | "so it heats up when you've got something running" | **Fixed** | L70 "Run your vacuum or a space heater off that outlet, and those few small spots heat up under the load." |

### Run 02's library fixes N1-N5 (now in the library; did run 03 follow them?)

| Fix | Run 03 | Evidence |
|---|---|---|
| N1 Each half lit then dark; the two-slot order; the two-probe tester's own live check | **Partly** | Each half: L105 "watch it light up, then do the bottom half"; L111 "stay dark in both halves". Two-probe: L125. Two-slot: **not followed** (B1; library fix N7 makes it required). |
| N2 Any later re-check in the same order | **Fixed** | L189-196, quoted above. |
| N3 No "I" line while the box is open | **Not followed** | L129, L130, L141 and L204 (W1). The rule is now clear; the writer and the audit missed it (N9). |
| N4 The check for a new two-prong outlet | **Fixed** | L218. |
| N5 A fix rung opens on a sense or a scene line | **Partly (5 of 7)** | Steps two, three, five and seven open on the scene ("Which outlet does your vacuum always go into?", "Has the cover plate ever felt warm…", "Take a good look", "Back from the store"). Step four ("turn the power off, prove it's off") and step six ("Buy a new outlet of the same rating") still open on a procedure. |
| N6 "close" as a two-way word | Declined by the operator; moot | No "close" in run 03. |

### Run 02's writer slips W1-W11

| Slip | Run 03 | Evidence |
|---|---|---|
| W1 the re-check order | **Fixed** | L189-196. |
| W2 the two-slot case and the two-probe tester | **Partly** | The two-probe tester is fixed (L125); the two-slot case is dropped (B1). |
| W3 only one half seen lit | **Fixed** | L105. |
| W4 no check for a two-prong outlet | **Fixed** | L218. |
| W5 the heat overstatement | **Fixed** | L70 "heat up under the load". |
| W6 terms | **Partly** | "Strip gauge": **fixed**, L205 "the strip gauge molded on the back of your outlet shows how much". "The overheating" too early: **fixed**, since the opening now says "overheating and fires" (L6) before L22. "Open ground": **not fixed** (L217; library fix N8). |
| W7 the open-box "I" line | **Not fixed** | L204 "I'd use the screws every time…", the same slot as run 02's L149, plus L129, L130 and L141. |
| W8 restated points | **Partly** | The opening-and-step-one echo: **fixed**. The opening now asks "Is that dangerous?" and step one gives the plug test once. The electrician three times: **not fixed** (L85, L88, L91). "I'd rather you": **worse**, three times (L130, L150, L172). |
| W9 the title's phrase once | **Fixed** | L43 "That's the real reason your plug won't stay in."; L186 "getting your plug to stay put"; L223 "It stays." |
| W10 the near-echo "I'd do this one first" | **Fixed** (reworded) | L12 "I'd do this one before you open anything." |
| W11 the evidence overclaims | **Not fixed** | "Rules (F): clean" again, over W1 and B1 to B3. |

### Run 02's "where the reference is still better"

| Item | Run 03 |
|---|---|
| The hotel moment | **Not fixed**: L49 is still an explanation. |
| "you" at 49.3 | **Partly**: 42.2, down from run 02's 47.1 but above the floor of 35 and run 01's 35.9. |

### The trend in one line

Each run fixed what the last report asked for. The safety order is now right everywhere it appears, and the library rules caused no new failures; the one safety gap left (the two-slot case) is a rule the library describes but doesn't require. The only measure to slide is sentence length: the floor of 12% short sentences held, but the mean rose from 12.5 to 15.1. "Simpler" needs the floors held nearer run 02's level, not just met.
