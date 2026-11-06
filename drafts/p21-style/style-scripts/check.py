#!/usr/bin/env python3
"""The hard-rules check for style scripts (P21, the simple way).

Usage:
    python3 check.py SCRIPT --channel scarlett|diane --title "LOCKED TITLE" --brief BRIEF [--models DIR]

It checks only hard rules and never asks for a line to be added to meet a count:
length, the two book blocks and their markers, the ending and the sign-off,
banned lines, the safety lines, numbers against the brief, the voice, and
copying from a model. FAIL lines must be fixed; INFO lines are for reading only.
The last line is "RESULT: PASS" or "RESULT: FAIL (n)".
"""
import argparse
import os
import re
import sys

MIN_WORDS, MAX_WORDS = 2100, 2700
MID_MIN, MID_MAX = 50, 100      # the page says 60 to 90; a little slack before failing
MAX_SENTENCE = 35
COPY_RUN = 8                    # words in a row shared with a model

CHANNELS = {
    "scarlett": {
        "name": "Scarlett Starling",
        "wpm": 169,
        "printed": "300 Budget-Friendly Ways to Look Expensive",
        "spoken": r"three hundred budget-friendly ways to look expensive",
        "signoff": "Until next time, ladies, stay elegant.",
        "facts": {300, 1000, 28, 35, 61, 251, 260, 10},
        "once": [
            (r"\b(?:sixty-one|61)(?: years old)?\b", "her age"),
            (r"\ba lifetime of dressing well\b", "a lifetime of dressing well"),
        ],
        "ban": [
            (r"\bScarlett?\b|\bSt[ae]rling\b(?!\s+silver)", "the channel's name", 0),
            (r"\bmy dear friends\b|\bcherie\b|\bdarling\b", "another channel's endearment (hers is 'ladies')"),
            (r"\bstay polished\b|\bstay sterling\b", "the old sign-off"),
            (r"\bI (?:gathered|collected)\b|\bcollecting (?:those|these)\b", "the old 'I gathered' book line"),
            (r"\bClaire\b", "the book's own people", 0),
            (r"\b(?:boardroom|gala|country[- ]club)s?\b", "an invented past"),
        ],
    },
    "diane": {
        "name": "Diane de Chambray",
        "wpm": 172,
        "printed": "The French Way",
        "spoken": r"the french way",
        "signoff": "With love from Paris, my dear friends.",
        "facts": {101, 400, 40, 63, 5},
        "once": [
            (r"\b(?:sixty-three|63)(?: years old)?\b", "her age"),
        ],
        "max2": [
            (r"\bAmerican women\b", "'American women' (at most twice)"),
        ],
        "ban": [
            (r"\bDiane\b|\b[Dd]e\s+Chambray\b", "the channel's name", 0),
            (r"\bcherie\b|\bchérie\b|(?<!old )\bladies\b", "another endearment (hers is 'my dear friends')"),
            (r"\bbient[oô]t\b|\bkeep it simple,? and let them wonder\b", "the old sign-offs"),
            (r"\bnot with me\b[^.!?]{0,60}\bbelong\b|\bmy part was gathering\b", "the old book line"),
            (r"\b(?:Marie|Sophie|Claudette)\b", "the book's characters", 0),
            (r"\b(?:arrondissement|rive gauche|left bank|my apartment|my flat|my street|Saint-Germain|Marais|Montmartre)\b", "a named neighbourhood or her home"),
            (r"\bevery French woman\b|\ball French women\b|\bFrench women (?:never|always)\b|\bno French woman\b", "an unhedged claim about French women"),
            (r"\billegal in France\b|\bFrench law\b", "an invented French law"),
            (r"\b(?:twenty|20) years younger\b", "the book subtitle's claim"),
            (r"\bwe Americans\b|\bus Americans\b", "speaking from the American side"),
            (r"\bscreams?\b", "'scream'"),
        ],
    },
}

