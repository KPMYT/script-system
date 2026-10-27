#!/usr/bin/env python3
"""Measure the HVAC study transcripts (comparison file 02-openings-and-numbers.md).

Read-only on data/ and notes/. Prints markdown tables to stdout.

    python3 tools/measure.py            # per-video table, group medians, item table
    python3 tools/measure.py --open 30  # first 30 s of every transcript
    python3 tools/measure.py --check ID # per-video detail for a hand check

How things are counted (also stated in the report):
- Words: whitespace tokens of the transcript text with the [m:ss] stamp and
  bracket tags ([Music], [Applause]) removed; a token counts if it holds a
  letter or digit.
- Minutes: the meta.md duration (not the last caption stamp).
- you/your: you, your, yours, yourself, yourselves (\\byou\\b also catches
  you're, you'll, you've, you'd). I/me/my: I (and I'm, I've, I'll, I'd), me,
  my, mine, myself. "but": the word but. All per 1,000 words.
- Viewer questions ("Q"): where the caption track is punctuated (20+ full
  stops per 1,000 words; 20 of 36 videos) every "?" is counted. The other 16
  have no punctuation: their count is a hand count kept in HAND_Q (below),
  shown as "4h" in the table. count_questions_lex() is a blunt pattern count
  kept for --check only; it finds well under half the "?" questions.
- First value: the notes' "First real value" time, re-checked against the
  transcript; FV_RECHECK holds the ones moved.
- Dollar figures: "$" amounts; a number (digits or words) followed by
  dollars/bucks/cents/grand; "a dollar/a buck", "a couple/few hundred/
  thousand dollars"; each end of a spoken range counts ("75 to 125 dollars"
  = 2). "hundreds/thousands of dollars" is counted apart as a vague phrase.
- Numbers: runs of digits, or of number words two..billion (not "one",
  "half" or ordinals), each run counted once ("five grand" = 1,
  "$1,200 to $1,800" = 2).
"""
import re
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
NOTES = ROOT / "notes"

FACELESS = {"ray-duttons-garage", "hvac-exposed", "vent-exposed", "lost-survival-knowledge"}
OWN = {"roger-the-pipe-guy"}

SHORT = {
    "atlas-ac": "Atlas AC", "deanin-it-yourself": "Deanin'", "everyday-home-repairs": "Everyday HR",
    "grayfurnaceman": "grayfurnaceman", "home-renovision-diy": "RenoVision", "how-to-home": "How To Home",
    "hvac-exposed": "HVAC Exposed", "hvac-guide-for-homeowners": "HVAC Guide", "lost-survival-knowledge": "Lost Survival",
    "project-farm": "Project Farm", "ray-duttons-garage": "Ray Dutton", "roger-the-pipe-guy": "Roger (own)",
    "silver-cymbal": "Silver Cymbal", "technology-connections": "Tech Connections", "the-diy-hvac-guy": "DIY HVAC Guy",
    "the-funny-carpenter": "Funny Carpenter", "the-provident-prepper": "Provident Prepper", "vent-exposed": "Vent Exposed",
    "word-of-advice-tv": "Word of Advice",
}

