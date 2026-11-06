#!/usr/bin/env python3
"""The hard-rules check for plumbing scripts (P21, the simple way).

Usage:
    python3 check.py SCRIPT --channel roger|mark|vintage|werner --title "LOCKED TITLE" --brief BRIEF [--models DIR] [--prices FILE]

It checks only hard rules and never asks for a line to be added to meet a count:
length at the channel's real speed, the CTA and the ending for the channel's
script type (Classic: no markers; Talking Head: two marker blocks), banned
lines, the safety requirements, prices against the brief and the price guide,
the voice, lists in the opening, and copying from a model.
FAIL lines must be fixed; INFO lines are for reading only.
The last line is "RESULT: PASS" or "RESULT: FAIL (n)".

Not checked, on the operator's word (2026-10-21, "dont even flag them"): boiling
water and dry washing soda. The brief wins on safety; the page carries the defaults.
"""
import argparse
import math
import os
import re
import sys

MAX_SENTENCE = 35
COPY_RUN = 8                    # words in a row shared with a model
SWEET_MAX_MINUTES = 20

CONTRACTION = r"\b\w+(?:n't|'re|'ve|'ll|'d|'m)\b|\b(?:it|that|there|here|what|he|she|who|let|where|how|why|when|nothing|something)'s\b"
COMMENT_END = r"\bI read every ?one\b"

CHANNELS = {
    "roger": {
        "name": "Roger the Pipe Guy", "wpm": 170, "type": "classic", "mid": True, "end": "book",
        "spoken": r"one hundred old[- ]house fixes that save you thousands",
        "tenure": 45, "contractions": True,
        "facts": {100, 16, 6},
        "ban": [
            (r"\broger the hvac guy\b|\bmy (?:hvac|heating) channel\b", "the other Roger channel (the two never mention each other)"),
            (r"\bhere(?:'?s| is) the part (?:people skip|nobody tells you)\b", "a stock line ('here's the part people skip')"),
        ],
        "once": [
            (r"\bfirst saturday\b", "his first-Saturday drain check"),
        ],
    },
    "mark": {
        "name": "Mark Silverbridge", "wpm": 181, "type": "classic", "mid": True, "end": "book",
        "spoken": r"fifty easy plumbing fixes that will save you ten thousand dollars",
        "tenure": 40, "contractions": False,
        "facts": {50, 10000, 10, 5},
        "ban": [
            (r"\bhere(?:'?s| is) the part (?:people skip|nobody tells you)\b", "a stock line ('here is the part people skip')"),
        ],
        "once": [],
    },
    "vintage": {
        "name": "The Vintage Pipefitter", "wpm": 190, "type": "classic", "mid": False, "end": "subscribe",
        "spoken": None,
        "tenure": 45, "contractions": True,
        "facts": set(),
        "ban": [
            (r"\buncle ray\b", "a named mentor (none)"),
            (r"\b(?:link in the description|QR code)\b|\bmy book\b", "a book pitch or a link (no book, no mid-video ask)"),
        ],
        "once": [
            (r"\bI'?ll tell you\b", "his aside 'I'll tell you'"),
            (r"\bnow here'?s the thing\b", "his aside 'now here's the thing'"),
            (r"\bhere(?:'?s| is) the part (?:people skip|nobody tells you)\b", "his aside 'here's the part people skip'"),
        ],
    },
    "werner": {
        "name": "Werner Finkbeiner", "wpm": 181, "type": "talking", "mid": True, "end": "book",
        "printed": "Werner's 101 Free Repairs",
        "spoken": r"werner'?s one hundred and one free repairs",
        "fixed": "My old mentor taught me this trade, and before he passed, I wrote down everything he showed me.",
        "tenure": 30, "contractions": False,
        "facts": {101, 12, 42, 51, 52, 61, 22, 31, 1, 11, 92},
        "ban": [
            (r"\bI(?:'m| am) Werner\b|\bmy name(?:'s| is) Werner\b|\bWerner Finkbeiner here\b", "a name intro"),
            (r"\bFinkbinder\b|\bFinkbiener\b|\bFinkbeimer\b|\bVerner\b", "a near-miss name"),
            (r"\beuros?\b", "a price in euros"),
            (r"\bBertha\b|\bMarcus\b|\bTexas\b", "the book's own stories"),
            (r"\bI once paid\b|\bninety-five dollars? to turn\b|\bthe first house I owned\b", "the book's own first-person stories"),
            (r"\bwhen I (?:came|moved|arrived) (?:to|in) (?:America|the States|the US|the United States)\b|\bmy first (?:year|winter|house|apartment) in (?:America|the States)\b", "an arrival story"),
            (r"\b(?:I grew up|back home|at home|my hometown|my village|where I come from) in (?:Munich|Berlin|Hamburg|Stuttgart|Cologne|Frankfurt|Bavaria|Swabia|the Black Forest|Saxony|Hesse)\b", "a hometown"),
            (r"\bmy (?:Meister|master'?s (?:certificate|exam|title)|apprenticeship|licen[cs]e|journeyman)\b", "a credential claim"),
            (r"\b(?:illegal|against the law|banned|forbidden) in Germany\b|\bGerman law (?:says|requires|forbids|bans)\b", "a German law claimed"),
            (r"\blederhosen\b|\boktoberfest\b|\bbratwurst\b|\bsauerkraut\b|\bdanke\b|\bja\b|\bnein\b|\bachtung\b|\bwunderbar\b", "comedy German or a national cliche"),
            (r"\bthe honest part I promised\b|\bthat number comes right after\b|\bat the very end, this same\b", "his old tease lines"),
            (r"\bthree small things for this week\b|\bthey were never separate (?:tricks|items|things)\b|\bhalfway,? and worth (?:one|a) look back\b", "his old recap moves"),
            (r"\bthe free in that name\b", "his old CTA line"),
            (r"\benough for today\b", "his old sign-off"),
            (r"\bhere(?:'?s| is) the part (?:people skip|nobody tells you)\b", "a stock line"),
        ],
        "once": [
            (r"\bFeierabend\b", "Feierabend"), (r"\bmy friend\b", "'my friend'"),
            (r"\bPfusch\b", "Pfusch"), (r"\bOrdnung\b", "Ordnung"),
        ],
    },
}

