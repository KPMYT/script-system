# TEST: judge rubric, the first style test runs (Scarlett Starling, Diane de Chambray, iter-07)

The judge's rubric. The writer never sees this file or the reference transcripts. Built 2026-10-29 from the HVAC rubric (`iter-06/judge-rubric.md`), adapted to the style pack, with the operator's hook instruction given its own weight: "the hooks should be very much format carried from our reference and just applied. not long, clear to the point and triggering the right emotions".

## Inputs for the judge

- The output as delivered: `test-run-NN/output.md` (the script alone: `test-run-NN/script.txt`) and the chat (`test-run-NN/chat.md`).
- The inputs: `brief-NN.txt` (the title and brief; the rotation log was "none").
- The scanner, run by the main session on the delivered script with every copy-guard file and the locked title: `test-run-NN/scanner-main-session.txt`, and `tools/verify_output.py`'s findings where given. Treat their counts as facts.
- The reference videos (judge only), in `refs/`:
  - run 01 (Scarlett, necklaces): our own old script on the same title, `w6w_ktMBHXM` (39,935 views, 75x the channel's normal; written before the library), and F01 (Vivian Sinclair, "5 Glasses That Make Women Over 60 Look Instantly Younger", 910K, a faceless item list: structure only).
  - run 02 (Scarlett, bob): our own old script, `h9MsF44shdQ` (514 views, 0.97x), and M12 (Justin Hickox, "You're Styling Your Bob Haircut WRONG! Do THIS Instead- 5 SECRETS", 3.2M; a model the writer could study for structure and emotion, never wording).
  - run 03 (Diane, frumpy): our own old script, `ISAL4NBlshQ` (3,826 views, 6.3x), and M21 (Marie-Anne Lecoeur, "7 Things That Scream 'Old Lady' (Harsh But True)", 1.04M; a model).
- The rules: `style-scripts/SKILL.md` (above all the overrides table, "The opening (the hook)", "Emotion" with the hair and fashion notes, "The video types" and the item shape, "CTAs", "The ending", "Length", "Voice", "Proof", "Money", "Safety", the banned list), `style-scripts/references/hooks.md` (the hook bank the writer must carry a format from), the channel's profile (`personas/scarlett-starling.md` or `personas/diane-de-chambray.md`, with the French lens for Diane) and its book index (`personas/books/`), and the core: `core/workflow.md` §4-5, `core/greenlight-audit.md`, `core/claims-policy.md`, `core/offer-rules.md`, `core/humanizer.md`.

## Score each, 1-10, for the new script and for both references

| Category | What it asks |
|---|---|
| **The hook (double weight)** | Did the writer name a hook model from `hooks.md` and carry its moves in the same order? Is it no longer than that model's hook and under about 110 words, with item one by about 45 seconds? Clear and to the point: one idea a sentence, no scene-setting, no "Picture…"? Does it name the title's feeling early, in her words (hair: the fear of the change, the cut that never looks right; fashion: older or frumpier than she feels, the body), then the promise? The title's promise word in the first sentence or two? No intro, age slogan, tease, task or recap? Quote the hook in full and set it beside the model's moves. |
| Keeping the title's promise | Every title word said at least twice, once in the first minute (the scanner's TITLE WORDS line); the count delivered (run 01: five that look expensive and three that age you; run 02: five secrets; run 03: five rules, and "it's not their weight" paid). |
| Clarity on one listen | Plain words, terms explained the first time, short sentences, one idea at a time. |
| Emotion | The pack's rules: practical fixes for emotional problems; a feeling named in about a quarter of items, one plain sentence, mostly before the fix; her own mirror or closet, never an imagined stranger; the why in every item; permission in plain words, never a slogan; the blame moved off her once in fresh words; the hair or fashion note; the hard word at most once and flagged. Count "you", "but", "I" and questions per 1,000 words, and the items naming a feeling. |
| Voice and persona | First person to one woman; "I" as opinion only, never experience; no age, years, career, relatives or clients; Scarlett's credential line or Diane's heritage line at most once and only where it does a job; at most one approved personal detail; never the name; no house vocabulary ("small gold hoops", "reads as", "from across the room", "quietly" more than once). Diane: every French claim hedged and from the brief or the documented staples; no invented customs; French words without accents, one or two at most. |
| Claims and proof | No try-on, "I wore", "I bought", clients, "studies show", pointing at the screen, the persona's age or face as proof; brands only from the brief (an opinion against a brand said as hers); no health or "reverse aging" claim. |
| Money | No price unless the title is a budget title; "look expensive" delivered through cut, fabric, fit and color, never a receipt. |
| Safety | The six defaults where the topic touches them (dye patch test, heat, thinning hair, shoes and falls, no diet plan, glasses), unless the brief says otherwise; one short line, in proportion. |
| Written for the voice | Heights, sizes and brand names as they're said; no symbols; French words written for the voice; no brackets or voice tags in the script. |
| CTA and ending | The book once mid-video after the first real payoff (60-90 words, the six-part shape, a true fact from the profile and the book match's Way or Secret), a one-line book reminder at the end, then the comment ask about her (her age and where she's watching from, a piece kept twenty years, the rule she was handed at 50), nothing after it; no subscribe ask, no sign-off, no "I read every one", no price, "free" or no-rush close. |
| Length and pacing | At least 12 minutes at the profile's words per minute (Scarlett 169, Diane 172: about 2,030-2,060 spoken words); 12-16 the aim; items about 180-300 words, longer where an item carries the video; nothing padded. |
| Originality vs the models | No lifted wording (copy guard); structure differs from any model it names in at least three named ways. |
| Audit honesty | Does the evidence block match the script? Quote any claim that's wrong. |

## The report

Save as `test-run-NN/judge-report.md`, labelled TEST:
1. Verdict: is it up to the operator's bar (hooks short, clear and aimed at the right feeling; "practical solutions to emotional problems"; "we need to do better" than our old scripts), and would you upload it? One paragraph.
2. The score table (new script vs our old script vs the winner), with the hook double-weighted in a total out of 140.
3. The hook, side by side: the model's moves and word count, the new hook's moves and word count, quoted in full.
4. Every failure with the quoted line, the rule it breaks (file and section) and the fix. Separate **library fixes** (a rule is missing, unclear or wrong) from **writer slips** (the rule was there and wasn't followed).
5. What the new script does better than our old one and than the winner, quoted.
6. The top five changes, ranked.
