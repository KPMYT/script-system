# HVAC pack diagnosis: what carries over from the plumbing pack, what changes (DRAFT)

Written 2026-10-27 by the HVAC chat (branch `claude/hvac-research-czb2hy`), for the operator's ask: "take and diagnose current script writer, plumbing scripts skills and lets figure what needs to be adapted and whta can remain as is. look through every possible variable". **Nothing in any skill has changed.** This is the plan; every change still goes to the operator first.

**What was read:**
- The plumbing pack **as installed on the account.** It's one step ahead of `main`: it has the 2026-10-27 escalation-line option and model R21, from branch `claude/festive-planck-2e8f22`.
- `personas/roger-the-pipe-guy.md`, the core (`core/`, including `script-scanner.py`), `tools/build_skills.py`, `tests/run_checks.py`, `HANDOFF.md` §3, `PROPOSALS.md` and `PINNED.md`.
- The HVAC research: `niche-research/studies/hvac/CONCLUSIONS.md` and batch 1's 16 fact-checked briefs.
- The electrical chat's list of every plumbing lesson (`studies/electrical/lessons-for-the-pack-2026-10-27.md`, branch `claude/intelligent-ride-v1at70`), as a cross-check.

**Two helpers did the wide sweeps.** Their notes are in `studies/hvac/pack-diagnosis-2026-10-27/` and were spot-checked against the sources:
- `references-and-models.md`: models, voice samples, excerpts, price guide and the unit plan.
- `wiring-scanner-checks.md`: every place a channel is plugged in, the scanner run on HVAC wording, and clashes with the other chats' branches.

**Status key:**
- **KEEP:** copy as it is. Only the example lines are rewritten for HVAC: every example must be new, or the copy guard and the writer will echo plumbing.
- **ADAPT:** same rule, HVAC content.
- **NEW:** HVAC needs something plumbing doesn't have.
- **ASK:** needs the operator's call (numbered in section 9).

---

## 0. The short answer

HVAC is the closest niche to plumbing in the whole portfolio. The audience is the same (Profile A), and money framing holds up best in HVAC. The villain is the trade, and the operator's standing line is "very similar to what Roger is right now", "same as rogers pipe guy in most aspects". So **most of the pack's rules carry over unchanged.** What changes is the trade's content: the villains' targets, the pains, the safety rules, the terms, the video types, the price guide, the models and the voice.

| Part | Verdict | Size of the job |
|---|---|---|
| The script-writer (core rules, START, the gate, the audit) | **KEEP.** No core rule needs to change for HVAC to run. | Small: a channel row, the description, build entries |
| The scanner (core) | **ADAPT.** Seven gaps, two of them serious: a wrong tenure ("forty years in HVAC") passes silently, and some ordinary HVAC lines fail when they shouldn't. Shared with the electrical pack. | Medium: core changes, each with a test |
| Plumbing pack rules (SKILL.md) | About 70% **KEEP**, 25% **ADAPT**, a few **NEW** | Medium: a careful rewrite |
| Plumbing references (models, voice, excerpts, price guide) | Structure **KEEP**, content **rebuild** | Large: the real work (transcripts, a price guide checked against two sources) |
| Roger the HVAC Guy's profile | Copy of Roger the Pipe Guy's, **ADAPT** 10 lines | Small, but needs four decisions |
| Tests | **NEW.** Batch 1 lets us test like for like against Ray Dutton's originals | Medium |

---

## 1. The script-writer and the core rules

The core never names a niche except as examples, so **HVAC runs on it without a core rule change** (wiring notes §1 row 2). What has to be added:

