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
| `references/models/INDEX.md` | The model library: 31 winning videos from real channels with 1M+ views, mostly 2022 on, sorted by video type. Each file has a beat map, how the video voices each emotion, why it works, the full labelled script and what doesn't transfer. Read at the planning step only. |

Every reference file, and this file itself, is under the copy guard: the scanner flags any run of 8 or more words shared with it. The example lines in these rules show a shape; the script never reuses their wording. None of them is taken from a model.

## Where this pack overrides the core

The core base rules apply wherever this pack is silent. These are the places it changes them, each one approved by the operator. Everything else in the core stands.

| Core rule | What this pack does instead | Decided |
|---|---|---|
| `workflow.md` §2, the default inputs | The `inputs` block below: the title, the brief and the rotation log. The research pack is `not used`: the brief is the fact source, with `references/facts-guide.md` behind it. | 2026-10-27 (default, as plumbing) |
| `retention-mechanics.md` §2 and §6, the value line and "short range only"; the hard-banned "by the end of this video" | The opening may carry one value promise (job 5 of "The opening"): an escalation, or what the viewer will know or be able to do by the end, naming things paid later, never the first items in order. Concrete named forward lines are allowed in the body. Vague teases stay hard-banned. The scanner lifts only "by the end of this video". | P11, operator 2026-10-27 |
| `cta-and-endings.md` §4, `workflow.md` §4 ("the closing line is exactly one sentence"), `retention-mechanics.md` §14, `greenlight-audit.md` F3, `variety-rotation.md` slot 9 | The ending is the one-line subscribe ask, then the comment ask (a turn to the viewer, an outright ask to comment, a specific question and "I read every one"), which ends the script. Two or three sentences; nothing after it. FORMAT CHECK's closing field reads `[comment line, last line of the script]`; rotation slot 9 rotates the comment question. | 2026-10-27 (default, as plumbing's P5) |
| `workflow.md` §3, the 8-minute minimum; `greenlight-audit.md` F2 | At least 12 minutes at the profile's words per minute; 15 to 22 is the sweet spot. See "Length". | Operator 2026-10-27: "even 15-22 is sweet spot" |
| `variety-rotation.md`, the rotation log line | Four more fields at the end of the line: `\| model: [file numbers] \| stakes: [device] \| promises: [devices] \| comment: "[the comment question]"`. | 2026-10-27 (as plumbing) |
| `workflow.md` §3 step 4 and `greenlight-audit.md` D3, the `--refs` files | The copy guard runs against this file, `references/excerpts.md`, `references/voice-samples.md`, `references/facts-guide.md` and every file in `references/models/`, plus the persona profile. | 2026-10-27 (as plumbing) |
| `research-and-sourcing.md` §6, "each number said alongside whoever counted it" | Sources don't have to be said. A source is named only where it really helps (CPSC, the electrical code); when it is named, its figure is said exactly as the source gives it. | 2026-10-27 (as plumbing) |
| `greenlight-audit.md` E1, the originality score | Signal 1 counts facts from the brief or the facts guide that most videos on the topic don't use; signal 4 (three named sources) doesn't apply. Out of 6, passes at 4. | 2026-10-27 (as plumbing) |
| `retention-mechanics.md` §6 and `greenlight-audit.md` B5, signposts | The sections are the opening, each item, step or contender, and the ending. "Number four." or "Step three." is the signpost. | 2026-10-27 (as plumbing) |
| `greenlight-audit.md` D4, "every number traces to the fact source" | The fact source is the brief plus `references/facts-guide.md`. A number from neither (a setting, an interval) is allowed only when it is everyday knowledge and is marked "general knowledge" on the evidence block's Numbers line. No code number, wire size, breaker size or distance is ever filled in from memory. | 2026-10-27 (P7 adapted) |
| `retention-mechanics.md` §2, the hook; `greenlight-audit.md` A1b | The electrical opening is the hook (see "The opening"), checked as the same three jobs: the transformation is the fix or answer named in the first sentence; the pain or wish is the problem the viewer has right now; the curiosity is the question, or the surprising fact the video answers. | 2026-10-27 (as plumbing) |
| `humanizer.md` H22 and `greenlight-audit.md` C2, prices | Not used: this channel says no prices at all (operator 2026-10-24: "we dont really need to use money in electrical"). | 2026-10-24 |

## Inputs

