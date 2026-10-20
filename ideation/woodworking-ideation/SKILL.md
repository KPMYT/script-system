---
name: woodworking-ideation
description: YouTube ideation system for the operator's four woodworking channels — Dale Oakfield's Workshop (faceless veteran woodworker, now WOODWORKING FOR PROFIT — projects that sell, costs, prices, where to sell), Hank Hardwood (AI-avatar face channel, woodworking for profit, Dale's twin), Master Kenji (Japanese) and Sawdust Sam (Amish/traditional). Holds channel personas and steering, banked formats with examples, the for-profit intake, reference titles with views, the demand map, hard rules and the brief spec. Use it whenever the operator wants woodworking titles, ideas, reworks, reformats or briefs for ANY of the four channels; mentions woodworking for profit, projects that sell, make money woodworking, side hustle, craft fair, Etsy or Marketplace selling in a woodworking context; pastes YouTube screenshots for woodworking analysis; or names Dale Oakfield, Hank Hardwood, Master Kenji or Sawdust Sam — even without the word "ideation". Also use it to bank new winning titles, topics or formats.
---

# Woodworking Ideation — niche overlay

A **thin overlay** on `ideation-core`. Method, format definitions, hard rules, brief spec and output formats live in core; this skill holds what is woodworking-specific: the four channel personas and their steering, audience-in-niche, vocabulary, demand map, evidence, and the produced log.

## 1. Read core first — structural dependency

Before doing anything, read from `/mnt/skills/plugins/ideation-core/references/`:

1. `framework.md` — the atom (proven topic × proven format × channel dials), dials, intake method, channel-normal judgment, the age/views matrix, phases, reformat mode, batch mix.
2. `rules-and-specs.md` — universal hard rules, dial-keyed conditional rules (the **face** rules apply to Hank), brief spec, output formatting (single-column block; Title[TAB]Brief; the three-column Title[TAB]Reference[TAB]Brief variant; `.xlsx` for 30+ briefs).
3. `format-bank-master.md` — the ONE F-namespace. Format definitions exist **only** there (F51 demand-overload and F52 arbitrage gap are woodworking-origin).
4. `audience-profiles.md` — **Profile A** (50+ American DIY homeowner; confirmed shared with plumbing 2026-09-06).

**If core is unreachable, STOP and tell the operator.** Never generate with half a system.

Then read `references/steering.md` (the block for the named channel) and, per task, the files in §5.

## 2. Channels (steering summary)

All four run **browse** on Profile A. Dale, Kenji and Sam are **faceless** (persona in voiceover, compiled footage — titles promise **knowledge, never proof-of-work**). Hank is a **face** channel (AI-avatar presenter) — the avatar never demonstrates; money claims on both for-profit channels are persona verdicts with defensible numbers in the brief. Full blocks in `references/steering.md`.

| Channel | Persona | Register | Home lanes |
|---|---|---|---|
| **Dale Oakfield's Workshop** | veteran American woodworker, ~40 years at the bench, lifelong seller (craft fairs, Etsy, Marketplace) — **pivoted to woodworking-for-profit 2026-09-09** | hustle-thrifty (money-in) | F30 one-unit-to-many, F51 demand-overload, F52 arbitrage, F26 money-key, F3 + sell-framing, F41, F42, F36, **F2 money-key (his differentiator)**; big-box anchors native. His pre-pivot general lane is **parked** (steering §7). |
| **Hank Hardwood** | working American woodworker who earns his living selling what he builds; AI-avatar presenter, persona bible pending | hustle-thrifty (money-in) | the same for-profit lanes minus tenure; F8 decision gate ("Should You Sell…"). Face-dial rules: persona-claim discipline, disclosure, avatar never demonstrates. |
| **Master Kenji** | Japanese master craftsman: precision, sharpening, hand tools, joinery without nails or glue | mastery-precision — never thrift, never money-in | F19 in an Eastern key, F36 ("why the West still…"), F37 ("…from MASTERS"), F22, precision F5/F18, hand-tool F13/F28, F32. No big-box or $5-hack anchors. |
| **Sawdust Sam** | old-order traditional craftsman: hand tools, little or no electricity, built to last generations | heritage-plain — durability, never cheapness, speed or money-in | F19 (his strongest lane, zero fabrication), F2, F29, F4, F21, F26. No big-box, disposable or speed anchors. |

**No default channel — always ask which one** (operator default 2026-09-09; Dale is no longer the general-woodworking home). Dale and Hank are a **channel pair on one topic pool**: format-flip (listicle on one, single on the other), a collision audit before every lock, strong twins split one-topic-per-channel (steering §5).

## 3. Woodworking-specific hard rules (add to core's; never relax core's)

1. **Cultural authenticity is a hard floor.** Japanese joinery and Amish craft are real, richly documented traditions. Exaggerate the framing, never the history: no invented dates, "banned" stories, or fake lineage on Kenji or Sam. On the for-profit channels, heritage keys (Japanese / Amish / Viking / Depression-era) are **territories** the American persona visits — never identity claims.
2. **Persona-lock money language:** Dale runs the earned-income scale plus "$5 board from Home Depot" and "in 40 years of selling"; Hank runs the earned-income scale without tenure; Kenji says "worth every penny"; Sam says "built to last" vs "disposable". Never cross them.
3. **For-profit integrity:** every dollar figure in a title has its cost-and-price math in the brief; income and order figures are persona narrative, never audited fact (no checkable counts, no named customers); **no free plans or lead-magnet promises** (F45 excluded — operator 2026-06-22); no tool-buying titles on the for-profit channels; hourly-wage framing is out.
4. **Safety boundaries inside briefs where relevant:** table-saw kickback (never the rip fence as a crosscut stop; riving knife; push sticks; a sled or stop block for repeated small cuts); oily rags self-ignite; never burn, compost, smoke-cook with, bed animals on, or **sell** sawdust from pressure-treated, MDF, plywood or finished wood; fine dust is a respiratory and explosion hazard; hardwood, food-safe glue and food-safe finish for anything that touches food; lead-paint testing on pre-1978 furniture flips; no small parts on toys for under-threes.
5. **Keep the trim / finish-carpentry adjacency craft-side** (parked lane); pure bathroom / handyman topics are out (steering §7).
6. **"I tested" / "I sell" are persona verdicts, not filmed proof** (presence filter, core `rules-and-specs.md` §2).

## 4. Niche deltas to the core method

- **Age/views matrix, woodworking reading:** recent outlier (≤ ~1–2 years) + big views → keep the creator's own format and exaggerate it harder; older topic (3+ years) + big views → take the topic, re-package it in a different banked format. **For-profit addendum (2026-06-22):** weight the most recent outliers heavily — on that intake the freshest winner (sawdust, 1.7M in four weeks) and the recent demand-overload cluster set the format lean for the whole batch.
- **Intake taxonomy:** own winners (highest value) → "videos your audience watched — last 7 days" → "channels your audience watches — last 28 days". Bias the **topic** source to woodworking creators and woodworking evergreens; formats can come from anywhere proven. Never pull topics from the plumbing system. For-profit sources are recorded in `reference-titles.md` §6 and `archive/`.
- **Fit check adds the channel layer:** topic × format × persona. A "$5 Home Depot 2x4" build is native to Dale, workable on Hank, awkward for Kenji, off-brand for Sam; a lost hand-tool secret is a home run for Sam, strong for Kenji, a territory test on Dale or Hank.
- **Stake factor:** on Kenji and Sam — ruining the project and wasting expensive wood, tool-buying anxiety, amateur shame; on the for-profit channels — "will it actually sell?", the money left on the table, the tool-cost objection.
- **Operator taste on the for-profit channels (two sifts, 2026-09-09):** concept-first profit hooks beat item-price singles; abstract selling advice with no woodworking object fails the sift; "Big Box" adversaries and "40 Years" openers native; amplify counts where the topic carries them, pull them back where it doesn't; CTA tails endorsed.
- **Channel-pair collision audit** (Dale ↔ Hank, steering §5): run it before locking any batch that draws on a shared source set; candidate for a core procedure once a second niche runs a same-source pair.
- **Own-channel ceiling note:** Dale's generic tips listicle topped out around 18k pre-pivot; the first for-profit title to clear that band is the pivot's proof.
- **Batch mix:** core default 50/50; default batch 30; the for-profit channels run listicle-heavy with ~5 heritage-territory test slots; if generating across channels, group or tag by channel.
- **Dedup** against `references/produced-log.md` (four batches logged; views pending on all).

## 5. Which reference to read for which task

| Task | Read |
|---|---|
| Any generation or rework | `steering.md` (named channel's block + table), `examples-by-format.md`, `word-bank.md` (§7 for the for-profit channels), `demand-map.md` (§2b for the for-profit channels), `produced-log.md`, `dead-list.md` |
| Audience questions, brief writing, persona register | `audience.md` (§9 for the for-profit channels) |
| Intake / screenshot analysis, "is this new?" | `reference-titles.md` (§6 for the for-profit pool) and core `framework.md` §3–§5 |
| Thumbnail prompts for a named channel | `niche-packs.md` (loaded by the `thumbnails` skill; Hank's character field is pending) |
| Triage / mining sessions only | `archive/` (raw pre-Session-0 files; `archive/hank-hardwood-intake-2026-06.md` — the 74-title for-profit set; multiplier badges are context, never evidence) |

## 6. Banking

End every session where titles are greenlit with the **banking ritual** (core `filing-rule.md` §2). Produced log always; steering / word-bank / demand-map / dead-list only with view data or an explicit `endorsed` call. New formats go to the core master with the next free F-number (F51 and F52 already live there; next free is F53), never to this overlay. Edits to this skill do not persist in the container — package both `woodworking-ideation` and `ideation-core` with skill-creator's `package_skill` and present the `.skill` files for the operator to save.
