"""Builds notes/INDEX.md and transcripts-combined/ from data/*/*/meta.md and transcript.txt.
Usage (from studies/hvac): python3 tools/build_index.py"""
import os, re, glob
rows, by_ch = [], {}
def field(s, name):
    m = re.search(r'^- ' + re.escape(name) + r':\s*(.*)$', s, re.M); return m.group(1).strip() if m else ''
for meta in sorted(glob.glob('data/*/*/meta.md')):
    slug, vid = meta.split('/')[1:3]; s = open(meta, encoding='utf8').read()
    title = s.split('\n', 1)[0].lstrip('# ').strip().replace('|', '\\|')
    ch = field(s, 'Channel').split(' (')[0]; vtype = re.sub(r'\s*\(.*', '', field(s, 'Video type'))
    dur = field(s, 'Duration').split(' ')[0]; views = re.sub(r'[^\d]', '', field(s, 'Views').split(' ')[0])
    mult = field(s, 'Views / normal').split(' ')[0]; fmt = field(s, 'Format').split(' (')[0].split('.')[0].split(',')[0].strip()
    tx = f'data/{slug}/{vid}/transcript.txt'; has_tx = os.path.exists(tx) and os.path.getsize(tx) > 100
    note = f'{slug}__{vid}.md'; has_note = os.path.exists('notes/' + note)
    rows.append((ch, vid, title, vtype, dur, f'{int(views):,}' if views else '', mult, fmt, has_tx, note if has_note else 'no notes (no transcript)'))
    if has_tx: by_ch.setdefault(slug, []).append((title, vid, ch, dur, views, mult, tx))
out = ['# HVAC study: index', '', 'One line per video, built by `tools/build_index.py` from the meta files. Views and multiples as of the collection date (2026-10-27); the multiple is views divided by the channel normal (see each meta.md).', '',
       '| Channel | Video ID | Title | Type | Length | Views | × normal | Format | Notes |', '|---|---|---|---|---|---|---|---|---|']
for r in rows: out.append(f'| {r[0]} | `{r[1]}` | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | {"`"+r[9]+"`" if r[9].endswith(".md") else r[9]} |')
open('notes/INDEX.md', 'w', encoding='utf8').write('\n'.join(out) + '\n')
os.makedirs('transcripts-combined', exist_ok=True)
for slug, vids in by_ch.items():
    parts = [f'# {vids[0][2]}: combined transcripts ({len(vids)} videos)\n']
    for title, vid, ch, dur, views, mult, tx in vids:
        parts.append(f'\n---\n\n## {title}\n\nVideo `{vid}` · {dur} · {int(views):,} views · {mult}x normal · https://www.youtube.com/watch?v={vid}\n\n' + open(tx, encoding='utf8').read().strip() + '\n')
    open(f'transcripts-combined/{slug}.md', 'w', encoding='utf8').write(''.join(parts))
print(len(rows), 'videos,', sum(r[8] for r in rows), 'with transcripts,', len(by_ch), 'combined files')