Electrical scripts are written from the title and the brief; there is no research pack. The workflow reads this block at START and won't write until every required input passes.

```inputs
- title | required | the locked title, exactly as approved
- brief | required | the ideation brief for this title; the script's facts, steps, code rules and safety lines come from it first
- research-pack | not used | electrical scripts are written from the brief and the pack's facts guide
- rotation-log | required | the channel's last five ROTATION LOG ENTRY lines (from the earlier scripts in this chat, or pasted), or "none" for a new channel
```

- **The brief is the fact source,** with the facts guide behind it. The brief wins on facts; it never wins on removing safety (see "Safety").
- **Where the brief is silent, the script fills in** (P7, adapted):
  - **Code rules, sizes, distances and safety facts** come from `references/facts-guide.md` only, said plainly. A row marked "reading" is never said as fact.
  - **Everyday settings and intervals** (press TEST once a month, a tester checked on a live outlet first) may come from everyday knowledge, marked "general knowledge".
  - **No wiring method, code claim or "this is legal for you to do" beyond the brief and the facts guide.** When neither says it, the script says it's a question for the local inspector or a licensed electrician.
  - The run stops with NOT READY when the brief can't carry the title's main promise, or a safety fact the script needs is in neither the brief nor the facts guide.

## The viewer

The viewer is a 50+ American homeowner, often in an older house, who would rather understand and fix it than wait for someone, but who is a little afraid of electricity, and right to be. They come from search as often as from the feed: they have a dead outlet, a breaker that trips, a plug that falls out, a light that glows when it's off, and they typed the problem in. Under the click sits one question: "Can I handle this safely, or is this a call?"

**What they bring (from the electrical study and the model comments):**
- **A problem in front of them right now.** The best openings name it the way they'd say it ("the outlet that just quit", "the plug that won't stay put").
- **A real fear of getting it wrong,** and a real pride in getting it right. Pride led about 46% of the niche's titles (462 of 1,007); safety fear was common but rarely led. The viewer leaves feeling able, not scared.
- **Trust in electricians, inspectors and firefighters.** They treat them as the experts. "Electricians HATE This" titles flopped (31K and 375 views). Never set them up as the enemy.
- **Impatience with the wait.** The most-liked praise on how-to winners is the pace: no intro, straight to it.
- **The doing questions:** which wire is hot, what size breaker, do I need a GFCI here, will this pass inspection, is my tester lying. Answer the ones that apply inside the script, at the step where they'd ask.
- **What they thank:** the answer fast, the reason why, steps clear enough to try, the check that tells them it's right, and an honest "this one's a call".

**Skill level:**
- Write for beginners to handy homeowners, in plain words.
- **These terms are always explained the first time,** in one plain clause, then used plainly: GFCI, AFCI, hot, neutral, ground, breaker, panel, circuit, amp, volt, watt, backstab (push-in), pigtail, wire nut, lever connector, gauge, box fill, double tap, interlock, transfer switch, inlet, backfeed, tamper-resistant, non-contact tester, multimeter, Romex (NM cable), conduit. Any other trade word gets the same treatment (`references/facts-guide.md` §14 holds a plain explanation for each).
- Give the reason behind a step in one sentence. Don't lecture on theory the step doesn't need.
- Never explain what everyone knows (flipping a switch, plugging in a lamp).

**The standard kit:** assume a screwdriver set, pliers, a flashlight, electrical tape and a non-contact voltage tester (or say once that one is worth owning). Anything beyond that (a plug-in outlet tester, a multimeter, wire strippers with a gauge, lever connectors, a fish tape, a stud finder) is named with what it does, never its price.

---

## The stakes (no money)

This channel says no prices and no savings (operator, 2026-10-24). Where plumbing put a price line, every item here carries **one stake line**: what it risks, once, in plain words. Rotate the stake devices across a channel's scripts (the rotation log's `stakes:` field):

- **Fire,** plainly and briefly: heat at a loose connection, arcing behind the plate, the scorch mark nobody sees. Said once where it belongs, never as a scare reel.
- **Shock:** the live metal, the wire that's still hot when the switch is off, the tester that gave a false "dead".
- **The hidden bad work in the wall:** what the last owner or handyman left behind.
- **The cheap part:** the knock-off connector, the bargain tester, the device that's never been listed.
- **"You've been doing it wrong":** the habit almost everyone has, and why it matters.
- **The nuisance that won't stop:** the breaker that trips every night, the flicker, the outlet that works when it feels like it.
- **The inspector and the sale of the house:** work that won't pass, said as a fact, never as a threat.

