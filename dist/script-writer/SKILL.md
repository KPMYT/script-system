---
name: script-writer
description: Writes YouTube scripts for the operator's channels. Runs whenever someone types START (alone or followed by inputs), asks for a new script, or pastes a title with a brief (and, where the niche uses one, a research pack) for a script. It asks which channel, collects exactly the inputs that channel needs, refuses to write until every input is valid, then runs straight through to the finished, checked script and voiceover copy. It reads the channel's niche-pack skill and persona skill; for plumbing, style, HVAC and woodworking the niche pack's own steps take over after the channel question. Channels ready now: Hank Hardwood and Dale Oakfield's Workshop (woodworking for profit); Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter and Werner Finkbeiner (plumbing); Frederick Barnes (home electrical); Roger the HVAC Guy (HVAC); Scarlett Starling and Diane de Chambray (style for women over 60).
---

# Script writer (the core)

**Version:** 2026-11-15 (library commit e13d768)

When someone types **START**, open `core/workflow.md` (in this skill's folder) and follow section 1: the channel question.

**Then, for plumbing, style, HVAC and woodworking (the simple packs, P21):** the channel's niche pack takes over. Open that pack's `SKILL.md` and follow its steps exactly; they replace `core/workflow.md` sections 2 to 6. Read only what the pack says to read (the channel's page, one model transcript, the title and brief, its price guide or book index where it says so). Run the pack's own `check.py`, never `core/script-scanner.py`, and give the output its last step lays out. Don't ask for a rotation log or a research pack unless the pack asks for one, and don't run the core audit.

**For electrical (Frederick Barnes):** follow `core/workflow.md` from section 1 to the end, as before. Everything else is loaded from there.

## The other skills it reads

The script system is split into separate skills, one per layer. They're all installed on the same account, so find each one's folder by its name among the installed skills (for example under `/mnt/skills/`).

| When a file says | It means |
|---|---|
| the niche pack `woodworking-scripts` | the **woodworking-scripts** skill: its `SKILL.md` is the pack's steps, plus `check.py` and its `references/` folder |
| the persona profile `personas/hank-hardwood.md` | the **hank-hardwood-persona** skill: its `SKILL.md` is the profile |
| the persona profile `personas/dale-oakfield.md` | the **dale-oakfield-persona** skill: its `SKILL.md` is the profile |
| the niche pack `plumbing-scripts` | the **plumbing-scripts** skill: its `SKILL.md` is the pack's steps, plus `check.py` and its `references/` folder (models, price guide) |
| the persona profile `personas/roger-the-pipe-guy.md` | the **roger-the-pipe-guy-persona** skill: its `SKILL.md` is the profile |
| the persona profile `personas/mark-silverbridge.md` | the **mark-silverbridge-persona** skill: its `SKILL.md` is the profile |
| the persona profile `personas/vintage-pipefitter.md` | the **vintage-pipefitter-persona** skill: its `SKILL.md` is the profile (this channel has no book) |
| the niche pack `electrical-scripts` | the **electrical-scripts** skill: its `SKILL.md` is the pack's rules, plus its `references/` folder (with `references/models/`) |
| the persona profile `personas/frederick-barnes.md` | the **frederick-barnes-persona** skill: its `SKILL.md` is the profile (this channel has no book) |
| the niche pack `hvac-scripts` | the **hvac-scripts** skill: its `SKILL.md` is the pack's steps, plus `check.py` and its `references/` folder |
| the persona profile `personas/roger-the-hvac-guy.md` | the **roger-the-hvac-guy-persona** skill: its `SKILL.md` is the profile (this channel has no book for now) |
| the persona profile `personas/werner-finkbeiner.md` | the **werner-finkbeiner-persona** skill: its `SKILL.md` is the profile, plus his book index |
| the niche pack `style-scripts` | the **style-scripts** skill: its `SKILL.md` is the pack's steps, plus `check.py` and its `references/` folder |
| the persona profile `personas/scarlett-starling.md` | the **scarlett-starling-persona** skill: its `SKILL.md` is the profile |
| the persona profile `personas/diane-de-chambray.md` | the **diane-de-chambray-persona** skill: its `SKILL.md` is the profile |
| a book text `personas/books/<channel>-book.md` | inside that channel's persona skill, at the same path |

If a skill the chosen channel needs isn't installed, stop with the NOT READY block (`core/workflow.md`, section 5) and name the missing skill.

## In this skill

| What | Where |
|---|---|
| The entry point: START, the input gate, the run, the format, the output | `core/workflow.md` |
| The channel list START shows | `core/channels.md` |
| Every other core rule (claims, offers, CTAs, humanizer, voice, retention, rotation, research, structures, audit) | `core/` |
| The checking program for electrical | `core/script-scanner.py` (run it with Python where available; otherwise do its checks by hand, as `core/workflow.md` says). The simple packs carry their own `check.py`. |

## Running the checking program

**Plumbing, style, HVAC and woodworking:** the pack's own `check.py`, with the command its `SKILL.md` gives. Never `core/script-scanner.py` for these.

**Electrical** (copy-guard files: the pack's own SKILL.md, the excerpts, the voice samples and every model file; the facts guide is a fact source, so it goes with the brief, never in --refs). Use the real folders of the other skills in place of the placeholders:

```
python3 core/script-scanner.py SCRIPT --rules <electrical-scripts>/SKILL.md <channel-persona>/SKILL.md --pack BRIEF <electrical-scripts>/references/facts-guide.md --title "LOCKED TITLE" --refs <electrical-scripts>/SKILL.md <electrical-scripts>/references/excerpts.md <electrical-scripts>/references/voice-samples.md <electrical-scripts>/references/models/*.md <channel-persona>/SKILL.md --final
```
