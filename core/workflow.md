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

**Before typing START:** open a new chat for every script, on the most capable model the account offers. The audit is only as good as the model running it, because the model that drafted the script also checks it. A fresh chat keeps prices and facts from one script out of the next.

---

## 1. START: the channel

1. If the message doesn't name the channel, reply with one question only: the numbered list of channels from `channels.md`. Accept the number or the exact name. Anything else gets the list again.
2. Load the channel's files from `channels.md`:
   - **Persona profile.** If it's missing, or marked pending, stop with the NOT READY block (section 5), giving the reason `[channel]'s persona profile isn't set up yet.` Nothing more is asked.
   - **Niche pack.** If the channel has none, use the core fallbacks: `script-structures.md`, the default research pack in `research-and-sourcing.md`, and the default inputs below.
3. **Test runs.** `START TEST` works exactly like START, except that the channel list, persona profiles and any test research packs come from `tests/fixtures/` (its `channels.md`), never from `channels.md` or `personas/`. The first line of every test output, even a one-line reply, is `TEST: DO NOT UPLOAD.` A real channel can't be picked in a test run, and a test channel can't be picked in a real one.

---

## 2. The gate: required inputs

**Which inputs are required.** Start from the core defaults:
- **title:** the locked title, exactly as approved
- **brief:** the ideation brief for that title
- **research-pack:** the verified research pack
- **rotation-log:** the channel's last five ROTATION LOG ENTRY lines, or "none" for a new channel
- **voice-samples:** 2-3 verbatim transcript excerpts of human narration from winning videos in the niche, each with its source, at least one starting at the video's opening so the hook can be graded (`greenlight-audit.md`, A2). Required only when neither the niche pack nor the persona profile has voice samples (`voice-anchoring.md`).

Then add or replace items from the niche pack's `inputs` block, then from the persona profile's `inputs` block.

**Asking.** Send one numbered message listing every missing required input, each with a single line on what a valid one looks like. Ask for nothing else:
- not tone, length, script type, voice provider or CTA. Those come from the files.
- anything a file marks as picked at random (a CTA variant, for example) is picked by the system, never asked, and recorded in the rotation log entry.

**Checking every input before anything is written:**
- **title:** present and non-empty.
- **brief:** present.
- **research-pack:**
  - has a "Verified on" date
  - its title matches the locked title
  - its live facts are within the niche's freshness window
  - no gap marked "blocking"
- **rotation-log:** up to five ROTATION LOG ENTRY lines, or "none." Fewer than five is accepted as stated (the channel has fewer scripts).
- **voice-samples** (when required): two or three excerpts from different videos, each roughly 60-90 seconds of narration, each with its source (channel, video, timestamp). If none starts at 0:00, accept them, and A2 is reported as "not run".
- **Anything from a niche pack or persona profile:** the check written in its `inputs` block (for example, "news article dated today").

**If anything is missing or fails:** reply naming only what's missing or wrong, and ask only for that. Repeat until everything passes.

**No way around it.** If asked to "just write it," "skip the research," or proceed anyway, don't. Reply with what's still needed.

**Bulk mode.** If START arrives with every input already included and all of them pass, go straight to section 3 without a single question.

**One script per chat.** Bulk work means many chats, never many scripts in one chat: facts from one research pack leak into the next script. If START arrives in a chat that has already printed a finished script, reply only: `Start a new chat for the next script.`

---

## 3. The run: no questions from here on

Run these steps in order. Never ask "shall I continue?" Never stop to check in.

1. **Load:**
   - from the persona profile: voice sample overrides, permitted personal details, CTA setup, closing line, script type, voice provider
   - from the niche pack: structure, rules, voice samples, excerpts, reference scripts (if it has them), scanner block
   - the research pack, and the voice-samples input if it was required
2. **Plan.** Fill in the niche's unit plan (or list the fallback structure's content units), including the variation choices against the rotation log (`variety-rotation.md`). Use the niche pack's reference scripts, if it has them, for structure and pacing only, never wording.
3. **Write,** following the niche pack (or the fallback structure) and every core rule.
4. **Sweep.**
   - Run the `humanizer.md` pass.
   - Run `script-scanner.py` with the niche pack and persona profile as rules files, the research pack as the pack, and the niche pack's `excerpts.md` and `reference-scripts.md` with `--refs` (the copy guard: any run of 8 or more words shared with them is fix-on-sight). Where Python isn't available, do the same checks by hand.
5. **Audit.** Run `greenlight-audit.md`, at most three rounds.
6. **Output,** in the format in section 5.

**If the run hits something it needs and doesn't have** (a missing fact, a blocking gap, an unsupportable title claim, a step the script must teach that the pack doesn't list), it stops with NOT READY and says exactly what's needed. It never fills the gap itself: not from memory, and never from the voice samples, excerpts or reference scripts, which supply voice and shape only, never facts, numbers or steps.

**Later:** once the research stage exists, a missing research pack starts the research stage automatically instead of being asked for.

---

## 4. The script format (Vidrush only)

There's one format: clean voiceover prose for the auto-edit tool.

**Never in the script:** headings, section labels, brackets, stage directions, timestamps, links or emoji. The only exception is the CTA markers in Talking Head scripts.

**Writing for the voice:**
- **Contractions,** and no em or en dashes (`humanizer.md`, H15).
- **List numbers are spoken as words** in the narration: "Number eight." Never rely on a marker to announce them.
- **Prices, years and stats are digits,** with commas in large numbers: "$4.65," "1,200," "1998." Small everyday counts can be words ("two boards").
- **Spell out anything a voice might misread,** the way it's said: measurements with fractions ("five and three-quarters inches") and degrees ("45 degrees"). Never symbols like ° or ½.
- **Introduce each named person by full name once.** After that, use the surname, a pronoun, or their role.

**Visuals come from the narration.** The video is built from the script, so anything the viewer should see is named in the narration, and the script never points at something it doesn't name ("look at this," "right here"). Outside the steps, no more than about two sentences in a row go by without naming something that can be shown (the object, the tool, the place, the listing and its price). Lines with nothing showable make the auto-edit repeat footage.

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

**Only PASS scripts are uploaded.** Any change after PASS, however small, voids it: the edited script runs the full audit again and gets a new verdict and evidence block.

---

## 6. The voiceover copy (ElevenLabs v4 voices only)

A second copy of the finished script, with light delivery tags so the voice reads it more naturally. It's produced automatically, straight after the audit evidence. Minimax voices get only the line `VO COPY: not required (Minimax voice)`.

**Identical words.** Not one word changes: nothing added, nothing removed, punctuation untouched. Tags are inserted, and that's the only change. In Talking Head scripts, every marker line is reproduced exactly, alone on its line, and never tagged.

**Tag format:** square brackets, placed right before the sentence they shape: `[thoughtful] That's the part most people skip.` No SSML. Pauses are `[short pause]` or `[long pause]`.

**A light touch:**
- About one tag per 80-120 words across the script, and never more than two in any 80 words. Never two in a row, never more than one per sentence. Most sentences get none.
- **Allowed tags only:** [warm] [thoughtful] [quietly] [matter-of-fact] [slightly amused] [sighs] [short pause] [long pause] [slower] [emphatic]
- **[slightly amused]** only on an honest-candor line, never to make a line sound like a joke.
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
