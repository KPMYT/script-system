#!/usr/bin/env python3
"""The hard-rules check for HVAC scripts (P21, the simple way).

Usage:
    python3 check.py SCRIPT --title "LOCKED TITLE" --brief BRIEF [--channel roger-hvac] [--models DIR] [--prices FILE]

It checks only hard rules and never asks for a line to be added to meet a count:
length at the profile's words per minute, the ending, banned lines, the safety
requirements (the carbon monoxide and gas-leak steps among them), prices against
the brief and the price guide, the voice, long sentences, lists of more than three
in the opening, and copying from a model. FAIL lines must be fixed; INFO lines are
for reading only. The last line is "RESULT: PASS" or "RESULT: FAIL (n)".
"""
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MIN_MINUTES = 12
MAX_SENTENCE = 35
COPY_RUN = 8                    # words in a row shared with a model
OPENING_CAP = 150               # the opening is the first paragraph, cut at this many words

CHANNELS = {
    "roger-hvac": {
        "name": "Roger the HVAC Guy",
        # The profile leaves words per minute unset; the account counts the 12-minute minimum at 150.
        "wpm": 150,
        "tenure": 45,
        "ban": [
            (r"\broger the pipe guy\b|\bthe pipe guy\b|\bpipe guy\b|\brogerthepipeguybooks\b|\bmy plumbing channel\b", "the other Roger channel (the two channels never mention each other)"),
            (r"\bold-house fixes\b|\bone hundred old-house\b|\b100 old-house\b|\bmy book\b|\be-?book\b", "a book (this channel has none)"),
            (r"\bmy (?:wife|husband|son|daughter|kids|grandkids|grandchildren|father|dad|mother|mom|brother|sister|family|truck|van|shop)\b", "a personal detail the profile doesn't allow (only the filter check with his coffee)"),
        ],
    },
}