RELATIVES = r"\bmy (?:father|dad|mother|mom|papa|mama|grandfather|grandmother|grandpa|grandma|opa|oma|uncle|aunt|wife|husband|son|daughter|brother|sister|family|parents|kids)\b"
GERMAN_WORDS = ["Feierabend", "Ordnung", "Werkstatt", "Handarbeit", "Sparsamkeit", "Wartung", "Vorsorge", "Pfusch", "Werkzeug", "Hausmittel"]
WERNER_DETAILS = [
    (r"\bI grew up in Germany\b|\bgrowing up in Germany\b|\bthe way I (?:was|got) trained\b|\bhow I was trained\b", "his German upbringing or training"),
    (r"\bthe heating goes off\b|\bspring check\b", "his spring check"),
    (r"\bscrew tin\b|\btin (?:on|from) the shelf\b|\bin the tin\b", "the screw tin"),
]

COMMON_BAN = [
    (r"\btoday,? (?:we'?re|we are|I'?m|I am) going to\b|\bin (?:today'?s|this) video,? (?:I|we)(?:'ll| will|'m| am|'re| are) (?:going to )?(?:show|teach|cover|look)\b|\bwelcome (?:back|to) (?:the|my) channel\b|\bthis channel (?:is for|exists|is all about)\b|\bmy name(?:'s| is)\b", "a channel or name intro, or 'today we're going to'"),
    (r"\bstay (?:till|until|to) the (?:very )?end\b|\bstick (?:around|with me)\b|\bby the end of (?:this|the) video\b|\bstay tuned\b|\bcoming up (?:next|later|in this)\b|\bstill to come\b|\blater in (?:this|the) video\b|\bhang around\b|\bmake sure you watch\b|\bwait (?:for|till|until) the (?:end|last one)\b|\bbonus tip\b", "a tease"),
    (r"\b(?:to|let'?s|quick) recap\b|\bto sum (?:it )?up\b|\bin summary\b", "a recap"),
    (r"\bhomework\b", "a homework list (one small thing, never a list)"),
    (r"\bring the bell\b|\bbell icon\b|\bnotification bell\b|\blike button\b|\bthumbs up\b|\bhit (?:that )?like\b|\bshare this video\b", "a like, bell or share ask"),
    (r"\bI(?:'ve| have)? (?:tested|tried|ran (?:a |the |some |my )?tests?)\b|\bmy (?:own )?(?:test|tests|testing|results)\b|\bwatch me\b", "a first-person test or demonstration"),
    (r"\bas you can see\b|\byou can see (?:here|that|this|right)\b|\blook at this\b|\bright here\b|\blook at the \w+(?: \w+)? on the (?:left|right)\b|\bas we zoom in\b", "pointing at the screen"),
    (r"\bnot a scam\b|\bisn'?t the scam\b|\bjust (?:plain )?(?:economics|arithmetic)\b|\bno conspiracy\b|\bgrab it now or later\b|\byour (?:wallet|pipes) will thank you\b|\b(?:just )?(?:do not|don'?t) volunteer it\b|\bif (?:you'?re|you are) finding this helpful\b|\bif this is helping\b|\blet'?s (?:continue|keep going)\b|\bcommon problems you might run into\b", "a template stock line"),
    (r"\bif you (?:take|remember) (?:only )?one thing (?:home )?from this (?:whole )?video\b|\bif you do (?:only )?one thing from this video\b", "the stock priority line ('if you take one thing from this video')"),
    (r"\bhorror movie\b|\bbrutal (?:honest )?(?:tests?|truth)\b", "hype that got mocked"),
    (r"\bscam\b|\brip(?:ping)? you off\b|\bgreed\w*\b|\bpays? (?:his|their) mortgage\b|\bbecause they (?:want|make|need) (?:your )?money\b|\bnobody who gets paid\b", "the trade's motives (say the price and the silence, never why)"),
    (r"\b(?:a|one|this) (?:homeowner|customer|client|neighbou?r|lady|gentleman|family) (?:once |I knew )?(?:asked|told|called|showed|had)\b|\bI once (?:fixed|found|opened|saw)\b|\bmy (?:customers?|clients?)\b|\bI had a (?:homeowner|customer|client)\b|\bI got called to\b", "a customer or job story"),
    (r"\bstudies show\b|\bresearch shows\b|\b(?:experts|scientists) say\b", "'studies show'"),
    (r"\be-?book\b", "'e-book' (say 'book')"),
    (r"\b(?:damn|dammit|hell|crap|shit|ass|bastard|pissed)\b", "swearing (none in plumbing)"),
    (r"\bnext video\b|\bupcoming video\b|\bin (?:a|my) (?:future|next|upcoming) video\b|\bsee you (?:next time|in the next)\b", "a future video"),
    (r"\blet me know if you\b", "a chatbot leftover ('let me know if you')"),
    (r"\bguarantee\w*\b", "a guarantee (never a guaranteed result or saving)"),
    (r"\bopen (?:the|all the|your) windows\b[^.!?]{0,60}\bgas\b|\bgas\b[^.!?]{0,60}\bopen (?:the|all the|your) windows\b|\bshut (?:it|the gas) off at the meter\b", "gas-leak advice the gas utilities don't give"),
    (r"\b(?:five|5) seconds\b[^.!?]{0,60}\b(?:burn|scald)\w*|\b(?:burn|scald)\w*\b[^.!?]{0,60}\b(?:five|5) seconds\b", "the scald time (about six seconds at 140 degrees, never five)"),
]
COMMON_ONCE = [
    (r"\bnine (?:times )?out of (?:10|ten)\b", "'nine times out of ten'"), (r"\bbetween you and me\b", "'between you and me'"),
    (r"\bask me how I know\b", "'ask me how I know'"), (r"\bI(?:'?ll| will) be (?:straight|square|honest) with you\b", "'I'll be straight with you'"),
    (r"\bthat(?:'?s| is) the whole (?:trick|method|job|game)\b", "'that's the whole trick'"), (r"\bin your pocket\b", "'in your pocket'"),
    (r"\bwhich (?:brings us|leaves)\b", "'which brings us'"), (r"\bhold that thought\b|\bput a pin in\b", "'hold that thought'"),
    (r"\bthe big one\b", "'the big one'"), (r"\bthe real kicker\b", "'the real kicker'"), (r"\bquick (?:thing|pause|one)\b", "'quick thing'"),
    (r"\bno shame in\b", "'no shame in'"), (r"\bfull stop\b", "'full stop'"), (r"\btrust me\b", "'trust me'"),
    (r"\babsolutely criminal\b", "'absolutely criminal'"), (r"\bhere'?s what (?:you|to) do\b|\bhere is what (?:you|to) do\b", "'here's what you do'"),
]
OPENING_BAN = [
    (r"\btoday,? (?:you(?:'ll| will)? (?:learn|see|find out)|I(?:'ll| will) show you|we(?:'ll| will) (?:learn|look at|fix))\b", "'today you learn'"),
    (r"\b(?:you(?:'ll| will)|I(?:'ll| will)|we(?:'ll| will))\b[^.!?]{0,40}\bin (?:the next )?(?:a few|two|three|five|ten|sixty|ninety|\d+) (?:minutes?|seconds?)\b", "a promise with a time on it"),
    (r"\bnumber (?!one\b)(?:two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|\d+) (?:is|can|will|saves?|costs?)\b", "a run-down of what a later item holds"),
]
OPENING_PROMISE = r"\byou(?:'ll| will) (?:hear|see|learn|know|find out|get)\b|\bI(?:'ll| will) (?:show|tell|teach|give)\b|\b(?:and|but) (?:that|this) comes (?:at|later)\b|\b(?:comes|is coming|waits) (?:at|in) the (?:last|final|end|very end)\b|\bcomes later\b"
NO_PLUMBER = r"\bnothing (?:here|in this (?:video|one)) needs a plumber\b|\bnone of this needs a plumber\b|\byou(?:'ll| will) never (?:need|call) a plumber\b|\bno plumber needed\b"
A_CALL = r"\bthat(?:'?s| is) a call\b|\bcall (?:a|the|your|in a) (?:plumber|pro|professional|licensed)\b|\bpick up the phone\b|\bcall someone\b|\bthen call\b"
ITEM_ONE = r"\b(?:number one|level one|step one|first up|the first (?:step|thing|fix|check|reason|cause|mistake|tip|level))\b"

