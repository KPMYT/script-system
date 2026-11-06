#!/usr/bin/env python3
"""The hard-rules check for woodworking scripts (P21, the simple way).

Usage:
    python3 check.py SCRIPT --channel hank|dale --title "LOCKED TITLE" --brief BRIEF [--pack PACK] [--models DIR]

It checks only hard rules and never asks for a line to be added to meet a count:
length at the channel's words a minute, the book blocks and their markers, the
ending, banned lines, swearing, the safety lines the build calls for, numbers and
money against the brief and research pack, the voice, sentences over 35 words,
lists of more than three in the opening, and copying from a model. FAIL lines
must be fixed; INFO lines are for reading only.
The last line is "RESULT: PASS" or "RESULT: FAIL (n)".
"""
import argparse
import math
import os
import re
import sys

MIN_MINUTES = 8
MAX_SENTENCE = 35
COPY_RUN = 8                    # words in a row shared with a model
SWEARS = r"\b(?:ass|damn|hell|crap)\b"
STRONG = r"\bf+u+c+k\w*|\bshit\w*|\bbitch\w*|\bbastard\w*|\bgoddamn\w*"

CHANNELS = {
    "hank": {
        "name": "Hank Hardwood",
        "wpm": 185,
        "printed": "100 Ways to Make Your First $1,000 with Woodworking",
        "spoken": r"a hundred ways to make your first thousand dollars with woodworking",
        "blocks": 2,                      # mid and end
        "last_line": "Keep all ten fingers and I'll see you at the bench.",
        "swear_max": 3,
        "facts": {100, 5, 1000},          # a hundred builds, five chapters, the first thousand
        "keep": ["a hundred ways to make your first thousand dollars with woodworking",
                 "keep all ten fingers and i'll see you at the bench",
                 "the qr code on screen or the top link in the description"],
        "ban": [
            (r"\bI'm Hank\b|\bthis is Hank Hardwood\b", "a channel intro"),
            (r"\bmy (?:wife|husband|son|daughter|kids?|grandkids?|grandson|granddaughter|dad|father|mother|mom|grandfather|grandpa|brother|sister|family)\b", "a relative (none approved)"),
        ],
    },
    "dale": {
        "name": "Dale Oakfield's Workshop",
        "wpm": 170,
        "printed": "The Ultimate DIY Woodworking Guide: Time-Tested Techniques, Money-Saving Shop Hacks, and Real Furniture Builds from 40 Years at the Bench",
        "spoken": r"the ultimate diy woodworking guide",
        "blocks": 1,                      # the main pitch only
        "last_line": "Now go make some sawdust.",
        "swear_max": 0,
        "facts": {5, 30},                 # five chapters, 30 Common Mistake callouts
        "grandfather": "My grandfather taught me everything I know about woodworking and made me promise to write it all down, so I did, every technique and fix in one place.",
        "keep": ["the ultimate diy woodworking guide", "now go make some sawdust", "here's what i'd ask of you",
                 "my grandfather taught me everything i know about woodworking and made me promise to write it all down so i did every technique and fix in one place"],
        "ban": [
            (r"\bI'm Dale\b|\bthis is Dale Oakfield\b|\bDale Oakfield's Workshop\b", "a channel intro or the channel's name"),
            (r"\bsubscribe\b", "a subscribe ask (Dale has none)"),
            (r"\bmy (?:wife|husband|son|daughter|kids?|grandkids?|grandson|granddaughter|dad|father|mother|mom|brother|sister|family|uncle|aunt)\b", "a relative (only his grandfather is approved)"),
            (r"\b(?:40|forty) years\b", "the book's '40 Years' (only if the title says it)"),
        ],
    },
}

