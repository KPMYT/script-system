---
name: style-ideation
description: YouTube ideation system for the operator's two 50+ women's style face-persona channels — Scarlett Sterling (ch. 1 — the affluent American; look younger, polished and expensive after 50 — hair, colors, outfits, makeup) and the French persona (ch. 2 — proven style topics re-made as "(The French Way)"; how French women over 50 stay chic, the rules Americans break, less-is-more wardrobes, natural hair, pharmacy beauty). Holds both steering blocks, the French flip recipe, the format table, demand map, audience psychology, hard rules and thumbnail packs. Use whenever the operator wants fashion, style, outfit, wardrobe, hair, haircut, gray-hair, color, makeup, skincare, "look younger", frumpy, elegant, classy, chic, quiet-luxury or old-money titles, ideas, reworks or briefs for women over 50 / 60; mentions the rich American woman, the French channel, French or Parisian women or "the French way"; or pastes screenshots of over-50 style, hair or beauty channels — even without the word "ideation".
---

# Style Ideation — niche overlay (50+ women's style: fashion · hair · color · makeup)

**Version:** the account's copy as synced on 2026-11-17, plus §4b (2026-11-17, P23: briefs that feed the style script rules; style only).

A **thin overlay** on `ideation-core`. The method, the format definitions, the hard rules, the brief spec and the output formats live in core; this skill holds only what is style-specific: the two channels, their steering, audience-in-niche, vocabulary, the demand map, evidence, and the produced log. **Launched 2026-09-14; the first intake (one faceless clone channel "S1" + a 105-row creator sheet) was triaged the same day and both channels' batch 1 (25 titles each) greenlit** — `proven` statuses rest on that ecosystem intake; nothing has own view data yet.

## 1. Read core first — structural dependency

Before doing anything, read from `/mnt/skills/plugins/ideation-core/references/` (older installs: `/mnt/skills/user/ideation-core/references/`):

1. `framework.md` — the atom (proven topic × proven format × channel dials), the dials, intake method, channel-normal judgment, phases, reformat mode, batch mix.
2. `rules-and-specs.md` — universal hard rules, dial-keyed conditional rules (both channels are **face** channels — persona-claim discipline and register lock are on), brief spec, output formatting.
3. `format-bank-master.md` — the ONE F-namespace. Format definitions exist **only** there; titles cannot be tagged without it.
4. `audience-profiles.md` — **Profile C (draft)**: 50+ American woman, style and appearance. Both channels point to it as a **hypothesis**; the first audience-tab screenshot decides whether C stands or collapses into Profile B (the 50+ American woman crafter).

**If core is unreachable, STOP and tell the operator.** Never generate with half a system.

Then read this skill's `references/steering.md` and, per task, the files in §5.

## 2. Channels (steering summary)

Both: **face** (on-camera presenter, real or synthetic TBC, disclosure on if generated) / **browse** / **Profile C (draft)**; footage is presenter + compiled outfit / hair / makeup b-roll, so titles promise **knowledge, never proof-of-work** — no try-ons, no filmed makeovers, no 30-day experiments, no real people's before-and-after photos. Full blocks in `references/steering.md` §1–§2; the two-channel rules in §3.

| Channel | # | Persona · register | Spine | Shelf lane (operator's call, not batch 1) |
|---|---|---|---|---|
| **Scarlett Sterling** (the American affluent woman) | 1 | American, 55–60, wealthy, sophisticated · **polished-affluent** (new register) | **look younger, polished, expensive** — the hairstyles, colors, outfits, makeup and accessories that take years off; what women who look expensive know; the mistakes that age you | elegance and etiquette (posture, manners, hosting — the old-money-behaviors lane) |
| **The French persona** (name TBC) | 2 | French woman, 55–65, Parisian lens · **French-chic** (new register) | **proven style topics re-made as "(The French Way)"** — how French women over 50 stay chic, the rules Americans break (F37c), less-is-more wardrobes, natural hair and gray, pharmacy beauty, the scarf and the trench | the art de vivre (walking, the market, the apartment, the habits beyond clothes) |

**No generation default — always ask which channel** (portfolio convention). Both channels draw on one topic pool: every apex topic can run on both, format-flipped, with a collision audit before every lock (`steering.md` §3). Default launch batch **20 per channel** until each normal is known; ch. 2's launch mix is the Werner mix — roughly 60% proven topics re-made through the lens, 40% national contrast pairs and French-native topics.

## 3. Style hard rules (add to core's; never relax core's)

