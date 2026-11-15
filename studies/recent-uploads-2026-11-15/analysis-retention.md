# Stage 2: Roger's last five videos, the retention graphs

Read after stage 1 (`analysis-scripts.md`) was written and committed. Section 4 checks the seven predictions stage 1 wrote down beforehand.

**The data:** the operator's YouTube Studio "Audience retention" exports, one folder per video in `retention/<videoId>/` (copied unchanged from the zips). Each holds 100 points (0% to 99% of the video) for all viewers, plus splits by subscribers, new and returning, and new, casual and regular viewers. All traffic is organic: the ad files are empty.

**How it was read:** each point was turned into seconds using the video's length (one point is 7.7 to 9.1 seconds), then matched to the caption line spoken there.

**Cautions:**
- **Small and early.** The exports cover each video's first 2 to 8 days, at 1,000 to 5,100 views. Once the curve is under about 20%, a few dozen viewers make each point, so a single point can wobble by one or two. Only patterns that show across several points, or across several videos, are reported.
- **One point is about 8 seconds,** so a drop can only be placed within a sentence or two.
- **"Compared to other videos"** is Studio's own comparison with videos of similar length (below zero means below them). It's quoted as Studio gives it.

## 1. The five curves

| # | Video | Still watching at 0:30 | at 1:00 | at 25% | at 50% | at 95% | Average share watched | Studio comparison at the start |
|---|---|---|---|---|---|---|---|---|
| 1 | Plunge (15:12) | 55% | 35% | 22% | 16% | 10% | about 19% (about 2:55) | -22 |
| 2 | Dishwasher tablet (12:54) | 67% | 42% | 30% | 17% | 10% | about 24% (about 3:02) | -15 |
| 3 | Toilet bowl (13:33) | 59% | 42% | 29% | 19% | 10% | about 24% (about 3:15) | -15 |
| 4 | Peroxide (13:13) | 60% | 43% | 32% | 25% | 12% | about 27% (about 3:30) | -10 |
| 5 | Washing machine (14:23) | 52% | 34% | 24% | 17% | 11% | about 21% (about 3:01) | -11 |

**The shape is the same on all five:** a cliff in the first minute (57% to 66% of viewers gone by 1:00), a slow bleed through the body (1.4 to 2.3 points a minute), a flat end where about one in ten watch to the comment ask, and a drop at the book line every time.

**Ranking by retention:** peroxide, then toilet and dishwasher (close), then washing machine, then plunge. Stage 1 ranked the scripts peroxide, toilet, dishwasher, plunge, washing machine. The top three match, and the bottom two swap.

## 2. Where viewers leave

### The first minute: one leak in two parts

| # | 0:00 to about 0:25 | about 0:25 to 0:30 (a lull) | about 0:30 to 0:45 (a second drop) | What's said in the second drop |
|---|---|---|---|---|
| 1 | 97 to 55 | 55 to 50 | 50 to 40 | "I've been at this 45 years, and there are nine things to get right before that plunger touches the sink. Everything here is yours until the clog is past the bend under the sink. Number one, block the overflow." |
| 2 | 96 to 69 | 69 to 67 | 67 to 49 (0:30 to 0:46) | "It won't clear a solid clog, and it won't touch hard water crust. Here are the seven jobs I'd give one ... Number one, you finish the dishes after a big Sunday dinner" |
| 3 | 96 to 65 | 65 to 59 | 59 to 45 (0:32 to 0:40) | "So this isn't on you. But it ends today with a cheap powder from the canning aisle, and every step of it is yours to do. Step one, drain the bowl" |
| 4 | 94 to 64 | 64 to 60 | 60 to 45 (0:31 to 0:47) | "Everything here is yours to do. The one call in this video is a clog, which peroxide was never going to fix. Five ways people kill this stuff ... The first mistake is the bottle itself." |
| 5 | 96 to 52 | 52 to 47 | 47 to 35 (0:34 to 0:43) | "Nearly all of this is yours. The one machine that isn't is packed so solid the drum has to come out, and the third cycle tells you which you've got. Step one" |