# ---------------------------------------------------------------------------
# Item boundaries in list videos: (label, start, end) in m:ss, read from the
# notes' segment maps and checked against the transcript (the line at each
# start is the item's first spoken line). End = start of whatever follows the
# item (next item, interlude, plug, recap). Mid-item CTAs are cut out where
# the notes mark them (listed in CUT).
ITEMS = {
    "K2jCz3D5z_0": [("1 fan auto/on", "1:07", "4:47"), ("2 colder", "4:47", "6:10"), ("3 one temp", "6:10", "8:00"),
                    ("4 thermostat wars", "8:00", "10:18"), ("5 20-degree rule", "10:18", "12:39")],
    "qbWN3OViWxQ": [("1 crank to 60", "0:59", "2:28"), ("2 closing vents", "2:28", "3:58"), ("3 shading", "4:32", "6:43"),
                    ("4 top-offs", "6:43", "9:05"), ("5 oversizing", "9:05", "11:59")],
    "dOZ-8__G4uU": [("1 out of cooling", "0:51", "2:24"), ("2 covering", "2:45", "5:26"), ("3 power, crankcase", "6:04", "9:45")],
    "fHAlfm21vYw": [("1 flame sensor", "0:52", "3:08"), ("2 test-fire", "3:08", "4:31"), ("3 airflow", "5:01", "7:13"),
                    ("4 white pipes", "7:13", "9:14"), ("5 temp rise", "9:14", "11:01")],
    "QKPPm6M0__o": [("1 Trane", "6:58", "7:24"), ("2 Carrier", "7:24", "8:05"), ("3 Rheem", "8:05", "8:46"),
                    ("4 Mitsubishi", "8:46", "9:28"), ("5 Bosch", "9:28", "10:34")],
    "86S3ITbfzQY": [("1-2 Trane/AmStd", "1:07", "2:50"), ("3 Carrier", "2:50", "4:40"), ("4 Goodman", "4:52", "6:20")],
    "rX4eyZaHAjw": [("15 bubble wrap", "1:49", "3:04"), ("14 pipe foam", "3:04", "4:29"), ("13 draft stopper", "4:29", "5:47"),
                    ("12 Mylar", "5:47", "6:56"), ("11 hand warmers", "6:56", "8:10"), ("10 hot water bottle", "8:10", "9:30"),
                    ("9 sheeting", "9:30", "10:52"), ("8 tent", "10:52", "12:07"), ("7 propane heater", "12:07", "13:41"),
                    ("6 thermos", "13:41", "15:05"), ("5 knit cap", "15:05", "16:04"), ("4 wool", "16:04", "17:17"),
                    ("3 lanterns", "17:17", "18:33"), ("2 sleeping bag", "18:33", "19:44"), ("1 CO detector", "19:44", "21:06")],
    "_g8gQ1gg1FM": [("5 old filter out", "0:21", "0:44"), ("4 power off", "0:44", "1:47"), ("3 backward", "1:47", "2:37"),
                    ("2 not often", "2:37", "3:20"), ("1 high MERV", "3:54", "5:13")],
    "Unx9Ze10N98": [("1 airflow", "0:17", "0:54"), ("2 covering", "0:54", "1:44"), ("3 ductwork", "1:44", "2:12"),
                    ("4 insulation", "2:12", "2:49"), ("5 humidity", "2:49", "3:23"), ("6 maintenance", "3:23", "6:12")],
    "AQQH9QwC46A": [("1 coil cleaning", "0:10", "2:03"), ("2 drain + filters", "2:03", "4:27"), ("3 contactor", "4:27", "9:40"),
                    ("4 capacitor", "9:40", "12:01")],
    "SkLMRM9NnBY": [("1 coils + filter", "1:00", "3:24"), ("2 condensate", "3:24", "6:04"), ("3 capacitor", "6:04", "12:41")],
    "mP0IjyvQtxw": [("1 covering", "0:44", "3:10"), ("2 coils", "3:10", "6:40"), ("3 test furnace", "6:40", "8:34"),
                    ("4 flame sensor", "8:34", "11:51"), ("5 CO/smoke", "11:51", "14:35")],
    "erq-QuCN0G0": [("1 drafts", "0:57", "2:40"), ("2 microclimate", "2:40", "4:35"), ("3 layers", "4:35", "6:07"),
                    ("4 warm food", "6:07", "6:36"), ("5 move", "6:36", "7:17"), ("6 heat sources", "7:17", "8:14")],
    "_b6p0fkWhCY": [("1 return vents", "1:03", "1:43"), ("2 filter", "1:43", "2:57"), ("3 outdoor coil", "2:57", "8:01")],
    "--A2I2s7aNw": [("1 safety", "1:13", "1:38"), ("2 filter", "1:38", "3:09"), ("3 flame sensor + clean", "3:09", "6:24"),
                    ("4 full cycle", "6:24", "8:21")],
}
# mid-item asides cut from item word counts: (video, start, end)
CUT = {
    "K2jCz3D5z_0": [("2:01", "2:17")],     # book plug inside item 1 ("Quick thing before we move on...")
    "fHAlfm21vYw": [("2:03", "2:16")],     # book plug inside item 1 ("Quick one before we keep going...")
}

