# Model file spec (style references)

How every file in `references/models/` is built (2026-10-29), adapted from `electrical-scripts/model-file-spec.md`. Kept for adding models later; not part of the installed skill.

**The library:** 30 real presenters (M01 to M30) and 7 faceless or AI videos (F01 to F06, F08), listed with views, dates and channel normals in `studies/style/models/approved-models.csv`. The operator's rules (HANDOFF §3, 2026-10-28 and session 14, P19): models from real people presenting to women over 50, outliers of the last 24 months plus a few big older ones, nothing before 2022, each picked for the operator ("your call on the rest"); a faceless section of 5-10 outliers on topics the real models don't cover. F07 was dropped (mostly music).
- **[real]** (M files): structure, voice and emotion may be borrowed, wording never. Justin Hickox (M06, M08, M10, M12) is a man: structure and emotion, never a voice sample. M05 (RaDona) is a salon cut-along: voice and emotion for the over-70 client, not structure.
- **[structure only]** (F files): the shape (order, item count and length, pacing, devices) may be borrowed; never the voice, the wording or the persona's claims.

Every model is ONE markdown file in `style-scripts/references/models/`, named `<ID>-<channel-slug>-<short-topic-slug>.md`, e.g. `M06-justin-hickox-look-10-years-younger.md`. The transcript and comments are already collected: `studies/style/data/<channel_slug>/<video_id>/` (`meta.md`, `transcript.txt`, `comments.md`), with the study notes in `studies/style/notes/<channel_slug>__<video_id>.md`. No NexLev calls are needed.

## File layout (exactly these sections, in this order)