- **Part one, 0:00 to about 0:25:** 24 to 44 points go in every video. Some of this is normal (wrong click, the thumbnail didn't match). It's heaviest in the two videos whose first two sentences give the whole fix away: washing machine 87 to 52 between 0:08 and 0:25 (35 points), and plunge 84 to 55 between 0:09 and 0:27 (29 points). The other three lost 24 to 27 points over the same stretch.
- **Part two, about 0:30 to 0:45:** after a short lull, every curve drops again, by 10 to 18 points, in the last 15 seconds of the hook. **In all five,** that stretch holds the same two things:
  - the line saying what's yours and where it becomes a call ("Everything here is yours until...", "It won't clear a solid clog", "The one machine that isn't...")
  - the count and the switch into item one
- **What this can't separate:** the drop could come from the limit line (it tells some viewers "this isn't for your problem"), or from the hook ending and the list beginning, or from both. The order is the same in all five, so the data can't pull them apart. Only a test can: the same kind of title, once with the limit line in the hook and once with it moved into the step where the call comes.

### The body: steady, with no step at item changes

- **After 1:00, the loss is slow and smooth:** 1.4 (plunge) to 2.3 (dishwasher) points a minute.
- **Changing items costs nothing.** Around every "Number N", "Step N" or "The fourth mistake" after item one, the curve moves under about 1 point either way (within noise) on all five. Stage 1's praise for the bridges between items holds.
- **Item one is the exception in the plunge video** (prediction 2, below).
- **Small rises** show viewers skipping forward or rewatching to find the how-to:
  - peroxide 5:48, +3 points, just before "Peroxide is slow. It needs a sit. ... 30 minutes is the floor. Overnight is better." (the "how long" answer)
  - plunge 9:34, +2.4, the stopper
  - plunge 7:36, +1.8, the cup plunger
  - toilet 1:29, +1.0, the valve
  - washing machine 3:44, +1.0, the filter

  That's what viewers come back for: the concrete instruction.

### The book line: the biggest drop after the first minute, in all five

| # | Book line | Still watching before, then after | Loss rate against the body's | Share of the viewers still there who left |
|---|---|---|---|---|
| 1 | 4:53 to 5:36 (32%) | 18.9 to 14.9 | 2.9 times | 21% |
| 2 | 6:09 to 6:39 (48%) | 20.0 to 14.8 | 3.0 times | 26% |
| 3 | 7:58 to 8:27 (59%) | 18.7 to 14.8 | 2.5 times | 21% |
| 4 | 7:08 to 7:37 (54%) | 24.2 to 15.3 | **6.6 times** | **37%** |
| 5 | 7:57 to 8:28 (55%) | 16.0 to 12.7 | 2.8 times | 21% |

(Before and after are taken 8 seconds either side of the line.)

- **About one viewer in five still watching leaves at the book line,** wherever it sits. The early spot (plunge, 32%) cost the same share as the late ones (48% to 59%). **The spot matters less than what's said.**
- **The peroxide line cost almost twice as much as the others:** 37% of the viewers still there. It's the one stage 1 marked as the weakest tie: a video about stains sends them to "Fixes 37 through 42, printed pages 48 through 51. The running toilet, the flapper, the tank level". The steepest points are on the fix and page numbers themselves (7:16 to 7:24).
- **The toilet line was the best match** ("a chart that takes a symptom like a weak flush ... the rim holes among them"). It lost at the usual rate, so a good match didn't win viewers, but a bad one cost a lot.
- **In absolute terms the book line costs 3 to 9 points** of the starting audience. The first minute costs 57 to 66.

### The ending: holds well

From 90% to 97%, every curve is flat (for example, the toilet video stays at about 10% from 90% to 97%). The last 2% drop of 1 to 2 points is the end screen. The viewers who reach the "one thing for tonight" stay for the book reminder and the comment ask.

## 3. Who watches

| # | At 1:00, subscribers against everyone else | At 95%, subscribers against everyone else | Regular viewers at 95% | New viewers at 50% |
|---|---|---|---|---|
| 1 Plunge | **31 against 40** | **6 against 13** | 12 | 18 |
| 2 Dishwasher | 49 against 40 | 15 against 8 | 14 | 9 |
| 3 Toilet | 51 against 37 | 17 against 6 | 19 | 11 |
| 4 Peroxide | 47 against 40 | 15 against 10 | 18 | 16 |
| 5 Washing machine | 36 against 32 | 12 against 8 | 11 | 8 |

- **On four videos, subscribers stay longer, as they should.** On the plunge video it's the reverse: subscribers left faster than strangers and finished at half their rate.
- **A reading of the plunge result:** the channel has already covered unclogging many times in the past month (among them "How to Unclog a Drain For Beginners", "$0.01 vs $1000 Drain Unclogging Tricks", "These 4 Liquids Will Clear EVERY Clog", "How To CLEAR Every Clog in Your House", "Pouring Drain Cleaner Is NOT Saving You Money" the same day). Subscribers have heard the plunger advice before. That's an ideation question (topic rotation), not a script one.
- **New viewers mostly don't reach the middle** (8% to 18% at 50%). The channel keeps people who already know Roger.

## 4. Stage 1's seven predictions, checked

| # | Stage 1 prediction | What the graphs show | Verdict |
|---|---|---|---|
| 1 | Hooks that give the fix away at 0:00 (plunge, toilet) lose more by 0:30 than those that hold it (dishwasher, peroxide) | At 0:30: dishwasher 67 and peroxide 60 (held); toilet 59 (half); plunge 55 and washing machine 52 (both name the whole fix in the first two sentences). The two full give-aways lost the most in the first 25 seconds (29 and 35 points against 24 to 27). | **Supported,** on five videos with different topics. A test would make it firm |
| 2 | The plunge video dips at 0:45, where item one repeats the hook | 41 to 33 between 0:54 and 1:12, while the overflow is explained again: twice the loss of item one's first 25 seconds on any other video (toilet 45 to 41, peroxide 45 to 43, washing machine 35 to 34) | **Supported** |
| 3 | A drop at each book line; the 32% spot against the 48% to 59% spots | A drop on all five, 2.5 to 6.6 times the body's rate. The 32% spot cost the same share as the late ones. The weakest tie (peroxide) cost the most | **Supported;** the place doesn't matter, the match does |
| 4 | Washing machine step one (0:49 to 1:50, the long explanation) is steeper than other openings | 34 to 30 over that minute, no worse than the others (35 to 28, 40 to 35, 41 to 36, 43 to 38). Its viewers were lost earlier, at 0:08 to 0:43 | **Not supported:** the explanation wasn't the problem, the hook was |
| 5 | The two recaps lose viewers before the comment ask | Dishwasher 12:11 and peroxide 11:57 are flat (about 10% and 12%) | **Not supported:** at that point only the loyal remain. Still a rule break, but a cheap one |
| 6 | Price-heavy stretches in the washing machine video dip | Nothing beyond noise around 5:06 or 11:51 | **Not supported** |
| 7 | Viewers drop at each "Number N" | Item changes are flat after item one | **Not supported** (good news: the bridges work) |

## 5. What the graphs add to stage 1

1. **The first minute is where the channel loses its audience,** not the body, the book line or the ending. Of every 100 who start, about 60 are gone by 1:00. Only about 25 to 30 more leave in the 12 to 14 minutes after, and about 10 stay to the end. Stage 1 marked the hooks as fixed against the 11-05 rules, and they are. But the rules themselves (first item by about 45 seconds, the honest limit, the count) produce a hook that loses 10 to 18 points in its last 15 seconds, every time.
2. **Two candidate causes, both in the hook:**
   - giving the whole fix away in the first two sentences (prediction 1)
   - the limit line and the count just before item one, whose effect can't be separated with this data
   
   Both are on the current page as guidance ("the first sentence makes the point: ... the fix or product itself, named outright"; "Where the job stops being theirs"). They aren't locked decisions in HANDOFF §3, but they came from the operator's approved P21 page, so any change needs the operator's yes.
3. **The book line:** the match matters more than the place. Fix and page numbers read out for a chapter that doesn't fit the video cost 37% of the viewers still there.
4. **The body and the ending work.** The bridges hold viewers through every item change, and nearly everyone who reaches the last minute stays to the comment ask.
5. **Topic repetition shows up with subscribers** (the plunge video). That's ideation, not script.

Findings only: nothing in the library changed. Possible tests and rule changes are listed for the operator in chat.
