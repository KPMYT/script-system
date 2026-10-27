# TEST: judge report, electrical test run 01 (Frederick Barnes)

The script under judgement is `script.txt`, the script part of `output.md`. It runs 3,152 spoken words, about 16.2 minutes at 195 words a minute. The title is "The REAL Reason Your Plug Won't Stay In The Outlet", the brief is A12 (`../brief-A12.txt`) and the rotation log is "none". I compare it with the reference video, Everyday Home Repairs, "Plug Won't Stay In Outlet" (`../refs/0h_r2bD5bMs-transcript.txt`, 11:13, 1,928 caption words). I judged it on 2026-10-27, against `../judge-rubric.md`, and changed no file except this one.

**How the counts were made:**
- Word counts split on whitespace, the scanner's method, so I get 3,152 like the scanner.
- Rates per 1,000 words come from regex counts on the spoken text, CTA and comment included.
  - "you" counts you, your, yours, yourself and their contractions.
  - "Fire words" are the pack's list: fire, burn, melt, ignite and their forms.
  - "I" counts I, I'd, I'm, I've, I'll, me and my.
  - Questions are sentences ending in "?".
- Sentence stats split on . ! ? and match the scanner's SENTENCES line: 191 sentences, 8.4% of them 6 words or fewer, 22 over 25 words.
- Times are word positions divided by 195.
- Line numbers ("L12") refer to `script.txt`.
- The scanner (`scanner-main-session.txt`) and verifier (`verify-output.txt`) counts are taken as fact.

**The count table:**

| Measure | Script | Reference | Pack target |
|---|---|---|---|
| "you" per 1,000 | 35.9 (113) | 49.3 (95) | at least 35 (fix videos; model median 43) |
| "but" per 1,000 | 5.4 (17) | 4.1 (8) | at least 5 |
| Questions to the viewer | 7 | about 1 ("what should you swap that out with") | 4 to 8 |
| "I/me/my" per 1,000 | 6.0 (19) | 23.3 (demonstrating) | 6 to 12 |
| Fire words | 4 (1.3 per 1,000): "fires" (CPSC line), "melted" twice, "burning" | 0 | about 2 per 1,000 at most |
| Death words | 0 | 0 | at most 2 |
| Sentences | mean 16.5; 8.4% at 6 words or fewer; 22 over 25; longest 33 | no punctuation (auto-captions) | none over 35 |
| Money words | 0 | "about 50 cents", "about two dollars" | 0 |

## 1. Verdict

**This is a safe, accurate and well-built script. It's far ahead of the reference on facts, safety and stakes, and it's up to the operator's bar for its first five minutes.**
- The point lands in sentence one: "If your plug won't stay in the outlet, the real reason is usually worn metal inside the outlet itself."
- The why is one plain chain: "Warm brass softens, so the grip gets weaker, so the contact gets smaller, so it runs hotter."
- Fire stays a stake, with 4 fire words and no death words.
- Every number traces to the brief or the facts guide, and nothing in the script is factually wrong.
- The CTA and the ending are exactly to the pack.

**It is not "simpler and stronger" through the middle.** From step three (6:32) to step six's end (14:24), half the video reads as a careful manual:
- Every step opens on a template line ("Step N is…"), never on what the viewer sees, hears or feels.
- Step six averages 20.6 words a sentence, with 7 sentences over 25 words.
- Steps two, five and seven have no sentence of 6 words or fewer.
- Steps four, six and seven ask no question.
- Steps three and four end on an instruction or a verdict, not a win.
- "you" sits just over the floor (35.9 against 35; the reference has 49.3).

**I would not upload it as delivered.** The prove-dead sequence, the step that matters most, has three logic gaps the audit called "clean":
1. The plug-in tester goes into the worn outlet only after the breaker is off. A dark tester in an outlet that "wants to drop" can mean a bad contact, not a dead circuit. The reference does this part right: it shows the tester lit, then dark.
2. "Every wire and every cable in that box" is tested before the outlet is eased forward and "the wires come into view" (L128 against L140).
3. The step never says how to prove a two-slot outlet dead, though step three treats the two-slot case. A three-prong plug-in tester won't go in one.

Separately, the store step comes before anyone has looked inside the box, so the part is bought before the viewer knows whether there's a ground wire or aluminum.

All of this is local to the script, so the verdict is **FIX-THEN-PASS**. Once the sequence is fixed and the middle is tightened, I'd upload it.

