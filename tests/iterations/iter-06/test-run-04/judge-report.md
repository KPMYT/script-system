# TEST: judge report, HVAC test run 04 (Roger the HVAC Guy, batch 1 #14, round 2)

**TEST material.** This report judges `script.txt`: 2,315 spoken words, about 15:26 at 150 words a minute. It was delivered in `output.md` with its audit block and VO copy.
- **Title:** "Furnace Keeps Shutting Off? The $12 Part Techs Charge $300 to Replace (Clean It Yourself)".
- **Inputs:** `../brief-14-v2.txt`, the corrected brief: part $10 to $30, "up to about $300 at night or on a weekend". Its REFERENCE line is ignored. Rotation log: "none".
- **The library:** the round-2 version, with the fixes in `../CHANGES.md`. The rules read were `hvac-scripts/SKILL.md` as it stands now, `references/price-guide.md`, models R27 and R28, `personas/roger-the-hvac-guy.md`, and the core files `workflow.md` §4-5, `greenlight-audit.md`, `claims-policy.md` and `humanizer.md`.
- **Reference video:** `../refs/3Jonl_TLkpE-transcript.txt` (Word of Advice TV, 1,558 caption words, 8:57; also model R28).
- **Round 1:** `../test-run-02/`, with its script and judge report.

Judged 2026-10-27. I wrote only this file.

**How I counted.** Words are split on whitespace, as the scanner does. Rates per 1,000 words come from regex counts on the spoken text. Times are estimates at 150 words a minute. Line numbers refer to `script.txt`. The scanner's counts (`scanner-main-session.txt`) are treated as facts: 0 in every fix-on-sight group, copy guard 0, numbers not in the fact source 0, 1 reframe, 8 shape-test flags (judged below).

---

## 1. Verdict

**This is a clear step up from round 1, and much closer to the operator's bar.** The emotion counts the fix aimed at have arrived:
- "but" rose from 4.1 to 7.3 per 1,000 words.
- The "you"/"your" family rose from 27.0 to 40.6 per 1,000, level with the plumbing script the operator passed (39.2).
- The belief-namer "figure" fell from four uses to one.

The feelings the pack names are now on the page:
- the dial that won't reach: "Just a thermostat that says 70 degrees and a house that never gets there."
- the clock: "it never says a word until the night it's finally thick enough, and that night is usually a cold one."
- the machine's sounds: "The hum. The click. The glow. The whoosh."
- relief: "you'll be warm again tonight, with the money still in your pocket."

Most of round 1's safety and fact failures are fixed:
- The tester is tried on a live outlet first.
- "Never bypass" now covers every safety switch.
- The trap is a named call, not a do-it-yourself job.
- The door-switch claim is gone.
- The night price matches the corrected brief.
- The gas-leak steps lead with "get everyone out".

**I would not upload it as delivered. It is FIX-THEN-PASS, and the fixes are about six lines.**
1. **The replacement step (line 110) is still not a clean shutdown.** It is one 55-word sentence, the longest in the script, and it sits at a safety step. It leaves out the cool-down and the thermostat, which the furnace needs because it has just run a test cycle. It ends on the comfort-zone test the pack bans: "if that's one step further than you want to go".
2. **One line is said as fact that nothing supports, and it leans on the trade's honesty:** "The invoice will say something like flame sensor service. It won't say scrub pad, and it won't say how short the job really was."
3. **Roger's own voice is thinner than in round 1.** An "I" opinion or verdict appears in 2 of 11 content sections (round 1: 4 of 13). After 9:45 the script asks the viewer nothing about their own furnace.

The audit's "Rules (F): clean" is wrong again, though on fewer findings than in round 1.

## 2. Scores