COMMON_BAN = [
    (r"\btoday we(?:'re| are) going to\b|\b(?:in|by the end of) (?:this|today'?s) video,? (?:I|we|you)(?:'ll| will| are going)\b|\bthis channel (?:is for|takes)\b|\bwelcome (?:back|to) (?:the|my) channel\b", "a channel intro or 'today we're going to'"),
    (r"\bstill ahead\b|\bwe'll get to\b|\bcoming up next\b|\bstill to come\b|\bstick around\b|\bstay tuned\b|\bthe one I promised\b|\blater in (?:this|the) video\b", "a tease"),
    (r"\b(?:to|let'?s|quick) recap\b|\bto sum (?:it )?up\b", "a recap"),
    (r"\bsubscribe\b|\bring the bell\b|\bbell icon\b|\bnotification bell\b|\blike button\b|\bhit (?:that )?like\b", "a subscribe or like ask"),
    (r"\bone of us\b|\bwomen our age\b|\bat our age\b|\bat your age\b", "'one of us', 'our age' or 'your age'"),
    (r"\bage is just a number\b|\bno (?:age limit|expiration date)\b|\byou(?:'ve| have) earned it\b|\byou deserve\b|\bnever too late\b|\belegance (?:is not|isn't) about age\b", "an age slogan"),
    (r"\bas you can see\b|\blook at this\b|\bright here (?:on|in) (?:the|this) (?:screen|picture|photo)\b", "pointing at the screen"),
    (r"\bstudies show\b|\bresearch shows\b|\b(?:psychologists|scientists|experts) say\b", "'studies show'"),
    (r"\bhere'?s the check\b|\bthe check is\b|\byour check\b", "an announced check"),
    (r"\bsmall gold hoops\b|\breads as\b|\breads (?:expensive|tired|dated|young|old|cheap)\b|\bfrom across the room\b", "an old house line"),
    (r"\bI read every\b", "'I read every one'"),
    (r"\be-?book\b", "'e-book' (say 'book')"),
    (r"\bnothing (?:about (?:it|this)|here) (?:expires|is (?:urgent|timed))\b|\bno clock on\b|\bwhenever (?:it )?suits you\b|\bno (?:rush|hurry|pressure)\b", "the old no-rush line"),
    (r"\bmy (?:mother|mom|maman|grandmother|husband|daughter|son|granddaughter|grandchildren|sister|family|aunt|friend|friends|circle)\b", "a relative or friend (none approved)"),
    (r"\bI (?:worked|designed) (?:for|at) [A-Z]\w+", "a named house or employer", 0),
    (r"\b(?:women|clients|ladies) (?:tell|say to|ask) me\b|\bmy clients?\b", "a client story or quote"),
    (r"\bdiet(?:s|ing)?\b|\bweight[- ]loss\b|\blos(?:e|ing) (?:the )?weight\b|\bcalories?\b|\bsupplements?\b", "diet or weight loss"),
    (r"\breverse aging\b|\banti-?aging\b|\bregrow(?:s|ing)? (?:your |the |new )?hair\b|\bgrows? (?:it|your hair|hair) back\b|\bbotox\b", "a medical or anti-aging claim"),
    (r"\bmutton dressed as lamb\b|\btrashy\b|\bfat\b|\bugly\b", "shaming the woman"),
    (r"\bwhich (?:one|of (?:the|these) \w+)\b[^.!?]{0,40}\b(?:first|try|trying)\b|\bwhich (?:\w+ )?(?:will|would) you try\b", "the old comment ask (ask about her instead)"),
    (r"\bfree\b[^.!?]{0,20}\b(?:book|guide|download)\b|\b(?:book|guide)\b[^.!?]{0,20}\bfree\b", "'free' with the book"),
]
HARSH = r"\bgrann(?:y|ies)\b|\bold lad(?:y|ies)\b"
CTA_BAN = r"\blook (?:\w+ )?younger\b|\banti-?aging\b|\bprice\b|\bdollars?\b|\$\d"

