# TEST: judge report, electrical test run 02 (Frederick Barnes)

The script under judgement is `script.txt`, the script part of `output.md`. It runs 3,376 spoken words, about 17.3 minutes at 195 words a minute. The title is "The REAL Reason Your Plug Won't Stay In The Outlet", the brief is A12 (`../brief-A12.txt`) and the rotation log is "none". Run 02 was written after library fixes L1-L8 from the run 01 report (`CHANGELOG.md`, 2026-10-27, "Electrical run 01's library fixes L1-L8 applied"). The writer's library still held E08 and E12; they now sit in `studies/electrical/models-removed-2026-10-27/`. I judged the rules from `electrical-scripts/SKILL.md` as it stands now; the model removal changed only the model lists.

The reference is the same as in run 01: Everyday Home Repairs, "Plug Won't Stay In Outlet" (`../refs/0h_r2bD5bMs-transcript.txt`, 11:13, 1,928 caption words). I judged it on 2026-10-27 against `../judge-rubric.md`, reading every "test-run-01/" in it as "test-run-02/". I changed no file except this one.

**How the counts were made** (the same method as run 01, so the two runs compare):
- **Word counts** split on whitespace, the scanner's method. I get 3,376, the same as the scanner.
- **Rates per 1,000 words** come from regex counts on the spoken text, CTA and comment included:
  - "you" counts you, your, yours, yourself and their contractions.
  - Fire words are fire, burn, melt and ignite in any form.
  - "I" counts I, I'd, I'm, I've, I'll, me and my.
  - Questions are sentences ending in "?".
- **Times** are word positions divided by 195.
- **"L12"** means line 12 of `script.txt`.
- **Facts:** the scanner (`scanner-main-session.txt`) and verifier (`verify-output.txt`) counts are taken as fact.
- **Run 01 check:** the same script re-counts run 01 at 35.9 "you", 5.4 "but" and 7 questions, matching the run 01 report.

**The count table:**

| Measure | Run 02 | Run 01 | Reference | Pack target |
|---|---|---|---|---|
| "you" per 1,000 | **47.1** (159) | 35.9 (113) | 49.3 (95) | at least 35 (fix) |
| "but" per 1,000 | 5.3 (18) | 5.4 (17) | 4.1 (8) | at least 5 |
| Questions | 8 (L3, L27, L37, L65, L105, L117 x2, L167) | 7 | about 1 | 4 to 8 |
| "I/me/my" per 1,000 | 6.2 (21) | 6.0 (19) | 23.3 | 6 to 12 |
| Fire words | 5 (1.5 per 1,000): "melted" L7, "fires" L57 (the CPSC line), "melted" L63, "burning" L71, "melted" L99 | 4 (1.3) | 0 | about 2 per 1,000 at most |
| Death words | 0 ("If the battery died halfway through", L91, is about a battery) | 0 | 0 | at most 2 |
| Sentences | **mean 12.5; 20.0% at 6 words or fewer; 7 over 25; longest 30** | mean 16.5; 8.4%; 22 over 25; longest 33 | no punctuation | at least 12% short; none over 35 |
| Steps with no short sentence | 0 | 3 | n/a | 0 |
| Highest step mean | 14.2 words (step five) | 20.6 (step six) | n/a | 18 at most |
| Money words | 0 | 0 | "about 50 cents", "about two dollars" | 0 |

**Per step** (word counts from the scanner; means, short sentences and questions counted by me):

| Step | Starts | Words | Mean words | Short | Questions | "but" |
|---|---|---|---|---|---|---|
| Opening | 0:00 | 140 | 12.7 | 1 | 1 | 1 |
| 1. Two-plug test | 0:43 | 260 | 11.8 | 6 | 0 | 1 |
| 2. Which plugs give up first | 2:03 | 388 | 11.1 | 9 | 2 | 3 |
| 3. Warning signs | 4:02 | 514 | 12.5 | 7 | 1 | 2 |
| 4. Look inside before you shop | 6:40 | 719 | 12.6 | 12 | 1 | 3 |
| 5. Pick the right outlet | 10:21 | 469 | 14.2 | 6 | 2 | 3 |
| 6. Make the swap | 12:46 | 531 | 13.3 | 6 | 0 | 2 |
| 7. Power back on and the test | 15:29 | 300 + ending | 11.1 | 5 | 1 | 3 |

## 1. Verdict

**This is a clear step up from run 01, and most of it now meets the operator's bar.**
- **It reads simpler and stronger all the way through, not just in the first five minutes.**
  - The mean sentence falls from 16.5 words to 12.5, and the short-sentence share rises from 8.4% to 20%.
  - Every step has a short line and ends on a win.
  - "you" jumps from 35.9 to 47.1 per 1,000.
- **The pain points are specific and in plain words:**
  - "Your phone charger slides out and your lamp cord drops" (L27)
  - "Most folks shrug it off as an old outlet being fussy. But that loose fit is a warning, and it's a warning about heat." (L5)
  - "You didn't do anything wrong. That outlet just wore out doing its job." (L49)
- **The run 01 structure problems are gone.**
  - The store step now comes after the look inside the box ("Step four. Look inside the box before you shop.").
  - The plug-in tester is seen lit before the breaker goes off: "Watch the lights come on. I like this tester for the job, because in a minute you'll watch those same lights go dark."
  - Every wire is tested only after the outlet is eased out.
  - "Say your tester still lights up at one of those wires. Then you stop" covers a wire that still shows power.
- **Facts:** every one traces to the brief or the facts guide, and nothing is wrong.