# Viewer questions in the 16 transcripts whose captions carry no punctuation:
# hand count. Candidates were listed by a broad pattern (an auxiliary before a
# pronoun, a wh-word before an auxiliary, "what if", "guess what/how", "ever
# wonder") and each was read in context; kept only if it is a question put to
# the viewer, or voiced for the viewer ("you might be asking..."). Questions a
# presenter asks himself while working, reported speech and "would you please
# hit like" are left out. Statement-shaped questions can't be found this way,
# so these are floors.
HAND_Q = {
    "r_uP9itJ0HQ": ["0:15", "3:52", "4:30", "5:19"],
    "dRL13JlclhM": ["0:00"],
    "--A2I2s7aNw": [],
    "sRvH-io-ZtA": ["0:39", "4:12"],
    "X3Y-yA42UBk": [],
    "J95l9Ue4224": ["14:15", "15:00"],
    "AQQH9QwC46A": [],
    "i8nDBZo6XyE": [],
    "Unx9Ze10N98": ["0:00", "6:14"],
    "_b6p0fkWhCY": ["8:32"],
    "qAxJb0J1HH0": ["4:56"],
    "HnMuNCl7tZ8": ["7:28", "8:48"],
    "Is0pv2Qnza0": ["0:23", "3:12"],
    "SkLMRM9NnBY": [],
    "y07w1hiKIrI": [],
    "erq-QuCN0G0": ["0:00", "13:35", "14:46", "14:50"],
}

# First real value, re-checked against the transcript: where the notes'
# timestamp is more than 4 s off the line it quotes, or the line the notes
# describe starts later, the transcript time is used. Everything else keeps
# the notes' figure.
FV_RECHECK = {
    "K2jCz3D5z_0": "1:13",   # "Look at your fan setting." (notes 1:04 = end of hook)
    "_ZgVjFpBnQA": "1:49",   # "That filter is not there to clean your air." (notes 1:42)
    "UdyqMC1GVxQ": "1:42",   # "That patch is now damaged" (notes 1:44, slats at 1:49)
    "dOZ-8__G4uU": "0:58",   # "do not just leave the thermostat set to cool" (notes 0:53 = "Number one")
    "fHAlfm21vYw": "1:08",   # "You reset it instead of reading it." (notes 0:53, flame sensor 1:22)
    "x2BK-zr4raE": "0:21",   # the two ways to buy (kept; first figure 0:49)
    "1bRsFAMgZRQ": "0:08",   # "four types of igniters" starts 0:08 (notes 0:11)
}


def sec(t):
    m, s = t.split(":")
    return int(m) * 60 + int(s)


def fmt(s):
    s = int(round(s))
    return f"{s // 60}:{s % 60:02d}"


TAG = re.compile(r"\[[A-Za-z ]+\]")


def load(path):
    segs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\[(\d+):(\d+)(?::(\d+))?\]\s?(.*)", line)
        if not m:
            continue
        if m.group(3):
            t = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
        else:
            t = int(m.group(1)) * 60 + int(m.group(2))
        segs.append((t, TAG.sub(" ", m.group(4)).replace("’", "'")))
    return segs


def words(text):
    return [w for w in text.split() if re.search(r"[A-Za-z0-9]", w)]


def meta(path):
    t = path.read_text(encoding="utf-8")
    d = re.search(r"Duration:\s*([\d:]+)\s*\((\d+) s\)", t)
    v = re.search(r"Views:\s*([\d,]+)", t)
    r = re.search(r"Views / normal:\s*([\d.,]+)", t)
    typ = re.search(r"Video type:\s*([^(\n]+)", t)
    title = t.splitlines()[0].lstrip("# ").strip()
    return dict(dur=int(d.group(2)), views=int(v.group(1).replace(",", "")),
                ratio=float(r.group(1).replace(",", "")), type=typ.group(1).strip(), title=title)