1. **Never shame the woman.** Every unflattering adjective attaches to the garment, the cut, the color or the habit — "outfits that look cheap", "the haircut that ages you" — never to the viewer or to other women. Banned: trashy, fat, ugly, slutty, "mutton dressed as lamb", and "old lady" / "grandma" as insults (they survive only in quotes as the feared look — "the 'old lady' haircut"). The message is always "nothing is wrong with you; this is what flatters."
2. **No diet, weight-loss, fasting, supplement or exercise-plan content, ever** — the honest lane is dressing and styling the body she has (proportion, fit, fabric, color, cut). "Look slimmer" means silhouette and line, never weight. A walk as a French lifestyle mention is fine; a program is not.
3. **No medical or procedure claims.** Skincare is cosmetic and hedged (SPF, moisture, texture; "talk to a dermatologist" for retinoids and anything prescription); hair thinning is a *styling* topic (cuts and color that read fuller) — never a diagnosis, never a cure; no Botox, filler, surgery, hormone or menopause-treatment advice; no "reverse aging". Age is styled, never treated.
4. **Persona-claim discipline, both channels (face dial):** soft uncheckable backstory only — "in 40 years of dressing for boardrooms and galas", "the way my mother dressed in Paris". No named employers, magazines, maisons, clients, celebrities, husbands' companies, clubs, neighborhoods, boutiques or first-hand dates; wealth is shown and implied, never quantified. No celebrity names in titles by default (checkable, often wrong — operator override only), never a celebrity as the persona's client or friend. **No first-person face-as-proof on a synthetic presenter** (added 2026-09-14): "did I have a facelift?", "what I use to look 20 years younger" turn the generated face into fabricated proof-of-work — the same lever runs honestly in third person ("what women over 70 are using…" · 2.3M).
5. **French claims are real, documented French practice only** (truth doctrine in `steering.md` §2): the capsule and the uniform, buy-less-buy-better, tailoring, the trench and the Breton stripe, the scarf, ballet flats and loafers, neutrals with one accent, no logos, air-dried and low-maintenance hair, gray worn on purpose, the bare face and the red lip, the pharmacy skincare culture. Hedge every generalization ("in Paris", "most Frenchwomen I know", "the way I was raised") — never an invented French rule, law, saying or history; "Americans" only in third person and only as the collective out-group (F37c), never the viewer as adversary; at most **one French word or phrase per title** (chic, Parisian, "je ne sais quoi") and it is a candidate until it wins.
6. **No sexual or suggestive framing.** Necklines, hems, sleeveless and swimwear-adjacent topics run as proportion and comfort advice; thumbnails never show lingerie, cleavage-focused crops or "sexy after 60" hooks.
7. **Brands in text only, never as logos or reproduced designs** in thumbnails (the portfolio's brand-default-off proposal applies); the persona never implies sponsorship or a personal relationship with a house. Naming a famous expensive brand as the benchmark (F13b) is fine.
8. **The age tag is native.** "Women Over 50 / 60 / 70" and "After 60" are the self-selection keys of this niche (the home-security demographic-tag reversal precedent: where the demographic *is* the concern, the tag reads as recognition, not patronizing). Every title carries one age tag unless the operator drops it; "over 60" is the working default (hypothesis — the intake decides which tag the pool runs).
9. **House-style hypotheses:** 1–3 caps words, the thumbnail shouts; US spelling on titles (**gray**, color) unless the intake shows the pool runs "grey"; one age scale per title ("10 years") — never stacked with a money scale.

## 4. Niche deltas to the core method

- **Intake sources, in value order:** own winners (none yet) → the over-50 style channels (faceless narrated listicle channels and real stylist presenters) → over-50 hair channels (hairdressers, the haircut lists) → beauty and skincare adjacents (format and vocabulary mines; topics only into the makeup / skincare-cosmetic lane) → the tradition-key persona networks already logged in core (the Mexican / Japanese / British / German "way" runs, 58k–1.7M — the flip recipe for ch. 2) → "videos your audience watched, last 7 days" → the audience tab (which also settles the profile question).
- **Stake factor:** looking older > looking frumpy or invisible ("given up") > looking cheap > wasted money on the wrong pieces. Vanity and self-image lead; money is the objection-killer (the home-security pattern, not plumbing's). No disgust lever, no emergency lever, no provider frame.
- **The niche's atom (hypothesis):** self-recognition of the aging tell × the insider's authority (the rich woman who knows, the Parisienne who was raised on it) × a concrete, tonight-sized fix (a cut, a color near the face, a third piece, a lip). Every launch batch leads with the "ages you / takes years off" engine (F9 / F27 / F22) re-made through each lens.
- **The age scale (candidate device, core §6):** `Ages You 10 Years` · `Takes 10 Years Off` · `Look 10 Years Younger` · `Instantly Younger` — the niche's stake rung; one per title, defensible as a styling effect, never a medical one.
- **Problem selection inside a proven template:** universality of the tell (gray hair, a thinning crown, the black cardigan, the jeans) × the age stake × how visible the fix is in a thumbnail × how honestly the persona owns it (`references/demand-map.md` §4).
- **Batch mix (operator 2026-09-14):** hair ≈ 40–45% · fashion incl. accessories and color ≈ 40–45% · **makeup ≤ 10–15%, knowledge form only** (the sheet's makeup pool is the deepest — 0.3M–12M — which is exactly why it is capped); core's 50/50 (proven ecosystem topics re-made through the lens / new territory) inside each channel; ch. 2 layers the Werner mix (60 / 40 — re-makes / F37c pairs and French-native topics). The operator's **angle grid** (tricks · mistakes · styles, `demand-map.md` §1b) and **topic matrix** (hair × fashion cells, `demand-map.md` §2) are the batch scaffold. Shelf lanes run only on the operator's call and never enter `demand-map.md`; a shelf lane that clears 1.5× the channel's normal opens the craft-section question via core `launch-playbook.md` §1.
- **The French flip recipe** (operator direction 2026-09-14 — "the inputs will mostly not be French; we flip them"): every non-French winner in an intake is filed as a topic and re-made through five proven lens devices — the series key on a superlative how-to, the in-group plural, the national contrast pair, the tradition-tenure F2, and the rules listicle (`steering.md` §2). Never a topic that no documented French practice supports.
- **Boundary with `fabrics-ideation`:** this niche covers *choosing, wearing and styling* clothes; *making* them (sewing, knitting garments, alterations as a tutorial) is fabrics. "Take it to a tailor" is style; "how to hem it" is fabrics.
- **Dedup** against `references/produced-log.md` (both channels); re-makes across the pair are adjacent by construction and flagged as intentional variants; thumbnails differ even when a topic repeats.

## 4b. Briefs that feed the style script rules (P23, style only)

Added 2026-11-17 for the style channels only (Scarlett Starling, Diane de Chambray): the operator's script decisions after the style upload review. They change nothing for any other niche. Briefs stay facts only (core `rules-and-specs.md` §4); these say which facts a style brief carries so the script can hold them.

- **Each item: the problem first, the answer kept apart** ("we cant have answers be given away early"). Give each item as the problem or question she has, then its answer (the piece, the cut, the color, the swap) as its own fact, so the script names the answer only inside that item. Never open a brief with the one rule that answers the whole title. A "one mistake, then N swaps" brief gives the mistake and a separate answer per swap, never one rule that fixes them all.
- **Each item: something of its own** ("we dont want this: Every tip runs one template"). Give every item at least one fact the others don't have: a moment she has lived, a test she can run in her own closet or mirror, a short true history, a question she'd ask, or what she may keep. Vary them down the list, so no two items next to each other rest on the same kind of fact. No "rule" line per item.
- **Most items: a belief and the truth** ("The voice lost its turns. this is not good"). For most items, not all, say what she has been told or believes about this piece, then the truth: the raw material for the script's turns. Some items carry a different turn instead (the obvious fix and why it fails; a question she'd ask). Never the same kind for every item, or the script turns them into one slot (iter-20: "We believe... But..." in 16 of 17 tips).
- **Makeup tips are fine** inside a fashion or hair brief (operator, 2026-11-17: "i dont care if makeup tips creep in"). The batch-mix cap on makeup titles (§4) stays.
- **Season and repeats:** no summer-only pieces in November to February (or the reverse) unless the title gives the reason (a trip, the season ahead). No two titles on one channel with the same items within two weeks; re-makes across the two channels stay allowed and flagged (§4 dedup).

## 5. Which reference to read for which task

| Task | Read |
|---|---|
| Any generation or rework | `steering.md` (the named channel's block + §3 + §4), `examples-by-format.md`, `word-bank.md`, `demand-map.md`, `produced-log.md`, `dead-list.md` |
| Generating for ch. 2 | additionally `steering.md` §2's truth doctrine and flip recipe, and `audience.md` §6 (the documented French practices) |
| Audience questions, brief writing, persona register, boundaries | `audience.md` |
| Intake / screenshot analysis, "is this new?", the first triage session | `reference-titles.md` and core `framework.md` §3–§5, `triage.md` |
| Thumbnail prompts for a named channel | `niche-packs.md` (the `thumbnails` skill loads this) |
| Triage / mining sessions only | `archive/` (raw intake with badges — never evidence, context only) |

## 6. Banking

End every session where titles are greenlit with the **banking ritual** (core `filing-rule.md` §2): propose the diff by destination file, the operator approves line by line, then write. Produced log always; steering, word-bank, demand-map and dead-list entries only with view data or the operator's explicit `endorsed` call. New formats go to the core master with the next free F-number (F53) — never to this overlay. **Status:** the launch intake was triaged 2026-09-14 (66-row table; data-backed and operator-endorsed rows banked; the F45 / F46 / F48 / F51 / F52 exclusions stay *proposed* until confirmed); batch 1 on both channels is the acceptance test — the first view data rebuilds `steering.md` §4 and the core scoreboard column. Two candidate devices wait on evidence: the age scale (§4) and the observer's-eye expression of F10 ("things people notice first") — never proposed as formats without a winning title.
