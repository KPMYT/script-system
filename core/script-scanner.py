#!/usr/bin/env python3
"""
script-scanner.py: mechanical pre-recording check for voiceover scripts.

It FLAGS; it doesn't judge. Hard bans, mechanical problems and niche bans are
fix-on-sight. Everything else is a candidate for a human or model to judge with
the shape test in voice-anchoring.md.

Usage:
  python3 script-scanner.py SCRIPT [--rules FILE ...] [--pack FACT_SOURCE ...] [--title TITLE] [--refs FILE ...]

  SCRIPT       the script file (plain text or markdown).
  --rules      niche pack and/or persona profile files. Any ```scanner block in them
               is read for extra bans and lifted bans:
                   ban: phrase | label
                   ban-regex: pattern | label
                   once: phrase | label        (fix on sight from the second use in a script)
                   once-regex: pattern | label
                   lift: phrase or label of a hard ban
                   allow: a line the channel says the same way every time (exempt from the copy guard)
                 and, in a persona profile, the persona's fixed facts:
                   name: the persona's or channel's name (one per line; near-misses are flagged)
                   book: the book's spoken title (near-misses are flagged)
                   tenure: years in the trade as a number, or "none" (any other tenure figure is flagged)
                 and, in a niche pack, its length minimum if it raises the core's 8 minutes:
                   min-minutes: 12
               A profile's "Words per minute ...: N" line sets the runtime estimate (150 if unset).
  --pack       the fact source: the research pack, or the brief where the niche pack doesn't use one.
               Every number in the script is checked against it.
  --title      the locked title. A years-in-the-trade figure in it ("A 30-Year Plumber's Verdict")
               is allowed in the script alongside the profile's tenure: title numbers win.
  --refs       optional reference files (the niche pack's copy-guard files, as its SKILL.md lists them).
               Any run of 8 or more consecutive words in the spoken script that also appears
               in a reference file is fix-on-sight "copied from reference". Case, punctuation
               and [bracketed] source tags are ignored.

Every script is also checked for production notes read aloud ("CTA", "stinger", "mid-roll",
"continuing with the final sections"), the same sentence twice in a row, and (judge) the script
talking about its own thumbnail or title.

Exit code: 1 if any fix-on-sight problem is found (hard ban, mechanical, niche ban, production note,
repeated sentence, persona fact, copied from reference), else 0.
"""
import re, sys, argparse, difflib
from collections import Counter

# ---------------------------------------------------------------- hard bans
HARD_BANS = [
    (r"\blet'?s dive(?: in| into)?\b|\bdive into it\b", "let's dive in"),
    (r"\blet'?s break (?:this|it) down\b", "let's break it down"),
    (r"\bwithout further ado\b", "without further ado"),
    (r"\blet'?s unpack\b", "let's unpack"),
    (r"\blet'?s jump (?:in|into)\b", "let's jump in"),
    (r"\bbuckle up\b", "buckle up"),
    (r"\bhere'?s the kicker\b", "here's the kicker"),
    (r"\bin today'?s (?:world|day and age)\b", "in today's world"),
    (r"\blet'?s get into it\b", "let's get into it"),
    (r"\bdelve\b|\btapestry\b|\bunleash\b|\brobust\b", "AI vocabulary"),
    (r"\bgame.?changer\b", "game-changer"),
    (r"\b(?:evolving|shifting|changing|ever[- ]changing|current|modern|competitive|digital)\s+landscape\b", "landscape metaphor"),
    # retention teases
    (r"\bstick around\b", "tease: stick around"),
    (r"\bstay tuned\b", "tease: stay tuned"),
    (r"\bbonus(?: tip)? at the end\b", "tease: bonus at the end"),
    (r"\bby the end of (?:this|the) video\b", "tease: by the end of this video"),
    (r"\byou won'?t believe\b", "tease: you won't believe"),
    (r"\bkeep watching\b", "tease: keep watching"),
    (r"\bwatch (?:un)?til the end\b", "tease: watch until the end"),
    (r"\bdon'?t skip (?:ahead|forward|to the|this (?:part|video|one)|the (?:end|rest))\b", "tease: don't skip ahead"),
    (r"\bwait (?:un)?til you (?:see|hear)\b", "tease: wait until you see"),
    (r"\bstay(?: with me)? (?:(?:un)?till?|to) the (?:very )?end\b", "tease: stay till the end"),
    (r"\bstick with me\b", "tease: stick with me"),
    (r"\b(?:do not|don'?t) (?:go )?click(?:ing)? away\b", "tease: don't click away"),
    (r"\bhang on (?:for|until|till|to the end)\b", "tease: hang on for"),
    (r"\bstay for (?:number|#|the last|the final)\b", "tease: stay for number"),
    (r"\b(?:(?:I'?ll|I will|we'?ll|we will|I'?m|I am|we'?re|I'?ve|we'?ve)\s+(?:\w+\s+){0,2}?(?:save|saving|saved|keep|keeping|show|showing|tell|telling|reveal|revealing|share|sharing|give you|giving you)|saving|saved|keeping)\b[^.!?]{0,90}\b(?:at|for|till|until) the very end\b|\bat the very end,? (?:I'?ll|I will|we'?ll)\b", "tease: at the very end"),
    (r"\bstay (?:right )?here with me\b", "tease: stay right here with me"),
    (r"\b(?:do not|don'?t) skip out\b", "tease: don't skip out on me"),
    (r"\bby the end,? you'?ll\b", "tease: by the end, you'll"),
    # pointing at the screen: banned everywhere (operator, 2026-10-20)
    (r"\bright here\b", "pointing: right here"),
    (r"\blook at this\b", "pointing: look at this"),
]

