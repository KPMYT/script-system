#!/usr/bin/env python3
"""Build the installable skills from the library: python3 tools/build_skills.py

Writes dist/<skill>/ (the folder) and dist/<skill>.skill (the same folder zipped) for:
  script-writer        START -> finished script: core rules, niche packs, persona profiles, books
  woodworking-ideation the edited woodworking ideation skill (needs ideation-core installed too)
  ideation-core        the shared ideation base, an unchanged copy (every niche's ideation skill needs it)
The library files stay the single source; dist/ is regenerated from them every time.
"""
import os, shutil, subprocess, zipfile, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")

def commit():
    try:
        return subprocess.run(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    except Exception:
        return "unknown"

STAMP = f"{datetime.date.today().isoformat()} (library commit {commit()})"

SCRIPT_WRITER_SKILL = """---
name: script-writer
description: Writes YouTube scripts for the operator's channels. Runs whenever someone types START (alone or followed by inputs), asks for a new script, or pastes a title with a brief and research pack for a script. It asks which channel, collects exactly the inputs that channel needs, refuses to write until every input is valid, then runs straight through to the finished, audited script and voiceover copy. Channels ready now: Hank Hardwood and Dale Oakfield's Workshop (woodworking for profit).
---

# Script writer

**Version:** {stamp}

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
"""

INSTALL = """# Installing the skills

**Version:** {stamp}

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
"""

def copytree(src, dst, ignore=()):
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", *ignore))

def zipdir(folder, out):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        base = os.path.dirname(folder)
        for d, _, files in os.walk(folder):
            for f in sorted(files):
                full = os.path.join(d, f)
                z.write(full, os.path.relpath(full, base))

def build_script_writer():
    out = os.path.join(DIST, "script-writer")
    copytree(os.path.join(ROOT, "core"), os.path.join(out, "core"))
    copytree(os.path.join(ROOT, "woodworking-scripts"), os.path.join(out, "woodworking-scripts"), ignore=("archive",))
    copytree(os.path.join(ROOT, "personas"), os.path.join(out, "personas"))
    with open(os.path.join(out, "SKILL.md"), "w") as f:
        f.write(SCRIPT_WRITER_SKILL.replace("{stamp}", STAMP))
    return out

def build_ideation():
    out = os.path.join(DIST, "woodworking-ideation")
    copytree(os.path.join(ROOT, "ideation", "woodworking-ideation"), out)
    return out

def build_ideation_core():
    out = os.path.join(DIST, "ideation-core")
    copytree(os.path.join(ROOT, "ideation", "ideation-core"), out)
    return out

def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    for folder in (build_script_writer(), build_ideation(), build_ideation_core()):
        zipdir(folder, folder + ".skill")
        n = sum(len(fs) for _, _, fs in os.walk(folder))
        print(f"built {os.path.relpath(folder, ROOT)}/ ({n} files) and {os.path.relpath(folder, ROOT)}.skill")
    with open(os.path.join(DIST, "INSTALL.md"), "w") as f:
        f.write(INSTALL.replace("{stamp}", STAMP))
    print(f"version: {STAMP}")

if __name__ == "__main__":
    main()