BAN = [
    (r"\btoday,? (?:we'?re|we are|I'?m|I am) going to\b|\bthis channel (?:is for|exists|is all about)\b|\bwelcome (?:back|to) (?:the|my) channel\b|\b(?:hey|hi|hello) (?:guys|folks|everybody|everyone)\b", "a greeting, channel intro or 'today we're going to'"),
    (r"\bstay tuned\b|\bstick (?:around|with me)\b|\bstay (?:till|until|to) the end\b|\bby the end of (?:this|the) video\b|\bwe'll get to (?:that|it)\b|\bcoming up (?:next|later)\b|\bstill to come\b|\blater in (?:this|the) video\b", "a vague tease"),
    (r"\b(?:to|let'?s|quick) recap\b|\bto sum (?:it )?up\b|\btonight'?s homework\b|\byour homework\b", "a recap or homework list"),
    (r"\bI(?:'ve| have)? (?:tested|tried|ran (?:a |the |some |my )?tests?)\b|\bmy (?:own )?(?:test|tests|testing|results)\b|\bwatch me\b", "a first-person test or demonstration"),
    (r"\bas you can see\b|\blook at this\b|\blook at the \w+(?: \w+)? on the (?:left|right)\b|\bright here (?:on|in) (?:the|this) (?:screen|picture|video)\b|\bin this picture\b", "pointing at the screen"),
    (r"\bmy customers?\b|\ba customer (?:of mine|called|told|once)\b|\bI had a (?:customer|lady|guy|fella|homeowner)\b|\bcustomers? (?:tell|told|ask|asked) me\b|\bthe worst (?:one|furnace|unit) (?:I|we) ever\b", "a customer story or claimed experience"),
    (r"\bnot a scam\b|\bisn'?t the scam\b|\bjust (?:plain )?(?:economics|arithmetic)\b|\bno conspiracy\b|\bgrab it now or later\b|\byour (?:wallet|furnace|system|unit|AC|air conditioner|heat pump|blower|filter) will thank you\b|\b(?:just )?(?:do not|don'?t) volunteer it\b|\bif (?:you'?re|you are) finding this helpful\b|\blet'?s (?:continue|keep going)\b|\bcommon problems you might run into\b|\bif you take one thing (?:away )?from this\b", "a template stock line"),
    (r"\bkeep your cool\b|\bsame companies\b|\bnone of this is hidden\b|\bif this (?:video )?saved you (?:a|the|one) (?:call|visit|service call|trip)\b|\bargue against myself\b", "the faceless leader's catchphrase (Ray Dutton)"),
    (r"\bscam\b|\bripp(?:ing|ed) (?:you|people|folks) off\b|\bgreed(?:y)?\b", "the trade's motives (say the price and the silence as facts)"),
    (r"\blet me know if you\b", "'let me know if you' (a chatbot leftover: ask outright)"),
    (r"\bhorror movie\b|\bbrutal tests?\b", "hype that got mocked"),
    (r"\b(?:damn|hell|crap|shit|ass)\b", "swearing"),
    (r"\bguarantee[sd]?\b[^.!?]{0,40}\bsav|\b(?:saves|will save) you (?:about |up to |over )?(?:\$\d|[\w-]+ (?:hundred|thousand)\b)", "a guaranteed saving (say 'can save you the visit')"),
    (r"\b911\b", "'911' in digits (write 'nine-one-one': a voice can read it 'nine eleven')"),
    (r"(?-i:\bCO\b)", "'CO' (write 'carbon monoxide')"),
    (r"\bR-?\d{2,3}[A-Za-z]?\b", "a refrigerant written as a code (write 'R-twenty-two', 'R-four-ten-A')"),
    (r"\b\d[\d,]*(?:\.\d+)?\s?(?-i:V|A|W|kW|kWh|Hz|VA|BTUh?|F)\b", "a unit written as a symbol (write 'twenty-four volts')"),
    (r"(?<![\w-])\$?\d[\d,]*\s?-\s?\$?\d", "a range written with a hyphen (write '$75 to $200')"),
    (r"\b[A-Za-z]+/[A-Za-z]+\b", "a slash between words (write 'heating and cooling')"),
]
OPENING_BAN = [
    (r"\btoday,? (?:you(?:'ll| will)? (?:learn|see|find out)|I(?:'ll| will) show you|we(?:'ll| will) (?:learn|look at|fix))\b|\bin (?:this|today'?s) video\b", "'today you learn' or 'in this video' in the opening"),
    (r"\b(?:you(?:'ll| will)|I(?:'ll| will)|we(?:'ll| will))\b[^.!?]{0,40}\bin (?:the next )?(?:a few|two|three|five|ten|\d+|sixty|ninety) (?:minutes?|seconds?)\b", "a promise with a time on it"),
    (r"\bcarbon monoxide\b|\bgas leak\b", "carbon monoxide or a gas leak in the opening (a safety line, never the hook)"),
]
OPENING_PROMISE = r"\byou(?:'ll| will) (?:hear|see|learn|know|find out|get)\b|\bI(?:'ll| will) (?:show|tell|teach|give)\b|\b(?:and|but) (?:that|this) comes (?:at|later)\b"
NO_TECH = r"\bnothing (?:here|in this (?:video|one)) needs a (?:tech|technician|pro)\b|\byou(?:'ll| will) never (?:need|call) (?:a tech|an HVAC (?:company|tech|guy))\b|\bno tech needed\b"
CALL_POINT = r"\bthat'?s a call\b|\bcall a tech\b|\b(?:a|the) tech you trust\b|\bcall (?:an?|the) (?:HVAC |trained )?(?:tech|technician|pro)\b"
ONCE = ["between you and me", "ask me how I know", r"here(?:'?s| is) the part (?:people skip|nobody tells you)",
        r"I(?:'?ll| will) be (?:straight|square|honest) with you", r"that(?:'?s| is) the whole (?:trick|method|job|game)",
        "in your pocket", r"which (?:brings us|leaves)", r"hold that thought|put a pin in", "the big one", "the real kicker",
        r"quick (?:thing|pause|one)", "no shame in", "full stop", "trust me", "absolutely criminal", "quietly",
        r"nine (?:times )?out of (?:10|ten)"]

