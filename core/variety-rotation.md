---
name: variety-rotation
description: Keeps scripts from sounding the same, within a channel and across the portfolio. Rotates both the move and the actual line in nine slots (opening, hook turn, segment bridges, return after the mid-CTA, adversary and doubter, personality lines, swear words, CTA wording, closing line), with the guardrails, the rotation log line, and the cross-script rules. Use when planning every script and when writing its rotation log entry. Base rule file: applies to every channel unless a niche pack or persona profile explicitly overrides a specific rule.
---

# Variety rotation

**How this file relates to niche packs.** This is a base rule file. A niche pack or persona profile overrides it only where that file explicitly says so. Niche packs supply niche-specific moves, such as their adversaries and opening shapes; this file supplies the method.

Every script has spots where a model falls back on the same phrasing every time. Viewers notice the pattern even when each line is fine on its own. This file rotates two things in each of those spots:

- **The move:** the kind of line. A bridge built on stakes, then next time a bridge built on progress.
- **The line:** the actual words. Every line is freshly written in the persona's voice. Lines are never reused from a bank, and once a line is logged, it can't come back.

The example lines below show the shape of each move. They are guides, never text to copy.

---

## Guardrails

1. **Rotation isn't a quality pass.** A varied hook can still be a weak one. Every hook has to stand up against real winners in its niche (the niche pack's excerpt library) and pass the shape test in `voice-anchoring.md`. If the strongest move collides with the log, sharpen it until it's clearly distinct. Don't downgrade to a novel but flat option.
2. **Change the move, not just the wording.** Compare the new opening with the openings of the channel's last 2-3 uploads. If it opens on the same move, switch moves. Viewers hear the move, not the words.
3. **No hard bans, ever.** No line built from any move may contain a phrase from the hard ban list in `humanizer.md`. Run the scanner on every finished script.

---

## The nine slots

### 1. Opening move

The shape of the hook, judged by its first sentence: that sentence's move is the one logged. The thumbnail's scene can be named inside any move (a question, a number, a contrarian line), so matching the thumbnail never forces the same move every time. "The problem at its worst" puts the viewer inside their own problem at its most annoying moment; "the universal situation" is something everyone recognizes that isn't the problem itself.

- **The promise with a number:** "Two boards, under $15, and about 40 pieces you can sell."
- **The everyday comparison:** "This takes less time than a load of laundry."
- **The contrarian opinion:** "I don't get why people still pay for drain cleaner."
- **The universal situation:** "Every closet has the one sweater nobody wears."
- **The season or timing:** "Markets are filling up, and this is the time to build stock."
- **The cost-to-result:** "$6 of wood, $60 of shelf."
- **The problem at its worst:** "The toilet's running again at two in the morning."
- **The question the viewer is already asking:** "Will anybody actually buy this?"

### 2. Hook turn

How the setup flips into tension.

- **The plain turn:** "But…" or "Except…". Use it least, because it's the most common.
- **The question turn:** "So why does the cheap one outlast the expensive one?"
- **The double take:** "It looks done. At least, it looks done until you run a hand over it."
- **The timing turn:** "That works in July. By November, the same board has cupped."
- **The cost turn:** "Fine, until you see what the pre-cut version costs."
- **The overlooked detail:** "The part nobody mentions is the glue."

### 3. Segment bridges

Short-range only, as set out in `retention-mechanics.md`, section 6.

- **The stakes of the next item:** "That one saves a service call. The next one saves a water heater."
- **Where the progress stands:** "It's square now, but it's still rough. Sanding's next."
- **Self-recognition:** "If your edges wave like this, the next row is the fix."
- **Cost or effort:** "This next one costs nothing and takes about a minute."
- **A grounded surprise:** "The next one sounds backwards, but it's how the old shops did it."

### 4. Return after the mid-CTA

How the script gets back to the content.

- **Straight back into the action:** "Right, the second cut."
- **Where things stand:** "So, the boards are cut and the edges are sanded."
- **Picking up the open question:** "Now, about that glue line."
- **The next item's stakes:** "Number four is the one that pays for the rest."

### 5. Adversary and doubter

Which adversary the script uses (from the niche pack's list) and how the doubt gets voiced.

- **The comment-section voice:** "Somebody's typing 'nobody pays $40 for that' right now."
- **The person at the table:** "Somebody at the table will tell you it's cheaper at the big store."
- **The price-tag comparison:** "The store version's $90, and it's particleboard."
- **The objection said outright:** "Fair question: what about the cost of the bits?"

The doubter is always a general voice, never an invented specific customer or relative.

### 6. Personality lines

Opinions and honest reactions in the persona's voice. They replace stock commentary.

- **An opinion:** "I'd skip the stain on this one."
- **An honest tradeoff:** "It's slower to sand than it looks."
- **A plain reaction to a number:** "Getting $40 for that is a good day."
- **A preference with a reason:** "I like the cedar here, because it smells like a gift."

### 7. Swear words

If the niche pack allows swearing, log which words were used and rotate them. The cap and the rules come from the niche pack.

### 8. CTA wording

Log the mid-CTA's opening words and the end-CTA's wording. The wording never repeats across scripts, even though the structure stays the same. `cta-and-endings.md` and the persona profile set the structure.

### 9. Closing line

The move of the one line after the end-CTA.

- **A callback to the opening.**
- **A practical next action.**
- **The persona's sign-off,** if the persona profile has one. That's the one fixed exception.

---

## The rotation log

The mechanism doesn't change. Every script ends with one rotation log line, and the next script's intake gets the last five lines pasted in. It works across different machines and VAs because the lines travel with the brief.

**Format:** one plain-text line, no emoji.

```
ROTATION LOG ENTRY: [date] | [title] | opening: [move] "[first 6-10 words]" | turn: [move] | bridges: [moves] | return: [move] | mid-CTA: "[first 6-10 words]" | end-CTA: "[first 6-10 words]" | structure: [which] | cta variant: [which, or n/a] | adversary: [which, how voiced] | personality: [moves] | swears: [words or none] | closing: [move]
```

---

## Cross-script rules

Check against the five pasted log lines:

1. **Never reuse a combination:** the same opening move plus the same hook turn as any of the last five.
2. **Bridges:** use at least two different bridge moves per script, and swap at least one compared with the last script.
3. **Adversary, doubter voice and personality moves:** change at least one compared with the last script.
4. **No line in the log comes back,** word for word or closely paraphrased. That includes the CTA opening words.
5. **Break the habit:** if one move appears in three or more of the last five lines, pick a different move.
6. **Swear words:** rotate them, never the same word three scripts running.

If a script still feels samey after rotation, check the "use sparingly" phrases (`humanizer.md`, H23) and the echo (H18).
