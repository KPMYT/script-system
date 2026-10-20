# Launch Playbook — new niches and new channels

## Table of contents
1. The niche boundary rule (what gets its own skill)
2. Launching a new niche
3. Overlay template
4. Adding a channel to an existing niche
5. Inheritance defaults

---

## 1. The niche boundary rule

**Four levels.** Profile (core) = who is watching; never defines a niche. Niche skill = a topic world: one demand map, one word bank, one steering evidence base. Craft section = files inside a niche skill (knitting vs crochet). Channel steering block = persona + dials + angle + batch mix.

**Same-skill test** (mostly yes → same niche skill; mostly no → separate skill):
1. **Demand-map test** — would the two pull ~70%+ of their topics from the same pool?
2. **Bleed test** — would one's example titles in the context window make the other's output better or worse?
3. **Word-bank test** — shared working vocabulary?

**Standing rulings.**
- Angles and monetization variants (woodworking-for-profit, plumbing-for-landlords) = channel steering blocks in the existing niche, never new skills.
- Adjacent crafts in the same world (embroidery → fabrics) = a new craft section.
- New topic worlds (gardening, blacksmithing) = a new niche skill, inheriting the shared profile and the nearest sibling's psychology as hypotheses.
- Audience differences alone never split a niche — that is what profiles are for.
- **National-lens persona channels** ("the German way", "the Italian way") = channel steering blocks in the niche whose topics they re-make (ruling 2026-09-07, Werner Finkbinder in plumbing), with a truth doctrine of real documented practice only and a labeled probe lane for adjacent topics; the probe lane graduates to a niche question only when probes clear the channel's normal and pass ~30% of its demand.

- **Multi-persona channel sets in one topic world** (ruling 2026-09-11, the home-security launch — Navy, Fireman, Locksmith) = **one niche skill** with per-persona steering blocks, a **persona-ownership split** of the shared topic pool (each proven topic has a natural owner; apex topics run on every channel with the format-flip and a collision audit), and **per-channel lanes** for the persona's adjacent world (fire safety, "not tracked") held in their own lane files inside the overlay — never in `demand-map.md`. A lane that clears 1.5× its channel's normal opens the multi-craft question (a craft section inside the skill); it becomes a separate skill only through the escape valves below.

- **A national-lens persona launched inside a brand-new niche** (ruling 2026-09-14, the French persona at the style launch) = the niche skill is created for the topic world and the lens persona is one of its steering blocks from day one, inheriting Werner's doctrine; the non-lens sibling channel owns the pool's American-native lanes (occasions, body-shape vocabulary, color analysis), the lens channel the practices its culture documents (the capsule, the scarf, the bare face). The two may run one topic set as intentional twins on the operator's call, format-flipped, thumbnails from different packs.

**Escape valves.** Promote a craft section to its own skill only when its steering becomes mostly exceptions to the shared rules, or its files grow so large that sessions load mostly irrelevant material. Merge a skill back when it is too thin to earn its overhead. Apply at launches and at compression audits; data decides.

## 2. Launching a new niche

1. **Boundary check** (§1). Confirm it is a new topic world, not a channel angle or a craft section.
2. **Profile.** Point to an existing profile if the audience tab shows the same adjacent channels as an existing niche; otherwise draft a new thin profile (values, tone limits, candidates only) and flag it.
3. **Kinship.** Name the nearest sibling persona/register in `kinship-map.md`; its niche psychology becomes the new overlay's `audience.md` as **labeled hypotheses**.
4. **Build the overlay** from the template (§3): copy the skill to a working directory, keep `SKILL.md` under 200 lines, and write the first instruction as "read core first".
5. **Steering.** One block per channel; every format row starts `inherited` (from the master, with the sibling's status as the hypothesis) until ~20 local datapoints exist. Dead-in-sibling formats start `untested`, not dead.
6. **Register it:** `registry.md` line, `scoreboard.md` column (all `inherited` / `untested`), `kinship-map.md` line, and a NICHE PACK in the overlay's `niche-packs.md` for the `thumbnails` skill.
7. **First evidence.** The first intake session for the niche runs as a triage session (`triage.md`) against the new overlay; the first live batch is the acceptance test.
8. **Package** with skill-creator's `package_skill` and present the `.skill` file; the operator clicks Save skill.

## 3. Overlay template

```
<niche>-ideation/
├── SKILL.md                      (< 200 lines)
│   frontmatter: name, pushy description naming every channel and persona
│   1. Read core first: framework.md, rules-and-specs.md, format-bank-master.md,
│      audience-profiles.md (the relevant profile). If core is unreachable, STOP
│      and tell the operator — never generate with half a system.
│   2. Channel steering summary (one line per channel: persona, dials, register)
│   3. Niche-specific hard rules (add to, never relax, the universal ones)
│   4. Niche deltas to the method (intake sources, stake factor, mix overrides)
│   5. Pointers: which reference to read for which task
└── references/
    ├── steering.md               per-channel blocks: persona, dials, profile pointer,
    │                             batch mix, format steering table (per F-number:
    │                             proven with evidence / untested / dead / endorsed /
    │                             inherited / excluded), topic boundaries. Canonical
    │                             source for the scoreboard.
    ├── examples-by-format.md     ≥1 real niche title per proven format, by F-number
    ├── audience.md               how this viewer shows up here: mode, lever ranking,
    │                             dead levers, money/time language, adversaries,
    │                             real mechanisms, safety boundaries
    ├── word-bank.md              niche vocabulary + modifier phrases + `candidates`
    ├── demand-map.md             topic demand map + seasonal calendar
    ├── reference-titles.md       distilled: proven titles per cluster, views, lesson
    ├── produced-log.md           greenlit/produced titles only; >18 months → archive/
    ├── dead-list.md              dated, evidence count, re-test-after date
    ├── niche-packs.md            per-channel thumbnail NICHE PACK
    └── archive/                  raw datasets; loaded only in triage/mining sessions
```

Multi-craft niches split craft-specific references per craft (`word-bank-knitting.md`, `demand-map-knitting.md`, …) or per-craft sections with a TOC, so a session loads only the active craft plus the shared files.

## 4. Adding a channel to an existing niche

1. **Steering block** in the overlay's `steering.md`: persona, dial values, profile pointer, register, batch mix, footage capability, topic boundaries, and a format steering table copied from the nearest sibling channel with every row relabeled `inherited`.
2. **NICHE PACK** in the overlay's `niche-packs.md` (character description, common objects/materials/settings, banned items, style tweaks) for the `thumbnails` skill.
3. **Registry line** in `registry.md`.
4. **Scoreboard** — no new column (columns are niches), but note the channel in the niche's data-pending line.
5. Kinship line only if the persona/register is new to the map.

## 5. Inheritance defaults

New channels inherit the **profile as facts** and the **nearest sibling's niche psychology as labeled hypotheses**; steering is set to `inherited until ~20 local datapoints`. Inherited rows are usable immediately — the label exists so audits can tell inheritance from evidence, and so the first ~20 datapoints are read as the test they are.
