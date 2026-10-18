---
name: greenlight-audit
description: The final quality gate every script passes before it ships. Six groups of checks (A hook, B retention, C clarity, D voice, E authenticity, F rules compliance), the evidence rule, the three verdicts, the three-round cap, the NOT READY rule, and the short evidence block that goes after the rotation log. Use on every finished draft, and again after every round of fixes. Base rule file: niche packs and persona profiles can add checks or change thresholds by saying so explicitly.
---

# Greenlight audit

**How this file relates to niche packs.** This is a base rule file. A niche pack or persona profile can add checks or change a threshold by saying so explicitly. Where they're silent, every check here applies.

**Why it matters.** Finished scripts go to upload without anyone reading them. This audit is the only quality check a script gets, so it has to actually run, every check, every time. Use the most capable model the account offers for the audit.

---

## How the audit runs

1. **Run all six groups, every time,** in order: A, B, C (structure), then D (voice), then E and F (policy and rules). A structural problem makes line polish pointless, so it's found first.
2. **Collect every finding before deciding the verdict.**
3. **Evidence both ways.** To fail a check, quote the exact line and name the condition it breaks. To pass, the evidence block records what was checked. If no line can be quoted against a condition, it passes.
4. **Never trust the first "clean."** After any fix, the whole audit runs again from group A. A run that applied fixes can't award its own pass.

---

## Group A: the hook

- **A1. The opening.** The viewer knows what the video is about within about 10 seconds, and the first line names the title's subject. By default the first sentence is a jolt, not a greeting, with no channel intro. A niche pack or persona profile can allow a greeting.
- **A2. Graded against real winners.** The hook holds up against 2-3 real winning hooks from the niche pack's excerpt library or voice samples. Quote the ones it was compared with. If the niche has no real hooks to compare against, mark A2 as "not run" rather than failed.
- **A3. The promise is mapped.** Every item the hook promises maps to the section of the body that delivers it.
- **A4. The hook's claims hold up.** Everything the hook claims is backed by the body, within the framing limits in `research-and-sourcing.md`.

## Group B: retention

- **B1. Every question opened gets answered,** fully, later in the script.
- **B2. The line after the hook** pays off or escalates, never background.
- **B3. Progression.** Every paragraph adds information, moves forward, raises an obstacle or shifts a feeling. One that does none is padding: cut it.
- **B4. None of the four retention mistakes:** the slow start, the context dump, a payoff with nothing after it, the broken promise.
- **B5. Bridges and pacing.** Bridges point only at the next segment, honestly, and the next segment delivers what they promise. No flat stretch runs longer than about 90 seconds without a payoff.
- **B6. "But" and "therefore"** connect the narrative and reasoning parts. Steps and list items may be sequential.
- **B7. Uneven rhythm.** No runs of same-length sentences, other than real lists and short instructions.
- **B8. List order.** The order follows the default, the niche pack's rule, or the hook's escalation promise, whichever applies.
- **B9. No retention killers:** repeated emphasis, piled-up qualifiers, announcing the obvious, throat-clearing.

## Group C: clarity

- **C1. One thread.** Any sentence traces back to the one thing the video exists to deliver.
- **C2. Easy to follow on one listen.** Plain words, and any term explained the first time it's used.
- **C3. The viewer's own words,** from the niche's vocabulary, not assumed jargon.
- **C4. The perspective shift,** only where the structure calls for one.
- **C5. The payoff is delivered exactly as promised,** and the ending doesn't recap or point back at the promise.

## Group D: voice

- **D1. The shape test.** Every sentence is tested against the niche pack's voice samples, or the persona profile's if it overrides them. Quote one matched line.
- **D2. The humanizer sweep,** H1-H23 (`humanizer.md`), including the counts for H20, H21 and H23.
- **D3. The scanner.** Run `script-scanner.py` with the niche pack and persona profile as rules files and the research pack as the pack. Hard bans, mechanical problems and niche bans must all be zero.
- **D4. Numbers trace to the research pack.** Every number appears in the pack, or is worked out from pack numbers with the math shown in the evidence block. A number the video relies on that traces to nothing is a Hold.
- **D5. Contrast and poster-quote lines.** At most one "it's not X, it's Y" reframe, and only one earned poster-quote line, if any.

