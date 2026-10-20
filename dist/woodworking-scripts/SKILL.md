---
name: woodworking-scripts
description: Script rules for the operator's woodworking channels, the scripting partner to woodworking-ideation. Currently covers the woodworking-for-profit lane: single-build YouTube scripts (Hank Hardwood, Dale Oakfield's Workshop, and any future channel in this lane). Use whenever a script is written, rewritten or reviewed for one of these channels, or whenever a woodworking research pack, build brief or "make this project and sell it" title arrives for scripting. Sets the skeleton, how length is decided, voice, proof, money math, adversaries, swearing, safety and how to write for AI-generated visuals. Persona, book and CTA wording come from the channel's persona profile; claims policy, output format and the audit come from the core rules.
---

# Woodworking scripts: the for-profit lane (single builds)

A single-build video shows the viewer one project, what it costs to make, and what it could sell for. The winners in this lane (BeardedViking, WhosTheVoss) name the materials within seconds, spend most of the runtime on the build, and save the money proof for the end. This skill copies that shape for channels with no real person in a real shop.

## What this skill covers

**It owns:** structure, pacing, length, voice, proof, money math, adversaries, swearing, safety and visual-friendly writing.

**It doesn't own:**
- **The persona:** name, sign-off, verbal habits, pets, backstory, any named doubter. These live in the channel's persona profile.
- **The book and CTA wording:** also in the persona profile.
- **The claims policy, output format, voiceover copy and audit:** these live in the core rules.

**Authority:** the core claims policy and offer rules come first, then safety and the title's promise, then the persona profile, then this skill, then the core base rules. The core `workflow.md` runs every script (START, the input gate, the output format).

## Files in this skill

| File | What it's for |
|---|---|
| `references/research-pack-template.md` | The input format. Write only from a completed pack. |
| `references/unit-plan-template.md` | The plan to fill in before any prose. |
| `references/voice-samples.md` | Three stretches of real human narration from lane winners: the voice anchor for every script (core `voice-anchoring.md`). |
| `references/excerpts.md` | Real lines from the winners, grouped by job. Use for shape and range, never wording. |
| `references/reference-scripts.md` | Read at the planning step for structure and pacing. Never copy wording. |
| `archive/` | Full competitor transcripts. Calibration only; don't read them while writing. |

## Inputs for this lane

The workflow reads this block at START and won't write until every input passes.

```inputs
- title | required | the locked title, exactly as approved
- brief | required | the ideation brief for this title
- research-pack | required | or "none", and the chat builds it (core workflow.md, section 2); follows references/research-pack-template.md; has a "Verified on" date; its title matches the locked title; live facts within the freshness window below; no gap marked blocking
- rotation-log | required | the channel's last five ROTATION LOG ENTRY lines, or "none" for a new channel
```

## Freshness

- **Live facts:** material prices, listing prices and platform fees. Re-check them if the pack's "Verified on" date is more than 30 days old.
- **Timeless facts:** cut lists, techniques and safety. These never need re-checking once verified.

## The viewer

The viewer is a 50+ American DIY homeowner, beginner to intermediate, who arrives wondering "could I make money from this?" Underneath that sits a deeper doubt: "would anything I make actually sell?" They want side income or a retirement supplement. They worry about buying the wrong tools and about wasting wood, and they take pride in doing things themselves.

The doubter in these scripts is their own doubt said out loud, which is why answering it with proof works.

For more depth, see `woodworking-ideation/references/audience.md` (§1 and §9 for this viewer, §7 for safety) and `word-bank.md` (§5 and §7 for vocabulary).

**Skill level:**
- Write for beginners without talking down. Use plain words.
- A trade term gets a short explanation the first time it appears ("the kerf, the slice the blade takes out"). After that, use it plainly.
- Never explain the obvious: sanding, drilling, measuring.

