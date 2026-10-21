# Pinned for later

Things parked during the rebuild, so nothing gets lost between sessions.

## Done so far
- **Core (complete):** `workflow.md` (START), `channels.md`, `claims-policy.md`, `persona-profile-template.md`, `humanizer.md`, `voice-anchoring.md`, `script-scanner.py`, `retention-mechanics.md`, `variety-rotation.md`, `cta-and-endings.md`, `offer-rules.md`, `research-and-sourcing.md`, `script-structures.md`, `greenlight-audit.md`.
- **Woodworking pack:** `woodworking-scripts`, with excerpts, voice samples, both templates, its scanner block, its inputs block, and freshness (live facts re-checked after 30 days; change if needed).
- **Plumbing pack (2026-10-21):** `plumbing-scripts`, with its overrides table, inputs block (no research pack), excerpts, voice samples, unit plan template, 38 model files and scanner block; Roger, Mark and Vintage ready in `core/channels.md`.
- **Tests:** `tests/run_checks.py`, 43 checks, all passing (the price-guide check added 2026-10-21; the post-merge audit's fixes added 2026-10-21; copy guard added in refs-01; the profile allow: check added 2026-10-20; the fraction-word and "e-book" checks added in iter-01; the plumbing tests added 2026-10-21).
- **First script test (iter-01, 2026-10-20):** Hank's lazy Susan script reviewed with the operator; fixes applied across core, the woodworking pack, both profiles and ideation. See `tests/iterations/iter-01/`.
- **refs-01 (2026-10-18):** excerpts expanded to 15 groups, `reference-scripts.md` added, copy guard (`--refs`) wired into the workflow and the audit. See `tests/iterations/refs-01/CHANGES.md`.

## Still to rebuild in the core
- Nothing. The core is complete.

## To build
- **Persona profiles for Hank and Dale:** done 2026-10-20 (`personas/hank-hardwood.md`, `personas/dale-oakfield.md`), approved by the operator.
- **Research stage** (between ideation and script). Runs in Cowork, following core `research-and-sourcing.md`, with the mandatory verification pass. It fills the niche's research pack template, so the two stages can't drift apart.
- **Niche launch skill and persona launch skill.** These collect every variable we've defined so far into a repeatable launch process:
  - competitor study (winners plus flops)
  - cold-niche research (moved from the old research file): outlier videos, title promises, openings, gaps in the comments
  - excerpt library and voice samples
  - research pack template and unit sizes
  - adversaries, swearing rules, safety
  - persona details, CTA style, named doubter, offer setup
- **Example script** for woodworking, written from a real research pack once the research stage exists.
- **Ops guide** (human-facing), if wanted.

## To update
- **Dale's book fit:** a general technique guide pitched to a for-profit audience.
- **Ideation:** stop producing titles the script can't deliver, such as tenure claims. Exaggeration stays allowed.
- **Connect ideation to research and script.** Update the ideation brief spec so it carries what the research stage needs (format, chosen project, title claims to support), and add the route for research flagging a title back.

## Ideas
- **Auto-edit pulls researched listings** from the web and shows them on screen. Blur the shop names.

## Decisions made
- **Vidrush mode is the only mode.** Scripts are always clean voiceover prose for the auto-edit tool. Traditional editor mode, with bracketed visual cues, is gone.
- **The video is built from the script.** Anything the viewer should see must be named in the narration, in the same or the next sentence. Never "take a look at this" without naming what "this" is; the visuals can't show something the script never mentions. Already applied in `voice-anchoring.md`, `retention-mechanics.md` and the woodworking pack.
- **The audit is visible and short.** A few lines of evidence after the rotation log force the checks to really happen, since scripts aren't reviewed before upload.
- **Only scripts that read PASS get uploaded.** A Hold or the three-round cap puts "NOT READY: DO NOT UPLOAD" on the first line. This goes into the VA instructions.
- **START is the only way in.** `workflow.md` asks for the channel, then exactly that channel's inputs, refuses to continue until they're valid, then runs straight to the final script with no questions.
- **The Four Pillars header is dropped.**
- **The old house-rules prompt is retired.** Its rules now live in `workflow.md`, `cta-and-endings.md`, `offer-rules.md` and `claims-policy.md`.

## Decisions still open
- ~~How the rebuilt core files get packaged as skills.~~ Decided 2026-10-20: one `script-writer` skill (core, niche packs, persona profiles, books), built by `tools/build_skills.py` into `dist/`, installed per account; ideation runs in Cowork, Etsy first.
- Distribution to VAs on personal Cowork accounts: a synced folder, a bootstrap skill, a version stamp, and developer-built queue and checks.

## Tests and data
- **Retention coaching was dropped** (decided 2026-10-18). Graphs get analyzed with Claude when needed. Two rules carry over:
  - **Judging any test or change:** compare videos at the same age (first 7 days), against the channel's own normal, and check click-through separately from retention, so you know whether the title or the script made the difference.
  - **Changing a rule:** only after a pattern shows on three or more videos. It then goes into the niche pack or persona profile, never pasted into chats.
- **The CTA test:** Hank's short CTA against Dale's unchanged one, comparing each channel before and after.
- **Data to pull:**
  - Studio first-7-day comparisons
  - click-through rate against retention
  - book clicks or QR scans per video
  - comments held for review
  - the AI disclosure label on avatar videos
  - hiding the repeat "BOGUS" commenter
