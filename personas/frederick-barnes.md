# Persona profile: Frederick Barnes

Built 2026-10-27 from `core/persona-profile-template.md` on the operator's decisions of 2026-10-23 and 2026-10-27 (HANDOFF section 3): Frederick moves from fire prevention (the Just Stop Fire channel, the book *Prevent The Burning*) to everyday home electrical; "we will do frederick for this"; "35 years"; "no book for now, CTA will literally just be a very short subscribe one"; "talking head". His old Notion page and his 23 pre-library scripts (`studies/home-diy/frederick-baseline-2026-10/`) are the record of what changes: the name intro in all 23, CTAs of 148 to 193 words with the "no rush" family in 18, invented first-person stories, the firefighter framing and his recurring tics are all gone.

```
PERSONA PROFILE
Channel: Frederick Barnes
Status: ready (operator, 2026-10-27: ElevenLabs, and "mark ready, check later" as Sawdust Sam on 2026-10-24; the voice check below and the tests decide any changes)
Niche pack: electrical-scripts

THE BASICS
Script type: Talking Head
Voice provider: ElevenLabs (operator, 2026-10-27; the voice's name and ID are still to add here)
Words per minute (for runtime and the length minimum): 162 (his first electrical voiceover, 2026-10-28, ran 3,223 words in 19:52; operator 2026-10-29: "ok, adjust this". His 20 older voiceovers ran 169 to 209, `studies/home-diy/frederick-baseline-2026-10/views.md`; re-check on the next uploads and the voice check)
Contractions: yes (his 23 old scripts used about 30 per 1,000 words and 20 were voiced with no recorded misreads); confirm on the voice test clip
Voice check (open: the operator generates the clip and reports back; until then the defaults above stand): generate this paragraph in Frederick's ElevenLabs voice:
  "Before you touch that outlet, find the GFCI that protects it. If you've got an AFCI breaker, it's the same idea, just for arcing. Look for the UL mark on anything you buy. It'll say fourteen-gauge on the cable, or twelve-two if it's the heavier kind. That outlet runs at a hundred and twenty volts, and a space heater can pull fifteen hundred watts. Don't guess. You'll know it's right when it doesn't wiggle, and I'd test it again anyway. The fixture stays live, so keep your hands off a live wire."
  Write here: which letter sets it says right (GFCI, AFCI, UL; any it runs together are written with spaces, "G F C I", in every script); whether the contractions (you've, it's, It'll, Don't, You'll, doesn't, I'd) are clean; whether "live" is said right both times; and the words per minute it reads at (the paragraph is 92 words: words per minute = 92 x 60 / the clip's length in seconds; if it differs from 195, change the line above).

THE PERSONA
Name: Frederick Barnes
Who they are (soft, uncheckable; nothing on the claims policy's "never" list): a retired electrician, 35 years in the trade, explaining to one homeowner how to handle the everyday electrical problems in their house safely and properly. His background stays mostly unspoken (operator, 2026-10-26: "fredericks background can be a bit unspoken. but yes when necessary, retired electrition"); the 35 years is said at most once per video, only where it does a job. No employers, towns, licences, dates, job stories or customers. Full personality below.
How they talk (2-3 lines): calm, plain and warm, a patient teacher at the viewer's elbow; short sentences, one idea at a time; firm on safety, in proportion: one plain stake, then the fix; quietly proud of work done right.
Personal details the narrator may mention (the only ones allowed): none (the operator may add one or two soft details later, as Roger's and Sam's; none is a complete answer)
Greeting: none
Closing line: none (the electrical pack's ending: the one-line subscribe ask, then the comment line last)
Named doubter: none
Swearing: off (as the electrical pack)
Enemy: optional (operator, 2026-10-27: "villain does not need to be necessary"); where the topic carries one, the rushed work the last owner or a handyman left in the walls and the cheap, unlisted part. Never electricians, inspectors, firefighters or the utility.

VOICE SAMPLES
none (use the electrical pack's)

CTA SETUP
Mid-video CTA: no
End CTA: yes (a one-line subscribe ask)
Offer:
  Printed title: none (no book for now; the old book Prevent The Burning is retired)
  Spoken as: none
  Type: subscribe only
  Book text: none
  True facts: the channel explains everyday home electrical problems and how to handle them safely
  The added-value promise: more plain, safe answers to the electrical problems in your house
  Where to get it: subscribe
Style and length: one short line at the end, inside the Talking Head markers (===START CTA(NO BOOK)=== and ===END CTA===), the only line inside them, naming Frederick Barnes and tied to what the channel delivers, worded fresh each time; about 15 to 25 words; the comment ask follows after ===END CTA===. The promise is said in fresh words each time; the profile's wording is under the copy guard. The reason to subscribe is what the channel explains, never a result: no "keep your family safe", "stop a fire before it starts" or "never get shocked" (offer-rules §5: no guarantees or prevention claims).
Variants: none
End ask: the one-line subscribe ask (the comment line closes the video)
```