## Group E: authenticity

YouTube judges channels on whether content is mass-produced or reused. This group checks the script against that.

- **E1. Originality signals:** score out of 7, passing at 5 or more, counting only signals with evidence.
  1. Research beyond the first page of results: the pack has sources most videos don't use.
  2. An angle different from the top videos on the topic.
  3. Editorial voice: opinions and reactions, not just reported facts.
  4. At least three specific, named sources.
  5. A connection between facts that isn't obvious.
  6. A structure different from the reference video and the channel's recent uploads (the rotation log).
  7. Persona-specific material: the channel's voice, opinions and canon, not generic narration.
- **E2. Red flags, which must be zero:**
  - template scripting (only the topic name changes)
  - the same script going out on more than one channel
  - lines copied word for word from a competitor transcript or the excerpt library
- **E3. Not a clone.** Where the title or structure mirrors a reference video, the angle, the voice and the sourcing all differ from it.
- **E4. Custom elements.** The video carries at least one element beyond generated footage, such as real listing screenshots, a custom thumbnail, or edits.

## Group F: rules compliance

- **F1. Structure.** The niche pack's structure is followed, or the fallback in `script-structures.md`: fixed parts present, flexible choices recorded.
- **F2. Length came from the content,** with no padding and no squeezing.
- **F3. CTAs and the ending** follow `cta-and-endings.md` and the persona profile:
  - placed after the first payoff
  - what the offer is, the added-value promise, and where to get it
  - the CTA or nothing, then stop
  - no named future video
- **F4. Offer rules** (`offer-rules.md`).
- **F5. The claims policy** (`claims-policy.md`). No checkable life facts, no invented sales, customers, family or history, and personal details only from the persona profile's list.
- **F6. Facts versus framing** stay within the limits in `research-and-sourcing.md`.
- **F7. Nothing pointed at without being named.** The visuals are built from the narration, so the script never points at something it doesn't name ("look at this," "right here").
- **F8. The niche's safety lines and bans** are present and respected.
- **F9. Rotation.** The script differs from the pasted rotation log, per the cross-script rules (`variety-rotation.md`).
- **F10. Format,** per `workflow.md`, sections 4 and 5.

---

## The three verdicts

- **PASS:** a full run with no findings.
- **FIX-THEN-PASS:** local problems that can be listed. Number them, fix them, then run the entire audit again.
- **HOLD:** a problem editing can't fix. Back to research or the outline. Holds include:
  - a bait-and-switch, where the hook promises a video the body doesn't contain
  - a fabricated fact, source or event, or an untraceable number the video relies on
  - a clone of the reference video (E3 fails on angle, voice and sourcing)
  - no single thread through the script (C1 fails everywhere)
  - the same script planned for more than one channel
  - a missing research pack, or one without a "verified on" date

---

## The cap and NOT READY

- **At most three full rounds.** If the third round still isn't clean, stop.
- **NOT READY.** If the cap is reached, or any Hold is found, the output is only the NOT READY block from `workflow.md`, section 5: the line below, the reasons, and what's needed. No script is printed.

  ```
  NOT READY: DO NOT UPLOAD.
  ```

- **The upload rule:** only a script whose verdict reads PASS gets uploaded. Anything else goes back.

---

## The evidence block

Every audited script carries this short block after the rotation log. It's never part of the voiceover. Its job is to make the audit actually happen, and to allow spot-checks later.

```
AUDIT EVIDENCE
Verdict: PASS (round [n] of 3)
Promise map: [what the hook promises] -> [where each is delivered]
Numbers: [each number = its research pack line, or the math from pack numbers]
Scanner: hard bans 0 | mechanical 0 | niche bans 0 | "Most..." [n] | reframes [n] | filler over limit [n] | numbers not in pack [n, each explained]
Voice: samples used = [which]; matched line = "[a script line]"
Originality: [n]/7 (missing: [which]) | red flags 0
Rules (F): clean, or [the finding]
```