| Category | Run 04 | Run 02 (round 1) | Reference (3Jonl_TLkpE) | Why (run 04) |
|---|---|---|---|---|
| Opening (first 45 s) | 8 | 8 | 4 | The point in sentence one ("check the flame sensor first"); a yes-or-no question answered in the next line; one dollar figure ($300) as the villain; scope; an escalation line. But it runs 177 words (about 1:11, against about 45 s), with a 37-word line 2 and a 40-word line 5. Round 1 ran 187. |
| Keeping promises | 9 | 9 | 7 | The $12 part, the $300 and the clean are all paid. "Step four is the one people overdo" (6:00) is paid at 10:05. The escalation line is paid at 12:00. |
| Clarity on one listen | 8 | 8 | 6 | Shorter sentences overall: 27% are six words or fewer (round 1: 12%). Every listed term is explained. Docked for four things: the 55-word replacement sentence; "a weak igniter" (line 117) contradicting line 4; "emery cloth" and "the signal" left unexplained; and "First, gather what you need" sitting just before "Step one." |
| Number load | 9 | 9 | 7 | Six dollar figures (2.6 per 1,000), one in the opening, all traced (the audit's Numbers line is right). The money section carries the title's $12, the part's range and the visit's range, two of them in one sentence. That's allowed for the quote-against-the-part device and the title's figure. |
| Money framing | 8 | 8 | 2 | $300 against a scrub pad at 0:42; the device is used cleanly; the title's money is paid at the win with what was avoided ("a $10 to $30 part you didn't buy and a service call you didn't make"). Round 1's "nothing unusual" is gone. Docked for the invoice line (W2). |
| Safety | 8 | 8 | 3 | The clean is now complete. Thermostat down, power off, tester proved on a live outlet, gas off, cool, the insistence line, the restart, and the check by ear. The gas-leak steps are complete and in order, and "never jumper or bypass a safety switch" covers both switches. Still short: the replacement step (W1), and the filter change lost round 1's "with the furnace switched off". Nearer 9 than round 1's 8. |
| Voice and persona | 8 | 7 | n/a (5 as its own voice) | Many more hammered lines ("Cold vents. Quiet burners.", "That's all.", "Leave it alone and you're fine."), one line of insistence, 45 years once, the filter detail once. Docked for three things: few "I" verdicts; "I think that's a hard number to swallow" word for word as in round 1; and a set-up tic ("So answer me this.", "Ask yourself this.", "Listen to me on this"). |
| Written for the voice | 9 | 9 | n/a | Ranges with "to", "70 degrees", "45 years"; mechanical 0. One risk: "call 911" in digits, where round 1 wrote "nine-one-one" (L1). |
| CTA and ending | 9 | 9 | 3 | No mid-video CTA. The one-line subscribe ask names the channel. The comment ask has a turn, "Leave me a comment", two own-numbers questions and "I read every one", last. The subscribe line sits close to the profile's own description ("plain fixes and honest answers about heating and cooling"), and like round 1's it opens "If ... straight answers". |
| Length and pacing | 8 | 7 | 6 | 15.4 minutes, with less restating than round 1. The hands-on part starts at about 6:43 (round 1: about 7:10). The "other causes" section runs 461 words for four causes. |
| Originality vs the models | 8 | 8 | n/a | Copy guard 0. It differs from R27 and R28 in at least five ways: the point first, the money section, gas off and the doors on, five numbered steps, and the cause ladder. Line 90 is a close paraphrase of R28 [4:15] ("If you scratch this rod, then the stuff will stick to it even faster"); it is idea, not wording. |
| Emotion | 7 | 6 | 4 | "you" 24.2, family 40.6, "but" 7.3, questions 2.2 per 1,000. Belief turns in most sections; bridges that turn. Short on four things: "I" verdicts in 2 of 11 sections; no question to the viewer after 9:45; the rod section opens on what the part is (line 29), the pack's own "Didn't" example; and comfort in the body appears once, at the end. |
| Audit honesty | 8 | 7 | n/a | The Numbers line is complete and right. The hook excerpts exist as cited (`excerpts.md` lines 43, 45, 67). The Scanner line reports the 8 flags honestly. The VO copy strips back to the script word for word (23 tags, all allowed). Wrong: "Rules (F): clean" (W1, W2, W3). Unremarked: four promise devices where the pack says "two or three". |

### My counts of the checks asked for

| Check | Run 04 | Run 02 | Plumbing run 03 (passed) | Reference |
|---|---|---|---|---|
| "you" per 1,000 | 24.2 (56) | 21.0 (56) | 26.4 | 25.7 |
| "you" family per 1,000 | 40.6 (94) | 27.0 (72) | 39.2 | 35.3 |
| "but" per 1,000 | 7.3 (17) | 4.1 (11) | 6.9 | 7.1 |
| Questions per 1,000 | 2.2 (5) | 2.6 (7) | 2.3 | 0.6 |
| Dollar figures | 6 (2.6 per 1,000) | 5 (1.9) | | 0 prices |
| Sentences, mean words | 13.7 | 15.0 | | 14.7 |
| Sentences of 6 words or fewer | 27% | 12% | | 14% |
| Longest sentence | 55 words (line 110) | 34 | | 42 |

- **Questions.**
  - Line 3 (0:29), "When yours quits, does it light first?", is answered at once.
  - Line 37 (4:36), "When was the last time anybody pulled yours out and looked at it?", is answered at once.
  - Line 82 (9:45), "So what color is yours?", is answered at once.
  - Line 47 is a line to say to the tech, and line 107 is a bridge.
  - That leaves gaps of about 4 and 5 minutes, then nothing about the viewer's own furnace from 9:45 to the comment ask at 15:12.
- **"But".**
  - Every content section has one, except step one, where the safety step doesn't need it.
  - Belief turns appear at lines 26, 35-36, 75, 87 and 90.
  - Turning bridges appear at lines 45, 49, 108 and 120.
- **45 years.** Once, at line 108: "I've had 45 years in this trade, and a dirty flame sensor is still the first thing I'd look at". It does a job, as credibility before a verdict.
- **The personal detail.** Once, at line 114: "On the first of the month, I slide my own filter out with my coffee in the other hand and hold it up to the light." 25 words, and it teaches. It matches the profile's facts.
- **Subscribe line.** "If you want more plain fixes and straight answers about heating and cooling, subscribe to Roger the HVAC Guy." One line, names the channel, no book, no plumbing channel.
- **Comment ask.** "And now it's your turn. Leave me a comment with what you were quoted the last time your furnace quit, and how many winters that furnace has on it. I read every one." It is correct in shape and order, and it is the last line.

### Safety defaults on every hands-on step (`SKILL.md`, Safety)

| Step | Thermostat down | Power off | Tester tried on a live circuit first, then proved off | Gas off | Let cool | Restart and the check after |
|---|---|---|---|---|---|---|
| The clean (lines 55-61, 94-104) | Yes, line 56 | Yes, line 57 | **Yes**, line 58: "hold your tester to an outlet you know is live, so you know the tester works, then hold it to the cable" | Yes, line 59: "so the handle sits crossways to the pipe" | Yes, line 60: "until everything in there is cool to the touch" | Yes: door, gas, power, thermostat, then the whole start-up by ear (lines 97-104) |
| The replacement (line 110) | **No** | Yes: "with the power and the gas off and proved off again" | Said only as "proved off again" | Yes | **No**, though the furnace has just run its test cycle | Implied by "the same steps you just did" |
| The filter (line 114) | No | **No** (round 1 had "with the furnace switched off") | n/a | n/a | n/a | n/a |
| The trap and vent pipe (lines 115-116) | No hands-on step; it is a named call (line 119) | | | | | |

- **Never bypass a safety switch:** yes. Line 118: "never jumper or bypass a safety switch to get the heat back. That switch is telling you something." The limit switch and the pressure switch are each introduced as a "safety switch" (lines 14 and 112), so the line covers both.
- **The brief's own safety:**
  - the igniter: lines 73-76
  - the gas smell: lines 62-67
  - no coarse sandpaper: line 90
  - grit kept off the ceramic: line 91

  Nothing in the brief's safety was removed.
- **The named call-a-tech trigger:** line 119, "If the rod's clean, the filter's fresh, and it still lights and quits, that's when you call a tech." Good. The replacement's "if that's one step further than you want to go" is the banned comfort-zone test (W1).

### The gas-leak steps against price guide §9

| §9 step | Run 04 |
|---|---|
| Get everyone out now, on foot, and move well away | Line 63, "Get everyone out of the house right away, on foot, and move well away from it." It now leads, as the round-1 judge asked. |
| Don't flip light switches, use the phone or the garage door opener, light anything, or start the car | Line 64, all five |
| Once well away, call 911 and the gas company; don't assume someone else did | Line 65, both |
| Don't go back in until they say it's safe; don't look for the leak | Line 66, both |
| Some people can't smell it; the smell can fade | Line 67, both, plus "take them at their word" |
| Leave out "open the windows" and "shut it off at the meter" | Both left out |

Complete. No carbon monoxide alarm is mentioned, so the carbon monoxide row doesn't apply.

### The 8 shape-test flags, judged

| Flag | Judgment |
|---|---|
| "Cold vents." / "Quiet burners." (line 25) | Keep. A real picture-enumeration, and the pack's "dial that won't reach". |
| "That $12 part in the title is the flame sensor" (line 41) | Keep. It pays the title honestly, inside the brief's $10 to $30. "in the title" could go ("That $12 part is the flame sensor"), but it isn't a failure. |
| "Step one." / "Next, the gas." | Keep: a step signpost and a short instruction. |
| "Step two." / "Don't touch the igniter." | Keep. |
| "Step three." / "Take the sensor out." | Keep. |
| "Step four." / "Polish it, lightly." / "That's all." | Keep. |
| Step five, ten short sentences | Keep the instructions and "The hum. The click. The glow. The whoosh." (it pays the check by ear). **Cut or change line 104, "Flame on. Blower running. Heat at the vents."** It restates line 103 one sentence later ("The blower kicks on, warm air comes out of your vents"): an echo (`humanizer.md` H18) and a third fragment run in the script. |
| "First, the rod itself." / "Second, your filter." | Keep: list signposts. |

---

## 3. Failures

### Writer slips (the rule was there and wasn't followed)

**W1. The replacement step is one 55-word sentence. It leaves out the cool-down and the thermostat, and it ends on the comfort-zone test.**
> "Swapping it is the same steps you just did, with the power and the gas off and proved off again, the wire moved from the old sensor to the new one, and if that's one step further than you want to go, a tech you trust can do it for the price of the visit."
- **Rules:**
  - `SKILL.md`, Safety default 1: "the burners and metal let cool. Say it again wherever a later step opens the furnace again". At this point the furnace has just run a full test cycle (lines 100-103), so the burners are hot.
  - "How safety sounds": the call-a-tech line "names its trigger ... Never the vague 'if it's outside your comfort zone'".
  - `greenlight-audit.md` C2: easy to follow on one listen.
- **Also muddled:** "the gas off and proved off" suggests the gas can be proved off with the tester.
- **Round 1's W2 is only half fixed, and round 1's W3 problem (an experience test, "unless you've cleaned one before") has moved here in new words.**
- **Fix:**
  > "Swapping it is the same five steps. Thermostat down, power off and proved off with your tester, gas off, and let it cool again, because it's just been running. Move the wire from the old sensor to the new one, and put it all back the way you did before."

  If a tech line is wanted, give it a trigger: "If yours sits behind other parts and you can't reach it without taking them off, that's a call for a tech you trust."

**W2. Said as fact, with no support, and leaning toward the trade's honesty.**
> "The invoice will say something like flame sensor service. It won't say scrub pad, and it won't say how short the job really was." (line 43)
- **Not in the brief or the guide.** It is also not true as a rule: a shop that bills by the hour lists the labor time on the invoice. "It won't say how short the job really was" hints at concealment, which is a step toward a motive.
- **Rules:** `SKILL.md`, The villain ("Aim it at the price, the upsell and the silence, not at motives"; "Say it as a billing fact ... the viewer can check"); Proof, Never ("Sweeping claims nobody can check"); `research-and-sourcing.md` §2 (the fact underneath is true).
- **Who will dispute it:** the study's techs answer price lines, and their defences get the big likes (`SKILL.md`, The viewer).
- **Fix:** "You're paying for the trip out, not the scrub pad." That is a true billing fact; the guide says a clean is "about the price of a service call".

**W3. Other lines said as fact beyond the brief.** Judged one by one:
- **Line 90, "a rough rod collects that film faster than a smooth one".** It is not in the brief or the guide. A real tech says it on camera (R28 [4:15], also `excerpts.md` line 278 and inside voice sample 2), and it is widely repeated in the trade. So it is not invented, and it may stay as everyday knowledge of "what a mistake leads to" (`SKILL.md`, Inputs). It is, though, the reference's own claim, closely paraphrased, and the audit picked it as the voice match. Safer and the writer's own: "It scratches the rod and can leave grit behind in the flame."
- **Line 91, "That ceramic is what keeps the signal on the rod".** True in substance: the ceramic insulates the rod from the metal around it, so the current goes through the flame. It is everyday knowledge, but "the signal" is a new term, never explained. Clearer: "That white ceramic keeps the rod's current from leaking into the metal around it."
- **Line 5, "most of the time all it needs is a light polish".** A frequency claim the brief doesn't make (round 1's W11, "very often the fix is...", in new words). Say "often".
- **Line 102, "And this time, the burners stay lit".** This reads as a promised result. Hedge it: "If it was the sensor, this time the burners stay lit".
- **Line 6, "Nothing here means opening a gas line".** This is the pack's own example line ("Nothing here means opening the gas line.") with one word changed. `SKILL.md`: "the example lines in these rules show a shape; the script never reuses their wording."

