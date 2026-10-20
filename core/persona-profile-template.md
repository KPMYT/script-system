---
name: persona-profile-template
description: The template every channel's persona profile follows. A profile is complete when every field is filled. The workflow refuses to script a channel whose profile is missing or pending.
---

# Persona profile template

Copy this into `personas/[channel-name].md`, fill in every field, then set the channel's status to **ready** in `channels.md`. Anything marked "or" means pick one.

```
PERSONA PROFILE
Channel:
Status: ready | pending
Niche pack:

THE BASICS
Script type: Talking Head | Classic
Voice provider: ElevenLabs | Minimax
Words per minute (optional, for runtime estimates):

THE PERSONA
Name:
Who they are (soft, uncheckable; nothing on the claims policy's "never" list):
How they talk (2-3 lines):
Personal details the narrator may mention (the only ones allowed; e.g. a pet's name, a catchphrase, each with a cap on how often):
Greeting: none | allowed: [what it sounds like]
Closing line: [signature sign-off, one sentence] | callback or next action
Named doubter: none | [the name, and how it's used]
Swearing: as the niche pack | off | [an override]

VOICE SAMPLES
none (use the niche pack's) | [2-3 verbatim transcript excerpts of 60-90 seconds each, with sources]

CTA SETUP
Mid-video CTA: yes | no
End CTA: yes | no
Offer(s), for each one:
  Printed title (exact, used in the markers):
  Spoken as (how the narration says the title):
  Type: e-book | email list | affiliate | subscribe only
  Book text (the offer's full text with page markers, for the book match): [file in personas/books/] | none
  True facts (contents, counts, chapters; the only facts a CTA may use):
  The added-value promise:
  Where to get it (description link, QR code, etc.):
Style and length: [e.g. "two lines: quick aside, one line on the offer, where to get it, back to it"
  or "full pitch: why it exists (real sources only), what's in it, one line tying it to this video,
  plain step-by-step directions, a no-pressure close; no subscribe ask in the mid-video CTA"]
Variants: none | [A, B, ...], chosen: random | assigned by operator
End ask: [the subscribe or engagement ask] | none
```

Optional blocks the workflow and scanner read, if the channel needs them:

````
```inputs
- name | required | what a valid one looks like and how it's checked
```

```scanner
lift: [a hard ban, by phrase]
ban: [phrase] | [label]
allow: [a line the channel says the same way every time, exempt from the copy guard]
```
````
