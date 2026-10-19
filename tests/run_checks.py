# Library test suite: run with  python3 tests/run_checks.py  from the library root (or set LIB_ROOT).
# Checks file references, stale leftovers, override statements, hard-ban and filler parity
# between humanizer.md and script-scanner.py, scanner behavior on clean and broken scripts,
# ban lifting, the numbers check, the woodworking inputs block, shared labels across files, the
# copy guard (--refs) against the niche pack's reference files, the README file map and the test fixtures.
import re, os, glob, subprocess, sys, tempfile, textwrap
sys.dont_write_bytecode = True
ROOT=os.environ.get("LIB_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORE=f"{ROOT}/core"; WW=f"{ROOT}/woodworking-scripts"; SCAN=f"{CORE}/script-scanner.py"
results=[]
def check(name, ok, detail=""):
    results.append((name, ok, detail))

lib_files=[f for f in glob.glob(f"{CORE}/*")+glob.glob(f"{WW}/**/*",recursive=True) if os.path.isfile(f) and not f.endswith(".txt")]
names={os.path.basename(f) for f in lib_files}
rels={os.path.relpath(f,WW) for f in lib_files if f.startswith(WW)}
# docs that point into the whole repo, not only the library
doc_files=glob.glob(f"{ROOT}/personas/*.md")+[f"{ROOT}/README.md",f"{ROOT}/PINNED.md"]
repo_files=[f for f in glob.glob(f"{ROOT}/**/*",recursive=True) if "/.git/" not in f]
repo_names={os.path.basename(f.rstrip("/")) for f in repo_files}

# 1. every referenced file exists
EXTERNAL={"woodworking-ideation/references/audience.md","word-bank.md","personas/hank-hardwood.md","personas/dale-oakfield.md","hank-hardwood.md","dale-oakfield.md","archive/","personas/[channel-name].md"}
missing=[]
for f in lib_files:
    if not f.endswith(".md"): continue
    for ref in re.findall(r"`([^`\s]+?\.(?:md|py)|[a-z-]+/)`", open(f).read()):
        if ref in EXTERNAL: continue
        base=os.path.basename(ref.rstrip("/"))
        if ref.endswith("/"):
            ok = os.path.isdir(os.path.join(WW,ref)) or os.path.isdir(os.path.join(ROOT,ref))
        else:
            ok = base in names or ref in rels
        if not ok: missing.append(f"{os.path.relpath(f,ROOT)} -> {ref}")
for f in doc_files:
    for ref in re.findall(r"`([^`\s]+?\.(?:md|py)|[a-z-]+/)`", open(f).read()):
        if ref in EXTERNAL: continue
        base=os.path.basename(ref.rstrip("/"))
        ok = os.path.exists(os.path.join(ROOT,ref)) or base in repo_names
        if not ok: missing.append(f"{os.path.relpath(f,ROOT)} -> {ref}")
check("1. every file reference resolves (library, personas, README, PINNED)", not missing, "; ".join(sorted(set(missing))))

# 2. no stale leftovers from FacelessOS / house rules
STALE=[r"FacelessOS", r"house rules", r"trailer-voice-scan", r"REAL-FACELESS", r"NICHE-SPECIFIC-HOOKS", r"master file",
       r"Traditional mode", r"Four Pillars", r"PROOF BANK", r"persona canon", r"STEP \d", r"swipe file", r"core output rules",
       r"HOUSE FORMAT", r"TYPE CONFIRMED", r"VOICE CONFIRMED", r"BUILD SHEET"]
hits=[]
# PINNED.md is left out on purpose: it names retired items in its decisions list
for f in lib_files+glob.glob(f"{ROOT}/personas/*.md")+[f"{ROOT}/README.md"]:
    if not (f.endswith(".md") or f.endswith(".py")): continue
    t=open(f).read()
    if f.endswith("/README.md"):   # the map may name the archive it describes
        t="\n".join(l for l in t.splitlines() if "facelessos-original" not in l)
    for p in STALE:
        for m in re.finditer(p,t):
            hits.append(f"{os.path.relpath(f,ROOT)}: '{m.group(0)}'")
check("2. no stale references to the old system", not hits, "; ".join(hits))

# 3. every base file states how it relates to niche packs
base=[f for f in glob.glob(f"{CORE}/*.md") if os.path.basename(f) not in ("workflow.md","channels.md","persona-profile-template.md","claims-policy.md")]
nooverride=[os.path.basename(f) for f in base if "How this file relates" not in open(f).read()]
check("3. every base file carries the override statement", not nooverride, ", ".join(nooverride))

# 4. hard-ban parity: humanizer list vs scanner
sys.path.insert(0,CORE)
import importlib.util
spec=importlib.util.spec_from_file_location("scanner",SCAN); sc=importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
hum=open(f"{CORE}/humanizer.md").read()
block=re.search(r"### Hard bans.*?```\n(.*?)```",hum,re.S).group(1)
phrases=[]
for line in block.splitlines():
    line=line.strip()
    if not line or line.endswith(":"): continue
    if line.startswith("landscape as a metaphor"): phrases.append("evolving landscape"); continue
    line=re.sub(r"\(.*?\)","",line)
    for part in line.split("/"):
        part=part.strip()
        if part: phrases.append(part)
unmatched=[p for p in phrases if not any(re.search(rx,p,re.I) for rx,_ in sc.HARD_BANS)]
check("4. every humanizer hard ban is enforced by the scanner", not unmatched, ", ".join(unmatched))

# 5. filler-phrase parity (H23)
h23=re.search(r"### H23.*?```\n(.*?)```",hum,re.S).group(1)
h23_list=[p.strip() for p in h23.replace("\n"," ").split(",") if p.strip()]
check("5. H23 phrases match the scanner's list", sorted(h23_list)==sorted(sc.SPARING), f"humanizer={sorted(h23_list)} scanner={sorted(sc.SPARING)}")

def run_scan(text, rules=(), pack=None, refs=()):
    with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write(text); p=t.name
    cmd=["python3",SCAN,p]+(["--rules",*rules] if rules else [])+(["--pack",pack] if pack else [])+(["--refs",*refs] if refs else [])
    r=subprocess.run(cmd,capture_output=True,text=True); return r.returncode, r.stdout

WWR=f"{WW}/SKILL.md"
# 6. a clean, rule-following woodworking script passes with zero fix-on-sight
clean=textwrap.dedent("""\
SCRIPT TYPE: Talking Head

Two 2x4s, about nine bucks at Lowe's, and twenty little shelf brackets you can sell. Prices subject to change.

Grab two 2x4x8 boards. Pick through the pile for the straightest ones. Cut each board into 16-inch pieces. Flip them. Sand the edges.

===START CTA(100 Ways to Make Your First $1,000 with Woodworking)===
Quick one. Every measurement for this bracket, plus a hundred more projects, is in my digital book, first link in the description. Back to the cut.
===END CTA===

Number two. Clamp a stop block at five and three-quarters inches, and let the blade stop before you lift it, so the offcut can't kick back.

These are listed between 14 and 22 dollars on Etsy, and I'd list them around 18.

===START CTA(100 Ways to Make Your First $1,000 with Woodworking)===
The book's in the description if you want the other ninety-nine. Subscribe so the next build shows up in your feed.
===END CTA===

Cut one board this weekend and see what it turns into.

VERDICT: PASS
ROTATION LOG ENTRY: test | stick around | bonus at the end
AUDIT EVIDENCE
VO COPY — ELEVENLABS V4
[warm] Stick around for the bonus at the end.
""")
code,out=run_scan(clean,[WWR])
fix=re.search(r"FIX ON SIGHT \((\d+)\)",out).group(1)
check("6. clean script with markers, skeleton and VO copy: zero fix-on-sight", fix=="0" and code==0, out if fix!="0" else "")
check("6b. 'Number two.' and short instructions not flagged as staccato", "staccato" not in out, out)

# 7. a broken script is caught
broken=textwrap.dedent("""\
Most people think pine is junk. Most woodworkers never use it. Let's get into it, and stick around for the bonus at the end.

I'm cutting the first piece now, right here. The fix is cheap — really cheap — and it's “easy”… That's twenty bucks an hour.

No glue. No nails. No excuses. The truth is it works. The truth is it lasts.
""")
code,out=run_scan(broken,[WWR])
need=["let's get into it","tease: stick around","tease: bonus at the end","first-person build narration","pointing at generated footage","em dash","curly quote","single-character ellipsis","hourly-wage framing"]
miss=[n for n in need if n not in out]
check("7. broken script: every planted problem caught", not miss and code==1, "missed: "+", ".join(miss))
check("7b. 'Most...' over the cap, staccato and filler flagged", "over the cap" in out and "staccato" in out and '"the truth is" x2' in out, out)

# 8. a persona file can lift a ban
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("```scanner\nlift: let's get into it\n```\n"); lift=t.name
code,out=run_scan("Cut the board. Let's get into it.\n",[WWR,lift])
check("8. persona lift removes exactly that ban", "let's get into it" in out.split("FIX ON SIGHT")[0] and "HARD BAN: let's get into it" not in out, out)
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("```scanner\nlift: robust\nlift: AI vocabulary\nlift: stick\n```\n"); lift2=t.name
code,out=run_scan("A robust jig. Delve into the tapestry and unleash it. Stick around.\n",[WWR,lift2])
check("8b. lifting one word lifts only that word; a group name or partial phrase lifts nothing",
      "HARD BAN: robust" not in out and all(f"HARD BAN: {w}" in out for w in ("delve","tapestry","unleash")) and "HARD BAN: tease: stick around" in out, out)

# 9. numbers check against a research pack
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("MATERIALS\n- 2x4x8 | Lowe's | $4.65\nLISTINGS\n- Etsy $14 | $22\nprice 18\n"); pk=t.name
code,out=run_scan("They list between 14 and 22 dollars, and I'd ask 18. Some folks clear $950 a month.\n",[],pk)
check("9. numbers check flags only the invented figure", "950" in out and " 18 " not in out.split("NUMBERS NOT FOUND")[1], out)
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("PRICE\n- listed at $42\n- costs $12.60\n"); pk2=t.name
code,out=run_scan("They're listed at $46. Each one costs about thirteen bucks to make.\n",[],pk2)
check("9b. numbers check: a price nudged up 10% is flagged, spoken rounding is not", "46" in out.split("NUMBERS NOT FOUND")[1] and "13  <<" not in out.split("NUMBERS NOT FOUND")[1], out)

# 10. woodworking inputs block parses
sk=open(WWR).read()
inp=re.search(r"```inputs\n(.*?)```",sk,re.S)
rows=[l for l in inp.group(1).splitlines() if l.strip().startswith("-")] if inp else []
okrows=all(len(r.split("|"))==3 for r in rows)
check("10. woodworking inputs block: 4 well-formed inputs", inp is not None and len(rows)==4 and okrows, str(rows))

# 11. shared strings agree across files
wf=open(f"{CORE}/workflow.md").read(); ga=open(f"{CORE}/greenlight-audit.md").read(); vr=open(f"{CORE}/variety-rotation.md").read()
pairs=[("NOT READY: DO NOT UPLOAD", wf, ga), ("AUDIT EVIDENCE", wf, ga), ("ROTATION LOG ENTRY:", wf, vr), ("three", wf, ga)]
bad=[p for p,a,b in pairs if p not in a or p not in b]
check("11. shared labels match between workflow, audit and rotation files", not bad, ", ".join(bad))

# 12. copy guard: a line copied from a reference file is caught; normal text is not
REFS=[f for f in (f"{WW}/references/excerpts.md", f"{WW}/references/reference-scripts.md") if os.path.isfile(f)]
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t:
    t.write('1. "Slide up to the lumber yard and grab yourself a 1x4x8 for around eight bucks." [Ref \u00b7 test \u00b7 0:00 \u00b7 9.9x]\n'); tref=t.name
copied="Cut your boards to length.\n\nSo slide up to the Lumber Yard, and grab yourself a 1x4x8 for around eight bucks, then sand it.\n"
code,out=run_scan(copied,[WWR],refs=[tref])
check("12. copy guard: a copied line is flagged fix-on-sight (case and punctuation ignored)",
      code==1 and "COPIED FROM REFERENCE" in out and "slide up to the lumber yard and grab yourself a 1x4x8 for around eight bucks" in out, out)
code,out=run_scan("Grab yourself a board and slide it up to the fence before you cut eight pieces.\n",[WWR],refs=[tref])
check("12b. copy guard: shared words under 8 in a row are not flagged", code==0 and "COPIED FROM REFERENCE" not in out, out)
code,out=run_scan(clean,[WWR],refs=REFS)
check("12c. copy guard: the clean script passes against the pack's real reference files",
      len(REFS)>=1 and code==0 and "COPIED FROM REFERENCE" not in out, f"refs={REFS} "+out[:600])
if REFS:
    line=None
    for l in open(REFS[-1]).read().splitlines():
        words=re.findall(r"[A-Za-z0-9']+", re.sub(r"\[[^\]]*\]","",l))
        if len(words)>=14 and not l.lstrip().startswith(("#","|","-","*",">")): line=" ".join(words[:12])+"."; break
    code,out=run_scan(f"Measure twice.\n\n{line}\n",[WWR],refs=REFS)
    check("12d. copy guard: a line lifted from the pack's own reference file is caught", line is not None and code==1 and "COPIED FROM REFERENCE" in out, f"line={line!r} "+out[:600])

# 13. README file map lists every library file (CLAUDE.md rule 7)
readme=open(f"{ROOT}/README.md").read()
mapped=[f for f in glob.glob(f"{CORE}/*")+glob.glob(f"{WW}/*.md")+glob.glob(f"{WW}/references/*")+glob.glob(f"{ROOT}/personas/*.md")
        +glob.glob(f"{ROOT}/tests/*.py")+glob.glob(f"{ROOT}/tests/fixtures/*.md")+glob.glob(f"{ROOT}/*.md") if os.path.isfile(f)]
mapped+=[f"{ROOT}/{d}" for d in ("studies/","archive/facelessos-original/","tests/iterations/","tests/fixtures/personas/","tests/fixtures/inputs/","tests/fixtures/judge-only/","woodworking-scripts/archive/")]
def in_map(f):
    name=os.path.basename(f.rstrip("/"))+("/" if f.endswith("/") else "")
    return re.search(r"`(?:[^`\s]*/)?"+re.escape(name)+r"`",readme) is not None
unmapped=[os.path.relpath(f,ROOT) for f in mapped if not in_map(f)]
check("13. README file map lists every library file and folder", not unmapped, ", ".join(unmapped))

# 14. persona profiles (real and TEST) fill every template field
tmpl=re.search(r"```\n(PERSONA PROFILE.*?)```",open(f"{CORE}/persona-profile-template.md").read(),re.S).group(1)
labels=[l.split(":")[0].strip() for l in tmpl.splitlines() if ":" in l and not l.rstrip().endswith("for each one:")]
labels=[l for l in labels if l and not l.startswith(("or ","plain "))]
gaps=[]
for f in glob.glob(f"{ROOT}/personas/*.md")+glob.glob(f"{ROOT}/tests/fixtures/personas/*.md"):
    if os.path.basename(f)=="README.md": continue
    body=open(f).read()
    for lab in labels:
        m=re.search(r"^\s*"+re.escape(lab)+r":[ \t]*(\S.*)$",body,re.M)
        if not m: gaps.append(f"{os.path.relpath(f,ROOT)}: {lab}")
check("14. every persona profile fills every template field", not gaps, "; ".join(gaps))

# 15. TEST data stays in tests/fixtures/, and fixtures are labelled TEST
FIX=f"{ROOT}/tests/fixtures"
fx=[f for f in glob.glob(f"{FIX}/**/*",recursive=True) if os.path.isfile(f)]
unlabelled=[os.path.relpath(f,ROOT) for f in fx if "TEST" not in open(f).read()]
real_rows=re.findall(r"^\|\s*\d+\s*\|([^|]+)\|",open(f"{CORE}/channels.md").read(),re.M)
test_rows=re.findall(r"^\|\s*\d+\s*\|([^|]+)\|",open(f"{FIX}/channels.md").read(),re.M) if os.path.isfile(f"{FIX}/channels.md") else []
leaks=[r.strip() for r in real_rows if "TEST" in r]+[os.path.basename(f) for f in glob.glob(f"{ROOT}/personas/*.md") if "TEST DATA" in open(f).read()]
badtest=[r.strip() for r in test_rows if not r.strip().startswith("TEST")]
check("15. fixtures are labelled TEST, TEST channels start with TEST, and none leak into core/channels.md or personas/",
      fx and test_rows and not unlabelled and not leaks and not badtest, f"unlabelled={unlabelled} leaks={leaks} badtest={badtest}")

for name,ok,detail in results:
    print(("PASS " if ok else "FAIL ")+name+("" if ok else f"\n      -> {detail[:900]}"))
print(f"\n{sum(ok for _,ok,_ in results)}/{len(results)} passed")