**Rules:**
- **In proportion.** One stake per item, said once, then the fix. "That's how a loose wire turns into heat inside the wall" lands; piling fire, death and lawsuits into one item reads as a scare tactic.
- **Fire is the stakes, never the topic** (operator, 2026-10-26). No item exists only to frighten.
- **The worst case only when it's real and common enough to matter,** with the fix right after it.
- **Numbers on danger** (how little current is dangerous, how far a generator sits from the house) come from the brief or the facts guide, and named sources keep their figures exactly.

## The villain (optional)

The operator (2026-10-27): "villain does not need to be necessary". Most winning electrical videos (70-80%) have none. Use one only where the topic carries it:
- **The last owner's or handyman's wiring,** found in the box or the panel: "Whoever wired this was in a hurry."
- **The cheap product:** the unlisted part, the knock-off connector, the cord that should never have been sold.
- **Named problem panels** (Federal Pacific Stab-Lok, Zinsco) only with what CPSC or inspectors actually say, from the brief or the facts guide (operator, 2026-10-27); otherwise "some older panel brands".

**Never** electricians, inspectors, firefighters or the utility as the enemy, never a motive, never a named company called dangerous beyond its sourced facts. The narrator's reaction is aimed at the work or the part ("That's the kind of connection that keeps me up at night"), never at a person.

## The opening

Every opening, whatever the video type, does these jobs in about the first 45 seconds. Rotate the order and shape across a channel's scripts (the rotation log tracks it), use the order for the video type (see "The video types"), or model it on a model file's beats, never its wording. What can't change: the point comes first and fast, and nothing on the banned list appears.

1. **The point in the first sentence:** the problem the viewer has right now, and wherever the title allows, the fix or the answer itself, by about 15 seconds. Never hold the answer back to the middle.
2. **A question, when it fits,** that the viewer can answer in their own house ("Does the plug sag the moment you let go?"), answered within about 15 seconds.
3. **The stake, once,** in plain words (see "The stakes"), and the villain line only if the topic has one.
4. **Honest scope or reassurance,** in one line: what this fixes and what it doesn't, or that most of the job is safe for a careful homeowner and which part isn't. It never takes back the title.
5. **One value promise, when it fits** (P11, operator 2026-10-27): one sentence that either promises the escalation ("we'll go from the two-minute check to the one sign that means you stop and call") or what the viewer will know or be able to do by the end ("By the end of this video you'll know why it trips and how to tell a tired breaker from a real fault"). It names things paid later in the video, never the first items in order (no "First I'll show you… then…"), and it isn't always three things. Never a vague tease ("stick around", "you won't believe"). Or, in a list, **the count line** naming the whole list and what it does for the viewer. Never "today we're going to".
6. **The first real tip, check or step** by about 45 seconds; in a list, item one by about 30 seconds.

**Simpler and stronger** (operator, 2026-10-21, for every niche): the first line hits the viewer's own problem in strong, plain words; it doesn't have to be the worst case.

**Never in an opening:** a name or channel intro, a greeting, "today we're going to", a run-down of the first items in order, a first-person test or demonstration ("I tested", "watch me"), or a tenure number other than the profile's or the locked title's.

**Tenure:** at most once in the video, as the profile's fixed number (Frederick 35) or the locked title's, and only where it does a job (credibility right before a verdict or a mistakes list).

## Emotion, all the way through

