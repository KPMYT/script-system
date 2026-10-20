# The for-profit pipeline — Hank Hardwood and Dale Oakfield's Workshop

Every woodworking-for-profit request runs these steps in order. Steps 1 and 2 are shown to the operator before anything else is written; nothing gets a brief until the operator picks it. Approved by the operator 2026-10-20.

Best run in Cowork, where Claude can browse Etsy in a real browser.

---

## Step 0: inputs (optional)

The operator may paste competitor videos (titles, screenshots, links). They feed two things:
- **Products:** anything a competitor builds or sells goes into the step 1 list, tagged `from: [video title]`.
- **Title formats:** a title shape not yet in the format bank (core `format-bank-master.md`) is flagged for banking under the next free F-number, through the banking ritual in `SKILL.md` §6.

## Step 1: the product scan

A table of **30 products** by default (or the number the operator asks for), for the named channel (Hank or Dale).

**Research mode (the default).** Claude checks **Etsy** by hand for each candidate product. eBay and Facebook Marketplace are optional extras, used when the operator asks or Etsy is thin.

**What to look for:**
- **Etsy:**
  - the "Bestseller" badge
  - "X people bought this in the past 24 hours"
  - "in X baskets"
  - the shop's total sales count
  - the asking-price range across several listings
- **eBay (optional):** sold prices from the Sold filter.
- **Facebook Marketplace (optional):** asking prices that are visible. Light spot-checks only, never bulk collection.

**Each row of the table:**

| # | Product | Materials and rough cost | Listed at (range) | Sales signals (labelled, dated) | Beginner kit? | Links |
|---|---|---|---|---|---|---|

- **Product:** what it is and what it looks like, in a few words (size, wood, finish, personalization).
- **Materials and rough cost:** the lumber and consumables, with store prices where checked.
- **Listed at:** the asking-price range seen, always worded "listed at".
- **Sales signals:** each one labelled with its platform and the date it was checked, for example "Etsy: Bestseller badge; 14 bought in past 24h (2026-10-21)", or "eBay: sold for $38-52 (5 sales, Oct 2026)".
- **Beginner kit?:** yes, if it needs only the standard kit (tape, square, circular or miter saw, drill, sander, clamps); otherwise, name the extra tool.

**Honesty labels.** Reviews aren't sales, and a shop's total sales aren't one listing's sales. Anything estimated says "estimate". The table shows the evidence and never turns it into a sales figure it doesn't have.

**Fallback: no research.** This applies when the operator asks for it, or when the sites block the checks. The products are invented, marked `INVENTED: no sales evidence`, and the row carries no sales signals and no sales figures.

**After the table:** a short note on which products look strongest and why (the evidence, the cost-to-price gap, beginner fit), plus any seasonal timing.

## Step 2: title and thumbnail-text options

The operator says which products to keep (or "all"). For each kept product:
- **3 to 5 titles:**
  - **Most from the format bank** (core `format-bank-master.md`), each tagged with its F-number and the evidence it rests on, in the core tag style.
  - **1 or 2 new creative ones,** built from the audience psychology (`audience.md`: the lever ranking, the stake factor, the money-motivated slice in §9) and tagged `New`.
  - **Exaggeration is allowed,** including tenure and income claims (operator 2026-10-20). Every dollar figure needs math the brief can show.
- **Thumbnail text for each title:** 2 to 4 words, in the channel's thumbnail pack style (`niche-packs.md`).

**Run as usual:**
- the age/views reading
- the dedup against `produced-log.md` and `dead-list.md`
- the Hank-Dale collision audit (steering §5)
- the channel's register and topic boundaries

The titles are numbered continuously, so the operator can pick by number.

## Step 3: the operator picks

Nothing more is written until the operator picks titles by number.

## Step 4: briefs (picked titles only)

**For woodworking for profit, this spec replaces core `rules-and-specs.md` §4.**

- **A bank of facts to pull from, nothing else.** No structure, no order, no hook, no tone, no wording, no script direction of any kind. The script library decides all of that.
- **Length:** about 500 to 800 words per brief.
- **Layout:** each brief is one spreadsheet cell, with its fact groups separated by " | " and each group starting with its label. For 30 or more briefs, deliver an `.xlsx` file.
- **Fact groups,** in this order, leaving out any group that has nothing real in it:
  1. **Product:** what it is, sizes, variants, personalization options.
  2. **Materials and cost:** each material with store and price where checked; pieces per board; consumables; cost per piece (rounded up).
  3. **Price evidence:** "listed at" ranges and any "sold for" prices, each with platform and date.
  4. **Demand signals:** what the scan found, labelled as in step 1.
  5. **Who buys it and when:** occasions, seasons, gift angles, where it sells best (Etsy, local, craft fairs).
  6. **The viewer:** the pain points and emotions this product touches for the channel's viewer (from `audience.md`), stated as facts about the audience.
  7. **Title support:** the math behind every number or claim in the title (units × price − cost − fees).
  8. **Tools and difficulty:** standard kit or not, and the alternatives for anything beyond it.
  9. **Safety facts:** the ones that apply (`audience.md` §7; food-safe finish, kickback and so on).
  10. **The reference video,** if there is one: its title, views, angle and structure, stated as facts (never its transcript).

## Step 5 (optional): the research pack

On request, for each picked title, Claude fills in the woodworking research-pack template from the `woodworking-scripts` skill (`references/research-pack-template.md`), including the verification pass and a "Verified on" date. The result can go straight into START in the script skill.

**This needs the new `woodworking-scripts` skill installed.** The old single-file version has no template.