COMMON_BAN = [
    (r"\btoday,? (?:we're|we are|I'm|I am) (?:going to|gonna)\b|\bby the end of (?:this|today'?s) (?:video|one)\b|\bin today'?s (?:video|build)\b|\bwelcome (?:back|to)\b", "a channel intro or 'today we're going to'"),
    (r"\bstick around\b|\bstay tuned\b|\bbonus at the end\b|\bcoming up\b|\bstill to come\b|\blater in (?:this|the) video\b|\bI told you to wait for\b|\bhold (?:on|tight) for\b|\bdon't go nowhere\b|\bI'll (?:answer|show you|tell you)\b[^.!?]{0,30}\b(?:at the (?:very )?end|later)\b", "a tease"),
    (r"\blet'?s (?:get into it|dive in|go)\s*[.!]", "'let's get into it' or 'let's go'"),
    (r"\b(?:to|let'?s|quick) recap\b|\bto sum (?:it )?up\b|\bthat'?s the whole build\b", "a recap"),
    (r"\bI(?:'m| am) (?:cutting|drilling|sanding|gluing|clamping|measuring|marking)\b|\bI(?:'ll| will) (?:cut|drill|sand|glue|clamp|measure|mark|grab)\b|\bwatch me\b", "first-person build narration"),
    (r"\bas you can see\b|\bright here\b|\blook at this\b|\btake a look at (?:this|these|that)\b", "pointing at the footage"),
    (r"(?:\$\s?\d[\d,.]*|\bbucks|\bdollars)\s*(?:an|per|a|/)\s*hour\b|\bper hour\b|\ban hourly\b", "a per-hour figure"),
    (r"\bscientists? (?:now )?(?:say|said|admit|are baffled)\b|\bstudies show\b|\bresearch shows\b", "an invented authority"),
    (r"\byears? of (?:selling|sales)\b", "a sales-history claim"),
    (r"\bI(?:'ve| have)? (?:sold|shipped)\b|\bmy (?:customers?|buyers?|booth|craft booth)\b|\bat (?:my|our) (?:table|booth)\b|\bthe last (?:batch|one|set)s? I (?:made|sold|built)\b|\bI (?:made|built) (?:one|a few|some|these|six|a set) for (?:my|a)\b|\bpeople (?:always )?ask me\b", "invented sales, customers or history"),
    (r"\be-?book\b", "'e-book' (say 'book')"),
    (r"\bguarantee[ds]?\b(?![^.!?]*\bnot\b)|\byou(?:'ll| will) (?:make|earn|clear|pocket) (?:about |over |at least |a )?\$", "an income guarantee"),
]

# (trigger, what must be said somewhere, why). The brief or pack can add more; these are the page's defaults.
SAFETY = [
    (r"\bstop block\b", r"\bblade (?:to )?(?:stop|come to a (?:full )?stop)\b|\blet the blade stop\b|\bblade stops?\b", "a stop block without 'let the blade stop'"),
    (r"\btable saw\b|\brip fence\b|\bnarrow rips?\b", r"\bpush stick\b|\bkickback\b", "a table saw or rip without a push stick or kickback line"),
    (r"\blinseed\b|\btung oil\b|\bdanish oil\b|\boily rags?\b", r"\brags?\b[^.!?]{0,80}\b(?:flat|water|metal can|sealed)\b|\b(?:flat|water|metal can|sealed)\b[^.!?]{0,80}\brags?\b", "an oil finish without the oily-rags line"),
    (r"\bspray (?:paint|finish|lacquer|poly\w*|on)\b|\bfine dust\b|\b(?:sort|tip|empty)\w* (?:out )?(?:the |your )?(?:sawdust|vac|dust)\b", r"\bmask\b|\brespirator\b", "spray finish or fine dust without a mask"),
    (r"\bcutting boards?\b|\bserving (?:boards?|trays?)\b|\bcharcuterie\b|\butensils?\b|\bwooden spoons?\b|\bdog bowls?\b|\bbowl stand\b|\bfeeders?\b|\bkibble\b|\bfood (?:touches|contact|goes)\b", r"\bfood[- ]safe\b", "food contact without a food-safe finish"),
    (r"\bfire ?starters?\b|\bkindling\b|\bwood stove\b|\bfirewood\b|\bfire pit\b|\bcutting boards?\b|\bserving\b|\bdog\b|\bcat\b|\bpets?\b|\bbird(?:house|s)?\b|\bchickens?\b|\bfeeders?\b", r"\b(?:never|no|not)\b[^.!?]{0,40}\btreated\b|\buntreated\b", "food, animals or burning without the no-treated-wood line"),
    (r"\btoys?\b|\btoddlers?\b|\bbab(?:y|ies)\b", r"\bunder (?:three|3)\b|\bsmall parts\b|\bchok\w+\b", "a toy without the small-parts line"),
    (r"\bold furniture\b|\bflip(?:s|ping|ped)?\b|\bbefore 1978\b|\brefinish\w* (?:an? )?old\b", r"\blead\b", "old furniture without the lead-paint test"),
    (r"\bcandle holders?\b|\btea ?lights?\b|\blamps?\b|\blanterns?\b", r"\bmetal\b|\bglass\b|\bLED\b|\blamp kit\b|\blisted\b|\bbattery\b", "a lamp or candle without the metal or glass cup, LED or lamp kit"),
    # Melting wax (iter-13's shared gap): the water topped up, and the burner off after the last pour.
    (r"\bmelt\w*\b[^.!?]{0,60}\bwax\b|\bwax\b[^.!?]{0,60}\bmelt\w*\b", r"\btop(?:ped|ping|s)? (?:it|the (?:pot|water)|that water|your water) (?:back )?up\b|\btop up the water\b|\bboils? dry\b|\bboil(?:ed|ing)? dry\b|\badd (?:more|a little|some) water\b|\bwater (?:level|topped)\b", "melting wax without keeping the pot's water topped up"),
]
BURNER_OFF = r"\b(?:turn|switch|shut|click)\w* (?:the |your )?(?:burner|heat|hot plate|stove)\b[^.!?]{0,15}\boff\b|\b(?:turn|switch|shut|click)\w* (?:it|that|them) off\b|\bburner off\b|\bunplug\w*\b"