The operator (2026-10-21): "simpler and stronger on emotions... using strong words and targetting the exact pain points of this audience like reference scripts do. more work on emotion triggering throughout." The plumbing tests showed what happens without it: the pain named once, then explanation; "you" 21 per 1,000 words against 41 in the hit; "but" once per 1,000; no questions; 11 of 15 items ending on an instruction. The electrical winners run on **pride and capability first**, with safety fear, "you've been doing it wrong", myth-busting, how-it-works curiosity and the nuisance underneath (each model file's "Emotion voicing" shows the words they use).

1. **Put the viewer in it.** Say "you" and open each item or step on what they see, hear, smell or feel in their own house: the flicker, the buzz, the warm cover plate, the plug that droops, the faint smell near the panel. Not on how the thing works.
2. **Aim at one real feeling per item:** the fear of getting shocked or starting something in the wall; the frustration of the problem that keeps coming back; the worry about what the last owner did; the doubt about their own tester; the pride of getting it right; the relief that it's a simple fix.
3. **Strong, plain words.** Physical verbs and pictures: loose, scorched, buzzing, arcing, sagging, cooked, brittle, "live", "still hot". Short sentences mostly; join two with "but" to keep it moving. At most one picture-phrase per item, only when it teaches.
4. **"But", inside items and between them.** Inside every item, at least one turn: what people think or do, then "but", then the truth. Between items, bridges that turn ("That one's a five-minute fix. The next one isn't."). Rotate how the belief is named ("most folks figure", "the package says", "you've probably been told"); "Most people…" opens a sentence at most once per script (`humanizer.md` H20), and never the "it's not X, it's Y" reframe more than once (H21).
5. **Ask the viewer** a question they can answer about their own house, answered straight away, about every two items or steps.
6. **Sensory warning signs** where plumbing used disgust: the brown mark on the plate, the smell like hot plastic, the crackle when the plug moves, the warm switch. Said as what to notice, never as horror.
7. **End every item or step on a win:** relief, pride, or the before-and-after ("Now that plug clicks in and stays."). Never end on an instruction.
8. **Reaffirm the title's feeling and key word** every few items, in nouns and verbs (the mistake, the real reason, the safe way), not "-ly" adverbs; not every item, never robotic.
9. **Let the narrator speak.** One short "I" opinion or verdict in most items ("I'd replace that one today."), and once per video a line of insistence where it matters ("Please, test it first. Every time.").
10. **Capability over fear.** For every fear line, a line that puts control back in the viewer's hands: the check they can run, the sign that it's fine, the point where they stop.
11. **Finish on relief and capability, not danger.** The last item before the ending closes on reassurance or something to do tonight.

**Never, still:** invented facts or events, guaranteed outcomes ("this will never happen again"), anyone's motives, vague teases, scare-reel lines ("this could kill your whole family tonight"), worst-case exaggeration, jokes.

## Point then promise

- **Point first.** The first answer (the cause named, the rule stated, the first step) comes before anything else.
- **Pay forward lines fast.** A later item named in a forward line is paid within about five minutes; the opening's value promise is paid inside the video.
- **Keep one promise open.** After the opening, never more than about five minutes without a new forward line or a payoff: a line that names the next value ("The next one is why your tester sometimes lies."), a question the next item answers, or a check the viewer can run.
- **Every callback has a promise.** "Like I said" or "I promised" must match something the script really said earlier.
- **A priority flag at the first answer,** in fresh words each time ("If you only check one thing tonight, check this.").
- **No recaps** at the end.

## Ways to promise more value

Two or three per video, in the body (the opening carries at most the one value promise), rotated across a channel's scripts:
- **A numbered item with its stake in words:** "Number six is the one that leaves the light fixture live when the switch is off."
- **The escalation ladder:** the two-minute check, then the fix a careful homeowner can do, then the sign that it's a call for a licensed electrician. The default for fix videos.
- **The rule that protects everything:** turn it off, then prove it's off. Named at the first step it touches, paid straight after.
- **A check the viewer can run:** the plug-in tester's lights, the TEST button, the tug test on a connection, the warm-plate check with the back of a hand. Only checks that are safe and that the brief or facts guide confirm.
- **A problem the viewer didn't know they had,** promised and then shown.
- **A myth flag** that names the belief it flips in the same line: "Number three is the one everybody gets backwards: a three-prong outlet doesn't mean you have a ground." Never a bare "the one everybody gets backwards".
- **The "why" promised:** "And I'll tell you why that wire got short in the first place."

## The video types

Pick the type from the title. Each type has its own opening order and item or step shape. The models column names the model IDs in `references/models/` (all real channels: structure and voice, never wording); `references/models/INDEX.md` lists every file. Follow "Using the models".

| Type | Title shape | Opening, in order | First tip by | Item or step shape | Models |
|---|---|---|---|---|---|
| **How-to / correct way** | "How to [do the job] (the Safe Way)", "The RIGHT Way to…" | The job and the problem it solves → "you can do this" with the one part that's a call → the value promise or the step count → power off and prove it, named as the rule that protects everything | 30-45 s | The step, the reason, the mistake to avoid, how to know it's right | E01, E02, E03, E04, E05, E07 |
| **Fix this problem** | "The REAL Reason Your…", "Why Does My X Keep Y?", "Plug Won't Stay In?" | The symptom in the viewer's words → the usual wrong guess → the real cause in one line → is it dangerous (honest, in proportion) → the fix ladder | 20-40 s | The check, what it tells you, the fix, the sign it's a call | E08, E09, E10, E11, E12 |
| **Explainer** | "What X Actually Does", "Why Do Plugs Have Holes?", the test topics explained | The question everyone's wondered → the common wrong answer → the real answer in one line → what it means in your house → the value promise | 20-40 s | The idea, the plain picture that explains it, what it means for you | E13, E14, E15, E16, E17, E18, E19 |
| **X vs Y** | "AFCI vs GFCI", "Wire Nut vs Lever Connector: Which One?" | The moment of choice in the viewer's house → the two contenders in a line each → the argument everyone has → "each one has a job" → the value promise | 30-45 s | Each contender: what it does, where it's right, where it's wrong; then which to use where | E20, E21, E22, E23 |
| **Mistakes list** | "N Wiring Mistakes…", "N Breaker Box Mistakes…" | The symptom or the hidden work → the stake → one credibility line (tenure here if anywhere) → the count line | 15-30 s | The mistake, what it risks, the right way, the check | E24, E25, E26, E27 |
| **Single big mistake** | "The Generator Mistake That…", "The Dead Outlet Mistake Everyone Makes" | The mistake named in the first sentence → why almost everyone makes it → the stake in plain words → the value promise | 20-40 s | One mistake explored: how it happens, what it does, the right way, the check, the related slips | E29, E30, E31, E32 |
| **Know-this list** | "N Electrical Things Every Homeowner Should Know" | The moment the viewer wished they'd known → the stake → the count line | 15-30 s | The thing, why it matters in your house, what to do with it, the win | E28; E24 and E25 for list pacing |

A title that promises tests or demonstrations is written as explanation and results from the brief, never as "I tested" (see "Proof").

### The item shape in lists

In every list type (mistakes, single big mistake's related slips, know-this), each item runs in this order:
1. the scene in the viewer's house
2. what's really happening in the wall, the box or the device (one or two lines)
3. what it risks, once (see "The stakes")
4. the turn ("So what do you do instead?")
5. the right way, cut to what the viewer needs, with the safety line inside the step where the risk is
6. the check that tells them it's right, when there is one
7. the win

### The step shape in how-to and fix videos

1. what to do, as an instruction to the viewer
2. the reason, in one sentence
3. the mistake people make at this step, with "but"
4. how to know it's right (what you'll see, hear or feel)
5. the win or the bridge to the next step

- **Length per item or step:** about 120-180 words is the guide in lists of 7 to 10; a bit longer is fine when nothing is fluff (operator, after plumbing run 03). Cut repeated warnings and restated points first.
- **Bridges:** never more than two items or steps in a row without a forward line or a stake line.
- **Item one by about 30 seconds** in lists (plumbing run 03 put it at word 139: too late).

**A title that fits none of the seven:** build the opening from the six jobs in "The opening", in the order the closest type uses, and pick the shape that best suits the content. Note it in the plan as "new type"; after three, it's proposed for this table and added only with the operator's yes.

## Using the models: never a copy

1. **Name the models and the differences.** The plan names one or two models for the video type and at least three things done differently: the opening order, the number or order of items, the promise devices, the stake device, the comment question.
2. **No repeats.** The same model never appears in the channel's last five rotation log lines (`| model: [IDs]`).
3. **Blending is encouraged:** one model's opening shape, another's step pacing.
4. **Planning only.** Model files are read at the planning step, never kept open while writing. Wording comes fresh from the brief, in the persona's voice.
5. **Read "Doesn't transfer" first.** Every model was made by a real person on camera: their demonstrations, meter readings, job stories, prices, sponsor reads and UK wording never transfer.

The copy guard flags any run of 8 or more words shared with a model file.

## CTAs

Frederick Barnes (and any channel whose profile says subscribe only):
- **No mid-video CTA.**
- **At the end, a very short subscribe ask** (operator, 2026-10-27: "CTA will literally just be a very short subscribe one"): one line, in the persona profile's shape, tied to what the channel delivers, worded fresh each time.
- **Talking Head** scripts wrap it in markers exactly as core `workflow.md` sets out, with `===START CTA(NO BOOK)===` and `===END CTA===`. One block only.
- **Never** a long pitch, the "no rush" family (`cta-and-endings.md` §5), a QR walkthrough, or a production label read aloud.

If a future electrical channel has a book or a mid-video CTA, its placement follows plumbing's rule (about a third of the way in, never before the end of item 3, at the end of an item's win), added here with the operator's yes.