def notes(channel, vid):
    p = NOTES / f"{channel}__{vid}.md"
    if not p.exists():
        return {}
    t = p.read_text(encoding="utf-8")
    out = {}
    h = re.search(r"Hook:\s*~?(\d+)\s*w(?:ords)?,\s*~?(\d+)\s*s", t)
    if h:
        out["hook_w"], out["hook_s"] = int(h.group(1)), int(h.group(2))
    f = re.search(r"First real value:\s*\[(\d+:\d+)\]", t)
    if f:
        out["fv"] = sec(f.group(1))
    return out


NUMW = ("two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
        "seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand "
        "million billion").split()
NUMTOK = r"(?:\d[\d,.]*|" + "|".join(NUMW) + r"|one|a)"


def count_numbers(text):
    toks = re.findall(r"[A-Za-z]+|\$?\d[\d,.]*%?°?", text.lower())
    n, prev = 0, False
    for tok in toks:
        isnum = bool(re.match(r"\$?\d", tok)) or tok in NUMW
        # "one" joins a run already started ("twenty one") but never starts one
        if tok in ("and", "one") and prev:
            continue
        if isnum and not prev:
            n += 1
        prev = isnum
    return n


MONEYWORD = r"(?:dollars?|bucks?|cents?|grand)"
SPOKEN_NUM = r"(?:\d[\d,.]*|(?:(?:" + "|".join(NUMW + ["one", "a", "and", "couple", "few", "of"]) + r")[\s-]*)+)"


def count_dollars(text):
    t = text.lower()
    n = 0
    # $ amounts, with an optional spoken range partner before them
    dollar = re.compile(r"\$\s?\d[\d,.]*(?:\s?(?:k|hundred|thousand|million|grand))?")
    n += len(dollar.findall(t))
    t = dollar.sub(" MONEY ", t)
    t = re.sub(r"money\s+(?:dollars?|bucks?)", "money", t)  # "$10 bucks" once
    # vague phrases counted apart
    vague = len(re.findall(r"\b(?:hundreds|thousands|millions) of (?:dollars|bucks)\b", t))
    t = re.sub(r"\b(?:hundreds|thousands|millions) of (?:dollars|bucks)\b", " ", t)
    # spoken amounts: "<number words or digits> dollars/bucks/cents/grand"
    pat = re.compile(r"((?:\b(?:\d[\d,.]*|" + "|".join(NUMW + ["one", "a", "couple", "few"]) +
                     r")\b[\s-]*(?:and\s+|of\s+)?)+)" + MONEYWORD + r"\b")
    for m in pat.finditer(t):
        n += 1
        # a spoken range just before: "75 to 125 dollars", "five or six dollars"
        before = t[max(0, m.start() - 30):m.start()]
        if re.search(r"(?:\d[\d,.]*|" + "|".join(NUMW) + r")\s+(?:to|or)\s+$", before):
            n += 1
    return n, vague


Q_AUX = re.compile(r"\b(?:do|did|does|have|are|were|can|could|would|will|should|don't|didn't|doesn't|haven't|"
                   r"aren't|won't|can't|wouldn't|shouldn't)\s+you\b(?!')", re.I)
Q_WH = re.compile(r"\b(?:what|why|how|where|when|which|who)\s+(?:do|does|did|is|are|was|were|would|should|can|could|will)\s+"
                  r"(?:you|your|it|that|this|they|we|i|he|she|these|those|there)\b", re.I)
Q_MISC = re.compile(r"\bwhat if\b|\bever (?:wonder|wondered|notice|noticed)\b|\byou know what\b|\bright\?", re.I)
# statement uses of the wh pattern: "that's what it", "here's how you", "know what you", "is why it"
Q_WH_NOT = re.compile(r"(?:that's|here's|that is|here is|this is|it's|exactly|know|see|show|tell|explain|matter|"
                      r"is|about|on|from|of|at|for|and|regardless of|no matter)\s+$", re.I)