**I would not upload it word for word, but it's four small line edits from upload.** One is a real safety-order slip, and three are loose ends.
1. **Step six's re-check (12:47) breaks "The order at a device".** The script itself raises the risk: "Somebody may have peeled that tape off while you were out." Then: "Check your pen tester on an outlet with power, take the plate off, ease the outlet out, test every wire…". The viewer pulls the outlet out by its strap before any test through the slots or at the terminals, at the one moment the script says power may be back.
2. **The two-probe tester is never checked on a live outlet,** although the proof rests on it in a two-slot outlet and in a metal box. **The two-slot viewer also never gets a dark check** before the plate comes off.
3. **Step seven has no check for a new two-prong outlet.** The script offers that outlet in L121, and the three-prong plug-in tester won't go into it.
4. **"so it heats up when you've got something running" (L55)** is still the overstatement run 01 flagged (W8).

The verdict is **FIX-THEN-PASS**, a much smaller fix than run 01's. With those four edits I'd upload it.

## 2. Score table

| Category | Run 02 | Run 01 | Reference | Why, in one line (run 02) |
|---|---|---|---|---|
| Opening (first 45 s) | **9** | 8 | 5 | The cause in sentence one, a house question answered in the next two sentences, the wrong guess turned with "but", heat as the stake in proportion, scope, and a value promise naming steps five and seven only. Step one comes at 0:43. |
| Keeping promises | **9** | 8 | 7 | The heat warning (0:20) is paid at 4:09; "one detail there matters in the next step" (9:43) at 10:21; the value promise at 10:21 and 15:29. The words "the real reason" never come back after 0:00. |
| Clarity on one listen | **8** | 6 | 6 | Mean 12.5, 20% short, longest 30. But step four (3:41, three testers, two branches) is dense, "open ground" is still unexplained, and "strip to the gauge" uses "gauge" in a second sense. |
| Number load | 9 | 9 | 6 | No figure in the opening; every figure traced. Step four carries the 1965 to mid-1970s range plus small counts (three lights, two breakers, two screws). |
| Stakes (no money) | 8 | 8 | 4 | No money; fire at 1.5 per 1,000, once where it's real, capability straight after. "when you've got something running" is still an overstatement. |
| Safety | **7** | 6 | 4 | Step four now follows the order closely. Remaining: the step-six re-check order, the two-probe tester never checked live, no dark check for a two-slot outlet, only one half seen lit, and no test for a new two-prong outlet. |
| Voice and persona | **9** | 8 | 6 | Calm, warm and plain; the tenure once, before a verdict; no stories; "I like this tester for the job", "I like that kind of fix". No template step openers. |
| Written for the voice | 9 | 9 | n/a | Units in words, "A L" spaced, button labels in lower case, no "live" or "lives". One small two-way word ("close to"). |
| CTA and ending | 9 | 9 | 3 | A 23-word subscribe line alone in the markers; "which outlet in your house lets go of a plug first… I read every one." |
| Length and pacing | **8** | 7 | 6 | 17.3 minutes, in the sweet spot; hands-on starts at 6:40 (run 01: 8:53). Some echo: the opening's question and step one's verdict say the same thing, and "electrician" comes three times in L69-73. |
| Originality vs the models | **9** | 8 | n/a | No 6-word run shared with the reference, E08, E12, the persona or the voice samples, and no pack example line reused. Five structural differences from E08. One near-echo of a pack example ("I'd do this one first"). |
| Emotion | **8** | 7 | 5 | Every floor met, 7 of 7 wins, 7 of 7 "but" steps, relief at the end. But steps four to seven open on a procedure, not the viewer's scene, and the title's phrase lands only once. |
| Audit honesty | 8 | 8 | n/a | `verify-output.txt`: 0 discrepancies, 46 quotes found; reframes now counted right. But "Rules (F): clean" again sits over safety-order gaps. |

## 3. Failures

### 3a. The rules, checked one by one

**Safety, line by line against `electrical-scripts/SKILL.md` "Safety" rule 1 and its new paragraph "The order at a device":**

