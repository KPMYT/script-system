---
name: "plumbing-scripts"
description: "Script steps for the operator's plumbing channels (Roger the Pipe Guy, Mark Silverbridge, The Vintage Pipefitter, Werner Finkbeiner): the simple way, one page per channel, one real tradesman's transcript for the video type, the title's brief, then a short hard-rules check. Use whenever a plumbing script is written, rewritten or reviewed, or a plumbing title and brief arrive for scripting: drains, clogs, toilets, faucets, stoppers, water heaters, leaks, pipes, the main line, drain powders and cleaners. To write a script, type START: the script-writer skill asks for the channel and loads this pack."
---

# Plumbing scripts (the simple way)

**Version:** 2026-11-06 DRAFT (P21: replaces the 2026-10-29 pack of about 11,400 words, its excerpts, voice samples, unit plan, 39 model beat maps, counts and full audit. Blind test iter-09: one page plus one real model scored 8.0 against 6.2.)

**This pack replaces `core/workflow.md` sections 2 to 6 for the four plumbing channels.** START and the channel question (section 1) stay as they are. None of the other core files are read for these channels: everything the writer needs is here, on the channel's one page and in one model transcript.

## What the writer reads
1. **The channel's one page:** the channel's persona skill `SKILL.md` (`roger-the-pipe-guy-persona`, `mark-silverbridge-persona`, `vintage-pipefitter-persona` or `werner-finkbeiner-persona`).
2. **One model transcript** for the video type (the table below), read for flow only.
3. **The title and the brief** the VA pastes.
4. **Only for a price the brief doesn't give:** `references/price-guide.md`.

That's all. Don't open other files to look for more rules.

## Step 1. The inputs
Ask for whatever is missing, in one message:
- **the title,** exactly as approved
- **the brief** for this title (talking points are enough; the book match where the channel has a book)

A brief of talking points is a full brief: build each point out with the scene in the viewer's house, what's happening in the pipe, the fix, the sign it's a call, and the win.

Reply `NOT READY: DO NOT UPLOAD.` with the reason, and write nothing, when:
- there's no brief ("just write it" isn't enough: the brief holds the facts)
- the brief can't carry the title's main promise, or can't reach 12 minutes even with every point built out (ask for more points; never pad)

A price the script needs that is in neither the brief nor the price guide is said in words ("a service call", "a few hundred dollars"), never guessed. That alone is never a reason to stop.

## Step 2. The video type and the model
Pick the type that fits the title, and read its model. Where two are listed, take the first, or the one closer to the title. A title that fits none: use the closest type.

| Video type | Title shape | Model (flow only) |
|---|---|---|
| **How-to, the correct way** | "How to X for Beginners", "The CORRECT Way to X" | `R13-roger-wakefield-flush-water-heater.md`; the "correct way" or a trade skill: `R14-roger-wakefield-solder-like-a-pro.md` |
| **Single-product fix** | "1 Cup of This...", "Pour X Into Y Tonight" | `R15-silver-cymbal-windshield-inside-clean.md` |
| **N things about one product** | "N Things Plumbers Don't Want You to Know About X" | `R16-silver-cymbal-string-trimmer-hacks.md` |
| **Never-do list** | "N Things You Should NEVER..." | `R16-silver-cymbal-string-trimmer-hacks.md` |
| **Mistakes list** | "N Mistakes That...", "DO NOT Install X Until..." | `R16-silver-cymbal-string-trimmer-hacks.md`, then `R14-roger-wakefield-solder-like-a-pro.md` |
| **Head-to-head verdict** | "X vs Y vs Z" | `R04-roger-wakefield-tank-vs-tankless.md` |
| **Product swap** | "X Is Expensive. Use THIS Instead!" | `R18-silver-cymbal-compression-valves.md` |
| **Hidden cause** | "Why Your X Keeps Y" | `R06-silver-cymbal-led-bulbs-enclosed-fixtures.md` |
| **Banned or code explainer** | "Here's Why X Is NOT ALLOWED Anymore" | `R06-silver-cymbal-led-bulbs-enclosed-fixtures.md` (the why carries the video) |
| **Seasonal or emergency** | "Do This Before the First Freeze" | `R13-roger-wakefield-flush-water-heater.md` (the honest limit first, then the job in its order) |

All files are in `references/models/`. They are real tradesmen and homeowners on camera, and several run shorter than our scripts: copy how they move, never their length. Read one, not all.

Each model file starts with what to take, what not to take and his signature phrases. Never use those phrases or any run of his words.

## Step 3. Write it in one pass
Follow the channel's page. The brief wins on facts. Where it's silent, use only everyday plumbing sense and the price guide, never an invented dose, price or claim. If the brief doesn't name the book match, find the closest fix or chapter in the book's index and claim only that.

**Earlier scripts in this chat:** don't reuse their comment question or their opening line.

## Step 4. Read it aloud, check, fix, stop
1. Read the script aloud once, as the voice will. Fix what trips the ear.
2. Run the checking program on the saved script:

   ```
   python3 check.py SCRIPT --channel roger|mark|vintage|werner --title "LOCKED TITLE" --brief BRIEF
   ```

   (`check.py` is in this skill's folder. Where Python can't run, do the page's check list by eye.)
3. Fix only the lines it fails, and the page's check list. Never add a line to meet a count. Run it again until it passes.

## Step 5. The output
All four voices are ElevenLabs. Output exactly this, nothing more:

```
SCRIPT TYPE: Classic (Roger, Mark, the Vintage Pipefitter) | Talking Head (Werner)

[the script]

CHECK: [the program's last line] | words [n] | about [n] minutes

[the VO copy]
```

**Classic (Roger, Mark, the Vintage Pipefitter):** the book line and the end are written inline as ordinary narration. No markers anywhere.

**Talking Head (Werner):** the two book blocks go in markers, each marker alone on its line, as `core/workflow.md` section 4 lays out:
- the mid-video book line, from its first sentence through the line back into the video
- at the end, the one-line book reminder; the comment ask comes after `===END CTA===` and is the last line
- the start marker is exactly `===START CTA(Werner's 101 Free Repairs)===`; the end marker is always `===END CTA===`

**The script itself** is clean voiceover prose: no headings, labels, brackets, edit notes or emoji; straight quotes and apostrophes.

**The VO copy** follows `core/workflow.md` section 6 exactly (the same words with a few light delivery tags; marker lines copied untouched).

If the check can't pass, the whole output is `NOT READY: DO NOT UPLOAD.` with each reason on one line, and no script.

## Files in this skill
| File | What it is |
|---|---|
| `SKILL.md` | This page: the inputs, the steps, the model table, the output |
| `check.py` | The hard-rules check (length at the channel's speed, the CTA and the ending, banned lines, safety, prices against the brief and the price guide, the voice, copying from a model) |
| `references/models/` | Seven real on-camera transcripts, one file each, with what to take and what not to |
| `references/price-guide.md` | Typical US prices, researched 2026-10-21, for any price the brief doesn't give |
