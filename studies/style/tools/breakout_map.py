"""Build round2/BREAKOUT-MAP.md from round2/outliers-all.csv and channels-all.csv. Run from studies/style/."""
import csv, collections, statistics
o = list(csv.DictReader(open('round2/outliers-all.csv', encoding='utf-8')))
c = {x['channel_id']: x for x in csv.DictReader(open('round2/channels-all.csv', encoding='utf-8'))}
def ok(x, topic):
    ch = c.get(x['channel_id'], {})
    return (x['on_topic'] == topic and x['since_2022'] == 'yes' and x['long_form'] == 'yes'
            and x['channel_keep'] == 'yes' and ch.get('audience_check', '').startswith('pass'))
V = lambda x: float(x['views'] or 0)
R = lambda x: float(x['ratio_vs_normal']) if x['ratio_vs_normal'] not in ('', 'NA', 'None') else None
def fmt(v): return f'{v/1e6:.1f}M' if v >= 1e6 else f'{v/1e3:.0f}K'
out = []
P = out.append
core = [x for x in o if ok(x, 'core')]; adj = [x for x in o if ok(x, 'adjacent')]
P('# Breakout map (round 2, 2026-10-28)\n')
P('Built by `../tools/breakout_map.py` from `outliers-all.csv`. **What counts:**\n')
P('- outlier videos of 5:00 or longer, from 2022 on, on kept channels that pass the audience check (channels marked "partly" 50+, such as Blowout Professor, are left out of the map but stay in the data)')
P('- an outlier is a video at 2x or more its channel\'s NexLev average, from the 100 most recent uploads')
P('- views are NexLev\'s rounded counts; dates are approximate')
P('- angle and object come from **keyword rules on the title** (a first pass, not a reading of the video), so a few titles are misfiled; about 10% are "other"')
P('- ratio = views ÷ the channel\'s normal (median of its 15 latest long uploads); very high ratios come from tiny normals\n')
P(f'**{len(core)} core videos** (hair, fashion, accessories, color for women 50+) and **{len(adj)} adjacent** (makeup, skincare), on {len({x["channel_id"] for x in core})} channels.\n')
grp = lambda xs, g: [x for x in xs if x['group'] == g]
P('| | real | faceless / AI | unclear |\n|---|---:|---:|---:|')
P('| core videos | ' + ' | '.join(str(len(grp(core, g))) for g in ('real', 'faceless-ai', 'unclear')) + ' |')
P('| core videos at 500K+ | ' + ' | '.join(str(sum(V(x) >= 5e5 for x in grp(core, g))) for g in ('real', 'faceless-ai', 'unclear')) + ' |')
P('| core videos at 1M+ | ' + ' | '.join(str(sum(V(x) >= 1e6 for x in grp(core, g))) for g in ('real', 'faceless-ai', 'unclear')) + ' |\n')
def table(key, title):
    P(f'## {title}\n')
    P('| ' + key.title() + ' | videos | real | faceless/AI | 500K+ | median views | top video (channel, views) |\n|---|---:|---:|---:|---:|---:|---|')
    by = collections.defaultdict(list)
    for x in core: by[x[key]].append(x)
    for k, xs in sorted(by.items(), key=lambda kv: -len(kv[1])):
        top = max(xs, key=V)
        P(f"| {k} | {len(xs)} | {len(grp(xs,'real'))} | {len(grp(xs,'faceless-ai'))} | {sum(V(x)>=5e5 for x in xs)} | {fmt(statistics.median(V(x) for x in xs))} | {top['title'][:70].replace('|','/')} ({top['channel_name']}, {fmt(V(top))}) |")
    P('')
table('angle', 'By angle (what the title promises)')
table('object', 'By object (what the video is about)')
P('## Angle × object (core videos; cells with 5+ videos)\n')
cell = collections.defaultdict(list)
for x in core: cell[(x['angle'], x['object'])].append(x)
P('| Angle | Object | videos | real | faceless/AI | median views | best (channel, views) |\n|---|---|---:|---:|---:|---:|---|')
for (a, b), xs in sorted(cell.items(), key=lambda kv: -len(kv[1])):
    if len(xs) < 5: continue
    top = max(xs, key=V)
    P(f"| {a} | {b} | {len(xs)} | {len(grp(xs,'real'))} | {len(grp(xs,'faceless-ai'))} | {fmt(statistics.median(V(x) for x in xs))} | {top['title'][:60].replace('|','/')} ({top['channel_name']}, {fmt(V(top))}) |")
P('')
for g, lab in (('real', 'real women on camera'), ('faceless-ai', 'faceless and AI channels')):
    P(f'## The 30 biggest core videos: {lab}\n')
    P('| # | Channel | Title | Views | Ratio | Angle | Object |\n|---:|---|---|---:|---:|---|---|')
    for i, x in enumerate(sorted(grp(core, g), key=V, reverse=True)[:30], 1):
        r = R(x)
        P(f"| {i} | {x['channel_name']} | {x['title'][:80].replace('|','/')} | {fmt(V(x))} | {f'{r:.0f}x' if r else ''} | {x['angle']} | {x['object']} |")
    P('')
P('## Channels with the most core breakouts\n')
P('| Channel | Type | Subscribers | Normal | Core outliers | 500K+ | Best |\n|---|---|---:|---:|---:|---:|---|')
bych = collections.defaultdict(list)
for x in core: bych[x['channel_id']].append(x)
for cid, xs in sorted(bych.items(), key=lambda kv: (-sum(V(x) >= 5e5 for x in kv[1]), -len(kv[1])))[:40]:
    ch = c[cid]; top = max(xs, key=V)
    P(f"| {ch['channel_name']} | {ch['type']} | {ch['subscribers']} | {ch['normal']} | {len(xs)} | {sum(V(x)>=5e5 for x in xs)} | {top['title'][:55].replace('|','/')} ({fmt(V(top))}) |")
open('round2/BREAKOUT-MAP.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('written', len(out), 'lines')
