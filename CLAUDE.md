# Script System: read this first

This repository is the master copy of the script-writing library for the operator's YouTube channels. Read `SESSION-HANDOVER.md` (where the last chat left off and what's next) first, then `HANDOFF.md` (decisions and why), `README.md` (what each file is) and `PINNED.md` (open items) before changing anything.

## Layout

- `core/`, `woodworking-scripts/` (and future niche packs), `personas/`, `tests/`: **the library.** The source of truth.
- `studies/`: research data (competitor transcripts, notes). Collect and describe only; never edit study data to fit a conclusion.
- `archive/facelessos-original/`: the original bought FacelessOS files and the old house-rules prompt. Read-only. Used for comparison, never as rules.

## Working rules

1. **Never change a locked decision** (`HANDOFF.md` section 3). If something suggests one should change, write it in `PROPOSALS.md` with the evidence, and leave the rule as it is.
2. **Log every change** in `CHANGELOG.md`: date | files | what changed | why.
3. **After every change,** run `python3 tests/run_checks.py`. Nothing is committed while a check fails.
4. **Never delete history.** Test runs live in `tests/iterations/iter-NN/`, each with its outputs, results and changes. Old iterations are never overwritten.
5. **Test data is labelled TEST** and lives in `tests/fixtures/`. It never goes into `personas/` or `core/channels.md`.
6. **Keep the layers clean:**
   - portfolio-wide rules go in `core/`
   - niche rules go in the niche pack
   - channel settings go in the persona profile
   - nothing is duplicated across layers
7. **Keep `README.md`'s file map current** whenever files are added or renamed.
8. **Handover and `main`.** `main` is the shared branch every new chat starts from. Work on the chat's own branch. At every handover (around 50% context, Claude says when), rewrite `SESSION-HANDOVER.md`, log it, run the checks, commit, then merge the chat's branch into `main` and push `main`. The operator has given standing permission for this push. Never force-push `main` and never delete branches.

## Testing with subagents

When testing script generation, keep the roles separate so the test is honest:

- **Writer:** sees only the library and the test inputs. It follows `core/workflow.md` exactly, as a VA's chat would. It never sees the rubric or the source script it's being compared against.
- **Operator:** plays the VA: types START, supplies inputs, tries mistakes such as missing inputs or "just write it."
- **Judge:** scores the writer's output against the rubric, the scanner and the original source script. It reports failures with quoted lines. Before judging, the main session runs `tools/verify_output.py` on the saved output; its findings go to the judge as facts.

Fixes are made by the main session, logged, tested, and then the cycle runs again.

## Adding a niche

1. Run a competitor study into `studies/<niche>/`.
2. Build a niche pack modelled on `woodworking-scripts/`, with:
   - inputs and freshness
   - skeleton
   - voice samples and excerpts
   - research pack and unit plan templates
   - a scanner block
3. Add tests.
4. Add its channels to `core/channels.md`.
