# TEST: judge report, HVAC test run 02 (Roger the HVAC Guy, batch 1 #14)

**TEST material.** The script judged is `script.txt` (2,667 spoken words, about 17:47 at 150 words a minute), delivered in `output.md` with its audit block and VO copy. The title is "Furnace Keeps Shutting Off? The $12 Part Techs Charge $300 to Replace (Clean It Yourself)". The inputs were `brief-14.txt` (its REFERENCE line ignored) and the rotation log "none". The reference video is `refs/3Jonl_TLkpE-transcript.txt` (Word of Advice TV, "Furnace Not Working - The Most Common Fix", 1,558 caption words, 8:57). It is also model R28. The rules are the library at `/home/user/script-system`: `hvac-scripts/SKILL.md`, `references/price-guide.md`, `references/models/INDEX.md`, R27 and R28, `personas/roger-the-hvac-guy.md`, and the core files `workflow.md` §4-5, `greenlight-audit.md`, `claims-policy.md` and `humanizer.md`. Judged 2026-10-27. I wrote only this file.

**How I counted.** Word counts split on whitespace, as the scanner does. Rates per 1,000 words come from regex counts on the spoken text, with timestamps stripped from the reference. Times are estimates at 150 words a minute, because the profile has no measured rate. The scanner's counts (`scanner-main-session.txt`) are treated as facts: 0 in every fix-on-sight group, copy guard 0, numbers not in the fact source 0.