## 2. Score table

| Category | Script | Reference | Why, in one line |
|---|---|---|---|
| Opening (first 45 s) | 8 | 5 | Script: the cause in sentence one, the wrong guess, a question, a stake in proportion, the scope and one value promise; but the cause is said three ways in three sentences, and the first check lands at 0:53. Reference: greeting and name intro, the cause at about 1:00, the first step at 1:25. |
| Keeping promises | 8 | 7 | Every forward line is paid, and the title's reason comes at 0:00 and 2:02-3:00. The AFCI line raises a requirement and never says what to buy. |
| Clarity on one listen | 6 | 6 | Mean 16.5 words; 8.4% short; step six at 20.6; "First… Fourth" inside "Step three", then "Step four" 54 seconds later; "open ground" never explained. |
| Number load | 9 | 6 | No figure in the opening, at most two per step, every one traced. The reference has prices, "15 amp", "12 gauge", "6-32", "three quarters of an inch" and "one inch". |
| Stakes (no money) | 8 | 4 | No money; fire as a stake at 1.3 per 1,000; capability back within two lines. One overstatement ("heats up whenever you've got something running"). The reference has two prices and no fire stake at all. |
| Safety | 6 | 4 | The fullest sequence and every stop sign and emergency step, but the three prove-dead gaps above, plus "If you open it up" in the store step, before power-off. Reference: breaker, then the plug-in tester lit then dark in the same outlet; no wire test, no re-check, no stop signs. |
| Voice and persona | 8 | 6 (its own voice) | Calm, plain, warm; the tenure once, before a verdict; no stories, tests or name. "I'd rather you" three times; seven identical step openers. Reference: a greeting, a name intro and on-camera demos (his format). |
| Written for the voice | 9 | n/a | Units in words; "T R" and "A L" spaced; no brackets; "live" never used as an adjective. "where the trouble lives" and "where the hair dryer lives" carry a two-pronunciation word. |
| CTA and ending | 9 | 3 | One 20-word subscribe line alone in the markers; a specific comment question; "I read every one." Reference: link CTAs mid-video, a sign-off, no comment ask. |
| Length and pacing | 7 | 6 | 16.2 minutes, inside 15-22. Some restating: the cause three times in the opening, the electrician three times in nine lines of step two, "your hands" twice in step four. Hands-on work starts at 8:53. |
| Originality vs the models | 8 | n/a | Copy guard 0; at least five structural differences from E08; many facts E08 never uses. But it re-uses short runs of the pack's own example lines, which happen to be about this exact topic. |
| Emotion | 7 | 5 | Floors met ("you", "but", questions, "I"), with relief at the end and the title word three times. But the feeling sits in the opening, the why and step two; 0 of 7 steps open on the senses; 5 of 7 end on a win. |
| Audit honesty | 8 | n/a | `verify-output.txt`: 0 discrepancies, 48 quotes found. But "reframes 0" (I count 1), "Rules (F): clean" over the prove-dead gaps, and a 45-second claim for a check that starts at 0:53. |

## 3. Failures

### 3a. The rules, checked one by one

**Safety, line by line against `electrical-scripts/SKILL.md` "Safety" (the most important table in this report):**