# Safety. (trigger, requirement, why): when the trigger is in the script, the requirement must be too.
CO = r"carbon monoxide (?:alarm|detector)s?\b[^.!?]{0,40}?\b(?:goes off|go off|went off|going off|sounds?|sounding)\b"
GAS = r"\bsmell(?:s|ing)? (?:of )?gas\b|\bgas leak\b"
REQUIRE = [
    (CO, r"\bignore\b", "carbon monoxide alarm: never ignore it or hunt for the source"),
    (CO, r"\boutside\b|\bfresh air\b|\boutdoors\b", "carbon monoxide alarm: everyone out, outside"),
    (CO, r"\bcount heads\b|\bhead ?count\b|\bevery (?:person|one|body)\b[^.!?]{0,40}\bout\b", "carbon monoxide alarm: count heads"),
    (CO, r"\bnine-one-one\b|\bfire department\b", "carbon monoxide alarm: call nine-one-one or the fire department from outside"),
    (CO, r"\bstay out\b|\b(?:don't|do not) go back in\b|\buntil [^.!?]{0,50}\bsafe\b", "carbon monoxide alarm: stay out until they say it's safe"),
    (CO, r"\banother appliance\b|\bany (?:other )?appliance\b|\bor an appliance\b|\bwhatever appliance\b|\bother appliance\b", "carbon monoxide alarm: the furnace or another appliance stays off until a trained tech fixes it (shorter, never narrower)"),
    (CO, r"\bmedical\b|\bdoctor\b|\bemergency room\b", "carbon monoxide alarm: medical help for anyone who feels sick"),
    (GAS, r"\bget (?:everyone|everybody) out\b|\bleave the house\b|\bget out of the house\b", "gas leak: everyone out now, on foot"),
    (GAS, r"\blight switch", "gas leak: no light switch"),
    (GAS, r"\bphone\b", "gas leak: no phone inside"),
    (GAS, r"\bgarage door\b", "gas leak: no garage door opener"),
    (GAS, r"\blight anything\b|\bflame\b|\bmatch(?:es)?\b|\blighter\b", "gas leak: don't light anything"),
    (GAS, r"\bstart the car\b|\bcar\b|\bengine\b", "gas leak: don't start the car"),
    (GAS, r"\bgas company\b|\butility\b", "gas leak: call nine-one-one and the gas company once well away"),
    (GAS, r"\bassume\b", "gas leak: never assume someone else called"),
    (GAS, r"\bgo back in\b|\bback inside\b|\buntil [^.!?]{0,50}\bsafe\b", "gas leak: stay out until they say it's safe"),
    (GAS, r"\bfade\b|\bcan(?:'t|not) smell\b", "gas leak: some people can't smell it, and the smell can fade"),
    (GAS, r"\bnine-one-one\b", "gas leak: call nine-one-one"),
]
PANEL_OFF = r"\b(?:door|panel|cover)s? (?:comes?|has to come|can come|coming) off\b|\b(?:take|pull|lift|get) (?:the |that |your )?(?:cabinet |furnace |front |access |burner )?(?:door|panel|cover) off\b|\b(?:remove|open) (?:the |that |your )?(?:cabinet|access panel|furnace door|burner cover)\b|\bdoor off\b"
TESTER = r"\b(?:non-contact )?(?:voltage )?tester\b"
TRIED_LIVE = r"\bknow (?:is|it'?s) (?:live|working|on)\b|\bknown live\b|\bsomething live\b|\blive outlet\b|\blamp (?:that'?s|that is) on\b|\b(?:an outlet|a lamp)[^.!?]{0,30}\b(?:you know|working|live|on)\b"
TEST_WHERE = r"\b(?:power )?(?:cable|cord)\b|\bwires? (?:going |running |that run |coming )?(?:into|in to|to|in) the (?:furnace|cabinet|unit|switch|control)\b|\b(?:switch|junction) box\b|\bwhere the power (?:comes|goes) in\b|\bthe (?:supply|feed|incoming) (?:wires?|line)\b"
POWER_OFF = r"\b(?:power|furnace|service) switch\b[^.!?]{0,30}\boff\b|\bflip it off\b|\bswitch (?:it )?off\b|\b(?:turn|shut|cut|kill) (?:off )?(?:the |your )?(?:power|breaker|disconnect)\b|\bpower(?:'s| is)? off\b|\bdisconnect (?:off|out)\b"
POWER_ON = r"\bpower (?:switch )?back on\b|\bswitch (?:it )?back on\b|\b(?:flip|turn) (?:the |your )?(?:power |furnace |service )?(?:switch |power |breaker )?back on\b|\bpower (?:goes|comes) back on\b|\bbring (?:the furnace|it) back up\b"
DEFAULTS = [
    (r"\bbleach\b(?=[\s\S]*\b(?:vinegar|ammonia)\b)|\b(?:vinegar|ammonia)\b(?=[\s\S]*\bbleach\b)",
     r"\bnever mix\b|\bnever bleach with\b|\bone cleaner at a time\b|\b(?:don't|do not) mix\b|\bnever (?:put|use) (?:bleach|them) (?:together|with)\b", "bleach and vinegar or ammonia: one cleaner at a time, never mixed"),
    (r"\b(?:condensate )?trap\b[^.!?]{0,80}\b(?:clean|rinse|flush|empt|remov|vinegar|off)\w*|\b(?:clean|rinse|flush|empt|remov)\w*[^.!?]{0,60}\btrap\b",
     r"\b(?:refill|fill|top(?:ped)? up)\b[^.!?]{0,40}\btrap\b|\btrap\b[^.!?]{0,40}\b(?:full|refill|refilled|filled|topped up)\b", "after cleaning a condensate trap, refill it with water"),
    (r"\bpressure[- ]switch hoses?\b|\binducer\b(?=[\s\S]*\b(?:pour|vinegar|cleaner)\b)",
     r"\b(?:nothing|never|don'?t|do not)\b[^.!?]{0,60}\b(?:hoses?|inducer)\b|\b(?:hoses?|inducer)\b[^.!?]{0,40}\bnothing\b|^(?=[\s\S]*\bnothing goes in (?:those|them)\b)", "nothing poured into the pressure-switch hoses or the inducer"),
    (r"\b(?:pressure|limit|rollout|float|high-limit) switch\b",
     r"\b(?:never|don'?t|do not)\b[^.!?]{0,40}\bbypass\b", "a safety switch named: never bypass it"),
    (r"\bcapacitors?\b", r"\b(?:holds?|hold on to|keeps?) (?:a |its )?charge\b|\bstay(?:s)? charged\b|\bstill (?:be )?charged\b", "capacitors hold a charge (a tech's job unless the brief gives a safe, named procedure)"),
    (r"\bcoils?\b[^.!?]{0,60}\b(?:pressure|power)[- ]wash|\b(?:pressure|power)[- ]wash\w*[^.!?]{0,60}\bcoils?\b", r"\bnever\b[^.!?]{0,40}\b(?:pressure|power)[- ]wash|\b(?:don't|do not)\b[^.!?]{0,40}\b(?:pressure|power)[- ]wash", "never pressure-wash the coils"),
    (r"\bspace heaters?\b", r"\bwall outlet\b", "space heaters plugged straight into a wall outlet, never a power strip or extension cord"),
    (r"\bspace heaters?\b", r"\bthree feet\b|\b3 feet\b", "space heaters three feet clear"),
    (r"\bgenerator\b|\b(?:run|running|idle|idling) (?:the |your )?car\b", r"\btwenty feet\b|\b20 feet\b", "a car or generator at least twenty feet from doors, windows and vents"),
    (r"\bgenerator\b|\b(?:run|running|idle|idling) (?:the |your )?car\b", r"\bgarage\b", "never a car or generator in a garage, even with the door open"),
    (r"\bgenerator\b", r"\bbackfeed\w*\b|\btransfer switch\b|\binterlock\b|\bwall outlet\b", "a generator never backfed into the house wiring"),
    (r"\b(?:air[- ]seal\w*|seal(?:ing)? (?:the |those |up )?(?:air )?leaks|weatherstrip\w*|caulk\w*)\b(?=[\s\S]*\b(?:chimney|natural-draft|water heater)\b)",
     r"\bcombustion\b|\bdraft test\b", "air sealing near a chimney-vented furnace or water heater needs a combustion (draft) test"),
    (r"\bdamper\b", r"\bfully out\b|\bcold\b", "the fireplace damper closes only when the fire is fully out and cold"),
]
REFRIGERANT_DIY = r"\b(?:add|adding|top(?:ping)? (?:it )?up|recharg\w*|charg(?:e|ing))\b[^.!?]{0,30}\b(?:refrigerant|freon)\b|\b(?:refrigerant|freon)\b[^.!?]{0,20}\b(?:top(?:ping)? (?:it )?up|recharg\w*)\b"