**The known input issue.** The brief the VA pasted carries two figures the price research has since corrected. It says the sensor costs "$10-$25" (now $10 to $30), and it says "$300 or more after hours" (the guide's flame-sensor row now reads "up to $300 at night or on a weekend"). Because the brief is the fact source, the writer is not marked down for using either figure. What the writer added on top of them is judged under W1.

---

## 1. Verdict

This is a clean, careful, safe script and it keeps the title's promise. The part is named in the first sentence. The money device (the shelf, a weekday visit, two in the morning in January) lands at about two minutes. The start-up is taught by sound, with every door on, and the clean is laid out step by step. The gas-leak line covers every step in price guide §9. The escalation ladder ends on named triggers for calling a tech, and the comment ask asks for the viewer's own quote. On safety, money and clarity it is far ahead of the reference.

**It is not yet at the operator's bar of "make the viewer feel it".** The voice is a patient teacher more than blunt Roger:
- "but" runs at 4.1 per 1,000 words.
- "I" opinions appear in 4 of the 13 sections.
- The cold house is one clause ("while the house gets colder").
- The hands-on clean doesn't start until about 7:10.

**It would not PASS the rules as written.** Four writer slips are fixable in place:
1. The replacement step doesn't restate the shutdown.
2. The condensate-trap line uses an experience test instead of a named trigger.
3. "Never bypass" covers the limit switch but not the pressure switch.
4. A door-switch claim is in neither the brief nor the guide and is wrong for most furnaces.

The night-price line also says "$300 or more is nothing unusual", which goes further than the brief does. The audit's "Rules (F): clean" misses all of this. Its originality evidence lists three "brief facts" that are not in the brief.

**FIX-THEN-PASS.** I would upload it once the four safety and fact fixes and the price line are done. The emotion work is what would take it from good to the operator's standard.

## 2. Scores

| Category | Script | Reference (3Jonl_TLkpE) | Why, in one line |
|---|---|---|---|
| Opening (first 45 s) | 8 | 4 | Script: point, breakdown line, villain, scope and escalation line all present, but it runs 187 words (about 1:14). Reference: a name intro and "Today I want to", and the part isn't named until 1:52, but its first step comes at 0:11. |
| Keeping promises | 9 | 7 | Script: the $12 part (as $10 to $25), the $300 and the clean are all paid, and the escalation line is paid at 13:18. Reference: keeps its own title, but has none of #14's money. |
| Clarity on one listen | 8 | 6 | Every listed term is explained. Small muddles: "four other things" holds five checks, and "just by listening" sits next to "a few seconds of blue flame". |
| Number load | 9 | 7 | 5 dollar figures (1.9 per 1,000), none in the opening, one per section except the device, each traced to a row. Reference: no prices, and "one in six calls ... guaranteed" is unsourced. |
| Money framing | 8 | 2 | The clock device is used well, the replacement quote is set against the part, and the title figure is paid with what was avoided. Docked for "nothing unusual". Reference: no money at all. |
| Safety | 8 | 3 | Power off and proved off, gas off, cooling, the restart and the check after, the igniter left alone, the gas leak complete, no limit-switch bypass, the trap refilled. Gaps W2-W5. Reference: power only, gas never off, runs the furnace with the door off, says "press down hard". |
| Voice and persona | 7 | n/a (5 as its own voice) | 45 years said once, doing a job; the filter detail once; no stories, tests, plumbing or catchphrases. But it's soft for Roger, with few hammered lines, and both disgust lines open "I think that's". |
| Written for the voice | 9 | n/a | "nine-one-one", "$10 to $25", "45 years"; no symbols, colons, dashes or capital runs; the scanner's mechanical count is 0. |
| CTA and ending | 9 | 3 | No mid-video CTA; a fresh one-line subscribe naming the channel; the comment ask has the turn, the ask, an own-numbers question and "I read every one", in that order. Reference: a pointer to his longer video and nothing else. |
| Length and pacing | 7 | 6 | 17.8 minutes; sections run 105 to 248 words. Some restating (W7) and a long run-up to the hands-on part. Reference: 8:57, under the 12-minute floor, with a 1:23 tangent. |
| Originality vs the models | 8 | n/a | Copy guard 0. The six differences the audit claims from R27 and R28 check out. The beats are still clearly R27's (normal start-up, the fault replayed, the lockout as protection, clean then replace) plus R28's sealed-box scope. That's a blend, which the pack encourages. |
| Emotion | 6 | 4 | "you" 21.0 per 1,000 (27.0 counting your, you're, you'll, you've, you'd); "but" 4.1; questions 2.6. The machine's sounds are excellent. The cold house and comfort felt in the body are thin, and "figure" is the belief-namer four times. Reference: "you" 25.7 (35.3 with the family), "but" 7.1 (4 of the 11 are "but anyways"), questions 0.6. |
| Audit honesty | 7 | n/a | The Numbers line, model differences, the hook comparisons (excerpts 1.2, 6.1, 3.1 exist as described), the VO tag check and the format check are all accurate. Wrong: originality signal 1's evidence and "Rules (F): clean" (W10). |

My counts of the checks the brief asked for:

| Check | Count or result |
|---|---|
| "you" per 1,000 words | 21.0 (56 of 2,667); 27.0 counting the "you" family (72) |
| "but" per 1,000 words | 4.1 (11). Sections with no turn of any kind: the money section and the normal start-up (the gas rule doesn't need one) |
| Questions per 1,000 words | 2.6 (7). Questions to the viewer about their own house: lines 50-51, 82, 141, 165. Line 63 is a check and line 143 is the line to say to the tech. Longest gap: line 82 (about 7:15) to line 141 (about 12:30) |
| Dollar figures | 5 (1.9 per 1,000): $10 to $25, $100 to $250, $300, $3,500 to $6,500, $150 to $400 |
| 45 years | Once, line 27, before the verdict "If you do just one thing before you call anybody, clean this rod." Allowed: it does a job |
| The personal detail | Once, line 157, in the profile's own facts: "On the first of the month, I pull my own furnace filter and look at it, with my coffee." 19 words, and it teaches ("the cheapest habit in this whole video") |
| Sentences | 178; mean 15.0 words; 11.8% are 6 words or fewer; longest 34 |
| VO copy | 25 tags (one per 107 words), all from the allowed list, never two in a row. Stripped of tags it matches `script.txt` word for word (checked with diff) |

### Safety defaults for this hands-on job (`SKILL.md`, Safety)

| Default | Present? | Line |
|---|---|---|
| 1. Power off and proved off; gas off for burner work; how it comes back on and the check after | **Yes** for the clean | "Then flip off the furnace's power switch." / "A non-contact voltage tester ... Touch it to the cable or cord running into the furnace. No beep, and the little light behind that window has gone dark? Then the power's off." / "That lever is off when it sits crosswise to the pipe." / "Turn the gas back on ... Then the power switch on, and the thermostat up a few degrees." / "Check that little light again". Cooling is from the brief: "give it a good while". |
| 1, again, for the replacement step | **Missing** | "It goes in exactly the way the old one came out." By this point the furnace is back together and running (W2). |
| 1, for the trap | **Missing** | "that's a job for the pros, unless you've cleaned one before." This leaves a hands-on job open with no shutdown (W3). |
| 2. Refrigerant is licensed work | n/a | Not mentioned. |
| 3. Never bypass a safety switch | **Partly** | "And never tape, jump or bypass a limit switch to keep a furnace running." The pressure switch is named three times as a cause but never covered (W4). |
| 4. Capacitors | n/a | Not mentioned. |
| 5. Refill the trap; nothing into the pressure-switch hoses | **Yes** | "furnace makers say to fill the trap with water after it's cleaned ..." / "And never pour anything into the little rubber hoses that run to the pressure switch." |
| 8. Red tag | n/a | Not mentioned. |
| The brief's own safety | **Yes, all of it** | The igniter: "Don't touch it, don't bump it, and keep your fingers off it. The oil from your skin can make it crack". Gas smell: see below. Coarse sandpaper: "Go light, and go fine." The ceramic: "Keep the grit off that white ceramic base". |
| The named call-a-tech triggers | **Yes, except the trap** | "If a clean filter goes in and it still trips, that's a call." / "If it still lights and dies after a clean, or it locks out again within a few days, call a tech you trust." / "If getting to it means opening a sealed box or pulling burners out ... call a tech you trust." |

### The gas-leak steps against price guide §9

| §9 step | In the script |
|---|---|
| Get everyone out now, on foot, and move well away | "Get everyone out of the house on foot, right now, and move well away." |
| Don't flip light switches, use your phone or the garage door opener, light anything, or start the car | "Don't flip a light switch, don't use your phone, don't touch the garage door opener, don't light anything, and don't start the car." |
| Once well away, call 911 and the gas company; don't assume someone else did | "Once you're well clear, call nine-one-one and the gas company, and don't assume somebody else already did." |
| Don't go back in until they say it's safe; don't look for the leak | "Don't go back in until they tell you it's safe, and don't go looking for the leak yourself." |
| Some people can't smell gas, and the smell can fade | "Some people can't smell gas at all, and the smell can fade." |
| Leave out "open the windows" and "shut it off at the meter" | Both left out. |

Every step is there and both leave-outs are respected. One point of order, not a failure: the five don'ts come before "get everyone out". On one listen, the action should lead. Leading with "Get everyone out of the house on foot, right now" and then the don'ts would match the guide's order.

---

## 3. Failures

### Writer slips (the rule was there and wasn't followed)

**W1. The night price goes further than the source.** "Call at two in the morning in January, and $300 or more is nothing unusual."
- **Rule:** `SKILL.md`, Money framing 2 (every price an estimate from the brief or the guide, said with "the top of it"); the framing limits in `research-and-sourcing.md` §2.
- **Judgement:** the "$300 or more" comes from the brief, so it is not a slip in itself. "Nothing unusual" is the writer's own addition: a claim about how often it happens, which the brief doesn't make.
- **Will viewers dispute it? Yes, likely, and from both sides.** The corrected research puts $300 as the top for a night or weekend call ("up to $300 at night or on a weekend"), and guide §2 says a clean is "about the price of a service call". The study found that techs answer price lines and their defences get the biggest likes (`SKILL.md`, The viewer: "we are not all out here" style replies, 1.6K). A tech who charges $150 to $200 to clean a sensor at night will call "$300 or more ... nothing unusual" inflated. Viewers who paid more will back it. The result is a split comment section on the video's headline number.
- **Fix:** "Call at two in the morning in January, and it can run up to about $300." This matches the title and the corrected row. Say the part as "about $10 to $30" once the corrected brief is in use.

**W2. The replacement step skips the shutdown.** "It goes in exactly the way the old one came out."
- **Rule:** `SKILL.md`, Safety default 1, and "Before handing over": "every hands-on step says the power is off and proved off".
- **Why it matters:** the furnace was put back together and test-run in the section before this one, so the viewer has to shut it down again.
- **Fix:** "Same shutdown as before: thermostat down, power off and checked, gas off, and let it cool. Then the new one goes in the way the old one came out."

**W3. The trap line uses an experience test and contradicts the brief.** "If the trap's full of gunk, or there's water where it shouldn't be, that's a job for the pros, unless you've cleaned one before."
- **Rules:** `SKILL.md`, Safety, "How safety sounds": the call-a-tech line names its trigger, never "if it's outside your comfort zone". "Unless you've cleaned one before" is that same test in other words. The brief says of these causes: "that's when to call a tech". The pack's Inputs rule says no method beyond the brief.
- **Why it matters:** it opens a hands-on job with no power-off line and no method.
- **Fix:** end the sentence at "that's a call for a tech you trust", and keep the refill fact as something the viewer can ask the tech about.

**W4. The pressure switch is missing from "never bypass".** The script names it as a cause three times ("the pressure switch won't close", "the pressure switch trips"), but the only bypass line is "never tape, jump or bypass a limit switch".
- **Rule:** `SKILL.md`, Safety default 3, which names the limit, pressure, rollout and float switches.
- **Fix:** "And never tape, jump or bypass a limit switch or a pressure switch to keep a furnace running."

**W5. A fact in neither the brief nor the guide, and wrong for most furnaces.** "Put the burner door back on and make sure it's seated all the way. Furnaces usually have a small door switch that keeps everything off while the door's open, so a door that isn't seated looks just like a dead furnace."
- **Why it's wrong:** on most upflow gas furnaces the door switch is pressed by the lower blower door, and the viewer never took that door off. The burner door usually has no switch.
- **Rules:** `SKILL.md`, Inputs: fill-ins must be "well-established, everyday HVAC knowledge"; claims-policy, nothing unsupported stated as fact.
- **It is also cited as evidence:** the audit lists "the door switch" as an originality fact.
- **Fix:** cut it, or say "If you took the lower door off too, seat it all the way: on many furnaces it holds down a safety switch, and the furnace won't start without it."

**W6. The opening runs long.** It is 187 words (about 1:14), against "the opening's six jobs run to about 45 seconds" (`SKILL.md`, The opening and the override row on the hook).
- Line 6 runs to 25 words and re-explains line 2: "The furnace is shutting its own gas off on purpose, because a coated rod can't feel the flame, so the furnace decides it never lit."
- Paragraph 2 then explains the same thing a third time.
- **Fix:** shorten line 6 to "It's shutting its own gas off on purpose, because a coated rod can't feel the flame." Cut the first paragraph of the cause section to its two new facts (the tiny current, and carbon or oxide building up season after season).

**W7. Restating.** The rule is `humanizer.md` H18 (the second mention must add something) and `SKILL.md`, Length ("Never pad").
- The safety-shutdown idea comes three times: "The furnace is shutting its own gas off on purpose" (line 6), then "it shuts the gas off to keep your house safe. The furnace is doing exactly what it should, just on bad information." (lines 18-19), then "But that lockout is the furnace looking after you." (line 48). The third adds the lockout; the second adds little.
- The replacement section says one thing twice: "The new one has to sit in the flame the same way the old one did. It goes in exactly the way the old one came out."
- "little" appears 9 times and "small" 6 times. That's a word tic, not an echo the scanner catches.
- **Fix:** cut lines 19 and 140, and vary or drop most of the "little"s.

**W8. Emotion below the pack's rules.** The rules are `SKILL.md`, Emotion 1, 4, 6, 11 and the Voice section; the persona profile's personality ("short hammered declaratives").
- **"But" turns:** 4.1 per 1,000 words. Plumbing run 03 reached 6.9 under the same rule. The money section and the normal start-up have no turn at all. (Rule 4: "Inside every item, at least one turn".)
- **Belief-namers:** "figure" is used four times ("A lot of folks figure", "You might figure", "they figure", "You'd figure"). The plumbing run 03 judge flagged the same tic.
- **"I" opinions:** in 4 of 13 sections (rule 11 says "most items"). The two disgust lines open the same way: "I think that's a hard number to swallow" and "I think that's far too much money".
- **The cold house:** it appears once, as a clause: "while the house gets colder". Comfort felt in the body (rule 6) never appears. "Warm air comes out of the vents" is said twice, but nobody in the house feels it.
- **Roger's register:** his short, hammered declaratives are rare. "Replace it." "Go light, and go fine." "It's telling you something." are nearly all of them.
- **Fix:**
  - Open the cause or money section on the cold scene the comments tell (the house at 60 by morning, the furnace clicking on and off down in the basement).
  - Add a "but" turn to the money section and the start-up section.
  - Rotate the belief-namers.
  - Give the clean and pipes sections a short "I" verdict each.
  - Close the reinstall section on comfort felt in the body.

**W9. Listening, then seeing.** "you can do that just by listening", then two sentences later "you get a few seconds of blue flame". With the doors on, most viewers can't see the flame.
- **Rule:** `SKILL.md`, Proof (checks "with what they'll see either way").
- **Fix:** "you hear the whoosh, a few seconds of burner roar, and then it goes quiet."

**W10. Audit honesty.** The rules are `greenlight-audit.md`'s evidence rule and E1, and the profile's CTA rules.
- **Originality evidence:** it gives signal 1 as "brief facts most videos skip = the trap's water seal, the door switch, the question to ask the tech". None of the three is in the brief. The seal is from price guide §9, the door switch is the writer's own (and wrong, W5), and the question to the tech is the writer's own. Signal 1 still passes on real brief facts the reference leaves out (skin oils crack the igniter, the four other causes, the prices), so 5/6 stands, but the evidence is wrong.
- **"Rules (F): clean"** is wrong while W2-W5 stand.
- **The Numbers line** leaves out "about ten minutes" (line 7).
- **The rotation log** doesn't record the subscribe line's opening words, which the profile asks for ("its opening words go in the rotation log"). See L5: the log has no field for it.

**W11. Minor.** "Same rod, same job, three very different prices." The shelf price isn't a job; try "Same rod, three very different bills." Separately, "very often the fix is a screwdriver, a kitchen scrub pad and about ten minutes" claims a frequency the brief doesn't give, and "about ten minutes" sits awkwardly beside "let the furnace cool ... give it a good while".

### Library fixes (a rule is missing, unclear or wrong)

**L1. A stale brief price beats the corrected guide.** `SKILL.md` (Inputs: "The brief is the fact source") and price-guide "How to use it" ("The brief comes first") let an old brief figure override a row the research has since corrected. That is exactly how "$10-$25" and "$300 or more" got in.
- **Proposal:** the gate or the scanner flags any brief price outside the guide's row for the same item, and the script uses the guide's row or says the price in words.
- **Process:** if "brief first" is a locked decision (`HANDOFF.md` §3), this goes to `PROPOSALS.md` with this run as the evidence. Either way, re-issue the corrected briefs to the VAs before the next run.

**L2. Safety default 1 doesn't say to test the tester.** A non-contact tester with a dead battery reads "off". Add to `SKILL.md` Safety default 1: "check the tester on a working outlet first". It is one of the commonest viewer corrections on hands-on electrical steps. "Let it cool" could also carry an everyday wait, or leave the time out and drop "about ten minutes" from openings.

**L3. The standard kit asks for prices the guide doesn't have.** `SKILL.md` (The standard kit) says a non-contact voltage tester and fine emery cloth get "their typical price range", but `price-guide.md` has no row for either. That forced "costs a lot less than a visit". Add rows to §5, or say that "in words" is fine when there's no row.

**L4. Two money devices are defined as the same thing.** In "Ways to promise more value", "the same part, two prices by the clock" is defined as three prices: the shelf, a weekday visit, and two in the morning in January. That is the same as "three prices side by side (the shelf, the weekday visit, the night visit)" in Money framing 4. The rotation can't tell them apart. This log says "money: the same part, two prices by the clock" for a script that says "three very different prices". Define them apart, for example "two by the clock" as the weekday visit against the night visit only.

**L5. No rotation-log field for the end CTA.** The persona profile says the subscribe line's opening words go in the rotation log, but the line format (`variety-rotation.md`, line 126, and the pack's added fields) has only `mid-CTA`. Add `end-CTA: "[first 6-10 words]"` to the pack's override row for the log.

**L6. The belief-namer tic keeps coming back.** "figure" appeared four times here and four times in plumbing run 03. Add a `once-regex` to the pack's scanner for the "you'd figure / folks figure / might figure" family (at most twice), and widen the list of rotations in Emotion 4.

**L7. Cosmetic.** `core/channels.md` numbers the channels 1-6 and 8, so the VA sees no 7 (chat turn 1). A VA who types "7" gets the list again, which is harmless, but it looks like a mistake. Either note the gap or renumber.

---

## 4. What the script does better than the reference

- **The part is named in the first breath.** "If your furnace keeps shutting off a few seconds after it lights, the part to look at first is the flame sensor." The reference starts with "Hey guys, Jay here" and names the sensor at 1:52.
- **The start-up is taught by sound, with the doors on.** "The fan, the click, the orange glow, the whoosh. And this time, the burners stay lit." The reference calls for heat with the door off.
- **The gas is turned off and the power is proved off.** "No beep, and the little light behind that window has gone dark? Then the power's off." / "That lever is off when it sits crosswise to the pipe." The reference only flips the power switch, never turns the gas off, and has no gas-leak line.
- **The method matches the brief.** "Give it a few gentle strokes all the way around, until it looks like clean metal. You're not after a mirror shine." The reference says "press down hard".
- **The igniter warning, which the reference doesn't have.** "The oil from your skin can make it crack the next time it heats up, and then a free fix just turned into a real repair."
- **Money, which the reference doesn't have at all.** "Same rod, same job, three very different prices." Also "A new standard furnace runs about $3,500 to $6,500 installed. I think that's far too much money to spend on a furnace that might only need its sensor cleaned."
- **A sentence to say to the tech.** "Did you clean the flame sensor, and did it still lock out after? An honest tech will have an answer, and he won't mind the question."
- **The honest limit, with a trigger and no sneer.** "If getting to it means opening a sealed box or pulling burners out, that's a good place to stop and call a tech you trust. There's no shame in that". The reference covers the same scope as a 1:23 aside about his own drill extensions.
- **The escalation ladder past the clean, with tellable differences.** "This one sounds different from a dirty sensor. The burners run a few minutes instead of a few seconds, then shut off while the blower keeps going". It ends on a line the viewer can act on: "If it still lights and dies after a clean, or it locks out again within a few days, call a tech you trust." The reference ends on a pointer to another video.
- **Relief, then a real comment ask.** "There's a good chance the heat stays on, and the house gets warm again." / "tell me what you were quoted the last time your furnace locked out, and whether it turned out to be that little rod. I read every one."

**Where the reference is still better:**
- It reaches the first step at 0:11; the script reaches the burner door at about 7:10.
- It gives the lockout reset: switch the power off for a few seconds.
- It says why the coating forms: dust pulled in for combustion settles on the rod.

Any of the three could go into the script in a line.

---

## 5. The top five changes, ranked

1. **Fix the four safety and fact slips.** Restate the shutdown before the replacement goes in (W2). Make the trap a named call for a tech (W3). Add the pressure switch to "never bypass" (W4). Cut or correct the door-switch claim (W5). Library: add "check the tester on a working outlet first" to Safety default 1 (L2).
2. **Make the viewer feel it (W8).** Put the viewer in the cold house in one or two concrete sentences. Add a "but" turn to the money and start-up sections, aiming for about 6 to 7 per 1,000 words. Rotate off "figure" (and add L6's scanner limit). Give more sections a short "I" verdict in Roger's hammered register. Close the reinstall section on warmth felt in the body, not only air at the vents.
3. **Settle the night price (W1, L1).** "it can run up to about $300", and "about $10 to $30" for the part. Re-issue the corrected briefs. Make the gate or scanner flag any brief price that conflicts with the guide row (or put it in `PROPOSALS.md` if "brief first" is locked).
4. **Tighten the front (W6, W7).** Bring the opening to about 45 seconds. Say the "it's protecting you" idea once in the cause section and once at the lockout. Cut the doubled replacement sentence and most of the "little"s. Consider R28's lockout-reset line as the payoff for a viewer who has already tried. That gets the hands-on clean to well before the seven-minute mark.
5. **Make the audit and the log honest (W10, L4, L5).** Originality evidence should list only brief facts. "Rules (F)" should report what is actually there. Add an `end-CTA` field to the rotation log and record "If straight answers like this". Define "two prices by the clock" apart from "three prices side by side" so the money rotation can work.