| Rule | The script | Result |
|---|---|---|
| Power off and proven, inside the first step that needs it, before any cover plate comes off | Step four, L79 "So you look first, with the power off and proven off." L85 breaker off; L91 "Take the cover plate off" comes after the plug-in tester's dark check | Met |
| Every tester the proof relies on gets the live check, before and after | Pen tester: L91 "check that it works on an outlet you know has power" … "Last, check the tester on that outlet with power one more time. If the battery died halfway through, that last check is what catches it." Plug-in tester: lit (L81), then dark (L85). Two-probe tester: L83 "Then you'll use a two-probe tester across the two slots." L93 "There, put the two-probe tester on the wires themselves." | **Partly.** The pen tester gets both checks; the plug-in tester gets lit-then-dark. The two-probe tester, the only real proof in a two-slot outlet or a metal box, is never checked on power before or after. |
| The plug-in tester goes into the outlet you'll work on before the breaker goes off; seen lit, then dark; held in | L81 "While the power's still on, push a plug-in outlet tester into your worn outlet… you can keep a hand on its body to hold it in. Watch the lights come on." L85 "Back at the outlet, hold the plug-in tester in again. Its lights should stay dark. Check the top half and the bottom half" | **Met, with a gap.** Only one half is seen lit; both are checked dark. L85 itself says "the two halves can be fed from two different breakers", and a worn half that won't seat stays dark with power on. The fix is "Watch the lights come on in the top half, then the bottom." |
| A two-slot outlet: no plug-in tester; the non-contact tester at each slot, then the two-probe tester across the slots | L83, placed before the breaker goes off: "skip the plug-in tester. You'll use a non-contact tester at each slot instead… Then you'll use a two-probe tester across the two slots." | **Partly.** It's named, but not in time order. The two-slot viewer hears no "see it read power, switch the breaker off, see it read nothing". L85's dark check is for the plug-in tester only, so this viewer has no dark check before the plate comes off. |
| At the box: plate off; tester on the terminals you can reach; mounting screws out; device eased forward by the strap without touching wires; then every wire and cable in view; only then hands | L91 "Take the cover plate off your worn outlet. Hold the tester to the screws on its sides. Take out the two screws… ease it forward by its metal strap, without touching the wires. Then hold your tester to every wire and every cable you can see in that box, not just the ones on the outlet." | **Met**: exactly the order. |
| A non-contact tester's silence is never proof; two-probe tester in a metal box or on armored cable | L93 "Your pen tester is handy, but its silence never proves a wire is dead on its own. In a metal box, or on cable wrapped in metal armor, it can stay quiet…" | Met (8.3, 8.4); see the live-check gap above |
| If any wire still shows power: stop, hands off, find the breaker, test again, else a call | L95 "Say your tester still lights up at one of those wires. Then you stop, and your hands stay out of the box. Go back to the panel, find the breaker that's still feeding that wire, switch it off, and test again. If you can't find it, call an electrician." | Met |
| Tape over the breaker; labels can be wrong | L87 "But labels can be wrong. The tester is what you trust." L89 "Put a strip of tape over that breaker and leave a note on it" | Met (8.13, 8.14) |
| A plug-in tester is a check, never permission | L165 "The plug-in tester is a good check, but it's never permission to go back in the box." | Met (8.11) |
| **The re-check before the swap** (step six) | L133 "Back home, prove it's dead again before you touch anything. Somebody may have peeled that tape off while you were out. Check your pen tester on an outlet with power, take the plate off, ease the outlet out, test every wire, and check the tester on the good outlet again." | **Slip.** The plate comes off and the outlet is eased out before any test through the slots or at the terminals, and "without touching the wires" is gone. This is the moment the script says the power may be back. Fix: "Push the plug-in tester into both halves: dark. Check your pen tester on an outlet with power. Plate off, the tester on the side screws, then ease the outlet out without touching the wires and test every wire. Then the pen tester on the good outlet again." |
| 2. How the power comes back, and the test after | L157 "Peel the tape off the breaker and switch it back on." L159 the tester, "usually two lights on", both halves. L161 open ground expected; the GFCI's test button. L163 the lamp test. L167 the plug that used to fall out. L169 the win. | **Met, with a gap.** No check is given for the new two-prong outlet that L121 offers ("Your choices are a two-prong outlet, or a GFCI outlet marked no equipment ground"), and the three-prong tester won't go into it. |
| 2. After a stop sign the breaker stays off | L99 "The breaker stays off, and that outlet stays out of service until a licensed electrician has seen it." L101 "that's a stop too." L103 "That's a stop." | Met |
| 3. The call-an-electrician line names its trigger, in order | L99 the signs, "you stop there", who; L73 "Heat or scorching means the trouble may be in the wiring behind your outlet too, and that's an electrician's job." | Met |
| 6. Old wiring | L101 brittle, cracked or crumbling insulation. L103 "between about 1965 and the mid-1970s… Dull silver instead of copper, or a cable printed with the letters A L or the word aluminum… Repairs on aluminum are a licensed electrician's job." | Met (7.5, 7.7, 7.9, 13.7) |
| 7. No ground: no plain three-prong; open ground expected; the GFCI's test button is the test | L121 "don't buy a plain three-prong outlet." L161 "the tester will show an open ground. That looks like a fault, but it's expected there. If you put in a GFCI marked no equipment ground, its test button is how you check it." | Met; "open ground" still unexplained (W6) |
| Look before you shop (rung shape, new) | L77 "Step four. Look inside the box before you shop." L107 "Then ease the outlet back in, put the plate back on, and leave the breaker off and taped while you shop." No stop sign lands after the store. | **Met** |
| Emergency 12.13 (hot or discolored) | L69 "stop using that outlet now. Unplug whatever's in it. Then get a licensed electrician to look at it soon." | Complete |
| Emergency 12.14 (smell, sparks, buzz) and the panel (9.5) | L71 "unplug what's in it or stop using it. If you can do it safely, switch that circuit off at the breaker… Then call a licensed electrician. If the smell or the buzz is coming from the panel itself, don't touch the panel." | Complete ("heat" at the panel left out of the panel line; minor) |
| What the visuals will draw | L53 "Pay attention to how that outlet feels, sounds and smells when you use it"; L63 "A cover plate that feels warm when you touch it in everyday use." L61 "I'd leave it empty and use a sound one nearby." L81 "keep a hand on its body to hold it in". | Met. Run 01's "Go to your outlet while something's plugged in and running" is gone. L81 would be safer as "on its plastic body", because a worn outlet can leave the tester's blades half out. |
| How safety sounds / Emotion rule 9: no "I" line or aside mid-step with the box open | L97 (outlet eased out): "I know that's a lot of testing for one outlet. Do every bit of it anyway. I mean that." L149 (mid-wiring): "I'd take my time on the hooks. A rushed one is how a brand-new outlet ends up with a loose connection of its own." | **Partly.** L97 comes after the prove-dead test and is the insistence line, so it's arguably allowed. L149 is an opinion mid-swap, which rule 9 forbids unless "after the test" means the prove-dead test (library fix N3). |
| Nothing removed from the brief's safety | Breaker off and verified, same rating, GFCI where required, tamper-resistant where required, scorched wires or melted box to an electrician, the exposed blade, no spreading the blades | Met |