UNITS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: 10 * (i + 2) for i, w in enumerate("twenty thirty forty fifty sixty seventy eighty ninety".split())}
SCALES = {"hundred": 100, "thousand": 1000}


def numbers_in(text):
    """Every number in the text, from digits and from number words ('a hundred', 'thirteen hundred')."""
    found = set()
    for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", text):
        try:
            found.add(int(float(m.group().replace(",", ""))))
        except ValueError:
            pass
    tokens = re.findall(r"[a-z]+", text.lower().replace("-", " "))
    cur, total, active = 0, 0, False
    for i, t in enumerate(tokens + ["."]):
        nxt = tokens[i + 1] if i + 1 < len(tokens) else ""
        if t == "a" and nxt in SCALES and not active:
            cur, active = 1, True
        elif t in UNITS:
            cur += UNITS[t]; active = True
        elif t in TENS:
            cur += TENS[t]; active = True
        elif t in SCALES and active:
            if t == "hundred":
                cur = (cur or 1) * 100
            else:
                total += (cur or 1) * 1000; cur = 0
        elif t == "and" and active and nxt in UNITS | TENS.keys():
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


def list_items(sentence):
    """How many items the longest 'a, b, and c' run in a sentence holds (0 when there is none)."""
    segs = [s.strip() for s in sentence.rstrip(".!?").split(",")]
    best = 0
    for last in range(1, len(segs)):
        if not re.match(r"(?:and|or)\b", segs[last], re.I) or len(segs[last].split()) > 6:
            continue
        items, j = 1, last - 1
        while j >= 0 and len(segs[j].split()) <= 4:
            items += 1
            if re.match(r"(?:and|or|but|so|then)\b", segs[j], re.I):
                break
            j -= 1
        best = max(best, items)
    return best


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
            sig = re.findall(r'"([^"]{8,})"', m.group(1))
        models.append((fn, body, sig))
    return models


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--channel", default="roger-hvac", choices=sorted(CHANNELS))
    ap.add_argument("--title", required=True)
    ap.add_argument("--brief", required=True)
    ap.add_argument("--models", default=os.path.join(HERE, "references", "models"))
    ap.add_argument("--prices", default=os.path.join(HERE, "references", "price-guide.md"))
    a = ap.parse_args()
    ch = CHANNELS[a.channel]
    raw = open(a.script, encoding="utf-8").read()
    brief = open(a.brief, encoding="utf-8").read()
    guide = open(a.prices, encoding="utf-8").read() if os.path.isfile(a.prices) else ""
    fails, infos = [], []

    def fail(rule, detail=""):
        fails.append(f"FAIL {rule}" + (f": {detail}" if detail else ""))

    if not guide:
        infos.append(f"INFO no price guide at {a.prices}: prices checked against the brief only")

    # Keep only the script if a whole output was pasted, and drop a TEST label line.
    raw = re.sub(r"^\s*SCRIPT TYPE:[^\n]*\n", "", raw)
    raw = re.split(r"\n\s*(?:CHECK:|VO COPY|WORD COUNT|Word count:)", raw)[0]
    m = re.match(r"\s*(TEST\b[^\n]*)\n", raw)
    if m:
        infos.append(f"INFO label line left out of the count: \"{m.group(1)[:80]}\"")
        raw = raw[m.end():]
    spoken = raw.strip()
    paras = [p.strip() for p in re.split(r"\n\s*\n", spoken) if p.strip()]
    lines = spoken.split("\n")
    words = norm_words(spoken)
    n = len(words)
    sents = sentences(spoken)

    # 1. Classic: no markers.
    for i, line in enumerate(lines, 1):
        if "===" in line:
            fail("markers", f"a CTA marker on line {i}; Roger the HVAC Guy is Classic, with no markers")

    # 2. Length at the profile's words per minute.
    minutes = n / ch["wpm"]
    need = MIN_MINUTES * ch["wpm"]
    if n < need:
        fail("length", f"{n} words, about {minutes:.1f} minutes at {ch['wpm']}; needs at least {need} (12 minutes). Add real help from the brief, never filler")
    elif minutes > 20:
        infos.append(f"INFO {minutes:.1f} minutes: past 20 (12 to 20 is the range); cut repetition if any")

    # 3. The ending: one subscribe line naming the channel, then the comment ask, then nothing.
    subs = [i for i, s in enumerate(sents) if re.search(r"\bsubscrib", s, re.I)]
    if not subs:
        fail("ending", f"no subscribe line (one line at the end, naming {ch['name']})")
    else:
        if len(subs) > 1:
            fail("ending", "the subscribe ask said more than once (one line, at the end only)")
        k = subs[-1]
        sub_s = sents[k]
        before = len(norm_words(" ".join(sents[:k])))
        if before < 0.85 * n:
            fail("ending", f"the subscribe line sits {100 * before // max(n, 1)}% in: no mid-video ask, it goes at the end")
        if not re.search(re.escape(ch["name"]), sub_s, re.I):
            fail("ending", f"the subscribe line doesn't name {ch['name']}: \"{sub_s[:120]}\"")
        tail = sents[k + 1:]
        tail_text = " ".join(tail)
        if not re.search(r"\bcomments?\b", tail_text, re.I):
            fail("ending", "after the subscribe line, an outright ask to comment ('in the comments', 'leave me a comment')")
        if not re.search(r"\bI read every one\b", tail_text, re.I):
            fail("ending", "the comment ask ends with 'I read every one.'")
        if len(tail) > 4:
            fail("ending", f"{len(tail)} sentences after the subscribe line: only the comment ask (two or three sentences), then stop")
        if tail and not re.search(r"\bI read every one\b", tail[-1], re.I):
            fail("ending", f"something after the comment ask: \"{tail[-1][:120]}\"")
        if tail:
            infos.append(f"INFO the comment question (about their own house or numbers? not the same as an earlier script in this chat?): \"{tail_text[:200]}\"")
        if k >= 1:
            infos.append(f"INFO the line before the subscribe ask (relief and one small thing for tonight, never a list): \"{sents[k - 1][:160]}\"")

    # 4. Banned lines.
    for rx, why in BAN + ch["ban"]:
        for mm in re.finditer(rx, spoken, re.I):
            fail("banned", f"{why}: \"{sentence_with(spoken, mm.start())}\"")
    name_hits = [mm for mm in re.finditer(r"\bRoger\b|\bI'?m Roger\b", spoken)]
    for mm in name_hits:
        s = sentence_with(spoken, mm.start())
        if not re.search(r"\bsubscrib", s, re.I):
            fail("banned", f"the name outside the subscribe line: \"{s}\"")
    if re.search(NO_TECH, spoken, re.I) and re.search(CALL_POINT, spoken, re.I):
        fail("scope", "'nothing here needs a tech' (or the like) while a step ends in a call")
    for rx, label in [(r"\b(?:forty-five|45) years\b", "forty-five years")]:
        k = len(re.findall(rx, spoken, re.I))
        if k > 1:
            fail("tenure", f"{label} said {k} times; at most once, where it backs a verdict")
    title_years = numbers_in(a.title)

    # Tenure said with "been", "spent" or "worked" (main session, 2026-11-06: the old scanner caught these).
    for mm in re.finditer(r"\b(?:I(?:'ve| have)? been|been at (?:it|this)|I(?:'ve| have) (?:spent|worked))\b[^.!?]{0,40}?\b((?:(?:twenty|thirty|forty|fifty|sixty)[- ])?[\w]+)\s+years\b", spoken, re.I):
        got = numbers_in(mm.group(1))
        if got and not got <= ({ch["tenure"]} | title_years):
            fail("tenure", f"a tenure number other than the channel's or the title's: \"{sentence_with(spoken, mm.start())}\"")
    for mm in re.finditer(r"\b([\w-]+(?: [\w-]+)?) years (?:in (?:the|this) trade|of (?:experience|doing this|HVAC))\b", spoken, re.I):
        got = numbers_in(mm.group(1))
        if got and not got <= ({ch["tenure"]} | title_years):
            fail("tenure", f"a tenure number other than {ch['tenure']} or the title's: \"{sentence_with(spoken, mm.start())}\"")
    for mm in re.finditer(REFRIGERANT_DIY, spoken, re.I):
        s = sentence_with(spoken, mm.start())
        if not re.search(r"\bnever\b|\bdon'?t\b|\bdo not\b|\blicensed\b|\bcertified\b|\btech\b", s, re.I):
            fail("safety", f"refrigerant work as the viewer's job (licensed work only): \"{s}\"")

    # 5. The opening: the first paragraph, cut at OPENING_CAP words.
    opening = paras[0] if paras else ""
    ow = norm_words(opening)
    if len(ow) > OPENING_CAP:
        opening = " ".join(opening.split()[:OPENING_CAP])
        ow = ow[:OPENING_CAP]
    for rx, why in OPENING_BAN:
        for mm in re.finditer(rx, opening, re.I):
            fail("opening", f"{why}: \"{sentence_with(opening, mm.start())}\"")
    promises = re.findall(OPENING_PROMISE, opening, re.I)
    if len(promises) > 1:
        fail("opening", f"{len(promises)} promises in the opening; one at most, and only one the end of the video pays")
    for s in sentences(opening):
        k = list_items(s)
        if k > 3:
            fail("opening list", f"a list of {k} in the opening (three at most): \"{s[:160]}\"")
    infos.append(f"INFO the opening (first paragraph): {len(ow)} words, about {len(ow) * 60 // ch['wpm']} seconds; the first real step by about 45 seconds (about {45 * ch['wpm'] // 60} words), as short as the model's opening")
    dollars_open = len(re.findall(r"\$\d|\bdollars?\b|\bbucks\b", opening, re.I))
    if dollars_open > 1:
        infos.append(f"INFO {dollars_open} prices in the opening (prices belong to the steps; one at most, if any)")

    # 6. Safety requirements.
    for trigger, req, why in REQUIRE:
        mm = re.search(trigger, spoken, re.I)
        if mm and not re.search(req, spoken, re.I):
            fail("safety", f"{why}: \"{sentence_with(spoken, mm.start())}\"")
    for trigger, req, why in DEFAULTS:
        mm = re.search(trigger, spoken, re.I)
        if mm and not re.search(req, spoken, re.I | re.M):
            if re.search(trigger, brief, re.I) and not re.search(req, brief, re.I | re.M) and re.search(r"\bcapacitor", why):
                infos.append(f"INFO {why}: the brief covers it without this line; the brief wins, check by eye")
            else:
                fail("safety", f"{why}: \"{sentence_with(spoken, mm.start())}\"")
    po = re.search(PANEL_OFF, spoken, re.I)
    if po:
        if not re.search(TESTER, spoken, re.I):
            fail("safety", f"a panel or door comes off with no non-contact tester proving the power off: \"{sentence_with(spoken, po.start())}\"")
        else:
            if not re.search(TRIED_LIVE, spoken, re.I):
                fail("safety", "the tester isn't tried first on something known to be live")
            ok = False
            idx = [i for i, s in enumerate(sents) if re.search(TESTER, s, re.I)]
            for i in idx:
                win = " ".join(sents[i:i + 4])
                win = re.sub(r"\bnear a live wire\b|\blive wires?\b", "", win, flags=re.I)
                if re.search(TEST_WHERE, win, re.I):
                    ok = True
            if not ok:
                fail("safety", "the tester step doesn't say where to hold it on the furnace (the power cable at the switch, or the wires going into the cabinet)")
        if not re.search(POWER_ON, spoken, re.I):
            fail("safety", "the power goes off but the script never says how it comes back on")
    # Carbon monoxide steps never inside a hands-on sequence (between power off and power back on).
    offs = [mm.start() for mm in re.finditer(POWER_OFF, spoken, re.I)]
    # "Before the power goes back on" names the restart; it isn't one.
    ons = [mm.start() for mm in re.finditer(POWER_ON, spoken, re.I)
           if not re.search(r"\b(?:before|until|till)\b[^.!?]{0,12}$", spoken[max(0, mm.start() - 25):mm.start()], re.I)]
    for mm in re.finditer(CO, spoken, re.I):
        prior_off = [o for o in offs if o < mm.start()]
        if prior_off and any(o > mm.start() for o in ons) and not any(prior_off[-1] < o < mm.start() for o in ons):
            fail("safety placement", f"the carbon monoxide alarm steps sit inside the hands-on job, between power off and power back on: \"{sentence_with(spoken, mm.start())}\"")
    # A check made during the job, said after the restart.
    if ons:
        for mm in re.finditer(r"\bwhile (?:you'?re|you are) (?:flushing|pouring|rinsing|draining|cleaning|waiting)\b|\bduring the (?:flush|rinse|pour)\b", spoken, re.I):
            if mm.start() > ons[0]:
                fail("order", f"an instruction for during the job comes after the power is back on: \"{sentence_with(spoken, mm.start())}\"")
    # Poured at a cleanout or vent tee, it runs down the line, not back through the trap.
    if re.search(r"\bcleanout\b|\bvent tee\b", spoken, re.I):
        for mm in re.finditer(r"\b(?:through|across) the trap\b", spoken, re.I):
            s = sentence_with(spoken, mm.start())
            if re.search(r"\bpour|\bvinegar\b|\bworking\b|\brunning\b|\bflush", s, re.I):
                fail("accuracy", f"poured at a cleanout or vent tee, it treats the line, not the trap: say 'down the line': \"{s}\"")

    # 7. Prices against the brief and the price guide.
    allowed = numbers_in(brief) | numbers_in(guide) | numbers_in(a.title)
    for mm in re.finditer(r"\$\s?\d[\d,]*(?:\.\d+)?|\b(?:dollars?|bucks|cents?)\b", spoken, re.I):
        s = sentence_with(spoken, mm.start())
        if re.match(r"\$", mm.group()):
            if "." in mm.group():
                fail("money", f"a price in cents (round it): \"{s}\"")
            got = numbers_in(mm.group())
        else:
            left = spoken[max(0, mm.start() - 90):mm.start()]
            left = re.split(r"[.!?,;:]", left)[-1]
            got = {x for x in numbers_in(left) if x > 0}
            if mm.group().lower().startswith("cent") and not re.search(r"\ba (?:month|year|week|day|use|cup|dose|load)\b|\bper\b|\beach (?:time|month|cup|use|dose|load)\b", s, re.I):
                fail("money", f"cents outside a cost per use: \"{s}\"")
        extra = got - allowed
        if extra:
            fail("money", f"a price not in the brief or the price guide ({', '.join(map(str, sorted(extra)))}): \"{s}\"")
    for s in sents:
        if re.search(r"\bper ?cent\b|%|\b\w+ out of (?:every )?(?:\d+|two|three|four|five|six|ten|a hundred)\b|\bsurvey\b|\bstudy\b|\btimes more\b", s, re.I):
            extra = {x for x in numbers_in(s) if x > 1} - allowed
            if extra:
                fail("numbers", f"a figure not in the brief or the price guide ({', '.join(map(str, sorted(extra)))}): \"{s[:160]}\"")
    other = sorted(x for x in numbers_in(spoken) - allowed if x > 12)
    if other:
        infos.append(f"INFO numbers in neither the brief nor the price guide (each must be everyday knowledge, never a claim): {', '.join(map(str, other))}")

    # 8. The voice.
    for i, line in enumerate(lines, 1):
        for pat, why in [(r"[%&+#=~@°\\|*_<>{}\[\]()]", "a symbol, bracket or label"),
                         (r"[—–]", "a dash"), (r"[‘’“”]", "a curly quote"),
                         (r"\b(?:haha|hmm+|ugh)\b", "a sound written as a word"),
                         (r"[\U0001F300-\U0001FAFF☀-➿]", "an emoji")]:
            mm = re.search(pat, line, re.I)
            if mm:
                fail("voice", f"{why} '{mm.group()}' on line {i}: \"{line.strip()[:100]}\"")
        if re.match(r"^\s*(?:#|[A-Z][A-Za-z ]{0,30}:\s*$)", line):
            fail("voice", f"a heading or label on line {i}: \"{line.strip()[:80]}\"")
    for s in sents:
        w = len(norm_words(s))
        if w > MAX_SENTENCE:
            fail("long sentence", f"{w} words: \"{s[:120]}...\"")
    body_lists = [s[:110] for s in sents if list_items(s) > 3 and s not in sentences(opening)]
    if body_lists:
        infos.append("INFO lists of four or more in the body (read by ear: pick three, or split them): " + " | ".join(body_lists))

    # 9. Copying from a model.
    models = load_models(a.models)
    if not models:
        infos.append(f"INFO no model files found in {a.models}: copying not checked")
    script_grams = {tuple(words[j:j + COPY_RUN]): j for j in range(len(words) - COPY_RUN + 1)}
    norm_spoken = " ".join(words)
    for fn, body, sig in models:
        mw = norm_words(body)
        shared = sorted({script_grams[g] for g in (tuple(mw[j:j + COPY_RUN]) for j in range(len(mw) - COPY_RUN + 1)) if g in script_grams})
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
            if " ".join(norm_words(phrase)) in norm_spoken:
                fail("model's phrase", f"{fn}'s signature phrase: \"{phrase}\"")

    # 10. For reading only.
    rep = []
    for phrase in ONCE:
        k = len(re.findall(r"\b" + phrase + r"\b", spoken, re.I))
        if k > 1:
            rep.append(f"'{phrase}' {k}")
    grams = collections.Counter(" ".join(words[j:j + 4]) for j in range(len(words) - 3))
    tics = [f"'{g}' {c}" for g, c in grams.most_common(8) if c >= 3 and not re.search(r"\b(?:the|a|of|to|and|you|it|that|in|is)\b(?: \b(?:the|a|of|to|and|you|it|that|in|is)\b){2,}", g)]
    if rep or tics:
        infos.append("INFO phrases that come back (a phrase is voice once, a tic when it repeats): " + ", ".join(rep + tics[:6]))
    if re.search(r"\bfilter\b[^.!?]{0,80}\bcoffee\b|\bcoffee\b[^.!?]{0,80}\bfilter\b", spoken, re.I):
        infos.append("INFO his filter-and-coffee habit is used (optional; only where it helps)")
    infos.append(f"INFO {n} words, about {minutes:.1f} minutes at {ch['wpm']} words a minute (the profile's words per minute is unset; 150 is the account's figure)")

    fails = list(dict.fromkeys(fails))
    for line in fails + infos:
        print(line)
    print("RESULT: PASS" if not fails else f"RESULT: FAIL ({len(fails)})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