UNITS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: 10 * (i + 2) for i, w in enumerate("twenty thirty forty fifty sixty seventy eighty ninety".split())}
SCALES = {"hundred": 100, "thousand": 1000, "million": 1000000}
NUMWORD = "|".join(list(UNITS) + list(TENS) + list(SCALES))


def numbers_in(text):
    """Every number in the text, from digits and from number words."""
    found = set()
    for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", text):
        try:
            found.add(int(float(m.group().replace(",", ""))))
        except ValueError:
            pass
    low = re.sub(r"\ba (hundred|thousand|million)\b", r"one \1", text.lower().replace("-", " "))
    tokens = re.findall(r"[a-z]+", low)
    cur, total, active = 0, 0, False
    for t in tokens + ["."]:
        if t in UNITS:
            cur += UNITS[t]; active = True
        elif t in TENS:
            cur += TENS[t]; active = True
        elif t in SCALES and active:
            if t == "hundred":
                cur = (cur or 1) * 100
            else:
                total += (cur or 1) * SCALES[t]; cur = 0
        elif t == "and" and active:
            continue
        else:
            if active:
                found.add(total + cur)
            cur, total, active = 0, 0, False
    return found


def norm_words(text):
    return re.findall(r"[a-z0-9']+", text.lower().replace("’", "'"))


