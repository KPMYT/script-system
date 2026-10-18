---
name: channels
description: The list of every channel the script workflow can write for, with each channel's niche pack, persona profile and status. Read by the workflow at START to show the channel choices and load the right files.
---

# Channels

The workflow shows this list at START. A channel can only be scripted when its status is **ready**.

| # | Channel | Niche pack | Persona profile | Status |
|---|---|---|---|---|
| 1 | Hank Hardwood | `woodworking-scripts` | `personas/hank-hardwood.md` | pending: persona profile not written yet |
| 2 | Dale Oakfield's Workshop | `woodworking-scripts` | `personas/dale-oakfield.md` | pending: persona profile not written yet |

## Adding a channel

1. Write its persona profile from `persona-profile-template.md` and save it in `personas/`.
2. Make sure its niche pack exists. If it doesn't, the channel runs on the core fallbacks until one is built.
3. Add a row here, with status **ready** only once the persona profile is complete.
