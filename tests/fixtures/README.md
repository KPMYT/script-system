# Test fixtures

**Everything in this folder is TEST data.** It exists so `START TEST` (`core/workflow.md`, section 1) can run the whole workflow without a real channel. None of it ever goes into `core/channels.md` or `personas/`, and no test output is ever uploaded.

| Path | What it is | Who may read it |
|---|---|---|
| `channels.md` | The channel list `START TEST` shows. | writer |
| `personas/` | TEST persona profiles, written from `core/persona-profile-template.md`. | writer |
| `inputs/` | The inputs an operator pastes at the gate: title, brief, research pack, rotation log, voice samples. | operator (pastes them); the writer sees only what's pasted |
| `judge-only/` | The original source scripts the judge compares against. | judge only. **The writer never opens this folder.** |

## The fixture sets

| Set | Channel | Niche pack | Title | Source (judge only) |
|---|---|---|---|---|
| plumbing-01 | TEST Plumbing | none (core fallbacks) | Why Your Toilet Keeps Running, and How to Fix it | `judge-only/plumbing-01-source.md` |

Inputs for plumbing-01: `inputs/test-plumbing-brief.md` (title and brief), `inputs/test-plumbing-research-pack.md`, `inputs/test-plumbing-rotation-log.md`, `inputs/test-plumbing-voice-samples.md`.