**The standard tool kit:**
- Assume the viewer owns a tape measure, speed square, pencil, circular saw or miter saw, drill/driver, sander or sanding block, and clamps.
- Anything beyond that (table saw, router, jigsaw, band saw, pocket-hole jig, Forstner bits, torch) needs an alternative or an "optional."

## The skeleton: fixed parts and flexible parts

**Fixed parts, always present, in this order:**

1. **Promise.** The title's promise with its number, in one or two sentences, plus one line that touches the viewer's fear or wish (core `retention-mechanics.md`, section 2). This viewer's main pains: having to buy tools first, wasting wood on something nobody buys, work that looks homemade, being out-priced by the big stores; and the wish underneath, side money from something they made. Point straight at how this build answers it. No persona intro, no channel name, no "today we're going to," no tease. Name the first material within about 15 seconds.
2. **Materials and where to buy.** Store and price for each priced item, then "prices subject to change" once, straight after the prices. One price per item, always rounded the way people talk ("about fifteen bucks"), never cents; small items can be grouped. Specs only as far as the viewer needs them to grab the right thing off the shelf ("a 12-pack of five-eighths inch wood screws," not the whole label).
3. **Cut list.** The exact measurements from the pack.
4. **Steps.**
5. **Finish.**
6. **Money block.**
7. **End CTA and closing line,** per the core rules and the persona profile.

When the build has to be finished before it's assembled (oil the top before the hardware goes on, finish the parts before the glue-up), the steps that must come after the finish (final assembly, hardware, felt pads, the quick check) follow it. Order follows the real build.

**Flexible parts.** Vary these across scripts; the plan records the choices:

- **Context:** none, or exactly one sentence, placed before the materials.
- **Tools:** their own short part, or folded into the materials.
- **A quick check of the finished piece** before the money block: whether it stands, fits or holds. Only include it if the pack supports it, and never as a claimed filmed test.
- **Where to sell:** its own part after the money block, or merged into it.
- **The listing angle** (how to present it for sale): include it when the pack has one.
- **Which money-block elements come first.** The listing proof can open the block, or the cost can.

**Mid-video CTA.** Place it right after the first real payoff, meaning the materials plus the first step. Never put it earlier, and never let it push the build later. Its length and wording come from the persona profile.

## Steps

- **Every step is an instruction to the viewer:** "Cut your first piece at five and three-quarters." Never "I'm cutting" or "watch me." Nobody on screen is the narrator.
- **Say each step in as few words as it allows.** Some steps take two words ("Flip them."), most take one ordinary sentence, and a genuinely tricky one (a compound angle, a jig) takes three or four.
- **A step earns extra words for:** a common mistake, a safety risk, a tool alternative, a quality tip, or a line of the persona's opinion, reaction or honest aside (an extra sentence here or there; personality is never stripped out to save words).
- **Repeats collapse into one line:** "Do the same on the other seven."
- **Safety is one practical line inside the step where the risk is,** with the reason. Never a separate section.

## Length comes from the content

There's no target length above the 8-minute minimum (core `workflow.md`, section 3). Fill in the unit plan first; the length is whatever the units add up to. Never pad, and never squeeze steps to fit a length. If the plan can't reach 8 minutes with real value, flag it: the fix is more research or a bigger project at the ideation stage, not more words.

Calibration from the winning scripts: these show the usual spread, they are not targets.

| Unit | Usual spread (middle 80% of lines) |
|---|---|
| Material line | 8-24 words |
| Step line | 8-31 words (about 1 in 7 is under 8 words) |
| Tip or safety line | 5-28 words |
| Money line | 5-28 words |
| Aside or opinion | 3-20 words |

Whole winning scripts ran 1,135-2,408 words, with 18-55 step lines; ours never go below 8 minutes (1,200 words at 150 words a minute).

**Uneven is the goal.** Real scripts put a two-word step next to a thirty-word one. Lines of matching length in a row sound machine-made.

## Exaggerated titles