def sentences(text):
    flat = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", flat) if s.strip()]


def sentence_with(text, start):
    left = max(text.rfind(".", 0, start), text.rfind("?", 0, start), text.rfind("!", 0, start), text.rfind("\n", 0, start))
    right = min([i for i in (text.find(".", start), text.find("?", start), text.find("!", start), text.find("\n", start)) if i != -1] or [len(text)])
    return re.sub(r"\s+", " ", text[left + 1:right + 1]).strip()[:160]


def paragraphs(text):
    return [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


MONEY_DIGITS = r"\$\s?\d[\d,]*(?:\.\d+)?(?:\s?(?:to|and|or|-)\s?\$?\s?\d[\d,]*(?:\.\d+)?)?(?:\s(?:thousand|million))?"
MONEY_WORDS = r"\b(?:(?:%s|a|and|to|or)(?:[- ]|\s+))*(?:%s)\s+(?:dollars?|bucks)\b" % (NUMWORD, NUMWORD)


def load_models(folder):
    """(name, transcript text, signature phrases) for every model file."""
    models = []
    if not folder or not os.path.isdir(folder):
        return models
    for fn in sorted(os.listdir(folder)):
        if not fn.endswith(".md"):
            continue
        raw = open(os.path.join(folder, fn), encoding="utf-8").read()
        body = raw.split("## Transcript", 1)[1] if "## Transcript" in raw else raw
        sig = []
        m = re.search(r"## Signature phrases[^\n]*\n(.*?)(?:\n## |\Z)", raw, re.S)
        if m:
            sig = [q for q in re.findall(r'"([^"]{8,})"', m.group(1))]
        models.append((fn, body, sig))
    return models


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--channel", required=True, choices=sorted(CHANNELS))
    ap.add_argument("--title", required=True)
    ap.add_argument("--brief", required=True)
    ap.add_argument("--models", default=os.path.join(here, "references", "models"))
    ap.add_argument("--prices", default=os.path.join(here, "references", "price-guide.md"))
    a = ap.parse_args()
    ch = CHANNELS[a.channel]
    raw = open(a.script, encoding="utf-8").read()
    brief = open(a.brief, encoding="utf-8").read()
    prices = open(a.prices, encoding="utf-8").read() if os.path.isfile(a.prices) else ""
    fails, infos = [], []

    def fail(rule, detail=""):
        fails.append(f"FAIL {rule}" + (f": {detail}" if detail else ""))

    if not prices:
        infos.append(f"INFO no price guide at {a.prices}: prices checked against the brief only")

    # Keep only the script if a whole output was pasted; drop a TEST label line.
    raw = re.sub(r"^\s*SCRIPT TYPE:[^\n]*\n", "", raw)
    raw = re.split(r"\n\s*(?:CHECK:|VO COPY)", raw)[0]
    raw = re.sub(r"^\s*TEST\b[^\n]*\n", "", raw)
    lines = raw.strip("\n").split("\n")

    # 1. Markers: Talking Head has two blocks; Classic has none.
    blocks, spoken_lines, inside, cur = [], [], False, None
    start_re = re.compile(r"^===START CTA\((.*)\)===$")
    for line in lines:
        s = line.strip()
        if "===" in s or "START CTA" in s:
            if ch["type"] == "classic":
                fail("markers", f"a Classic script has no CTA markers: {s[:80]}")
                continue
            m = start_re.match(s)
            if m and not inside:
                if m.group(1) != ch["printed"]:
                    fail("book marker", f"the start marker must read ===START CTA({ch['printed']})===, found {s}")
                inside, cur = True, {"start": len(spoken_lines), "lines": []}
            elif s == "===END CTA===" and inside:
                inside = False; cur["end"] = len(spoken_lines); blocks.append(cur)
            else:
                fail("book marker", f"a marker out of place or not alone on its line: {s[:80]}")
            continue
        spoken_lines.append(line)
        if inside:
            cur["lines"].append(line)
    if inside:
        fail("book marker", "a START CTA marker with no END CTA")
    if ch["type"] == "talking" and len(blocks) != 2:
        fail("book blocks", f"need exactly two (mid and end), found {len(blocks)}")

    spoken = "\n".join(spoken_lines)
    words = norm_words(spoken)
    n = len(words)
    paras = paragraphs(spoken)
    sents = sentences(spoken)

    # 2. Length at the channel's real speed.
    min_words = math.ceil(12 * ch["wpm"])
    minutes = n / ch["wpm"]
    if n < min_words:
        fail("length", f"{n} words ({minutes:.1f} minutes at {ch['wpm']}); needs at least {min_words} (12 minutes)")
    elif minutes > SWEET_MAX_MINUTES:
        infos.append(f"INFO {minutes:.1f} minutes: past the 12-to-20-minute sweet spot (fine if nothing is padding)")

    # 3. The opening: before item one, or the first 45 seconds if no signpost is found.
    flat_words = " ".join(words)
    m1 = re.search(ITEM_ONE, flat_words)
    k1 = len(flat_words[:m1.start()].split()) if m1 else None
    opening_limit = k1 if k1 is not None else round(ch["wpm"] * 0.75)
    opening, seen = [], 0
    for s_ in sents:
        if seen >= opening_limit:
            break
        opening.append(s_)
        seen += len(norm_words(s_))
    opening_text = " ".join(opening)
    for rx, why in OPENING_BAN:
        for m in re.finditer(rx, opening_text, re.I):
            fail("opening", f"{why}: \"{sentence_with(opening_text, m.start())}\"")
    first_minute = " ".join(words[:ch["wpm"]])
    proms = re.findall(OPENING_PROMISE, first_minute, re.I)
    if len(proms) > 1:
        fail("opening promises", f"{len(proms)} promises in the first minute ({', '.join(proms)}); at most one, and only one the end pays")
    for s_ in opening:
        if s_.count(",") >= 3:
            fail("opening list", f"a list of more than three in the opening (three at most; no tool list): \"{s_[:160]}\"")
    if k1 is not None:
        infos.append(f"INFO the opening: {k1} words before item one, about {k1 / ch['wpm'] * 60:.0f} seconds (the first real step by about 45)")
    else:
        infos.append("INFO no 'number one', 'level one' or 'step one' found: check the first real step lands by about 45 seconds")
    op_money = len(re.findall(MONEY_DIGITS + "|" + MONEY_WORDS, opening_text, re.I))
    infos.append(f"INFO dollar figures in the opening: {op_money} (one at most, often none)")
    if re.search(NO_PLUMBER, spoken, re.I) and re.search(A_CALL, spoken, re.I):
        m = re.search(NO_PLUMBER, spoken, re.I)
        fail("scope", f"'no plumber needed' while a step ends in a call: \"{sentence_with(spoken, m.start())}\"")

    # 4. The CTA and the ending, by script type.
    last = paras[-1] if paras else ""
    if not (re.search(r"\bcomments?\b", last, re.I) and ("?" in last or re.search(r"\btell me\b", last, re.I))):
        fail("ending", "the last paragraph must be the comment ask: an outright ask to comment and one question about their house")
    if not sents or not re.search(COMMENT_END, sents[-1], re.I):
        fail("ending", "the last line must close the comment ask with 'I read every one.'")
    before_last = paras[-4:-1]

    if ch["type"] == "classic" and ch["mid"]:
        idx = next((i for i, p in enumerate(paras) if re.search(ch["spoken"], p, re.I)), None)
        if idx is None or idx >= len(paras) - 3:
            fail("mid book line", "the book's spoken title isn't said in the body of the video")
        else:
            p = paras[idx]
            if not (re.search(r"\bdescription\b", p, re.I) and re.search(r"\bQR\b", p, re.I)):
                fail("mid book line", "say it's at the link in the description and the QR code on screen")
            before = len(norm_words(" ".join(paras[:idx])))
            infos.append(f"INFO mid book line: in a paragraph of {len(norm_words(p))} words, starting at {100 * before // max(n, 1)}% of the script (about a third of the way in; never before the end of the third item; about 60 to 80 words)")
        if not any(re.search(r"\bbook\b|" + ch["spoken"], p, re.I) and re.search(r"\bdescription\b", p, re.I) and re.search(r"\bQR\b", p, re.I) for p in before_last):
            fail("ending", "one line reminding them of the book, the link in the description and the QR code, just before the comment ask")
        pitches = [p for p in paras if re.search(r"\bdescription\b", p, re.I)]
        if len(pitches) > 2:
            fail("book line", f"the link is pitched in {len(pitches)} places; the book goes once in the middle and once at the end")
    if ch["type"] == "classic" and ch["end"] == "subscribe":
        subs = [p for p in paras if re.search(r"\bsubscribe\b", p, re.I)]
        if not any(re.search(r"\bsubscribe\b", p, re.I) and re.search(r"\bvintage pipe ?fitter\b", p, re.I) for p in before_last):
            fail("ending", "one line asking them to subscribe to the Vintage Pipefitter, just before the comment ask")
        if len(subs) > 1:
            fail("subscribe", f"subscribe asked in {len(subs)} places; once, at the end")
    if ch["type"] == "classic" and a.channel != "vintage":
        for m in re.finditer(r"\bsubscribe\b", spoken, re.I):
            fail("banned", f"a subscribe ask (none on this channel): \"{sentence_with(spoken, m.start())}\"")

    if ch["type"] == "talking":
        for m in re.finditer(r"\bsubscribe\b", spoken, re.I):
            fail("banned", f"a subscribe ask (none on this channel): \"{sentence_with(spoken, m.start())}\"")
        if blocks:
            mid = " ".join(blocks[0]["lines"])
            mw = len(norm_words(mid))
            before = len(norm_words("\n".join(spoken_lines[:blocks[0]["start"]])))
            infos.append(f"INFO mid book block: {mw} words, starts at {100 * before // max(n, 1)}% of the script (about a third of the way in; never before the end of the third item)")
            if not 30 <= mw <= 65:
                fail("mid book block length", f"{mw} words; the page says about 40 to 55")
            if " ".join(norm_words(ch["fixed"])) not in " ".join(norm_words(mid)):
                fail("mid book block", f"the mentor line, word for word: {ch['fixed']}")
            if not re.search(ch["spoken"], mid, re.I):
                fail("mid book block", "the book's spoken title isn't said")
            if not (re.search(r"\bdescription\b", mid, re.I) and re.search(r"\bQR\b", mid, re.I)):
                fail("mid book block", "say it's at the link in the description and the QR code on screen")
            outside = "\n".join(l for i, l in enumerate(spoken_lines) if not (blocks[0]["start"] <= i < blocks[0]["end"]))
            for m in re.finditer(r"\bmentor\b", outside, re.I):
                fail("mentor", f"the mentor only in the mid-video book line: \"{sentence_with(outside, m.start())}\"")
        if len(blocks) >= 2:
            end = " ".join(blocks[-1]["lines"])
            if not (re.search(r"\bbook\b|" + ch["spoken"], end, re.I) and re.search(r"\bdescription\b", end, re.I) and re.search(r"\bQR\b", end, re.I)):
                fail("ending", "the end block is one line reminding them of the book, the link in the description and the QR code")
            after = "\n".join(spoken_lines[blocks[-1]["end"]:]).strip()
            if not after:
                fail("ending", "the comment ask comes after ===END CTA=== and is the last line")
            if not "\n".join(spoken_lines[blocks[0]["end"]:blocks[-1]["start"]]).strip():
                fail("book blocks", "no video between the mid and end blocks")
    for p in paras:
        if re.search(r"\bbook\b", p, re.I) and re.search(r"\b(?:everything|all of (?:it|this)|every (?:fix|step|tip|repair|one of these)|all (?:three|four|five|eight|ten|of these))\b[^.!?]{0,60}\b(?:book|in it|inside)\b", p, re.I):
            fail("book claim", f"the book line claims the whole video is in the book: \"{p[:140]}\"")

    # 5. Banned lines and once-only phrases.
    for rx, why in COMMON_BAN + ch["ban"]:
        for m in re.finditer(rx, spoken, re.I):
            fail("banned", f"{why}: \"{sentence_with(spoken, m.start())}\"")
    if a.channel != "werner":
        for m in re.finditer(RELATIVES + r"|\bmy (?:old )?mentor\b", spoken, re.I):
            fail("banned", f"a relative or a mentor (none on this channel): \"{sentence_with(spoken, m.start())}\"")
    else:
        for m in re.finditer(RELATIVES, spoken, re.I):
            fail("banned", f"a relative (none; the trade mentor only, in the fixed line): \"{sentence_with(spoken, m.start())}\"")
    once = COMMON_ONCE + ch["once"]
    if a.channel == "vintage":
        once = [o for o in once if "people skip" not in o[0]]
    for rx, why in once:
        k = len(re.findall(rx, spoken, re.I))
        if k > 1:
            fail("said twice", f"{why}, said {k} times (never the same phrase twice)")
    if not ch["contractions"]:
        for m in re.finditer(CONTRACTION, spoken.replace("’", "'"), re.I):
            fail("contraction", f"'{m.group()}' (this voice mishandles contractions): \"{sentence_with(spoken, m.start())}\"")

    # 6. The tenure: the profile's figure or the title's, once at most.
    tn = r"\b(\w+(?:-\w+)?)\s+years?\s+(?:in (?:the|this) trade|as a plumber|of plumbing|in plumbing|on the job|doing this|on the tools|in the business)\b|\bin (?:the|this) trade,? (?:for )?(\w+(?:-\w+)?) years\b"
    allowed_tenure = {ch["tenure"]} | numbers_in(a.title)
    hits = list(re.finditer(tn, spoken, re.I))
    for m in hits:
        got = numbers_in(m.group())
        if got and not got <= allowed_tenure:
            fail("tenure", f"{', '.join(map(str, sorted(got)))} years; the channel's figure is {ch['tenure']} (or the title's): \"{sentence_with(spoken, m.start())}\"")
    if len(hits) > 1:
        fail("tenure", f"the years in the trade said {len(hits)} times; once at most")

    # 7. Werner: the German words and the personal details.
    if a.channel == "werner":
        used = [w for w in GERMAN_WORDS if re.search(r"\b" + w + r"\b", spoken)]
        if len(used) > 3:
            fail("German words", f"{len(used)} German words ({', '.join(used)}); up to three")
        outside = "\n".join(l for i, l in enumerate(spoken_lines) if not any(b["start"] <= i < b["end"] for b in blocks))
        got = [why for rx, why in WERNER_DETAILS if re.search(rx, outside, re.I)]
        if len(got) > 1:
            fail("personal details", f"{len(got)} personal details ({', '.join(got)}); one at most outside the book line")
        for rx, why in WERNER_DETAILS:
            k = len(re.findall(rx, spoken, re.I))
            if k > 1:
                fail("said twice", f"{why}, said {k} times")
        starts = [bool(re.match(r"^So\b", p)) for p in paras]
        for i in range(1, len(starts)):
            if starts[i] and starts[i - 1]:
                fail("'So.'", f"two paragraphs running open on 'So': \"{paras[i][:80]}\"")

    # 8. Safety requirements (the brief wins: these fire only where the script raises the risk).
    plunger = list(re.finditer(r"\bplung(?:e|er|ers|ing)\b|\bsnake\b|\bauger\b", spoken, re.I))
    chem = re.search(r"\b(?:chemical|caustic|lye)\b[^.!?]{0,30}\b(?:drain )?cleaners?\b|\bdrain cleaners?\b|\bthe jug\b", spoken, re.I)
    if plunger and chem:
        warn = r"\b(?:don'?t|do not|never|no)\b[^.!?]{0,40}\b(?:plung\w*|snake)\b|\bcan(?:'?t|not) (?:safely )?plunge\b|\bnothing (?:else )?(?:goes|gets added|is added|added)\b[^.!?]{0,60}\b(?:chemical|cleaner)|\b(?:chemical|cleaner)\b[^.!?]{0,80}\b(?:don'?t|do not|never|stop)\b"
        w = re.search(warn, spoken, re.I)
        op_end = len(opening_text)
        flat = " ".join(p for p in paras if not re.search(r"\bbook\b", p, re.I))
        later = [m for m in re.finditer(r"\bplung(?:e|er|ers|ing)\b|\bsnake\b|\bauger\b", flat, re.I) if m.start() > op_end]
        wf = re.search(warn, flat, re.I)
        if not w:
            fail("safety", "chemical cleaner and a plunger or snake in the same script, with no line saying never to plunge or add anything to a drain with chemical cleaner in it")
        elif later and wf.start() > later[0].start():
            fail("safety", f"the chemical-cleaner check comes after the first plunger or snake step; it goes before: \"{sentence_with(flat, later[0].start())}\"")
    backup = [s_ for s_ in sents if re.search(r"\bmain(?: sewer)? line\b|\bthe main\b", s_, re.I) and re.search(r"\bback(?:s|ing|ed)? up\b|\bcom(?:e|es|ing) up\b|\btwo (?:or more )?(?:drains|fixtures)\b|\bmore than one drain\b", s_, re.I)]
    if backup:
        if not re.search(r"\bstop (?:running|using|sending) (?:any )?(?:the )?water\b|\bstop (?:every|all) (?:the )?(?:taps?|faucets?|flush\w*)\b|\b(?:don'?t|do not) (?:run|use|flush)\b[^.!?]{0,30}\b(?:water|tap|toilet|anything)\b|\bno more water\b|\bstop (?:the )?water\b|\bstop running\b|\bstop using\b", spoken, re.I):
            fail("safety", f"a main-line backup with no line to stop running water: \"{backup[0][:140]}\"")
        if not re.search(A_CALL, spoken, re.I):
            fail("safety", "a main-line backup with no call named")
    if re.search(r"\bgas leak\b|\bsmell (?:of )?gas\b|\bsmell gas\b|\brotten eggs?\b", spoken, re.I):
        need = [(r"\b(?:get|everyone|everybody|all of you)\b[^.!?]{0,40}\bout\b|\bleave the house\b", "everyone out"),
                (r"\bswitch", "no light switches"), (r"\b(?:light anything|flames?|match(?:es)?|lighter|candles?|light a)\b", "nothing lit"),
                (r"\bcars?\b", "no car started"), (r"\b911\b|\bnine[- ]one[- ]one\b", "911"), (r"\bgas company\b|\butility\b", "the gas company")]
        miss = [why for rx, why in need if not re.search(rx, spoken, re.I)]
        if miss:
            fail("safety", f"a gas leak gets every step; missing: {', '.join(miss)}")
    for thing, other, why in [(r"\bbleach\b", r"\bammonia\b|\bvinegar\b|\bacids?\b|\bcitric\b", "bleach with ammonia, vinegar or an acid"),
                              (r"\bperoxide\b", r"\bvinegar\b", "peroxide with vinegar")]:
        if re.search(thing, spoken, re.I) and re.search(other, spoken, re.I):
            ok = any(re.search(thing, s_, re.I) and re.search(r"\b(?:never|don'?t|do not|not|no)\b", s_, re.I) and re.search(r"\bmix\w*|\btogether\b|\bmeet\b|\bsame\b|\bwith\b|\bone (?:cleaner )?at a time\b", s_, re.I) for s_ in sents) \
                or re.search(r"\bone cleaner at a time\b", spoken, re.I)
            if not ok:
                fail("safety", f"{why} both in the script, with no line saying never to mix them")
    if re.search(r"\b(?:flush|drain)(?:ing|ed)? (?:the |your |a )?(?:water heater|tank heater|heater tank)\b|\banode rod\b|\bwater heater\b[^.!?]{0,60}\b(?:element|thermostat|drain valve)\b", spoken, re.I):
        if not re.search(r"\b(?:power|breaker|gas)\b[^.!?]{0,40}\boff\b|\bturn (?:off|down) the (?:power|gas|breaker)\b|\bvacation\b|\bpilot setting\b", spoken, re.I):
            fail("safety", "a water-heater job with no line turning the power or the gas off first")

    # 9. Prices against the brief and the price guide; figures against the brief.
    sources = [l for l in (brief + "\n" + prices).splitlines() if l.strip()]
    source_sets = [numbers_in(l) for l in sources]
    title_nums = numbers_in(a.title)
    allowed = numbers_in(brief) | title_nums | ch["facts"]
    for m in re.finditer(MONEY_DIGITS + "|" + MONEY_WORDS, spoken, re.I):
        got = numbers_in(m.group())
        if not got:
            continue
        if re.search(r"\$\s?\d+\.\d|\bcents?\b", m.group(), re.I):
            fail("money", f"a price in cents (round it): \"{sentence_with(spoken, m.start())}\"")
            continue
        if got <= title_nums | ch["facts"] or any(got <= s for s in source_sets):
            continue
        fail("money", f"a price not in the brief or the price guide (a range must come from one line of either): \"{sentence_with(spoken, m.start())}\"")
    for m in re.finditer(r"\b\d+ cents\b|\b(?:%s)(?:[- ](?:%s))* cents\b" % (NUMWORD, NUMWORD), spoken, re.I):
        infos.append(f"INFO cents said (only a cost per use may be in cents): \"{sentence_with(spoken, m.start())}\"")
    for s_ in sents:
        if re.search(r"\bper ?cent\b|%|\b\w+ out of (?:every )?(?:\d+|two|three|four|five|ten|a hundred)\b|\bsurvey\b|\bstudy\b|\btimes more\b", s_, re.I):
            extra = {x for x in numbers_in(s_) if x > 1} - allowed
            if extra:
                fail("numbers", f"a figure not in the brief ({', '.join(map(str, sorted(extra)))}): \"{s_[:160]}\"")
    other = sorted(x for x in numbers_in(spoken) - allowed - numbers_in(prices) if x > 12)
    if other:
        infos.append(f"INFO numbers in neither the brief nor the price guide (check each is plain sense, not a claim): {', '.join(map(str, other))}")

    # 10. The voice.
    for i, line in enumerate(spoken_lines, 1):
        for pat, why in [(r"[%&+#=~@°/\\|*_<>{}\[\]()½¼¾]", "a symbol, bracket or label"),
                         (r"[—–]", "a dash"), (r"[‘’“”]", "a curly quote"),
                         (r"\b\d+\s?[x×]\s?\d+\b", "a size with an x"), (r"\b(?:haha|hmm+|ugh)\b", "a sound written as a word"),
                         (r"\d\s?(?:ft|oz|lbs?|gal|psi|in\.|mm|cm)\b", "a unit written short (say the word)"),
                         (r"\b\d[\d,]*\s+\d", "two numbers side by side"),
                         (r"[äöüÄÖÜß]", "an umlaut or eszett (the voice garbles them)"),
                         (r"[\U0001F300-\U0001FAFF☀-➿]", "an emoji")]:
            m = re.search(pat, line, re.I if "x" not in pat else 0)
            if m:
                fail("voice", f"{why} '{m.group()}' on line {i}: \"{line.strip()[:100]}\"")
        if re.match(r"^\s*(?:#|[A-Z][A-Za-z ]{0,30}:\s*$)", line):
            fail("voice", f"a heading or label on line {i}: \"{line.strip()[:80]}\"")
    for s_ in sents:
        w = len(norm_words(s_))
        if w > MAX_SENTENCE:
            fail("long sentence", f"{w} words: \"{s_[:120]}...\"")

    # 11. Copying from a model.
    models = load_models(a.models)
    if not models:
        infos.append(f"INFO no model files found in {a.models}: copying not checked")
    keep = [ch["fixed"]] if ch.get("fixed") else []
    keep += [ch["spoken"].replace("'?", "'").replace("[- ]", " ")] if ch["spoken"] else []
    keep += ["the link in the description and the QR code on your screen"]
    allow = set()
    for k in keep:
        kw = norm_words(k)
        for j in range(len(kw) - COPY_RUN + 1):
            allow.add(tuple(kw[j:j + COPY_RUN]))
    script_grams = {}
    for j in range(len(words) - COPY_RUN + 1):
        script_grams.setdefault(tuple(words[j:j + COPY_RUN]), j)
    norm_spoken = " ".join(words)
    for fn, body, sig in models:
        mw = norm_words(body)
        shared = sorted({script_grams[g] for g in (tuple(mw[j:j + COPY_RUN]) for j in range(len(mw) - COPY_RUN + 1)) if g in script_grams and g not in allow})
        runs, last_j = [], -10
        for j in shared:
            if j > last_j + 1:
                runs.append([j, j])
            else:
                runs[-1][1] = j
            last_j = j
        for r0, r1 in runs:
            fail("copied", f"{r1 - r0 + COPY_RUN} words in a row from {fn}: \"{' '.join(words[r0:r1 + COPY_RUN])}\"")
        for phrase in sig:
            if " ".join(norm_words(phrase)) in norm_spoken:
                fail("model's phrase", f"{fn}'s signature phrase: \"{phrase}\"")

    # 12. For reading only.
    first = sents[0] if sents else ""
    shared_w = sorted(set(norm_words(first)) & set(norm_words(a.title)) - {"the", "a", "an", "to", "of", "and", "that", "your", "you", "for", "in", "it", "is", "this", "how", "why", "with", "on"})
    infos.append(f"INFO the first sentence (does it make the point?): \"{first[:160]}\" | title words in it: {', '.join(shared_w) or 'none'}")
    infos.append(f"INFO {n} words, about {minutes:.1f} minutes at {ch['wpm']} words a minute")

    for line in fails + infos:
        print(line)
    print("RESULT: PASS" if not fails else f"RESULT: FAIL ({len(fails)})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
