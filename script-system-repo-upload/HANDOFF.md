# Handoff: how this system was built, and why

Context carried over from the claude.ai conversation that designed this library (October 2026). Read with `README.md` (what each file is) and `PINNED.md` (open items).

---

## 1. What this is

A script-writing system for a portfolio of faceless and AI-avatar YouTube channels aimed at viewers over 50 (practical education, some channels selling e-books). It replaced a bought product, FacelessOS, which was built for entertainment documentaries and full of material that didn't fit. FacelessOS was rebuilt as our own library. The original files are kept in `archive/facelessos-original/` for comparison only.

## 2. Architecture and precedence

- **Core (`core/`):** base rules for every channel.
- **Niche packs** (e.g. `woodworking-scripts/`) override core base rules wherever they say so explicitly. Where they're silent, core applies.
- **Persona profiles** (`personas/`): per-channel settings (voice, CTA, offers, script type). They can override niche and core where explicit.
- **`core/claims-policy.md` and `core/offer-rules.md` sit above everything.** Packs and profiles can tighten them, never loosen them.
- **Every script starts with START** (`core/workflow.md`): pick the channel, the input gate (refuses to write until every input is valid), then an uninterrupted run to the final output.

## 3. Decisions, and why (locked unless the operator changes them)

### From the woodworking-for-profit study

The data: BeardedViking and WhosTheVoss winners against Dale and Hank's own videos. Hank's old faceless videos were deliberately excluded.

- **No persona or channel intro.** The winners never introduce themselves.
- **Get to the first material fast:** within about 15 seconds. BeardedViking does it in 5-15 seconds.
- **No retention teases** ("stick around," "bonus at the end"), no problem essays, at most one sentence of context.
- **Length comes from the content, never word budgets.** Each unit (material, step, tip, cost line) takes what it needs. Trivial items are batched, repeated steps collapse, and the plan comes before the prose.
- **The money block is a bookend:** promised in line one, proven at the end with listings, price, cost, fees and what's left.
- **Proof is always researched online listings,** worded honestly: "listed at" for asking prices, "sold for" only with sales evidence.
- **Where to buy,** with "prices subject to change" said once.
- **Tool alternatives are shown, and safety is one line inside the step.**
- **Voice:** "you" for steps, "I" for opinions. Honest candor yes, jokes no (AI humor is hard to prompt).
- **Adversaries:** the doubter (the default), big box markup, scammers, overpriced materials. Categories only. Never clickbait YouTube or the algorithm. The old "hardwood crowd" is retired.
- **Swearing:** mild words, 1-3 per video, aimed at targets, never in CTAs, titles or thumbnails.
- **Visuals are AI-generated from the script.** Every step names a visible object and action, and the script never points at something it doesn't name.
- **Steps are instructions to the viewer,** never "I'm cutting." The persona never claims sales, customers or history.
- **Single builds only for now.** Listicles come later, written fresh from research packs, never re-cut from finished videos.
- **CTA test:** Hank gets a short CTA right after the first payoff; Dale stays as he is. Compare each channel before and after.
- **Ideation must stop producing titles the script can't deliver.** Exaggeration in degree is allowed.
- **No hourly-wage framing** (the operator dropped it).

### From the FacelessOS rebuild

- **Kept and rewritten:** humanizer, voice anchoring, scanner, retention mechanics, variety rotation, CTA mechanics, research rules, fallback structures, audit.
- **Cut:** the master file, quick start, title formulas, celebrity, true crime, hero's journey, visual scripting, the hook swipe files, retention coaching, the "Four Pillars" header, word-count tables, editor notation.
- **Vidrush voiceover prose is the only format;** Talking Head markers or Classic.
- **Humanizer:**
  - H1-H23 (H20 "Most people…" allowed once; H23 filler phrases at most once each)
  - hard bans include the retention teases and "let's get into it"
  - a niche pack or persona profile can lift a ban only by naming it
- **Voice samples:** 2-3 verbatim clips of human narration from niche winners, stored in the niche pack. Never AI-written uploads.
- **Rehooks:** short-range bridges between segments are allowed and encouraged. Long-range promises are banned.
- **CTAs:**
  - content, length and style come from the persona profile
  - every CTA promises real added value
  - mid-CTA after the first payoff
  - the ending is the CTA or nothing, then exactly one closing line
  - never name a future video (the script has no idea what comes next)
- **Research stage rules:**
  - facts are always verified
  - framing (stakes, villain tone, title degree) may be exaggerated, but not to an extreme
  - freshness windows are set per niche
  - a mandatory verification pass
  - titles that can't be supported get flagged back to ideation
- **Audit:**
  - groups A-F, with a short visible evidence block (scripts are uploaded without anyone reading them)
  - at most three rounds
  - NOT READY prints no script
  - only PASS scripts are uploaded
- **Rotation log:** the VA pastes the last five lines. Scripts are made in bulk on different PCs, so there's no shared file.
- **Greetings:** off by default; a niche or persona can allow one.

### Rejected, so they don't come back

- **An API pipeline:** too expensive.
- **Team plan seats for VAs:** VAs use their own Claude or Cowork accounts.
- **An automatic rotation-log file:** VAs work on different PCs.
- **Twin-channel cross-checks.**
- **Adding faceless competitors.**
- **Jokes.**
- **Retention coaching.**
- **The Four Pillars header.**
- **Hourly framing.**
- **Fixed CTA lengths, or e-book-only CTAs.**

## 4. Competitor findings worth keeping (woodworking)

- **Script length:** winning scripts ran 1,135-2,408 words, about 1,900 typical. Dale's and Hank's ran about 2,900.
- **Specific numbers per minute:** about 5.5 for the winners, against 2.9 (Dale) and 3.8 (Hank).
- **Words spent on build steps:** about 44% for the winners, against 21-25% for Dale and Hank.
- **First-person "I" per 1,000 words:** about 28 for the winners (they're real people). Dale about 4, Hank about 7.
- **Channel intro:** never, for the winners. Dale and Hank had one in every video.
- **Retention teases:** none for the winners. Dale averaged three per video.
- **Words spent on CTAs:** about 45-65 for the winners, about 125-130 for Dale and Hank.
- **Comments:** about 40% of Dale's and 36% of Hank's were "AI" or "fake" remarks. The most-liked complaints were about narration not matching the footage.
- **Hank's faceless versus avatar results** were confounded (best-of against all, different video ages). Don't treat them as evidence.

## 5. Known limits

- **The scanner's number check matches values, not meanings.** "40 pieces" can match a $40 price.
- **Facebook Marketplace's fee for shipped orders** isn't settled in published sources. The research pack must verify it every time.
- **No real end-to-end run has happened yet.** Persona profiles and the research stage don't exist yet.
