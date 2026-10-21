---
name: "plumbing-ideation"
description: YouTube ideation system for the user's plumbing channels (Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter, and Werner Finkbinder — the German-way face persona that re-makes proven plumbing winners as "(The German Way)" and probes HVAC, pest and home-DIY topics through the lens). Contains the banked winning title formats (F1–F57), word banks, reference titles with view data, audience psychology, the topic demand map, hard title rules, and the video-brief spec. Use this skill whenever the user asks for plumbing video titles, video ideas, ideation, title reworks or reformats, video briefs, or pastes YouTube screenshots (their own channel, competitor channels, or audience-tab data) for analysis — even if they never say the word "ideation". Also use it whenever the user mentions Werner, the German way, or wants a tradition-key (Mexican / Japanese / British way) title re-made for plumbing. Also use it when the user wants to add newly discovered winning titles, topics, or formats to the bank.
---

# Plumbing Ideation — niche overlay

This is a **thin overlay** on `ideation-core`. The method, the format definitions, the hard rules, the brief spec and the output formats live in core; this skill holds only what is plumbing-specific: channels, steering, audience-in-niche, vocabulary, demand map, evidence, and the produced log.

## 1. Read core first — structural dependency

Before doing anything, read from `/mnt/skills/plugins/ideation-core/references/`:

1. `framework.md` — the atom (proven topic × proven format × channel dials), the dials, intake method, channel-normal judgment, phases, reformat mode, batch mix.
2. `rules-and-specs.md` — universal hard rules, dial-keyed conditional rules, brief spec, output formatting.
3. `format-bank-master.md` — the ONE F-namespace. Format definitions exist **only** there; titles cannot be tagged without it.
4. `audience-profiles.md` — **Profile A** (50+ American DIY homeowner). All plumbing channels point to it.

**If core is unreachable, STOP and tell the operator.** Never generate with half a system — an overlay without the master bank cannot tag formats, and untagged titles cannot be banked.

Then read this skill's `references/steering.md` and, per task, the files in §5.

## 2. Channels (steering summary)

Channels 1–3: **faceless** (persona lives in voiceover) / **browse** / **veteran-tradesman** / **Profile A**; footage is compiled b-roll, so titles promise **knowledge, never proof-of-work**. Channel 4 (Werner) is the niche's first **face** channel: presenter + compiled b-roll, still knowledge only, with the face-dial rules (persona-claim discipline, register lock) switched on. Full blocks in `references/steering.md`.

| Channel | # | Notes |
|---|---|---|
| **Roger the Pipe Guy** | 1 | The evidence base: every own-channel winner in the files is his. Persona: veteran plumber, 45 years — the honest insider breaking ranks. |
| **Mark Silverbridge** | 2 | Faceless sibling; the June 2026 batch skewed water heaters. Steering **inherited** from Roger until ~20 local datapoints. |
| **The Vintage Pipefitter** | 3 | Faceless sibling; runs "45 years". Steering **inherited** from Roger until ~20 local datapoints; first own datapoint 148k (limescale). |
| **Werner Finkbinder** | 4 | **Face** persona (talking head): German Meister plumber re-making proven plumbing winners as "(The German Way)" and testing HVAC / energy / pest / home-DIY probes through the lens. Dials: face / proven topics re-made through the lens / **German-precision**. Steering **inherited** from Roger; first batch of 14 greenlit 2026-09-07. Tenure number, presenter type and collab tag still open — see `steering.md` §4. |
| *(one more launching)* | — | Add via core `launch-playbook.md` §4: steering block + niche pack + registry line. |

**No generation default.** When no channel is named, **ask which channel** before generating (operator call, 2026-09-06). Variants of one concept across channels (different counts, different angles) are normal and intentional — the ecosystem openly clones winners across channels, and it works.

## 3. Plumbing-specific hard rules (add to core's; never relax core's)

