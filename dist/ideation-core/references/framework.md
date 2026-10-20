# Framework — the shared ideation doctrine

Read this before any ideation session in any niche. It is the method; the overlay supplies the niche.

## Table of contents
1. The atom: proven topic × proven format × channel dials
2. The three universal dials
3. Intake — how evidence enters
4. The canonical intake record
5. Judging performance (and why tool outlier scores are excluded)
6. The age/views matrix, outliers, and head-to-heads
7. The presence filter
8. Phases of a generation session
9. Reformat mode
10. Batch mix and batch size
11. Standing doctrine (lessons that repeat across niches)
12. Session types and the one-niche rule

---

## 1. The atom

Every video is **proven topic × proven format × channel dials**. Topics and formats are separate variables and are always extracted separately: a winning title teaches a *topic that has demand* and a *structure that packages demand*, and the two transfer independently. Formats live once, in `format-bank-master.md`, and transfer across niches; topics never cross niches and live only in the overlay's demand map. The channel's dials (below) decide which pairings read native.

Do not invent formats. Experimental titles are recombinations of banked formats and proven topics. A new format enters the master only from new winning data or an explicit operator endorsement, tagged as such (see `filing-rule.md`).

## 2. The three universal dials

Every channel in the registry has a value on each dial. Overlays record the values in `steering.md`; the values switch conditional rules on and off (see `rules-and-specs.md` §2).

