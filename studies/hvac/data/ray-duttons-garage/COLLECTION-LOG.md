# Collection log — Ray Dutton's Garage (faceless persona, structure only)

Collected 2026-10-27 by collector helper D, following `studies/hvac/study-brief.md`. NexLev MCP tools only, no web search. Rows 28–33 of `inputs/videos.md`.

## Channel

- Channel ID UCvcKEgZcY9ZgEULZouaNAOA · @RayDuttonsGarage · https://www.youtube.com/channel/UCvcKEgZcY9ZgEULZouaNAOA
- `youtube_channel_videos` meta: 32.1K subscribers; videosCount 31; about text starts "Hi, I'm Ray Dutton, a retired HVAC pro. I show homeowners how to keep their furnace, heat pump and air conditioner running without getting robbed. For twenty..."
- `check_faceless_channel` (cached 2026-10-27 03:36 UTC): isFaceless=false, confidence 0.99, format "tutorial", tags how to / education / home repair / personal finance, Trends keyword "hvac repair". The selection marks the channel F (faceless AI or persona). The flag suggests a presenter figure is on screen (possibly an AI avatar); the videos were not viewed, so this is not verified.

## Videos

| Row | Video ID | Type | Upload | Duration | Views | Likes | Normal | × normal | Segments | Comments (top + newest) |
|---|---|---|---|---|---|---|---|---|---|---|
| 28 | K2jCz3D5z_0 | habit list | 2026-08-18 | 14:27 | 1,130,705 | 13,395 | 8,345 | 135.49 | 341 | 32 + 20 (927 shown) |
| 29 | qbWN3OViWxQ | mistakes list | 2026-07-31 | 14:05 | 589,617 | 14,609 | 8,345 | 70.66 | 351 | 25 + 20 (1K shown) |
| 30 | dOZ-8__G4uU | seasonal checklist | 2026-09-11 | 11:49 | 1,234,081 | 7,295 | 8,345 | 147.88 | 313 | 43 + 20 (476 shown) |
| 31 | fHAlfm21vYw | seasonal checklist | 2026-09-14 | 14:42 | 949,093 | 9,196 | 8,345 | 113.73 | 350 | 31 + 20 (245 shown) |
| 32 | _ZgVjFpBnQA | product villain / myth-bust | 2026-08-02 | 15:10 | 776,933 | 14,039 | 8,345 | 93.10 | 367 | 22 + 20 (1.1K shown) |
| 33 | UdyqMC1GVxQ | doing it wrong | 2026-08-28 | 13:30 | 140,875 | 1,427 | 8,345 | 16.88 | 310 | 20 + 20 (68 shown) |

All views, likes, dates and durations from `youtube_video_details` on 2026-10-27. All descriptions open with the same two lines: "🔧 Everything I learned fixing HVAC for 25 years, in one plain-English book. 📘 THE HVAC SURVIVAL GUIDE - get it here: https://raydutton.com". Every description lists chapters and has a comment ask ("I read every one").

## Normal = 8,345

Median of exact views of the 15 most recent long-form uploads (≥ 5:00, Videos tab, so no Shorts) published at least 7 days before 2026-10-27. Source: `youtube_channel_videos` sort=newest, page 1 (30 items). Excluded as under 7 days old: AglSKzOY2E8 (1 day), j2OYzAHipok (3 days), vHVITBbPcQI (5 days).

Listing views are rounded above 1,000 (for example "8.3K"), so exact counts were pulled with `youtube_video_details` for the median video and the four newest. The gaps either side of the median (6.5K below, 11K above) are wider than the rounding, so the median is the exact count of Wn7lGvsvpfY.

