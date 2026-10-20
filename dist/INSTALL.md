# Installing the skills

**Version:** 2026-10-20 (library commit 7e78d46)

Three skill files. Install all three on every account that will do ideation or scripts (yours and each VA's), in claude.ai under Settings, Capabilities, Skills (they then work in Claude and in Cowork).

| File | What it does | Changed? |
|---|---|---|
| `script-writer.skill` | Type **START** to write a script. Holds the core rules, the woodworking pack, Hank's and Dale's profiles and both books. | **New.** Replaces the old `woodworking-scripts` skill. |
| `woodworking-ideation.skill` | Woodworking ideation: the Etsy-first product scan (30 products), title and thumbnail-text options, then fact briefs and the optional research pack. | **Updated.** Replaces the installed `woodworking-ideation`. |
| `ideation-core.skill` | The shared base every ideation skill needs (format bank, rules, audience profiles). | **Unchanged.** Only install it where it's missing (for example a new VA account). |

## Steps

1. **Remove the old `woodworking-scripts` skill** from the account. If it stays, it can clash with `script-writer`.
2. **Upload `script-writer.skill`.**
3. **Replace `woodworking-ideation`** with the new file (remove the old one, upload the new one).
4. **Upload `ideation-core.skill`** only if the account doesn't have it.
5. **Turn all three on.**

## Using them (in Cowork)

- **Ideation:** "Woodworking ideation for Hank" (or Dale). It scans Etsy, shows 30 products, then title options. You pick by number, and it writes the briefs. Ask for the research pack if you want it.
- **Script:** open a new chat for each script and type **START**. Pick the channel, then paste the title, the brief, the research pack and the rotation log (the channel's last five ROTATION LOG ENTRY lines, or "none").
- **Upload rule:** only upload a script whose output says **VERDICT: PASS**. Anything that starts "NOT READY: DO NOT UPLOAD" goes back.

## Updating

The master copies live in the script-system repo. Whenever the rules change, the skills are rebuilt from the repo (`python3 tools/build_skills.py`) and re-uploaded. The version line at the top of each `SKILL.md` and of this file says which build you have.
