#!/usr/bin/env python3
"""
script-scanner.py: mechanical pre-recording check for voiceover scripts.

It FLAGS; it doesn't judge. Hard bans, mechanical problems and niche bans are
fix-on-sight. Everything else is a candidate for a human or model to judge with
the shape test in voice-anchoring.md.

Usage:
  python3 script-scanner.py SCRIPT [--rules FILE ...] [--pack FACT_SOURCE ...] [--title TITLE] [--refs FILE ...] [--final]

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
                 and, optionally, report settings (the ITEMS and SENTENCES lines; report only):
                   item-words: 120-180        (each item's words against this band)
                   first-item-seconds: 45     (item one later than this is marked)
                   sentence-max: 35           (the sentence cap; 35 if unset, fix on sight on every channel)
                 and, to guard the pack's own quoted example lines with a shorter run than the copy guard's 8:
                   example-guard: 5           (any 5 words in a row from a "quoted example" in that file, fix on sight)
                 and letter words the niche says as letters every day (no judge line for them):
                   letters-ok: HVAC, AC, MERV
                 and steps that must all be there once a topic comes up (fix on sight when one is missing):
                   require-if: trigger pattern => needed pattern | label
                 and the title's promise words: any listed word (a prefix: "instant" covers "instantly") that is in
                 the --title must be said at least twice, the first time within the first minute (fix on sight):
                   title-words: instant, young, expensive, ten years | the title's promise words
               A profile's "Words per minute ...: N" line sets the runtime estimate (150 if unset).
  --pack       the fact source: the research pack, or the brief where the niche pack doesn't use one.
               Every number in the script is checked against it.
  --title      the locked title. A years-in-the-trade figure in it ("A 30-Year Plumber's Verdict")
               is allowed in the script alongside the profile's tenure: title numbers win.
  --final      the delivered text: a script under the length minimum is fix-on-sight.
  --refs       optional reference files (the niche pack's copy-guard files, as its SKILL.md lists them).
               Any run of 8 or more consecutive words in the spoken script that also appears
               in a reference file is fix-on-sight "copied from reference". Case, punctuation
               and [bracketed] source tags are ignored.

Every script is also checked for production notes read aloud ("CTA", "stinger", "mid-roll",
"continuing with the final sections"), the same sentence twice in a row, (judge) the script
talking about its own thumbnail or title, and forms the voice misreads (`[SPOKEN: ...]`, fix on
sight: 2x4, 8 ft, 3/8, 19%, symbols, two numbers side by side, $4.00, KD19, "haha"; judged:
capital-letter runs such as AAV, and words with two pronunciations such as "lead" or "live",
each judged once with a count), voice tags or brackets left in the script, and sentences over 35 words.
It also prints an ITEMS line (the spoken signposts "Number one." ... in order: item one's word and
seconds, each item's words, items with no "I" line or no "but") and a SENTENCES line (report only).

Exit code: 1 if any fix-on-sight problem is found (hard ban, mechanical, spoken, niche ban,
production note, repeated sentence, sentence over 35 words, persona fact, copied from reference,
and with --final the length minimum), else 0.
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
    # the channel intro (locked: no greeting or channel intro; P19, 2026-10-29)
    (r"\bthis channel is (?:for|where)\b|\b(?:I'?m|I am) here for (?:every )?wom[ae]n over\b", "channel intro: this channel is for"),
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
# ---------------------------------------------------------------- written for the voice (operator, 2026-10-25)
# Forms the text-to-speech voice misreads or guesses at: fix on sight. Sam's bench video turned
# "2x4" into "a 24" and "one 2x4, 8 ft" into "1 2 4 8 ft"; Mark's voice dropped "AAV" twice.
SPOKEN = [
    (r"\b\d+(?:\.\d+)?(?:\s?[xX\u00d7]\s?\d+)+s?\b|\b\d+[xX]\b", "size written with x (write 'two by four')"),
    (r"\b\d+[- ]by[- ]\d+s?\b", "size written in digits (write 'two by four')"),
    (r"\b\d+(?:\.\d+)?(?:\s|-)?(?:ft|in\.|oz|lbs?|gal|mm|cm|psi|yds?)(?![A-Za-z])|\b\d+-?in\b(?!-)", "unit abbreviation (write the word)"),
    (r"(?i)\bpsi\b", "'psi' (say 'pounds of pressure' or 'pounds per square inch')"),
    (r"(?<![$\d.,])\d+(?:\.\d+)?\s?(?:\"|'')|(?<![$\d.,])\d+'(?![a-z])", "inch or foot mark (write the word)"),
    (r"\b\d+/\d+\b", "fraction with a slash (write 'three-eighths')"),
    (r"%", "percent sign (write 'percent')"),
    (r"[&+#=~@]", "symbol (write the word)"),
    (r"(?<![\d,.$])\b\d(?:[\d,.]*\d)?\s+\d(?:[\d,.]*\d)?\b", "two numbers side by side"),
    (r"\$\d[\d,]*\.\d{2}\b", "cents written out ($4.00)"),
    (r"\$?\b\d+(?:\.\d+)?\s?[kKmM]\b", "money or number written short ($1.4M, 50k)"),
    (r"\bNo\.\s?\d|(?i:\bvs\b\.?)|(?i:\betc\b\.?)|(?i:\be\.g\.|\bi\.e\.)|(?i:\bapprox\.)|\b(?:Dr|Mr|Mrs|Ms|St|Ave|Jr|Sr)\.(?=\s)", "abbreviation (write the word)"),
    (r"\b(?=[A-Z0-9]*[A-Z])(?=[A-Z0-9]*\d)[A-Z0-9]{2,}\b", "letters-and-digits code (write it as it's said: 'K D 19')"),
    (r"(?i)\b(?:ha){2,}\b|\bhm+\b|\blol\b|\bugh\b", "laugh or filler sound written as a word"),
]
# judged: letters the voice may skip or read as a word, and words with two pronunciations
SPOKEN_LETTERS = re.compile(r"\b[A-Z]{2,5}s?\b")
SPOKEN_LETTERS_OK = {"OK", "TV", "QR", "DIY", "US", "USA"}
SPOKEN_TWO_WAYS = re.compile(r"(?i)\b(?:lead|bow|bows|bowed|bowing|wound|live|lives)\b")
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
    r"(?i)\b(?:won|doesn|don|didn|can|isn|aren|wasn)['\u2019]?t\s+(\w+)\b[^.!?\n]{0,60}[.;]\s*(?:[^.!?\n]{0,25},\s*)?(?:(?:it|that|this)\s+\1s|they\s+\1)\b",
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
VOICE_TAG_LINE = re.compile(r"(?m)^(?!\s*===).*?(\[[^\]]{1,40}\])")
SENTENCE_MAX = 35      # words; a longer sentence is fix-on-sight on every channel (run 03's judge fix, P13)

def script_part(text):
    """The script itself: everything before the verdict, the log or the VO copy (tags belong only in the VO copy)."""
    out = []
    for line in text.splitlines():
        if STOP_SECTION.match(line):
            break
        if not SKIP_LINE.match(line):
            out.append(line)
    return "\n".join(out)

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
    facts = {"name": [], "book": [], "tenure": None, "once": [], "wpm": None, "min": None, "letters_ok": set(),
             "item_words": None, "first_item_seconds": None, "sentence_max": None, "examples": [], "require": [], "title_words": []}
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
                elif key.strip() == "item-words":
                    lo, _, hi = pat.partition("-")
                    facts["item_words"] = (int(lo), int(hi))
                elif key.strip() == "first-item-seconds":
                    facts["first_item_seconds"] = int(pat)
                elif key.strip() == "sentence-max":
                    facts["sentence_max"] = int(pat)
                elif key.strip() == "example-guard":
                    facts["examples"].append((int(pat), p))
                elif key.strip() == "letters-ok":
                    facts["letters_ok"].update(x.strip() for x in pat.split(",") if x.strip())
                elif key.strip() == "title-words":
                    facts["title_words"].extend(x.strip().lower() for x in pat.split(",") if x.strip())
                elif key.strip() == "require-if" and " => " in pat:
                    trig, _, need = pat.partition(" => ")
                    facts["require"].append((re.compile(trig.strip(), re.I), re.compile(need.strip(), re.I), label))
    return bans, lifts, allows, facts

# ---------------------------------------------------------------- numbers
WORD_NUM = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: 10 * i for i, w in enumerate("_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()) if w != "_"}
SCALES = {"hundred": 100, "thousand": 1000, "million": 1000000}
UNIT_WORDS = {"dollar", "dollars", "buck", "bucks", "cent", "cents", "year", "years", "month", "months", "week", "weeks", "day", "days",
              "hour", "hours", "minute", "minutes", "gallon", "gallons", "ounce", "ounces", "pound", "pounds", "foot", "feet",
              "inch", "inches", "percent", "degree", "degrees", "to", "old",
              "amp", "amps", "volt", "volts", "watt", "watts", "gauge", "milliamp", "milliamps", "kilowatt", "kilowatts", "hertz"}
FRACTIONS = {"a half": .5, "a quarter": .25, "three-quarters": .75, "three quarters": .75, "one-half": .5}

def word_numbers(text):
    vals = []
    toks = []
    for t in re.findall(r"[a-z]+(?:-[a-z]+)?|[,;:.!?]", text.lower()):   # punctuation ends a number ("one-twenty, two-forty")
        ps = t.split("-")
        # only "twenty-five" (tens then one to nine) is one number; "twelve-two", "one-twenty", "fourteen-thirty" are two
        if len(ps) == 2 and all(p in WORD_NUM or p in TENS for p in ps) and not (ps[0] in TENS and ps[1] in WORD_NUM and 0 < WORD_NUM[ps[1]] < 10):
            toks.extend([ps[0], "|", ps[1]])
        else:
            toks.append(t)
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

# the pack's own quoted example lines: a shorter run is enough, because a writer copies their shape and wording
# (woodworking's Lazy Susan lines; electrical run 01's "If you only check one thing..." and "that plug clicks in and holds")
EXAMPLE_SKIP = set("hundred thousand twenty thirty forty fifty sixty fifteen twelve fourteen ten one two three four five six seven eight nine "
                   "amp amps volt volts watt watts gauge minute minutes year years inch inches i i'd i'm you you're your it's that's".split())

def example_runs(n, path):
    """Every n-word run inside a quoted example sentence in the rules file (outside its scanner block: a quote that
    starts with a capital and ends on . ? or !) that carries at least three content words (not common words,
    numbers or units). Quoted wording the pack asks for ("a licensed electrician's job") isn't a sentence, so it's left out."""
    txt = re.sub(r"```scanner.*?```", " ", open(path, encoding="utf8", errors="ignore").read(), flags=re.S)
    runs = {}
    quotes = []
    for line in txt.splitlines():
        marks = [i for i, c in enumerate(line) if c == '"']
        quotes += [line[a + 1:b] for a, b in zip(marks[0::2], marks[1::2])]
    for q in quotes:
        q = q.strip()
        if not re.match(r"[A-Z]", q) or q[-1:] not in ".?!":
            continue
        toks = copy_tokens(q)
        for i in range(len(toks) - n + 1):
            g = tuple(toks[i:i + n])
            if sum(1 for w in g if w not in ECHO_STOP and w not in EXAMPLE_SKIP) >= 3:
                runs.setdefault(g, q)
    return runs

def example_check(text, examples, allows=None):
    hits = []
    for n, path in examples or []:
        runs = example_runs(n, path)
        name = path.replace("\\", "/").rsplit("/", 1)[-1]
        for para in spoken_paragraphs(text):
            toks = mask_allowed(copy_tokens(para), allows)
            i = 0
            while i <= len(toks) - n:
                g = tuple(toks[i:i + n])
                if g in runs:
                    hits.append(f"[EXAMPLE LINE REUSED: {name}] \"{' '.join(g)}\" (the pack's example: \"{runs[g][:70]}\"; say it in fresh words)")
                    i += n
                else:
                    i += 1
    return hits

# ---------------------------------------------------------------- persona facts (fix on sight)
NUM_WORD = r"(?:\d{1,2}|(?:twenty|thirty|forty|fifty|sixty|seventy)(?:[- ](?:one|two|three|four|five|six|seven|eight|nine))?|ten|eleven|twelve|fifteen|five|six|seven|eight|nine)"
_TRADE = r"(?:experience|trade|trades|plumbing|plumber|pipefitt\w*|pipe ?fitter|tools|bench|shop|job|field|business|woodworking|woodworker|carpentry|craft|career|wrenching|fixing \w+|doing this|in this line|(?:master |journeyman |licensed )?electricians?|electrical(?: work| trade| contracting)?|electric|wiring(?: houses| homes)?|lineman|wireman|hvac|heating|cooling|air conditioning|furnaces?|(?:hair)?stylists?|styling(?: women| hair)?|hairdress\w*|colou?rists?|fashion(?: world| industry| business)?|dressing(?: women)?|doing hair|cutting hair)"
TENURE_RX = [
    # "45 years in the trade", "35 years of experience", "40 years as a plumber"
    re.compile(r"(?<![\w-])(" + NUM_WORD + r")[- ]years?\s+(?:(?:of|in|on|at|as|behind|under)\s+)?(?:(?:the|a|an|my)\s+)?" + _TRADE + r"\b", re.I),
    # "been a plumber for over 35 years", "fixing pipe for 30 years", "on the tools for 30 years"
    re.compile(r"\b(?:been|spent|worked|working|wired|wiring (?:houses|homes)|plumbing|fixing|on the tools|in the trade|doing this|at the bench|a (?:hair)?stylist|a hairdresser|a colou?rist|styling women|dressing women|doing hair|cutting hair)\b[^.!?]{0,40}?\bfor (?:over |nearly |almost |about |more than |close to )?(" + NUM_WORD + r")[- ]years?\b", re.I),
    # "I've been doing this 40 years", "in the trade 45 years" (no "for"; 2026-10-27)
    re.compile(r"\b(?:doing this|in the trade|on the tools|at the bench)\s+(?:over |nearly |almost |about |more than |close to )?(" + NUM_WORD + r")[- ]years?\b", re.I),
    # "a 45-year plumber", "45-year veteran", "a 40-year electrician", "a 30-year HVAC tech"
    re.compile(r"(?<![\w-])(" + NUM_WORD + r")-year\s+(?:(?:hvac|heating|furnace|service|electrical)\s+)?(?:plumber|pipefitter|veteran|master|tradesman|woodworker|carpenter|pro|career|tech|techs|technician|electrician|lineman|journeyman|serviceman|man|guy|(?:hair)?stylist|hairdresser|colou?rist)\b", re.I),
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
    out, seen, spans = [], set(), []
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
            if m.start(1) in seen or any(a <= m.start(1) < b for a, b in spans):
                continue           # "Thirty five years": the "five" inside an earlier figure isn't a second one
            near = para[max(0, m.start() - 40):m.end() + 40]
            if rx is TENURE_RX[0] and not re.search(r"\b(?:I|I'?ve|I'?m|[Mm]e|[Mm]y|[Ww]e|[Ww]e'?ve)\b", near):
                continue
            # someone else's years ("Techs with 20 years of experience told me..."): a third party just before the figure (2026-10-27)
            if rx is TENURE_RX[0] and re.search(r"\b(?:techs?|technicians?|plumbers?|electricians?|contractors?|installers?|pros|guys|folks|people|someone|somebody|anybody|anyone|he|she|they|a tech|the tech|my (?:dad|father|grandfather|uncle|neighbor|neighbour))\b(?:(?!\b(?:I|I'?ve|I'?m|my|me|we)\b)[^.!?]){0,30}$", para[max(0, m.start() - 45):m.start()], re.I):
                continue
            # "been ... for N years" counts only with the persona as its subject ("I've been...", not "the heater has been...")
            # "been / spent / worked / working ... for N years" counts only with the persona as its subject:
            # "I've been...", "I spent...", "My hands have been..." (check 29); not "the heater has been...",
            # "that old compressor kept working...", "my furnace has been running..." (2026-10-27)
            if rx is TENURE_RX[1] and re.match(r"(?:been|spent|worked|working|wired|wiring)\b", m.group(0), re.I) and not re.search(r"(?:\b(?:I|I'?ve|I have|I had|I'?d|we|we'?ve|we have)\s+(?:\w+\s+){0,2}|\bmy\s+(?:hands|knees|back|eyes|life|whole life|career)\s+(?:have|has|had)\s+|(?:^|[.!?]\s+)(?:(?:after|from|since|with|in)\s+)?)$", para[max(0, m.start() - 30):m.start()], re.I):
                continue
            seen.add(m.start(1)); spans.append((m.start(1), m.end(1)))
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

# ---------------------------------------------------------------- items and sentences (report only)
ORDINALS = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()
_SIGN_WORDS = r"(?:Step|Mistake|Item|Reason|Sign|Rung|Fix|Check|Tip|Thing|Rule|Secret|Cut|Colou?r|Shade|Knot|Habit|Trick|Piece|Swap|Way)"
# "Number one.", "Mistake one.", and (P19, style) "Rule number three.", "Secret number five."
SIGNPOST = re.compile(r"(?:^|(?<=[.!?]\s))(?:And |So |Now,? )?(?:" + _SIGN_WORDS + r" number |[Nn]umber |" + _SIGN_WORDS + r" )(" + "|".join(ORDINALS) + r"|\d{1,2})\b")
I_LINE = re.compile(r"\bI(?:'d|'m|'ve|'ll)?\b")

TITLE_WORD_MIN, TITLE_WORD_FIRST_SECONDS = 2, 60   # P19 (operator 2026-10-29, suggestion 2 of the style study)
_ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
_TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()

def _digits_to_words(s):
    """ "10 YEARS" -> "ten years", so a title's digits match a script written for the voice."""
    def w(m):
        n = int(m.group(0))
        if n < 20: return _ONES[n]
        if n < 100: return _TENS[n // 10] + ("" if n % 10 == 0 else "-" + _ONES[n % 10])
        return m.group(0)
    return re.sub(r"\b\d{1,2}\b", w, s)

def title_words_check(text, title, facts, wpm):
    """The pack's title-words that the locked title uses: each must be said at least twice, once in the first minute.
    Returns (report lines, fix-on-sight lines)."""
    entries = facts.get("title_words") or []
    if not entries or not title:
        return [], []
    t = _digits_to_words(title.lower())
    spoken = _digits_to_words(" ".join(spoken_paragraphs(text)).lower())
    rep_parts, fix = [], []
    for e in entries:
        rx = re.compile(r"\b" + r"[\s-]+".join(re.escape(x) for x in e.split()) + r"\w*")
        if not rx.search(t):
            continue
        hits = [m.start() for m in rx.finditer(spoken)]
        first = len(spoken[:hits[0]].split()) / wpm * 60 if hits else None
        rep_parts.append(f"{e} {len(hits)}" + (f" (first at about {first:.0f} s)" if hits else ""))
        if len(hits) < TITLE_WORD_MIN:
            fix.append(f"[TITLE WORD] \"{e}\" is in the title and said {len(hits)} time(s); say it at least {TITLE_WORD_MIN} times, once in the first minute")
        elif first > TITLE_WORD_FIRST_SECONDS:
            fix.append(f"[TITLE WORD] \"{e}\" is first said at about {first:.0f} seconds; say it in the first minute")
    return ([("  TITLE WORDS: " + "; ".join(rep_parts)) if rep_parts else "  TITLE WORDS: none of the pack's title-words is in the title"], fix)

def item_report(text, facts, wpm):
    """Finds the spoken signposts in order ("Number one." ... "Step two."), and returns report lines:
    item one's word, each item's words against the pack's band, items with no "I" line or no "but", and the sentence stats."""
    # the CTA marker blocks aren't item content (iter-07: they inflated the long-item flags)
    full = " ".join(spoken_paragraphs(re.sub(r"===START CTA.*?===END CTA===", " ", text, flags=re.S)))
    starts, want = [], 1
    for m in SIGNPOST.finditer(full):
        g = m.group(1).lower()
        n = int(g) if g.isdigit() else ORDINALS.index(g) + 1
        if n == want:
            starts.append(m.start()); want += 1
    out = []
    if starts:
        lo, hi = facts.get("item_words") or (0, 10 ** 6)
        first_word = len(full[:starts[0]].split())
        secs = first_word / wpm * 60
        cap = facts.get("first_item_seconds")
        out.append(f"  ITEMS: {len(starts)} | item one at word {first_word} (about {secs:.0f} seconds at {wpm})"
                   + (f"  << later than {cap} seconds" if cap and round(secs) > cap else ""))
        sizes, no_i, no_but, no_short = [], [], [], []
        for k, a in enumerate(starts):
            chunk = full[a:starts[k + 1]] if k + 1 < len(starts) else full[a:]
            n = len(chunk.split())
            sizes.append(f"{k + 1} = {n}" + (" <<" if facts.get("item_words") and not lo <= n <= hi else ""))
            if not I_LINE.search(chunk):
                no_i.append(str(k + 1))
            if not re.search(r"\bbut\b", chunk, re.I):
                no_but.append(str(k + 1))
            if not any(len(x.split()) <= 6 for x in sentences(chunk)):
                no_short.append(str(k + 1))
        band = sum(1 for k, a in enumerate(starts)
                   if lo <= len((full[a:starts[k + 1]] if k + 1 < len(starts) else full[a:]).split()) <= hi)
        out.append("  item words: " + ", ".join(sizes) + " (the last runs to the end of the script)")
        if facts.get("item_words"):
            out.append(f"  in band {lo}-{hi}: {band} of {len(starts)}")
        out.append(f"  no 'I' line: {', '.join(no_i) or 'none'} | no 'but': {', '.join(no_but) or 'none'} | no sentence of 6 words or fewer: {', '.join(no_short) or 'none'}")
    else:
        out.append("  ITEMS: no spoken signposts found (\"Number one.\", \"Step one.\" ...)")
    lens = [len(s.split()) for p in spoken_paragraphs(text) for s in sentences(p)]
    if lens:
        cap = facts.get("sentence_max") or SENTENCE_MAX
        out.append(f"  SENTENCES: {len(lens)} | mean {sum(lens) / len(lens):.1f} words | 6 or fewer {100 * sum(1 for n in lens if n <= 6) / len(lens):.1f}%"
                   f" | over 25: {sum(1 for n in lens if n > 25)} | longest {max(lens)} | over {cap}: {sum(1 for n in lens if n > cap)}")
    return out

# ---------------------------------------------------------------- scan
def scan(text, extra_bans, lifts, ref_runs=None, allows=None, facts=None, title=None):
    fix, judge = [], []
    once_judged = {}       # letter sets and two-way words: judged once, at the first use, with a count
    for m in VOICE_TAG_LINE.finditer(script_part(text)):
        fix.append(f"[MECHANICAL: bracket or voice tag in the script (tags go only in the VO copy)] {m.group(1)}")
    facts = facts or {"name": [], "book": [], "tenure": None, "once": []}
    for src, run in copy_check(text, ref_runs, allows):
        fix.append(f"[COPIED FROM REFERENCE: {src}] \"{run}\" ({len(run.split())} words in a row)")
    fix.extend(example_check(text, (facts or {}).get("examples"), allows))
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
        for rx, name in SPOKEN:
            for m in re.finditer(rx, para):
                fix.append(f"[SPOKEN: {name}] ...{ctx(m)}...")
        for m in SPOKEN_LETTERS.finditer(para):
            ok = SPOKEN_LETTERS_OK | facts.get("letters_ok", set())
            if m.group(0).rstrip("s") not in ok and m.group(0) not in ok:
                key = "L:" + m.group(0).rstrip("s")
                if key not in once_judged:
                    once_judged[key] = [len(judge), 0]
                    judge.append(f"[SPOKEN, judge: letters '{m.group(0)}' (keep only if people say it as letters; otherwise the words)] ...{ctx(m)}...")
                once_judged[key][1] += 1
        for m in SPOKEN_TWO_WAYS.finditer(para):
            key = "W:" + m.group(0).lower()
            if key not in once_judged:
                once_judged[key] = [len(judge), 0]
                judge.append(f"[SPOKEN, judge: '{m.group(0)}' can be said two ways; reword if both fit] ...{ctx(m)}...")
            once_judged[key][1] += 1
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
    for i, n in once_judged.values():
        judge[i] += f" (x{n} in the script)"
    fix.extend(repeated_sentences(paras))
    for para in paras:
        for s in sentences(para):
            if len(s.split()) > (facts.get("sentence_max") or SENTENCE_MAX):
                fix.append(f"[SENTENCE OVER {facts.get('sentence_max') or SENTENCE_MAX} WORDS] ({len(s.split())} words) \"{s[:90]}...\" (split it; join two with \"but\" only where it turns)")
    whole = "\n\n".join(paras)
    for trig, need, name in facts.get("require", []):
        if trig.search(whole) and not need.search(whole):
            fix.append(f"[NICHE/PERSONA REQUIRED: {name}] the script brings up \"{trig.search(whole).group(0)}\" but leaves this out")
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
                # an instruction ("Don't touch it. It's fragile.") is not a reframe
                if re.match(r"(?i)do(?:n['\u2019]?t| not)\b", m.group(0)) and re.search(r"(?:^|[.!?,]\s+|\b(?:and|or|just|never|so)\s+)$", para[:m.start()], re.I):
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
    ap.add_argument("--final", action="store_true", help="the delivered text: running under the length minimum is fix-on-sight")
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
    for line in item_report(text, facts, wpm):
        print(line)
    tw_lines, tw_fix = title_words_check(text, a.title, facts, wpm)
    for line in tw_lines:
        print(line)
    fix.extend(tw_fix)
    if a.final and mins < minimum:
        fix.append(f"[LENGTH] {words} spoken words = about {mins:.1f} minutes at {wpm} words a minute; the minimum is {minimum}")
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
        # the profile's book title counts as a fact source too ("Three Hundred Budget-Friendly Ways...": P19 follow-up, iter-07)
        missing = number_check(text, "\n".join(open(f, encoding="utf8", errors="ignore").read() for f in a.pack) + "\n" + "\n".join(facts["book"]))
        print(f"\nNUMBERS NOT FOUND IN THE FACT SOURCE ({len(missing)})  (invented, or derived: confirm the math)")
        for v, s in missing[:30]:
            print(f"  {v:g}  <<  {s[:110]}")
    sys.exit(1 if fix else 0)

if __name__ == "__main__":
    main()