1. **Honest persona version of every suppression / lost-wisdom format.** Roger IS the old-timer, so F19/F21/F22/F29 run as "the trick plumbers used before drain cleaner existed", never as invented dates, buried documents or fake bans. Real code stories (S-traps, saddle valves, polybutylene, galvanized, lead solder, Orangeburg) are the honest ammunition.
2. **Water damage is the apex fear; money is the most-used lever.** Every brief carries real dollar anchors (service-call costs, part prices, "$400 to a plumber vs $6 in parts").
3. **Safety boundaries inside briefs where relevant:** gas lines are never DIY push-fit territory; never mix cleaning chemicals (bleach + ammonia, peroxide + vinegar in-pipe); boiling-water cautions on porcelain and PVC; wet-rated vacs only around water. The persona's trust is the channel's moat.
4. **Explicit demographic tags ("Safe for Seniors") are candidates only** — they can land as targeted or patronizing. Test deliberately, never by default.
5. **"I tested" framings are persona verdicts** ("After 45 years, here's which one I trust"), never filmed experiments (presence filter, core `rules-and-specs.md` §2.3).
6. **Werner's German claims are real, documented German practice only** (truth doctrine in `steering.md` §4): hedged community claims ("the way I was trained", "most German homes"), never an invented ban or law, no named towns, employers or dates, at most one German word per title, and one constant tenure number once it is fixed. German is the persona's origin and a method territory, never a claim that Americans are the adversary — the adversary stays the shortcut, builder grade and big box.

## 4. Niche deltas to the core method

- **Intake sources, in value order:** Roger's own winners → direct faceless plumbing comps → audience-overlap channels (pest, cleaning, lawn, energy, appliances: the same homeowner defending the same castle) → mega-pool evergreens (old + huge = durable demand) → "videos your audience watched, last 7 days" (the hottest live signal; act fast on ride-the-wave topics).
- **Stake factor:** flood / burst / sewage / the plumber's invoice. Disgust is plumbing's unfair advantage (gunk, grease, biofilm) and pairs with F20 causal horror.
- **Problem selection when slotting a topic into a proven template:** how universal × how disgusting or annoying × how frequent × how expensive the pro fix. Universality sets the ceiling.
- **Batch mix:** core default 50/50 (doubling down on own proven topics × formats / new territory from the demand map and transferred formats). Default batch 30.
- **Re-attacks are standing strategy:** every own topic has a higher-ceiling angle available (see the head-to-heads in `references/reference-titles.md` §5).
- **Dedup** against `references/produced-log.md` (all channels); adjacent angles on a produced topic are fine. Werner's re-makes of sibling winners are adjacent by construction (the face-twin doctrine: re-produce, never re-upload) and are flagged as intentional variants in the log.
- **Werner's probe lane** (HVAC, energy, mold, pest, home DIY) is a channel-level test, not a plumbing topic source: probe topics live only in his steering block, never in `demand-map.md`; if probes clear his normal and pass ~30% of his demand, open the home-DIY-niche question via core `launch-playbook.md` §1.

## 5. Which reference to read for which task

| Task | Read |
|---|---|
| Any generation or rework | `steering.md` (the block for the named channel), `examples-by-format.md`, `word-bank.md`, `demand-map.md`, `produced-log.md`, `dead-list.md` |
| Audience questions, brief writing, persona register | `audience.md` |
| Intake / screenshot analysis, "is this new?" | `reference-titles.md` (distilled evidence + lessons) and core `framework.md` §3–§5 |
| Thumbnail prompts for a named channel | `niche-packs.md` (the `thumbnails` skill loads this) |
| Triage / mining sessions only | `archive/` (raw pre-Session-0 files, multiplier badges included — never evidence, context only) |

## 6. Banking

End every session where titles are greenlit with the **banking ritual** (core `filing-rule.md` §2): propose the diff by destination file, the operator approves line by line, then write. Produced log always; steering, word-bank, demand-map and dead-list entries only with view data or the operator's explicit `endorsed` call. New formats go to the core master with the next free F-number — never to this overlay.
