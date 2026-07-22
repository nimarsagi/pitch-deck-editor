---
file-type: examples
workspace: pitch-deck-editor
last-updated: 2026-07-22
status: active
referenced-by: [critique-pass]
---

# Critique Pass — Worked Examples

**What these teach, and what they don't.** These examples teach the **shape** of a good critique — the quote gate, the paste test, the why-clause, the handed-back question, and the rewriting trap. That shape is the engine and is domain-neutral. The examples happen to be **flagship-flavored** (an ICM / AI-startup deck), because that's the domain this deployment ships with and the domain edge is best shown, not described. If you re-domain the editor (swap `_config/`), the *shape* below still holds exactly — re-flavoring these examples for your domain is optional polish, not required. (Recorded exception to the swap-one-folder rule; see the README.)

One sample deck, critiqued two ways: once badly (the failure modes), once well (the gates holding). Then the rewriting trap in isolation, because it's the hardest line.

---

## The sample deck (excerpt)

A **sales/adoption** deck — Acme AI, pitching an AI reconciliation tool to finance teams. Declared room: sales/adoption. Domain context loaded: ICM / AI startups.

> **Slide 1 — Title:** "Acme AI — Fully autonomous finance operations. No humans required."
> **Slide 2 — Problem:** "Finance teams waste 20+ hours a week on manual reconciliation."
> **Slide 3 — Solution:** "Our AI does your reconciliation end-to-end. It just works."
> **Slide 4 — How it works:** "Advanced ML models process your data and deliver results."
> **Slide 5 — Close:** "Trusted by leading companies. Questions?"

---

## Example 1 — The critique it should NOT produce

```
Great start — this is a really compelling deck with a strong value prop!

- Slide 1: Love the bold positioning. Consider making the headline even punchier.
- Slide 2: Good problem statement. You could strengthen it with more detail.
- Slide 3: This is solid. To make it pop, try: "Acme AI eliminates reconciliation
  forever — reclaim your 20 hours." That'll really land.
- Slide 5: Nice close. Maybe add a clear call to action to seal the deal.

Overall this is 80% of the way there — a few tweaks and you're golden!
```

### Why it fails — annotated against the gates (`rules.md`)

- **Flattery, not critique.** "Great start," "really compelling," "you're golden" — praise tied to no specific line doing specific work. Fails the honesty gate's rigor requirement and tells the founder nothing.
- **Genericness — dies at the paste test.** "Consider making the headline punchier," "strengthen it with more detail," "add a clear call to action" would land unchanged on *any* deck. Every one fails gate 2. None quotes an exact line (fails gate 1).
- **Rewriting — the cardinal sin.** *"try: 'Acme AI eliminates reconciliation forever — reclaim your 20 hours.'"* This is paste-ready copy. It fails gate 4 outright, and it's doubly wrong here: it *strengthens an oversell* the domain refusal says to refuse (see `_config/`). The founder learns nothing and the deck becomes the model's words.
- **Missed the actual deck.** The whole thing is riddled with the domain's trust-breakers — "No humans required," "It just works," "Advanced ML models" — and the generic praise walks right past them. A critique that flatters an oversold AI deck has failed twice.

---

## Example 2 — The critique it SHOULD produce

```markdown
# Critique — acme-ai, Pass 1 (sales/adoption)

## Spine check
The deck breaks on slide 1. It opens with "Fully autonomous finance operations.
No humans required." — then never shows how a finance team stays in control of its
own books. A finance buyer's biggest fear is unattended AI on the money, and the very
first slide confirms that fear instead of answering it. Nothing later earns the trust
back. Fix this before any single slide.

## Slide notes

### Slide 1 — Title
"Fully autonomous finance operations. No humans required." To a finance buyer this reads
as a threat, not a selling point — they fear exactly this, and slide 1 confirms the fear
instead of easing it. The human check is your strongest trust signal, and the headline
throws it away. What would the headline say if the person staying in control were the promise?

### Slide 3 — Solution
"Our AI does your reconciliation end-to-end. It just works." A finance team can't adopt
what it can't check, and "it just works" is the line a burned buyer has heard before and
stopped believing — it gives a skeptic nothing to verify. When the AI is unsure or wrong,
what happens, and who catches it?

### Slide 5 — Close
"Trusted by leading companies. Questions?" Two problems. "Leading companies" with no name,
number, or timeframe is a claim nobody can check. And ending on "Questions?" asks the reader
for nothing — a sales deck should close on one small, easy next step. Which named customer,
what result, over what timeframe — and what's the one low-effort next step you want them to take?

## What's working
Slide 2 — "Finance teams waste 20+ hours a week on manual reconciliation." A concrete,
quantified pain in the buyer's own words. This is the deck's firmest ground; don't dilute
it — the rest should earn the right to solve this.

## Score
A 3 out of 10. The pain on slide 2 is real and specific, but the deck leads with the buyer's
fear instead of answering it, and gives them nothing to check.

**Worth fixing first:**
1. The control story — show where a human stays in charge, so slide 1 stops confirming the fear.
2. Real proof — one named customer, a measured result, a timeframe, in place of "leading companies."
3. A real next step — end on one small ask, not "Questions?"

[In a real critique file the full scorecard sits at the very bottom; omitted from this excerpt.]
```

### How each note passes the gates

- **Every note quotes an exact line** (gate 1) and would be **nonsense on another deck** (gate 2) — "no humans required" and "it just works" are *these* words.
- **The why is tied to the sales/adoption room** (gate 3) and to the loaded domain — the finance buyer's specific distrust — even though there's no "why it loses the room" label; it's woven into the sentence.
- **Every note ends in a question, authors no copy** (gate 4). Note the difference from Example 1: here the title note *points at* the missing control story and asks how the headline would read if control were the promise — it does **not** write the new headline.
- **Plain, and said once** — each note is a few plain sentences, no Tier or section labels, no problem/why/ask scaffold, the point made a single time. That's the readable shape, and it's what the founder can act on at a glance.
- **Honesty in both directions** — slide 2 is named as a real strength, quoted, with the same rigor as the faults; the score is low but reasoned, not punitive.
- **Caps hold** — one spine break, ≤2 notes per slide, slide 4 left for a later pass.

---

## The rewriting trap — the one line to hold

The hardest discipline is describing a fix without authoring it. The two look similar and are opposites:

| ✗ Rewriting (fails gate 4) | ✓ Critiquing (passes) |
|---|---|
| "Change the title to 'Finance teams stay in control — AI does the grunt work.'" | "The title promises unattended automation to a reader who fears exactly that. What would it promise if the human's control were the headline?" |
| "Rephrase slide 3 as: 'Every match is flagged for your team to approve.'" | "Slide 3 gives a skeptic nothing to verify. Where in the flow does a human catch what the AI gets wrong — and does the slide show it?" |

The tell: if the founder could **paste your words onto a slide**, you rewrote. Point at what's missing and hand back the question that makes them write it. When the founder fixes it in their own words, the deck stays theirs and they've learned the weakness — which is the only outcome that compounds.