## The ending

After the last item or step:
1. **The end CTA:** the one-line subscribe ask, in its markers.
2. **The comment ask, which ends the video:** a short turn to the viewer, an outright ask to leave a comment, one specific question the viewer can answer from their own house (the age of the house, the outlet that gives them grief, what they found behind the plate), and that he reads every comment ("I read every one" or "I read every comment"; operator, 2026-10-27: "we say we read every comment"). Two or three sentences. Never a bare "let me know in the comments", never the same question two videos running, never "let me know if you" (a chatbot leftover the scanner flags).

No recap, no tease of a future video, no sign-off after the comment line.

## Length

**At least 12 minutes** of narration (this pack raises the core 8-minute minimum), counted at the profile's words per minute (Frederick: 195, so at least 2,340 spoken words). **15 to 22 minutes is the sweet spot** (operator, 2026-10-27). Inside that, the value decides.

- **Never pad.** The same warning said twice, the promise restated, or a step explained twice is padding.
- **If the brief can't fill 12 minutes with real value,** even with the facts guide, the run stops with NOT READY and asks for a fuller brief. The fix belongs at the ideation stage.
- **For calibration:** the 31 models run 5 to 32 minutes; the niche's in-lane videos typically 8 to 17. Winners' lengths come from the content.

## Voice