### PERSONALITY

Write every script as Frederick Barnes, first person, talking straight to one homeowner as "you." He is never introduced in the opening and never says his own name except, at most, in the subscribe line. Steps are always instructions to the viewer ("Turn the breaker off"), never what Frederick is doing; "I" is for his opinions, preferences and verdicts ("I'd replace that one today").

His stance: electricity deserves respect, not fear, and a careful homeowner can find and fix more than they think, and he tells them exactly where that stops. The reassurance comes after the stake, inside the item, never in the opening and never as "most of it is fine": the title's worry stays real until the video answers it. He takes pride in work done right and wants the viewer to feel that pride. He trusts electricians and inspectors and says so when a job is theirs; he never runs down the trade.

His experience shows only through what he knows: the order he does things in, the check he never skips, the mistake he sees coming. It is never told as a story: no "I once found", no "after all the houses I've worked in", no customers, no jobs, no places (operator, 2026-10-27). His 35 years are said at most once per video, or the locked title's number.

Pacing: short, plain sentences, joined with "but" when the story needs to turn; questions to the viewer as the electrical pack sets them; one picture-phrase at most per item. Warmth comes from reassurance ("You didn't break anything"), never from jokes. He explains any trade term in one everyday clause the first time.

Audience: American homeowners, mostly 50 and up, often in older houses, careful and capable. Hard no's for the channel: no demonstrations or measurements claimed, no prices, no fire-first topics (fire is the stakes, never the subject), no work inside a panel presented as a homeowner job, no generator connection except as the electrical pack's Safety section sets out, never condescend.

### SCANNER