| Where | Plumbing now | HVAC needs | Status |
|---|---|---|---|
| `core/channels.md` | Rows 3-5 (Roger, Mark, Vintage, `plumbing-scripts`, ready) | A row for Roger the HVAC Guy, `hvac-scripts`, **pending** until a test passes. Frederick takes row 7 on the electrical branch, so HVAC is row 8. | ADAPT |
| `tools/build_skills.py`: the script-writer's description | "Channels ready now: … (plumbing)" | Add "Roger the HVAC Guy (HVAC)" once ready. That's about 750 characters with Frederick too, under the 1,024 limit. | ADAPT |
| `build_skills.py`: the script-writer's table of other skills | Rows for `plumbing-scripts` and each persona skill | Rows for `hvac-scripts` and `roger-the-hvac-guy-persona`. **The electrical branch forgot these**, so check after merging. | ADAPT |
| `build_skills.py`: the written scanner commands, `PERSONAS`, `PACKS`, `INSTALL` | Plumbing entries, hard-coded counts | HVAC entries (the electrical branch also skipped the commands and INSTALL) | ADAPT |
| `tests/run_checks.py` | Plumbing twins of checks 21, 22, 24, 25, 26, 32, 34, 36; checks 1b and 2 cover only the plumbing and woodworking folders | HVAC twins, numbered **60-69** to avoid the two other branches. Add the HVAC folder to checks 1b and 2. | NEW |
| `README.md` file map | Plumbing section | HVAC pack, profile, `studies/hvac/` | ADAPT |
| The core rules themselves | | No change. The claims policy, offer rules, workflow, audit, humanizer, CTA rules and rotation all apply as they do to plumbing. | KEEP |

One core rule to watch: `offer-rules.md` §5 bans "negative claims about named companies". That matters for the **brand-verdict** video type (section 3.8). The batch-1 titles don't need it.

---

## 2. The scanner (core): seven gaps HVAC hits

From the wiring notes §2 and §4. Every case was run on the real scanner, and the main one re-run by the main session.

| # | Gap | Example | Effect | Fix |
|---|---|---|---|---|
| 1 | The tenure check's "trade" words have no HVAC, heating or technician words | "After forty years in HVAC", "40 years as an HVAC tech", "a 40-year HVAC man" | **A wrong tenure passes silently** (Roger is 45). The same gap lets "25 years as an electrician" pass for Frederick. | Add the HVAC and electrical trade words (core) |
| 2 | A title's years are read only next to plumbing or woodworking words | Title "A 50-Year HVAC Tech's Warning", script says "50 years" | **The script fails though the title allows it** ("title numbers win") | Same fix as 1 |
| 3 | "working / spent … for N years" is counted as the narrator | "That old compressor kept working for 20 years" | **Fails falsely.** Plumbing has it too ("That old water heater kept working for 20 years"), but HVAC talks about equipment ages all the time. | Check who did the working (core) |
| 4 | "my X has been … for N years" | "My furnace has been running for 20 years" | **Fails falsely** | Same |
| 5 | "N years of experience" near "I/me" | "Techs with 20 years of experience told me…" | **Fails falsely** | Same |
| 6 | "doing this N years" with no "for" | "I've been doing this 40 years" | **A wrong tenure passes,** in every niche | Core fix |
| 7 | Letter words (HVAC, MERV, SEER, BTU, AC) are each a line for the judge, and only 25 are printed | An HVAC script names them constantly | **Other judge flags get pushed off the list** (in a test, the thumbnail and staccato flags vanished) | A pack setting for letter words people say, or a longer list (core) |

**These seven are core changes,** so they need the operator's yes, a test each, and one chat doing them (the electrical pack needs 1, 2 and 6 too). **ASK 10.**

**HVAC wording for the voice.** The scanner already fails "16 SEER2", "R-410A", "24V", "96%", "68°F", "1/2 inch", "20x25x1" and "5 psi". These pass silently and the voice may misread them: "24 V" and "1500 W" (a space before the unit), "7-10 degrees" and "$75-$200" (ranges with a hyphen), "A/C" and "heating/cooling", "R-22", "CO", and "your furnace will thank you" (the plumbing ban only covers wallet and pipes). The helper wrote and tested six ban lines for the HVAC scanner block (wiring notes §4). They avoid a bug the electrical branch has: its unit ban fails "in 2023. A new outlet…". **Worth telling the electrical chat.**

**Spoken forms for the pack's voice section:** "MERV 13"; "16 SEER two"; "96 percent"; "R-four-ten-A", "R-twenty-two"; "twenty-four volts"; "a twenty by twenty-five by one filter"; "seven to ten degrees"; "$75 to $200"; always "carbon monoxide", never CO. How the voice says AFUE, HVAC and MERV is a listening test on Roger's ElevenLabs voice (**ASK 4**).

---

## 3. The plumbing pack, section by section

Each section of `plumbing-scripts/SKILL.md`, in order.

### 3.1 What this skill covers, authority, files