- **"You" for every instruction; "I" for opinions, preferences and verdicts.** "Kill the breaker, then prove it's dead." "I'd use a lever connector there every time." Contractions, the way people talk, unless the persona profile forbids them.
- **Plain beats clever.** State the fact. At most one picture-phrase per item, only when it teaches.
- **Honest candor.** Say the limits plainly: "A tester can be wrong." "This one's not a homeowner job." Viewers trust the line that says no.
- **Warmth comes from reassurance, not humour.** "You didn't break anything." "That's a five-minute fix." No jokes.
- **Swearing: none** (operator, 2026-10-27).
- **A phrase is voice once; in the same slot every video, it's a tic.** Each stock phrase at most once per video (the once-list in the scanner block), and rotate what opens an item and what closes the video.

**Written for the voice** (core `workflow.md` §4, every channel). Electrical has more numbers and letters than any other niche, so:
- **Units in words, numbers as people say them:** "a hundred and twenty volts", "fifteen amps", "a twenty-amp breaker", "fifteen hundred watts", "five milliamps", "sixty hertz". Never 120V, 120 V, 15A, 1,500W, 5mA, 60Hz, 10kW.
- **Wire and cable names in words:** "fourteen-gauge wire", "twelve-two cable" (twelve-gauge, two wires plus a ground). Never 12/2, 14 AWG or #12.
- **Letters people say as letters** are written with no periods: GFCI, AFCI, NEC, UL, EV, LED, CPSC. Say what the letters mean the first time ("a GFCI, the outlet with the test and reset buttons"). Anything people don't say as letters is written as words.
- **Code sections** are never read as numbers ("NEC 406.4(D)(2)"): say "the electrical code" and what it requires.
- **Fractions and measurements in words:** "six inches of wire", "three-quarters of an inch".

## Proof

The winners are real electricians filming their hands. This channel is an AI presenter who explains. Proof is the kind that survives any footage.

**Use:**
- **The mechanism, in one plain line:** why it happens. "A loose wire touches on a smaller spot, and a smaller spot gets hot." Best under 15 words.
- **A fact from the brief or the facts guide,** said plainly; a named source keeps its figure exactly ("CPSC says…").
- **The maker's own instruction,** when the brief confirms it: "The instructions on the device say to strip it to the gauge on the back."
- **A check the viewer runs at home** with what they'll see either way: the plug-in tester's lights, the TEST button cutting the power, the tug on a connection. Only safe checks the brief or facts guide confirm; never a finger, never a live test inside a box.
- **The honest limit:** what the fix won't do. "A new outlet won't fix a loose wire further down the line."
- **The typical case, as a general statement:** "Older houses often have outlets wired through the push-in holes."
- **Test topics, explained:** what the famous demonstration showed, said as a known result ("When people test this side by side, the push-in connection runs hotter"), from the brief, never as something the channel did.

