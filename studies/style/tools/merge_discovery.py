import csv, sys, collections, re
raw, out = sys.argv[1], sys.argv[2]
lanes_files = ['fashion','hair','french-makeup','faceless-ai']
rows = collections.defaultdict(list)
for f in lanes_files:
    for x in csv.DictReader(open(f'{raw}/{f}.csv', newline='')):
        x['_src'] = f
        rows[x['channel_id'].strip()].append(x)

def num(s):
    s = (s or '').replace(',', '').strip()
    m = re.match(r'^~?(\d+(?:\.\d+)?)', s)
    return float(m.group(1)) if m else None

def group(t):
    return {'real_on_camera':'real','faceless_narrated':'faceless-ai','ai_avatar':'faceless-ai','ai_clone':'faceless-ai'}.get(t, 'unclear')

def tier(v):
    if v is None: return 'unknown'
    return 'A 1M+' if v >= 1e6 else 'B 300K-1M' if v >= 3e5 else 'C 100K-300K' if v >= 1e5 else 'D under 100K'

cols = ['channel_name','handle','channel_id','url','country','subscribers','group','type','type_readings','lanes','audience_fit',
        'best_video_views','tier','top1_title','top1_views','top1_date','top2_title','top2_views','top2_date','top3_title','top3_views','top3_date',
        'last_upload','uploads_last_90d','est_monthly_revenue','rpm_est','nexlev_faceless','found_in','data_gaps','notes']
master = []
for cid, rs in rows.items():
    filled = lambda x: sum(1 for v in x.values() if str(v).strip())
    base = max(rs, key=filled)
    types = collections.Counter(r['type'].strip() for r in rs if r['type'].strip())
    tset = sorted(types)
    if len(tset) == 1: typ = tset[0]
    else:
        specific = [t for t in tset if t not in ('unclear','mixed')]
        typ = specific[0] if len(specific) == 1 else 'disputed'
    vids = {}
    for r in rs:
        for i in (1,2,3):
            t = r[f'top{i}_title'].strip(); v = num(r[f'top{i}_views'])
            if not t: continue
            k = re.sub(r'\W+', '', t.lower())[:60]
            if k not in vids or (v or 0) > (vids[k][1] or 0):
                vids[k] = (t, v, r[f'top{i}_date'].strip())
    top = sorted(vids.values(), key=lambda z: -(z[1] or 0))[:3]
    subs = max((num(r['subscribers']) or 0 for r in rs), default=0)
    best = top[0][1] if top else None
    pick = lambda k: next((r[k].strip() for r in sorted(rs, key=filled, reverse=True) if r[k].strip()), '')
    gaps = []
    if len(top) < 3: gaps.append(f'top videos {len(top)}/3')
    lu = pick('uploads_last_90d')
    if not lu or lu.startswith('n/a'): gaps.append('uploads_last_90d')
    if any('approx' in (r['top1_views']+r['top1_date']+r['notes']).lower() or '~' in r['top1_date'] for r in rs): gaps.append('approx views/dates')
    m = {
        'channel_name': base['channel_name'], 'handle': pick('handle'), 'channel_id': cid, 'url': pick('url'), 'country': pick('country'),
        'subscribers': int(subs) if subs else '', 'type': typ, 'group': group(typ) if typ != 'disputed' else 'unclear',
        'type_readings': '; '.join(f"{r['_src']}: {r['type']} ({r['type_basis'][:120]})" for r in rs),
        'lanes': ' | '.join(sorted({r['lane'].strip() for r in rs if r['lane'].strip()})),
        'audience_fit': ' | '.join(sorted({r['audience_fit'].strip() for r in rs if r['audience_fit'].strip()})),
        'best_video_views': int(best) if best else '', 'tier': tier(best),
        'last_upload': pick('last_upload'), 'uploads_last_90d': lu, 'est_monthly_revenue': pick('est_monthly_revenue'),
        'rpm_est': pick('rpm_est'), 'nexlev_faceless': ' | '.join(sorted({r['nexlev_faceless'].strip() for r in rs if r['nexlev_faceless'].strip()})),
        'found_in': ', '.join(r['_src'] for r in rs), 'data_gaps': '; '.join(gaps),
        'notes': ' || '.join(f"[{r['_src']}] {r['notes'].strip()}" for r in rs if r['notes'].strip()),
    }
    for i in (1,2,3):
        t = top[i-1] if len(top) >= i else ('', None, '')
        m[f'top{i}_title'], m[f'top{i}_views'], m[f'top{i}_date'] = t[0], (int(t[1]) if t[1] else ''), t[2]
    master.append(m)
order = {'real':0,'faceless-ai':1,'unclear':2}
master.sort(key=lambda m: (order[m['group']], -(m['best_video_views'] or 0)))
with open(out, 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(master)
c = collections.Counter((m['group'], m['tier']) for m in master)
print(len(master)); [print(k, v) for k, v in sorted(c.items())]
print('disputed', sum(1 for m in master if m['type']=='disputed'))
print('lanes', collections.Counter(l for m in master for l in m['lanes'].split(' | ')))
