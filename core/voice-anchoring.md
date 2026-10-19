---
name: voice-anchoring
description: How every script gets anchored to real spoken narration instead of the model's default written-cinematic voice. Covers where voice samples come from, the per-sentence shape test, the four written-not-spoken tells, and how to fix a line without weakening it. Use before writing any script, during the audit, and whenever a draft reads polished but robotic. Base rule file: applies to every channel unless a niche pack or persona profile explicitly overrides a specific rule.
---

# Voice anchoring

**How this file relates to niche packs.** This is a base rule file. It defines the method. The voice samples themselves live in each niche pack, because a niche's viewers share one way of being spoken to. A niche pack or persona profile overrides this file only where it explicitly says so.

Ask a model for good YouTube copy and it writes good *writing*: dramatic parallels, clever paired sentences, poetic fragments. None of it is banned vocabulary, so it slips past every slop check, and it still sounds robotic the moment a narrator reads it aloud. The reliable fix is to anchor every script to real spoken narration before writing a line, then test every sentence against it.

---

## Where the voice samples come from

**What a sample is:** 60-90 seconds of narration, copied verbatim from a transcript, never written from memory.

**How many:** two or three, from different winning videos. One clip only holds a handful of sentence shapes, so the test ends up rejecting normal speech that just didn't happen to appear in it.

**Where they're stored:**
- **The niche pack holds the samples** for its lane, with each source noted (channel, video, timestamp).
- **A persona profile can add or replace one** when that persona speaks differently from the rest of the lane, for example a German-precision presenter in a plain-spoken niche.
- **The niche pack's excerpt library**, if it has one, gives the test a wider range of shapes to check against.

**Source order:**
1. **Human narration from winners in the niche.** Use 2-3 videos well above their channel's normal, from different channels, and anchor to the shapes they share. You're learning how the lane talks, not copying one creator.
2. **Your own uploads,** but only if a human wrote and narrated them. Scripts that were AI-written are never a voice sample: anchoring to them anchors the voice to exactly the robotic writing this file exists to escape. They're useful only for checking a channel's established habits, such as its sign-off.

**No samples, no script.** If a channel has no niche pack yet and no samples in its persona profile, the workflow's gate requires the `voice-samples` input (2-3 transcripts, `workflow.md` section 2) before anything is written. An imagined "good YouTube voice" doesn't exist. Imagining one produces the written-cinematic default every time.

**Rules for samples:**
- **Voice, never content.** A sample teaches how sentences are built: how the narrator counts things off, moves between points, and where they breathe. It never supplies hooks, structure, angles, claims or topics. Borrowing content is cloning.
- **Keep it raw.** Keep the hand-offs, the self-corrections and the natural filler. A cleaned-up sample teaches nothing about shape. Only fix obvious transcription errors.
- **Skip bad habits.** A sample's "hey guys, welcome back" is a habit to write past, not a shape to copy.
- **First-person claims stay with their owner.** If the sample's narrator says "I sold these at a craft fair," that's their life, not the persona's. Borrow how the sentence sounds, and apply the channel's claims rules to what it says.
- **Match the language.** Samples are in the language the channel publishes in.
- **The persona profile wins on the persona.** Where the profile's "How they talk" lines and the samples disagree (sentence length, register), the profile decides for this channel. The samples still decide the lane's natural shapes: how steps are handed over, how numbers are said.

---

## The shape test

Ask this of every sentence of spoken copy: **"Does the narration in the samples ever build a sentence like this?"** Measure against the actual samples, never against "narrators in general." Plenty of documentary narrators produce exactly the shapes this test exists to catch.

Judge the shape, not the quality. A line that reads beautifully can still fail; reading well is how bad lines survive every other check. Sentence length proves nothing in either direction.

**Shapes that pass, because people talk this way:**
- **Lists that count real things:** "Flour, salt, water. That's all the dough needs."
- **Instructions:** "Flip it over and do the other side."
- **Self-corrections:** "It took ten minutes. Fifteen, if the glue's cold."
- **Describing what's on screen** ("now look at the top edge"): real speech, but avoid it by default. The video is built from the script, so the edit can only show what the narration names. Use it only when the same or the next sentence names exactly what's being shown, and any niche pack may ban it outright.

**Shapes that fail, because they're writing:**
- **Dramatic parallels:** mirrored beats built for the page.
- **Paired one-liners:** two polished sentences that define each other.
- **Poetic compression:** a line squeezed until it sounds literary rather than sayable.

If a shape appears nowhere in the samples, rewrite it into one that does.

---

## The four written-not-spoken tells

These four survive slop filters because nothing in them is banned vocabulary. Every example below is the failure.

### 1. Movie Trailer

Escalating dramatic beats, cut like a teaser. The tell is grand, high-stakes framing.

```
"One drip. Then a puddle. Then a ceiling on the kitchen floor."
```

### 2. Wise Narrator

Essay-style verdicts: short sentences that pronounce a general truth. The tell is the pronouncement.

```
"Old houses don't lie. They just wait."
```

### 3. Staccato-Robotic

Fragments in a drumbeat that don't count real things. The tell is rhythm for its own sake.

```
"No glue. No nails. No excuses."
```

Compare it with a real list. "Flour, salt, water" counts three things you could put on screen; the line above counts nothing.

### 4. Reading-Not-Speaking

Clever written pairs, second-person prophecy, and grammar no mouth produces live. The tell is page-grammar.

```
"Comfort is the deposit. Style is the interest."
"You'll never look at your closet the same way again."
```

Try saying either one into a microphone as your own sentence without feeling like you're reciting.

---

## Fixing a line

The fix is translating the delivery, never deleting the line. Three things survive every fix:
- **The jolt:** whatever grabs attention.
- **The proof:** the number or the specific detail.
- **The tension:** the open question the line plants.

Only the delivery changes. The samples govern how a sentence is built, never what it says.

**Worked example** (the Movie Trailer line above):

```
Original:   "One drip. Then a puddle. Then a ceiling on the kitchen floor."
De-clawed:  "Over time, small leaks can sometimes cause water damage."
Translated: "That drip under the sink looks like nothing, and that's the problem. Leave it a few weeks and it soaks into the floor, and then you're paying for a ceiling instead of a washer."
```

The de-clawed version fixes the voice and kills the line: the stakes and the pull are gone. If a fix makes the line weaker, the fix is wrong, so translate again. The translated version keeps the escalation and the stakes, in shapes a person actually says.

The rule cuts both ways:
- A strong line in trailer voice fails.
- An easy-to-say line that lost the video's best tension also fails.
- Never downgrade the strongest angle because the spoken version is harder to write. Keep translating until it's strong *and* sayable.

---

## Smaller rules

- **Contractions from the first draft:** it's, don't, you're, that's. Uncontracted forms are written English, and fixing them later means redrafting, not polishing.
- **Filler follows the samples.** Natural words like "look," "honestly" or "now" appear at the density the samples show. The same filler pasted into every script becomes its own robotic tic.
- **Persona habits come from the persona profile,** within the humanizer's ban rules and capped so they don't repeat into a tic.
- **Run the test twice.** Anchor before writing, then shape-test the finished draft sentence by sentence during the audit. Hold hooks to the hardest standard, because "viral on paper" is exactly where trailer voice sneaks back in.