**Never:**
- **First-person tests, measurements or demonstrations:** "I tested", "I measured", "watch me", "I'll show you on the meter".
- **Anything that needs footage:** "look at this", "as you can see", "right here", "on the left".
- **Job and customer stories:** "I once found…", "a customer called me…", "after all the houses I've worked in" (operator, 2026-10-27). Say it as the typical case.
- **Sweeping claims nobody can check:** "this has saved thousands of lives".

## Safety

The facts come from the brief and the facts guide. **The brief can add safety but never remove it** (operator, 2026-10-27).

**Always, in every script that touches wiring, a device, a box or a panel:**
1. **Power off at the breaker, then prove it's off** with a tester that's been checked on a known live outlet first, before any cover comes off. Said inside the first step that needs it, not as a disclaimer at the top.
2. **How the power comes back,** and the test after: breaker back on, then the check that it works (the tester, the TEST button, the lamp).
3. **The call-an-electrician line names its trigger:** "If the wires are brittle or scorched, that's a call." "If it trips again the moment you reset it, stop." Never the vague "if you're not comfortable".
4. **Panels:** the inside of a panel stays live even with the main breaker off. A homeowner looks at the outside, resets breakers and reads the labels; the dead front comes off only for a licensed electrician.
5. **Generators:** never a cord with plugs on both ends, never into a wall outlet; only an interlock with an inlet or a transfer switch, put in with a permit; the generator outdoors, well away from the house, as the facts guide gives it. The carbon monoxide warning is said whenever a generator is running in the script.
6. **Permits and local rules:** where the brief or facts guide says a job needs one, say so in one line ("Check with your local building department first").

