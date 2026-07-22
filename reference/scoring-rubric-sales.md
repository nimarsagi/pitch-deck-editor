---
file-type: reference
workspace: pitch-deck-editor
last-updated: 2026-07-21
status: active
note: Sales-deck sibling to scoring-rubric.md. Criteria drawn from pitch-craft.md §2. Shares that file's machinery — levels, conversion, the two lenses, artifact deductions, reporting format, and the §7 clarification shape — and does not restate them. Classify the deck (pitch-craft.md §0) before choosing which rubric to use.
---

# scoring-rubric-sales.md — Weighted 1–10 Sales Deck Score

**Purpose:** The sales-deck criteria set. `scoring-rubric.md` scores investor decks; this scores sales and adoption decks. Everything structural is shared with that file — read it first.

**Scope check before you score.** Applying investor criteria to a sales deck, or the reverse, invalidates the whole critique (`pitch-craft.md` §0). Telltales for *this* rubric: the hero of the story is the prospect, not the market; the product appears late, after pain is established; the deck ends in a next step, not an ask. If the deck mixes both — a sales deck carrying a TAM diagram and team bios — report that **structural identity error first**; it supersedes any score.

**Inherited from `scoring-rubric.md`, unchanged:**
- The 0–3 levels (Unacceptable / Acceptable / Target / Exemplary)
- The tier weights: **A ×3, B ×2, C ×1**
- The anchored conversion, including straight-Target = **8.0**
- The two lenses (§4), artifact defect deductions, and send-readiness bands
- The reporting format (§6) and the clarification shape (§7)

Total is 105 raw points again — Tier A 45, Tier B 54, Tier C 6 — so the anchors carry over exactly:

```
if p ≤ 0.667:   Score = 1.0 + 10.5 × p
if p >  0.667:  Score = 8.0 +  6.0 × (p − 0.667)      where p = earned ÷ possible
```

Below the Target anchor, 1 raw point = **+0.10**. Tier A improvement = **+0.30**, Tier B = **+0.20**, Tier C = **+0.10**.

**Notation:** write levels and points as fractions of maximum — `2/3 → 6/9 pts`. Never `2 → 6`.

---

## 1. Score sheet

| # | Criterion | Tier | Wt | Level (of 3) | Points (of max) |
|---|---|---|---|---|---|
| A1 | Narrative order & product placement | A | ×3 | | |
| A2 | Standalone comprehension | A | ×3 | | |
| A3 | Commercial insight — the teach | A | ×3 | | |
| A4 | Cost of inaction | A | ×3 | | |
| A5 | Stakeholder tailoring | A | ×3 | | |
| B1 | The shift is bigger than the vendor | B | ×2 | | |
| B2 | Winners and losers | B | ×2 | | |
| B3 | Promised Land | B | ×2 | | |
| B4 | The pain in the prospect's language | B | ×2 | | |
| B5 | Proof specificity | B | ×2 | | |
| B6 | Capabilities as obstacles overcome | B | ×2 | | |
| B7 | The call to action | B | ×2 | | |
| B8 | Headline craft | B | ×2 | | |
| B9 | One idea per slide & specificity | B | ×2 | | |
| C1 | Visual craft & legibility | C | ×1 | | |
| C2 | Length discipline | C | ×1 | | |
| | | | **Total** | | **/105** |

### The high-severity gate

`pitch-craft.md` §2.3 lists five failures that are disqualifying regardless of how the rest scores. **If any of these sits at level 0, cap the final score at 6.9** — the deck cannot reach "Strong" while one of them is open:

- **A1** product-first opening · **A2** not comprehensible standalone · **A3** no insight (unless N/A) · **A4** no cost of inaction · **B5** no real proof · **B7** no call to action

Report the cap explicitly and name which gate triggered it. The gate exists because weighting alone under-punishes a single fatal omission: a deck can score respectably on fifteen criteria and still be unsendable because it never asks for anything.

---

## 2. Level descriptors

### Tier A — measured (×3)

**A1 · Narrative order & product placement** — *DocSend's feature-first deck: 17.5% of viewers reached the last slide. Rebuilt around a narrative arc — and two slides longer — 65.4%.*
- **0** — Opens with the company, logo, "about us", or a feature list; the product lands on slide 1–2. This is the exact shape measured at 17.5% completion.
- **1** — Some framing precedes the product, but it arrives before pain is established, or the order oscillates between the buyer's world and the vendor pitch.
- **2** — Pain is established before the product appears; the deck runs customer's world → change → stakes → better future → product → proof → next step.
- **3** — The order builds momentum: each slide makes the next feel necessary, and the product arrives as the obvious resolution of a tension already created.

