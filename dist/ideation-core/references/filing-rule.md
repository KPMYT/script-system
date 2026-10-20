# Filing Rule — where every learning goes

## 1. Learning → destination

| Learning | Goes to |
|---|---|
| New format | core `format-bank-master.md` (next free F, origin tag, founding evidence) + `scoreboard.md` cell + overlay `steering.md` row + overlay `examples-by-format.md` entry |
| Format proven or dead in a niche | overlay `steering.md` (+ `scoreboard.md` cell at the next rebuild; a dead format also gets a dated `dead-list.md` entry) |
| Niche word or modifier phrase | overlay `word-bank.md` |
| Audience-bound word (audience-tab find) | profile `candidates` in `audience-profiles.md` → `proven` once validated by the operator's own titles |
| Word proven on two channels serving the same audience (any niches) | profile `proven` list in `audience-profiles.md` |
| Word proven for both audience profiles | cross-audience universal list in `audience-profiles.md` |
| Topic | overlay `demand-map.md`. Topics never cross niches. |
| Greenlit title | overlay `produced-log.md` (greenlit / produced only, never every candidate; entries older than 18 months move to `archive/`) |
| Repeated flop | overlay `dead-list.md` — dated, with evidence count and a "re-test after" date; suppresses default generation only, never an explicit request |
| Rule change | core `rules-and-specs.md` + a dated changelog line — **ask the operator first** |
| New channel | overlay `steering.md` block + overlay `niche-packs.md` pack + `registry.md` line + `scoreboard.md` column check |
| New niche | new overlay via `launch-playbook.md` + `registry.md` + `kinship-map.md` + `scoreboard.md` column (+ a new profile only if the audience is new) |
| Thumbnail mechanic | `thumbnails/references/pattern-bank.md` (deconstructed with data; promoted to a thumbnails rule only after repeating across niches) |
| Source reference on any banked format or topic | the **full source video title + views** (never shorthand) wherever a format or topic is referenced — master bank, steering, examples, demand map, produced log, briefs, thumbnail seeds — so the thumbnails skill can find the source thumbnail by name (operator call 2026-09-07). Where a bank holds only a shorthand (e.g. "peroxide down every drain tonight" · 372k), say so and correct it when the exact title arrives |
| Collab credit on an intake item | the `collab credit` field of the intake record (`framework.md` §4); it changes which channel's normal the item is read against |

**Status tags** used on every banked entry: `proven` (own view data) · `endorsed` (operator's call, no data yet — usable immediately, stays labeled, converts to proven on the first win) · `candidate` (unvalidated find) · `excluded` (operator ruled it out for this niche; written into that niche's steering as "do not transfer" so audits never re-propose it) · `inherited` (carried from a sibling with no local data) · `dead`.

## 2. Banking ritual (end of every session)

Run it whenever titles are greenlit, and prompt for it if the operator has not asked.

1. Propose the diff, labeled by destination file, in this shape:

```
BANKING PROPOSAL — <niche> — <date>
produced-log.md        + <greenlit titles, channel, date, format tags>
steering.md            <F-n>: <old status> → <new status> — evidence: <title · views · age · channel normal>
demand-map.md          + <topic> (<evidence>)
word-bank.md           + <word/phrase> (<source>)
dead-list.md           + <pairing> — <evidence count> — re-test after <date>
format-bank-master.md  + F<next> <name> — origin <niche> — founding evidence <…>   [core]
audience-profiles.md   candidate: <word> (<profile>, <tab find>)                     [core]
rules-and-specs.md     <proposed rule change> — needs your approval                  [core]
```

2. The operator approves line by line (or "approve all").
3. Write only what was approved.

**Source-reference convention (operator call 2026-09-07):** every proposal line that cites a source video names it by full title and views.

**Evidence threshold:** the produced log is always written. Everything else is written only with view data (`proven`) or the operator's explicit call (`endorsed`). Never promote on a not-assessable item.

## 3. Candidate test protocol

- A candidate (format, word, topic pairing) gets **at most two test titles**, on whichever channel the operator picks at batch time. Claude flags pending candidates relevant to the current channel and offers test titles; a niche may keep a standing default test channel (`registry.md` — fabrics: Crochet Decoded) but the choice is always per test.
- Record with each entry: the test channel and its dial values. Results are judged against **that channel's own normal**; a fail under one dial setting (for example on a face channel) does not kill the candidate for the other setting.
- **Promote** after one win clearly above the channel's normal — default 1.5×, overridable per channel in steering.
- **Drop** after two misses across comparable tests (same dial values); write the dead-list entry with a re-test date.

## 4. Thumbnail seed

Emitted for greenlit titles only, one line each, alongside the produced-log entry: **proof moment + layout hint + reference pointer** (a banked anatomy or pattern from `thumbnails/references/pattern-bank.md`). It is context for the `thumbnails` skill's SEED field, not a directive — the concept engine still runs in full.
