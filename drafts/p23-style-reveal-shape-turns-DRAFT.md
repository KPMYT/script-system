# P23 draft: style, no early answers, no one-template tips, the voice's turns back

**Status:** DRAFT, nothing applied. The wording below goes into the two style pages (`personas/scarlett-starling.md`, `personas/diane-de-chambray.md`) and `style-scripts/check.py` once the operator says yes. These are the library's P21 style pages: the account still runs the 2026-10-31 style skills, so nothing reaches the VAs until the style skills are rebuilt and uploaded.

**Where it comes from:** the style review (`studies/recent-uploads-2026-11-16/`) and the operator's answers, 2026-11-17:
- "i dont care if makeup tips creep in"
- "we cant have answers be given away early"
- "we dont want this: Every tip runs one template."
- "The voice lost its turns. this is not good"

## 1. Makeup tips: nothing to change

The P21 style pages don't ban makeup tips inside a fashion or hair video: the ban was in the 2026-10-31 account rules. Once P21 style is uploaded, tips like Diane's "skin before makeup" are fine. Two lines stay:
- **NOT READY** for a title that is wholly about makeup or skincare (pack step 1: "that waits for its own pack")
- **Diane's book line** can't claim makeup lessons, because the book has none (a fact, not a style rule)

Question 1 below asks whether to drop the first of these too.

## 2. No answer given away early (both pages)

**Goes right after "Hold the reveal", in the hook section:**

> **Never give an answer away early** (operator, 2026-11-17: "we cant have answers be given away early"). Each tip's answer (the piece, the cut, the color, the swap, the rule) is said only inside that tip, after she knows why the old way fails.
> - **The hook names no tip,** not even its topic ("It's the color, the hem, the shoe" is three answers early), and never states the rule the whole video turns on.
> - **In a "one mistake" video,** show the mistake and what it costs her, never the rule that fixes it. Each swap reveals its own piece of the answer.
> - **The signpost names the question, not the answer:** "Number one is the earring most women reach for first", never "Number one, a slim gold hoop". The piece is named once she knows why the old one fails.
> - **A bridge hands on the next tip's feeling or problem,** never its answer ("Number six is the shoe" in a bridge gives it away).

**The checker (`style-scripts/check.py`):** fails the opening (before item one) on "the rule", "here is the rule", "fixes all of it", "the answer is" and "the secret is". The signposts and bridges stay by eye and for the judge, since a program can't tell an answer from a question.

## 3. No one-template tips (both pages)

**Replaces the bullet "Each item takes its own shape. Don't end each on the same kind of line; never announce a check":**

> **No template** (operator, 2026-11-17: "we dont want this: Every tip runs one template"). Build each tip from what that tip needs, not from a fixed list of beats:
> - **Open them differently:** one on her mirror, one on a moment she has lived, one on a test she can run, one on a question to her.
> - **End them differently:** one on the compliment, one on a verdict, one on permission, one on what she'll see tomorrow.
> - **Never say a beat's name as a line:** "the rule I always give", "my rule", "that's the rule", "the rule is ... the result is", "here's why it works", "So, which do you choose?". A design-years line only where it truly explains the point, never as a slot every tip fills.
> - **Any line or opener used in three tips is a template:** rewrite two of them.
> - **Tips differ in length too:** the one that matters most gets the most room.
>
> Never announce a check ("your check is").

**The checker:**
- fails when any four-word run (common phrases and the title's own words left out) turns up in three or more different tips. That catches "the rule I always give", "the result is that" and "you know the moment".
- fails "my rule", "the rule I always give" or "that's the rule" said more than twice in a script.

## 4. The voice's turns (both pages)

**Replaces the line "Natural sentences: often a longer one with the reason, then a short verdict; 'but' where the thought turns" (Diane's: "Her sentences: longer storytelling sentences with a short verdict; 'but' where the thought turns"):**

> **Turn the thought** (operator, 2026-11-17: "The voice lost its turns. this is not good"). Most tips turn at least once:
> - what she was told or believes, then "but" the truth
> - the obvious fix, then why it fails
> - a question to her, answered at once
>
> "But" carries most turns ("You'd think a longer coat adds bulk. But it does the opposite."), with "yet", "instead" and "except" now and then. A tip that only states rules, verdict after verdict, is flat: turn it. Keep her sentence rhythm: often a longer one with the reason, then a short verdict. Never add a "but" to a sentence that doesn't turn.

**The checker:** fails when "but" runs under 2.5 per 1,000 spoken words, with the message "turn real thoughts (belief, then the truth); never insert a 'but'". It also reports the question count.

The evidence for the floor (caption counts per 1,000 words):

| Group | "but" per 1,000 |
|---|---|
| The flat scripts | 0.4 to 1.3 (Scarlett's three newest, Diane's three newest) |
| The scripts the review ranked best | 2.8 to 4.9 (Scarlett's coats and 80+, Diane's earrings and over-70) |
| The 11-05 uploads | about 5 |

The limit is a floor, not a target. P21's lesson was that writers treat a limit as a target, so the page wording asks for real turns, and the floor only catches the flat cases.

## 5. Also proposed: the plumbing fixes, carried to style (each needs its own yes)

The review found the same faults the plumbing review did.

| # | Change | Why (from the review) |
|---|---|---|
| a | **One reason to stay to the end,** paid by a strong last tip; the "if you remember only one, make it this" flag at two-thirds and "best first" go | All ten videos tell her the best is over at 60 to 72%, and the tips after it get shorter. Diane's 80+ video calls its last tip "the smallest thing on this list" |
| b | **The book once, short and general:** what it goes deeper on and why, who it's for, where; about 35 to 60 words; no Way, Secret, chapter or page numbers; no end reminder (Talking Head: one marker block) | Said twice with 2 to 5 numbers in all ten; "who it's for" in none |
| c | **The comment ask quick and easy, a fresh question each video** | Scarlett asked "the piece you've kept longest" in 4 of 5 |
| d | **Design-career lines:** at most one or two, and only where they explain the point | 5 to 9 a video, inventing backstory |
| e | **Length:** 14 minutes the floor at her real speed, up to 25 when the brief has the meat; a thin brief filled out, never NOT READY | as plumbing |
| f | **The hook shorter:** back to about 110 words, item one by about 45 seconds, instead of P21's six beats at 100 to 160 words | The three newest on each channel ran the longer hook at about 160 words, item one at 0:55 to 0:58, and were the flattest of each batch |

## 6. Questions for the operator ("1 yes, 2 no...")

1. **Makeup-only titles:** keep NOT READY for a title wholly about makeup or skincare, or let those through too?
2. **Apply sections 2, 3 and 4** (no early answers, no template, the turns) to both style pages and the checker?
3. **Section 5, a to f:** which of the plumbing fixes carry over to style?
4. **The template and turns checks for plumbing too?** The Roger review found the same drumbeat item endings and low "but" counts on plumbing.
5. **After applying:** a test round (one Scarlett and one Diane script on the new pages, judged against their published videos), then rebuild and upload the style skills?
