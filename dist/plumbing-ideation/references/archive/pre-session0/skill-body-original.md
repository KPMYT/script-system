---
name: plumbing-ideation
description: YouTube ideation system for the user's plumbing channels (Roger the Pipe Guy plus sibling faceless plumbing channels). Contains the banked winning title formats (F1–F35), word banks, reference titles with view data, audience psychology, the topic demand map, hard title rules, and the video-brief spec. Use this skill whenever the user asks for plumbing video titles, video ideas, ideation, title reworks or reformats, video briefs, or pastes YouTube screenshots (their own channel, competitor channels, or audience-tab data) for analysis — even if they never say the word "ideation". Also use it when the user wants to add newly discovered winning titles, topics, or formats to the bank.
---

# Plumbing YouTube Ideation

A complete ideation system for faceless plumbing YouTube channels targeting 50+ American DIY homeowners. Built from analysis of the user's own winners plus ~15 competitor and audience-overlap channels. The system treats **topics** and **title formats** as separate variables, and its core move is: **proven topic × proven format = new video**.

## Before generating anything

Read these reference files first — they ARE the system:

1. `references/format-bank.md` — the 35 banked formats with examples, modifier families, and word banks. Required reading before writing any title.
2. `references/reference-titles.md` — proven titles with view counts (the user's winners + ecosystem mega-winners), the lessons each batch taught, and titles already produced (avoid duplicating these).
3. `references/audience-and-topics.md` — audience psychology levers, the topic demand map, seasonal calendar, and channel context.

## Channel context (always applies)

- **Faceless channels.** Footage is compiled from other creators, so titles must promise **knowledge**, never **proof-of-work**. No single-project transformations, no "watch this exact pipe across 20 cuts", no builds. Persona claims delivered in voiceover ("In 45 years of plumbing…") are fine — credibility is narrative, not visual. "I tested" framings only work as persona verdicts ("After 45 years, here's which one I trust"), not as filmed experiments.
- **The persona** is a veteran plumber (Roger-type, 45 years in the trade) — the honest insider breaking ranks. This unlocks lost-wisdom and insider formats without fabrication: Roger IS the grandpa/old-timer.
- **Audience:** 50+ American DIY homeowners. See `references/audience-and-topics.md` for the psychology levers; the best titles pull two or more at once.
- The user runs **multiple plumbing channels**. Variants of the same concept across channels (different item counts, different angles) are normal and intentional — the ecosystem openly clones winners across channels.

## Hard title rules (never break these)

1. **Under 100 characters, always.** Count the characters of every title before output. If a title lands at 99–100, trim it — leave margin.
2. **Never reference a specific listicle item in a title** ("#6 is why…", "#2 causes…"). Use that slot for proven hooks instead: THOUSANDS, NO ONE knows, GENIUS, an adversary, GUARANTEED, You Do Most of Them Daily.
3. **Listicles should exceed 3 items when content allows** — longer videos are preferred. Exception: "Only N" survivor shortlists (Only 2 Brands…) and counted-mystery titles (Two Kitchen Ingredients…) stay small deliberately, because the low number IS the hook; those videos still run long by covering everything that fails.
4. **Not every title needs a two-part em-dash structure.** Vary structure and mirror proven reference skeletons closely. Sometimes a single clean clause is stronger ("7 Things You Should NEVER Flush Down Your Toilet"). Mix: single clauses, parentheticals, question openers, em-dash two-parts.
5. **Exaggerate freely** — stronger adjectives, bigger claims, more clickbait is allowed and encouraged. But keep every claim defensible in the script: puffery and superlatives yes; invented statistics, fake dates, and fabricated suppression stories no. The honest version usually exists (e.g., "BURIED since 1947" → "The trick plumbers used before drain cleaner existed").
6. **Apply winning topics to winning formats — do not invent new formats.** Experimental titles should still be recombinations of banked formats and proven topics. New formats enter the bank only from new winning data the user supplies.
7. **House style:** 1–3 ALL-CAPS power words per title, no more. Em-dash for two-part titles. Exclamation marks sparingly, matching the reference skeleton being mirrored.

## The method

### Phase 1 — Intake (when the user pastes screenshots or title lists)

Process each batch as it arrives; do not generate titles until asked. For every batch:

- Transcribe every title with views, age, and any VPH/multiplier badges. **Multipliers beat raw views** — they normalize for channel size and isolate true demand.
- Extract two separate things: **topics that work** and **title structures that work**. Compare against the existing bank: what confirms, what's new.
- Apply the **age/views matrix**:
  - Old + huge views → durable topic demand pool; the topic carried it. These are re-packaging targets.
  - New + huge views → current meta: proven topic × proven format. The format is the extractable, transferable asset.
  - New + modest views on a big channel → fatigue or bad topic-format fit. Useful negative signal.
- **Outliers are the purest signal.** A single outlier on a faced channel escaped the subscriber base into cold browse traffic — topic and packaging did all the work.
- **Head-to-heads are gold.** When the same topic exists on the user's channel and a competitor's at different scale, the framing is the variable. Flag re-attack opportunities on the user's own topics using the higher-ceiling angle.
- Run the **faceless filter** on everything: does the title promise knowledge or proof-of-work? Only knowledge transfers.
- Source priority: the user's own channel winners are the highest-value information; competitor data is inspiration to adapt. "Videos your audience watched — last 7 days" data is the hottest current signal and identifies ride-the-wave topics to act on fast.
- Propose new formats/modifiers/vocabulary for the bank with the next available F-number, and offer to update this skill's reference files so the bank stays current.

### Phase 2 — Format-topic fit check

A format only transfers when the topic has the raw material the format needs: suppression framing needs a plausible suppressor; ease framing needs a job people currently believe is hard; banned framing needs a real rule; in-group framing needs a group with a believable habit. Check fit before pairing.

### Phase 3 — Title generation

- Default batch size is 30 unless told otherwise.
- Default mix when the user asks for a batch: **50% doubling down** on the channel's own proven topics/formats (reworks can be as simple as a bigger listicle number or a stronger adjective) and **50% new territory** (banked formats from competitor data, new topics from the demand map, twists/recombinations). Confirm or adapt the ratio if the user specifies one.
- Group output by topic cluster. Tag each title lightly with its format numbers (e.g., *[F20×F18]*) so the user can reference the logic.
- Check every title against the hard rules above — especially the character count — before sending.
- Avoid duplicating titles already produced (listed at the bottom of `references/reference-titles.md`); adjacent angles on the same topic are fine and often intended.

### Reformat mode

When the user likes a **topic** but not the **format**, give ~5 alternative titles for that topic, each from a different banked format, each tagged with its format number, so the user can pick. This is a standard request — handle it without re-asking what they want.

## Video briefs

Whenever titles are generated, briefs come with them (short by default; **200–300 words each on request**, typically for final chosen batches).

Brief rules:
- **Talking points and content context only** — the facts, mechanisms, listicle items, cautions, and money/cost anchors a scriptwriter needs. No structural direction, no editing direction, no language/tone direction.
- One single flowing paragraph per brief (no internal line breaks or bullets) so each brief pastes into a single spreadsheet cell.
- Ground every exaggerated title in defensible facts: the brief is where the honest mechanism lives (anode rod chemistry, the dye test, what wipes actually do, why the vinegar+baking soda volcano is mostly theater). Include real dollar figures (service call costs, part prices) — money anchors are core to this audience.
- Flag genuine safety boundaries inside briefs where relevant (gas lines, chemical mixing, boiling water on porcelain/PVC) — the channel's trust depends on it.

## Output formatting

- When the user asks for copy-paste format (or after delivering a final list): provide titles in a fenced code block, **one title per line, single column**, so pasting into Google Sheets puts each title in its own row. No numbering, no tags inside the block.
- The user may paste tab-separated multi-column lists back (3 channels = 3 columns). Parse columns as separate channels and preserve that grouping in deliverables.
- Keep conversational analysis tight and operator-grade: pattern → evidence (views/age) → what to do with it. No filler.
