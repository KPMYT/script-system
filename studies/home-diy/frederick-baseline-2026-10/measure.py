import re, sys, glob, os
d = sys.argv[1]
W = lambda s: re.findall(r"[A-Za-z0-9$']+", s)
def per(n, w): return round(n * 1000 / max(w, 1), 1)
rows = []
for f in sorted(glob.glob(os.path.join(d, "NEW-*.txt"))):
    t0 = open(f).read().replace("\\===", "===")
    tags = len(re.findall(r"\\?\[[a-z ,-]+\\?\]", t0))
    t = re.sub(r"\\?\[[a-z ,-]+\\?\]\s*", "", t0)
    t = t.replace("\u2019", "'")
    ctas = re.findall(r"===START CTA.*?===(.*?)===END CTA===", t, re.S)
    spoken = re.sub(r"===START CTA.*?===|===END CTA===", "", t)
    words = W(spoken); n = len(words)
    body = re.sub(r"===START CTA.*?===.*?===END CTA===", "", t, flags=re.S)
    low = spoken.lower()
    sents = [s for s in re.split(r"(?<=[.!?])\s+", spoken.strip()) if W(s)]
    lens = [len(W(s)) for s in sents]
    short = sum(1 for l in lens if l <= 6)
    you = len(re.findall(r"\byou(?:r|rs|rself|'re|'ll|'ve|'d)?\b", low))
    i_ = len(re.findall(r"\b(?:i|me|my|i'm|i've|i'd|i'll)\b", low))
    first_person_anec = len(re.findall(r"\bi(?:'ve| once| pulled| knelt| watched| opened| found| saw| put)\b", low))
    q = spoken.count("?")
    but = len(re.findall(r"\bbut\b", low))
    nums = len(re.findall(r"\$?\d[\d,.]*", spoken))
    intro = bool(re.search(r"i'm frederick barnes[,.]", low[:1500]))
    first_num = re.search(r"\bnumber (one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen)\b", low)
    w_before = len(W(spoken[:first_num.start()])) if first_num else None
    cta_w = [len(W(c)) for c in ctas]
    pos = None
    if ctas:
        idx = t.find("===START CTA"); pos = round(len(W(re.sub(r"===.*?===", "", t[:idx]))) / n * 100)
    fire_words = len(re.findall(r"\b(?:die|dies|died|death|deaths|kill|killed|kills|burn(?:s|ed|ing)? down|trapped|smoke|flames?|fatal|deadly)\b", low))
    firefighter = len(re.findall(r"\bfire ?fighters?\b|\bfire departments?\b|\bfire marshals?\b", low))
    rows.append((os.path.basename(f)[:-4], tags, n, round(n/165,1), per(you,n), per(i_,n), first_person_anec, q, per(but,n), round(sum(lens)/len(lens),1), round(short*100/len(lens)), nums, intro, w_before, "/".join(map(str,cta_w)), pos, per(fire_words,n), firefighter))
hdr = ["script","voice tags","words","min@165","you/1k","I/1k","I-anecdotes","?","but/1k","sent","<=6w%","digits","intro","words_before_#1","CTA words","midCTA@%","dread/1k","firefighter refs"]
print(" | ".join(hdr))
for r in rows: print(" | ".join(str(x) for x in r))