- **Presence** — *faceless* (persona or brand voice in voiceover; footage compiled or from an owned hands library) or *face* (an on-camera presenter). Presence decides what a title may promise (§7) and whether persona claims are allowed.
- **Demand shape** — *browse* (the click is won in the feed: listicles, exposés, warnings, curiosity) or *search* (the click is won on a query: follow-along tutorials, "how to X", decision versus). Most channels are one or the other; some run a fixed mix (recorded as the channel's batch mix). Search titles keep the query intact; browse titles exaggerate freely.
- **Register** — the channel's locked voice: veteran-tradesman, friendly-thrifty, mastery-precision, heritage-plain, granny-cozy, neutral-clean, aesthetic-girly, and so on. Register decides vocabulary and money language, and is never mixed on one channel.

Audience (who is watching) is not a dial — it is a profile pointer in the registry (`audience-profiles.md`). How that viewer shows up in a niche lives in the overlay's `audience.md`.

## 3. Intake — how evidence enters

Process each batch as it arrives; do not generate titles until asked. Inputs arrive as screenshots, scraper sheets, CSV exports, pasted title lists, or single finds, with or without operator notes.

- Transcribe every title with whatever is visible: views, age or upload date, channel, subscriber count, source tool. Do not ask the operator for fields that are not there — extract what is present, mark the rest unknown (§4), and weight the evidence accordingly. Incomplete items are processed, not rejected.
- Extract two separate things from every item: **topics that work** and **title structures that work**. Compare each against the banks: what confirms an existing F-number, what is a variant (propose a modifier, not a new format), what is new (propose the next free number).
- Know the intake taxonomy. The operator's **own-channel winners** are the highest-value data of all. "Videos your audience watched — last 7 days" is the hottest current signal and identifies ride-the-wave topics to act on fast. "Channels your audience watches — last 28 days" is the adjacent-demand pool: topics and format inspiration. Competitor and adjacent-niche data is inspiration to adapt, never a topic source for another niche.
- Bias the topic source to the niche being worked. Formats can be pulled from anywhere proven — the master bank, any sibling's steering, or a fresh screenshot (tag those *src*). Topics come only from the niche's own ecosystem and evergreens.
- If a scrape lacks upload dates, say so: the age/views matrix cannot run without them, so treat its topics as durable-demand signals and its packaging as unverified-freshness.
- Propose bank additions with the next free F-number and offer the banking ritual (`filing-rule.md`) so the banks stay current.

## 4. The canonical intake record

This is a target structure for Claude, never a form for the operator. For every item, Claude fills what it can:

| Field | Notes |
|---|---|
| title | verbatim |
| channel | name; note if it is the operator's own |
| views | as shown |
| upload date / age | date if visible, else age ("3y", "2 wks"); else unknown |
| channel size | subscribers if visible; else unknown |
| source tool | screenshot type, scraper, audience tab, own analytics; else unknown |
| date observed | today's date when the item entered |
| collab credit | other channels named in the byline ("and Roger the Pipe Guy", "and 2 more") — YouTube's collaboration credit pushes the video into every credited channel's feeds and confounds the channel-normal read; record it, and read the video against the largest credited channel when in doubt (added 2026-09-07; the Vintage byline that prompted it is still TBC) |

An item with only a title and a view count is still processed — it is simply weak evidence, and is flagged as weak rather than silently accepted.

## 5. Judging performance

Performance is always judged **against the channel's own normal**, never against raw view counts and never against tool-reported outlier scores.

- **Tool-reported outlier scores (multipliers, "31x", VPH badges, outlier ratios) are never used as evidence.** Different tools compute them differently, so they cannot be compared across screenshots or across time. Transcribe them if you like, but they carry no weight. This applies portfolio-wide.
- Claude judges with one consistent method: from views, age, and channel size where visible, estimate what a normal video on that channel does, and ask how far this one sits above or below that. A 300k video on a 2M-subscriber channel is normal; the same number on a 6k-subscriber channel is an outlier that escaped its subscriber base into cold traffic.
- When the channel's normal cannot be estimated (bare view counts, unknown channel, no age), mark the item **not assessable** and treat it as weak evidence. Never promote a format or word to `proven` on a not-assessable item alone.
- Raw view size still matters for one thing: topic ceiling. An 8M view video proves the topic can carry 8M somewhere; it does not prove the format outperformed.

## 6. The age/views matrix, outliers, and head-to-heads

- **Old (3+ years) + huge views** → durable topic demand pool; the topic carried it but the packaging is dated. Take the **topic** and plug it into a different, more applicable winning format from the bank (or one lifted from a recent screenshot). These are re-packaging targets.
- **Recent (≤ ~1–2 years) + big views** → current meta: proven topic × proven format. Keep the creator's own format and **exaggerate it harder**; the format is the transferable asset and the topic is proven live.
- **New + modest views on a big channel** → fatigue or bad topic–format fit. Useful negative signal.
- **Recency weighting (operator standing order, 2026-09-25).** Only videos **2 years old or newer** with strong views carry **format** weight; anything older is a **topic** signal only — re-package it in a current format. Which channel a source comes from does not change its weight, with one exception: a channel the operator **designates** as top weight (so far the real trainer on camera in dogs and the face-persona channel in cats — animals overlay `reference-titles.md`) leads its section's formats and thumbnails. A days-old face channel re-making faceless winners and beating them is the strongest recency signal in the portfolio (cats, 2026-09-26).
- **In output**, each source's verdict is written in plain words in its topic header — `Recent, so exaggerate.` / `Recent, but exaggerate only on the honest parts.` / `Old, so re-package.` / `Old, but a strong escape — exaggerate once, re-package the rest.` / `Footage-bound — topic only.` (`rules-and-specs.md` §5).
- **Outliers are the purest signal.** A single outlier on a faced or established channel escaped its subscriber base into cold browse traffic — topic and packaging did all the work.
- **Head-to-heads are gold.** The same topic on two channels at different scale means the framing is the variable. Flag re-attack opportunities on the operator's own topics using the higher-ceiling angle; every plain explainer has a banned / REAL-reason / free-fix re-attack available.
- Once a template is proven on a channel, the work shifts to **problem selection**: universality of the problem × the niche's stake factor × frequency (the overlay states its own stake factor). Universality sets the view ceiling.

## 7. The presence filter

Run it on every intake item and every generated title: **does the title's promise require footage this channel can actually produce?**

- Knowledge promises (lists, warnings, diagnoses, exposés, decisions) compile from generic b-roll — they transfer to every channel.
- Follow-along promises (slow tutorials, "make your first X") need an owned hands library or an on-camera presenter. They transfer only to channels whose registry line lists that capability.
- Proof-of-work promises (a single-project transformation filmed start to finish, a filmed experiment, "I tested all three to destruction") need a real filmed build. No channel currently in the registry can honor them. Such items may still transfer **as a format** — the skeleton is extractable even when the footage is not — and "I tested" survives only as a persona verdict ("after 45 years, here's the one I trust"), never as a filmed claim.

Persona claims delivered in voiceover are compatible with faceless channels: credibility is narrative, not visual. Whether a channel may make persona claims at all is set by its presence value and the persona-claim rules in `rules-and-specs.md`.

## 8. Phases of a generation session

1. **Intake** (§3) — process what the operator pastes; no titles yet.
2. **Fit check — topic × format × channel.** A format transfers only when the topic has the raw material the format's fit-requirements name (see each entry in the master): suppression framing needs a plausible suppressor, ease framing needs a job people believe is hard, banned framing needs a real rule, a versus needs a real tribal debate, a slowness promise needs a genuinely fiddly skill. Then add the channel layer: does the pairing fit this channel's dials and register? The same proven topic often runs on sibling channels by swapping the persona lens — variants across channels are intentional, not duplication.
3. **Generation.** Lay the output out in the standing generation layout (`rules-and-specs.md` §5): topics on top with every source and its age/views verdict, then each title tagged `Exaggerated`, `Reformat` or `New`, with the source topic's views and the source format's views (F-number; `src` for a format lifted from a fresh screenshot). Run every title through the hard rules — especially the character count — before sending. Check the overlay's `produced-log.md` and never duplicate a produced title; adjacent angles on the same topic are fine and often intended. Check `dead-list.md` and suppress dead pairings from default generation (an explicit operator request always overrides).

## 9. Reformat mode

When the operator likes a **topic** but not the **format**, give about five alternative titles for that topic, each from a different banked format, each tagged with its F-number, so they can pick. Lay it out like any generation output (`rules-and-specs.md` §5): the topic header with its source and verdict, then each alternative tagged `Reformat` with the topic's and the format's source views. This is a standard request — handle it without re-asking what they want.

## 10. Batch mix and batch size

- Default batch size is 30 unless told otherwise.
- Default mix is **50% doubling down** on the channel's own proven topics and formats (reworks can be as simple as a bigger listicle number or a stronger adjective) and **50% new territory** (banked formats on new topics from the demand map, twists, recombinations). Confirm or adapt the ratio if the operator specifies one.
- **Initial batches (operator standing order, 2026-09-25):** a channel with no own data runs **80–85% on the ecosystem's winning topics** — either the strong outlier's own title pushed harder (`Exaggerated`) or the winning topic applied in another banked format (`Reformat`); the matrix (§6) decides which mode a topic gets — and **15–20% new territory** (evergreen topics in banked formats, `New`). From the channel's second batch its own data takes over (the default above, or the channel's standing mix).
- A channel may carry a standing mix in its steering block that layers on top of this (for example, a search-leaning channel that runs 70% knowledge formats / 30% tutorial tests, or a face channel whose default batch is direct one-to-one transformations of proven tutorial titles). The channel's mix wins over the default.
- When generating across several channels of one niche, keep every title native to its channel and group or tag by channel.

