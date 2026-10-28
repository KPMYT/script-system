"""Measure the style study's transcripts (the 45 study videos and our own 38).
Read-only on data/, own-baseline-2026-10/data/ and inputs/videos.csv. Writes comparison/00-measures.md
and comparison/measures.csv. Run from studies/style/: python3 -I tools/measure.py

How things are counted:
- Words: tokens holding a letter or digit, from the transcript text with the [m:ss] stamp and
  bracket tags ([Music]) removed. Minutes: the meta.md duration.
- you = you/your/yours/yourself (and you're, you'll...); I = I/me/my/mine/myself (and I'm, I've...);
  but = the word "but". All per 1,000 words.
- Questions: "?" per 1,000 words, only where the track is punctuated (20+ full stops per 1,000 words).
- Age said: "over/after/at/past/in your" + 40-80 (digits or words), plus "women our age", "mature women",
  "older women", "a certain age". Shame words: old lady, granny, grandma, frumpy, dowdy, invisible.
  Reassurance words: "nothing wrong with you", "you deserve", "beautiful at any age", "it's not your fault",
  "you are not", "give yourself permission". CTA words: subscribe, "comment"/"comments", "like this video",
  "link", "description", "bell", "share".
- First 30 s: the words in segments starting before 0:30.
"""
import csv, re, statistics as st
from pathlib import Path
R = Path('.')
def secs(t):
    p = [int(x) for x in re.findall(r'\d+', t)]
    return sum(v * 60 ** i for i, v in enumerate(reversed(p)))
def load(meta, tx):
    m = meta.read_text(encoding='utf-8'); d = re.search(r'Duration[^:]*:\s*([\d:]+)', m)
    lines = tx.read_text(encoding='utf-8').splitlines(); segs = []
    for l in lines:
        mm = re.match(r'\[(\d+:\d+(?::\d+)?)\]\s*(.*)', l)
        if mm: segs.append((secs(mm.group(1)), re.sub(r'\[[^\]]*\]', ' ', mm.group(2))))
    return (secs(d.group(1)) if d else None), segs
N = r'(?:4|5|6|7|8)0s?|forty|fifty|sixty|seventy|eighty'
AGE = re.compile(r"\b(?:over|after|at|past|in your)\s+(?:the age of\s+)?(?:" + N + r")\b|\bwomen (?:of )?our age\b|\bmature wom[ae]n\b|\bolder wom[ae]n\b|\ba certain age\b", re.I)
SHAME = re.compile(r'\bold lad(?:y|ies)\b|\bgrann(?:y|ies)\b|\bgrandma\b|\bfrumpy\b|\bdowdy\b|\binvisible\b', re.I)
REASS = re.compile(r"nothing (?:is )?wrong with you|you deserve|beautiful at any age|(?:it'?s|it is) not your fault|you are not (?:too old|invisible|alone)|permission", re.I)
CTA = re.compile(r'\bsubscrib\w*|\bcomments?\b|\blike this video\b|\blink\b|\bdescription\b|\bbell\b|\bshare\b', re.I)
def measure(segs, dur):
    text = ' '.join(s for _, s in segs); words = [w for w in text.split() if re.search(r'[A-Za-z0-9]', w)]
    n = len(words) or 1; low = text.lower(); per = lambda c: round(c * 1000 / n, 1)
    punct = text.count('.') * 1000 / n >= 20
    return dict(words=len(words), minutes=round(dur / 60, 1) if dur else '', wpm=round(len(words) / (dur / 60)) if dur else '',
        you=per(len(re.findall(r"\byou(?:r|rs|rself|'re|'ll|'ve|'d)?\b", low))), i=per(len(re.findall(r"\b(?:i|me|my|mine|myself|i'm|i've|i'll|i'd)\b", low))),
        but=per(len(re.findall(r'\bbut\b', low))), q=(per(text.count('?')) if punct else 'unpunct.'),
        age=len(AGE.findall(text)), shame=len(SHAME.findall(text)), reassure=len(REASS.findall(text)), cta=len(CTA.findall(text)),
        first30=sum(len(s.split()) for t, s in segs if t < 30))
rows = []
for v in csv.DictReader(open('inputs/videos.csv', encoding='utf-8')):
    if 'DROPPED' in v['why']: continue
    d = R / 'data' / v['channel_slug'] / v['video_id']
    if not (d / 'transcript.txt').exists(): continue
    dur, segs = load(d / 'meta.md', d / 'transcript.txt')
    side = 'real' if v['type'] == 'real' else 'faceless/AI'
    if v['group'].startswith('Pair'): side = 'pair-' + ('winner' if v['why'].startswith('the winner') else 'copy')
    rows.append(dict(side=side, group=v['group'], channel=v['channel'], video_id=v['video_id'], title=v['title'][:70], **measure(segs, dur)))
for d in sorted((R / 'own-baseline-2026-10' / 'data').glob('*/*')):
    if not (d / 'transcript.txt').exists(): continue
    dur, segs = load(d / 'meta.md', d / 'transcript.txt'); title = (d / 'meta.md').read_text(encoding='utf-8').split('\n', 1)[0].lstrip('# ')
    rows.append(dict(side='own: ' + d.parent.name, group='own', channel=d.parent.name, video_id=d.name, title=title[:70], **measure(segs, dur)))
keys = ['words', 'minutes', 'wpm', 'you', 'i', 'but', 'q', 'age', 'shame', 'reassure', 'cta', 'first30']
with open('comparison/measures.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
out = ['# Measures: the study videos and our own (generated)', '', 'Built by `../tools/measure.py`; how each figure is counted is in the script\'s header. Per-video rows are in `measures.csv`. "unpunct." means the caption track has no punctuation, so questions can\'t be counted.', '',
       '## Medians by side', '', '| Side | Videos | ' + ' | '.join(keys) + ' |', '|---|---:|' + '---:|' * len(keys)]
for side in ['real', 'faceless/AI', 'pair-winner', 'pair-copy', 'own: scarlet-sterling', 'own: diane-de-chambray']:
    xs = [r for r in rows if r['side'] == side]
    if not xs: continue
    med = lambda k: (st.median([r[k] for r in xs if isinstance(r[k], (int, float))]) if any(isinstance(r[k], (int, float)) for r in xs) else '')
    out.append(f'| {side} | {len(xs)} | ' + ' | '.join(str(round(med(k), 1)) if med(k) != '' else '' for k in keys) + ' |')
out += ['', '## Every video', '', '| Side | Channel | Title | ' + ' | '.join(keys) + ' |', '|---|---|---|' + '---:|' * len(keys)]
for r in rows: out.append(f"| {r['side']} | {r['channel']} | {r['title'].replace('|','/')} | " + ' | '.join(str(r[k]) for k in keys) + ' |')
Path('comparison/00-measures.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(rows), 'videos measured')
