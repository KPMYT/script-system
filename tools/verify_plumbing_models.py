# Checks every plumbing model file: the labelled script (labels removed) against its study transcript, 8-word windows.
# Small "missing" counts come from label notes in parentheses, e.g. "(1, cont.)". Run: python3 tools/verify_plumbing_models.py
import re,glob,sys,os
root=os.environ.get("LIB_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for f in sorted(glob.glob(f"{root}/drafts/plumbing-scripts-refs/references/models/[RS]*.md")):
    s=open(f).read()
    vid=re.search(r"\*\*Video:\*\*\s*([A-Za-z0-9_-]{11})",s)
    sec=re.search(r"## Script \(verbatim, labelled\)\n(.*?)\n## Doesn",s,re.S)
    if not vid or not sec: print(os.path.basename(f),"FORMAT?"); continue
    body=re.sub(r"\[[^\]]*\]","",sec.group(1)); body=re.sub(r"\(\d+(?:, cont\.)?\)|\([a-z ,.]*cont\.\)","",body)
    tf=glob.glob(f"{root}/studies/plumbing/data/*/*/{vid.group(1)}/transcript.txt")[0]
    t=re.sub(r"\[[^\]]*\]","",open(tf).read())
    tw=" ".join(re.findall(r"[a-z0-9]+",t.lower())); bw=re.findall(r"[a-z0-9]+",body.lower())
    miss=sum(1 for k in range(len(bw)-8) if " ".join(bw[k:k+8]) not in tw)
    secs=[h for h in ["## Beat map","## Why it works","## Script (verbatim, labelled)","## Doesn't transfer"] if h not in s]
    print(f"{os.path.basename(f):60} words {len(bw):5} / transcript {len(tw.split()):5}  missing8 {miss:3}  emdash {s.count(chr(8212))}  missingsections {secs}")