UNITS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: 10 * (i + 2) for i, w in enumerate("twenty thirty forty fifty sixty seventy eighty ninety".split())}
SCALES = {"hundred": 100, "thousand": 1000}


def numbers_in(text, rounding=False):
    """Every number in the text, from digits and from number words. With rounding,
    a figure with cents also allows the whole numbers either side of it."""
    found = set()
    for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", text):
        try:
            v = float(m.group().replace(",", ""))
        except ValueError:
            continue
        found.add(int(v))
        if rounding and v != int(v):
            found.add(math.ceil(v))
    tokens = re.findall(r"[a-z]+", re.sub(r"\ba (hundred|thousand)\b", r"one \1", text.lower().replace("-", " ")))
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
                total += (cur or 1) * 1000; cur = 0
        elif t == "and" and active:
            continue
        else:
            if active:
                found.add(total + cur)
            cur, total, active = 0, 0, False
    return found


def norm_words(text):
    return re.findall(r"[a-z0-9']+", text.lower().replace("’", "'"))


def count_words(text):
    """Words as a reader (and wc -w) counts them: a hyphenated word is one word."""
    return len([w for w in text.split() if re.search(r"[A-Za-z0-9]", w)])


def sentences(text):
    flat = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", flat) if s.strip()]


def sentence_with(text, start):
    left = max(text.rfind(".", 0, start), text.rfind("?", 0, start), text.rfind("!", 0, start), text.rfind("\n", 0, start))
    right = min([i for i in (text.find(".", start), text.find("?", start), text.find("!", start), text.find("\n", start)) if i != -1] or [len(text)])
    return re.sub(r"\s+", " ", text[left + 1:right + 1]).strip()[:160]


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
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--channel", required=True, choices=sorted(CHANNELS))
    ap.add_argument("--title", required=True)
    ap.add_argument("--brief", required=True)
    ap.add_argument("--pack", default=None, help="the research pack, if it's a separate file")
    ap.add_argument("--models", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "references", "models"))
    a = ap.parse_args()
    ch = CHANNELS[a.channel]
    raw = open(a.script, encoding="utf-8").read()
    facts_text = open(a.brief, encoding="utf-8").read()
    if a.pack:
        facts_text += "\n" + open(a.pack, encoding="utf-8").read()
    fails, infos = [], []

    def fail(rule, detail=""):
        fails.append(f"FAIL {rule}" + (f": {detail}" if detail else ""))

    # Keep only the script if a whole output was pasted; drop a TEST label line from the test harness.
    raw = re.sub(r"^\s*SCRIPT TYPE:[^\n]*\n", "", raw)
    raw = re.sub(r"^\s*TEST\b[^\n]*\n", "", raw)
    raw = re.split(r"\n\s*(?:CHECK:|VO COPY)", raw)[0]
    lines = raw.strip("\n").split("\n")
    start_re = re.compile(r"^===START CTA\((.*)\)===$")

    # 1. The book blocks and their markers.
    blocks, spoken_lines, inside, cur = [], [], False, None
    for line in lines:
        s = line.strip()
        if "===" in s:
            m = start_re.match(s)
            if m and not inside:
                if m.group(1) != ch["printed"]:
                    fail("book marker", f"the start marker must read ===START CTA({ch['printed']})===, found {s[:120]}")
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
    if len(blocks) != ch["blocks"]:
        want = "two (mid and end)" if ch["blocks"] == 2 else "one (the main pitch)"
        fail("book blocks", f"need exactly {want}, found {len(blocks)}")

    spoken = "\n".join(spoken_lines)
    words = norm_words(spoken)
    n = count_words(spoken)
    block_text = "\n".join("\n".join(b["lines"]) for b in blocks)
    outside = "\n".join(l for i, l in enumerate(spoken_lines) if not any(b["start"] <= i < b["end"] for b in blocks))

    # 2. Length: the 8-minute floor at the channel's words a minute.
    minutes = n / ch["wpm"]
    floor = MIN_MINUTES * ch["wpm"]
    if n < floor:
        fail("length", f"{n} words ({minutes:.1f} minutes at {ch['wpm']}); needs at least {floor}")

    # 3. The book blocks and the ending.
    nonempty = [l.strip() for l in spoken_lines if l.strip()]
    for b in blocks:
        bt = "\n".join(b["lines"])
        priced = re.sub(ch["spoken"], " ", bt, flags=re.I)
        for m in re.finditer(r"\$\s?\d|\bdollars?\b|\bbucks\b|\bprice\b|\bfree\b|\bdiscount\b", priced, re.I):
            fail("book claim", f"'{m.group()}' in a book block (never a price)")
        for m in re.finditer(SWEARS + "|" + STRONG, bt, re.I):
            fail("swearing", f"'{m.group()}' in a book block")
    if blocks:
        mid = "\n".join(blocks[0]["lines"])
        mw = count_words(mid)
        before = count_words("\n".join(spoken_lines[:blocks[0]["start"]]))
        infos.append(f"INFO book pitch: {mw} words, starts at {100 * before // max(n, 1)}% of the script")
        prev = sentences("\n".join(spoken_lines[:blocks[0]["start"]]))
        last_in = sentences(mid)
        if prev and last_in:
            infos.append(f"INFO the line before the pitch: \"{prev[-1][:120]}\" | the line back: \"{last_in[-1][:120]}\" (does it name what the viewer was holding?)")
        if not re.search(ch["spoken"], mid, re.I):
            fail("book pitch", "the book's spoken title isn't said")
    if a.channel == "hank":
        if blocks:
            mid = "\n".join(blocks[0]["lines"])
            if not (re.search(r"\bQR\b", mid) and re.search(r"\bdescription\b", mid, re.I)):
                fail("book pitch", "say both: the QR code on screen and the top link in the description")
            if re.search(r"\bsubscribe\b", mid, re.I):
                fail("book pitch", "no subscribe ask in the mid-video block")
        if len(blocks) >= 2:
            end = "\n".join(blocks[-1]["lines"])
            if not re.search(r"\bbook\b|" + ch["spoken"], end, re.I):
                fail("ending", "the end block has no line on the book")
            if not (re.search(r"\bQR\b", end) and re.search(r"\bdescription\b", end, re.I)):
                fail("ending", "the end block must say both: the QR code and the top link in the description")
            if not (re.search(r"\bsubscribe\b", end, re.I) and re.search(r"\bHank Hardwood\b", end)):
                fail("ending", "the end block needs a subscribe ask naming Hank Hardwood")
            after = [l.strip() for l in spoken_lines[blocks[-1]["end"]:] if l.strip()]
            if after != [ch["last_line"]]:
                fail("closing line", f"after the end block there must be one line, exactly: {ch['last_line']} (found: {' / '.join(after)[:120]})")
            if not "\n".join(spoken_lines[blocks[0]["end"]:blocks[-1]["start"]]).strip():
                fail("book blocks", "no build between the mid and end blocks")
        if re.search(r"\bsubscribe\b", outside, re.I):
            fail("subscribe", "a subscribe ask outside the end block")
        if re.search(r"\bHank Hardwood\b", outside):
            fail("banned", "the channel's name outside the end block's subscribe ask")
    else:
        if blocks:
            mid = "\n".join(blocks[0]["lines"])
            flat_mid = " ".join(norm_words(mid))
            if " ".join(norm_words(ch["grandfather"])) not in flat_mid:
                fail("book pitch", f"the grandfather line must be said word for word: \"{ch['grandfather']}\"")
            if not re.search(r"\blink below\b", mid, re.I):
                fail("book pitch", "say 'link below'")
            if re.search(r"\bQR\b|\bsubscribe\b", mid, re.I):
                fail("book pitch", "Dale's pitch points to the link below only, with no subscribe ask")
            if not 30 <= count_words(mid) <= 75:
                fail("book pitch length", f"{count_words(mid)} words; the page says about 45")
        if not nonempty or nonempty[-1] != ch["last_line"]:
            fail("closing line", f"the last line must be exactly: {ch['last_line']} (found: {(nonempty[-1] if nonempty else '')[:100]})")
        m = re.search(r"Here's what I'd ask of you", spoken)
        if not m:
            fail("ending", "the ending opens with \"Here's what I'd ask of you\"")
        else:
            tail = spoken[m.start():]
            if not (re.search(r"\bcomments?\b", tail, re.I) and "?" in tail):
                fail("ending", "the ending needs one specific question for the comments")
            if not re.search(r"\bI read every one\b", tail, re.I):
                fail("ending", "the ending says \"I read every one.\"")
            if re.search(r"\bbook\b|" + ch["spoken"], tail, re.I):
                fail("ending", "no book in the last part of the script")
        g = len(re.findall(r"\bgrandfather\b|\bgrandpa\b", outside, re.I))
        if g > 1:
            fail("at most once", f"his grandfather outside the pitch, said {g} times")
        mentions = [s for s in sentences(outside) if re.search(r"\bbook\b|" + ch["spoken"], s, re.I)]
        for s in mentions:
            if re.search(r"\blink\b|\bbuy\b|\bdescription\b|\bQR\b", s, re.I):
                fail("book mention", f"a mention with a link or 'buy': \"{s[:120]}\"")
        if len(mentions) > 5:
            fail("book mentions", f"{len(mentions)} sentences mention the book; up to five, each different")
        infos.append(f"INFO book mentions outside the pitch: {len(mentions)} (up to five, only where the book covers the tip; no number to reach)")

    # 4. Banned lines.
    for entry in COMMON_BAN + ch["ban"]:
        rx, why = entry[0], entry[1]
        if why.startswith("the book's '40 Years'") and re.search(r"\b(?:40|forty) years\b", a.title, re.I):
            continue
        for m in re.finditer(rx, spoken, re.I):
            fail("banned", f"{why}: \"{sentence_with(spoken, m.start())}\"")

    # 5. Swearing.
    for m in re.finditer(STRONG, spoken, re.I):
        fail("swearing", f"strong profanity '{m.group()}'")
    sw = [m.group().lower() for m in re.finditer(SWEARS, spoken, re.I)]
    if len(sw) > ch["swear_max"]:
        fail("swearing", f"{len(sw)} mild swear words ({', '.join(sw)}); this channel allows {ch['swear_max']}")
    for m in re.finditer(r"\b(?:do|cut|sand|get|grab|make|buy|go|run) the (?:damn|hell)\b", spoken, re.I):
        fail("swearing", f"aimed at the viewer: \"{sentence_with(spoken, m.start())}\"")
    if ch["swear_max"]:
        infos.append(f"INFO mild swear words: {', '.join(sw) or 'none'} (three at most; none is fine)")

    # 6. Safety lines the build calls for.
    for trigger, need, why in SAFETY:
        m = re.search(trigger, spoken, re.I)
        if m and not re.search(need, spoken, re.I):
            fail("safety", f"{why}: \"{sentence_with(spoken, m.start())}\"")
    if re.search(SAFETY[-1][0], spoken, re.I):
        offs = [s for s in sentences(spoken) if re.search(BURNER_OFF, s, re.I) and not re.search(r"\bfire\b|\bflames?\b|\bcatch\w*\b|\bburning\b", s, re.I)]
        if not offs:
            fail("safety", "melting wax without turning the burner off once the pouring is done (a burner-off line for a wax fire doesn't count)")

    # 7. Numbers and money against the brief and research pack.
    allowed = numbers_in(facts_text, rounding=True) | numbers_in(a.title, rounding=True) | ch["facts"]
    money_rx = r"\$\s?\d[\d,]*(?:\.\d+)?|\b\d[\d,]*\s?(?:dollars?|bucks)\b|\b(?:[a-z]+[- ])?(?:hundred|thousand|[a-z]+ty|ten|eleven|twelve|[a-z]+teen|one|two|three|four|five|six|seven|eight|nine)\s+(?:dollars?|bucks)\b"
    money_text = re.sub(ch["spoken"], " ", spoken, flags=re.I)
    prices = 0
    for m in re.finditer(money_rx, money_text, re.I):
        prices += 1
        if not (numbers_in(m.group()) <= allowed):
            fail("money", f"a price not in the brief or pack: \"{sentence_with(money_text, m.start())}\"")
    for m in re.finditer(r"\$\s?\d[\d,]*\.\d|\bcents?\b", spoken, re.I):
        fail("money", f"cents (always round): \"{sentence_with(spoken, m.start())}\"")
    if re.search(r"\bsold for\b", spoken, re.I) and not re.search(r"\bsold (?:listings?|count|for)\b|\bsales? (?:count|evidence|history)\b", facts_text, re.I):
        fail("money", "'sold for' with no sales evidence in the brief or pack (say 'listed at')")
    k = len(re.findall(r"\bprices? (?:are )?subject to change\b", spoken, re.I))
    if prices and k == 0:
        fail("money", "'prices subject to change' is never said (once, straight after the prices)")
    elif k > 1:
        fail("money", f"'prices subject to change' said {k} times (once)")
    for s in sentences(spoken):
        if re.search(r"\bper ?cent\b|%|\b\w+ out of (?:every )?(?:\d+|two|three|four|five|ten|a hundred)\b|\bsurvey\b|\bstudy\b|\btimes more\b", s, re.I):
            extra = {x for x in numbers_in(s) if x > 1} - allowed
            if extra:
                fail("numbers", f"a figure not in the brief or pack ({', '.join(map(str, sorted(extra)))}): \"{s[:160]}\"")
    for m in re.finditer(r"\bpages? (\d+)(?: (?:to|and|through) (\d+))?", spoken, re.I):
        for g in m.groups():
            if g and int(g) not in allowed:
                fail("book page", f"page {g} isn't in the brief's book match: \"{sentence_with(spoken, m.start())}\"")
    other = sorted(x for x in numbers_in(spoken) - allowed if x > 12)
    if other:
        infos.append(f"INFO numbers not in the brief or pack (check each is plain sense, not a claim): {', '.join(map(str, other))}")

    # 8. The voice.
    for i, line in enumerate(spoken_lines, 1):
        for pat, why in [(r"\b\d+\s?[x×]\s?\d+\b|\b\d+[- ]by[- ]\d+\b", "a size written with numbers (say 'a two by four')"),
                         (r"\b\d+(?:\.\d+)?\s?(?:in(?!\s+(?:the|a|an|my|your|his|her|this|that|each|every|one|two|front|back|place|half|line|stock)\b)|ft|oz|lbs?|gal|mm|cm|psi)\b\.?|\d\s?[\"']|°", "a unit abbreviation or symbol"),
                         (r"\b\d+/\d+\b|[½¼¾⅛⅜⅝⅞]", "a fraction with a slash"),
                         (r"\b\d[\d,]*\s+\$?\d", "two numbers side by side"),
                         (r"[%&+#=~@/\\|*_<>{}\[\]()]", "a symbol, bracket or label"),
                         (r"[—–]", "a dash"), (r"[‘’“”]", "a curly quote"),
                         (r"\b(?:haha|hmm+|ugh|heh)\b", "a sound written as a word"),
                         (r"[\U0001F300-\U0001FAFF☀-➿]", "an emoji")]:
            m = re.search(pat, line, re.I)
            if m:
                fail("voice", f"{why} '{m.group()}' on line {i}: \"{line.strip()[:100]}\"")
        if re.match(r"^\s*(?:#|[A-Z][A-Za-z ]{0,30}:\s*$)", line):
            fail("voice", f"a heading or label on line {i}: \"{line.strip()[:80]}\"")
    for s in sentences(spoken):
        w = count_words(s)
        if w > MAX_SENTENCE:
            fail("long sentence", f"{w} words: \"{s[:120]}...\"")

    # 9. Lists: three at most. The opening (the first paragraphs, up to about 40 words) fails a
    # sentence with three or more commas; in the body such sentences are listed for reading by ear.
    paras = [p.strip() for p in re.split(r"\n\s*\n", outside) if p.strip()]
    opening, ow = [], 0
    for p in paras:
        if ow >= 40:
            break
        opening.append(p); ow += count_words(p)
    open_sents = set(sentences(" ".join(opening)))
    body_lists = []
    for s_ in sentences(spoken):
        if s_.count(",") >= 3:
            if s_ in open_sents:
                fail("opening list", f"a list of more than three in the opening (three at most): \"{s_[:160]}\"")
            else:
                body_lists.append(s_[:110])
    if body_lists:
        infos.append("INFO sentences with three or more commas (read by ear: never a list of more than three): " + " | ".join(body_lists))
    counted = [p[:60] for p in paras if re.match(r"(?:the )?(?:first|second|third|fourth|fifth|sixth)\b(?: (?:thing|item|ingredient|one|material))?\s*(?:is\b|,|:)|number (?:one|two|three|four|five)\b", p, re.I)]
    if len(counted) >= 2:
        fail("counted list", "paragraphs counted off out loud like a list (walk through them instead): " + " | ".join(counted))

    # 10. Copying from a model.
    models = load_models(a.models)
    if not models:
        infos.append(f"INFO no model files found in {a.models}: copying not checked")
    allow = set()
    for keep in ch["keep"]:
        kw = norm_words(keep)
        for j in range(len(kw) - COPY_RUN + 1):
            allow.add(tuple(kw[j:j + COPY_RUN]))
    script_grams = {tuple(words[j:j + COPY_RUN]): j for j in range(len(words) - COPY_RUN + 1)}
    norm_spoken = " " + " ".join(words) + " "
    for fn, body, sig in models:
        mw = norm_words(body)
        shared = sorted({script_grams[g] for g in (tuple(mw[j:j + COPY_RUN]) for j in range(len(mw) - COPY_RUN + 1)) if g in script_grams and g not in allow})
        runs, last = [], -10
        for j in shared:
            if j > last + 1:
                runs.append([j, j])
            else:
                runs[-1][1] = j
            last = j
        for r0, r1 in runs:
            fail("copied", f"{r1 - r0 + COPY_RUN} words in a row from {fn}: \"{' '.join(words[r0:r1 + COPY_RUN])}\"")
        for phrase in sig:
            if " " + " ".join(norm_words(phrase)) + " " in norm_spoken:
                fail("model's phrase", f"{fn}'s signature phrase: \"{phrase}\"")

    # 11. For reading only.
    first15 = " ".join(words[:ch["wpm"] // 4])
    infos.append(f"INFO the first 15 seconds (is the first material named?): \"{first15}\"")
    tnum = sorted(x for x in numbers_in(a.title) if x > 1)
    if tnum:
        said = [x for x in tnum if x in numbers_in(" ".join(words[:120]))]
        infos.append(f"INFO the title's number in the opening: {'yes' if said else 'no'} ({', '.join(map(str, tnum))})")
    online = [p[:50] for p in paras if re.search(r"\bonline\b|\bEtsy\b", p, re.I) and re.search(r"\bfee|\bshipping|\bpostage|\bkeeps\b|\bsell\b|\blist\b", p, re.I)]
    if len(online) > 1:
        infos.append("INFO paragraphs on selling online (say it in one place): " + " | ".join(online))
    if a.channel == "hank":
        shop = [w for w, rx in [("Biscuit", r"\bBiscuit\b"), ("coffee", r"\bcoffee\b"), ("scrap bin", r"\bscrap bin\b"), ("pencil", r"\bpencil\b"),
                                ("broom", r"\bbroom\b"), ("radio", r"\bradio\b"), ("door", r"\bdoor\b[^.]{0,30}\bsqueak|\bsqueak\w*\b"),
                                ("clamp rack", r"\bclamp rack\b"), ("calendar", r"\bcalendar\b"), ("shop vac", r"\bshop vac\b")] if re.search(rx, spoken, re.I)]
        infos.append(f"INFO shop details named: {', '.join(shop) or 'none'} (one or two if they fit; none is fine)")
    if re.search(r"\bbatch\b|\ball (?:thirty|twenty|forty|fifty|\d+)\b", spoken, re.I):
        infos.append(f"INFO 'if they all sell' said: {'yes' if re.search(r'if (?:they|all|every|the whole)[^.!?]{0,25}sells?', spoken, re.I) else 'no'} (every batch total is conditional)")
    infos.append(f"INFO {n} words, about {minutes:.1f} minutes at {ch['wpm']} words a minute")

    for line in fails + infos:
        print(line)
    print("RESULT: PASS" if not fails else f"RESULT: FAIL ({len(fails)})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