# ---------------------------------------------------------------- production notes read aloud (fix on sight)
PRODUCTION = [
    (r"\bCTAs?\b", "CTA label"),
    (r"\bstingers?\b", "stinger label"),
    (r"\bmid-?rolls?\b", "mid-roll label"),
    (r"\bb-?roll\b", "B-roll label"),
    (r"\bSFX\b|\bsound effects?\b", "sound-effect label"),
    (r"\boutro\b|\bintro\s*:", "intro/outro label"),
    (r"\b(?:smash )?cut to\s*:|\bcut to (?:black|camera|footage|the (?:shot|clip|footage|b-?roll|graphic))\b", "edit instruction"),
    (r"\b(?:continuing|moving on|carrying on)\b[^.!?]{0,25}\bsections?\b|\bfinal sections?\b|\b(?:section|segment|scene) (?:\d+|one|two|three|four|five|six|seven|eight|nine|ten)\b", "section label"),
    (r"\bon-?screen text\b|\btext overlay\b|\blower third\b|\bend screen\b|\bvoice-?over\b|\bnarrator\b", "production term"),
    (r"\b(?:insert|show) (?:a )?(?:clip|footage|image|graphic|b-?roll)\b", "edit instruction"),
    (r"\((?:pause|beat|laughs?|music|sfx|visual|b-?roll)[^)]*\)", "stage direction"),
    (r"(?:^|(?<=[.!?]\s))(?:visual|scene|shot|camera|graphic|music|vo)\s*:", "stage direction"),
]

# ---------------------------------------------------------------- the script talking about its own packaging (judge)
PACKAGING = r"\bthe thumbnail\b|\b(?:this|the) video'?s title\b|\btitle of (?:this|the) video\b|\b(?:picture|image|video|title) you clicked\b|\byou clicked on\b|\bin (?:the|that|this) title\b"

