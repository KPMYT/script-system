---
name: workflow
description: The entry point for writing any script on the operator's channels. Runs whenever the user types START, alone or followed by inputs. It asks for the channel, then for exactly the inputs that channel requires, refuses to continue until every input is present and valid, then runs straight through to the finished script with no further questions. Defines the one script format (Vidrush voiceover prose, Talking Head markers or Classic), the output skeleton, and the ElevenLabs voiceover copy. Use for every script request, including "START", "new script", or a pasted brief.
---

# Script workflow

This is the entry point. When someone types **START**, this file runs, and nothing else happens first. It reads:
- `channels.md`, to find the channel
- the channel's persona profile and niche pack
- every other core file, as each step needs it

**How the files relate:**
- A niche pack or persona profile overrides the core base files wherever it says so explicitly.
- `claims-policy.md` and `offer-rules.md` sit above everything. Packs and profiles can tighten them, never loosen them.

---

## 1. START: the channel

1. If the message doesn't name the channel, reply with one question only: the numbered list of channels from `channels.md`. Accept the number or the exact name. Anything else gets the list again.
2. Load the channel's files from `channels.md`:
   - **Persona profile.** If it's missing, or marked pending, stop: `NOT READY: [channel]'s persona profile isn't set up yet.` Nothing more is asked.
   - **Niche pack.** If the channel has none, use the core fallbacks: `script-structures.md`, the default research pack in `research-and-sourcing.md`, and the default inputs below.

---

## 2. The gate: required inputs

**Which inputs are required.** Start from the core defaults:
- **title:** the locked title, exactly as approved
- **brief:** the ideation brief for that title
- **research-pack:** the verified research pack, or "none" (the chat then builds it; see below). A niche pack may mark it `not used`: then it is never asked for or built, and the brief is the fact source.
- **rotation-log:** the channel's last five ROTATION LOG ENTRY lines, or "none" for a new channel

Then add, replace or drop items from the niche pack's `inputs` block, then from the persona profile's `inputs` block. An item marked `not used` isn't asked for or checked.

**The fact source** is the research pack, or the brief where the niche pack marks the research pack `not used`. Every fact, price and number in the script comes from it, and the steps below that name the pack use the brief instead.

**Asking.** Send one numbered message listing every missing required input, each with a single line on what a valid one looks like. Ask for nothing else:
- not tone, length, script type, voice provider or CTA. Those come from the files.
- anything a file marks as picked at random (a CTA variant, for example) is picked by the system, never asked, and recorded in the rotation log entry.

**Checking every input before anything is written:**
- **title:** present and non-empty.
- **brief:** present.
- **research-pack** (unless the niche pack marks it `not used`):
  - has a "Verified on" date
  - its title matches the locked title
  - its live facts are within the niche's freshness window
  - no gap marked "blocking"
- **rotation-log:** up to five ROTATION LOG ENTRY lines (fewer only if the channel has fewer scripts), or "none."
- **Anything from a niche pack or persona profile:** the check written in its `inputs` block (for example, "news article dated today").

**If anything is missing or fails:** reply naming only what's missing or wrong, and ask only for that. Repeat until everything passes.

**No research pack.** In a niche that uses one (never where the niche pack marks it `not used`), if the reply is "none" (or the pack is missing and the operator says there isn't one), the chat builds it, by running the research stage (`research-and-sourcing.md` and the niche pack's research pack template), including the verification pass. It saves the pack as its own file, then checks it at this gate like any other pack. If the research finds a title claim it can't support, it stops with NOT READY, names the claim, and offers honest versions of the title for the operator to re-lock; it never changes the title itself. (Operator, 2026-10-20.)

**No way around it.** If asked to "just write it," "skip the research," or proceed anyway, don't. Reply with what's still needed. Building the pack is allowed; writing without one never is (in a niche that uses one).

**Bulk mode.** If START arrives with every input already included and all of them pass, go straight to section 3 without a single question.

---

