# Installing the skills

**Version:** 2026-10-20 (library commit 51d1eeb)

Six skill files, one per layer. Install them on every account that will do ideation or scripts (yours and each VA's), in claude.ai under Settings, Capabilities, Skills. They then work in Claude and in Cowork.

| File | Layer | What it does | On your account now |
|---|---|---|---|
| `script-writer.skill` | Core | Type **START** to write a script. The core rules every channel uses; it reads the skills below. | **New:** upload it. |
| `woodworking-scripts.skill` | Niche | The woodworking-for-profit rules (structure, money block, proof, safety, voice) and the research-pack template. | **Replace** the old `woodworking-scripts` (delete the old one, upload this). |
| `hank-hardwood-persona.skill` | Channel | Hank's profile, CTA rules and book. | **New:** upload it. |
| `dale-oakfield-persona.skill` | Channel | Dale's profile, CTA rules and book. | **New:** upload it. |
| `woodworking-ideation.skill` | Ideation | The Etsy-first product scan (30 products), title and thumbnail-text options, fact briefs, the optional research pack. | **Replace** the old `woodworking-ideation`. |
| `ideation-core.skill` | Ideation | The shared base every ideation skill needs. | **Unchanged:** only install it where it's missing (for example a new VA account). |

All of the script skills must be installed together: `script-writer` stops with NOT READY if the channel's niche or persona skill is missing.

## Steps

1. **Delete** the old `woodworking-scripts` and the old `woodworking-ideation`.
2. **Upload** `script-writer`, `woodworking-scripts`, `hank-hardwood-persona`, `dale-oakfield-persona` and `woodworking-ideation`.
3. **Upload `ideation-core`** only if the account doesn't have it.
4. **Turn them all on.**

## Using them (in Cowork)

- **Ideation:** "Woodworking ideation for Hank" (or Dale). It scans Etsy, shows 30 products, then title options. You pick by number, and it writes the briefs. Ask for the research pack if you want it.
- **Script:** open a new chat for each script and type **START**. Pick the channel, then paste the title, the brief, the research pack and the rotation log (the channel's last five ROTATION LOG ENTRY lines, or "none").
- **Upload rule:** only upload a script whose output says **VERDICT: PASS**. Anything that starts "NOT READY: DO NOT UPLOAD" goes back.

## Updating

The master copies live in the script-system repo. Whenever the rules change, the skills are rebuilt from the repo (`python3 tools/build_skills.py`) and re-uploaded. The version line in each skill and in this file says which build you have.
