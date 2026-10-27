# Library test suite: run with  python3 tests/run_checks.py  from the library root (or set LIB_ROOT).
# Checks file references, stale leftovers, override statements, hard-ban and filler parity
# between humanizer.md and script-scanner.py, scanner behavior on clean and broken scripts,
# ban lifting, the numbers check, the woodworking inputs block, shared labels across files, the
# copy guard (--refs) against the niche pack's reference files, production notes read aloud,
# repeated sentences, persona facts (tenure, near-miss names, title numbers win), the tease phrasings and once-per-script phrases,
# and the plumbing pack: its inputs block, scanner block, Mark's contraction ban, the copy guard over every model file,
# the plumbing profiles' fixed facts and the channel list, and the HVAC pack (checks 60+).
import re, os, glob, subprocess, sys, tempfile, textwrap
sys.dont_write_bytecode = True
ROOT=os.environ.get("LIB_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORE=f"{ROOT}/core"; WW=f"{ROOT}/woodworking-scripts"; PL=f"{ROOT}/plumbing-scripts"; PERS=f"{ROOT}/personas"; SCAN=f"{CORE}/script-scanner.py"
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
            ok = base in names or ref in rels or os.path.isfile(os.path.join(ROOT,ref))
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

WWR=f"{WW}/SKILL.md"
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
code3,out3=run_scan("After 40 years at the bench I know this.\n",[f"{ROOT}/personas/hank-hardwood.md"])
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

# 18. the woodworking profiles carry their fixed facts
fx=[l.strip() for f in ("hank-hardwood","dale-oakfield") for l in re.findall(r"```scanner\n(.*?)```",open(f"{ROOT}/personas/{f}.md").read(),re.S)[0].splitlines()]
check("18. Hank's and Dale's profiles give their name, book and tenure to the scanner",
      fx.count("tenure: none")==2 and "name: Hank Hardwood" in fx and "name: Dale Oakfield" in fx and sum(l.startswith("book:") for l in fx)==2, str(fx))

# 19. title numbers win: a years figure in the locked title is allowed; any third figure still fails
code,out=run_scan("I have been a plumber for 30 years, and this one matters.\n",[facts],title="Borax vs Washing Soda: A 30-Year Plumber's Verdict")
code2,out2=run_scan("I have been a plumber for 35 years, and this one matters.\n",[facts],title="Borax vs Washing Soda: A 30-Year Plumber's Verdict")
code3,out3=run_scan("After 40 years at the bench I know this.\n",[f"{ROOT}/personas/hank-hardwood.md"],title="What 40 Years of Woodworking Taught Me")
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
PLR=f"{PL}/SKILL.md"; ROGER=f"{PERS}/roger-the-pipe-guy.md"; MARK=f"{PERS}/mark-silverbridge.md"; VINT=f"{PERS}/vintage-pipefitter.md"
PL_REFS=[PLR, f"{PL}/references/excerpts.md", f"{PL}/references/voice-samples.md"]+sorted(glob.glob(f"{PL}/references/models/*.md"))

# 21. plumbing inputs block parses: title, brief and rotation log required, the research pack not used
sk=open(PLR).read()
inp=re.search(r"```inputs\n(.*?)```",sk,re.S)
rows=[[c.strip() for c in l.strip()[1:].split("|")] for l in inp.group(1).splitlines() if l.strip().startswith("-")] if inp else []
want={"title":"required","brief":"required","research-pack":"not used","rotation-log":"required"}
check("21. plumbing inputs block: 4 well-formed inputs, research pack not used",
      len(rows)==4 and all(len(r)==3 for r in rows) and {r[0]:r[1] for r in rows}==want, str(rows))

# 22. the plumbing scanner block: every ban fires, once-limits fail on the second use, a clean plumbing paragraph passes
clean_pl=textwrap.dedent("""\
One cup of washing soda, stirred into hot tap water, clears the slow kitchen drain you keep paying somebody to snake.

A drain call for that usually starts around a hundred and fifty dollars. A box of washing soda runs about five to seven dollars and gives you close to a dozen treatments.

It won't touch a hair clog in the bathroom. That's a different job, and number four handles it.

Number four is the two-dollar tool that pulls the hair out in one go. And the final item keeps every bit of this safe on your old cast-iron line.

Number one. Stir one cup of washing soda into about three cups of hot tap water until it's clear. Pour it in slowly and leave it six to eight hours. If the sink empties fast in the morning, you're done.

What's the oldest pipe in your basement, and which sink backs up first at your place? I read every one.
""")
planted={"first-person test claim":"I tested all three on a slow sink.","first-person demonstration":"Now watch me pour it in.",
         "pointing at the screen":"Look at the trap on the left before you start.","template stock line: the economics aside":"It's not a scam, it's just economics.",
         "template stock line: channel promise":"This channel is all about saving you money.","template stock line":"Grab it now or later.",
         "hype that got mocked":"It looked like a horror movie under there."}
code,out=run_scan(clean_pl,[PLR,ROGER])
bad=[]
for label,line in planted.items():
    c,o=run_scan(f"Rinse the trap.\n\n{line}\n",[PLR])
    if c!=1 or f"NICHE/PERSONA BAN: {label}]" not in o: bad.append(label)
code2,out2=run_scan("Between you and me, it is the flapper.\n\nAnd between you and me, the chain is fine too. Trust me on this one.\n",[PLR])
check("22. plumbing scanner block: each ban fires; a once-phrase used twice fails and once passes; a clean plumbing paragraph passes",
      code==0 and "FIX ON SIGHT (0)" in out and not bad and code2==1 and "NICHE/PERSONA LIMIT: between you and me] used 2 times" in out2
      and "trust me] used" not in out2, f"missed: {bad} | "+out[:500]+out2[:500])

# 23. Mark's profile bans contractions; his no-contraction style passes
code,out=run_scan("Do not pour it in dry. It is the flapper nine times out of ten, and that is a cheap part.\n",[PLR,MARK])
code2,out2=run_scan("Don't pour it in dry. It's the flapper, and you'll want a cheap part.\n",[PLR,MARK])
check("23. Mark's contraction ban: contractions are fix-on-sight, his plain style passes",
      code==0 and code2==1 and out2.count("contraction")>=3, out+out2)

# 24. copy guard over the plumbing references: the clean paragraph passes against all of them, and a line lifted from
#     every model file (and from the excerpts and voice samples) is caught and traced to that file
runs=sc.read_refs(PL_REFS)
lifted=[]; nolift=[]
for f in PL_REFS:
    name=os.path.basename(f); got=None
    for para in open(f).read().split("\n\n"):
        toks=sc.copy_tokens(para)
        for i in range(len(toks)-12):
            if all(runs.get(tuple(toks[j:j+sc.COPY_RUN]))==name for j in range(i,i+5)):
                got=" ".join(toks[i:i+12]); break
        if got: break
    (lifted.append((name,got)) if got else nolift.append(name))
code,out=run_scan("\n\n".join(g.capitalize()+"." for _,g in lifted)+"\n",[PLR],refs=PL_REFS)
uncaught=[n for n,_ in lifted if f"COPIED FROM REFERENCE: {n}]" not in out]
code2,out2=run_scan(clean_pl,[PLR,ROGER],refs=PL_REFS+[ROGER])
check("24. copy guard: the clean plumbing paragraph passes against the pack's SKILL.md, excerpts, voice samples and all model files; a line from each is caught",
      len(PL_REFS)>=42 and not nolift and not uncaught and code==1 and code2==0 and "COPIED" not in out2,
      f"refs={len(PL_REFS)} no line found in {nolift}; not caught {uncaught}; "+out2[:400])

# 25. the plumbing profiles give the scanner their fixed facts
def facts_of(p): return [l.strip() for l in re.findall(r"```scanner\n(.*?)```",open(p).read(),re.S)[0].splitlines()]
fr,fm,fv=facts_of(ROGER),facts_of(MARK),facts_of(VINT)
check("25. Roger's, Mark's and Vintage's profiles give their name, book and tenure (45, 40, 45; Vintage has no book)",
      "name: Roger the Pipe Guy" in fr and "tenure: 45" in fr and sum(l.startswith("book:") for l in fr)==1
      and "name: Mark Silverbridge" in fm and "tenure: 40" in fm and sum(l.startswith("book:") for l in fm)==1
      and "name: The Vintage Pipefitter" in fv and "tenure: 45" in fv and not any(l.startswith("book:") for l in fv), str((fr,fm,fv)))
code,out=run_scan("I have been at this for 40 years.\n",[PLR,ROGER])
code2,out2=run_scan("I have been at this for 45 years.\n",[PLR,ROGER])
check("25b. a plumbing tenure that differs from the profile fails; the profile's passes", code==1 and "PERSONA FACT: tenure" in out and code2==0, out+out2)

# 26. the channel list: the three plumbing channels are ready, on plumbing-scripts, and their profiles say so
ch=open(f"{CORE}/channels.md").read()
bad=[]
for name,slug in (("Roger the Pipe Guy","roger-the-pipe-guy"),("Mark Silverbridge","mark-silverbridge"),("The Vintage Pipefitter","vintage-pipefitter")):
    row=re.search(rf"^\| \d+ \| {re.escape(name)} \| `plumbing-scripts` \| `personas/{slug}.md` \| ready \|$",ch,re.M)
    prof=open(f"{PERS}/{slug}.md").read()
    if not (row and "Status: ready" in prof and "Niche pack: plumbing-scripts" in prof): bad.append(name)
check("26. channels.md lists Roger, Mark and Vintage as ready on plumbing-scripts, and their profiles agree", not bad and os.path.isfile(PLR), ", ".join(bad))

# 27. (iter-01's check 14) the numbers check finishes on spoken fractions and lumber names (it used to loop forever on them)
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("Drill a three-quarter inch hole. Use five-eighths inch screws on a one-by-eight, seventeen and three-quarters across.\n"); fs=t.name
with tempfile.NamedTemporaryFile("w",suffix=".md",delete=False) as t: t.write("17.75 0.75 0.625\n"); fp=t.name
try:
    r=subprocess.run(["python3",SCAN,fs,"--pack",fp],capture_output=True,text=True,timeout=20); ok14,d14=r.returncode==0,r.stdout[-400:]
except subprocess.TimeoutExpired:
    ok14,d14=False,"scanner did not finish within 20 seconds"
check("27. numbers check finishes on fraction words (three-quarter, five-eighths, one-by-eight)", ok14, d14)

# 28. (iter-01's check 15) every persona profile's scanner block flags "e-book" (the offer is always called "book")
PROFILES=sorted(glob.glob(f"{ROOT}/personas/*.md"))
PROFILES=[p for p in PROFILES if "```scanner" in open(p).read()]
noflag=[os.path.basename(p) for p in PROFILES if run_scan("Grab my e-book from the link.\n",[p])[0]!=1]
check("28. every persona profile flags 'e-book'", len(PROFILES)>=2 and not noflag, f"profiles={[os.path.basename(p) for p in PROFILES]} not flagging: {noflag}")

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
code,out=run_scan("Cut the board.\n",[WWR,f"{PERS}/hank-hardwood.md"])
code2,out2=run_scan("Rinse the trap.\n",[PLR,ROGER])
check("32. runtime uses the profile's words per minute (Hank 185) and the pack's minimum (plumbing 12, woodworking 8)",
      "at 185 words a minute; minimum 8" in out and "at 150 words a minute; minimum 12" in out2, out[:300]+out2[:300])

# 33. a title's years of selling unlock that figure (Dale's title format)
code,out=run_scan("I've spent forty years at the bench.\n",[WWR,f"{PERS}/dale-oakfield.md"],title="In 40 Years of Selling, Nothing Beats This Build")
check("33. 'In 40 Years of Selling' in the title allows forty years in the script", code==0 and "PERSONA FACT" not in out, out)

# 34. the wording each profile requires passes its own copy guard
cases=[(ROGER,PLR,"Grab it from the link in the description and the QR code on screen."),
       (MARK,PLR,"It is at the link in the description and the QR code on screen."),
       (f"{PERS}/hank-hardwood.md",WWR,"Grab it with the QR code on screen or the top link in the description."),
       (f"{PERS}/dale-oakfield.md",WWR,"Here's what I'd ask of you. Try it this week.")]
bad=[os.path.basename(pf) for pf,rules,line in cases if run_scan(line+"\n",[rules,pf],refs=[pf])[0]!=0]
check("34. each profile's required CTA or ending wording passes the copy guard against the profile", not bad, ", ".join(bad))

# 35. plumbing bans the 'today we're going to' opening; Mark's uncontracted stock phrases still count once; more contractions caught
code,out=run_scan("Today we're going to fix the drain.\n",[PLR,ROGER])
code2,out2=run_scan("Here is the part nobody tells you.\n\nAnd here is the part nobody tells you again.\n",[PLR,MARK])
code3,out3=run_scan("Let's look. Where's the valve?\n",[PLR,MARK])
check("35. plumbing: 'today we're going to' banned; Mark's 'here is the part nobody tells you' limited to once; 'Let's' and 'Where's' caught",
      code==1 and "today we're going to" in out and code2==1 and "NICHE/PERSONA LIMIT" in out2 and code3==1 and out3.count("contraction")>=2, out+out2+out3)

# 36. the plumbing price guide: every table row is rounded (no cents), carries a check mark, and the pack points to it
PG=f"{PL}/references/price-guide.md"
rows=[l for l in open(PG).read().splitlines() if l.startswith("| ") and not l.startswith("| Item") and not l.startswith("| Fact") and not set(l) <= set("|- ")] if os.path.isfile(PG) else []
cents=[l for l in rows if re.search(r"\$\d[\d,]*\.\d", l)]
nocheck=[l for l in rows if l.rstrip(" |").split("|")[-1].strip() not in ("confirmed","adjusted","thin","in words")]
check("36. price guide: 100+ rows, none in cents, each marked confirmed / adjusted / thin / in words; the plumbing pack and its scanner line use it",
      len(rows)>=100 and not cents and not nocheck and "references/price-guide.md" in open(PLR).read()
      and "price-guide.md" in open(f"{ROOT}/tools/build_skills.py").read(), f"rows={len(rows)} cents={cents[:3]} nocheck={nocheck[:3]}")

# ---- the emotion draft applied (2026-10-21, after plumbing test run 02) ----
# 37. the plumbing pack carries the emotion section, the list item shape, the CTA template, the number cap, the gas steps,
#     the trade terms and the myth flag's belief; Roger's and Mark's profiles carry the new CTA; the scanner command guards SKILL.md
sk=open(PLR).read()
need=["## Emotion, all the way through","### The item shape in lists","about 100-130 words","**The number cap**",
      "figures on no more than about half the items","never before the end of item 3","about 60-80 words","an outright ask to leave a comment",
      "When the script names a source, its figure is said as the source gives it","as long as nothing in it is fluff",
      "the gas-leak row of `references/price-guide.md` section 9","no flame, no car",
      "psi, trap, P-trap, jetting, relining, anode rod, cleanout, PRV","names the belief it flips","absolutely criminal",
      "this file (`SKILL.md`)","much more of it, inside items and between them"]
miss=[n for n in need if n not in sk]
prof_bad=[os.path.basename(p) for p in (ROGER,MARK) if "20-60" in open(p).read() or "about 60-80 words, about a third of the way in, never before the end of item 3" not in open(p).read()]
bs=open(f"{ROOT}/tools/build_skills.py").read()
check("37. plumbing pack: emotion, item shape, CTA template (a third in, not before item 3), comment ask, number cap, named-source figures, gas steps, trade terms, myth flag; Roger and Mark profiles; SKILL.md in the scanner's --refs",
      not miss and not prof_bad and "--refs <plumbing-scripts>/SKILL.md" in bs and "20-60" not in sk, f"missing {miss}; profiles {prof_bad}")

# 38. the outrage line: "criminal" trips no ban, the operator's phrase passes once and fails on the second use (rotate it);
#     a line lifted from the pack's own opening example is caught by the copy guard
code,out=run_scan("A new sewer line can run into the thousands. That is absolutely criminal, for a pipe in the ground.\n",[PLR,ROGER])
code2,out2=run_scan("That is absolutely criminal.\n\nAnd that is absolutely criminal too.\n",[PLR,ROGER])
code3,out3=run_scan("That slow flush you keep ignoring? It can end with a crew digging up your front yard.\n",[PLR,ROGER],refs=PL_REFS+[ROGER])
code4,out4=run_scan("On the high end, this can run up to $15,000. It can cost you anywhere from $300 to $600, depending on where you live and how bad it's got.\n\n"
                    "If you smell gas, get everybody out of the house right now and walk away upwind. Don't flip a light switch, don't use the phone inside, "
                    "don't light a match and don't start the car. Once you're well down the street, call 911 and the gas company yourself. "
                    "Don't go back in until they tell you it's safe, and let them turn the gas back on and relight the pilots. Some people can't smell it at all.\n\n"
                    "Tell me which drain gives you trouble every winter. I read every one.\n",[PLR,ROGER],refs=PL_REFS+[ROGER])
check("38. 'absolutely criminal' passes once and is limited to once; the pack's own example lines are under the copy guard, but its range wording, the gas steps in fresh words and 'I read every one' are not flagged",
      code==0 and code2==1 and "absolutely criminal] used 2 times" in out2 and code3==1 and "COPIED FROM REFERENCE: SKILL.md]" in out3
      and "COPIED" not in out4, out[:300]+out2[:300]+out3[:300]+out4[:600])

# 39. core: straight quotes, and the scanner line comes from a real run on the delivered text (or says "checked by hand")
wf=open(f"{CORE}/workflow.md").read(); ga=open(f"{CORE}/greenlight-audit.md").read()
check("39. core: straight quotes before the final scan; the Scanner evidence line is a real run on the delivered text or 'checked by hand'",
      "**Straight quotes and apostrophes only**" in wf and "Run it last on the exact text that will be delivered" in wf
      and "Scanner: [run on the delivered text | checked by hand]" in ga and "never reports a count it didn't measure" in ga)

# ---- Sawdust Sam relaunch (2026-10-23) ----
# 40. the woodworking pack carries the heritage section (P8, P9), its safety lines and scanner line; the template has a HERITAGE block;
#     the core's research rules point to the exception
SAM=f"{PERS}/sawdust-sam.md"
wk=open(WWR).read(); tp=open(f"{WW}/references/research-pack-template.md").read(); rs=open(f"{CORE}/research-and-sourcing.md").read()
need=["## Heritage builds (old-world and foreign styles)","**The skeleton doesn't change.**","**Heritage beats.**","**Style, never replica.**",
      "**The old way is an option, never the main step.**","**What the history may say (P8, operator 2026-10-23).**","**Proof for a heritage build (P9, operator 2026-10-23).**",
      "**Lamps and lights:**","**Old-world finishes and pigments:**"]
miss=[n for n in need if n not in wk]
check("40. woodworking pack: heritage builds (beats, style not replica, old way as option, P8 history, P9 proof), lamp and old-finish safety; template HERITAGE block; core points to the exception",
      not miss and "HERITAGE                           [heritage builds only" in tp and "the assumption, if none found" in tp and "P8, operator 2026-10-23" in rs, f"missing {miss}")

# 41. Sam's profile: Talking Head, 174 wpm, tenure none, his name and book, the CTA points to both the QR code and the top link,
#     the book file exists with its page map and the never-cite-past-80 rule; the channel row is pending until the details are picked
sp=open(SAM).read(); sb=f"{PERS}/books/sawdust-sam-book.md"
fs=facts_of(SAM); ch=open(f"{CORE}/channels.md").read()
check("41. Sam's profile: Talking Head, 174 wpm, name/book/tenure facts, QR code and top link, book file with page map; channels.md row 6 ready",
      "Script type: Talking Head" in sp and "Words per minute (for runtime and the 8-minute minimum): 174" in sp and "tenure: none" in fs and "name: Sawdust Sam" in fs
      and "book: The Old Ways" in fs and "the QR code on screen or the top link in the description (every CTA says both)" in sp
      and os.path.isfile(sb) and "## Chapter page map" in open(sb).read() and "cite nothing past page 80" in sp
      and re.search(r"^\| 6 \| Sawdust Sam \| `woodworking-scripts` \| `personas/sawdust-sam.md` \| ready \|$",ch,re.M) is not None, str(fs))

# 42. Sam's scanner: invented trips, encounters, teachers and "scientists now say" fail; his required CTA wording, a plain
#     old-way line and his name pass; a years figure fails (tenure none)
fails=[l for l in ("When I was in Kyoto I saw this.","I once met an old carver who did this.","I visited a temple workshop.",
                   "My old mentor taught me this joint.","Scientists now say the Vikings were right.","After 40 years at the bench I know this.")
       if run_scan(l+"\n",[WWR,SAM])[0]!=1]
passes=[l for l in ("Grab it with the QR code on screen or the top link in the description.","That's how they did it the old way.",
                    "Subscribe to Sawdust Sam for more.","That one's on page 25 of Sawdust Sam's book, and Hank Hardwood's too.") if run_scan(l+"\n",[WWR,SAM],refs=[SAM])[0]!=0]
check("42. Sam's scanner: invented trips, encounters, teachers, 'scientists now say' and a years figure fail; his CTA wording and plain lines pass",
      not fails and not passes, f"not failing: {fails}; not passing: {passes}")

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

# 45. no promise block in the plumbing hook (P10, operator 2026-10-25): the opening's job 5 is the count line, the promise
#     block is on the opening's never list, and the plan template carries the count line
pk=open(f"{ROOT}/plumbing-scripts/SKILL.md").read(); up=open(f"{ROOT}/plumbing-scripts/references/unit-plan-template.md").read()
op=pk[pk.index("## The opening"):pk.index("## Emotion, all the way through")]
check("45. plumbing hook: no promise block (P10); job 5 is the count line, which never names a single item; the plan template follows",
      "5. **The count line, when the video has a count**" in op and "5. **The promise block**" not in op
      and "a promise block or any run-down of what later items hold" in op and "Promise straight after" not in pk
      and "- count line:" in up and "- promise block:" not in up, "")

# ---- the HVAC pack and Roger the HVAC Guy (2026-10-27; numbered 60+ to stay clear of the other branches' checks) ----
HV=f"{ROOT}/hvac-scripts"; HVR=f"{HV}/SKILL.md"; ROGER_HVAC=f"{PERS}/roger-the-hvac-guy.md"; ROGER_PIPE=f"{PERS}/roger-the-pipe-guy.md"
HV_REFS=[HVR,f"{HV}/references/excerpts.md",f"{HV}/references/voice-samples.md"]+sorted(glob.glob(f"{HV}/references/models/*.md"))
HV_REFS=[r for r in HV_REFS if os.path.exists(r)]

# 60. every file reference in the HVAC pack and its profile resolves (placeholders in the spec and templates aside)
HV_PLACEHOLDER={"references/models/R04-...md","R44-...md","<ID>-<channel-slug>-<short-topic-slug>.md","references/audience.md",
                "CONCLUSIONS.md","niche-research/studies/hvac/CONCLUSIONS.md"}  # the last two live in the niche-research repository
hv_files=[f for f in glob.glob(f"{HV}/**/*.md",recursive=True)]+[ROGER_HVAC]
missing=[]
for f in hv_files:
    for ref in re.findall(r"`([^`\s]+?\.(?:md|py)|[a-z-]+/)`", open(f).read()):
        if ref in HV_PLACEHOLDER: continue
        ok = any(os.path.isdir(os.path.join(b,ref)) for b in (ROOT,HV,PERS,os.path.dirname(f))) if ref.endswith("/") else (os.path.basename(ref) in repo_names or ref in repo_rels or os.path.isfile(os.path.join(HV,ref)))
        if not ok: missing.append(f"{os.path.relpath(f,ROOT)} -> {ref}")
check("60. every file reference in the HVAC pack and Roger the HVAC Guy's profile resolves", not missing, "; ".join(sorted(set(missing))))

# 61. HVAC inputs block: title, brief and rotation log required, the research pack not used
hvs=open(HVR).read(); ib=re.search(r"```inputs\n(.*?)```",hvs,re.S)
rows={l.split("|")[0].strip("- ").strip():l.split("|")[1].strip() for l in (ib.group(1).splitlines() if ib else []) if "|" in l}
check("61. HVAC inputs block: title, brief, rotation log required; research pack not used",
      rows.get("title")=="required" and rows.get("brief")=="required" and rows.get("rotation-log")=="required" and rows.get("research-pack")=="not used", str(rows))

# 62. the HVAC scanner block: every ban fires; spoken forms and a clean HVAC paragraph pass
bad=["Today we're going to fix your furnace.","I tested all four filters.","Set it to 24 V.","That runs $75-$200.","Your A/C needs air.",
     "Old R-22 units are rare.","Get a CO alarm.","Your furnace will thank you.","Keep your cool out there.","None of this is hidden because it's hard.",
     "If this saved you a call, subscribe.","Same companies, same story.","Stay tuned for the last one."]
fails=[l for l in bad if run_scan(l+"\n",[HVR,ROGER_HVAC])[0]!=1]
clean_hv=("When the furnace fires up and then shuts off again, the usual culprit is a dirty flame sensor, the small rod that tells it the burner caught. "
          "Turn the power off at the furnace switch, check it's dead with a non-contact tester, and close the gas valve. "
          "A tech charges anywhere from $100 to $250 to clean it, depending on where you live. A MERV 13 filter on an older HVAC system "
          "can choke the blower, and your AC coil can freeze. Old R-twenty-two units are getting rare, and a carbon monoxide alarm goes on every floor.\n")
code,out=run_scan(clean_hv,[HVR,ROGER_HVAC])
once2=run_scan("It goes quietly. It fails quietly.\n",[HVR,ROGER_HVAC])[0]
check("62. HVAC scanner block: every ban fires (units, hyphen ranges, slashes, refrigerant codes, CO, stock lines, the faceless leader's catchphrases); spoken forms pass; 'quietly' once",
      not fails and code==0 and once2==1, f"not failing: {fails}; clean: {out[-600:] if code else ''}")

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

# 65. the two Roger channels never mention each other (operator, 2026-10-27)
a1=run_scan("Over on the Pipe Guy channel I cover drains.\n",[HVR,ROGER_HVAC])[0]
a2=run_scan("Grab One Hundred Old-House Fixes from the link.\n",[HVR,ROGER_HVAC])[0]
a3=run_scan("My friend Roger the HVAC Guy covers furnaces.\n",[PLR,ROGER])[0]
a4=run_scan("Subscribe to Roger the HVAC Guy for more.\n",[HVR,ROGER_HVAC])[0]
check("65. the two Rogers: each profile fails the other channel's name (and the HVAC one the plumbing book); its own name passes",
      a1==1 and a2==1 and a3==1 and a4==0, f"{a1}{a2}{a3}{a4}")

# 66. HVAC references are real people on camera only (operator, 2026-10-27): no S files, every model tagged real; the copy guard
#     runs over every HVAC reference file and catches a line lifted from a model
models=sorted(glob.glob(f"{HV}/references/models/[RS]*.md"))
sfiles=[os.path.basename(m) for m in models if os.path.basename(m).startswith("S")]
untagged=[os.path.basename(m) for m in models if "**Tag:** [real]" not in open(m).read()]
lift=""
for m in models:
    sc_=re.search(r"## Script.*?\n(.*?)\n## ",open(m).read(),re.S)
    if sc_:
        w=re.sub(r"\[[^\]]*\]","",sc_.group(1)).split()
        if len(w)>40: lift=" ".join(w[20:32]); break
code_l,out_l=run_scan(lift+".\n",[HVR,ROGER_HVAC],refs=HV_REFS) if lift else (0,"")
code_c,out_c=run_scan(clean_hv,[HVR,ROGER_HVAC],refs=HV_REFS)
check("66. HVAC models: real people only (no S files, every model tagged real); the copy guard catches a lifted model line and passes the clean paragraph",
      len(models)>=15 and not sfiles and not untagged and code_l==1 and "copied from reference" in out_l.lower() and code_c==0,
      f"models={len(models)} S={sfiles} untagged={untagged} lift={code_l} clean={code_c} {out_c[-300:] if code_c else ''}")

# 67. wiring: the channel row and the profile agree (pending until a test passes), on hvac-scripts; the builder ships both skills
ch=open(f"{CORE}/channels.md").read(); pr=open(ROGER_HVAC).read(); bs=open(f"{ROOT}/tools/build_skills.py").read()
row=re.search(r"^\| \d+ \| Roger the HVAC Guy \| `hvac-scripts` \| `personas/roger-the-hvac-guy.md` \| (\w+) \|",ch,re.M)
pst=re.search(r"^Status: (\w+)",pr,re.M)
check("67. Roger the HVAC Guy: channel row and profile status agree, on hvac-scripts; the builder ships hvac-scripts and his persona skill with an HVAC scanner command",
      bool(row) and bool(pst) and row.group(1)==pst.group(1) and "Niche pack: hvac-scripts" in pr
      and '"hvac-scripts": ("archive", "model-file-spec.md")' in bs and '"roger-the-hvac-guy":' in bs and "--refs <hvac-scripts>/SKILL.md" in bs,
      f"row={row.group(1) if row else None} profile={pst.group(1) if pst else None}")

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
      and "references/price-guide.md" in open(HVR).read() and "<hvac-scripts>/references/price-guide.md" in open(f"{ROOT}/tools/build_skills.py").read(),
      f"rows={len(hrows)} cents={hcents[:3]} nocheck={hnocheck[:3]} missing={hmiss} warn={hwarn}")

for name,ok,detail in results:
    print(("PASS " if ok else "FAIL ")+name+("" if ok else f"\n      -> {detail[:900]}"))
print(f"\n{sum(ok for _,ok,_ in results)}/{len(results)} passed")
