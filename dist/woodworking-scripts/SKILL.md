---
name: "woodworking-scripts"
description: "Script steps for the operator's woodworking-for-profit channels (Hank Hardwood, Dale Oakfield's Workshop): the simple way, one page per channel, one real maker's transcript for the video type, the title's brief and research pack, then a short hard-rules check. Use whenever a woodworking script is written, rewritten or reviewed, or a woodworking research pack, build brief or \"make this project and sell it\" title arrives for scripting. To write a script, type START: the script-writer skill asks for the channel and loads this pack."
---

# Woodworking scripts (the simple way)

**Version:** 2026-11-06 (library commit b04b004) (P21: replaces the 2026-10-21 pack of about 4,100 words and about 36,000 words of references, its skeleton template, unit plan, rotation log and full audit. Blind test iter-13: one page and one real model scored 49 of 60 against the account's skills' 46.)

**This pack replaces `core/workflow.md` sections 2 to 6 for Hank Hardwood and Dale Oakfield's Workshop.** START and the channel question (section 1) stay as they are. Everything the writer needs is here, on the channel's one page and in one model transcript. The one exception is building a missing research pack (Step 1).

## What the writer reads
1. **The channel's one page:** the `hank-hardwood-persona` or `dale-oakfield-persona` skill's `SKILL.md`.
2. **One model transcript** for the video type (the table below), read for flow only.
3. **The title, the brief and the research pack** the VA pastes.

That's all. Don't open other files to look for more rules.

## Step 1. The inputs
Ask for whatever is missing, in one message:
- **the title,** exactly as approved
- **the brief** for this title
- **the research pack** (this pack still requires one): a pack with a "Verified on" date, its title matching the locked title, prices, listings and fees checked within the last 30 days, and no gap marked blocking. If the reply is "none", the chat builds it first: the research stage in `core/research-and-sourcing.md`, filled in on `references/research-pack-template.md`, with its verification pass. It saves the pack as its own file and checks it like any other. Measurements, steps and safety never need re-checking once verified.

Where the brief and the pack disagree on a figure, the pack wins: it's the checked one.

Reply `NOT READY: DO NOT UPLOAD.` with the reason, and write nothing, when:
- there's no brief, or no pack and it can't be built ("just write it" isn't enough: the pack holds the facts)
- the pack fails the check above
- the title is a list of builds: single builds only for now
- the title's number can't be reached even by generous math from the pack (offer honest versions of the title; never change it yourself)
- the build can't fill 8 minutes with real value (the fix is more research or a bigger project, never more words)

## Step 2. The video type and the model
Pick the type that fits the build, and read its model. Where two fit, take the one closer to the title.

| Video type | What it is | Model (flow only) |
|---|---|---|
| **Recipe build, no cutting** | Sawdust, wax or scraps mixed, packed or poured; a test before selling | `W01-whosthevoss-sawdust-fire-starters.md` |
| **Seasonal piece** | A holiday or season decoration from a board or two, sold before the date | `W02-bearded-viking-pumpkins.md` |
| **Many from one board** | A batch of small pieces from one or two boards; titles about paying for tools | `W03-whosthevoss-train-whistles.md` |
| **Small furniture** | A riser, step stool, stand or small bench: it holds weight | `W04-bearded-viking-step-stool.md` |
| **Better than the store's** | A bought product set against a two-by-four build that does the job | `W05-whosthevoss-storage-riser.md` |
| **No saw, no cuts** | Ready-made parts or lumber-yard cuts, hardware, a finish and a personal touch | `W06-whosthevoss-zero-cuts.md` |

All files are in `references/models/`. Read one, not all. Each starts with what to take, what not to take and the maker's signature phrases. Never use those phrases or any run of his words.

**A heritage title** (an Amish-style bench, a Japanese-style box, a "forgotten" method) takes the model for its build. The heritage lives inside the build as short asides tied to the step in hand, never as an opening. It's a modern piece in the old style, never a replica. The basic-kit way comes first, and the old tool or method follows as an option (never an unsafe one). History stays general and hedged ("the way it's usually told"): never a date, a named person or a figure unless the brief or pack gives it with its source. Old finishes only in today's safe versions (no lead pigments; lye or charring with gloves, eye protection and the maker's instructions). If the heritage version has no listings, the money uses the plain product's listings and says so, and the heritage angle is opinion only.

## Step 3. Write it in one pass
Follow the channel's page. A title that claims his own selling or tenure ("I can't keep them in stock") is delivered through the numbers; the narration never claims it. For the book match, use the brief's; if it has none, search the book index in the channel's skill for this build or technique, and cite a page only where the book really covers it.

**Earlier scripts in this chat:** don't reuse their opening move, shop detail, swear words, book benefit or the first words of a book block.

## Step 4. Read it aloud, check, fix, stop
1. Read the script aloud once, as the voice will. Fix what trips the ear.
2. Run the checking program on the saved script:

   ```
   python3 check.py SCRIPT --channel hank|dale --title "LOCKED TITLE" --brief BRIEF [--pack PACK]
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

**The book blocks** go in markers, each marker alone on its line, as `core/workflow.md` section 4 ("Talking Head") lays out. The start marker carries the printed title exactly; the end marker is always `===END CTA===`.
- **Hank, two blocks:** the mid-video block from its first sentence through the line back into the build; the end block from its first sentence through the subscribe ask. The closing line comes after `===END CTA===` and is the last line. `===START CTA(100 Ways to Make Your First $1,000 with Woodworking)===`
- **Dale, one block:** the main pitch, from its opening aside through the line back into the build. His book mentions and his ending are plain narration with no markers. `===START CTA(The Ultimate DIY Woodworking Guide: Time-Tested Techniques, Money-Saving Shop Hacks, and Real Furniture Builds from 40 Years at the Bench)===`

**The script itself** is clean voiceover prose: no headings, labels, brackets, notes or emoji; straight quotes and apostrophes.

**The VO copy** follows `core/workflow.md` section 6 exactly (the same words with a few light delivery tags, marker lines untouched).

If the check can't pass, the whole output is `NOT READY: DO NOT UPLOAD.` with each reason on one line, and no script.

## Files in this skill
| File | What it is |
|---|---|
| `SKILL.md` | This page: the inputs, the steps, the model table, the output |
| `check.py` | The hard-rules check (length, the book blocks, the ending, banned lines, safety, numbers and money against the brief or pack, the voice, copying from a model) |
| `references/models/` | Six real makers' transcripts, one file each, with what to take and what not to |
| `references/research-pack-template.md` | The research pack's layout, for building a missing pack (unchanged) |