## 3. The run: no questions from here on

Run these steps in order. Never ask "shall I continue?" Never stop to check in.

1. **Load:**
   - from the persona profile: voice sample overrides, permitted personal details, CTA setup, closing line, script type, voice provider
   - from the niche pack: structure, rules, voice samples, excerpts, scanner block
   - the fact source (the research pack, or the brief where the niche pack doesn't use one)
2. **Plan.** Fill in the niche's unit plan (or list the fallback structure's content units), including the variation choices against the rotation log (`variety-rotation.md`).
   - **The book match.** If the persona profile names a book text, search it for the video's topic (the build, the technique, the problem) and record each relevant page range with one line on what's there, or "nothing relevant." CTAs and book mentions may cite only these pages (`cta-and-endings.md`, section 3).
   - **The 8-minute minimum.** Every script runs at least 8 minutes of narration, counted at the persona profile's words per minute, or 150 if it sets none (so at least 1,200 spoken words at 150). Above that, length comes from the content: every line must add value, and longer is fine. If the plan can't reach 8 minutes with real value, never pad: stop with NOT READY and ask for more research or a bigger angle. A niche pack may raise the minimum (the plumbing pack sets 12 minutes) and add guidance on length.
3. **Write,** following the niche pack (or the fallback structure) and every core rule. **The quality bar** (operator, 2026-10-20): the script follows the core unless the niche pack overrides it (the pack always wins), is tailored to the audience's emotions, gives real value, opens on a strong hook that plays on their pain points, is solution-driven, and is easy to follow on one listen.
4. **Sweep.**
   - Run the `humanizer.md` pass.
   - Run `script-scanner.py` with the niche pack and persona profile as rules files, the fact source as the pack, the locked title with `--title` (a years figure in it is allowed: title numbers win), and the niche pack's copy-guard files (woodworking: `excerpts.md` and `reference-scripts.md`; a pack may name others, as plumbing does) plus the persona profile with `--refs` (the copy guard: any run of 8 or more words shared with them is fix-on-sight, except lines the profile's scanner block marks `allow:`, such as a fixed sign-off). Where Python isn't available, do the same checks by hand.
5. **Audit.** Run `greenlight-audit.md`, at most three rounds.
6. **Output,** in the format in section 5.

**If the run hits something it needs and doesn't have** (a missing fact, a blocking gap, an unsupportable title claim), it stops with NOT READY and says exactly what's needed. It never fills the gap itself.

**A pack built in this chat** follows section 2: it's built, verified and checked at the gate before the run starts.

---

## 4. The script format (Vidrush only)

There's one format: clean voiceover prose for the auto-edit tool.

**Never in the script:** headings, section labels, brackets, stage directions, timestamps, links or emoji. The only exception is the CTA markers in Talking Head scripts.

**Writing for the voice:**
- **Contractions,** and no em or en dashes (`humanizer.md`, H15).
- **List numbers are spoken as words** in the narration: "Number eight." Never rely on a marker to announce them.
- **Prices, years and stats are digits,** with commas in large numbers: "$15," "1,200," "1998." Small everyday counts can be words ("two boards").
- **Few numbers, easy to follow:** always rounded the way people talk ("about four bucks," "around $40"), never cents; one price per item; never a fee schedule or every listing read aloud (`humanizer.md`, H22).
- **Spell out anything a voice might misread,** the way it's said: measurements with fractions ("five and three-quarters inches") and degrees ("45 degrees"). Never symbols like ° or ½.
- **Introduce each named person by full name once.** After that, use the surname, a pronoun, or their role.

**Visuals come from the narration.** The video is built from the script, so anything the viewer should see is named in the narration, and the script never points at something it doesn't name ("look at this," "right here").

**The two script types.** The persona profile sets which one a channel uses.

*Classic:* CTAs written inline as normal narration. No markers anywhere.

*Talking Head:* each CTA is wrapped in markers, laid out exactly like this:

