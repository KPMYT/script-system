# Script System: what's in each file

The whole system is one library. `core/` holds the rules every channel uses. Each niche gets its own pack (so far, `woodworking-scripts/`). Each channel gets a persona profile in `personas/`. Typing **START** runs `core/workflow.md`, which pulls in everything else.

## core/ (every channel)

| File | What's in it |
|---|---|
| `workflow.md` | **The entry point.** START, picking the channel, the input gate (refuses to write until every input is valid), the run with no questions, the Vidrush script format and Talking Head markers, the output layout, the ElevenLabs voiceover copy, and the NOT READY rule. |
| `channels.md` | The channel list START shows, with each channel's niche pack, persona profile and status. |
| `persona-profile-template.md` | The blank template for each channel's settings: persona, script type, voice provider, CTA setup and offers. |
| `claims-policy.md` | What a persona may and may not claim: opinions yes, checkable life facts no; no health claims, guarantees, or false facts about named companies. |
| `offer-rules.md` | How any offer (e-book, email list, affiliate, subscribe) may be talked about: facts only from the profile, an added-value promise, price-silent paid products. |
| `cta-and-endings.md` | CTA mechanics (placement after the first payoff, what every CTA contains) and how videos end: the CTA or nothing, then one closing line. |
| `humanizer.md` | The 23 "AI tells" (H1-H23), the hard-ban list (including retention teases), the "use sparingly" phrases, and the clean-up procedure. |
| `voice-anchoring.md` | How scripts are matched to real human narration, the sentence-by-sentence shape test, and the four written-not-spoken tells. |
| `retention-mechanics.md` | Holding attention: the first seconds, the line after the hook, the progression test, short rehooks, list order and pacing guides. |
| `variety-rotation.md` | Keeps scripts from sounding alike: nine rotating slots (move and wording), the rotation log line, and the cross-script rules. |
| `research-and-sourcing.md` | The research stage's rules: facts versus allowed framing, verify-or-cut, evidence wording, freshness, the verification pass, the default research pack, and flagging titles back to ideation. |
| `script-structures.md` | Fallback structures for niches without their own: list, how-to, why it happens, comparison, essay, transformation. Plus the hook options. |
| `greenlight-audit.md` | The final quality gate: checks A-F, three verdicts, the three-round cap, and the evidence block. |
| `script-scanner.py` | The program that mechanically checks a script: banned phrases, dashes and odd characters, niche bans, filler counts, echoes, and numbers missing from the research pack. |

## woodworking-scripts/ (the woodworking niche pack)

| File | What's in it |
|---|---|
| `SKILL.md` | All woodworking-for-profit rules: inputs, freshness, viewer, skeleton, steps, length, money math, proof, where to sell, safety, voice, AI-visual writing, banned list, scanner rules. |
| `references/research-pack-template.md` | What a woodworking research pack must contain. |
| `references/unit-plan-template.md` | The plan filled in before writing, so length comes from the content. |
| `references/voice-samples.md` | Three real narration samples from winning competitors: the voice anchor. |
| `references/excerpts.md` | Winning competitors' lines grouped by job, each marked as usable, rewrite or doesn't transfer. |
| `archive/` | The full BeardedViking and WhosTheVoss transcripts, used for calibration only. |

## personas/

One persona profile per channel. Hank's and Dale's are still to be written.

## tests/

`run_checks.py`: 13 automated checks across the whole library. Run it after any edit.

## PINNED.md

The to-do list, the decisions made, the decisions still open, and the data to pull.