Titles may exaggerate in degree ("EVERY tool," "stupid money"). The script delivers that through math, never through a claimed event. The promise line states what the build can do, and the money block shows the numbers that make the title reachable: how many pieces at what price would cover it. If even generous math can't reach the title's claim, flag it back to ideation rather than inventing support. Titles may also claim the persona's own selling or tenure ("the laziest thing I sell," "40 years of selling"), for Hank and Dale alike (operator, 2026-10-20). Those aren't flagged: the script delivers them through the numbers, and the narration never claims sales, customers or history.

## Money block rules

- **Cost per piece** = lumber cost divided by pieces per board, plus consumables per piece (glue, screws or nails, finish, sandpaper, hardware). Round up.
- **Tools are one-time costs.** Leave them out of the per-piece cost. The doubter can raise them ("and the drill bits?"), and the answer is that they're paid off over many batches.
- **Fees:** subtract the fee of the venue the script recommends, using the dated fee from the pack.
- **Price:** give it as the narrator's opinion, set inside the listing range and never at the top of it ("I'd list them around $40").
- **What's left** is price minus cost minus fees, per piece. Any batch total is conditional: "if all 20 sell."
- **Time** is per piece or per batch, labelled as an estimate. No hourly-wage framing; the operator dropped it.
- **Never guarantee income.**
- **Keep it easy to follow** (core `humanizer.md`, H22). The money block answers "is it worth it?" with the few numbers that prove it: the parts cost, the price, what's left, and one batch line. Everything else is rounded and collapsed ("the pads, oil and sandpaper add about six bucks"). Fees are given as one total ("Etsy takes about $9 of that"), never as the fee schedule. The research pack keeps every cent; the script says only what the viewer needs.

## Proof

Proof is always researched online listings, worded honestly:
- **"Listed at"** means an asking price.
- **"Sold for"** only with real sales evidence, such as a sold listing or a shop's sales count.
- **Give a range rather than one cherry-picked high price:** "listed between $35 and $60." Then one example at most, ideally the one closest to this build. Never read every listing out one by one.
- **Never name a seller or a shop** (operator, 2026-10-20). Say "one Etsy shop" or "a seller on Etsy". The editor blurs shop names on the screenshots.

At each proof moment, name the platform and the price (never the shop) so the editor can place the real screenshot.

The narrator never claims personal sales, customers or history: no "I've sold 200," no "my wife asked for one." Opinions and preferences are fine: "I'd skip the stain on this one."

## Where to sell

The fees below are general knowledge as of 2026. Always use the dated fee from the pack.

- **Etsy (US):** a $0.20 listing fee, 6.5% transaction fee and 3% + $0.25 payment processing, roughly 10% of a sale before ads. Offsite Ads can take up to 15% on sales they bring in. Suits small, light, giftable or personalized pieces.
- **Facebook Marketplace:** free for local pickup. Shipped checkout orders carry a selling fee, and published rates differ, so verify it. Suits bulky pieces and anything that doesn't ship well.
- **Craft fairs and markets:** booth fees vary widely (roughly $50-500). Impulse-priced small pieces sell in volume. Q4 is the strongest season.

## Safety

These lines are mandatory where the build calls for them, always inside the relevant step:

- **Kickback:** with a stop block, let the blade stop before lifting. Never use the rip fence as a crosscut stop. Use push sticks on narrow rips.
- **Spinning tools:** no gloves or loose sleeves near them.
- **Fumes and dust:** a mask for spray finishes and fine dust.
- **Oily rags** (linseed, tung): dry them flat, or store them in water or a sealed metal can.
- **Food contact:** food-safe finish and glue on anything that touches food, including the factory glue in edge-glued panels and rounds (the research pack checks it).
- **What a product can be made from:** never treated lumber, MDF, plywood or finished wood (or their sawdust) in anything for food, animals or burning.
- **Toys:** no small parts on toys for children under three.
- **Old furniture flips:** test for lead paint on anything made before 1978.

Describe only safe technique. The visuals are generated from the script, so an unsafe instruction becomes an unsafe picture.

## Voice

