# Installing the skills

**Version:** 2026-10-27 (library commit dedf3d3)

Eleven skill files, one per layer (`script-writer` also comes as `script-writer.zip`, the same skill). Install them on every account that will do ideation or scripts (yours and each VA's), in claude.ai under Settings, Capabilities, Skills, not in a project. They then work in Claude and in Cowork.

| File | Layer | What it does | On your account now |
|---|---|---|---|
| `script-writer.skill` | Core | Type **START** to write a script. The core rules every channel uses; it reads the skills below. | **New** (not on the account when this was built): upload it. If an older `script-writer` is on the account, delete it first. |
| `woodworking-scripts.skill` | Niche | The woodworking-for-profit rules (structure, money block, proof, safety, voice) and the research-pack template. | **Replace** the copy on the account (delete it, upload this). |
| `hank-hardwood-persona.skill` | Channel | Hank's profile, CTA rules and book. | **Replace** the copy on the account (delete it, upload this). |
| `dale-oakfield-persona.skill` | Channel | Dale's profile, CTA rules and book. | **Replace** the copy on the account (delete it, upload this). |
| `sawdust-sam-persona.skill` | Channel | Sawdust Sam's profile, CTA rules and book (pages 1-80). Ready since 2026-10-24. | **New:** upload it. |
| `plumbing-scripts.skill` | Niche | The plumbing rules (inputs: title and brief, the opening, promises, the ten video types, CTAs, the ending, length, voice, proof, money, safety), the 38 model scripts and the copy guard's files. | **Replace** the copy on the account (delete it, upload this). |
| `roger-the-pipe-guy-persona.skill` | Channel | Roger's profile, CTA rules and book. | **Replace** the copy on the account (delete it, upload this). |
| `mark-silverbridge-persona.skill` | Channel | Mark's profile, CTA rules and book. | **Replace** the copy on the account (delete it, upload this). |
| `vintage-pipefitter-persona.skill` | Channel | The Vintage Pipefitter's profile and its one-line subscribe ask (no book). | **Replace** the copy on the account (delete it, upload this). |
| `woodworking-ideation.skill` | Ideation | The Etsy-first product scan (30 products), title and thumbnail-text options, fact briefs, the optional research pack. | **Replace** the copy on the account (delete it, upload this). |
| `plumbing-ideation.skill` | Ideation | Plumbing titles and briefs for Roger, Mark, Vintage and Werner; briefs now give each item its cost and the right way (the script fills gaps from the plumbing price guide). | **Replace** the copy on the account (delete it, upload this). |
| `ideation-core.skill` | Ideation | The shared base every ideation skill needs. | **Unchanged:** only install it where it's missing (for example a new VA account). |

All of the script skills must be installed together: `script-writer` stops with NOT READY if the channel's niche or persona skill is missing.

## Steps

1. **Delete** the old copies of `plumbing-ideation`, `woodworking-scripts`, `hank-hardwood-persona`, `dale-oakfield-persona`, `woodworking-ideation`, `plumbing-scripts`, `roger-the-pipe-guy-persona`, `mark-silverbridge-persona` and `vintage-pipefitter-persona`.
2. **Upload all eleven from this build together**: those nine, `script-writer` and the new `sawdust-sam-persona` (delete any older `script-writer` first). They're built from one library version, so they agree with each other; never mix files from two builds (the version line says which build a file is).
3. **Upload `ideation-core`** only if the account doesn't have it.
4. **Turn them all on.**

## Using them (in Cowork)

- **Ideation:** "Woodworking ideation for Hank" (or Dale). It scans Etsy, shows 30 products, then title options. You pick by number, and it writes the briefs. Ask for the research pack if you want it.
- **Script:** type **START** in the chat where that channel's scripts are written, so each new script reads the rotation log lines of the earlier ones (in a fresh chat, paste the last five ROTATION LOG ENTRY lines, or "none"). Pick the channel, then paste what it asks for: for woodworking, the title, the brief, the research pack (or "none", and the chat builds one) and, in a fresh chat, the rotation log; for plumbing, the title, the brief and, in a fresh chat, the rotation log (no research pack).
- **Upload rule:** only upload a script whose output says **VERDICT: PASS**. Anything that starts "NOT READY: DO NOT UPLOAD" goes back.

## Updating

The master copies live in the script-system repo. Whenever the rules change, the skills are rebuilt from the repo (`python3 tools/build_skills.py`) and re-uploaded. The version line in each skill and in this file says which build you have.