**W4. The weak igniter contradicts the opening.**
- Line 4: "If it does [light first] ... It means the gas is getting there and the igniter is doing its job."
- Line 117 then lists "a weak igniter, one that glows dim or slow" among the causes of a furnace that lights and quits.
- Round 1 kept the two apart ("the igniter glows weak and dim, or not at all, and the burners never catch").
- **Rule:** `greenlight-audit.md` C1 and C2.
- **Fix:** "Fourth, an igniter that's getting weak, so the burners are slow to catch or don't catch at all".

**W5. Roger's "I" is thin, and the back half asks the viewer nothing.**
- **"I" opinions or verdicts:** only line 44 (money) and line 108 (the cause ladder), plus the insistence line (61) and the persona detail (114). That is 2 of 11 content sections. Rule 11 says "most items"; the rule now names round 1's 4 of 13 as the gap.
- **The disgust line repeats round 1 word for word:** "I think that's a hard number to swallow".
- **Questions:** nothing about the viewer's own furnace after line 82 (9:45). Rule 5 asks for one about every two items.
- **Rules:** `SKILL.md`, Emotion 5 and 11; Villain, "rotating the wording".
- **Fix:**
  - A short verdict in the rod, step-four, step-five and filter sections. For example: "I'd clean it every fall before the first cold night." / "I'd rather go too light and do it twice." / "That's the sound I like to hear."
  - A question in the cause ladder that the clock clue answers: "So how long does yours run before it quits, seconds or minutes?"
  - Rotate the disgust line.

