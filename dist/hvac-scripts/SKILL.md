---
name: "hvac-scripts"
description: "Script steps for the operator's HVAC channel, Roger the HVAC Guy (and any future channel in this niche): the simple way, one page for the channel, one real model transcript for the video type, the title's brief, then a short hard-rules check. Use whenever an HVAC script is written, rewritten or reviewed, or an HVAC title and brief arrive for scripting: furnaces, AC, heat pumps, filters, thermostats, condensate drains, drafts, the heating and cooling bill, space heaters, outage heat. To write a script, type START: the script-writer skill asks for the channel and loads this pack."
---

# HVAC scripts (the simple way)

**Version:** 2026-11-06 (library commit b04b004) (P21: replaces the account's pack of about 11,200 words, its excerpts, voice samples, plan template, 31 model beat maps, counts and full audit. Blind test iter-12: one page plus one real model 46 of 60, the account pack 44.)

**This pack replaces `core/workflow.md` sections 2 to 6 for Roger the HVAC Guy.** START and the channel question (section 1) stay as they are. None of the other core files are read for this channel: everything the writer needs is here, on the channel's one page and in one model transcript.

## What the writer reads
1. **The channel's one page:** the `roger-the-hvac-guy-persona` skill's `SKILL.md`.
2. **One model transcript** for the video type (the table below), read for flow only.
3. **The title and the brief** the VA pastes.
4. **The price guide** (`references/price-guide.md`), only for a price or safety fact the brief doesn't give.

That's all. Don't open other files to look for more rules.

## Step 1. The inputs
Ask for whatever is missing, in one message:
- **the title,** exactly as approved
- **the brief** for this title (its talking points, facts, prices and limits)

Reply `NOT READY: DO NOT UPLOAD.` with the reason, and write nothing, when:
- there's no brief ("just write it" isn't enough: the brief holds the facts)
- the brief can't carry the title's main promise, or can't fill 12 minutes even with everyday HVAC know-how (then ask for a fuller brief)
- the title is a brand verdict ("The Only N Furnace Brands Worth Buying"): its rules wait for the operator

A price in neither the brief nor the price guide is said in words ("a few hundred dollars") or left out; that alone is no reason to stop.

## Step 2. The video type and the model
Pick the type that fits the title, and read its model. Where two are listed, take the one closer to the title. A title that fits none: use the closest type.

| Video type | What it is | Model (flow only) |
|---|---|---|
| **Single-product fix** | One cheap thing that fixes or prevents one problem: "1 Cup of This...", "Pour X Into Y Tonight" | `R35-silver-cymbal-unclog-ac-drain.md` |
| **N things about one product** | "N Things HVAC Techs Don't Want You to Know About X" | `R34-the-diy-hvac-guy-3-things-contractors.md` |
| **Mistakes or habits list, never-do list** | "N Furnace Mistakes...", "NEVER Plug Your Space Heater Into These..." | `R25-hvac-guide-for-homeowners-winter-mistakes.md` |
| **How-to, the correct way** | A job told as steps in the order the hands do it | `R23-everyday-home-repairs-yearly-furnace-maintenance.md` |
| **Hidden cause or symptom** | "Furnace Keeps Shutting Off?": what normal looks and sounds like, the cause, the check, when it's a call | `R27-everyday-home-repairs-furnace-wont-turn-on.md`; one quick fix: `R28-word-of-advice-tv-furnace-most-common-fix.md` |
| **Seasonal or emergency** | "Do These N Things Before the First Cold Snap", the outage | `R22-the-diy-hvac-guy-before-heat-this-fall.md` |
| **Product swap, the heating bill** | The dear option against the cheap one, judged fairly | `R42-home-renovision-diy-rim-joist-heat-bill.md` |
| **Head-to-head or ranked verdict** | "X vs Y vs Z": each one's job, then which for which house | `R42-home-renovision-diy-rim-joist-heat-bill.md` (the closest on disk: good, better, best, then the verdict) |
| **Banned or rule explainer** | "Why They Keep Banning Your Refrigerant" | none yet: the closest type's model |

All files are in `references/models/`. Read one, not all. Every model is a real person on camera (operator, 2026-10-27: "we dont want any ai or faceless for reference").

Each model file starts with what to take, what not to take and his signature phrases. Never use those phrases or any run of his words. A title that promises tests ("I Tested 5 Filters") is written as tests and results from the brief, never as "I tested".

## Step 3. Write it in one pass
Follow the channel's page. The brief wins on facts and on safety. Where the brief is silent, fill in only with everyday HVAC know-how (a setting, how often to check, what a mistake leads to) and with the price guide; never a chemical, electrical or gas method beyond the brief and the page's safety defaults.

**Earlier scripts in this chat:** don't reuse their comment question or their opening shape.

## Step 4. Read it aloud, check, fix, stop
1. Read the script aloud once, as the voice will. Fix what trips the ear, and any step a listener couldn't do from the audio alone.
2. Run the checking program on the saved script:

   ```
   python3 check.py SCRIPT --title "LOCKED TITLE" --brief BRIEF
   ```

   (`check.py` is in this skill's folder; it reads the models and the price guide from `references/`. Where Python can't run, do the page's check list by eye.)
3. Fix only the lines it fails, and the page's check list. Never add a line to meet a count. Run it again until it passes.

## Step 5. The output
Roger the HVAC Guy is a **Classic** script on an ElevenLabs voice: no CTA markers anywhere; the subscribe line and the comment ask are plain narration. Output exactly this, nothing more:

```
SCRIPT TYPE: Classic

[the script]

CHECK: [the program's last line] | words [n] | about [n] minutes at 150 words a minute

[the VO copy]
```

**The script itself** is clean voiceover prose in paragraphs: no headings, labels, brackets, notes or emoji; straight quotes and apostrophes.

**The VO copy** follows `core/workflow.md` section 6 exactly (the same words with a few light delivery tags, headed `VO COPY — ELEVENLABS V4`), as the account's run did in iter-12.

If the check can't pass, the whole output is `NOT READY: DO NOT UPLOAD.` with each reason on one line, and no script.

## Files in this skill
| File | What it is |
|---|---|
| `SKILL.md` | This page: the inputs, the steps, the model table, the output |
| `check.py` | The hard-rules check (length, the ending, banned lines, the safety requirements, prices against the brief and the price guide, the voice, long sentences, lists in the opening, copying from a model) |
| `references/models/` | Eight real on-camera transcripts, one file each, with what to take and what not to |
| `references/price-guide.md` | Typical US prices and the safety facts (section 9: the carbon monoxide and gas-leak steps), unchanged from the account's pack |
