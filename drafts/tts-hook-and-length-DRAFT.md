# Draft: writing for the voice, the plumbing hook ending, and real runtimes (2026-10-25)

**Status (2026-10-25):** Part 1 applied as written. Part 2 applied with the operator's change (a count line in place of the promise block; see `HANDOFF.md`, "Operator decisions, 2026-10-25"). Part 3 not applied ("do not change 3 yet"). VAs don't ask for lengths; the VO copy tags stay. The text below is the draft as it was put to the operator.

**When drafted, nothing here was applied yet.** It answers the operator's three points of 2026-10-25. The evidence is in `studies/recent-uploads-2026-10-25/analysis.md`. Each part can be answered on its own ("1 yes, 2 yes, 3 no"). Part 2 changes a locked decision (P3), so it's also in `PROPOSALS.md` as P10.

---

## Part 1. Write every word the way the voice should say it (every channel)

**The operator (2026-10-25):** "we should write them so that it is always read out properly by the text-to-speech... verify this across all scripts, across all channels, that there's nothing which is read out in such a way that the voiceover can hallucinate it. It has to be written for text-to-speech."

**What went wrong:** Sam's bench video misread every lumber size, five times: "a single 2x12 and a 2x4" came out as "a single 2x12 and **a 24**", "one 2x4, 8 ft" as "**1 2 4 8 ft**", "one 2x12 and one 2x4" as "**one 212 and one two host**". Mark's voice dropped "AAV" twice ("It is **a of** a short pipe", "And **the The** has to sit"). Dale's read "Haha" out loud. The library itself teaches "2x4": the woodworking pack's model line "First, one 2x4 from the big box store" and the core's "one 2x4, about four bucks". ElevenLabs' own advice is to write numbers, units, symbols and abbreviations as words, and to put spaces between letters that should be read one by one.

### 1a. `core/workflow.md` §4, "Writing for the voice"

**Before** (one bullet):
> - **Spell out anything a voice might misread,** the way it's said: measurements with fractions ("five and three-quarters inches") and degrees ("45 degrees"). Never symbols like ° or ½.

**After** (that bullet becomes this block):
> - **Write every word the way the voice should say it** (operator, 2026-10-25: "It has to be written for text-to-speech"). The voice reads only what's on the page and guesses at anything that isn't a plain word, and it guesses differently from one sentence to the next: in one video, "2x12" came out right once and as "212" later, and "2x4" as "a 24" and "two host". Briefs, research packs and reference transcripts write sizes and units the short way; the narration never does.
>   - **Lumber and any size with an "x" in it, in words:** "a two by four", "two two by twelves", "a four by eight sheet of plywood", "a one by six". Never 2x4, 2 x 4, 2×4 or 2-by-4.
>   - **Units as full words:** inches, feet, ounces, pounds, gallons, percent, degrees, volts. Never in, ", ft, ', oz, lb, gal, %, ° or psi ("pounds of pressure").
>   - **Fractions in words:** "three-eighths of an inch", "sixteen and a half inches", "a quarter inch for every foot". Never a slash (3/8, 16 1/2) or ½.
>   - **Never two numbers side by side.** Turn the phrase so a word sits between them: "one eight-foot two by four", not "one 2x4, 8 ft"; "four pieces at ten inches", not "4 10-inch pieces".
>   - **No abbreviation or code a person wouldn't say aloud.** Say what it stands for: "an air admittance valve" (the voice dropped "AAV" twice), "number two grade", "kiln-dried". A short set of letters everyone says as letters (EPA) is fine, with no periods. A stamp or model code is written the way a person reads it: "the stamp that says K D 19".
>   - **No symbols in the narration:** x, /, %, &, +, #, =, ~, @, °. Write the word ("and", "plus", "about").
>   - **Money:** whole-dollar prices stay as digits ("$50", "$2,500", "$4 to $10", with the dollar sign on both ends of a range), the forms every recent voiceover read correctly. Never "$4.00", cents, "$1.4M" or "50k" (write "$1.4 million", "50 thousand dollars").
>   - **No laugh or filler sounds written as words** ("haha", "hmm", "ugh"): the voice says them as words. Delivery belongs in the voiceover copy's tags ([chuckles]).
>   - **Words with two pronunciations:** where "lead" (the metal), "bow" or "bowed" (a bent board) or "wound" could be read the other way, reword so only one reading fits: "lead paint" is clear; "under their lead limit" isn't ("under their limit for lead in paint").
>   - The scanner fails a script on the mechanical forms above and lists the two-pronunciation words to judge.

**Also in §4, one more clause on the line above it ("Prices, years and stats are digits..."):** "...Small everyday counts can be words ("two boards"). **The unit after a digit is always a word ("19 percent", "8 feet").**"

### 1b. The library's own examples (so the writer stops copying the short form)

