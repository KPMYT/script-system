#!/usr/bin/env python3
"""
verify_output.py: re-counts a delivered script output against its own AUDIT EVIDENCE block.

The writer's audit can't be taken on trust (plumbing run 03 claimed "mechanical 0" over 122 curly
quotes, and quoted originality facts the script didn't contain). Before a judge reads a test output,
the main session runs this on the saved output; its findings go to the judge as facts (P13, 2026-10-27).

Usage:
  python3 tools/verify_output.py OUTPUT [--script SCRIPT] [--rules FILE ...]

  OUTPUT    the saved output as pasted: the script, then VERDICT / FORMAT CHECK / ROTATION LOG ENTRY /
            AUDIT EVIDENCE (and the VO copy, which is ignored).
  --script  the script on its own, when it's saved separately (otherwise everything in OUTPUT before
            the first VERDICT line is read as the script).
  --rules   the niche pack and persona profile, for the words per minute, the length minimum and the
            item band (the same files the scanner reads).

It reports:
  - curly quotes in the script against the evidence's "mechanical n"
  - spoken words and minutes against the evidence's Length line
  - the scanner's ITEMS and SENTENCES lines (item one's word, each item's words, items with no "I" line)
  - every quoted line in the AUDIT EVIDENCE block that the script doesn't contain
  - the reframe floor against the evidence's "reframes n"
Exit 1 when any claim doesn't match the script. It reads; it never edits.
"""
import argparse
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("scanner", os.path.join(HERE, "..", "core", "script-scanner.py"))
scanner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scanner)

CURLY = re.compile("[‘’“”]")
QUOTED = re.compile("[\"“]([^\"“”]{12,}?)[\"”]")

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").lower()
    return " ".join(re.findall(r"[a-z0-9']+", s))

def split_output(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.match(r"^\s*VERDICT\b", line):
            return "\n".join(lines[:i]), "\n".join(lines[i:])
    return text, ""

def evidence_block(rest):
    m = re.search(r"^\s*AUDIT EVIDENCE\s*$(.*?)(?=^\s*VO COPY\b|\Z)", rest, re.M | re.S)
    return m.group(1) if m else ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output")
    ap.add_argument("--script")
    ap.add_argument("--rules", nargs="*", default=[])
    a = ap.parse_args()
    text = open(a.output, encoding="utf8", errors="ignore").read()
    script, rest = split_output(text)
    if a.script:
        script = open(a.script, encoding="utf8", errors="ignore").read()
    ev = evidence_block(rest)
    _, lifts, _, facts = scanner.read_rules(a.rules)
    wpm, minimum = facts.get("wpm") or 150, facts.get("min") or 8
    problems = []

    print(f"VERIFY: {a.output}")
    if not ev:
        print("  no AUDIT EVIDENCE block found")
        problems.append("no AUDIT EVIDENCE block")

    # mechanical: curly quotes
    curly = len(CURLY.findall("\n".join(scanner.spoken_paragraphs(script))))
    m = re.search(r"mechanical (\d+)", ev)
    claimed = int(m.group(1)) if m else None
    print(f"  curly quotes in the script: {curly}" + (f" | evidence says mechanical {claimed}" if claimed is not None else ""))
    if claimed is not None and curly > claimed:
        problems.append(f"MECHANICAL CLAIMED {claimed}, the script has {curly} curly quotes")

    # length
    words = sum(len(p.split()) for p in scanner.spoken_paragraphs(script))
    mins = words / wpm
    m = re.search(r"Length:\s*([\d,]+) words", ev)
    print(f"  spoken words: {words} (about {mins:.1f} minutes at {wpm}; minimum {minimum})"
          + (f" | evidence says {m.group(1)}" if m else ""))
    if mins < minimum:
        problems.append(f"LENGTH {words} words = about {mins:.1f} minutes, under the minimum of {minimum}")
    if m and abs(int(m.group(1).replace(",", "")) - words) > max(30, 0.03 * words):
        problems.append(f"LENGTH CLAIMED {m.group(1)} words, the script has {words}")

    # items and sentences
    for line in scanner.item_report(script, facts, wpm):
        print(line)
        if "<< later than" in line:
            problems.append("ITEM ONE late: " + line.strip())

    # reframes
    reframes = scanner.scan(script, [], lifts, facts=facts)[3]
    m = re.search(r"reframes (\d+)", ev)
    if m and len(reframes) > int(m.group(1)):
        problems.append(f"REFRAMES CLAIMED {m.group(1)}, the scanner's floor is {len(reframes)}")

    # quoted evidence lines that aren't in the script
    body = norm(script)
    missing = []
    for q in QUOTED.findall(ev):
        if "[" in q:          # a pattern such as "Number [two to fifteen] is...", not a quoted line
            continue
        parts = [p for p in re.split(r"\.\.\.|…", q) if len(norm(p).split()) >= 3]
        for p in parts:
            if norm(p) and norm(p) not in body:
                missing.append(q.strip()); break
    quoted = len(QUOTED.findall(ev))
    print(f"  quoted lines in the evidence: {quoted} | not found in the script: {len(missing)}")
    for q in missing:
        print(f"    NOT IN THE SCRIPT: \"{q[:100]}\"")
        problems.append(f"QUOTE NOT IN THE SCRIPT: \"{q[:60]}\"")

    print(f"\nDISCREPANCIES ({len(problems)})")
    for p in problems:
        print("  " + p)
    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
