---
name: claims-policy
description: What a persona may and may not claim, on every channel: opinions versus checkable life facts, permitted personal details, health, guarantees, and named companies. Applies to every script, description and pinned comment. Sits above niche packs and persona profiles, which can tighten it but never loosen it.
---

# Claims policy

**Where this file sits.** Above everything else. Niche packs and persona profiles can tighten these rules but never loosen them, apart from the one approved family detail, the one approved heritage line and the fixed years in the trade below. Claims about offers are covered in `offer-rules.md`. The limits on exaggeration and framing are in `research-and-sourcing.md`, section 2.

---

## The persona is a narrator and a curator

**Always allowed:**
- opinions ("I'd skip the stain on this one")
- preferences, reactions and enthusiasm
- honest tradeoffs and limits

**Allowed only when the persona profile lists them:** soft personal details nobody could check, such as a catchphrase, a pet's name, or a sign-off. The narrator mentions no personal detail that isn't on the profile's list.

**Never allowed** (checkable life facts the persona doesn't have):
- ages, named relatives, heritage or identity membership (except the profile's approved family detail and heritage line, below)
- years of experience (except the profile's fixed figure, or the locked title's, below) or credentials
- places worked or lived, employers, towns
- having personally made, sold, tested, built, lived or collected something
- customers, orders, sales, income or results

**Build narration.** Steps are instructions to the viewer, never "I'm cutting" or "watch me," unless a niche pack explicitly allows first-person demonstration.

---

## Health

- **No health, efficacy, treatment or prevention claims of any kind,** in any niche.
- **Practical safety guidance is not a health claim and stays in:** wear a mask, let the blade stop, keep chemicals apart.

## Guarantees

- **No guarantees** of money, results or outcomes. Money is always conditional ("if they sell"), and time is always an estimate.

## One approved family detail

A persona profile may name one fixed, soft family detail that the operator has approved (for example, "learned at his grandfather's bench"), used only as the profile words it and as often as it allows. This is the only exception to "no invented family or history", and nothing beyond it is ever invented.

## One approved heritage line

A persona profile may name one fixed, soft heritage line that the operator has approved (for example, "grew up in Germany, where water and heating cost real money"), used only as the profile words it and as often as it allows. It never comes with a town, a date, an employer, a licence or a named teacher, and nothing beyond it is ever invented. (P14, operator 2026-10-27, for Werner Finkbeiner: "allow it".)

## Fixed years in the trade

A persona profile may set one fixed years-in-the-trade figure on its `tenure:` line, approved by the operator. The script may say it, the same way every time. When the locked title states a different years figure, the script may use the title's figure instead (title numbers win). With `tenure: none`, the title's figure is the only one the script may say. It never comes with dates, employers, towns, licences or other credentials, and it is never proof that the persona personally made or tested anything. The scanner fails any figure that is neither the profile's nor the title's.

## Named companies and people

- **Neutral mentions are fine:** where to buy, which product is used.
- **Casting a company or category as the villain is fine as tone** ("the big stores would rather you didn't know this").
- **Nothing false or unsupported is ever stated as fact** about a named company or person.

## Who checks it

- `greenlight-audit.md` checks this in F5.
- Niche packs add their own bans in their `scanner` block, such as first-person build lines.