**A2 · Standalone comprehension** — *buyers spend only ~17% of the purchase journey with suppliers (Gartner); most reading happens rep-free*
- **0** — Several slides are meaningless without a rep talking over them.
- **1** — Broadly followable, but the key slides need narration to land.
- **2** — Every slide states its own point; a forwarded copy survives intact.
- **3** — Reads as a self-contained argument your champion could present internally on your behalf, uncoached.

**A3 · Commercial insight — the teach** — *Challenger reps were 54% of high performers in complex B2B; relationship builders 7% (CEB/Gartner, ~6,000 reps)*
- **0** — Contains nothing the buyer doesn't already know; describes the vendor, not the buyer's world.
- **1** — Offers market context, but nothing that changes how the buyer sees their own situation.
- **2** — Teaches at least one thing that genuinely reframes the buyer's understanding of their problem.
- **3** — The reframe is the spine of the deck, specific to this buyer's world, and leads naturally to a capability only you have.

**A4 · Cost of inaction** — *Challenger's "rational drowning"; the step amateurs skip*
- **0** — Pain is named but never costed; nothing makes staying put feel expensive.
- **1** — Consequences gestured at qualitatively — "wasted time", "frustration", "missed opportunities".
- **2** — The cost of doing nothing is quantified — hours, dollars, churn, risk — with a stated basis.
- **3** — Quantified in the buyer's own numbers, and shown to compound over time.

**A5 · Stakeholder tailoring** — *Challenger, committee sales. N/A for single-buyer or transactional deals — see §4*
- **0** — One undifferentiated deck aimed at a multi-stakeholder committee; no role is ever addressed.
- **1** — Generic nods to different roles without reframing the insight for any of them.
- **2** — The core insight is framed per role: margin for finance, throughput for ops, risk for security.
- **3** — Per-role framing plus material a champion can lift and forward to each stakeholder separately.

### Tier B — expert consensus (×2)

**B1 · The shift is bigger than the vendor** — *Raskin's documented failure mode is framing the shift as "you used our competitor, now use us"*
- **0** — No shift named, or the shift is really "switch from them to us".
- **1** — A shift is named, but it's a product-category trend rather than a change in the world.
- **2** — A genuine world-level change — technological, regulatory, behavioural — that a journalist could report without mentioning you.
- **3** — That, evidenced, and plainly explaining why the buyer's current approach now sits on the wrong side of it.

**B2 · Winners and losers** — *loss aversion*
- **0** — The shift, where present, carries no stakes; nobody visibly loses.
- **1** — Upside described; the cost of missing the shift left implicit.
- **2** — Both sides shown — who is winning from this change and who is being left behind.
- **3** — Named, recognisable examples on both sides, positioned so the buyer can see which side they are currently on.

**B3 · Promised Land** — *the desirable future defined as life with the outcome, not as having your technology*
- **0** — The future state is "using our product", or a feature set.
- **1** — An outcome is stated, but in vendor terms — "fully integrated", "AI-powered", "seamless".
- **2** — A desirable future described as the buyer's daily reality, independent of your product.
- **3** — Specific and vivid enough that the buyer wants it before knowing what you sell — and visibly hard to reach unaided.

**B4 · The pain in the prospect's language**
- **0** — Generic pain statements: "companies struggle with inefficiency".
- **1** — Plausible pain, but written in vendor or analyst language.
- **2** — Pain traceable to this buyer's world — their workflow, their constraints, their terms.
- **3** — Their actual words, from discovery calls or support tickets, quoted back to them.

**B5 · Proof specificity**
- **0** — No proof, or a logo wall with no named outcome attached.
- **1** — Testimonials or case studies without measured outcomes, or drawn from a mismatched segment.
- **2** — Named customer, measured outcome, timeframe: "cut Acme's onboarding from six weeks to four days".
- **3** — That, from a segment matching this buyer, with the mechanism explained so the result reads as transferable rather than anecdotal.

**B6 · Capabilities as obstacles overcome** — *Raskin's "magic gifts"*
- **0** — A feature list or a product tour.
- **1** — Features with benefit statements bolted on.
- **2** — Each capability introduced as the thing that removes a specific obstacle to the Promised Land.
- **3** — Capabilities ordered to mirror the obstacles in sequence, so the product reads as a route rather than a catalogue.

**B7 · The call to action**
- **0** — No next step; "Questions?"; or a bare pricing table as the closing slide.
- **1** — A vague invitation: "get in touch", "let's talk".
- **2** — One concrete, low-friction next step, clearly scoped and owned — a pilot, a scoped trial, a named workshop.
- **3** — That, plus what follows it and what success in that step looks like: a mutual action plan rather than an ask.

