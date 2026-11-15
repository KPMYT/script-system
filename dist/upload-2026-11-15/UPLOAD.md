# Upload, 2026-11-15: script-writer and the 13 rebuilt channel skills

**What this is:** the simple version of the skills (P21, built 2026-11-06 but never uploaded) for style, plumbing, HVAC and woodworking, with today's plumbing changes (P22) in the plumbing ones:
- one reason to stay to the end, and the secret held until its reveal
- the tips counted
- no plumber in the opening; a call only for a gas leak, live wiring or the main line
- the book once, short (what, why, who, where)
- a quick comment ask at the end
- 14 minutes and up

## Steps (claude.ai, Settings, Capabilities, Skills; on your account and every VA's)

1. **Delete these 14 from the account:**
   - `style-scripts`, `scarlett-starling-persona`, `diane-de-chambray-persona`
   - `plumbing-scripts`, `roger-the-pipe-guy-persona`, `mark-silverbridge-persona`, `vintage-pipefitter-persona`, `werner-finkbeiner-persona`
   - `hvac-scripts`, `roger-the-hvac-guy-persona`
   - `woodworking-scripts`, `hank-hardwood-persona`, `dale-oakfield-persona`
   - `sawdust-sam-persona` (Sawdust Sam is dropped)
   - `script-writer` (the old one still runs the October workflow and checker for these channels)
2. **Upload the 14 `.skill` files in this folder,** all together, and turn them on. `script-writer` also comes as `script-writer.zip` (the same skill), if that's how you upload it.
3. **Leave everything else as it is:** `electrical-scripts`, `frederick-barnes-persona`, every ideation skill and `ideation-core`. Your account's `plumbing-ideation` is newer than the library's.

**The new `script-writer`:** after START and the channel question, it hands plumbing, style, HVAC and woodworking straight to the channel's pack (its steps, its `check.py`). Electrical runs as before. Scarlett and Diane stay ready, as on your account now; Sawdust Sam is gone from the list.

**Plumbing only for now?** Upload the new `script-writer` with the five plumbing skills. The old style, HVAC and woodworking skills on your account are written for the old workflow, so leave those channels alone until their new skills go up too.

## Using them

- Type **START**, pick the channel, then paste the title and the brief.
- Only upload a script whose output ends with a check line saying **PASS**. Anything that starts "NOT READY: DO NOT UPLOAD" goes back.
- **Length:** 14 minutes is the minimum. A full brief can carry 16 to 25. A thin brief is filled out by the writer from everyday plumbing knowledge and lands at about 14 to 16; it never stops with NOT READY for length.