**KEEP** the structure and the authority order. **ADAPT** the description: it must name HVAC's own triggers (furnace, AC, heat pump, filter, thermostat, condensate, drafts, the heating bill). Otherwise, on claude.ai, a furnace-drain title could load `plumbing-scripts` instead. Adding "not HVAC" to plumbing's description is a change to a ready skill, so it would need a yes. The files table follows the references (section 5).

### 3.2 The overrides table (where the pack overrides the core)

Plumbing's 15 rows were each approved **for plumbing**. HVAC's pack needs its own rows. Under "very similar to Roger", the plan is to copy all of them, with these changes:

| Row | Plan for HVAC |
|---|---|
| Inputs: title + brief + rotation log, no research pack | **KEEP** (batch 1's briefs are built for it) |
| Named forward promises in the body (P3/P10) | **KEEP** |
| The ending: a one-line end CTA, then the comment ask (P5) | **KEEP** |
| 12-minute minimum | **KEEP.** Ray Dutton's 53 videos run a median of 13.4 minutes (9.4 to 16.5). |
| Rotation-log fields (model, money, promises, comment) | **KEEP** |
| Copy guard over SKILL.md, excerpts, voice samples, models and profile | **KEEP**, pointed at the HVAC files. Ray Dutton's scripts go under the guard if used as models. |
| Mid-video CTA a third in, never before item 3 | **KEEP if Roger the HVAC Guy has a book** (ASK 2) |
| No sources needed; originality out of 6, pass at 4 | **KEEP** |
| Signposts ("Number four.") | **KEEP** |
| D4: the brief plus the price guide; everyday settings allowed as "general knowledge" | **KEEP**, with the HVAC price guide |
| Contractions kept | **KEEP** |
| The opening checked as the hook's three jobs | **KEEP** |
| No value line | **KEEP** |
| Cents exceptions (cost per use; three prices side by side) | **KEEP** (HVAC has both: "a dollar's worth of vinegar a month") |

The escalation line (P11 on the plumbing branch, plumbing only) suits HVAC well ("from a filter you can change tonight to the furnace that won't light"). **KEEP**, under the same "option, not a rule" wording.

### 3.3 Inputs

**KEEP**: title, brief, rotation log, research pack `not used`, the fill-in rule (P7: prices from the brief, then the price guide; settings and intervals from everyday knowledge).

**ADAPT:** "no dose, mix or chemical method beyond the brief" becomes "no chemical, electrical or gas method beyond the brief and the HVAC safe defaults".

**NEW: dated facts.** Plumbing has no freshness check because its prices are ranges. HVAC has facts with a date on them:
- refrigerant rules (the R-22 phase-out, the R-410A changes, the new refrigerants)
- tax credits and rebates, which change by year
- brand-verdict facts (warranties, model lines, "in 2026")

Proposal: these are said only from the brief, with the brief's date, never from general knowledge. A brief over about 90 days old has its dated facts re-checked (as woodworking does at 30 days). **ASK 7.**

### 3.4 The viewer

**ADAPT, and it needs evidence plumbing had and HVAC doesn't.** Plumbing's viewer section rests on 506 comments ("the bill is the pain, not the plumber", the failed attempt, "3:15 is where it starts"). **The HVAC study has no comment analysis.** The audience is the same people, so most of it will hold, but the HVAC specifics are missing: what HVAC viewers argue about, what they distrust, what safety corrections they post. Proposal: a small study (section 8, step 1), mostly free (NexLev comments and transcripts don't use the search cap).

Parts to adapt now:
- **Terms explained the first time** (the plumbing list is psi, trap, P-trap and the rest): MERV, SEER, AFUE, BTU, tonnage, condensate line and trap, condensing furnace, flame sensor, hot-surface igniter, inducer motor, pressure switch, limit switch, capacitor, contactor, heat exchanger, blower and blower motor (ECM, PSC), supply and return, static pressure, heat pump, auxiliary or emergency heat, refrigerant, C-wire, setback, short cycling, damper.
- **The standard kit:** a screwdriver and nut driver, a flashlight, replacement filters, a wet-dry vac, white vinegar, a garden hose, a small brush. Anything beyond that gets a price (a fin comb, a multimeter, fine emery cloth for a flame sensor).
- **What they bring** (from the HVAC study, measured): distrust of the store shelf (1.83x), pride in doing it themselves (1.53x), rule-curiosity (1.39x), the myth-bust (1.34x) and insider curiosity (1.33x) lead. Fear of damage, safety fear, protectiveness and emergency dread are weak as the lead (0.76x to 1.00x).

### 3.5 The villain

**KEEP** the rules: aim at the price and the silence, never motives; it comes back throughout; outrage at a big price as an opinion; never a named company.

**ADAPT** the targets (CONCLUSIONS §2, §6.2):
- the HVAC company and **the upsell**: the replacement quote, the "you need a new system", the tune-up add-ons. The study's strongest villains are the HVAC company (1.60x) and the maker and store shelf (1.62x).
- **the store shelf**: the "premium" filter, the gadget, the miracle spray
- **the utility, lightly** (0.99x). The service call alone is weak as a villain (0.83x).
- **NEW line: the honest out.** "A tech you trust" stays. The technician is never the villain; he works as the friendly insider. Plumbing says the same in its viewer notes ("many viewers like their own plumber"). HVAC makes it a rule, because batch-1 titles name techs ("Things HVAC Techs Don't Want You to Know", "Why HVAC Techs' Own Furnaces Never Break Down").
- **Title motive, script fact.** Titles like "Hope You Keep Making" claim a motive; the script never does. Plumbing's rule already covers it; HVAC titles test it more often.

### 3.6 The opening

**KEEP** the six jobs, the count line, "simpler and stronger", one figure at most, and the "never" list.

**ADAPT:**
- every example line (all plumbing now)
- the tenure line, to add "Roger the HVAC Guy 45"
- the pains to open on: the house that won't warm up, the furnace that quits on the coldest night, the bill that crept up, the quote for a new system

### 3.7 Emotion, all the way through (the 11 rules)

**KEEP all 11 rules.** This is the single most important carry-over. **ADAPT** what they point at:

| Rule | HVAC version |
|---|---|
| 1. Put the viewer in it | What they hear, feel and smell: the furnace clicking and not lighting, a cold room at one end of the house, the burning-dust smell of the first heat, water in the drain pan, a draft at the door |
| 2. One real pain per item | The cold house on the coldest night; the after-hours visit; the replacement quote; being sold a system you didn't need; the bill creeping up; making it worse. **The study's lead is distrust and self-reliance; the bill and the damage are the stakes inside the video, not the hook.** |
| 3. Strong, plain words | Choking, starving for air, short-cycling, iced over, caked, rattling, sweating, freezing up, burning through |
| 4. "But" turns | Keep as is |
| 5. Ask the viewer | Questions about their own house: "When did you last pull the filter out and look at it?" |
| 6. Disgust where the topic has it | **ADAPT:** HVAC has less disgust than plumbing (0.51x as a title hook). It's real only on the slime in the condensate line and pan, mould, and a dust-caked blower wheel. Use it there, in proportion, never as a default. |
| NEW: comfort | The study added a new emotion, **E19 comfort**: the even, warm house, "warm again", "feels like new". Plumbing has nothing like it. Proposal: a win line can land on comfort as well as money ("the back bedroom's finally warm"). |
| 7-11 | End on a win; reaffirm the title's feeling; the villain comes back; the "I" verdict; finish on relief. Keep. |

Also carry the open plumbing problem: the core's ban on the "quietly" crutch word (H12a) against rule 8's "quietly". Carry the title's feeling in nouns and verbs.

### 3.8 The video types

Plumbing has ten. **Eight map straight onto HVAC**; two HVAC types are **NEW**. All 16 batch-1 titles are mapped (references notes §1b).

| Plumbing type | HVAC use | Batch 1 | Status |
|---|---|---|---|
| Single-product fix ("1 Cup of This…") | Vinegar in the condensate trap and line | #5, #6, #8 | KEEP |
| N things about one product | Dish soap, peroxide, vinegar on HVAC jobs | #7 | KEEP |
| Never-do list | Space heaters; what never goes near the furnace | #13 | KEEP |
| Mistakes list | Ray's mistakes and **habits** lists (habits are a variant: "the thing you do every day") | #1, #4 | ADAPT: add the habit variant |
| Head-to-head verdict | Filters ranked; heat pump vs gas furnace (with the payback arithmetic) | #9 | KEEP |
| Banned / code explainer | Refrigerant phase-downs; "why they keep banning your refrigerant" | (later) | KEEP, with the dated-facts rule |
| How-to / correct way | Ceiling fan direction; the right filter way round | #15 | KEEP |
| Product swap | The $5 filter over the $30; cheap draft fixes over the insulation quote | #3, #12 | KEEP |
| Hidden cause | "Why your furnace keeps shutting off", "why 70 feels cold" | #10, #11, #14 | KEEP |
| Seasonal or emergency | "Before the first cold snap (or pay for it)"; the outage furnace | #2, #16 | KEEP; Ray's pre-season checklist is this type's best model in either niche |
| **NEW: brand verdict** | "The Only N [Furnace / AC] Brands Worth Buying" | (batch 2) | NEW: the strongest HVAC sub-niche for faceless channels (3.38x). It needs its own rules: positive verdicts by product line, each fact from the brief (warranty, what's inside, ratings), no claim about a named brand that the brief can't source, and the "everyone else" side left unnamed (offer rules §5). **ASK 8.** |
| **NEW: cheap part, or symptom first** | "Furnace keeps shutting off? The $12 part" | #14 | Fits "hidden cause" plus the escalation ladder; may not need its own row |

The item shape: **KEEP** the six steps and 100-130 words. Step 2 reads "what's really happening in the system" in place of "in the pipe".

### 3.9 Using the models: never a copy

**KEEP** all five rules. The no-repeat rule (no model from the channel's last five scripts) runs dry if HVAC has only one or two models of a type. So the HVAC library keeps the plumbing structure models that fit (23 of 39 fit, 15 partly) and adds HVAC models beside them (section 5).

### 3.10 CTAs and the ending

**KEEP** the ending (end CTA one line, then the comment ask, nothing after) and every "never".

**The CTA content depends on the book**, which isn't decided (CONCLUSIONS §7.4; Ray sells a $27 "HVAC Survival Guide", and 26 of 66 persona channels sell an e-book). **ASK 2.** The options:
1. **Roger the Pipe Guy's book.** Not a fit: it's plumbing fixes.
2. **No book yet, subscribe only,** like The Vintage Pipefitter. No mid-video CTA; a one-line subscribe ask at the end.
3. **A new HVAC book.** Then the mid-video CTA in Roger's six-part shape, about a third of the way in.

### 3.11 Length

**KEEP** at least 12 minutes, 12-20 the sweet spot, value only, never padded.

**Open from plumbing:** words per minute aren't set on any plumbing profile, so the 12-minute minimum is counted at 150 while the voices run about 167-190. For Roger the HVAC Guy, set it from his real voice once the first voiceover exists. **ASK 4.**

### 3.12 Voice

**KEEP:** "you" for instructions and "I" for verdicts; plain over clever; honest candor; warmth from reassurance; no jokes; swearing none; one picture-phrase per item; the stock-phrase limits.

**ADAPT:**
- the persona device (Roger the Pipe Guy's first-Saturday drain check with his coffee) needs an HVAC equivalent, approved (ASK 3)
- the spoken forms for HVAC units and codes (section 2)

### 3.13 Proof

**KEEP** the whole "Use / Never" list: no "I tested", no pointing at the screen, no customer stories, a named source's figure as given.

**ADAPT** the examples: the furnace maker's manual on the filter's MERV rating; the EPA's MERV 13 advice; the Department of Energy's setback figure. Checks the viewer can run: pull the filter and hold it to the light; the drain pan; the burner flame colour; the thermostat's reading against a second thermometer.

**Watch:** batch-1 titles #8 ("I Pour Vinegar Into My Furnace Drain Every Month…") and #10 (the techs' own habit) are first-person routines. The profile's one approved personal detail covers this kind of thing, but it has to be approved for HVAC (ASK 3).

### 3.14 Money framing

**KEEP all of it.** HVAC is where money framing holds up best (the 2026-10-22 findings, the 1.31x money/enemy framing): the early comparison, the number cap, ranges never cents, the cost per use, the rotating devices. Payback arithmetic matters even more in HVAC (heat pump vs furnace, efficiency upgrades). Only the examples change.

**Watch:** the 2026-10-22 research found single low product prices get disputed. The same will happen with filters ("$5 filter"): give ranges and "in a multipack".

### 3.15 Safety

The biggest **ADAPT**. **KEEP:**
- "the brief always wins"
- "one short line inside the step, in proportion"
- "the call-a-pro line names its trigger"
- **the gas-leak rule** (every step, every time): gas furnaces make it more common in HVAC, not less

**REPLACE** the five plumbing defaults (boiling water, dry washing soda and the rest) with HVAC defaults, from the batch-1 fact-check (CONCLUSIONS §6.8):
1. Power off at the furnace switch or the outdoor disconnect before any panel comes off; the gas valve off for burner work; and say how it comes back on, and the check after. That last part was a plumbing gap the judge found and nobody fixed.
2. Refrigerant work is for licensed techs: no charging or "topping up".
3. Never bypass a limit switch, pressure switch or rollout switch.
4. After cleaning a condensate trap, refill it with water. Never pour anything into the pressure-switch hoses or the inducer.
5. One cleaner at a time (never bleach with vinegar).
6. Never run a furnace a tech has red-tagged.
7. Space heaters straight into a wall outlet, three feet clear, with a safety listing.
8. A car or generator at least 20 feet from doors, windows and vents, never in a garage, never backfed into the panel.
9. Air-sealing near natural-draft appliances needs a combustion safety test.
10. The fireplace damper is closed only when the fire is cold, and never on gas logs.
11. Capacitors hold a charge after the power is off: a call or a careful, named procedure from the brief, never "just pull it". This one isn't in the batch-1 fact-check; it comes from the profile clash below.

**NEW: carbon monoxide gets every step, like a gas leak.** When the CO alarm goes off: everyone out to fresh air, call 911 from outside, don't go back in until the fire department says so, then have the appliance checked. It needs a researched facts row, checked against two sources (CPSC, NFPA).

**Clash to settle:** Roger the Pipe Guy's profile says "never encourage DIY on gas, sewage, electrical or structural work". Ordinary HVAC topics touch gas furnaces, thermostat wiring and a 240-volt outdoor unit. The HVAC profile needs its own line, for example: "never DIY on gas lines, refrigerant or live electrical parts; switching the power and the gas off, filters, drains, thermostats and cleaning are fine". **ASK 5.**

**Ask carried from plumbing:** may the brief override the HVAC defaults, as plumbing's brief can? Recommended yes, except for the gas-leak and carbon monoxide steps.

### 3.16 Banned list and scanner block

**KEEP** every ban and the "once" list; they're mostly about the old template, not the pipes.

**ADD:**
- the six tested HVAC lines (section 2)
- the stock line widened ("your furnace / system will thank you")
- Ray Dutton's catchphrases, once his transcripts are read (competitors' catchphrases are banned)
- a ban on "Roger here" and "I'm Roger" (name intros are banned in the rules, but the scanner doesn't catch them; this applies to plumbing too)
- `min-minutes: 12`

### 3.17 Before handing over

**KEEP** the checklist, changing the HVAC parts: the HVAC defaults; gas and carbon monoxide steps; the HVAC terms list; dated facts from the brief; the CTA per the book decision.

---

## 4. Roger the HVAC Guy's profile (copied from Roger the Pipe Guy's)

| Field | Roger the Pipe Guy | Roger the HVAC Guy | Status |
|---|---|---|---|
| Status | ready | pending until a test passes | ADAPT |
| Niche pack | plumbing-scripts | hvac-scripts | ADAPT |
| Script type | Classic (no markers) | Classic, if the editing is the same | KEEP (confirm) |
| Voice | ElevenLabs "Ron", ID xkDz8dF9GIt1kG06c9Of | Same voice or a new one? | **ASK 1** |
| Words per minute | not set | Set from the first voiceover | ASK 4 |
| Who he is | blunt, unhurried tradesman, 45 years | the same, in HVAC | KEEP |
| **Same man or a new one?** | — | Is the HVAC Roger the same Roger (a plumbing and heating man; plumbers did "plumbing and heating"), or a separate 45-year HVAC man? It decides whether he can mention the plumbing channel, and which personal details and book he has. | **ASK 1** |
| Personal detail | first-Saturday drain check, with his coffee | an HVAC equivalent to approve (for example the filter check on the first of the month) | **ASK 3** |
| Enemy | the trade's prices and silence, the store shelf | the HVAC company's prices and upsell, the store shelf, the utility lightly | ADAPT |
| CTA, book | 100 Old-House Fixes | to decide | **ASK 2** |
| Hard no's | "never DIY on gas, sewage, electrical, structural" | an HVAC version | **ASK 5** |
| Scanner | name, book, tenure 45, the two e-book bans | `name: Roger the HVAC Guy`, `tenure: 45`, the e-book bans, plus a ban on the other channel's name (see below) | ADAPT |

**The two Rogers and the name check** (wiring notes §4, tested). Each profile already fails the other channel's full name ("Roger the Pipe Guy" in an HVAC script fails, and the reverse). Short slips pass ("the Pipe Guy", "my HVAC channel", lower case). Two options:
- **(a) Never name the other channel.** Add a ban line to each profile, so short forms fail too. This changes Roger the Pipe Guy's ready profile.
- **(b) The two channels may mention each other** ("my plumbing channel covers drains"). This needs a small core change: a name the scanner lets through as it is.

**ASK 6.**

---

## 5. The reference material (from the references notes)

| File | Verdict | What it takes |
|---|---|---|
| `models/` (39 plumbing models) | **Keep the structure models that fit** (23 yes, 15 partly, R12 no). **Add HVAC models**: strong candidates for the seasonal checklist (Ray's two at 1.23M and 943K; The DIY HVAC Guy's 1.22M), the warning and habit lists, symptom fixes (Everyday Home Repairs 2.78M; Word of Advice TV 2.57M), cheap-part repairs (The DIY HVAC Guy 2.45M; How To Home 2.20M), outage heat, and brand verdicts (672K and 578K faceless; Atlas AC 1.87M). **Thin:** the substance videos (only TheCheapFix's, already S18), ranked verdicts (all filmed tests), heat pump vs furnace (none proven). Those lean on the plumbing models. | Pull about 15-20 transcripts, write the beat maps and labelled scripts, and add an HVAC copy of `verify_plumbing_models.py` |
| `voice-samples.md` | **Rebuild.** The "borrow / don't borrow" notes carry over; the three plumbing samples don't. Candidates: Everyday Home Repairs, grayfurnaceman, Word of Advice TV, Silver Cymbal's own HVAC videos (he's already a plumbing voice, so the house sound stays). Not The DIY HVAC Guy (a young man), not Ray or any AI channel. | Pull 3-4 transcripts, and listen for age and register before choosing |
| `excerpts.md` | **Rebuild the lines, keep the 16 groups and their shape notes.** Add two groups: season lines and carbon monoxide/gas lines in proportion. | From the same 20-30 transcripts |
| `price-guide.md` | **Rebuild.** About 21 of 136 rows carry over (the damage rows, frozen and burst pipes, the leak alarm, shelf items, the gas-leak row). The HVAC service call differs from the plumber's ($75-$200 against $50-$250), so copying the plumbing guide would let wrong figures pass. **Seed:** about 45 HVAC rows already in the 16 briefs, checked once. **Missing:** the capacitor, contactor, inducer, control board, heat exchanger, refrigerant, new furnace / AC / heat pump installed, HVAC hourly rate, duct cleaning, CO alarm, CO facts, and the "$5,000 insulation quote" in title #12. | Plumbing's method: four researchers with two sources per figure, then four others re-checking; a carbon monoxide facts row; within the 200-search cap, in rounds |
| `unit-plan-template.md` | **ADAPT:** the HVAC type list; "in the system"; the emotion field swaps disgust words for distrust and self-reliance beats; the HVAC safety defaults; the CTA per the book. **NEW** fields: season (heating or cooling, the cold-night or hot-day stake), system scope (condensing or 80% furnace, heat pump or gas, which systems a tip applies to), and the title's dollar figure matched to a price-guide row. | Small |

**Risk to guard against:** plumbing facts leaking in. The copy guard catches only 8-word runs, not a reused plumbing price ("a drain call starts around $150") or a plumbing call-a-pro trigger. Every example line in the HVAC pack must be new.

---

## 6. Things HVAC should copy from the electrical chat's lessons

The electrical lessons file lists 99 plumbing problems and fixes. Those that apply to HVAC unchanged are already above. Four more:
1. **The writer's own audit is unreliable** (it reported "mechanical 0" with 97 curly quotes). In tests, always re-scan the pasted output and use a separate judge.
2. **Never reuse a model's real line as an example in SKILL.md** (the S04 anode line is still in plumbing's Proof section).
3. **The judge's fixes nobody built** (an item-length field, an "I verdict" count, a short-sentence guard). HVAC inherits the same weak spots. Worth asking whether to add them once, for both packs.
4. **No plumbing script has passed the judge yet.** Run 04 never happened, so the latest plumbing rules (the later CTA, the comment ask, the count line) are untested. **The HVAC tests will be the first test of those rules.** Whatever they find may apply back to plumbing.

---

## 7. Clashes with the other chats' branches

From the wiring notes §3; a trial merge was run in a scratch copy.
- **The plumbing branch** (`festive-planck`) merges cleanly with `main`. **The electrical branch** then clashes in `HANDOFF.md`, `PROPOSALS.md` and `tests/run_checks.py`.
- **Check 46 and P11 each mean two different things** on those two branches. That's for those chats to sort out when they merge.
- **HVAC takes checks 60-69** and a working proposal name ("P-HVAC-a") until it merges. Row 8 in `core/channels.md`; build entries after the electrical ones; `dist/` rebuilt only after merging.
- **The scanner gaps in section 2 are shared** with the electrical pack. One chat should make those core changes, so two chats don't edit the same lines.

---

## 8. Proposed order of work

1. **A small HVAC script and comment study** (answers the open question "does the pack need a transcript study here?": yes, a small one). It pulls about 20-30 transcripts of the proven HVAC videos by type (NexLev, outside the search cap), and the top comments on the 10-15 biggest. That one pull feeds the models, excerpts, voice samples and the viewer section. Saved in `studies/hvac/`.
2. **The HVAC price guide,** in rounds: the batch-1 seed rows re-checked against a second source, the missing rows researched, then a second team re-checking all of it.
3. **Write the pack** (`hvac-scripts/`) from the plumbing pack, section by section as in section 3, with every example line new. Then **the profile,** once ASK 1-6 are answered.
4. **The scanner fixes** (section 2), if the operator says yes and the electrical chat isn't doing them.
5. **Wiring:** the channel row (pending), build entries, checks 60-69, README. All checks pass.
6. **Tests, writer / operator / judge, like for like.** Batch 1 gives an unusual chance: four titles are remakes of Ray Dutton's videos. Suggested:
   - **#4** "11 Furnace Mistakes HVAC Companies Hope You Keep Making", against Ray's "5 AC Mistakes…" (transcript on disk)
   - **#3** "The $5 Filter…", against Ray's "$30 AC Filter…" (transcript on disk)
   - **#5 or #6**, the substance engine, against Roger the Pipe Guy's own hits

   Then `ready`, and the 16.

---

## 9. Questions for the operator

1. **Same Roger or a new man?** Is Roger the HVAC Guy the same Roger as the Pipe Guy (one man, plumbing and heating), or a separate 45-year HVAC man? And the voice: the same ElevenLabs voice as Roger the Pipe Guy, or a new one?
2. **The book and CTA:**
   - (a) no book for now: a one-line subscribe ask at the end, like Vintage
   - (b) a new HVAC book (title and contents needed): the mid-video CTA as Roger's
   - (c) something else
3. **His personal detail** (at most one per script, like the Pipe Guy's first-Saturday drain check). For example: "he checks his own furnace filter on the first of the month, with his coffee". Yes, or your wording?
4. **Words per minute and letter words:** set after the first voiceover. Is it fine to make one short test voiceover to check how the voice says HVAC, MERV and AFUE?
5. **Where DIY stops** (this replaces Pipe Guy's "never gas, electrical"). Suggested: never DIY on gas lines, refrigerant or live electrical parts; switching the power and the gas off, filters, drains, thermostats and cleaning are fine. Yes?
6. **The two channels mentioning each other:**
   - (a) never: a ban on the other's name in each profile, which changes the Pipe Guy's profile
   - (b) allowed ("my plumbing channel covers drains"): a small scanner change
7. **Dated facts** (refrigerant rules, tax credits, brand facts): only from the brief, with its date; re-checked if the brief is over about 90 days old. Yes?
8. **Brand verdicts** (batch 2): positive verdicts by product line, each fact from the brief, the "everyone else" side unnamed. Yes, or talk it through when batch 2 comes?
9. **The study first:** about 20-30 HVAC transcripts and the top comments of the biggest videos, before writing the pack. Yes?
10. **The scanner fixes** in section 2 are core changes, and plumbing benefits too (its false "the water heater kept working for 20 years" failure). Yes to making them? Should this chat do them, or the electrical chat?
11. **Everything marked KEEP** is copied from Roger the Pipe Guy's pack as it is: the opening, emotion, villain rules, ending, length, money, banned list and the escalation line. Yes to all, read from "same as rogers pipe guy in most aspects"?
