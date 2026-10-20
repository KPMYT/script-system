# Triage — cross-niche inspiration intake

## What a triage session is

The operator feeds any volume of inspiration from any source in one session — screenshots, CSV or scraper exports, pasted title lists, cross-niche outlier dumps, single finds — with or without notes on where things should go. Claude sorts everything into the banks; the operator approves the routing. Mining is the same thing at scale: a big structured export is simply a large triage input.

**A triage chat never generates titles.** It is cross-niche by nature and safe only because nothing in the window can bleed into output. Close it after banking and open a generation chat (one niche) for titles.

Load for triage: `framework.md`, `format-bank-master.md`, `scoreboard.md`, `audience-profiles.md`, `filing-rule.md`, `registry.md`, plus each candidate niche's `steering.md` and `word-bank.md` (not its examples). Raw `archive/` files are loaded only when mining them.

## Per-item procedure

For every input item:

1. **Extract** every transferable asset it contains. A single title often yields a format skeleton, a power word, a topic, a lever and a thumbnail pattern.
2. **Classify** each asset by type — format / word / topic / lever / thumbnail pattern — because the filing rule differs by type.
3. **Fit-check** against candidate destinations: the presence dial (a proof-of-work title may transfer as a format only — `framework.md` §7), the format's fit-requirements in the master, and the destination audience profile. Foreign-niche items (a topic outside every niche we run) lose the topic automatically; only format, word, lever and thumbnail pattern are extracted, weighted by audience overlap.
4. **Check the banks:** already banked (confirms F-n — note the confirmation), a variant (propose a modifier, not a new format), or new (propose the next free F-number from the master header).
5. **Propose destination(s)** per `filing-rule.md`, with evidence, a status tag, and a confidence rating with a one-line reason, so the operator can skim and scrutinize only the low-confidence rows.

Judge every item's performance against its channel's own normal (`framework.md` §5). Rows where that cannot be judged (bare view counts, unknown channel, no age) are flagged **weak evidence**, never silently accepted, and never promote anything to `proven` on their own.

## The approval table

One row per asset:

| # | Asset | Type | Source & evidence (views · age · channel context · tool) | Proposed destination(s) | Status | Confidence | Note |
|---|---|---|---|---|---|---|---|

The operator replies with edits by row number — "3 → also Kenji", "7 → drop", "12 → ALL", "approve rest". Claude then writes the bank diffs grouped by destination file and runs the normal banking ritual (`filing-rule.md` §2).

## Status tags

`proven` (own view data) · `endorsed` (operator's call, no data yet — usable immediately, stays labeled so audits can tell judgment from data; converts to `proven` on the first win) · `candidate` (unvalidated find) · `excluded` (operator ruled it out for this niche — written into that niche's steering as "do not transfer" so future transfer audits never re-propose it).

## Operator annotations

Plain sentences work ("this is plumbing, not fabrics"; "this format goes everywhere"; "strong keyword"). Optional shorthand for speed:

- `ALL:` — format goes to the master, `endorsed` in every niche
- `NOT <niche>:` — exclusion for that niche
- `WORD:` — treat as vocabulary; Claude asks or infers which audience it came from
- `<niche> ONLY:` — file only to that niche

Annotations may also appear inside a single-niche generation chat; the filing rule is global, so Claude files the foreign item to the right bank without loading that niche's examples.

## Volume handling

- Prefer CSV or text over screenshots for large dumps.
- Process in chunks of roughly 30–50 items, each producing its own approval table.
- If the chat grows very long, split into a second triage chat — the banks carry state, not the transcript.
- Keep a running tally of proposed next-F assignments within the session so two new formats never claim the same number; the master header is updated once, at banking.
