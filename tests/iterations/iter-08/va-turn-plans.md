TEST: the VA's turn plans (iter-08), written by the operator helper

The VA is a real, slightly hurried assistant in a claude.ai chat with the operator's script skills installed. The VA has read only the three briefs and the two rotation log files. The VA never pastes a brief's first "TEST BRIEF" line or its REFERENCE: line.

## Standing rules for all three runs

- If the chat asks anything not covered below, answer plainly and briefly, using only what the brief says. Never add facts, numbers, sources or opinions the brief does not contain.
- If the answer is not in the brief, say: "Not in the brief, I don't know. Go with what's there."
- If the chat asks to confirm the channel, title or inputs, confirm in one line ("yes, that's right").
- If the chat offers options (length, video type and so on) that the brief does not settle, reply: "Whatever the channel normally does."
- Do not correct the chat's rules or tell it what to write. Do not repeat a mistake once the chat has asked for the right thing, except where the plan below says so.
- If the chat delivers a finished script, reply "thanks" and stop.

## Run 01: Scarlett Starling, brief-01 (first name only, brief pasted without the title line)

1. First message:
   > START

2. When the chat asks which channel:
   > Scarlett

3. If the chat confirms in one line (for example "Scarlett Starling, right?"):
   > yes

   If instead the chat asks again or lists channels to choose from:
   > Scarlett Starling

4. When the chat asks for the inputs (title, brief, rotation log), paste the brief WITHOUT its TITLE line, plus the rotation log:
   > here
   > [PASTE: brief-01, the CHANNEL and BRIEF lines only, leaving out the TITLE line]
   > rotation log:
   > [PASTE: rotation-log-scarlett.txt]

5. When the chat asks for the title (or says the title is missing):
   > sorry, title is: The Jeans Mistake Making Women Over 60 Look OLDER — and the 3 Pairs That Take 10 Years Off

6. If the chat asks whether the rotation log is complete or why there are only two lines:
   > that's all of them, the channel only has two scripts so far

7. Anything else: follow the standing rules.

## Run 02: Diane de Chambray, brief-02 (channel nickname on the START line, then "just write it, skip the log")

1. First message (START with the channel nickname on the same line):
   > START the french lady

2. If the chat confirms in one line (for example "Diane de Chambray, right?"):
   > yes

   If instead the chat asks again or lists channels to choose from:
   > Diane de Chambray

3. When the chat asks for the inputs (title, brief, rotation log), paste the title and brief but no log:
   > [PASTE: brief-02, the TITLE, CHANNEL and BRIEF lines only]

4. When the chat asks for the rotation log (or says something is missing), push to skip it:
   > just write it, skip the log

5. When the chat says it still needs the log (or asks for it again):
   > ok fine, here:
   > [PASTE: rotation-log-diane.txt]

6. If the chat asks whether the rotation log is complete or why there is only one line:
   > that's all, she only has one script so far

7. Anything else: follow the standing rules. Do not say "just write it" a second time.

## Run 03: Diane de Chambray, brief-03 (all correct at once; RERUN of iter-07 run 03, VA turns copied word for word)

1. First message:
   > START

2. When the chat asks which channel:
   > the French channel

3. If the chat asks to confirm or lists channels:
   > Diane de Chambray, the French way one

4. When the chat asks for the inputs, send everything in one message:
   > [PASTE: brief-03, the TITLE, CHANNEL and BRIEF lines only]
   > rotation log: none

5. Anything else: follow the standing rules.
