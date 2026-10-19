# iter-01 test protocol: plumbing-01 (no niche pack)

TEST run. Roles kept separate, per `CLAUDE.md` ("Testing with subagents"). The main session relays messages between the operator and the writer word for word and does nothing else during the run.

## Roles and what each may read

| Role | Reads | Never reads |
|---|---|---|
| **Writer** (a VA's chat) | `core/`, `tests/fixtures/channels.md`, `tests/fixtures/personas/`, and only what the operator pastes. May run `core/script-scanner.py`. Scratch files go in `writer-work/`. | `tests/fixtures/inputs/` (inputs arrive pasted), `tests/fixtures/judge-only/`, `tests/iterations/`, `studies/`, `archive/`, `woodworking-scripts/` (the channel has no pack), the root docs (`HANDOFF.md`, `PINNED.md`, `CHANGELOG.md`, `PROPOSALS.md`, `SESSION-HANDOVER.md`). |
| **Operator** (plays the VA) | `tests/fixtures/inputs/`, `tests/fixtures/channels.md`, this protocol. | the library rules, the source script. |
| **Judge** | Everything: the transcript of the run, the writer's final output, `core/` (the rubric), the scanner, the research pack, the voice samples, and the source script in `tests/fixtures/judge-only/`. | nothing is off limits. |

## The operator's script (planned mistakes)

1. `START TEST`, naming no channel. Expected: one question, the numbered TEST channel list, nothing else.
2. `1`. Expected: one numbered message listing every missing required input (title, brief, research-pack, rotation-log, and voice-samples, since the channel has no pack and the profile has none), each with one line on what a valid one looks like. Nothing about tone, length, script type, voice provider or CTA.
3. Pastes title, brief and rotation log only, and says to just write it and skip the research pack and samples. Expected: refusal; asks only for research-pack and voice-samples.
4. Pastes the research pack and the voice samples. Expected: no more questions; the full output skeleton (TEST line first, SCRIPT TYPE, script with Talking Head markers, VERDICT, FORMAT CHECK, ROTATION LOG ENTRY with an end-CTA field, AUDIT EVIDENCE with `copied`, VO COPY) or a correct NOT READY block.
5. After a finished script: `START TEST` again. Expected: only `Start a new chat for the next script.`

## What the judge reports

- **Gate behavior:** each operator turn against its expected reply above.
- **Format and skeleton:** `core/workflow.md` sections 4-6.
- **The audit, re-run independently:** every check in `core/greenlight-audit.md` (A-F), quoting failing lines; the scanner run with the research pack as `--pack` and the source script as `--refs` (to catch lines copied from the source).
- **Against the source:** does the script deliver the same promise at least as well (diagnosis by symptom, free checks before parts, concrete numbers), without the source's weaknesses (wind-up, "separate video" references, misnamed part, recap, generic ending), and without cloning it (E3)?
- **Numbers:** every number traced to the research pack.
- **Verdict:** would this script be safe to upload unread? Plus a ranked list of library fixes (rule, file, why), separating library problems from writer slips.
