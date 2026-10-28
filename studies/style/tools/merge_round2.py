"""Merge the round-2 helpers' files into round2/channels-all.csv and round2/outliers-all.csv,
and tag every outlier with an angle and an object from its title (first pass, keyword rules).
Run from studies/style/: python3 -I tools/merge_round2.py"""
import csv, glob, re, collections, statistics

# Main-session audience calls on channels that pass the numbers (from the helpers' reports, 2026-10-28).
AUDIENCE = {
    'fail': {"WISE ELDER'S INSIGHT": 'retirement money', 'Historias de Adobe': 'drama stories since mid-October 2026',
             'Loya the Fashion Queen': 'general and celebrity trends', 'Prime of your life': 'menopause nutrition',
             'Whispers Fashion & Styles': 'switched to Old West stories in September 2026',
             'Older Line Podcast With Penelope': 'posed photos in stockings and short dresses, framed as 50+ fashion (helper 4 reading; against the niche hard rule on suggestive framing)',
             'Only Fame': 'hosiery photo compilations of named women (helper 1: all outliers off)',
             '10 Years Younger': 'TV makeover show built on cosmetic surgery (all outliers off)',
             'Tina Yong': 'no mature-skin content in the newest 30 videos',
             'Feminine Over 50 With Mia': 'posed photos in stockings and short dresses, framed as 50+ fashion (helper 4 reading; against the niche hard rule on suggestive framing)'},
    'partly': {'All Fashion Milano': 'street style, no age marker', 'Curiosity Street Style': 'street style, no age marker',
               'Lisa Eldridge': 'broad makeup', 'Style With Serena': 'one "over 40" hit', 'Glam Guide': 'one 3:39 over-50 compilation', 'Hindash': 'male artist on models; one mature-skin title', 'Blowout Professor': 'broad haircare, no age marker'},
}
GROUP = {'real_on_camera': 'real', 'faceless_narrated': 'faceless-ai', 'ai_avatar': 'faceless-ai', 'ai_clone': 'faceless-ai'}

ANGLES = [  # first match wins, so the order matters
    ('national lens', r'\b(french|parisian|paris|italian|japanese|korean|european|british|old money|scandinavian|german)\b'),
    ('makeover / transformation', r'makeover|transform|speechless|before (and|&) after|made her look|look what|she (just )?wanted|her (husband|daughter)|speechless|fine at \d\d'),
    ('mistakes / stop / never', r'mistake|\bstop\b|never|avoid|don.?t|ditch|outdated|out of style|retire|worst|wrong|aging you|age you|ages you|aging (black )?women|old lady|granny|frumpy|dated|cheap|scream|leave behind|instead|sloppy|ruin|throw out|remove|declutter|regret|look larger|grandma|should not|not have'),
    ('personal story / journey', r'journey|story|\bi (quit|colou?red|stopped|tried)|years in|\bmy\b|finding the'),
    ('truths / why explainer', r'truth|\bwhy\b|brutal|nobody talks|reveals|what.?s (actually|really)|happening|scam|levels of|icons?\b'),
    ('comparison / which one', r'\bvs\.?\b|which one|beat the|or\b.*\?'),
    ('look younger', r'younger|years off|youthful|anti.?ag'),
    ('look expensive / elegant', r'expensive|rich\b|wealthy|classy|elegan|chic|luxur|polished|sophisticat|stunning|beautiful|gorgeous|turn heads|timeless'),
    ('slimmer / body shape / face shape', r'slim|tummy|belly|apple|pear|petite|plus.?size|curv|heavy|body (shape|type)|figure|hide|face shape|round face|taller|flatter'),
    ('product picks / reviews / dupes', r'dupe|drugstore|worth it|review|first impression|tried|tested|products|brand|amazon|walmart|target|h&m|zara|chico|picks|haul|favorites|budget'),
    ('trends / season', r'trend|20\d\d|\b(fall|autumn|winter|spring|summer)\b|this season'),
    ('how-to technique / DIY', r'how to (cut|blend|curl|colou?r|cover|fix|style|tie|do|wear|find|dress|choose|pick|build|create|re-?create)|at home|diy|tutorial|step by step|ways to|blend|cover gr[ae]y'),
    ('best / only / must-have list', r'\bbest\b|\bonly\b|must|essential|need|rules|secrets|tricks|tips|hacks|things|ideas|outfits'),
    ('outfit ideas / lookbook', r'lookbook|collection|inspiration|what i (actually )?wear|ootd|get ready'),
]
OBJECTS = [
    ('gray hair', r'gr[ae]y hair|silver hair|going gr[ae]y|white hair'),
    ('thin / fine hair', r'\bthin\b|thinning|fine hair|fine/|/fine|volume|thick'),
    ('haircut / hairstyle', r'hair|bob\b|pixie|bangs|layers|shag|cut\b|cuts\b'),
    ('makeup', r'makeup|eyeliner|mascara|concealer|lipstick|\blips?\b|eyebrow|\bbrows?\b|blush|hooded'),
    ('skincare', r'\bskin\b|skincare|wrinkle|serum|cream|retinol|castor|jowl|crepey'),
    ('glasses', r'glasses|eyewear|frames'),
    ('jewelry', r'jewel|necklace|earring|pearl|\brings?\b|bracelet'),
    ('shoes', r'shoe|sneaker|boot|heel|sandal|loafer|flats'),
    ('bags', r'\bbag|handbag|purse'),
    ('scarf', r'scarf|scarves'),
    ('jeans / pants / leggings', r'jean|denim|pants|trouser|legging'),
    ('tops / blouses', r'blouse|top\b|tops\b|shirt|sweater|cardigan'),
    ('dresses / skirts', r'dress|skirt'),
    ('jackets / coats', r'jacket|coat|blazer|trench'),
    ('colors', r'colou?r'),
    ('whole look / wardrobe', r'wardrobe|outfit|style|fashion|look|wear|cloth'),
]
def tag(title, table):
    t = title.lower()
    for name, rx in table:
        if re.search(rx, t): return name
    return 'other'
