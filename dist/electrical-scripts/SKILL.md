---
name: electrical-scripts
description: Script rules for the operator's home-electrical channel (Frederick Barnes, and any future channel in this niche). Use whenever an electrical script is written, rewritten or reviewed, or an electrical title and brief arrive for scripting. Sets the viewer, the stakes (fire and shock, never money), the opening by video type, emotion all the way through (pride and capability first), "point then promise", the seven video types and the item and step shapes, the CTA and ending, length, voice for the text-to-speech, proof, safety and the electrical scanner checks. Persona, tenure and CTA wording come from the channel's persona profile; claims policy, output format and the audit come from the core rules. To write a script, type START: the script-writer skill runs it and loads this pack.
---


# Electrical scripts

An electrical video fixes one everyday problem in the viewer's house, or explains one thing they've always wondered about, for an older homeowner who wants to do it right and stay safe. The winners in this niche (Everyday Home Repairs, How To Home, LRN2DIY, Practical Engineering, Technology Connections, Top Homeowner) name the problem in the first breath, make the viewer feel able to handle it, and keep the danger real but in proportion: fire and shock are the reason it matters, never the topic. This skill copies that shape for a talking-head AI presenter who explains and never demonstrates.

## What this skill covers

**It owns:** the viewer, the stakes, the villain (optional), the opening by video type, emotion all the way through, "point then promise", the video types and their item or step shapes, CTA placement and the ending, length, voice for the text-to-speech, proof, safety and the electrical scanner checks. Scripts are clean narration only: no edit notes, cues or directions of any kind.

**It doesn't own:**
- **The persona:** name, tenure, sign-off, personal details. These live in the channel's persona profile.
- **The CTA wording:** also in the persona profile.
- **The claims policy, output format, voiceover copy and audit:** these live in the core rules.

**Authority:** the core claims policy and offer rules come first, then safety and the title's promise, then the persona profile, then this skill, then the core base rules. The core `workflow.md` runs every script (START, the input gate, the output format).

## Files in this skill

| File | What it's for |
|---|---|
| `references/unit-plan-template.md` | The plan to fill in from the title and brief before any prose. |
| `references/facts-guide.md` | Well-established US electrical facts (code rules, sizes, safety facts, the emergency steps, the terms to explain), each checked against sources and re-checked by a second researcher. Used for any fact the brief doesn't give. No prices. |
| `references/voice-samples.md` | Stretches of real human narration from the model winners: the voice anchor for every script (core `voice-anchoring.md`). |
| `references/excerpts.md` | Real lines from the models grouped by job (the point, the stakes, the turn, the check, the call-an-electrician line, the win, the comment question). Use for shape and range, never wording. |
| `references/models/INDEX.md` | The model library: 31 winning videos from real channels with 1M+ views, all posted 2022 on, sorted by video type. Each file has a beat map, how the video voices each emotion, why it works, the full labelled script and what doesn't transfer. Read at the planning step only. |

Every reference file except the facts guide, and this file itself, is under the copy guard: the scanner flags any run of 8 or more words shared with it. The example lines in these rules show a shape; the script never reuses their wording. None of them is taken from a model.

## Where this pack overrides the core

The core base rules apply wherever this pack is silent. These are the places it changes them, each one approved by the operator. Everything else in the core stands.