| Rule | The script | Result |
|---|---|---|
| 1. Power off at the breaker, then prove it, inside the first step that needs it | L117 "Turn the power off, then prove it's off." L120 "Then switch off the breaker for the worn outlet." | Met |
| 1. …before any cover plate comes off | L124-126 (the plug-in tester, both halves) come before L127 "Then take the cover plate off." | Met |
| 1. Check the tester on an outlet you know is live | L119 "Hold your non-contact tester… up to an outlet you know is working, and make sure it lights up." | **Partly.** Only the non-contact tester is checked. The plug-in tester (L124) and the two-probe tester (L133, the deciding test in a metal box) never are. |
| 1. Test every wire in the box: both halves, every cable | L124-126 "top half… then the bottom half… Both halves matter, because some outlets are split". L128 "hold the tester to every wire and every cable in that box". | **Partly.** L128 comes while the outlet is still screwed in; the wires only "come into view" at L140 ("ease it forward a little so the wires come into view"), and nothing is tested after that. |
| 1. Check the tester on the live outlet again | L134 "Last, go back to that working outlet and check your tester one more time." | Met, for the non-contact tester only |
| 1. A non-contact tester's silence never proves dead; two-probe tester in a metal box | L131-133 "So its silence isn't proof on its own. If your box is metal, or the cable has a metal jacket, use a two-probe tester on the wires themselves" | Met |
| 1. A plug-in tester is a check, never permission | L124-125 "holding it in if it wants to drop. You want no lights on either one." | **Gap.** In a worn outlet, no lights can mean the tester isn't making contact. Seeing it lit before the breaker goes off is what makes a dark tester mean something; the reference does exactly that: "i have two amber color lights on that means the outlet is working… so now we can see that all lights are off". |
| 1. Two-slot outlets | Step three says "an outlet with only two slots and no round hole" (L106) is a case the viewer may have. | **Gap.** A three-prong plug-in tester can't go into a two-slot outlet, so on that outlet the proof rests on the non-contact tester alone, which L132 says isn't proof. |
| 1. Tape over the breaker; labels can be wrong | L123 "Put a piece of tape over that breaker and a note on the panel door". L121-122 "breaker labels can be wrong. I'd trust the tester over that label every time." | Met (8.13, 8.14) |
| 1. What if a wire still shows power | Nothing | **Missing.** No line says to stop and find the right breaker. |
| 2. How the power comes back, and the test after | L180 "Take the tape off the breaker and switch it back on." L181-186 the tester in both halves, then press test and reset. L187-188 if it reads wrong, breaker off, prove it dead, check against the picture, then the electrician. L190-191 the plug test. L192 the win. | Met. There's no named check for a new two-prong outlet, where the tester won't fit. |
| 2. After a stop sign the breaker stays off | L143 "leave that breaker off and taped, and call a licensed electrician". L81 "the breaker stays off until they've seen it." | Met |
| 3. The electrician line names its trigger, in order | L141 the signs, L142 "any one of those means stop", L143 who, L144 "Heat or age has already reached the wiring, and that's a repair past a new outlet." | Met |
| 6. Old wiring | L147-149 1965 to the mid-1970s, "dull silver", "the letters A L or the word aluminum", "An ordinary outlet never goes on aluminum wire". L141 cloth, brittle or cracked insulation. | Met (7.5, 7.7, 3.16, 13.7) |
| 7. No-ground GFCI: open ground expected; its test button is the test | L183 "your tester will show an open ground, and that's expected there". L184 "its own test button tells you the protection works". | Met |
| 8. Permits | L113 "check with your local building department before you buy." | Met (13.3) |
| Emergency, 12.13 (hot or discolored) | L75-76 "stop using it right now. Unplug whatever's in it, and get a licensed electrician out as soon as you can." | Complete (stricter: "warm or hot") |
| Emergency, 12.14 (smell, sparks, buzz) | L77-81: unplug or stop using it; "if it's safe to reach your panel… turn off the breaker"; "don't touch the panel at all"; electrician. | Complete |
| What the visuals will draw | L109 (step three, at the store, before power-off) "If you open it up and there is a bare or green ground wire in there after all". L66 "Go to your outlet while something's plugged in and running, and give it your full attention." | **Two slips.** The first is an open box before the verify-dead line. The second sends the viewer to a known-loose outlet under load to inspect it, next to a list that includes a warm plate. The pack allows noticing a warm plate "in everyday use… never a thing to touch on purpose". |
| How safety sounds: no aside while the box is open | L162-165, the backstab explanation and "You might figure the holes are fine…". L176 "If I had to pick the minute that matters most in this whole job…" (32 words, mid-swap). | Partly (see library fix L5) |
| Nothing removed from the brief's safety | Breaker off and verified, same rating, GFCI and tamper-resistant where required, scorched wires or melted box to an electrician, the exposed-blade shock, no spreading the blades | Met |

**Fact check.** Every factual line was checked against the brief and the facts guide rows on the Numbers line:

