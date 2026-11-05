# iter-11 blind judge report: "7 Outlet Wiring Mistakes I Find in Almost Every Older House"

Judge read only `brief.txt`, `judge/script-X.txt` and `judge/script-Y.txt`. Word counts by `wc -w`: X 3,312, Y 3,314.

## 1. As a listener

### Scores (1-10)

| | X | Y |
|---|---|---|
| (a) Flow: each part leads into the next | 7 | 8 |
| (b) Sounds like one real electrician, not a template | 6 | 8 |
| (c) Opening pulls you in, gets to mistake 1 fast | 7 | 8 |
| (d) Easy to follow by ear | 7 | 8 |
| (e) Trust: calm, knowing, on your side, safety in proportion | 9 | 8 |
| (f) Would keep watching | 7 | 8 |
| **Average** | **7.2** | **8.0** |

### Script X: strengths

- The lamp explanation lands cleanly and plainly: "So with the lamp switched off, the metal shell around the bulb can still carry power. That's the part your fingers are on when you change a bulb."
- Calm, in-proportion aluminum verdict: "This is a known problem with a known fix. It's not a reason to panic, and it's not a reason to put it off either. After thirty-five years in the trade, my advice on this one is plain." The tenure line is used once, right before a verdict, as the brief asks.
- The bootleg-ground payoff: "The plug-in tester will now read open ground. That isn't a step backwards. That's the outlet finally telling the truth."
- A useful diagnostic for item 3 that goes past the brief and is correct: "if your house has two-wire cable, and one old three-prong outlet reads correct while the others read open ground, that one is worth opening."
- A natural bridge from 5 to 6: "sometimes the fresh end comes up short. Or you ease an outlet out and find two wires crammed under one screw. Either way, that's number six."
- The pride landing: "That's the connection a careful electrician makes, and it's yours."

### Script X: where it stops flowing

- The kit list arrives straight after mistake 1 is named, so the hook stalls: "The first one is the outlet wired backwards... You'll want a few things for this, and they'll carry you through all seven. A plug-in outlet tester... A non-contact pen tester... A two-probe voltage tester... A screwdriver. And a pair of wire strippers." The viewer gets five tools before using one.
- The prove-dead order is one paragraph of about 250 words: "First, hold the pen tester... Second... Third... Fourth... Fifth... Sixth... Seventh... And last..." It is correct, but it reads like a numbered checklist, and by ear it's hard to hold onto.
- The refrains become a template. "Then, power back on." opens a paragraph six times (items 1, 2, 3, 5, 6 and 7). "Same order as number one." appears five times, and "that's where you stop" about six times. A listener will notice the pattern.
- An ambiguous pronoun after the warning-signs detour: "If you find it, that's where you stop." Here "it" means aluminum, but the paragraph before is about hot plates and burning smells.
- A long sentence that carries a definition in the middle: "In a room that now needs AFCI protection, which guards against arcing, electricity jumping a small gap where it shouldn't, the replacement needs that too."

### Script Y: strengths

- The hook is tight, and mistake 1 arrives within about 90 words: "Here are seven mistakes hiding behind the plates in almost every older house, six you can fix yourself and one for a licensed electrician. Number one is the outlet that's wired backwards..."
- It sounds like a person with views: "I won't do it any other way, and I don't want you to either." / "I'd rather have an honest open ground than a fake correct, every time." / "I don't like that shortcut at all."
- Strong bridges that carry the "tester" thread: "That tester has told you the truth twice now. But there's one outlet it gets wrong, and that's number three." / "You can find those first three with a tester and a screwdriver. Number four you can check from the basement..."
- It draws the viewer in with questions: "What does your tester say at the outlet behind your computer? That's the one I'd check first." / "Was your house built in those years? Then this check is for you."
- It reassures in proportion after the aluminum warnings: "I know that's a lot of warning signs. But here's what I want you to hold onto. This is a known problem, and it has a known fix."
- It tools up as needed: the pen tester, the two-probe tester and the strippers each arrive when they're used, not in a list up front.

### Script Y: where it stops flowing

- The recap of the prove-dead order in item 2 is made of noun-phrase fragments that read like notes: "The pen tester checked on an outlet you know has power, and the plug-in tester lit in both halves. Then the breaker off and taped, and the plug-in tester dark in the top outlet and the bottom one."
- The "never proof" line comes after the order has already finished, so it sounds bolted on: "A pen tester going quiet is never proof on its own, because it can miss a live wire. That's why you check it on a working outlet before and after."
- Stacked definitions, then a dangling clause: "Gauge is the wire's thickness, and amps are how much current flows. And never for aluminum."
- "Your" and "you" are overused to the point of oddness: "so your newer plugs would fit", "It looks tidy to you.", "the outlet still works for you."
- The many one-line paragraphs can sound staccato over long stretches (lines 107-141), although short sentences suit text-to-speech.