| Core rule | What this pack does instead | Decided |
|---|---|---|
| `workflow.md` §2, the default inputs | The `inputs` block below: the title, the brief and the rotation log. The research pack is `not used`: the brief is the fact source, with `references/facts-guide.md` behind it. | 2026-10-27 (default, as plumbing) |
| `retention-mechanics.md` §2 and §6, the value line and "short range only"; the hard-banned "by the end of this video" | The opening may carry one value promise (job 5 of "The opening"): an escalation, or what the viewer will know or be able to do by the end, naming things paid later, never the first items in order. Concrete named forward lines are allowed in the body. Vague teases stay hard-banned. The scanner lifts only "by the end of this video". | P11, operator 2026-10-27 |
| `cta-and-endings.md` §4 and §1 ("one ask per moment"), `retention-mechanics.md` §1.4, `workflow.md` §4 ("the closing line is exactly one sentence"), `retention-mechanics.md` §14, `greenlight-audit.md` F3, `variety-rotation.md` slot 9 | The ending is the one-line subscribe ask, then the comment ask (a turn to the viewer, an outright ask to comment, a specific question and "I read every one"), which ends the script. Two or three sentences; nothing after it. The two asks are separated by the turn line to the viewer; the practical next action closes the last item (Emotion rule 11). FORMAT CHECK's closing field reads `[comment line, last line of the script]`; rotation slot 9 rotates the comment question. | 2026-10-27 (default, as plumbing's P5) |
| `workflow.md` §3, the 8-minute minimum; `greenlight-audit.md` F2 | At least 12 minutes at the profile's words per minute; 15 to 22 is the sweet spot. See "Length". The evidence block's Length line reads "(minimum 12)". | Operator 2026-10-27: "even 15-22 is sweet spot" |
| `variety-rotation.md`, the rotation log line | Six more fields at the end of the line: `\| model: [IDs] \| type: [video type, or new: shape] \| topic: [3-5 words] \| stakes: [device] \| promises: [devices] \| comment: "[the comment question]"`. For Frederick, the core fields read: return: n/a \| mid-CTA: n/a \| cta variant: n/a \| adversary: none, or the old work / the cheap part with how it was voiced \| swears: none \| details: none \| book: none \| closing: comment line. The opening field also records the order: opening: [move], order [type default \| changed: …] "[first 6-10 words]". | 2026-10-27 (as plumbing) |
| `workflow.md` §3 step 4 and `greenlight-audit.md` D3, the `--refs` files | The copy guard runs against this file, `references/excerpts.md`, `references/voice-samples.md` and every file in `references/models/`, plus the persona profile. The facts guide is left out (as plumbing's price guide is): its facts are said in the script's own words, and a plain fact can't be guarded word for word. | 2026-10-27 (as plumbing) |
| `research-and-sourcing.md` §6, "each number said alongside whoever counted it" | Sources don't have to be said. A source is named only where it really helps (CPSC, the electrical code); when it is named, its figure is said exactly as the source gives it. | 2026-10-27 (as plumbing) |
| `greenlight-audit.md` E1, the originality score | Signal 1 counts facts from the brief or the facts guide that most videos on the topic don't use; signal 4 (three named sources) doesn't apply. Out of 6, passes at 4. The evidence block reads "Originality: [n]/6 (missing: …)". | 2026-10-27 (as plumbing) |
| `retention-mechanics.md` §6 and `greenlight-audit.md` B5, signposts | The sections are the opening, each item, step or contender, and the ending. "Number four." or "Step three." is the signpost. In an explainer, each block opens on the question it answers ("So where does that current actually go?"); in X vs Y, the contender's name is the signpost ("Now the lever connector."). Core B5's 90-second payoff limit stands; the five-minute limit is for forward lines. | 2026-10-27 (as plumbing) |
| `greenlight-audit.md` D4, "every number traces to the fact source" | The fact source is the brief plus `references/facts-guide.md`. A number from neither (a setting, an interval) is allowed only when it is everyday knowledge and is marked "general knowledge" on the evidence block's Numbers line. No code number, wire size, breaker size or distance is ever filled in from memory. | 2026-10-27 (P7 adapted) |
| `retention-mechanics.md` §2, the hook; `greenlight-audit.md` A1b | The electrical opening is the hook (see "The opening"), checked as the same three jobs: the transformation is the fix or answer named in the first sentence; the pain or wish is the problem the viewer has right now; the curiosity is the question, or the surprising fact the video answers. The Hook line records those three lines and the value promise ("value line: '[line]'" or none). The "first payoff" in A1b is the point: the problem with its fix or answer, by about 15 seconds; the opening's six jobs run to about 45 seconds, and in a list item one starts by about 30. The value promise (P11) replaces retention §2's value line: at most one, on any video where it fits (not "one in three"), placed as job 5, never the first sentence. | 2026-10-27 (as plumbing) |
| `humanizer.md` H22 and `greenlight-audit.md` C2, prices and the number load | H22's price clauses don't apply: the script says no prices at all; the rest of H22 stands for technical figures (see "Numbers" under "Voice"), and C2's "three or more dollar figures" check reads "three or more figures in one sentence". C2's price clauses don't apply either: the script says no prices at all (operator 2026-10-24: "we dont really need to use money in electrical"), and the C2 check quotes any money word or dollar figure as a failure. The rest of C2 (plain words, every term explained the first time, numbers easy to follow) stands. | 2026-10-24 |
| `workflow.md` §4, "Prices, years and stats are digits" | Volts, amps, watts, milliamps, wire and cable sizes and plug codes are written in words, the way an electrician says them ("a twenty-amp breaker", "fifteen hundred watts", "twelve-two cable"); years stay digits ("the 2023 code"). One form for the whole script. The scanner's number check reads the word forms. See "Written for the voice". | P13 item 6, operator 2026-10-27 |
| `greenlight-audit.md`, the evidence block | One more line after the core's extra lines: `Emergency: none \| [situation] -> facts guide rows [n-n] -> "[line]" for each step`. The I-verdicts line ends `\| open-box: none`, or quotes every "I" line said between the plate coming off and the power back on (Emotion rule 9; runs 02 and 03 each had some, and the audit called the rules clean). Numbers: each figure is followed by "= brief" or "= facts guide [row]". | P13 item 5, operator 2026-10-27 |
| `variety-rotation.md` slots 1, 2, 3, 5 and 6, the money moves | Not used: the promise with a number (when the number is money), the cost-to-result, the result as a life reward, the surprise about a price, the cost turn, the cost bridge, the price-tag comparison and the reaction to a price. Use instead: slot 1 the problem at its worst, the question the viewer is already asking, the surprise (a fact, never a price), the pain then the good news, the unnamed object ("There's a part in most outlet boxes that…"); slot 2 the double take, the overlooked detail, the question turn; slot 3 effort or time ("This next one takes about a minute and a screwdriver"); slot 5 the objection said outright; slot 6 a verdict, a tradeoff, a preference with a reason. | 2026-10-24 (no money) |

## Inputs

Electrical scripts are written from the title and the brief; there is no research pack. The workflow reads this block at START and won't write until every required input passes.

```inputs
- title | required | the locked title, exactly as approved
- brief | required | the ideation brief for this title; the script's facts, steps, code rules and safety lines come from it first
- research-pack | not used | electrical scripts are written from the brief and the pack's facts guide
- rotation-log | required | the channel's last five ROTATION LOG ENTRY lines (from the earlier scripts in this chat, or pasted), or "none" for a new channel
```

- **The brief is the fact source,** with the facts guide behind it. The brief wins on facts; it never wins on removing safety (see "Safety"), and never over a facts-guide "Never say" line (7,200 volts as every street's figure, "recalled", "is illegal"): there the narrower one is said and the plan notes the disagreement.
- **Where the brief is silent, the script fills in** (P7, adapted):
  - **Code rules, sizes, distances and safety facts** come from `references/facts-guide.md` only, said plainly. A row marked "reading" or "thin" is never the source for a number, a code claim or anything that loosens safety; a row marked "kept" (one checker, no second source) is said only with "in most cases" or the source's name. A "reading" row that makes the viewer more careful (test every wire in the box, tape over the breaker, labels can be wrong, never water on an electrical fire, what to look at with the panel door open) is said in plain, general words.
  - **Everyday settings and intervals** that aren't safety steps (which way a screw turns, how long a job takes) may come from everyday knowledge, marked "general knowledge". A safety step, a check that decides whether something is safe to touch, a code claim, and any number on wire, breakers, distances or danger never come from general knowledge: they come from the brief or the facts guide, or the script says it's a question for the local inspector or a licensed electrician.
  - **No wiring method, code claim or "this is legal for you to do" beyond the brief and the facts guide.** When neither says it, the script says it's a question for the local inspector or a licensed electrician.
  - The run stops with NOT READY when the brief can't carry the title's main promise, or a safety fact the script needs is in neither the brief nor the facts guide.
  - **A title that promises a job the facts guide gives to a licensed electrician** as the viewer's own work (§9, 13.4: the panel's inside, aluminum repairs, a generator hookup without an interlock or transfer switch) is written as "When the job is a licensed electrician's" sets out; if it can't be, it stops with NOT READY, names the claim and offers honest versions for the operator to re-lock (core `workflow.md` §3). The script never changes the title itself.
- **Each script's facts come from its own brief and the facts guide only,** never from an earlier script in this chat; same-chat rotation reads only the ROTATION LOG ENTRY lines.

## The viewer

The viewer is a 50+ American homeowner, often in an older house, who would rather understand and fix it than wait for someone, but who is a little afraid of electricity, and right to be. They come from search as often as from the feed: they have a dead outlet, a breaker that trips, a plug that falls out, a light that glows when it's off, and they typed the problem in. Under the click sits one question: "Can I handle this safely, or is this a call?"

**What they bring (from the electrical study and the model comments):**
- **A problem in front of them right now.** The best openings name it the way they'd say it ("the outlet that just quit", "the plug that won't stay put").
- **A real fear of getting it wrong,** and a real pride in getting it right. Pride appeared in about 46% of the niche's titles (462 of 1,007) and was the first emotion in more than any other (about 29%); safety fear appeared in 293 and led in outlet and switch titles only once in 9. The viewer leaves feeling able, not scared.
- **Trust in electricians, inspectors and firefighters.** They treat them as the experts. "Electricians HATE This" titles flopped (31K and 375 views). Never set them up as the enemy.
- **Impatience with the wait.** The most-liked praise on how-to winners is the pace: no intro, straight to it.
- **The doing questions:** which wire is hot, what size breaker, do I need a GFCI here, will this pass inspection, is my tester lying. Answer the ones that apply inside the script, at the step where they'd ask.
- **What they thank:** the answer fast, the reason why, steps clear enough to try, the check that tells them it's right, and an honest "this one's a call".

**Skill level:**
- Write for beginners to handy homeowners, in plain words.
- **These terms are always explained the first time,** in one plain clause, then used plainly: GFCI, AFCI, hot, neutral, ground, breaker, panel, dead front, circuit, amp, volt, watt, backstab (the push-in holes on the back of an outlet or switch; not a push-in wire connector, which is a listed splice), pigtail, wire nut, lever connector, gauge, box fill, double tap, two-pole breaker, interlock, transfer switch, inlet, backfeed, service drop and meter, tamper-resistant, listed (UL), non-contact tester, multimeter, Romex (NM cable), conduit, aluminum wiring, CO/ALR, knob-and-tube, line and load, open ground (on a plug-in tester: no ground wire connected), junction box, fuse. Any other trade word gets the same treatment (`references/facts-guide.md` §14 holds a plain explanation for each).
- Give the reason behind a step in one sentence. Don't lecture on theory the step doesn't need.
- Never explain what everyone knows (flipping a switch, plugging in a lamp).

**The standard kit:** assume a screwdriver set, pliers, a flashlight, electrical tape and a non-contact voltage tester (or say once that one is worth owning), plus a plug-in outlet tester in any script that opens an outlet. The non-contact tester finds live wires; its silence never proves one dead (facts guide 8.3). Anything beyond that (a two-probe voltage tester or multimeter, wire strippers with a gauge, lever connectors, a fish tape, a stud finder) is named with what it does, never its price.

---

## The stakes (no money)

This channel says no prices and no savings (operator, 2026-10-24). Where plumbing put a price line, **every list item carries one stake line**: what it risks, once, in plain words. **In how-to and fix videos, the stake goes only in the steps where the risk really is** (the power-off step, the connection that can loosen, the sign that it's a call), usually two to four in a video; a step with no real risk carries none. The calmest how-to winners name almost no danger (E01, E05). Rotate the stake devices across a channel's scripts (the rotation log's `stakes:` field):

- **Fire,** plainly and briefly: heat at a loose connection, arcing behind the plate, the scorch mark nobody sees. Said once where it belongs, never as a scare reel.
- **Shock:** the live metal, the wire that's still hot when the switch is off, the tester that gave a false "dead".
- **The hidden bad work in the wall:** what the last owner or handyman left behind.
- **The cheap part:** the knock-off connector, the bargain tester, the device that's never been listed.
- **"You've been doing it wrong":** the habit almost everyone has, why it looks right, and why it matters. Never a scold.
- **The nuisance that won't stop:** the breaker that trips every night, the flicker, the outlet that works when it feels like it.
- **The inspection:** work that won't pass, said only where the brief or the facts guide gives the rule, as a fact, never as a threat. Never the sale of the house or insurance as a stake (facts guide 13.9 is "thin… keep out of scripts"), except knob-and-tube and insurers, which 7.4 confirms.

**Rules:**
- **In proportion.** One stake per item, said once, then the fix. "That's how a loose wire turns into heat inside the wall" lands; piling fire, death and lawsuits into one item reads as a scare tactic.
- **Fire is the stakes, never the topic** (operator, 2026-10-26). No item exists only to frighten.
- **The worst case only when it's real and common enough to matter,** with the fix right after it.
- **How much fire.** Fire is the stake on about one item in three at most, and fire words (fire, burn, melt, ignite) come up about twice per 1,000 words at most, about six in a 3,000-word script. The models use 0 to 6 per video, and 14 of 31 never say one (measured on the model set of 2026-10-27, before six were removed). Death words (kill, die, deadly, fatal) only where the title or a generator, panel or shock item makes them real, and at most twice. "Possibly worse" often does the job.
- **Numbers on danger** (how little current is dangerous, how far a generator sits from the house) come from the brief or the facts guide, and named sources keep their figures exactly.

## The villain (optional)

The operator (2026-10-27): "villain does not need to be necessary". Most winning electrical videos (70-80%) have none. Use one only where the topic carries it:
- **The last owner's or handyman's wiring,** found in the box or the panel: "A splice buried in the wall with no box around it."
- **The cheap product:** the unlisted part, the knock-off connector, the cord that should never have been sold.
- **Named problem panels,** only as the old panels they are and only with what CPSC or inspectors say, from the brief or the facts guide, plus Federal Pacific's independent test results with the source named (operator, 2026-10-27): the old Federal Pacific Electric Stab-Lok panels (CPSC closed its investigation in 1983 without a recall; inspectors routinely flag them) and old Zinsco panels (inspectors flag them and report breakers that can fuse to the bus). Never "recalled", never that a panel will fail or burn, never the bare company name as if it traded today. Federal Pacific's independent test results may be said as facts guide 9.15 gives them, credited to the independent testing, never to CPSC, and never as "they will fail" (P13 item 8, operator 2026-10-27). Otherwise "some older panel brands". Replacing one is a licensed electrician's job.

**Never** electricians, inspectors, firefighters or the utility as the enemy, never a motive, never a named company called dangerous beyond its sourced facts. The narrator's reaction is aimed at the work or the part ("That's the kind of connection that keeps me up at night"), never at a person.

## The opening

Every opening, whatever the video type, does these jobs in about the first 45 seconds. Rotate the order and shape across a channel's scripts (the rotation log tracks it), use the order for the video type (see "The video types"), or model it on a model file's beats, never its wording. What can't change: the point comes first and fast, and nothing on the banned list appears.

1. **The point in the first sentence:** the problem the viewer has right now, and wherever the title allows, the fix or the answer itself, by about 15 seconds. Never hold the answer back to the middle.
2. **A question, when it fits,** about something the viewer can see, hear, smell or feel in their own house in under a minute, without a tool and without opening anything (does the light flicker only when the fan is on; is the dead outlet near a bathroom, the kitchen, the garage or outside; does the light dim only when the dryer starts), answered in the next sentence with what each answer means. Never a question only the footage can answer, and never a thought experiment with the answer held back.
3. **The stake, once,** in plain words: the title's own stake (see "The stakes"). Fire or shock comes into the opening only when the title is about a danger (a generator, a panel called dangerous, a WARNING title) or the fix-video order asks "is it dangerous". Otherwise the opening's stake is the nuisance, the habit or the hidden work, and the first fire or shock line waits for the item where the risk is real (the models bring danger in at a median of about 1:37; only 8 of 27 do it in the first 45 seconds; measured on the model set of 2026-10-27, before six were removed). The villain line only if the topic has one.
4. **Honest scope or reassurance,** in one line: what this fixes and what it doesn't, or that most of the job is safe for a careful homeowner and which part isn't. It never takes back the title.
5. **One value promise, when it fits** (P11, operator 2026-10-27): one sentence that either promises the escalation ("we'll go from the two-minute check to the one sign that means you stop and call") or what the viewer will know or be able to do by the end ("By the end of this video you'll know how to tell a tired breaker from a real fault, and the one sign that means you leave the panel alone"). It names only things paid after item three (or after the third step, check or block), never item one, two or three (operator: "as long as they are not iteams one 2 and 3"), and it isn't always three things ("doesnt have to be 3 items also"). An escalation may name its starting rung, since the operator allowed "a simple promise of escalation" on its own terms. In a list of three, it names what the viewer will be able to do, not an item. Never "First I'll show you… then…". Write it as "By the end of this video…"; the short "By the end, you'll…" is still a banned tease. Never a vague tease ("stick around", "you won't believe"). Or, in a list, **the count line** naming the whole list and what it does for the viewer. Never "today we're going to".
6. **The first real tip, check or step** by about 45 seconds; in a list, item one by about 30 seconds.

**Simpler and stronger** (operator, 2026-10-21, for every niche): the first line hits the viewer's own problem in strong, plain words; it doesn't have to be the worst case.

**One figure at most in the opening** (a distance, a voltage, a wire size or a statistic); the rest belong to the step or item that uses them, and the opening never repeats item one's figure.

**The title's promise, word by word.** The plan lists every promise in the locked title (the fix, "the right way", "no patching", "never again", "is yours one?", "it's not the breaker", "I find") and where each is paid. The electrical code and the device's own instructions always win over the title: nothing in the script promises a shortcut either one forbids. An absolute word in the title ("Never Fall Out Again", "Never Solder Wires Again", "Everyone Makes") is delivered as the strongest true version in the title's own key words, tied to the cause it fixes ("A clamp-style connector grips the wire from both sides, and that grip is what stops the loosening"); it is never repeated as a promise ("it'll never fall out again", "no more fire risk") and never walked back with a disclaimer. The scope line may name the one case it doesn't cover, once, as a check ("If it only flickers on one bulb, it's the bulb, not the wiring."). A title written in the first person ("I Find") is paid as the typical case plus an "I" verdict ("In a house that age, I'd expect at least three of these."), never as a story. A question in the title ("Is Yours One?", "Can You Run Romex in Conduit?") is answered in the opening and turned into a check the viewer can run. If the brief can't pay a promise honestly, the run stops with NOT READY.

**Never in an opening:** a name or channel intro, a greeting, "today we're going to", a run-down of the first items in order, a first-person test or demonstration ("I tested", "watch me"), or a tenure number other than the profile's or the locked title's.

**Tenure:** at most once in the video, as the profile's fixed number (Frederick 35) or the locked title's, and only where it does a job (credibility right before a verdict or a mistakes list).

## Emotion, all the way through

The operator (2026-10-21): "simpler and stronger on emotions... using strong words and targetting the exact pain points of this audience like reference scripts do. more work on emotion triggering throughout." The plumbing tests showed what happens without it: the pain named once, then explanation; "you" 21 per 1,000 words against 41 in the hit; "but" once per 1,000; no questions; 11 of 15 items ending on an instruction. The electrical titles lead with **pride and capability** (research: pride in 462 of 1,007 titles). The winning scripts carry it like this: capability or reassurance by about 30 seconds; one spine feeling at nearly every item (rule 2); how-it-works curiosity in 24 of the 31 models (the model figures in this section were measured on the model set of 2026-10-27, before six were removed); safety fear quiet, said in a sentence or two at a median of about 1:37, answered straight away; and pride as the landing at the wins and the close. Each model file's "Emotion voicing" shows the words they use.

1. **Put the viewer in it.** Say "you", and tie every item, step or block to the viewer's own house. In lists, how-to and fix videos, open each item or step on what they see, hear, smell or feel there (the flicker, the buzz, the warm cover plate, the switch that clicks but does nothing, the faint smell near the panel), not on how the thing works. In explainers and X vs Y, a block may open on the question the viewer has or on the plain picture, as the winners do at nearly every block. Either way, the block ends on what it means in the viewer's house.
2. **One spine feeling, all the way through, and one real feeling per item on top of it.** The spine comes from the video type and comes back at nearly every item, step or block in fresh words (13 of the 31 models do this):
   - **Mistakes lists and single big mistake:** "you've been doing it wrong", said kindly: why the habit looks right, then the turn.
   - **Explainers and X vs Y:** "so that's why", with the belief it flips.
   - **Fix videos:** the nuisance named at the start and paid off as relief at the end.
   - **How-to:** capability: you can do this, and here's how you'll know it's right.
   - **Know-this lists:** the "I wish I'd known", landing on pride.

   Pride and capability are where every item lands (the win), whatever the spine. On top of the spine, each item aims at one real feeling: the fear of getting shocked or starting something in the wall; the frustration of the problem that keeps coming back; the worry about what the last owner did; the doubt about their own tester; the "so that's why" of seeing how it works; wanting to keep the people in the house safe; the pride of getting it right; the relief that it's a simple fix.
3. **Strong, plain words.** Physical verbs and pictures: loose, scorched, buzzing, arcing, sagging, cooked, brittle, "live", "still hot". Danger is said plainly with "can" or "could" and its cause ("a loose wire can heat up and char the plastic around it"), the way the winners say it; the strong words go on what the viewer sees, hears and feels, never piled onto the disaster. Short sentences mostly; join two with "but" to keep it moving. **At least one sentence of six words or fewer in every item, step or block, and at least 12% across the script** (the punctuated models run 2% to 54%, the middle about 12%; test run 01 had 8.4%, and its step six averaged 20.6 words a sentence). A step whose sentences average over 18 words gets split. The scanner's SENTENCES line gives the share, and its ITEMS line names any item with no short sentence. At most one picture-phrase per item, only when it teaches.
4. **"But", inside items and between them.** Inside every item, at least one turn: what people think or do, then "but", then the truth. Between items, bridges that turn ("That one's a five-minute fix. The next one isn't."). Rotate how the belief is named ("most folks figure", "the package says", "you've probably been told"); "Most people…" opens a sentence at most once per script (`humanizer.md` H20), and never the "it's not X, it's Y" reframe more than once (H21).
5. **Ask the viewer,** 4 to 8 times in the script (about every two items): a question about their own house, answered straight away ("Does the light flicker when the fan kicks on?"), or the turn question the next line answers. Never a question only the footage can answer.
6. **Sensory warning signs,** where the winners would show the damage on camera: the brown mark on the plate, the smell like hot plastic, the crackle when the plug moves, the warm switch. At most one per item, only where it's the real sign of that problem, said as what to notice and what it means, never as horror.
7. **End every item or step on a win:** relief, pride, the before-and-after ("Now that switch clicks on and the light comes on with it, every time."), or, in explainers, the "so that's why" or the protection that's already there. Never end on an instruction.
8. **Reaffirm the title's feeling and key word** every few items, in nouns and verbs (the mistake, the real reason, the safe way), not "-ly" adverbs; not every item, never robotic. **When the title's feeling is fear** ("WARNING", "Dangerous", "Can Kill", "Worst", "BEWARE"), what comes back is the title's noun (the mistake, the backfeed, the panel, the lineman), not the danger word. The danger itself is said about three times in the whole video: in the opening, at the item where it's real, and once near the end as the reason the fix matters. Each time, the next line puts control back (rule 10). Fear never becomes the script's lead feeling: pride and capability lead every title.
9. **Let the narrator speak.** One short "I" opinion or verdict in most items ("I'd replace that one today."), and once per video a line of insistence where it matters ("Please, test it first. Every time."). In a step done with the box open, the "I" line is the stop-sign verdict or comes after the test that ends the step (the power back on and the tester's lights), never while the box is open (Safety, "How safety sounds").
10. **Capability over fear, straight after it.** Every fear line is answered in the same item, within a sentence or two, by a line that puts control back: the check they can run, the sign that it's fine, the point where they stop, or the protection already in the house doing its job (the breaker that trips, the GFCI that cuts the power, the ground wire that gives a fault somewhere to go), named only where the brief or the facts guide confirms it. The winners bracket every danger this way (E13, E14, E15, E16, E22).
11. **Finish on relief and capability, not danger.** The last item before the ending closes on reassurance or one small thing to do tonight. One thing, never a to-do list or "homework" that runs back over earlier items: that is a recap (core `retention-mechanics.md` §14).

**Targets** (measured in the 31 models with labels stripped, on the model set of 2026-10-27 before six were removed; a judge measures the finished script the same way. These are floors, never quotas: a sentence never gets a "you" or a "but" just to hit a number.)
- **"you"** (you, your, yourself and their contractions): at least 35 per 1,000 words in fix, mistakes, single-big-mistake and know-this scripts (model medians: fix 43, mistakes 37, know-this 33, single 28); at least 30 in how-to (every step is "you" here, because there is no on-camera "I"); at least 20 in explainers and X vs Y (model medians 16 and 30). Frederick's old scripts: 26.6.
- **"but":** at least 5 per 1,000 (models: median 5.5, middle half 4.1 to 7.2, top 11.5), spread across the items rather than stacked in one. Frederick's old scripts: 1.0.
- **Questions to the viewer:** 4 to 8 in the script. Frederick's old scripts: 0.
- **"I":** "I/me/my" about 6 to 12 per 1,000 (the models that don't demonstrate run 5.1 to 8.7). Verdict lines ("I'd…", "I won't…") in most items, about 2 to 4 per 1,000. No demonstration "I" at all.

**Never, still:** invented facts or events, guaranteed outcomes ("this will never happen again"), anyone's motives, vague teases, scare-reel lines ("this could kill your whole family tonight"), worst-case exaggeration, jokes.

## Point then promise

- **Point first.** The first answer (the cause named, the rule stated, the first step) comes before anything else.
- **Pay forward lines fast.** A later item named in a forward line is paid within about five minutes; the opening's value promise is paid inside the video.
- **Keep one promise open.** After the opening, never more than about five minutes without a new forward line or a payoff: a line that names the next value ("The next one is why your tester sometimes lies."), a question the next item answers, or a check the viewer can run.
- **Every callback has a promise.** "Like I said" or "I promised" must match something the script really said earlier.
- **A priority flag at the first answer,** in fresh words each time, never the same shape twice across a channel's scripts (for example, "Do this one first, before anything else.").
- **No recaps** at the end.

## Ways to promise more value

Two or three per video, in the body (the opening carries at most the one value promise), rotated across a channel's scripts:
- **A numbered item with its stake in words:** "Number six is the one that leaves the light fixture with power when the switch is off."
- **The escalation ladder:** the two-minute check, then the fix a careful homeowner can do, then the sign that it's a call for a licensed electrician. The default for fix videos.
- **The rule that protects everything:** turn it off, then prove it's off. Named at the first step it touches, paid straight after.
- **A check the viewer can run:** the plug-in tester's lights, the test button, the tug test on a connection, noticing a cover plate or plug that feels warm in everyday use (a sign to act on, never a thing to touch on purpose: hot, buzzing or smelling means the sequence in "Safety"). Only checks that are safe and that the brief or facts guide confirm.
- **A problem the viewer didn't know they had,** promised and then shown.
- **A myth flag** that names the belief it flips in the same line: "Number three is the one everybody gets backwards: a three-prong outlet doesn't mean you have a ground." Never a bare "the one everybody gets backwards".
- **The "why" promised:** "And I'll tell you why that wire got short in the first place."

## The video types

Pick the type from what the title promises, not its first words. "How to fix [a problem]", "The REAL reason your…" and "Why does my X keep Y" are **fix this problem**. "How to [add, install, connect, replace] X" is **how-to** (and a licensed electrician's job is explained, never instructed: see below). "Why do [things everyone owns] have/do X?", with nothing wrong in the house, is **explainer**; a "why does it do that" about a fault the viewer has (the glow, the trip) is **fix**. A title that names one mistake is **single big mistake** even when the brief gives several causes: they become the related slips. A "vs" inside a how-to title is the how-to with one X vs Y block at the step where the choice is made. These are the most common types, not the only ones. Each type has its own opening order and item or step shape. The models column names the model IDs in `references/models/` (all real channels: structure and voice, never wording); `references/models/INDEX.md` lists every file. Follow "Using the models".

| Type | Title shape | Opening, in order | First tip by | Item or step shape | Models |
|---|---|---|---|---|---|
| **How-to / correct way** | "How to [do the job] (the Safe Way)", "The RIGHT Way to…" | The job and the problem it solves → "you can do this" with the one part that's a call → the value promise or the step count (the power-off rule is named at the first step that touches wiring, as the rule that protects everything, never in the opening) | 30-45 s | The step, the reason, the mistake to avoid, how to know it's right | E01, E02, E03, E04, E05, E07, E33, E34 |
| **Fix this problem** | "The REAL Reason Your…", "Why Does My X Keep Y?", "Plug Won't Stay In?" | The symptom in the viewer's words → the usual wrong guess → the real cause in one line → is it dangerous (honest, in proportion) → the fix ladder | the real cause by about 15 s (it counts as the point); the first check by 30-45 s | The check, what it tells you, the fix, the sign it's a call | E09, E10, E11 |
| **Explainer** | "What X Actually Does", "Why Do Plugs Have Holes?", the test topics explained | The question everyone's wondered → the common wrong answer, turned in one line → the real answer's first layer in one line (what it is, or what it isn't) → what it means in your house → the value promise | 20-40 s | The idea, the plain picture that explains it, what it means for you | E13, E14, E15, E16, E18, E19, E37 |
| **X vs Y** | "AFCI vs GFCI", "Wire Nut vs Lever Connector: Which One?" | The moment of choice in the viewer's house → the contenders in a line each (two, or a third as the reference: E22's ordinary breaker) → the argument everyone has → "each one has a job" → the value promise | 30-45 s | Each contender: what it does, where it's right, where it's wrong (E22); or each test or criterion with both contenders side by side (E21); then which to use where, as new information, never a restatement of each one | E21, E22 |
| **Mistakes list** | "N Wiring Mistakes…", "N Breaker Box Mistakes…" | The symptom or the hidden work → the stake → one credibility line (tenure here if anywhere) → the count line | 15-30 s | The mistake, what it risks, the right way, the check | E24, E25, E26, E27, E35, E36 |
| **Single big mistake** | "The Generator Mistake That…", "The Dead Outlet Mistake Everyone Makes" | The mistake named in the first sentence → why almost everyone makes it → the stake in plain words → the value promise | 20-40 s | One mistake explored: how it happens, what it does, the right way, the check, the related slips | E29, E30, E31, E32 |
| **Know-this list** | "N Electrical Things Every Homeowner Should Know" | The moment the viewer wished they'd known → the stake → the count line | 15-30 s | The thing, why it matters in your house, what to do with it, the win | E28 (read its warning: one unsafe tip cost the list its trust); E04; E24 and E25 for list pacing |

**Explainers are a chain of whys.** The first layer of the answer comes in the opening (point first); each block then answers the next question the last one raised ("So why are the holes always in that spot?"), every block pays something, and the deepest layer lands by about the middle, never later. The models do this: E37 starts knocking down the myths at 0:37 and reaches the "so that's why" (the patents) at 4:06, before the middle; E13 answers yes-or-no at 1:04 and the why at 7:49. In an explainer, each block opens on the question it answers.

A title that promises tests or demonstrations is written as explanation and results from the brief, never as "I tested" (see "Proof").

### The item shape in lists

In the mistakes list and a single big mistake's related slips, each item runs in this order (the table's item shape says what goes into it):
1. the scene in the viewer's house
2. what's really happening in the wall, the box or the device (one or two lines)
3. what it risks, once (see "The stakes")
4. the turn ("So what do you do instead?")
5. the right way, cut to what the viewer needs, with the safety line inside the step where the risk is
6. the check that tells them it's right, when there is one
7. the win

In a know-this list, each item runs: the moment in the viewer's house when it matters, the thing in one plain line, why it matters there (the stake, once), what to do with it (the safety line inside), the check when there is one, the win.

**Order:** the way the viewer meets them in the job or the house (which screw, how much to strip, which way to hook; or what you can see with the cover on before what the electrician finds inside), each item setting up the next, with the most capable, lowest-stakes item last (E24 ends on the screwdriver bit, E26 on the clamp outlet).

**Small counts.** When the title's count is small (three to five), each item is split into its named parts (one mistake on the outlet, the same mistake on the switch), and each part gets its own scene, turn and check; the signpost stays the title's number ("Number one, part two"). Never add items that change the title's count. One extra item may close the list only when it's called a bonus as it arrives, never promised in the opening (that's a tease).

### The step shape in how-to videos

1. what to do, as an instruction to the viewer (on a licensed electrician's job, what is done and what you check: see below)
2. the reason, in one sentence
3. the turn, with "but": the mistake people make at this step where there is a common one (in about half the steps; a how-to's spine is capability, not correction), otherwise the reason it's done this way rather than the way it looks ("You'd think any screw will hold it, but…")
4. how to know it's right (what you'll see, hear or feel)
5. the win or the bridge to the next step

No aside or side story inside a step where the box is open or the panel cover is off; asides go between steps.

**One step, one job** (operator, 2026-10-29: "thats fine to be honest as long as its not waffling. but yes if within that step there are 2 steps in it, it can be split"). A long step is fine when every sentence does the job. A step that holds two jobs the viewer would do one after the other is split into two numbered steps: prove it dead, then look inside; make the connections, then choose the outlet type. Frederick's outlet video ran step two at 555 words (prove dead, then the whole look inside) and step ten at 514 (the connections, then GFCI and AFCI).

**No "first, second, third" inside a numbered step or item** (test run 01: "Fourth" came 54 seconds before "Step four", and on one listen they collide). Name the parts instead: the rating, the shutters, the wet spots, the box with no ground.

### The rung shape in fix videos

**In any swap, look before you shop** (test run 01). Anything that decides which part to buy and can only be seen inside the box (a ground wire or none, aluminum, how many wires, a stop sign such as scorching or a melted box) is checked first: power off, prove it dead, ease the device out and look, put it back, then shop. Or the shopping step says plainly to buy after that look. The store step never describes opening the box, and no stop sign lands after the part is bought. **The buying step adapts to what the viewer found** (operator, 2026-10-29: "make sure the script is adaptive for this"): for each thing the look can turn up, it says what to buy or where to stop, never one assumed case. The wire size against the breaker (facts guide 1.18: 12-gauge on a 15-amp breaker is fine, so the new cable may be 14 or 12; on 20 amps, 12 only; 14-gauge on 20 amps is the call); copper or aluminum (aluminum is the stop); a ground wire or none; a metal or plastic box; room in the box or not. Rules keyed to a place go by where the **new** device sits (GFCI: facts guide 4.30), and a kitchen or bathroom circuit limit is said by room (1.17a). An AFCI receptacle covers an extension only at the first outlet of the existing circuit (6.19a).

Each rung of the fix ladder, easiest first, call last:
1. what the viewer notices or checks, as an instruction that points at a sense ("Turn the fan on and watch the light.") or follows one line of the scene in their house (Emotion rule 1); never a bare procedure ("Step six. Make the swap." alone)
2. what that tells them: the cause it points to, in one line
3. the belief it turns, with "but"
4. the fix for that cause, with the safety line inside it
5. how to know it worked
6. the sign it's a call (a named trigger), then the win or the bridge to the next rung

### When the job is a licensed electrician's

When the brief or the facts guide says the work is a licensed electrician's job (anything inside the panel, a generator interlock, inlet or transfer switch, a meter-socket adapter, aluminum wiring repairs, a new outdoor run that needs a permit), no step is an instruction to the viewer. Each step says what is done and why, as what the electrician does ("The electrician fits a two-pole breaker sized to the inlet, so…"). Then it says what the homeowner sees, checks or asks for: the kit listed for that exact panel, the permit and the inspection, the routine on a storm night, the sign it was done right. The opening's scope line says so plainly ("This is the part you hire out. Here's what right looks like, so you know it when you see it."). In a mistakes list about the panel, "the right way" is what the electrician does, and "the check" is what the viewer can see without opening anything: the label and the directory, the filler plates, a breaker that's warm or buzzing, scorch on the cover, the brand on the panel label. A "How to" title is paid as how it's done right and what to ask for, never as panel work the viewer does. The viewer's steps are only the parts that are theirs: choosing, the questions for the electrician, and, for a generator, running it on storm night exactly as the brief or the facts guide gives the order. Adding or swapping any breaker, an aluminum repair and a new 240-volt or EV circuit are on the electrician's side too. In the opening, "power off and prove it" gives way to the rule that protects everything for that job (for a generator: the house and the utility can never be connected at once).

**A title that sells a product or method made for another job** (B7's solder-seal connectors are made for cars, boats and low-voltage lighting): the opening says plainly where it belongs and what goes in a house box instead, inside the first 45 seconds, and the house-wiring answer gets at least as much time as the other.

**Code in its place.** A code rule, permit note or other code background goes inside the step that needs it, in two or three plain sentences. It may come before the first fix only when every fix is judged against it, and then in under about 40 seconds (E09 gives the free-wire rule in 37 seconds before its ladder); never a block of code before the fix.

- **Length per item, step or block: set by the 12-minute minimum, never below it.** At Frederick's 162 words a minute, about 1,700 words sit inside the items at 12 minutes and about 2,200 at 15 (the opening and the ending take about 220). So the guide per item is:

  | Items | Words each at 12 min | at 15 min | at 22 min |
  |---|---|---|---|
  | 3 | about 575 (split into named parts: see "Small counts") | 735 | 1,115 |
  | 5 | 345 | 440 | 670 |
  | 7 | 245 | 315 | 480 |
  | 9 | 190 | 245 | 370 |
  | 10 | 170 | 220 | 335 |

  How-to steps and fix rungs can be shorter (60 to 150 words) when the job has many steps; an explainer block runs about 150 to 250 words (E13, E14, E16). The winners' 12-minute lists ran items of about 170 to 430 words (E24, E25). The minimum never wins over value: a longer item carries more of the brief (the reason, the check, the sign it's a call, the related slip), never a warning said twice or a point restated. Cut those first; never cut power off, prove it dead, how the power comes back or the test after.
- **Bridges:** never more than two items or steps in a row without a forward line: a line naming what comes next, a question the next item answers, or a check the viewer is about to run. An item's own stake line doesn't count.
- **Item one by about 30 seconds** in lists (plumbing run 03 put it at word 139: too late); the first check or step by about 45 seconds in fix and how-to videos. The scanner marks item one only past 45 seconds, so in a list the plan checks the 30 itself.

**A title that fits none of the seven:** build the opening from the six jobs in "The opening", in the order the closest type uses, and pick the shape that best suits the content. Note it in the plan as "new type: [the shape in a few words]". When the same new shape comes up on three or more scripts (the rotation log's `type:` field shows it), it's proposed for this table and added only with the operator's yes.

## Using the models: never a copy

The models show how winning videos are built. A script borrows their structure, never their wording, and never one model's structure whole.

1. **Read "Doesn't transfer" first, then the labels.** Before the beat map, read the file's "Doesn't transfer" list, and treat every passage labelled [UNSAFE], [ELECTRICIAN'S JOB], [FIRST-PERSON DEMO], [POINTING], [MONEY], [TRADE BASHING], [SPONSOR], [TEASE], [RECAP], [INTRO] or [PRODUCTION NOTE] as if it weren't there. Every model was made by a real person on camera: their demonstrations, meter readings and tests, pointing, job, family and customer stories, prices and cost verdicts ("worth the extra cost"), sponsor reads and links, trade bashing, jokes, UK and European wording and voltages, and unsafe methods never transfer. Never turn a banned method into a "don't do this" line that describes it (E19). A model's missing power-off step never transfers (`references/models/INDEX.md`, "Read with care"), and a fact, figure or test result in a model file is never a fact source: it comes into the script only when the brief or the facts guide carries it.
2. **Panel and generator work is the electrician's part.** Where a model's presenter works inside a panel or fits an interlock (E02, E25, E32, E33, E34), the script explains what the electrician does and gives the viewer only what can be checked from outside (see "When the job is a licensed electrician's" and "Safety").
3. **Name the models and the differences.** The plan names one or two models for the video type, or a model filed under another type whose beat map fits the content (INDEX "also fits"; E09 for a single big mistake whose related slips are a diagnose ladder; E21 or E22 for a how-to with a choice in its title), and at least three things done differently: the opening order, the number or order of items, the promise devices, the stake device, the comment question. Where the locked title is a model's own title (A1/E01, A30/E25, B6/E26), take the opening or the item order from a second model.
4. **No repeats.** The same model never appears in the channel's last five rotation log lines (`| model: [IDs]`). If every model for the topic is blocked, use the closest model of the same video type on another topic, and say so in the plan; never reuse one.
5. **Blending is encouraged:** one model's opening shape, another's step pacing.
6. **Planning only.** Model files are read at the planning step, never kept open while writing. Wording comes fresh from the brief, in the persona's voice.
7. **The audit checks it:** the plan lists what doesn't transfer, its differences and its models, and no model in it appears in the last five rotation log lines.

The copy guard flags any run of 8 or more words shared with a model file.

## Two titles on one topic

When two locked titles share a topic, each script takes the part its title promises and leaves the rest to the other. "How to fix" and "the real reason" titles carry the diagnosis and the ladder. "The mistake" and "pull this out" titles carry the one mistake or the one fix, explored in depth with its related slips. A danger title on a shared topic carries the chain of what happens; a product title carries the part itself and why it's sold. The plan's SIBLING line names the other title and what this script leaves to it. When the brief's facts are mostly the sibling's, the run stops with NOT READY and asks for this title's own material.

## CTAs

Frederick Barnes (and any channel whose profile says subscribe only):
- **No mid-video CTA.**
- **At the end, a very short subscribe ask** (operator, 2026-10-27: "CTA will literally just be a very short subscribe one"): one line, in the persona profile's shape, tied to what the channel delivers, worded fresh each time. Shape: one sentence of 15 to 25 words: the ask, Frederick Barnes or the channel, and what it brings next in the viewer's terms (the plain, safe answer to the next thing in the house that won't behave). No like or bell ask, no "if you want" hedging, no sign-off; the comment ask follows straight after.
- **Talking Head** scripts wrap it in markers exactly as core `workflow.md` sets out, with `===START CTA(NO BOOK)===` and `===END CTA===`. One block only. The block holds the subscribe line only. The comment ask comes after ===END CTA===, after one blank line, as ordinary narration and the last line of the script:

```
[the last line of the last item]

===START CTA(NO BOOK)===
[the one-line subscribe ask]
===END CTA===

[the comment ask: two or three sentences, the last words of the script]
```
- **Never** a long pitch, the "no rush" family (`cta-and-endings.md` §5), a QR walkthrough, or a production label read aloud.

If a future electrical channel has a book or a mid-video CTA, its placement follows plumbing's rule (about a third of the way in, never before the end of item 3, at the end of an item's win), added here with the operator's yes.

## The ending

After the last item or step:
1. **The end CTA:** the one-line subscribe ask, in its markers.
2. **The comment ask, which ends the video:** a short turn to the viewer, an outright ask to leave a comment, one specific question the viewer can answer from their own house (the age of the house, the outlet that gives them grief, what they found behind the plate), and that he reads every comment ("I read every one" or "I read every comment"; operator, 2026-10-27: "we say we read every comment"). Two or three sentences. Never a bare "let me know in the comments", never the same question two videos running, never "let me know if you" (a chatbot leftover the scanner flags). Rotate the question across a channel's scripts among: which outlet or switch gives them grief; what the viewer found behind the plate; the breaker that trips; what their tester or the test button showed; the one thing they'll check tonight (the age of the house is plumbing's question, so use it rarely). Never ask the viewer to tell Frederick something he should know (E04 [4:07]).

No recap, no tease of a future video, no sign-off after the comment line.

## Length

**At least 12 minutes** of narration (this pack raises the core 8-minute minimum), counted at the profile's words per minute (Frederick: 162, so at least 1,950 spoken words; operator 2026-10-29, from his first electrical upload: 3,223 words played in 19:52). **15 to 22 minutes is the sweet spot** (operator, 2026-10-27). Inside that, the value decides.

- **A request to make a finished script longer** ("make it 14-16 minutes") gets one reply: the length comes from the brief, and a longer video needs a fuller brief from ideation. The chat never adds words to a script that passed (operator, 2026-10-25: "tell VAS NOT to ask for length").
- **Never pad.** The same warning said twice, the promise restated, or a step explained twice is padding.
- **If the brief can't fill 12 minutes with real value,** even with the facts guide, the run stops with NOT READY and asks for a fuller brief. The fix belongs at the ideation stage.
- **For calibration:** the 31 models run 5 to 32 minutes; the niche's in-lane videos typically 8 to 17. At 195 words a minute (the figure the pack was built on), 14 of the models would run under 12 minutes even with their demonstrations and CTAs (E01, E05, E09, E10, E15, E19, E21, E22, E26, E29, E32, E33, E34, E37). A script modelled on one of them needs more content than the model, never slower or longer sentences.
- **The length check comes before any prose.** The plan gives each item, step or block its words from what the brief and the facts guide give it: each distinct fact, check, step or slip, said with its reason and its win, carries about 60 to 120 spoken words. If the total is under 12 minutes at the profile's words per minute (Frederick: about 1,950) without any restatement, the run stops with NOT READY and names what the brief is missing (more causes, the warning signs, the related slips, the second method).

## Voice

- **"You" for every instruction; "I" for opinions, preferences and verdicts.** "Kill the breaker, then prove it's dead." "I'd use a lever connector there every time." Contractions, the way people talk, unless the persona profile forbids them.
- **Plain beats clever.** State the fact. At most one picture-phrase per item, only when it teaches.
- **Honest candor.** Say the limits plainly: "A tester can be wrong." "This one's not a homeowner job." Viewers trust the line that says no.
- **Warmth comes from reassurance, not humour.** "You didn't break anything." "That's a five-minute fix." No jokes.
- **Swearing: none** (operator, 2026-10-27).
- **The same example in every video is a tic too.** A channel's old scripts may have leaned on the same examples (Frederick's: the space heater in 17 of 23, a parent's house 17, the ten-year alarm 14, the closed bedroom door 16, the e-bike 15): use one only when the title is about it.
- **A phrase is voice once; in the same slot every video, it's a tic.** Each stock phrase at most once per video (the once-list in the scanner block), and rotate what opens an item and what closes the video.

**Numbers** (core H22, for technical figures: plumbing run 02 carried 25 figures on 11 of 15 items and was hard to follow on one listen):
- **The opening carries one figure at most,** and never item one's.
- **One figure per item or step where you can, two at most,** and only the ones the viewer needs at that step (the breaker size and the wire that goes with it; how far the generator sits from the house). Figures on no more than about half the items.
- **Never three figures in one sentence,** and never a code table read aloud ("fourteen on fifteen, twelve on twenty, ten on thirty" is a table).
- **Check the arithmetic of every pairing and sum** against the brief or the facts guide (fourteen-gauge with a fifteen-amp breaker, twelve-gauge with twenty), and show the math on the evidence block's Numbers line, each figure followed by "= brief" or "= facts guide [row]".
- **A figure said twice adds something new the second time.**

**Written for the voice** (core `workflow.md` §4, every channel). Electrical has more numbers, codes and letters than any other niche, and the briefs write all of them the short way (15 A, 14 AWG, 12-2, NEMA 5-15, L14-30, 120/240 V, NEC 210.8). The narration never does:
- **Volts, amps, watts and wire sizes in words, the way an electrician says them:** "a hundred and twenty volts", "fifteen amps", "a twenty-amp breaker", "fifteen hundred watts" (never 1,500, which the voice reads "one thousand five hundred"), "five milliamps", "sixty hertz", "fourteen-gauge wire". Never 120V, 120 V, 120v, 15A, 1,500W, 5mA, 60Hz, 10kW, 14 AWG or #12. Years stay digits ("the 2023 code"). One form for the whole script.
- **Cable names in words:** "twelve-two cable" (twelve-gauge, two wires plus a ground). Never 12/2 or 12-2.
- **Two numbers joined by a hyphen or a slash, in words:** "a hundred and twenty and two hundred and forty volts", or as electricians say it, "one-twenty, two-forty"; "fifteen to twenty years"; "six-thirty-two screws". Never 120/240, 15-20 or 6-32.
- **Plug, outlet and inlet codes:** name the thing first in plain words, and use the code at most once, only when the viewer needs it at the store, written the way it's said: "the four-prong twist-lock inlet, the kind marked L fourteen-thirty", "a fourteen-fifty outlet", "the everyday three-prong outlet, what the trade calls a five-fifteen", "the twenty-amp kind with the sideways slot, a five-twenty". Never L14-30, 14-50, NEMA 5-15 or 5-20; leave "NEMA" out. Model numbers the same way ("a Wago two-twenty-one"), or leave them out.
- **Letters people say as letters,** with no periods: GFCI, AFCI, UL, EV, LED, CPSC, USB. Say what they mean the first time in one plain clause of your own (`references/facts-guide.md` §14 has one for each, and it's outside the copy guard). Written as words, never letters: carbon monoxide (never CO), the electrical code (never NEC, and never a section number such as 406.4(D)(2)), Romex or "the plastic-jacketed cable" (never NM), gauge (never AWG), air conditioner or alternating current (never AC), "single insulated wires" (never THHN). If the voice test runs a letter set together, it's written with spaces ("G F C I") in every script.
- **Button labels in lower case:** the test button, press reset. Never TEST or RESET.
- **"Live" only before a noun** ("a live wire", "a live outlet"). After a verb ("the fixture stays live") the voice can rhyme it with "give": write "still has power" or "is still hot".
- **Switches, breakers and plugs in words:** a three-way switch, a double-pole breaker, a three-prong plug. Never 3-way or 2-pole.
- **Fractions and measurements in words:** "six inches of wire", "three-quarters of an inch", "two cubic inches". Never 3/4", 6 in. or cu in.

## Proof

The winners are real electricians filming their hands. This channel is an AI presenter who explains. Proof is the kind that survives any footage.

**Use:**
- **The mechanism, in one plain line:** why it happens. "A loose wire touches on a smaller spot, and a smaller spot gets hot." Best under 15 words.
- **A fact from the brief or the facts guide,** said plainly; a named source keeps its figure exactly ("CPSC says…").
- **The maker's own instruction,** when the brief confirms it: "The instructions on the device say to strip it to the gauge on the back."
- **A check the viewer runs at home** with what they'll see either way: the plug-in tester's lights, the test button cutting the power, the tug on a connection. Only safe checks the brief or facts guide confirm; never a finger, never a live test inside a box.
- **The device's instructions and the code decide every step, and the hook never promises what they forbid.** Strip length, the wire count and gauge a connector is rated for, which terminals are line and which load, and box fill come from the brief, the maker's instructions or the facts guide; an opening never promises a shortcut ("no box needed", "no permit") that any of them rules out.
- **The honest limit:** what the fix won't do. "A new outlet won't fix a loose wire further down the line."
- **The typical case, as a general statement:** "Older houses often have outlets wired through the push-in holes."
- **Test topics, explained:** the result the brief gives, said as the fact or the mechanism ("A plug with no holes grips the outlet just as tight: by the time it's all the way in, the holes have already slid past the contacts."), never as something the channel did, never "when people test this" or a named video or creator, and never a result the brief or the facts guide doesn't carry. A demonstration in a model file is never a fact source. A dangerous test is said as its result, never as how it was done (shorting an outlet to find the breaker, touching a live wire, a meter left on amps), with one line on why not to try it.

**Never:**
- **First-person tests, measurements or demonstrations:** "I tested", "I measured", "watch me", "I'll show you on the meter".
- **Anything that needs footage:** "look at this", "as you can see", "right here", "on the left".
- **Job and customer stories, and nameless claimed experience:** "I once found…", "a customer called me…", "after all the houses I've worked in" (operator, 2026-10-27), "the worst panel I've ever opened", "I've seen this a thousand times", "I find it in almost every older house" (even when the title says "I Find"). Say it as the typical case: "a lot of older houses have this".
- **A first-person title** ("…I Find in Almost Every Older House"): the title may say it; the narration says it as the typical case ("the seven you'll find in almost every older house"), never "I find", "I see" or "I've seen". The tenure never props up a finding ("in thirty-five years I've seen…" is a job story); it goes only before a verdict ("Thirty-five years in, I still won't trust a pen tester's silence").
- **Sweeping claims nobody can check:** "this has saved thousands of lives".

## Safety

The facts come from the brief and the facts guide. **The brief can add safety but never remove it** (operator, 2026-10-27).

**Always, in every script that tells the viewer to take off a cover plate, open a box, a fixture or a panel door, or wire anything:**
1. **Power off at the breaker, then prove it's off,** inside the first step that needs it, not as a disclaimer at the top, and before any cover plate, fixture or device comes off: check the tester on an outlet you know is live, test every wire in the box (both halves of a split outlet and every cable in it, not just the one you're working on), then check the tester on the live outlet again (facts guide 8.2, 8.5, 4.27). An outlet that's already dead, a switch turned off, a tripped GFCI or a GFCI's test button never proves the box is dead. A non-contact tester's silence is never proof on its own (8.3): in a metal box or on armored cable, a two-probe tester on the wires (8.4). A plug-in tester is a check, never permission to touch (8.11). Tape over the breaker so nobody flips it back on (8.13).
   **The order at a device, said in this order** (test run 01: a script that followed the line above still had the viewer "test every wire" before any wire was in view, and trusted a plug-in tester that was never seen lit): every tester the proof relies on gets the live check, before and after, not only the first one. A plug-in tester goes into the outlet you'll work on **before** the breaker goes off, so the viewer sees it light, then sees it go dark (in a worn outlet, a tester that won't seat proves nothing; hold it in). The plug-in tester is seen lit in each half before the breaker goes off, then dark in each half after. A two-slot outlet takes no plug-in tester: the non-contact tester at each slot, then the two-probe tester across the slots, read with the power on first (it shows power), then again after the breaker is off (it shows none). The two-probe tester gets its own live check too: it reads power on a working outlet before and after, like any tester (test run 02: the pen tester was checked twice, the two-probe tester never). Then at the box: the plate off; the tester on the terminals you can reach; the mounting screws out and the device eased forward by its strap without touching the wires; then every wire and cable now in view; only then hands near the wires. If any wire still shows power, stop: hands off, find the breaker that feeds it and test again, and if you can't find it, that's a call for an electrician. **Any later re-check** (back from the store, or after the job was left) runs the same order, said briefly: the tester checked live, the plug-in tester dark in both halves, the plate off, the terminals, then the device out and every wire, then the tester checked live again. Never "take the plate off, ease it out, then test" (test run 02). **Any script that opens an existing outlet also says, in one or two lines at the prove-dead step, what to do when the plug-in tester can't be used:** a two-slot outlet, or a worn half that won't hold the tester. The fallback is the two-probe tester across the slots, checked on a working outlet first, showing power before the breaker goes off and none after, then checked on the working outlet again (test run 03 told every viewer to push the plug-in tester in and gave no other way).
2. **How the power comes back, and the test after,** as its own short step said to "you": the breaker back on; the named check and what a good result looks like (the plug-in tester's two lights; the test button cuts the power and reset brings it back); then the problem the viewer came with, tried again; then the win. Never "if you turned it off". **Except after a stop sign:** when the step ends on a call-an-electrician trigger (scorch, melting, a tingle, a burning smell, a hot plate, brittle insulation, aluminum wire), the breaker stays off and the device stays unplugged until a licensed electrician has seen it (facts guide 12.6, 12.13, 13.7). If the new device is a two-prong outlet, the check is the two-probe tester across the slots (power present), then a lamp plugged in and the plug's grip tried.
3. **The call-an-electrician line names its trigger,** in this order: the sign the viewer can see, smell, hear or feel; "that's where you stop"; who does it; why, in one clause. The signs come from the brief or facts guide 12.18 and 9.5: brittle, cracked or scorched insulation; a breaker that trips again the moment it's reset; a warm or buzzing panel, a hot breaker or a burning smell; anything behind the panel's dead front; no free space in the panel or a new circuit; the generator connection itself; wiring that doesn't match what the brief describes. Never the vague "if you're not comfortable".
4. **Panels:** the door is the homeowner's; the dead front, the inner metal cover the breaker handles poke through, is not. With the door open, a homeowner reads the labels, finds the tripped handle and resets it once by pushing it fully off, then on (facts guide 9.6), and looks for rust or water stains, scorch marks, buzzing, heat or a burning smell. Any of those last four means don't touch it, don't reset it, call (9.5). Everything behind the dead front stays live even with the main breaker off (9.4), so taking it off, and adding, swapping or upsizing any breaker (a GFCI or AFCI breaker included), is a licensed electrician's job (13.4). The meter and the wires from the pole belong to the utility (13.5, 9.19); never tell a viewer to pull the meter. In a panel-mistakes list, a fault behind the dead front is said as what an electrician finds when the inner cover comes off, and the item's check is what the viewer can see with the door open or what to ask for. It's never "take the cover off and check yours".
5. **Generators:** the house wiring is fed only through an interlock kit with an outdoor inlet, a transfer switch, or a meter-socket device the utility approves, each put in by a licensed electrician with a permit (facts guide 11.13, 11.14, 11.23). Never a cord with plugs on both ends, never into a wall, dryer or range outlet. Without that equipment, appliances plug straight into the generator with outdoor-rated cords sized for the load (11.18). The generator runs outdoors only, at least twenty feet from doors, windows and vents, as the facts guide gives it; the carbon monoxide sequence (below) is said in full whenever a generator runs in the script. If neither the brief nor the facts guide gives the storm-night order (main off, then the generator side, loads one at a time, and the way back), the script says the order is printed in the kit's instructions and the electrician walks you through it at install, and gives no order of its own.
6. **Old wiring:** in any script that swaps a device, splices or pigtails, one line for houses wired from about 1965 to the mid-1970s: wire that's dull silver instead of copper, or cable printed "AL" or "ALUMINUM", is aluminum, and that's a stop. Aluminum repairs are a licensed electrician's job (facts guide 7.5, 7.7, 7.9, 3.16, 3.17). Never an ordinary outlet or switch, a push-in hole, a copper-only lever connector or an ordinary wire nut on aluminum. Cloth-covered, brittle or cracked insulation is a stop too (13.7); knob-and-tube isn't dangerous just for being old (7.2): the line is "have it checked", never a scare, and the homeowner never reworks it (7.1 to 7.4). Never say either kind of wiring "is illegal" or "has to be torn out" (facts guide §7).
7. **Parts and methods:** only connectors and devices listed for house wiring go in a house box (facts guide 3.14, 3.15): never a solder-seal or heat-shrink butt connector, never twisted wires and tape, never a splice outside a box. A breaker or fuse is never made bigger to stop it tripping: it protects the wire (1.2 to 1.4, 7.13). Indoor cable (NM, Romex) never goes outdoors, underground or into outdoor conduit (2.14). A box with no ground wire takes only what 4.15 lists; a GFCI there protects people but adds no ground (4.17). Where the plug-in tester is the check on a box with no ground wire, the script says what it will show (an open ground, explained as "no ground wire connected", is expected there; the missing wire causes that reading, never the GFCI) and that the GFCI's own TEST button is the test; never a jumper to the ground screw (7.11). A product made for cars, boats or low-voltage lighting is named as that, and never shown or said as the fix for house wiring. Never a burial depth from memory: an outdoor or underground run is a permit job where the inspector sets the depth, and any script that has the viewer dig says to call 811 first (once the brief or the facts guide carries it; otherwise NOT READY on that line).
8. **Permits and local rules:** where the brief or facts guide says a job needs one, say so in one line ("Check with your local building department first").

**Emergency sequences get every step, whatever the brief leaves out** (the gas-leak lesson from plumbing run 02), in the script's own words, whenever the script mentions the situation, even in passing. First-aid steps are said exactly as the facts guide gives them, never expanded into treatment or reassurance ("they'll be fine"):
- **Someone being shocked** (facts guide 12.8 to 12.11): don't touch them while they're in contact, the current can pass into you; cut the power (unplug it, or switch off the breaker or pull the fuse); if you can't, push the source away with something dry that doesn't conduct (wood, plastic, cardboard); call 911 for anyone hurt by electricity, and at once if they have burns, confusion, trouble breathing, an irregular heartbeat, muscle pain or spasms, a seizure, or passed out even briefly; CPR if they aren't breathing or have no pulse; a doctor even when they seem fine. Near a power line, stay back and call 911 (12.12).
- **An outlet or switch that's hot, uncomfortable to touch or discolored** (12.13): stop using it now, unplug what's in it, and get a licensed electrician soon.
- **A burning or rubbery smell, sparks, buzzing or crackling** at an outlet, switch or appliance (12.14): unplug it or stop using it, switch that circuit off at the breaker if you can do it safely, and call a licensed electrician. If the smell, heat or buzz is at the panel itself, don't touch the panel (9.5).
- **Smoke or flames** (12.15): get everyone out, stay out, and call 911 from outside. Never water on an electrical fire. Nobody goes to the panel through smoke.
- **A downed power line** (12.12): assume it's live; stay at least thirty-five feet away, and away from anything it touches (a fence, a puddle); call 911 or the utility; never touch a person or a car that's in contact with it; in a car it falls on, stay inside.
- **Carbon monoxide, whenever a generator runs in the script** (11.1 to 11.7): outdoors only, at least twenty feet from doors, windows and vents; never in the house, garage, basement, crawl space or shed, even with the doors open; you can't see or smell it; dizzy, weak or sick near a running generator means fresh air now, then 911; battery or battery-backup CO alarms on every level.
- **Backfeeding, whenever it's named** (11.8 to 11.12): it can electrocute line crews and neighbors on the same transformer; a cord with a plug on both ends has live, bare prongs; the only safe ways to feed the house are in rule 5.
Never "pull them off the wire", "throw water on it" or "turn the main off and backfeed carefully".

**How safety sounds:** one short line inside the step where the risk is, with the reason, in proportion. Vague danger reads as a scare tactic; a plain reason reads as care. No aside, opinion or detour while the viewer has a box or a panel open: the steps from power off to the test after run straight through; the verdict comes after the win.

**What the visuals will draw.** The footage is generated from the narration, so every risky line is written as a safe picture:
- Never narrate an unsafe step: no hands in a live box or panel, no testing by touch, no "it's only 120 volts".
- In each step, the verify-dead line comes before any line that puts hands at wires. A line that says a wire is still live has no hand, finger or tool in it ("the tester lights up at that wire", never "reach in and feel it").
- The inside of a panel is what the electrician sees with the inner cover off, never with a hand or tool in it.
- A mistake is named as what's found (the cord with a plug on both ends, the wire pushed into the hole on the back), never as steps someone could follow.

## Banned in these scripts

**Never:**
- **A name or channel intro,** a greeting, "today we're going to", or "this channel is for…" (Frederick's old scripts opened with his name in all 23).
- **Vague teases:** "stay till the end", "stick with me", "you won't believe" and the rest of the core hard-ban list. "By the end of this video you'll know…" is allowed only as the opening's one value promise (P11).
- **A run-down of the first items in order** in the opening (P10's lesson).
- **A recap anywhere** (core B9), including a closing "so, ranked…" or a run-down of every contender.
- **First-person tests, measurements and demonstrations; pointing at the screen; job and customer stories; anyone's motives.**
- **Money:** prices, savings, "save hundreds", the bill (operator, 2026-10-24).
- **Electricians, inspectors, firefighters or the utility as the villain;** "electricians hate", "what they don't want you to know".
- **An old channel template:** the long CTA and the "no rush" family (each channel's own old lines are banned in its persona profile).
- **Edit notes, cues, labels or directions** of any kind.
- **Hype that gets mocked:** "horror movie", "brutal tests", and any "every", "never" or "forever" the script then walks back.
- **Copying 8 or more words in a row** from a reference file.

**At most once per video:** the phrases in the scanner block's `once` lines.

## Scanner rules for this niche

The scanner (core `script-scanner.py`) reads this block. `allow` lines are wording these rules require; `lift` removes one core hard ban for this pack only (P11); `ban` lines are fix-on-sight; `once` lines fail on the second use.

```scanner
min-minutes: 12
first-item-seconds: 45
example-guard: 5
lift: tease: by the end of this video
allow: by the end of this video you'll know
once-regex: \bby the end of (?:this|the) video\b | the opening's value promise (P11: once, in the opening)
allow: I read every one
allow: I read every comment
ban-regex: \btoday,? (?:we'?re|we are|I'?m|I am) going to\b | opening: "today we're going to"
ban-regex: \bI(?:'ve| have)? (?:tested|tried|measured|ran (?:a |the |some |my )?tests?)\b | first-person test claim
ban-regex: \bmy (?:own )?(?:test|tests|testing|results|meter reading)\b | first-person test claim
ban-regex: \b(?:watch|let) me show you\b|\bwatch me\b|\bI'?ll show you on (?:the|my) meter\b | first-person demonstration
ban-regex: \bwe(?:'ve| have)? (?:tested|tried|measured|ran (?:a |the |some )?tests?)\b|\bour (?:own )?(?:test|tests|testing|results)\b | first-person test claim
ban-regex: \bI (?:put|held|hooked up|clamped|stuck|ran) (?:a |my |the )?(?:meter|multimeter|tester|probes?|thermal camera|clamp meter|heat gun)\b | first-person measurement
ban: as you can see | pointing at the screen
ban-regex: \blook at this\b|\bright here\b|\bon the (?:left|right) (?:side )?of (?:the|your) screen\b | pointing at the screen
ban-regex: \b(?:after|in) all the (?:houses|homes|jobs|panels) I'?ve (?:worked|been|seen|wired)\b|\bI once (?:found|had|saw|walked)\b|\ba customer (?:of mine|called|asked)\b|\bon a job (?:once|last)\b | job or customer story
ban-regex: \belectricians? (?:hate|don'?t want)\b|\bwhat (?:they|electricians|the electrician|inspectors|contractors|the pros) (?:won'?t|don'?t) (?:tell you|want you to know)\b | trade as villain
ban-regex: \$\s?\d|\b(?:dollars?|bucks|cents)\b|\bsave (?:you )?(?:hundreds|thousands|money)\b|\b(?:electric|electricity|power|energy|utility) bills?\b | money (no money framing on this channel)
ban-regex: \bthis channel (?:is for|exists|is all about)\b | template stock line: channel promise
ban-regex: \bno rush\b|\bno pressure\b|\bwhenever you'?re ready\b | CTA "no rush" family
ban: horror movie | hype that got mocked
ban-regex: \bbrutal tests?\b | hype that got mocked
ban-regex: \b(?:it'?s|that'?s|it is|that is) (?:only|just) (?:a hundred and twenty|one hundred (?:and )?twenty|120|one-twenty|household|house)(?: volts?| current| power)?\b|\b(?:it|that|this|a hundred and twenty|120|one-twenty)(?: volts)? won'?t kill you\b | unsafe line
ban-regex: \b\d(?:[\d,]*\d)?(?:\.\d+)?(?:\s?(?:(?-i:VAC|VDC|VA|V|A|W|mA|Ah)|kWh?|Hz)|(?-i:v|a|w|ma))\b | unit written as a symbol (write the word: 'fifteen amps')
ban-regex: \b\d+\s?AWG\b|\bAWG\s?\d|#\s?\d{1,2}\b | wire gauge written as a code (write 'fourteen-gauge')
ban-regex: \b\d+(?:-\d+)+\b | numbers joined by a hyphen (12-2, 14-3, 5-15, 6-32, 15-20): write them as said ('twelve-two cable', 'a five-fifteen outlet', 'fifteen to twenty years')
ban-regex: \b\d{3}/\d{3}\b | voltage pair with a slash (write 'a hundred and twenty and two hundred and forty volts', or 'one-twenty, two-forty')
ban-regex: \b[1-4]/0\b | aught wire size with a slash (write 'four-aught')
ban-regex: (?-i:\bCO\b) | 'CO' (write 'carbon monoxide')
ban-regex: \bcu\.?\s?in\b | 'cu in' (write 'cubic inches')
ban-regex: \b[2-4]-(?:way|pole|prong|gang)\b | write it in words ('a three-way switch', 'a double-pole breaker', 'a three-prong plug')
ban-regex: (?:^|(?<=[.!?]\s))(?:hey|hi|hello|howdy)(?: there| folks| everyone| friends| guys)?\b|\bwelcome (?:back|to (?:the|my|this) channel)\b | greeting
ban-regex: \bask me how I know\b | implied job story
ban-regex: \blook at (?:that|the|this|those|these) [\w ]{0,30}?(?:on the (?:left|right)|for a (?:second|moment))\b | pointing at the screen
ban-regex: \btoday,? (?:I'?m|I am|we'?re|we are) (?:giving|showing|covering|walking|taking|sharing)\b | opening: "today I'm giving you"
ban-regex: \b(?:I|we) (?:put|ran) (?:all |each |every )?(?:\w+ ){0,3}(?:through|to) (?:\w+ ){0,2}tests?\b | first-person test claim
ban-regex: \bI'?ve seen (?:this|that|it)\b[^.!?]{0,40}\b(?:times|more than|than any|so often)\b|\bI had a (?:homeowner|customer|client|neighbou?r)\b | job story or nameless claimed experience
ban-regex: \bhold on(?:to)? that\b|\bwe'?ll get there\b | old tease: "Hold onto that. We'll get there."
ban-regex: \b(?:it|that|this|they|the breaker|the outlet|your plugs?)(?:'ll| will) never (?:trip|fail|spark|burn|overheat|come loose|fall out|happen)(?: again)?\b|\bno more (?:fire|shock) risk\b|\b(?:fire|shock)[- ]proof\b | guaranteed outcome (claims policy)
ban-regex: \b(?:to (?:sum|wrap) (?:it |this )?up|to recap|let'?s recap|quick recap|in summary|so,? ranked)\b | recap (core B9: none anywhere)
ban-regex: \bfirst,? (?:I'?ll|we'?ll) (?:show|tell|cover|look at)\b[^.!?]{0,80}\bthen\b | a run-down of the items in order (P10)
once-regex: \byou'?d (?:think|figure)\b | belief-namer "you'd think / you'd figure" (rotate it)
once: in your pocket
ban-regex: \b(?:14|12|10|8|6)/[234]\b | cable name with a slash (write 'twelve-two cable')
ban-regex: \bNEC\s?\d|\b\d{3}\.\d{1,3}\b | code section read as a number (say 'the electrical code')
once: between you and me
once-regex: \bhere(?:'?s| is) the (?:part|thing) (?:people skip|nobody tells you)\b | here's the part nobody tells you
once-regex: \bI(?:'?ll| will) be (?:straight|square|honest) with you\b | I'll be straight with you
once-regex: \bthat(?:'?s| is) the whole (?:trick|job|game)\b | that's the whole trick
once-regex: \bwhich brings us\b | which brings us
once-regex: \bhold that thought\b|\bput a pin in\b | hold that thought
once: the big one
once-regex: \bquick (?:thing|pause|one)\b | quick thing
once: no shame in
once: full stop
once: trust me
once-regex: \b(?:nine|9) (?:times )?out of (?:10|ten)\b | nine times out of ten
once-regex: \bfive-minute fix\b | a five-minute fix (this pack's own example)
once: you didn't break anything
once-regex: \bI'?d replace (?:that|this|it)(?: one)? today\b | I'd replace that one today (this pack's own example)
once-regex: \bplease,? test it\b | the insistence line
once-regex: \bthat'?s a call\b | that's a call
ban-regex: \bkill(?:s|ing)? (?:you in your sleep|your (?:whole )?family|everyone)\b|\bburn(?:s|ed|ing)? (?:your|the|a) (?:house|home) (?:down|to the ground)\b|\bdeath ?traps?\b | scare-reel line (fire is the stakes, never the topic)
once-regex: \bwhile you(?:'re)? (?:sleep|sleeping)\b | Frederick's old fire-channel tic: while you sleep
once-regex: \btrapped heat\b | Frederick's old fire-channel tic: trapped heat
once-regex: \bso what do you do instead\b | the item shape's turn question (word it fresh each time)
```

## Before handing over

Check that:
- the point comes in the first sentence, with the problem the viewer has and the fix or answer named by about 15 seconds
- one job per step (a step that holds two jobs is split); the buying step covers each case the look inside can turn up (1.18, 4.30, 1.17a, 6.19a)
- the opening follows the video type's order, with at most one value promise that never runs down the first items in order, and no intro, greeting, vague tease or recap
- every item or step puts the viewer in the scene, aims at one feeling, has at least one "but" turn and ends on a win; bridges turn between items; a question about every two items; the title's feeling and key word come back every few items; an "I" verdict in most items and one insistence line; capability balances every fear line; the last item closes on relief
- items follow the item shape (lists), the step shape (how-to) or the rung shape (fix), each at the words the plan's length estimate gave it, item one by about 30 seconds in lists, and no more than two in a row without a forward line (an item's own stake line doesn't count)
- every list item carries one stake, once, in proportion; how-to and fix steps carry one only where the risk is; fire is never the topic; fire words about twice per 1,000 at most; death words only where real, at most twice; no prices, savings or money words anywhere
- the spine feeling comes back at nearly every item; "you", "but", questions and "I" meet the targets in "Emotion"; danger enters where it's real and is answered within a sentence or two
- the villain, if any, is the old work or the cheap part, never electricians, inspectors, firefighters or the utility; named panels only with sourced facts
- every forward line is paid within about five minutes; no stretch runs past five minutes without a forward line or a payoff; every callback matches a real promise
- the tenure appears at most once, as 35 or the title's number; no job or customer story; no "I tested", no pointing
- in any outlet script, the fallback when the plug-in tester can't be used (two slots, or a half that won't hold it) is said at the prove-dead step; any later re-check runs the same order
- the buying step answers every rule it raises with what to buy (or what to ask for); wherever the script offers a GFCI, the wiring step says the incoming power goes on the line screws, never "the same spot as the old outlet"
- safety: power off and prove it (live, every wire, live again) in the first step that needs it; how the power comes back and the test after, or the breaker left off after a stop sign; the call-an-electrician trigger named; the viewer's part kept apart from the electrician's (nothing behind the dead front, no breaker swaps, no generator hookup or aluminum repair as the viewer's steps); the old-wiring line in any device swap or splice; only listed parts in a house box, never a bigger breaker, no NM outdoors; panels and generators as set out above; every emergency sequence complete; no line that draws hands in a live box or panel, and no wrong way taught as steps; the brief added safety, never removed it
- no first-person test or measurement; no job story or claimed experience ("I find", "I've seen", "I've pulled"); a first-person title said as the typical case; an absolute title delivered as its strongest true version, never as a guarantee and never walked back
- every code rule, size, distance and danger figure traces to the brief or the facts guide; settings from everyday knowledge are marked "general knowledge"
- every unit, wire size and number is written for the voice; every term on the list is explained the first time
- the CTA follows the persona profile: no mid-video CTA, the one-line subscribe ask alone inside its NO BOOK markers; the comment ask after ===END CTA===, ending the script
- the video ends on the comment ask, with nothing after it
- each once-phrase appears at most once; the opening shape, stake device and comment question differ from the rotation log
- the plan names its models with at least three differences, and no model was used in the channel's last five scripts
- at most one figure in the opening (never item one's), one or two per item, figures on about half the items, never three in a sentence; every pairing and sum checked
- the script runs at least 12 minutes at the profile's words per minute (15 to 22 is the sweet spot), with nothing padded