**Fact check, line by line** (brief, and the facts-guide rows named):

| Line | Source | Result |
|---|---|---|
| L1 "The metal grips inside its slots have worn loose." | brief | Correct |
| L3 the two-way plug-or-outlet question; L11-15 the two-plug test | brief ("try the plug in another outlet first") | Correct |
| L15 "thin and flimsy… cheap phone chargers" | brief | Correct |
| L17 "the CPSC, says bending plug blades usually makes the overheating worse" | 4.28 | Correct. On one listen, "the overheating" (1:20) arrives before overheating is explained (4:09); "heat" was named at 0:20, so it's a smaller jump than run 01's. |
| L19 tenure, then "I'd replace it, not reshape it" | profile (35) | Correct; the tenure is once and before a verdict |
| L27, L33 two-prong plugs first; the ground pin braces the plug; "the path that gives stray current a safe way back" | brief; 14.3 | Correct |
| L29-31 brass spring pinches the blade; two jobs | brief | Correct |
| L35 hotel rooms, kitchens and bathrooms | brief | Correct |
| L37-41 thousands of insertions, the angled yank, vacuum and hair-dryer heat | brief | Correct |
| L45 "a worn contact doesn't spring back… The fix for a worn outlet is a new outlet." | brief (fatigue; "have the outlet replaced") | Correct |
| L55 "it only touches your plug's blade on a small spot… so it heats up when you've got something running" | brief: "the contact heats under load" | **Overstated** (as run 01's W8). A phone charger is something running. |
| L57 "loose-fitting plugs can cause overheating and fires… a loose connection can't carry much current without getting hot" | brief (CPSC) | As the source gives it |
| L59 the softening loop; arcing explained; scorches the body | brief; 14.18 | Correct |
| L61 the half-out blade "still carry power"; "a small finger" | brief ("exposed to fingers") | Correct ("small finger" hints at a child: in proportion) |
| L63 the sign list | brief | Correct; the flicker matches "power that cuts in and out when the cord moves" |
| L69, L71 emergency steps; breaker, panel and circuit explained | 12.13, 12.14, 9.5 | Correct |
| L81 "the little tester with three lights on its face" | 8.11 | Correct |
| L85 "the two halves can be fed from two different breakers" | 4.27 | Correct |
| L91-95 live-dead-live, every wire, metal box, armored cable | 8.2, 8.3, 8.4, 8.5 | Correct |
| L99-103 stop signs, aluminum | 13.4, 13.7, 7.5, 7.7, 7.9 | Correct |
| L105 the ground wire, the brass tab | 14.3, 4.27 | Correct |
| L113 "a little sideways T… the twenty-amp kind, and your new one has to match" | 4.18; brief ("same rating") | Correct; avoids 4.18's disputed clause; "Amps" explained one sentence after first use |
| L115 tamper-resistant: shutters, "wherever the code calls for it, and in a home that takes in most outlets" | 4.1, 4.2, 4.14 | Correct |
| L117-119 GFCI places, "within six feet of a sink, a tub or a shower", upstream protection, the sticker, weather-resistant outside, "check with your local inspector" | 4.5, 4.11, 6.13, 14.19, 4.3, guide's "Code is local" | Correct |
| L121 no ground: "a two-prong outlet, or a GFCI outlet marked no equipment ground… it doesn't add a ground" | 4.15, 4.17 | Correct ("Your choices are" leaves out 4.15's third option, which is allowed) |
| L123 listed, UL | 14.48 | Correct |
| L125 push-in holes "Many outlets", spring loosens with heat; screws and clamps grip better | 14.27, 3.7, 3.5 | Correct (uses the adjusted "many outlets", not "cheap") |
| L135 "Where a wire goes straight into a hole in the back, cut it off close to the old outlet." | none | **Unsourced** procedure (general practice, low risk; the plan doesn't mark it general knowledge) |
| L135 pigtail for a short wire | 2.4, 2.5, 14.26 | Correct |
| L137 hot to brass, neutral to silver, ground to green; reversed, the lamp socket carries power | 4.19, 14.1-14.3 | Correct |
| L139-145 strip to the device's gauge, clockwise hook three-quarters around, one wire per screw, the tab, the maker's tightness | 3.1, 3.2, 3.4, 4.27, 3.9 | Correct |
| L147 line and load, "the maker's own advice is to call a qualified electrician" | 6.10, 14.22, 13.6 | Correct (13.6 says "consult"; this is slightly stronger, in the safe direction) |
| L151 every outlet gets its plate | 2.12 | Correct |
| L159 "usually two lights on" | general knowledge (the tester's chart) | Correct; marked as such in the evidence |
| L163 the lamp test; replace a GFCI that fails | 6.5 | Correct |

Nothing in the script is wrong as a fact. The AFCI line that run 01 raised and never answered is gone.

**Emotion, against the pack's eleven rules:**

| Rule | Result | Evidence |
|---|---|---|
| 1. The viewer in the scene; steps open on what they see, hear or feel | **Partly (3 of 7)** | Scene or sense openers: step two ("Watch which plugs give up first. In most houses it's the two-prong ones. Your phone charger slides out and your lamp cord drops"), step three ("Pay attention to how that outlet feels, sounds and smells when you use it") and, at a push, step one ("Take the plug that keeps dropping out"). Steps four to seven open on a procedure title: "Look inside the box before you shop.", "Pick the right outlet. Start with those slots.", "Make the swap. Back home, prove it's dead again", "Power back on, and the test that proves it. Peel the tape off". Run 01's "Step N is…" template is gone. |
| 2. One spine feeling (fix: nuisance, then relief) | Met | The nuisance: "shrug it off… fussy" (L5), "A droop is easy to put up with" (L65), "If yours only droops, you're ahead of it" (L75). The relief: "Does yours hold? That's the grip your old outlet lost." (L167-169) |
| 3. Strong, plain words; short sentences; a short line in every step; 12% across | **Met** | "sliding out", "worn loose", "the yank", "the metal gets tired", "pinches", "scorch", "flimsy", "sags". 20% short; no step without a short line; highest step mean 14.2. |
| 4. A "but" turn inside every step | Met (7 of 7) | L17 blades, L45 "the face isn't cracked… But the wear is all behind the slots", L65 droop, L87 labels, L117 "It's easy to assume any outlet will do… But where it sits decides", L141 hook direction, L167 "Those lights tell you the wiring's right. But the real test is the plug". |
| 5. A question about every two steps; 4 to 8 | Met (8) | None in steps one and six; the longest gap is L117 (10:57) to L167 (16:23). |
| 6. Sensory warning signs | Met | L63: warm plate, brown marks, crackle or buzz, "A smell like hot plastic", the lamp that flickers when the cord moves. |
| 7. Every step ends on a win | **Met (7 of 7)** | L21 "now you know which one you're fixing"; L49 "That outlet just wore out doing its job."; L75 "you're ahead of it"; L109 "knowing exactly what your box needs, instead of guessing in the aisle"; L129 "You've done the hard thinking"; L153 "every wire where it belongs"; L169 "You can feel that it's right." |
| 8. The title's feeling and key word come back | **Partly** | "the real reason" L1 only; then "the real problem behind the droop" (L63) and "the real test" (L167). Step two, the actual answer to the title, lands on "So that's why your phone charger is always the first to go." (L49) and never says "that's the real reason". "won't stay in" comes back as "stays put" (L21, L167) and "lets go of a plug" (L177). |
| 9. "I" verdicts in most steps; one insistence line | Met (7 of 7) | Insistence: L97 "Do every bit of it anyway. I mean that." See the open-box note in the safety table (L149). |
| 10. Capability straight after fear | Met | L57-59 heat, then L65 "If all you've got is the droop, you've caught it early… That's a swap"; L61 the blade, then "I'd leave it empty and use a sound one nearby"; L73 "The good news is you'll notice every one of those signs in everyday life". |
| 11. Finish on relief | Met | L169-171: the plug holds, then "This week, give the outlets that work the hardest the same two-plug test from step one." |

**The chat:** run 02 has no `chat.md`, so the VA stage (START, the missing inputs, "just write it") can't be judged this run.

### 3b. Library fixes (the rule is missing, unclear or wrong)

Run 01's L1-L8 all landed in `SKILL.md` and the scanner, and most worked (see "Run 01 -> run 02"). Four narrower gaps remain.

**N1. "The order at a device" doesn't spell out the two-probe tester's live check, the two-slot dark check or each half.** File: `electrical-scripts/SKILL.md` "Safety" rule 1, "The order at a device".
- **Two-probe tester:** the general clause "every tester the proof relies on gets the live check, before and after" didn't reach it. The writer checked the pen tester twice and the two-probe tester never.
- **Two-slot sentence:** it gives the tools but not the time order.
- **"sees it light":** it doesn't say "in each half".
- Proposed, after "…then the two-probe tester across the slots":
  > "…read with the power on first, so the viewer sees it show power, then again after the breaker is off, showing none. The two-probe tester gets its own live check: it reads power on the working outlet before and after, like any tester. The plug-in tester is seen lit in each half before the breaker goes off, then dark in each half after."

**N2. A re-check after leaving the job doesn't say to repeat the order.** File: same paragraph.
- The rule sets the order for "the first step that needs it". The writer's step-six re-check compressed it and dropped the slot and terminal tests before the device came out (L133). The re-check is the right instinct: the script itself says the tape may have been peeled.
- Proposed:
  > "Any later re-check (after a trip to the store, or the breaker left alone) runs the same order, said briefly: the plug-in tester dark in both halves, the plate off, the terminals, then the device out and every wire."

**N3. Emotion rule 9's "comes after the test" is ambiguous.** File: `electrical-scripts/SKILL.md` "Emotion" rule 9 against "Safety", "How safety sounds" ("the verdict comes after the win").
- **Read as "after the prove-dead test",** both L97 and L149 pass.
- **Read as "after the power-back-on test",** both fail.
- Proposed:
  > "…comes after the test that ends the step (the power back on and the tester's lights), never while the box is open."
- Or, if the operator wants the insistence line inside the testing, say so explicitly.

**N4. The power-back-on rule names only three-prong checks.** File: `electrical-scripts/SKILL.md` "Safety" rule 2.
- Rule 2 names "the plug-in tester's two lights; the test button", and the two-slot clause sits only in rule 1. A script that offers a two-prong replacement (L121) has no named check for it.
- Proposed, added to rule 2:
  > "If the new device is a two-prong outlet, the check is the two-probe tester across the slots, then the lamp."

**Smaller, optional:**
- **N5. Emotion rule 1 vs "The rung shape in fix videos" item 1.** Rule 1 asks each step to open on what the viewer sees, hears, smells or feels. The rung shape opens on "what the viewer notices or checks, as an instruction". Steps four to seven took the rung shape's instruction reading. A line such as this would settle it:
  > "In a fix rung, the instruction points at a sense ('Watch which plugs give up first', 'Listen at the plate') or follows one scene line."
- **N6. Two-way words.** "close" ("cut it off close to the old outlet", L135) is a two-way word like "live". It reads right here in context, but it could join the `core/workflow.md` §4 list with "near" as the fix.

### 3c. Writer slips (the rule was there)

**W1. The step-six re-check pulls the outlet before testing it** (rule: `SKILL.md` "Safety" rule 1, "The order at a device": "the plate off; the tester on the terminals you can reach; the mounting screws out and the device eased forward… without touching the wires").
- The line: L133 (quoted in the safety table).
- Fix: the order as given there (also library fix N2).

**W2. The two-slot case and the two-probe tester are left half done** (rule: "every tester the proof relies on gets the live check, before and after"; the two-slot sentence).
- The lines:
  - L83 "Then you'll use a two-probe tester across the two slots."
  - L93 "There, put the two-probe tester on the wires themselves."
- Fix: in L83, "With the power still on, put the two-probe tester across the two slots and watch it read power." After the breaker, "it should read nothing". In L93, "check it first on the outlet with power, and again after".

**W3. Only one half is seen lit** (rule: the plug-in tester is seen lit, then dark).
- The lines: L81 "Watch the lights come on." against L85 "Check the top half and the bottom half".
- Fix: "Watch the lights come on in the top half, then the bottom."

**W4. No check for a new two-prong outlet** (rule: "Safety" rule 2, "the named check and what a good result looks like").
- The script offers a two-prong outlet in L121, but step seven says only "Push the plug-in tester into your new outlet."
- Fix: one line in step seven, "If you put in a two-prong outlet, the two-probe tester across the slots should read power, and your lamp should light."

**W5. The heat line is still overstated** (rules: "Emotion", "Never… worst-case exaggeration"; the brief wins on facts; run 01's W8).
- The line: L55 "so it heats up when you've got something running".
- Fix: "so it heats up when something's pulling hard, like a vacuum or a hair dryer." This also ties back to L41.

**W6. Terms on one listen** (rules: "The viewer", every term explained the first time; core C2).
- **"open ground"** (L161) is still unexplained. "That looks like a fault" helps, but the viewer doesn't know what it means. Fix: "the tester will show an open ground, the light pattern that says no ground wire is connected".
- **"Strip each wire to the gauge molded on the back"** (L139) uses "gauge" in a second sense, 30 seconds after "wire strippers… sized notches". The term list says "gauge" is explained the first time. Also, L135 says "strip a fresh end" before the viewer knows how much. Fix: "the strip guide, the little mark molded on the back that shows how much bare wire it wants". Say it at L135.
- **"makes the overheating worse"** (L17, 1:20) comes before overheating is explained. Fix: "makes the heat worse".

**W7. The open-box "I" line** (rules: "Emotion" rule 9, "How safety sounds").
- The line: L149 "I'd take my time on the hooks. A rushed one is how a brand-new outlet ends up with a loose connection of its own."
- Fix: move it after the win at L153, as "A careful hook is what keeps that new grip tight. I'd take my time on it every time.", or settle N3 first.

**W8. Restated points** (rules: "Length", "Never pad"; `humanizer.md` H18).
- **The opening and step one say the same verdict:**
  - L3 "Every plug in one outlet points at the outlet. One plug everywhere points at the plug."
  - L13-15 "you've found it. It's the outlet… If your loose plug falls out everywhere you try it, look hard at the plug instead."
  - Fix: keep the question in the opening and let step one give the answer, or make L3 one line ("Your answer tells you which one is worn.").
- **The electrician three times in five lines:**
  - L69 "Then get a licensed electrician to look at it soon."
  - L71 "Then call a licensed electrician."
  - L73 "that's an electrician's job."
  - The first two are separate emergency sequences and must stay. L73 can become "Heat or scorching can reach the wiring behind your outlet too."
- **"I'd rather you" twice:**
  - L47 "I'd rather you swap a tired outlet…"
  - L65 "I'd much rather you catch it there"
  - Fix: reword one.

**W9. The title's phrase comes back only once** (rule: "Emotion" rule 8; the operator's "the title's feeling repeated").
- Step two pays the title (2:03-3:50) but closes on "So that's why your phone charger is always the first to go."
- Fix: "So that's the real reason your plug won't stay in: the springs behind the slots wore out, not your plug." That is one sentence, and it replaces L49's first sentence.

**W10. A near-echo of a pack example** (rule: "Point then promise", the priority flag "in fresh words each time"; "Files in this skill").
- L21 "I'd do this one first, every time." shares four words in a row ("do this one first") with the pack's example "Do this one first, before anything else."
- It's under the 5-word guard, and the step already has its own fresh flag: L9 "Do it before you pick up a screwdriver."
- Fix: cut L21's middle sentence.

**W11. The evidence block overclaims in two places** (rules: `core/greenlight-audit.md`, the evidence block).

| The evidence says | The script |
|---|---|
| "Rules (F): clean" | The safety-order gaps in W1 to W4 and the open-box "I" line in W7 (or N3). |
| Numbers: "at most two figures per step" | Step four: "three lights" (L81), "two different breakers" (L85), "the two screws" (L91) and "about 1965 and the mid-1970s" (L103). Only the date range is a real load on one listen, so it's a small overclaim, not a numbers failure. |

`verify-output.txt` found 0 discrepancies in 46 quoted lines, and its re-counts (3,376 words, ITEMS, SENTENCES) match. The reframe count is now right ("reframes 1 = I'd replace it, not reshape it"), and item one is honestly given as 43 seconds.

## 4. What the script does better than the reference

| What | Reference | Run 02 |
|---|---|---|
| The point | "hey guys how's it going it's scott with everyday home repairs and i want to talk a little bit about a very common problem…" | "If a plug keeps sliding out of your outlet, the real reason is usually the outlet itself. The metal grips inside its slots have worn loose." |
| Plug or outlet | Never checks the plug; uses a charger as proof the outlet is worn | "Does every plug you own fall out of that one outlet, or does one plug fall out of every outlet you try?" then the two-plug test |
| The why | "from heat and just use over time it's really opened up and that is why it's not holding" | "Every time you push a plug in, the brass flexes. Do that thousands of times and the metal gets tired. Then there's the yank… And then there's heat." |
| The stake | "this can obviously be a safety hazard because you start to expose a connected hot side piece of metal" | Heat first, sourced ("The CPSC says loose-fitting plugs can cause overheating and fires."), then "A plug hanging halfway out leaves part of its metal blades showing, and those blades still carry power." Each one is answered: "I'd leave it empty and use a sound one nearby." |
| The tester, lit then dark | "i have two amber color lights on… now we can see that all lights are off" | Now matched and widened: "Watch the lights come on… in a minute you'll watch those same lights go dark", plus the pen tester live-dead-live, every wire after the outlet is eased out, and what to do if a wire still shows power. |
| Look before you buy | Confirms the rating only mid-install: "i didn't talk about earlier but i did confirm that the old outlet that i'm replacing is 15 amp" | "Look inside the box before you shop… And look closely at the slots on the old outlet, because one detail there matters in the next step." |
| The right part | Prices and "commercial grade" | Rating by the sideways T, tamper-resistant, GFCI by location, the no-ground options, weather-resistant, listed, screws or clamps over push-in holes. No money. |
| Stop signs | none | Scorch, melted box, brittle insulation, aluminum, each with "The breaker stays off". |
| The finish | "we won't have any issues for years to come hopefully that helped you out" | "Push it in. It should take a firm push to seat, and it should stay put with the cord hanging down. Does yours hold?" Then the same test on "the one your vacuum always goes into". |

**Where the reference is still better:** its hotel scene is a moment the viewer has lived: "you try to plug in your phone and the outlet just literally will not hold the plug at all". Run 02 has the place but not the moment: "the worn outlets you remember are in hotel rooms, kitchens and bathrooms" (L35). One line would close it: "the hotel outlet where your phone charger slid out every night".

## 5. The top five changes, ranked

1. **Fix the step-six re-check and finish the tester sequence (W1-W4; library fixes N1, N2, N4).** This is the only blocker. In step six: plug-in tester dark in both halves, plate off, the side screws, then ease the outlet out without touching the wires, every wire, then the tester re-check. In step four:
   - both halves seen lit;
   - the two-slot order in time (reads power, breaker off, reads nothing);
   - the two-probe tester checked live before and after.

   In step seven, add a check for a new two-prong outlet.
2. **Correct the heat line (W5):** "so it heats up when something's pulling hard, like a vacuum or a hair dryer."
3. **Bring the title home in step two (W9):** "So that's the real reason your plug won't stay in…" Add the hotel moment at L35.
4. **Open steps four to seven on the viewer's scene (rule 1; N5).** For example:
   - "Step four. Your hand's on the cover plate screw; stop there."
   - "Step six. You're back from the store with the new outlet in your bag."
   - "Step seven. The new outlet's in, the plate's on, and the breaker's still taped."
5. **Clean the loose ends (W6-W8, W10, W11):**
   - Explain "open ground" and the strip guide, and say "makes the heat worse".
   - Move L149's "I" line after the win.
   - Cut L73's third electrician, one "I'd rather you" and L21's "I'd do this one first".
   - Make the opening's question set up step one instead of answering it.
   - Correct the evidence ("Rules (F)" and the step-four figure count).

## Run 01 -> run 02

### Scores side by side

| Category | Run 01 | Run 02 | Change |
|---|---|---|---|
| Opening (first 45 s) | 8 | 9 | +1 |
| Keeping promises | 8 | 9 | +1 |
| Clarity on one listen | 6 | 8 | +2 |
| Number load | 9 | 9 | 0 |
| Stakes (no money) | 8 | 8 | 0 |
| Safety | 6 | 7 | +1 |
| Voice and persona | 8 | 9 | +1 |
| Written for the voice | 9 | 9 | 0 |
| CTA and ending | 9 | 9 | 0 |
| Length and pacing | 7 | 8 | +1 |
| Originality vs the models | 8 | 9 | +1 |
| Emotion | 7 | 8 | +1 |
| Audit honesty | 8 | 8 | 0 |
| **Total (of 130)** | **101** | **110** | **+9** |
| Verdict | FIX-THEN-PASS (middle reads as a manual; three prove-dead gaps; store before the look) | FIX-THEN-PASS (four small line edits; one safety-order slip) | |

### Run 01's top five changes

| # | Run 01 asked for | Run 02 | Evidence |
|---|---|---|---|
| 1 | Rebuild the prove-dead sequence | **Mostly fixed** | Lit first: L81 "While the power's still on, push a plug-in outlet tester into your worn outlet… Watch the lights come on." Every wire after the outlet is out: L91 "ease it forward by its metal strap, without touching the wires. Then hold your tester to every wire and every cable you can see". Still showing power: L95 "Then you stop, and your hands stay out of the box." Two-slot: L83. **Not yet:** the two-probe tester's live check, the two-slot dark check, each half lit, the step-six re-check (L133). |
| 2 | Look inside before shopping | **Fixed** | L77 "Step four. Look inside the box before you shop." L107 "leave the breaker off and taped while you shop." The store step (step five) never opens the box. |
| 3 | Make the middle feel it | **Mostly fixed** | Short lines in every step (20% overall); step six's mean falls from 20.6 to 13.3; step four now asks "Is there a bare copper or green wire in the box?"; every step ends on a win ("knowing exactly what your box needs, instead of guessing in the aisle"). **Not yet:** steps four to seven open on a procedure ("Step six. Make the swap."), and step six still asks no question. |
| 4 | Get the outlet examples out of SKILL.md, add a 5-word guard, reword L11, L192, L196 | **Fixed** | The scanner's example guard reports 0. No 6-word run is shared with SKILL.md's examples (the shared runs are its required safety wording). Run 01's "If you only check one thing…", "the springs… that's what holds the plug" and "that plug clicks in and holds" are gone. One 4-word near-echo remains (W10). |
| 5 | Cut restatements, close loose ends | **Partly** | Cause once: **fixed** (L1). AFCI: **fixed** (cut). Check at everyday use: **fixed** (L53, L63). Evidence: **partly** ("reframes 1" now right; "Rules (F): clean" still overclaims). The electrician once in the signs step: **not fixed** (L69, L71, L73). One "I'd rather you": **not fixed** (L47, L65). "open ground": **not fixed** (L161). "heats up when something's pulling hard": **not fixed** (L55). |

### Run 01's library fixes L1-L8 (now in the library; did run 02 follow them?)

| Fix | Run 02 | Evidence |
|---|---|---|
| L1 "The order at a device" | **Partly** (followed closely in step four, not in the re-check; see N1, N2) | Fixed: L81, L85 "Its lights should stay dark. Check the top half and the bottom half", L91, L93, L95. Gaps: L83 two-probe with no live check and no order; L133 "take the plate off, ease the outlet out, test every wire". |
| L2 Look before you shop | **Fixed** | L77, L105 "Take a picture with your phone and make a few notes. Is there a bare copper or green wire in the box?", L107. |
| L3 Pack examples moved; 5-word guard | **Fixed** | Copy guard 0; no run 01 echo; one 4-word near-echo (W10). |
| L4 A short sentence in every step; 12% across; split any step over 18 | **Fixed** | SENTENCES 20.0%; "no sentence of 6 words or fewer: none"; highest step mean 14.2. Step four, for example: "But labels can be wrong. The tester is what you trust." |
| L5 "I" lines out of open-box steps | **Partly** | L149 "I'd take my time on the hooks." comes mid-swap; L97 sits with the outlet eased out. The rule's "after the test" is ambiguous (N3). |
| L6 `first-item-seconds: 45` | **Fixed** (as applied) | The scanner gives "item one at word 140 (about 43 seconds at 195)" with no false flag. It still measures to the "Step one" header, not the first instruction (L11 "Take the plug that keeps dropping out", 0:47). The opening's question at 0:08 is a real check, so nothing is late. |
| L7 No ordinal sub-list inside a step | **Fixed** | Step five names its parts: "Start with those slots." "Next, your new outlet should be tamper-resistant." "It's easy to assume any outlet will do from there." "One more thing to check on the package." No "First… Fourth". |
| L8 "lives" as a two-way word | **Fixed** | No "live" or "lives" in the script. The trouble "sits" instead: "the reason sits inside. Behind each slot in your outlet sits a strip of brass" (L29). |

### Run 01's writer slips W1-W10

| Slip | Run 02 | Evidence |
|---|---|---|
| W1 the store step opens the box | **Fixed** | The no-ground choice now refers back: "If you found no ground wire in the box, don't buy a plain three-prong outlet." (L121) |
| W2 template step openers | **Partly** | "Step N is…" is gone, and steps two and three open on the senses. Steps four to seven open on a procedure. |
| W3 the pack's example wording | **Fixed** | All three lines rewritten: L169 "That's the grip your old outlet lost… You can feel that it's right." |
| W4 steps three and four end on an instruction | **Fixed** | L75 "If yours only droops, you're ahead of it." L109 "Now you'll walk into the store knowing exactly what your box needs". |
| W5 restated points | **Partly** | The cause is said once and "hands" once, but the electrician comes three times in L69-73, "I'd rather you" twice, and the opening question echoes in step one. |
| W6 terms in order | **Partly** | The amp is now explained one sentence after first use ("Amps measure how much current is flowing"). "open ground" is still unexplained, and "the overheating" still comes early. |
| W7 the check at a loaded outlet | **Fixed** | L53 "when you use it"; L63 "when you touch it in everyday use". |
| W8 overstated heat | **Not fixed** | L55 "so it heats up when you've got something running" (run 01: "whenever you've got something running"). |
| W9 AFCI raised, never answered | **Fixed** (cut; the brief gives no AFCI rule) | No AFCI line. |
| W10 audit evidence | **Partly** | "reframes 1" is correct, and item one is honestly 43 s. "Rules (F): clean" is still claimed over gaps. |

### Run 01's "where the reference is still better"

| Item | Run 02 |
|---|---|
| The tester lit, then dark | **Fixed**: L81, L85 |
| The frustration scene | **Partly**: "Your phone charger slides out and your lamp cord drops" (L27) is a scene; the hotel line (L35) is still an explanation. |
| "you" at 49.3 | **Fixed**: 47.1, against 35.9 in run 01 |
