# Library test suite: run with  python3 tests/run_checks.py  from the library root (or set LIB_ROOT).
# Checks file references, stale leftovers, override statements, hard-ban and filler parity
# between humanizer.md and script-scanner.py, scanner behavior on clean and broken scripts,
# ban lifting, the numbers check, the woodworking inputs block, shared labels across files, the
# copy guard (--refs) against the niche pack's reference files, production notes read aloud,
# repeated sentences, persona facts (tenure, near-miss names, title numbers win), the tease phrasings and once-per-script phrases,
# and the plumbing pack: its inputs block, scanner block, Mark's contraction ban, the copy guard over every model file,
# the plumbing profiles' fixed facts and the channel list, the HVAC pack (checks 60-68), Werner's profile (70) and the plumbing escalation line (46b).
#
# P21 (operator 2026-11-06, "yes use defaults"): style, plumbing, HVAC and woodworking now run on the simple packs (SKILL.md,
# check.py, references/) and one-page persona pages. The old packs and profiles are in archive/pre-p21-2026-11-06/ (read-only).
# - Checks that test the core scanner (core/script-scanner.py, still shipped in script-writer and used by electrical) keep the
#   archived pack and profile files as read-only rule fixtures (OWW, OPL, OHV, OSTY, OPERS below): they test the scanner, not those packs.
# - Checks of a rule that still exists in the new version are retargeted to the new files (mostly to each pack's check.py).
# - Checks of a rule the new version dropped are retired: their numbers stay in "retired 2026-11-06, P21" comment blocks, never reused.
# - New checks 94-99 (93 is taken by the unmerged stoic-mayer branch; 78-82 left free as before) test the new packs.
import re, os, glob, subprocess, sys, tempfile, textwrap
sys.dont_write_bytecode = True
ROOT=os.environ.get("LIB_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORE=f"{ROOT}/core"; WW=f"{ROOT}/woodworking-scripts"; PL=f"{ROOT}/plumbing-scripts"; PERS=f"{ROOT}/personas"; SCAN=f"{CORE}/script-scanner.py"
OLD=f"{ROOT}/archive/pre-p21-2026-11-06"   # read-only fixtures for the core scanner checks (P21)
OWW=f"{OLD}/woodworking-scripts"; OPL=f"{OLD}/plumbing-scripts"; OHV=f"{OLD}/hvac-scripts"; OSTY=f"{OLD}/style-scripts"; OPERS=f"{OLD}/personas"
HV=f"{ROOT}/hvac-scripts"; STY=f"{ROOT}/style-scripts"
NPACK={"style":STY,"plumbing":PL,"hvac":HV,"woodworking":WW}
IT=f"{ROOT}/tests/iterations"
# the saved P21 test scripts: (pack, script, channel, brief); the title is the brief's TITLE line
P21_RUNS=[("style",f"{IT}/iter-14/final/script.txt","scarlett",f"{IT}/iter-14/brief.txt"),
          ("style",f"{IT}/iter-15/run-new/script.txt","diane",f"{IT}/iter-15/brief.txt"),
          ("plumbing",f"{IT}/iter-16/run-roger/script.txt","roger",f"{IT}/iter-16/brief-roger.txt"),
          ("plumbing",f"{IT}/iter-16/run-mark/script.txt","mark",f"{IT}/iter-16/brief-mark.txt"),
          ("plumbing",f"{IT}/iter-16/run-vintage/script.txt","vintage",f"{IT}/iter-16/brief-vintage.txt"),
          ("plumbing",f"{IT}/iter-16/run-werner/script.txt","werner",f"{IT}/iter-16/brief-werner.txt"),
          ("hvac",f"{IT}/iter-17/run-new/script.txt","roger-hvac",f"{IT}/iter-17/brief.txt"),
          ("woodworking",f"{IT}/iter-18/run-hank/script.txt","hank",f"{IT}/iter-18/brief-hank.txt"),
          ("woodworking",f"{IT}/iter-18/run-dale/script.txt","dale",f"{IT}/iter-18/brief-dale.txt")]
def title_of(brief): return re.search(r"^TITLE: (.*)$",open(brief).read(),re.M).group(1).strip()
def pack_check(pack, text, channel, brief, title=None):
    """Run a P21 pack's check.py on a script text; returns (exit code, output)."""
    with tempfile.NamedTemporaryFile("w",suffix=".txt",delete=False) as t: t.write(text); p=t.name
    r=subprocess.run([sys.executable,"-B",f"{NPACK[pack]}/check.py",p,"--channel",channel,"--title",title or title_of(brief),"--brief",brief],capture_output=True,text=True)
    return r.returncode, r.stdout+r.stderr
def run_of(channel): return next(r for r in P21_RUNS if r[2]==channel)
def plant(channel, line, where=2):
    """The channel's passing test script with one line added as its own paragraph (after paragraph `where`), run through its check.py."""
    pack,script,ch,brief=run_of(channel)
    paras=open(script).read().split("\n\n")
    paras.insert(where,line)
    return pack_check(pack,"\n\n".join(paras),ch,brief)
def load_check(pack):
    import importlib.util as _u
    sp=_u.spec_from_file_location(f"p21_{pack}",f"{NPACK[pack]}/check.py"); m=_u.module_from_spec(sp); sp.loader.exec_module(m); return m
results=[]
def check(name, ok, detail=""):
    results.append((name, ok, detail))

lib_files=[f for f in glob.glob(f"{CORE}/*")+glob.glob(f"{WW}/**/*",recursive=True) if os.path.isfile(f) and not f.endswith(".txt")]
pl_files=[f for f in glob.glob(f"{PL}/**/*",recursive=True)+glob.glob(f"{PERS}/**/*",recursive=True) if os.path.isfile(f) and not f.endswith(".txt")]
names={os.path.basename(f) for f in lib_files}
rels={os.path.relpath(f,WW) for f in lib_files if f.startswith(WW)}
# the plumbing pack and the profiles may also cite the study files they were built from
repo_files=[os.path.join(d,f) for d,ds,fs in os.walk(ROOT) if "/.git" not in d and "/dist" not in d for f in fs]
repo_names={os.path.basename(f) for f in repo_files}
repo_rels={os.path.relpath(f,base) for f in repo_files for base in (ROOT,PL,PERS) if f.startswith(base+"/")}

# 1. every referenced file exists
EXTERNAL={"woodworking-ideation/references/audience.md","word-bank.md","personas/hank-hardwood.md","personas/dale-oakfield.md","archive/","personas/[channel-name].md"}
missing=[]
for f in lib_files:
    if not f.endswith(".md"): continue
    for ref in re.findall(r"`([^`\s]+?\.(?:md|py)|[a-z-]+/)`", open(f).read()):
        if ref in EXTERNAL: continue
        base=os.path.basename(ref.rstrip("/"))
        if ref.endswith("/"):
            ok = os.path.isdir(os.path.join(WW,ref)) or os.path.isdir(os.path.join(ROOT,ref))
        else:
            # P21: core still names the old woodworking pack's files (archived) and the new models cite their study files (meta.md)
            ok = base in names or ref in rels or os.path.isfile(os.path.join(ROOT,ref)) or base in repo_names
        if not ok: missing.append(f"{os.path.relpath(f,ROOT)} -> {ref}")
check("1. every file reference resolves", not missing, "; ".join(sorted(set(missing))))

# 1b. the same for the plumbing pack and the persona profiles (placeholders in templates and specs aside)
PLACEHOLDER={"plumbing-ideation/references/audience.md","references/models/R01-...md","S18-...md","<ID>-<channel-slug>-<short-topic-slug>.md"}
missing=[]
for f in pl_files:
    if not f.endswith(".md"): continue
    for ref in re.findall(r"`([^`\s]+?\.(?:md|py)|[a-z-]+/)`", open(f).read()):
        if ref in PLACEHOLDER: continue
        if ref.endswith("/"):
            ok = any(os.path.isdir(os.path.join(b,ref)) for b in (ROOT,PL,PERS,os.path.dirname(f)))
        else:
            ok = os.path.basename(ref) in repo_names or ref in repo_rels
        if not ok: missing.append(f"{os.path.relpath(f,ROOT)} -> {ref}")
check("1b. every file reference in the plumbing pack and the persona profiles resolves", not missing, "; ".join(sorted(set(missing))))

# 2. no stale leftovers from FacelessOS / house rules
STALE=[r"FacelessOS", r"house rules", r"trailer-voice-scan", r"REAL-FACELESS", r"NICHE-SPECIFIC-HOOKS", r"master file",
       r"Traditional mode", r"Four Pillars", r"PROOF BANK", r"persona canon", r"STEP \d", r"swipe file", r"core output rules"]
hits=[]
for f in lib_files+[f for f in pl_files if f.startswith(PL)]:
    if not (f.endswith(".md") or f.endswith(".py")): continue
    t=open(f).read()
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

def run_scan(text, rules=(), pack=None, refs=(), title=None):
    with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write(text); p=t.name
    cmd=["python3",SCAN,p]+(["--rules",*rules] if rules else [])+(["--pack",pack] if pack else [])+(["--refs",*refs] if refs else [])+(["--title",title] if title else [])
    r=subprocess.run(cmd,capture_output=True,text=True); return r.returncode, r.stdout

WWR=f"{OWW}/SKILL.md"   # P21: the archived woodworking pack's scanner block, a read-only fixture for the core scanner checks
# 6. a clean, rule-following woodworking script passes with zero fix-on-sight
clean=textwrap.dedent("""\
SCRIPT TYPE: Talking Head

Two two by fours, about nine bucks at Lowe's, and twenty little shelf brackets you can sell. Prices subject to change.

Grab two eight-foot two by fours. Pick through the pile for the straightest ones. Cut each board into 16-inch pieces. Flip them. Sand the edges.

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
need=["let's get into it","tease: stick around","tease: bonus at the end","first-person build narration","pointing: right here","em dash","curly quote","single-character ellipsis","hourly-wage framing"]
miss=[n for n in need if n not in out]
check("7. broken script: every planted problem caught", not miss and code==1, "missed: "+", ".join(miss))
check("7b. 'Most...' over the cap, staccato and filler flagged", "over the cap" in out and "staccato" in out and '"the truth is" x2' in out, out)

# 8. a persona file can lift a ban
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("```scanner\nlift: let's get into it\n```\n"); lift=t.name
code,out=run_scan("Cut the board. Let's get into it.\n",[WWR,lift])
check("8. persona lift removes exactly that ban", "let's get into it" in out.split("FIX ON SIGHT")[0] and "HARD BAN: let's get into it" not in out, out)

# 9. numbers check against a research pack
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("MATERIALS\n- 2x4x8 | Lowe's | $4.65\nLISTINGS\n- Etsy $14 | $22\nprice 18\n"); pk=t.name
code,out=run_scan("They list between 14 and 22 dollars, and I'd ask 18. Some folks clear $950 a month.\n",[],pk)
check("9. numbers check flags only the invented figure", "950" in out and " 18 " not in out.split("NUMBERS NOT FOUND")[1], out)

# 10. retired 2026-11-06, P21: the woodworking pack has no inputs block any more (its SKILL.md lists the inputs in words;
#     the research-pack rule is kept, operator default 2026-11-06)

# 11. shared strings agree across files
wf=open(f"{CORE}/workflow.md").read(); ga=open(f"{CORE}/greenlight-audit.md").read(); vr=open(f"{CORE}/variety-rotation.md").read()
pairs=[("NOT READY: DO NOT UPLOAD", wf, ga), ("AUDIT EVIDENCE", wf, ga), ("ROTATION LOG ENTRY:", wf, vr), ("three", wf, ga)]
bad=[p for p,a,b in pairs if p not in a or p not in b]
check("11. shared labels match between workflow, audit and rotation files", not bad, ", ".join(bad))

# 12. copy guard: a line copied from a reference file is caught; normal text is not
REFS=[f for f in (f"{OWW}/references/excerpts.md", f"{OWW}/references/reference-scripts.md") if os.path.isfile(f)]  # P21: archived fixtures
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

# 13. a profile's allow: lines are exempt from the copy guard; anything else copied from the profile is still caught
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("Closing line: Keep all ten fingers and I'll see you at the bench.\nVoice: casual run-on sentences broken by short punchy fragments, never scripts.\n\n```scanner\nallow: Keep all ten fingers and I'll see you at the bench\n```\n"); prof=t.name
code1,out1=run_scan("Sand it.\n\nKeep all ten fingers and I'll see you at the bench.\n",[prof],refs=[prof])
code2,out2=run_scan("Sand it.\n\nCasual run-on sentences broken by short punchy fragments work best.\n",[prof],refs=[prof])
check("13. copy guard: a profile's allow: line passes; a copied example line from the profile is caught",
      code1==0 and "COPIED" not in out1 and code2==1 and "COPIED FROM REFERENCE" in out2, out1+out2)

# 14. production notes read aloud are fix-on-sight; ordinary words that look like them are not
code,out=run_scan("Rinse the trap. Mid-roll subscribe CTA. Quick thing before number six.\n\nContinuing with the final sections now, number five is paint.\n\nBonus tip stinger. One more before you go.\n")
need=["CTA label","mid-roll label","section label","stinger label"]
miss=[n for n in need if n not in out]
code2,out2=run_scan("Cut to length, then cut the pipe to sixteen inches. A section of pipe this old needs care.\n")
check("14. production notes read aloud are caught; 'cut to length' and 'a section of pipe' are not",
      not miss and code==1 and "PRODUCTION NOTE" not in out2 and code2==0, "missed: "+", ".join(miss)+" | "+out2[:400])

# 15. the same sentence twice in a row
code,out=run_scan("Number four. Number four. Pour the soda in hot water.\n")
code2,out2=run_scan("Number four. Pour it in. Number five. Pour it in slowly.\n")
check("15. the same sentence twice in a row is caught; a repeated word pattern with different sentences is not",
      code==1 and "REPEATED SENTENCE" in out and "REPEATED SENTENCE" not in out2, out+out2)

# 16. persona facts from a profile: tenure and near-miss names
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t:
    t.write("```scanner\nname: The Vintage Pipefitter\nname: Mark Silverbridge\ntenure: 45\n```\n"); facts=t.name
code,out=run_scan("Well, I have been a plumber for over 35 years. Subscribe to the Vintage Plumber. Mark Silverbrook here.\n",[facts])
code2,out2=run_scan("I've been on the tools for 45 years. Subscribe to The Vintage Pipe Fitter, the Pipefitter way. This pipe held 20 years of grease, and in 10 years your pipes will thank you.\n",[facts])
code3,out3=run_scan("After 40 years at the bench I know this.\n",[f"{OPERS}/hank-hardwood.md"])
check("16. persona facts: a wrong tenure and near-miss names are caught; the right tenure, spacing variants and other 'years' are not; tenure none catches any figure",
      code==1 and out.count("PERSONA FACT: tenure")==1 and '"the Vintage Plumber"' in out and '"Mark Silverbrook"' in out
      and "PERSONA FACT" not in out2 and code2==0 and "PERSONA FACT: tenure" in out3 and code3==1, out+out2+out3)

# 17. the tease phrasings found in the plumbing study are hard bans
teases=["Stay till the end because I'll show you.","And stick with me for number nine.","So do not go clicking away early on me.",
        "Hang on for the bonus habit.","Stay for number 10, because that one matters.","I'll save the best one for you at the very end.",
        "By the end, you'll have the routine.","And the bonus tip at the end could save you.",
        "Wait until you hear what it does to the seal.","So stay right here with me.","Please do not skip out on me now.",
        "I'm keeping a running tally of every dollar you save, and at the very end I'll add it up."]
missed=[t for t in teases if run_scan(t+"\n")[0]!=1]
check("17. tease phrasings from the plumbing study are hard bans", not missed, "; ".join(missed))

# 18. the woodworking channels carry their fixed facts (P21: retargeted from the profiles' scanner blocks to woodworking-scripts/check.py)
wwc=load_check("woodworking").CHANNELS
c18=[plant(ch,"After 40 years at the bench I know this.")[1] for ch in ("dale",)]
check("18. woodworking check.py: Hank's and Dale's names, printed and spoken book titles and last lines; Dale's '40 years' fails unless the title says it",
      wwc["hank"]["name"]=="Hank Hardwood" and wwc["dale"]["name"]=="Dale Oakfield's Workshop"
      and wwc["hank"]["printed"].startswith("100 Ways to Make Your First $1,000") and wwc["dale"]["printed"].startswith("The Ultimate DIY Woodworking Guide")
      and wwc["hank"]["last_line"]=="Keep all ten fingers and I'll see you at the bench." and wwc["dale"]["last_line"]=="Now go make some sawdust."
      and "the book's '40 Years'" in c18[0], c18[0][-600:])

# 19. title numbers win: a years figure in the locked title is allowed; any third figure still fails
code,out=run_scan("I have been a plumber for 30 years, and this one matters.\n",[facts],title="Borax vs Washing Soda: A 30-Year Plumber's Verdict")
code2,out2=run_scan("I have been a plumber for 35 years, and this one matters.\n",[facts],title="Borax vs Washing Soda: A 30-Year Plumber's Verdict")
code3,out3=run_scan("After 40 years at the bench I know this.\n",[f"{OPERS}/hank-hardwood.md"],title="What 40 Years of Woodworking Taught Me")
code4,out4=run_scan("I've been on the tools for 45 years.\n",[facts],title="Pour This Down Your Drain Tonight")
check("19. title numbers win: the title's years figure passes (also with tenure none); a third figure fails; no title figure leaves the profile's",
      code==0 and "PERSONA FACT" not in out and code2==1 and "title says 30" in out2 and code3==0 and code4==0, out+out2+out3+out4)

# 20. a niche pack's once-per-script phrases: the first use passes, the second is fix-on-sight
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t:
    t.write("```scanner\nonce-regex: \\bnine (?:times )?out of (?:10|ten)\\b | nine times out of 10\nonce: between you and me\n```\n"); oncef=t.name
code,out=run_scan("Nine times out of 10 it is the flapper. Between you and me, it is a cheap part.\n",[oncef])
code2,out2=run_scan("Nine times out of 10 it is the flapper.\n\nAnd nine out of ten times the chain is fine too.\n",[oncef])
check("20. once-per-script phrases from a niche pack: one use passes, a second use anywhere in the script is fix-on-sight",
      code==0 and "NICHE/PERSONA LIMIT" not in out and code2==1 and "NICHE/PERSONA LIMIT: nine times out of 10] used 2 times" in out2, out+out2)

# ---- the plumbing pack (step 4, 2026-10-21) ----
# P21: PLR and the three profiles here are the archived files, read-only fixtures for the core scanner checks (29, 30, 32, 63, 74);
# the new pack's rules are tested through plumbing-scripts/check.py on the saved iter-16 scripts.
PLR=f"{OPL}/SKILL.md"; ROGER=f"{OPERS}/roger-the-pipe-guy.md"; MARK=f"{OPERS}/mark-silverbridge.md"; VINT=f"{OPERS}/vintage-pipefitter.md"
want={"title":"required","brief":"required","research-pack":"not used","rotation-log":"required"}   # the electrical inputs (check 46)
def facts_of(p): return [l.strip() for l in re.findall(r"```scanner\n(.*?)```",open(p).read(),re.S)[0].splitlines()]
plc=load_check("plumbing").CHANNELS
def passing(channel):
    pk,sc_,ch_,br=run_of(channel); return pack_check(pk,open(sc_).read(),ch_,br)

# 21. retired 2026-11-06, P21: the plumbing pack has no inputs block (title and brief are listed in words; the rotation log is dropped)

# 22. plumbing bans (P21: retargeted from the scanner block to check.py): each planted ban fails on Roger's passing iter-16 script;
#     a once-phrase used twice fails
p22={"a first-person test or demonstration":"I tested all three on a slow sink.","pointing at the screen":"Look at the trap on the left before you start.",
     "a template stock line":"It's not a scam, it's just economics.","hype that got mocked":"It looked like a horror movie under there.",
     "a channel or name intro":"Today we're going to fix the drain."}
bad=[lab for lab,line in p22.items() if f"FAIL banned: {lab}" not in plant("roger",line)[1]]
twice=plant("roger","Between you and me, it is the flapper. And between you and me, the chain is fine too.")
check("22. plumbing check.py: each planted ban fails on Roger's passing script; 'between you and me' twice fails",
      passing("roger")[0]==0 and not bad and "FAIL said twice: 'between you and me', said 2 times" in twice[1], f"missed: {bad} | "+twice[1][-400:])

# 23. Mark's contraction ban (P21: retargeted to check.py): a contraction planted in his passing script fails; his own script passes
c23=plant("mark","Don't pour it in dry. It's the flapper, and you'll want a cheap part.")
check("23. Mark's contraction ban: contractions fail on his passing script; his plain style passes",
      passing("mark")[0]==0 and c23[1].count("FAIL contraction")>=3 and plc["mark"]["contractions"] is False and plc["werner"]["contractions"] is False, c23[1][-500:])

# 24. copy guard over the plumbing models (P21: retargeted to check.py, which guards the model transcripts): eight words in a row
#     lifted from each of the seven models fail, and are traced to that model file
miss24=[]
PLM=sorted(glob.glob(f"{PL}/references/models/*.md"))
for m in PLM:
    tr=re.findall(r"[\w']+",open(m).read().split("## Transcript",1)[1])
    lift=" ".join(tr[60:72])
    if f"from {os.path.basename(m)}" not in plant("roger",lift[0].upper()+lift[1:]+".")[1]: miss24.append(os.path.basename(m))
check("24. copy guard: a twelve-word run lifted from each of the seven plumbing models fails check.py, traced to its file",
      len(PLM)==7 and not miss24, f"models={len(PLM)} not caught: {miss24}")

# 25. the plumbing channels' fixed facts (P21: retargeted from the profiles' scanner blocks to check.py's CHANNELS)
check("25. plumbing check.py: names, tenures 45, 40, 45, 30; Roger's, Mark's and Werner's books; the Vintage Pipefitter has none",
      [plc[c]["name"] for c in ("roger","mark","vintage","werner")]==["Roger the Pipe Guy","Mark Silverbridge","The Vintage Pipefitter","Werner Finkbeiner"]
      and [plc[c]["tenure"] for c in ("roger","mark","vintage","werner")]==[45,40,45,30]
      and all(plc[c]["end"]=="book" and plc[c]["spoken"] for c in ("roger","mark","werner")) and plc["vintage"]["end"]=="subscribe" and plc["vintage"]["spoken"] is None, "")
c25=plant("roger","In 40 years as a plumber I never saw this.")
check("25b. a plumbing tenure that differs from the channel's fails on Roger's passing script", "FAIL tenure: 40 years; the channel's figure is 45" in c25[1], c25[1][-400:])

# 26. the channel list: the four plumbing channels are ready on plumbing-scripts, and their pages exist (P21: the pages carry no status line)
ch=open(f"{CORE}/channels.md").read()
bad=[name for name,slug in (("Roger the Pipe Guy","roger-the-pipe-guy"),("Mark Silverbridge","mark-silverbridge"),("The Vintage Pipefitter","vintage-pipefitter"),("Werner Finkbeiner","werner-finkbeiner"))
     if not (re.search(rf"^\| \d+ \| {re.escape(name)} \| `plumbing-scripts` \| `personas/{slug}.md` \| ready \|$",ch,re.M) and os.path.isfile(f"{PERS}/{slug}.md"))]
check("26. channels.md lists Roger, Mark, Vintage and Werner as ready on plumbing-scripts, and their pages exist", not bad and os.path.isfile(f"{PL}/SKILL.md"), ", ".join(bad))

# 27. (iter-01's check 14) the numbers check finishes on spoken fractions and lumber names (it used to loop forever on them)
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("Drill a three-quarter inch hole. Use five-eighths inch screws on a one-by-eight, seventeen and three-quarters across.\n"); fs=t.name
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("17.75 0.75 0.625\n"); fp=t.name
try:
    r=subprocess.run(["python3",SCAN,fs,"--pack",fp],capture_output=True,text=True,timeout=20); ok14,d14=r.returncode==0,r.stdout[-400:]
except subprocess.TimeoutExpired:
    ok14,d14=False,"scanner did not finish within 20 seconds"
check("27. numbers check finishes on fraction words (three-quarter, five-eighths, one-by-eight)", ok14, d14)

# 28. every P21 check.py bans "e-book" (the offer is always called "book"; P21: retargeted from the profiles' scanner blocks)
noflag=[ch_ for ch_ in ("scarlett","roger","werner","roger-hvac","hank","dale") if "e-book" not in plant(ch_,"Grab my e-book from the link.")[1].lower()]
check("28. every P21 pack's check.py fails 'e-book' (style, plumbing, HVAC, woodworking)", not noflag, f"not flagging: {noflag}")

# ---- fixes from the post-merge audit (2026-10-21) ----
# 29. tenure: ordinary ages of pipes and heaters are not the persona's years; the persona's own still are
code,out=run_scan("That water heater has been running for 10 years. A pipe that has been in your walls for 50 years is fine.\n",[PLR,ROGER])
code2,out2=run_scan("I've been at this for 40 years.\n",[PLR,ROGER])
missed=[l for l in ("After working on old houses for thirty years, you learn.","Plumbing for 30 years teaches you this.","Been at it for thirty years.",
                    "It's been the same since I've been plumbing for 50 years.","My hands have been in pipes for 30 years.") if run_scan(l+"\n",[PLR,ROGER])[0]!=1]
check("29. tenure check ignores pipe and heater ages; the persona's own wrong figure still fails, in every form",
      code==0 and "PERSONA FACT" not in out and code2==1 and "PERSONA FACT: tenure" in out2 and not missed, out+out2+str(missed))

# 30. spoken prices are read correctly by the numbers check
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("drain call 150 dollars; flapper 5 to 15\n"); bp=t.name
code,out=run_scan("A drain call starts around a hundred and fifty dollars. A flapper is five to fifteen. That one can save you a two-hundred-dollar call. Keep a hundred-dollar bill and a ten-dollar part.\n",[PLR],bp)
miss=out.split("NUMBERS NOT FOUND")[1] if "NUMBERS NOT FOUND" in out else ""
check("30. numbers check reads 'a hundred and fifty' as 150, 'two-hundred-dollar' as 200, 'a hundred-dollar' as 100, 'ten-dollar' as 10",
      "200" in miss and "100" in miss and "  10  " in miss and " 50 " not in miss and "150" not in miss, out)

# 31. "at the very end" in a build order is not a tease; the teases still are
code,out=run_scan("We'll put the felt pads on at the very end, once the oil is dry.\n")
code2,out2=run_scan("I'll save the best one for you at the very end.\n")
okb=[l for l in ("We'll add the felt pads at the very end.","We'll give it one last coat at the very end.") if run_scan(l+"\n")[0]!=0]
tz=[l for l in ("I'm saving the best for the very end.","I've saved the best one for the very end.","At the very end, I'll add it all up.") if run_scan(l+"\n")[0]!=1]
check("31. build-order 'at the very end' lines pass; 'saving the best for the very end' teases are hard bans",
      code==0 and code2==1 and "tease: at the very end" in out2 and not okb and not tz, out+out2+str(okb)+str(tz))

# 32. runtime: the profile's words per minute and the niche pack's minimum
code,out=run_scan("Cut the board.\n",[WWR,f"{OPERS}/hank-hardwood.md"])
code2,out2=run_scan("Rinse the trap.\n",[PLR,ROGER])
check("32. runtime uses the profile's words per minute (Hank 185, Roger 170) and the pack's minimum (plumbing 12, woodworking 8)",
      "at 185 words a minute; minimum 8" in out and "at 170 words a minute; minimum 12" in out2, out[:300]+out2[:300])

# 33. a title's years of selling unlock that figure (Dale's title format)
code,out=run_scan("I've spent forty years at the bench.\n",[WWR,f"{OPERS}/dale-oakfield.md"],title="In 40 Years of Selling, Nothing Beats This Build")
check("33. 'In 40 Years of Selling' in the title allows forty years in the script", code==0 and "PERSONA FACT" not in out, out)

# 34. retired 2026-11-06, P21: the copy guard no longer runs against the profiles (check.py guards the model transcripts only;
#     each page's required wording is checked by check.py itself)

# 35. plumbing (P21: retargeted to check.py): 'today we're going to' fails; Mark's 'here is the part nobody tells you' is banned;
#     'Let's' and 'Where's' are contractions for Mark
c35a=plant("roger","Today we're going to fix the drain.")
c35b=plant("mark","Here is the part nobody tells you.")
c35c=plant("mark","Let us look. Let's look. Where's the valve?")
check("35. plumbing check.py: 'today we're going to' fails; Mark's 'here is the part nobody tells you' fails; 'Let's' and 'Where's' caught",
      "'today we're going to'" in c35a[1] and "a stock line ('here is the part people skip')" in c35b[1] and "'Let's'" in c35c[1] and "'Where's'" in c35c[1], c35a[1][-300:]+c35b[1][-300:]+c35c[1][-300:])

# 36. the plumbing price guide (P21: the new pack's copy, byte-identical to the archived one, check 96): every row rounded and marked;
#     the pack points to it, and check.py reads it by default
PG=f"{PL}/references/price-guide.md"
rows=[l for l in open(PG).read().splitlines() if l.startswith("| ") and not l.startswith("| Item") and not l.startswith("| Fact") and not set(l) <= set("|- ")] if os.path.isfile(PG) else []
cents=[l for l in rows if re.search(r"\$\d[\d,]*\.\d", l)]
nocheck=[l for l in rows if l.rstrip(" |").split("|")[-1].strip() not in ("confirmed","adjusted","thin","in words")]
check("36. price guide: 100+ rows, none in cents, each marked confirmed / adjusted / thin / in words; the plumbing pack and its check.py use it",
      len(rows)>=100 and not cents and not nocheck and "references/price-guide.md" in open(f"{PL}/SKILL.md").read()
      and '"references", "price-guide.md"' in open(f"{PL}/check.py").read(), f"rows={len(rows)} cents={cents[:3]} nocheck={nocheck[:3]}")

# 37. retired 2026-11-06, P21: the emotion section's rates, the item shape, the CTA template's word counts and the number cap
#     were dropped (counts and templates; drafts/p21-plumbing/README.md, "Dropped")

# 38. 'absolutely criminal' (P21: retargeted to check.py): once passes, twice fails
c38=plant("roger","That is absolutely criminal, for a pipe in the ground. And that is absolutely criminal too.")
c38b=plant("roger","That is absolutely criminal, for a pipe in the ground.")
check("38. 'absolutely criminal' passes once on Roger's script and fails when said twice",
      c38b[0]==0 and "FAIL said twice: 'absolutely criminal', said 2 times" in c38[1], c38b[1][-300:]+c38[1][-300:])

# 39. core: straight quotes, and the scanner line comes from a real run on the delivered text (or says "checked by hand")
wf=open(f"{CORE}/workflow.md").read(); ga=open(f"{CORE}/greenlight-audit.md").read()
check("39. core: straight quotes before the final scan; the Scanner evidence line is a real run on the delivered text or 'checked by hand'",
      "**Straight quotes and apostrophes only**" in wf and "Run it last, with `--final`, on the exact text that will be delivered" in wf
      and "Scanner: [run on the delivered text | checked by hand]" in ga and "never reports a count it didn't measure" in ga)

# ---- Sawdust Sam relaunch (2026-10-23) ----
# 40. the woodworking pack keeps the heritage rules (P8, P9) in plain words (P21: retargeted to the new SKILL.md); the template keeps
#     its HERITAGE block; the core's research rules point to the exception
wk=open(f"{WW}/SKILL.md").read(); tp=open(f"{WW}/references/research-pack-template.md").read(); rs=open(f"{CORE}/research-and-sourcing.md").read()
need=["**A heritage title**","never as an opening","never a replica","the old tool or method follows as an option","History stays general and hedged",
      "never a date, a named person or a figure unless the brief or pack gives it with its source","no lead pigments","the heritage angle is opinion only"]
miss=[n for n in need if n not in wk]
check("40. woodworking pack: heritage builds (style not replica, the old way as an option, hedged history P8, proof P9, safe old finishes); template HERITAGE block; core points to the exception",
      not miss and "HERITAGE                           [heritage builds only" in tp and "the assumption, if none found" in tp and "P8, operator 2026-10-23" in rs, f"missing {miss}")

# 41. retired 2026-11-06, P21: Sawdust Sam is dropped (operator 2026-11-06, "sawdust sam is dropped"); his profile and book are archived
# 42. retired 2026-11-06, P21: the same (Sam's scanner lines)

# 43. Sam's ideation: the simple-build filter, single builds, the operator's title formats and the longer brief, wired into the pipeline
so=f"{ROOT}/ideation/woodworking-ideation/references/sam-old-world.md"
sot=open(so).read() if os.path.isfile(so) else ""
need=["## 1. Simple builds only","**Single builds to begin with**","`Simple build?`","But They Never Sell Them","You Can Sell It for $[high]",
      "about 800 to 1,200 words","6b. **History facts:**","6c. **Old tools and methods:**","11. **The book match:**","2b. **The build in outline:**"]
check("43. Sam's ideation file: simple builds, single builds, title formats, longer briefs; the pipeline and SKILL.md point to it",
      not [n for n in need if n not in sot] and "sam-old-world.md" in open(f"{ROOT}/ideation/woodworking-ideation/references/pipeline.md").read()
      and "sam-old-world.md" in open(f"{ROOT}/ideation/woodworking-ideation/SKILL.md").read(), str([n for n in need if n not in sot]))

# 44. written for the voice (operator, 2026-10-25): the forms the voice misread fail; the spoken forms pass;
#     the library's own narration examples carry no "2x4"
bad=["a single 2x12 and a 2x4.","Then one 2x4, 8 ft, about $4.","Grab two 2x4x8 boards.","Use 3-in screws.","An 11in board.",
     "a 3/8 dowel.","at 19% moisture.","thousands of psi.","the stamp that says KD19.","Haha, the scrap pile pays its rent.",
     "It runs $4.00 a box.","about $1.4M.","No. 2 grade.","Wood & glue.","about 6\" of tape.","Then 1 2 4 8 feet."]
fails=[l for l in bad if run_scan(l+"\n",[WWR])[0]!=1]
good=["a single two by twelve and a two by four.","Then one eight-foot two by four, about $4.","a three-eighths inch dowel.",
      "at 19 percent moisture, set to 120 degrees.","In 2026, 15 people paid $4 to $10.","about $1.4 million.","It took 3 in a row.",
      "the stamp that says K D 19."]
passes=[l for l in good if run_scan(l+"\n",[WWR])[0]!=0]
judged=run_scan("It is called an AAV, under their lead limit.\n",[WWR])[1]
ex=open(f"{CORE}/retention-mechanics.md").read()+open(WWR).read()
wf=open(f"{CORE}/workflow.md").read()
check("44. written for the voice: 2x4, 8 ft, 3/8, 19%, psi, KD19, haha, $4.00, symbols fail; spoken forms pass; AAV and lead judged; no 2x4 in narration examples",
      not fails and not passes and "letters 'AAV'" in judged and "'lead' can be said two ways" in judged
      and "one 2x4" not in ex and "**Write every word the way the voice should say it**" in wf,
      f"not failing: {fails}; not passing: {passes}")

# 45. no promise block in the plumbing hook (P10, operator 2026-10-25; P21: retargeted to check.py): a line in the opening that says
#     what a later item holds fails; the count line naming no single item passes
c45=plant("roger","Number four is the two-dollar tool that pulls the hair out in one go.",1)
c45b=plant("roger","Three levels, smallest first.",1)
check("45. plumbing hook: a run-down of a later item in the opening fails check.py (P10); a plain count line passes",
      "FAIL opening: a run-down of what a later item holds" in c45[1] and c45b[0]==0, c45[1][-400:]+c45b[1][-300:])

# ---- the electrical pack and Frederick Barnes (2026-10-27) ----
EL=f"{ROOT}/electrical-scripts"; ELR=f"{EL}/SKILL.md"; FRED=f"{PERS}/frederick-barnes.md"
EL_REFS=[ELR, f"{EL}/references/excerpts.md", f"{EL}/references/voice-samples.md"]+sorted(glob.glob(f"{EL}/references/models/*.md"))
EL_REFS=[f for f in EL_REFS if os.path.isfile(f)]

# 46. electrical inputs block: title, brief and rotation log required, the research pack not used
ek=open(ELR).read()
inp=re.search(r"```inputs\n(.*?)```",ek,re.S)
rows=[[c.strip() for c in l.strip()[1:].split("|")] for l in inp.group(1).splitlines() if l.strip().startswith("-")] if inp else []
check("46. electrical inputs block: 4 well-formed inputs, research pack not used",
      len(rows)==4 and all(len(r)==3 for r in rows) and {r[0]:r[1] for r in rows}==want, str(rows))

# 47. the electrical scanner block: every ban fires, a once-phrase twice fails, P11 lifts only "by the end of this video",
#     and a clean electrical paragraph passes with Frederick's profile
clean_el=textwrap.dedent("""\
That outlet in the hallway that quit on you last night probably isn't broken at all.

Does the bathroom outlet have two little buttons on it? Press reset on that one first. That's a GFCI, a safety outlet that cuts the power in a blink, and it often covers other outlets in the house.

By the end of this video you'll be able to find the cause yourself, and you'll know exactly when it's a job for a licensed electrician instead.

Step one. Turn the breaker off, then prove the outlet is dead with a tester you've checked on a working outlet first. I'd never skip that part.

Most folks figure the panel is the first place to look. But a tripped GFCI two rooms away is the usual reason, and it takes ten seconds to check.

So turn the breaker back on, press reset, and plug a lamp in. If it lights, you're done.

Down in the comments, tell me which breaker in your panel trips the most. I read every one.
""")
planted={"first-person test claim":"I tested all three connectors side by side.","first-person demonstration":"Now watch me pull the outlet out.",
         "pointing at the screen":"As you can see, the wire is loose.","job or customer story":"I once found a melted box in a basement.",
         "trade as villain":"Electricians hate this simple trick.","money (no money framing on this channel)":"A new outlet runs about $5.",
         "CTA \"no rush\" family":"No rush, take your time with it.",
         "unit written as a symbol (write the word: 'fifteen amps')":"Use a 15 A breaker here.",
         "wire gauge written as a code (write 'fourteen-gauge')":"Run 14 AWG copper.",
         "cable name with a slash (write 'twelve-two cable')":"Pull a run of 12/2 through the wall.",
         "code section read as a number (say 'the electrical code')":"NEC 406.4 says so."}
code,out=run_scan(clean_el,[ELR,FRED])
bad=[]
for label,line in planted.items():
    c,o=run_scan(f"Check the outlet.\n\n{line}\n",[ELR])
    if c!=1 or f"NICHE/PERSONA BAN: {label}]" not in o: bad.append(label)
code2,out2=run_scan("Between you and me, it is the GFCI.\n\nAnd between you and me, the breaker is fine.\n",[ELR])
code3,out3=run_scan("Stick around, because the last one matters.\n",[ELR])
check("47. electrical scanner block: each ban fires; a once-phrase twice fails; P11 lifts only 'by the end of this video'; a clean electrical paragraph passes",
      code==0 and "FIX ON SIGHT (0)" in out and not bad and code2==1 and "NICHE/PERSONA LIMIT: between you and me] used 2 times" in out2
      and code3==1 and "tease: stick around" in out3, f"missed: {bad} | "+out[:600])

# 48. electrical units written for the voice: symbols fail, spoken forms pass
bad_u=["It runs on 120V.","a 20 A circuit.","about 1,500 W.","as little as 5mA.","at 60Hz.","a 10kW generator."]
good_u=["It runs on a hundred and twenty volts.","a twenty-amp circuit.","fifteen hundred watts.","fourteen-gauge wire and twelve-two cable."]
fails=[l for l in bad_u if run_scan(l+"\n",[ELR])[0]!=1]
passes=[l for l in good_u if run_scan(l+"\n",[ELR])[0]!=0]
check("48. electrical units: 120V, 20 A, 1,500 W, 5mA, 60Hz and 10kW fail; the spoken forms pass", not fails and not passes,
      f"not failing: {fails}; not passing: {passes}")

# 49. copy guard over the electrical references: the clean paragraph passes against all of them; a line lifted from each is caught
runs=sc.read_refs(EL_REFS)
lifted=[]; nolift=[]
for f in EL_REFS:
    name=os.path.basename(f); got=None
    for para in open(f).read().split("\n\n"):
        toks=sc.copy_tokens(para)
        for i in range(len(toks)-12):
            if all(runs.get(tuple(toks[j:j+sc.COPY_RUN]))==name for j in range(i,i+5)):
                got=" ".join(toks[i:i+12]); break
        if got: break
    (lifted.append((name,got)) if got else nolift.append(name))
code,out=run_scan("\n\n".join(g.capitalize()+"." for _,g in lifted)+"\n",[ELR],refs=EL_REFS)
uncaught=[n for n,_ in lifted if f"COPIED FROM REFERENCE: {n}]" not in out]
code2,out2=run_scan(clean_el,[ELR,FRED],refs=EL_REFS+[FRED])
EL_MODELS=sorted(os.path.basename(f).split("-")[0] for f in glob.glob(f"{EL}/references/models/E*.md"))
EL_KEPT=[f"E{n:02d}" for n in (1,2,3,4,5,7,9,10,11,13,14,15,16,18,19,21,22)+tuple(range(24,38))]
EL_GONE=("E08","E12","E17","E20","E23","E38")  # removed 2026-10-27 (operator): kept in studies/electrical/models-removed-2026-10-27/
check("49. copy guard: the clean electrical paragraph passes against the pack's SKILL.md, excerpts, voice samples and all 31 model files (E01-E37 less E06, E08, E12, E17, E20, E23; none of the six removed 2026-10-27 in references/models/); a line from each is caught",
      EL_MODELS==EL_KEPT and not any(g in EL_MODELS for g in EL_GONE)
      and all(glob.glob(f"{ROOT}/studies/electrical/models-removed-2026-10-27/{g}-*.md") for g in EL_GONE)
      and len(EL_REFS)==35 and not nolift and not uncaught and code==1 and code2==0 and "COPIED" not in out2,
      f"models={EL_MODELS}; refs={len(EL_REFS)} no line found in {nolift}; not caught {uncaught}; "+out2[:400])

# 50. Frederick's profile: Talking Head, 162 wpm (195 until 2026-10-29), no book (NO BOOK marker), subscribe only, name and tenure 35;
#     a different tenure, a name intro and the firefighter framing fail
fp=open(FRED).read(); ff=facts_of(FRED)
code,out=run_scan("I have been at this for 25 years.\n",[ELR,FRED])
code2,out2=run_scan("I have been at this for 35 years.\n",[ELR,FRED])
code3,out3=run_scan("I'm Frederick Barnes, and as a retired firefighter I know this.\n",[ELR,FRED])
check("50. Frederick's profile: Talking Head, 162 wpm, subscribe only (NO BOOK), name and tenure 35; 25 years, a name intro and the firefighter framing fail",
      "Script type: Talking Head" in fp and "Words per minute (for runtime and the length minimum): 162" in fp and "Type: subscribe only" in fp
      and "NO BOOK" in fp and "Mid-video CTA: no" in fp and "name: Frederick Barnes" in ff and "tenure: 35" in ff and not any(l.startswith("book:") for l in ff)
      and code==1 and "PERSONA FACT: tenure" in out and code2==0 and code3==1 and "name intro" in out3 and "firefighter" in out3, out+out2+out3)

# 51. the electrical pack's decisions are in place: no money, stakes, P11 in the opening, safety never removed,
#     the comment ending, the 12-minute minimum, the seven video types
check("51. electrical pack: no money, the stakes section, P11 opening promise, safety the brief can't remove, comment ending, 12 minutes, seven types",
      "## The stakes (no money)" in ek and "5. **One value promise, when it fits** (P11" in ek and "**The brief can add safety but never remove it**" in ek
      and "min-minutes: 12" in ek and "allow: I read every comment" in ek and "lift: tease: by the end of this video" in ek
      and all(t in ek for t in ("**How-to / correct way**","**Fix this problem**","**Explainer**","**X vs Y**","**Mistakes list**","**Single big mistake**","**Know-this list**"))
      and not re.search(r"\$\d", ek.split("```scanner")[0]), "")

# 52. electrical voice (review R4, 2026-10-27): the brief's short forms fail; the spoken forms and years before a capital "A" pass;
#     the P11 promise passes the copy guard and fails on a second use; Frederick's old sign-off fails; his old tics fail on the second use.
#     (The tenure-in-words and number-check parts are checks 53 and 54, since P13 was approved.)
bad_v=["Run 12-2 cable to the outlet.","A regular outlet is a NEMA 5-15.","It lasts 15-20 years.","Your panel is a 120/240 panel.",
       "The heater pulls 1500w on high.","Most outlets run at 120v.","Use 14 awg copper.","Plug in the CO alarm.","Box fill is 2.25 cu in. per wire.",
       "A new outlet runs about twenty dollars.","Your electric bill goes up.","Hey there, folks.","It's just 120 volts.","Ask me how I know."]
good_v=["It was built in 2014. A lot of houses were.","The code changed in 2017. VA ratings came later.","Run twelve-two cable to the outlet.",
        "A regular outlet is what the trade calls a five-fifteen.","Your panel is a one-twenty, two-forty panel.","A thirty-amp double-pole breaker feeds the dryer.",
        "A three-way switch runs the stairs.","Leave at least six inches of wire and strip three-quarters of an inch.","Plug in the carbon monoxide alarm."]
f_v=[l for l in bad_v if run_scan(f"Check the outlet.\n\n{l}\n",[ELR,FRED])[0]!=1]
p_v=[l for l in good_v if run_scan(l+"\n",[ELR,FRED])[0]!=0]
p11=run_scan("By the end of this video you'll know where the hidden reset sits and when it's a call for an electrician.\n",[ELR,FRED],refs=EL_REFS+[FRED])
p11x2=run_scan("By the end of this video you'll know one thing.\n\nBy the end of this video you'll know another.\n",[ELR,FRED])
shift=run_scan("Tell me which outlet gives you grief. I read every one, and I'll see you next shift.\n",[ELR,FRED])
tics=run_scan("Rest your palm on the plate tonight.\n\nThen rest your palm on the switch tonight.\n",[ELR,FRED])
stories=[l for l in ["I've watched a neighbor run a generator cord through a kitchen window.","A homeowner once asked me why the plug kept falling out.",
         "That's the worst panel I've ever opened.","These are the seven I find in almost every older house.","We tested all three connectors.",
         "I put a meter on it and it read zero."] if run_scan(l+"\n",[ELR,FRED])[0]!=1]
check("52. electrical voice and claims: short forms fail, spoken forms and years pass; P11 passes the guard and is once-only; old sign-off, tics, job stories and test claims fail",
      not f_v and not p_v and p11[0]==0 and p11x2[0]==1 and shift[0]==1 and "next shift" in shift[1]
      and "the palm check" in tics[1] and "tonight" in tics[1] and not stories,
      f"bad passing: {f_v}; good failing: {p_v}; p11: {p11[1][-300:] if p11[0] else ''}; stories passing: {stories}")
# ---- the HVAC pack and Roger the HVAC Guy (2026-10-27; numbered 60+ to stay clear of the other branches' checks) ----
# P21: HVR and ROGER_HVAC are the archived pack and profile, read-only fixtures for the core scanner checks (63, 64, 71, 72);
# the new pack is tested through hvac-scripts/check.py on the saved iter-17 script.
HVR=f"{OHV}/SKILL.md"; ROGER_HVAC=f"{OPERS}/roger-the-hvac-guy.md"; ROGER_PIPE=f"{PERS}/roger-the-pipe-guy.md"
NHVR=f"{HV}/SKILL.md"; NROGER_HVAC=f"{PERS}/roger-the-hvac-guy.md"

# 60. every file reference in the new HVAC pack and Roger the HVAC Guy's page resolves (P21: retargeted to the new files)
HV_PLACEHOLDER={"CONCLUSIONS.md","niche-research/studies/hvac/CONCLUSIONS.md"}  # these live in the niche-research repository
hv_files=[f for f in glob.glob(f"{HV}/**/*.md",recursive=True)]+[NROGER_HVAC]
missing=[]
for f in hv_files:
    for ref in re.findall(r"`([^`\s]+?\.(?:md|py)|[a-z-]+/)`", open(f).read()):
        if ref in HV_PLACEHOLDER: continue
        ok = any(os.path.isdir(os.path.join(b,ref)) for b in (ROOT,HV,PERS,os.path.dirname(f))) if ref.endswith("/") else (os.path.basename(ref) in repo_names or ref in repo_rels or os.path.isfile(os.path.join(HV,ref)))
        if not ok: missing.append(f"{os.path.relpath(f,ROOT)} -> {ref}")
check("60. every file reference in the HVAC pack and Roger the HVAC Guy's page resolves", not missing, "; ".join(sorted(set(missing))))

# 61. retired 2026-11-06, P21: the HVAC pack has no inputs block (title and brief in words; the rotation log is dropped)

# 62. the HVAC bans (P21: retargeted from the scanner block to check.py): each planted line fails on the passing iter-17 script
bad62=["Today we're going to fix your furnace.","I tested all four filters.","Set it to 24 V.","That runs $75-$200.","Your heating/cooling needs air.",
       "Old R-22 units are rare.","Get a CO alarm.","Keep your cool out there.","None of this is hidden because it's hard.",
       "If this saved you a call, subscribe.","Same companies, same story.","Stay tuned for the last one."]
p62=[l for l in bad62 if "FAIL banned" not in plant("roger-hvac",l)[1]]
check("62. HVAC check.py: every planted ban fails (units, hyphen ranges, slashes, refrigerant codes, CO, stock lines, the faceless leader's catchphrases); the saved script passes",
      passing("roger-hvac")[0]==0 and not p62, f"not failing: {p62}")

# 63. tenure in HVAC words: a wrong figure fails in every form; equipment ages and other people's years pass; title numbers win
wrong=["After forty years in HVAC, I can tell you this.","I spent 40 years as an HVAC tech.","Take it from a 40-year HVAC man.",
       "I've been doing this 40 years.","In my 40 years in heating and cooling, I've seen it all.","I've been working on furnaces for 40 years."]
fine=["That old compressor kept working for 20 years.","My furnace has been running for 20 years.","Techs with 20 years of experience told me the same thing.",
      "Most furnaces last 15 to 20 years.","A 20-year-old furnace can still run fine.","A 10-year parts warranty is normal.","I've been doing this 45 years."]
miss=[l for l in wrong if "PERSONA FACT: tenure" not in run_scan(l+"\n",[HVR,ROGER_HVAC])[1]]
false=[l for l in fine if "PERSONA FACT: tenure" in run_scan(l+"\n",[HVR,ROGER_HVAC])[1]]
tt=run_scan("After 50 years in HVAC, here's my warning.\n",[HVR,ROGER_HVAC],title="Don't Replace Your Furnace Yet: A 50-Year HVAC Tech's Warning")[1]
pipe=run_scan("That old water heater kept working for 20 years.\n",[PLR,ROGER])[1]
check("63. tenure in HVAC words: wrong figures fail; equipment ages and other people's years pass; an HVAC title's years win; plumbing's heater age passes too",
      not miss and not false and "PERSONA FACT: tenure" not in tt and "PERSONA FACT: tenure" not in pipe, f"missed: {miss}; false: {false}")

# 64. letter words the HVAC pack says every day aren't judged one by one (letters-ok); without the pack they still are
withp=run_scan("Check the HVAC filter, the MERV rating and the AC coil.\n",[HVR,ROGER_HVAC])[1]
without=run_scan("Check the HVAC filter, the MERV rating and the AC coil.\n",[ROGER_HVAC])[1]
check("64. letters-ok: HVAC, MERV and AC aren't judge lines with the HVAC pack, and still are without it",
      "letters 'HVAC'" not in withp and "letters 'MERV'" not in withp and "letters 'HVAC'" in without, withp[-400:])

# 64. letter words the HVAC pack says every day aren't judged one by one (letters-ok) — a core scanner check on the archived fixture
withp=run_scan("Check the HVAC filter, the MERV rating and the AC coil.\n",[HVR,ROGER_HVAC])[1]
without=run_scan("Check the HVAC filter, the MERV rating and the AC coil.\n",[ROGER_HVAC])[1]
check("64. letters-ok: HVAC, MERV and AC aren't judge lines with the HVAC pack fixture, and still are without it",
      "letters 'HVAC'" not in withp and "letters 'MERV'" not in withp and "letters 'HVAC'" in without, withp[-400:])

# 65. the two Roger channels never mention each other (operator, 2026-10-27; P21: retargeted to the two check.py files)
a1=plant("roger-hvac","Over on the Pipe Guy channel I cover drains.")[1]
a2=plant("roger-hvac","Grab One Hundred Old-House Fixes from the link.")[1]
a3=plant("roger","My friend Roger the HVAC Guy covers furnaces.")[1]
check("65. the two Rogers: each check.py fails the other channel's name (and the HVAC one the plumbing book)",
      "the other Roger channel" in a1 and "a book (this channel has none)" in a2 and "the other Roger channel" in a3, a1[-300:]+a2[-300:]+a3[-300:])

# 66. HVAC models are real people on camera (operator, 2026-10-27; P21: retargeted to the eight new model files): no S files;
#     each says it's a real person on camera; a run lifted from each model fails check.py
HVM=sorted(glob.glob(f"{HV}/references/models/*.md"))
sfiles=[os.path.basename(m) for m in HVM if os.path.basename(m).startswith("S")]
untagged=[os.path.basename(m) for m in HVM if "A real person on camera" not in open(m).read()]
miss66=[]
for m in HVM:
    tr=re.findall(r"[\w']+",open(m).read().split("## Transcript",1)[1])
    lift=" ".join(tr[60:72])
    if f"from {os.path.basename(m)}" not in plant("roger-hvac",lift[0].upper()+lift[1:]+".")[1]: miss66.append(os.path.basename(m))
check("66. HVAC models: eight, real people on camera only (no S files); a run lifted from each fails check.py",
      len(HVM)==8 and not sfiles and not untagged and not miss66, f"models={len(HVM)} S={sfiles} untagged={untagged} not caught={miss66}")

# 67. wiring (P21: retargeted): channel row 8 ready on hvac-scripts; the build ships hvac-scripts and his persona skill
ch=open(f"{CORE}/channels.md").read(); bs=open(f"{ROOT}/tools/build_skills.py").read()
check("67. Roger the HVAC Guy: channel row 8 ready on hvac-scripts; his page exists; the builder ships hvac-scripts and his persona skill",
      "| 8 | Roger the HVAC Guy | `hvac-scripts` | `personas/roger-the-hvac-guy.md` | ready |" in ch and os.path.isfile(NROGER_HVAC)
      and '"hvac-scripts": (),' in bs and '"roger-the-hvac-guy":' in bs and '"roger-the-hvac-guy-persona": "p21-hvac"' in bs, "")

# 68. the HVAC price guide: every row rounded (no cents) and check-marked; the gas-leak and carbon monoxide rows carry every step;
#     the stale brief figures are warned off; the pack points to it and the builder ships it with the HVAC scanner command
HPG=f"{HV}/references/price-guide.md"
hpg=open(HPG).read() if os.path.isfile(HPG) else ""
hrows=[l for l in hpg.splitlines() if l.startswith("| ") and not l.startswith(("| Item","| Fact")) and not set(l) <= set("|- ")]
hcents=[l for l in hrows if re.search(r"\$\d[\d,]*\.\d", l)]
hnocheck=[l for l in hrows if l.rstrip(" |").split("|")[-1].strip() not in ("confirmed","adjusted","thin","in words")]
gas=next((l for l in hrows if l.startswith("| A gas leak |")),"")
co=next((l for l in hrows if l.startswith("| A carbon monoxide alarm sounds |")),"")
gas_need=["get everyone out","light switches","garage door opener","don't light anything","don't start the car","call 911 and the gas company","don't assume someone else","don't go back in","can't smell"]
co_need=["never ignore it","get everyone out","count heads","call 911","stay out until","don't run it again","medical help","four quick beeps"]
hmiss=[n for n in gas_need if n not in gas]+[n for n in co_need if n not in co]
warn=["Never \"9 out of 10\" or \"88%\"","federal tax credits for new heat pumps","\"pure sine\"","Don't quote a whole system at"]
hwarn=[w for w in warn if w not in hpg]
check("68. HVAC price guide: 100+ rows, none in cents, each marked; gas-leak and CO rows carry every step; stale figures warned off; the pack and builder use it",
      len(hrows)>=100 and not hcents and not hnocheck and not hmiss and not hwarn
      and "references/price-guide.md" in open(NHVR).read() and "<hvac-scripts>/references/price-guide.md" in open(f"{ROOT}/tools/build_skills.py").read(),
      f"rows={len(hrows)} cents={hcents[:3]} nocheck={hnocheck[:3]} missing={hmiss} warn={hwarn}")

# ---- P13: the core checker fixes (operator, 2026-10-27: E1 "apply all") ----
# 53. tenure (R4 B1-B2, R5 M14): "thirty-five years in the trade" passes for tenure 35, the same for Mark's "forty-five";
#     a wrong tenure said the electrician way fails; a wiring age doesn't count as tenure
ten_good=[l for l in ["In thirty-five years in the trade, I'd replace that one first.","Thirty five years in the trade taught me one thing.",
                      "After thirty-five years of doing this, I'd replace it."] if run_scan(l+"\n",[ELR,FRED])[0]!=0]
mark_good=run_scan("In forty-five years in the trade, I'd fix that first.\n",[f"{OPERS}/vintage-pipefitter.md"])  # P21: archived fixture
ten_bad=[l for l in ["In 25 years as an electrician, I'd replace it.","I wired houses for 30 years, and I'd replace it.","I'm a 40-year electrician, and I'd replace it.",
                     "After 25 years of electrical work, I'd replace it.","My twenty-five years in the trade say replace it.","I spent forty years as an electrician.",
                     "I spent 25 years as a lineman.","In thirty years of wiring houses, I learned one thing."]
         if "PERSONA FACT: tenure" not in run_scan(l+"\n",[ELR,FRED])[1]]
ten_age=[l for l in ["Wiring that's forty years old isn't bad, and I'd keep it. Old wiring like that held up for 40 years.",
                     "That panel has been in the wall for forty years.","If your house has forty years of wiring in it, check the outlets.",
                     "Your 40-year-old electrical panel deserves a look."] if run_scan(l+"\n",[ELR,FRED])[0]!=0]
check("53. tenure: 'thirty-five years' in words passes (and 'forty-five' for 45); wrong tenures said the electrician way fail; wiring ages pass",
      not ten_good and mark_good[0]==0 and not ten_bad and not ten_age, f"good failing: {ten_good}; 45: {mark_good[1][-200:] if mark_good[0] else ''}; bad passing: {ten_bad}; ages failing: {ten_age}")

# 54. numbers in words (R4 M2): "a forty-amp breaker on eight-gauge wire" is number-checked; "twelve-two" is two numbers
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("Copper 14 AWG is protected at 15 A, 12 AWG at 20 A.\n"); brief54=t.name
num=run_scan("A forty-amp breaker on eight-gauge wire feeds the dryer.\n",[ELR,FRED],pack=brief54)
num_ok=run_scan("A fifteen-amp breaker on fourteen-gauge wire, a twenty-amp breaker on twelve-gauge.\n",[ELR,FRED],pack=brief54)
spec54=importlib.util.spec_from_file_location("scan54", SCAN); sc54=importlib.util.module_from_spec(spec54); spec54.loader.exec_module(sc54)
wn=[sc54.word_numbers(x) for x in ("twelve-two cable","thirty-five years","a hundred and twenty volts","fifteen hundred watts","one-twenty, two-forty")]
check("54. number words: amp, volt, watt and gauge forms are checked against the fact source; 'twelve-two' is 12 and 2, 'thirty-five' is 35",
      "NUMBERS NOT FOUND IN THE FACT SOURCE (2)" in num[1] and "NUMBERS NOT FOUND IN THE FACT SOURCE (0)" in num_ok[1]
      and wn==[[12,2],[35],[120],[1500],[1,20,2,40]], f"{num[1][-200:]} | {num_ok[1][-200:]} | {wn}")

# 55. letter sets and two-way words judged once with a count (R4 M5, M6); "3-in-1" is no unit (m7); voice tags in the script fail (R6 M12);
#     a sentence over 35 words fails; --final fails a short script (R7 F8)
lt=run_scan("Press the test button on the GFCI. A GFCI trips fast. Every GFCI has a reset. The fixture stays live.\n")
inone=run_scan("The 3-in-1 tester is handy.\n")
tag=run_scan("[chuckles] Check the outlet. [short pause] Then the breaker.\n")
tag_vo=run_scan("Check the outlet.\n\nVO COPY\n[thoughtful] Check the outlet.\n")
long_s=run_scan("Check the outlet "+"and then the breaker "*9+"before you call.\n")
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("Check the outlet before you call anyone.\n"); short_s=t.name
fin=subprocess.run([sys.executable,SCAN,short_s,"--rules",ELR,FRED,"--final"],capture_output=True,text=True)
nofin=subprocess.run([sys.executable,SCAN,short_s,"--rules",ELR,FRED],capture_output=True,text=True)
check("55. letters 'GFCI' judged once (x3); 'live' judged; '3-in-1' passes; voice tags in the script fail, in the VO copy pass; a 36-word sentence fails; --final fails a short script",
      lt[1].count("letters 'GFCI'")==1 and "(x3 in the script)" in lt[1] and "'live' can be said two ways" in lt[1] and inone[0]==0
      and tag[0]==1 and "voice tag in the script" in tag[1] and tag_vo[0]==0 and long_s[0]==1 and "SENTENCE OVER 35 WORDS" in long_s[1]
      and fin.returncode==1 and "[LENGTH]" in fin.stdout and nofin.returncode==0, lt[1][-400:]+inone[1][-200:]+tag[1][-200:]+tag_vo[1][-200:]+long_s[1][-200:]+fin.stdout[-200:])

# 56. the ITEMS / SENTENCES report (R7 F11, T6) and tools/verify_output.py (R7 F7, T5) on plumbing run 03 (history is read, never written)
R03=f"{ROOT}/tests/iterations/iter-04/test-run-03"
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("```scanner\nitem-words: 100-130\nfirst-item-seconds: 30\n```\n"); band=t.name
rep=subprocess.run([sys.executable,SCAN,f"{R03}/script.txt","--rules",band],capture_output=True,text=True).stdout
ver=subprocess.run([sys.executable,f"{ROOT}/tools/verify_output.py",f"{R03}/chat-and-output.md","--script",f"{R03}/script.txt",
                    "--rules",f"{OPL}/SKILL.md",f"{OPERS}/roger-the-pipe-guy.md"],capture_output=True,text=True)  # P21: archived fixtures
check("56. scanner ITEMS/SENTENCES report and verify_output.py: run 03 shows item one at word 139, 0 of 15 in band, longest sentence 45, 'MECHANICAL CLAIMED 0' against 122 curly quotes",
      "item one at word 139" in rep and "in band 100-130: 0 of 15" in rep and "longest 45" in rep and "<< later than 30 seconds" in rep
      and ver.returncode==1 and "MECHANICAL CLAIMED 0, the script has 122 curly quotes" in ver.stdout, rep[:600]+ver.stdout[-600:])

# 57. the P13 text: offer rules §5 scoped to offers; the electrical pack allows Federal Pacific's independent test results with the source,
#     has the numbers-in-words override row and first-item-seconds; core audit carries the quoted evidence lines and --final; check 52's
#     wait note is gone (P12 rejected: H21 unchanged)
orr=open(f"{CORE}/offer-rules.md").read(); ga=open(f"{CORE}/greenlight-audit.md").read(); wf=open(f"{CORE}/workflow.md").read(); ek=open(ELR).read()
check("57. P13 text: offer rules §5 scoped to offers; Federal Pacific test results with the source; numbers-in-words row; audit's quoted evidence lines; --final; 35-word limit",
      "Negative claims about named companies in a CTA, pitch, description or pinned comment" in orr
      and "Federal Pacific's independent test results may be said" in ek and "P13 item 6, operator 2026-10-27" in ek and "first-item-seconds: 45" in ek
      and "Items: [paste the scanner's ITEMS line" in ga and "A quoted line the script doesn't contain fails the audit" in ga and "`--final`" in wf
      and "**No sentence over 35 words**" in wf, "")

# ---- iter-05 run 01 fixes (operator 2026-10-27: "answer the questions yourself") ----
# 58. the electrical pack: the prove-dead order at a device, look before you shop, no ordinal sub-lists, the short-sentence floor,
#     "I" lines with the box open; the example guard catches run 01's two echoes of the old example lines and passes the new pack
#     on run 01; no plug or outlet example lines left in "Emotion"; "lives" judged; ITEMS names items with no short sentence
ek=open(ELR).read()
R01=f"{ROOT}/tests/iterations/iter-05/test-run-01/script.txt"
old_ek=subprocess.run(["git","-C",ROOT,"show","98f92de:electrical-scripts/SKILL.md"],capture_output=True,text=True).stdout
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write(old_ek.replace("first-item-seconds: 30\n","first-item-seconds: 45\nexample-guard: 5\n")); old58=t.name
old_run=subprocess.run([sys.executable,SCAN,R01,"--rules",old58,FRED],capture_output=True,text=True).stdout
new_run=subprocess.run([sys.executable,SCAN,R01,"--rules",ELR,FRED],capture_output=True,text=True).stdout
lv=run_scan("Check the outlet where the hair dryer lives.\n")
emo=ek.split("## Emotion, all the way through")[1].split("## Point then promise")[0]
check("58. run 01 fixes: prove-dead order, look before you shop, no ordinal sub-lists, 12% short sentences, 'I' lines with the box open; the example guard catches run 01's echoes; 'lives' judged",
      "**The order at a device, said in this order**" in ek and "**In any swap, look before you shop**" in ek and "**No \"first, second, third\" inside a numbered step or item**" in ek
      and "at least 12% across the script" in ek and "never while the box is open (Safety" in ek and "example-guard: 5" in ek
      and "\"if you only check one\"" in old_run and "\"now that plug clicks in\"" in old_run and "EXAMPLE LINE REUSED" not in new_run
      and "no sentence of 6 words or fewer: 2, 5" in new_run and not any(x in ek for x in ("plug clicks in","plug sag","plug droop","If you only check one thing","grip like new","wiggle the plug")) and "'lives' can be said two ways" in lv[1],
      old_run[-600:]+new_run[-300:]+lv[1][-200:])

# 59. run 02 fixes N1-N5 (operator 2026-10-27: "answer the questions yourself"): the plug-in tester lit and dark in each half; the two-slot
#     outlet read with power on, then off; the two-probe tester's own live check; any later re-check runs the same order; a two-prong
#     outlet's check after power-back-on; the open-box "I" line after the step's closing test; a fix rung opens on a sense or a scene line
ek=open(ELR).read()
check("59. run 02 fixes: each half lit then dark; two-slot read live then dead; two-probe tester checked live; re-checks repeat the order; two-prong check; rule 9 wording; rungs open on a sense",
      "seen lit in each half before the breaker goes off, then dark in each half after" in ek and "read with the power on first (it shows power)" in ek
      and "The two-probe tester gets its own live check too" in ek and "**Any later re-check**" in ek
      and "If the new device is a two-prong outlet, the check is the two-probe tester across the slots" in ek
      and "after the test that ends the step (the power back on and the tester's lights)" in ek and "as an instruction that points at a sense" in ek, "")

# 69. run 03 fixes N7-N10 (numbered 69 at the merge with the HVAC branch, whose checks are 60-68): the two-slot / won't-seat fallback required in outlet scripts; "open ground" explained (term list, rule 7,
#     facts guide 14.50); the buying step answers its rules and a GFCI's incoming power goes on the line screws; open-box "I" lines on
#     the evidence block
ek=open(ELR).read(); fg=open(f"{ROOT}/electrical-scripts/references/facts-guide.md").read()
check("69. run 03 fixes: two-slot / won't-seat fallback required; 'open ground' explained (terms, rule 7, facts 14.50); buying step and GFCI line screws on the checklist; open-box 'I' lines on the evidence block",
      "what to do when the plug-in tester can't be used" in ek and "open ground (on a plug-in tester: no ground wire connected)" in ek
      and "never the GFCI)" in ek and "| 14.50 | Open ground" in fg and "the incoming power goes on the line screws" in ek and "open-box: none" in ek, "")
# 71. require-if (operator, 2026-10-27: "2 ok yes"): a carbon monoxide alarm or a gas smell brings every step from the
#     price guide; a narrowed step ("the furnace" without "another appliance") fails; the full steps pass
co_full=("If your carbon monoxide alarm goes off, never ignore it. Get everyone outside into fresh air. Count heads. "
         "Call nine-one-one from outside, and stay out until the firefighters say it's safe. The furnace or another appliance "
         "stays off until a trained tech fixes it, and anyone who feels sick gets medical help.\n")
co_narrow=co_full.replace("The furnace or another appliance stays off","The furnace stays off")
gas_full=("If you smell gas, get everyone out now, on foot. Don't flip a light switch, don't use your phone or the garage door opener, "
          "don't light anything, and don't start the car. Once you're well away, call nine-one-one and the gas company, and don't assume "
          "somebody else did. Don't go back in until they say it's safe. Some people can't smell it, and the smell can fade.\n")
gas_short=gas_full.replace(" or the garage door opener","")
c1,o1=run_scan(co_full,[HVR,ROGER_HVAC]); c2,o2=run_scan(co_narrow,[HVR,ROGER_HVAC]); c3,o3=run_scan(gas_full,[HVR,ROGER_HVAC]); c4,o4=run_scan(gas_short,[HVR,ROGER_HVAC])
check("71. HVAC require-if: full carbon monoxide and gas-leak steps pass; a narrowed CO step and a missing gas step fail",
      "REQUIRED" not in o1 and "another appliance" in o2 and "REQUIRED" in o2 and "REQUIRED" not in o3 and "garage door" in o4 and "REQUIRED" in o4,
      (o1+o2+o3+o4)[-900:])

# 72. reframes split across two sentences are counted ("won't show up on a bill. At its worst, it shows up as a fire");
#     an instruction ("Don't touch it. It's fragile.", "...shuts down, don't try to get around it. It's telling you something") is not
c5,o5=run_scan("That mistake won't show up on a repair bill. At its worst, it shows up as a fire.\n",[HVR,ROGER_HVAC])
c6,o6=run_scan("Don't touch the igniter. It's fragile. If it still shuts down, don't try to get around that switch. It's telling you something.\n",[HVR,ROGER_HVAC])
check("72. reframe floor: a same-verb flip across two sentences is caught; instructions starting \"don't\" are not",
      "REFRAME FLOOR (H21): 1" in o5 and "REFRAME FLOOR (H21): 0" in o6, o5[-300:]+o6[-300:])

# 70. Werner (relaunched 2026-10-27; P21: retargeted from his profile's scanner block to plumbing-scripts/check.py and his page):
#     Talking Head with his printed title in the markers, the mentor line word for word, tenure 30, no contractions, 181 words a minute;
#     row 9 ready; the book index; in the build; his passing iter-16 script passes and his banned lines fail on it
wc_=plc["werner"]; wp=open(f"{PERS}/werner-finkbeiner.md").read()
bad_w=["I am Werner Finkbeiner, and this is my channel.","My grandfather showed me this.","When I came to America, the pipes surprised me.",
       "A bottle costs about one euro.","Enough for today.","My father showed me this.","Bertha kept a coffee can by the sink.","My neighbor Marcus tried it.",
       "In 25 years as a plumber I never saw this.","Achtung, this is important.","Three small things for this week, then.","Werner Finkbinder wrote it down."]
w_pass=[l for l in bad_w if plant("werner",l)[0]!=1]
chan=open(f"{CORE}/channels.md").read(); bs=open(f"{ROOT}/tools/build_skills.py").read()
check("70. Werner: check.py's entry (Talking Head, his printed title, the mentor line, tenure 30, no contractions, 181 wpm); row 9 ready; the book index; in the build; his script passes, his banned lines fail",
      wc_["type"]=="talking" and wc_["printed"]=="Werner's 101 Free Repairs" and wc_["fixed"].startswith("My old mentor taught me this trade")
      and wc_["tenure"]==30 and wc_["contractions"] is False and wc_["wpm"]==181 and "Werner Finkbeiner" in wp
      and "| 9 | Werner Finkbeiner | `plumbing-scripts` | `personas/werner-finkbeiner.md` | ready |" in chan
      and '"werner-finkbeiner": ("Werner Finkbeiner", "personas/werner-finkbeiner.md"' in bs
      and os.path.exists(f"{PERS}/books/werner-finkbeiner-book.md") and "| 54 | Silence a Running Toilet by Replacing the Flapper | 7 | 277 |" in open(f"{PERS}/books/werner-finkbeiner-book.md").read()
      and passing("werner")[0]==0 and not w_pass, f"banned lines passing: {w_pass}")
# 46b. the escalation line (plumbing P17, operator 2026-10-27; P21: retargeted to the pages): an option in the opening ("If it fits"),
#     never naming a single item. (R21 and the model INDEX are archived with the old pack; that part is retired, 2026-11-06, P21.)
esc=[n for n in ("roger-the-pipe-guy","mark-silverbridge","vintage-pipefitter") if "If it fits, add a question" not in open(f"{PERS}/{n}.md").read() or "the escalation said simply" not in open(f"{PERS}/{n}.md").read()]
check("46b. plumbing hook: the escalation line is an option ('If it fits... the escalation said simply') on Roger's, Mark's and Vintage's pages",
      not esc, f"missing on: {esc}")

# ---- the Werner and Frederick upload review (operator, 2026-10-29) ----
# 73. every plumbing channel's real words per minute (Roger 170, Mark 181, Vintage 190, Werner 181; P21: retargeted to check.py's CHANNELS),
#     and the length check uses it: Werner's script cut to 2,010 words fails under 12 minutes; Frederick 162
wpk,wsc,wch,wbr=run_of("werner"); wtxt=open(wsc).read(); wcut=" ".join(wtxt.split()[:2010])
c73=pack_check(wpk,wcut,wch,wbr)
check("73. plumbing check.py sets real words per minute (170/181/190/181); a 2,010-word Werner script fails under 12 minutes; Frederick 162",
      [plc[c]["wpm"] for c in ("roger","mark","vintage","werner")]==[170,181,190,181] and "minutes at 181); needs at least 2172 (12 minutes)" in c73[1]
      and "Words per minute (for runtime and the length minimum): 162" in open(f"{PERS}/frederick-barnes.md").read()
      and "1,950" in open(f"{EL}/SKILL.md").read(), c73[1][-400:])

# 74. the plumbing opening (core scanner; P21: the archived plumbing pack, Werner's and Hank's profiles as read-only fixtures):
#     "today you learn", a promise with a time on it and two promises in the first minute fail; one promise is judged;
#     "nothing here needs a plumber" is judged; "Level one" is a signpost; item one past 45 seconds is marked; "tonight's homework" fails
WERNP=f"{OPERS}/werner-finkbeiner.md"
_,o74a=run_scan("The toilet is blocked. So, today you learn to unclog a toilet. If the answer is no, you will know in two minutes. Nothing from a jug goes in, and you will hear why.\n",[PLR,WERNP])
_,o74b=run_scan("The toilet is blocked, and the water is climbing. By the last level, you will know the one sign that means the main line.\n",[PLR,WERNP])
_,o74c=run_scan("Nothing here needs a plumber. Level one, slow. Plunge it.\n",[PLR,WERNP])
c74d,o74d=run_scan("Cut the board. And that is the whole of tonight's homework.\n",[WWR,f"{OPERS}/hank-hardwood.md"])
_,o74e=run_scan(("The water sits high in the bowl. "*40)+"Level one, slow. Soap and hot water. Level two, rising. Lift the lid.\n",[PLR,WERNP])
check("74. plumbing opening (core scanner): 'today you learn', a timed promise and two promises fail; one end promise and 'no plumber needed' judged; Level signposts; homework fails anywhere",
      "today you learn" in o74a and "a promise with a time on it" in o74a and "OPENING: 2 promises" in o74a
      and "OPENING:" not in o74b.split("JUDGE")[0] and "is it paid at the end of the video" in o74b
      and "no plumber needed" in o74c and "ITEMS: 1" in o74c and c74d==1 and "homework" in o74d
      and "ITEMS: 2" in o74e and "later than 45 seconds" in o74e, o74a[-500:]+o74b[-300:]+o74c[-300:]+o74e[:300])

# 75. the opening and ending rules (P21: the plumbing parts retargeted to check.py and the pages; the unit-plan template parts retired):
#     'today you learn', a timed promise and 'no plumber needed' with a call fail in check.py; a tool list in the opening fails;
#     one small thing at the end on every plumbing and HVAC page, in the electrical pack and the core
c75a=plant("roger","So, today you learn to unclog it, and you will know in two minutes.",1)
c75b=plant("roger","Nothing here needs a plumber.",1)
c75c=plant("roger","You need a plunger, a bucket, a flashlight, gloves and a drain snake.",1)
rm=open(f"{CORE}/retention-mechanics.md").read(); ga=open(f"{CORE}/greenlight-audit.md").read()
small=[n for n in ("roger-the-pipe-guy","mark-silverbridge","vintage-pipefitter","werner-finkbeiner","roger-the-hvac-guy") if "one small thing" not in open(f"{PERS}/{n}.md").read()]
check("75. opening rules in check.py ('today you learn', a timed promise, 'no plumber needed' with a call, no tool list); one small thing at the end on every plumbing and HVAC page, electrical and core",
      "'today you learn'" in c75a[1] and "a promise with a time on it" in c75a[1] and "FAIL scope: 'no plumber needed'" in c75b[1] and "FAIL opening list" in c75c[1]
      and not small and "one small thing to do tonight" in open(f"{EL}/SKILL.md").read()
      and "**One** action: a closing to-do list" in rm and "closing to-do list or \"homework\"" in ga, f"pages missing: {small} | "+c75a[1][-300:]+c75b[1][-300:]+c75c[1][-300:])

# 76. Frederick: one step, one job; the buying step adapts to what the look found; facts guide 1.18 (gauge against breaker),
#     1.17a (kitchen and bathroom circuits by room), 4.30 (GFCI by the new outlet's place), 6.19a (AFCI outlet at the first outlet)
ekp=open(f"{EL}/SKILL.md").read(); fgp=open(f"{EL}/references/facts-guide.md").read()
check("76. electrical: one step one job; adaptive buying step; facts 1.18, 1.17a, 4.30, 6.19a",
      "**One step, one job**" in ekp and "**The buying step adapts to what the viewer found**" in ekp
      and "| 1.18 | The breaker can be smaller than the wire allows" in fgp and "| 1.17a |" in fgp and "| 4.30 |" in fgp
      and "first receptacle outlet of the existing circuit" in fgp, "")

# 77. second round (operator, 2026-10-29; P21: retargeted to hvac-scripts/check.py and the new SKILL.md files): HVAC's opening
#     fails 'today you learn' and a timed promise, and 'no tech needed' with a call; every HVAC script models off a real winner;
#     plumbing talking-point briefs are full briefs. (The unit-plan template's "[file numbers; never none]" is retired with the template.)
hpk,hsc,hch,hbr=run_of("roger-hvac"); hparas=open(hsc).read().split("\n\n")
c77=pack_check(hpk,"\n\n".join(["The furnace quit. So, today you learn the fix. You will know in two minutes."]+hparas),hch,hbr)
c77b=plant("roger-hvac","Nothing here needs a tech.")
hvp=open(NHVR).read()
check("77. HVAC check.py: 'today you learn' and a timed promise fail in the opening; 'no tech needed' with a call fails; one model transcript per video type; plumbing talking-point briefs",
      "'today you learn'" in c77[1] and "a promise with a time on it" in c77[1] and "FAIL scope" in c77b[1]
      and "**One model transcript** for the video type" in hvp and "A brief of talking points is a full brief" in open(f"{PL}/SKILL.md").read(), c77[1][-400:]+c77b[1][-300:])
# ---- P20 (operator 2026-10-29): core scanner changes for style ----
# 83. the title-word check: a pack's title-words in the locked title must be said twice, once in the first minute; title digits match spoken words
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("```scanner\ntitle-words: instant, young, ten years | promise words\n```\nWords per minute: 170\n"); tw=t.name
TT="3 Haircuts That INSTANTLY Make You Look 10 Years YOUNGER"
tw_bad=run_scan("These cuts make you look instantly younger.\n\nNumber one. Keep the length.\n",[tw],title=TT)
tw_good=run_scan("These cuts make you look instantly younger, ten years younger.\n\nNumber one. Keep the length. Instantly lighter, ten years off.\n",[tw],title=TT)
tw_none=run_scan("These cuts are lovely.\n",[tw],title="3 Haircuts for Fine Hair")
check("83. P20 title words: a title word said once (\"younger\"), or not at all, fails; said twice with one early passes; '10 Years' in the title matches 'ten years'; words not in the title aren't asked for",
      tw_bad[0]==1 and '[TITLE WORD] "instant"' in tw_bad[1] and '[TITLE WORD] "ten years"' in tw_bad[1] and '[TITLE WORD] "young" is in the title and said 1 time' in tw_bad[1]
      and tw_good[0]==0 and "TITLE WORDS: instant 2" in tw_good[1] and tw_none[0]==0 and "none of the pack's title-words is in the title" in tw_none[1],
      tw_bad[1][-600:]+tw_good[1][-400:])
# 84. the channel intro is a core hard ban (every channel)
ci=[run_scan(f"Check the hem.\n\n{l}\n")[1] for l in ("I'm Scarlet Sterling and this channel is for women over 60.","I'm Diane, and I'm here for women over 60.")]
check("84. P20: 'this channel is for' and 'I'm here for women over' are core hard bans",
      all("[HARD BAN: channel intro: this channel is for]" in x for x in ci) and "channel intro" not in run_scan("This channel of light at the window helps.\n")[1], "")
# 85. style tenure words: a stylist's or fashion years figure is checked against the profile's tenure; a hair-dye or closet age is not
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("```scanner\ntenure: none\n```\n"); tn=t.name
st_bad=["As a stylist for 30 years, I know this.","After 30 years in fashion, I know this.","In forty years of dressing women, I learned this.","She is a 25-year stylist.","I spent 20 years in the fashion world."]
st_ok=["Ten years of hair dye can dull the ends.","Your jeans have been in the closet for 20 years.","You've been wearing that cut for thirty years."]
st_miss=[l for l in st_bad if run_scan(l+"\n",[tn])[0]!=1]; st_false=[l for l in st_ok if "TENURE" in run_scan(l+"\n",[tn])[1].upper().split("FIX ON SIGHT")[1]]
check("85. P20: style tenure words (stylist, fashion, dressing women, a 25-year stylist) fail with tenure none; hair-dye and closet ages pass",
      not st_miss and not st_false, f"missed: {st_miss}; false: {st_false}")
# 86. style signposts: "Rule number one", "Secret number two" and "Knot three" are items; the build script's electrical command block is closed
sp=run_scan("A short opening line.\n\nRule number one. Keep the length.\n\nSecret number two. Lift the crown.\n\nKnot three. The loop.\n")[1]
bs=open(f"{ROOT}/tools/build_skills.py").read()
check("86. P20: 'Rule number one', 'Secret number two', 'Knot three' are read as items 1-3; the electrical scanner command's code block is closed before HVAC's",
      "ITEMS: 3 | item one at word 4" in sp and "--final\n```\n\nHVAC (the same shape as plumbing" in bs, sp[-400:])

# ---- the style pack and its two channels (operator 2026-10-29: the diagnosis answers) ----
# P21: the style pack, Scarlett's and Diane's pages are the 2026-11-06 simple versions; the 2026-10-31 pack is in archive/pre-p21-2026-11-06/
STR=f"{STY}/SKILL.md"; SCAR=f"{PERS}/scarlett-starling.md"; DIAN=f"{PERS}/diane-de-chambray.md"
sk=open(STR).read(); stc=load_check("style").CHANNELS
# 87. retired 2026-11-06, P21: the old pack's inputs block, overrides and title-words scanner key are gone (the inputs are listed in
#     words; the title's word is "said plainly at least once where it's true", reported only)

# 88. the style bans (P21: retargeted from the scanner block to check.py): both saved scripts pass; the house vocabulary, age slogans,
#     a subscribe ask, a tease, clients, 'studies show', 'one of us', 'e-book' and 'I read every one' fail on Scarlett's script
bad_s=["Small gold hoops finish it.","It reads as expensive.","She looks polished from across the room.","Age is just a number.","You've earned it.",
       "Subscribe for more.","We'll get to that one later.","My clients love this cut.","Studies show it works.","So many of us feel like one of us.","I read every one."]
s_pass=[l for l in bad_s if "FAIL banned" not in plant("scarlett",l)[1]]
harsh=plant("scarlett","She looks like an old lady in it. Nobody wants the granny look.")[1]
check("88. style check.py: both saved scripts pass; house vocabulary, age slogans, subscribe, tease, clients, 'studies show', 'one of us' and 'I read every one' fail; a second harsh word fails",
      passing("scarlett")[0]==0 and passing("diane")[0]==0 and not s_pass and "FAIL harsh word" in harsh, f"passing: {s_pass}; {harsh[-300:]}")

# 89. the two channels (P21: retargeted from the profiles' scanner blocks to check.py's CHANNELS): 169 and 172 words a minute,
#     the printed and spoken book titles, the sign-offs; the name is never spoken; the old intros, sign-offs and book lines fail
pb_s=[l for l in ("I'm Scarlett Starling.","Until next time, stay polished.","I gathered three hundred of them.","Whenever it suits you, it's there.","My daughter loves it.")
      if plant("scarlett",l)[0]!=1]
pb_d=[l for l in ("Diane here.","A bientot.","Every French woman owns a trench.","Marie and Sophie swear by it.","We Americans buy it differently.")
      if plant("diane",l)[0]!=1]
check("89. style check.py: Scarlett 169 and Diane 172 wpm, their books (printed and spoken) and sign-offs; old intros, sign-offs, book lines and unhedged claims fail",
      stc["scarlett"]["wpm"]==169 and stc["diane"]["wpm"]==172 and stc["scarlett"]["printed"]=="300 Budget-Friendly Ways to Look Expensive" and stc["diane"]["printed"]=="The French Way"
      and stc["scarlett"]["signoff"]=="Until next time, ladies, stay elegant." and stc["diane"]["signoff"]=="With love from Paris, my dear friends."
      and not pb_s and not pb_d, f"scarlett passing: {pb_s}; diane passing: {pb_d}")
# 90. wiring: rows 10 and 11 pending; the build knows the pack and both pages; README sections
chan=open(f"{CORE}/channels.md").read(); bs=open(f"{ROOT}/tools/build_skills.py").read(); rd=open(f"{ROOT}/README.md").read()
check("90. style wiring: channel rows 10 and 11 pending; build entries for style-scripts and both personas; README sections",
      "| 10 | Scarlett Starling | `style-scripts` | `personas/scarlett-starling.md` | pending |" in chan and "| 11 | Diane de Chambray | `style-scripts` | `personas/diane-de-chambray.md` | pending |" in chan
      and '"style-scripts": (),' in bs and '"scarlett-starling": ("Scarlett Starling"' in bs and '"diane-de-chambray": ("Diane de Chambray"' in bs
      and "## style-scripts/" in rd and "`scarlett-starling.md`" in rd, "")

# 91. the style references (P21: retargeted): 11 real women's model files (M01, M04, M07, M09, M13, M18, M19, M21, M24, M28, M30) and
#     the H01 hook reference; no F (structure only) files; the pack's description fits the skill limit
SM=f"{STY}/references/models"; mfiles=sorted(f for f in os.listdir(SM) if f.endswith(".md"))
sd=re.search(r"^description: (.*)$",sk,re.M).group(1)
check("91b. the style pack's description fits the skill limit (1,024 characters)", 0<len(sd)<=1024, str(len(sd)))
check("91. style references: 11 M files (M23 dropped) and H01, no F files, each with a 'Signature phrases' section and a transcript",
      [f[:3] for f in mfiles]==["H01","M01","M04","M07","M09","M13","M18","M19","M21","M24","M28","M30"]
      and all("## Signature phrases" in open(f"{SM}/{f}").read() and "## Transcript" in open(f"{SM}/{f}").read() for f in mfiles), str(mfiles))

# 92. iter-07 fixes (operator 2026-10-29; P21: the core parts kept, the pack parts retired with the old style pack): the book's spoken
#     title passes the copy guard; the channel gate confirms a clear one-channel reply; verify_output.py skips M/F model quotes; the
#     scanner's item counts leave out CTA blocks
wf=open(f"{CORE}/workflow.md").read(); vo=open(f"{ROOT}/tools/verify_output.py").read()
bk=run_scan("It's called Three Hundred Budget-Friendly Ways to Look Expensive, and it helps.\n",[f"{OSTY}/SKILL.md",f"{OPERS}/scarlett-starling.md"],refs=[f"{OPERS}/scarlett-starling.md"])
cta=run_scan("Number one. A line.\n\n===START CTA(X)===\nA long aside about the book that runs on and on and on.\n===END CTA===\n\nNumber two. Another line.\n")[1]
check("92. iter-07 core fixes: book title allowed (core scanner, archived fixtures); gate confirms a clear one-channel reply; model quotes skipped; CTA blocks out of item counts",
      "COPIED FROM REFERENCE" not in bk[1] and '"[exact name], right?"' in wf and "[ERSMF]" in vo and "item words: 1 = 4, 2 = 4" in cta, bk[1][-300:]+cta[-300:])

# ---- P21 applied (operator 2026-11-06: "yes use defaults"; "sawdust sam is dropped"): the new packs' own checks ----
# 94. each P21 pack's check.py runs and passes on its saved test scripts, with the title and brief in each iteration folder
bad94=[]
for pk,script,ch_,brief in P21_RUNS:
    code_,out_=pack_check(pk,open(script).read(),ch_,brief)
    if code_!=0 or not out_.rstrip().endswith("RESULT: PASS"): bad94.append(f"{os.path.relpath(script,ROOT)} ({ch_}): {out_[-300:]}")
check("94. P21: each pack's check.py passes its saved test scripts (iter-14 final, iter-15 run-new, iter-16 four runs, iter-17 run-new, iter-18 two runs)",
      len(P21_RUNS)==9 and not bad94, " | ".join(bad94))

# 95. every "Signature phrases" quote in each model file occurs exactly (whitespace joined) in that file's transcript.
#     One known exception, reported: H01's transcript holds the three hooks only (up to item one), so its last phrase is matched
#     in the full study transcript of the same video.
SIG_ELSEWHERE={("H01-paris-never-ages-hooks.md","why do I look so tired today"):f"{ROOT}/studies/style/competitors/paris-never-ages/ZLjhi5s2Znw/transcript.txt"}
bad95=[]; n95=0
for pk in ("style","plumbing","hvac","woodworking"):
    for m in sorted(glob.glob(f"{NPACK[pk]}/references/models/*.md")):
        raw=open(m).read(); sec=re.search(r"## Signature phrases[^\n]*\n(.*?)(?=\n## )",raw,re.S); parts=raw.split("\n## Transcript",1)
        if not sec or len(parts)<2: bad95.append(f"{os.path.basename(m)}: no Signature phrases or Transcript section"); continue
        tr=re.sub(r"\s+"," ",parts[1].split("\n",1)[1])
        for q in re.findall(r'^- "(.+)"\s*$',sec.group(1),re.M):
            n95+=1; q=re.sub(r"\s+"," ",q)
            if q in tr: continue
            alt=SIG_ELSEWHERE.get((os.path.basename(m),q))
            if alt and os.path.isfile(alt) and q in re.sub(r"\s+"," ",open(alt).read()): continue
            bad95.append(f"{os.path.basename(m)}: \"{q}\"")
check("95. P21: every signature phrase in the 39 model files is quoted exactly from its transcript (H01's last one from the full study transcript)",
      n95>=150 and not bad95, f"{n95} phrases; not found: {bad95}")

# 96. the two price guides are byte-identical to the archived ones (copied unchanged, operator default: no price change in P21)
same96=[pk for pk in ("plumbing","hvac") if open(f"{NPACK[pk]}/references/price-guide.md","rb").read()==open(f"{OLD}/{pk}-scripts/references/price-guide.md","rb").read()]
check("96. P21: the plumbing and HVAC price guides are byte-identical to the archived ones", same96==["plumbing","hvac"], str(same96))

# 97. every channel page of the nine P21 channels carries the "Hold the reveal" rule (operator, 2026-11-06)
P21_PAGES=["scarlett-starling","diane-de-chambray","roger-the-pipe-guy","mark-silverbridge","vintage-pipefitter","werner-finkbeiner","roger-the-hvac-guy","hank-hardwood","dale-oakfield"]
noreveal=[n for n in P21_PAGES if "**Hold the reveal**" not in open(f"{PERS}/{n}.md").read()]
check("97. P21: all nine channel pages carry the 'Hold the reveal' rule", not noreveal, ", ".join(noreveal))

# 98. the build list: the four P21 packs and nine persona skills are built (from the library copies, laid out as drafts/p21-*/), and
#     Sawdust Sam is not; the defaults stay as accepted (Dale's five book mentions, Roger the HVAC Guy at 150, the research pack, 7 plumbing models)
spec98=importlib.util.spec_from_file_location("build98",f"{ROOT}/tools/build_skills.py"); b98=importlib.util.module_from_spec(spec98); spec98.loader.exec_module(b98)
want98={f"{n}-persona" for n in P21_PAGES}|{"style-scripts","plumbing-scripts","hvac-scripts","woodworking-scripts"}
built98={f"{k}-persona" for k in b98.PERSONAS}|set(b98.PACKS)
dale=open(f"{PERS}/dale-oakfield.md").read()
check("98. P21 build list: the 13 skills (4 packs, 9 persona pages) are built and listed in P21_SKILLS; Sawdust Sam is not built; the accepted defaults hold",
      want98<=built98 and set(b98.P21_SKILLS)==want98 and all(b98.PACKS[p_]==() for p_ in ("style-scripts","plumbing-scripts","hvac-scripts","woodworking-scripts"))
      and "sawdust-sam" not in b98.PERSONAS and "sawdust-sam-persona" not in built98
      and "Five of them, spread through the middle" in dale and load_check("hvac").CHANNELS["roger-hvac"]["wpm"]==150 and "research pack" in open(f"{WW}/SKILL.md").read()
      and len(glob.glob(f"{PL}/references/models/*.md"))==7
      and not os.path.exists(f"{PERS}/sawdust-sam.md") and os.path.isfile(f"{OPERS}/sawdust-sam.md") and os.path.isfile(f"{OPERS}/books/sawdust-sam-book.md")
      and "| 6 | Sawdust Sam | `woodworking-scripts` | `archive/pre-p21-2026-11-06/personas/sawdust-sam.md` | dropped |" in open(f"{CORE}/channels.md").read(),
      f"missing from build: {sorted(want98-built98)}; P21_SKILLS: {sorted(set(b98.P21_SKILLS)^want98)}")

for name,ok,detail in results:
    print(("PASS " if ok else "FAIL ")+name+("" if ok else f"\n      -> {detail[:900]}"))
print(f"\n{sum(ok for _,ok,_ in results)}/{len(results)} passed")