- `woodworking-scripts/SKILL.md`, "Into the materials": "First, one 2x4 from the big box store, about four bucks" becomes "First, one two by four from the big box store, about four bucks".
- `core/retention-mechanics.md` §2, the hook's transformation: "(one 2x4, about four bucks)" becomes "(one two by four, about four bucks)".
- `plumbing-scripts/SKILL.md`, "Safety", default 3: "Peroxide means the 3% drugstore bottle" becomes "Peroxide means the 3 percent drugstore bottle".

### 1c. The scanner (`core/script-scanner.py`)

A new family of **fix-on-sight** findings, labelled `[SPOKEN: ...]`, on the spoken text only (markers, the audit and the VO copy header are already skipped):

| Finding | Catches (examples) |
|---|---|
| size written with x or digits | 2x4, 2 x 12, 4×8, 2-by-4, 2 by 4 |
| unit abbreviation | 8 ft, 3 in., 3-in screws, 11in, 8 oz, 5 lb, 200 gal, 60 psi, 6", 8' |
| fraction with a slash | 3/8, 16 1/2 |
| percent sign | 19% |
| symbol | & + # = ~ @ (the core already fails ° and ½ as non-standard characters) |
| two numbers side by side | 1 2 4 8, "4 10-inch" |
| money written short | $4.00, $1.4M, 50k |
| abbreviation | No. 2, vs., etc., e.g., i.e., approx., Dr., St. |
| letters-and-digits code | KD19, S4S, B12 |
| laugh or filler word | haha, hmm, ugh, lol |

And two **judged** findings (listed, not failed): a run of two to five capital letters (AAV, PEX, CPSC: keep it only if people say it as letters, otherwise say the words), and the two-pronunciation words (lead, bow, bowed, bows, wound).

`tests/run_checks.py` gets a check that the scanner fails each form, passes the word forms ("a two by four", "three-eighths of an inch", "19 percent", "$4 to $10"), and that the library's narration examples carry no "2x4". The audit needs no new line: D3 already requires every fix-on-sight scanner finding at zero.

### 1d. Not changed

- Prices, years and stats stay digits. All seven videos read every whole-dollar price correctly, and the scanner's number check reads both forms. **If you'd rather go all the way** (every number in words, as ElevenLabs recommends for its fastest models), say so and it's a one-line change to 1a.
- Briefs, research packs and the ideation skills can keep "2x4": they're never read by the voice. Titles too.

---

## Part 2. Remove the promise block from the plumbing hook (P10)

**The operator (2026-10-25):** "It ends by saying, 'The first part, I'll teach you this. The second thing I'll teach you this,' and nothing, and just goes to the first part... That doesn't make sense. I think we remove that part of the hook entirely. As in, going forward, I don't like it."

**What it changes:** P3 (2026-10-20) and the opening's job 5 in `plumbing-scripts/SKILL.md`. The forward lines **inside** the video stay ("The next one is the reason your tank sweats in July."): the operator objected to the hook, and those are what keep a list moving. If you want those gone too, say so.

**What the opening becomes:** the point → a question the viewer can answer at home → the villain line → one line of honest scope → (for a list) the count → item one. Roger's water heater opening would end "...None of this saves a tank leaking out of its own body, or one past 12 or 15 years with rust in the hot water. Eight things to check. Number one, the reset button." and item one starts about 8 seconds sooner. In the peroxide video it would start about 27 seconds sooner.

### The edits, all in `plumbing-scripts/` unless marked

1. **"The opening", job 5** ("The promise block... Right after the point, promise two or three specific later payoffs...") is deleted; job 6 becomes job 5.
2. **"Never in an opening"** gains: "a promise block or any run-down of what later items hold ("Number three tells you...", "Before we get to the fixes, you will hear...") (operator, 2026-10-25)".
3. **"Point then promise":**
   - "Point first. The first answer... comes before the first forward promise." becomes "...comes before anything else."
   - "Promise straight after. The promise block follows within about 30 seconds of the first answer." is deleted.
   - "Pay the first promise early. The first promised item is paid within about five minutes. Nothing promised in the opening is held past the middle of the video, except the safety rule or a second use for the product." becomes "**Pay forward lines fast.** A later item named in a forward line is paid within about five minutes. Nothing is promised in the opening."
   - "Keep one promise open" and the rest stay.