```
# <ID>. <Video title, exactly as on YouTube, curly quotes straightened>

- **Channel:** <name> · **Video:** <id> · https://www.youtube.com/watch?v=<id>
- **Tag:** [real] (structure, voice and emotion; never wording) | [structure only] (faceless or AI: the shape only; never voice, wording or claims)
- **Views / normal:** <N.NNx> (<views> on <collection date> / channel normal <normal>, from meta.md)
- **Posted:** <YYYY-MM-DD> · **Length:** <m:ss> · <N> spoken words · **Video type:** <one of the types below> · **Side:** hair | fashion
- **Presenter:** <real woman | real man | AI or faceless narrator: as heard, e.g. "named narrator claiming 40 years in a fitting room">

## Beat map

| Time | Beat | What it does (no quoted wording) | Emotion | Words |
|---|---|---|---|---|
| 0:00-0:14 | POINT | names the look the viewer is worried about and the promise | fear of looking older → hope | 38 |

- **Items:** how many, how long each runs (shortest, longest, typical), in what order and why; where item one starts (time and word).
- **Item shape:** the moves inside a typical item, in order (the look, why it ages or works, the turn, the swap, the check, the result), and which it skips.
- **The title's promise:** the title's key words ("younger", "expensive", "instantly", the count) and where each is said; whether the promise is paid.
- **Feelings:** how many items name an inner feeling (07's rule: a feeling about herself, not a look word); before or after the fix; first person or about the viewer.
- **Villain:** who or what is blamed, if anyone (the advice she was handed, the shop, makers, trends, her past self, the salon), how often; whether it's aimed at a habit or at people.
- **Hard words:** "frumpy", "old lady", "granny", "dated" and the like: how many, and how they are flagged.
- **CTA placement:** where, how long (sponsor reads: say so).
- **Ending:** what the last 30 seconds do.
- **What sets it apart from other models of its type:** 2-3 bullets.

## Emotion voicing

For each feeling the video uses, with `studies/style/comparison/07-emotions-and-age.md`'s codes (permission and rebellion; relief at being understood or at the why; fear of the change; the body, comfort and confidence; frumpy or feeling old; invisible or unheard; judged; comparison with her past self or younger women; being seen, compliments), give: where it first comes in (timestamp), how often it returns, and 2-4 verbatim lines with timestamps showing the words that carry it. One line on the emotional arc of the whole video (e.g. "worry about looking older → why → small swap → seen as polished → permission").

## Why it works

One paragraph: what the comments thank and complain about (quote 3-6 from `comments.md` with like counts, never usernames), the pace, the opening, what viewers say they'll change.

## Script (verbatim, labelled)

The full transcript, each paragraph starting with its [m:ss] timestamp, labels in square brackets at the start of the passage they cover.
Labels: [POINT] [QUESTION] [SCOPE] [REASSURANCE] [PROMISE] [ITEM] (1), (2)... [LOOK] [WHY] [TURN] [SWAP] [CHECK] [RESULT] [FEELING] [PERMISSION] [HARD WORD] [CREDENTIAL] [ASIDE] [FORWARD] [CTA] [COMMENT] [CLOSE]
Banned (label wherever they occur): [INTRO: banned] (name or channel intro) [TEASE: banned] [RECAP: banned] [POINTING: banned] ("as you can see", "look at this") [TRY-ON: banned] (wearing, trying, buying or owning it herself; her own body, face or age as proof) [CLIENT: banned] (clients and stories about named or unnamed people she styled) [AGE SLOGAN: banned] ("no age limit", "you've earned it", "you deserve", "never too late") [SALON BLAME: banned] (the stylist or salon as the villain: "salon is not the enemy", operator 2026-10-29) [SHAMING: banned] (adjectives on the woman, not the garment) [MONEY: only on budget titles] [HEALTH CLAIM: banned] (regrow, reverse aging, diet or weight loss) [SUBSCRIBE: banned for these channels] [SIGN-OFF: banned for these channels] [PRODUCTION NOTE: banned] [SPONSOR] [INVENTED PERSONA: banned] (F files: the narrator's claimed years, family, clients or past)
Conventions: two labels on one line = the passage does both, in order; "(2, cont.)" = an item picked up again. Keep the transcript text verbatim (auto-caption mistakes kept); drop only noise tags like [Music]; straighten curly quotes. Replace any email address, phone number or discount code with [removed]. A sponsor read over about 150 words may be shortened to "[SPONSOR] (sponsor read, N words, omitted)". Long product lists in a description are not part of the script.

## Lines worth studying ([real] files only)

Up to 8 verbatim lines with timestamps, each labelled with its job: hook, the turn, the why, a feeling line, permission, the flagged hard word, a comment ask about the viewer, a bridge. These feed `references/excerpts.md`. F files write "None (structure only)."

## Doesn't transfer

Bullets, each quoting the line with its [m:ss]: everything Scarlett Starling and Diane de Chambray (AI talking-head presenters; no age, no years, no career; Diane's one heritage line "raised in Paris"; no relatives, clients or checkable facts; the book as the only CTA; no subscribe ask; no sign-off) can't or mustn't use: try-ons and "as you can see", her own body, face, age or purchases as proof, clients and salon stories, greetings and name intros, teases, recaps, age slogans, salon or stylist blame, prices on titles that aren't about budget, health or diet claims, sponsor reads, discount codes, subscribe asks, sign-offs, and any factual slip you notice (mark your own as "check against the brief"). For F files, also the narrator's invented persona.

## The video types (use these names)

mistakes that age you; never these, wear these instead; the best N; styling it wrong (N secrets); how to wear X; body-shape fixes; the rules she never breaks; the why explainer. Use "other: <short description>" if none fits (e.g. "other: salon cut-along", "other: gray-hair story").

## Rules for the builders

- Use the collected files only; write ONLY your assigned model files. Don't commit, push or run git. Scratch work goes in your own subfolder of the session scratchpad; run Python with `python3 -I`.
- Verify by script that the labelled script text (labels removed) matches `transcript.txt` word for word, and that every quote in "Emotion voicing", "Why it works", "Lines worth studying" and "Doesn't transfer" is verbatim with the right timestamp (within 3 seconds of the segment start) and every comment quote matches `comments.md` with its likes.
- Plain, clear English in your own text; no em dashes, no curly quotes, no ellipsis characters.
- When done, reply with: each file name, its video type, side, spoken words, item count, feeling items, its emotional arc, and anything you couldn't do or flagged.