| Line | Source | Result |
|---|---|---|
| L1-2, L29-39: spring brass, two jobs, three causes | brief | Correct |
| L16 "thin blades a lot on cheap phone chargers" | brief | Correct |
| L21 "the CPSC, says bending the blades usually makes the overheating worse" | 4.28 | Correct. On one listen, "the overheating" hasn't been introduced yet; it arrives at 3:56. |
| L24 "a listing mark on it, like UL, which means a testing lab has checked it" | 14.48 | Correct |
| L43-46: two-prong plugs first, ground pin braces, hotel | brief | Correct |
| L53 "so it heats up whenever you've got something running" | brief: "the contact heats under load" | **Overstated.** A phone charger isn't "a load" in the brief's sense. The opening's own line is the accurate one: "when something's working hard". |
| L55 "Loose-fitting plugs can cause overheating and fires, and a loose connection can't carry much current without getting hot." | brief (CPSC); 3.8 | Exactly as the source gives it |
| L57-58: softening loop, arcing scorches the body | brief; 14.18 | Correct |
| L60 "those blades still have power on them" | brief | Correct; "live" avoided as the pack asks |
| L90-92: sideways T = twenty-amp, plain = fifteen-amp, same rating | 4.18, 4.22, brief | Correct; avoids 4.18's disputed clause |
| L94-96: shutters, "newer code has required them in homes for years" | 4.1, 4.14 | Correct |
| L97 "the letters T R printed on the face" | 14.23 gives only the abbreviation | True but **unsourced** (a marking, not a safety fact; low risk) |
| L99-104: GFCI places, protection upstream, the sticker | 4.5, 4.11, 6.13, 14.19 | Correct ("near a sink" is looser than "within six feet") |
| L106-109: no ground; two-prong or GFCI "No Equipment Ground"; three-prong if a ground is found | 4.15, 4.16, 4.17 | Correct (one of 4.15's three options left out, which is allowed) |
| L110-111: arc-fault "may" be required | 4.13, 6.15 | Correct, but 4.13's answer (an AFCI outlet, or downstream of one) is never given |
| L131-133: the non-contact tester's blind spots; two-probe tester | 8.3, 8.4, 14.47 | Correct |
| L147-149: aluminum | 7.5, 7.7, 3.16 | Correct |
| L155-157: hot, neutral and ground; screw colors | 4.19, 14.1-14.3 | Correct |
| L159-160: the brass tab | 4.27 | Correct |
| L162-167: push-in holes for fourteen-gauge solid only; strip gauge; clockwise hook | 3.6, 3.7, 3.1, 3.2 | Correct |
| L168-170: one wire per screw, pigtail, tighten as the instructions say | 3.4, 3.9 | Correct (no torque number, as the guide asks) |
| L171-173: line and load; "the maker's own advice is to have a qualified electrician do it" | 6.10, 13.6 | Correct (13.6 says "consult"; the script's version is slightly stronger, in the safe direction) |
| L194: test monthly, "the way the CPSC recommends", "they can fail without any sign" | 6.5, 6.7 | Correct |

Nothing in the script is wrong or unsafe as a fact. The safety problems are all in the order of the steps, above.

**Emotion, against the pack's eleven rules:**

| Rule | Result | Evidence |
|---|---|---|
| 1. The viewer in the scene; steps open on what they see, hear or feel | **Partly.** 1 of 7 steps opens on the senses (step two). | All seven open on a description of the step: "Step one takes about a minute…", "Step three happens at the store…", "Step four is the rule that protects everything else…", "Step five is a look before you loosen anything.", "Step six is the swap itself, and it's simpler than it looks.", "Step seven is the test, and it's the part you've been waiting for." Good scene lines exist but sit later: "so the lamp flickers every time someone bumps it" (L74). |
| 2. One spine feeling (fix: nuisance, then relief) | **Partly** | The nuisance is in the opening, L50 ("keep pushing the plug back in"), L84, L176 ("a tight grip is what you came here for") and L189-196. Steps three to five carry none of it. |
| 3. Strong, plain words; short sentences mostly | **Partly** | Strong: "tired", "spreads open", "yanked sideways", "goes slack", "scorch", "crackle", "brittle". Not short: 16 of 191 sentences run 6 words or fewer, and steps two, five and seven have none. L166 runs 33 words: "If the bare end of a wire is nicked or bent up, snip it clean and strip fresh insulation, to the length on the strip gauge molded on the back of the outlet." |
| 4. A "but" turn inside every step | **Mostly** (6 of 7 belief turns) | Turns: L17-20 (blades), L33, L95, L121, L142, L165, L189. Step two's only "but" (L84 "But if all you've got is a plug that droops…") is a contrast, not a belief turned. |
| 5. A question about every two steps | **Met, with a gap.** 7 in all. | They come at L4, 13, 28, 41, 67, 99 and 141. None in steps four, six or seven, so about 5:20 run from L141 (10:47) to the end. |
| 6. Sensory warning signs | **Met** | L70-74: the warm plate, "Brown marks around the slots", "A crackle or a buzz", "A smell like hot plastic", "the lamp flickers every time someone bumps it". |
| 7. Every step ends on a win | **5 of 7** | Wins: L26, L85, L151, L177 (a bridge), L196. Step three ends on "I'd rather you make one phone call than two trips to the store." Step four ends on "Only then do your hands go near the wires." (an instruction). |
| 8. The title's feeling and key word come back | **Met** | "the real reason" at L1, L40 ("That's the real reason your plug won't stay in.") and L193 ("That's the real reason, fixed where it started."); "won't hold" at L46 and L203. |
| 9. "I" verdicts in most steps; one insistence line | **Met** | 7 of 7 (the evidence block's list is accurate). Insistence: L136 "Please, test it every single time, even on an outlet you're sure about." |
| 10. Capability straight after fear | **Met** | L62-63 "I'm telling you because the fix is one part, it's a job you can learn"; L84-85; L151. |
| 11. Finish on relief | **Met** | L196 "And now that plug clicks in and holds, and you're the one who made it hold." (but see writer slip W3) |

**How the chat handled the VA's mistakes (`chat.md`): correct both times** (`core/workflow.md` §2):
- To "just write it, the brief is basically the title", it took the title, refused, and named the two missing inputs with one line each.
- To the brief without a rotation log, it asked only for the rotation log.
- It never asked for anything the files decide.

### 3b. Library fixes (the rule is missing, unclear or wrong)

**L1. The prove-dead sequence for a device swap.** File: `electrical-scripts/SKILL.md` "Safety" rule 1 (and `references/facts-guide.md` §8, which has no row on it).
- The rule says "check the tester on an outlet you know is live" without saying which tester when the script uses three. It says "test every wire in the box" without saying when the wires can actually be reached. It says nothing about a two-slot outlet or a wire that still shows power.
- The writer followed it to the letter and still produced L124 and L128 (quoted in 3a).
- Proposed wording, added after "Tape over the breaker…":
  > "Every tester the proof relies on gets the live check before and after, not only the first one. Where a plug-in tester is the first check, it goes into the outlet you'll work on **before** the breaker goes off, so the viewer sees it light and then sees it go dark; in a worn outlet, a tester that won't seat proves nothing. A two-slot outlet takes no plug-in tester: the two-probe tester goes in its slots. The order at the box: plate off; test the terminals you can reach; take out the mounting screws and ease the device forward by its strap; then test every wire and cable now in view; only then do hands go near the wires. If any wire still shows power, stop: switch the device back into the box, find the breaker that feeds it, and test again; if you can't, it's a call."

**L2. Opening the box before the part is bought.** File: `electrical-scripts/SKILL.md` "The rung shape in fix videos" (or "The step shape in how-to videos").
- Nothing says that what decides the part, if it can only be seen inside the box, is seen before the shopping step.
- The writer put "Step three happens at the store" ahead of power-off and the look inside, so the store step has to say "If you open it up and there is a bare or green ground wire in there after all" (L109), and step five's stop signs can land after the part is bought.
- Proposed:
  > "In a device swap, anything that decides which part to buy and can only be seen inside the box (a ground wire, aluminum, the wire count, a stop sign) is checked first: power off, prove it dead, ease the device out and look, put it back, then shop. Or the shopping step says plainly to buy after that look. The store step never describes opening the box."

**L3. The pack's example lines are about this exact topic.** Files: `electrical-scripts/SKILL.md`:
- "Emotion" rule 7 ("Now that plug clicks in and holds the way it did when the outlet was new.")
- "Point then promise" ("If you only check one thing tonight, check this.")
- "The title's promise, word by word" ("New contacts grip like new, and that grip is what holds a plug"; "If the plug's blades are bent or thin, it's the plug, not the wall.")
- "The opening" job 2 ("does the plug droop when you let go")
- "Emotion" rule 5 ("Does the plug sag the moment you let go?")

The script's L196, L11, L192, L15-16 and L4 track those lines' shape and wording, and no run reaches the 8-word copy guard. This is the woodworking Lazy Susan problem again (`CHANGELOG.md`, 2026-10-21: "Lazy Susan example lines replaced with other builds' shapes (the writer had copied them)"), and plumbing run 03's recommendation 6 (a 5-word guard on SKILL.md's quoted examples) was never applied. Proposed fix, in two parts:
- Move every outlet or plug example in SKILL.md onto a topic that isn't a locked title (the flicker, the tripping bathroom GFCI, the switch that glows).
- Add to "Using the models" and the scanner block: "the scanner flags any run of 5 or more words shared with a quoted example line in this file."

**L4. No floor on short sentences.** File: `electrical-scripts/SKILL.md` "Emotion" rule 3 and "Before handing over".
- "Short sentences mostly" has no number. The SENTENCES line reports 8.4% at 6 words or fewer, and nothing judges it.
- Plumbing run 03 was called "not simpler" at 4.8%. Here step six's sentences average 20.6 words, and three steps have no short sentence.
- Proposed:
  > "At least one sentence of six words or fewer in every step, item or block, and about 15% across the script; any step whose sentences average over 18 words is split."
- Have the scanner print the short-sentence count per item next to the item words.

**L5. "I" verdicts against "no aside while the box is open".** File: `electrical-scripts/SKILL.md` "Emotion" rule 9 against "Safety", "How safety sounds" ("No aside, opinion or detour while the viewer has a box or a panel open… the verdict comes after the win").
- Rule 9 asks for a verdict in most steps, and steps five and six happen with the box open. The writer met rule 9 with L145 and with L176 ("If I had to pick the minute that matters most in this whole job…", mid-swap).
- Proposed, added to rule 9:
  > "In steps done with the box open, the 'I' line is the stop-sign verdict or comes after the test, never mid-step."

**L6. The scanner's first-item limit is the list limit.** File: `electrical-scripts/SKILL.md` scanner block, `first-item-seconds: 30`.
- In a fix video the pack allows the first check by 30 to 45 seconds, so every fix script gets the false flag "<< later than 30 seconds".
- The scanner also measures to the "Step one" header (word 147), not to the first check, which here starts at word 173 (0:53, L12 "Take the plug that keeps falling out…").
- Proposed: a `first-check-seconds: 45` line for fix and how-to scripts, chosen by the plan's video type. The evidence block's Items line then quotes the first instruction's word position.

**L7. Ordinal lists inside a numbered step.** File: `electrical-scripts/SKILL.md` "Voice" or "The rung shape".
- Step three counts "First… Second… Third… Fourth" (L88-106), and "Step four" follows 54 seconds after "Fourth". On one listen these collide.
- Proposed:
  > "No ordinal sub-list inside a numbered step or item; name the parts instead ('the rating', 'the shutters', 'the wet spots', 'the box with no ground')."

**L8. "lives" can be read two ways.** File: `core/workflow.md` §4, "Words with two pronunciations", and the pack's "live" line in "Written for the voice".
- "where the trouble lives" (L26) and "where the hair dryer lives" (L42) can be voiced to rhyme with "knives".
- Proposed: add "lives" (the verb) to the two-pronunciation list, with the fix "is", "sits" or "stays".

**L9. Test hygiene, for the main session.** `brief-A12.txt` carries the line "REFERENCE (judge only): 'Plug Won't Stay In Outlet'… https://www.youtube.com/watch?v=0h_r2bD5bMs", and `chat.md` turn 4 says the VA pasted the brief "verbatim as in ../brief-A12.txt". If it was pasted as is, the writer saw the reference video's title and link. The effect is small, because E08 is the same video in the library, but the judge-only line should be stripped from what the operator pastes.

### 3c. Writer slips (the rule was there)

**W1. The store step talks about opening the box before power-off** (rule: SKILL.md "Safety", "What the visuals will draw": "the verify-dead line comes before any line that puts hands at wires").
- The line: L109 "If you open it up and there is a bare or green ground wire in there after all, a regular three-prong outlet connected to it is the right one."
- Fix: move it into step five ("If you see a bare or green wire in the box, a regular three-prong outlet connected to it is the right one"), or reorder as in L2.

**W2. Every step opens on a template, never on the viewer's scene** (rules: "Emotion" rule 1; "Voice", "rotate what opens an item").
- All seven step openers are "Step N is/takes/happens…" plus a description (quoted in 3a).
- Fix: keep the bare signpost and lead with the scene. For example: "Step four. Your hand's already on the cover plate screw, and that's the moment to stop." Or: "Step six. The old outlet's hanging out of the box on its wires."

**W3. The pack's example wording re-used** (rules: SKILL.md "Files in this skill": "The example lines in these rules show a shape; the script never reuses their wording"; "Point then promise": a priority flag "in fresh words each time").

| Script | Pack |
|---|---|
| L196 "And now that plug clicks in and holds, and you're the one who made it hold." | "Now that plug clicks in and holds the way it did when the outlet was new." |
| L11 "If you only check one thing before you buy anything, check this." | "If you only check one thing tonight, check this." |
| L192 "The springs in your new outlet are tight again, and that's what holds the plug" | "New contacts grip like new, and that grip is what holds a plug" |

- Fix: reword all three in fresh words. The tenure line (L22 "Thirty-five years in, I wouldn't bend a blade…") follows the pack's prescribed position and is fine.

**W4. Steps three and four don't end on a win** (rule: "Emotion" rule 7, "Never end on an instruction").
- Step three ends: "I'd rather you make one phone call than two trips to the store."
- Step four ends: "Only then do your hands go near the wires."
- Fix: end step four on what the viewer has now, for example "Now you know it's dead, not hoping it is."

**W5. Restated points** (rules: "Length", "Never pad. The same warning said twice, the promise restated…"; `humanizer.md` H18).
- The cause, three times in the first 15 seconds:
  - L1 "the real reason is usually worn metal inside the outlet itself"
  - L2 "once it spreads open, nothing holds the plug"
  - L3 "most of the time the tired part is in the wall"
- The electrician, three times in nine lines:
  - L76 "get a licensed electrician out as soon as you can"
  - L81 "that's a visit from a licensed electrician"
  - L83 "I'd treat a warm plate as a stop sign, and I'd make that call the same day."
- Hands: L128 "Before your hands go anywhere near the wires" and L137 "Only then do your hands go near the wires."
- One phrase three times: L22 "I'd rather you didn't either", L114 "I'd rather you make one phone call", L145 "I'd much rather you make that call".
- Fix: keep one of each.

**W6. Terms and order on one listen** (rules: "The viewer": "Any other trade word gets the same treatment"; core C2).
- "open ground" (L183) is never explained.
- "makes the overheating worse" (L21) comes at 1:33, more than two minutes before overheating is explained (L53, 3:56).
- "twenty-amp" (L90) is used two sentences before "An amp is…" (L92).
- Fix: explain "open ground" in a clause ("the light that says no ground wire is connected"); say "makes the heat worse" at L21; explain the amp at its first use.

**W7. The check sends the viewer to a worn outlet under load** (rule: "Ways to promise more value", a warm plate is noticed "in everyday use (a sign to act on, never a thing to touch on purpose…)"; checks must be "safe and that the brief or facts guide confirm").
- The line: L66 "Go to your outlet while something's plugged in and running, and give it your full attention."
- Fix: "Next time something's running in it, notice…", with no instruction to approach or touch a loose, loaded outlet.

**W8. Overstated heat** (rules: "Emotion", "Never… worst-case exaggeration"; the brief wins on facts).
- The line: L53 "so it heats up whenever you've got something running".
- The brief says "the contact heats under load". Fix: "so it heats up when something's pulling hard".

**W9. The AFCI requirement is raised and never answered** (rules: core B1, "Every question opened gets answered"; facts guide 4.13 has the answer).
- The line: L110 "newer code may also call for arc-fault protection when it's replaced."
- The viewer in a bedroom doesn't know what to buy. Fix: one line from 4.13 ("an arc-fault outlet does it, or ask the inspector what your town accepts"), or cut the AFCI lines.

**W10. Audit evidence that doesn't match the script** (rules: `core/greenlight-audit.md`, the evidence block; H21 "counted from the script itself").

| The evidence says | The script |
|---|---|
| "reframes 0" (Scanner and Turns lines) | One by hand: L62-63 "I'm not telling you this to scare you. I'm telling you because the fix is one part…". L189 "The lights look like the finish line, but the real test is…" is borderline. It's within H21's limit of 1, but the count is wrong. |
| "Rules (F): clean (power off and proven dead live-dead-live with every wire and both halves in step four…)" | The every-wire test comes before the wires are in view; only one of three testers gets the live check. |
| Items line: "the first check by 30 to 45 seconds" (implying it's met) | The first check starts at word 173, 0:53. |
| Verdict: "round 1 found 'you' at 34.8 per 1,000, under the fix-video floor of 35… fixed" | This can't be verified from the output. The pack says "a sentence never gets a 'you'… just to hit a number"; the main session may want round 1's diff. |

`verify-output.txt` found 0 discrepancies in the 48 quoted lines, and the counts it can check (3,152 words, the ITEMS and SENTENCES lines) match.

## 4. What the script does better than the reference

| What | Reference | Script |
|---|---|---|
| The point | "hey guys how's it going it's scott with everyday home repairs and i want to talk a little bit about a very common problem…" | "If your plug won't stay in the outlet, the real reason is usually worn metal inside the outlet itself." |
| Ruling out the plug | Uses a two-prong Apple charger as proof the outlet is worn, and never checks the plug. | "Take the plug that keeps falling out and try it in an outlet in another room. Does it hold tight there?" |
| The why | "from heat and just use over time it's really opened up and that is why it's not holding" | "Warm brass softens, so the grip gets weaker, so the contact gets smaller, so it runs hotter." |
| The stake, sourced | "this can obviously be a safety hazard because you start to expose a connected hot side piece of metal" | "Loose-fitting plugs can cause overheating and fires, and a loose connection can't carry much current without getting hot." (CPSC, as given), plus the exposed blade: "those blades still have power on them." |
| The myth | none | "But spreading the blades isn't a fix. The Consumer Product Safety Commission, the CPSC, says bending the blades usually makes the overheating worse." |
| Warning signs and stop signs | none | Step two's signs with the full 12.13 and 12.14 steps; step five's "brown, black or scorched… melted or warped… brittle, cracked or wrapped in old cloth", and aluminum. |
| Tester honesty | "most licensed electricians or at least some of them really don't like the non-contact" | "A non-contact tester can stay quiet on a wire that still has power, inside a metal box, on metal-armored cable, or with a weak battery. So its silence isn't proof on its own." |
| The right part | "this one would be about 50 cents… this is about two dollars i recommend this guy" | The rating by the slot shape, tamper-resistant, GFCI where required, the no-ground options, weather-resistant outdoors, the permit check. No money. |
| The finish | "now we have a nice secure hold and we won't have any issues for years to come" (a guarantee) and a sign-off | "You should feel it seat firmly, and when you let go of the cord, it stays put." Then the monthly GFCI test, the neighbouring outlets, and a specific comment question. |

**Where the reference is still better, and worth taking back:**
1. **The plug-in tester lit, then dark, in the same outlet:** "i have two amber color lights on… now i need to go hit the breaker… all lights are off". The script lost this (L1, W1).
2. **The frustration scene:** "if you've been at a hotel and you try to plug in your phone and the outlet just literally will not hold the plug at all". The script's version is an explanation at 3:31: "It's the same reason the outlets in a hotel room are so often the ones that won't hold your charger."
3. **"you" at 49.3 per 1,000** against the script's 35.9.

## 5. The top five changes, ranked

1. **Rebuild the prove-dead sequence (safety; library fix L1, then the script):**
   - The plug-in tester goes into the worn outlet before the breaker goes off (lit), then after (dark, held in).
   - A two-slot outlet gets the two-probe tester in its slots.
   - Every tester relied on is checked live before and after.
   - Plate off, ease the outlet out, then test every wire now in view.
   - If anything still shows power, stop and find the breaker.
2. **Look inside before shopping (library fix L2; writer slip W1).** Move the store step after power-off and the look (stop signs, ground wire, aluminum), or tell the viewer to buy after that look. Delete "If you open it up…" from the store.
3. **Make the middle feel it (library fix L4; writer slips W2, W4):**
   - Open each step on the viewer's scene after a bare "Step N.".
   - At least one short line per step.
   - Split step six's seven long sentences.
   - Add a question in step four or six.
   - End steps three and four on a win.
4. **Get the pack's plug-and-outlet examples out of SKILL.md and add a 5-word guard (library fix L3).** Then reword L11, L192 and L196 (W3). Do it before the next outlet title, or it will happen again.
5. **Cut the restatements and close the loose ends (W5 to W10):**
   - The cause once in the opening.
   - The electrician once in step two.
   - One "I'd rather you".
   - Explain "open ground".
   - Answer or drop the AFCI line.
   - "heats up when something's pulling hard".
   - Point the check at everyday use.
   - Correct the evidence ("reframes 1", the F line, 0:53).