**W6. The opening still runs long.**
- It is 177 words (about 1:11), against "the opening's six jobs run to about 45 seconds" (`SKILL.md`, The opening; the hook override row).
- Line 2 (37 words) and line 5 (40 words) carry most of it.
- **Fix:** split line 5. "A tech can charge up to about $300 on a night or a weekend to clean that one little rod. Most nights, it needs a scrub pad." Trim line 2 to "When that rod gets coated, the furnace can't tell there's a fire, so it shuts the gas off and tries again, while the house gets colder around you."

**W7. The same idea, three times.**
- Line 12 ("cuts the gas to be safe"), line 26 ("that's exactly what you want it to do") and line 36 ("the furnace is doing its job perfectly ... bad information").
- Line 104 restates line 103 (see the shape-test table).
- "every single time" appears twice (lines 9 and 61).
- Three set-ups in the same shape: "So answer me this." (3), "Ask yourself this." (37), "Listen to me on this" (61).
- **Rules:** `humanizer.md` H18; `SKILL.md`, Voice ("A phrase is voice once").
- **Fix:** cut line 36's second sentence or line 26's last clause. Cut line 104, or turn it into comfort felt in the body: "Ten minutes later, you can feel it in the back bedroom." Drop "So answer me this." and ask the question bare.

**W8. Scope lost from round 1.** None of these is a rule breach, but round 1 was better on each:
- **The sealed burner box.** Round 1 had an honest limit for high-efficiency furnaces whose burners sit in a sealed box: "If getting to it means opening a sealed box or pulling burners out, that's a good place to stop and call a tech you trust." Run 04's step two ("Most burner doors lift up and out") leaves those owners without a stop sign.
- **The free outdoor check of the vent-pipe ends** (snow, leaves).
- **"with the furnace switched off" for the filter change.**

