---
name: script-writer
description: Writes YouTube scripts for the operator's channels. Runs whenever someone types START (alone or followed by inputs), asks for a new script, or pastes a title with a brief and research pack for a script. It asks which channel, collects exactly the inputs that channel needs, refuses to write until every input is valid, then runs straight through to the finished, audited script and voiceover copy. Channels ready now: Hank Hardwood and Dale Oakfield's Workshop (woodworking for profit).
---

# Script writer

**Version:** 2026-10-20 (library commit 7e78d46)

When someone types **START**, open `core/workflow.md` and follow it exactly, from section 1. Everything else is loaded from there.

## Where things are (all paths are from this skill's folder)

| What | Where |
|---|---|
| The entry point: START, the input gate, the run, the format, the output | `core/workflow.md` |
| The channel list START shows | `core/channels.md` |
| Every other core rule (claims, offers, CTAs, humanizer, voice, retention, rotation, research, structures, audit) | `core/` |
| The checking program | `core/script-scanner.py` (run it with Python where available; otherwise do its checks by hand, as `core/workflow.md` says) |
| The woodworking niche pack | `woodworking-scripts/SKILL.md` and `woodworking-scripts/references/` |
| Channel persona profiles | `personas/` (for example `personas/hank-hardwood.md`) |
| Each channel's book text, for the book match | `personas/books/` |

When `core/channels.md` or a file names a niche pack such as `woodworking-scripts`, it means the folder of that name inside this skill. A persona profile path such as `personas/hank-hardwood.md` is inside this skill too.

## Running the checking program

From this skill's folder:

```
python3 core/script-scanner.py SCRIPT --rules woodworking-scripts/SKILL.md personas/<channel>.md --pack RESEARCH_PACK --refs woodworking-scripts/references/excerpts.md woodworking-scripts/references/reference-scripts.md personas/<channel>.md
```