| # | Video ID | Upload | Length | Views |
|---|---|---|---|---|
| 1 | LhrgMgcHw_A | 2026-10-16 | 11:57 | 19,980 (exact) |
| 2 | MYzFE1UsUEI | 2026-10-14 | 13:42 | 48,303 (exact) |
| 3 | 1NsI2Juk-C4 | 2026-10-11 | 11:11 | 4,551 (exact) |
| 4 | V8MTmzrxN2g | 2026-10-10 | 12:04 | 2,330 (exact) |
| 5 | YYpatfw54S4 | ~2 weeks | 9:25 | 5.5K (listing) |
| 6 | H0MBgMMzmyg | ~3 weeks | 12:17 | 263K |
| 7 | U_pHy5xLGTA | ~3 weeks | 13:37 | 11K |
| 8 | MoB-obRdbro | ~3 weeks | 11:56 | 6.5K |
| 9 | GKizclJLSq0 | ~3 weeks | 13:15 | 156K |
| 10 | Wdu-y_wkowI | ~4 weeks | 12:20 | 1.9K |
| 11 | 2Z3Z9RoH6t8 | ~4 weeks | 13:32 | 5.5K |
| 12 | **Wn7lGvsvpfY** | 2026-09-26 | 11:35 | **8,345 (exact) = median** |
| 13 | 1UQFw6XKlR8 | ~1 month | 11:54 | 17K |
| 14 | JVClcu4P6d0 | ~1 month | 13:06 | 5.1K |
| 15 | 9MbOdR2x0N8 | ~1 month | 13:26 | 127K |

16th, outside the window: aspLlFv3Ij0 (14:05, 11K). None of the six study videos fall in the window: the closest, fHAlfm21vYw and dOZ-8__G4uU, are positions 22 and 23 in the listing.

## Method

1. `youtube_video_details` for the six videos.
2. `get_bulk_video_transcripts` in two calls (2 + 4 videos). All six succeeded, English auto-generated tracks, written as `[m:ss] text`, one line per segment.
3. Earlier pulls of two of these videos exist in `niche-research/studies/hvac/data/raw/ray-sources-2026-10-26/transcripts/` (tx_ray2.txt = qbWN3OViWxQ, tx_ray3.txt = _ZgVjFpBnQA). They are a single block of plain text with no timestamps or line breaks. After normalising case and punctuation, the word sequences are identical to the fresh pulls (2,328 and 2,311 words; 0 differences). The only difference is the format.
4. `youtube_video_comments`, top-level only, text and likes only. Top sort: page 1 (20), then the continuation pages. New unique comments per page: K2j p2 12, p3 0, p4 0; qbWN p2 5, p3 0; dOZ p2 15, p3 8; fHA p2 8, p3 3; _Zg p2 2, p3 0; Udy p2 0 (exact repeat of p1, p3 not fetched). Newest sort: one page of 20 each. No comment by the channel owner appeared anywhere (authorIsChannelOwner false throughout), so nothing is marked [OWNER].
5. `check_faceless_channel` once.
6. Notes written from the transcripts and comments: `notes/ray-duttons-garage__<id>.md`.

## Failures and gaps

- None of the NexLev calls failed.
- The top-comment lists stop at 20–43 unique per video, not ~60, because the continuation pages repeat earlier pages (see step 4).
- The notes run 560–720 words (counted with headings and timestamps), above the 300–400 target, because every section in the brief is filled in.

## How Ray does his CTA (the e-book, "The HVAC Survival Guide")

- **Description, all six:** the same two opening lines naming the book and https://raydutton.com, above the summary.
- **In the narration, four of six** (K2j, dOZ, fHA, Udy): one short plug, 14–21% of the way in, inside or right after item 1. It opens with a "quick" aside, names the guide without its title, gives the URL, says "no pressure", then returns ("All right, back to it").
  - K2jCz3D5z_0 [2:01]: "Quick thing before we move on. All of this, cooling and heating both, the price math and the exact questions to ask, it's in one plain guide over at raydutton.com. It's there if you want it, no pressure."
  - dOZ-8__G4uU [2:24]: "Quick word while we are out here, then right back to it. Just about everything I picked up doing this work… I put down in plain writing in a short guide over at raydutton.com. It is there if you want it, no pressure either way."
  - fHAlfm21vYw [1:59]: "Quick one before we keep going. Every fix in this video, and all of it, including the whole heating section, is written down in one plain guide over at raydutton.com. No pressure, it sits there if you want it."
  - UdyqMC1GVxQ [2:50]: "Quick thing before we go further, and it fits right here. All of this, cooling and heating both, the cheap fixes and the exact way to spot the expensive stuff before somebody sells it to you, it's in one plain guide over at raydutton.com. It's there if you want it, no pressure."
