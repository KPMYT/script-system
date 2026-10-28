"""Builds notes/INDEX.md and transcripts-combined/ for the style study. Run from studies/style/: python3 -I tools/build_index.py"""
import csv, os, re
from pathlib import Path
m = {x['video_id']: x for x in csv.DictReader(open('comparison/measures.csv', encoding='utf-8'))}
rows, by = [], {}
for v in csv.DictReader(open('inputs/videos.csv', encoding='utf-8')):
    d = Path('data') / v['channel_slug'] / v['video_id']; meta = (d / 'meta.md').read_text(encoding='utf-8') if (d / 'meta.md').exists() else ''
    g = lambda k: (re.search(r'^- ' + k + r'[^:]*:\s*(.*)$', meta, re.M) or [None, ''])[1]
    note = f"{v['channel_slug']}__{v['video_id']}.md"; dropped = 'DROPPED' in v['why']
    rows.append(f"| {v['n']} | {v['group']} | {v['channel']} | {v['type']} | {v['title'][:70].replace('|','/')} | {g('Views').split(' (')[0]} | {g('Views / normal').split(' ')[0]} | {g('Duration').split(' ')[0]} | {m.get(v['video_id'], {}).get('words', '')} | " + ('dropped (not English)' if dropped else f'`{note}`') + ' |')
    if not dropped and (d / 'transcript.txt').exists():
        by.setdefault(v['channel_slug'], []).append((v, d))
out = ['# Style study: index', '', 'One line per study video, built by `../tools/build_index.py`. Views and multiples as collected on 2026-10-28; see each `meta.md`. Our own 38 videos are indexed in `../own-baseline-2026-10/SUMMARY.md`.', '',
       '| # | Group | Channel | Type | Title | Views | × normal | Length | Words | Notes |', '|---:|---|---|---|---|---:|---:|---:|---:|---|'] + rows
Path('notes/INDEX.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
os.makedirs('transcripts-combined', exist_ok=True)
for slug, vs in by.items():
    parts = [f"# {vs[0][0]['channel']}: combined transcripts ({len(vs)} videos)\n"]
    for v, d in vs:
        parts.append(f"\n---\n\n## {v['title']}\n\nVideo `{v['video_id']}` · group: {v['group']} · https://www.youtube.com/watch?v={v['video_id']}\n\n" + (d / 'transcript.txt').read_text(encoding='utf-8').strip() + '\n')
    Path(f'transcripts-combined/{slug}.md').write_text(''.join(parts), encoding='utf-8')
print(len(rows), 'rows;', len(by), 'combined files')
