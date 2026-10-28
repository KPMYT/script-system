import sys, csv, re, time, json
sys.path.insert(0, sys.argv[3]); import ytlib
src, out = sys.argv[1], sys.argv[2]
items, sec, seen = [], None, set()
for line in open(src, encoding='utf-8'):
    line = line.rstrip('\n')
    if line.startswith('## '): sec = line[3:].strip().lower(); continue
    if not line.strip() or line.startswith('#'): continue
    q = re.sub(r'\s*-\s*YouTube\s*$', '', line).strip()
    key = (sec, re.sub(r'\W+', '', q.lower()))
    if key in seen: continue
    seen.add(key); items.append((sec, line, q))
rows = []
for sec, raw, q in items:
    m = re.search(r'watch\?v=([\w-]{11})', q)
    row = {'section': sec, 'pasted': raw, 'match': '', 'score': '', 'videoId': '', 'title': '', 'channel': '', 'channelId': '', 'views': '', 'published': '', 'length': '', 'note': ''}
    try:
        if m:
            vid = m.group(1)
            res = ytlib.search(vid)
            hit = next((r for r in res if r['videoId'] == vid), None)
            if not hit:
                o = json.loads(ytlib.get(f'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json'))
                res = ytlib.search(o['title'] + ' ' + o['author_name'])
                hit = next((r for r in res if r['videoId'] == vid), None) or {'videoId': vid, 'title': o['title'], 'channel': o['author_name']}
            row.update({k: hit.get(k, '') for k in ['videoId', 'title', 'channel', 'channelId']}); row['match'] = 'url'; row['score'] = '1.00'
        else:
            res = ytlib.search(q)[:20]
            t0 = q.split(' | ')[0]; want = q.split(' | ')[1].lower() if ' | ' in q else ''
            vn = lambda r: int(re.sub(r'[^0-9]', '', r['views_text']) or 0)
            scored = [(ytlib.sim(t0, r['title']), r) for r in res]
            near = [(s_, r) for s_, r in scored if s_ >= 0.8]
            if want: named = [x for x in near if want.strip() in x[1]['channel'].lower()]
            else: named = []
            exact = [x for x in near if x[0] >= 0.97]
            pool = named or exact or near
            if pool: s, best = max(pool, key=lambda x: vn(x[1]))
            elif scored: s, best = max(scored, key=lambda x: x[0])
            else: s, best = 0, None
            if best:
                row.update({k: best[k] for k in ['videoId', 'title', 'channel', 'channelId']})
                row['score'] = f'{s:.2f}'; row['match'] = 'exact' if s >= 0.9 else 'close' if s >= 0.7 else 'weak'
                others = [r for s_, r in near if r['channelId'] != best['channelId']]
                row['note'] = (f"{len(others)} near-identical titles on other channels: " + '; '.join(f"{r['channel']} {vn(r)}" for r in others[:6])) if others else ''
                hit = best
            else: row['note'] = 'no results'; hit = {}
        row['views'] = re.sub(r'[^\d]', '', hit.get('views_text', '')) if hit else ''
        row['published'] = hit.get('published_text', ''); row['length'] = hit.get('length', '')
    except Exception as e:
        row['note'] = f'error: {e}'
    rows.append(row); print(row['match'], row['score'], row['views'], row['channel'], '|', row['title'][:60], flush=True)
    time.sleep(1.5)
with open(out, 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