Put back the sealed-box line at step two. It is also the natural home for a named trigger (see W1).

**W9. Minor slips.**
- "First, gather what you need" (line 52) comes just before "Step one". Use "Before step one, gather what you need."
- Emery cloth gets no price and no plain explanation. The guide now has a row: about $7 to $15, or say "a fine sanding cloth" in words.
- The rotation log lists four promise devices; `SKILL.md`, "Ways to promise more value", says two or three.
- Step four ends on an instruction (line 92), not a win (Emotion 8).

**W10. Audit honesty.**
- "Rules (F): clean" is wrong while W1 (F8, safety), W2 (F6, facts and framing) and W3 stand.
- Everything else in the block checks out: the Numbers line, the Hook excerpts, the Scanner line with its judged flags, and 6/6 originality, which is defensible on the brief's igniter, ceramic and other-cause facts, the money angle, the clock clue and the persona detail.

### Library fixes (a rule is missing, unclear or wrong)

**L1. "911" isn't covered by the voice forms.** Round 1 wrote "nine-one-one" and round 2 wrote "911". The pack's Voice list doesn't say which, and the scanner passes both. Add to `SKILL.md` Voice: "emergency numbers as they're said: nine-one-one". This is a small text-to-speech risk on a safety line.

**L2. A non-contact tester can't read through metal-clad cable or conduit.** Safety default 1 now proves the tester on a live outlet (good). But many furnace switches feed the furnace through armored cable or conduit, where a working tester stays silent on a live circuit. Add a second proof that needs no tool, from everyday knowledge:
- "with the thermostat turned up, nothing runs: no hum, no click", or
- "the little light on the control board goes out".