## 11. Standing doctrine

Lessons that have repeated across niches and are now part of the method:

- **The ecosystem clones winners across channels, and it works.** Near-identical titles on sibling channels pull comparable numbers. Variants of one concept across the operator's own channels (different counts, different persona lens) are normal and intentional.
- **Face twins re-produce, never re-upload.** When a face channel mirrors a faceless sibling's winner, it gets a new voice, face segments, a new edit and new thumbnails. Same proven topic, different packaging.
- **Promote strong thumbnail hooks into their own titles.** When a broad title won on a sharp thumbnail hook, that hook is a proven topic; give it a dedicated title.
- **Sensory titling.** Name the problem in the viewer's own sensory vocabulary (what it sounds, smells, looks like), never the technical cause.
- **Seasonality.** Publish the problem at the season's front edge; the overlay's calendar says when. Evergreen anchors carry the schedule between spikes.
- **Prolific single-craft specialists win.** Ecosystem tops are held by channels that stay inside one topic world — the separate-channels architecture is data-backed.
- **Packaging moves worth reusing anywhere:** part-numbered ladders, "updated tutorial" re-issues of one's own winners, staccato negation strings ("No Chemicals. No Plumber."), title–thumbnail interlock with THIS, expected-answer negation ("— And It's NOT Vinegar").
- **Sibling collab tagging as a distribution lever (approved 2026-09-07):** the audience's diet is full of collab-credited uploads ("Frugal Frannie and Vintage Lifestyle USA", "Ramón Delgado and 4 more"); a small sibling channel's upload credited to the big channel appears in the big channel's subscriber feeds. Use it for launches — tag a new channel's uploads with the flagship — and always record the credit in the intake record, because it confounds the small channel's normal. Evidence: four sightings in one audience-tab batch; the Vintage Pipefitter's 148k limescale title carried "and Roger the Pipe Guy" (credit TBC).

## 12. Session types and the one-niche rule

Four session types: **Triage** (anything in, sorted to banks — `triage.md`), **Generation** (one niche, titles out), **Thumbnails** (the `thumbnails` skill), **Maintenance** (audits, compression, launches — `launch-playbook.md`, `filing-rule.md`).

**One niche per generation chat.** Example titles in the context window bleed into output, so a generation chat never loads two niches' examples. Triage chats are cross-niche by nature and are safe because they generate no titles — close a triage chat after banking and open a generation chat. If a foreign-niche item appears in a generation chat, file it to the right bank via the filing rule without loading that niche's examples.