# ---------------------------------------------------------------- mechanical sweep
MECHANICAL = [
    (r"\u2014", "em dash"),
    (r"\u2013", "en dash"),
    (r"(?<=\w) ?-- ?(?=\w)", "double hyphen used as a dash"),
    (r"[\u2018\u2019\u201C\u201D]", "curly quote"),
    (r"\u2026", "single-character ellipsis"),
    (r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", "emoji"),
    (r"(?i)\bI hope this helps\b|\bwould you like me to\b|\blet me know if you\b|\bas an AI\b|\bcertainly!|\bgreat question\b", "chatbot leftover"),
    (r"(?i)\bas of my last update\b|\bwhile details are limited\b|\bmy knowledge cutoff\b", "knowledge-cutoff disclaimer"),
]
OTHER_NON_ASCII = re.compile(r"[^\x00-\x7F\u2014\u2013\u2018\u2019\u201C\u201D\u2026\U0001F300-\U0001FAFF\u2600-\u27BF]")

# ---------------------------------------------------------------- trailer-voice tells (judge each)
TELLS = [
    (r"\bNot [a-z]+\. [A-Z]", "not-X-period beat"),
    (r"\. Not [a-z][^.]{0,30}\.", "trailing 'Not Y.' beat"),
    (r"\btells you everything\b|\bchanges everything\b|\bsays everything about\b", "aphoristic 'everything'"),
    (r"\bnothing would ever be the same\b|\bnever the same again\b", "narrator prophecy"),
    (r"\byou'?ll never look at\b|\byou will never look at\b", "second-person prophecy"),
    (r"\bIn a world\b", "trailer open"),
    (r"\bThis is the story of\b", "narrator open"),
    (r"\bwhat happens next\b", "narrator tease"),
    (r"\bThe rest, as they say\b", "narrator cliche"),
    (r"\bis the (?:thermometer|medicine|engine|fuel|currency|architecture|deposit|interest) of\b|\bis the \w+\. \w+ is the \w+\.", "clever written pair"),
    (r"(?i)\b(?:countless|numerous|myriad|innumerable|a plethora of|tons of|huge amounts of)\b", "vague quantity (H19)"),
]

# reframe family (H21), counted
REFRAME = [
    r"(?i)\b(?:is|was|are|were|do|does|did|has|had)n['\u2019]?t\b[^.!?\n]{2,50}?[.,;]\s*(?:it|that|this)\b(?:['\u2019]s|\s+(?:is|was))\b",
    r"(?i)\bnot\s+(?:about|just|only|merely)\b[^.!?\n]{0,50}?[.,;]\s*(?:it['\u2019]?s|it\s+(?:is|was)|that['\u2019]?s|this is|but)\b",
    r"(?i)\bless\s+\w+[^.!?\n]{0,25},\s*more\s+\w+\b",
    r"\bNot [a-z]+\. [A-Z]",
]

# stock filler phrases (H23): allowed once per script each, never two in one paragraph
SPARING = ["the truth is", "here's the thing", "at the end of the day", "long story short", "needless to say",
           "fast forward to", "as it turns out", "in fact", "you see", "it didn't take long for"]
SPARING_RX = [(p, re.compile(r"\b" + re.escape(p).replace("'", "'?") + r"\b", re.I)) for p in SPARING]

MOST_OPENER = re.compile(r"(?:^|(?<=[.!?]\s)|(?<=\n))Most (?:people|folks|homeowners|beginners|women|men|owners|crafters|woodworkers|travelers|of you|[a-z]+s)\b")

# short instructions are speech, not staccato
INSTRUCTION_VERBS = set("""
add apply attach brush buy check clamp clean close cut do drill dry fill flip fold glue grab hang hold
iron knit lay let lift line lock mark measure mix nail open pick place plug pour press pull push
put remove repeat rinse rub sand screw scrub set sew shut slide soak spray stack stain stitch tap
test tie tighten trim turn twist unplug use wait wipe wrap
""".split())

ECHO_STOP = set(("the a an and or but so of to in on at for from with that this those these it its is was are "
                 "were has had have will would could been being as by he she they we you his her their our not").split())

# ---------------------------------------------------------------- spoken-text extraction
STOP_SECTION = re.compile(r"^\s*(?:VERDICT|HOUSE FORMAT|ROTATION LOG|VO COPY|BUILD SHEET|UNIT PLAN)\b", re.I)
SKIP_LINE = re.compile(r"^\s*(?:#|[-*>|]|\d+\.\s|```|===|SCRIPT TYPE:|TYPE CONFIRMED|VOICE CONFIRMED|\*\*)")
INLINE_TAG = re.compile(r"\[[^\]]{1,40}\]")

def spoken_paragraphs(text):
    """Only the spoken script: stop at the verdict/log/VO copy, skip markers, headings, lists, tags."""
    paras, buf = [], []
    for line in text.splitlines():
        if STOP_SECTION.match(line):
            break
        if not line.strip():
            if buf:
                paras.append(" ".join(buf)); buf = []
            continue
        if SKIP_LINE.match(line):
            continue
        buf.append(INLINE_TAG.sub("", line).strip())
    if buf:
        paras.append(" ".join(buf))
    return [p for p in paras if p.strip()]

def sentences(para):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", para) if s.strip()]

# ---------------------------------------------------------------- rules files
def read_rules(paths):
    """Returns bans, lifts, allows and the persona facts {"name": [...], "book": [...], "tenure": "45" | "none" | None}."""
    bans, lifts, allows = [], [], []
    facts = {"name": [], "book": [], "tenure": None, "once": [], "wpm": None, "min": None}
    for p in paths or []:
        txt = open(p, encoding="utf8", errors="ignore").read()
        w = re.search(r"^Words per minute[^:\n]*:\s*(\d+)", txt, re.M)
        if w:
            facts["wpm"] = int(w.group(1))
        for block in re.findall(r"```scanner\s*\n(.*?)```", txt, re.S):
            for line in block.splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, _, val = line.partition(":")
                val = val.strip()
                if " | " in val:
                    pat, _, label = val.rpartition(" | ")   # label after the LAST " | ", so regex alternation survives
                else:
                    pat, label = val, ""
                pat, label = pat.strip(), (label.strip() or pat.strip())
                if key.strip() == "ban":
                    bans.append((re.compile(r"\b" + re.escape(pat) + r"\b", re.I), label))
                elif key.strip() == "ban-regex":
                    bans.append((re.compile(pat, re.I), label))
                elif key.strip() == "once":
                    facts["once"].append((re.compile(r"\b" + re.escape(pat) + r"\b", re.I), label))
                elif key.strip() == "once-regex":
                    facts["once"].append((re.compile(pat, re.I), label))
                elif key.strip() == "lift":
                    lifts.append(pat.lower())
                elif key.strip() == "allow":
                    allows.append(pat)
                elif key.strip() in ("name", "book"):
                    facts[key.strip()].append(pat)
                elif key.strip() == "tenure":
                    facts["tenure"] = pat.lower()
                elif key.strip() == "min-minutes":
                    facts["min"] = int(pat)
    return bans, lifts, allows, facts

# ---------------------------------------------------------------- numbers
WORD_NUM = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: 10 * i for i, w in enumerate("_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()) if w != "_"}
SCALES = {"hundred": 100, "thousand": 1000, "million": 1000000}
UNIT_WORDS = {"dollar", "dollars", "buck", "bucks", "cent", "cents", "year", "years", "month", "months", "week", "weeks", "day", "days",
              "hour", "hours", "minute", "minutes", "gallon", "gallons", "ounce", "ounces", "pound", "pounds", "foot", "feet",
              "inch", "inches", "percent", "degree", "degrees", "to", "old"}
FRACTIONS = {"a half": .5, "a quarter": .25, "three-quarters": .75, "three quarters": .75, "one-half": .5}

def word_numbers(text):
    vals = []
    toks = re.findall(r"[a-z]+(?:-[a-z]+)?|and", text.lower())
    i = 0
    while i < len(toks):
        t = toks[i]
        parts = t.split("-")
        lead_a = t == "a" and i + 1 < len(toks) and toks[i + 1].split("-")[0] in SCALES   # "a hundred and fifty"
        if parts[0] in WORD_NUM or parts[0] in TENS or lead_a:
            total, cur = 0, 0
            start = i
            if lead_a:
                cur = 1; i += 1
            while i < len(toks):
                t = toks[i]; ps = t.split("-")
                k = 0
                while k < len(ps) and (ps[k] in WORD_NUM or ps[k] in TENS or ps[k] in SCALES):
                    k += 1
                if k and (k == len(ps) or ps[k] in UNIT_WORDS):
                    for p in ps[:k]:                   # "two-hundred" is one token; "hundred-dollar" keeps its number
                        if p in SCALES:
                            cur = max(cur, 1) * SCALES[p]
                            if SCALES[p] >= 1000:
                                total += cur; cur = 0
                        else:
                            cur += WORD_NUM.get(p, 0) + TENS.get(p, 0)
                    if k < len(ps):                    # the unit ends the number
                        i += 1
                        break
                elif t == "and" and i + 1 < len(toks) and (toks[i + 1] in ("a", "three-quarters", "one-half") or toks[i + 1].split("-")[0] in WORD_NUM or toks[i + 1].split("-")[0] in TENS):
                    if i + 2 < len(toks) and " ".join(toks[i + 1:i + 3]) in FRACTIONS:
                        cur += FRACTIONS[" ".join(toks[i + 1:i + 3])]; i += 2
                    elif toks[i + 1] in FRACTIONS:
                        cur += FRACTIONS[toks[i + 1]]; i += 1
                else:
                    break
                i += 1
            if i == start:      # a word like "three-quarter" or "one-by-eight" that isn't a whole number: step past it
                i += 1
            vals.append(total + cur)
        else:
            i += 1
    return vals

def digit_numbers(text):
    vals = []
    for m in re.finditer(r"\$?\d[\d,]*(?:\.\d+)?(?:\s+\d+/\d+|\s*/\s*\d+)?", text):
        s = m.group(0).replace("$", "").replace(",", "").strip()
        try:
            if "/" in s:
                parts = s.split()
                if len(parts) == 2:
                    a, b = parts[1].split("/"); vals.append(float(parts[0]) + float(a) / float(b))
                else:
                    a, b = s.replace(" ", "").split("/"); vals.append(float(a) / float(b))
            else:
                vals.append(float(s))
        except (ValueError, ZeroDivisionError):
            pass
    return vals

def all_numbers(text):
    return digit_numbers(text) + word_numbers(text)

def number_check(script_text, pack_text):
    pack_vals = set(round(v, 2) for v in all_numbers(pack_text))
    missing = []
    for para in spoken_paragraphs(script_text):
        for s in sentences(para):
            for v in set(round(x, 2) for x in all_numbers(s)):
                if v <= 3:      # tiny counts ("one board", "two coats") are too noisy to check
                    continue
                if any(abs(v - p) <= max(0.1 * p, 0.5) for p in pack_vals):
                    continue
                missing.append((v, s))
    return missing

# ---------------------------------------------------------------- copy guard
COPY_RUN = 8   # words in a row shared with a reference file = copied

def copy_tokens(text):
    """Lower-case word tokens, ignoring punctuation and [bracketed] tags (timestamps, source tags)."""
    text = INLINE_TAG.sub(" ", text.replace("\u2019", "'").replace("\u2018", "'")).lower()
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", text)

def read_refs(paths):
    """Every COPY_RUN-word run in the reference files, mapped to the first file it came from."""
    runs = {}
    for p in paths or []:
        name = p.replace("\\", "/").rsplit("/", 1)[-1]
        for line in open(p, encoding="utf8", errors="ignore").read().split("\n\n"):
            toks = copy_tokens(line)
            for i in range(len(toks) - COPY_RUN + 1):
                runs.setdefault(tuple(toks[i:i + COPY_RUN]), name)
    return runs

def mask_allowed(toks, allows):
    """Blank out lines a profile marks allow: (a fixed sign-off, a spoken title) so no copied run can use them."""
    for phrase in allows or []:
        a = copy_tokens(phrase)
        for i in range(len(toks) - len(a) + 1):
            if a and toks[i:i + len(a)] == a:
                toks[i:i + len(a)] = [f"\x00{i}_{j}" for j in range(len(a))]
    return toks

def copy_check(text, ref_runs, allows=None):
    """Merge overlapping shared runs per paragraph; return (source file, copied words)."""
    hits = []
    if not ref_runs:
        return hits
    for para in spoken_paragraphs(text):
        toks = mask_allowed(copy_tokens(para), allows)
        start = end = None; src = None
        for i in range(len(toks) - COPY_RUN + 1):
            g = tuple(toks[i:i + COPY_RUN])
            if g in ref_runs:
                if start is not None and i <= end:
                    end = i + COPY_RUN
                else:
                    if start is not None:
                        hits.append((src, " ".join(toks[start:end])))
                    start, end, src = i, i + COPY_RUN, ref_runs[g]
        if start is not None:
            hits.append((src, " ".join(toks[start:end])))
    return hits

# ---------------------------------------------------------------- persona facts (fix on sight)
NUM_WORD = r"(?:\d{1,2}|(?:twenty|thirty|forty|fifty|sixty|seventy)(?:[- ](?:one|two|three|four|five|six|seven|eight|nine))?|ten|eleven|twelve|fifteen|five|six|seven|eight|nine)"
_TRADE = r"(?:experience|trade|trades|plumbing|plumber|pipefitt\w*|pipe ?fitter|tools|bench|shop|job|field|business|woodworking|woodworker|carpentry|craft|career|wrenching|fixing \w+|doing this|in this line)"
TENURE_RX = [
    # "45 years in the trade", "35 years of experience", "40 years as a plumber"
    re.compile(r"\b(" + NUM_WORD + r")[- ]years?\s+(?:(?:of|in|on|at|as|behind|under)\s+)?(?:(?:the|a|an|my)\s+)?" + _TRADE + r"\b", re.I),
    # "been a plumber for over 35 years", "fixing pipe for 30 years", "on the tools for 30 years"
    re.compile(r"\b(?:been|spent|worked|working|plumbing|fixing|on the tools|in the trade|doing this|at the bench)\b[^.!?]{0,40}?\bfor (?:over |nearly |almost |about |more than |close to )?(" + NUM_WORD + r")[- ]years?\b", re.I),
    # "a 45-year plumber", "45-year veteran"
    re.compile(r"\b(" + NUM_WORD + r")-year\s+(?:plumber|pipefitter|veteran|master|tradesman|woodworker|carpenter|pro|career)\b", re.I),
]

def _num(tok):
    tok = tok.lower().replace("-", " ")
    if tok.isdigit():
        return int(tok)
    parts = tok.split()
    return sum(TENS.get(w, WORD_NUM.get(w, 0)) for w in parts)

# titles also state tenure as years of selling or making ("In 40 Years of Selling...")
TITLE_TENURE_EXTRA = re.compile(r"\b(" + NUM_WORD + r")[- ]years?\s+(?:of\s+)?(?:selling|sales|making|building)\b", re.I)

def title_tenure(title):
    """The years-in-the-trade figure a locked title states ("A 45-Year Plumber's Verdict"), or None. Title numbers win."""
    for rx in TENURE_RX + [TITLE_TENURE_EXTRA]:
        m = rx.search(title or "")
        if m:
            return _num(m.group(1))
    return None

def tenure_check(para, tenure, title_n=None):
    """Any years-in-the-trade figure that differs from the profile's tenure (or any at all, for "none").
    A figure the locked title states is allowed instead (title numbers win)."""
    out, seen = [], set()
    if not tenure and title_n is None:
        return out
    tenure = tenure or "none"
    for rx in TENURE_RX:
        pos = 0
        while True:
            m = rx.search(para, pos)
            if not m:
                break
            pos = m.start() + 1          # overlapping: a skipped "been ..." match mustn't hide a later one
            if m.start(1) in seen:
                continue
            near = para[max(0, m.start() - 40):m.end() + 40]
            if rx is TENURE_RX[0] and not re.search(r"\b(?:I|I'?ve|I'?m|me|my|we|we'?ve)\b", near):
                continue
            # "been ... for N years" counts only with the persona as its subject ("I've been...", not "the heater has been...")
            if rx is TENURE_RX[1] and m.group(0).lower().startswith("been") and not re.search(r"(?:\b(?:I|I'?ve|I have|I had|I'?d|we|we'?ve|we have)\s+(?:\w+\s+){0,2}|\bmy\s+\w+\s+(?:have|has|had)\s+|(?:^|[.!?]\s+))$", para[max(0, m.start() - 30):m.start()], re.I):
                continue
            seen.add(m.start(1))
            n = _num(m.group(1))
            if title_n is not None and n == title_n:
                continue
            if tenure == "none" or (tenure.isdigit() and n != int(tenure)):
                want = "no tenure figure (the profile keeps experience numberless)" if tenure == "none" else f"{tenure} years"
                if title_n is not None:
                    want += f", and the title says {title_n} years"
                out.append(f"[PERSONA FACT: tenure] \"{para[max(0, m.start() - 20):m.end() + 15].strip()}\" (the profile says {want})")
    return out

def _squash(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

SMALL_WORDS = {"the", "a", "an", "of", "to", "with", "and", "your", "my", "for", "in", "on", "at"}

def name_check(para, names):
    """A capitalised phrase that shares a key word with a fixed name or book title but isn't it
    ("the Vintage Plumber" for The Vintage Pipefitter). Exact and partial uses ("the Pipe Guy") pass;
    spacing and case are ignored ("Pipe Fitter" = "Pipefitter"). One finding per name per paragraph."""
    out = []
    toks = [(m.group(0), m.start()) for m in re.finditer(r"[A-Za-z0-9'$]+", para)]
    words = [w for w, _ in toks]
    sent_start = {i for i, (_, pos) in enumerate(toks) if i == 0 or re.search(r"[.!?]\s*$", para[:pos])}
    for name in names:
        nw = re.findall(r"[A-Za-z0-9'$]+", name)
        name_words = {w.lower() for w in nw}
        target = _squash(name)
        bare_name = re.sub(r"^(?:the|a)\s+", "", name, flags=re.I)
        bare = _squash(bare_name)
        if len(nw) < 2 or not target:
            continue
        masked = set()
        for size in range(1, len(nw) + 3):
            for i in range(len(words) - size + 1):
                if _squash(" ".join(words[i:i + size])) in (target, bare):
                    masked.update(range(i, i + size))
        key = {w.lower() for w in nw if len(w) > 3 and w.lower() not in SMALL_WORDS | {"this", "that", "from", "make"}}
        sizes = {len(nw), len(re.findall(r"[A-Za-z0-9'$]+", bare_name))}
        best = None
        for size in sorted(sizes | {max(sizes) + 1, min(sizes) - 1} - {0, 1}):
            for i in range(len(words) - size + 1):
                if masked & set(range(i, i + size)):
                    continue
                win = words[i:i + size]
                cand = _squash(" ".join(win))
                if cand in target or not any(w.lower() in key for w in win):
                    continue
                if not all(w[:1].isupper() or w[:1].isdigit() or w.lower() in SMALL_WORDS for w in win):
                    continue
                if sum(w[:1].isupper() for w in win) < 2:
                    continue
                # the wrong word: capitalised, not part of the name, not a pronoun, not just a new sentence starting
                if not any(w[:1].isupper() and re.sub(r"['\u2019]s$", "", w.lower()) not in name_words and w.lower() not in ("i", "i'm", "i've", "i'll", "i'd")
                           and (i + k) not in sent_start for k, w in enumerate(win)):
                    continue
                score = max(difflib.SequenceMatcher(None, cand, target).ratio(), difflib.SequenceMatcher(None, cand, bare).ratio())
                shared = len({w.lower() for w in win} & key) / max(1, len(key))
                if score >= 0.6 or shared >= 0.5:
                    if not best or score > best[0]:
                        best = (score, " ".join(win))
        if best:
            out.append(f"[PERSONA FACT: near-miss name] \"{best[1]}\" (the profile says \"{name}\")")
    return out

def repeated_sentences(paras):
    """The same sentence twice in a row ("Number four. Number four.")."""
    out, prev = [], None
    for para in paras:
        for snt in sentences(para):
            norm = " ".join(re.findall(r"[a-z0-9']+", snt.lower()))
            if prev and norm == prev and len(norm.split()) >= 2:
                out.append(f"[REPEATED SENTENCE] \"{snt}\" said twice in a row")
            prev = norm
    return out

# ---------------------------------------------------------------- scan
def scan(text, extra_bans, lifts, ref_runs=None, allows=None, facts=None, title=None):
    fix, judge = [], []
    facts = facts or {"name": [], "book": [], "tenure": None, "once": []}
    for src, run in copy_check(text, ref_runs, allows):
        fix.append(f"[COPIED FROM REFERENCE: {src}] \"{run}\" ({len(run.split())} words in a row)")
    paras = spoken_paragraphs(text)
    hard = [(re.compile(rx, re.I), name) for rx, name in HARD_BANS
            if not any(l in name.lower() or re.search(rx, l, re.I) for l in lifts)]
    for para in paras:
        ctx = lambda m: para[max(0, m.start() - 40):m.end() + 40]
        for rx, name in hard:
            for m in rx.finditer(para):
                fix.append(f"[HARD BAN: {name}] ...{ctx(m)}...")
        for rx, name in extra_bans:
            for m in rx.finditer(para):
                fix.append(f"[NICHE/PERSONA BAN: {name}] ...{ctx(m)}...")
        for rx, name in MECHANICAL:
            for m in re.finditer(rx, para):
                fix.append(f"[MECHANICAL: {name}] ...{ctx(m)}...")
        for rx, name in PRODUCTION:
            for m in re.finditer(rx, para, re.I):
                fix.append(f"[PRODUCTION NOTE: {name}] ...{ctx(m)}...")
        fix.extend(tenure_check(para, facts["tenure"], title_tenure(title)))
        fix.extend(name_check(para, facts["name"] + facts["book"]))
        for m in re.finditer(PACKAGING, para, re.I):
            judge.append(f"[talks about its own packaging] ...{ctx(m)}...")
        for m in OTHER_NON_ASCII.finditer(para):
            fix.append(f"[MECHANICAL: non-standard character '{m.group(0)}'] ...{ctx(m)}...")
        for rx, name in TELLS:
            for m in re.finditer(rx, para):
                judge.append(f"[{name}] ...{ctx(m)}...")
        sents = sentences(para)
        shorts = [s for s in sents if len(s.split()) <= 4 and s[-1:] in ".!"
                  and s.split()[0].lower().strip(",.!?") not in INSTRUCTION_VERBS
                  and not s.lower().startswith(("so", "ok", "okay", "yeah", "yes", "no,", "now,", "then", "number",
                                                "back to", "quick", "right", "all right", "alright"))]
        if len(shorts) >= 2:
            judge.append(f"[staccato x{len(shorts)}] " + " | ".join(f'"{s}"' for s in shorts[:4]))
    fix.extend(repeated_sentences(paras))
    for rx, name in facts.get("once", []):
        n = sum(len(rx.findall(para)) for para in paras)
        if n > 1:
            fix.append(f"[NICHE/PERSONA LIMIT: {name}] used {n} times (allowed once per script)")
    sparing_counts, sparing_paras = Counter(), []
    for para in paras:
        hits = [p for p, rx in SPARING_RX for _ in rx.finditer(para)]
        sparing_counts.update(hits)
        if len(hits) >= 2:
            sparing_paras.append(f"two or more in one paragraph: {', '.join(hits)} << {para[:70]}...")
    sparing = [f'"{p}" x{n}' for p, n in sparing_counts.items() if n > 1] + sparing_paras
    full = "\n\n".join(paras)
    most = [m.group(0) for m in MOST_OPENER.finditer(full)]
    reframes = []
    for para in paras:
        spans = []
        for rx in REFRAME:
            for m in re.finditer(rx, para):
                if any(m.start() < e and m.end() > s for s, e in spans):
                    continue
                spans.append((m.start(), m.end()))
                reframes.append(para[max(0, m.start() - 30):m.end() + 30])
    grams, nums = Counter(), Counter()
    for para in paras:
        words = [w.strip(".,'\"!?") for w in para.lower().split()]
        words = [w for w in words if w]
        for i in range(len(words) - 3):
            g = tuple(words[i:i + 4])
            if all((w in ECHO_STOP or len(w) < 5) and not any(c.isdigit() for c in w) for w in g):
                continue
            grams[g] += 1
        for tok in re.findall(r"\$[\d][\d,.]*|\b\d[\d,.]*\b", para):
            t = tok.rstrip(".,")
            if t.startswith("$") or (t.replace(",", "").replace(".", "").isdigit() and float(t.replace(",", "")) >= 10):
                nums[t] += 1   # single-digit counts and measurements repeat naturally; skip them
    echoes = [f'phrase x{n}: "{" ".join(g)}"' for g, n in grams.most_common() if n >= 3][:6]
    echoes += [f'number x{n}: "{t}" (mentions past the second must add something new)' for t, n in nums.items() if n >= 4]
    return fix, judge, most, reframes, echoes, sparing

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--rules", nargs="*", default=[])
    ap.add_argument("--pack", nargs="+", default=[], help="the fact source; several files are read as one (the plumbing brief plus its price guide)")
    ap.add_argument("--refs", nargs="+", default=[])
    ap.add_argument("--title", help="the locked title; a years-in-the-trade figure in it is allowed in the script")
    a = ap.parse_args()
    text = open(a.script, encoding="utf8", errors="ignore").read()
    bans, lifts, allows, facts = read_rules(a.rules)
    fix, judge, most, reframes, echoes, sparing = scan(text, bans, lifts, read_refs(a.refs), allows, facts, a.title)
    print(f"SCAN: {a.script}")
    if a.refs:
        print(f"  copy guard: {COPY_RUN}+ words in a row shared with {', '.join(a.refs)}")
    if lifts:
        print(f"  lifted bans in effect: {', '.join(lifts)}")
    if facts["name"] or facts["book"] or facts["tenure"]:
        print(f"  persona facts: names {facts['name']}, book {facts['book']}, tenure {facts['tenure']}")
    if title_tenure(a.title) is not None:
        print(f"  title tenure: {title_tenure(a.title)} years (title numbers win)")
    words = sum(len(p.split()) for p in spoken_paragraphs(text))
    wpm, minimum = facts.get("wpm") or 150, facts.get("min") or 8
    mins = words / wpm
    print(f"  spoken words: {words} (about {mins:.1f} minutes at {wpm} words a minute; minimum {minimum})" + ("  << under the minimum" if mins < minimum else ""))
    print(f"\nFIX ON SIGHT ({len(fix)})")
    for f in fix: print("  " + f)
    print(f"\nJUDGE WITH THE SHAPE TEST ({len(judge)})")
    for j in judge[:25]: print("  " + j)
    print(f"\n\"MOST ...\" OPENERS: {len(most)} (allowed: 1)" + ("  << over the cap" if len(most) > 1 else ""))
    print(f"REFRAME FLOOR (H21): {len(reframes)} machine-caught (allowed: 1; the audit's count may never be lower)")
    for r in reframes[:6]: print(f"  ...{r}...")
    print(f"FILLER PHRASES OVER THE LIMIT (H23): {len(sparing)}")
    for x in sparing: print("  " + x)
    print(f"ECHO (H18): {len(echoes)}")
    for e in echoes: print("  " + e)
    if a.pack:
        missing = number_check(text, "\n".join(open(f, encoding="utf8", errors="ignore").read() for f in a.pack))
        print(f"\nNUMBERS NOT FOUND IN THE FACT SOURCE ({len(missing)})  (invented, or derived: confirm the math)")
        for v, s in missing[:30]:
            print(f"  {v:g}  <<  {s[:110]}")
    sys.exit(1 if fix else 0)

if __name__ == "__main__":
    main()