- **No plug in the narration** in qbWN3OViWxQ and _ZgVjFpBnQA (the two oldest, July 31 and August 2); there the book appears only in the description.
- The narration never says the title "The HVAC Survival Guide", a price or "e-book"; it is always "one plain guide" / "a short guide".
- **End CTAs, all six:** a comment ask with a specific question (thermostat setting and bill; cover/power on or off and unit age; state, furnace age and which mistake; filter and price; state and unit age), always "I read every one" or "I read every single one"; then a subscribe ask tied to having been saved ("if this just saved you a service call", five of six); then the sign-off. Three videos tease the next video by topic (qbWN → filters, _Zg → "the house goes dead silent at 100 degrees", Udy "I put one of these out every few days").
- One comment shows the website being visited: "Headed to the Ray Dutton website now." (K2jCz3D5z_0 newest, 0 likes).

## Catchphrases repeated across the six videos

| Phrase | Videos and timestamps |
|---|---|
| "I'm Ray Dutton. Keep your cool and I'll see you in the next one." (dOZ: "I am Ray Dutton. Keep your cool and I will see you in the next one.") | all 6: K2j [14:23], qbWN [14:00], dOZ [11:43], fHA [14:35], _Zg [15:03], Udy [13:26] |
| "25 years…" credential in the first minute ("25 years I did this", "25 years in attics, crawl spaces") | all 6: K2j [0:49], qbWN [0:25], dOZ [0:39], fHA [0:29], _Zg [0:47], Udy [0:43] |
| "for the same companies…" (that mail you the bill / I'm about to tell you about) | 4: K2j [0:53], qbWN [0:28], dOZ [0:44], fHA [0:34] |
| "I read every one" / "I read every single one" | 5: K2j [14:15], qbWN [13:18], dOZ [11:27], fHA [14:29], _Zg [14:38] (Udy: "because I read them") |
| "Do me one favor" / "Do me a favor" / "do something for me" before the comment ask | 4: K2j [14:08], dOZ [11:15], _Zg [14:28], Udy [12:59] |
| "if this (just) saved you…" + subscribe | 5: qbWN [13:31], dOZ [11:33], fHA [14:32], _Zg [14:43], Udy [13:11] |
| "I'll be straight with you" / "honest with you" / "I'll be fair" before a caveat | 6: K2j [9:35], qbWN [4:45] and [8:09], dOZ [8:43], _Zg [10:56], Udy [4:09] |
| "the way I always am in this garage" / "that's how we do things in this garage" | 2: dOZ [2:04], qbWN [4:49] |
| "I'm going to argue against myself for a minute" | 2: fHA [6:36], _Zg [6:48] |
| "None of this is hidden because it's complicated. It's hidden because…" (_Zg: "a secret because") | 4: qbWN [12:42], fHA [14:12], _Zg [13:49], Udy [12:23] |
| "Now, stop right there" / "Now, stop and look at what we've got" (mid-video interlude) | 3: dOZ [5:25], fHA [4:31], qbWN [3:53] ("Stop right there. Two mistakes in…") |
| "one plain guide over at raydutton.com… no pressure" | 4 (see the CTA section) |

## Check of my own work (2026-10-27)

- **Meta re-check:** `youtube_video_details` called again for qbWN3OViWxQ. Duration 845 s and upload date 2026-07-31 match meta.md. Views 589,606 against 589,617 in meta.md (−11, a small YouTube count adjustment between the two calls); likes 14,609 match.
- **Quote re-check:** three lines from the notes compared with transcript.txt by hand:
  - qbWN3OViWxQ [7:33] "topping it off without finding that leak isn't a repair, it's rent." Transcript: "[7:33] And topping it off without finding that" / "[7:35] leak isn't a repair, it's rent." Matches.
  - fHAlfm21vYw [5:18] "a furnace is a hairdryer the size of a refrigerator." Transcript: "[5:18] because a furnace is a hairdryer the" / "[5:20] size of a refrigerator." Matches.
  - dOZ-8__G4uU [3:43] "to a mouse looking for somewhere to spend the winter, that is a mansion." Matches the transcript lines at [3:43]–[3:48].
- Also checked by script: every transcript quote in the six notes was matched against the transcript within its timestamp window, and timestamps were moved to the exact segment where each quote starts. Every quoted comment was matched against comments.md, likes included (0 misses).
