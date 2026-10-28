import json, re, time, urllib.request, urllib.parse, difflib
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36', 'Accept-Language': 'en-US,en;q=0.9'}
def get(url):
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
        except Exception as e:
            err = e; time.sleep(2 * (i + 1))
    raise err
def blob(html, name):
    m = re.search(r'(?:var |window\["?)' + name + r'"?\]?\s*=\s*', html)
    if not m: return None
    dec = json.JSONDecoder()
    obj, _ = dec.raw_decode(html[m.end():])
    return obj
def walk(o, key):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key: yield v
            yield from walk(v, key)
    elif isinstance(o, list):
        for v in o: yield from walk(v, key)
def txt(x):
    if not x: return ''
    if 'simpleText' in x: return x['simpleText']
    return ''.join(r.get('text', '') for r in x.get('runs', []))
def search(q):
    html = get('https://www.youtube.com/results?search_query=' + urllib.parse.quote(q))
    d = blob(html, 'ytInitialData'); out = []
    for v in walk(d, 'videoRenderer'):
        own = v.get('ownerText', {}).get('runs', [{}])[0]
        out.append({'videoId': v.get('videoId'), 'title': txt(v.get('title')), 'channel': own.get('text', ''),
                    'channelId': own.get('navigationEndpoint', {}).get('browseEndpoint', {}).get('browseId', ''),
                    'views_text': txt(v.get('viewCountText')), 'published_text': txt(v.get('publishedTimeText')), 'length': txt(v.get('lengthText'))})
    return out
def watch(vid):
    html = get('https://www.youtube.com/watch?v=' + vid)
    p = blob(html, 'ytInitialPlayerResponse') or {}
    vd = p.get('videoDetails', {}); mf = p.get('microformat', {}).get('playerMicroformatRenderer', {})
    return {'videoId': vid, 'title': vd.get('title', ''), 'channel': vd.get('author', ''), 'channelId': vd.get('channelId', ''),
            'views': vd.get('viewCount', ''), 'seconds': vd.get('lengthSeconds', ''), 'publishDate': mf.get('publishDate', '')[:10],
            'category': mf.get('category', ''), 'description': vd.get('shortDescription', ''),
            'captions': [c.get('languageCode') + (':asr' if c.get('kind') == 'asr' else '') for c in p.get('captions', {}).get('playerCaptionsTracklistRenderer', {}).get('captionTracks', [])]}
def sim(a, b):
    n = lambda s: re.sub(r'[^a-z0-9 ]', '', s.lower())
    return difflib.SequenceMatcher(None, n(a), n(b)).ratio()