```
[the line before the CTA]

===START CTA(Exact Printed Offer Title)===
[the CTA text]
===END CTA===

[the line after the CTA]
```

**Marker rules:**
- Each marker sits alone on its own line, with nothing before or after it on that line.
- The CTA text starts on the line directly under the start marker. The end marker goes on the line directly after the CTA's last sentence.
- **The start marker** carries the offer's printed title, copied character for character from the persona profile: digits, symbols and capitals exactly as printed. Inside the spoken CTA, the title is written the way it should be said.
- **No offer:** the end CTA's start marker reads `===START CTA(NO BOOK)===`.
- **The end marker** is always exactly `===END CTA===`.
- **What goes inside:**
  - Mid-video CTA: from its first sentence through the return line back into the content.
  - End CTA: from its first sentence through its ask.
- **How many blocks:** one per CTA the persona profile switches on. Usually two, mid and end.
- **No formatting or cleaning rule anywhere ever touches a marker line.** Everything between markers stays clean voiceover prose.

**The ending,** per `cta-and-endings.md`:
- After the final payoff: the end CTA, if the channel has one, then the closing line, then nothing.
- **The closing line is exactly one sentence,** under about 15 words, and it's the last line of the script:
  - the persona's signature sign-off, if the profile has one (its final sentence only, if the sign-off runs longer)
  - otherwise, a callback or a practical next action
- It never promises a specific future video.

---

## 5. The output skeleton

Every output follows this order, with nothing missing and nothing added:

```
SCRIPT TYPE: [Talking Head | Classic]

[the script]

VERDICT: PASS
FORMAT CHECK: [type] | [markers: n blocks, each alone on its line, titles exact | none] | [end CTA directly after the final content] | [one closing line, last line of the script] | PASS
ROTATION LOG ENTRY: [per variety-rotation.md]
AUDIT EVIDENCE
[per greenlight-audit.md]
[the VO copy per section 6, or the line: VO COPY: not required (Minimax voice)]
```

**When it isn't ready.** If the gate, the run or the audit ends in NOT READY, the whole output is:

```
NOT READY: DO NOT UPLOAD.
[each reason, one line]
[exactly what's needed to fix it]
```

No script is printed when the output is NOT READY, so a failed script can't be uploaded by mistake.

**If the output runs out of room,** continue in the next message, unprompted, until the skeleton is complete.

**Only PASS scripts are uploaded.**

---

## 6. The voiceover copy (ElevenLabs v4 voices only)

A second copy of the finished script, with light delivery tags so the voice reads it more naturally. It's produced automatically, straight after the audit evidence. Minimax voices get only the line `VO COPY: not required (Minimax voice)`.

**Identical words.** Not one word changes: nothing added, nothing removed, punctuation untouched. Tags are inserted, and that's the only change. In Talking Head scripts, every marker line is reproduced exactly, alone on its line, and never tagged.

**Tag format:** square brackets, placed right before the sentence they shape: `[thoughtful] That's the part most people skip.` No SSML. Pauses are `[short pause]` or `[long pause]`.

**A light touch:**
- About one tag per 80-120 words. Never two in a row, never more than one per sentence. Most sentences get none.
- **Allowed tags only:** [warm] [thoughtful] [quietly] [matter-of-fact] [slightly amused] [chuckles] [sighs] [short pause] [long pause] [slower] [emphatic]
- **Never:** sound effects, accents, whispering, shouting, or anything that reads as a sound cue rather than a way of speaking.
- **Pauses** only where a natural beat belongs: after a key reveal, before the mid-video CTA, before the closing line. Never next to an existing "...".
- **CTA sections** stay warm and even: at most one [warm] at the start of each, nothing else inside.

**Layout:**

```
VO COPY — ELEVENLABS V4
[the full script with tags inserted, markers intact]
```

Nothing comes after it.

**Check before delivering:**
- Strip every tag: the result must match the script word for word, marker lines included.
- The tag count is within the density rule, no two tags are adjacent, and no marker line is tagged.
