#!/usr/bin/env python3
"""Build the installable skills from the library: python3 tools/build_skills.py

Writes dist/<skill>/ (the folder) and dist/<skill>.skill (the same folder zipped) for:
  script-writer          START -> finished script: the core rules (it finds the other skills by name)
  woodworking-scripts    the woodworking niche pack
  <channel>-persona      one per channel: the persona profile (as SKILL.md) and the channel's book text
  woodworking-ideation the edited woodworking ideation skill (needs ideation-core installed too)
  ideation-core        the shared ideation base, an unchanged copy (every niche's ideation skill needs it)
The library files stay the single source; dist/ is regenerated from them every time.
"""
import os, re, shutil, subprocess, zipfile, datetime
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
description: Writes YouTube scripts for the operator's channels. Runs whenever someone types START (alone or followed by inputs), asks for a new script, or pastes a title with a brief and research pack for a script. It asks which channel, collects exactly the inputs that channel needs, refuses to write until every input is valid, then runs straight through to the finished, audited script and voiceover copy. Holds the core rules; it reads the channel's niche-pack skill and persona skill. Channels ready now: Hank Hardwood and Dale Oakfield's Workshop (woodworking for profit).
---

# Script writer (the core)

**Version:** {stamp}

When someone types **START**, open `core/workflow.md` (in this skill's folder) and follow it exactly, from section 1. Everything else is loaded from there.

## The other skills it reads

The script system is split into separate skills, one per layer. They're all installed on the same account, so find each one's folder by its name among the installed skills (for example under `/mnt/skills/`).

| When a file says | It means |
|---|---|
| the niche pack `woodworking-scripts` | the **woodworking-scripts** skill: its `SKILL.md` is the pack's rules, plus its `references/` folder |
| the persona profile `personas/hank-hardwood.md` | the **hank-hardwood-persona** skill: its `SKILL.md` is the profile |
| the persona profile `personas/dale-oakfield.md` | the **dale-oakfield-persona** skill: its `SKILL.md` is the profile |
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

Use the real folders of the other skills in place of the placeholders:

```
python3 core/script-scanner.py SCRIPT --rules <woodworking-scripts>/SKILL.md <channel-persona>/SKILL.md --pack RESEARCH_PACK --refs <woodworking-scripts>/references/excerpts.md <woodworking-scripts>/references/reference-scripts.md <channel-persona>/SKILL.md
```
"""

INSTALL = """# Installing the skills

**Version:** {stamp}

Six skill files, one per layer. Install them on every account that will do ideation or scripts (yours and each VA's), in claude.ai under Settings, Capabilities, Skills, not in a project. They then work in Claude and in Cowork.

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
"""

def copytree(src, dst, ignore=()):
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", *ignore))

def validate(folder):
    """claude.ai's upload rules: exactly one SKILL.md, YAML frontmatter first, a name, a description of at most 1024 characters."""
    found = [os.path.join(d, f) for d, _, fs in os.walk(folder) for f in fs if f == "SKILL.md"]
    assert found == [os.path.join(folder, "SKILL.md")], f"{folder}: needs exactly one SKILL.md at the top, found {found}"
    s = open(found[0], encoding="utf8").read()
    assert s.startswith("---\n"), f"{folder}: SKILL.md must start with YAML frontmatter (---)"
    head = s.split("\n---\n", 1)[0]
    fields = {k.strip(): v.strip().strip('"') for k, _, v in (l.partition(":") for l in head.splitlines()[1:]) if v}
    name, desc = fields.get("name", ""), fields.get("description", "")
    assert re.fullmatch(r"[a-z0-9-]{1,64}", name), f"{folder}: bad name {name!r}"
    assert 0 < len(desc) <= 1024, f"{folder}: description is {len(desc)} characters (limit 1024)"

def zipdir(folder, out):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        base = os.path.dirname(folder)
        for d, _, files in os.walk(folder):
            for f in sorted(files):
                full = os.path.join(d, f)
                z.write(full, os.path.relpath(full, base))

PERSONAS = {
    "hank-hardwood": ("Hank Hardwood", "personas/hank-hardwood.md", "personas/books/hank-hardwood-book.md"),
    "dale-oakfield": ("Dale Oakfield's Workshop", "personas/dale-oakfield.md", "personas/books/dale-oakfield-book.md"),
}

def build_script_writer():
    out = os.path.join(DIST, "script-writer")
    copytree(os.path.join(ROOT, "core"), os.path.join(out, "core"))
    with open(os.path.join(out, "SKILL.md"), "w") as f:
        f.write(SCRIPT_WRITER_SKILL.replace("{stamp}", STAMP))
    return out

def build_pack():
    out = os.path.join(DIST, "woodworking-scripts")
    copytree(os.path.join(ROOT, "woodworking-scripts"), out, ignore=("archive",))
    return out

def build_persona(slug):
    channel, profile, book = PERSONAS[slug]
    out = os.path.join(DIST, f"{slug}-persona")
    os.makedirs(os.path.join(out, os.path.dirname(book)))
    shutil.copy(os.path.join(ROOT, book), os.path.join(out, book))
    head = (f"---\nname: {slug}-persona\ndescription: The channel profile for {channel}: persona, personal details, "
            f"CTA rules, ending and the channel's book text. Read by the script-writer skill when a script is written "
            f"for this channel (START). Not used on its own.\n---\n\n**Version:** {STAMP}\n\n")
    with open(os.path.join(out, "SKILL.md"), "w") as f:
        f.write(head + open(os.path.join(ROOT, profile), encoding="utf8").read())
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
    for folder in (build_script_writer(), build_pack(), *[build_persona(s) for s in PERSONAS], build_ideation(), build_ideation_core()):
        validate(folder)
        zipdir(folder, folder + ".skill")
        n = sum(len(fs) for _, _, fs in os.walk(folder))
        print(f"built {os.path.relpath(folder, ROOT)}/ ({n} files) and {os.path.relpath(folder, ROOT)}.skill")
    with open(os.path.join(DIST, "INSTALL.md"), "w") as f:
        f.write(INSTALL.replace("{stamp}", STAMP))
    # one folder (zipped) with every skill file and the install guide, for Drive
    bundle = os.path.join(DIST, f"script-system-skills-{datetime.date.today().isoformat()}.zip")
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(os.listdir(DIST)):
            if f.endswith(".skill") or f == "INSTALL.md":
                z.write(os.path.join(DIST, f), os.path.join("script-system-skills", f))
    print(f"bundle: {os.path.relpath(bundle, ROOT)}")
    # the same skills as plain, readable files (a normal zip that opens on any computer)
    readable = os.path.join(DIST, f"script-system-skills-readable-{datetime.date.today().isoformat()}.zip")
    with zipfile.ZipFile(readable, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(DIST, "INSTALL.md"), os.path.join("script-system-skills-readable", "INSTALL.md"))
        for name in sorted(os.listdir(DIST)):
            folder = os.path.join(DIST, name)
            if os.path.isdir(folder):
                for d, _, files in os.walk(folder):
                    for f in sorted(files):
                        full = os.path.join(d, f)
                        z.write(full, os.path.join("script-system-skills-readable", os.path.relpath(full, DIST)))
    print(f"readable: {os.path.relpath(readable, ROOT)}")
    print(f"version: {STAMP}")

if __name__ == "__main__":
    main()