## 2. Basics (pass/fail)

| Check | X | Y |
|---|---|---|
| 12+ min (~1,950+ words) | PASS (3,312) | PASS (3,314) |
| No channel intro or teases | PASS | PASS. Note: the tenure line sits in the opening ("After thirty-five years in the trade, I still wouldn't trust an older house's outlets until they'd been checked for these."). The brief says tenure goes "only before a verdict". This one leans toward a verdict but works as intro credentials. Borderline; move it to the aluminum verdict. |
| Breaker off AND proven dead with a tester, every time it matters | PASS. The full order at item 1, then "Same order as number one" at items 2, 3, 5, 6 and 7. | PASS with a soft spot. The full order at item 1 and a brief order at items 2, 3, 5 and 6. Item 7 only says "always with the power off and proved off first", placed after the steps rather than before them. |
| Stop signs that name their trigger | PASS. Aluminum, brittle or scorched insulation, a melted box, black already on brass but still reversed, a live wire with no breaker found, two cables with no way to tell line from load, a packed box. The breaker stays off after each one. | PASS. The same triggers. "Breaker stays off" is said for insulation and for wiring that doesn't match, but not explicitly for aluminum ("that's where you stop") or for the line/load stop. |
| Facts consistent with the brief | PASS | PASS |
| Short subscribe, then comment ask | PASS. Wrapped in `===START CTA(NO BOOK)===` markers, which must be stripped before TTS. | PASS |
| No recap or homework list | PASS (one small action, as the brief asks) | PASS (one small action) |

## 3. Facts check

Neither script has a wrong or risky claim. Both get these right:
- **Polarity:** hot goes on brass and neutral on silver; the wide blade is neutral; the lamp's shell stays live.
- **Grounding:** open ground means nothing is connected; the code's three choices with the exact labels; the GFCI adds no ground and does not cause the open-ground reading; the test button is the check that counts.
- **Bootleg ground:** the neutral-to-ground jumper; a three-light tester can't detect it; it is against code.
- **Aluminum:** 1965 to the mid-1970s per CPSC; the "AL" print on the jacket; CO/ALR is "at best, an incomplete repair"; COPALUM by trained and authorized electricians, with AlumiConn next best; the list of what never goes on aluminum.
- **Backstabs:** 14-gauge solid copper on 15-amp circuits only; back-wire clamp terminals are a different thing.
- **The rest:** one wire per screw unless marked for two; clockwise about three-quarters of the way round; the strip gauge.
- **GFCI places and other code:** the GFCI list including the crawl space and "within 6 feet"; AFCI and tamper-resistant outlets on replacement; "code is local / local inspector". Neither uses brands (beyond the two named in the brief), prices or code section numbers.

Small notes:
- **Y:** "If your chart says the hot and neutral are reversed, the wires behind that outlet are on the wrong screws". This states the cause as certain, then later qualifies it ("if the black was already on the brass..."). It's minor, but X's framing ("here's what's going on behind the plate") is no better. Y adds two correct and helpful points: "If you found a ground wire and connected it, the plug-in tester should now read correct", and that the pigtail should be new copper of the same gauge. Y's tamper-resistant gloss ("so a child can't push something into one slot") is correct.
- **X:** "COPALUM" written in all caps may be spelled out letter by letter by the text-to-speech. Write it "Copalum". The CTA marker lines must not reach the voice.
- **Both:** "the code gives you three choices" would be safer as "the code in most places gives you three choices", although both follow it with the local-inspector line.

## 4. Verdict

**I would publish Y, by a modest margin (about 0.8 on the listener average).** Y sounds like one man talking to you. Its bridges carry a thread ("that tester has told you the truth twice now"), its hook gets to mistake 1 without a detour, and its opinions ("I'd rather have an honest open ground than a fake correct") build trust. X is the more disciplined safety script: its stop signs are fuller and its tenure placement is cleaner. But it reads by ear like a well-made template: the kit list up front, a seven-step block paragraph, and "Then, power back on." six times.

- **Y: light edit.** Move the tenure line from the opening to the aluminum verdict. Turn the item-2 prove-dead fragments into full sentences. Move "a pen tester going quiet is never proof" ahead of the order. Put an explicit prove-dead step before the item-7 steps. Add "the breaker stays off" to the aluminum and line/load stops. Trim the stray "your" and "you".
- **X: light edit, leaning to medium.** Move the kit list so each tool arrives when it's used. Break the prove-dead block into shorter spoken beats. Vary the "Then, power back on." and "Same order as number one." refrains. Fix "If you find it". Change COPALUM to Copalum for the TTS. Add a few first-person lines of opinion.
