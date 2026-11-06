---
name: "style-scripts"
description: "Script steps for the operator's hair-and-fashion channels for women over 60 (Scarlett Starling, Diane de Chambray): the simple way, one page per channel, one real model transcript for the video type, the title's brief, then a short hard-rules check. Use whenever a style script is written, rewritten or reviewed, or a style title and brief arrive for scripting: haircuts, gray or thinning hair, outfits, wardrobe, colors, glasses, jewelry, scarves, shoes, body shape, looking younger or expensive, frumpy, the French way. Not makeup or skincare. To write a script, type START: the script-writer skill asks for the channel and loads this pack."
---

# Style scripts (the simple way)

**Version:** 2026-11-06 DRAFT (P21: replaces the 2026-10-31 pack of about 8,000 words, its hook formula, eight-beat item, counts and full audit. Blind tests iter-08 and iter-10: one page plus one real model scored 8.0 to 8.5 against 6.3 to 7.3.)

**This pack replaces `core/workflow.md` sections 2 to 6 for Scarlett Starling and Diane de Chambray.** START and the channel question (section 1) stay as they are. None of the other core files are read for these two channels: everything the writer needs is here, on the channel's one page and in one model transcript.

## What the writer reads
1. **The channel's one page:** the `scarlett-starling-persona` or `diane-de-chambray-persona` skill's `SKILL.md`.
2. **One model transcript** for the video type (the table below), read for flow only.
3. **The title and the brief** the VA pastes.

That's all. Don't open other files to look for more rules.

## Step 1. The inputs
Ask for whatever is missing, in one message:
- **the title,** exactly as approved
- **the brief** for this title (its items, swaps and facts; usually with the book match)

Reply `NOT READY: DO NOT UPLOAD.` with the reason, and write nothing, when:
- there's no brief ("just write it" isn't enough: the brief holds the facts)
- the brief can't carry the title (too few items, no real swaps, or not enough for 12 minutes)
- the title is about makeup or skincare (that waits for its own pack)

## Step 2. The video type and the model
Pick the type that fits the title, and read its model. Where two are listed, take the first for the channel shown, or the one closer to the title. A title that fits none: use the closest type.

| Video type | What it is | Model (flow only) |
|---|---|---|
| **Mistakes that age you** | N looks that add years or look frumpy, each with the swap (whole look, one piece, or hair) | fashion: `M18-capsule-closet-stylist.md`; hair: `M04-chery.md`; Diane: `M21-marie-anne-lecoeur.md` |
| **Never these, wear these instead** | A list of pieces (glasses, jewelry, shoes, bags): each "never" paid by a "wear this" | `M13-adore-your-wardrobe.md`; Diane: `M28-aliceinparis.md` |
| **The best N** | The cuts, colors or pieces that work, each with why and for whom | hair: `M07-glam-girl-gabi.md`; fashion: `M13-adore-your-wardrobe.md` |
| **Styling it wrong: N secrets** | What she's doing at home, and the better way | hair: `M09-summer-beauty.md`; fashion: `M24-diana-goss.md` |
| **How to wear X** | One piece worn well, several ways | `M19-beth-djalali.md`; scarves and accessories: `M30-kay-harms.md` |
| **Body-shape fixes** | Line, proportion and silhouette for a body part, never weight; opens on reassurance | `M24-diana-goss.md` |
| **The rules she never breaks** | The woman who gets it right, or the French rules: each rule a habit and a swap | Diane: `M28-aliceinparis.md`, then `M21-marie-anne-lecoeur.md`; Scarlett: `M18-capsule-closet-stylist.md` |
| **The why explainer** | The hidden cause, then the fixes | hair: `M01-summer-beauty.md`; fashion: `M19-beth-djalali.md` |
| **One mistake, then N swaps** | The one mistake explained early, then each swap a full item fashion: `M13-adore-your-wardrobe.md`, then `M19-beth-djalali.md`; hair: `M04-chery.md` |

All files are in `references/models/`. Read one, not all, plus `H01-paris-never-ages-hooks.md` for the hook's beats (a competitor: the beats only, never its words).

Each model file starts with what to take, what not to take and her signature phrases. Never use those phrases or any run of her words.

## Step 3. Write it in one pass
Follow the channel's page. If the brief doesn't name the book match, find the closest Way or Secret in the book index ("The book match for style videos") and claim only that.

**Earlier scripts in this chat:** don't reuse their comment question.

## Step 4. Read it aloud, check, fix, stop
1. Read the script aloud once, as the voice will. Fix what trips the ear.
2. Run the checking program on the saved script:

   ```
   python3 check.py SCRIPT --channel scarlett|diane --title "LOCKED TITLE" --brief BRIEF
   ```

   (`check.py` is in this skill's folder. Where Python can't run, do the page's check list by eye.)
3. Fix only the lines it fails, and the page's check list. Never add a line to meet a count. Run it again until it passes.

## Step 5. The output
Both channels are Talking Head scripts on an ElevenLabs voice. Output exactly this, nothing more:

```
SCRIPT TYPE: Talking Head

[the script]

CHECK: [the program's last line] | words [n] | about [n] minutes

[the VO copy]
```

**The two book blocks** go in markers, each marker alone on its line, as `core/workflow.md` section 4 ("Talking Head") lays out:
- the mid-video book line, from its first sentence through the line back into the video
- at the end, the book reminder and the comment ask; the sign-off comes after `===END CTA===` and is the last line
- the start marker carries the printed title exactly: `===START CTA(300 Budget-Friendly Ways to Look Expensive)===` for Scarlett, `===START CTA(The French Way)===` for Diane; the end marker is always `===END CTA===`

**The script itself** is clean voiceover prose: no headings, labels, brackets, notes or emoji; straight quotes and apostrophes.

**The VO copy** follows `core/workflow.md` section 6 exactly (the same words with a few light delivery tags).

If the check can't pass, the whole output is `NOT READY: DO NOT UPLOAD.` with each reason on one line, and no script.

## Files in this skill
| File | What it is |
|---|---|
| `SKILL.md` | This page: the inputs, the steps, the model table, the output |
| `check.py` | The hard-rules check (length, the book blocks, the ending, banned lines, safety, numbers against the brief, the voice, copying from a model) |
| `references/models/` | The model transcripts, one file each, with what to take and what not to |
