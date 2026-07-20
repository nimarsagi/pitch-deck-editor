---
file-type: reference
workspace: pitch-deck-editor
last-updated: 2026-07-20
status: active
note: Imported near-verbatim from validated research (input/research/pitch-craft.md). Engine-side and domain-neutral — carries no domain content and no refusal. Its §0 is the room lens that reference/room-lenses.md summarizes; keep this file whole.
---

# pitch-craft.md — What Makes a Pitch Deck Good

**Purpose:** Reference knowledge for an agentic workflow that *evaluates and critiques* pitch decks. The AI gives feedback; it does not create. This file defines what good looks like, what bad looks like, and how confident to be about each claim.

**Epistemics rule (read first):** Claims in this file carry evidence tiers. When critiquing, weight feedback by tier. If two heuristics conflict, the higher tier wins. Never present a Tier C heuristic with the confidence of a Tier A finding.

- **Tier A — Measured:** Primary quantitative research (DocSend/Harvard 2015 study of 200 startups; DocSend annual reports; Challenger Sale study of ~6,000 reps; DocSend's own sales-deck rebuild).
- **Tier B — Expert consensus:** Convergent guidance from primary practitioners (Sequoia template, YC guidance, Guy Kawasaki, Andy Raskin, First Round). Multiple independent authorities agree.
- **Tier C — Practitioner folklore:** Widely repeated, plausible, but unverified or vendor-sourced. Use as soft suggestions only, never as violations.

**Caveat that applies to everything:** the flagship dataset (DocSend/Harvard 2015) is n=200, seed-stage, and a decade old. Famous decks (Airbnb, Uber) are survivorship-biased — Uber raised despite a famously bad traction slide. Critique the *discipline* behind good decks, not resemblance to famous ones.

---

## 0. First Question: Which Deck Is This?

Before any critique, classify the deck. **Applying investor-deck criteria to a sales deck (or vice versa) invalidates the entire critique.** This is the single most consequential classification step.

| Signal | Investor deck | Sales deck |
|---|---|---|
| Hero of the story | The market opportunity + team | The prospect/customer |
| What's being sold | Future upside, vision, scale | Relief from a specific pain; a better daily reality |
| Product placement | Early, brief (proof of execution) | Late, after pain is established |
| Telltale slides | TAM/SAM/SOM, team, financials, ask | Cost of inaction, case studies, ROI, CTA/next step |
| Ending | The ask (amount + milestones) | A single concrete next step (pilot, trial) |

If the deck mixes both (e.g., a sales deck with a team-bio slide and TAM diagram, or an investor deck that reads like a feature tour), flag this as a **structural identity error** before critiquing individual slides.

---

## 1. Investor Decks

### 1.1 The evidence base (Tier A — anchor all critique here)

From the DocSend/Harvard 2015 study (200 startups, $360M raised, Prof. Tom Eisenmann) and DocSend's subsequent annual reports:

- **Average investor read time: 224 seconds.** Durable across years (dipped below 2 min for seed decks in 2023). **Implication for critique: the deck must survive a fast, skimming read. Every slide must land its point in seconds. Any slide that requires study fails the primary use condition.**
- **Successful seed decks averaged 19.2 slides; ≤20 is the evidence-backed guardrail.** Engagement drops beyond ~20. Flag decks >20 slides as a Tier A violation; suggest moving detail to an appendix.
- **Dwell time per section (longest → shortest):** Financials 23.2s, Team 22.8s, Competition 16.6s, Why Now 16.3s, Purpose 15.3s, Business Model 14.9s, Product 13.9s, Market 13.3s, Problem 11.3s, Solution 10.6s.
  - **Implication 1:** Investors scrutinize **financials and team** hardest. Weak versions of these slides do disproportionate damage. A generic team slide (names + titles, no "why us for this problem") is a high-severity finding.
  - **Implication 2:** Problem/solution slides get the *fastest* scan. They must work as headlines — a problem slide that needs a paragraph to parse is broken even if the content is good.
- **Financials: ~57–58% of successful decks included them; 0% of failed decks did.** Absence of financials is a statistically loaded omission at seed. Flag missing financials as high-severity (with the caveat: correlation, small n).
- **Team slide appeared in 100% of successful decks.** A missing team slide is a hard flag. Positionally, team appeared at the very start or very end — never the middle.
- **~30% of decks that lead to meetings are first shared internally without the founder present.** **Implication: every slide must be standalone-comprehensible. Any slide whose meaning depends on a verbal narration fails.** This is one of the strongest critique lenses available: read each slide cold and ask "does this make sense with nobody talking?"
- **More investor meetings did not correlate with more money raised** — fit beats volume. (Context for founders, not a slide-level check.)

### 1.2 Structure (Tier B — convergent Sequoia / YC / Kawasaki template)

The canonical sequence. Deviations are not automatically errors, but each section should exist somewhere or its absence should be explainable:

1. Purpose — what you do in one declarative sentence
2. Problem — the pain, how it's solved today, why that's inadequate
3. Solution — value proposition, use cases
4. Why Now — the shift (tech/regulatory/behavioral) that makes this possible today
5. Market — TAM top-down, SAM/SOM bottom-up, beachhead
6. Competition — who, and your durable advantage
7. Product — form factor, brief
8. Business model — how you make money, unit economics
9. Team — why *this* team is uniquely suited
10. Financials — projections
11. Ask — amount + what milestones it buys

**Critique heuristics derived from Tier A + B:**

- **"What do you do by slide 3."** If a cold reader can't state the company's business by slide 3, flag at highest severity. (Tier B, universally repeated by VCs; consistent with the 224-second skim behavior.)
- **The deck is an argument, not a brochure.** Each slide should make one claim that the next slide's claim builds on. Check the headline chain: reading only the slide titles in order should produce a coherent case. (Tier B, Sequoia framing + assertion-evidence research.)
- **Stage-aware weighting:** "Why Now" matters most at pre-seed/seed; by Series A the deck should be traction/unit-economics-heavy. Critique against the stage, not a universal ideal. (Tier B.)

### 1.3 Red flags (evidence-weighted)

High severity (Tier A-adjacent):
- Missing team slide, or team slide placed mid-deck
- Missing financials at seed+
- >20 slides without an appendix split
- Slides that don't work standalone (narration-dependent)
- Unclear what the company does by slide 3

Medium severity (Tier B):
- "We have no competition" — signals naïveté; everything competes with the status quo
- Vague ask (no number, no milestones) — best practice: state amount + runway + milestones; leave *terms* out of the deck
- Giant top-down TAM with no bottom-up beachhead path
- Team slide as credential list without problem-specific relevance
- Speculative exit scenarios / "potential outcomes" slides (the documented Uber-deck mistake)
- Out-of-date numbers anywhere

Low severity (Tier C — mention softly):
- Buzzwords ("democratize", "revolutionize")
- Mockups where real screenshots exist
- Design-polish critiques beyond legibility

### 1.4 Design rules (Tier B, with one research anchor)

- **Assertion-evidence headlines:** slide title = a full-sentence claim ("Revenue grew 3× in 6 months"), body = one visual supporting it. This structure is research-backed (Michael Alley) as more comprehensible and memorable than topic-label + bullets. **A deck whose titles are topic labels ("Traction", "Market") is leaving its strongest lever unused — flag it.**
- One idea per slide (YC: "Legible, Simple, Obvious")
- ≥30pt fonts (Kawasaki — a forcing function against cramming, not a law)
- ≤ ~25 words per slide as a soft ceiling
- Detail belongs in an appendix, not the main flow

---

## 2. Sales Decks

### 2.1 The evidence base (Tier A — anchor all critique here)

- **DocSend's own rebuild (best quantified sales-deck datapoint):** their old feature-heavy deck had **17.5%** of viewers reach the last slide (<40% reached halfway). Rebuilt around a storytelling arc — and *two slides longer* — completion rose to **65.4%**. **Implication: narrative order beats length. If engagement data shows early drop-off, the fix is reordering (front-load the strongest, most customer-relevant content), not cutting slides.** Caveat: self-reported vendor before/after, not a controlled A/B — treat magnitude as illustrative, direction as reliable.
- **Challenger Sale (CEB/Gartner, ~6,000 reps, 90 companies):** in *complex* B2B sales, Challengers were **54% of high performers; Relationship Builders just 7%**. The winning behavior is *teaching a commercial insight that reframes the buyer's view*, not rapport. **Implication: a sales deck that contains no insight — nothing the buyer doesn't already know — is missing its engine. Ask of every deck: "what does this teach?"** Caveat: measured in complex sales; in simple transactional sales the profiles performed similarly, so don't demand Challenger machinery from a small-ticket deck.
- **Buyer self-education (Gartner):** buyers spend only ~17% of their purchase journey meeting suppliers; most research happens rep-free. **Implication: like investor decks, sales decks are read unaccompanied. Standalone comprehensibility is a Tier A lens here too.**
- **Concision (Tier A-/B, vendor data):** Storydoc's analysis of 100k+ presentations found ~10–11 slide decks average 22% more engagement; personalized decks showed +41% reading time and 2.3× more internal sharing. Vendor-sourced — treat as directional support for concision and personalization, not exact thresholds.

### 2.2 Structure (Tier B — Raskin / Challenger / PAS, which share one DNA)

All three dominant frameworks converge on the same arc: **customer's world → change/pain → stakes → better future → product as bridge → proof → next step.**

Raskin's 5 elements (the Zuora narrative):
1. Name a big, undeniable **shift in the world** (not your product, not "a problem")
2. Show **winners and losers** of that shift (engages loss aversion)
3. Tease the **Promised Land** — the desirable future state, defined as *life with the outcome*, not "having your technology"
4. Introduce product capabilities as **"magic gifts"** for overcoming obstacles to the Promised Land
5. **Evidence** you can make the story come true (named customers, measured outcomes)

Challenger's teaching choreography (maps onto slides): Warmer → Reframe → Rational Drowning (quantify consequences) → Emotional Impact → A New Way (solution category before your product) → Your Solution.

PAS (for shorter/simpler decks): Problem → Agitate (make inaction feel expensive) → Solve.

**Critique heuristics derived from Tier A + B:**

- **Where does the product first appear?** If it's on slide 1–2 (logo, feature list, "about us"), the deck has the exact shape DocSend measured at 17.5% completion. Highest-severity structural finding for a sales deck.
- **Is there a cost-of-inaction moment?** The agitation step is the one amateurs skip. A deck that names a pain but never quantifies the cost of leaving it unsolved has no urgency engine.
- **Is the shift bigger than the vendor?** Raskin's documented failure mode: framing the shift as "you used to use our competitor, now use us" — too small. Test: could a journalist tell this shift story without mentioning the product? If not, it's not a strategic narrative.
- **Whose language is the pain in?** The strongest openings use the prospect's own words (discovery calls, tickets). Generic pain statements ("companies struggle with inefficiency") are a flag.
- **Proof specificity:** "Cut Acme's onboarding from 6 weeks to 4 days" beats "trusted by 500+ companies." A logo wall with no named outcome is weak evidence. Also check segment match — a startup-logo case study shown to an enterprise buyer is a mismatch flag.
- **The last slide:** must be one concrete, low-friction next step. "Questions?" or a bare pricing table = missing CTA, high severity.
- **Tailoring by stakeholder (Challenger, Tier A-backed):** in committee sales, the same insight must be framed per role (CFO: margin; ops: throughput). A single undifferentiated deck for a buying committee is a soft flag on complex deals.

### 2.3 Red flags (evidence-weighted)

High severity:
- Product/company/feature-first opening (the measured 17.5%-completion shape)
- No cost-of-inaction / agitation anywhere
- No proof with named customer + measured outcome + timeframe
- No CTA, or CTA is "any questions?"
- Deck not comprehensible standalone

Medium severity:
- Shift framed too small (vendor-vs-competitor, not world-level)
- Generic pain language not traceable to the prospect's world
- Case-study segment mismatch
- Feature list presented as features rather than obstacles-overcome
- One-size-fits-all deck for a multi-stakeholder committee

Low severity (Tier C):
- Deck length beyond ~11 slides (directional vendor data only — remember DocSend's *winning* deck was longer than its loser)
- Visual polish critiques beyond clarity

### 2.4 Deal-size calibration (Tier A-derived boundary condition)

- **Complex/enterprise deals (> ~$50K ARR):** full narrative arc applies; modular slides (security, implementation, mutual action plan) are expected, not bloat.
- **Transactional deals (< ~$15–25K):** the Challenger evidence does *not* extend here. Demanding a 5-part strategic narrative from a simple deck is over-critique. A tight PAS or Before-After-Bridge is the right standard.

---

## 3. Universal Principles (apply to both deck types)

Ranked by evidence strength:

1. **The deck is read fast and alone.** (Tier A: 224 seconds; ~30% shared internally; 83% of buyer journey rep-free.) — Every slide standalone, every point landable in seconds. This is the master lens; most other rules derive from it.
2. **Narrative order is the highest-leverage variable.** (Tier A: 17.5%→65.4% from reordering alone.) — Critique sequence before critiquing content, and content before critiquing design.
3. **Headlines carry the deck.** (Tier B + assertion-evidence research.) — Title-chain test: read only the slide titles; they should form the complete argument.
4. **One idea per slide.** (Tier B, universal.) — Any slide serving two ideas should be split or cut.
5. **Specificity beats claims.** (Tier B.) — Numbers with timeframes and names > adjectives. "Reduces onboarding time" is a claim; "6 weeks to 4 days at Acme" is evidence.
6. **The heaviest-scrutinized slides deserve the most effort.** (Tier A: financials/team for investors; Tier B: first three slides for sales — practitioners put ~70% of prep there.) — Weight critique severity by where the audience's attention measurably goes.

---

## 4. Critique Protocol (how an evaluating agent should use this file)

1. **Classify** the deck (§0). If misclassified or hybrid, report that first — it supersedes slide-level feedback.
2. **Run the master lens:** cold-read each slide standalone; note every slide that fails without narration.
3. **Check sequence** against the relevant framework (§1.2 or §2.2) before touching content. Order errors outrank content errors (Tier A basis).
4. **Run the title-chain test.** Report whether headlines alone tell the story.
5. **Apply red-flag lists** (§1.3 / §2.3), reporting severity and evidence tier for each finding. Format findings as: *what's wrong → why it matters (with tier) → concrete fix.*
6. **Calibrate to context:** stage (investor) or deal size (sales). Do not apply seed-deck rules to a Series B deck or Challenger machinery to a $5K sale.
7. **Confidence discipline:** Tier A findings may be stated firmly ("this measurably hurts"). Tier B as strong recommendations. Tier C as optional polish, clearly hedged. Never inflate a Tier C heuristic into a rule.
8. **Do not rewrite.** This workflow augments; it critiques and explains. Fixes are described ("reframe this title as the takeaway claim it supports"), not authored, unless the human explicitly asks.

---

## Appendix: Source Map

- DocSend/Harvard 2015 (Eisenmann): read times, dwell per section, slide counts, financials/team presence — the Tier A backbone for investor decks
- DocSend annual reports: durability + drift of the above (e.g., <2min seed reads in 2023)
- DocSend "DocSend for Sellers" rebuild: 17.5%→65.4% completion — Tier A backbone for sales-deck ordering
- Dixon & Adamson, *The Challenger Sale* (CEB/Gartner, ~6,000 reps): teaching-insight evidence, complex-vs-transactional boundary
- Gartner buyer research: rep-free buying journey (~17% supplier time)
- Sequoia template, YC seed guidance, Kawasaki 10/20/30: Tier B structural consensus
- Andy Raskin, "The Greatest Sales Deck I've Ever Seen" (Zuora): Tier B sales-narrative framework
- Michael Alley, assertion-evidence research: headline convention
- Storydoc 100k-presentation analysis: Tier C/B- concision and personalization data (vendor-sourced)
