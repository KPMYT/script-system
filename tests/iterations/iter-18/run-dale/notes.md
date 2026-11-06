# iter-18 run-dale: writer's notes

Date: 2026-11-06. Channel: Dale Oakfield's Workshop. Title: "Dog Owners Pay $90 for This $15 Build I Can't Keep Them in Stock". Brief and pack: `tests/iterations/iter-18/brief-dale.txt` (passed as both `--brief` and `--pack`).

Files read: the woodworking-scripts `SKILL.md`, the dale-oakfield-persona `SKILL.md`, its book file (chapter map and the brief's book-match pages only: 10 to 13, 60 to 62, 82 to 84, 90 to 91), the W04 model, `check.py`, and `core/workflow.md` sections 4 and 6.

## Model picked
**W04, `W04-bearded-viking-step-stool.md` (Small furniture).** A raised feeder is a stand that holds weight. "Better than the store's" (W05) partly fits too, because of the boutique-store comparison, but the build itself is small furniture.

## Check results
**Run 1: RESULT: FAIL (2)**
- `FAIL voice: a unit abbreviation or symbol '2 in' on line 15` ("Technique 2 in the book, pages 10 to 13, ...")
- `FAIL voice: a unit abbreviation or symbol '24 in' on line 47` ("... Common Mistake for Technique 24 in the book, on page 91.")
- INFO lines: pitch 57 words, starts at 8%; 5 book mentions; title's number in the opening: yes (15, 90); 2328 words, about 13.7 minutes.

**What I fixed:** I reworded only those two sentences. "In the book, Technique 2 on pages 10 to 13 is about..." and "...the Common Mistake for the book's Technique 24, on page 91." Both were false positives: the checker read "2 in" and "24 in" as inches.

**Run 2: RESULT: PASS**
- `INFO book pitch: 57 words, starts at 8% of the script`
- `INFO the line before the pitch: "Buy the bowls before you buy anything else, ..." | the line back: "Now, back to those bowls and the rest of the list."`
- `INFO book mentions outside the pitch: 5`
- `INFO sentences with three or more commas: Once you've built one, there's a single-bowl stand ...` (this is the three-variant sentence: three items, which the rules allow)
- `INFO the first 15 seconds: "... about 15 of pine turns into a raised dog feeder ..."`
- `INFO the title's number in the opening: yes (15, 90)`
- `INFO 2328 words, about 13.7 minutes at 170 words a minute`

The check also passes when run on `output.md`. The VO copy has 25 tags (about one per 93 words). With the tags stripped, it matches the script word for word, and no marker line is tagged.

## Unclear or contradictory points
1. **Is the pack verified?** The brief file says "RESEARCH PACK: none (TEST: this brief's figures stand in for the pack; anything marked (check) is unverified)". It has no "Verified on" date, which Step 1 requires. I went ahead because the task statement said the pack was verified on 2026-11-06.
2. **Where to sell.** The persona says "Etsy for small, light, giftable or personalized pieces; Facebook Marketplace (local pickup, no fee) for bulky ones". The brief says "No brand or store named" and "Not found: which platform or fee." I followed the brief and wrote "a craft market, or a local listing online for pickup". The reason given, "bulky to ship", is my own reading.
3. **Fee, time and batch.** The persona asks for "The venue's fee as one total, then what's left, one batch line 'if they all sell', the time as an estimate". The brief says these are "not found ... (the research pack must supply any fee or time used)". So the script gives what's left before fees ("about $60 a stand") and tells the viewer to find out the fee. It has no time estimate. The batch line ("two large ones ... about $120 left before fees") is my own math on the pack's figures, not a figure from the pack.
4. **Prices in the materials walk.** The persona says "each thing with its price". The pack prices only the wood and the wood-plus-bowls total, and it gives the pen as "about the price of a good lunch". Everything else is left unpriced.
5. **No alternative for the pocket-hole jig.** The persona says "Anything more (... pocket-hole jig) gets an alternative or is said as optional". The brief gives no alternative, so the script has none for it.
6. **Screw length may be a fact problem.** The pack gives "2 and a half inch ... pocket screws" with the jig "set for inch-and-a-half stock". These drive from two-by-six aprons into three-quarter-inch end panels. The book's page 61 Common Mistake is exactly a screw that's too long punching through the face. I kept the pack's figure and added "test a joint in scrap first". Someone should check this by hand.
7. **Book mentions.** The persona asks for "Five of them", but the brief's book match covers four techniques. My fifth mention uses the page 62 safety note (clamp before drilling) at the bowl-hole step. In the book, that note is written for pocket holes. The judge should decide whether it counts.
8. **Length.** The script is 2,328 words, about 14 minutes. The persona says "Above that the build sets the length; never pad". The original video ran 16:15.
9. **Pitch length.** The pitch is 57 words against the persona's "about 45". The checker allows 30 to 75.
10. **Minor points in the pages.** The pack says it "replaces `core/workflow.md` sections 2 to 6", yet Step 5 points back to sections 4 and 6. The layout in section 6, "VO COPY — ELEVENLABS V4", contains an em dash. I kept it as printed.