- **Use "you" for steps and "I" for opinions and preferences.** Write in contractions, the way people talk.
- **Use honest candor sometimes:** real tradeoffs and limits ("This one's slower to sand than it looks," "It won't ship well, so it's a local item"). Never invented mishaps.
- **No jokes.**
- **Personal details from the profile** (a pet, the coffee, the pencil) go at a natural pause: after a step lands, while the glue or oil dries, before a bridge. Never inside a tricky instruction, where they get in the way of the step.
- **Adversaries:** one per video, two at most. Categories only, never named companies.
  - **The doubter** (the default choice).
  - The big box store's markup.
  - Scammers.
  - Overpriced materials.
- **Retired adversaries:** clickbait YouTube, "the algorithm," and any group of people (including the old "hardwood crowd").
- **Swearing:**
  - Mild words only (ass, damn, hell, crap), aimed at the adversary or a price, never at the viewer, a customer or a named company. An order to the viewer counts as aimed at the viewer: "So do the damn math" fails; "That's a hell of a markup" works.
  - One to three per video, rotating the words.
  - Never in CTAs, titles or thumbnails, and no strong profanity.

## Writing for AI-generated visuals

- **Name the object and the action in every step line** ("Clamp the two sides to the base," not "Bring it together").
- **Keep measurements in the narration.** Generated visuals won't show them accurately.
- **Never point at the screen** ("right here," "look at this"), not even at listings and prices shown as real screenshots. Name the platform and the price instead.

## Variation: never a template

Two scripts on the same channel should never feel like the same script with new nouns.

- **Change the promise shape, the adversary and the swear words** from the channel's last few scripts.
- **Vary which flexible parts appear.**
- **Vary the order inside the money block.**
- **Let step lengths fall unevenly.**

Record these choices in the unit plan's variation check. The rotation log in the core rules tracks them across videos. The excerpts show the range available, so pick a different shape each time and never write the same shape twice in a row on one channel.

## Banned in these scripts

- Persona or channel intros in the opening.
- Retention teases ("stick around," "bonus at the end," "by the end of this video").
- Problem essays, and more than one sentence of context.
- Recaps.
- First-person build narration ("I'm cutting," "watch me").
- Invented sales, customers, family or history.
- Income guarantees and hourly-wage framing.
- Negative claims about named companies.
- Pointing at generated footage.
- Competitors' catchphrases or signature lines.
- Copying any run of 8 or more words from a reference file (`references/excerpts.md`, `references/reference-scripts.md`). The scanner's copy guard (`--refs`) flags it.

## Scanner rules for this lane

The scanner (core `script-scanner.py`) reads this block. These are fix-on-sight in this lane only.

```scanner
ban-regex: \bI(?:'m| am) (?:cutting|drilling|sanding|gluing|clamping|measuring|marking)\b | first-person build narration
ban-regex: \bI(?:'ll| will) (?:cut|drill|sand|glue|clamp|measure|mark|grab)\b | first-person build narration
ban: watch me | first-person build narration
ban: right here | pointing at generated footage
ban: look at this | pointing at generated footage
ban: as you can see | pointing at generated footage
ban-regex: (?:\$\s?\d[\d,.]*|\bbucks|\bdollars)\s*(?:an|per|a|/)\s*hour\b | hourly-wage framing
ban: per hour | hourly-wage framing
```

## Before handing over

Check that:
- the first material comes within about 15 seconds, and the opening touches the viewer's fear or wish
- the numbers are easy to follow: no runs of figures (any sentence with three or more dollar figures gets a second look), and no shop is named
- there's no intro and no tease
- every step is an instruction with a visible object and action
- every number, measurement and listing traces to the pack
- the mid-CTA sits after the first payoff
- the money block uses "listed at" or "sold for" correctly, includes fees, and makes no guarantee
- there's one adversary, two at most
- swearing is within one to three, with none in the CTAs
- the length came from the unit plan, and line lengths are uneven
- the opening shape, adversary and swear words differ from the channel's last script