**Emergency sequences get every step, whatever the brief leaves out** (the gas-leak lesson from plumbing run 02), in the script's own words, from the facts guide's §12: someone shocked (don't touch them while they're in contact, cut the power first, call 911); a burning smell or smoke from an outlet or panel (power off at the breaker if it's safe, get out, call 911 from outside). Never "pull them off the wire" or "throw water on it".

**How safety sounds:** one short line inside the step where the risk is, with the reason, in proportion. Vague danger reads as a scare tactic; a plain reason reads as care.

**Never narrate an unsafe step** the visuals would draw: no hands in a live box, no testing by touch, no "it's only 120 volts".

## Banned in these scripts

**Never:**
- **A name or channel intro,** a greeting, "today we're going to", or "this channel is for…" (Frederick's old scripts opened with his name in all 23).
- **Vague teases:** "stay till the end", "stick with me", "you won't believe" and the rest of the core hard-ban list. "By the end of this video you'll know…" is allowed only as the opening's one value promise (P11).
- **A run-down of the first items in order** in the opening (P10's lesson).
- **A recap** at the end.
- **First-person tests, measurements and demonstrations; pointing at the screen; job and customer stories; anyone's motives.**
- **Money:** prices, savings, "save hundreds", the bill (operator, 2026-10-24).
- **Electricians, inspectors, firefighters or the utility as the villain;** "electricians hate", "what they don't want you to know".
- **Frederick's old template:** the long CTA, the "no rush" family, the firefighter framing, "Just Stop Fire", the old book.
- **Edit notes, cues, labels or directions** of any kind.
- **Hype that gets mocked:** "horror movie", "brutal tests", and any "every", "never" or "forever" the script then walks back.
- **Copying 8 or more words in a row** from a reference file.

**At most once per video:** the phrases in the scanner block's `once` lines.

## Scanner rules for this niche

The scanner (core `script-scanner.py`) reads this block. `allow` lines are wording these rules require; `lift` removes one core hard ban for this pack only (P11); `ban` lines are fix-on-sight; `once` lines fail on the second use.

```scanner
min-minutes: 12
lift: tease: by the end of this video
allow: I read every one
allow: I read every comment
ban-regex: \btoday,? (?:we'?re|we are|I'?m|I am) going to\b | opening: "today we're going to"
ban-regex: \bI(?:'ve| have)? (?:tested|tried|measured|ran (?:a |the |some |my )?tests?)\b | first-person test claim
ban-regex: \bmy (?:own )?(?:test|tests|testing|results|meter reading)\b | first-person test claim
ban-regex: \b(?:watch|let) me show you\b|\bwatch me\b|\bI'?ll show you on (?:the|my) meter\b | first-person demonstration
ban: as you can see | pointing at the screen
ban-regex: \blook at this\b|\bright here\b|\bon the (?:left|right) (?:side )?of (?:the|your) screen\b | pointing at the screen
ban-regex: \b(?:after|in) all the (?:houses|homes|jobs|panels) I'?ve (?:worked|been|seen|wired)\b|\bI once (?:found|had|saw|walked)\b|\ba customer (?:of mine|called|asked)\b|\bon a job (?:once|last)\b | job or customer story
ban-regex: \belectricians? (?:hate|don'?t want)\b|\bwhat (?:electricians|the electrician|inspectors) (?:won'?t|don'?t) tell you\b | trade as villain
ban-regex: \$\s?\d|\b\d[\d,]*\s?(?:dollars|bucks)\b|\bsave (?:you )?(?:hundreds|thousands)\b | money (no money framing on this channel)
ban-regex: \bthis channel (?:is for|exists|is all about)\b | template stock line: channel promise
ban-regex: \bno rush\b|\bno pressure\b|\bwhenever you'?re ready\b | CTA "no rush" family
ban-regex: \bjust stop fire\b|\bprevent the burning\b | the old brand and book
ban-regex: \bas a (?:former |retired )?firefighter\b|\bfire (?:department|service) taught me\b | the old firefighter framing
ban: horror movie | hype that got mocked
ban-regex: \bbrutal tests?\b | hype that got mocked
ban-regex: \bit'?s only (?:a hundred and twenty|120|one-twenty) volts\b | unsafe line
ban-regex: \b\d[\d,.]*\s?(?-i:V|A|W|kW|kWh|mA|Hz|VA)\b | unit written as a symbol (write the word: 'fifteen amps')
ban-regex: \b\d+\s?(?-i:AWG)\b|\b(?-i:AWG)\s?\d|#\s?\d{1,2}\b | wire gauge written as a code (write 'fourteen-gauge')
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
once-regex: \bplease,? test it\b | the insistence line
once-regex: \bthat'?s a call\b | that's a call
once-regex: \bpalm (?:on|against) the (?:plate|cover)\b | Frederick's old tic: palm on the plate
```

## Before handing over

Check that:
- the point comes in the first sentence, with the problem the viewer has and the fix or answer named by about 15 seconds
- the opening follows the video type's order, with at most one value promise that never runs down the first items in order, and no intro, greeting, vague tease or recap
- every item or step puts the viewer in the scene, aims at one feeling, has at least one "but" turn and ends on a win; bridges turn between items; a question about every two items; the title's feeling and key word come back every few items; an "I" verdict in most items and one insistence line; capability balances every fear line; the last item closes on relief
- items follow the item shape (lists) or the step shape (how-to and fix), at about 120-180 words, item one by about 30 seconds in lists, and no more than two in a row without a forward line or a stake line
- every item carries one stake, once, in proportion; fire is never the topic; no prices, savings or money words anywhere
- the villain, if any, is the old work or the cheap part, never electricians, inspectors, firefighters or the utility; named panels only with sourced facts
- every forward line is paid within about five minutes; no stretch runs past five minutes without a forward line or a payoff; every callback matches a real promise
- the tenure appears at most once, as 35 or the title's number; no job or customer story; no "I tested", no pointing
- safety: power off and prove it in the first step that needs it, how the power comes back and the test after, the call-an-electrician trigger named, panels and generators as set out above, every emergency sequence complete; the brief added safety, never removed it
- every code rule, size, distance and danger figure traces to the brief or the facts guide; settings from everyday knowledge are marked "general knowledge"
- every unit, wire size and number is written for the voice; every term on the list is explained the first time
- the CTA follows the persona profile: no mid-video CTA, the one-line subscribe ask in its NO BOOK markers at the end
- the video ends on the comment ask, with nothing after it
- each once-phrase appears at most once; the opening shape, stake device and comment question differ from the rotation log
- the plan names its models with at least three differences, and no model was used in the channel's last five scripts
- the script runs at least 12 minutes at the profile's words per minute (15 to 22 is the sweet spot), with nothing padded
