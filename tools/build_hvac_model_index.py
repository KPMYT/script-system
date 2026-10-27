# Builds hvac-scripts/references/models/INDEX.md from the model files' headers, grouped by the video types in
# hvac-scripts/SKILL.md (2026-10-27). Run: python3 tools/build_hvac_model_index.py
import re, glob, os
root = os.environ.get("LIB_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MD = f"{root}/hvac-scripts/references/models"
TYPES = [  # the SKILL.md video-types table; a model may serve more than one type
    ("Single-product fix", ["R35", "R36", "R15", "R20"]),
    ("N things about one product", ["R33", "R34"]),
    ("Never-do list", ["R26", "R16"]),
    ("Mistakes or habits list", ["R24", "R25"]),
    ("Head-to-head or ranked verdict", ["R37", "R39", "R04"]),
    ("Banned / rule explainer", []),
    ("How-to / correct way", ["R23", "R13", "R21", "R06", "R15"]),
    ("Product swap", ["R42", "R43", "R05", "R18"]),
    ("Hidden cause or symptom", ["R27", "R28", "R30", "R31", "R32", "R44", "R20", "R06"]),
    ("Seasonal or emergency", ["R22", "R23", "R40", "R41", "R17"]),
    ("Brand verdict", ["R38"]),
]
files = {os.path.basename(f).split("-")[0]: f for f in glob.glob(f"{MD}/R*.md")}
def row(i):
    f = files.get(i)
    if not f: return f"| {i} | (file not written yet) | | | | |"
    s = open(f, encoding="utf8").read()
    title = s.split("\n", 1)[0].split(". ", 1)[1].strip().replace("|", "\\|")
    ch = re.search(r"\*\*Channel:\*\*\s*([^·\n]+)", s); vn = re.search(r"\*\*Views(?: / normal)?:\*\*\s*([^\n(·]+)", s)
    ln = re.search(r"\*\*Length:\*\*\s*([0-9:]+)", s)
    apart = re.search(r"What sets it apart[^\n]*\n\s*- ([^\n]+)", s) or re.search(r"## What to take from it\n\n([^\n]+)", s)
    note = (apart.group(1).strip() if apart else "").replace("|", "\\|")
    return f"| [{i}]({os.path.basename(f)}) | {title} | {ch.group(1).strip() if ch else ''} | {vn.group(1).strip() if vn else ''} | {ln.group(1) if ln else ''} | {note} |"
out = ["# Model library: HVAC", "",
       "Winning videos sorted by video type, each one file with a beat map (what each stretch does, with timings, items, promise devices, money, safety and CTA placement; no wording) and the full labelled script. Built by `tools/build_hvac_model_index.py` from the files' headers.", "",
       "- **Every model is a real person on camera** (operator, 2026-10-27: \"we dont want any ai or faceless for reference\"): borrow structure and voice. No faceless or AI-voiced video, our own channels' included, is a model.",
       "- **R22 onward** are HVAC videos from the HVAC study (`studies/hvac/`). **R04-R21** are the ten plumbing and home-repair models kept from the plumbing pack (Silver Cymbal, Roger Wakefield, Arrow Pest Service, Nailed it) for shapes HVAC has no proven script for.", "",
       "**How to use them** (SKILL.md, \"Using the models: never a copy\"): at the planning step, where a model fits, pick one or two for the video type that weren't used in the channel's last five scripts, read their beat maps first, and name at least three things this script does differently. Never copy wording; the copy guard flags 8 words in a row. Each file's \"Doesn't transfer\" section lists the on-camera moves, unsafe steps and claims to leave behind.", "",
       "**Read with care:** R26 and R39 (Technology Connections) hold only the stretches they're picked for. R37 (Project Farm) is filmed tests: only its ranking structure transfers. R30, R31 and R41 work on live parts or wiring: take their openings and symptoms, never their hands-on steps. R21 holds the drywall video's two opening moves only, with no script.", ""]
for t, ids in TYPES:
    out += [f"## {t} ({len(ids)} model{'s' if len(ids) != 1 else ''})", ""]
    if not ids:
        out += ["None yet: build it from the opening's six jobs in SKILL.md.", ""]; continue
    out += ["| File | Title | Channel | Views / normal | Length | What sets it apart |", "|---|---|---|---|---|---|"] + [row(i) for i in ids] + [""]
listed = {i for _, ids in TYPES for i in ids}
extra = sorted(set(files) - listed)
if extra: out += ["## Not yet filed under a type", ""] + [f"- {i}" for i in extra] + [""]
open(f"{MD}/INDEX.md", "w", encoding="utf8").write("\n".join(out))
print(len(files), "model files;", len(listed), "listed; not filed:", extra)