def count_questions_lex(text):
    n = len(Q_AUX.findall(text)) + len(Q_MISC.findall(text))
    for m in Q_WH.finditer(text):
        if not Q_WH_NOT.search(text[max(0, m.start() - 25):m.start()]):
            n += 1
    return n


def segs_between(segs, a, b):
    return " ".join(t for s, t in segs if a <= s < b)


def all_videos():
    for tp in sorted(DATA.glob("*/*/transcript.txt")):
        yield tp.parent.parent.name, tp.parent.name, tp


def measure():
    rows = []
    for ch, vid, tp in all_videos():
        segs = load(tp)
        text = " ".join(t for _, t in segs)
        w = len(words(text))
        m = meta(tp.parent / "meta.md")
        nt = notes(ch, vid)
        mins = m["dur"] / 60
        punct = text.count(".") / w * 1000 >= 20
        dol, vague = count_dollars(text)
        row = dict(ch=ch, vid=vid, **m, words=w, mins=mins, wpm=w / mins,
                   you=len(re.findall(r"\b(?:you|your|yours|yourself|yourselves)\b", text, re.I)) / w * 1000,
                   i=len(re.findall(r"\b(?:i|me|my|mine|myself)\b", text, re.I)) / w * 1000,
                   but=len(re.findall(r"\bbut\b", text, re.I)) / w * 1000,
                   qmark=text.count("?") if punct else None, qlex=count_questions_lex(text), punct=punct,
                   dollars=dol, vague=vague, dpm=dol / mins, npm=count_numbers(text) / mins,
                   group="own" if ch in OWN else ("faceless" if ch in FACELESS else "real"), **nt)
        if vid in ITEMS:
            row["item1"] = sec(ITEMS[vid][0][1])
        if not punct:
            row["qhand"] = len(HAND_Q.get(vid, []))
        row["q"] = row["qmark"] if punct else row.get("qhand")
        if "fv" in row:
            row["fv_notes"] = row["fv"]
            if vid in FV_RECHECK:
                row["fv"] = sec(FV_RECHECK[vid])
        if "fv" in row:
            row["dollars_open"] = count_dollars(" ".join(t for s_, t in segs if s_ < row["fv"]))[0]
        if "hook_s" in row:
            row["hook_w_recount"] = len(words(" ".join(t for s_, t in segs if s_ < row["hook_s"])))
        rows.append(row)
    return rows


def item_table():
    out = []
    for ch, vid, tp in all_videos():
        if vid not in ITEMS:
            continue
        segs = load(tp)
        cuts = [(sec(a), sec(b)) for a, b in CUT.get(vid, [])]
        lens = []
        for label, a, b in ITEMS[vid]:
            a, b = sec(a), sec(b)
            txt = " ".join(t for s, t in segs if a <= s < b and not any(c0 <= s < c1 for c0, c1 in cuts))
            lens.append((label, len(words(txt)), b - a, count_dollars(txt)[0]))
        out.append((ch, vid, lens))
    return out


def med(xs):
    xs = [x for x in xs if x is not None]
    return st.median(xs) if xs else None


