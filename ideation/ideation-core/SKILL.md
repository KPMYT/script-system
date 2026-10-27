---
name: "ideation-core"
description: Shared brain for the operator's YouTube ideation portfolio (plumbing, HVAC, woodworking, fabrics, home security, style, air travel, animals) — the one master format bank (F-numbers), scoreboard, universal rules, audience profiles, filing rule, registry, launch playbook and triage procedure. The niche overlays read it automatically, so do NOT use it for an ordinary single-niche title, brief or reformat request — the overlay is the entry point. DO use it, even unnamed, for anything portfolio-level or cross-niche — launching a new niche or channel; transfer audits or scoreboard rebuilds; compression or maintenance of any ideation skill; F-number questions (next number, deprecation); audience profiles or "same audience?"; cross-niche questions ("does this format work in woodworking too"); "which skill should I use"; and every triage session — any inspiration dump, scrape, CSV, screenshot set spanning more than one niche, a multi-niche outlier list, or "sort these", "where should these go", "file these", "triage".
---

# Ideation Core

The shared brain of the portfolio. Every niche overlay reads this skill first and adds only its niche on top. Core is never used alone for daily ideation — it is the entry point for portfolio-level work: triage, launches, audits, maintenance, F-number administration, audience profiles, and routing questions.

**Granularity rule:** skill per niche · channel per steering block · audience per thin profile in core.

## Which skill? (route first)

| The operator wants… | Use |
|---|---|
| Titles, briefs, reworks, reformats, screenshot analysis for one niche | that niche's overlay (`plumbing-ideation`, `hvac-ideation` — Roger the HVAC Guy, `woodworking-ideation` — incl. the for-profit channels Dale Oakfield's Workshop and Hank Hardwood, `fabrics-ideation`, `home-security-ideation` — the Navy, Fireman and Locksmith face channels, `style-ideation` — Scarlett Sterling and the French persona, 50+ women's style, `air-travel-ideation` — the Flight Attendant channel, flying advice and airline exposés) — it loads core itself |
| Thumbnail prompts, thumbnail revision | `thumbnails` (loads the channel's NICHE PACK from the overlay) |
| An inspiration dump / scrape / outlier list spanning more than one niche; "sort these" | core → `references/triage.md` |
| A new niche or a new channel | core → `references/launch-playbook.md` |
| Transfer audit, scoreboard rebuild, compression, skill cleanup | core → `references/filing-rule.md` + `references/scoreboard.md` |
| F-number questions, next free number, deprecation | core → `references/format-bank-master.md` header |
| Audience / profile questions | core → `references/audience-profiles.md` |

If a request is ambiguous between generation and triage, ask one question: "Titles out, or sort into the banks?" — the answer decides the session type.

## Session types

- **Triage** — anything in, sorted to banks, cross-niche, **never generates titles**. Close it after banking.
- **Generation** — one niche per chat, titles out. Overlay is the entry point.
- **Thumbnails** — the `thumbnails` skill.
- **Maintenance** — audits, compression, launches, rule changes. Core is the entry point.

## What to read for each task

| Task | Read |
|---|---|
| Any ideation (via an overlay) | `framework.md`, `rules-and-specs.md`, `format-bank-master.md`, the relevant profile in `audience-profiles.md` |
| Triage | the above + `scoreboard.md`, `filing-rule.md`, `registry.md`, `triage.md`, then each candidate niche's `steering.md` and `word-bank.md` (never its examples) |
| Launch a niche / add a channel | `launch-playbook.md`, `registry.md`, `kinship-map.md`, `audience-profiles.md`, `scoreboard.md` |
| Transfer audit | every overlay's `steering.md` → rebuild `scoreboard.md`; propose transfers for formats `proven` in one niche and `untested`/`inherited` in another, skipping `excluded` cells |
| Compression audit | `launch-playbook.md` §1 escape valves; check every SKILL.md < 200 lines (core < 150), every reference > 300 lines has a TOC, `produced-log.md` entries > 18 months moved to `archive/` |
| F-number administration | `format-bank-master.md` header (next free number); numbers are immutable — deprecate, never renumber or reuse |
| Rule change | `rules-and-specs.md` — **ask the operator first**, then add a dated changelog line |

## Non-negotiables (do not change without the operator)

Topic × format as the atom · banked formats only (no invented formats without winning data or a tagged operator endorsement) · performance judged against the channel's own normal, never raw views and never tool-reported outlier scores · exaggerate-but-defensible · brief spec (facts only, one paragraph, one cell) · produced-title dedup · reformat mode · operator as final curator · thumbnails rulebook and revision loop · one niche per generation chat · F-numbers immutable · the topic-batched generation layout — sources and their age/views verdicts on top, every title tagged `Exaggerated` / `Reformat` / `New` with the topic's and the format's source views (`rules-and-specs.md` §5) · initial batches 80–85% on winning topics (`framework.md` §10).

## Maintenance procedures (short form)

- **Banking ritual** (end of every session, any type): propose the diff labeled by destination file; operator approves line by line; write. Produced log always; everything else only with view data or an explicit `endorsed`. Template in `filing-rule.md` §2.
- **Transfer audit:** read every overlay's steering, rebuild the scoreboard cache, list formats proven somewhere and untested elsewhere, propose transfers with evidence, honor every `excluded` cell. Steering is canonical; the scoreboard is a cache.
- **Candidate tests:** at most two titles per candidate, test channel chosen per test, results judged against that channel's normal, promote at one clear win (default 1.5×), drop at two comparable misses. `filing-rule.md` §3.
- **Status tags** everywhere: `proven` · `endorsed` · `candidate` · `inherited` · `untested` · `dead` · `excluded`.

## Reference map

- `references/framework.md` — the doctrine: the atom, the three dials, intake method and the canonical intake record, performance judgment, the age/views matrix, presence filter, phases, reformat mode, batch mix, standing doctrine, session types.
- `references/format-bank-master.md` — the one F-namespace, F1–F57 plus sub-letters (F3b, F3c, F5b, F7b, F13b, F13c, F19b, F27b, F37b, F37c) and one held candidate (product villain), skeletons with placeholders, drivers, fit-requirements, origin and founding evidence; modifier families; next free number in the header.
- `references/scoreboard.md` — format × niche status cache; rebuilt from overlay steering at every transfer audit.
- `references/rules-and-specs.md` — universal hard rules, dial-keyed conditional rules, house style, brief spec, output formatting (incl. the standing topic-batched generation layout), dated changelog.
- `references/audience-profiles.md` — thin profiles A and B, drafts C (style), D (air travel) and E (pet owners — animals dogs and cats); the two-channel promotion rule; the aesthetic-girly register note; the cross-audience universal word list.
- `references/filing-rule.md` — learning → destination table, banking ritual template, candidate test protocol, thumbnail seed.
- `references/kinship-map.md` — persona/register siblings.
- `references/registry.md` — every niche skill: path, channels, dials, footage capability, profile pointers, standing test-default channel.
- `references/launch-playbook.md` — the niche boundary rule, new-niche procedure, overlay template, add-a-channel procedure, inheritance defaults.
- `references/triage.md` — the cross-niche intake procedure and approval table.

## If an overlay cannot reach core

Format definitions exist only here, so titles cannot be tagged without core. An overlay that cannot read these files must STOP and tell the operator — never generate with half a system.