Round 1 used the board light.

**L3. No check on very long sentences.** The script's longest sentence (55 words) carries the replacement safety step. Nothing in the pack or the scanner flags length.
- **Proposal:** the scanner lists any sentence over about 35 words to judge.
- **Pack rule:** "a safety step is said in short sentences, one action each".

**L4. Still open from round 1 (for the operator, as `CHANGES.md` notes):**
- The rotation log has no field for the end CTA's opening words (round 1's L5). Both rounds' subscribe lines open "If ... straight answers", and nothing would catch it.
- No scanner limit on the belief-namer family (round 1's L6). Not needed this time: "figure" appeared once.
- The channel menu still jumps from 6 to 8 (chat turn 1).

**L5. The writer reaches for the same lines across runs.** Run 02 and run 04 share these, word for word:
- "I think that's a hard number to swallow"
- "And this time, the burners stay lit"
- the comment question "what you were quoted the last time your furnace [locked out / quit]"

The rotation log would catch the comment question but not the other two.
- **Proposal:** log the disgust line's wording in the `adversary` field, or add "hard number to swallow" to the pack's `once` list as a stock phrase.

---

## 4. What the script does better than the reference

- **The point first, with a check the viewer can run at once.** "If your furnace lights, runs a few seconds and shuts right back off, check the flame sensor first." / "When yours quits, does it light first? If it does, that's good news." The reference opens "Hey guys, Jay here" and names the sensor at 1:52.
- **The start-up taught by ear with the doors on.**
  - "Turn the thermostat up a few degrees and go stand by the furnace with the doors on."
  - "First you'll hear a small fan hum to life ... Then a soft click ... Then another click as the gas valve opens, and a soft whoosh as the burners catch."
  - The reference runs the furnace with the door off.
- **The feeling the reference never reaches.** "Cold vents. Quiet burners. Just a thermostat that says 70 degrees and a house that never gets there." / "It builds a little every winter, but it never says a word until the night it's finally thick enough, and that night is usually a cold one."
- **The lockout as protection.** "It's your furnace refusing to keep pouring gas into a fire it can't see, and that's exactly what you want it to do."
- **Money, which the reference doesn't have at all.** "A tech can charge you up to about $300 on a night or a weekend to clean or swap that one little rod". The win: "That's a $10 to $30 part you didn't buy and a service call you didn't make."
- **A sentence to say to the tech, with the honest out.** "Did you clean the flame sensor before you wrote this up? An honest tech will already have done it, and that's a tech you trust."
- **A full shutdown, proved, and the gas off, for the clean.** "Now hold your tester to an outlet you know is live, so you know the tester works". The reference only flips the switch and never turns the gas off.
- **The method as the brief gives it.** "A light hand takes the film off and leaves the metal alone." The reference says "press down hard".
- **The igniter, which the reference never warns about.** "Not with your fingers, not with your rag, not with your elbow while you reach past it."
- **A clue that tells the causes apart.** "The clue is the clock. A dirty sensor quits in a few seconds. Heat usually takes a few minutes of running before it trips."
- **A named line for the call, then relief.** "If the rod's clean, the filter's fresh, and it still lights and quits, that's when you call a tech." / "you'll be warm again tonight".

**Where the reference is still better:**
- It reaches its first step at 0:11; the script's hands-on part starts at about 6:43, though the check by ear starts at 1:11.
- It gives the lockout reset (power off a few seconds, then on).
- It explains where the dust on the rod comes from: the burners pull in air.
- It scopes the hard-to-reach sensors and the sealed burner box, which round 1 had and round 2 dropped (W8).

---

## 5. The top five changes, ranked

1. **Rewrite the replacement step (W1).** Use short sentences, one action each: thermostat down, power off and proved off, gas off, let it cool because it has just run, swap the wire, then put it back the way you did before. Replace "if that's one step further than you want to go" with a named trigger. Put back round 1's sealed-burner-box stop at step two (W8).
2. **Clear the unsupported lines (W2, W3, W4).**
   - Replace the invoice line with "You're paying for the trip out, not the scrub pad."
   - "most of the time" becomes "often".
   - Reword the ceramic line in plain terms, and hedge "this time, the burners stay lit".
   - Fix the weak-igniter contradiction.
   - Give the rough-rod line the writer's own reason (scratches, grit).
3. **Give Roger his "I", and ask the viewer in the back half (W5).** Short verdicts in the rod, step-four, step-five and filter sections. Add "how long does yours run before it quits, seconds or minutes?" to the cause ladder. Rotate the disgust line. Replace line 104 with comfort felt in the body.
4. **Tighten (W6, W7).** Bring the opening to about 45 seconds by splitting lines 2 and 5. Say the "it's protecting you" idea twice, not three times. Drop "So answer me this." and the second "every single time".
5. **Library (L1-L3, L5).** Add "nine-one-one" to the voice forms. Give Safety default 1 a second, tool-free proof that the power is off (no hum or click with the thermostat up, or the board light out). Have the scanner list sentences over about 35 words. Catch repeated disgust lines across scripts. Then make the audit's "Rules (F)" report what is there (W10).

---

## Round 1 against round 2

| Round 1 finding (`test-run-02/judge-report.md`) | Round 2 | Status |
|---|---|---|
| W1 "$300 or more is nothing unusual" | "up to about $300 on a night or a weekend"; "more than that at night or on a weekend" (brief corrected too) | **Fixed** |
| W2 replacement skips the shutdown | "with the power and the gas off and proved off again". No cool-down, no thermostat, in a 55-word sentence | **Half fixed** (W1) |
| W3 trap: "unless you've cleaned one before" | The trap is now a named call; no hands-on trap work | **Fixed**, but the same experience test reappears at the replacement ("if that's one step further than you want to go") |
| W4 pressure switch missing from "never bypass" | "never jumper or bypass a safety switch", both switches introduced as safety switches | **Fixed** |
| W5 door-switch claim | Gone. A new unsupported line arrives: the invoice (W2) | **Fixed**, new slip |
| W6 opening 187 words | 177 words (about 1:11) | **Not fixed** |
| W7 restating; "little" 9, "small" 6 | "little" 7, "small" 3; the doubled replacement line is gone. The "protecting you" idea is still said three times, and there is a new echo at line 104 | **Partly fixed** |
| W8 emotion: "but" 4.1, "figure" 4, cold house one clause, "I" 4 of 13 | "but" 7.3, family 40.6, "figure" 1; the dial, the clock, the sounds and relief are present. "I" 2 of 11, and questions fell from 2.6 to 2.2 | **Mostly fixed**, with "I" and questions worse |
| W9 "just by listening", then "blue flame" | "with the doors on" plus "If your burner door has a little glass window in it, you can watch the flames come on" | **Fixed** |
| W10 audit: false originality facts, "Rules (F): clean" | Originality no longer lists false facts; the Numbers line is complete; "Rules (F): clean" is still wrong | **Partly fixed** |
| W11 "very often the fix is..." | "most of the time all it needs is a light polish" | **Not fixed** (reworded) |
| L2 test the tester | Library changed; script: "hold your tester to an outlet you know is live" | **Fixed** |
| L3 no price rows for the tester and emery cloth | Rows added; tester $15 to $25 and scrub pads "a few dollars a pack" used. Emery cloth's price not given | **Fixed** (writer left emery unpriced) |
| L4 two money devices read the same | Defined apart; this script logs "the quote against the part", which is what it does | **Fixed** |
| L1, L5, L6, L7 (brief vs guide, end-CTA log field, "figure" limit, menu gap) | Left for the operator, as `CHANGES.md` says. The menu still skips 7 | **Open** |

**What improved:**
- The emotion counts: "but" and the "you" family are now at the passed plumbing script's level.
- Roger's hammered rhythm.
- The HVAC feelings are on the page.
- The tester is proved first, the bypass line is complete, and the gas-leak order now leads with "get everyone out".
- Every price agrees with the corrected brief.
- The clean is in numbered steps, with a stake promised and paid.
- The money device is now distinct from round 1's, and the log names it correctly.
- A slightly shorter run-up to the hands-on part.

**What got worse:**
- Fewer "I" verdicts (4 of 13 down to 2 of 11), and fewer viewer questions, with none after 9:45.
- The longest sentence went from 34 to 55 words, and it lands on a safety step.
- Round 1's sealed-burner-box stop, the outdoor vent check and "furnace switched off" for the filter are gone.
- The weak-igniter line now contradicts the opening.
- "911" in digits.
- A new unsupported line (the invoice).
- Two lines repeated word for word from round 1 ("hard number to swallow", "this time, the burners stay lit").