**B8 · Headline craft** — *assertion-evidence*
- **0** — No headlines, or headlines that mislabel their slide.
- **1** — Topic labels: "Our Solution", "Case Study", "Pricing".
- **2** — Most headlines state the claim the slide then evidences.
- **3** — Every headline is the takeaway; read alone, they deliver the whole argument.

**B9 · One idea per slide & specificity**
- **0** — Slides carry several competing ideas; adjectives stand in for evidence.
- **1** — Mostly single-purpose, but with crowding and some unearned claims.
- **2** — One idea per slide; claims carry numbers, names, and timeframes.
- **3** — Ruthless: every slide has exactly one job, every claim is falsifiable.

### Tier C — folklore (×1)

**C1 · Visual craft & legibility**
- **0** — Illegible type, broken layout, low-resolution assets.
- **1** — Readable but inconsistent or dated.
- **2** — Clean, consistent, legible at a glance.
- **3** — Design carries argumentative weight; the eye is led to the point.

**C2 · Length discipline** — *deliberately Tier C here, unlike the investor rubric*
- **0** — So long the arc is lost, or padded with material belonging in a leave-behind.
- **1** — Noticeably longer than the argument needs.
- **2** — Every slide earns its place; modular sections kept separate from the main arc.
- **3** — Tight, with optional modules cleanly appended for the stakeholders who need them.

> **Never cut a sales deck for length alone.** The strongest measured result in this whole file came from a rebuild that was **two slides longer** than the deck it replaced. If engagement drops early, the fix is reordering (A1), not deleting. Length is Tier C here precisely because the evidence points the other way — vendor data only, and contradicted by the one controlled-ish before/after available.

---

## 3. Score bands

Same bands as `scoring-rubric.md` §3, and the same warning: these describe the **as designed** score only. Artifact scores use the send-readiness bands in that file's §4.

| Score | Band | Reading |
|---|---|---|
| **9.0–10** | Exceptional | Rare. Teaches, reframes, and closes; several sections create advantage |
| **8.0–8.9** | Strong | Complete arc, real proof, clear next step. Send it |
| **6.5–7.9** | Good, with named gaps | The arc works; two or three sections underpowered. **Most real decks live here** |
| **5.0–6.4** | Solid core, material gaps | Recognisable structure, but key moves missing outright |
| **3.5–4.9** | Structurally incomplete | Likely feature-first or insight-free; needs rebuilding, not editing |
| **1.0–3.4** | Not ready | Missing the basics of the form |

**Calibration is not yet benchmarked.** The investor rubric carries one anchored reference deck (Airbnb 7.1, reproducible via `tools/score.py`). This one has none — no sales deck has been scored with it. Treat absolute numbers as provisional until two or three real decks are run through and the anchors are checked. Relative ranking and the fix-priority list are trustworthy from the first use; the specific number is not, yet.

---

## 4. Deal-size calibration (the N/A valve)

The sales analogue of stage calibration. **The Challenger evidence was measured in *complex* sales and does not extend to transactional ones** — demanding a five-part strategic narrative from a small-ticket deck is over-critique, not rigour.

**Complex / enterprise (> ~$50K ARR)** — everything applies. Modular slides for security, implementation, and mutual action planning are *expected*, not bloat; do not penalise them under C2.

**Transactional (< ~$15–25K)** — the right standard is a tight PAS (Problem → Agitate → Solve) or Before-After-Bridge. Legitimately N/A:
- **A5** Stakeholder tailoring — usually a single buyer
- **A3** Commercial insight — the Challenger finding doesn't reach here; in simple sales the profiles performed similarly
- **B1, B2, B3** — the Raskin strategic-narrative machinery is disproportionate at this deal size

**Mid-market** — judge by whether a buying committee exists, not by the dollar figure alone.

**Never N/A at any deal size:** A1 (order), A2 (standalone), A4 (cost of inaction), B4 (their language), B5 (proof), B7 (the CTA). These hold from a $2K self-serve deck to a $2M enterprise one.

Record every N/A with a one-line reason. An unexplained N/A is score inflation.

---

## 5. Reporting

Follow `scoring-rubric.md` §6 and §7 exactly — same order, same six-move shape when the founder asks why a row scored what it did, same rule about offering clarification rather than pre-explaining every criterion.

Two additions specific to this rubric:

1. **State the deal-size band and where the committee sits** in the header, alongside the room. The score is meaningless without it, and it determines which criteria were N/A'd.
2. **If the high-severity gate fired, say so before the number** — "capped at 6.9: no call to action" — so the cap reads as a diagnosis rather than an arbitrary ceiling.

Do not rewrite the deck. Describe fixes; do not author them, unless explicitly asked.