SAFETY = [
    (r"\bbox dye\b|\b(?:dye|colou?r)(?: (?:it|your hair))? at home\b|\bhome (?:hair )?colou?r\w*\b|\bat-home colou?r\b|\bdrugstore (?:dye|colou?r)\b",
     r"\bpatch test\b", "home hair color without a patch test"),
    (r"\bflat iron\b|\bcurling (?:iron|wand)\b|\bhot (?:tools|rollers)\b|\bheat tools?\b|\bstraightener\b|\bblow-?dry\w*\b|\bhair ?dryer\b",
     r"\bheat protect\w*\b|\blow(?:er)? (?:heat|setting|temperature)\b|\bcool(?:er)? setting\b", "heat tools without heat protectant or a lower setting"),
    (r"\bshedding\b|\bbald (?:patch|spot)\w*\b|\b(?:bald|thin) patch(?:es)?\b|\bpatchy\b|\bhair loss\b",
     r"\bdoctor\b|\bdermatologist\b", "shedding or patches without the doctor line"),
]

UNITS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: 10 * (i + 2) for i, w in enumerate("twenty thirty forty fifty sixty seventy eighty ninety".split())}
SCALES = {"hundred": 100, "thousand": 1000}


def numbers_in(text):
    """Every number in the text, from digits and from number words."""
    found = set()
    for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", text):
        try:
            found.add(int(float(m.group().replace(",", ""))))
        except ValueError:
            pass
    tokens = re.findall(r"[a-z]+", text.lower().replace("-", " "))
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
    ap.add_argument("--models", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "references", "models"))
    a = ap.parse_args()
    ch = CHANNELS[a.channel]
    raw = open(a.script, encoding="utf-8").read()
    brief = open(a.brief, encoding="utf-8").read()
    fails, infos = [], []

    def fail(rule, detail=""):
        fails.append(f"FAIL {rule}" + (f": {detail}" if detail else ""))

    # Keep only the script if a whole output was pasted.
    raw = re.sub(r"^\s*SCRIPT TYPE:[^\n]*\n", "", raw)
    raw = re.split(r"\n\s*(?:CHECK:|VO COPY)", raw)[0]
    lines = raw.strip("\n").split("\n")
    start_re = re.compile(r"^===START CTA\((.*)\)===$")

    # 1. The book blocks and their markers.
    blocks, spoken_lines, inside, cur = [], [], False, None
    for i, line in enumerate(lines):
        s = line.strip()
        if "===" in s:
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
    if len(blocks) != 2:
        fail("book blocks", f"need exactly two (mid and end), found {len(blocks)}")

    spoken = "\n".join(spoken_lines)
    words = norm_words(spoken)
    n = len(words)

    # 2. Length.
    minutes = n / ch["wpm"]
    if not MIN_WORDS <= n <= MAX_WORDS:
        fail("length", f"{n} words ({minutes:.1f} minutes at {ch['wpm']}); needs {MIN_WORDS} to {MAX_WORDS}")

    # 3. The mid book block.
    if blocks:
        mid = "\n".join(blocks[0]["lines"])
        mw = len(norm_words(mid))
        before = len(norm_words("\n".join(spoken_lines[:blocks[0]["start"]])))
        infos.append(f"INFO mid book block: {mw} words, starts at {100 * before // max(n, 1)}% of the script")
        if not MID_MIN <= mw <= MID_MAX:
            fail("mid book block length", f"{mw} words; the page says 60 to 90")
        if not re.search(ch["spoken"], mid, re.I):
            fail("mid book block", "the book's spoken title isn't said")
        if not (re.search(r"\bdescription\b", mid, re.I) and re.search(r"\bQR\b|\bcode\b", mid, re.I)):
            fail("mid book block", "say it's at the link in the description and the QR code on screen")
        for b in blocks:
            for m in re.finditer(CTA_BAN, "\n".join(b["lines"]), re.I):
                fail("book claim", f"'{m.group()}' in a book block")
    if len(blocks) >= 2:
        end = "\n".join(blocks[-1]["lines"])
        if not re.search(r"\bbook\b|" + ch["spoken"], end, re.I):
            fail("ending", "the end block has no line reminding her of the book")
        if not re.search(r"\bcomments?\b", end, re.I) or "?" not in end:
            fail("ending", "the end block needs an outright comment ask with a question about her")
        if re.search(r"\b(?:everything|all of (?:it|this)|every (?:tip|cut|color|colour|rule|piece|swap)|all (?:seven|five|ten|of these))\b[^.!?]{0,60}\b(?:book|in it|inside)\b", end, re.I):
            fail("ending", "the book line claims the whole video is in the book")
        after = [l.strip() for l in spoken_lines[blocks[-1]["end"]:] if l.strip()]
        if after != [ch["signoff"]]:
            fail("sign-off", f"after the end block there must be one line, exactly: {ch['signoff']} (found {len(after)} lines: {' / '.join(after)[:120]})")
        text_after_mid = "\n".join(spoken_lines[blocks[0]["end"]:blocks[-1]["start"]])
        if not text_after_mid.strip():
            fail("book blocks", "no video between the mid and end blocks")

    # 4. Banned lines and limits.
    for entry in COMMON_BAN + ch["ban"]:
        rx, why = entry[0], entry[1]
        flags = entry[2] if len(entry) > 2 else re.I
        for m in re.finditer(rx, spoken, flags):
            fail("banned", f"{why}: \"{sentence_with(spoken, m.start())}\"")
    for rx, why in ch.get("once", []):
        k = len(re.findall(rx, spoken, re.I))
        if k > 1:
            fail("at most once", f"{why}, said {k} times")
    for rx, why in ch.get("max2", []):
        k = len(re.findall(rx, spoken, re.I))
        if k > 2:
            fail("at most twice", f"{why}, said {k} times")
    k = len(re.findall(HARSH, spoken, re.I))
    if k > 1:
        fail("harsh word", f"'granny' or 'old lady' said {k} times; at most once, flagged as harsh")

    # 5. Safety lines.
    for trigger, need, why in SAFETY:
        m = re.search(trigger, spoken, re.I)
        if m and not re.search(need, spoken, re.I):
            fail("safety", f"{why}: \"{sentence_with(spoken, m.start())}\"")

    # 6. Numbers against the brief.
    allowed = numbers_in(brief) | numbers_in(a.title) | ch["facts"]
    budget = re.search(r"budget|cheap|afford|without spending|for less|\$|dollar|under \d", a.title, re.I)
    for m in re.finditer(r"\$\s?\d[\d,]*|\b\d[\d,]*\s?dollars?\b|\b(?:[a-z]+[- ])?(?:hundred|thousand|[a-z]+ty|ten|[a-z]+teen|one|two|three|four|five|six|seven|eight|nine)\s+(?:dollars?|bucks)\b", spoken, re.I):
        if not budget:
            fail("money", f"a price on a title that isn't about budget: \"{sentence_with(spoken, m.start())}\"")
        elif not (numbers_in(m.group()) <= allowed):
            fail("money", f"a price not in the brief: \"{sentence_with(spoken, m.start())}\"")
    for s in sentences(spoken):
        if re.search(r"\bper ?cent\b|%|\b\w+ out of (?:every )?(?:\d+|two|three|four|five|ten|a hundred)\b|\bsurvey\b|\bstudy\b|\btimes more\b", s, re.I):
            extra = {x for x in numbers_in(s) if x > 1} - allowed
            if extra:
                fail("numbers", f"a figure not in the brief ({', '.join(map(str, sorted(extra)))}): \"{s[:160]}\"")
    other = sorted(x for x in numbers_in(spoken) - allowed if x > 12)
    if other:
        infos.append(f"INFO numbers not in the brief (check each is plain sense, not a claim): {', '.join(map(str, other))}")

    # 7. The voice.
    for i, line in enumerate(spoken_lines, 1):
        for pat, why in [(r"[%&+#=~@°/\\|*_<>{}\[\]()]", "a symbol, bracket or label"),
                         (r"[—–]", "a dash"), (r"[‘’“”]", "a curly quote"),
                         (r"\b\d+\s?x\s?\d+\b", "a size with an x"), (r"\b(?:haha|hmm+|ugh)\b", "a sound written as a word"),
                         (r"[\U0001F300-\U0001FAFF☀-➿]", "an emoji")]:
            m = re.search(pat, line, re.I)
            if m:
                fail("voice", f"{why} '{m.group()}' on line {i}: \"{line.strip()[:100]}\"")
        if re.match(r"^\s*(?:#|[A-Z][A-Za-z ]{0,30}:\s*$)", line):
            fail("voice", f"a heading or label on line {i}: \"{line.strip()[:80]}\"")
    for s in sentences(spoken):
        w = len(norm_words(s))
        if w > MAX_SENTENCE:
            fail("long sentence", f"{w} words: \"{s[:120]}...\"")

    # 7b. Lists: three at most (operator, 2026-11-06). The hook fails a sentence with three or more
    # commas; in the body such sentences are listed for reading by ear.
    sents = sentences(spoken)
    seen, body_lists = 0, []
    for s_ in sents:
        in_hook = seen < 150 and not re.search(r"\bnumber one\b", " ".join(norm_words(" ".join(sents[:sents.index(s_)]))))
        if s_.count(",") >= 3:
            if in_hook:
                fail("hook list", f"a list of more than three in the hook (three at most): \"{s_[:160]}\"")
            else:
                body_lists.append(s_[:110])
        seen += len(norm_words(s_))
    if body_lists:
        infos.append("INFO sentences with three or more commas (read by ear: never a list of more than three): " + " | ".join(body_lists))

    # 8. Copying from a model.
    models = load_models(a.models)
    if not models:
        infos.append(f"INFO no model files found in {a.models}: copying not checked")
    allow = set()
    for keep in (ch["spoken"], ch["signoff"]):
        kw = norm_words(keep)
        for j in range(len(kw) - COPY_RUN + 1):
            allow.add(tuple(kw[j:j + COPY_RUN]))
    script_grams = {tuple(words[j:j + COPY_RUN]): j for j in range(len(words) - COPY_RUN + 1)}
    norm_spoken = " ".join(words)
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
            if " ".join(norm_words(phrase)) in norm_spoken:
                fail("model's phrase", f"{fn}'s signature phrase: \"{phrase}\"")

    # 9. For reading only.
    m1 = re.search(r"\bnumber one\b|\bthe first (?:cut|color|colour|mistake|rule|piece|thing|one)\b", " ".join(words))
    if m1:
        k = len(" ".join(words)[:m1.start()].split())
        infos.append(f"INFO the hook: {k} words before item one (about 100 to 160, item one inside a minute)")
        soft = re.findall(r"\b(?:may|might|perhaps|maybe|possibly)\b", " ".join(words[:k]))
        if soft:
            infos.append(f"INFO softeners in the hook (push harder, say it with certainty): {', '.join(soft)}")
    first = sentences(spoken)[0] if sentences(spoken) else ""
    shared = sorted(set(norm_words(first)) & set(norm_words(a.title)) - {"the", "a", "an", "to", "of", "and", "that", "your", "you", "for", "in", "over", "with"})
    infos.append(f"INFO the hook's first sentence (does it pay off the title?): \"{first[:160]}\" | title words in it: {', '.join(shared) or 'none'}")
    title_words = [w for w in norm_words(a.title) if w in {"instantly", "younger", "expensive", "elegant", "chic", "classy", "polished", "older", "frumpy", "granny", "rich", "luxury", "french"}]
    if title_words:
        counts = [w + " " + str(len(re.findall(r"\b" + w + r"\b", spoken, re.I))) for w in title_words]
        infos.append("INFO the title's words said: " + ", ".join(counts))
    for cap in re.findall(r"\b[A-Z]{3,}\b", a.title):
        if cap.lower() not in {"the", "and", "for", "you", "not"} and not re.search(r"\b" + cap + r"\b", spoken, re.I):
            fail("title word", f"the title's capitalised word '{cap}' is never said; say it once where it's true")
    endear = r"\bladies\b" if a.channel == "scarlett" else r"\bmy dear friends\b"
    k1, k2 = len(re.findall(endear, spoken, re.I)), len(re.findall(r"when I was designing", spoken, re.I))
    infos.append(f"INFO endearment {k1}, 'when I was designing' {k2}: no number to reach")
    infos.append(f"INFO {n} words, about {minutes:.1f} minutes at {ch['wpm']} words a minute")

    for line in fails + infos:
        print(line)
    print("RESULT: PASS" if not fails else f"RESULT: FAIL ({len(fails)})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
