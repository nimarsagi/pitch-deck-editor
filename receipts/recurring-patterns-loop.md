---
file-type: receipt
workspace: pitch-deck-editor
demonstrates: memory/recurring-patterns.md — the propose → approve → append loop
status: reconstruction, not a live capture (see "What this is" below)
built: 2026-07-23
---

# Receipt — the recurring-patterns loop, worked

**What this is.** A worked demonstration that the propose → approve → append loop in
`memory/recurring-patterns.md` produces a correct, gate-compliant entry when exercised.
It is **not** a screenshot of the loop firing live — the four calibration passes it
draws on (`output/critique-pass-1-{airbnb,coinbase,immediately,snapchat}.md`) were run
before `skills/critique-pass.md` was wired to read the memory file during Step 2.5, and
before Step 5's proposal habit was in place. None of those four files contains a
proposal. This receipt is the honest fix for that: it applies the actual governance
rule in `memory/recurring-patterns.md` to the actual scorecard data already committed
in those four files, in the order they were run, and shows what Step 5 should have
surfaced at the point the rule's own trigger condition — *a pattern recurring across
decks* — was first met.

**Why it lives here and not in `memory/`.** `memory/recurring-patterns.md` is what a
clone of this workspace inherits. If this reconstruction were appended there, everyone
who runs the editor would start with someone else's calibration patterns baked in,
which defeats the point of a per-deployment cross-deck memory. The live file stays
`(none yet)`. This receipt is proof the mechanism works, kept separate from the
mechanism's actual state.

---

## The timeline as it actually happened

All four passes ran 2026-07-22, same session, same declared domain (`icm-ai-startups`
config loaded, though none of the four decks are AI-startup decks — see each file's
own provenance note).

| Pass | Deck | Room | Relevant scorecard line |
|---|---|---|---|
| 1 | airbnb-seed-2008 | investor | B8 Ask **0/3** — "no ask" |
| 2 | coinbase-zlides-reconstruction | investor | B8 Ask **0/3** — ends on a URL |
| 3 | immediately-sales-2015 | sales | B5 Proof specificity **0/3** — gate fired |
| 4 | snapchat-advertiser-2015 | sales | B7 Call to action **0/3** — gate fired |

Two shapes recur, each one visible from pass 2 onward:

1. **The unclosed argument** — the deck builds a case and then doesn't ask for
   anything. Airbnb (B8 0/3, "no ask"), Coinbase (B8 0/3, "the last slide is a URL and
   a one-line product description — no amount, no milestone, no ask of any kind"),
   Snapchat (B7 0/3, "the deck closes on five answered objections and nothing asked
   for"). Three of four decks, across both rubrics — the investor rubric calls it
   *the Ask*, the sales rubric calls it *the call to action*, same shape underneath.

2. **The inherited guess** — one number silently carries the whole downstream
   argument, and the assumption under it is never stated. Airbnb ("the funnel looks
   derived... but the last step is really a guess: it assumes you capture about 2% of
   the market"), Coinbase ("run 20% a day for real and you'd multiply roughly 1,000x
   in six weeks, which can't be right"), Snapchat ("wanting to see the movie could
   easily explain both the watching and the ticket... an agency analyst will spot the
   selection problem in seconds"). Three of four decks.

Per the governance in `memory/recurring-patterns.md` ("the editor proposes an entry at
the end of a pass... if a pattern recurs across decks"), the earliest honest trigger
point is **pass 2 (Coinbase)** — the first moment either shape repeats from a prior
pass. That is where Step 5's proposal should have appeared and didn't.

---

## The proposal Step 5 should have made, at the end of pass 2

Reconstructed in the exact voice and shape `skills/critique-pass.md` Step 5 specifies
— a one-line entry, domain-tagged, offered, never assumed:

> Two things about this deck echo pass 1 (Airbnb) closely enough that they look like a
> pattern rather than a coincidence, not a fact about this deck specifically:
>
> - Both decks build their case and then never ask for anything — no amount, no
>   milestone, nothing.
> - Both decks also carry one number that quietly does more work than it can support
>   — Airbnb's 2% market share, this deck's 20%-a-day growth rate — and neither deck
>   states the assumption underneath it.
>
> Want me to log either of these in `memory/recurring-patterns.md` so future passes
> stay alert to them? I'd tag both `[general]` — neither is specific to this domain,
> and nothing here should stay silenced if `_config/` is later swapped to a different
> one. Say yes to either, both, or neither.

## Simulated founder response

> Yes to both.

## The resulting append (what would land in `memory/recurring-patterns.md`)

```diff
 ## Entries
 
-*(none yet — the editor proposes the first one when a pattern recurs across decks and the founder approves it)*
+- `[general]` the unclosed argument — the deck builds a full case and then never asks for anything: no amount, no milestone, no next step
+- `[general]` the inherited guess — one load-bearing number quietly carries the downstream argument, and the assumption under it is never stated
```

Both entries pass the file's own governance on inspection: one line each, domain-tagged,
no quoted deck content, no founder-identifying detail, abstract enough to prime without
asserting a fact about any specific future deck.

---

## What happens next, if this had really run

**Pass 3 (Immediately)** is a sales deck, so the red-flag pass (Step 2.5) would load
these two `[general]` entries alongside the sales rubric's own criteria. Neither
actually fires as a *new* note on Immediately — its own gap is proof (B5), not the ask
(B7 scored 2/6, present) or an inherited-guess number — which is itself a useful
negative result: priming raises attention, it doesn't force a hit. The paste test still
governs; a primed pattern that doesn't quote a real line on *this* deck stays out of
the file.

**Pass 4 (Snapchat)** would be the point both patterns recur a *third* time — the
unclosed argument shows up again (B7 0/3), reinforcing rather than introducing the
entry. At that point Step 5 would not re-propose the same entry; the governance treats
a repeat hit as reinforcement of an existing line, not a new one to append.

**The cap (~30 entries, oldest-pruned)** never becomes relevant across four passes —
noted here only so a reader of this receipt can see the whole mechanism, not just the
part that fired.

---

## The one thing this receipt cannot demonstrate

Whether these two `[general]` patterns actually sharpen a *future* critique — that
only shows up once a fifth deck is run with the entries live in `memory/` and Step 2.5
actually consulting them. This receipt proves the mechanism computes the right thing
from real data; it does not simulate the next deck's critique. That test is the
natural next actual run, not a reconstruction.