def main():
    args = sys.argv[1:]
    if args and args[0] == "--open":
        lim = int(args[1]) if len(args) > 1 else 30
        for ch, vid, tp in all_videos():
            segs = load(tp)
            txt = " ".join(t for s, t in segs if s < lim)
            print(f"=== {ch} {vid} ({len(words(txt))} words before {lim}s)\n{txt}\n")
        return
    if args and args[0] == "--check":
        for r in measure():
            if r["vid"] == args[1]:
                for k, v in r.items():
                    print(k, v)
        return
    rows = measure()
    print("| Channel | Video | Type | ×normal | Words | Min | WPM | you /1k | I /1k | but /1k | Q | Q /1k | $ figs | $ /min | nums /min | Hook w (recount) / s | $ before first value | First value | Item 1 |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    order = {"real": 0, "faceless": 1, "own": 2}
    for r in sorted(rows, key=lambda r: (order[r["group"]], r["ch"], -r["ratio"])):
        hook = f'{r.get("hook_w", "?")} ({r.get("hook_w_recount", "?")}) / {r.get("hook_s", "?")}'
        fv = fmt(r["fv"]) if "fv" in r else "?"
        it = fmt(r["item1"]) if "item1" in r else "–"
        q = f'{r["q"]}' if r["punct"] else f'{r["q"]}h' 
        print(f'| {SHORT[r["ch"]]} | `{r["vid"]}` | {r["type"]} | {r["ratio"]:.1f} | {r["words"]:,} | {fmt(r["dur"])} | '
              f'{r["wpm"]:.0f} | {r["you"]:.1f} | {r["i"]:.1f} | {r["but"]:.1f} | {q} | {r["q"] / r["words"] * 1000:.1f} | {r["dollars"]} | '
              f'{r["dpm"]:.2f} | {r["npm"]:.1f} | {hook} | {r.get("dollars_open", "?")} | {fv} | {it} |')
    print()
    print("| Group | n | ×normal | Words | Min | WPM | you /1k | I /1k | but /1k | Q /1k | $ figs | $ /min | nums /min | Hook w | Hook s | First value s | Item 1 s |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for g, name in (("real", "Real people"), ("faceless", "Faceless / persona"), ("own", "Roger the Pipe Guy (own)")):
        rs = [r for r in rows if r["group"] == g]
        qk = med([r["q"] / r["words"] * 1000 for r in rs])
        ql = med([r["dollars"] for r in rs])
        vals = [med([r["ratio"] for r in rs]), med([r["words"] for r in rs]), med([r["mins"] for r in rs]),
                med([r["wpm"] for r in rs]), med([r["you"] for r in rs]), med([r["i"] for r in rs]),
                med([r["but"] for r in rs]), qk, ql, med([r["dpm"] for r in rs]), med([r["npm"] for r in rs]),
                med([r.get("hook_w") for r in rs]), med([r.get("hook_s") for r in rs]),
                med([r.get("fv") for r in rs]), med([r.get("item1") for r in rs])]
        cells = []
        for i, v in enumerate(vals):
            if v is None:
                cells.append("–")
            elif i == 2:
                cells.append(fmt(v * 60))
            elif i in (1,):
                cells.append(f"{v:,.0f}")
            else:
                cells.append(f"{v:.1f}" if i not in (3, 11, 12, 13, 14) else f"{v:.0f}")
        print(f"| {name} | {len(rs)} | " + " | ".join(cells) + " |")
    print()
    print("| Channel | Video | Items | Words per item (each, in spoken order) | Shortest | Median | Longest | Median s | $ figures per item | Items with a $ figure | Most in one item |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for ch, vid, lens in item_table():
        ws = [x[1] for x in lens]
        ss = [x[2] for x in lens]
        ds = [x[3] for x in lens]
        print(f'| {SHORT[ch]} | `{vid}` | {len(ws)} | {", ".join(str(x) for x in ws)} | {min(ws)} | {st.median(ws):.0f} | '
              f'{max(ws)} | {st.median(ss):.0f} | {", ".join(str(x) for x in ds)} | {sum(1 for d in ds if d)} of {len(ds)} | {max(ds)} |')
    print()
    print("| Group | $ figures /1k words (median) | $ figures + vague money phrases /1k (median) | Videos 12 min or longer |")
    print("|---|---|---|---|")
    for g, name in (("real", "Real people"), ("faceless", "Faceless / persona"), ("own", "Roger (own)")):
        rs = [r for r in rows if r["group"] == g]
        print(f'| {name} | {med([r["dollars"] / r["words"] * 1000 for r in rs]):.1f} | '
              f'{med([(r["dollars"] + r["vague"]) / r["words"] * 1000 for r in rs]):.1f} | '
              f'{sum(1 for r in rs if r["dur"] >= 720)} of {len(rs)} |')


if __name__ == "__main__":
    main()
