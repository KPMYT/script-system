---
name: script-writer
description: Writes YouTube scripts for the operator's channels. Runs whenever someone types START (alone or followed by inputs), asks for a new script, or pastes a title with a brief (and, where the niche uses one, a research pack) for a script. It asks which channel, collects exactly the inputs that channel needs, refuses to write until every input is valid, then runs straight through to the finished, audited script and voiceover copy. Holds the core rules; it reads the channel's niche-pack skill and persona skill. Channels ready now: Hank Hardwood, Dale Oakfield's Workshop and Sawdust Sam (woodworking for profit); Roger the Pipe Guy, Mark Silverbridge and The Vintage Pipefitter (plumbing).
---

# Script writer (the core)

**Version:** 2026-10-27 (library commit dedf3d3)

When someone types **START**, open `core/workflow.md` (in this skill's folder) and follow it exactly, from section 1. Everything else is loaded from there.

## The other skills it reads

The script system is split into separate skills, one per layer. They're all installed on the same account, so find each one's folder by its name among the installed skills (for example under `/mnt/skills/`).

| When a file says | It means |
|---|---|
| the niche pack `woodworking-scripts` | the **woodworking-scripts** skill: its `SKILL.md` is the pack's rules, plus its `references/` folder |
| the persona profile `personas/hank-hardwood.md` | the **hank-hardwood-persona** skill: its `SKILL.md` is the profile |
| the persona profile `personas/dale-oakfield.md` | the **dale-oakfield-persona** skill: its `SKILL.md` is the profile |
| the persona profile `personas/sawdust-sam.md` | the **sawdust-sam-persona** skill: its `SKILL.md` is the profile |
| the niche pack `plumbing-scripts` | the **plumbing-scripts** skill: its `SKILL.md` is the pack's rules, plus its `references/` folder (with `references/models/`) |
| the persona profile `personas/roger-the-pipe-guy.md` | the **roger-the-pipe-guy-persona** skill: its `SKILL.md` is the profile |
| the persona profile `personas/mark-silverbridge.md` | the **mark-silverbridge-persona** skill: its `SKILL.md` is the profile |
| the persona profile `personas/vintage-pipefitter.md` | the **vintage-pipefitter-persona** skill: its `SKILL.md` is the profile (this channel has no book) |
| a book text `personas/books/<channel>-book.md` | inside that channel's persona skill, at the same path |

If a skill the chosen channel needs isn't installed, stop with the NOT READY block (`core/workflow.md`, section 5) and name the missing skill.

## In this skill

| What | Where |
|---|---|
| The entry point: START, the input gate, the run, the format, the output | `core/workflow.md` |
| The channel list START shows | `core/channels.md` |
| Every other core rule (claims, offers, CTAs, humanizer, voice, retention, rotation, research, structures, audit) | `core/` |
| The checking program | `core/script-scanner.py` (run it with Python where available; otherwise do its checks by hand, as `core/workflow.md` says) |

## Running the checking program

Use the real folders of the other skills in place of the placeholders. `FACT_SOURCE` is the research pack, or the brief where the niche pack doesn't use one.

Woodworking:

```
python3 core/script-scanner.py SCRIPT --rules <woodworking-scripts>/SKILL.md <channel-persona>/SKILL.md --pack FACT_SOURCE --title "LOCKED TITLE" --refs <woodworking-scripts>/references/excerpts.md <woodworking-scripts>/references/reference-scripts.md <channel-persona>/SKILL.md
```

Plumbing (the pack's copy-guard files: the pack's own SKILL.md, the excerpts, the voice samples and every model file):

```
python3 core/script-scanner.py SCRIPT --rules <plumbing-scripts>/SKILL.md <channel-persona>/SKILL.md --pack BRIEF <plumbing-scripts>/references/price-guide.md --title "LOCKED TITLE" --refs <plumbing-scripts>/SKILL.md <plumbing-scripts>/references/excerpts.md <plumbing-scripts>/references/voice-samples.md <plumbing-scripts>/references/models/*.md <channel-persona>/SKILL.md
```