def secs(l):
    p = [int(x) for x in re.findall(r'\d+', l or '')]
    return sum(v * 60 ** i for i, v in enumerate(reversed(p))) if p else None
def num(s):
    try: return float(s)
    except: return None

chans = []
for f in sorted(glob.glob('round2/channels-[0-9].csv')):
    for x in csv.DictReader(open(f, newline='', encoding='utf-8')):
        x['helper'] = f[-5]
        name = x['channel_name'].strip()
        aud = next((k for k, d in AUDIENCE.items() if name in d), 'pass')
        x['audience_check'] = aud + (': ' + AUDIENCE[aud][name] if aud != 'pass' else '')
        x['group'] = GROUP.get(x['type'].strip(), 'unclear')
        x['final_keep'] = 'yes' if x['keep'].strip().lower() == 'yes' and aud != 'fail' else 'no'
        chans.append(x)
byid = {c['channel_id']: c for c in chans}
outs, seen = [], set()
for f in sorted(glob.glob('round2/outliers-[0-9].csv')):
    for x in csv.DictReader(open(f, newline='', encoding='utf-8')):
        if x['video_id'] in seen: continue
        seen.add(x['video_id']); c = byid.get(x['channel_id'], {})
        x['group'] = c.get('group', ''); x['type'] = c.get('type', ''); x['channel_keep'] = c.get('final_keep', '')
        s = secs(x['length']); x['seconds'] = s or ''; x['long_form'] = 'yes' if s and s >= 300 else 'no'
        x['angle'] = tag(x['title'], ANGLES); x['object'] = tag(x['title'], OBJECTS)
        outs.append(x)
cc = list(chans[0].keys()); oc = list(outs[0].keys())
csv.DictWriter(open('round2/channels-all.csv', 'w', newline='', encoding='utf-8'), fieldnames=cc).writeheader()
w = csv.DictWriter(open('round2/channels-all.csv', 'a', newline='', encoding='utf-8'), fieldnames=cc); w.writerows(chans)
w = csv.DictWriter(open('round2/outliers-all.csv', 'w', newline='', encoding='utf-8'), fieldnames=oc); w.writeheader(); w.writerows(outs)
print('channels', len(chans), 'final keep', sum(c['final_keep'] == 'yes' for c in chans))
print(collections.Counter((c['group']) for c in chans if c['final_keep'] == 'yes'))
print('outliers', len(outs))