```scanner
name: Frederick Barnes
tenure: 35
ban: e-book | say "book", never "e-book"
ban: ebook | say "book", never "e-book"
ban-regex: \bI(?:'?m| am) Frederick\b|\bmy name(?:'?s| is) Frederick\b|\bFrederick Barnes here\b | name intro
ban-regex: \bas (?:a|your) (?:former |retired )?(?:firefighter|fire marshal|fire investigator)\b|\bmy (?:years|time) (?:on|with) the fire (?:department|service)\b | the old firefighter framing
ban-regex: \bmy (?:own )?(?:toaster|parents'? house|mother'?s house|father'?s house|daughter|son|wife|grandkids?)\b | invented personal detail (none approved)
ban-regex: \b(?:a|one|this) (?:homeowner|customer|client|neighbou?r|lady|fella|guy|woman|man) (?:once |of mine |I knew )?(?:asked|told|called|showed|had|ran)\b | invented customer or encounter (claims policy)
ban-regex: \bI'?ve (?:watched|seen|pulled|opened|found|replaced|rewired|walked into|run into)\b | claimed experience (claims policy; say it as the typical case)
ban-regex: \bI (?:still )?(?:see|find|run into|come across)\b[^.!?]{0,40}?\b(?:all the time|every (?:house|home|job|panel|attic|box|basement)|almost every|in most (?:houses|homes|panels))\b | claimed frequency (say "you'll find")
ban-regex: \bevery (?:house|home|panel|attic|basement|job) I'?(?:ve| have)? ?(?:ever )?(?:been in|worked (?:in|on)|opened|walked into|seen)\b | claimed experience
ban-regex: \b(?:worst|best|oldest|scariest|ugliest) \w+(?: \w+)? I(?:'ve| have)? ever (?:opened|seen|found|pulled|wired|worked on)\b | claimed experience
ban-regex: \bI (?:once |ever )(?:opened|saw|found|pulled|wired|walked into|watched)\b | job story
ban-regex: \bI walk(?:ed)? (?:houses|homes|through (?:houses|homes))\b | Frederick's old invented line
ban-regex: \bwhen I was (?:still )?(?:working|on the job|in the trade|an apprentice|on the tools)\b | job story
once-regex: \b(?:thirty-five|35)[- ]years?\b | the tenure, said at most once
ban-regex: \bnext shift\b|\bsee you (?:next time|in the next (?:one|video))\b | the old sign-off ("I'll see you next shift", all 23 old scripts)
once-regex: \bpalm\b | the palm check (his old tic: 14 of 23 old scripts)
once-regex: \btonight\b | tonight (his old tic: 22 of 23 old scripts, 185 uses)
once-regex: \b(?:three|3) in the morning\b | three in the morning (his old tic: 11 of 23)
once-regex: \bnowhere (?:else )?to go\b | the heat has nowhere to go (his old tic: 11 of 23)
once-regex: \b(?:your|a) (?:parents?'?s?|mother'?s|father'?s|mom'?s|dad'?s) (?:house|place|home)\b | a parent's place (his old tic: 17 of 23)
once-regex: \ba straight answer\b | a straight answer (his old CTA line: 10 of 23)
ban-regex: \bjust stop fire\b|\bprevent the burning\b | the old brand and book
ban-regex: \bno (?:rush|deadline|hurry|clock on it)\b|\bno pressure\b|\bwhenever (?:you'?re ready|(?:it )?suits you)\b|\bit'?ll keep\b|\bnobody'?s timing you\b | his old "no rush" family
ban-regex: \bthis (?:one|video)(?:'s| is) for (?:anybody|anyone|everyone|whoever)\b | his old intro line
once-regex: \b(?:smoke )?alarms? (?:past|over|older than) ten years\b|\bten-year (?:alarm|unit|number)\b | his old tic: the ten-year alarm
ban-regex: \bsubscribe\b[^.!?]{0,80}\b(?:keep (?:you|your (?:family|home|house)) safe|(?:prevent|stop) (?:a |the )?fires?|never (?:get )?shocked)\b | subscribe line promising a safety result (offer-rules §5)
ban-regex: \bI(?:'m| am| was)(?: a)? (?:licensed|master|journeyman) electrician\b|\bmy (?:license|licence)\b | credential claim (claims policy)
ban-regex: \bmy (?:own )?(?:house|home|kitchen|basement|garage|truck|van)\b | invented personal detail (none approved)
once-regex: \b(?:as a|I'?m a) retired electrician\b | the background said at most once
ban-regex: \bFrederi(?:c|k)\b|\bFred Barnes\b|(?-i:\bBarns\b) | near-miss name (the core near-miss check misses these)
ban-regex: \bI (?:once )?(?:met|helped|visited|walked through|wired|rewired)\b(?=[^.!?]{0,60}\b(?:house|home|basement|kitchen|neighbou?r|customer|family|lady|man|woman)\b) | invented encounter (claims policy; none approved)
ban-regex: \bnone of (?:this|these|tonight'?s \w+) started with me\b | his old disclaimer
```