4. **"Ways to promise more value":** "Use two or three per video, and rotate them" becomes "Use two or three per video, in the body only (never as a list in the opening), and rotate them". "The rule that protects everything: a safety or method rule promised early" becomes "...a safety or method rule, named at the first item it touches".
5. **"The video types", the opening column:** "→ what it won't do → the promise block" (single-product fix) becomes "→ what it won't do"; "→ the count, with one money item and one safety item → one rule" (N things) becomes "→ the count"; "→ the count → one numbered item with its stake" (never-do list) and "→ the count → one numbered stake" (mistakes list) become "→ the count".
6. **"Where this pack overrides the core":**
   - The `retention-mechanics.md` §6 row: "Concrete named promises may point further than the next segment: the promise block in "The opening" and the forward lines in "Point then promise"." becomes "...further than the next segment, in the body only: the forward lines in "Point then promise" and "Ways to promise more value". Never in the opening." Source: "P3, 2026-10-20; the opening's block removed 2026-10-25 (P10)".
   - The hook row: "the curiosity is the opening question or the promise block" becomes "the curiosity is the opening question, or a surprising fact the video answers"; "the opening's six jobs" becomes "five jobs".
   - The value line row: "Not used: the promise block, in every plumbing video, does its job. The Hook line reads `value line: none (promise block)`." becomes "Not used: the opening goes from the point to item one with nothing announcing what's coming (operator, 2026-10-25). The Hook line reads `value line: none`."
7. **"Using the models"** gains: "A model's promise block is never copied: several of our hits and TheCheapFix's open with one, and the pack no longer does (2026-10-25). The excerpts' group 5 lines are for forward lines in the body."
8. **The banned list:** "Concrete, named promises are the plumbing exception (P3)." becomes "...the plumbing exception (P3), in the body only."
9. **"Before handing over":** "the promise block follows the first answer; every promise is paid, the first within about five minutes, and no stretch runs past about five minutes without a forward line or a payoff" becomes "no promise block: the opening ends on the count or item one; every forward line is paid within about five minutes, and no stretch runs past about five minutes without a forward line or a payoff".
10. **`references/unit-plan-template.md`:** the "promise block:" line is deleted; the PROMISES CHECK line becomes "each forward line -> where it's paid [within ~5 min; nothing promised in the opening]".
11. **Elsewhere:** `HANDOFF.md` §3 records the decision, `PROPOSALS.md` P10 is closed, and Roger's and Mark's profiles keep their "concrete named promises paid inside the video (P3)" wording, which still holds for the body.

---

## Part 3. Make the 12-minute plumbing minimum really 12 minutes

**What went wrong:** Roger's, Mark's and the Vintage Pipefitter's profiles leave "Words per minute" unset, so the script-writer counts every plumbing script at 150 words a minute (1,800 words for 12 minutes). The voices now read at about 167 to 190. The Vintage Pipefitter's peroxide script, 2,141 words, passes the check at 150 (about 14 minutes) and plays in 11:15. The persona template already says to measure this from the channel's real voiceovers. Hank (185), Dale (170) and Sam (174) have theirs set.

| Profile | Before | After | Measured from |
|---|---|---|---|
| `personas/roger-the-pipe-guy.md` | Words per minute (optional, for runtime estimates): not set | Words per minute (for runtime and the 12-minute minimum): 170 | the two newest videos (167, 170); the older study videos ran about 152 |
| `personas/mark-silverbridge.md` | (same) | 185 | the newest video (185); the older ones about 159 |
| `personas/vintage-pipefitter.md` | (same) | 190 | the newest video (190); the older ones about 164 |

So 12 minutes becomes about 2,040 words for Roger, 2,220 for Mark and 2,280 for Vintage, still filled with value and never padding (the pack's rule). These numbers come from one or two new videos each, so the next few uploads should re-check them.

**Not in this draft, and worth thinking about:** shorter videos lower average view duration in minutes even when viewers watch the same share. Roger's two newest are about 14 minutes against 24 for his older ones. Judge the new scripts on average percentage viewed at seven days, against each channel's normal.

---

## Not rule changes: things to check

- **Dale's newest video** ("I still don't understand how we make so much money on 2x4s") has "stick around", "the bonus at the end", "I'm Dale Oakfield", "at our table" sales claims, an 11-item list and the old ending. The script-writer's scanner fails a script on the first two, so either this script wasn't written with it or a NOT READY script was uploaded. Worth asking the VA which they used.
- **The voiceover copy's tags:** Sam's video was voiced from the VO copy, and the caption's one "[snorts]" falls exactly where the VO copy put `[warm]` ("Sand it smooth. [warm] Those round plugs..."). Most tags come out as intended (none of the others shows up as a sound), and the throat-clears in Roger's and Mark's videos fall mid-sentence, where no tag goes, so those are the voice itself. Worth a listen to decide whether the VO copy should keep [warm], [chuckles] and [sighs], or only the pauses.
- **VAs asking for a length:** Sam's chat passed at about 9.7 minutes and the VA then asked "MAKE IT 14-16 MINS LONG"; the chat added about 800 words, mostly real value, some padding (`analysis.md` §5). The library has no rule on it. Do you want VAs to ask for lengths, and if so, what length per channel?
- **A listen** to the spots the captions can't settle: Vintage "200 gall" (0:57, 7:20), "biofilm" (2:02) and "peracetic acid" (10:02); Hank "lead limit" (6:26); Roger's "In the In the flush it through" (1:57).
