# iter-01 changes

Applied 2026-10-20 after the operator approved each finding in `REVIEW.md` ("you can make the required edits"). Copies of every file as it was before are in `before/`. Checks: `python3 tests/run_checks.py`, 20/20 passing (two new checks).

| File | What changed | Why (REVIEW.md) |
|---|---|---|
| `core/retention-mechanics.md` | Section 2: the opening plays on the viewer's pain point or wish and points at the solution (one sentence, never delays the first payoff; a numbers-only hook is flat). Section 4: personality isn't padding; an extra sentence here or there is allowed. | W1, W4 |
| `core/script-structures.md` | Every hook also touches the viewer's pain point or wish. | W1 |
| `core/workflow.md` | Run step 3 carries the operator's quality bar. Section 4: few numbers, easy to follow (H22). Section 2: research-pack may be "none", and the chat then builds, verifies and gate-checks the pack; a title claim it can't support stops with NOT READY and offers honest titles for the operator to re-lock; writing without a pack is still refused. The old "Later:" line replaced. | W1, W3, 9 |
| `core/humanizer.md` | H22 extended: too many numbers is the same tell; exact figures only where the viewer needs them, one price per item, small costs collapsed, no fee schedules or lists of listings read aloud. | W3 |
| `core/greenlight-audit.md` | New A1b (the hook plays on emotion; quote the line). C2 covers numbers (quote any sentence with three or more dollar figures). B3: personality isn't padding. F3: the CTA direction as the profile words it. F4: "book", never "e-book". | W1, W3, W4, 1, 12 |
| `core/offer-rules.md` | A book is always "the book" or "my book", never "e-book" or "ebook", on every channel. | 12 |
| `core/research-and-sourcing.md` | Section 1: who runs research (ideation's pack step, or the script chat when START has no pack). Section 2 and 10: title-only claims about the persona's selling, income or tenure are allowed and never flagged; narration still never claims them. | 8, 9 |
| `core/persona-profile-template.md` | Words per minute measured from the channel's real voiceovers (150 if none yet). Offer type "book (digital download)". | W2, 12 |
| `core/script-scanner.py` | The word-number parser steps past a token like "three-quarter", "five-eighths" or "one-by-eight" instead of looping forever. | 7 |
| `tests/run_checks.py` | Check 14: the scanner finishes on fraction words. Check 15: every persona profile flags "e-book". | 7, 12 |
| `woodworking-scripts/SKILL.md` | Promise: one line on the viewer's fear or wish, with this audience's pains named. Materials: one price per item, specs as asked at the store. Build order may put assembly after the finish. Steps earn extra words for a personality line. Exaggerated titles: selling and tenure claims for Hank and Dale. Money block kept easy to follow (fees as one total). Proof: range plus one example; never name a shop. Swearing: an order to the viewer counts as aimed at the viewer (example). Personal details at natural pauses, never inside a tricky step. Food contact includes factory glue. Before-handing-over checklist adds the hook and numbers. Inputs: research-pack may be "none". | W1, W3, W4, W5, 2, 3, 8, 9, 10, 11 |
| `woodworking-scripts/references/unit-plan-template.md` | Promise: the fear or wish it touches. Money block: numbers worth saying. New OPINION MOMENTS. | W1, W3, W4 |
| `woodworking-scripts/references/research-pack-template.md` | Safety: food contact checks the finish and every glue, factory glue included. | 3 |
| `personas/hank-hardwood.md` | Words per minute 185. Offer type: "the book", never "e-book". Every CTA points to both the QR code and the top link in the description. Scanner bans "e-book" and "ebook". | W2, 1, 12 |
| `personas/dale-oakfield.md` | Words per minute 170. Offer type: "the book", never "e-book". Scanner bans "e-book" and "ebook". CTA unchanged ("link below"). | W2, 12 |
| `ideation/woodworking-ideation/SKILL.md`, `references/steering.md`, `references/audience.md`, `references/word-bank.md` | Hank's titles may claim selling and tenure too, in his own words; "40 years" stays Dale's. | 8 |
| `HANDOFF.md` | New block "Operator decisions, 2026-10-20 (first script test review, iter-01)". | record |
| `README.md`, `PINNED.md` | Check count 20; iter-01 noted. | record |
| `tools/build_skills.py` | Each skill is also built as a plain `.zip` (same contents as its `.skill`), included in the Drive bundle; INSTALL.md says to use whichever the upload screen takes, on the account, not in a project. | Operator's request: an upload zip per skill. |
| `dist/` | Rebuilt with `tools/build_skills.py`. | packaging |
